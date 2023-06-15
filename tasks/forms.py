from django import forms
from django.forms import ModelForm
from .models import Servicio, UsuarioPersonalizado


class UserLoginForm(forms.Form):


    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'loginUsername',
                'type': 'username',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
    widget=forms.PasswordInput(attrs={
            'id': 'loginPassword',
            'type': 'password',
            'class': 'form-control',
        })
    )

class UserSignUpForm(forms.Form):



    

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'signupUsername',
                'type': 'username',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'signupPassword',
                'type': 'password',
                'class': 'form-control'
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control'
            }
        ))


    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'nombre',
                'class': 'form-control'
            }
        )
    )

    apellido = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'apellido',
                'class': 'form-control'
            }
        )
    )

    pais = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'pais',
                'class': 'form-control'
            }
        )
    )

    es_Guia = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'type': 'es_Guia',
                'class': 'form-control'
            }
        )
    )

    es_Cliente = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'type': 'es_Cliente',
                'class': 'form-control'
            }

        )
    )

    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return cd['password2']





    

    

    






"""class TaskForm(ModelForm):
    class Meta:
        model= Servicio
        fields= ['nombre', 'precio', 'ruta', 'HoraInicio', 'HoraFin', 'userUsuarioCustom']

class UsuarioCustomForm(ModelForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'nombre', 'apellido', 'pais', 'es_Guia', 'es_Cliente']
"""

