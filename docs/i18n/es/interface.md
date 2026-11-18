# ![](/icons/sliders.webp) Menú Interfaz {#interface-menu}

Este menú reúne muchas opciones para personalizar la interfaz de Nomad.

![](/images/interface_overview2.webp)

Nomad se puede personalizar a fondo. Este menú se divide en 5 pestañas: Interfaz, Atajos, Gesto, Atajos (de teclado y botones) y Depurar.

![](/images/interface_menu.webp)


::: tip
Esta página trata del menú Interfaz, ¡no de la interfaz en sí! La interfaz en general se describe en [Primeros pasos](gettingstarted.md).
:::

## ![](/icons/sliders.webp) Interfaz {#interface}

La pestaña Interfaz controla el color, el tamaño y la distribución de la interfaz de Nomad. Tiene dos subpestañas, `Apariencia` y `Distribución`.

![](/images/interface_overview3.webp)

### ![](/icons/palette.webp) Colores {#presets}

![](/images/interface_presets.webp)

La subpestaña `Apariencia` empieza con una colección de colores predefinidos para la interfaz. Toca uno para aplicarlo y luego afínalo con las opciones de abajo.

#### Acento y Base {#color-widgetcolor-base}
Los colores principales de la interfaz: `Acento` para los botones seleccionados y las barras de los reguladores, `Base` para los paneles.

#### Opacidad del texto {#text-opacity}
Suaviza el texto y los iconos sobre los paneles.

#### Interruptores, Casilla, Pestañas {#high-contrast-button}
El estilo de los interruptores (`Suave` o `Sólido`), de las casillas (`Contorno`, `Acento` o `Relleno`) y de las pestañas (`Subrayado`, `Suave` o `Sólido`).

#### Herramientas con color {#colored}
Colorea los iconos por categoría; por ejemplo, todas las herramientas de máscara son marrones, las de corte rojas, las de aplanado verdes, etc.

#### Sombra de panel {#material-color-preview}
Los paneles proyectan una sombra para destacar sobre la escena.

#### Panel transparente {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Al activarlo, aparecen opciones adicionales para controlar el aspecto de los menús y paneles de Nomad: `Tinte de panel` fija su color, `Fuerza de difuminado` cuánto se difumina la escena que hay detrás, y `Cristal` añade refracción y brillos en los bordes, más visibles con poco difuminado.

::: tip
En dispositivos pequeños puede ser útil poner el tinte del panel casi blanco y transparente, con poca fuerza de difuminado, para que los menús no tapen la escena.
:::

#### ![](/icons/reset.webp) Restablecer apariencia {#reset-style}
Devuelve todas las opciones de apariencia a sus valores por defecto.

### ![](/icons/panel_detach.webp) Distribución {#layout}

La subpestaña `Distribución` controla dónde están los elementos y qué tamaño tienen.

#### Caja de herramientas {#toolbox}

Opciones del menú de herramientas que hay a la derecha de la interfaz de Nomad.

![](/images/interface_toolbox.webp)

##### ![](/icons/resize_bottom_right.webp) Redimensionar {#ui-resize-corner}

Muestra u oculta un tirador para cambiar el tamaño en la esquina inferior de la caja de herramientas.

##### Oculta {#hidden}
Normalmente, el icono de la caja de herramientas de la barra superior alterna entre una sola columna larga y una lista de herramientas en varias columnas. Con esta opción, alterna entre la lista en varias columnas y ocultarla.

##### Restablecer el orden {#reset-order}
Devuelve las herramientas por defecto de la caja de herramientas a su orden original. Los iconos personalizados se quedan en la caja de herramientas, al final de la lista.

#### Barra superior {#rows-auto-1}
`Adaptable` elige qué hace la barra superior cuando no cabe en la pantalla, algo que importa sobre todo en pantallas pequeñas: `Multilínea` reparte los menús en varias líneas, `Desplazar` mantiene una sola línea que puedes desplazar.

#### Invertir barra superior {#mirror-top-bar}
Invierte el orden de los menús de la barra superior.

#### Invertir barras laterales {#mirror-side-bars}
Intercambia las barras laterales, de modo que la caja de herramientas queda a la izquierda y las opciones de la herramienta a la derecha.

