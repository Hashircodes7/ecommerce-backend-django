from django.contrib import admin
from cart.models import Cart,CartItem
# Register your models here.
@admin.register(Cart)
class register_cart(admin.ModelAdmin):
    list_display=['user','created_at','updated_at']
    search_fields=['user__username']

@admin.register(CartItem)
class register_cart_item(admin.ModelAdmin):
    list_display=['cart','product','quantity']
    search_fields=['cart__user__username','product__name','quantity']

