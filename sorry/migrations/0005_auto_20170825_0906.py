# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorry', '0004_auto_20170825_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorry',
            name='relationship',
            field=models.CharField(choices=[('Ex-Lover', 'Ex-Lover'), ('Family', 'Family'), ('Significant Other', 'Significant Other'), ('Friend', 'Friend'), ('Co-Worker', 'Co-Worker'), ('Stranger', 'Stranger')], max_length=3),
        ),
    ]
