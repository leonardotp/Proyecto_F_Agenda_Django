from django.db import models

# Mantenemos el ID de tarea único como en los proyectos pasados,
# también mantenemos el concepto de título, la fecha, la prioridad y las etiquetas
class Tarea(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    titulo = models.CharField(max_length=200)
    fecha = models.DateField(null=True, blank=True)
    prioridad = models.IntegerField(default=3)
    etiquetas = models.CharField(
        max_length=255,
        blank=True,
        help_text="Escribe etiquetas separadas por comas, por ejemplo: estudio,python"
    )

    # Caso para cuando va vacía
    descripcion = models.TextField(blank=True)

    # Luego otro caso para saber cuando ya está acabada 
    completada = models.BooleanField(default=False)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo} - {self.titulo}"
