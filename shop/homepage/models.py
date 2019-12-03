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
   
    product = models.OneToOneField(Product,related_name='products', on_delete=models.CASCADE,null=True)
    # TODO: Define fields here
    start_deal =  models.DateTimeField(default=now,editable=False)
    end_deal = models.DateTimeField("Ngày hết")
    available = models.BooleanField(default=True)
    time_deal   = models.CharField(editable=False, max_length=50)
    
    class Meta:
        """Meta definition for HotDeal."""

        verbose_name = 'HotDeal'
        verbose_name_plural = 'HotDeals'
    def save(self,*args, **kwargs):
        if self.start_deal > self.end_deal:
            self.end_deal = self.start_deal
            
        super(HotDeal, self).save(*args, **kwargs)
    def __str__(self):
        """Unicode representation of HotDeal."""
        return '{} - Thời gian: {}'.format(self.product,self.time_deal)
