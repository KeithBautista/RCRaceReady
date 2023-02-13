from django.shortcuts import render, redirect, reverse

# Create your views here.

def adjust_bag(request, item_id):
    """ Adjusting the quantity of the specified product to the specified amount """

    quantity = int(request.POST.get('quantity'))  # converted to integer
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop[item_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def view_bag(request):
    """Renders Basket Cart"""
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Added quantity when object added into bag """

    quantity = int(request.POST.get('quantity'))  # converted to integer
    redirect_url = request.POST.get('redirect_url')  # redirect url
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity  # increments the quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)