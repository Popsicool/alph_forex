from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from user_profile.models import Document
from dashboard.models import Withdraw
from authz.models import User

# Create your views here.
def index(request):
    context = {}
    return render(request, "alph/index.html", context)

class superman(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        email = user.email
        withdraw = Withdraw.objects.filter(status=False)
        document = Document.objects.filter(status=False)
        context= {"user":user,"withdraw":withdraw,"document":document}
        return render(request, "alph/super.html", context)
    def post(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "alph/super.html", context)


class superver(LoginRequiredMixin, View):
    def get(self, request, pk):
        cust= User.objects.get(email=pk)
        email = cust.email
        document = Document.objects.get(email=email)
        user = request.user
        context= {"user":user, "document":document}
        return render(request, "alph/superver.html", context)
    def post(self, request, pk):
        user = request.user
        context= {"user":user}
        return render(request, "alph/super.html", context)

class superwit(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = request.user
        withdraw = Withdraw.objects.get(ref=pk)
        context= {"user":user, "withdraw":withdraw}
        return render(request, "alph/superwit.html", context)


def alph4(request):
    return render(request, "alph/alph4.html")

def appwit(request,pk):
    Withdraw.objects.filter(ref=pk).update(status=True)
    return redirect('alph:superman')
def appwit2(request,pk):
    withdraw = Withdraw.objects.get(ref=pk)
    email= withdraw.email
    user= User.objects.get(email=email)
    balance = int(user.balance) + int(withdraw.amount)
    User.objects.filter(email=email).update(balance=balance)
    Withdraw.objects.filter(ref=pk).delete()
    return redirect('alph:superman')
def appwit3(request,pk):
    User.objects.filter(email=pk).update(is_document_verified=True)
    Document.objects.filter(email=pk).update(status=True)
    return redirect('alph:superman')
def appwit4(request,pk):
    User.objects.filter(email=pk).update(is_document_submitted=False)
    Document.objects.filter(email=pk).delete()
    return redirect('alph:superman')
    
def about(request):
    return render(request, "alph/about.html")
def why(request):
    return render(request, "alph/why.html")
def contact(request):
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
