from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('hoody/', views.hoody, name='hoody'),
    path('admin dashboard', views.dashboard, name='dashboard'),
    path('user dashboard', views.userdashboard, name='user dashboard'),
    path('addregister/', views.addregister, name='registering'),
    path('addstore/', views.addstore, name='addstore'),
    path('editstore/<int:store_id>/', views.edit_store, name='edit_store'),

    # URL pattern for deleting a store
    path('deletestore/<int:store_id>/', views.delete_store, name='delete_store'),

]
