from django.urls import path
from . import views

urlpatterns = [
    # Lista de las tareas
    path("", views.lista_tareas, name="lista_tareas"),
    # Formulario para cuando vamos a crear una nueva tarea
    path("nueva/", views.crear_tarea, name="crear_tarea"),

    # Linea que define si una tarea está o no acabada
    path("completar/<str:codigo>/", views.completar_tarea, name="completar_tarea"),

    # Linea para eliminar una tarea
    path("eliminar/<str:codigo>/", views.eliminar_tarea, name="eliminar_tarea"),
]
