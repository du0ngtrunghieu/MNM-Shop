
from django.urls import path,include
from . import views

urlpatterns = [
   path('carts/', views.CartListPage, name='detail-cart'),
   path('cart/add/<slug:slug>',views.cart_add,name='add-cart')
]