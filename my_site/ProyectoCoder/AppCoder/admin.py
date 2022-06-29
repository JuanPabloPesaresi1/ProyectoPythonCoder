from django.contrib import admin

from .models import *

# Register your models here.
class FamiliaresAdmin(admin.ModelAdmin):
        
        list_display = ("nombre","apellido","fechaDeNacimiento","email")
        search_fields = ('nombre',"apellido","fechaDeNacimiento","email")
        
admin.site.register(Familiares,FamiliaresAdmin)

class PeliculasAdmin(admin.ModelAdmin):

        list_display = ("nombrePelicula","genero","anioDeLanzamiento")
        search_fields = ('nombre',"genero","anioDeLanzamiento")
        
admin.site.register(Peliculas,PeliculasAdmin)

class ButacasAdmin(admin.ModelAdmin):

        list_display = ("nombreReserva","fila","asiento")
        search_fields = ('nombreReserva',"fila","asiento")
        
admin.site.register(Butacas,ButacasAdmin)

# admin, admin -> python manage.py createsuperuser