from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from authz.models import User
from django.contrib import messages




class verify(LoginRequiredMixin, View):
    def post(self, request):
        amount= request.POST['amount']
        user = request.user
        context = {'user':user}
        return render(request, "user_profile/verify.html", context)

    def get(self, request):
        user = request.user
        context = {'user':user}
        return render(request, "user_profile/verify.html", context)



class change_password(LoginRequiredMixin, View):
    def post(self, request):
        amount= request.POST['amount']
        user = request.user
        context = {'user':user}
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        new_password2 = request.POST['confirm_new_password']
        if len(new_password) < 1 or len(confirm_new_password) < 1:
            messages.info(request, "Field cannot be empty")
            return redirect('user_profile:change_password')            
            if new_password == confirm_new_password:
                u = User.objects.get(email=user.email)
                u.set_password(new_password)
                u.save()
                messages.info(request, "Password updated!!")
                user = auth.authenticate(email=user.email, password=new_password)
            else:
                messages.info(request, "Password did not match!!")
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard:dash')







        return render(request, "user_profile/change_password.html", context)

    def get(self, request):
        user = request.user
        context = {'user':user}
        return render(request, "user_profile/change_password.html", context)
# Create your views here.
