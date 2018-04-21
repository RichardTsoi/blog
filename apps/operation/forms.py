__author__ = 'Tsoingkam'
__date__ = '2018/4/16 10:44'

from django import forms

from .models import UserComment, ReplyComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ['comment']


class ReplyCommentForm(forms.ModelForm):
    class Meta:
        model = ReplyComment
        fields = ['text']
