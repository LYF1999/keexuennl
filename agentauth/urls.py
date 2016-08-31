# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
__author__ = 'Pure White'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
