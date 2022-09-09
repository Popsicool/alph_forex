from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from user_profile.models import Document
from dashboard.models import Withdraw
from authz.models import User
from user_profile.models import Account
from dashboard.models import Payment
from .models import Contact

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dash')
    context = {}
    return render(request, "alph/index.html", context)

class superman(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        if (user.is_superuser == False):
            return render(request, "alph/404.html")
        email = user.email
        deposit = Payment.objects.filter(verified=False)
        withdraw = Withdraw.objects.filter(status=False)
        document = Document.objects.filter(status=False)
        context= {"user":user,"withdraw":withdraw,"document":document,"deposit":deposit}
        return render(request, "alph/super.html", context)
   

class superver(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = request.user
        if (user.is_superuser == False):
            return render(request, "alph/404.html")
        cust= User.objects.get(email=pk)
        email = cust.email
        document = Document.objects.get(email=email)
        user = request.user
        context= {"user":user, "document":document}
        return render(request, "alph/superver.html", context)
    

class superwit(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = request.user
        if user.is_superuser == False:
            return render(request, "alph/404.html")
        withdraw = Withdraw.objects.get(ref=pk)
        context= {"user":user, "withdraw":withdraw}
        return render(request, "alph/superwit.html", context)

class superdep(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = request.user
        if user.is_superuser == False:
            return render(request, "alph/404.html")
        payment = Payment.objects.get(ref=pk)
        context= {"user":user, "payment":payment}
        return render(request, "alph/superdep.html", context)


def alph4(request):
    return render(request, "alph/alph4.html")

def appwit(request,pk):
    user = request.user
    if (user.is_superuser == False):
        return render(request, "alph/404.html")
    Withdraw.objects.filter(ref=pk).update(status=True)
    return redirect('alph:superman')

def appdep(request,pk):
    user = request.user
    if (user.is_superuser == False):
        return render(request, "alph/404.html")
    payment = Payment.objects.get(ref=pk)
    amount = payment.amount
    user = Account.objects.get(account_number=payment.acc)
    balance = int(user.balance) + int(amount)
    Account.objects.filter(account_number=payment.acc).update(balance=balance)
    Payment.objects.filter(ref=pk).update(verified=True)
    return redirect('alph:superman')

def appdep2(request,pk):
    user = request.user
    if (user.is_superuser == False):
        return render(request, "alph/404.html")
    Payment.objects.filter(ref=pk).delete()
    return redirect('alph:superman')

def appwit2(request,pk):
    user = request.user
    if (user.is_superuser == False):
        return render(request, "alph/404.html")
    withdraw = Withdraw.objects.get(ref=pk)
    acc= withdraw.account
    user = Account.objects.get(account_number=withdraw.account)
    balance = int(user.balance) + int(withdraw.amount)
    Account.objects.filter(account_number=withdraw.account).update(balance=balance)
    Withdraw.objects.filter(ref=pk).delete()
    return redirect('alph:superman')
def appwit3(request,pk):
    user = request.user
    if (user.is_superuser == False):
        return render(request, "alph/404.html")
    User.objects.filter(email=pk).update(is_document_verified=True)
    Document.objects.filter(email=pk).update(status=True)
    return redirect('alph:superman')
def appwit4(request,pk):
    user = request.user
    if (user.is_superuser == False):
        return render(request, "alph/404.html")
    User.objects.filter(email=pk).update(is_document_submitted=False)
    Document.objects.filter(email=pk).delete()
    return redirect('alph:superman')
    
def about(request):
    return render(request, "alph/about.html")
def why(request):
    return render(request, "alph/why.html")
def contact(request):
    if request.method == "POST":
        full_name=request.POST['input_1']
        email=request.POST['input_3']
        language=request.POST['input_8']
        existing = request.POST['input_4']
        try:
            phone_num = request.POST['input_7']
        except:
            phone_num = None

        try:
            account_number = request.POST['input_6']
        except:
            account_number = None
        enquiry_type = request.POST['input_7']
        message=request.POST['message']
        contact = Contact(
            full_name=full_name, email=email,language=language,existing=existing,phone_num=phone_num,account_number=account_number,enquiry_type=enquiry_type, message=message)
        contact.save()
    return render(request, "alph/contact.html")
def legal(request):
    return render(request, "alph/legal.html")
def faq(request):
    return render(request, "alph/faq.html")
def testimonals(request):
    return render(request, "alph/testimonal.html")

def platform(request):
    return render(request, "alph/platform.html")
def web(request):
    return render(request, "alph/web.html")
def metatrader(request):
    return render(request, "alph/metatrader.html")
def metatrader(request):
    return render(request, "alph/metatrader.html")

def error_404(request,exception):
    return render(request, "alph/404.html")

def error_500(request):
    return render(request, "alph/500.html")