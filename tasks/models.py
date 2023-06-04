from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UsuarioGuia(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    placa = models.TextField(max_length=100)

class UsuarioCliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.TextField(blank=True)
    ruta = models.TextField(blank=True)
    HoraInicio = models.DateTimeField(null=True, blank=True)
    HoraFin = models.DateTimeField(null=True, blank=True)
    userCliente = models.ForeignKey(UsuarioCliente, on_delete=models.CASCADE)
    userGuia = models.ForeignKey(UsuarioGuia, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '- by ' + self.user.username
    

    


