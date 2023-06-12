from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UsuarioPersonalizado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    es_Guia = models.BooleanField(default=False, blank=True)
    es_Cliente = models.BooleanField(default=True, blank=True)

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.TextField(blank=True)
    ruta = models.TextField(blank=True)
    HoraInicio = models.DateTimeField(null=True, blank=True)
    HoraFin = models.DateTimeField(null=True, blank=True)
    userUsuarioCustom = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE)


