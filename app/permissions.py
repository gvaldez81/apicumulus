from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.views import APIView
from .models import App
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ObjectDoesNotExist

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class AppView(APIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

def isApp(user):
    try:
        App.objects.get(app=user.username)
        return True
    except ObjectDoesNotExist:
        return False


