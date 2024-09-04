from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    """Count the number of items in the cart for the current user."""
    cart_count = 0
    
    if 'admin' in request.path:
        return {}
    
    try:
        cart = Cart.objects.filter(cart_id=_cart_id(request)).first()
        
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user)
        else:
            cart_items = CartItem.objects.filter(cart=cart) if cart else []
        
        for cart_item in cart_items:
            cart_count += cart_item.quantity
            
    except Cart.DoesNotExist:
        cart_count = 0
    
    return dict(cart_count=cart_count)