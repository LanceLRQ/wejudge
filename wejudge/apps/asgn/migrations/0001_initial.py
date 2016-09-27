# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 04:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('problem', '0001_initial'),
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asgn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('remark', models.TextField(default=b'{}')),
                ('signature', models.SmallIntegerField(default=1000)),
                ('create_time', models.IntegerField(default=0)),
                ('full_score', models.IntegerField(default=0)),
                ('lang', models.CharField(blank=True, default=b'all', max_length=255, null=True)),
                ('arrangement_setting', models.TextField(default=b'{}')),
                ('arrangement', models.ManyToManyField(blank=True, to='education.Arrangement')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='account.User')),
                ('black_list', models.ManyToManyField(blank=True, related_name='black_list', to='account.User')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.Course')),
                ('judge_status', models.ManyToManyField(blank=True, to='problem.JudgeStatus')),
            ],
        ),
        migrations.CreateModel(
            name='AsgnProblems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.IntegerField(default=0)),
                ('submission', models.IntegerField(default=0)),
                ('require', models.BooleanField(default=False)),
                ('ignore_flag', models.CharField(blank=True, max_length=255, null=True)),
                ('score', models.IntegerField(default=0)),
                ('lang', models.CharField(blank=True, default=b'inherit', max_length=255, null=True)),
                ('problem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='problem.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.IntegerField(default=0)),
                ('submission', models.IntegerField(default=0)),
                ('ignore', models.IntegerField(default=0)),
                ('accepted', models.IntegerField(default=0)),
                ('first_ac_time', models.IntegerField(default=-1)),
                ('asgn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asgn.Asgn')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.User')),
                ('judge_status', models.ManyToManyField(blank=True, to='problem.JudgeStatus')),
                ('problems', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='problem.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='StuReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judge_score', models.IntegerField(default=0)),
                ('finally_score', models.IntegerField(default=0)),
                ('ac_counter', models.IntegerField(default=0)),
                ('submission_counter', models.IntegerField(default=0)),
                ('solved_counter', models.IntegerField(default=0)),
                ('impression', models.TextField(blank=True, null=True)),
                ('create_time', models.IntegerField(default=0)),
                ('deadline_time', models.IntegerField(default=0)),
                ('modify_time', models.IntegerField(default=0)),
                ('teacher_check', models.BooleanField(default=False)),
                ('teacher_remark', models.TextField(blank=True, null=True)),
                ('asgn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asgn.Asgn')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.User')),
            ],
        ),
        migrations.AddField(
            model_name='asgn',
            name='problemset',
            field=models.ManyToManyField(blank=True, to='asgn.AsgnProblems'),
        ),
    ]
