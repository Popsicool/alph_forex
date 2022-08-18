from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import  auth
from .models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy, reverse
import os

# Create your views here.


def login(request):
    if request.method == 'POST':
        email= request.POST['email']
        first_name = request.POST['first_name']
        password = request.POST['password']
        if User.objects.filter(email=email, first_name=first_name).exists():
            user = auth.authenticate(email=email,password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('alph:index')
            else:
                messages.info(request, 'Invalid credeeeeentials')
                return redirect('authz:login')
        else:
            messages.info(request, 'Invalid credaaaantials')
            return redirect('authz:login')
    return render(request, "authz/login.html")


# ============================================
# ============================================


def logout(request):
    auth.logout(request)
    return redirect('/')


# =============================================
# =============================================


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['secondName']
        phone_num = request.POST['phoneNo']
        email = request.POST['email']
        gender= request.POST['Gender']
        password = request.POST['password']
        pass2 = request.POST['password2']
        email = email.lower()
        if password == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('authz:signup')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, 
                    password=password, phone_num = phone_num, gender=gender)
                user.save()
                messages.info(request, "Account created")
                return redirect('authz:login')
        else:
            messages.info(request, "Password didnt match")
            return redirect('authz:signup')

    return render(request, "authz/signup.html")

