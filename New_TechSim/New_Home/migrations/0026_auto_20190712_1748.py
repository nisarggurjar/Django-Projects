# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-12 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New_Home', '0025_auto_20190712_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='certificate',
        ),
        migrations.AddField(
            model_name='dates',
            name='certificate',
            field=models.BooleanField(default=False),
        ),
    ]
