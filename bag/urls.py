from django.urls import path
from . import views

urlpatterns = [
    path('review', views.view_bag, name="view_bag"),
    path('', views.add_to_bag, name="add_to_bag"),
    path('remove/<item_id>/', views.remove_from_bag, name="remove_from_bag"),
    
]
