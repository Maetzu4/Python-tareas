from django.shortcuts import render
from .models import Evento
from datetime import datetime

def listar_eventos(request):
    eventos = Evento.objects.all()
    context = {
        'nombre_sistema': 'Sistema de Gestión de Eventos Académicos (SGEA)',
        'fecha_actual': datetime.now(),
        'eventos': eventos
    }
    return render(request, 'eventos.html', context)