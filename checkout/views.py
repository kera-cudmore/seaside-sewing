from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is currently empty")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MKQDtCsSyXX0JFXkkAY7q0llbSBIRF3HFp1Wx8AAn9eVx7ePUlZdJ8rsBB6QnI3HdiJOavWxeDFuNii5nKmrHb700HvWOo6gy',
        'client_secret': 'test-client-secret',
    }

    return render(request, template, context)
