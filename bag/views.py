from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from products.models import Product
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents
import stripe
import json
import time


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def view_bag(request):
    """ A view that renders the bag contents page """

    """ Stripe payment """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]

            current_bag = bag_contents(request)
            total = current_bag['grand_total']

            order.grand_total = total

            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            return redirect(reverse('skydive-packages'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.default_email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'time': time,
        'client_secret': intent.client_secret,
    }
    return render(request, 'bag.html', context)


def add_to_bag(request):
    """ Add Jumper with details of products and basic information """
    # Get jumper details
    name = request.POST.get('jumper_Name')
    phone = request.POST.get('Phone_Number')
    email = request.POST.get('Email')
    film = request.POST['film_selection']

    # Page redirect and get bag
    bag = request.session.get('bag', {})
    redirect_url = request.POST.get('redirect_url')

    if request.method == 'POST':
        request.session['bag'] = bag
        # Find a new id for each new jumper
        if bag:
            id = max([int(i['id']) for i in bag.values()]) + 1
        else:
            id = 0
        customer = ({
            'id': id, 'name': name, 'phone': phone, 'email': email,
            'tandem': '1', 'film': film})
        bag[id] = customer

        messages.success(request, f'Jump ticket for {name} was added!')

        if request.POST.get('another'):
            return redirect(redirect_url)
        if request.POST.get('checkout'):
            return redirect('view_bag')


def remove_from_bag(request, item_id):
    bag = request.session.get('bag', {})

    del bag[item_id]
    request.session['bag'] = bag

    HttpResponse(status=200)
    return redirect('view_bag')


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_phone_number': order.phone_number,
                'default_email': order.email,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.country,

            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    if 'bag' in request.session:
        del request.session['bag']

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

    context = {
        'order': order,
        'bag_items': bag_items
    }

    return render(request, 'checkout_success.html', context)
