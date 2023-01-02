from django.shortcuts import render
from products.models import Category


def index(request):
    """
    View that returns the home page
    """
    categories = Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, "home/index.html", context)


def privacy(request):
    """
    View that returns the privacy policy page
    """
    return render(request, "home/privacy.html")


def terms(request):
    """
    View that returns the terms and conditions page
    """
    return render(request, "home/terms.html")


def delivery(request):
    """
    View that returns the delivery policy page
    """
    return render(request, "home/delivery.html")
