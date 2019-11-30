
from django.urls import path,include
from . import views
app_name = 'cart'
urlpatterns = [
   path('carts/', views.CartListPage, name='detail-cart'),
   path('cart/add/<slug:slug>',views.cart_add,name='add-cart'),
   path('cart/delete/<slug:slug>',views.cart_remove,name='remove-cart'),
   path('check-coupon',views.coupon_check, name='check-coupon'),
   path('coupon/delete/<slug:slug>',views.coupon_remove,name='remove-coupon'),
]