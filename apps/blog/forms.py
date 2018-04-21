__author__ = 'Tsoingkam'
__date__ = '2018/4/16 18:19'

from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True, max_length=255)
    subject = forms.CharField(required=True, max_length=100)
    text = forms.Textarea()
