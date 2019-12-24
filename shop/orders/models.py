from django.db import models
from products.models import Product
from carts.models import Coupon
from django.contrib.auth import get_user_model
User = get_user_model()
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField("Đã thanh toán",default=False)
    promo = models.ForeignKey(Coupon, on_delete=models.CASCADE,blank=True,null=True)
    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        if self.promo:
            return int(sum(item.get_cost() for item in self.items.all()) - self.promo.amount)
        else:
            return int(sum(item.get_cost() for item in self.items.all()))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
    
