# coding=utf-8
from agentauth.models import Agent
from django import forms


class Authorize(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput({
        'autocomplete': 'off'
    }))
    wechat_no = forms.CharField(widget=forms.TextInput({
        'autocomplete': 'off'
    }))
    mobile_phone = forms.CharField(widget=forms.TextInput({
        'autocomplete': 'off'
    }))
    supervisor = forms.CharField(widget=forms.TextInput({
        'autocomplete': 'off'
    }))
    date = forms.CharField(widget=forms.TextInput({
        'autocomplete': 'off'
    }))
    auth_no = forms.CharField(widget=forms.TextInput({
        'autocomplete': 'off'
    }))

    class Meta:
        model = Agent
        fields = ('name', 'wechat_no', 'mobile_phone', 'supervisor', 'date', 'auth_no')
