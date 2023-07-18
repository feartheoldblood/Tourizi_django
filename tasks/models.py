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
    
    def create_superuser(self, username, nombre, apellido, password=None, **extra_fields):
        return self._create_user(username, nombre, apellido, '', False, False, password, True, True, **extra_fields)


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

class Catalogo(models.Model):
    lugar = models.CharField(max_length=100)
    precio = models.TextField(max_length=100)  

class Horario(models.Model):
    dia = models.DateField(max_length=100)
    horaInicio = models.TimeField(max_length=100)
    horaFin = models.TimeField(max_length=100)

class Guia(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="fotos",null=True)
    calificacion_promedio = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_calificaciones = models.PositiveIntegerField(default=0)
    nombre_servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE, null=True)

    def actualizar_calificacion(self, nueva_calificacion):
        # Calcular el promedio de calificaciones actualizado
        nuevo_total_calificaciones = self.total_calificaciones + 1
        nuevo_promedio = (
            (self.calificacion_promedio * self.total_calificaciones) + nueva_calificacion
        ) / nuevo_total_calificaciones

        # Actualizar los campos del taxista
        self.calificacion_promedio = nuevo_promedio
        self.total_calificaciones = nuevo_total_calificaciones
        self.save()

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.TextField(blank=True)
    ruta = models.TextField(blank=True)
    horario = models.ForeignKey(Horario, null=True, on_delete=models.CASCADE)
    userUsuarioCustom = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cantidadpasajeros = models.TextField(blank=True, null=True)
    detallesadicionales = models.TextField(blank=True)
    incluircomida = models.BooleanField(default=False)
    catalogo = models.ForeignKey(Catalogo, null=True, on_delete=models.CASCADE)
    cantidadGuias = models.ForeignKey(Guia, null=True, on_delete=models.CASCADE)


class Pago(models.Model):
    titular = models.TextField(max_length=100)
    monto = models.TextField(max_length=100)


class Rutas(models.Model):
    nombre = models.TextField(max_length=100)
    lugares = models.TextField(max_length=100)

class Reserva(models.Model):
    userUsuarioCustom = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Ruta = models.ForeignKey(Rutas, null=True, on_delete=models.CASCADE)
    Pago = models.ForeignKey(Pago, null=True, on_delete=models.CASCADE)


    


