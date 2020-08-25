from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product

from .models import UserProfile
from .forms import UserProfileForm

from bag.models import Order
import json

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Update failed. Ensure the form is valid')    
    else:            
        form = UserProfileForm(instance=profile)
    

    orders = profile.orders.all()
    template = 'profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    bag_items = []
    orginal = json.loads(order.original_bag)

    for key, value in orginal.items():
        tandem = int(value.get('tandem'))
        tandem = get_object_or_404(Product, pk=tandem)
        film = int(value.get('film'))
        film = get_object_or_404(Product, pk=film)

        bag_items.append({
            'name' : value.get('name'),
            'phone' : value.get('phone'),
            'email' : value.get('email'),
            'film' : film,
            'tandem' : tandem,
            })

    template = 'checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
        'bag_items': bag_items
    }

    return render(request, template, context)    