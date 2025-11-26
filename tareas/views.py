from django.shortcuts import render
from .models import Tarea

def lista_tareas(request):
    # Por ahora sólo traemos todas las tareas. Después metemos orden y filtros.
    tareas = Tarea.objects.all().order_by('fecha', 'prioridad', 'titulo')
    contexto = {
        "tareas": tareas,
    }
    return render(request, "tareas/lista_tareas.html", contexto)
