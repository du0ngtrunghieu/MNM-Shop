from decimal import Decimal
from django.conf import settings
from products.models import Product
from .models import Coupon


class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')
    def __len__(self):
        return sum(1 for item in self.cart.values())
    def add(self, product, quantity, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        
        self.save()
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    def removeAll(self):
        cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.save()
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
           
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            item['total_price_vnd'] = '{:,} VNĐ'.format(item['total_price'])    
            yield item
         
    def get_total_price(self):
        return '{:,} VNĐ'.format(sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()))
    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id) 
        return None
    def get_total_price_after_discount(self):
        
        if self.coupon.amount is None:
            self.coupon.amount = 0
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()) - self.coupon.amount
        
    def get_total_price_after_discount_vnd(self):
        if self.coupon is None:
            return '{:,} VNĐ'.format(sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()))
        return '{:,} VNĐ'.format(sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()) - self.coupon.amount)
    def amount_coupon_vnd(self):
        return '{:,} VNĐ'.format(self.coupon.amount)
    
