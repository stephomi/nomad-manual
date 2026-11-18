# ![](/icons/play.webp) Primeros pasos {#getting-started}

## ¡Bienvenido a Nomad! {#welcome-to-nomad}

Nomad es una aplicación de escultura 3d que funciona en muchos dispositivos, y da lo mejor de sí en tabletas con un lápiz sensible a la presión, por ejemplo un iPad con Apple Pencil o una Samsung Galaxy Tab con su lápiz.

Se inspira en aplicaciones de escultura de escritorio como Zbrush y Blender, con una interfaz fácil de entender que no renuncia a ninguna función. Si ya has usado aplicaciones de escultura 3d, Nomad te resultará muy familiar.

Si es la primera vez que esculpes en 3d, te vendrá bien conocer algunos conceptos básicos.

::: tip ¿Prefieres vídeos?
En Youtube hay ya MUCHOS tutoriales en vídeo para principiantes; aquí tienes algunos enlaces muy buenos:

* [Curso intensivo de Nomad Sculpt, de Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Tutorial de Nomad Sculpt para principiantes, de Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [Serie NOMAD FOR BEGINNERS, de SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

Merece la pena echar un vistazo al canal principal de estos creadores: publican tutoriales nuevos con frecuencia.
:::

## Tu primera escultura {#your-first-sculpt}

La primera vez que abras Nomad verás una esfera en la pantalla. Basta con arrastrar el lápiz sobre la esfera para empezar a esculpir. La simetría está activada por defecto para que esculpir sea más fácil.

![](/videos/gettingstarted_01.mp4)

Para hacer el pincel más grande o más pequeño, usa el regulador de radio de la izquierda.

![](/videos/gettingstarted_02.mp4)

Para hacer el pincel más fuerte o más suave, usa el regulador de intensidad de la izquierda.

![](/videos/gettingstarted_03.mp4)

La herramienta por defecto es `Arcilla`, que añade material a la superficie. Para quitar material, pulsa el botón `Sub` de la izquierda. Para volver a añadir, pulsa de nuevo el botón Sub.

![](/videos/gettingstarted_04.mp4)

Para suavizar la superficie, pulsa el botón `Suavizar`. Para volver a esculpir con normalidad, pulsa de nuevo el botón Suavizar.

![](/videos/gettingstarted_05.mp4)

Para girar alrededor del modelo, arrastra en el espacio vacío fuera del modelo.

![](/videos/gettingstarted_06.mp4)

Para hacer zoom, usa el gesto de pellizcar con dos dedos.

![](/videos/gettingstarted_07.mp4)

Para desplazar la cámara, apoya 2 dedos en la pantalla y arrastra.

![](/videos/gettingstarted_08.mp4)

Si te equivocas, un toque con 2 dedos deshace la última acción; también puedes usar el botón de deshacer abajo a la izquierda.

![](/videos/gettingstarted_09.mp4)

::: tip Versión de escritorio
En escritorio, la tecla alt/opt sirve para controlar la cámara:

* arrastrar con la punta en el espacio vacío = girar la cámara
* alt + arrastrar con la punta = desplazar
* alt + arrastrar con la punta y luego soltar alt = zoom (igual que en zbrush)

Con las tabletas Wacom cuyo lápiz tiene 2 botones o más, configura la punta y los botones así en los ajustes de Wacom:

* punta = clic izquierdo
* botón inferior = clic central
* botón superior = clic derecho

Con estos ajustes puedes manejar la cámara solo con el lápiz:

* botón superior y mover el lápiz sin tocar = girar la cámara
* botón inferior y mover el lápiz sin tocar = desplazar
:::

## Añadir color {#add-color}

Nomad te permite pintar la superficie de tu escultura. En el menú de herramientas de la derecha, busca la herramienta `Pintar` y púlsala. En la barra de herramientas de la izquierda aparecerá una esfera de color. Púlsala para abrir un selector de color. Elige un color y pinta sobre tu modelo.

![](/videos/gettingstarted_10.mp4)

Para borrar, pulsa el botón `Borrar` de la barra de herramientas izquierda y borra sobre la superficie. Pulsa de nuevo el botón Borrar para volver al modo de pintura.

![](/videos/gettingstarted_11.mp4)

Con el pincel de arcilla en sus modos de añadir y quitar, el suavizado y la pintura, intenta hacer una cabeza de dibujos animados sencilla:

![](/images/gettingstarted_head1.webp)

## Otras herramientas {#other-tools}

La paleta de herramientas tiene muchas herramientas para ayudarte a esculpir. Hasta ahora has usado el pincel de arcilla (la herramienta inicial por defecto), el suavizado y la pintura. Como el suavizado se usa muy a menudo, tiene un acceso directo adicional en la barra de herramientas izquierda.

Las herramientas de Nomad hacen cosas muy variadas, desde herramientas propias de la escultura como mover, pliegue o inflar, hasta herramientas como dividir o recortar, más parecidas a las de carpintería o metalistería. En la página [Herramientas](tools.md) encontrarás más información.

Intenta usar las herramientas mover, pliegue, inflar y suavizar para añadir más detalle a tu cabeza y cambiar su forma:

![](/images/gettingstarted_head2.webp)

Ahora que conoces lo básico de Nomad, veamos el resto de la interfaz.

## Interfaz {#interface}

![](/images/interface_overview1.webp)

* `Menús superiores` - Los menús que dan acceso a la mayoría de las funciones de Nomad. Los menús de arriba a la izquierda tratan sobre todo de la escena y los objetos; los de arriba a la derecha están relacionados con las herramientas. En pantallas pequeñas, estos menús se agrupan para ahorrar espacio.
* `Estadísticas` - Información sobre la escena, el objeto actual, el estado de la máscara y el uso de memoria.
* `Cubo de navegación` - Una ayuda que muestra qué lado de la escultura estás mirando, y también un atajo para saltar a distintas vistas. Al tocar el cubo, la vista salta al lado tocado. Al arrastrar el cubo, la vista gira. Toca los iconos pequeños junto al cubo para encuadrar el objeto actual, volver a la vista inicial por defecto, bloquear la cámara o mostrar la cuadrícula. En la aplicación se llama `Cubo de ajuste`, y puedes cambiar su aspecto y posición en la [Configuración](settings.md#snap-cube).
* `Caja de herramientas` - Las herramientas de Nomad están disponibles en esta zona desplazable.
* `Barra de herramientas izquierda` - Reguladores de radio e intensidad para la mayoría de las herramientas, botones específicos para otras, y atajos para la simetría, el modo alt/sub de la herramienta, el suavizado, la máscara, ocultar, los grupos de caras, el gizmo y las opciones de pintura. Puedes reordenar los atajos en el menú [Interfaz](interface.md#side-bar).
* `Barra de herramientas inferior` - Atajos para las funciones más usadas, que se explican a continuación.

::: tip ¿Eres zurdo?
Puedes invertir la posición y el orden de todas las barras de herramientas; consulta [Invertir barra superior](interface.md#mirror-top-bar) y otras opciones relacionadas.
:::

## Barra de herramientas inferior {#bottom-toolbar}

![](/images/interface_bottom_toolbar.webp)

* `Deshacer` - anula la última operación
* `Rehacer` - restaura la última operación deshecha
* `Historial` - da acceso a las opciones del historial, explicadas en el menú [Historial](history.md).
* `Individual` - Alterna entre mostrar solo el objeto actual o todos los objetos
* `Rayos X` - Muestra todos los demás objetos en modo rayos X y el objeto actual sólido. Con una pulsación larga o deslizando hacia arriba puedes elegir el matcap y el color de los rayos X, y a qué objetos se aplican.
* `Vóxel` - Un atajo al botón de remallado del [Remallado por vóxeles](topology.md#voxel-remesher). Con una pulsación larga o deslizando hacia arriba aparecen las opciones del remallado por vóxeles, como la resolución.
* `Cuadrícula` - Muestra u oculta la cuadrícula. Con una pulsación larga o deslizando hacia arriba aparecen las opciones de la cuadrícula, como su color y el ajuste.
* `Malla alámbrica` - Muestra u oculta la malla alámbrica superpuesta. Con una pulsación larga o deslizando hacia arriba aparecen sus opciones.
* `Inspector` - Muestra u oculta datos adicionales de la malla actual. Por defecto muestra las UV, pero con una pulsación larga o deslizando hacia arriba puedes inspeccionar otras propiedades si existen, y elegir si se muestran en el fondo o sobre la malla.
* `Registros` - Muestra u oculta una ventana con los registros de depuración de Nomad.
* `Grupo de caras` - Muestra u oculta la superposición de grupos de caras; consulta la herramienta [Grupo de caras](tools.md#facegroup).

Puedes añadir, quitar y reordenar estos atajos en el menú [Interfaz](interface.md#add-shortcuts-bottom).

## Siguientes pasos {#next-steps}

¡Lo siguiente que aprendas depende de ti y de lo que te parezca interesante! Aquí tienes algunas sugerencias:

¿Quieres saber más sobre las herramientas de escultura? Ve a la sección [Herramientas](tools.md).

¿Quieres exportar tus modelos? ¿O importar modelos para esculpir sobre ellos? ¿O crear imágenes de tus esculturas? Ve a la sección [Archivos](files.md).

¿Quieres aprender a controlar el detalle de tu escultura? Ve a la sección [Topología](topology.md) y descubre la multiresolución y el diezmado.

¿Quieres trabajar con más objetos? ¿Combinar objetos simples y primitivos en una escena más grande? Ve a la sección [Escena](scene.md).

¿Quieres aprenderlo *todo* sobre Nomad? ¡Buena elección! Este manual cubre todo Nomad, incluye muchos trucos y consejos, y tiene una búsqueda muy útil en la parte superior. Usa la navegación de la izquierda para aprender más.

Si prefieres los vídeos, Holger Schönischka ha creado en Youtube una enorme colección de trucos y consejos para Nomad: https://www.youtube.com/@ProcreateFX/videos


## Obtener ayuda {#getting-help}

Si aún tienes dudas después de leer el manual y ver los tutoriales en vídeo, hay tres formas principales de hablar con otros usuarios de Nomad o con su desarrollador:

* Visita el foro: [forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* Únete al chat de Discord de Nomad: [https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* Contacta directamente con el desarrollador en support@nomadsculpt.com
