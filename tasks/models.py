from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UsuarioCliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important =  models.BooleanField(default=False)
    user = models.ForeignKey(UsuarioCliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '- by ' + self.user.username
    

    


