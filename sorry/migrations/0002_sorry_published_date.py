# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorry',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
