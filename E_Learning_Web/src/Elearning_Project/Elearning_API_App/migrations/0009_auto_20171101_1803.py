# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning_API_App', '0008_auto_20171101_0510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_videos',
        ),
        migrations.AddField(
            model_name='video',
            name='video_course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Elearning_API_App.Course'),
            preserve_default=False,
        ),
    ]
