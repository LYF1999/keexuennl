# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
import datetime


class Agent(models.Model):
    name = models.CharField('名称', max_length=255)
    wechat_no = models.CharField('微信号', max_length=255, unique=True)
    level = models.CharField('等级', max_length=255, null=True, blank=True)
    mobile_phone = models.CharField('手机号', max_length=255, unique=True)
    supervisor = models.CharField('上级名称', max_length=255)
    start_date = models.DateField('授权日期', null=True)
    end_date = models.DateField('结束日期', null=True, blank=True)
    auth_no = models.CharField('授权号码', max_length=255, unique=False, blank=True, null=True)

    def get_code(self):
        code = Agent.objects.order_by('-id').all()[0].id + 1
        while Agent.objects.filter(auth_no=code).exists():
            code += 1
        return code

    def save(self, *args, **kwargs):
        if self.end_date is None or self.end_date == "":
            self.end_date = datetime.date(self.start_date.year + 1, self.start_date.month, self.start_date.day)
        if self.auth_no is None or self.auth_no == "":
            self.auth_no = self.get_code()
        super(Agent, self).save(*args, **kwargs)
