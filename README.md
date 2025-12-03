# MODELADO Y PROGRAMACIÓN 
# PROYECTO FINAL - AGENDA WEB CON DJANGO
# Facultad de Ciencias, UNAM
# Carranza Bolaños Jatniel
# Téllez Peña Leonardo


EL proyecto gira al rededor de una agenda de tareas en donde reutilizamos la base de los proyectos anteriores, así mismo, agregamos funcionalidades en html y css integrados desde Django para poder hacer la agenda web. 
El PDF solicitaba ciertas funcionalidades que se fueron agregando en el desarrollo del proyecto, tales como:

- Registrar tareas con un ID único, un título y una prioridad.
- Poder marcar tareas como completadas o volverlas a poner como pendientes.
- Guardar la fecha en la que se completó una tarea.
- Eliminar tareas que ya no necesitemos.
- Panel central 

El desarrollo lo dividimos en dos ramas principales, el frontend y el backend en donde cada integrante del equipo desarrollamos una y una.

## Estructura del proyecto

Más allá de cómo nos dividimos el desarrollo de entre frontend y backend el proyecto tiene dos secciones principales, la parte de la app que modela las tareas y la otra que es la parte con Django.

Ahora, en el proyecto lo tenemos dividido en carpetas, en donde cada una de estas contiene información de distinto tipo pero igual de importante:

- Carpeta `agenda_project/`  
  Aquí viene la configuración general de Django, tiene el `settings.py` donde se conectan las apps y la base de datos, también está el `urls.py` principal que es el que va a mandar todo lo que empiece con `/tareas/` hacia la app.

- Carpeta `tareas/`  
  Esta es la app que va a modelar toda la parte de las tareas, aquí está `models.py` con el modelo de `Tarea` que define cómo se guarda cada tarea en la base de datos y que es el objeto central del proyecto.
  También está el archvo`views.py` que es el que tiene las funciones para listar, crear, completar y eliminar tareas.
  En el documento`urls.py` están  las rutas internas de la app 
  y en `templates/tareas/`  están las plantillas que vienen por defecto de HTML.

- También hay algunos archivos raíz que no afectan directamente en el funcionamiento pero que también son necesarios:
  - `manage.py` es el script que se usó para correr el servidor, hacer migraciones, crear superusuarios, etc.  
  - `requirements.txt` lleva el registro de las dependencias para que otra persona pueda instalar el proyecto igual que nosotros.

## Instrucciones para ejecutar nuestro proyecto

- Clonar el repositorio desde https://github.com/leonardotp/Proyecto_F_Agenda_Django.git
- Activar tu entorno virtual (dependiendo desdde que sistema operativo lo vayas a ejecutar)
- Instalar dependencaias y crear un superusuario para poder ejecutarlo
- Arrancar el servidor


## Tecnologías que usamos durante el desarrollo     

- Python 3
- Django 5
- SQLite (base de datos por defecto de Django)
- HTML

##  Funcionalidades principales

### Lista completa de las tareas (`/tareas/`)

Esta función nos permite ver una lista completa de las tareas en donde se puede ver todda la información de las tareas, su código, nombre, estado y fecha.

### Crear nueva tarea (`/tareas/nueva/`)

Esta funcionalidad es para crear una nueva tarea que eventualmente se va a agregar a la lista general de tares. 

Para crear una nueva tarea tienes que llenar un formulario con todos los aspectos de esa nueva tarea.

También le agregamos una excepción para cuando quiaras agregar una nueva tarea con ID único, entonces ahí no se puede porque es justo el objetivo de ese ID.
  
### Marcar como completada / pendiente

Esta es una fucnión que lo único que hace es cambiar de estado una tarea, si se activa en una tarea en estado pendiente se cambia a realizada y veceversa.

### Eliminar una tarea

Primero buscamos una tarea oor su ID único, si no la encuentra nos manda a un 404 y si si la encuentra la quita de la lista de tareas.

### Panel central

Ess una vista en donde podemos manipular las tareas y hacer operaciones sobre ellas.

## Pruebas 

Antes de dar por bueno el backend, probé a mano los casos que podían romper la app o darnos datos raros. Más o menos seguí esta idea:

- **Crear tareas normales**  
  - Entré a `/tareas/nueva/`, llené código, título y prioridad, y verifiqué que aparecieran en la lista.  
  - Revisé en el admin que se estuvieran guardando con los mismos datos y con el campo `completada` en `False` al inicio.

- **Intentar repetir el mismo código**  
  - Volví a `/tareas/nueva/` e intenté registrar una tarea con un código que ya existía (por ejemplo `001`).  
  - En lugar de la pantalla amarilla de error, ahora se queda en el formulario y muestra el mensaje de que ese código ya está ocupado, pero sin borrar lo que yo había escrito.

- **Marcar y desmarcar como completada**  
  - Desde `/tareas/` usé el enlace de “Marcar como completada” y confirmé que el texto cambiara a “completada en …”.  
  - Luego volví a presionar el enlace de “Marcar como pendiente” y revisé que regresara al estado original.  
  - También verifiqué en el admin que el campo `completada` cambiara entre `True` y `False`, y que la fecha se estuviera actualizando cuando tocaba.

- **Eliminar tareas**  
  - Probé el enlace de “Eliminar” en la lista y confirmé que la tarea desapareciera de `/tareas/`.  
  - Revisé en el admin que tampoco apareciera ahí, para asegurarme de que sí se borró de la base de datos.

- **Comportamiento sin tareas**  
  - Después de borrar todas las tareas, abrí `/tareas/` otra vez para validar que no tronara nada y que se mostrara el mensaje de “No hay tareas todavía”, en lugar de una lista vacía rara.

Con estas pruebas me aseguré de que el flujo básico (crear, listar, completar/pendiente y eliminar) si trabaje bien y que los errores más comunes no nos tiraran la app.

## Posibles mejoras

Si tuviera que seguir perfeccionando el proyecto algunas implementaciones que haría serían:

- Agregar validaciones más estrictas en el formulario (por ejemplo, prioridad solo dentro de un rango válido).

- Manejar todavía más mensajes a lo largo de las operaciones sobre las tareas.

## Conclusiones

### Leonardo Téllez Peña
Al final, el proyecto  cumplió con las métricas del PDF y sentí que realmente estabammos desarrollando algo funcional, algo que yo usaría.

También al ser mi primera vez haciendo un proyecto del estilo encontré el proyecto entretenido ya que era algo muy visual, algo que podías ver ell progreso de forma tangible, lo que también me ayudó a identificar posibles areas de mejora y corrección de errores.

Otra cosa que me resultó interesante es que durante el desarrollo del proyecto usamos muchas cosas que usualmente se quedaban en teoría en otras materias y el hecho de ver una base de datos, una página y a Visual Studio code trabajando juntos me llamó mucho a atención.
