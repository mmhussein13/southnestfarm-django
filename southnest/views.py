# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.shortcuts import render
from store.models import Product

def home(request):
    """Render the home page with available products."""
    products = Product.objects.filter(is_available=True)  # Simplified query
    
    context = {
        'products': products,
    }
    
    return render(request, 'home.html', context)
