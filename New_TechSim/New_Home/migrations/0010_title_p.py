# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-11 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New_Home', '0009_auto_20190711_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='p',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
