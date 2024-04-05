from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def login(request, ):
    template = loader.get_template('bootsrap.html')
    return HttpResponse(template.render())
def new (request,):
    template = loader.get_template('new file.html')
    return HttpResponse(template.render())
def base (request,):
    template = loader.get_template('base.html',)
    return HttpResponse(template.render())

