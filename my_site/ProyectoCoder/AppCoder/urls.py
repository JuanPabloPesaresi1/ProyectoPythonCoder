from django.urls import path

from .views import *


urlpatterns = [
    #URLS
    path("",index, name="inicio"),
    path('peliculas/',peliculas, name="peliculas"),
    path('asientos/',asientos, name="asientos"),
    path('contacto/',contacto, name="contacto"),
    # path('base/',base),     
]
