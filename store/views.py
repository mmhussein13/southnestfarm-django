# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Product
from carts.models import CartItem
from django.db.models import Q

from carts.views import _cart_id
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

def store(request, category_slug=None):
    """Render the store page with available products, optionally filtered by category."""
    category = None
    products = None
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        paginator = Paginator(products, 4)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    
    context = {
        'products': paged_products,
        'product_count': product_count,
        'category': category,
    }
    
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    """Render the product detail page for a specific product."""
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()
        
    except Product.DoesNotExist:
        return HttpResponse("Product not found")
    
    context = {
        'product': product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)

def search(request):
    """Render the search results page based on the provided keyword."""
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword)).order_by('-created_date')
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)
