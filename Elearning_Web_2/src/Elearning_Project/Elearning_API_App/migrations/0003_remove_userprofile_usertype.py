# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-13 00:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning_API_App', '0002_auto_20171113_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='userType',
        ),
    ]
