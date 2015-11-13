from django.conf.urls import patterns, url
from pacientes import views

urlpatterns = patterns('',
    url(r'^(?P<paciente_id>\d+)/$', views.PacienteDetailView.as_view(), name='paciente'),
    url(r'^(?P<curp>\w+)/$', views.PacientePorCurpView.as_view(), name='paciente_por_curp'),
    url(r'^(?P<paciente_id>\d+)/eventos$', views.EventosView.as_view(), name='eventos'),
    url(r'^(?P<paciente_id>\d+)/intervenciones$', views.IntervencionesView.as_view(), name='intervenciones'),
    url(r'^(?P<paciente_id>\d+)/diagnosticos$', views.DiagnosticosView.as_view(), name='diagnosticos'),
    url(r'^(?P<paciente_id>\d+)/alergias$', views.AlergiasView.as_view(), name='alergias'),
    url(r'^(?P<paciente_id>\d+)/tomas_signos$', views.TomasSignosView.as_view(), name='tomas_signos'),
    url(r'^(?P<paciente_id>\d+)/medicamentos$', views.MedicamentosView.as_view(), name='medicamentos'),
    url(r'^(?P<paciente_id>\d+)/recetas$', views.RecetasView.as_view(), name='recetas'),
    url(r'^(?P<paciente_id>\d+)/historia$', views.HistoriaView.as_view(), name='historia'),
    #
    url(r'^(?P<paciente_id>\d+)/hospital/(?P<hospital_id>\d+)/$', views.PacientePermisoHospitalView.as_view(), name='paciente_permiso_hospital'),
    url(r'^(?P<curp>\w+)/hospital/(?P<hospital_id>\d+)/$', views.PacienteTieneHospitalView.as_view(), name='paciente_tiene_hospital'),
)
