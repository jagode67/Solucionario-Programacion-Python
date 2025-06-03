from django.http import HttpResponse
from django.shortcuts import render,redirect
from productos.models import Productos
from django.forms import modelform_factory
# Create your views here.
def productos(request):
    nProductos={'nProductos':Productos.objects.count(),
                 'productos':Productos.objects.order_by('nombre')
                 }
    return render(request,"productos.html",nProductos)

def detalleProducto(request,id):
    detalle={'producto':Productos.objects.get(pk=id)}
    return render(request,'detalleP.html',detalle)

ProductosForm = modelform_factory(Productos, exclude=[])
def editarProducto(request,id):
    #detalle = {'persona': Personas.objects.get(pk=id)}
    persona=Productos.objects.get(pk=id)
    if request.method =='POST':
        formulario=ProductosForm(request.POST,instance=persona)
        if formulario.is_valid():
            formulario.save()
            return redirect("index")
        else:
            formulario = {"formulario": formulario}
            return render(request,"nuevoP.html",formulario)
    else:
        formulario = {"formulario": ProductosForm(instance=persona)}
        return render(request, "editarP.html", formulario)

def nuevoProducto(request):
    if request.method =='POST':
        formulario=ProductosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("index")
        else:
            return render(request,"nuevoP.html",formulario)
    else:
        formulario = {"formulario": ProductosForm()}
        return render(request, "nuevoP.html", formulario)

def eliminarProducto(request,id):
    persona=Productos.objects.get(pk=id)
    if persona:
        persona.delete()
    return redirect("index")