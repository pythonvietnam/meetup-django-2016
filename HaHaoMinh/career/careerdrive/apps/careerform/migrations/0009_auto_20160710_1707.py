# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 10:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('careerform', '0008_auto_20160708_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='career',
            old_name='file',
            new_name='attachment',
        ),
    ]