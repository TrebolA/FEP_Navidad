from __future__ import unicode_literals
from django.db import models 
from jugador.models import Datos

class Resultados(models.Model):
    persona = models.ForeignKey(Datos)
    inicio = models.TimeField()
    tiempo = models.TimeField(blank=True, null=True)
    vidas = models.IntegerField(default=3)
    pistasFaltantes = models.IntegerField(default=20)
    respuesta = models.CharField(blank=True, null=True)

    def publish(self):
        self.save()
        
    def __str__(self):
        return self.persona