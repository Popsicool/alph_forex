from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'dashboard'
urlpatterns = [
     path('', views.dashboard, name='dash'),
     path('deposit', views.deposit.as_view(), name='deposit'),
     path('withdraw', views.withdraw.as_view(), name='withdraw'),
     path('transfer', views.transfer.as_view(), name='transfer'),
     path('history', views.history.as_view(), name='history'),
         ]