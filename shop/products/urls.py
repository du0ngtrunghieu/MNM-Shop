
from django.urls import path,include
from products import views

urlpatterns = [
   path('products/', views.ProductListPage, name='list-products'),
   path('products/<slug:slug>',views.ProductDetailPage ,name='detail-products'),

]