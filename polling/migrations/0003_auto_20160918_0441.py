# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-18 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0002_auto_20160913_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
