from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('register_user/', views.register, name='register'),
    path('hoody/', views.hoody, name='hoody'),
    path('admin dashboard', views.dashboard, name='dashboard'),
    path('user dashboard', views.userdashboard, name='user dashboard'),
    path('adduser', views.adduser, name='registering'),
    path('addstore/', views.addstore, name='addstore'),
    path('editstore/<id>/', views.edit_store, name='edit_store'),
    path('updatestore/<id>', views.updatestore, name='updatestore'),
    # URL pattern for deleting a store
    path('deletestore/<id>/', views.delete_store, name='delete_store'),
    path('stores/', views.stores, name='store'),
    path('registeruser', views.registration_page, name='registeruser'),
    path('products/', views.product_list),
    path('authenticate/', views.authenticate_user, name='authenticate'),
    path('shoes/', views.shoe_list),
]
