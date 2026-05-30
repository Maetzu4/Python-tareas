from django.urls import path
from . import views

# Definimos las rutas específicas de la aplicación de eventos universitarios
urlpatterns = [
    # Ruta raíz (Página principal con estadísticas)
    path('', views.home, name='home'),
    
    # Ruta para el listado completo de eventos
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    
    # Ruta para el formulario de registro de eventos
    path('eventos/nuevo/', views.registrar_evento, name='registrar_evento'),
]
