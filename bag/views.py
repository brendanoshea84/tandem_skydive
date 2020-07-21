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
    print("working stage 1")
    redirect_url = request.POST.get('redirect_url')
    name = request.POST.get('jumper_Name')
    dob = request.POST.get('jumper_Date_Of_Birth')

    a = 0
    print(a)

    print("working stage 2")
    
    bag = request.session.get('bag', {})

    print("working stage 3")

    if request.method == 'POST':
        a += 1
        customer = {
            "name": name,
            "dob": dob
        }
        bag[a] = customer
        
        print("*********")
        print(a)
        print("*********")
        print(customer)
        print("*********")
        print("test bag")
        print(bag)
        
        
    

    return redirect(redirect_url)