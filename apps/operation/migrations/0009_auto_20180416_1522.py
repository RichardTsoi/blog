# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-16 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0008_auto_20180416_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replycomment',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='comment',
            field=models.TextField(),
        ),
    ]
