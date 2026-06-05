from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'categoria', 'responsable', 'fecha_registro', 'disponible']
        labels = {
            'nombre': 'Nombre del Equipo',
            'categoria': 'Categoría',
            'responsable': 'Responsable',
            'fecha_registro': 'Fecha de Registro',
            'disponible': 'Disponible para préstamo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Laptop Dell Latitude 5420',
            }),
            'categoria': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Cómputo, Audiovisual, Redes',
            }),
            'responsable': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del encargado de TI',
            }),
            'fecha_registro': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }
