# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-12 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20190812_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='short',
            field=models.CharField(default='', max_length=20),
        ),
    ]
