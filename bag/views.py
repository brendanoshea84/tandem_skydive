from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from products.models import Product, Jumper
# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    jumper =  get_object_or_404(Jumper)  

    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    request.session['bag'] = bag
    return redirect(redirect_url)