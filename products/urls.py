from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('film', views.film, name='film'),
    
]