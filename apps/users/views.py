from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend

from .forms import LoginForm, RegisterForm, ForgetPWDForm, ChangePWDForm
from .models import UserProfile, EmailVerifyCode
from utils.email_send import send_to_email


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        redirect_to = request.GET.get('next', '')
        return render(request, 'users/login.html', {'next': redirect_to})

    def post(self, request):
        form = LoginForm(request.POST)
        redirect_to = request.POST.get('next', '')
        if form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if redirect_to:
                        return redirect(redirect_to)
                    else:
                        return redirect('/')
                else:
                    return render(request, 'users/login.html', {'msg': '该账号未激活，请前往邮箱激活'})
            else:
                return render(request, 'users/login.html', {'msg': '账号或密码错误'})
        else:
            return render(request, 'users/login.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        redirect_to = request.GET.get('next', '')
        return render(request, 'users/register.html', {'next': redirect_to})

    def post(self, request):
        form = RegisterForm(request.POST)
        redirect_to = request.POST.get('next', '')
        if form.is_valid():
            email = request.POST.get('email', '')
            user_name = request.POST.get('username', '')
            nick_name = request.POST.get('name', '')
            if UserProfile.objects.filter(username=user_name):
                return render(request, 'users/register.html', {'msg': '该用户名已被注册，请换另一个'})
            if UserProfile.objects.filter(email=email):
                return render(request, 'users/register.html', {'msg': '该邮箱已被注册，请换另一个'})
            if UserProfile.objects.filter(name=nick_name):
                return render(request, 'users/register.html', {'msg': '该昵称已被使用，请换另一个'})
            pass_word1 = request.POST.get('password', '')
            pass_word2 = request.POST.get('password1', '')
            if pass_word1 != pass_word2:
                return render(request, 'users/register.html', {'msg': '两次输入密码不一致'})
            user = UserProfile.objects.create_user(username=user_name)
            user.email = email
            user.password = make_password(pass_word2)
            user.is_active = False
            user.name = nick_name
            user.save()

            send_to_email(email, 'register')

            if redirect_to:
                return redirect(redirect_to)
            return redirect('/')
        return render(request, 'users/register.html', {'form': form})


class ActiveView(View):
    def get(self, request, active_code):
        email_record = EmailVerifyCode.objects.filter(code=active_code)
        if email_record:
            for record in email_record:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'users/active_failed.html')
        return render(request, 'users/login.html')


class ForgetPWDView(View):
    def get(self, request):
        return render(request, 'users/forgetpwd.html')

    def post(self, request):
        form = ForgetPWDForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(email=email):
                send_to_email(email, 'reset')
                return render(request, 'users/send_email_success.html')
            return render(request, 'users/forgetpwd.html', {'msg': '该邮箱未被注册过'})
        return render(request, 'users/forgetpwd.html', {'msg': '邮箱填写错误'})


class ChangePWDView(View):
    def get(self, request):
        return render(request, 'users/reset_password.html')

    def post(self, request):
        form = ChangePWDForm(request.POST)
        if form.is_valid():
            password = request.POST.get('password', '')
            password1 = request.POST.get('password1', '')
            verify_code = request.POST.get('code', '')
            if password == password1:
                records = EmailVerifyCode.objects.filter(code=verify_code)
                if records:
                    for record in records:
                        email = record.email
                        user = UserProfile.objects.get(email=email)
                        user.password = make_password(password)
                        user.save()
                        return render(request, 'users/login.html')
            return render(request, 'users/reset_password.html', {'msg': '两次输入密码不一致'})
        return render(request, 'users/reset_password.html', {'msg': '密码或验证码输入错误'})
