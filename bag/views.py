from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from products.models import Product, Jumper


def view_bag(request):
    """ A view that renders the bag contents page """

    # bag_items = []
    # bag = request.session.get('bag', {})

    # # bag = request.session['bag']

    # tandem = get_object_or_404(Product, pk=1)
 
    # context = {
        
    #     'bag': bag,
    #     'tandem': tandem
    # }

    return render(request, 'bag.html')


def add_to_bag(request):
    """ Add Jumper with details of products and basic information """

    # Get jumper details
    name = request.POST.get('jumper_Name')
    phone= request.POST.get('jumper_Phone_Number')
    film = request.POST['film_selection']

    # Page redirect and get bag
    bag = request.session.get('bag', {})
    redirect_url = request.POST.get('redirect_url')
    
 
    if request.method == 'POST':
        test = len(bag)
        customer =({'id': test, 'name': name, 'phone': phone, 'tandem': '1', 'film': film})
        
        bag[test] = customer

        if request.POST.get('another'):
            request.session['bag'] = bag
            
            print('views 111111111111')
            print(bag)
            return redirect(redirect_url)
            
        if request.POST.get('checkout'): 
            request.session['bag'] = bag
            print('views 222')
            print(bag) 
            return render(request, 'bag.html')

    

    