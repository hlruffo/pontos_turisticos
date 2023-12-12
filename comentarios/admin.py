from django.contrib import admin
from .models import Comentario  
from .actions import reprovar_comentarios, aprovar_comentarios

# Register your models here.
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'aprovado']
    actions = [aprovar_comentarios, reprovar_comentarios]

    
    
admin.site.register(Comentario, ComentarioAdmin)

