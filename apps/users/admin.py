from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'birthday', 'gender']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmailVerifyCode)
