from rest_framework import serializers
from core.models import PontosTuristico
from avaliacoes.api.serializers import AvaliacoesSerializer
from comentarios.api.serializers import ComentariosSerializer
from atracoes.api.serializers import AtracoesSerializer
from enderecos.api.serializers import EnderecosSerializer


class PontosTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    comentarios = ComentariosSerializer(many=True)
    avaliacoes = AvaliacoesSerializer(many=True)
    endereco = EnderecosSerializer
    
    class Meta:
        model= PontosTuristico
        #fields= ('id','nome','descricao','foto')
        fields= '__all__'