# coding=utf-8
from django.shortcuts import render
from agentauth.models import Agent
from django.utils import timezone
from .forms import Authorize


# Create your views here.
def command(request):
    form = Authorize()
    if request.method == "GET":
        return render(request, 'command.html', {
            'form': form
        })
    else:
        form = Authorize(data=request.POST)
        if form.is_valid():
            Agent.objects.create(name=form.cleaned_data['name'],
                                 wechat_no=form.cleaned_data['wechat_no'],
                                 mobile_phone=form.cleaned_data['mobile_phone'],
                                 supervisor=form.cleaned_data['supervisor'],
                                 date=form.cleaned_data['date'],
                                 auth_no=form.cleaned_data['auth_no'],
                                 )
        else:
            return render(request, 'command.html', {
                'form': form
            })
