__author__ = 'Tsoingkam'
__date__ = '2018/4/13 21:02'

from django import template
from blog.models import *


register = template.Library()


@register.simple_tag
def get_category():
    return Category.objects.all()


@register.simple_tag
def get_recent_articles():
    return Article.objects.all().order_by('-add_time')[:5]


@register.simple_tag
def achives():
    return Article.objects.dates('add_time', 'month', order='DESC')


@register.simple_tag
def get_tag():
    return Tag.objects.all()
