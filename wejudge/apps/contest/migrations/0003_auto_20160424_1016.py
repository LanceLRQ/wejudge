# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-24 02:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_contest_problemset'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contestsolution',
            old_name='content',
            new_name='contest',
        ),
    ]
