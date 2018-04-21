from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'category', 'add_time', 'like_numbers', 'click_numbers']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
