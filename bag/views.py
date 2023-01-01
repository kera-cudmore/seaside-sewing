from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    HttpResponse,
)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """
    View that returns the shopping bag page
    to allow users to view the contents of their bag
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified product to the shopping bag
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # If product already in bag - update quantity & check stock level
    if item_id in list(bag.keys()):
        updated_quantity = bag[item_id] + quantity
        check_quantity = product.stock - updated_quantity

        # if there is enough stock, add to bag and show message
        if check_quantity >= 0:
            bag[item_id] = updated_quantity
            messages.success(request, f'Added an additional {quantity} of \
                {product.name} to your bag. The total quantity of \
                {product.name} in your bag is {updated_quantity}.')

        # if not enough stock return error toast
        else:
            messages.error(request, f'Sorry, we do not currently have \
                stock levels for {product.name} to fulfill your \
                current needs. Please adjust your quantity for \
                {product.name}.')

    # add product to bag
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Update quantity of a specified product to the updated amount
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to \
            {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove product from bag
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
