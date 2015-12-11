"""apicumulus URL Configuration

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

from rest_framework.urlpatterns import format_suffix_patterns

from pacientes import urls as pac_urls
from app import urls as app_urls
from pemex import urls as pemex_urls
from pacientes.views import search, routes, login
from app.views import apptoken, AppResetKeyView

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pacientes/', include(pac_urls)),
    url(r'^app/', include(app_urls)),
    url(r'^pemex/', include(pemex_urls)),
    url(r'^login$', login, name='login'),
    url(r'^$', routes, name='routes'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
