"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^0', 'learn.views.index', name='home'),# Notice this line
    # url(r'^1', 'learn1.views.home', name='home'),# Notice this line
    url(
    regex =r'^$',
    view  ='learn5.views.index',
    name='learn5'
    ),#
    # url(
    # regex =r'^_sae/shell$',
    # view  ='learn3.views.seashell',
    # name='seashell'
    # ),#
    #url(r'^4/$', 'learn4.views.index', name='home'),
    #url(r'^add/$', 'learn4.views.add', name='add'),
    #url(r'^ajax_list/$', 'learn4.views.ajax_list', name='ajax-list'),
    #url(r'^ajax_dict/$', 'learn4.views.ajax_dict', name='ajax-dict'),
    # url(r'^add/$', 'learn3.views.add', name='add'),
    url(r'^admin/', include(admin.site.urls)),
]
