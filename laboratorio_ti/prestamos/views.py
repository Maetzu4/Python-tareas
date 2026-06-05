from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Equipo
from .forms import EquipoForm

def inicio(request):
    """Redirige automáticamente al listado de equipos."""
    return redirect('lista_equipos')

def registrar_equipo(request):
    """Muestra el formulario y procesa el registro de un nuevo equipo."""
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            equipo = form.save()
            messages.success(request, f'¡El equipo "{equipo.nombre}" se ha registrado con éxito!')
            return redirect('lista_equipos')
    else:
        form = EquipoForm()
    
    return render(request, 'prestamos/registrar_equipo.html', {'form': form})

def lista_equipos(request):
    """Muestra todos los equipos y las tarjetas de resumen estadísticas."""
    equipos = Equipo.objects.all().order_by('-id')
    total_equipos = Equipo.objects.count()
    total_disponibles = Equipo.objects.filter(disponible=True).count()
    total_prestados = Equipo.objects.filter(disponible=False).count()
    
    context = {
        'equipos': equipos,
        'total_equipos': total_equipos,
        'total_disponibles': total_disponibles,
        'total_prestados': total_prestados,
        'active_tab': 'todos'
    }
    return render(request, 'prestamos/equipos.html', context)

def equipos_disponibles(request):
    """Muestra únicamente los equipos disponibles."""
    equipos = Equipo.objects.filter(disponible=True).order_by('-id')
    total_equipos = Equipo.objects.count()
    total_disponibles = equipos.count()
    total_prestados = total_equipos - total_disponibles
    
    context = {
        'equipos': equipos,
        'total_equipos': total_equipos,
        'total_disponibles': total_disponibles,
        'total_prestados': total_prestados,
        'active_tab': 'disponibles'
    }
    return render(request, 'prestamos/disponibles.html', context)

def equipos_prestados(request):
    """Muestra únicamente los equipos prestados."""
    equipos = Equipo.objects.filter(disponible=False).order_by('-id')
    total_equipos = Equipo.objects.count()
    total_prestados = equipos.count()
    total_disponibles = total_equipos - total_prestados
    
    context = {
        'equipos': equipos,
        'total_equipos': total_equipos,
        'total_disponibles': total_disponibles,
        'total_prestados': total_prestados,
        'active_tab': 'prestados'
    }
    return render(request, 'prestamos/prestados.html', context)

def cambiar_estado(request, id):
    """Cambia el estado de un equipo entre Disponible y Prestado y redirige al listado."""
    equipo = get_object_or_404(Equipo, id=id)
    equipo.disponible = not equipo.disponible
    equipo.save()
    
    nuevo_estado = "Disponible" if equipo.disponible else "Prestado"
    messages.success(request, f'El estado de "{equipo.nombre}" ha sido cambiado a "{nuevo_estado}".')
    return redirect('lista_equipos')
