# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-08 19:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180408_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='modified_time',
        ),
    ]