# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-30 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20160428_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='headimg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
