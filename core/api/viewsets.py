from rest_framework.viewsets import ModelViewSet
from core.models import PontosTuristico
from .serializers import PontosTuristicoSerializer

class PontosTuristicosViewSet(ModelViewSet):
    queryset = PontosTuristico.objects.all()
    serializer_class = PontosTuristicoSerializer
    #permission_classes = [permissions.IsAuthenticated]
