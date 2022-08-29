from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'dashboard'
urlpatterns = [
     path('', views.dashboard.as_view(), name='dash'),
     path('deposit', views.deposit.as_view(), name='deposit'),
     path('withdraw', views.withdraw.as_view(), name='withdraw'),
     path('banktransfer', views.banktransfer.as_view(), name='banktransfer'),
     path('creditcard', views.creditcard.as_view(), name='creditcard'),
     path('banktransferwitdrw', views.banktransferwitdrw.as_view(), name='banktransferwitdrw'),
     path('banktransferwithdraw', views.banktransferwithdraw.as_view(), name='banktransferwithdraw'),
     path('transfer', views.transfer.as_view(), name='transfer'),
     path('creditcard', views.creditcard.as_view(), name='creditcard'),
     path('history', views.history.as_view(), name='history'),
     path('bonus', views.bonus.as_view(), name='bonus'),
     path('ib_assignment', views.ib_assignment.as_view(), name='ib_assignment'),
     path('internal_transfer', views.internal_transfer.as_view(), name='internal_transfer'),
     path('premium_normal', views.premium_normal.as_view(), name='premium_normal'),
     path('request_overview', views.request_overview.as_view(), name='request_overview'),
     path('swap_free', views.swap_free.as_view(), name='swap_free'),
     path('top_trader_comp', views.top_trader_comp.as_view(), name='top_trader_comp'),
     path('trading_report', views.trading_report.as_view(), name='trading_report'),
     path('trading_platform', views.trading_platform.as_view(), name='trading_platform'),
     path('test/<str:pk>', views.test.as_view(), name='test'),
     path('initiate_payment', views.initiate_payment, name='initiate_payment'),
     path('<str:ref>', views.verify_payment, name='verify_payment'),
         ]