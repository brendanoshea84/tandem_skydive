from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from products.models import Product, Jumper
from products.forms import JumperProfileForm


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag.html')


def add_to_bag(request):
    """ Add Jumper with details of products and basic information """

    # Get jumper details
    name = request.POST.get('jumper_Name')
    phone= request.POST.get('Phone_Number')
    email= request.POST.get('Email')
    film = request.POST['film_selection']

    # Page redirect and get bag
    bag = request.session.get('bag', {})
    redirect_url = request.POST.get('redirect_url')

    if request.method == 'POST':
        request.session['bag'] = bag
        if bag:
            id = max([int(i['id']) for i in bag.values()]) + 1 
        else :    
            id = 0
        customer =({'id': id, 'name': name, 'phone': phone, 'email': email, 'tandem': '1', 'film': film})
        bag[id] = customer

        if request.POST.get('another'):
            return redirect(redirect_url)
        if request.POST.get('checkout'):
            return redirect('view_bag')     


def remove_from_bag(request, item_id):
    
    bag = request.session.get('bag', {})
    del bag[item_id]    
    request.session['bag'] = bag
    return HttpResponse(status=200)


