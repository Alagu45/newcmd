from django.shortcuts import render
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
    return render(request,"myapp/home.html")


def login(request):
    return render(request,"myapp/login.html")


def regsiter(request):
    form=CreateUserForm()
    return render(request,"myapp/reg.html",{'form':form})
