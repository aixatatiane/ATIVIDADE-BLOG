from django.shortcuts import render

# Create your views here.
from .models import *

# Create your views here.
def index(request):
    eutati = Eu.objects.all() 
    informacoes = {
        'lista': eutati,
    }
    return render(request, 'blog/index.html',informacoes)

def sobre_me(request):
    eutati = Eu.objects.all() 
    informacoes = {
        'lista': eutati,
    }
    return render(request, 'blog/sobre.html',informacoes)