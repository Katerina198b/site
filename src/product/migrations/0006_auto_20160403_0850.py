# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20160402_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]