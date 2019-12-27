from django.shortcuts import render
from django.http import JsonResponse
from carts.cart import Cart
from carts.models import Coupon
from .models import OrderItem,Order
from products.models import StockProduct 
from django.db.models import Q,F
from django.contrib.auth.decorators import login_required
from categories.models import Category


# Create your views here.
@login_required
def order_list(request):
    cart = Cart(request)
    order = Order.objects.filter(user = request.user).order_by('-created')
    category = Category.objects.filter(featured = True)
    context ={
        'cart':cart,
        'order':order,
        'categories':category

    }

    return render(request,"order-list.html",context)
def create_order(request):
    cart = Cart(request)
    first_name = request.GET.get('ho')
    last_name = request.GET.get('ten')
    email = request.GET.get('email')
    address = request.GET.get('diachi')
    city = request.GET.get('thanhpho')
    coupon = None
    if 'coupon_id' in request.session:
        coupon_id = request.session['coupon_id']
        coupon = Coupon.objects.get(id=coupon_id)
    
    order = Order.objects.create(
        first_name=first_name,
        last_name = last_name,
        email = email,
        address =address,
        city = city,
        user=request.user,
        promo = coupon
    )
    for item in cart:
        OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
        
        StockProduct.objects.filter(product = item['product']).update(is_sold=F('is_sold') +int(item['quantity']),in_stock = F('in_stock')-int(item['quantity']))
        productstock =StockProduct.objects.filter(product = item['product'])
        
        # if productstock[0].in_stock <= 0:
        #     productstock.update(is_stock = False,in_stock = 0)
    cart.clear()
    return JsonResponse({"status":"ok"}) #3
    
    