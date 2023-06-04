from django.contrib import admin
from .models import Servicio, UsuarioCliente, UsuarioGuia
# Register your models here.
admin.site.register(Servicio)
admin.site.register(UsuarioCliente)
admin.site.register(UsuarioGuia)