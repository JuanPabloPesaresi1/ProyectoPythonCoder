from distutils.command.upload import upload
import email
from email.mime import image
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)

class Familiares(models.Model):
    
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fechaDeNacimiento=models.IntegerField()
    email=models.EmailField(blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Familiares"
        
    def __str__(self) -> str:
        return f"Nombre : {self.nombre} - Apellido {self.apellido} - Año de Nacimiento {self.fechaDeNacimiento} - E-Mail {self.email}"
    
class Peliculas(models.Model):
    
    nombrePelicula=models.CharField(max_length=40)
    genero=models.CharField(max_length=15)
    anioDeLanzamiento=models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Peliculas"
    
    def __str__(self) -> str:
        return f"Pelicula : {self.nombrePelicula} - Genero {self.genero} - Año de Lanzamiento {self.anioDeLanzamiento}"
    
class Butacas(models.Model):
    
    nombreReserva=models.CharField(max_length=30)
    fila=models.IntegerField()
    asiento=models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Butacas"
    
    def __str__(self) -> str:
        return f"Nombre de la Reserva : {self.nombreReserva} - Fila {self.fila} - Asiento {self.asiento}"