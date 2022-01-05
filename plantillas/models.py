from django.db import models

# Create your models here.


class Plantilla(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    observaciones = models.TextField()

    def __str__(self):
        return self.nombre
