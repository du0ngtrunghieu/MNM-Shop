
from django.urls import path,include
from categories import views
app_name = 'category'
urlpatterns = [
   path('categories/', views.index, name='category-list'),
   path('categories/<slug:slug>', views.category_Page,name='list-category'),
]