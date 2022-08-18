from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'authz'
urlpatterns = [
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("signup", views.signup, name="signup"),
   
]