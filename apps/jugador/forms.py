from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser
from .models import Datos
from django import forms

# Esta clase maneja todo el formulario con todos los datos del registro a 
# excepcion del celular
class RegistroForm(UserCreationForm):
    
    class Meta:
        # Hacemos uso del modelo User que trae Django por defecto para extraer
        # nombre, apellido, correo y contrasenia
        model = Datos
        
        # Este es el arreglo de los campos que usaremos
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
                'celular',
            ]
        
        # Este es el arreglo con las etiquetas para cada uno de los campos que
        # usaremos
        labels = {
                'username': 'Nombre de usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellido',
                'email': 'Correo',
                'celular': 'Celular',
            }
        
        # En este arreglo se definen parametros HTML para cada uno de los campos
        # que usaremos, en este caso el unico parametro es el 'placeholder'
        widgets = {
                'username': forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
                'first_name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
                'last_name': forms.TextInput(attrs={'placeholder': 'Apellido'}),
                'email': forms.EmailInput(attrs={'placeholder': 'Correo'}),
                'password1': forms.PasswordInput(attrs={'placeholder': 'Contrasenia'}),
                'password2': forms.PasswordInput(attrs={'placeholder': 'Contrasenia'}),
                'celular': forms.NumberInput(attrs={'placeholder': 'Celular'}), 
            } 