from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='my first login page'),
    path('new/', views.new, name='home'),
    path('base/', views.new, name='my first news page')
]
