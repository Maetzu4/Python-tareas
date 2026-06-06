from django.contrib import admin
from django.urls import path, include  # Importa 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miapp.urls')),  # Redirige el tráfico hacia tu app
]