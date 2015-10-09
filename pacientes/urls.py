from django.conf.urls import patterns, url
from pacientes import views

urlpatterns = patterns('',
    url(r'^(?P<paciente_id>\d+)/$', views.paciente, name='paciente'),
)
