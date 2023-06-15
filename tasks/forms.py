from django import forms
from django.forms import ModelForm
from .models import Servicio, UsuarioPersonalizado


class FormularioUsuario(forms.ModelForm):
    """Formulario de registro de un usuario en la bd"""
    """Password 1 es la contraseña y password 2 es la verificacion"""

    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese su contraseña...',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label = 'Contraseña de confirmacion',
        widget = forms.PasswordInput( attrs = {
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required': 'required',
        }
     ))
    
    class Meta:
        model = UsuarioPersonalizado
        fields = ('username', 'nombre', 'apellido')
        widget = {
            'username': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Correo username',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su nombre',
                }        
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese sus apellidos'
                }
            )
        }


    

    

    






