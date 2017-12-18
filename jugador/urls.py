from django.conf.urls import url
from .views import RegistroJugador

urlpatterns = [
    # Creamos la URL para el formulario de registro
    url(r'^registrar', RegistroJugador.as_view(), name="registrar"),
]