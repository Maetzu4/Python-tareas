from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    responsable = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
