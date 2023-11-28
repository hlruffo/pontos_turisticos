from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco
# Create your models here.

class PontosTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default = False)
    atracoes = models.ManyToManyField("atracoes.Atracao")
    comentarios = models.ManyToManyField("comentarios.Comentario")
    avaliacoes = models.ManyToManyField("avaliacoes.Avaliacao")
    endereco = models.ForeignKey("enderecos.Endereco", on_delete=models.CASCADE,blank=True, null=True)
    foto=models.ImageField(upload_to='pontos_turisticos',blank=True, null=True)
    
    def __str__(self):
        return self.nome
    