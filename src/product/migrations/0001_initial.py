# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 09:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_auto_20160402_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lol', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439',
                'verbose_name_plural': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('name', models.CharField(default='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430', max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430')),
                ('description', models.TextField(default='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('changed_at', models.DateField(auto_now=True)),
                ('publish', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('shop', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.Shop')),
            ],
            options={
                'verbose_name': '\u0422\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='product.Product'),
        ),
    ]
