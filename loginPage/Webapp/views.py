from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import  UserCreationForm
from .forms import Customer
from django.contrib.auth.models import Group


# Create your views here.
def registerPage(request):  

    form = Customer()

    if request.method == 'POST':
        form = Customer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')          
    context = {form: 'form'}
    return render(request, 'accounts/register.html', context)


def home(request):
    context = {}
    return render(request, 'accounts/home.html' ,context)