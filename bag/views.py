from django.shortcuts import render, redirect

# Create your views here.


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