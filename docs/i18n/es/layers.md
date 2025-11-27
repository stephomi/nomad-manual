# ![](/icons/layer.webp) Capas 

Este menú contiene la pila de capas, una forma de almacenar ediciones en tu objeto de manera no destructiva, y muchas formas de combinar y reutilizar capas.

![](/images/layers_overview.webp) 

## Descripción general

Las capas de Nomad cumplen múltiples propósitos.

La información de pintura (Color, Rugosidad, Metalicidad, Opacidad) funciona con capas de forma similar a las aplicaciones de pintura 2D. Se puede crear una capa y aplicar pintura a un modelo. La capa se puede activar o desactivar, ajustar su opacidad, duplicar, cambiar su orden en la pila de capas y ajustar su modo de fusión.

Nomad también usa capas para esculpido. Una capa puede almacenar detalles finos como arrugas, o puede almacenar cambios grandes, permitiendo que funcionen como blendshapes/shape keys/morph targets en otras aplicaciones 3D. Por ejemplo, podrías esculpir diferentes expresiones faciales en distintas capas y ajustar los deslizadores de capa para combinarlas en nuevas expresiones.

En este caso, los cambios almacenados en una capa son puramente aditivos; el orden de las capas no importa como sí lo hace para la pintura.

Las capas se pueden borrar parcialmente mediante la herramienta [Delete Layer](tools.md#delete-layer), y las capas también se pueden usar para crear máscaras basadas en la distinta información almacenada en la capa.

![](/videos/layer.mp4)

::: tip
A diferencia de la mayoría del software de esculpido, cambiar la topología de una malla no descartará las capas. Puedes usar el [Voxel Remesher](topology.md#voxel-remesher), el [Multiresolution](topology.md#multiresolution) o las herramientas [Trim](tools.md#trim)/[Split](tools.md#split), pero ten en cuenta que al usar el [Voxel Remesher](topology.md#voxel-remesher), la calidad de la capa se verá afectada.
:::

::: tip
Si usas capas para blendshapes/morph targets, hay funcionalidad extra de capas en el [menú de escena](scene.md#object-menu). Puedes separar capas en objetos y combinar objetos coincidentes en capas.
:::
----

## Menú de capas 

![](/images/layers_menu.webp)

Pulsa `Add layer` para crear una nueva capa.

Cada capa tiene un nombre, un deslizador para controlar su intensidad/factor y botones de opciones.

### Opciones

| Acción       | Icono                        | Descripción                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Visible      | ![](/icons/eye_open.webp)   | Mostrar/ocultar la capa                             |
| Modo de fusión | ![](/icons/opacity.webp)  | El modo de fusión al estilo Photoshop. Los 4 iconos muestran los modos para Color, Rugosidad, Metalicidad, Opacidad. |
| Editar nombre | ![](/icons/pencil.webp)    | Editar el nombre de la capa                         |
| Eliminar     | ![](/icons/trash.webp)      | Eliminar la capa                                    |
| Duplicar     | ![](/icons/clone.webp)      | Duplicar la capa                                    |
| Combinar hacia abajo | ![](/icons/merge_down.webp) | Combinar la capa con la capa inferior (o la malla base) |
| Más          | ![](/icons/more.webp)       | Opciones [More...](#more)                           |

Para mover una capa a otra parte de la pila de capas, mantén pulsado su nombre y arrástrala.

### More...

El botón 'More...' mostrará opciones adicionales para la capa actual:

![](/images/layers_more.webp) 

#### Factores de canal

Estos controles te permiten escalar la cantidad de esculpido/color/rugosidad/metalicidad/opacidad de la capa. Estos valores se multiplican por el deslizador de factor de capa, así que, por ejemplo, si la intensidad de la capa es 1, pero el factor del canal de color es 0.5, entonces el color mostrado tendrá una intensidad de 0.5.

`Offset` controla la intensidad de esculpido de la capa. Mientras que color/rugosidad/metalicidad están limitados entre 0 y 1, offset puede tener cualquier valor, tanto positivo como negativo. 

::: tip
Offset se puede usar para convertir una capa de bultos en una capa de cavidades, o una sonrisa en un ceño fruncido:
![](/videos/layer_happysad.mp4)


Una capa simétrica se puede clonar y luego dividir en formas izquierda/derecha con del layer:
![](/videos/layer_leftright.mp4)

Las capas con factores de offset negativos se pueden hornear en capas vacías para crear nuevas formas positivas.

Las capas con factores de offset positivos por encima de 1 se pueden usar para experimentar con blendshapes más extremos.
:::

::: warning
Por el momento las capas solo comparten un único canal de opacidad para los 3 canales (color/metalicidad/rugosidad).
Si combinas varias capas con intensidad por canal que no estén a intensidad completa, es posible que el resultado final se vea diferente.

Quizá en el futuro cada canal tenga su propio canal alfa para eliminar esta limitación.
:::


#### ![](/icons/tool_mask.webp) Mask
El botón de máscara junto a cada deslizador creará una máscara a partir de ese canal. Similar al uso de capas para hacer selecciones en aplicaciones de pintura, esto te permite reutilizar el trabajo que has hecho en una capa para otras operaciones.

#### ![](/icons/preview.webp) Preview
![](/images/layers_preview.webp) 

Cuando está activado, previsualizará los ajustes de extracción para esta capa (ver la siguiente sección).

Cuando el modo rayos X está activado, solo la forma extraída será sólida; el resto de la forma se volverá transparente, lo cual es útil si estás usando alturas de extracción negativas.

#### Extract
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

El botón `Extract` duplicará el contenido de la capa en un nuevo objeto, normalmente con un grosor especificado por el usuario establecido en la siguiente sección.

`Closing action` determina cómo se realiza la duplicación:

* None - Simplemente extrae la parte, sin intentar generar lados ni rellenar agujeros.
* Fill - El agujero se rellena y se suaviza con triángulos. No uses esta opción para superficies planas.
* Shell - Cierra la forma extraída con las opciones de valor de grosor y dirección.
* Layer - Extrae la diferencia de la capa.

#### ![](/icons/height.webp) Thickness
![](/images/layers_thickness.webp) 

La profundidad de la extrusión del shell. Los valores positivos crecen hacia fuera de la superficie, los valores negativos crecen hacia dentro de la superficie.

El signo más/menos junto a este valor establecerá la dirección de la extrusión:
* Menos ( - ) comenzará desde la superficie actual y extruirá hacia abajo. 
* Más ( + ) comenzará desde la superficie actual y extruirá hacia arriba.
* MásMenos ( ± ) empujará la parte superior e inferior de la extrusión hacia afuera en cantidades iguales, de modo que quedará a medio incrustar en la superficie original.

#### Suavidad
![](/images/layers_smoothness.webp) 

Si los bordes de la región a extraer son irregulares, este deslizador intentará difuminar el borde para obtener una forma más suave. 

#### ![](/icons/height.webp) Edge loop (side)
![](/images/layers_edgeloop.webp) 

Esta sección es visible cuando la acción de cierre es 'Shell'. 

`Auto Edge-loop (side)` calculará el número de edge loops a lo largo de los lados del shell para crear polígonos cuadrados. 

Si se desactiva, el deslizador `Division` establecerá el número de divisiones en los lados.

_Este es el final del submenú 'More...'._

### Avanzado
![](/images/layers_advanced.webp)

#### Keep top layers details

Garantiza que los pequeños detalles en las capas superiores sigan siendo visibles cuando se realizan cambios grandes en las capas inferiores.

De forma predeterminada, si esculpes pequeñas arrugas en una capa y luego haces cambios grandes en la capa base, las arrugas se perderán. Activar este interruptor permitirá que esos pequeños detalles siempre floten por encima de los grandes cambios inferiores. En el siguiente vídeo, observa cómo el detalle de la arruga se elimina de forma predeterminada, pero permanece visible cuando 'keep top layers details' está activado:

![](/videos/layers_details.mp4)


#### UI: Expand list

El menú de capas predeterminado te permite alternar la visibilidad de la capa y la opacidad de la capa. Activar esta opción expande los controles completos para cada capa.

![](/images/layers_expand.webp)

#### Sync transform

Si está activado, todas las capas no seleccionadas se ajustarán en función de la rotación, escala y deformación de la transformación. 

Desactiva esta opción si las otras capas están pensadas para usarse sin la nueva transformación que estás aplicando.

Cuando está en `Auto`, solo se ajustarán las capas visibles.
