from django.contrib import admin
from .models import Product,Category,ProductImage,Feature,Brand,StockProduct
# Register your models here.

class MultilImageProduct(admin.StackedInline):
    model = ProductImage
    extra = 0
class MultilFeatureProduct(admin.StackedInline):
    model = Feature
    extra = 0
   
class PageAdminProduct(admin.ModelAdmin):
    def show_categories(self, obj):
        return '{}'.format(obj.brands.productfamily.categories.nameCat) 
    list_display= ('title','slug','price','available','brands',)
    inlines = (MultilImageProduct,MultilFeatureProduct,)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ('product','is_stock','in_stock','is_sold')
admin.site.register(Product,PageAdminProduct)
admin.site.register(ProductImage)
admin.site.register(Brand)
admin.site.register(StockProduct,StockProductAdmin)