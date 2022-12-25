from django.shortcuts import render


def index(request):
    """
    View that returns the home page
    """
    return render(request, "home/index.html")


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
