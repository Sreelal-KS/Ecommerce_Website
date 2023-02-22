from django.shortcuts import render, redirect, get_object_or_404
from Ecommerce_App.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def cart_id(request):
    cart = request.session.session_key  # Getting the session key
    if not cart:  # If there is nothing in the session then creating the session key
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, cart=cart, quantity=1)
        cart_item.save()
    return redirect('Cart_App:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass  # pass means no operation
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))
    # 'dict()' is another method to pass the objects as dictionary {'key': and value}


def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity = cart_item.quantity - 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('Cart_App:cart_detail')


def cart_delete(request, product_id):
    cart = Cart.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('Cart_App:cart_detail')
