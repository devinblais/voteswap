# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-23 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20160923_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='active',
        ),
    ]
