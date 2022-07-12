from distutils.log import info
from re import template
import re
from tkinter.messagebox import RETRY
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import Context, Template
from AppCoder.models import *
from django.db.models import Q
from .forms import butacasFormulario, familiaresFormulario, formularioPeliculas, peliculasFormulario
from django.forms.models import inlineformset_factory
from django.db.models import DEFERRED
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
import datetime


# Create your views here.

def entrada(request):
    return redirect("inicio")

def index(request):
    ctx={"familia":familiar}
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "/media/avatar/generica.png"
        return render(request,"index.html",ctx,{"url":url})
    familiar=Familiares.objects.all()
    
    
    
    return render(request,"index.html",ctx,{"url":url})
    

@login_required
def peliculas(request):    
    
    if request.method == "POST":
        
        search = request.POST["search"]
        
        if search != "":
            peliculas = Peliculas.objects.filter(Q(nombrePelicula__icontains=search) | Q(genero__icontains=search) ).values()
            
            return render(request,"peliculas.html",{"peliculas":peliculas, "search":True, "busqueda":search})
    
    pelis=Peliculas.objects.all()
    
    ctx={"peliculas":pelis}
    
    return render(request,"peliculas.html",ctx)

def eliminar_peliculas(request, pk):
    
    pelicula= get_object_or_404(Peliculas, id=pk)
    pelicula.delete()
    
    return redirect('peliculas')

def modificar_peliculas(request,pk):
    
    peliculas = Peliculas.objects.get(id=pk)

    if request.method == "POST":

        formulario = formularioPeliculas(request.POST)

        if formulario.is_valid():
            
            info_peliculas = formulario.cleaned_data
            
            peliculas.nombrePelicula = info_peliculas["nombrePelicula"]
            peliculas.genero = info_peliculas["genero"]
            peliculas.anioDeLanzamiento = info_peliculas["anioDeLanzamiento"]
            peliculas.save()

            return redirect("peliculas")

    # get
    formulario = formularioPeliculas(initial={"nombrePelicula":peliculas.nombrePelicula, "genero":peliculas.genero, "anioDeLanzamiento": peliculas.anioDeLanzamiento})
    
    return render(request,"modificar_peliculas.html",{"form":formulario})

def formulario_peliculas(request):
    
    if request.method == "POST":
        
        formulario= peliculasFormulario(request.POST)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
        
            pelicula = Peliculas(nombrePelicula=info["nombrePelicula"],genero=info["genero"],anioDeLanzamiento=int(info["anioDeLanzamiento"]))
            pelicula.save()
        
        return redirect("peliculas")
    
    return render(request,"formulario_peliculas.html")

def busqueda_pelicula(request):
    if request.method == "POST":
        
        pelis=request.POST["pelicula"]
        
        peliculasBusqueda =Peliculas.objects.filter(nombrePelicula__icontains=pelis)
        
        return render(request,"busqueda_pelicula.html",{"peliculas":peliculasBusqueda})
    
    else:
        
        peliculasBusqueda=[]
    
        return render(request,"busqueda_pelicula.html",{"peliculas":peliculasBusqueda})


@login_required
def contacto(request):
    
    personas=Familiares.objects.all()
    
    return render(request,"contacto.html",{"nombre":personas})

def base(request):
    return render(request,"base.html")


def formulario_butacas(request):
    
    if request.method == "POST":
        
        formulario=butacasFormulario(request.POST)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            butacas = Butacas(nombreReserva=info["nombreReserva"],fila=int(info["fila"]),asiento=int(info["asiento"]))
            butacas.save()
        
        return redirect("asientos")
    
    return render(request,"formulario_butacas.html")


@login_required
def asientos(request):
    
    butacas=Butacas.objects.all()
    
    ctx={"asientos":butacas}
    
    return render(request,"asientos.html",ctx)
    


def formulario_personas(request):
    
    
    if request.method == "POST":
        
        formulario=familiaresFormulario(request.POST)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
        
            personas = Familiares(nombre=info["nombre"],apellido=info["apellido"],fechaDeNacimiento=int(info["fechaDeNacimiento"]),email=info["email"])

            personas.save()
        
        return redirect("inicio")
    
    return render(request,"formulario_personas.html")


def login_user (request):
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request,"login.html",{"form":form})


def register_user(request):
    if request.method == "POST":
        
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') # es la primer contraseña, no la confirmacion

            form.save() # registramos el usuario
            # iniciamos la sesion
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")

        return render(request,"register.html",{"form":form})

    # form = UserCreationForm()
    form = UserRegisterForm()

    return render(request,"register.html",{"form":form})

def logout_request(request):
    
    logout(request)
    return redirect("inicio")

@login_required
def edit_user (request):
    
    user = request.user # usuario con el que estamos loggueados

    if request.method == "POST":
        
        form = UserEditForm(request.POST) # cargamos datos llenados

        if form.is_valid():

            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            user.save()

            return redirect("inicio")
    else:
        form = UserEditForm(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name})

    return render(request,"editar_usuario.html",{"form":form})


def agregar_avatar(request):
    
    if request.method == "POST":
            
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username) # usuario con el que estamos loggueados

            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])

            # avatar.save()

            # avatar = Avatar()
            # avatar.usuario = request.user
            # avatar.imagen = form.cleaned_data["imagen"]
            avatar.save()

            return redirect("inicio")

    else:
        form = AvatarForm()
    
    return render(request,"agregar_avatar.html",{"form":form})