from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "titulo", "prioridad", "completada", "fecha")
    list_filter = ("completada", "prioridad")
    search_fields = ("codigo", "titulo", "descripcion", "etiquetas")
