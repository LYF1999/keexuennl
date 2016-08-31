# -*- coding:utf-8 -*-
from django.shortcuts import render
__author__ = 'Pure White'


def index(request):
    return render(request, 'index.html')
