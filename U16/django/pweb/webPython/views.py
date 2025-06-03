from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse("Respuesta desde Django")

def inicio(request):
    return HttpResponse("<H1>Página de inicio</H1>")

def despedida(request):
    return HttpResponse("<H3>Página de despedida</H3>")