from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.command, name='command'),
    url(r'^login/$', views.login, name='login'),
]
