"""FEP_Navidad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, password_reset, password_reset_done,\
    password_reset_confirm, password_reset_complete

urlpatterns = [
    # URL del sitio de administracion
    url(r'^admin/', admin.site.urls),
    # URL de la pagina principal de jugador
    url(r'^jugador/', include('apps.jugador.urls', namespace='jugador')),
    # URL de la pagina principal del juego
    url(r'^juego/', include('apps.juego.urls', namespace='juego')),
    # Creamos la URL para el incio de sesion
    url(r'^login', login, {'template_name':'jugador/login.html'}, name='login'),
    # Creamos las URL para resetear la contrasenia
    url(r'^reset/password_reset$', password_reset, {'template_name':'Reset/password_reset.html', 'email_template_name':'Reset/password_reset_email.html'}, name='password_reset'),
    url(r'^reset/password_reset_done$', password_reset_done, {'template_name':'Reset/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name':'Reset/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/password_reset_complete', password_reset_complete, {'template_name':'Reset/password_final.html'}, name='password_reset_complete'),
]
