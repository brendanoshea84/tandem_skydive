from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Product, Category
from .forms import ProductForm


# Create your views here.
def all_products(request):
    """View all products and packages"""
    products = Product.objects.all()
    categories = None

    if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products
    }
    return render(request, 'all_products.html', context)

def film(request): 
    """Show the difference between the film experiences"""
    return render(request, 'film.html')   