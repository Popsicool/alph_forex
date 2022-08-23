from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'dashboard'
urlpatterns = [
     path('', views.dashboard, name='dash'),
     path('deposit', views.deposit.as_view(), name='deposit'),
     path('withdraw', views.withdraw.as_view(), name='withdraw'),
     path('banktransfer', views.banktransfer.as_view(), name='banktransfer'),
     path('creditcard', views.creditcard.as_view(), name='creditcard'),
     path('banktransferwitdrw', views.banktransferwitdrw.as_view(), name='banktransferwitdrw'),
     path('banktransferwithdraw', views.banktransferwithdraw.as_view(), name='banktransferwithdraw'),
     path('transfer', views.transfer.as_view(), name='transfer'),
     path('creditcard', views.creditcard.as_view(), name='creditcard'),
     path('history', views.history.as_view(), name='history'),
         ]