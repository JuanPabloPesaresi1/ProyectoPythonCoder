import email
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from AppCoder.models import *

# Create your views here.

def index(request):
        
    nombre="juan"
    apellido="pesaresi"
    fecha="2001"
    email="juanpablopesaresi@gmail.com"
    
    familia= Familiares(nombre=nombre,apellido=apellido,fechaDeNacimiento=fecha,email=email)
    
    familia.save()
    
    personas=Familiares.objects.all()
    
    ctx={"familia":personas}
    
    return render(request,"index.html",ctx)

def asientos(request):
    
    personas=Familiares.objects.all()
    
    return render(request,"asientos.html",{"nombre":personas})

def peliculas(request):
    return render(request,"peliculas.html")

def contacto(request):
    
    personas=Familiares.objects.all()
    
    return render(request,"contacto.html",{"nombre":personas})

def base(request):
    return render(request,"base.html")