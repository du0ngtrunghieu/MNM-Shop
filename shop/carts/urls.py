
from django.urls import path,include
from . import views
app_name = 'cart'
urlpatterns = [
   path('carts/', views.CartListPage, name='detail-cart'),
   path('cart/add/<slug:slug>',views.cart_add,name='add-cart'),
   path('cart/add/<slug:slug>/<int:quantity>',views.cart_add_from_detail,name='add-cart-with-quantity'),
   path('cart/delete/<slug:slug>',views.cart_remove,name='remove-cart'),
   path('cart/delete-all',views.cart_remove_all,name='remove-all-cart'),
   path('check-coupon',views.coupon_check, name='check-coupon'),
   path('coupon/delete/<slug:slug>',views.coupon_remove,name='remove-coupon'),
   path('cart/update/<slug:slug>/<int:quantity>',views.cart_update,name='update-cart'),
]