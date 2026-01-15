from django.shortcuts import render
from products.models import Product,Category
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
# Create your views here.

def paginate_queryset(request, queryset, per_page=8):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)



def product_list(request):
    products=Product.objects.all()
    page_obj=paginate_queryset(request,products)
    return render(request,'products/allproductlist.html',{'page_obj':page_obj})

def product_detail(request,slug):
    product=get_object_or_404(Product,slug=slug)
    return render(request,'products/specproduct.html',{'product':product})

def product_by_category_slug(request,slug):
    category=get_object_or_404(Category,slug=slug)
    products=Product.objects.filter(category=category) 
    page_obj=paginate_queryset(request,products)


    return render(request,'products/catproduct.html',
    {
        'page_obj': page_obj,
        'category':category
    }
    )

def product_newest(request):
    products=Product.objects.all().order_by('-created_at')
    page_obj=paginate_queryset(request,products)
    return render(request,'products/allproductlist.html',{'page_obj':page_obj})

def product_oldest(request):
    products=Product.objects.all().order_by('created_at')
    page_obj=paginate_queryset(request,products)
    return render(request,'products/allproductlist.html',{'page_obj':page_obj})


def product_in_stock(request):
    products=Product.objects.filter(stock__gt=0)
    page_obj=paginate_queryset(request,products)
    return render(request,'products/allproductlist.html',{'page_obj':page_obj})

def product_out_of_stock(request):
    products=Product.objects.filter(stock=0)
    page_obj=paginate_queryset(request,products)
    return render(request,'products/allproductlist.html',{'page_obj':page_obj})
