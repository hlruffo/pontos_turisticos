from rest_framework import serializers
from comentarios.models import Comentario

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comentario
        fields= '__all__'