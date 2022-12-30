from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout-success/<order_number>', views.checkout-success, name='checkout-success'),
]
