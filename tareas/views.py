# Imports para renderizar plantillas, redirigir los links y traer objetos o ya directamente el 404,
# también para obtener la fecha del server e importar el modelo que ya tenía para la tarea 
from django.shortcuts import render, redirect, get_object_or_404  
from django.utils import timezone                                   
from .models import Tarea                                           

# Lista completa de las tareas impresa
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "tareas/lista_tareas.html", {"tareas": tareas})


# Vista para cuando agregamos una nueva tareaa
def crear_tarea(request):
    if request.method == "POST":
        codigo = request.POST.get("codigo")
        titulo = request.POST.get("titulo")
        prioridad = request.POST.get("prioridad")
        completada = request.POST.get("completada") == "on"

        # Guardo la fecha actual
        fecha_hoy = timezone.now().date()

        # Se revisa que no haya una tarea con el mismo codigo, si si ya había una con el
        # mismo código manda una alerta 
        if Tarea.objects.filter(codigo=codigo).exists():
            # Si ya hay una tarea con ese código, regreso al formulario con un mensajito
            contexto = {
                "error": "Ya existe una tarea con ese código. intenta con otro.",
                "codigo": codigo,
                "titulo": titulo,
                "prioridad": prioridad,
                "completada": completada,
            }
            return render(request, "tareas/crear_tarea.html", contexto)

        #  Si el ID es nuevo entonces si creo la nueva tarea 
        Tarea.objects.create(
            codigo=codigo,
            titulo=titulo,
            prioridad=prioridad,
            completada=completada,
            fecha=fecha_hoy,
        )

        # Cuando se termine este proceso volvemos a la lista con todas las tareas
        return redirect("lista_tareas")
    return render(request, "tareas/crear_tarea.html")


# Vista para marcar o desmarcar una tarea como completada
def completar_tarea(request, codigo):
    tarea = get_object_or_404(Tarea, codigo=codigo)
    # Aca solo se invierte el estado
    tarea.completada = not tarea.completada
    tarea.save()
    # Cuando se terminen los cambios se regresa la lista con estos cambios ya reflejados 
    return redirect("lista_tareas")


# Vista para cuando eliminamos una tarea específica
def eliminar_tarea(request, codigo):
    # Igual que en nuestro otro caso se manda a  404 si no la encuentra el programa
    tarea = get_object_or_404(Tarea, codigo=codigo)
    # Si si se encontró entonces ya solo se borra la tarea de la base de datos
    tarea.delete()
    # Se regresa la lista ya sin la tarea que quitamos 
    return redirect("lista_tareas")
