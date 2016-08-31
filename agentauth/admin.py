from django.contrib import admin
from .models import Agent


class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'wechat_no', 'mobile_phone', 'supervisor', 'date')

admin.site.register(Agent, AgentAdmin)
