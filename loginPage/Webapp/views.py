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
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name = 'Customer')
            user.groups.add(group)
            

    context = {form: 'form'}
    return render(request, 'accounts/register.html', context)


def home(request):
    context = {}
    return render(request, 'accounts/home.html' ,context)