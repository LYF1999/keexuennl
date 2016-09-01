# coding=utf-8
from django.shortcuts import render
from agentauth.models import Agent
from django.utils import timezone
from .forms import Authorize
from django.http import JsonResponse


def command(request):
    form = Authorize()
    if request.method == "GET":
        return render(request, 'command.html', {
            'form': form
        })
    else:
        errors={}
        print request.POST
        name = request.POST.get('name')
        wechat_no = request.POST.get('wechat_no')
        mobile_phone = request.POST.get('mobile_phone')
        supervisor = request.POST.get('supervisor')
        date = request.POST.get('date')
        auth_no = request.POST.get('auth_no')
        if not name:
            errors.setdefault('error1', "＊ 未填写")
        if not wechat_no:
            errors.setdefault('error2', "＊ 未填写")
        if not mobile_phone:
            errors.setdefault('error3', "＊ 未填写")
        if not supervisor:
            errors.setdefault('error4', "＊ 未填写")
        if not date:
            errors.setdefault('error5', "＊ 未填写")
        if not auth_no:
            errors.setdefault('error6', "＊ 未填写")
        if Agent.objects.filter(wechat_no=request.POST.get('wechat_no')).exists():
            errors.setdefault('error2', "＊ 已存在")
        if Agent.objects.filter(mobile_phone=request.POST.get('mobile_phone')).exists():
            errors.setdefault('error3', "＊ 已存在")
        if Agent.objects.filter(auth_no=request.POST.get('auth_no')).exists():
            errors.setdefault('error6', "＊ 已存在")
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
