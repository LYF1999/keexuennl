# coding=utf-8
from django.shortcuts import render
from agentauth.models import Agent
from .forms import Authorize, Login
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse
import django.contrib.auth as auth
import re


@login_required
def command(request):
    form = Authorize()
    if request.method == "GET":
        return render(request, 'command.html', {
            'form': form
        })
    else:
        errors = {'error1': '', 'error2': '', 'error3': '', 'error4': '', 'error5': '', 'error6': ''}
        name = request.POST.get('name')
        wechat_no = request.POST.get('wechat_no')
        mobile_phone = request.POST.get('mobile_phone')
        supervisor = request.POST.get('supervisor')
        date = request.POST.get('date')
        auth_no = request.POST.get('auth_no')
        if not name:
            errors['error1'] = '＊ 未填写'
        if not wechat_no:
            errors['error2'] = '＊ 未填写'
        if not mobile_phone:
            errors['error3'] = '＊ 未填写'
        if not supervisor:
            errors['error4'] = '＊ 未填写'
        if not date:
            errors['error5'] = '＊ 未填写'
        if not auth_no:
            errors['error6'] = '＊ 未填写'
        if not re.match(u'^\d{4}-[0-1][0-9]-[0-3][0-9]$', date):
            errors['error5'] = '＊ 格式错误'
        if Agent.objects.filter(wechat_no=request.POST.get('wechat_no')).exists():
            errors['error2'] = '＊ 已存在'
        if Agent.objects.filter(mobile_phone=request.POST.get('mobile_phone')).exists():
            errors['error3'] = '＊ 已存在'
        if Agent.objects.filter(auth_no=request.POST.get('auth_no')).exists():
            errors['error6'] = '＊ 已存在'
        if errors:
            return JsonResponse({
                'result': False,
                'errors': errors,
            })
        else:
            Agent.objects.create(name=name,
                                 wechat_no=wechat_no,
                                 mobile_phone=mobile_phone,
                                 supervisor=supervisor,
                                 date=date,
                                 auth_no=auth_no,
                                 )
            return JsonResponse({
                'result': True
            })


def login(request):
    if request.method == "GET":
        form = Login()
        return render(request, 'login.html', {
            'form': form
        })
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print request.POST
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_staff:
                auth.login(request, user)
                return JsonResponse({
                    'result': True
                }, safe=False)
        return JsonResponse({
            'result': False,
        })


def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
