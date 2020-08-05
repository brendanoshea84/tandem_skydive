from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    bag = request.session.get('bag', {})

    for key, value in bag.items():
        
        test = value.get('name')
        test2 = value.get('phone')

        bag_items.append({
            'name': test,
            'phone': test2
            
            })
       
    context = {
        'bag': bag,
        'bag_items': bag_items,
        'test': test,
        'test2': test2
        
    }     

   
    print('contexts!!!!!!!')
    return context   