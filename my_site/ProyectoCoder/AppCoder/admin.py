from django.contrib import admin

from .models import *

# Register your models here.
class FamiliaresAdmin(admin.ModelAdmin):
        
        list_display = ("nombre","apellido","fechaDeNacimiento","email")
        search_fields = ('nombre',)
        
admin.site.register(Familiares,FamiliaresAdmin)

class PeliculasAdmin(admin.ModelAdmin):

        list_display = ("nombre","genero","anioDeLanzamiento")
        search_fields = ('nombre',)
        
admin.site.register(Peliculas,PeliculasAdmin)

class ButacasAdmin(admin.ModelAdmin):

        list_display = ("nombreReserva","fila","asiento")
        search_fields = ('asiento',)
        
admin.site.register(Butacas,ButacasAdmin)

# admin, admin -> python manage.py createsuperuser