from django import views
from django.urls import path


from .views import *


urlpatterns = [
    #URLS
    path('',index, name="inicio"),
    #TodoLogin
    path('login/',login_user,name="login"),
    path('register/',register_user,name="register"),
    path('logout/', logout_request, name="logout"),
    path('editar_perfil/', edit_user, name="editar_perfil"),
    path('agregar_avatar/', agregar_avatar, name="agregar_avatar"),
    #TodoPeliculas
    path('peliculas/',peliculas, name="peliculas"),
    path('formulario_peliculas/',formulario_peliculas, name="formulario_peliculas"),
    path('eliminar_pelicula/<int:pk>/',eliminar_peliculas, name="eliminar_peliculas"),
    path('modificar_peliculas/<int:pk>/',modificar_peliculas, name="modificar_peliculas"),
    #TodoAsientos
    path('asientos/',asientos, name="asientos"),
    path('butacas/',formulario_butacas, name="formulario_butacas"),
    #TodoContacto
    path('contacto/',contacto, name="contacto"),
    #TodoPersonas
    path('formulario_personas/',formulario_personas, name="formulario_personas"),
    
]
