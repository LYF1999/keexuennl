# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from .api import auth

__author__ = 'Pure White'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/$', auth, name='auth')
]
