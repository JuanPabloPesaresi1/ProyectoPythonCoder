from django import views
from django.urls import path

from .views import *


urlpatterns = [
    #URLS
    path("",index, name="inicio"),
    path('peliculas/',peliculas, name="peliculas"),
    path('eliminar_pelicula/<int:pk>/',eliminar_peliculas, name="eliminar_peliculas"),
    path('modificar_peliculas/<int:pk>/',modificar_peliculas, name="modificar_peliculas"),
    path('busqueda_pelicula/',busqueda_pelicula, name="busqueda_pelicula"),
    path('asientos/',asientos, name="asientos"),
    path('contacto/',contacto, name="contacto"),
    path('formulario_peliculas/',formulario_peliculas, name="formulario_peliculas"),
    path('butacas/',formulario_butacas, name="formulario_butacas"),
    path('formulario_personas/',formulario_personas, name="formulario_personas"),
    
    
    
    # path('base/',base),     
]
