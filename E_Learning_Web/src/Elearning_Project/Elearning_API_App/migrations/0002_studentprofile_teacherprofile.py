# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 02:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning_API_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('subscribedCourses', jsonfield.fields.JSONField()),
            ],
            options={
                'abstract': False,
            },
            bases=('Elearning_API_App.userprofile',),
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('averageRatings', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('Elearning_API_App.userprofile',),
        ),
    ]
