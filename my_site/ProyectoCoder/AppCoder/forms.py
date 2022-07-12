from pyexpat import model
from dataclasses import field, fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class formularioPeliculas(ModelForm):
    class Meta :
        model = Peliculas
        fields = '__all__'
        

class familiaresFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    fechaDeNacimiento=forms.IntegerField()
    email=forms.EmailField()
    
class peliculasFormulario(forms.Form):
    
    nombrePelicula=forms.CharField(max_length=40)
    genero=forms.CharField(max_length=15)
    anioDeLanzamiento=forms.IntegerField()
    
class butacasFormulario(forms.Form):
    
    nombreReserva=forms.CharField(max_length=30)
    fila=forms.IntegerField()
    asiento=forms.IntegerField()
    
class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', 'first_name', 'last_name']

        help_texts = {k:"" for k in fields}
    
class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

        help_texts = {k:"" for k in fields}
        

class AvatarForm(forms.Form):

    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:
        model = Avatar
        fields = ['imagen']