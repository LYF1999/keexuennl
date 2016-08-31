from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Agent
# Create your views here.


def index(request):
    if 'wechat_no' not in request.GET and 'name' not in request.GET:
        return Http404('para error')
    if 'wechat_no' in request.GET:
        agent = get_object_or_404(Agent, wechat_no=request.GET['wechat_no'])
    else:
        agent = get_object_or_404(Agent, name=request.GET['name'])
    return render(request, 'authorization.html')
