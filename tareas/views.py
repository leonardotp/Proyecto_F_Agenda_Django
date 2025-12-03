from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea

def lista_tareas(request):
    pendientes = Tarea.objects.filter(completada=False).order_by('prioridad')
    completas = Tarea.objects.filter(completada=True).order_by('-fecha_actualizacion')
    return render(request, "tareas/lista.html", {
        "pendientes": pendientes,
        "completas": completas
    })


def crear_tarea(request):
    if request.method == "POST":
        codigo = request.POST.get("codigo")
        titulo = request.POST.get("titulo")
        prioridad = request.POST.get("prioridad")
        fecha = request.POST.get("fecha")
        etiquetas = request.POST.get("etiquetas")
        descripcion = request.POST.get("descripcion")

        Tarea.objects.create(
            codigo=codigo,
            titulo=titulo,
            prioridad=prioridad,
            fecha=fecha if fecha else None,
            etiquetas=etiquetas,
            descripcion=descripcion
        )

        return redirect("lista_tareas")

    return render(request, "tareas/crear.html")


def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if request.method == "POST":
        id = request.POST.get("codigo")
        tarea.titulo = request.POST.get("titulo")
        tarea.prioridad = request.POST.get("prioridad")
        tarea.fecha = request.POST.get("fecha") or None
        tarea.etiquetas = request.POST.get("etiquetas")
        tarea.descripcion = request.POST.get("descripcion")
        tarea.save()

        return redirect("lista_tareas")

    return render(request, "tareas/editar.html", {
        "tarea": tarea
    })


def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    return redirect("lista_tareas")


def toggle_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect("lista_tareas")
