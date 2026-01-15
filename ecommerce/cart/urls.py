from django.urls import path
from .views import (
    CartDetailView,
    CartAddView,
    CartUpdateView,
    CartRemoveView,
    CartClearView
)

urlpatterns = [
    path('all/', CartDetailView.as_view(), name='cart-home'),
    path('add/<int:product_id>/', CartAddView.as_view(), name='add-cart'),
    path('update/<int:product_id>/', CartUpdateView.as_view(), name='update-cart'),
    path('remove/<int:product_id>/', CartRemoveView.as_view(), name='remove-cart'),
    path('clear/', CartClearView.as_view(), name='clear-cart'),
]
