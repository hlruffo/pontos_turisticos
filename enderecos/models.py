from django.db import models

# Create your models here.
class Endereco(models.Model):
    linha1=models.CharField(max_length=150)
    linha2=models.CharField(max_length=150, blank=True, null=True)
    cidade=models.CharField(max_length=100)
    estado=models.CharField(max_length=100)
    pais=models.CharField(max_length=100)
    latitude =models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.linha1
    
    class Meta:
        verbose_name_plural = "Endereços"