from django.shortcuts import redirect,render
from django.contrib import messages
from products.models import Product
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.cartlogic import add_to_Cart,get_or_create_cart,update_cart_item,clear_cart,remove_from_cart
# Create your views here.

class CartDetailView(LoginRequiredMixin,View):
    def get(self,request):
        cart=get_or_create_cart(request.user)
        return render(request,'cart/cart_detail.html',{'cart':cart})

class CartAddView(LoginRequiredMixin,View):
    def get(self,request,product_id):
        try:
            add_to_Cart(request.user,product_id,quantity=1)
            messages.success(request, 'Product added to cart.')
        except ValueError as e:
            messages.error(request, str(e))
        return redirect('product-detail',slug=Product.objects.get(id=product_id).slug)

class CartUpdateView(LoginRequiredMixin,View):
    def post(self,request,product_id):
        if request.method=='POST':
            quantity=int(request.POST.get('quantity',1))
        try:
            update_cart_item(request.user,product_id,quantity)
            messages.success(request, 'Cart updated successfully.')
        except ValueError as e:
            messages.error(request, str(e))
        return redirect('cart-home')

class CartRemoveView(LoginRequiredMixin,View):
    def get(self,request,product_id):
        remove_from_cart(request.user,product_id)
        messages.success(request, 'Item removed from cart.')
        return redirect('cart-home')

class CartClearView(LoginRequiredMixin,View):
    def get(self,request):
        clear_cart(request.user)
        messages.success(request, 'Cart cleared.')
        return redirect('cart-home')
