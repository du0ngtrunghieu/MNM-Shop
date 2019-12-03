from django.shortcuts import render,get_object_or_404
from django.views.generic import (TemplateView,DetailView,ListView)
from .models import Product
from categories.models import Category 
from carts.cart import Cart
from django.shortcuts import get_object_or_404
from django.db.models import Count,Max,Min
# Phân trang
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def get_count_post_by_categories():
    #Product.objects.values('productfamily__categories__nameCat').annotate(count = Count('productfamily__categories__nameCat'))
    queryset = Category.objects.values('nameCat','slug').annotate(count = Count('category__productfamily')).order_by('nameCat')
    return queryset
def ProductListPage(request):
    numb_display_page = 12
    all_product = Product.objects.filter( available = True)
    categories_count = get_count_post_by_categories()
    paginator = Paginator(all_product, numb_display_page)
    cart = Cart(request)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        "all_product":products,
        "cart" : cart,
        "categories_count":categories_count
        
    }

    return render(request,"product.html",context)
def ProductDetailPage(request,slug):
    product = get_object_or_404(Product,slug = slug)
    cart = Cart(request)
    context = {
        "product":product,
        "cart":cart,
        
    }
    return render(request,"product-detail.html",context)