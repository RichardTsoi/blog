__author__ = 'Tsoingkam'
__date__ = '2018/4/13 21:50'

from django import forms

from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'name', 'password', 'email']


class ForgetPWDForm(forms.Form):
    email = forms.CharField(required=True, max_length=255)


class ChangePWDForm(forms.Form):
    password = forms.CharField(required=True, min_length=6)
    password1 = forms.CharField(required=True, min_length=6)
    code = forms.CharField(required=True, max_length=6, min_length=6)
