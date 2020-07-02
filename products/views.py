from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Product, Category
from .forms import ProductForm


# Create your views here.
def all_products(request):
    """View all products and packages"""
    products = Product.objects.all()


    context = {
        'products': products
    }
    return render(request, 'all_products.html', context)