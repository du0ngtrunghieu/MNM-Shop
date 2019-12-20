from django.shortcuts import render,get_object_or_404
from .models import Category,ProductFamily
# Create your views here.
def index(request):
    return render(request,"category-list.html",{})
def category_Page(request,slug):
    product_cate = get_object_or_404(Category,slug=slug)
    context = {
        'product_cate':product_cate
    }
    print(context)
    return render(request,"category-list.html",context)
