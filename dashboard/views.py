from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from authz.models import User
from django.contrib import messages
# Create your views here.

def dashboard(request):
    owner = request.user
    balance = int(owner.balance)
    context={ 'balance':balance}
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

        return render(request, "dashboard/deposit.html")


class withdraw(LoginRequiredMixin, View):
    def post(self, request):
        amount= request.POST['amount']
        owner = request.user

        id = owner.id
        if int(owner.balance) < int(amount):
            messages.info(request, 'Insufficient fund')
            return render(request, "dashboard/withdraw.html")
        else:
            balance = int(owner.balance) - int(amount)
            User.objects.filter(id=id).update(balance=balance)
            messages.info(request, 'Withdrawal succesfull')
            return render(request, "dashboard/dashboard.html")
    def get(self, request):
        return render(request, "dashboard/withdraw.html")

class transfer(LoginRequiredMixin, View):
    def post(self, request):
        recepient = request.POST['recepient']
        amount= request.POST['amount']
        owner = request.user

        id = owner.id
        if int(owner.balance) < int(amount):
            messages.info(request, 'Insufficient fund')
            return render(request, "dashboard/transfer.html")
        else:
            if User.objects.filter(email=recepient).exists():
                balance = int(owner.balance) - int(amount)
                User.objects.filter(id=id).update(balance=balance)
                receiver = User.objects.get(email=recepient)
                receiver_balance = int(receiver.balance) + int(amount)
                User.objects.filter(email=recepient).update(balance=receiver_balance)
                messages.info(request, 'Transfer succesfull')
                return render(request, "dashboard/dashboard.html")

            else:
                messages.info(request, 'user does not exit')


        return render(request, "dashboard/transfer.html")
    def get(self, request):
        return render(request, "dashboard/transfer.html")

class history(LoginRequiredMixin, View):
    def post(self, request):

        return render(request, "dashboard/history.html")
    def get(self, request):
        return render(request, "dashboard/history.html")