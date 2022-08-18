from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'alph'
urlpatterns = [
    path("", views.index, name="index"),
    path("alph4", views.alph4, name="alph4"),
    path("about", views.about, name="about"),
    path("why", views.why, name="why"),
    path("contact", views.contact, name="contact"),
    path("legal", views.legal, name="legal"),
    path("faq", views.faq, name="faq"),
    path("testimonal", views.testimonals, name="testimonals"),
    path("platform", views.platform, name="platform"),
    path("web", views.web, name="web"),
    path("metatrader", views.metatrader, name="metatrader"),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
         ]
