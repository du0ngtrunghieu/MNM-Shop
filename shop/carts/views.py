from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import HttpResponseRedirect
from products.models import Product
from .cart import Cart
from .models import Coupon
def cart_add(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    cart.add(product=product, quantity=1)
    return redirect('cart:detail-cart')
def cart_remove(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    cart.remove(product=product)
    return redirect('cart:detail-cart')
# Create your views here.
def CartListPage(request):
    cart = Cart(request)
    return render(request, 'cart-detail.html', {'cart': cart})

@require_POST
def coupon_check(request):
    if request.method=="POST":
        cart = Cart(request)
        code=request.POST.get("code")
        try:
            coupon = Coupon.objects.get(code=code)
            request.session['coupon_id'] = str(coupon.id)
            print(coupon.id)
            messages.success(request, f"Đã thêm mã giảm giá : {code}")
            
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except ObjectDoesNotExist:
            messages.warning(request, f'MÃ GIẢM GIÁ KHÔNG ĐÚNG')     
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def coupon_remove(request,slug):
    if slug:
        coupon = Coupon.objects.get(code=slug)
        coupon_id = str(coupon.id)
        
        if int(coupon_id) == int(request.session.get('coupon_id')):
           
            del request.session['coupon_id']      
            return redirect('cart:detail-cart')
    return redirect('cart:detail-cart')