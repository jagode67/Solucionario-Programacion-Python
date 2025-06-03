from django.db import models
class Domicilio(models.Model):
    calle=models.CharField(max_length=100)
    no_calle=models.IntegerField()
    pais=models.CharField(max_length=50)

class Personas(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    domicilio=models.ForeignKey(Domicilio,on_delete=models.SET_NULL,null=True)

