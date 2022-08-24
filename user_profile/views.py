from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import check_password
from django.views import View
from authz.models import User
from django.contrib.auth.models import  auth
from django.contrib import messages




class verify(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        nationality = request.POST['nationality']
        gender = request.POST['gender']
        dob_dd = request.POST['dob_dd']
        tin = request.POST['tin']
        tax_country = request.POST['tax_country']

        address1 = request.POST['address1']
        address2 = request.POST['address2']
        town = request.POST['town']
        postcode = request.POST['postcode']
        country = request.POST['country']

        phone_landline = request.POST['phone_landline']
        phone_mobile = request.POST['phone_mobile']
        employment_status = request.POST['employment_status']
        business_nature = request.POST['business_nature']
        funds_source = request.POST['funds_source']
        expected_deposit_id = request.POST['expected_deposit_id']
        annual_income = request.POST['annual_income']
        net_worth = request.POST['net_worth']
        traded_forex = request.POST['traded_forex']
        traded_forex_frequency = request.POST['traded_forex_frequency']
        traded_forex_volume = request.POST['traded_forex_volume']
        traded_bonds_frequency = request.POST['traded_bonds_frequency']
        traded_bonds_volume = request.POST['traded_bonds_volume']
        traded_products_frequency = request.POST['traded_products_frequency']
        traded_products_volume = request.POST['traded_products_volume']
        seminar_experience = request.POST['seminar_experience']
        seminar_course_experience = request.POST['seminar_course_experience']

        work_experiencework_experience = request.POST['work_experience']
        work_qualification_experience = request.POST['work_qualification_experience']
        messages.info(request, "Ok")
        context = {'user':user}
        return render(request, "user_profile/verify.html", context)

    def get(self, request):
        user = request.user
        context = {'user':user}
        return render(request, "user_profile/verify.html", context)



class change_password(LoginRequiredMixin, View):
    login_url = 'authz:login'
    REDIRECT_FIELD_NAME = 'next'
    def post(self, request):
        user = request.user
        context = {'user':user}
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        new_password2 = request.POST['confirm_new_password']
        print(user.password)
        matchcheck =  check_password(old_password, user.password)
        if (matchcheck == False):
            messages.info(request, "Incorrect old password")
            return render(request, "user_profile/change_password.html", context)
        if len(new_password) < 1 or len(new_password2) < 1 or len(old_password) < 1 :
            messages.info(request, "Field cannot be empty")
            return render(request, "user_profile/change_password.html", context)         
        if new_password == new_password2:
            u = User.objects.get(email=user.email)
            u.set_password(new_password)
            u.save()
            messages.info(request, "Password updated!!")
            user = auth.authenticate(email=user.email, password=new_password)
            if user is not None:
                auth.login(request, user)
                return render(request,'user_profile/change_password.html', context)
        else:
            messages.info(request, "Password did not match!!")
            return render(request, "user_profile/change_password.html", context)
        






        return render(request, "user_profile/change_password.html", context)

    def get(self, request):
        user = request.user
        context = {'user':user}
        return render(request, "user_profile/change_password.html", context)
# Create your views here.



class documents(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "user_profile/documents.html", context)
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "user_profile/documents.html", context)

class newaccount(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "user_profile/newaccount.html", context)
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "user_profile/newaccount.html", context)
