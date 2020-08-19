from django.urls import path
from . import views

urlpatterns = [
    path('review', views.view_bag, name="view_bag"),
    path('', views.add_to_bag, name="add_to_bag"),
    path('remove/<item_id>/', views.remove_from_bag, name="remove_from_bag"),
    path('cache_checkout_data/', views.cache_checkout_data, name="cache_checkout_data"),
    path('checkout_success/<order_number>', views.checkout_success, name="checkout_success"),
]
