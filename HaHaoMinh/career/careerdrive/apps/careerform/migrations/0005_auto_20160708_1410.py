# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerform', '0004_auto_20160708_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='cvfile',
            field=models.FileField(blank=True, null=True, upload_to='cv/%Y/%m/%d'),
        ),
    ]
