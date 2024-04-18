from django.db import models
from django.forms import forms


# Create your models here.
class student(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Store_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    store_address = models.TextField(blank=True, null=True)


class register(models.Model):
    userName = models.CharField(max_length=100)
    userEmail = models.EmailField()
    userPassword = models.CharField(max_length=100)

class StoreForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'email', 'store_name', 'contact_number', 'store_address']
