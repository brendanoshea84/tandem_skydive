from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    bag = request.session.get('bag', {})

    for key, value in bag.items():
        tandem = int(value.get('tandem'))
        tandem = get_object_or_404(Product, pk=tandem)
        film = int(value.get('film'))
        film = get_object_or_404(Product, pk=film)

        subtotal = tandem.price + film.price

        bag_items.append({
            'name' : value.get('name'),
            'phone' : value.get('phone'),
            'email' : value.get('email'),
            'film' : film,
            'tandem' : tandem,
            'subtotal': subtotal
            })
            
       
    context = {
        'bag': bag,
        'bag_items': bag_items,
        
           
    }     

    print('contexts!!!!!!!')
    return context   