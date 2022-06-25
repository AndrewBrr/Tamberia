from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Formulario_Productos(forms.Form):
    
    nombre = forms.CharField(max_length=20)
    calidad = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=20)
    precio = forms.IntegerField()


class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class Formulario_Usuario(forms.Form):
    class meta:
        fields = ['nombre', 'apellido', 'email', 'telefono']
    #nombre = forms.CharField(max_length=50)
    #apellido = forms.CharField(max_length=50)
    #direccion = forms.CharField(max_length=50)
    #email = forms.EmailField()
    #telefono = forms.IntegerField()