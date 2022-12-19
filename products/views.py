from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    view to return all products in store,
    and allow sorting and search queries
    """

    products = Products.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
