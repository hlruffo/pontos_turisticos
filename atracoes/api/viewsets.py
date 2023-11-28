from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracoesSerializer
from rest_framework import filters

class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer
    
    #filter usando configuração do settings
    #filterset_fields = ['nome', 'descricao']
    
    #search
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao', 'idade_minima']
    
    #permission_classes = [permissions.IsAuthenticated]
