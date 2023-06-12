from django.forms import ModelForm
from .models import Servicio, UsuarioPersonalizado

class TaskForm(ModelForm):
    class Meta:
        model= Servicio
        fields= ['nombre', 'precio', 'ruta', 'HoraInicio', 'HoraFin', 'userUsuarioCustom']

class UsuarioCustomForm(ModelForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['usuario', 'nombre', 'apellido', 'pais', 'es_Guia', 'es_Cliente']


