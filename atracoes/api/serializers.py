from rest_framework import serializers
from atracoes.models import Atracao

class AtracoesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Atracao
        #fields= ('id','nome','descricao','horario_func', 'idade_minima')
        fields= '__all__'