# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agentauth', '0002_auto_20160904_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='auth_no',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='\u6388\u6743\u53f7\u7801'),
        ),
    ]