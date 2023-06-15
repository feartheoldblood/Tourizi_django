from django import forms
from django.forms import ModelForm
from .models import Servicio, UsuarioPersonalizado
from django.contrib.auth.forms import AuthenticationForm

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class']= 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

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
        fields = ('username', 'nombre', 'apellido', 'pais', 'es_Guia', 'es_Cliente')
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
            ),
            'pais' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su pais de residencia'
                }
            ),
            'es_Guia' : forms.CheckboxInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : '¿Usted es guia?'
                }
            ),
            'es_Cliente' : forms.CheckboxInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : '¿Usted es cliente?'
                }
            )
        }

    def clean_password2(self):
        """ Validación de Contraseña

        Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas
        y guardadas en la base dedatos, Retornar la contraseña Válida.

        Excepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2

    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    

    

    






