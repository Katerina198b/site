# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20160408_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='first_name',
            field=models.CharField(default='Name', max_length=255, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='last_name',
            field=models.CharField(default='Last name', max_length=255, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f'),
        ),
    ]
