from django import forms
from .models import Evento
from datetime import date

class EventoForm(forms.ModelForm):
    """
    Formulario web basado en el modelo Evento.
    Implementa estilos de Bootstrap 5 y validaciones de negocio adicionales.
    """
    class Meta:
        model = Evento
        fields = ['nombre', 'organizador', 'fecha', 'cupos', 'inscritos']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej. Congreso de Inteligencia Artificial',
                'id': 'id_nombre'
            }),
            'organizador': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej. Facultad de Ingeniería',
                'id': 'id_organizador'
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date',
                'id': 'id_fecha'
            }),
            'cupos': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Cantidad total de cupos (Ej. 100)',
                'min': '1',
                'id': 'id_cupos'
            }),
            'inscritos': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Estudiantes inscritos a la fecha (Ej. 0)',
                'min': '0',
                'id': 'id_inscritos'
            }),
        }

    def clean_fecha(self):
        """
        Validación para asegurar que la fecha del evento no sea en el pasado.
        """
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha < date.today():
            raise forms.ValidationError("La fecha del evento no puede ser en el pasado. Debe ser hoy o un día posterior.")
        return fecha

    def clean(self):
        """
        Validación cruzada de campos en el formulario.
        """
        cleaned_data = super().clean()
        cupos = cleaned_data.get('cupos')
        inscritos = cleaned_data.get('inscritos')

        # Controlar que los inscritos no superen los cupos totales
        if cupos is not None and inscritos is not None:
            if inscritos > cupos:
                self.add_error('inscritos', "La cantidad de personas inscritas no puede superar el límite de cupos totales.")
                self.add_error('cupos', "El número de cupos debe ser igual o mayor al número de personas inscritas.")
            
            if cupos <= 0:
                self.add_error('cupos', "Los cupos totales deben ser un valor mayor a cero.")
                
            if inscritos < 0:
                self.add_error('inscritos', "El número de personas inscritas no puede ser negativo.")

        return cleaned_data
