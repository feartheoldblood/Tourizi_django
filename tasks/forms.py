from django.forms import ModelForm
from .models import Task, UsuarioCliente

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=['title','description','important']

class UsuarioClienteForm(ModelForm):
    class Meta:
        model = UsuarioCliente
        fields = ['nombre', 'apellido', 'pais']