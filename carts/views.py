# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from store.models import Product
from .models import Cart, CartItem
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart: 
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id) # Getting the product
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) # Getting cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request), 
        )
    cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    
    return redirect('cart')

def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_item=None):
    try:
        tax = 0
        grand_total = 0
        shipping_flat_rate = 0
        shipping_local_pickup = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items   = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity
        
        tax         = (17 * total)/100
        shipping_flat_rate = 20000
        shipping_local_pickup = 0
        grand_total = total + tax + shipping_flat_rate
        
        

    except ObjectDoesNotExist:
        total = quantity = cart_items = None

    context = {
        'total'                 : total,
        'quantity'              : quantity,
        'cart_items'            : cart_items,
        'tax'                   : tax,
        'grand_total'           : grand_total,
        'shipping_flat_rate'    : shipping_flat_rate,
        'shipping_local_pickup' : shipping_local_pickup,
    }
    return render(request, 'store/cart.html', context)


@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cart_item=None):
    try:
        tax = 0
        grand_total = 0
        shipping_flat_rate = 25000  # Example flat rate
        shipping_local_pickup = 0   # Example local pickup rate
        total = 0
        quantity = 0
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        # Calculate total price and quantity
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity

        # Calculate tax (if applicable)
        tax = (17 * total) / 100

        # Determine selected shipping method (default to flat rate)
        shipping_method = request.POST.get('selectprice', 'flateRate')  # Default to 'flateRate'

        # Calculate grand total based on shipping method
        if shipping_method == 'flateRate':
            grand_total = total + shipping_flat_rate
        elif shipping_method == 'localPickup':
            grand_total = total + shipping_local_pickup
        else:
            grand_total = total  # No shipping cost if none of the above is selected

    except ObjectDoesNotExist:
        total = quantity = cart_items = None

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
        'shipping_flat_rate': shipping_flat_rate,
        'shipping_local_pickup': shipping_local_pickup,
    }
    return render(request, 'store/checkout.html', context)