from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import  auth
from .models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy, reverse
import os
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_str,DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


def send_activation_email(user,request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('authz/activate.html', {
        'user':user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email= EmailMessage(subject=email_subject,body=email_body, from_email= settings.EMAIL_FROM_USER,to=[user.email])
    email.send()

def login(request):
    if request.method == 'POST':
        email= request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            user = auth.authenticate(email=email,password=password)
                

            if user is not None:
                if not user.is_email_verified:
                    messages.info(request, 'Email not  verified yet, do that before you can log in')
                    return redirect('authz:login')


                auth.login(request, user)
                return redirect('alph:index')
            else:
                messages.info(request, 'Invalid credentials')
                return redirect('authz:login')
        else:
            messages.info(request, 'Invalid credentials')
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
                user = User.objects._create_user(email, password, first_name, last_name, phone_num, gender)
                user.save()

                messages.info(request, "Account created, check your email for activation link")

                send_activation_email(user,request)


                return redirect('authz:login')
        else:
            messages.info(request, "Password didnt match")
            return redirect('authz:signup')

    return render(request, "authz/signup.html")

def activate_user(request,uidb64,token):
    
    try:
        uid= force_str(urlsafe_base64_decode(uidb64))

        user=User.objects.get(pk=uid)

    except Exception as e:
        user= None

    if user and generate_token.check_token(user,token):
        user.is_email_verified= True
        user.save()

        messages.info(request, "email verified")
        return redirect('authz:login')

    return render(request, 'authz/activation_fail.html', {'user':user})


def resend_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        user= User.objects.get(email=email)
        send_activation_email(user,request)
        messages.info(request, "email resent")
        return redirect('authz:login')
