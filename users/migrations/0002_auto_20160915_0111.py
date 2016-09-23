# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-15 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(null=True, related_name='_profile_friends_+', to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='preferred_candidate',
            field=models.CharField(choices=[('Clinton', 'Clinton'), ('Johnson', 'Johnson'), ('Stein', 'Stein'), ('Trump', 'Trump')], max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='second_candidate',
            field=models.CharField(choices=[('Clinton', 'Clinton'), ('Johnson', 'Johnson'), ('Stein', 'Stein'), ('Trump', 'Trump')], max_length=255),
        ),
    ]