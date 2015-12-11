from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
    url(r'^apptoken$', apptoken, name='apptoken'),
    url(r'^resetkey$', AppResetKeyView.as_view(), name='resetkey'),
)

