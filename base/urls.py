from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name= 'home'),
path ('account/', views.account, name= 'account'),
path ('favourites/', views.favourites, name= 'favourites'),
path ('cart/', views.cart, name= 'cart'),
path ('charity/', views.charity, name= 'charity')
]