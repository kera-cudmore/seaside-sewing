from django.shortcuts import render


def view_bag(request):
    """
    View that returns the shopping bag page
    to allow users to view the contents of their bag
    """

    return render(request, 'bag/bag.html')
