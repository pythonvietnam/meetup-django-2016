# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerform', '0002_career_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='csvfile',
            field=models.FileField(upload_to='cv/%Y/%m/%d'),
        ),
    ]
