# ![](/icons/cog.webp) Ajustes {#reset-to-default}

El menú de ajustes contiene muchas opciones para controlar la apariencia y el comportamiento de Nomad.

![](/images/settings_overview.webp)

## Ajustes de visualización {#display-settings}
Esta sección contiene accesos directos de lanzamiento rápido para la mayoría de los ajustes más abajo en este menú.

![](/images/settings_display_settings.webp)

### Sombreado suave {#smooth-shading}
Alterna entre sombreado suave y facetado. Cuando está facetado, los polígonos se sombrean de forma independiente, por lo que puedes ver la topología subyacente.
Puede ser útil ver el sombreado facetado durante la etapa de esculpido y luego cambiar a sombreado suave para el renderizado.

Desactivar el sombreado suave mejora un poco el rendimiento.

### Contorno {#outline-quick}
Activa o desactiva un contorno en tu selección actual.

Esto es útil para obtener retroalimentación visual sobre tu malla(s) seleccionada actual en caso de que [Oscurecer no seleccionados](#darken-unselected-objects) esté desactivado.

Desde el punto de vista del rendimiento, usar [Oscurecer no seleccionados](#darken-unselected-objects) es mucho mejor que usar la solución de contorno.

### Cuadrícula {#grid-quick}
Activa o desactiva una cuadrícula de fondo, útil para entender la colocación y escala de los objetos.

### Doble cara {#two-sided-quick}
Activa o desactiva la visualización de polígonos de doble cara. Todas las caras apuntan en una cierta dirección.
Las caras que se consideran *backface* son las que apuntan “lejos” del punto de vista de la cámara.

Por ejemplo, la esfera simple de inicio tendrá sus caras apuntando hacia el exterior.
Si mueves la cámara dentro de la esfera, entonces verás la cara posterior de estas caras.

La mayoría de las veces no deberías ver la parte posterior de las caras, por lo que colorearlas puede ayudarte a detectar posibles problemas o topología incorrecta.

Desactivar el renderizado `two sided` puede mejorar un poco el rendimiento del renderizado.


### Malla alámbrica {#wireframe-quick}
Activa o desactiva una superposición de malla alámbrica. 

Ten en cuenta que activar la malla alámbrica reducirá el rendimiento.

### Cubo de ajuste {#snap-cube-quick}
Activa o desactiva un icono de ayuda en la esquina de la escena, útil para orientarte en el espacio y cambiar rápidamente entre las vistas frontal/trasera/izquierda/derecha/superior/inferior.

### Mostrar pintura {#show-painting}
Activa o desactiva la visualización de la pintura. La pintura predeterminada es un material blanco no metálico, con un 25% de rugosidad.

### Usar ocultar {#use-hide}
Activa o desactiva el modo de ocultar. Cuando está desactivado sigue existiendo, solo está desactivado. Este botón está deshabilitado si estás usando actualmente la herramienta de ocultar.

### Mostrar máscara {#show-mask}
Activa o desactiva el modo de máscara. Cuando está desactivado sigue existiendo, solo está desactivado. Pulsa este botón de nuevo para volver a activarlo.

Si necesitas ocultar la máscara Y que siga activa, usa el color de máscara de abajo y ponlo en blanco. ¡Recuerda cambiarlo de nuevo a un gris cuando termines!

Ten en cuenta que este botón está deshabilitado si estás usando actualmente una herramienta de máscara. 

### Máscara -> Opaca {#mask-opaque}
Máscara -> opaco ignorará los vértices transparentes para la máscara enmascarada. Esto solo es relevante para la opacidad de vértices y texturas; las caras ocultas por “ocultar” seguirán ocultas.

### Resaltar {#highlight-quick}
Activa o desactiva el destello de resaltado de selección. Al seleccionar objetos, hace parpadear temporalmente el objeto seleccionado en rosa intenso durante 500 milisegundos. El color y la duración del destello se pueden personalizar más abajo.

### Estadísticas {#stats-quick}
Activa o desactiva el texto de estado en la vista 3D. Esto muestra información sobre la memoria de tu sistema, el recuento total de vértices de la escena y el recuento de vértices de la selección actual.

----- 

### Oscurecer objetos no seleccionados {#darken-unselected-objects}
Los objetos que no están seleccionados se oscurecerán para que la selección actual destaque.

### Máscara {#mask}
El color usado para enmascarar, por defecto un gris medio, multiplicado contra el color de tu objeto. Ponlo en blanco para hacer la máscara invisible, ¡pero recuerda cambiarlo de nuevo a gris cuando termines!

## ![](/icons/cursor.webp) Cursor {#cursor}

### Mostrar círculo al esculpir {#show-circle-while-sculpting}
Seguir mostrando el radio del pincel mientras se esculpe.

### Mostrar punto pequeño {#show-small-dot}
Muestra un punto en el centro del trazo del pincel mientras se esculpe, o cuando se cambia el pivote de la cámara.

### Mostrar estabilizador de cuerda {#show-rope-stabilizer}
Dibuja una línea para indicar la longitud de la cuerda cuando el estabilizador de cuerda perezosa está activo en los ajustes de trazo.

## ![](/icons/cursor.webp) Indicador {#indicator}
![](/images/settings_indicator.webp)

Muestra indicadores visuales para tutoriales y capturas de pantalla.

Los botones `Finger`, `Stylus` y `Mouse` activarán la visualización de un icono cuando se detecte ese tipo de entrada.

### Color {#indicator-color}
El color del indicador.

### Tamaño/Icono/Círculo {#indicator-shape}
Controles para ajustar el tamaño del indicador y las formas dentro del indicador.

## ![](/icons/wireframe.webp) Malla alámbrica {#wireframe}
![](/images/settings_wireframe.webp)
Activa la superposición de malla alámbrica.

### Destino {#target}
Define si los objetos no seleccionados mostrarán malla alámbrica, o solo los objetos seleccionados, o todos los objetos.

### Ocultar {#hide}
Define si la malla alámbrica seguirá mostrándose para los polígonos ocultos.

### Multirresolución: solo nivel 0 {#multiresolution-level-0-only}
Multirresolución mostrará las mallas alámbricas para el nivel 0 más oscuras, y los niveles superiores progresivamente más claras. Cuando está activada, esta opción solo mostrará la malla alámbrica del nivel 0.

### Color {#wireframe-color}
Define el color y la opacidad de la malla alámbrica.

## ![](/icons/grid.webp) Cuadrícula {#grid}
![](/images/settings_grid.webp)
Activa la cuadrícula.

### Color {#grid-color}
Define el color y la opacidad de la cuadrícula.

### Ajustar {#snap}
Activa el ajuste a la cuadrícula para las herramientas basadas en curvas.

## ![](/icons/culling.webp)Two sided {#two-sided}
Activa ver las caras de los polígonos desde ambos lados.

### Color cara posterior, Color de cara posterior {#backface-color}
Activa el teñido de las caras posteriores y el color del tinte.

## ![](/icons/outline.webp)Outline {#outline}
Activa un contorno alrededor del objeto activo.

### Color de contorno, Grosor {#outline-color-thickness}
Define el color y el grosor del contorno.


## ![](/icons/bang.webp) Resalte {#highlight}
Activa un breve destello cuando se cambia el objeto activo.
### Color, Duración {#color-duration}
Define el color y la duración del destello en milisegundos.

## ![](/icons/snap_cube.webp) Cubo de ajuste {#snap-cube}
![](/images/settings_snapcube.webp)

Muestra un icono de ayuda en la esquina de la escena, útil para cambiar rápidamente entre las vistas frontal/trasera/izquierda/derecha/superior/inferior. Toca los lados del cubo para cambiar entre vistas ortográficas.

### Forma {#shape}
Elige entre una forma de cubo, esfera o gnomon para el cubo de alineación.

### Restringir alineación {#restrict-alignment}
Activa el bloqueo de rotación de la cámara al arrastrar sobre el cubo de alineación. Cuando está activo, un movimiento de arrastre sobre el cubo de alineación solo irá a izquierda/derecha o arriba/abajo.

### Tamaño {#size}
Define el tamaño del cubo de alineación.

### Voltear 180 {#flip-180}
Activa un comportamiento de toque de modo que, si la vista está alineada, tocar el centro del cubo rotará la vista 180 grados. Por ejemplo, si la vista está alineada al frente, tocar el cubo de vista rotará a la vista trasera.

### Posición {#snap-position}
Define en qué esquina estará el cubo de alineación.


## ![](/icons/edit_radius_n.webp) Estadísticas {#stats}
![](/images/settings_stats.webp)

Muestra información sobre la memoria de tu sistema, el recuento total de vértices de la escena y el recuento de vértices de la selección actual.

### Posición {#stats-position}
Define en qué esquina estarán las estadísticas.

## Primtive/Repeaters {#primitive-repeaters}
## Entrada numérica {#gizmo-input}
Permite la entrada numérica al tocar los widgets del gizmo.

## Multirresolución {#multires}
### Recuento máximo de vértices {#multires-lowres-count}
Define un umbral para no permitir una operación de subdivisión de multirres por encima de este recuento de polígonos, lo que probablemente bloquearía Nomad. El valor predeterminado es 10 millones.
### Umbral de baja resolución {#multires-lowres-threshold}
Se puede mostrar una resolución más baja de la malla cuando mueves la cámara. Puedes aumentar este valor si quieres mostrar una resolución más alta de la malla.

## Ajustes {#advanced}
### Restablecer valores predeterminados {#reset}
Restablece todos los ajustes a sus valores predeterminados.