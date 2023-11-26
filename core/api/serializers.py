from rest_framework import serializers
from core.models import PontosTuristico

class PontosTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model= PontosTuristico
        fields= ('id','nome','descricao')
        #fields= '__all__'