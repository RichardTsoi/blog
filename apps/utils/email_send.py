__author__ = 'Tsoingkam'
__date__ = '2018/4/14 15:56'

from random import Random

from django.core.mail import send_mail
from django.conf import settings

from users.models import EmailVerifyCode


def get_random_code(code_length=6):
    code = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(0, code_length):
        code += chars[random.randint(0, length)]
    return code


def send_to_email(email, send_type='register'):
    email_record = EmailVerifyCode()
    email_record.code = get_random_code()
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        title = 'Richard Tsoi博客在线注册链接'
        body = '点击链接激活账号：http://127.0.0.1:8000/user/active/{0}'.format(email_record.code)

        send_status = send_mail(title, body, settings.DEFAULT_FROM_EMAIL, [email])
        if send_status:
            pass

    if send_type == 'reset':
        title = 'Richard Tsoi博客找回密码链接'
        body = '点击链接找回密码：http://127.0.0.1:8000/user/changepwd ，验证码为{0}'.format(email_record.code)

        send_status = send_mail(title, body, settings.DEFAULT_FROM_EMAIL, [email])
        if send_status:
            pass


