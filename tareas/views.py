from django.shortcuts import render, redirect
from .models import Tarea
from django.utils import timezone  # si quieres poner la fecha automática


def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "tareas/lista_tareas.html", {"tareas": tareas})


def crear_tarea(request):
    if request.method == "POST":
        codigo = request.POST.get("codigo")
        titulo = request.POST.get("titulo")
        prioridad = request.POST.get("prioridad")

        # Checkbox de completada (si está marcado viene en el POST)
        completada = request.POST.get("completada") == "on"

        # Si tu modelo tiene campo fecha y permite null, puedes rellenarlo así:
        fecha_hoy = timezone.now().date()

        Tarea.objects.create(
            codigo=codigo,
            titulo=titulo,
            prioridad=prioridad,
            completada=completada,
            fecha=fecha_hoy,
        )

        # Después de guardar, regresamos a la lista
        return redirect("lista_tareas")

    # Si es GET, solo mostramos el formulario vacío
    return render(request, "tareas/crear_tarea.html")
