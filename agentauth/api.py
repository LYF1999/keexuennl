# coding=utf-8

from django.http import Http404, JsonResponse, HttpResponseNotFound, HttpResponse
from agentauth.models import Agent


# Create your views here.

def auth(request):
    if 'query' not in request.GET:
        return HttpResponseNotFound()
    if not request.GET['query']:
        return HttpResponseNotFound()
    if not (Agent.objects.filter(wechat_no=request.GET['query']).exists() or Agent.objects.filter(
            name=request.GET['query']).exists()):
        return JsonResponse({'result': False})
    else:
        if (Agent.objects.filter(wechat_no=request.GET['query']).count() == 0) and (Agent.objects.filter(
                name=request.GET['query']).count() > 1):
            return JsonResponse({'result': 2})
        return JsonResponse({'result': True})
