
from django.urls import path,include
from orders import views
app_name = 'order'
urlpatterns = [
   path('order/create', views.create_order, name='create-order'),

]