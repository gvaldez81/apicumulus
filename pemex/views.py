from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PemexInfo
from .webservices import DerechoHabienteDumb

# Create your views here.
@api_view(['POST'])
def derecho_habiente(request, format=None):
    emp = request.data.get('numeroEmpleado', '')
    cdh = request.data.get('codigoDerechoHabiente', '')

    if not emp or not cdh:
        return Response({'message': 'Missing Parameters'}, status=status.HTTP_400_BAD_REQUEST)

    pinfo, created = PemexInfo.objects.get_or_create(numeroEmpleado=emp, codigoDerechoHabiente=cdh)

    if not created and pinfo.is_recent():
        response = { "derechoHabiente": pinfo.derechoHabiente }
    else:
        response = DerechoHabienteDumb(request.POST).request()
        pinfo.refresh(response['derechoHabiente'])

    return Response(response, status=status.HTTP_200_OK)
