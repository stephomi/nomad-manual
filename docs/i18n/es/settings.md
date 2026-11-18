# ![](/icons/cog.webp) Configuración {#reset-to-default}

El menú de configuración contiene muchas opciones para controlar el aspecto y el comportamiento de Nomad.

![](/images/settings_overview.webp)

La fila de botones de la parte superior del menú salta directamente a una sección: `Cursor`, `Indicador`, `Alámbrica`, `Cuadrícula`, `Dos caras`, `Contorno`, `Resaltar selección`, `Cubo de ajuste`, `Estadísticas`, `Manipuladores`, `Forma`, `Repetidores` y `Multiresolución`.

## Configuración de pantalla {#display-settings}
Esta sección contiene accesos rápidos a la mayoría de los ajustes que aparecen más abajo en este menú.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Sombreado suave {#smooth-shading}
Alterna entre sombreado suave y facetado. En facetado, los polígonos se sombrean de forma independiente, así que puedes ver la topología subyacente.
Puede ser útil ver el sombreado facetado mientras esculpes y luego cambiar al sombreado suave para el render.

Desactivar el sombreado suave mejora un poco el rendimiento.

### ![](/icons/outline.webp) Contorno {#outline-quick}
Muestra u oculta un contorno alrededor de la selección actual.

Es útil para ver claramente qué malla o mallas tienes seleccionadas cuando [Oscurecer mallas no seleccionadas](#darken-unselected-objects) está desactivado.

En cuanto a rendimiento, usar [Oscurecer mallas no seleccionadas](#darken-unselected-objects) es mucho mejor que usar el contorno.

### ![](/icons/grid.webp) Cuadrícula {#grid-quick}
Muestra u oculta una cuadrícula de fondo, útil para entender la posición y la escala de los objetos.

### ![](/icons/culling.webp) Dos caras {#two-sided-quick}
Activa o desactiva la visualización de los polígonos por las dos caras. Todas las caras apuntan en una dirección.
Las caras que se consideran *posteriores* son las que apuntan "en sentido contrario" al punto de vista de la cámara.

Por ejemplo, la esfera simple del inicio tiene sus caras apuntando hacia fuera.
Si metes la cámara dentro de la esfera, verás la cara posterior de esas caras.

La mayor parte del tiempo no deberías ver la cara posterior de las caras, así que colorearla puede ayudarte a detectar posibles problemas o una topología incorrecta.

Desactivar el render a `Dos caras` puede mejorar un poco el rendimiento.


### ![](/icons/wireframe.webp) Malla alámbrica {#wireframe-quick}
Muestra u oculta una malla alámbrica superpuesta.

Ten en cuenta que activar la malla alámbrica reduce el rendimiento.

### ![](/icons/snap_cube.webp) Cubo de ajuste {#snap-cube-quick}
Muestra u oculta un icono de ayuda en una esquina de la escena, útil para orientarte en el espacio y cambiar rápidamente entre las vistas frontal, trasera, izquierda, derecha, superior e inferior.

### ![](/icons/palette.webp) Mostrar pintura {#show-painting}
Muestra u oculta la pintura. Si está desactivado, los objetos se muestran con un material blanco no metálico, con un 25 % de rugosidad, en lugar de con su pintura.

### ![](/icons/tool_hide.webp) Usar Ocultar {#use-hide}
Activa o desactiva el modo de ocultar. Al desactivarlo, la ocultación sigue ahí, solo que inactiva. Este botón está deshabilitado si estás usando la herramienta de ocultar.

### ![](/icons/shield.webp) Mostrar máscara {#show-mask}
Activa o desactiva el modo de máscara. Al desactivarlo, la máscara sigue ahí, solo que inactiva. Pulsa de nuevo este botón para volver a activarla.

Si necesitas ocultar la máscara Y que siga activa, usa el color de máscara de más abajo y ponlo en blanco. ¡Acuérdate de volver a ponerlo en gris cuando termines!

Ten en cuenta que este botón está deshabilitado si estás usando una herramienta de máscara.

### ![](/icons/shield.webp) Máscara → Opaco {#mask-opaque}
`Máscara → Opaco` ignora los vértices transparentes al enmascarar. Solo afecta a la opacidad de vértices y de texturas: las caras ocultas con "ocultar" siguen ocultas. Solo está disponible mientras `Mostrar máscara` está activado.

### ![](/icons/bang.webp) Resaltar selección {#highlight-quick}
Activa o desactiva el destello de resaltado de la selección. Al seleccionar objetos, el objeto seleccionado destella durante 500 milisegundos. El color y la duración del destello se pueden personalizar más abajo.

### ![](/icons/list.webp) Estadísticas {#stats-quick}
Muestra u oculta el texto de estado en la vista 3d. Muestra información sobre la memoria del sistema, el número total de vértices de la escena y el número de vértices de la selección actual.

----- 

### ![](/icons/cube.webp) Oscurecer mallas no seleccionadas {#darken-unselected-objects}
Los objetos que no están seleccionados se oscurecen para que la selección actual destaque.

### ![](/icons/shield.webp) Máscara {#mask}
El color que se usa para la máscara, por defecto un gris medio, multiplicado por el color del objeto. Ponlo en blanco para que la máscara sea invisible, ¡pero acuérdate de volver a ponerlo en gris cuando termines!

## ![](/icons/cursor.webp) Cursor {#cursor}

### Círculo {#show-circle-while-sculpting}
Cuándo mostrar el círculo del radio del pincel:

* `Auto` - muestra el círculo, pero lo oculta mientras esculpes.
* `No` - nunca muestra el círculo.
* `Sí` - muestra siempre el círculo, incluso mientras esculpes.

### Mostrar punto pequeño {#show-small-dot}
Muestra un punto en el centro del trazo del pincel mientras esculpes, o cuando cambia el pivote de la cámara.

### Mostrar estabilizador de cuerda {#show-rope-stabilizer}
Dibuja una línea que indica la longitud de la cuerda cuando el [estabilizador de cuerda](stroke.md#lazy-rope-stabilizer) está activo en los ajustes de trazo.

### Mostrar indicación de giro {#show-roll-hint}
Muestra la guía de dirección de giro mientras usas un atajo de teclado de giro.

### ![](/icons/radius.webp) Tamaño {#dot-size}
El tamaño del punto pequeño.

### Colores {#cursor-colors}
El cursor cambia de color según lo que estés haciendo: `Esculpir`, `Fondo` (al pasar por encima del fondo), `Máscara`, `Suavizar`, `Cámara` y `Radio`. Aquí puedes personalizar cada color.

## ![](/icons/cursor.webp) Indicador {#indicator}
![](/images/settings_indicator.webp)

Muestra uno o varios indicadores visuales para tutoriales y capturas de pantalla. Ponlo en `Sí` para activarlo (en iOS también hay una opción `Auto`).

Los botones `Dedo`, `Lápiz` y `Ratón` muestran un icono cuando se detecta ese tipo de entrada.

### Color {#indicator-color}
El color del indicador.

### Tamaño/Icono/Círculo {#indicator-shape}
Controles para ajustar el tamaño del indicador y la opacidad del icono y del círculo dentro del indicador.

## ![](/icons/wireframe.webp) Malla alámbrica {#wireframe}
![](/images/settings_wireframe.webp)
Activa la malla alámbrica superpuesta.

### Objetivo {#target}
Define si la malla alámbrica se muestra en los objetos no seleccionados, solo en los seleccionados o en todos los objetos.

### Ocultar {#hide}
Define si la malla alámbrica se sigue mostrando en los polígonos ocultos.

### Multiresolución: Solo nivel 0 {#multiresolution-level-0-only}
La multiresolución muestra la malla alámbrica del nivel 0 más oscura, y los niveles superiores progresivamente más claros. Con esta opción activada, solo se muestra la malla alámbrica del nivel 0.

### Color {#wireframe-color}
Define el color y la opacidad de la malla alámbrica.

## ![](/icons/grid.webp) Cuadrícula {#grid}
![](/images/settings_grid.webp)
Activa la cuadrícula.

### Ajuste {#snap}
Estas opciones hacen que los puntos de las herramientas basadas en curvas y formas (`Torno`, `Tubo`, formas de polígono y de trayectoria...) se ajusten mientras los dibujas:

* `Ajustar a la cuadrícula` - se ajustan a la cuadrícula.
* `Ajustar a puntos (vista alineada)` - se ajustan a los puntos existentes cercanos cuando la cámara está alineada con un eje.
* `Ajustar a puntos (vista libre)` - se ajustan a los puntos existentes cercanos cuando la cámara no está alineada.

### Color {#grid-color}
Define el color y la opacidad de la cuadrícula. Estas opciones aparecen cuando la cuadrícula está visible.

`Viñeta` difumina la cuadrícula hacia sus bordes. `Umbral de división de ajuste` define, en píxeles, lo densas que pueden llegar a ser las líneas de la cuadrícula en pantalla antes de que la cuadrícula pase a otro nivel de subdivisión.

## ![](/icons/culling.webp)Dos caras {#two-sided}
Permite ver las caras de los polígonos por los dos lados.

### Color de cara posterior {#backface-color}
`Cara posterior coloreada` activa el tinte de las caras posteriores, y `Color de cara posterior` define el color del tinte.

## ![](/icons/outline.webp)Contorno {#outline}
Activa un contorno alrededor de los objetos seleccionados.

### Color del contorno, espesor {#outline-color-thickness}
Define el color y el `Espesor` del contorno.


## ![](/icons/bang.webp) Resaltar selección {#highlight}
Activa un breve destello cuando cambia la selección.
### Color, duración {#color-duration}
Define el color y la duración del destello, en milisegundos.

## ![](/icons/snap_cube.webp) Cubo de ajuste {#snap-cube}
![](/images/settings_snapcube.webp)

Muestra un icono de ayuda en una esquina de la escena, útil para cambiar rápidamente entre las vistas frontal, trasera, izquierda, derecha, superior e inferior. Toca los lados del cubo para cambiar entre las vistas ortográficas.

### Forma {#shape}
Elige entre una esfera, un cubo o un gnomon como forma del cubo de ajuste.

### Restringir alineación {#restrict-alignment}
Alinea las vistas de ajuste con los ejes del mundo. Si está activado, solo son posibles las 6 vistas principales. En `Auto`, esta restricción solo se aplica cuando la cámara está en modo `Plataforma giratoria`.

### Tamaño {#size}
Define el tamaño del cubo de ajuste.

### Voltear 180° {#flip-180}
Activa un comportamiento al tocar: si la vista está ajustada, tocar el centro del cubo gira la vista 180 grados. Por ejemplo, si la vista está ajustada al frente, al tocar el cubo de vista pasa a la vista trasera.

### Aristas y esquinas {#edges-corners}
Añade vistas de ajuste en las aristas y las esquinas del cubo (las zonas ámbar). No está disponible con la forma de gnomon.

### Arrastre de plataforma giratoria {#turntable-drag}
Al arrastrar el cubo, la vista gira sin inclinar la cámara y se detiene en cada vista de ajuste. Desactívalo para arrastrar el cubo con la rotación `Trackball`. En ambos casos, el arrastre se mantiene horizontal o vertical. Con una cámara en `Plataforma giratoria`, el cubo siempre se arrastra así.

### Posición {#snap-position}
Define en qué esquina está el cubo de ajuste.


## ![](/icons/list.webp) Estadísticas {#stats}
![](/images/settings_stats.webp)

Muestra información sobre la memoria del sistema, el número total de vértices de la escena y el número de vértices de la selección actual.

### Posición {#stats-position}
Define en qué esquina aparecen las estadísticas.

## ![](/icons/edit_radius.webp) Manipulador {#handle}
Ajustes de los manipuladores que arrastras en la vista, como el gizmo.

### Entrada numérica {#gizmo-input}
Permite introducir valores numéricos al tocar uno de los controles del gizmo.

### Ocultar en interacción {#hide-on-interaction}
Atenúa el gizmo mientras interactúas con él, para que no estorbe.

### ![](/icons/opacity.webp) Opacidad {#handle-opacity}
La opacidad de los manipuladores.

## ![](/icons/shape_lasso.webp) Forma {#shape-settings}
El aspecto en pantalla de las formas que dibujas con los trazos de forma (lazo, rectángulo, curva...).

### ![](/icons/opacity.webp) Relleno, contorno {#shape-fill-outline}
La opacidad del interior de la forma y de la línea que la rodea.

### Colores {#shape-colors}
El color de la forma para cada tipo de herramienta: `Máscara`, `Ocultar`, `Grupo de caras` y `Recortar`.

## ![](/icons/array.webp) Repetidores {#primitive-repeaters}
Límites para las copias que crean los [repetidores](scene#repeaters) (matriz, radial, curva, superficie). Mantienen Nomad fluido cuando un repetidor se descontrola.

### ![](/icons/cube.webp) Máx. copias {#repeater-max-copies}
El máximo de copias que crea un solo repetidor. A Nomad le cuesta manejar muchos objetos, sea cual sea su tamaño.

### ![](/icons/cube.webp) Copias en la escena {#repeater-scene-copies}
El presupuesto de copias de toda la escena. Una copia con pocos polígonos cuesta poca geometría, pero sigue siendo un objeto completo, así que las copias pequeñas son las que antes llegan a este límite.

### ![](/icons/triangle.webp) Caras máx. {#repeater-max-faces}
El presupuesto de caras de todas las copias de la escena. Si se supera, los objetos más pesados son los primeros en perder copias.

## ![](/icons/multires.webp) Multiresolución {#multires}
### Recuento máximo de vértices {#multires-lowres-count}
Define un umbral para no permitir una subdivisión de multiresolución que supere este número de vértices, lo que probablemente haría que Nomad se cerrara: Nomad no comprueba la memoria disponible antes de subdividir. El valor por defecto es de 10 millones.
### Umbral de baja resolución {#multires-lowres-threshold}
Al mover la cámara se puede mostrar una versión de menor resolución de la malla. Puedes subir este valor si quieres que se muestre una resolución mayor de la malla.

## Configuración {#advanced}
### ![](/icons/reset.webp) Restablecer predeterminados {#reset}
Restablece todas las preferencias de la aplicación a sus valores por defecto.

Algunos recursos se guardan aparte y NO se restablecen: proyectos, atajos de teclado, ajustes preestablecidos de herramientas, entornos HDR, MatCaps, alfas, texturas de pincel e imágenes de referencia. Todo lo que se guarda con el proyecto, como la iluminación, el posprocesado o las vistas de cámara, también se conserva intacto.
