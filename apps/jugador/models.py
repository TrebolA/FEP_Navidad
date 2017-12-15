from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

# Creamos el modelo Datos para obtener el celular de las personas
class Datos(AbstractUser):
    # Creamos el campo celular, con la condicion de que tenga maximo y minimo 10
    # numeros y que solo pueda empezar con 3
    celular = models.BigIntegerField(validators=[MinValueValidator(3000000000, 'No es un numero de celular valido'), MaxValueValidator(3999999999, 'No es un numero de celular valido')])