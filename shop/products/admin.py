from django.contrib import admin
from .models import Product,Category,ProductImage,Feature
# Register your models here.

class MultilImageProduct(admin.StackedInline):
    model = ProductImage
    extra = 0
class MultilFeatureProduct(admin.StackedInline):
    model = Feature
    extra = 0
class PageAdminProduct(admin.ModelAdmin):
    list_display= ('title','slug','price','available')
    inlines = (MultilImageProduct,MultilFeatureProduct,)

admin.site.register(Product,PageAdminProduct)
admin.site.register(ProductImage)