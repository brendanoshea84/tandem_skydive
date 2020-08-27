from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from .models import Order
from products.models import Product
from profiles.models import UserProfile
from bag.contexts import bag_contents
import json
import time
from django.contrib import messages


class StripeWH_Handler:
    """Handle Stripe webhooks"""
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        bag_items = []
        orginal = json.loads(order.original_bag)

        for key, value in orginal.items():
            tandem = int(value.get('tandem'))
            tandem = get_object_or_404(Product, pk=tandem)
            film = int(value.get('film'))
            film = get_object_or_404(Product, pk=film)

            bag_items.append({
                'name': value.get('name'),
                'phone': value.get('phone'),
                'email': value.get('email'),
                'film': film,
                'tandem': tandem,
                })

        cust_email = order.email

        subject = ('Your Jump Tickets from Skydive Göteborg')
        body = render_to_string(
            'email/email_body.txt',
            {'order': order, 'bag': bag_items})

        send_mail(
            subject,
            body,
            'projects4bos@gmail.com',
            [cust_email])

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = billing_details.phone
                profile.default_email = billing_details.email
                profile.default_country = billing_details.address.country
                profile.default_town_or_city = billing_details.address.city
                profile.default_street_address1 = billing_details.address.line1
                profile.default_street_address2 = billing_details.address.line2

                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    country__iexact=billing_details.address.country,
                    postcode__iexact=billing_details.address.postal_code,
                    town_or_city__iexact=billing_details.address.city,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    original_bag=bag,
                    stripe_pid=pid,
                )

                order_line_item = []
                for key, value in json.loads(bag).items():
                    tandem = int(value.get('tandem'))
                    tandem = get_object_or_404(Product, pk=tandem)
                    film = int(value.get('film'))
                    film = get_object_or_404(Product, pk=film)

                    order_line_item.append({
                        'name': value.get('name'),
                        'phone': value.get('phone'),
                        'email': value.get('email'),
                        'film': film,
                        'tandem': tandem,
                    })

                order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        print('email 2')
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
