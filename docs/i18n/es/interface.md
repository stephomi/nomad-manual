# ![](/icons/interface.webp) Menú de interfaz {#interface-menu}

Este menú controla muchas opciones para personalizar la interfaz de Nomad. 

![](/images/interface_overview2.webp)

Nomad se puede personalizar a un nivel bastante profundo, este menú se divide en 4 secciones: Interface, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
¡Esta página es para el menú de interfaz, no para la interfaz en sí! La interfaz general se describe en [Getting Started](gettingstarted.md).
:::

## Interfaz {#interface}

La sección de interfaz te permite añadir atajos, crear barras de herramientas flotantes y controlar el color, tamaño y apariencia de la interfaz de usuario de Nomad.

![](/images/interface_overview3.webp)

### Añadir atajos (parte inferior)... {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

La barra de herramientas inferior tiene estos atajos activados por defecto:
* `Undo` - deshacer la operación anterior
* `Redo` - restaurar la operación previamente deshecha
* `Solo` - Oculta temporalmente todos los demás objetos, dejando visible solo el seleccionado. Pulsa de nuevo para restaurar todos los objetos.
* `X-ray` - Vuelve temporalmente semitransparentes todos los demás objetos, dejando solo el seleccionado como sólido. Pulsa de nuevo para restaurar los materiales por defecto.
* `Voxel remesh` - Remalla el objeto actual usando la última resolución de vóxel utilizada. Una pulsación larga o un deslizamiento hacia arriba mostrará un control deslizante de resolución y un interruptor de bordes afilados.
* `Grid` - Alterna la cuadrícula de vista. Una pulsación larga o un deslizamiento hacia arriba te permitirá cambiar el color y la opacidad de la cuadrícula.
* `Wireframe` - Alterna una superposición de malla alámbrica. Una pulsación larga o un deslizamiento hacia arriba te permitirá cambiar el color y la opacidad de la malla alámbrica.
* `Inspector` - te permite ver propiedades de tu malla como UVs, texturas horneadas y otras propiedades, superpuestas sobre el fondo de Nomad.
* `Face Group` - Alterna la superposición de grupos de caras, más información en [Tools->FaceGroup](tools.md#facegroup) 

Otros atajos de uso común están disponibles desde este menú, muchos más se pueden encontrar dentro del botón de bindings.

#### ![](/icons/more.webp) Asignaciones {#bindings-list}

Casi todas las funciones de Nomad se pueden añadir a la barra de atajos mediante el botón de bindings. Se mostrará un menú de bindings cuando se pulse el botón:

![](/images/interface_bindings_search.webp)

Puedes buscar por categoría mediante los iconos de la parte superior, o usar el campo de búsqueda para encontrar funciones por nombre. Haz clic en una función para añadirla a la barra de herramientas. Haz clic de nuevo para eliminarla.

#### ![](/icons/list.webp) Orden {#order}

Esto mostrará una lista de los atajos. Mantén pulsado y arrastra para reordenar los atajos.

#### ![](/icons/reset.webp) Restablecer {#reset}

Reset restaurará la barra inferior a su configuración por defecto.

### Añadir atajos (ventana)... + {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Al hacer clic en + se añadirá una barra de herramientas flotante. No será visible hasta que pulses el botón de bindings y le añadas algunos atajos, entonces podrás hacerla visible. 

Puedes crear muchas barras de herramientas, cada barra tiene las siguientes opciones en este menú:

* ![](/icons/checked.webp) `Visible` - Alterna la visibilidad de la barra de herramientas
* ![](/icons/more.webp)`Bindings` - Muestra la ventana de bindings para seleccionar funciones que añadir o eliminar de la barra de herramientas.
* ![](/icons/list.webp)`Order` - Muestra un menú para reordenar la barra de herramientas.
* ![](/icons/reset.webp) `Reset` - Restablece la barra de herramientas a su estado por defecto.
* ![](/icons/resize_bottom_right.webp) `Resize corner` - Activa un tirador de cambio de tamaño en la esquina inferior derecha de la barra de herramientas.
* ![](/icons/sort_down.webp) `Collapsable` - Activa un tirador de colapso en la esquina superior derecha.
* ![](/icons/trash.webp) `Delete` - Elimina la barra de herramientas.

### Caja de herramientas {#toolbox}

Opciones para el menú de herramientas a la derecha de la interfaz de Nomad.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Esquina de cambio de tamaño de la IU {#ui-resize-corner}

Activa un tirador de cambio de tamaño en la esquina inferior de la barra de herramientas.

#### Oculto {#hidden}
Normalmente el icono de toolbox en la barra superior alternará entre una sola columna larga o una lista de herramientas en varias columnas. Esta opción alternará entre la lista de varias columnas o estar oculto.

#### Coloreado {#colored}
Codifica por color los iconos por categoría, por ejemplo todas las herramientas de máscara son marrones, las herramientas de corte son rojas, las de aplanar verdes, etc.

#### Filas: Auto (>1) {#rows-auto-1}

#### Restablecer orden {#reset-order}
Restablece las herramientas por defecto del toolbox a su orden original. Los iconos personalizados permanecerán en el toolbox al final de la lista.


### Preajustes {#presets}

![](/images/interface_presets.webp)

Una colección de presets de color para la interfaz.

#### Botón de alto contraste {#high-contrast-button}
Un estilo alternativo para los botones que los hace más visibles cuando están activados. Si se establece en Auto, Nomad usará este modo cuando el contraste de color de la interfaz entre activado/desactivado sea bajo.

#### Widget de color/Color base {#color-widgetcolor-base}
Los colores principales usados en la interfaz.

#### Panel transparente, Panel de color, Intensidad de desenfoque {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Cuando está activado, aparecerán opciones adicionales para controlar cómo se ven los menús y paneles en Nomad. Se puede ajustar su color, transparencia y cantidad de desenfoque.

::: tip
En dispositivos pequeños puede ser útil hacer el panel de color casi blanco, transparente y con poco desenfoque, para que los menús no oculten la escena.
:::

----

### Espejar barra superior {#mirror-top-bar}
Invierte el orden de los menús en la barra superior.

### Espejar barras laterales {#mirror-side-bars}
Intercambia las barras laterales para que el toolbox esté a la izquierda y las opciones de herramienta a la derecha.

### Espejar barra inferior {#mirror-bottom-bar}
Mueve la barra inferior a la esquina inferior derecha e invierte el orden de los botones.

### Vista previa del color del material {#material-color-preview}
Cuando seleccionas un color para un material, se muestra una vista previa de este material en el objeto actualmente seleccionado.

----
### Ventana de ayuda al pasar el ratón {#help-popup-on-hover}

Para dispositivos que admiten hover, activa si la ayuda contextual en Nomad representada con el icono ![](/icons/help.webp) aparecerá al pasar el cursor por encima, o solo al hacer clic.

----

### Escala general {#overall-scale}
Un multiplicador de tamaño para todos los elementos de la interfaz.
### Ancho del panel {#panel-width}
El ancho de los menús y paneles.
### Escala de fuente {#font-scale}
Escala las fuentes.
### Espaciado vertical {#vertical-spacing}
El espaciado entre elementos en menús y paneles.
### Espaciado vertical (izquierda) {#vertical-spacing-left}
El espaciado entre elementos en la barra de herramientas izquierda.

----

### Margen del borde {#edge-offset}
Solo deberías cambiar estos valores si tienes problemas al interactuar con los botones en los bordes de la pantalla. Si estos deslizadores están desactivados, Nomad usará los valores de área segura devueltos por el propio dispositivo.

::: tip
Cuando migres Nomad a un nuevo dispositivo (por ejemplo, reemplazar un iPhone 12 por un iPhone 15), ¡asegúrate de restablecer las opciones de borde a los valores por defecto!
:::

### Restablecer estilo {#reset-style}
Restablece todos los elementos de la interfaz a sus valores por defecto.


## Gesto {#gesture}
El menú de gestos controla cómo los toques con lápiz y dedo controlan Nomad.

![](/images/interface_gesture.webp)

### Opciones de gestos {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad puede limitar operaciones según el dispositivo de entrada. Por ejemplo, un arrastre con el dedo podría solo mover la cámara, mientras que un arrastre con el lápiz solo esculpe. Si tienes un ratón o trackpad, también se puede asignar para controlar operaciones específicas.

Actualmente Nomad te permite configurar estos modos para que se controlen con cualquier combinación de gestos de dedo, lápiz o ratón:

* Camera
* Sculpt
* Gizmo
* Material picking (mediante una pulsación larga)
* Select object


`Finger always smooths` - Smooth se puede configurar para que solo funcione con un arrastre con el dedo.

### ![](/icons/tool_mask.webp) Máscara {#mask}

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Activa los siguientes atajos de un toque sin tener que mantener pulsado el botón de máscara. Permitirá los siguientes gestos:
* tocar en el fondo para invertir la máscara
* tocar en un área enmascarada para difuminar la máscara
* tocar en un área sin máscara para afilar la máscara

### Alternar Máscara <-> SelMask {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - Una pulsación larga alternará entre Mask y SelMask y comenzará un nuevo trazo. Al final del trazo, se vuelve a seleccionar la herramienta anterior. 
* `Tool` - Pulsación larga y soltar sin mover para cambiar entre Mask y SelMask. 

### ![](/icons/tool_hide.webp) Ocultar {#hide}
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` activará los siguientes atajos con la herramienta de ocultar:
* Tocar en un grupo de caras para ocultarlo
* Tocar en un espacio vacío para invertir los polígonos ocultos

### ![](/icons/finger3.webp) Tres dedos {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Si tu dispositivo admite gestos de 3 dedos, configura atajos para ese gesto. 

La matriz de opciones te permite definir arrastres verticales y horizontales como atajos separados. Ten en cuenta que si se elige el mismo gesto para 2 opciones, una se desactivará.

* `Rotate lighting` - Rota el entorno, las luces y el Matcap.
* `Tool Radius` - Edita el radio de la herramienta.
* `Tool Intensity` - Edita la intensidad de la herramienta. 

### ![](/icons/fingerprint.webp) Historial 2/3 {#history-23}
`History shortcuts` - cuando está activado, los siguientes gestos están activos:
* Undo - tocar con 2 dedos
* Redo - tocar con 3 dedos

`Long press` - cuando está activado, mantener 2/3 dedos pulsados deshará/rehacerá rápidamente.

### Accesibilidad {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Assistive window` mostrará una barra de herramientas flotante para controlar operaciones de arrastre, pellizco, giro y cámara.

### Cámara {#camera}
Un atajo para ir al menú `Camera` (las opciones de cámara solían estar aquí, pero se movieron al menú de cámara).

### Doble toque con lápiz -> Asignaciones {#pencil-tap}

Un atajo para ir al menú `Bindings` (las opciones de toque y doble toque del Pencil solían estar aquí, pero se han movido al menú de bindings).


## Asignaciones {#bindings}
Los atajos de teclado y botones se pueden definir desde el menú de bindings:

![](/images/interface_bindings.webp)
Casi todas las funciones de Nomad se pueden vincular a atajos de teclado si tu dispositivo tiene teclado, o a botones extra de tu lápiz, o incluso a mandos de juego.

Para crear un binding, haz clic en el rectángulo junto a la función y pulsa la tecla/botón. 

Encuentra funciones mediante los iconos de categoría en la parte superior, o mediante la barra de búsqueda para encontrarlas por nombre. 

Los bindings individuales se pueden desactivar mediante la casilla de verificación junto al nombre del binding.

### ![](/icons/more.webp) Menú contextual {#context-menu}
El icono ![](/icons/more.webp) después de cada binding abre un menú contextual:

![](/images/interface_bindings_context.webp)

* `Clone` - Clona el binding
* `Reset` - Restablece el binding
* `Delete` - Elimina el binding
* `Toggle shortcut on key tap` - Configura si un toque frente a una pulsación larga se tratan de forma diferente. Cuando está activado, un toque activará la herramienta. Una pulsación larga activará la herramienta solo mientras la tecla esté pulsada, al soltarla volverá a la herramienta anterior. A veces se llama “sticky keys” en otras aplicaciones 3D.

### Avanzado {#advanced}
En la parte inferior del menú de bindings hay un menú de engranaje para opciones avanzadas:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - Un toque de los atajos estándar para mask, smooth, gizmo, hide, sub alternará a ese modo, pero manteniendo la tecla pulsada cambiará a ese modo y, cuando se suelte la tecla, el modo volverá al anterior. A veces se llama “sticky keys” en otras aplicaciones 3D.
* `Toggle tool shortcuts` - Al usar uno de los atajos de herramienta, si el mismo atajo se pulsa dos veces, alternará a la herramienta anterior. De este modo puedes seguir cambiando entre dos herramientas con la misma tecla rápida.
* `Invert Y (Zooming)` - Invertirá el zoom
* `Reset bindings` - restablece todos los bindings a sus valores por defecto.


## iOS ⌘ Visualización de atajos de teclado {#ios-keyboard-shortcuts-display}

En dispositivos iOS con teclado, mantén pulsada la tecla ⌘ (cmd) para mostrar una lista de atajos.

El soporte de teclado en Android es algo experimental.

![](/images/shortcuts.webp)


## Depuración {#debug}
Algunas opciones experimentales y de depuración se almacenan en este menú. Muchas de estas opciones deberían dejarse en sus valores por defecto y solo modificarse después de contactar con el soporte de Nomad.

![](/images/interface_debug.webp)
### UV {#uv}
* `Normalize Uvs` - Nomad normalizará las UVs dentro del tile [0-1].

### Quad Remesh {#quad-remesh}
* `Instant Mesh` - Activa el algoritmo de remallado instantáneo
* `Quadriflow` - Un método alternativo de remallado quad.

### Renderizar {#render}
* `Heightmap` - Cambia el visor para renderizar la profundidad de la escena. Esto se puede usar para crear mapas alfa para usar en pinceles.
* `Refraction write depth (back)` - La cara posterior de las mallas de refracción se escribirá en el búfer de profundidad.
* `Flip Y (normal map)` - Invierte el canal Y al hornear mapas de normales, necesario para ciertos motores de juego y render.
* `Angle weighted smooth normals` - Un ajuste en cómo funciona el sombreado suave que puede evitar pliegues en ciertos casos.

### FPS objetivo {#target-fps}
Cuando está desactivado, Nomad sincronizará sus fotogramas por segundo con la frecuencia de actualización de tu pantalla.

Cuando está activado, puedes establecer los fotogramas por segundo que Nomad renderizará.

### Interfaz {#debug-interface}
* `Top: layout` 
  * Collapse: En dispositivos pequeños la barra superior se colapsará en más submenús. 
  * Scroll: Si estás acostumbrado a Nomad en pantallas grandes y prefieres el diseño normal, al activar esto se usará la barra superior ancha estándar y se podrá desplazar.
  * Multiline: Muestra todo el menú superior en varias líneas.
* `Bottom: draggable popup` - La barra de herramientas inferior tiene varios botones que muestran un diálogo emergente. Si esta opción está activada, esos diálogos se pueden mover a otra parte de la pantalla.  
* `Toolbox: show all` - Nomad ocultará herramientas que no sean relevantes para la selección actual, por ejemplo, todos los pinceles de esculpido se ocultan en primitivas que no están validadas. Esta opción atenuará las herramientas desactivadas en lugar de ocultarlas.
* `Toolbox: colored` - Codifica por color los iconos del toolbox según su tipo.
* `Panel: Drop shadows` - Dibuja sombras alrededor de menús y paneles. En algunos dispositivos antiguos esto puede afectar al rendimiento.
* `Panel: Blending` - Opción de depuración
* `Pointer: hovering dot` - Para dispositivos que admiten hover con lápiz, muestra un punto cuando el lápiz está sobrevolando menús y paneles.

### Gif de mesa giratoria {#gif-turntable}
Nomad puede exportar un gif animado de turntable. Ten en cuenta que debido a las limitaciones del formato gif la calidad es baja. Normalmente la grabación de pantalla es un método mejor.

* `Duration` - cuánto durará en segundos el turntable
* `Rotation center` - dónde está el pivote de la cámara, por lo tanto qué parte de la escena será el centro de rotación de la cámara
* `Transparent background` - Usa la opción de transparencia para gifs. Ten en cuenta que los gifs solo admiten transparencia de 1 bit, por lo que los bordes pueden quedar muy dentados.
* `Max frame sampling` - Muchos de los efectos de renderizado de alta calidad de Nomad provienen de combinar varios fotogramas. Este control establece cuántos fotogramas combinar.
* `Export (GIF)` - inicia el proceso de exportación del gif.

### Posprocesado {#post-process}
* `Filtering` - Opción de depuración
* `Format` - Opción de depuración
* `Buffer reuse` - Opción de depuración

### Rendimiento {#performance}
* `Multicore general` - Opción de depuración
* `Multicore sculpting` - Opción de depuración
* `Partial Drawing` - ¡Función experimental! Úsala si estás esculpiendo una parte relativamente pequeña de una malla de alta densidad de polígonos. Debería hacer el esculpido más fluido, pero ¡no deberías activar la malla alámbrica! Además, podría añadir artefactos visuales durante las pinceladas.

### Característica {#feature}
* `Flip quad split (on tap)` -  Opción de depuración
* `Join: merge radius` - Los vértices se soldarán automáticamente si están lo suficientemente cerca cuando se unan mallas. Puedes ajustar el radio con este control deslizante.

### Depuración {#dev}
* `Logs` - Muestra una vista de registro
* `App review popup` - Opción de depuración
* `FPS` - añade un contador de fotogramas por segundo a las estadísticas del visor.