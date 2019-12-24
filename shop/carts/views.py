from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import Product,StockProduct
from .cart import Cart
from .models import Coupon
def cart_add(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    cart.add(product=product, quantity=1)
    return redirect('cart:detail-cart')
def cart_add_from_detail(request):
    cart = Cart(request)
    slug = request.POST.get("slug")
    quantity = request.POST.get("quantity")
    product = get_object_or_404(Product, slug=slug)
    cart.add(product=product, quantity=int(quantity))
    return redirect('cart:detail-cart')
def cart_remove(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    cart.remove(product=product)
    messages.success(request, f"Đã xoá sản phẩm trong giỏ hàng")
    return redirect('cart:detail-cart')
def cart_remove_all(request):
    cart = Cart(request)
    cart.removeAll()
    messages.success(request, f"Đã xoá tất cả sản phẩm trong giỏ hàng")
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
            coupon = Coupon.objects.get(code__iexact=code)
            request.session['coupon_id'] = str(coupon.id)
            
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
            messages.info(request, f'Đã xoá mã giảm giá')      
            return redirect('cart:detail-cart')
    return redirect('cart:detail-cart')

@require_POST
@csrf_exempt
def cart_update(request,slug,quantity):
    
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    if quantity ==0:
        cart.remove(product=product)
    else:
        # kiểm tra số lượng trong kho so với số lượng update
        check =StockProduct.objects.filter(product = product,in_stock__gt = quantity).exists()
        if(check == True):
            cart.add(product=product, quantity=quantity,update_quantity=True)
            messages.info(request, f'Cập nhật giỏ hàng thành công')  
        else:
            messages.warning(request,f'Số lượng phải nhỏ hơn số lượng còn lại trong kho')
        
    return JsonResponse({'status': 'true'})
    

