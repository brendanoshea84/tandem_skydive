from django.urls import path
from . import views

urlpatterns = [
    path('skydive-packages', views.skydive_packages, name='skydive-packages'),
    path('film', views.film, name='film'),
    
]