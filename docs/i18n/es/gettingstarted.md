# Empezando {#getting-started}

## ¡Bienvenido a Nomad! {#welcome-to-nomad}

Nomad es una aplicación de esculpido 3D que funciona en muchos dispositivos, y funciona mejor en tabletas con un lápiz óptico sensible a la presión, por ejemplo un iPad con Apple Pencil, o una Samsung Galaxy Tab con lápiz.

Está inspirada en aplicaciones de esculpido de escritorio como ZBrush y Blender, con un enfoque en una interfaz fácil de entender, sin sacrificar funciones. Si ya has usado aplicaciones de esculpido 3D antes, Nomad te resultará muy familiar.

Si esta es tu primera vez haciendo esculpido 3D, es bueno conocer algunos conceptos básicos.

::: tip ¿Prefieres vídeo?
Youtube tiene ahora MUCHOS tutoriales en vídeo para principiantes, aquí hay algunos enlaces excelentes:

* [Nomad Sculpt Crash Course by Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Nomad Sculpt Beginner tutorial by Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [NOMAD FOR BEGINNERS series by SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

Vale la pena revisar el canal principal de esos creadores, publican nuevos tutoriales con frecuencia.
:::

## Tu primera escultura {#your-first-sculpt}

Cuando inicies Nomad por primera vez verás una esfera en pantalla. Simplemente arrastra tu lápiz sobre la esfera para empezar a esculpir. La simetría está activada por defecto para facilitar el esculpido.

![](/videos/gettingstarted_01.mp4)

Para hacer el pincel más grande o más pequeño, usa el deslizador de radio en la izquierda.

![](/videos/gettingstarted_02.mp4)

Para hacer el pincel más fuerte o más débil, usa el deslizador de intensidad en la izquierda.

![](/videos/gettingstarted_03.mp4)

La herramienta predeterminada es la `Clay tool`, y añade material a la superficie. Para restar de la superficie, toca el botón `Sub` en la izquierda. Para volver a añadir a la superficie, toca de nuevo el botón Sub.

![](/videos/gettingstarted_04.mp4)

Para suavizar la superficie, toca el botón `Smooth`. Para volver al esculpido normal, toca de nuevo el botón Smooth.

![](/videos/gettingstarted_05.mp4)

Para rotar alrededor del modelo, arrastra en el espacio vacío fuera del modelo.

![](/videos/gettingstarted_06.mp4)

Para hacer zoom, usa el gesto de pellizcar/zoom con dos dedos.

![](/videos/gettingstarted_07.mp4)

Para desplazar la cámara, apoya 2 dedos en la pantalla y arrastra.

![](/videos/gettingstarted_08.mp4)

Si cometes un error, un toque con 2 dedos deshará la acción, o usa el botón de deshacer en la parte inferior izquierda. 

![](/videos/gettingstarted_09.mp4)

::: tip Versión de escritorio
En escritorio, la tecla alt/opt se usa para controlar la cámara:

* toque y arrastre en espacio vacío = rotar cámara
* alt+toque y arrastre = desplazar
* alt+toque y arrastre, luego soltar alt = zoom (igual que en ZBrush)

Con tabletas Wacom que tienen 2 o más botones en el lápiz, usa la configuración de Wacom para configurar la punta y los botones así:

* punta = clic izquierdo
* balancín inferior = clic central
* balancín superior = clic derecho

Con esas configuraciones, puedes manipular la cámara solo con el lápiz:

* balancín superior y movimiento en el aire = rotar cámara
* balancín inferior y movimiento en el aire = desplazar
:::

## Añadir color {#add-color}

Nomad te permite pintar la superficie de tu escultura. En el menú de herramientas de la derecha, busca la herramienta `Paint` y haz clic en ella. En la barra lateral izquierda aparecerá una esfera de color. Haz clic en ella, esto abrirá un selector de color. Elige un color y pinta sobre tu modelo.

![](/videos/gettingstarted_10.mp4)

Para borrar, toca el botón `Erase` en la barra lateral izquierda, luego borra sobre la superficie. Toca de nuevo el botón Erase para volver al modo de pintura.

![](/videos/gettingstarted_11.mp4)

Usando el pincel de arcilla en modos add/sub, smooth, paint, intenta crear una cabeza caricaturesca sencilla:

![](/images/gettingstarted_head1.webp)

## Otras herramientas {#other-tools}

La paleta de herramientas tiene muchas herramientas para ayudar con el esculpido. Hasta ahora has usado el pincel de arcilla (la herramienta inicial por defecto), smooth y paint. Como smooth se usa con frecuencia, tiene un atajo extra en la barra lateral izquierda.

Las herramientas en Nomad pueden hacer una gran variedad de cosas, desde herramientas relacionadas con el esculpido como move, crease, inflate, hasta herramientas como split y trim que se parecen más a herramientas de carpintería o metalurgia. La página de [Tools](tools.md) tiene más información.

Intenta usar las herramientas move, crease, inflate y smooth para añadir más detalle a tu cabeza y cambiar su forma:

![](/images/gettingstarted_head2.webp)

Ahora que conoces lo básico de Nomad, veamos el resto de la interfaz.

## Interfaz {#interface}

![](/images/interface_overview1.webp)

* `Top menus` - Los menús para acceder a la mayoría de las funciones de Nomad. Los menús de la parte superior izquierda cubren principalmente funciones de escena y objeto, los menús de la parte superior derecha están relacionados con las herramientas. En pantallas más pequeñas estos menús se contraerán juntos para ahorrar espacio.
* `Stats` - Información sobre la escena, el objeto actual, el estado de la máscara y el uso de memoria.
* `Nav Cube` - Una ayuda para mostrar desde qué lado de la escultura estás mirando, así como un atajo para saltar a diferentes vistas. Al tocar el cubo, la vista saltará al lado tocado. Arrastrar el cubo lo rotará. Toca los pequeños iconos al lado del cubo para encuadrar el objeto actual o restablecer a la vista inicial por defecto.
* `Toolbox` - Las herramientas de Nomad están disponibles en esta región desplazable.
* `Left toolbar` - Deslizadores para radio e intensidad para la mayoría de las herramientas, botones específicos de contexto para otras herramientas y atajos para simetría, el modo alt/sub de la herramienta, enmascarado, suavizado, el gizmo y opciones de pintura.
* `Bottom toolbar` - Atajos para funciones de uso común, explicadas a continuación.

::: tip ¿Eres zurdo?
Puedes reflejar la colocación y el orden de todas las barras de herramientas, consulta [Mirror top bar](interface.md#mirror-top-bar) y otras opciones relacionadas.
:::

## Barra de herramientas inferior {#bottom-toolbar}

![](/images/interface_bottom_toolbar.webp)

* `Undo` - revierte la última operación
* `Redo` - restaura la última operación deshecha
* `History` - accede a las opciones de historial, explicadas en el menú [History](history.md).
* `Solo` - Alterna entre mostrar solo el objeto actual o todos los objetos
* `X-Ray` - Hace que todos los demás objetos se rendericen en modo rayos X, y el objeto actual en sólido. Una pulsación larga o deslizar hacia arriba te permitirá establecer el color y la opacidad del modo rayos X.
* `Voxel` - Un atajo para el botón de [Voxel Remesher](topology.md#voxel-remesher) de remallado por vóxeles. Una pulsación larga o deslizar hacia arriba mostrará atajos para establecer la calidad del remallado por vóxeles.
* `Grid` - Alterna la visualización de la cuadrícula. Una pulsación larga o deslizar hacia arriba mostrará opciones para la cuadrícula.
* `Wire` - Alterna una superposición de malla alámbrica. Una pulsación larga o deslizar hacia arriba mostrará opciones para la malla alámbrica.
* `Inspect` - Alterna la visualización de datos extra sobre la malla actual. Por defecto mostrará las UVs, pero una pulsación larga o deslizar hacia arriba te permitirá inspeccionar otras propiedades si existen, y si esto se muestra en el fondo o sobre la malla.

## Próximos pasos {#next-steps}

Lo que deberías aprender a continuación depende de ti y de lo que te resulte interesante. Aquí van algunas sugerencias:

¿Quieres aprender más sobre las herramientas de esculpido? Ve a la sección [Tools](tools.md).

¿Quieres exportar tus modelos? ¿O importar modelos para esculpir sobre ellos? ¿O crear imágenes de tus esculturas? Ve a la sección [Files](files.md).

¿Quieres aprender más sobre cómo controlar el detalle en tu escultura? Ve a la sección [Topology](topology.md) y aprende sobre multires y decimation.

¿Quieres trabajar con más objetos? ¿Combinar objetos simples y primitivas en una escena más grande? Ve a la sección [Scene](scene.md).

¿Quieres aprender *todo* sobre Nomad? Buena elección. Este manual cubre todo Nomad, incluye muchos consejos y trucos, y tiene una excelente función de búsqueda en la parte superior. Usa la navegación de la izquierda para aprender más.

Si prefieres vídeo, Holger Schönischka ha creado una enorme colección de consejos y trucos para Nomad en Youtube: https://www.youtube.com/@ProcreateFX/videos


## Obtener ayuda {#getting-help}

Si aún tienes preguntas después de leer el manual y ver los vídeos tutoriales, hay tres formas principales de hablar con otros usuarios de Nomad o con el desarrollador de Nomad:

* Visita los foros: [forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* Únete al chat de Discord de Nomad: [https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* Contacta directamente con el desarrollador en support@nomadsculpt.com