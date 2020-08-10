
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('day-plan', views.day_plan, name="day-plan"),
    path('contact-us', views.contact_us, name="contact-us"),
    path('products', include('products.urls')),
    path('profile', include('profiles.urls')),
    path('bag', include('bag.urls')),
    
]