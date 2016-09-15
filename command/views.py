# coding: utf-8
from django.shortcuts import render
from agentauth.models import Agent
from .forms import Authorize
from django.http import JsonResponse
from .forms import Authorize, Login
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse
import django.contrib.auth as auth
from command.models import Gallery
import re


@login_required
def command(request):
    form = Authorize()
    if request.method == "GET":
        return render(request, 'command.html', {
            'form': form
        })
    else:
        errors = {'error1': '', 'error2': '', 'error3': '', 'error4': '', 'error5': '', 'error6': '', 'error7': ''}
        name = request.POST.get('name')
        wechat_no = request.POST.get('wechat_no')
        level = request.POST.get('level')
        mobile_phone = request.POST.get('mobile_phone')
        supervisor = request.POST.get('supervisor')
        date = request.POST.get('date')
        auth_no = request.POST.get('auth_no')
        if not name:
            errors['error1'] = '＊ 未填写'
        if not level:
            errors['error7'] = '＊ 未填写'
        if not wechat_no:
            errors['error2'] = '＊ 未填写'
        if not mobile_phone:
            errors['error3'] = '＊ 未填写'
        if not supervisor:
            errors['error4'] = '＊ 未填写'
        if not date:
            errors['error5'] = '＊ 未填写'
        # if not auth_no:
        #     errors['error6'] = '＊ 未填写'
        if not re.match(u'^\d{4}-[0-1][0-9]-[0-3][0-9]$', date):
            errors['error5'] = '＊ 格式错误'
        if Agent.objects.filter(wechat_no=request.POST.get('wechat_no')).exists():
            errors['error2'] = '＊ 已存在'
        if Agent.objects.filter(mobile_phone=request.POST.get('mobile_phone')).exists():
            errors['error3'] = '＊ 已存在'
        if Agent.objects.filter(auth_no=request.POST.get('auth_no')).exists():
            errors['error6'] = '＊ 已存在'
        if errors['error1'] or errors['error2'] or errors['error3'] or errors['error4'] or errors['error5'] or errors[
            'error6']:
            return JsonResponse({
                'result': False,
                'errors': errors,
            })
        else:
            Agent.objects.create(name=name,
                                 level=level,
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


def check_name(name):
    if not Gallery.objects.filter(name=name).exists():
        Gallery.objects.create(name=name)


def create_gallery():
    for i in range(1, 25):
        check_name(name='gallery' + str(i))
    check_name(name='gallery1-1')
    check_name(name='gallery8-1')
    check_name(name='gallery13-1')
    check_name(name='gallery20-1')
    check_name(name='gallery2,3,7,9..')
    check_name(name='gallery')
