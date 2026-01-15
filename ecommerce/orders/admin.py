from django.contrib import admin
from orders.models import Order,OrderItem
# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'price', 'quantity')

    
@admin.register(Order)
class register_order(admin.ModelAdmin):
    list_display=['id','user','total_price','created_at','status']
    list_filter = ('status', 'created_at')
    inlines = [OrderItemInline]
