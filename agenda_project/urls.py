# Importes para los modulos y las funciones de las URLs de Django
from django.contrib import admin
from django.urls import path, include

# RUTAS CENTRALES DEL PROYECTO 
urlpatterns = [
    # Ruta para el panel de control
    path("admin/", admin.site.urls),

    # Ruta para manejar todas las funciones de las tareas
    path("tareas/", include("tareas.urls")),
]
