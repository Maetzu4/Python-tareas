from django.db import models

class Conferencista(models.Model):
    nombre_completo = models.CharField(max_length=150)
    profesion = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_completo} - {self.profesion}"


class Evento(models.Model):
    nombre_evento = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    lugar = models.CharField(max_length=150)
    cupos_disponibles = models.IntegerField()
    conferencista = models.ForeignKey(Conferencista, on_delete=models.CASCADE, related_name='eventos')

    def __str__(self):
        return self.nombre_evento


class Participante(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombre_completo = models.CharField(max_length=150)
    correo_electronico = models.EmailField(unique=True)
    programa_academico = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_completo


class Inscripcion(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='inscripciones')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Inscripciones"
        unique_together = ('participante', 'evento') # Evita duplicar inscripción

    def __str__(self):
        return f"{self.participante.nombre_completo} en {self.evento.nombre_evento}"