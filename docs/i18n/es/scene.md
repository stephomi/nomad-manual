# ![](/icons/scene.webp) Escena {#scene}

Este menú te permite gestionar objetos, luces, cámaras y repetidores en Nomad. Muestra la jerarquía de la escena como una vista en árbol, lo que te permite modificar muchos aspectos de tus objetos. También te permite crear nuevos objetos, así como combinar y separar objetos de varias maneras.


![](/images/scene_menu_summary.webp)


## Barra de atajos {#shortcut-bar}
| Acción                | Icono                             | Descripción                                                                                                         |
| :-------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Añadir...](#add-menu) | ![](/icons/plus.webp)           | Muestra el [Menú Añadir](#add-menu) para añadir un objeto a la escena                                               |
| Eliminar              | ![](/icons/trash.webp)           | Elimina el objeto                                                                                                   |
| Bloquear              | ![](/icons/lock.webp)            | Hace que el objeto no se pueda seleccionar en el visor. Todavía se puede seleccionar desde la vista en árbol.      |
| Unir                  | ![](/icons/merge.webp)           | Une los objetos seleccionados en un solo objeto sin cambios en la geometría                                        |
| Separar               | ![](/icons/diagonal.webp)        | Si un objeto está compuesto por cascarones de polígonos únicos, lo divide en objetos separados. Lo contrario de unir |
| [Booleano...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Muestra el menú [Booleano](#boolean)                                                                               |
| Clonar                | ![](/icons/clone.webp)           | Duplica el objeto en un nuevo objeto                                                                               |
| Instancia             | ![](/icons/link.webp)            | Duplica el objeto como una instancia, de modo que los cambios de modelado en uno se apliquen a todas las instancias. |
| Desinstanciar         | ![](/icons/unlink.webp)          | Convierte una instancia en una forma única, de modo que los cambios de modelado ya no se copien a otras instancias |
| Sincronizar           | ![](/icons/link.webp)            | Si las instancias tienen hijos, asegura que todas las instancias compartan la misma jerarquía de hijos             |


## Vista de árbol {#tree-view}
![](/images/scene_treeview.webp) 

| Acción       | Icono                      | Descripción              |
| :----------: | :------------------------: | :----------------------: |
| Seleccionar  | ![](/icons/checked.webp)  | Alterna seleccionado/no seleccionado |
| Visible      | ![](/icons/eye_open.webp) | Alterna visibilidad      |
| Menú         | ![](/icons/more.webp)     | Muestra el menú del objeto |

::: tip CONSEJO: Seleccionar u ocultar rápidamente muchos objetos

Toca el icono de selección para alternar un solo objeto, o arrastra verticalmente en la columna de selección para seleccionar muchos objetos. Lo mismo se puede hacer con la columna de visibilidad.

:::

### Manipulación de la vista de árbol {#tree-view-manipulation}

Mantén pulsado un elemento en la vista en árbol hasta que se vuelva amarillo. Entonces podrás moverlo hacia arriba o hacia abajo en la vista en árbol, así como arrastrarlo sobre otro elemento para convertirlo en hijo de ese elemento.

Cuando muchos elementos están seleccionados, la mayoría serán de un amarillo oscuro y uno será de un amarillo más claro. Mantén pulsado y arrastra el elemento más claro para mover todos los objetos a la vez.

Cuando seleccionas un elemento padre, por defecto todos los elementos hijos también se seleccionarán. Tocar el icono del padre alternará entre seleccionar solo el padre, o el padre y los hijos.

### Menú de objeto {#object-menu}

Al hacer clic en el botón de puntos suspensivos (...) de un objeto en la vista en árbol se mostrará el menú del objeto.  
Muchas de estas opciones son similares a la barra de atajos de la parte superior, repetidas por comodidad.

|       Acción        |                        Icono                        | Descripción                                                                                                                                                             |
| :-----------------: | :-------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      Instancia      |               ![](/icons/link.webp)            | Duplica el objeto como una instancia, de modo que los cambios de modelado en uno se apliquen a todas las instancias.                                                   |
|        Clonar       |              ![](/icons/clone.webp)            | Duplica el objeto en un nuevo objeto                                                                                                                                   |
|        Nombre       |              ![](/icons/pencil.webp)           | Cambia el nombre del objeto                                                                                                                                             |
|       Eliminar      |              ![](/icons/trash.webp)            | Elimina el objeto                                                                                                                                                       |
|      Eliminar+      |            ![](/icons/removeNode.webp)         | Elimina el objeto y sus hijos                                                                                                                                           |
|    Desinstanciar    |              ![](/icons/unlink.webp)           | Convierte una instancia en una forma única, de modo que los cambios de modelado ya no se copien a otras instancias.                                                    |
| Separar topología   |             ![](/icons/separate.webp)          | Si un objeto está compuesto por cascarones de polígonos únicos, lo divide en objetos separados. Lo contrario de la operación de unir.                                  |
| Separar grupo de caras |         ![](/icons/faceGroup.webp)          | Si un objeto tiene varios grupos de caras, divide la malla en objetos separados.                                                                                        |
|  Separar capas      |              ![](/icons/layer.webp)            | Si un objeto tiene capas, divide cada capa en un objeto separado. Útil para enviar blendshapes a otras aplicaciones.                                                   |
|   Unir -> Capas     | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Si se seleccionan varios objetos y tienen topología coincidente, fusiona esos objetos en capas para el objeto principal (los otros objetos se eliminarán). De nuevo, útil para blendshapes que vienen DE otras aplicaciones.<br><br> Ten en cuenta que las capas estarán desactivadas por defecto. Actívalas si necesitas ajustar sus deslizadores. |




### Multiselección {#multiselection}
Puedes seleccionar varios objetos para ayudar a lograr dos cosas:
- usar la herramienta de gizmo para mover varios objetos a la vez
- fusionar objetos usando operaciones de unión y booleanas.

Puedes hacerlo usando la casilla `Multiselection` y luego haciendo clic en el objeto en la lista.

::: tip Multiselección rápida
También puedes hacer multiselección en el visor manteniendo pulsado el atajo `Smooth` y tocando otra malla.

Puedes deseleccionar un objeto tocándolo de nuevo (solo si tu selección tiene más de un objeto).
:::

::: warning Función limitada del gizmo
Cuando se usa multiselección, la herramienta de gizmo siempre ignorará el enmascarado.  
Además, se elimina el escalado X/Y/Z.

La razón es que la multiselección solo permite la transformación de la malla completa, no la transformación por vértice.  
Esto podría mejorarse en el futuro.
:::


## Unir {#join}
Esta opción simplemente creará una única entrada de objeto a partir de varios objetos seleccionados.

Puedes ver un ejemplo en vídeo en la sección [Separar](#separate).

## Booleano {#boolean}
![](/images/scene_boolean_menu.webp) 
Combina objetos en una sola superficie.

`Voxel merge` conservará el volumen de los objetos y calculará nuevos polígonos uniformemente espaciados en la superficie. Debido al paso de cálculo, una fusión de vóxeles puede manejar geometría compleja, pero puede perder detalles finos si la resolución objetivo no es lo suficientemente alta.

`Boolean` intentará dejar los polígonos en su disposición original y coser los polígonos donde los objetos se superponen. Esto puede producir resultados mucho más limpios y nítidos que una fusión de vóxeles; sin embargo, requiere mallas "estancas": no puede haber agujeros ni formas malformadas en los objetos. Si esto falla, normalmente una fusión de vóxeles funcionará.

### Operaciones booleanas {#boolean-operations}
Tanto Voxel Merge como Boolean usarán la visibilidad de los objetos para controlar la operación:

#### Unión {#union}
Ambos objetos visibles crearán una **unión** booleana, la piel exterior de los objetos se combina, sin superficies interiores. ![](/images/boolean_union.webp)

#### Sustraer {#subtract}
Un objeto invisible = **sustracción** booleana, el objeto invisible se restará del objeto visible. ![](/images/boolean_subtract.webp)

#### Intersecar {#intersect}
Ambos objetos invisibles = **intersección** booleana, crea una nueva forma solo donde los dos objetos se superponen. ![](/images/boolean_intersect.webp)


### Botón de fusión de vóxeles {#voxel-merge-button}
Al pulsar este botón se realizará una operación de fusión de vóxeles en los objetos seleccionados. Cuando se hace en un solo objeto, lo retopologiza en polígonos uniformemente espaciados, útil cuando un objeto tiene polígonos estirados.

### Resolución {#resolution}
La resolución de la rejilla 3D de vóxeles utilizada para hacer el cálculo. Cuando se cambia este valor, se superpone un patrón de tablero de ajedrez en el objeto para previsualizar el tamaño de los polígonos.

### Construir multirresolución {#build-multiresolution}
Crea niveles de multirresolución por debajo de tu resolución objetivo. Así que si tu resolución es 400 y construir multirresolución es 3, obtendrás una nueva malla con, digamos, 296.000 polígonos, pero habrá 3 niveles de subdivisión inferiores de 74.000, 18.000, 4.000k.

### Mantener bordes nítidos {#keep-sharp-edges}
Activa el ajuste de la malla de vóxeles a los bordes. Esto funciona mejor en formas simples.

### Botón booleano {#boolean-button}
Al pulsar este botón se realizará una operación booleana de polígonos usando la biblioteca Manifold de Emmett Lalish. 


## Separar {#separate}
Si tienes un solo objeto basado en varias partes desconectadas, puedes dividir este objeto en varios objetos.  
Esto puede verse como lo opuesto a la [Unión simple](#simple-merge).

![](/videos/merge_separate.mp4)


## Menú Añadir {#add-menu}

![](/images/scene_addmenu_overview.webp)

Este menú creará primitivas, grupos, cámaras, repetidores y luces.

Las primitivas son tipos de formas básicas que se pueden ajustar usando parámetros. Una vez que tengas la primitiva ajustada a tus necesidades, la "validas", lo que hornea esos parámetros en una malla de polígonos que se puede esculpir y pintar. Una primitiva no puede tener sus parámetros ajustados después de haber sido validada.


![](/images/scene_addmenu_top.webp)

### En el gizmo {#on-gizmo}
Activa colocar la nueva primitiva donde esté la forma seleccionada actual o el gizmo. Cuando está desactivado, la primitiva se colocará en el centro de la escena.

### Seleccionar gizmo {#select-gizmo}
Activa cambiar automáticamente a la herramienta de gizmo cuando se crea una nueva primitiva. 

### Avanzado {#add-advanced}

Este menú te permite establecer tu preferencia sobre dónde se crearán las nuevas primitivas, grupos y repetidores. Pueden estar en el objeto seleccionado, en el origen del mundo o en la ubicación del gizmo.


### UV's {#uvs}
Activa las UV en las primitivas. Las UV (a menudo llamadas coordenadas de textura) son datos adicionales usados en 3D para permitir que las texturas se apliquen a las superficies. Ocupan más memoria, pero para la mayoría de los dispositivos esto no debería ser un problema a menos que entres en recuentos de polígonos muy altos (por ejemplo, 10 millones de polígonos o más). 

### Primitivas {#primitives}

| Primitiva      | Icono                                     | Descripción                                                                                                     |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Caja           | ![](/icons/cube.webp)                    | Es un cubo simple, puedes controlar la división en X, Y y Z                                                     |
| Esfera         | ![](/icons/circle.webp)                  | Por comodidad se llama Esfera, pero en realidad es una caja subdividida, con `Project on sphere` forzado       |
| Cilindro       | ![](/icons/cylinder.webp)                | Puedes añadir un agujero central al cilindro, por ejemplo para hacer un tubo hueco                              |
| Toro           | ![](/icons/torus.webp)                   | El toro puede ser un buen punto de partida para anillos                                                         |
| Cono           | ![](/icons/cone.webp)                    | -                                                                                                               |
| Icosaedro      | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| Esfera UV      | ![](/icons/circle.webp)                  | Una esfera con distribución de polígonos desigual, ver [Advertencia abajo](#uv-sphere)                         |
| Plano          | ![](/icons/rectangle.webp)               | Es un plano simple, ten en cuenta que esta es la única primitiva que no está cerrada                           |
| Tubo           | ![](/icons/tool_tube.webp)               | ver [Tubo](tools#tube)                                                                                          |
| Torno          | ![](/icons/tool_lathe.webp)              | ver [Lathe](tools#lathe)                                                                                        |
| Triplanar      | ![](/icons/triplanar.webp)               | ver [Triplanar](#triplanar)                                                                                     |
| Captura de sombras | ![](/icons/material_shadow_catcher.webp) | ver [Shadow Catcher](#shadow-catcher)                                                                       |
| Cabeza         | ![](/icons/face.webp)                    | Una cabeza simple con una capa para mezclar entre masculino/femenino                                            |

::: tip
Si te preguntas cuál es la malla base cuando inicias Nomad: también es una caja subdividida.  
Sin embargo, la malla base en Nomad no usa `Project on sphere`, lo que significa que no es perfectamente redonda.
:::

### Barra de herramientas de primitivas {#primitive-toolbar}

![](/images/scene_primitive_toolbar.gif)

Una vez que se crea una primitiva, aparecerá una barra de herramientas para controlar sus parámetros.

* `Validate` Hornea la primitiva en un objeto estándar para que pueda ser esculpido y pintado.
* `Edit` Alterna la visualización del gizmo de la primitiva. Se muestra directamente en la primitiva para controlar sus parámetros, por ejemplo, el ancho del cubo o el radio del agujero de un cilindro.
* `Mirror` Alterna colocar un repetidor de espejo sobre la primitiva.
* `...` Muestra el menú de la primitiva.

Las diferentes primitivas tendrán opciones adicionales en la barra de herramientas:

* `Project` La esfera se construye como un cubo subdividido, ya que esto es mejor para esculpir, pero significa que no es perfectamente redonda. Esta opción forzará la forma más cerca de una esfera perfecta. El icosaedro comparte esta opción.
* `Cap` Alterna tapas en los extremos de una forma, por ejemplo, un cilindro puede tener tapas arriba, abajo, ambas o ninguna.
* `Hole` Alterna la creación de un agujero a través del centro de una forma. Esto cicla entre sin agujeros, agujero con un solo radio o agujero con radio diferente arriba y abajo.
* `Radius` Alterna si un cilindro debe tener un solo radio o un radio diferente en su parte superior e inferior.
* `Disk` Alterna si un plano debe ser una forma de 4 lados o una forma circular.

La pequeña barra de herramientas debajo de la barra principal te permitirá alternar entre el gizmo de la primitiva y el gizmo de transformación.

::: tip

Al hacer clic en el título de la barra de herramientas se alternará entre la parte superior o inferior de la pantalla. Al hacer clic en la flecha de la esquina se colapsará.

:::


### Menú de primitivas {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Contiene todos los parámetros de la primitiva seleccionada. Los parámetros son las descripciones básicas de una forma. Para describir un anillo, por ejemplo, describirías su radio exterior, su radio interior y el número de polígonos.

La mayoría de los parámetros de las primitivas deberían ser autoexplicativos, y hay algunos parámetros comunes compartidos por todas las primitivas:

* `UVs` El pequeño botón de UVs en la parte superior del menú alterna la creación de coordenadas UV
* `Validate` El pequeño botón de validar hornea la primitiva en un objeto estándar para que pueda ser esculpido y pintado.
* `Max faces` Establece un límite superior en la cantidad de polígonos del objeto para evitar que tu dispositivo se bloquee.
* `Post subdivision` Activa el número elegido de subdivisiones de la sección de multirresolución del menú de topología. Esto se puede usar para hacer primitivas suavizadas, con esquinas suaves, en combinación con divisiones de topología bajas. Por ejemplo, establecer las divisiones de topología de una caja en 2 y las subdivisiones posteriores en 4 hará una caja con esquinas suaves.
* `Linear subdivision` Establece cuántos niveles de subdivisión lineal usar antes de usar la subdivisión suave normal. Esto se puede usar para controlar cuán afiladas o suaves son las esquinas en las superficies subdivididas. Por ejemplo, establece las divisiones de topología de una caja en 2, subdivisiones posteriores en 4 y luego prueba a cambiar las subdivisiones lineales entre 0 y 4. Las esquinas de la caja pasarán de suaves a afiladas.

### Topología {#topology}

Controla el número de polígonos en una primitiva. Normalmente los controles están vinculados, por lo que cambiar el único control deslizante activo ajustará todos los polígonos de manera uniforme. Puedes tocar el botón de desvincular y controlar por separado las divisiones X/Y/Z de una forma.

### Geometría {#geometry}

Controla el tamaño general de una primitiva, en unidades X/Y/Z para formas cuadradas y en radio para formas redondas.


### Esfera UV {#uv-sphere}
::: warning
La Esfera UV no es adecuada para esculpir, especialmente en los polos.

Por favor, prefiere las primitivas [Esfera](#sphere), [Caja](#box) o [Icosaedro](#icosahedron), junto con la opción `Project on sphere`.

Ten en cuenta que la topología puede ser aceptable para esculpir si usas un valor muy bajo para los deslizadores de `Division`.  
Luego puedes usar el deslizador `Overall Subdivision` para aumentar el número de polígonos.

Aunque no es adecuada para esculpido general, es útil para ojos; si rotas la esfera de modo que los polos se sitúen en la pupila, la distribución de polígonos se ajustará de forma natural para pintar y esculpir el iris y la pupila.
:::


### Triplanar {#triplanar}
Esta primitiva es especial en el sentido de que deberías usar la [herramienta de máscara](tools.md#mask) sobre ella para dar forma a la geometría.

![](/videos/triplanar.mp4)


::: tip
Toca dos veces en un plano y la cámara se centrará en ese plano en particular.  
Sin embargo, esto no funcionará si rotas la primitiva con el gizmo.
:::

Triplanar usa la información de máscara de 3 planos para rellenar una rejilla de vóxeles que luego se poligoniza (gracias al [Remallador de vóxeles](topology.md#voxel-remeshere)).

Cada plano tiene su propio plano de simetría.

::: warning
Cada vez que actualices el tamaño de la primitiva Triplanar, la calidad del pintado de la máscara se degradará.

Por ahora no hay opción para "bloquear" el pintado en un solo plano, pero quizá llegue en el futuro.  
Puedes usar la [Topología conectada](stroke.md#connected-topology) para ayudar un poco, en el sentido de que si tu cursor se encuentra precisamente en un plano no afectará a los otros planos.
:::

### Capturador de sombra {#shadow-catcher}
Añade un plano con el material de captura de sombras. Consulta el [material Shadow Catcher](material.md#shadow-catcher) para más detalles. 


## Grupo/Cámara {#groupcamera}
### Grupo {#group}
Crea un objeto "vacío" en el que puedes agrupar otros objetos como hijos. Esto se puede usar simplemente para organizar la jerarquía colocando muchos objetos bajo un grupo y luego cerrándolo. Un grupo también se puede usar como ayuda para mover objetos; muchos objetos se pueden colocar bajo un grupo y luego mover, rotar y escalar el grupo con la herramienta de gizmo.

### Añadir vista {#add-view}
Crea una cámara.

## Repetidores {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Los repetidores son nodos que crean instancias de los objetos que tienen debajo. 

### Matriz {#array}
![](/images/scene_primitive_array.webp)

Cuando los objetos se convierten en hijos de este nodo, pueden instanciarse en una disposición de rejilla. Cuando está seleccionado, tiene controles para:
* Fit inside - alterna entre controlar el tamaño de la rejilla/caja de la matriz o controlar el espacio entre las instancias de la matriz
* CountX/Y/Z - el número de instancias en cada eje
* OffsetX/Y/Z - distancia entre las instancias cuando Fit inside está activado
* SizeX/Y/Z - el ancho/alto/profundidad de la rejilla total de la matriz cuando Fit inside está activado.

### Curva {#curve}
![](/images/scene_primitive_curve.webp)
Esto creará una curva; los hijos de este nodo se repetirán a lo largo de la curva. Cuando está seleccionado, tiene controles para:
* Edit - permite añadir puntos a la curva y mover puntos en la curva.
* Snap - ajusta los puntos de la curva a otra geometría
* Align - rotará las formas hijas para alinearlas en la dirección de la curva
* Count - el número de instancias
* Closed - alterna la curva para unir el inicio y el final, o para que sea una curva abierta
* Radius - alterna controles en cada punto de la curva para controlar la escala de las instancias
* Twist - alterna controles en cada punto de la curva para controlar la rotación de torsión de las instancias 
* B-spline - alterna para que las instancias sigan la curva exactamente o usen interpolación B-spline, que tiene resultados más suaves. 

### Radial {#radial}
![](/images/scene_primitive_radial.webp)

Los hijos de este nodo se instanciarán en un círculo. Mueve el objeto hijo para modificar el radio de este repetidor. Cuando está seleccionado, tiene controles para:
* RadialX/Y/Z - al seleccionar estos botones se establecerá el eje radial y el número de instancias.



### Espejo {#mirror}
![](/images/scene_primitive_mirror.webp)

Los hijos de este nodo se reflejarán a través de un eje. Cuando está seleccionado tiene controles para:
* Gizmo - activa el gizmo de transformación para establecer el centro del espejo. También se puede rotar y escalar. Cuando termines, toca Gizmo de nuevo para mostrar los controles estándar.
* X/Y/Z - establece el plano de espejo

Todos los repetidores tienen un control `Validate`, que horneará los resultados del repetidor y preguntará cómo realizar el horneado:
* Join children - las instancias se unen en un solo objeto
* Keep instances - las instancias permanecen como instancias, pero ya no tienen el repetidor como "padre"
* Un-instances - las instancias se convierten en objetos únicos

::: tip Consejo: Combinar repetidores
Los repetidores se pueden agrupar unos bajo otros y varios objetos se pueden convertir en hijos de repetidores, lo que lleva a efectos complejos.

![](/images/scene_repeater_combine.webp)
:::

::: tip Consejo: Pivotes de repetidores

Algunos repetidores intentarán autoajustar el pivote de los objetos hijos, por lo que incluso si los mueves o rotas con la herramienta de gizmo, no se moverán. Si necesitas anular este comportamiento, inserta un grupo entre el repetidor y el hijo. Ahora puedes mover la forma hija independientemente del repetidor.
:::

## Luz {#light}

![](/images/scene_primitive_light.webp)

### Direccional {#directional}
Crea una luz direccional, una fuente de luz infinitamente lejana como el sol.

### Foco {#spot}
Crea una luz de foco, con controles sobre el ancho del cono y la suavidad

### Punto {#point}
Crea una luz puntual

## Avanzado {#advanced}
### Enfocar en elemento {#focus-on-item}
Al hacer doble clic en un elemento de la lista de Escena se centrará la cámara en ese elemento en la vista 3D.

### Sincronizar visibilidad {#sync-visibility}
Usar el icono del ojo afectará a todos los elementos seleccionados. 

### Instancia: Mostrar {#instance-show}
Muestra una cápsula de color a la izquierda de la lista de escena para indicar instancias.


### Iconos {#icons}
Establece el tamaño y la opacidad de los iconos de grupo, luz, cámara y espejo en el visor

### Líneas de jerarquía {#hierarchy-lines}
Muestra una línea entre el padre y sus hijos en el visor

## Barra de herramientas inferior {#bottom-toolbar}
Estos iconos alternarán la visibilidad de Grupo, Luz, Cámara, Repetidor y líneas de Jerarquía en el visor.