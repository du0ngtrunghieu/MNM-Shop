from django.db import models
from django.urls import reverse
from slugify import slugify
from shop.untils import generate_unique_slug

# Create your models here.
class Category(models.Model):
    nameCat = models.CharField('Tên Thể Loai',max_length=5000, unique=True)
    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',verbose_name='Thể Loại Cha')
    slug = models.SlugField(unique=True,editable=False , blank = True)
    timestamp = models.DateTimeField('Ngày Tạo', auto_now=False, auto_now_add=True)
    featured = models.BooleanField(default = True)
    
    class Meta:
        #unique_together = ('slug', 'parent',)    
        verbose_name_plural = "Thể Loại"
    def __str__(self):
        return self.nameCat
    
    def save(self, *args, **kwargs):
        if self.slug:  
            if slugify(self.nameCat) != self.slug:
                self.slug = generate_unique_slug(Category, self.nameCat)
        else: 
            self.slug = generate_unique_slug(Category, self.nameCat)
        super(Category, self).save(*args, **kwargs)
class ProductFamily(models.Model):
    name = models.CharField('Dòng sản phẩm', max_length=200 )
    categories = models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name_plural = "Dòng Sản Phẩm"

    def __str__(self):
        return self.name