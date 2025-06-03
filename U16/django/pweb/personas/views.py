
from django.shortcuts import render,redirect
from django.http import HttpResponse
from personas.models import Personas

from django.forms import modelform_factory
PersonaForm = modelform_factory(Personas, exclude=[])
def editarPersona(request,id):
    #detalle = {'persona': Personas.objects.get(pk=id)}
    persona=Personas.objects.get(pk=id)
    if request.method =='POST':
        formulario=PersonaForm(request.POST,instance=persona)
        if formulario.is_valid():
            formulario.save()
            return redirect("index")
        else:
            formulario = {"formulario": formulario}
            return render(request,"nueva.html",formulario)
    else:
        formulario = {"formulario": PersonaForm(instance=persona)}
        return render(request, "editar.html", formulario)

def nuevaPersona(request):
    if request.method =='POST':
        formulario=PersonaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("index")
        else:
            return render(request,"nueva.html",formulario)
    else:
        formulario = {"formulario": PersonaForm()}
        return render(request, "nueva.html", formulario)


def personas(request):
    nPersonas={'nPersonas':Personas.objects.count(),
#               'personas':Personas.objects.all()}
               'personas': Personas.objects.order_by('nombre','apellido')}

    return render(request,'personas.html',nPersonas)

def detallePersona(request,id):
    detalle={'persona':Personas.objects.get(pk=id)}
    return render(request,'detalle.html',detalle)

def eliminarPersona(request,id):
    persona=Personas.objects.get(pk=id)
    if persona:
        persona.delete()
    return redirect("index")
