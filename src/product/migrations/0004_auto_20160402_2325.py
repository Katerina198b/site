# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-02 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20160402_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static/product.jpg', upload_to=b''),
        ),
    ]