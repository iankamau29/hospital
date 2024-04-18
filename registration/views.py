# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .models import register
from .models import student

def login(request, template):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))


def home(request, ):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))


def register(request, ):
    """

    :rtype: object
    """
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

@csrf_exempt
def addregister(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        password = request.POST.get('Password')

        mydata = {'Name': name, 'Email': email, 'Password': password}
        print(mydata)

        obj1 = register(userName=name, userEmail=email, userPassword=password)
        obj1.save()
        return render(request, 'home.html')


from django.shortcuts import render
from .models import student
@csrf_exempt
def addstore(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        storename = request.POST.get('storename')
        contactnumber = request.POST.get('contactnumber')
        storeaddress = request.POST.get('storeaddress')

        # Create a new instance of the student model and save it to the database
        obj1 = student(Name=name, Email=email, Store_name=storename, contact_number=contactnumber, store_address=storeaddress)
        obj1.save()

        # Fetch all data from the student model
        mydata = student.objects.all()
        context = {'stores': mydata}  # Pass the data to the template context

        return render(request, 'admin_dashboard.html', context)
    else:
        return render(request, 'admin_dashboard.html')  # Render the template without context if the request method is not POST


def edit_store(request, store_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        storename = request.POST.get('storename')
        contactnumber = request.POST.get('contactnumber')
        storeaddress = request.POST.get('storeaddress')

        edit_store=student.objects.get(pk=store_id)
        edit_store.Name=name
        edit_store.Email=email
        edit_store.Store_name=storename
        edit_store.contact_number=contactnumber
        edit_store.store_address=storeaddress
    return redirect('admin_dashboard')


def delete_store(request, store_id):
    # Retrieve the store object using the store_id
    delete_store=student.objects.get(pk=store_id)
    # Your delete logic here
    delete_store.delete()
    return redirect('/admin_dashboard')