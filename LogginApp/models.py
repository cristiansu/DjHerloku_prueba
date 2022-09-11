from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    pais = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
