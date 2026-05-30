from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    """
    Configuración profesional del modelo Evento en el panel de administración de Django.
    """
    # Columnas que se mostrarán en la tabla del panel de administración
    list_display = ('nombre', 'organizador', 'fecha', 'cupos', 'inscritos', 'cupos_disponibles_admin', 'estado_admin')
    
    # Habilitar barra de búsqueda por nombre del evento y organizador
    search_fields = ('nombre', 'organizador')
    
    # Filtros rápidos en la barra lateral derecha
    list_filter = ('fecha', 'organizador')
    
    # Criterio de ordenamiento predeterminado (por fecha más cercana)
    ordering = ('fecha',)
    
    # Campo de solo lectura para evitar modificar datos de cálculo manual
    readonly_fields = ('cupos_disponibles_admin', 'estado_admin')

    def cupos_disponibles_admin(self, obj):
        """
        Método de conveniencia para mostrar los cupos restantes en el admin de forma legible.
        """
        return obj.cupos_disponibles
    # Título de la columna en el panel admin
    cupos_disponibles_admin.short_description = "Cupos Libres"

    def estado_admin(self, obj):
        """
        Muestra de manera textual el estado de disponibilidad del evento.
        """
        return "Disponible" if obj.tiene_cupos else "Agotado"
    estado_admin.short_description = "Estado de Cupos"
