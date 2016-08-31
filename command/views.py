# coding=utf-8
from django.shortcuts import render
from agentauth.models import Agent
from django.utils import timezone


# Create your views here.
def command(request):
    if request.method == "GET":
        return render(request, 'command.html')
    else:
        authorize = request.POST.get('authorize')
        wechat = request.POST.get('wechat')
        mobile_phone = request.POST.get('phone')
        date = request.POST.get('date')
        supervisor = request.POST.get('supervisor')
        auth_no = request.POST.get('auth_no')
        errors = check(authorize=authorize, phone=mobile_phone, wechat=wechat, supervisor=supervisor, auth_no=auth_no, date=date)
        if errors:
            Agent.objects.create(name=authorize,
                                 wechat_no=wechat,
                                 mobile_phone=mobile_phone,
                                 supervisor=supervisor,
                                 date=date,
                                 auth_no=auth_no
                                 )
        return render(request, 'command.html', {
            'errors': errors,
        })


def check(authorize, wechat, phone, supervisor, auth_no, date):
    errors = {}
    if not authorize:
        errors.setdefault('authorize_error', u'兹授权为空,请填写')
    if Agent.objects.filter(name=authorize).exists():
        errors.setdefault('authorize_error', u'名称重复, 请重新填写')
    if not wechat:
        errors.setdefault('wechat_error', u'微信号为空, 请填写')
    if Agent.objects.filter(wechat_no=wechat).exists():
        errors.setdefault('wechat_error', u'微信号重复, 请重新填写')
    if not auth_no:
        errors.setdefault('auth_no_error', u'授权号码为空,请填写')
    if Agent.objects.filter(auth_no=auth_no).exists():
        errors.setdefault('auth_no_error', u'授权号码重复,请重新填写')
    if not phone:
        errors.setdefault('phone_error', u'手机号为空, 请填写')
    if not supervisor:
        errors.setdefault('supervisor_error', u'上级名称为空请填写')
    if not date:
        errors.setdefault('date_error', u'日期为空, 请填写')
    return errors
