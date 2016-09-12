# -*- coding:utf-8 -*-
from django.shortcuts import render
from command.models import Gallery
import simplejson as json
__author__ = 'Pure White'


def index(request):
    gallery = Gallery.objects.all()
    return render(request, 'index.html', {
        'gallery': gallery,
    })
