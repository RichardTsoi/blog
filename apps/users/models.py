from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    name = models.CharField(max_length=20, verbose_name='昵称')
    birthday = models.DateTimeField(null=True, blank=True, verbose_name='生日')
    image = models.ImageField(upload_to='media/users/image', default='css/img/default.jpg', max_length=100,
                              verbose_name='用户头像')
    email = models.EmailField(max_length=255, verbose_name='用户邮箱')
    gender = models.CharField(default='male', choices=(('male', '男'), ('female', '女')), max_length=6, verbose_name='性别')

    class Meta(AbstractUser.Meta):
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=6, verbose_name='验证码')
    email = models.CharField(max_length=255, default='', verbose_name='邮箱')
    send_type = models.CharField(max_length=10, choices=(('register', '注册'), ('reset', '重置密码')), verbose_name='发送类型',
                                 default='register')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
