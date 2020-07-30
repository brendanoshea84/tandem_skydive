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

    product = get_object_or_404(Product, pk=1)

    redirect_url = request.POST.get('redirect_url')
    name = request.POST.get('jumper_Name')
    dob = request.POST.get('jumper_Date_Of_Birth')

    bag = request.session.get('bag', {})
    
    print("stage 1")

    customer =({'name': name,'dob': dob})

    if bag == {}:
        print("stage 1")    
        bag[0] = customer

    else:
        print("stage 2")   
        test = len(bag)
        print(test)
        bag[test] = customer

    
    print("stage 4")
    request.session['bag'] = bag
    
    print(bag)




# if bag == {}:
#         bag = customer
#     else:    
#         bag.append(customer)

       
# session = [{"stuff": "things"},]

# bag = []
# customer = [{"name": "michael", "dob": "yonks ago"}, {"name": "michael2", "dob": "younger than michael"}]

# if customer:
#         for i in customer:
#                 bag.append(i)

# session.append({"bag": bag})

# print(session)






    return redirect(redirect_url)