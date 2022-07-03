from dataclasses import fields
from django.forms import ModelForm
from django import forms
from .models import *

class formularioPeliculas(ModelForm):
    class Meta :
        model = Peliculas
        fields = '__all__'
        
        
