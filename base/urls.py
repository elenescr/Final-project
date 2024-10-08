from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name= 'home'),
path ('account/', views.account, name= 'account'),
path ('contact/', views.contact_view, name= 'contact'),
path ('info/', views.info_view, name= 'info'),
path ('favourites/<str:pk>/', views.favourites, name= 'favourites'),
path ('product/', views.product, name= 'product'),
path ('about/<str:id>', views.about, name= 'about'),
path ('charity/', views.charity, name= 'charity'),
path ('adding/<str:id>/', views.adding, name= 'adding'),
path ('delete/<str:id>/', views.delete, name= 'delete'),
path ('login/', views.login_page, name= 'login'),
path ('register/', views.register_page, name= 'register'),
path ('logout/', views.logout_user, name= 'logout'),
path ('add/', views.add_item, name= 'add'),
path ('delete_item/<int:id>/', views.delete_item, name= 'delete_item'),
path ('update_user/', views.update_user, name= 'update_user'),
path ('delete_comment/<int:id>/', views.delete_comment, name= 'delete_comment'),
path ('update_item/<int:item_id>/', views.update_item, name= 'update_item'),
path ('success/', views.success, name= 'success'),

]