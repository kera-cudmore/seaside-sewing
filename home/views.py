from django.shortcuts import render


def index(request):
    """
    View that returns the home page
    """
    return render(request, "home/index.html")
