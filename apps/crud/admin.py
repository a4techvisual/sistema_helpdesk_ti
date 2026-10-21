from django.contrib import admin
from .models import Chamado

# Register your models here.
@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('codigo_chamado', 'titulo', 'solicitante', 'setor', 'prioridade', 'status', 'data_abertura')
    list_filter = ('status', 'prioridade', 'categoria')
    search_fields = ('titulo', 'solicitante', 'patrimonio')
