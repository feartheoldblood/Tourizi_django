from django.forms import ModelForm
from .models import Servicio, UsuarioCliente, UsuarioGuia

class TaskForm(ModelForm):
    class Meta:
        model=Servicio
        fields=['nombre', 'precio', 'ruta', 'HoraInicio', 'HoraFin', 'userCliente', 'userGuia']

class UsuarioClienteForm(ModelForm):
    class Meta:
        model = UsuarioCliente
        fields = ['nombre', 'apellido', 'pais']

class UsuarioGuiaForm(ModelForm):
    class Meta:
        model = UsuarioGuia
        fields = ['nombre', 'apellido', 'pais', 'placa']