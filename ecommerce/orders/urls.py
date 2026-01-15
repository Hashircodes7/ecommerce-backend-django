from django.urls import path
from .views import PlaceOrderView, MyOrdersView, OrderSuccessView

urlpatterns = [
    path('create/', PlaceOrderView.as_view(), name='create-order'), 
    path('my-orders/', MyOrdersView.as_view(), name='my-orders'),    
    path('success/', OrderSuccessView.as_view(), name='order-success')
]