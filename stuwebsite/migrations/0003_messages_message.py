# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuwebsite', '0002_auto_20151221_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='message',
            field=models.TextField(default='deger gir'),
        ),
    ]
