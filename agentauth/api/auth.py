# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse, HttpResponseNotFound
from agentauth.models import Agent
import json


# Create your views here.
# 用于替换views的方法= =

def index(request):
    if 'query' not in request.GET:
        return Http404(request)
    if not request.GET['query']:
        return HttpResponseNotFound()
    if not (Agent.objects.filter(wechat_no=request.GET['query']).exists() or Agent.objects.filter(
            name=request.GET['query']).exists()):
        return JsonResponse(json.dumps(0), safe=False)
    if Agent.objects.filter(wechat_no=request.GET['query']).exists():
        agent = get_object_or_404(Agent, wechat_no=request.GET['query'])
    else:
        agent = get_object_or_404(Agent, name=request.GET['query'])
    return render(request, 'authorization.html', locals())
