
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

# Create your views here.


def login(request):
    return render(request, 'login.html',)


def verify_user(request):
    username = request.POST['username']
    password = request.POST['password']
    # ruturns none if not valid, the user object if valid
    valid_user = auth.authenticate(
        request, username=username, password=password)
    if valid_user is not None:
        auth.login(request, valid_user)
        return redirect('/')
    else:
        return redirect('/register/login/')


def register(request):
    return render(request, 'register.html')


def create_user(request):
    username = request.POST['username']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    if confirm_password == password and not(User.objects.filter(username=username).exists()):
        User.objects.create_user(username=username, password=password).save()
        return redirect('/register/login/')
    else:
        return redirect('/register/')
