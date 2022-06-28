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

def estudiantes(request):
    
    personas=Familiares.objects.all()
    
    return render(request,"estudiantes.html",{"nombre":personas})

def profesores(request):
    return render(request,"profesores.html")

def cursos(request):
    
    personas=Familiares.objects.all()
    
    return render(request,"cursos.html",{"nombre":personas})