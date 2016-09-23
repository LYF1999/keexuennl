# encoding: utf-8
from __future__ import unicode_literals

from django.db import models


class Agent(models.Model):
    name = models.CharField('名称', max_length=255)
    wechat_no = models.CharField('微信号', max_length=255, unique=True)
    level = models.CharField('等级', max_length=255, null=True, blank=True)
    mobile_phone = models.CharField('手机号', max_length=255, unique=True)
    supervisor = models.CharField('上级名称', max_length=255, blank=True, null=True)
    start_date = models.DateField('授权日期', null=True, blank=True)
    end_date = models.DateField('结束日期', null=True, blank=True)
    auth_no = models.CharField('授权号码', max_length=255, unique=False, blank=True, null=True)
