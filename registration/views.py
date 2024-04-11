# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def login(request, ):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))


def home(request, ):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))


def register(request, ):
    template = loader.get_template('register.html', )
    return HttpResponse(template.render({}, request))


def hoody(request):
    template = loader.get_template('hoody.html', )
    return HttpResponse(template.render({}, request))


def dashboard(request):
    template = loader.get_template('admin_dashboard.html', )
    return HttpResponse(template.render({}, request))


def userdashboard(request):
    template = loader.get_template('user_dashboard.html', )
    return HttpResponse(template.render({}, request))
