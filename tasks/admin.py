from django.contrib import admin
from .models import Servicio, UsuarioPersonalizado, Catalogo, Pago, Reserva, Rutas, Guia, Horario



# Register your models here.
admin.site.register(Servicio)
admin.site.register(UsuarioPersonalizado)
admin.site.register(Catalogo)
admin.site.register(Pago)
admin.site.register(Reserva)
admin.site.register(Rutas)
admin.site.register(Guia)
admin.site.register(Horario)