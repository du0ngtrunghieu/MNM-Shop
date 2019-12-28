from django.shortcuts import render
from .models import HotDeal,Slider,SpecialOffer
from categories.models import Category 
from django.db.models import Q
from django.utils.timezone import now
from carts.cart import Cart
from products.models import Product

from django.db.models import Count,Max,Min,Sum
# Create your views here.

# __gt : >
# __lt : <

def RemoveHotDealnotUse():
    HotDeal.objects.filter(Q(end_deal__lte = now())).delete()

def HomePage(request):
    RemoveHotDealnotUse()
    cart = Cart(request)
    deal_sale = HotDeal.objects.filter(Q(start_deal__lte=now()),Q(end_deal__gte=now()),available = True)
    category = Category.objects.filter(featured = True)
    slider = Slider.objects.all()
    # top rate : giá + só lượng mua nhiều nhất
    top_rated = Product.objects.annotate(sum_quatity = Sum('order_items__quantity')).order_by('-sum_quatity','-price')[:4]
    # Ưu Đãi Đặc Biệt
    # Special Offer
    special_offer = SpecialOffer.objects.filter(Q(start_deal__lte=now()),Q(end_deal__gte=now()),available = True).annotate(sum_quatity = Sum('product__order_items__quantity')).order_by('product__discount_price')[:1]
    # Đang sale 
    is_sale = Product.objects.filter(available = True).order_by('-discount_price')[:6]
    # Hàng đầu : giá
    top_product = Product.objects.filter(available =True).order_by('-price')[:6]
    # mới nhất 
    new_product = Product.objects.filter(available =True).order_by('-created_at')[:6]
    # phổ biến : mua nhiều
    buy_product = Product.objects.annotate(sum_quatity = Sum('order_items__quantity')).order_by('-sum_quatity')[:6]
    # Hàng cũ :
    old_product =  Product.objects.filter(available =True).order_by('created_at')[:5]
    trend_product = Product.objects.annotate(sum_quatity = Sum('order_items__quantity')).order_by('-sum_quatity','price')[:6]
    product_category = Category.objects.all()[:4]
    
    context = {
        'deal_sale' : deal_sale,
        "cart" : cart,
        'categories':category,
        'slider':slider,
        'top_rated':top_rated,
        'special_offer':special_offer,
        'is_sale':is_sale,
        'top_product':top_product,
        'new_product':new_product,
        'buy_product':buy_product,
        'old_product':old_product,
        'product_category':product_category,
        'trend_product':trend_product,
    }
    return render(request,"index.html",context)