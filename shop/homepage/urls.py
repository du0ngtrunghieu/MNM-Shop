
from django.urls import path,include
from homepage import views
app_name = 'homepage'
urlpatterns = [
   path('', views.HomePage, name='homepage'),

]