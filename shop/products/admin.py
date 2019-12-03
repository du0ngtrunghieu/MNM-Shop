from django.contrib import admin
from .models import Product,Category,ProductImage,Feature,Brand
# Register your models here.

class MultilImageProduct(admin.StackedInline):
    model = ProductImage
    extra = 0
class MultilFeatureProduct(admin.StackedInline):
    model = Feature
    extra = 0
   
class PageAdminProduct(admin.ModelAdmin):
    def show_categories(self, obj):
        return '{}'.format(obj.productfamily.categories.nameCat) 
    list_display= ('title','slug','price','available','productfamily','show_categories')
    inlines = (MultilImageProduct,MultilFeatureProduct,)

admin.site.register(Product,PageAdminProduct)
admin.site.register(ProductImage)
admin.site.register(Brand)