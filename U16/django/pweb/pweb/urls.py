"""
URL configuration for pweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webPython.views import *

from personas.views import *
from productos.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/',personas),
    path('persona/<int:id>',detallePersona),
    path('nueva',nuevaPersona),
    path('editar/<int:id>',editarPersona),
    path('eliminar/<int:id>',eliminarPersona),
    path('productos/',productos,name="index"),
    path('producto/<int:id>',detalleProducto),
    path('nuevoP/',nuevoProducto),
    path('editarP/<int:id>',editarProducto),
    path('eliminarP/<int:id>',eliminarProducto)
]
