from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('amount',)
