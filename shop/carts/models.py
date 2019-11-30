from django.db import models

# Create your models here.

class Coupon(models.Model):
    code = models.CharField("Mã giảm giá", max_length=50)
    amount = models.BigIntegerField("Số tiền giảm giá",default=0)
    def __str__(self):
        return '{} - {} VNĐ'.format(self.code,self.amount)