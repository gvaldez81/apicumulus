from django.conf.urls import patterns, url
from pacientes import views

urlpatterns = patterns('',
    url(r'^/?$', views.PacientesView.as_view(), name='pacientes'),
    url(r'^/(?P<curp>\w+)$', views.PacienteDetailView.as_view(), name='paciente'),
    url(r'^/(?P<curp>\w+)/alergias$', views.AlergiasView.as_view(), name='alergias'),
    url(r'^/(?P<curp>\w+)/medicamentos$', views.MedicamentosView.as_view(), name='medicamentos'),
    url(r'^/(?P<curp>\w+)/eventos$', views.EventosView.as_view(), name='eventos'),
    url(r'^/(?P<curp>\w+)/eventos/(?P<evento_id>\d+)$', views.EventoDetailView.as_view(), name='evento'),
    url(r'^/(?P<curp>\w+)/eventos/(?P<evento_id>\d+)/intervenciones$', views.IntervencionesView.as_view(), name='intervenciones'),
    url(r'^/(?P<curp>\w+)/eventos/(?P<evento_id>\d+)/diagnosticos$', views.DiagnosticosView.as_view(), name='diagnosticos'),
    url(r'^/(?P<curp>\w+)/eventos/(?P<evento_id>\d+)/tomas_signos$', views.TomasSignosView.as_view(), name='tomas_signos'),
    url(r'^/(?P<curp>\w+)/eventos/(?P<evento_id>\d+)/recetas$', views.RecetasView.as_view(), name='recetas'),
    url(r'^/(?P<curp>\w+)/eventos/(?P<evento_id>\d+)/cuestionarios$', views.CuestionarioView.as_view(), name='cuestionarios'),
)