#### Invertir barra inferior {#mirror-bottom-bar}
Mueve la barra inferior a la esquina inferior derecha e invierte el orden de los botones.

#### ![](/icons/move.webp) Arrastrar panel {#drag-panel}
Un panel flotante siempre se mueve arrastrando su barra; esta opción te permite arrastrarlo también desde su contenido. En `Auto`, un dedo o un lápiz mueven el panel solo cuando el arrastre es más horizontal que vertical, así que un arrastre vertical sigue desplazando el contenido. Ponlo en `Sí` para arrastrarlo también con el ratón, en cualquier dirección.

#### ![](/icons/pencil.webp) Usar cuadro de diálogo Nomad {#use-nomad-dialog}
Muestra el cuadro de texto propio de Nomad en lugar del del sistema cuando escribes un nombre o un valor.

#### ![](/icons/stylus.webp) Punto al pasar {#hover-dot}
Muestra un pequeño punto en la interfaz cuando se detecta un lápiz suspendido sobre la pantalla.

#### ![](/icons/help.webp) Ayuda emergente al pasar el cursor {#help-popup-on-hover}

En los dispositivos que detectan el paso del cursor, elige si la ayuda contextual de Nomad, representada con el icono ![](/icons/help.webp), aparece al pasar por encima o solo al pulsarla.

#### Escala general {#overall-scale}
Un multiplicador de tamaño para todos los elementos de la interfaz.
#### Ancho del panel {#panel-width}
El ancho de los menús y paneles.
#### Escala de fuente {#font-scale}
Escala el texto.
#### Espaciado vertical {#vertical-spacing}
El espacio entre los elementos de los menús y paneles.
#### Espaciado vertical (izquierda) {#vertical-spacing-left}
El espacio entre los elementos de la barra de herramientas izquierda.

#### Desplazamientos de borde {#edge-offset}
Solo deberías cambiar estos valores si tienes problemas para usar los botones de los bordes de la pantalla. Si estos reguladores están desactivados, Nomad usa los valores de área segura que indica el propio dispositivo.

::: tip
Si pasas Nomad a un dispositivo nuevo (por ejemplo, de un iPhone 12 a un iPhone 15), ¡no olvides restablecer las opciones de bordes a sus valores por defecto!
:::

#### ![](/icons/reset.webp) Restablecer distribución {#reset-layout}
Devuelve todas las opciones de distribución a sus valores por defecto.

## ![](/icons/window.webp) Atajos {#shortcuts}

La pestaña Atajos elige qué botones rápidos aparecen alrededor de la vista 3d y te permite crear tus propias barras de herramientas flotantes.

### Barra lateral {#side-bar}
Los botones de herramientas rápidas de la parte inferior de la barra lateral izquierda: `Suavizar`, `Máscara`, `Ocultar`, `Grupo de caras` y `Gizmo`. Arrástralos para cambiar su orden.

