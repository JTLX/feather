# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todolist_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='todotag',
            name='color',
            field=models.CharField(default='#000000', max_length=20),
        ),
    ]
