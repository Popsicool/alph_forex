from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile


class FileUpload(forms.Form):
    upload_file = forms.FileField()
