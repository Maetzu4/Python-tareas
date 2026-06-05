from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'responsable', 'fecha_registro', 'disponible')
    list_filter = ('disponible', 'categoria', 'fecha_registro')
    search_fields = ('nombre', 'responsable', 'categoria')
    ordering = ('-fecha_registro',)
