from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'alph'
urlpatterns = [
    path("", views.index, name="index"),
    path("superman", views.superman.as_view(), name="superman"),
    path("alph4", views.alph4, name="alph4"),
    path("about", views.about, name="about"),
    path("why", views.why, name="why"),
    path("contact", views.contact, name="contact"),
    path("legal", views.legal, name="legal"),
    path("faq", views.faq, name="faq"),
    path("superver/<str:pk>", views.superver.as_view(), name="superver"),
    path("superwit/<str:pk>", views.superwit.as_view(), name="superwit"),
    path("testimonal", views.testimonals, name="testimonals"),
    path("platform", views.platform, name="platform"),
    path("web", views.web, name="web"),
    path("appwit/<str:pk>", views.appwit, name="appwit"),
    path("appwit2/<str:pk>", views.appwit2, name="appwit2"),
    path("appwit3/<str:pk>", views.appwit3, name="appwit3"),
    path("appwit4/<str:pk>", views.appwit4, name="appwit4"),
    path("metatrader", views.metatrader, name="metatrader"),
    
         ]
