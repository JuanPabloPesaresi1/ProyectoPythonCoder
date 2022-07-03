import email
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import Context, Template
from AppCoder.models import *
from django.db.models import Q
from .forms import formularioPeliculas
from django.forms.models import inlineformset_factory
from django.db.models import DEFERRED

# Create your views here.

def index(request):
    
    personas=Familiares.objects.all()
    
    ctx={"familia":personas}
    
    return render(request,"index.html",ctx)

def asientos(request):
    
    butacas=Butacas.objects.all()
    
    ctx={"asientos":butacas}
    
    return render(request,"asientos.html",ctx)

def peliculas(request):    
    pelis=Peliculas.objects.all()
    
    ctx={"peliculas":pelis}
    
    return render(request,"peliculas.html",ctx)

def contacto(request):
    
    personas=Familiares.objects.all()
    
    return render(request,"contacto.html",{"nombre":personas})

def base(request):
    return render(request,"base.html")

def formulario_peliculas(request):
    
    if request.method == "POST":
        
        info_formulario = request.POST
        
        pelicula = Peliculas(nombrePelicula=info_formulario["nombrePelicula"],genero=info_formulario["genero"],anioDeLanzamiento=int(info_formulario["anioDeLanzamiento"]))
        
        pelicula.save()
        
        return redirect("peliculas")
    
    return render(request,"formulario_peliculas.html")

def formulario_butacas(request):
    
    
    if request.method == "POST":
        
        info_formulario = request.POST
        
        butacas = Butacas(nombreReserva=info_formulario["nombreReserva"],fila=int(info_formulario["fila"]),asiento=int(info_formulario["asiento"]))
        
        butacas.save()
        
        return redirect("asientos")
    
    return render(request,"formulario_butacas.html")

def busqueda_pelicula(request):
    if request.method == "POST":
        
        pelis=request.POST["pelicula"]
        
        peliculasBusqueda =Peliculas.objects.filter(nombrePelicula__icontains=pelis)
        
        return render(request,"busqueda_pelicula.html",{"peliculas":peliculasBusqueda})
    
    else:
        
        peliculasBusqueda=[]
    
        return render(request,"busqueda_pelicula.html",{"peliculas":peliculasBusqueda})

def formulario_personas(request):
    if request.method == "POST":
        
        info_formulario = request.POST
        
        personas = Familiares(nombre=info_formulario["nombre"],apellido=info_formulario["apellido"],fechaDeNacimiento=int(info_formulario["fechaDeNacimiento"]),email=info_formulario["email"])
        
        personas.save()
        
        return redirect("inicio")
    
    return render(request,"formulario_personas.html")

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


