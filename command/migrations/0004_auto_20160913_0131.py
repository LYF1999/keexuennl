# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0003_auto_20160913_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='gallery', verbose_name='\u56fe\u7247'),
        ),
    ]
