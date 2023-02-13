from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
# Create your views here.


def remove_from_bag(request, item_id):
    """Removes item from bag"""

    product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'{product.name} has been removed from your basket')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing this item from your basket {e}')
        return HttpResponse(status=500)


def adjust_bag(request, item_id):
    """Adjusting the quantity of object"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))  # converted to integer
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')

    else:
        bag.pop(item_id)
        messages.success(request, f'{product.name} has been removed from your basket')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def view_bag(request):
    """Renders Basket Cart"""
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Added quantity when object added into bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))  # converted to integer
    redirect_url = request.POST.get('redirect_url')  # redirect url
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity  # increments the quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')

    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)