from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ExampleModel
from .serializers import ExampleModelSerializer

class ExampleModelViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo ExampleModel.
    Proporciona operaciones CRUD completas.
    """
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer

@api_view(['GET'])
def api_root(request):
    """
    Endpoint raíz de la API.
    """
    return Response({
        'message': 'Bienvenido a la API de core',
        'endpoints': {
            'examples': '/api/examples/',
            'admin': '/admin/',
        }
    }) 