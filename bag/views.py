from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from products.models import Product, Jumper
# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request):
    """ Add a quantity of the specified product to the shopping bag """

    redirect_url = request.POST.get('redirect_url')
    name = request.POST.get('jumper_Name')
    dob = request.POST.get('jumper_Date_Of_Birth')

    bag = request.session.get('bag', {})

    print("stage 1")
    testing = []
    
    if request.method == 'POST':
        testing.append({
            "name": name,
            "dob": dob  
        })   
        bag[testing]
        return(testing)

    request.session['bag'] = bag
    print("*******") 
    print(testing) 
    print("*******") 
    print(bag)
       
    return redirect(redirect_url)