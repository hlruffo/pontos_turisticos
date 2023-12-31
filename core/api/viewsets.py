from rest_framework.viewsets import ModelViewSet
#from rest_framework.decorators import action #para criação de ação especifica
from core.models import PontosTuristico
from .serializers import PontosTuristicoSerializer

class PontosTuristicosViewSet(ModelViewSet):
    queryset = PontosTuristico.objects.all()
    serializer_class = PontosTuristicoSerializer
    
    ##aplica permissão de acesso
    #permission_classes = [permissions.IsAuthenticated]
    
    ##Sobre escreve o método gert_queryset
    # def get_queryset(self):
    #     return PontosTuristico.objects.filter(aprovado=True)
    
    ## implementando ação especifica a um item associado a id
    # @action(methods=['get'], detail=True) #note detail true
    # def denunciar(self, request, pk=None):
    #     pass
    
    ## implementando ação especifica a um recurso
    # @action(methods=['get'], detail=False) #note detail false
    # def denunciar(self, request, pk=None):
    #     pass