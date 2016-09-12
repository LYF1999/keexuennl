# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class Gallery(models.Model):
    name = models.CharField('名字', null=True, blank=True, max_length=255)
    photo = models.ImageField('图片', upload_to='gallery', blank=True, null=True)

    class Meta:
        ordering = ['id']

# Create your models here.
