# ![](/icons/layer.webp) Capas {#layers}

Este menú contiene la pila de capas, una forma de guardar los cambios de tu objeto de manera no destructiva, y muchas formas de combinar y reutilizar las capas.

![](/images/layers_overview.webp) 

## Visión general {#overview}

Las capas de Nomad sirven para varias cosas.

La información de pintura (color, rugosidad, metalicidad, opacidad) funciona con capas de forma parecida a las aplicaciones de pintura 2d. Puedes crear una capa y pintar sobre el modelo. La capa se puede activar o desactivar, se puede ajustar su opacidad, duplicar, cambiar de orden en la pila de capas y cambiar su modo de mezcla.

Nomad también usa las capas para esculpir. Una capa puede guardar detalles finos como arrugas, o cambios grandes, de modo que funcione como los blendshapes/shape keys/morph targets de otras aplicaciones 3d. Por ejemplo, puedes esculpir distintas expresiones faciales en distintas capas y ajustar los reguladores de las capas para combinarlas en expresiones nuevas.

En este caso, los cambios guardados en una capa son puramente aditivos: el orden de las capas no importa, a diferencia de lo que ocurre con la pintura.

Las capas se pueden borrar parcialmente con la herramienta [Eli. capa](tools.md#delete-layer), y también se pueden usar para crear máscaras a partir de la distinta información que guarda la capa.

![](/videos/layer.mp4)

::: tip
A diferencia de la mayoría de los programas de escultura, cambiar la topología de una malla no elimina las capas. Puedes usar el [Remallado por vóxeles](topology.md#voxel-remesher), la [Multiresolución](topology.md#multiresolution) o las herramientas [Recortar](tools.md#trim)/[Dividir](tools.md#split), pero ten en cuenta que con el [Remallado por vóxeles](topology.md#voxel-remesher) la calidad de la capa se verá afectada.
:::

::: tip
Si usas las capas como blendshapes/morph targets, el [menú de escena](scene.md#object-menu) tiene funciones adicionales para capas: puedes separar capas en objetos y combinar objetos equivalentes en capas.
:::
----

## Menú de capas {#layer-menu}

![](/images/layers_menu.webp)

El título muestra el nombre del objeto seleccionado. Las capas no están disponibles en los primitivos, así que primero valida el primitivo.

Pulsa `Añadir capa` para crear una capa nueva. `Combinar capas` fusiona todas las capas en la malla base; el número junto a su icono indica cuántas capas hay.

Cada capa tiene un nombre, un regulador para controlar su fuerza (factor) y botones de opciones. Toca una capa para que sea la activa: lo que esculpas y pintes irá a esa capa. Toca `Base` para volver a trabajar en la malla base.

### ![](/icons/sort_right.webp) Desplegar la lista {#ui-expand-list}

Por defecto, la lista de capas solo muestra la visibilidad, el modo de mezcla y la fuerza de cada capa, y la capa activa se despliega con todos sus controles. La flecha a la izquierda del título despliega todos los controles de todas las capas.

![](/images/layers_expand.webp)

### Opciones {#options}

| Acción       | Icono                        | Descripción                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Visible      | ![](/icons/eye_open.webp)   | Muestra u oculta la capa                            |
| Mezcla       | ![](/icons/opacity.webp)    | El modo de fusión al estilo de Photoshop. Los 4 iconos muestran los modos de color, rugosidad, metalicidad y opacidad. |
| Editar nombre | ![](/icons/pencil.webp)    | Edita el nombre de la capa                          |
| Eliminar     | ![](/icons/trash.webp)      | Elimina la capa                                     |
| Duplicar     | ![](/icons/clone.webp)      | Duplica la capa                                     |
| Fusionar hacia abajo | ![](/icons/merge_down.webp) | Fusiona la capa con la capa inferior (o con la malla base) |
| Más          | ![](/icons/more.webp)       | Opciones de [Más...](#more)                         |

Cuando una capa no está desplegada, `Editar nombre`, `Eliminar`, `Duplicar` y `Fusionar hacia abajo` están en su menú [Más...](#more).

Para mover una capa a otro lugar de la pila, mantén pulsado su nombre y arrástrala.

### Base {#base}

El botón de 3 puntos de la fila `Base` lleva la pintura de la malla base a una capa nueva, con el botón `Base → Capa`. La base vuelve entonces al material de fondo. Es útil cuando has pintado mucho antes de crear ninguna capa.

* Los botones de máscara y ocultar de al lado dejan intactas las zonas enmascaradas y ocultas.
* `Extraer` - los canales que se mueven: `Color`, `Opacidad`, `Rugosidad` y `Metalicidad`.
* `Material de fondo` - si está activado, solo se mueven los valores que difieren de este material. Ajústalo con los reguladores o tómalo del modelo con el cuentagotas.

### ![](/icons/more.webp) Más... {#more}

El botón 'Más...' muestra opciones adicionales para la capa actual, en dos pestañas: los ajustes (icono del engranaje) y la extracción (icono del cubo).

![](/images/layers_more.webp) 

#### Factores de canal {#channel-factors}

Estos controles te permiten escalar la cantidad de escultura, color, rugosidad, metalicidad y opacidad de la capa. Estos valores se multiplican por el regulador de factor de la capa; por ejemplo, si la fuerza de la capa es 1 pero el factor del canal de color es 0,5, el color se mostrará con una fuerza de 0,5.

`Desplazamiento` controla la fuerza de la escultura de la capa. Mientras que el color, la rugosidad y la metalicidad están limitados entre 0 y 1, el desplazamiento puede tener cualquier valor, positivo o negativo.

::: tip
El desplazamiento sirve para convertir una capa de bultos en una capa de huecos, o una sonrisa en un ceño fruncido:
![](/videos/layer_happysad.mp4)


Una capa simétrica se puede clonar y luego dividir en formas izquierda/derecha con Eli. capa:
![](/videos/layer_leftright.mp4)

Las capas con factores de desplazamiento negativos se pueden hornear en capas vacías para crear nuevas formas positivas.

Las capas con factores de desplazamiento positivos mayores que 1 sirven para experimentar con blendshapes más extremos.
:::

::: warning
Por ahora, las capas comparten un único canal de opacidad para los 3 canales (color/metalicidad/rugosidad).
Si fusionas varias capas con intensidades por canal que no están al máximo, puede que el resultado final se vea distinto.

Quizá en el futuro cada canal tenga su propio canal alfa para eliminar esta limitación.
:::


#### ![](/icons/shield.webp) Máscara {#mask}
El botón de máscara junto a cada regulador crea una máscara a partir de ese canal. Igual que cuando usas capas para hacer selecciones en las aplicaciones de pintura, esto te permite reutilizar en otras operaciones el trabajo que has hecho en una capa.

#### ![](/icons/preview.webp) Vista previa {#preview}
![](/images/layers_preview.webp) 

Las siguientes opciones están en la pestaña de extracción del menú 'Más...'.

Si está activada, muestra una vista previa de los ajustes de extracción de esta capa (consulta la siguiente sección).

`Rayos X` elige qué objetos se vuelven transparentes durante la vista previa (`Ninguno`, `No seleccionados`, `Seleccionados` o `Todo`), para que la forma extraída se vea sólida. Es útil si usas alturas de extracción negativas.

#### ![](/icons/mask_extract.webp) Extraer {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

El botón `Extraer` duplica el contenido de la capa en un objeto nuevo, normalmente con el espesor que indiques en la siguiente sección.

`Acción de cierre` determina cómo se hace la duplicación:

* `Ninguno` - Simplemente extrae la parte, sin intentar generar lados ni rellenar agujeros.
* `Rellenar` - El agujero se rellena con triángulos y se suaviza. No uses esta opción en superficies planas.
* `Carcasa` - Cierra la forma extraída usando el espesor y las opciones de dirección.
* `Capa` - Extrae la diferencia de la capa.

#### ![](/icons/height.webp) Altura {#thickness}
![](/images/layers_thickness.webp) 

La profundidad de la extrusión de la carcasa. Los valores positivos crecen hacia fuera de la superficie y los negativos hacia dentro. Se oculta cuando la acción de cierre es `Capa`.

El más/menos junto a este valor define la dirección de la extrusión:
* Menos ( - ) parte de la superficie actual y extruye hacia abajo.
* Más ( + ) parte de la superficie actual y extruye hacia arriba.
* MásMenos ( ± ) separa la parte superior y la inferior de la extrusión a partes iguales, de modo que queda medio incrustada en la superficie original.

#### Lados {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Esta sección se ve cuando la acción de cierre es `Carcasa`.

`Divisiones de pared` define el número de divisiones a lo largo de los lados de la carcasa. Con su interruptor `Auto` activado, Nomad calcula el número de bucles de aristas para crear polígonos cuadrados.

#### Suavidad {#smoothness}
![](/images/layers_smoothness.webp) 

Si los bordes de la zona que se va a extraer son irregulares, activa esta opción para suavizarlos y darles una forma más limpia. `Todo` suaviza toda la superficie extraída y `Solo bordes` suaviza sus bordes. `Iteraciones` define la fuerza del suavizado.

_Aquí termina el submenú 'Más...'._

### ![](/icons/cog.webp) Avanzado {#advanced}
![](/images/layers_advanced.webp)

El botón `Avanzado` de la parte inferior del menú aparece en cuanto el objeto tiene capas.

#### Conservar detalles de capas superiores {#keep-top-layers-details}

Hace que los detalles pequeños de las capas superiores sigan visibles cuando haces cambios grandes en las capas inferiores. Mientras esculpes, la deformación que viene de las capas superiores se ignora, pero sus detalles siguen visibles. Solo funciona bien si esas capas superiores contienen detalles relativamente pequeños.

Por defecto, si esculpes arrugas pequeñas en una capa y luego haces cambios grandes en la capa base, las arrugas se pierden. Al activar esta opción, esos pequeños detalles flotan siempre por encima de los cambios grandes de debajo. En el siguiente vídeo, fíjate en cómo el detalle de las arrugas desaparece por defecto, pero sigue visible cuando 'Conservar detalles de capas superiores' está activado:

![](/videos/layers_details.mp4)


#### Sincronizar transformación {#sync-transform}

Si está activado, todas las capas no seleccionadas se ajustan según la rotación, la escala y el cizallamiento de la transformación cuando usas las herramientas Gizmo o Transformar. Puede ser `Auto`, `No` o `Sí`.

Desactiva esta opción si las demás capas deben usarse sin la nueva transformación que estás aplicando.

En `Auto`, solo se ajustan las capas visibles.
