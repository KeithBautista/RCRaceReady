from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """Renders Basket Cart"""
    
    return render(request, 'bag/bag.html')