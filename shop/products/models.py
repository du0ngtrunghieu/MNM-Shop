from django.db import models
from django.urls import reverse
from slugify import slugify
from shop.untils import generate_unique_slug
from categories.models import Category,ProductFamily
from filebrowser.fields import FileBrowseField
# Create your models here.
LABEL_CHOICES = (
    ('N', 'News'),
    ('H', 'Hot'),
    ('T', 'Trend')
)


    

class Product(models.Model):
    title = models.CharField('Tên sản phẩm',max_length=200)
    price = models.BigIntegerField('Giá')
    # phầm trăm giảm giá
    discount_price = models.BigIntegerField('Giảm giá (%)',blank=True, null=True)
    brands = models.ForeignKey("Brand",related_name='brands', on_delete=models.CASCADE,null=True)
    productfamily = models.ForeignKey(ProductFamily,related_name='productfamily', on_delete=models.CASCADE,null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=20,null=True,blank=True)
    slug = models.SlugField(unique=True,editable=False , blank = True)
    description = models.TextField('Thông tin sản phẩm') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    thumb = FileBrowseField("Image", max_length=5000, directory="products/", extensions=[".jpg",".jpeg",".png"], blank=True)
    
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
        return reverse("product:detail-products", kwargs={"slug": self.slug})
    def get_price_vnd(self):
        return '₫ {:,}'.format(self.price)
       
    def get_price_discount_vnd(self):
        if self.discount_price:
            return '₫ {:,}'.format(int(self.price -( self.price * self.discount_price/100)))
        return self.get_price_vnd()
    def get_price_discount(self):
        if self.discount_price:
            return int(self.price -( self.price * self.discount_price/100))
        return self.price

class Feature(models.Model):
    title = models.CharField('Tên ',max_length=200)
    product = models.ForeignKey(Product,related_name='features', on_delete=models.CASCADE,null=True)
    class Meta:
            
        verbose_name_plural = "Tính năng Sản Phẩm"

    def __str__(self):
        return self.title


class ProductImage(models.Model):
   
    thumbnail = FileBrowseField("Image", max_length=5000, directory="products/", extensions=[".jpg",".jpeg",".png"], blank=True)
    product = models.ForeignKey(Product,related_name='images', on_delete=models.CASCADE,null=True)
class ProductSize(models.Model):
    name = models.CharField('Tên: ', max_length=50)
    price = models.BigIntegerField('Giá',null=True)   
class Brand(models.Model):
    name = models.CharField('Tên nhãn hiệu', max_length=200 )
    productfamily = models.ForeignKey(ProductFamily,related_name='brands_PF', on_delete=models.CASCADE,null=True)
    class Meta:
        verbose_name_plural = "Nhãn Hiệu"

    def __str__(self):
        return self.name
class StockProduct(models.Model):
    product = models.OneToOneField(Product,related_name='stocks', on_delete=models.CASCADE,null=True)
    is_stock = models.BooleanField("Trạng Thái Trong Kho",default=True) # còn hàng = True
    in_stock = models.IntegerField("Số lượng sản phẩm trong kho",default=1)
    is_sold  = models.IntegerField("Số Lượng đã bán",default=0)


    class Meta:
        verbose_name = "Kho Hàng"
        verbose_name_plural = "Kho Hàng"

    def __str__(self):
        return self.product.title

    
