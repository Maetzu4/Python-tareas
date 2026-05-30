from django.db import models
from django.core.exceptions import ValidationError

class Evento(models.Model):
    """
    Modelo de Base de Datos para el Sistema de Gestión de Eventos Universitarios.
    Representa un evento dentro del campus con cupos de asistencia limitados.
    """
    nombre = models.CharField(
        max_length=100, 
        verbose_name="Nombre del Evento",
        help_text="Introduce el nombre descriptivo del evento universitario."
    )
    organizador = models.CharField(
        max_length=100, 
        verbose_name="Organizador",
        help_text="Facultad, semillero, grupo estudiantil o dependencia organizadora."
    )
    fecha = models.DateField(
        verbose_name="Fecha del Evento",
        help_text="Fecha programada para la realización del evento."
    )
    cupos = models.IntegerField(
        verbose_name="Cupos Totales",
        help_text="Número máximo de personas permitidas para asistir."
    )
    inscritos = models.IntegerField(
        verbose_name="Inscritos",
        help_text="Número de personas registradas hasta el momento."
    )

    def clean(self):
        """
        Validaciones personalizadas a nivel de modelo para asegurar la integridad de los datos.
        """
        super().clean()
        
        # Validar que los cupos totales no sean negativos
        if self.cupos is not None and self.cupos <= 0:
            raise ValidationError({
                'cupos': 'El número total de cupos debe ser mayor que cero.'
            })
            
        # Validar que los inscritos no sean un valor negativo
        if self.inscritos is not None and self.inscritos < 0:
            raise ValidationError({
                'inscritos': 'El número de personas inscritas no puede ser negativo.'
            })

        # Validar que los inscritos no superen la cantidad total de cupos
        if self.inscritos is not None and self.cupos is not None:
            if self.inscritos > self.cupos:
                raise ValidationError({
                    'inscritos': f'No es posible tener más inscritos ({self.inscritos}) que los cupos disponibles ({self.cupos}).'
                })

    @property
    def cupos_disponibles(self):
        """
        Método de conveniencia para calcular los cupos libres.
        """
        return max(0, self.cupos - self.inscritos)

    @property
    def tiene_cupos(self):
        """
        Método de conveniencia para verificar si quedan cupos.
        """
        return self.inscritos < self.cupos

    def __str__(self):
        """
        Representación en texto del objeto Evento.
        """
        return f"{self.nombre} - {self.organizador} ({self.fecha})"

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['fecha']
