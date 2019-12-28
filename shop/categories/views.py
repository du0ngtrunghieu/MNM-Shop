from django.shortcuts import render,get_object_or_404
from .models import Category,ProductFamily
from carts.cart import Cart
from products.models import Product,Brand
from django.db.models import Count,Max,Min
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def get_count_product_by_categories():
    #Product.objects.values('productfamily__categories__nameCat').annotate(count = Count('productfamily__categories__nameCat'))
    queryset = Category.objects.values('nameCat','slug').annotate(count = Count('category__brands_PF')).order_by('nameCat')
    return queryset
def get_price_min_max():
    queryset = Product.objects.aggregate(max = Max('price'),min = Min('price'))
    return queryset
def get_count_product_by_brands():
    queryset = Brand.objects.values('name','id').annotate(count =Count('brands'))
    return queryset

def index(request):
    return render(request,"category-list.html",{})
def category_Page(request,slug):
    all_product = Product.objects.filter(brands__productfamily__categories__slug=slug);
    sort_key = request.GET.get('sort') 
    price_min = request.GET.get('start')
    price_max = request.GET.get('end')
    category_sort = request.GET.get('category')
    product_family = request.GET.get('p')
    brands = request.GET.get('b')
    search = request.GET.get('search')
    queryset="?" if price_max is None and price_max is None and sort_key is None and category_sort is None else ""
    if price_max and price_min:
        all_product = all_product.filter(price__gte = price_min , price__lte=price_max)
        queryset = queryset + "&start="+price_min+"&?end="+price_max
    elif sort_key:
        sort = VALID_SORTS.get(sort_key, DEFAULT_SORT)
        all_product = all_product.filter( available = True).order_by(sort)
        queryset = queryset + "&sort="+sort_key
    elif category_sort:
        all_product = all_product.filter(brands__productfamily__categories__slug=category_sort)
        queryset = queryset + "&category="+category_sort
    
    elif brands and product_family:
        all_product = all_product.filter(brands =brands)
    elif product_family:
        all_product = all_product.filter(brands__productfamily__id=product_family)
    elif search:
        all_product = all_product.filter(title__icontains=search)
    numb_display_page = 12
    categories_count = get_count_product_by_categories()
    max_min_price = get_price_min_max()
    brands_count = get_count_product_by_brands()
    category = Category.objects.filter(featured = True) 
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
        "categories_count":categories_count,
        "max_min_price":max_min_price,
        'brands_count':brands_count,
        'queryset':queryset,
        'categories':category
        
    }
    
    return render(request,"category.html",context)
