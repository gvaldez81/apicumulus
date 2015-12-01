from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .models import Paciente

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class PacienteView(APIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    authentication_classes = (TokenAuthentication, )

    def get_ctapac(self, paciente_id):
        pac = get_object_or_404(Paciente, id=paciente_id)
        self.check_object_permissions(self.request, pac)
        return pac
