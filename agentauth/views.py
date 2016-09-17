from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse, HttpResponseNotFound
from .models import Agent
import json


# Create your views here.


def index(request):
    if 'query' not in request.GET:
        return HttpResponseNotFound()
    if not request.GET['query']:
        return HttpResponseNotFound()

    if Agent.objects.filter(wechat_no=request.GET['query']).exists():
        agent = get_object_or_404(Agent, wechat_no=request.GET['query'])
    else:
        if Agent.objects.filter(name=request.GET['query']).count()>1:
            return HttpResponseNotFound()
        agent = get_object_or_404(Agent, name=request.GET['query'])
    return render(request, 'authorization.html', locals())
