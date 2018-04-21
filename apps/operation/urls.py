__author__ = 'Tsoingkam'
__date__ = '2018/4/16 10:52'

from django.conf.urls import url

from .views import CommentView, ReplyCommentView

app_name = 'operation'
urlpatterns = [
    url(r'^comment/(?P<article_id>[0-9]+)/$', CommentView.as_view(), name='user_comment'),
    url(r'^reply/comment/(?P<article_id>[0-9]+)/(?P<comment_id>[0-9]+)/$', ReplyCommentView.as_view(), name='reply_comment'),
]
