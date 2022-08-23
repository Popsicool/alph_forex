from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from authz.models import User
from django.contrib import messages
# Create your views here.

def dashboard(request):
    user = request.user
    balance = int(user.balance)
    context={'balance':balance}
    return render(request, "dashboard/dashboard.html",context)



    
class deposit(LoginRequiredMixin, View):
    def post(self, request):
        amount= request.POST['amount']
        owner = request.user
        balance = int(owner.balance) + int(amount)
        id = owner.id
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
        id = owner.id
        if int(owner.balance) < int(amount):
            messages.info(request, 'Insufficient fund')
            return render(request, "dashboard/withdraw.html", context)
        else:
            balance = int(owner.balance) - int(amount)
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
        id = owner.id
        if int(owner.balance) < int(amount):
            messages.info(request, 'Insufficient fund')
            return render(request, "dashboard/banktransferwitdrw.html", context)
        else:
            balance = int(owner.balance) - int(amount)
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


class transfer(LoginRequiredMixin, View):
    def post(self, request):
        recepient = request.POST['recepient']
        amount= request.POST['amount']
        owner = request.user
        context = {}
        id = owner.id
        if int(owner.balance) < int(amount):
            messages.info(request, 'Insufficient fund')
            return render(request, "dashboard/banktransfer.html", context)
        else:
            if User.objects.filter(email=recepient).exists():
                balance = int(owner.balance) - int(amount)
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
    def post(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/history.html", context)
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/history.html", context)



class banktransferwithdraw(LoginRequiredMixin, View):
    def post(self, request):
        amount= request.POST['amount']
        owner = request.user
        
        user = request.user
        context= {"user":user}
        id = owner.id
        if int(owner.balance) < int(amount):
            messages.info(request, 'Insufficient fund')
            return render(request, "dashboard/banktransferwithdraw.html", context)
        else:
            balance = int(owner.balance) - int(amount)
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
        owner = request.user
        user = request.user
        context= {"user":user}
        id = owner.id
        if int(owner.balance) < int(amount):
            messages.info(request, 'Insufficient fund')
            return render(request, "dashboard/creditcard.html", context)
        else:
            balance = int(owner.balance) - int(amount)
            User.objects.filter(id=id).update(balance=balance)
            messages.info(request, 'Withdrawal succesfull')
            return render(request, "dashboard/creditcard.html", context)
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/creditcard.html", context)
