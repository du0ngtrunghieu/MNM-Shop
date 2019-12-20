from django.shortcuts import render
from django.http import JsonResponse
from carts.cart import Cart
from carts.models import Coupon
from .models import OrderItem,Order
# Create your views here.
def create_order(request):
    cart = Cart(request)
    first_name = request.GET.get('ho')
    last_name = request.GET.get('ten')
    email = request.GET.get('email')
    address = request.GET.get('diachi')
    city = request.GET.get('thanhpho')
    coupon_id = None
    if 'coupon_id' in request.session:
        coupon_id = request.session['coupon_id']
    
    order = Order.objects.create(
        first_name=first_name,
        last_name = last_name,
        email = email,
        address =address,
        city = city,
        user=request.user,
        promo = Coupon.objects.get(id=coupon_id)
    )
    for item in cart:
        OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
    cart.clear()
    return JsonResponse({"status":"ok"}) #3
    
    