from django.contrib import admin
from products.models import Category,Product
# Register your models here.
@admin.register(Category)
class register_category(admin.ModelAdmin):
    list_display=['name','slug']
    search_fields=['name','slug']

@admin.register(Product)
class register_product(admin.ModelAdmin):
    list_display=['name','price','category','stock','created_at','is_active']
    search_fields=['name','category__name','is_active']


