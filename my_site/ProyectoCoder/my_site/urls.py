from django import views
from django.contrib import admin
from django.urls import path,include
from my_site.views import *
from AppCoder import views


urlpatterns = [
    path('admin/', admin.site.urls),
        
    #URLS DE LA APP
    path('appcoder/',include('AppCoder.urls')),
]
