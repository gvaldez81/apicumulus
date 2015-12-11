from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .models import Paciente, Evento

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class PacienteView(APIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    authentication_classes = (TokenAuthentication, )

    def get_pac(self, curp):
        pac = get_object_or_404(Paciente, curp=curp)
        self.check_object_permissions(self.request, pac)
        return pac

class EventoView(PacienteView):
    def get_evento(self, evt):
        evento = pac = get_object_or_404(Evento, id=evt)
        return evento

class AppView(APIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    authentication_classes = (TokenAuthentication, )

def isApp(user):
    return user.is_staff or user.is_superuser
