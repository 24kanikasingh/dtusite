# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-20 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('qual', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('special', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
    ]
