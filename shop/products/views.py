from django.shortcuts import render,get_object_or_404
from django.views.generic import (TemplateView,DetailView,ListView)
from .models import Product

from django.shortcuts import get_object_or_404
# Phân trang
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def ProductListPage(request):
    numb_display_page = 5
    all_product = Product.objects.filter( available = True)
    paginator = Paginator(all_product, numb_display_page)
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        "all_product":products
    }

    return render(request,"product-test.html",context)
def ProductDetailPage(request,slug):
    return render(request,"product-detail-test.html",{})