from django.contrib import admin
from .models import Servicio, UsuarioPersonalizado
#cambio pasarela
from .models import Product


# Register your models here.
admin.site.register(Servicio)
admin.site.register(UsuarioPersonalizado)
#cambio pasarela
admin.site.register(Product)
#admin.site.register(Product)
