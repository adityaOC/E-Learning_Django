# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning_API_App', '0016_remove_course_course_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_thumbnail_url',
            field=models.CharField(default='https://www.python.org/static/opengraph-icon-200x200.png', max_length=255),
        ),
    ]
