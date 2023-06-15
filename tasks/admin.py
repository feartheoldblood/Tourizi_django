from django.contrib import admin
from .models import Servicio, UsuarioPersonalizado
from django.contrib.auth.admin import UserAdmin
from .forms import UserSignUpForm

# Register your models here.
admin.site.register(Servicio)

class UsuarioPersonalizadoAdmin(UserAdmin):
    form = UserSignUpForm

admin.site.register(UsuarioPersonalizado)
