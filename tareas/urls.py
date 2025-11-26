from django.urls import path
from . import views

urlpatterns = [
    # Página principal: lista de tareas
    path("", views.lista_tareas, name="lista_tareas"),
]
