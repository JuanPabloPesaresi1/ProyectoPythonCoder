import email
from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class Familiares(models.Model):
    
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fechaDeNacimiento=models.IntegerField()
    email=models.EmailField(blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Familiares"
    
class Peliculas(models.Model):
    
    nombrePelicula=models.CharField(max_length=40)
    genero=models.CharField(max_length=15)
    anioDeLanzamiento=models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Peliculas"
    
    
class Butacas(models.Model):
    
    nombreReserva=models.CharField(max_length=30)
    fila=models.IntegerField()
    asiento=models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Butacas"