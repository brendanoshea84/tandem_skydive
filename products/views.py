from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Product, Category
from .forms import ProductForm


# Create your views here.
def skydive_packages(request):
    """View all products and packages"""
    
    tandems = Product.objects.filter(category= 1)
    films = Product.objects.filter(category= 2)



    context = {
        'tandems': tandems,
        'films' : films

    }
    return render(request, 'skydive-packages.html', context)

def film(request): 
    """Show the difference between the film experiences"""
    return render(request, 'film.html')   