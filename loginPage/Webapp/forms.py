from django.forms import  ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from  django.contrib.auth.models import User
from .models import *


class  Customer(ModelForm):
    class  Meta:
        model = Customer
        fields = '__all__'