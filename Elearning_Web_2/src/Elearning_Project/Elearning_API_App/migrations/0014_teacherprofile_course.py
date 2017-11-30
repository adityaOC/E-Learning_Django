# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning_API_App', '0013_auto_20171130_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherprofile',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Author_Course_Relation', to='Elearning_API_App.Course'),
            preserve_default=False,
        ),
    ]