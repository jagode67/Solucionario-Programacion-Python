from django.contrib import admin

from personas.models import Personas, Domicilio

# Register your models here.
admin.site.register(Personas)
admin.site.register(Domicilio)