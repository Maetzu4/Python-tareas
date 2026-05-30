"""
URL configuration for universidad_eventos project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Ruta del panel de administración de Django
    path('admin/', admin.site.urls),
    # Enrutamiento principal delegado a la aplicación "eventos" usando include()
    path('', include('eventos.urls')),
]
