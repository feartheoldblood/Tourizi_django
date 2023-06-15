from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify



# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_user(self, nombre, password, username, apellido, **otherfields):

        if not username:
            raise ValueError(_('Tienes que dar un username'))

        user = self.model(username = username, nombre = nombre,
                              apellido = apellido, **otherfields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, nombre, password, username, apellido, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(nombre, password, username, apellido, **other_fields)
        

class UsuarioPersonalizado(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    es_Guia = models.BooleanField(default=False, blank=True)
    es_Cliente = models.BooleanField(default=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'pais'
                       ,'es_Guia', 'es_Cliente']

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.TextField(blank=True)
    ruta = models.TextField(blank=True)
    HoraInicio = models.DateTimeField(null=True, blank=True)
    HoraFin = models.DateTimeField(null=True, blank=True)
    userUsuarioCustom = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


