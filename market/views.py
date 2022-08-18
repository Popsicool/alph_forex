from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def market_page(request):
    return render(request, "market/market.html")
def forex(request):
    return render(request, "market/forex.html")

def metals(request):
    return render(request, "market/metals.html")

def indices(request):
    return render(request, "market/indices.html")

def commodities(request):
    return render(request, "market/commodities.html")

def futures(request):
    return render(request, "market/futures.html")

def shares(request):
    return render(request, "market/shares.html")
def trade(request):
    return render(request, "market/trade.html")
def account_type(request):
    return render(request, "market/account_type.html")
def spread(request):
    return render(request, "market/spread.html")