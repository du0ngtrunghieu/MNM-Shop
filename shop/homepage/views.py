from django.shortcuts import render
from .models import HotDeal,Slider
from categories.models import Category 
from django.db.models import Q
from django.utils.timezone import now
from carts.cart import Cart


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
    
    context = {
        
        'deal_sale' : deal_sale,
        "cart" : cart,
        'categories':category,
        'slider':slider,
    }
    return render(request,"index.html",context)