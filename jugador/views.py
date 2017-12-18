from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from .forms import RegistroForm
from .models import Datos

def index(request):
        return render(request, 'index.html', {})

# Esta clase crea toda la vista y el manejo de los formularios
class RegistroJugador(CreateView):
    # Hacemos uso del modelo User que trae Django por defecto
    model = Datos
    # Establecemos el template en el que se visualizara el formulario de 
    # registro
    template_name = "jugador/registrar.html"
    # La clase de form que usaremos principalmente es el ExtensionForm para
    # obtener el celular
    form_class = RegistroForm
    # La url a la que se le redigira al jugador cuando se registre
    success_url = reverse_lazy('jugador:login')