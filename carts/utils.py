from .models import Cart

def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id') #None
    cart = Cart.objects.filter(cart_id=cart_id).first() #None

    if cart is None:
        cart = Cart.objects.create(user=user)

    request.session['cart_id'] = cart.cart_id

    return cart

def destroy_cart(request):
    request.session['cart_id'] = None
