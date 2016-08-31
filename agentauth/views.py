from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Agent
# Create your views here.


def index(request):
    if 'query' not in request.GET:
        return Http404(request)
    if Agent.objects.filter(wechat_no=request.GET['query']).exists():
        agent = get_object_or_404(Agent, wechat_no=request.GET['query'])
    else:
        agent = get_object_or_404(Agent, name=request.GET['query'])
    return render(request, 'authorization.html', locals())
