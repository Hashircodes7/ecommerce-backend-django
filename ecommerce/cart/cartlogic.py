from cart.models import Cart,CartItem
from products.models import Product
from django.shortcuts import get_object_or_404
from django.db import transaction

def get_or_create_cart(user):
    try:
        cart=Cart.objects.get(user=user) 
    except Cart.DoesNotExist: 
        cart=Cart.objects.create(user=user)

    return cart 

@transaction.atomic 
def add_to_Cart(user,product_id,quantity=1):
    cart=get_or_create_cart(user) 
    product=get_object_or_404(Product,id=product_id)
    if product.stock < quantity:
        raise ValueError("Not enough stock available.") 
    
    try:
        cartitem=CartItem.objects.get(cart=cart,product=product) 
    except CartItem.DoesNotExist:
        cartitem=CartItem.objects.create(cart=cart,product=product) 
    
    if product.stock < cartitem.quantity+quantity: 
        raise ValueError("Not enough stock available.")
    cartitem.quantity+=quantity
    cartitem.save()

@transaction.atomic
def update_cart_item(user,product_id,quantity):

    cart=get_or_create_cart(user) 
    cartitem=get_object_or_404(CartItem,cart=cart,product=product_id) 
   

    if quantity<=0:
        cartitem.delete()
        return
    

    if cartitem.product.stock < quantity:
        raise ValueError("Not enough stock available")

    cartitem.quantity=quantity 
    cartitem.save()


@transaction.atomic
def remove_from_cart(user,product_id):
    cart=get_or_create_cart(user)
    cartitem=get_object_or_404(CartItem,cart=cart,product=product_id)
    cartitem.delete()

@transaction.atomic
def clear_cart(user):
    cart=get_or_create_cart(user)
    cart.items.all().delete()
