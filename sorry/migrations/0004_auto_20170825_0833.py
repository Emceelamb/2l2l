# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorry', '0003_auto_20170825_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorry',
            name='relationship',
            field=models.CharField(choices=[('EXL', 'Ex-Lover'), ('FAM', 'Family'), ('SOT', 'Significant Other'), ('FRI', 'Friend'), ('COW', 'Co-Worker'), ('STG', 'Stranger')], max_length=3),
        ),
    ]
