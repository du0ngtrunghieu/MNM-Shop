from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from shop.untils import generate_unique_slug
from categories.models import Category
from filebrowser.fields import FileBrowseField
# Create your models here.
LABEL_CHOICES = (
    ('0', 'News'),
    ('25', '25%'),
    ('15', '15%')
)

class ProductImage(models.Model):
    title = models.CharField('Tên bộ ảnh',max_length=200)
    thumbnail = FileBrowseField("Image", max_length=5000, directory="uploads/", extensions=[".jpg",".jpeg","png"], blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ProductImage_detail", kwargs={"pk": self.pk})
class Feature(models.Model):
    title = models.CharField('Tên ',max_length=200)
    class Meta:
            
        verbose_name_plural = "Tính năng Sản Phẩm"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Feature_detail", kwargs={"pk": self.pk})

class Product(models.Model):
    title = models.CharField('Tên sản phẩm',max_length=200)
    price = models.FloatField('Giá')
    discount_price = models.FloatField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    label = models.CharField(choices=LABEL_CHOICES, max_length=20)
    slug = models.SlugField(unique=True,editable=False , blank = True)
    description = models.TextField() 
    feature = models.ManyToManyField(Feature) # Tính năng
    images = models.ManyToManyField(ProductImage)
    
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
        return reverse("Product_detail", kwargs={"pk": self.pk})


