# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-18 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnuzoj', '0003_auto_20160518_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='web_login_black_list',
            field=models.TextField(blank=True, default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='web_login_white_list',
            field=models.TextField(blank=True, default=b'', null=True),
        ),
    ]
