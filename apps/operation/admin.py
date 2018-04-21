from django.contrib import admin

from .models import *


class UserCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'comment']


admin.site.register(UserComment, UserCommentAdmin)
admin.site.register(UserLike)
