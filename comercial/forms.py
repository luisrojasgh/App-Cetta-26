from django import forms
from .models import Usuario
from enum import Enum


class TipoDocumento(Enum):
    CC = 'Cédula'
    TI = 'Tarjeta de Identidad'
    CE = 'Cédula de Extranjería'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class RegistroUsuario(forms.Form):
    username = forms.CharField(label='Nombre de usuario/a', required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'username',
                                    'placeholder': 'Nombre de usuario/a para la aplicación. "mínimo 5 caracteres."'
                                }))
    first_name = forms.CharField(label='Nombres', required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'first_name',
                                    'placeholder': 'Tu nombre'
                                }))
    last_name = forms.CharField(label='Apellidos', required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'last_name',
                                    'placeholder': 'Tus apellidos'
                                }))

    email = forms.EmailField(label='Correo electrónico', required=True,
                                widget=forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'id': 'email',
                                    'placeholder': 'tucorreo@correo.com'
                                }))
    password = forms.CharField(label='Contraseña', required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Tu contraseña'
                                }))
    password2 = forms.CharField(label='Confirmar contraseña',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Repite tu contraseña'
                                }))
    tipo_documento = forms.ChoiceField(choices=TipoDocumento.choices(), required=True,
                                       widget=forms.Select(attrs={
                                           'class': 'form-control',
                                           'id': 'tipo_documento'
                                       }))

    documento = forms.IntegerField(required=True,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'documento',
                                    'placeholder': 'Tu número de documento de identidad'
                                }))
    numero_telefono = forms.CharField(label='Número de teléfono fijo', required=False,  
                                       max_length=15,
                                       widget=forms.TextInput(attrs={
                                           'class': 'form-control',
                                           'id': 'numero_telefono',
                                           'placeholder': 'Tu número de teléfono fijo'
                                       }))
    numero_celular = forms.CharField(label='Número de celular', required=True,
                                     max_length=20,
                                     widget=forms.TextInput(attrs={
                                         'class': 'form-control',
                                         'id': 'numero_celular',
                                         'placeholder': 'Tu número de celular'
                                     }))
    direccion = forms.CharField(label='Dirección', required=True,
                                max_length=200,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'direccion',
                                    'placeholder': 'Tu dirección de residencia'
                                }))
    municipio = forms.CharField(required=True,
                                max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'municipio',
                                    'placeholder': 'El Municipio donde vives'
                                }))
    barrio_vereda = forms.CharField(label='Barrio o Vereda', required=True,
                                    max_length=50,
                                    widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'barrio_vereda',
                                        'placeholder': 'El Barrio o Vereda donde vives'
                                    }))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError('!Atención¡ Ingresa otro nombre de usuario/a. El nombre de usuario está siendo usado por otro usuario/a.')
        return username
    
    def clean_documento(self):
        documento = self.cleaned_data.get('documento')

        if Usuario.objects.filter(documento=documento).exists():
            raise forms.ValidationError('!Atención¡ Ingresa otro numero de documento. El que ingresaste está siendo usado por otro usuario/a.')

        return documento
    
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', '!Atención¡ La contraseña no coincide.')



    
            