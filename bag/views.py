from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from products.models import Product, Jumper


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request):
    """ Add a quantity of the specified product to the shopping bag """

    # Get tandem and film packages 
    tandem = get_object_or_404(Product, pk=1)
    film_package = get_object_or_404(Product, pk=product.id)

    # Get jumper details
    name = request.POST.get('jumper_Name')
    dob = request.POST.get('jumper_Date_Of_Birth')

    # Page redirect and get bag
    bag = request.session.get('bag', {})
    redirect_url = request.POST.get('redirect_url')
    
   
    if request.method == 'POST':
        test = len(bag)
        customer =({'id': test, 'name': name,'dob': dob})
        bag[test] = customer

    
    request.session['bag'] = bag
    
    print(bag)

    return redirect(redirect_url)