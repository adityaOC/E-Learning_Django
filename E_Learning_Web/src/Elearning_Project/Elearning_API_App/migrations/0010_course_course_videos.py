# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning_API_App', '0009_auto_20171101_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_videos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Elearning_API_App.Video'),
            preserve_default=False,
        ),
    ]
