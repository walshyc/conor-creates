# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-13 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20190813_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='brief',
            field=models.TextField(default=''),
        ),
    ]
