from django.db import models
from django.urls import reverse
from slugify import slugify
from shop.untils import generate_unique_slug
from categories.models import Category
from filebrowser.fields import FileBrowseField
# Create your models here.
LABEL_CHOICES = (
    ('N', 'News'),
    ('H', 'Hot'),
    ('T', 'Trend')
)


    

class Product(models.Model):
    title = models.CharField('Tên sản phẩm',max_length=200)
    price = models.FloatField('Giá')
    discount_price = models.FloatField('Giảm giá (%)',blank=True, null=True)
    categories = models.ManyToManyField(Category)
    label = models.CharField(choices=LABEL_CHOICES, max_length=20)
    slug = models.SlugField(unique=True,editable=False , blank = True)
    description = models.TextField('Thông tin sản phẩm') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    
    
    class Meta:
            
        verbose_name_plural = "Sản Phẩm"
    def save(self, *args, **kwargs):
        if self.slug:  
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Product, self.title)
        else: 
            self.slug = generate_unique_slug(Product, self.title)
        super(Product, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail-products", kwargs={"slug": self.slug})

class Feature(models.Model):
    title = models.CharField('Tên ',max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    class Meta:
            
        verbose_name_plural = "Tính năng Sản Phẩm"

    def __str__(self):
        return self.title


class ProductImage(models.Model):
   
    thumbnail = FileBrowseField("Image", max_length=5000, directory="products/", extensions=[".jpg",".jpeg",".png"], blank=True)
    product = models.ForeignKey(Product,related_name='images', on_delete=models.CASCADE,null=True)
    