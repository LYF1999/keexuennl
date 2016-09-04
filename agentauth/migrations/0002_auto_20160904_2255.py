# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agentauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='level',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b49\u7ea7'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='auth_no',
            field=models.CharField(max_length=255, unique=True, verbose_name='\u6388\u6743\u53f7\u7801'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='mobile_phone',
            field=models.CharField(max_length=255, unique=True, verbose_name='\u624b\u673a\u53f7'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='wechat_no',
            field=models.CharField(max_length=255, unique=True, verbose_name='\u5fae\u4fe1\u53f7'),
        ),
    ]