__author__ = 'Tsoingkam'
__date__ = '2018/4/13 21:52'

from django.conf.urls import url

from .views import LoginView, RegisterView, ActiveView, ForgetPWDView, ChangePWDView

app_name = 'users'
urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<active_code>.*)$', ActiveView.as_view(), name='active'),
    url(r'^forget/$', ForgetPWDView.as_view(), name='forget_pwd'),
    url(r'^changepwd/$', ChangePWDView.as_view(), name='change_pwd'),
]
