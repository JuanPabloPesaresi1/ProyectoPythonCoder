from django.urls import path

from .views import *


urlpatterns = [
    
    path("",index),
    path('profesores/',profesores),
    path('estudiantes/',estudiantes),
    path('cursos/',cursos),    
]
