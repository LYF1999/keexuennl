from django.contrib import admin
from .models import Agent


class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'wechat_no', 'mobile_phone', 'supervisor', 'start_date', 'end_date')
    search_fields = ('name', 'mobile_phone')

admin.site.register(Agent, AgentAdmin)
