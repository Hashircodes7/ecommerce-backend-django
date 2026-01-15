from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from orders.models import Order,OrderItem
from django.views import View
from cart.models import Cart
# Create your views here.


class OrderSuccessView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'orders/order_success.html')
    
class PlaceOrderView(LoginRequiredMixin, View):

    @transaction.atomic
    def post(self, request):
        
        cart = Cart.objects.get(user=request.user)
        
        if not cart.items.exists():
            return redirect('cart-home')

        order = Order.objects.create(user=request.user)

        total = 0  
        
        for item in cart.items.select_related('product'):
            product = item.product
               
            if product.stock < item.quantity:
                raise ValueError("Stock changed, not enough items")

           
            order_item=OrderItem.objects.create(
                order=order,
                product=product,
                price=product.price,
                quantity=item.quantity
            )

            
            product.stock -= item.quantity
            product.save()

            
            total += order_item.price * order_item.quantity

       
        order.total_price = total
        order.save()

        
        cart.items.all().delete()

        return redirect('order-success')


class MyOrdersView(LoginRequiredMixin,View):

    def get(self,request):
        orders=Order.objects.filter(user=request.user).prefetch_related('items')

        return render(request,'orders/my_orders.html',{'orders':orders})




