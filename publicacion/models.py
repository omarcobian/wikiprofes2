from django.db import models
from materia.models import Materia
from profesor.models import Profesor
from django.contrib.auth.models import User

# Create your models here.
class Publicacion(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=80)
    fecha = models.DateField()
    comentario = models.TextField(max_length=2000)
    dominio = models.IntegerField()
    puntualidad = models.IntegerField()
    asistencia = models.IntegerField()
    dificultad = models.IntegerField()
    seguimiento = models.IntegerField()

    def __str__(self):
        return f'{self.titulo}'