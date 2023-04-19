from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.home, name = 'home'),
    # path('login/', views.loginform.as_view(), name = 'login'),
    path('login/', views.login, name = 'login'),
    path('logup/', views.logup, name = 'logup'),
    path('shop/', views.shop, name = 'shop'),
    path('single/', views.single, name= 'single'),
    path('cart/', views.cart, name = 'cart')
]