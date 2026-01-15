from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.product_list, name='product-list'),
    path('in-stock/', views.product_in_stock, name='product-in-stock'),
    path('out-of-stock/', views.product_out_of_stock, name='product-out-of-stock'),
    path('newest/', views.product_newest, name='product-newest'),
    path('oldest/', views.product_oldest, name='product-oldest'),
    path('category/<slug:slug>/', views.product_by_category_slug, name='product-by-category'),
    path('<slug:slug>/', views.product_detail, name='product-detail'),
]
