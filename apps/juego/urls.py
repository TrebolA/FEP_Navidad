from django.conf.urls import url
from .views import reglas, gracias

urlpatterns = [
    url(r'^reglas', reglas, name='reglas'),
    url(r'^gracias', gracias, name='gracias'),
]