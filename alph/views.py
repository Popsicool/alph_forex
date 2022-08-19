from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "alph/index.html", context)
def alph4(request):
    return render(request, "alph/alph4.html")
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
