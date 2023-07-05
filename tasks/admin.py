from django.contrib import admin
from .models import Servicio, UsuarioPersonalizado, Catalogo



# Register your models here.
admin.site.register(Servicio)
admin.site.register(UsuarioPersonalizado)
admin.site.register(Catalogo)