
from django.urls import path,include
from orders import views
app_name = 'order'
urlpatterns = [
   path('order/create', views.create_order, name='create-order'),
   path('order/',views.order_list,name='list-order'),
]