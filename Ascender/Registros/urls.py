from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^login/$', login, {'template_name': 'registro/login.html'}),
    url(r'^registrar/$', views.registrar, name='registrar'),

    url(r'^oauth/', include('social_django.urls', namespace='social')),
]