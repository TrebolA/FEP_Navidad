from django.shortcuts import render

# Create your views here.

def reglas(request):
        return render(request, 'juego/reglas.html', {})
    
def gracias(request):
        return render(request, 'juego/thank_you.html', {})