from django.db import models
from filebrowser.fields import FileBrowseField
from products.models import Product
from django.utils.timezone import now
from datetime import datetime, timezone
from django.db.models.signals import pre_save, post_save
from django.core.exceptions import ValidationError
from django import forms
from django.contrib import messages

# Create your models here.
class Slider(models.Model):
    """Model definition for Slider."""

    # TODO: Define fields here
    thumb1 = FileBrowseField("Image", max_length=5000, directory="products/", extensions=[".jpg",".jpeg",".png"], blank=True)
    thumb2 = FileBrowseField("Image", max_length=5000, directory="products/", extensions=[".jpg",".jpeg",".png"], blank=True)
    thumb3 = FileBrowseField("Image", max_length=5000, directory="products/", extensions=[".jpg",".jpeg",".png"], blank=True)
    thumb4 = FileBrowseField("Image", max_length=5000, directory="products/", extensions=[".jpg",".jpeg",".png"], blank=True)
    class Meta:
        """Meta definition for Slider."""

        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

     
class HotDeal(models.Model):
    """Model definition for HotDeal."""
   
    product = models.OneToOneField(Product,related_name='hotdeal', on_delete=models.CASCADE,null=True)
    # TODO: Define fields here
    start_deal =  models.DateTimeField("Ngày bắt đầu giảm giá")
    end_deal = models.DateTimeField("Ngày hết")
    available = models.BooleanField(default=True)
    
    class Meta:
        """Meta definition for HotDeal."""

        verbose_name = 'HotDeal'
        verbose_name_plural = 'HotDeals'
    def save(self,*args, **kwargs):
        if self.start_deal > self.end_deal:
            self.end_deal = self.start_deal
            self.available = False
            
        super(HotDeal, self).save(*args, **kwargs)
    def __str__(self):
        """Unicode representation of HotDeal."""
        return '{}'.format(self.product)
class SpecialOffer(models.Model):
    """Model definition for Special Offer."""
    product = models.OneToOneField(Product,related_name='specialoffer', on_delete=models.CASCADE,null=True)
    # TODO: Define fields here
    start_deal =  models.DateTimeField("Ngày bắt đầu giảm giá")
    end_deal = models.DateTimeField("Ngày hết")
    available = models.BooleanField(default=True)
    
    save_price = models.BigIntegerField(editable=False ,blank=True)
    # TODO: Define fields here
    
    class Meta:
        """Meta definition for Seller."""

        verbose_name = 'Ưu Đãi'
        verbose_name_plural = 'Ưu đãi đặc biệt'
    def save(self, *args, **kwargs):
        if self.product.discount_price:
           self.save_price = self.product.price - self.get_price_change()
        super(SpecialOffer, self).save(*args, **kwargs) # Call the real save() method
    def get_price_change(self):
        # tiến sau khi giảm giá
        if self.product.discount_price:
            return int(self.product.price - (self.product.price * self.product.discount_price/100))
    def __str__(self):
        """Unicode representation of Seller."""
        return '{} ---- Tiền sau khi giảm giá {} - tiết kiệm {}'.format(self.product,self.get_price_change(),self.save_price)
