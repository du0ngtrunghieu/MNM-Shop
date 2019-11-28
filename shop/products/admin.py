from django.contrib import admin
from .models import Product,Category,ProductImage
# Register your models here.
class PageAdminProduct(admin.ModelAdmin):
    list_display= ('title','slug','price')
admin.site.register(Product,PageAdminProduct)
admin.site.register(ProductImage)