from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import  UserCreationForm
from .forms import Customer


# Create your views here.
def registerPage(request):  

    form = Customer()

    context = {form: 'form'}
    return render(request, 'Webapp/register.html', context)


def home(request):
    context = {}
    return render(request, 'Webapp/home.html' ,context)