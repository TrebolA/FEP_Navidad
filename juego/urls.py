from django.conf.urls import url
from .views import reglas, gracias
from juego import views

urlpatterns = [
    url(r'^reglas', reglas, name='reglas'),
    url(r'^gracias', gracias, name='gracias'),
    url(r'', views.inicioJuego, name='inicioJuego'),
    url(r'^juego', views.juego, name='juego'),
]