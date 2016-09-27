# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-11 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0004_remove_problem_classify'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='classify',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='problem.ProblemClassify'),
        ),
    ]
