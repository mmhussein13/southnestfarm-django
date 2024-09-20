# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)
    
    context = {
        'products': products,
    }
    
    return render(request, 'home.html', context)


def coming_soon(request):
    return render(request, 'coming_soon.html')


def page_not_found(request):
    return render(request, 'page_not_found.html')


def contact_us(request):
    return render(request, 'contact_us.html')