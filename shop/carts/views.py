from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart

def cart_add(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    cart.add(product=product, quantity=1)
    return redirect('detail-cart')

# Create your views here.
def CartListPage(request):
    cart = Cart(request)
    return render(request, 'cart-list.html', {'cart': cart})