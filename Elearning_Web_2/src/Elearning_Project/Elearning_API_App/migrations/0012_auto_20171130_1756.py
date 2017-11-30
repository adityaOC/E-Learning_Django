# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning_API_App', '0011_auto_20171130_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherprofile',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='course_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Elearning_API_App.TeacherProfile'),
            preserve_default=False,
        ),
    ]