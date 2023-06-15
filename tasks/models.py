from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify



# Create your models here.

class UsuarioManager(BaseUserManager):
    def _create_user(self, username, nombre, apellido, pais, es_Guia, es_Cliente,  password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            nombre=nombre,
            apellido = apellido,
            pais = pais,
            es_Guia = es_Guia,
            es_Cliente = es_Cliente,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, nombre, apellido, pais, es_Guia, es_Cliente, is_staff, password=None, **extra_fields):
        return self._create_user(username, nombre, apellido, pais, es_Guia, es_Cliente, password, is_staff, False, **extra_fields)
    
    def create_superuser(self,username,nombre,apellido, pais, es_Guia, es_Cliente, password = None,**extra_fields):
        return self._create_user(username, nombre, apellido, pais, es_Guia, es_Cliente, password, True, True, **extra_fields)



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
    cantidadpasajeros = models.IntegerField(blank=True, null=True)
    detallesadicionales = models.TextField(blank=True)
    incluircomida = models.BooleanField(default=False)

