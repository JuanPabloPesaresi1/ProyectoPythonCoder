from django.urls import path

from .views import *


urlpatterns = [
    #URLS
    path("",index, name="inicio"),
    path('peliculas/',peliculas, name="peliculas"),
    path('asientos/',asientos, name="asientos"),
    path('contacto/',contacto, name="contacto"),
    path('formulario_peliculas/',formulario_peliculas, name="formulario_peliculas"),
    path('butacas/',formulario_butacas, name="formulario_butacas"),
    path('formulario_personas/',formulario_personas, name="formulario_personas"),
    path('busqueda_pelicula/',busqueda_pelicula, name="busqueda_pelicula"),
    
    
    # path('base/',base),     
]
