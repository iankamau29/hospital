import email
from os import name

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import student, registration, shoes
import requests
from .models import product
from .serializers import ProductSerializer, shoesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status
from django.http import JsonResponse


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def shoe_list(request):
    if request.method == 'GET':
        shoe = shoes.objects.all()
        serializer = shoesSerializer(shoe, many=True)
        return Response(serializer.data)


def login(request):
    return render(request, 'login.html')


@csrf_exempt
def register(request):
    template = loader.get_template('registration.html')
    return HttpResponse(template.render())


@csrf_exempt
def registration_page(request):
    template = loader.get_template('login.html')
    if request.method == 'POST':
        userName = request.POST.get('username')
        userEmail = request.POST.get('email')
        password = request.POST.get('password')
        mydata = {'name': userName, 'email': userEmail, 'password': password}
        print(mydata)
        query = registration(userName=userName, userEmail=userEmail, userPassword=password)
        query.save()
    return HttpResponse(template.render())


@csrf_exempt
def adduser(request):
    template = loader.get_template('login.html')
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mydata = {'name': name, 'email': email, 'password': password}
        print(mydata)
        query = registration(userName=name, userEmail=email, userPassword=password)
        query.save()
    return HttpResponse(template.render())


def addstore(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        storename = request.POST.get('storename')
        contactnumber = request.POST.get('contactnumber')
        storeaddress = request.POST.get('storeaddress')

        obj1 = student(Name=name, Email=email, Store_name=storename, contact_number=contactnumber,
                       store_address=storeaddress)
        obj1.save()

        mydata = student.objects.all()
        context = {'stores': mydata}
        return render(request, 'admin_dashboard.html', context)
    else:
        return render(request, 'admin_dashboard.html')


def updatestore(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        storename = request.POST.get('storename')
        contactnumber = request.POST.get('contactnumber')
        storeaddress = request.POST.get('storeaddress')

        editestore = student.objects.get(id=id)
        editestore.Name = name
        editestore.Email = email
        editestore.Store_name = storename
        editestore.contact_number = contactnumber
        editestore.store_address = storeaddress
        editestore.save()

    return redirect('/stores')


def delete_store(request, id):
    deletestore = student.objects.get(id=id)
    deletestore.delete()
    return redirect('/stores')


def stores(request):
    mydata = student.objects.all()
    context = {'stores': mydata}
    return render(request, 'admin_dashboard.html', context)


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))


def userdashboard(request, template):
    template = loader.get_template('user_dashboard.html')
    return HttpResponse(template.render({}, request))


def hoody(request):
    template = loader.get_template('hoody.html')
    return HttpResponse(template.render({}, request))


def some_view(request):
    url = "https://example.com"
    response = requests.get(url)

    if response.status_code == 200 and response.headers.get("X-Frame-Options") is not None:
        pass


@csrf_exempt
def dashboard(request):
    mydata = student.objects.all()
    context = {'stores': mydata}
    return render(request, 'admin_dashboard.html', context)


def edit_store(request, id):
    data = student.objects.get(id=id)
    context = {'data': data}
    return render(request, 'user_dashboard.html', context)


def authenticate_user(request):
    if request.method == 'POST':
        userName = request.POST.get('username')
        password = request.POST.get('password')

        users = registration.objects.filter(userName=userName)
        if users.exists():
            for user in users:
                if user.userPassword == password:
                    print('success')
                    return redirect('home')
        return redirect('/login')
