# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170420_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='profile',
            field=models.TextField(null=True),
        ),
    ]
