from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import *
from .utils import raw_sql_search, secret_key_gen
from .permissions import isApp, AppView

@api_view(['POST'])
def apptoken(request, format=None):
    username = request.POST.get('username','')
    password = request.POST.get('password','')

    if not username or not password:
        return Response({'message': 'Incorrect params'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({'message': 'No such user'}, status=status.HTTP_404_NOT_FOUND)

    if isApp(user):
        return login(request)
    else:
        return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

class AppResetKeyView(AppView):
    def post(self, request, format=None):
        key = secret_key_gen()
        keyapp = User.objects.get(id=request.POST.get('comboApp'))
        keyapp.set_password(key)
        keyapp.save()
        apps = App.objects.filter(admins=User.objects.filter(username=request.user.username))
        return render(request, 'reset.html', {'apps':apps, 'key':key})

    def get(self, request, format=None):
        apps = App.objects.filter(admins=User.objects.filter(username=request.user.username))
        return render(request, 'reset.html', {'apps':apps})
