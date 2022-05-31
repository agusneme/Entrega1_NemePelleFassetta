from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

#### Persona
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    altura = models.FloatField(default=0.0)
    edad = models.IntegerField(default=0)

#### Profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

#### Curso
class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.CharField(max_length=50)
