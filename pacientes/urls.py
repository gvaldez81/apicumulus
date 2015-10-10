from django.conf.urls import patterns, url
from pacientes import views

urlpatterns = patterns('',
    url(r'^(?P<paciente_id>\d+)/$', views.paciente, name='paciente'),
    url(r'^(?P<paciente_id>\d+)/eventos$', views.eventos, name='eventos'),
)
