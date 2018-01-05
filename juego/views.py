from django.shortcuts import render, redirect
from juego.forms import JuegoForm, InicioJuegoForm
import time

# Create your views here.

def reglas(request):
        return render(request, 'juego/reglas.html', {})
    
def gracias(request):
        return render(request, 'juego/thank_you.html', {})
    
def inicioJuego(request):
        if request.method == "POST":
            form = InicioJuegoForm(request.POST)
            if form.is_valid():
                inicio = form.save(commit=False)
                inicio.persona = request.user
                inicio.inicio = time.strftime("%H:%M:%S")
                inicio.save()
                return redirect('juego')
        else:
            form = InicioJuegoForm()
        return render(request, 'juego/juego.html', {'form': form})


def juego(request):
        if request.method == "POST":
            form = JuegoForm(request.POST)
            if form.is_valid():
                resultados = form.save(commit=False)
                resultados.persona = request.user                
                resultados.save()
                return redirect('gracias')
        else:
            form = JuegoForm()
        return render(request, 'juego/juego.html', {'form': form})