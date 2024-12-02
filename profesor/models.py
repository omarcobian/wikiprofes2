from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=80)
    usuarios = models.ManyToManyField(User, through='publicacion.Publicacion')

    def __str__(self):
        return f'{self.nombre}'
    
    def get_general_rating(self):
        from publicacion.models import Publicacion  # Importación retrasada
        publicaciones = Publicacion.objects.filter(profesor=self)
        if not publicaciones.exists():
            return 0
        total = 0
        count = 0
        for pub in publicaciones:
            total += (pub.dominio + pub.puntualidad + pub.asistencia + pub.dificultad + pub.seguimiento)
            count += 1
        return total / (count * 5)  # Porque hay 5 rubros

    def get_rubric_averages(self):
        from publicacion.models import Publicacion  # Importación retrasada
        publicaciones = Publicacion.objects.filter(profesor=self)
        if not publicaciones.exists():
            return {}
        rubros = ['dominio', 'puntualidad', 'asistencia', 'dificultad', 'seguimiento']
        averages = {rubro: 0 for rubro in rubros}
        count = publicaciones.count()
        for pub in publicaciones:
            for rubro in rubros:
                averages[rubro] += getattr(pub, rubro)
        for rubro in rubros:
            averages[rubro] /= count
        return averages