from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    grand_total = 0
    bag = request.session.get('bag', {})

    for key, value in bag.items():
        tandem = int(value.get('tandem'))
        tandem = get_object_or_404(Product, pk=tandem)
        film = int(value.get('film'))
        film = get_object_or_404(Product, pk=film)

        subtotal = tandem.price + film.price
        grand_total += subtotal
        bag_items.append({
            'id' : value.get('id'),
            'name' : value.get('name'),
            'phone' : value.get('phone'),
            'email' : value.get('email'),
            'film' : film,
            'tandem' : tandem,
            'subtotal': subtotal,
            
            })
            
       
    context = {
        'bag': bag,
        'bag_items': bag_items,
        'grand_total': grand_total,
        
           
    }     

    print('contexts!!!!!!!')
    return context   