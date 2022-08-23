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
        old_password = request.POST['pass1']
        new_password = request.POST['pass2']
        new_password2 = request.POST['pass2']
            if len(password1) < 1 or len(password2) < 1:
                messages.info(request, "Field cannot be empty")
                return redirect('metadata:profile', pk=pk)
            if password1 == password2:
                u = User.objects.get(username=username)
                u.set_password(password1)
                u.save()
                messages.info(request, "Password updated!!")
                user = auth.authenticate(username=username, password=password1)
                if user is not None:
                    auth.login(request, user)
                    return redirect('metadata:profile', pk=pk)







        return render(request, "user_profile/change_password.html", context)

    def get(self, request):
        user = request.user
        context = {'user':user}
        return render(request, "user_profile/change_password.html", context)
# Create your views here.
