from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('hoody/', views.hoody, name='hoody'),
    path('admin dashboard', views.dashboard, name='dashboard'),
    path('user dashboard', views.userdashboard, name='user dashboard'),
]
