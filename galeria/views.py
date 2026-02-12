from django.shortcuts import render



def index(request):
    dados = {
    1: {"nome" : "Nebulosa de Carina", "legenda" : "webbtelescope.org / NASA/ James Webb"},
    2: {"nome" : "Galaxia NGX 1079", "legenda" : "nasa.org / NASA / Hubble"}
    }
    
    return render(request, 'galeria/index.html', {"cards": dados})
# Create your views here.
def imagem(request):
    return render(request, 'galeria/imagem.html')