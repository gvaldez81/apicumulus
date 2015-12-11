from django.conf.urls import patterns, url
from pemex import views

urlpatterns = patterns('',
    url(r'^derecho_habiente$', views.derecho_habiente, name='derecho_habiente'),
)
