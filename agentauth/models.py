# encoding: utf-8
from __future__ import unicode_literals

from django.db import models


class Agent(models.Model):
    name = models.CharField('名称', max_length=255)
    wechat_no = models.CharField('微信号', max_length=255)
    mobile_phone = models.CharField('手机号', max_length=255)
    supervisor = models.CharField('上级名称', max_length=255)
    date = models.DateField('授权日期', null=True)
    auth_no = models.CharField('授权号码', max_length=255, unique=True)
