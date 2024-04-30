from django.db import models
from django.forms import forms


# Create your models here.
class student(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Store_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    store_address = models.TextField(blank=True, null=True)


class registration(models.Model):
    userName = models.CharField(max_length=100)
    userEmail = models.EmailField()
    userPassword = models.CharField(max_length=100)


class StoreForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'email', 'store_name', 'contact_number', 'store_address']


class shoes(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='shoes/')
    description = models.TextField()
    price = models.IntegerField()




class product(models.Model):
    productname = models.CharField(max_length=100)
    price = models.IntegerField()

