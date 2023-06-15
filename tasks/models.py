from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify



# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, nombre, username, apellido, password = None):

        if not nombre:
            raise ValueError(_('Tienes que dar un nombre'))

        usuario = self.model(username = username, nombre = nombre, apellido = apellido)
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self, nombre, apellido, password, username):

        usuario = self.create_user(username = username, nombre = nombre, password = password, apellido = apellido
                    
        )

        usuario.is_staff = True
        usuario.save()
        return usuario

class UsuarioPersonalizado(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True)
    es_Guia = models.BooleanField(default=False, blank=True)
    es_Cliente = models.BooleanField(default=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre', 'apellido']

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.TextField(blank=True)
    ruta = models.TextField(blank=True)
    HoraInicio = models.DateTimeField(null=True, blank=True)
    HoraFin = models.DateTimeField(null=True, blank=True)
    userUsuarioCustom = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


@property
def is_staff(self):
    return self.is_staff