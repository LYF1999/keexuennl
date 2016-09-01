# coding=utf-8
from agentauth.models import Agent
from django import forms


class Authorize(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ('name', 'wechat_no', 'mobile_phone', 'supervisor', 'date', 'auth_no')