### Barra inferior {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Toca un atajo para añadirlo a la barra inferior o para quitarlo. Estos están activados por defecto:
* `Deshacer` - deshace la operación anterior
* `Rehacer` - recupera la última operación deshecha
* `Individual` - Oculta temporalmente todos los demás objetos y deja visible solo el seleccionado. Vuelve a pulsarlo para mostrar de nuevo todos los objetos.
* `Rayos X` - Vuelve temporalmente semitransparentes todos los demás objetos y deja opaco solo el seleccionado. Vuelve a pulsarlo para recuperar los materiales por defecto.
* `Vóxel` - Remalla el objeto actual con la última resolución de vóxeles usada. Una pulsación larga o un deslizamiento hacia arriba muestran un regulador de resolución y la opción de bordes nítidos.
* `Cuadrícula` - Muestra u oculta la cuadrícula de la vista. Una pulsación larga o un deslizamiento hacia arriba te permiten cambiar su color y su opacidad.
* `Malla alámbrica` - Superpone u oculta la malla alámbrica. Una pulsación larga o un deslizamiento hacia arriba te permiten cambiar su color y su opacidad.
* `Inspeccionar` - te permite ver propiedades de tu malla, como las UVs, las texturas horneadas u otras propiedades, superpuestas sobre el fondo de Nomad.
* `Grupo de caras` - Muestra u oculta la superposición de los grupos de caras; más información en [Herramientas->Grupo de caras](tools.md#facegroup)

También hay otros atajos de uso habitual: `Contorno`, `Proyección` (perspectiva u ortográfica), `MatCap`, `DynTopo`, y los botones `Subdividir`, `Reverso` y de nivel de la [Multiresolución](topology.md#multiresolution).

#### ![](/icons/more.webp) Atajos {#bindings-list}

Casi todas las funciones de Nomad se pueden añadir a la barra inferior con el botón de atajos, que muestra cuántos atajos contiene la barra. Al pulsarlo, se abre un menú de atajos:

![](/images/interface_bindings_search.webp)

Puedes buscar por categoría con los iconos de la parte superior, o usar el campo de búsqueda para encontrar funciones por su nombre. Pulsa una función para añadirla a la barra. Vuelve a pulsarla para quitarla.

#### ![](/icons/eye_open.webp) Visible {#order}

Muestra u oculta toda la barra inferior.

#### ![](/icons/reset.webp) Restablecer {#reset}

Restablecer devuelve la barra inferior a su configuración por defecto.

### Ventanas flotantes {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Al pulsar el + se añade una barra de herramientas flotante. No será visible hasta que pulses el botón de atajos y le añadas algunos; después podrás hacerla visible.

Puedes crear muchas barras, y cada una tiene una fila con estas opciones:

* Arrastra el tirador de la izquierda de una fila para reordenar las barras.
* `Nombre` - El nombre de la barra.
* `Visible` - Muestra u oculta la barra.
* `Barra` - Muestra una barra de título en la barra de herramientas.
* `Compacta` - Mantiene la barra en pantalla cuando la interfaz está minimizada.
* `Atajos` - Muestra la ventana de atajos para elegir qué funciones añadir a la barra o quitar de ella.
* `Eliminar` - Elimina la barra.


## ![](/icons/gesture.webp) Gesto {#gesture}
El menú Gesto controla cómo manejan Nomad tu dedo, el lápiz, el ratón y el panel táctil.

![](/images/interface_gesture.webp)

### Opciones de gestos {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad puede limitar las operaciones según el dispositivo de entrada. Por ejemplo, arrastrar con el dedo podría solo mover la cámara, mientras que arrastrar con el lápiz solo esculpiría. Si tienes un ratón o un panel táctil, también puedes asignarles operaciones concretas.

Cada fila es una operación: activa `Dedo`, `Lápiz` y `Ratón` para elegir qué entradas pueden realizarla.

* `Cámara` - Mueve la cámara.
* `Edición de nodos` - Arrastra los controladores dibujados en el lienzo, por ejemplo para editar una primitiva, una curva, un repetidor o una luz.
* `Esculpir` - Esculpe con los pinceles. Las herramientas que tienen su propia fila más abajo siguen esa fila.
* `Seleccionar objeto` - Toca un objeto para seleccionarlo.
* `Selección de material` - Mantén pulsado sobre el lienzo para tomar el color o el material que hay bajo el cursor. Solo funciona si el pincel actual tiene la pintura activada.
* `Pulsación` - Los atajos de toque de herramientas como Máscara, Ocultar y Grupo de caras (ver abajo).
* `Pintura` - Las herramientas Pintar y Difuminar.
* `Máscara` - La herramienta Máscara.
* `Cara` - Las herramientas Ocultar y Grupo de caras.
* `Crear` - Las herramientas Tubo, Torno e Insertar.
* `Cortar` - Las herramientas Recortar, Dividir y Proyectar.
* `Seleccionar` - Las herramientas Seleccionar y Medir.
* `Gizmo` - Las herramientas Gizmo y Enrejado.
* `Transformar` - Las herramientas Transformar y Organizar.

::: tip
Una configuración habitual en tableta es dejar que solo el lápiz esculpa y pinte, y reservar los dedos para la cámara. Así, ni la palma ni un dedo despistado dejarán nunca un trazo sobre tu modelo.
:::

### ![](/icons/tool_smooth.webp) El dedo siempre suaviza {#finger-always-smooths}
Si está activado, el dedo siempre suaviza mientras haya una herramienta de esculpido activa, sea cual sea el pincel. Al activarlo se quita `Dedo` de la fila `Esculpir`, así que el lápiz esculpe y el dedo suaviza.

### Permitir trazo aéreo {#allow-air-stroke}
Permite empezar un trazo aunque el cursor se apoye primero fuera de la malla. Elige las herramientas a las que se aplica: `Herramienta` (todos los demás pinceles), `Suavizar`, `Máscara` y `Ocultar`. Solo funciona con las entradas que pueden esculpir pero no mover la cámara, así que estos botones están desactivados hasta que configures así alguna de tus entradas.

### ![](/icons/stroke.webp) Ajuste de trazo {#stroke-snap}
Deja el puntero quieto al final de un trazo para convertirlo en una línea recta o una curva suave. Sigue arrastrando para girar y escalar el trazo ajustado alrededor de su punto de inicio.

`Tiempo de pulsación` fija cuánto tiempo tienes que quedarte quieto antes de que el trazo se ajuste, o antes de que una forma pase a modo de edición.

### ![](/icons/stylus.webp) Utilice muestras de entrada adicionales {#use-extra-input-samples}
Usa las muestras de entrada adicionales que proporciona el dispositivo. Desactívalo si tus trazos salen dentados o la presión no se comporta bien. Esta opción no aparece en iOS.

### ![](/icons/tool_mask.webp) Máscara {#mask}

![](/images/interface_gesture_mask.webp)

`Atajos de un toque` - Activa los siguientes atajos de un toque sin tener que mantener pulsado el botón de máscara. Permite estos gestos:
* toca el fondo para invertir la máscara
* toca una zona enmascarada para difuminar la máscara
* toca una zona sin máscara para hacer más nítida la máscara

#### Pulsación larga {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)

Una pulsación larga con la herramienta Máscara cambia entre el pincel de máscara y el lazo (Sel. máscara):
* `Pulsación larga - Esculpir` - Mantén pulsado y sigue arrastrando: el trazo se dibuja con el otro modo, y el anterior vuelve al terminar el trazo.
* `Pulsación larga - Alternar` - Mantén pulsado y suelta sin moverte para cambiar entre los dos.

### ![](/icons/tool_smooth.webp) Suavizar {#smooth}
`Pulsación larga - Lazo` - Una pulsación larga con la herramienta Suavizar cambia a la herramienta Seleccionar mientras dura el trazo de selección.

### ![](/icons/tool_hide.webp) Ocultar {#hide}
![](/images/interface_gesture_hide.webp)

`Atajos de un toque` activa estos atajos con la herramienta Ocultar:
* Toca un grupo de caras para ocultarlo
* Toca un espacio vacío para invertir los polígonos ocultos

### ![](/icons/finger3.webp) Tres dedos {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Si tu dispositivo admite gestos con 3 dedos, configura atajos para ese gesto.

La matriz de opciones te permite asignar atajos distintos al arrastre vertical y al horizontal, o elegir `No` para dejarlo desactivado. Ten en cuenta que si eliges el mismo gesto para 2 opciones, una de ellas se desactiva y su nombre aparece tachado.

* `Girar iluminación` - Gira el entorno, las luces y el MatCap.
* `Radio de herramienta` - Cambia el radio de la herramienta.
* `Intensidad de herramienta` - Cambia la intensidad de la herramienta.

### ![](/icons/fingerprint.webp) Historial 2/3 {#history-23}
`Atajos del historial` - si está activado, se activan estos gestos:
* Deshacer - toca con 2 dedos
* Rehacer - toca con 3 dedos

`Pulsación larga` - si está activado, mantener 2 o 3 dedos sobre la pantalla deshace o rehace rápidamente.

### ![](/icons/mouse.webp) Rueda del ratón {#mouse-wheel}
`Velocidad (zoom 3d)` fija la rapidez con la que la rueda acerca o aleja la vista, y `Velocidad (interfaz 2d)` la rapidez con la que desplaza los menús y paneles. El botón de menos junto a cada regulador invierte la dirección.

### ![](/icons/fingerprint.webp) Panel táctil {#trackpad}
En un Mac, `Dos dedos` elige qué hacen dos dedos sobre el panel táctil. Pellizcar siempre hace zoom y girar los dedos siempre gira la vista.
* `Desactivado` - Desplazarse con dos dedos hace zoom, como la rueda del ratón. Los dedos no se leen por separado.
* `Desplazar` - Dos dedos desplazan la vista, y al levantar uno de ellos se orbita. Igual que en una tableta.
* `Orbitar` - Dos dedos orbitan la vista, y al levantar uno de ellos se desplaza.

### Accesibilidad {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Ventana de asistencia` muestra una barra de herramientas flotante para controlar el arrastre, el pellizco, el giro y las operaciones de cámara.

### Cámara {#camera}
Un acceso directo al menú `Cámara` (las opciones de cámara antes estaban aquí, pero se trasladaron al menú Cámara).

### Pulsar dos veces con el lápiz -> Atajos {#pencil-tap}

Un acceso directo al menú `Atajos`, donde se define qué hace la doble pulsación del Pencil. Fuera de iOS aparece como `Botón de lápiz → Atajos`, para el botón del lápiz.

### Rechazo de palma {#palm-rejection}
En teléfonos y tabletas, ignora los toques cuya superficie de contacto supera el `Umbral de tamaño máximo`, como la palma de la mano apoyada en la pantalla. Puede que no funcione en todos los dispositivos, así que desactívalo si tienes problemas al usar el lienzo.


## ![](/icons/keyboard.webp) Atajos {#bindings}
Los atajos de teclado y de botones se definen desde la pestaña Atajos con el icono del teclado:

![](/images/interface_bindings.webp)
Casi todas las funciones de Nomad se pueden asignar a atajos de teclado si tu dispositivo tiene teclado, a los botones adicionales del lápiz o incluso a mandos de videojuegos.

Para crear un atajo, pulsa el rectángulo junto a la función y presiona la tecla o el botón.

Encuentra las funciones con los iconos de categoría de la parte superior, o con la barra de búsqueda para buscarlas por nombre.

Puedes desactivar cada atajo con la casilla junto a su nombre. Mantén pulsada la casilla y arrastra para reordenar la lista.

Cuando dos atajos activados usan la misma combinación, aparece un icono ![](/icons/help.webp) junto a ellos, con la lista de las funciones en conflicto.

### ![](/icons/more.webp) Menú contextual {#context-menu}
El icono ![](/icons/more.webp) que hay tras cada atajo abre un menú contextual:

![](/images/interface_bindings_context.webp)

* `Clonar` - Clona el atajo, por ejemplo para dar a una función un segundo atajo.
* `Restablecer` - Restablece el atajo
* `Eliminar` - Elimina el atajo. Solo es posible cuando la función tiene más de un atajo.

Debajo, algunos atajos tienen opciones adicionales:

* `Teclas fijas` - Para los atajos de herramientas y los atajos rápidos (Máscara, Suavizar, Gizmo, Ocultar, Grupo de caras, Añadir/Restar), elige cómo cambia de herramienta una pulsación de tecla. `Auto` usa el valor por defecto fijado en las opciones [Avanzado](#advanced).
  * `Mantener` - Mantén pulsada la tecla para usar la herramienta y suéltala para volver a la herramienta anterior.
  * `Activar/desactivar` - Pulsa una vez para cambiar de herramienta.
  * `Presión rápida` - Mantén pulsado para usar la herramienta temporalmente, o pulsa brevemente para cambiar a ella.
* `Mantener Revertir` - Para los atajos rápidos, elige si al soltar una tecla mantenida se vuelve siempre a la herramienta anterior, incluso si esa herramienta ya estaba activa.
* `Alternar herramienta anterior` - Para los atajos de herramientas, pulsar el atajo de la herramienta actual vuelve a la última herramienta. Necesita `Teclas fijas` en `Activar/desactivar` o `Presión rápida`.
* `Posición` - Para los atajos de ventanas flotantes, abre la ventana donde estaba (`Conservar anterior`) o bajo el cursor (`En el cursor`).
* `Traslación (al soltar)` / `Zoom (al soltar)` - Para los atajos de zoom y desplazamiento de la cámara, cambia al otro al soltar la tecla.
* Dirección del arrastre - Para `Girar iluminación`, `Radio de herramienta` e `Intensidad de herramienta`, elige un arrastre horizontal o vertical.
* `Sincronizar` - Para las funciones que añaden, clonan o instancian objetos, elige si se sincroniza el resultado. Por defecto, usa el valor de sincronización fijado en el menú Escena.
* `En el fondo` - Para los atajos rápidos de Suavizar y Máscara, arrastra sobre el fondo mientras mantienes la tecla para dibujar un lazo: un lazo de selección para Suavizar, un lazo de máscara para Máscara.
* `Forzar cámara` - Para los atajos de cámara, mueve la cámara aunque otro atajo use la misma combinación, normalmente un atajo de herramienta o Añadir/Restar.
* `Giro lineal` - Para el atajo de giro, gira con un arrastre horizontal, vertical o diagonal en lugar de moverte alrededor del pivote.

::: tip
Con `Presión rápida`, una sola tecla sirve para las dos cosas: mantenla pulsada para suavizar o enmascarar un momento y volverás a tu pincel al soltarla, o tócala para quedarte en esa herramienta.
:::

### ![](/icons/cog.webp) Avanzado {#advanced}
En la parte inferior del menú de atajos hay un menú del engranaje con opciones avanzadas:

![](/images/interface_bindings_advanced.webp)

* `Atajos rápidos` - Los valores por defecto de `Teclas fijas` y `Mantener Revertir` para los atajos de Máscara, Suavizar, Gizmo, Ocultar, Grupo de caras y Añadir/Restar.
* `Atajos de herramientas` - Los valores por defecto de `Teclas fijas` y `Alternar herramienta anterior` para los atajos de herramientas. Con `Alternar herramienta anterior` puedes ir cambiando entre dos herramientas con la misma tecla.
* `Ventana de atajos` - El modo de `Teclas fijas` de los atajos que muestran las ventanas flotantes.
* `Invertir zoom Y` - Invierte la dirección del arrastre vertical al hacer zoom con un atajo.
* `Giro lineal` - Gira la vista con un arrastre horizontal, vertical o diagonal en lugar de moverte alrededor del pivote.
* `SpaceMouse` - Activa la compatibilidad con el SpaceMouse de 3Dconnexion. En algunos sistemas aparecen opciones adicionales: qué mueve (`Objeto`, `Cámara`, `Primera persona`, `Dron`), `Actualizar pivote automáticamente` para llevar el pivote a la superficie bajo el cursor cuando empieza a moverse, y sus velocidades de `Traslación`, `Zoom` y `Rotación`.
* `Zonas muertas (deriva)` - Para los controladores `Mando`, `Joystick` y `Botón`. Sube estos valores si la cámara se mueve cuando no tocas el controlador.
* `Radio de herramienta` - Cómo cambia el tamaño del pincel un arrastre con el atajo de radio (`Círculo`, `Centro` o `dx`), y luego cuánto suman (en píxeles) o multiplican los atajos de radio en cada pulsación.
* `Intensidad de herramienta` - Cuánto suman o multiplican los atajos de intensidad en cada pulsación.
* `Cámara - Velocidad` - La velocidad de `Traslación` y de `Rotación` de los atajos que desplazan y giran la vista.
* `Restablecer atajos` - devuelve todos los atajos a sus valores por defecto.
* `Restablecer el orden` - recupera el orden por defecto de la lista de atajos.


## Atajos de teclado ⌘ en iOS {#ios-keyboard-shortcuts-display}

En los dispositivos iOS con teclado, mantén pulsada la tecla ⌘ (cmd) para ver una lista de atajos.

La compatibilidad con teclados en Android es algo experimental.

![](/images/shortcuts.webp)


## ![](/icons/bug.webp) Depurar {#debug}
Este menú reúne algunas opciones experimentales y de depuración. Muchas de ellas deberían dejarse con sus valores por defecto y cambiarse solo después de contactar con el soporte de Nomad. Los iconos de la parte superior llevan a cada sección.

![](/images/interface_debug.webp)
### ![](/icons/uv.webp) UV {#uv}
* `Normalizar UVs` - Nomad normaliza las UVs de la malla seleccionada dentro del mosaico [0-1].

### ![](/icons/sun.webp) Sombreado {#render}
* `Escribir profundidad de refracción (detrás)` - La cara trasera de las mallas con refracción se escribe en el búfer de profundidad.
* `Normales suavizadas ponderadas por ángulo` - Un ajuste del funcionamiento del sombreado suave que puede evitar pliegues en ciertos casos.

### ![](/icons/speed.webp) FPS objetivo {#target-fps}
Si está desactivado, Nomad sincroniza sus fotogramas por segundo con la frecuencia de refresco de tu pantalla.

Si está activado, puedes fijar los fotogramas por segundo que renderiza Nomad.

### ![](/icons/window.webp) Interfaz {#debug-interface}
* `Herramientas: mostrar todas` - Nomad oculta las herramientas que no sirven para la selección actual; por ejemplo, todos los pinceles de esculpido se ocultan en las primitivas sin validar. Esta opción atenúa las herramientas desactivadas en lugar de ocultarlas.

Las demás opciones de interfaz que antes estaban aquí ahora se encuentran en la pestaña [Interfaz](#interface).

### ![](/icons/turntable.webp) Plataforma giratoria {#gif-turntable}
Nomad puede exportar un gif animado de la escena girando. Ten en cuenta que, por las limitaciones del formato gif, la calidad es baja. Grabar la pantalla suele ser un método mejor.

* `Duración` - cuántos segundos dura la animación
* `Máx. muestreo de fotogramas` - Muchos de los efectos de renderizado de alta calidad de Nomad se obtienen combinando varios fotogramas. Este regulador fija cuántos fotogramas se combinan, y su casilla lo activa o desactiva.
* `Centro de rotación` - alrededor de qué gira la cámara: `Mantener actual` conserva el pivote actual, `(0, 0, 0)` usa el centro del mundo, `Escena` el centro de la escena.
* `Fondo transparente` - Usa la opción de transparencia para los gifs. Ten en cuenta que los gifs solo admiten transparencia de 1 bit, así que los bordes pueden verse muy dentados.
* `Exportar (GIF)` - inicia la exportación del gif.

### ![](/icons/postprocess.webp) Posprocesado {#post-process}
* `Filtrado` - Opción de depuración
* `Formato` - Opción de depuración
* `Reutilizar búferes` - Opción de depuración

### ![](/icons/ram.webp) Rendimiento {#performance}
* `Multihilo: general` - Opción de depuración
* `Multihilo: escultura` - Opción de depuración
* `Dibujar repeticiones por instancias` - Dibuja todas las copias de un repetidor en una sola llamada de dibujo. Opción de depuración.

### ![](/icons/star.webp) Función {#feature}
* `nom: comprimir multirresolución` - Reduce el tamaño de los proyectos y de las exportaciones de Nomad que usan multiresolución. Las versiones antiguas de Nomad no pueden abrir estos archivos. Puede que en el futuro esta opción desaparezca y se active por defecto.
* `Invertir diagonal de quads (al tocar)` - Opción de depuración

### ![](/icons/bug.webp) Depurar {#dev}
* `Registros` - Abre una ventana de registros
* `Registrar eventos` - Escribe tus eventos de puntero (dedo, lápiz, ratón) en la ventana de registros, para investigar problemas de entrada.
* `FPS` - añade un contador de fotogramas por segundo a las estadísticas de la vista.
* `Ventana de valoración de la app` - Opción de depuración, en iOS y Android.

### ![](/icons/image.webp) Iconos personalizados {#custom-icons}
Sustituye los iconos de Nomad por tus propios archivos png.
* `Importar iconos` - Importa archivos png en `tmp_session/icons`. Cada uno sustituye al icono base con el mismo nombre. Se descartan al reiniciar Nomad.
* `Exportar iconos de herramientas` - Copia los iconos base `tool_<tool>.png` en `tmp_session/icons`, sin sobrescribir. Puedes editarlos allí y aplicarlos con `Recargar iconos`.
* `Recargar iconos` - Aplica los iconos de `tmp_session/icons`.

### Remallado de cuadrángulos {#quad-remesh}
Las opciones de remallado de cuadrángulos ya no están en este menú: consulta [Remallado de cuadrángulos](topology.md#quad-remesh-instant) en el menú Topología y la herramienta [Quad Remesher](tools.md#quad-remesher).

### Crear miniaturas de tienda {#make-store-thumbnails}
Renderiza capturas de pantalla con los tamaños que pide la App Store de iOS.
