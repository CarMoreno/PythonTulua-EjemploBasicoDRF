from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.

class Films(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    fecha_lanzamiento = models.DateTimeField(null=False)
    genero = models.CharField(max_length=50, null=False, default='Sin genero')
    puntuacion = models.IntegerField(default=1, validators=[MaxValueValidator(100)])
    sinopsis = models.TextField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'films'