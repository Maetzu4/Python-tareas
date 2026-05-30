from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import F, Q
from .models import Evento
from .forms import EventoForm

def home(request):
    """
    Vista de la Página de Inicio (Home) del sistema.
    Muestra estadísticas dinámicas de los eventos usando el ORM de Django.
    """
    # Consulta de datos generales con ORM
    eventos_totales = Evento.objects.count()
    
    # Eventos que tienen cupos (inscritos menor que cupos)
    # Usamos la expresión F() de Django para comparar dos campos del mismo modelo de forma eficiente en SQL
    eventos_con_cupos = Evento.objects.filter(inscritos__lt=F('cupos')).count()
    
    # Eventos agotados (inscritos mayor o igual que cupos)
    eventos_agotados = Evento.objects.filter(inscritos__gte=F('cupos')).count()
    
    context = {
        'eventos_totales': eventos_totales,
        'eventos_con_cupos': eventos_con_cupos,
        'eventos_agotados': eventos_agotados,
    }
    return render(request, 'eventos/index.html', context)

def listar_eventos(request):
    """
    Vista que muestra el listado completo de eventos organizados por fecha.
    Incluye un buscador funcional que filtra por nombre u organizador usando el ORM.
    """
    query = request.GET.get('q', '') # Obtener parámetro de búsqueda
    
    if query:
        # Uso de filter() y order_by() con filtros lógicos Q
        eventos = Evento.objects.filter(
            Q(nombre__icontains=query) | Q(organizador__icontains=query)
        ).order_by('fecha')
    else:
        # Uso de objects.all() y order_by()
        eventos = Evento.objects.all().order_by('fecha')
        
    context = {
        'eventos': eventos,
        'query': query,
    }
    return render(request, 'eventos/eventos.html', context)

def registrar_evento(request):
    """
    Vista funcional (FBV) para registrar nuevos eventos universitarios en la base de datos.
    Valida la información ingresada, maneja errores y muestra mensajes flash de éxito con Bootstrap 5.
    """
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            # Guarda el objeto en la base de datos
            evento_guardado = form.save()
            # Muestra un mensaje de éxito usando el sistema de mensajes de Django
            messages.success(request, f'¡Excelente! El evento "{evento_guardado.nombre}" ha sido registrado con éxito.')
            # Redirección segura a la lista de eventos
            return redirect('listar_eventos')
        else:
            # Si el formulario tiene errores, los mensajes flash informan al usuario
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        # Petición GET: se muestra un formulario vacío
        form = EventoForm()
        
    context = {
        'form': form,
    }
    return render(request, 'eventos/nuevo_evento.html', context)
