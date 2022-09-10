from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from authz.models import User
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from .forms  import PaymentForm
from django.conf import settings
import secrets
from .models import Payment, Withdraw, Transfer
import random
import os

from io import BytesIO
import sys
sys.stdout.reconfigure(encoding='utf-8')
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
# from django.http import StreamingHttpResponse
# from WSGIREF.UTIL import FileWrapper
# import mimetypes
from user_profile.models import Document, Account
# Create your views here.

def generateReferenceNumber():
    return random.randrange(1111111111, 9999999999)
class dashboard(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        accounts = Account.objects.filter(user=user)
        context={"accounts":accounts}
        return render(request, "dashboard/dashboard.html",context)
    def post(self,request,response):
        user = request.user
        resp = response.reference
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
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/withdraw.html", context)
    def get(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/withdraw.html", context)


class banktransferwitdrw(LoginRequiredMixin, View):
    def post(self, request):
        amount= request.POST['amount']
        account= request.POST['acc']
        beneficiary_fullname= request.POST['beneficiary_fullname']
        beneficiary_address= request.POST['beneficiary_address']
        beneficiary_city= request.POST['beneficiary_city']
        beneficiary_zip= request.POST['beneficiary_zip']
        beneficiary_country= request.POST['beneficiary_country']
        bank_account= request.POST['bank_account']
        bank_name= request.POST['bank_name']
        branch_code= request.POST['branch_code']
        bank_address= request.POST['bank_address']
        beneficiary_swift= request.POST['beneficiary_swift']
        bic= request.POST['bic']
        notes= request.POST['notes']
        user = request.user
        email = user.email
        balance = Account.objects.get(account_number=account).balance
        context = {"user":user}
        try:
            amount = int(amount)
        except:
            messages.info(request, 'Enter Integer amount only')
            return render(request, "dashboard/banktransferwitdrw.html", context)
        if (int(amount) > int(balance) ):
            messages.info(request, 'Insufficient fund')
            return render(request, "dashboard/banktransferwitdrw.html", context)
        ref = 0
        while (ref == 0):
            ref2 = generateReferenceNumber()
            object_with_similar_ref = Withdraw.objects.filter(ref=ref2)
            if not object_with_similar_ref:
                ref = ref2

        money= Withdraw.objects.create(amount=amount,account=account, ref=ref,email=email,beneficiary_fullname=beneficiary_fullname,
        beneficiary_address=beneficiary_address,beneficiary_city=beneficiary_city, beneficiary_zip=beneficiary_zip,
        beneficiary_country=beneficiary_country,bank_account=bank_account,bank_name=bank_name,branch_code=branch_code,
        bank_address=bank_address,beneficiary_swift=beneficiary_swift,bic=bic, notes=notes)
        money.save()
        balance = Account.objects.get(account_number=account).balance
        balance = int(balance) - int(amount)
        Account.objects.filter(account_number=account).update(balance=balance)        
        messages.info(request, 'Withrawal request Submitted')
        return redirect("dashboard:dash")
        
        
    def get(self, request):
        user = request.user
        accounts = Account.objects.filter(user=user.id)
        context = {"user":user, "accounts":accounts}
        return render(request, "dashboard/banktransferwitdrw.html", context)

class banktransfer(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        accounts = Account.objects.filter(user=user.id)
        context = {"user":user, "accounts":accounts}
        return render(request, "dashboard/banktransfer.html", context)
    def post(self, request):
        user = request.user
        accounts = Account.objects.filter(user=user.id)
        context = {"user":user, "accounts":accounts}
        email = user.email
        amount = request.POST['amount']
        acc = request.POST['account']
        currency = request.POST['currency']
        preferred_bank = request.POST['bank']
        bank_name= request.POST['bank_name']

        ref = 0
        while (ref == 0):
            ref2 = generateReferenceNumber()
            object_with_similar_ref = Payment.objects.filter(ref=ref2)
            if not object_with_similar_ref:
                ref = ref2

        money= Payment.objects.create(acc=acc,amount=amount,email=email,ref=ref, currency=currency,
        preferred_bank=preferred_bank,bank_name=bank_name)
        
        money.save()




        return redirect("dashboard:downloadfile", ref)

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
        deposit = Payment.objects.filter(email=email)
        withdraw = Withdraw.objects.filter(email=email)
        transfer = Transfer.objects.filter(user=user)
        context= {"user":user, "deposit":deposit, "withdraw":withdraw, "transfer":transfer}
        return render(request, "dashboard/history.html", context)



class banktransferwithdraw(LoginRequiredMixin, View):
    def post(self, request):
        amount= request.POST['amount']
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
        accounts = Account.objects.filter(user=user.id)
        context= {"user":user,"accounts":accounts}
        return render(request, "dashboard/internaltransfer.html", context)
    def post(self, request):
        user = request.user
        accounts = Account.objects.filter(user=user.id)
        accountFrom = request.POST['accountFrom']
        accountTo = request.POST['accountTo']
        amount = request.POST['amount']
        if (accountFrom == accountTo):
            messages.info(request, "Can't transfer to same account")
            return redirect("dashboard:internal_transfer")
        try:
            amount = int(amount)
        except:
            messages.info(request, 'Amount must be Number only')
            return redirect("dashboard:internal_transfer")
        if (amount <= 0):
            messages.info(request, 'Amount must be greater than zero')
            return redirect("dashboard:internal_transfer")

        ref = 0
        while (ref == 0):
            ref2 = generateReferenceNumber()
            object_with_similar_ref = Transfer.objects.filter(ref=ref2)
            if not object_with_similar_ref:
                ref = ref2

        if (accountFrom == "Base Account"):
            account1 = User.objects.get(email=user.email).balance
        else:
            account1= Account.objects.get(account_number=accountFrom).balance
            print(account1)
        if (accountTo == "Base Account"):
            account2 = User.objects.get(email=user.email).balance
        else:
            account2= Account.objects.get(account_number=accountTo).balance
            print(account2)

        if (amount > int(account1)):
            messages.info(request, 'Insufficient fund in the selected account')
            return redirect("dashboard:internal_transfer")
        else:
            balance1 = account1 - amount
            balance2 = account2 + amount

        if (accountFrom == "Base Account"):
            User.objects.filter(email=user.email).update(balance=balance1)
        else:
            Account.objects.filter(account_number=accountFrom).update(balance=balance1)

        if (accountTo == "Base Account"):
            User.objects.filter(email=user.email).update(balance=balance2)
        else:
            Account.objects.filter(account_number=accountTo).update(balance=balance2)
            
        transfer = Transfer.objects.create(user=user,amount=amount,sent_from=accountFrom,sent_to=accountTo, ref=ref)
        transfer.save()
        messages.info(request, 'Transfer Succcessful')
        return redirect("dashboard:dash")
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
    def post(self, request):
        user = request.user
        context= {"user":user}
        return render(request, "dashboard/top-trader-comp.html", context)

class trading_report(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        accounts = Account.objects.filter(user=user.id)
        context= {"user":user, "accounts":accounts}
        return render(request, "dashboard/tradingreport.html", context)
    def get(self, request):
        user = request.user
        accounts = Account.objects.filter(user=user.id)
        context= {"user":user, "accounts":accounts}
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
        amount = request.POST['amount']
        acc = request.POST['acc']
        try:
            amount = int(amount)
        except:
            messages.info(request, 'Amount in integers only')
            return render (request, 'dashboard/initiate_payment.html')

        user = request.user
        email= user.email
        accounts = Account.objects.filter(user=user.id)
        ref = 0
        while (ref == 0):
            ref2 = generateReferenceNumber()
            object_with_similar_ref = Payment.objects.filter(ref=ref2)
            if not object_with_similar_ref:
                ref = ref2

        money= Payment.objects.create(acc=acc,amount=amount,email=email,ref=ref)
        
        money.save()
        
        payment = {"amount":amount, "email":email, "ref":ref, "acc":acc}
        context = {"payment":payment, 'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY, "accounts":accounts}
        return render(request, 'dashboard/make_payment.html', context)

    # else:
    #     payment_form = PaymentForm
    user = request.user
    accounts = Account.objects.filter(user=user.id)
    context= {"accounts":accounts, "user":user}
    return render (request, 'dashboard/initiate_payment.html', context)

def verify_payment(request:HttpRequest, ref:str) -> HttpResponse:
    user = request.user
    Payment.objects.filter(ref=ref).update(verified=True)
    email = user.email
    data = Payment.objects.get(ref=ref, email=email)
    acc = data.acc
    account = Account.objects.get(account_number= acc)
    balance = int(account.balance) + data.amount
    Account.objects.filter(account_number=acc).update(balance=balance)
    messages.info(request, 'Deposit succesfull')
    context = {"user":user}
    return redirect("dashboard:dash")

def cancel_withrawal(request, pk):
    user = request.user
    person= Withdraw.objects.get(ref=pk,email=user.email)
    amount = person.amount
    balance = Account.objects.get(account_number=person.account).balance
    balance = int(balance) + int(amount)
    Account.objects.filter(account_number=person.account, user=user).update(balance=balance) 
    Withdraw.objects.filter(ref=pk).delete()
    messages.info(request, ' Withdrawal Request Cancelled')
    return redirect("dashboard:dash")

def cancel_deposit(request, pk):
    user = request.user
    Payment.objects.filter(ref=pk, email= user.email).delete()
    messages.info(request, 'Deposit Request Cancelled')
    return redirect("dashboard:dash")


def downloadfile(request, pk):
    user = request.user
    accounts = Account.objects.filter(user=user.id)
    pk = pk
    context= {"accounts":accounts, "user":user, "pk":pk}

    template_src = "dashboard/teller.html"
    try:
        dep = Payment.objects.get(ref=pk, email = request.user.email)
    except:
        return render(request, "alph/404.html")
    data = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email':user.email,
        'bank': dep.bank_name,
        'ref': dep.ref,
        'amount': dep.amount,
        'currency': dep.currency,
        }

    template= get_template(template_src)
    html = template.render(data)
    result = BytesIO()
    # pdf = pisa.pisaDocument(BytesIO(urlsafe_base64_encode(force_bytes(html))), result)
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:

        email_subject = 'Bank Transfer Instruction'
        first_name = user.first_name
        last_name= user.last_name
        email_body = render_to_string('dashboard/teller_email.html', {
            'first_name': first_name,
            'last_name': last_name,
            })
        rece = user.email
        filename = 'Bank_Transfer_Request.pdf'
        some=result.getvalue()
        email= EmailMessage(subject=email_subject,body=email_body, from_email= settings.EMAIL_FROM_USER,to=[rece])
        email.attach(filename, some,'application/pdf')
        # email.send(fail_silently=True)



    return render (request, 'dashboard/downloadfile.html', context)

def down(request, pk):
    with open(str(os.path.join(settings.BASE_DIR)+"/media/Bank_Transfer_Request.pdf"), 'rb') as f:
        data= f.read()
    response = HttpResponse(data, content_type='text/pdf')
    response['Content-Disposition'] = 'attachment; filename="Bank_Transfer_Request.pdf"'
    return response




def render_to_pdf(template_src, context_dic={}):
    template= get_template(template_src)
    html = template.render(context_dic)
    result = BytesIO()
    # pdf = pisa.pisaDocument(BytesIO(urlsafe_base64_encode(force_bytes(html))), result)
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:

        # email_subject = 'Bank Transfer Instruction'
        # first_name = context_dic['first_name']
        # last_name= context_dic['last_name']
        # email_body = render_to_string('dashboard/teller_email.html', {
        #     'first_name': first_name,
        #     'last_name': last_name,
        #     })
        # rece = context_dic['email']
        # filename = 'Bank_Transfer_Request.pdf'
        # some=result.getvalue()
        # email= EmailMessage(subject=email_subject,body=email_body, from_email= settings.EMAIL_FROM_USER,to=[rece])
        # email.attach(filename, some,'application/pdf')
        # email.send(fail_silently=False)
        return  HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
class GenerateTeller(View):
    def get (self, request, pk):
        try:
            dep = Payment.objects.get(ref=pk, email = request.user.email)
        except:
            return render(request, "alph/404.html")
        user = request.user
        data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email':user.email,
            'bank': dep.bank_name,
            'ref': dep.ref,
            'amount': dep.amount,
            'currency': dep.currency,
        }
        pdf = render_to_pdf("dashboard/teller.html", data)

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = 'Bank_Transfer_Request.pdf'
            content = "inline; filename='%s'" %(filename)
            content = "attachment; filename = %s" %(filename)
            response['content-Disposition'] = content




            # email_subject = 'Bank Transfer Instruction'
            # email_body = render_to_string('dashboard/teller_email.html', {
            #     'first_name': user.first_name,
            #     'last_name': user.last_name,
            #     })
            
            # filename = 'Bank_Transfer_Request.pdf'
            # email= EmailMessage(subject=email_subject,body=email_body, from_email= settings.EMAIL_FROM_USER,to=[user.email])
            # email.attach(filename, content,'application/pdf')
            # email.send()
       
        
            return response
        return HttpResponse("Not found")


