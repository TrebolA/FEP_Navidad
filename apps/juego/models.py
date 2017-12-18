from __future__ import unicode_literals
from django.db import models 
#from jugador.models import Datos

class Resultados(models.Model):
 #   asd = models.OneToOneField(Datos, null=False, blank=False)
    inicio = models.TimeField(auto_now_add=True)

