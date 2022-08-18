from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'market'
urlpatterns = [
    path("forex", views.forex, name="forex"),
    path("metals", views.metals, name="metals"),
    path("indices", views.indices, name="indices"),
    path("commodities", views.commodities, name="commodities"),
    path("futures", views.futures, name="futures"),
    path("shares", views.shares, name="shares"),
    path("market", views.market_page, name="market_page"),
    path("trade", views.trade, name="trade"),
    path("account_type", views.account_type, name="account_type"),
    path("spread", views.spread, name="spread")
   
]