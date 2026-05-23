from django.db import models

class Facultad(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    fecha_creacion = models.DateField()

    def __str__(self):
        return self.nombre


class ProgramaAcademico(models.Model):
    nombre = models.CharField(max_length=100)
    codigo_snies = models.CharField(max_length=20, unique=True)
    cantidad_semestres = models.IntegerField()
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, related_name='programas')

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    TIPO_DOC_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
    ]
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOC_CHOICES)
    numero_documento = models.CharField(max_length=20, unique=True)
    nombre_completo = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)
    edad = models.IntegerField()
    promedio_acumulado = models.FloatField()
    estado = models.BooleanField(default=True)  # True = Activo, False = Inactivo
    programa = models.ForeignKey(ProgramaAcademico, on_delete=models.PROTECT, related_name='estudiantes')

    def __str__(self):
        return self.nombre_completo


class Docente(models.Model):
    nombre_completo = models.CharField(max_length=150)
    profesion = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    salario = models.DecimalField(max_length=12, decimal_places=2, max_digits=12)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.nombre_completo


class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    creditos = models.IntegerField()
    semestre = models.IntegerField()
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='asignaturas')

    def __str__(self):
        return self.nombre


class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='matriculas')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='matriculas')
    nota_definitiva = models.FloatField()
    fecha_matricula = models.DateField()
    estado_aprobacion = models.BooleanField(default=False) # True = Aprobado, False = Reprobado

    def __str__(self):
        return f"{self.estudiante.nombre_completo} - {self.asignatura.nombre}"