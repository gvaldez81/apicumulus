from django.conf.urls import patterns, url
from pacientes import views

urlpatterns = patterns('',
    url(r'^(?P<paciente_id>\d+)/$', views.paciente, name='paciente'),
    url(r'^(?P<curp>\w+)/$', views.paciente_por_curp, name='paciente_por_curp'),
    url(r'^(?P<paciente_id>\d+)/eventos$', views.eventos, name='eventos'),
    url(r'^(?P<paciente_id>\d+)/intervenciones$', views.intervenciones, name='intervenciones'),
    url(r'^(?P<paciente_id>\d+)/diagnosticos$', views.diagnosticos, name='diagnosticos'),
    url(r'^(?P<paciente_id>\d+)/alergias$', views.alergias, name='alergias'),
    url(r'^(?P<paciente_id>\d+)/tomas_signos$', views.tomas_signos, name='tomas_signos'),
    url(r'^(?P<paciente_id>\d+)/medicamentos$', views.medicamentos, name='medicamentos'),
    url(r'^(?P<paciente_id>\d+)/recetas$', views.recetas, name='recetas'),
    #
    url(r'^(?P<paciente_id>\d+)/hospital/(?P<hospital_id>\d+)/$', views.paciente_permiso_hospital, name='paciente_permiso_hospital'),
    url(r'^(?P<curp>\w+)/hospital/(?P<hospital_id>\d+)/$', views.paciente_por_hospital, name='paciente_por_hospital'),
)
