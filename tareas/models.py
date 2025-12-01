from django.db import models

class Tarea(models.Model):
    # ID humano tipo "T-0001". Django ya tiene un id numérico interno,
    # esto es solo para mantener el estilo de tu proyecto viejo.
    codigo = models.CharField(max_length=10, unique=True, null=True, blank=True)

    # Lo que antes era --titulo
    titulo = models.CharField(max_length=200)

    # Lo que antes era --fecha (YYYY-MM-DD). Puede venir vacío.
    fecha = models.DateField(null=True, blank=True)

    # --prioridad (1 a 5). Ponemos 3 por defecto como en el proyecto viejo.
    prioridad = models.IntegerField(default=3)

    # --etiquetas, como texto separado por comas, igual que antes.
    etiquetas = models.CharField(
        max_length=255,
        blank=True,
        help_text="Escribe etiquetas separadas por comas, por ejemplo: estudio,python"
    )

    # --descripcion (puede ir vacía)
    descripcion = models.TextField(blank=True)

    # Para saber si está completada (lo que antes hacías con done)
    completada = models.BooleanField(default=False)

    # Campos automáticos para tener control de cuándo se creó / actualizó
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk and not self.codigo:
            last = Tarea.objects.order_by('-id').first()
            next_number = 1 if not last else last.id + 1
            self.codigo = f"T-{next_number:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} - {self.titulo}"