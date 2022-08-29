from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from authz.models import User
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from .forms  import PaymentForm
from django.conf import settings
import secrets
from .models import Payment
import random
# Create your views here.

def generateReferenceNumber():
    return random.randrange(1111111111, 9999999999)
class dashboard(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        balance = int(user.balance)
        context={'balance':balance}
        return render(request, "dashboard/dashboard.html",context)
    def post(self,request,response):
        user = request.user
        resp = response.reference
        print(type(resp))
        balance = int(user.balance)
        context={'balance':balance}
        return render(request, "dashboard/dashboard.html",context)


    
class deposit(LoginRequiredMixin, View):
    def post(self, request):
        amount= request.POST['amount']
        user = request.user
        balance = int(user.balance) + int(amount)
        id = user.id
        User.objects.filter(id=id).update(balance=balance)
        messages.info(request, 'Deposit succesfull')
        return render(request, "dashboard/dashboard.html")

    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/deposit.html", context)


class withdraw(LoginRequiredMixin, View):
    def post(self, request):
        amount= request.POST['amount']
        user = request.user
        context = {}
        id = user.id
        if int(user.balance) < int(amount):
            messages.info(request, 'Insufficient fund')
            return render(request, "dashboard/withdraw.html", context)
        else:
            balance = int(user.balance) - int(amount)
            User.objects.filter(id=id).update(balance=balance)
            messages.info(request, 'Withdrawal succesfull')
            return render(request, "dashboard/dashboard.html")
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/withdraw.html", context)


class banktransferwitdrw(LoginRequiredMixin, View):
    def post(self, request):
        amount= request.POST['amount']
        user = request.user
        context = {}
        if (user.is_document_verified == False):
            messages.info(request, 'Account not yet verified, withdrawal can not  be processed ')
            return render(request, "dashboard/banktransferwitdrw.html", context)
        id = user.id
        if int(user.balance) < int(amount):
            messages.info(request, 'Insufficient fund')
            return render(request, "dashboard/banktransferwitdrw.html", context)
        else:
            balance = int(user.balance) - int(amount)
            User.objects.filter(id=id).update(balance=balance)
            messages.info(request, 'Withdrawal succesfull', context)
            return render(request, "dashboard/dash", context)
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/banktransferwitdrw.html", context)

class banktransfer(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/banktransfer.html", context)

class creditcard(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/creditcard.html.html", context)
    def post(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/creditcard.html.html", context)



class transfer(LoginRequiredMixin, View):
    def post(self, request):
        recepient = request.POST['recepient']
        amount= request.POST['amount']
        user = request.user
        context = {}
        id = user.id
        if int(user.balance) < int(amount):
            messages.info(request, 'Insufficient fund')
            return render(request, "dashboard/banktransfer.html", context)
        else:
            if User.objects.filter(email=recepient).exists():
                balance = int(user.balance) - int(amount)
                User.objects.filter(id=id).update(balance=balance)
                receiver = User.objects.get(email=recepient)
                receiver_balance = int(receiver.balance) + int(amount)
                User.objects.filter(email=recepient).update(balance=receiver_balance)
                messages.info(request, 'Transfer succesfull')
                return render(request, "dashboard/dashboard.html", context)

            else:
                messages.info(request, 'user does not exit')


        return render(request, "dashboard/banktransfer.html", context)
    def get(self, request):
        return render(request, "dashboard/banktransfer.html")

class history(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        email = user.email
        data = Payment.objects.all()
        context= {"user":user, "data":data}
        print(data)
        return render(request, "dashboard/history.html", context)



class banktransferwithdraw(LoginRequiredMixin, View):
    def post(self, request):
        amount= request.POST['amount']
        user = request.user
        
        user = request.user
        context= {"user":user}
        id = user.id
        if int(user.balance) < int(amount):
            messages.info(request, 'Insufficient fund')
            return render(request, "dashboard/banktransferwithdraw.html", context)
        else:
            balance = int(user.balance) - int(amount)
            User.objects.filter(id=id).update(balance=balance)
            messages.info(request, 'Withdrawal succesfull')
            return render(request, "dashboard/dashboard.html")
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/banktransferwithdraw.html", context)


class creditcard(LoginRequiredMixin, View):
    def post(self, request):
        amount= request.POST['amount']
        user = request.user
        user = request.user
        context= {"user":user}
        id = user.id
        if int(user.balance) < int(amount):
            messages.info(request, 'Insufficient fund')
            return render(request, "dashboard/creditcard.html", context)
        else:
            balance = int(user.balance) - int(amount)
            User.objects.filter(id=id).update(balance=balance)
            messages.info(request, 'Withdrawal succesfull')
            return render(request, "dashboard/creditcard.html", context)
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/creditcard.html", context)

class bonus(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/bonus.html", context)

class ib_assignment(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/ib-assignment.html", context)

    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/ib-assignment.html", context)

class internal_transfer(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/internaltransfer.html", context)
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/internaltransfer.html", context)

class premium_normal(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/premium-normal.html", context)
    def post(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/premium-normal.html", context)

class request_overview(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/requestoverview.html", context)

class swap_free(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/swapfree.html", context)
    def post(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/swapfree.html", context)

class top_trader_comp(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/top-trader-comp.html", context)

class trading_report(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/tradingreport.html", context)
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/tradingreport.html", context)
    
class trading_platform(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/tradingplatform.html", context)

class test(LoginRequiredMixin, View):
    def get(self, request,pk):
        user = request.user
        balance = int(user.balance)
        context={'balance':balance}
        resp = pk
        print('a')
        print(type(resp))
        print(pk)
        print('b')
        return render(request, "dashboard/test.html",context)
    def post(self,request,response):
        user = request.user
        resp = response.reference
        print(type(resp))
        balance = int(user.balance)
        context={'balance':balance}
        return render(request, "dashboard/test.html",context)



def initiate_payment(request:HttpRequest):
    if request.method == "POST":
        # payment_form = PaymentForm(request.POST)
        # if payment_form.is_valid():
        #     payment = payment_form.save()
        #     render(request, 'dashboard/make_payment.html', {"payment":payment})
        amount = request.POST['amount']
        try:
            amount = int(amount)
        except:
            messages.info(request, 'Amount in integers only')
            return render (request, 'dashboard/initiate_payment.html')

        user = request.user
        email= user.email
        ref = 0
        while (ref == 0):
            ref2 = generateReferenceNumber()
            object_with_similar_ref = Payment.objects.filter(ref=ref2)
            if not object_with_similar_ref:
                ref = ref2

        money= Payment.objects.create(amount=amount,email=email,ref=ref)
        
        money.save()
        
        payment = {"amount":amount, "email":email, "ref":ref}
        context = {"payment":payment, 'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY}
        return render(request, 'dashboard/make_payment.html', context)

    # else:
    #     payment_form = PaymentForm
    return render (request, 'dashboard/initiate_payment.html')

def verify_payment(request:HttpRequest, ref:str) -> HttpResponse:
    user = request.user
    Payment.objects.filter(ref=ref).update(verified=True)
    email = user.email
    data = Payment.objects.get(ref=ref, email=email)
    balance = int(user.balance)
    balance = int(data.amount) + balance
    User.objects.filter(email=user.email).update(balance=balance)
    messages.info(request, 'Deposit succesfull')
    context = {"user":user}
    return redirect("dashboard:dash")