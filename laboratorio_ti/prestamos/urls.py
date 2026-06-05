from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('registrar/', views.registrar_equipo, name='registrar_equipo'),
    path('disponibles/', views.equipos_disponibles, name='equipos_disponibles'),
    path('prestados/', views.equipos_prestados, name='equipos_prestados'),
    path('cambiar_estado/<int:id>/', views.cambiar_estado, name='cambiar_estado'),
]
