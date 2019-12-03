from django.contrib import admin
from .models import Category,ProductFamily
# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display= ('nameCat','slug')

admin.site.register(Category,AdminCategory)
admin.site.register(ProductFamily)