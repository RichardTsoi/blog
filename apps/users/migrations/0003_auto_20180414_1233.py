# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-14 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180414_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='css/img/default.jpg', upload_to='media/users/image', verbose_name='用户头像'),
        ),
    ]