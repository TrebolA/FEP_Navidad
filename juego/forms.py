from django import forms
from .models import Resultados

class InicioJuegoForm(forms.ModelForm):

    class Meta:
        model = Resultados
        fields = ('')
        
class JuegoForm(forms.ModelForm):

    class Meta:
        model = Resultados
        fields = ('respuesta')