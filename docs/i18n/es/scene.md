# ![](/icons/scene.webp) Escena {#scene}

Este menú te permite gestionar los objetos, luces, cámaras y repetidores de Nomad. Muestra la jerarquía de la escena en una vista de árbol, desde la que puedes modificar muchos aspectos de tus objetos. También te permite crear objetos nuevos, así como combinarlos y separarlos de varias formas.


![](/images/scene_menu_summary.webp)


## Barra de accesos directos {#shortcut-bar}
| Acción                 | Icono                             | Descripción                                                                                                         |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Añadir...](#add-menu) | ![](/icons/plus.webp)            | Muestra el [menú Añadir](#add-menu) para añadir un objeto a la escena                                               |
| Eliminar               | ![](/icons/trash.webp)           | Elimina los objetos seleccionados. Sus hijos se conservan.                                                          |
| Bloquear               | ![](/icons/lock.webp)            | Impide seleccionar los objetos seleccionados en la vista 3d. Aún se pueden seleccionar desde la vista de árbol. Bloquear un grupo bloquea todo lo que contiene. Vuelve a tocar para desbloquear. |
| [Unir](#join)          | ![](/icons/merge.webp)           | Une los objetos seleccionados en un solo objeto, sin cambiar la geometría                                           |
| [Separar...](#separate) | ![](/icons/separate.webp)       | Muestra la ventana [Separar](#separate), para dividir un objeto en varios. Es lo contrario de la operación Unir      |
| [Booleano...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Muestra la ventana [Booleano](#boolean)                                                                       |
| Clonar                 | ![](/icons/clone.webp)           | Duplica los objetos seleccionados como objetos nuevos                                                               |
| Instancia              | ![](/icons/link.webp)            | Duplica los objetos seleccionados como instancias, de modo que los cambios de modelado en una se aplican a todas.   |
| Desinstanciar          | ![](/icons/unlink.webp)          | Convierte una instancia en una forma única, para que los cambios de modelado ya no se copien a las demás instancias |
| Sincronizar            | ![](/icons/checked.webp)         | Si está marcada, las operaciones se aplican a todas las instancias de los objetos seleccionados, no solo a los seleccionados. Solo está disponible cuando la selección contiene instancias. La [pestaña Sincronizar](#sync) de la ventana `Avanzado` define qué operaciones siguen esta casilla. |

::: tip
Cuando una operación vaya a afectar también a las demás instancias, aparece un pequeño icono de enlace en su botón.
:::


## Vista de árbol {#tree-view}
![](/images/scene_treeview.webp) 

La vista de árbol muestra los objetos, grupos, repetidores, luces y cámaras de la escena. Junto al nombre de una malla verás su número de vértices, con un icono de capa en color si tiene capas. Cada fila tiene estos botones:

| Acción       | Icono                      | Descripción              |
| :----------: | :------------------------: | :----------------------: |
| Nombre       | ![](/icons/pencil.webp)   | Cambia el nombre del objeto. Si está seleccionado, se renombran a la vez todos los objetos seleccionados, añadiendo un número. Mantén pulsado para renombrarlo junto con sus hijos. |
| Seleccionar  | ![](/icons/checked.webp)  | Selecciona o deselecciona |
| Visible      | ![](/icons/eye_open.webp) | Muestra u oculta         |
| Menú         | ![](/icons/more.webp)     | Muestra el [menú del objeto](#object-menu) |

::: tip CONSEJO: Seleccionar u ocultar muchos objetos rápidamente

Toca el icono de selección para cambiar un solo objeto, o arrastra en vertical sobre la columna de selección para seleccionar muchos objetos. Lo mismo funciona con la columna de visibilidad.

Mantén pulsado el icono de selección o de visibilidad para que afecte también a los hijos.

:::

### Cabecera de la vista de árbol {#tree-view-header}

La fila que hay encima de la lista tiene algunas ayudas:

* ![](/icons/sort_down.webp) - pliega o despliega todos los grupos a la vez.
* ![](/icons/preview.webp) - activa o desactiva las `Vistas previas de objetos`, una pequeña miniatura renderizada de cada objeto de la lista.
* ![](/icons/search.webp) - filtra la lista por nombre.

### Manipular la vista de árbol {#tree-view-manipulation}

Mantén pulsado un elemento de la vista de árbol hasta que se resalte. Entonces puedes moverlo hacia arriba o hacia abajo, o arrastrarlo sobre otro elemento para convertirlo en hijo de ese elemento.

Cuando hay muchos elementos seleccionados, uno de ellos es la selección principal y se muestra más brillante. Mantén pulsado y arrastra cualquiera de ellos para mover todos los objetos seleccionados a la vez.

Al seleccionar un elemento padre, por defecto también se seleccionan todos sus hijos. Si vuelves a tocar el padre, alternas entre seleccionar solo el padre o el padre y sus hijos.

Toca dos veces un elemento para centrar la cámara en él (ver [Avanzado](#focus-on-item)).

### Menú del objeto {#object-menu}

Al pulsar el botón de puntos suspensivos (...) de un objeto en la vista de árbol, se abre el menú del objeto.
Muchas de estas opciones son las mismas que las de la barra de accesos directos de arriba, repetidas por comodidad.

|       Acción        |                        Icono                       | Descripción                                                                                                                                                             |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Nombre       |              ![](/icons/pencil.webp)           | Cambia el nombre del objeto                                                                                                                                             |
|    Desinstanciar    |              ![](/icons/unlink.webp)           | Convierte una instancia en una forma única, para que los cambios de modelado ya no se copien a las demás instancias.                                                   |
|      Instancia      |               ![](/icons/link.webp)            | Duplica el objeto como instancia, de modo que los cambios de modelado en una se aplican a todas.                                                                        |
|       Clonar        |              ![](/icons/clone.webp)            | Duplica el objeto como un objeto nuevo                                                                                                                                  |
|      Eliminar       |              ![](/icons/trash.webp)            | Elimina el objeto. Sus hijos se conservan, salvo que `Hijos` esté marcado.                                                                                              |
|        Hijos        |            ![](/icons/hierarchy.webp)          | Si está marcado, `Instancia`, `Clonar` y `Eliminar` también actúan sobre los hijos del objeto.                                                                          |
| Separar por Partes  |             ![](/icons/separate.webp)          | Si un objeto está formado por partes desconectadas, crea un objeto distinto para cada una. Es lo contrario de la operación Unir.                                       |
| Separar por Grupos  |            ![](/icons/group.webp)          | Si un objeto tiene varios grupos de caras, crea un objeto distinto para cada grupo de caras.                                                                               |
| Separar por Capas   |              ![](/icons/layer.webp)            | Si un objeto tiene capas, crea objetos distintos para la malla base y para cada capa. Útil para enviar blendshapes a otras aplicaciones.                                 |
|   Unir → Capas      | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Si hay varios objetos seleccionados con la misma topología, los fusiona como capas del objeto principal (los demás objetos se eliminan). De nuevo, útil para blendshapes que vienen DE otras aplicaciones.<br><br> Ten en cuenta que las capas estarán desactivadas por defecto. Actívalas si necesitas ajustar sus reguladores. |
|  Curva (Repetidor)  |              ![](/icons/curve.webp)            | Solo para un tubo o un torno: añade un repetidor [Curva](#curve) que sigue la misma curva, como hijo del objeto.                                                        |
|        Tubo         |             ![](/icons/tube.webp)              | Para un torno, añade un [tubo](tools.md#tube) que sigue su perfil, como hijo. Para un cilindro, un cono o un toro, lo convierte en un tubo con la misma forma, para que puedas doblarlo a lo largo de una curva. |




### Selección múltiple {#multiselection}
Puedes seleccionar varios objetos para conseguir dos cosas:
- usar la herramienta gizmo para mover varios objetos a la vez
- fusionar objetos con las operaciones Unir y Booleano.

En la vista de árbol, toca el icono de selección de cada objeto o arrastra a lo largo de la columna de selección. Al tocar los nombres, mantén pulsado el acceso directo `Máscara` (o `Ctrl` en un teclado) para añadir o quitar un solo objeto, o el acceso directo `Suavizar` (o `Shift`) para seleccionar todos los objetos entre el actual y el que toques.

::: tip Selección múltiple rápida
También puedes seleccionar varios objetos en la vista 3d manteniendo pulsado el acceso directo `Suavizar` (o `Shift`) y tocando otra malla.

Para deseleccionar un objeto, vuelve a tocarlo (solo si la selección tiene más de un objeto).
:::

El gizmo mueve juntos todos los objetos seleccionados, ver [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Unir {#join}
Esta opción simplemente convierte varios objetos seleccionados en una sola entrada.
Los puntos y las UVs más cercanos que el [radio de soldadura](#weld-radius) se fusionan.

Puedes ver un ejemplo en vídeo en la sección [Separar](#separate).

## ![](/icons/bool_subtract_circle.webp) Booleano {#boolean}
![](/images/scene_boolean_menu.webp) 
Combina objetos en una sola superficie.

`Combinar Vóxel` conserva el volumen de los objetos y calcula nuevos polígonos regulares sobre la superficie. Gracias a este paso de cálculo, una combinación por vóxeles puede con geometrías complejas, pero puede perder detalle fino si la resolución elegida no es lo bastante alta.

`Booleano` intenta dejar los polígonos con su distribución original y cose los polígonos donde los objetos se solapan. El resultado puede ser mucho más limpio y nítido que con una combinación por vóxeles, pero requiere mallas "estancas": los objetos no pueden tener agujeros ni formas defectuosas. Si falla, normalmente funcionará una combinación por vóxeles.

### Operaciones booleanas {#boolean-operations}
Tanto Combinar Vóxel como Booleano usan la visibilidad de los objetos para controlar la operación, como recuerdan las indicaciones de la parte inferior de la ventana:

#### Unión {#union}
Con los dos objetos visibles se obtiene una **unión** booleana: se combina la piel exterior de los objetos, sin superficies interiores. ![](/images/boolean_union.webp)

#### Resta {#subtract}
Un objeto invisible = **resta** booleana: el objeto invisible se resta del visible. ![](/images/boolean_subtract.webp)

#### Intersección {#intersect}
Los dos objetos invisibles = **intersección** booleana: se crea una nueva forma solo donde los dos objetos se solapan. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Combinar Vóxel {#voxel-merge-button}
Este botón combina por vóxeles los objetos seleccionados. Si se aplica a un solo objeto, lo retopologiza con polígonos regulares, algo útil cuando un objeto tiene polígonos estirados. Las opciones de abajo funcionan como las del [Remallado por vóxeles](topology.md#voxel-remesher).

### Resolución {#resolution}
La resolución de la cuadrícula 3d de vóxeles usada en el cálculo. Al cambiar este valor, se superpone un tablero de ajedrez sobre el objeto para previsualizar el tamaño de los polígonos.

El cuentagotas junto al regulador toma el detalle de la densidad de la malla bajo tu dedo. El botón de al lado cambia el regulador a `Longitud del borde`, un tamaño en el mundo: así, el mismo valor da el mismo detalle en cualquier objeto.

### Construir multiresolución {#build-multiresolution}
Crea niveles de multiresolución por debajo de la resolución elegida. Así, si la resolución es 400 y Construir multiresolución está a 3, obtendrás una malla nueva de, por ejemplo, 296.000 polígonos, pero con 3 niveles de subdivisión inferiores de unos 74.000, 18.500 y 4.600.

### Engrosar las partes finas {#thicken-thin-parts}
Engrosa las partes demasiado finas para la cuadrícula de vóxeles, para que no se rompan. No está disponible con `Bordes nítidos` ni con `Borde nítido`.

### Agujeros {#holes}
Cómo se cierran los agujeros de los objetos abiertos antes de combinarlos:
* `Rellenar` - cada agujero se cierra por separado, a partir de su borde.
* `Forma` - los agujeros se cierran siguiendo la superficie que los rodea, y las piezas abiertas que se solapan se unen.

### ![](/icons/angle.webp) Mantener bordes nítidos {#keep-sharp-edges}
El botón `Bordes nítidos` ajusta la malla de vóxeles a las aristas vivas de los objetos. Funciona mejor con formas sencillas y puede introducir deformaciones en algunas zonas.

### ![](/icons/group.webp) Borde nítido {#sharp-border}
Las nuevas caras siguen los bordes de los grupos de caras, y un borde se mantiene nítido allí donde la superficie forma un pliegue a lo largo de él.

### ![](/icons/group_separate.webp) Mantener grupos separados {#keep-groups-separate}
Cada grupo de caras se remalla por separado: los grupos nunca se fusionan, y cada uno queda como una pieza cerrada en su propio grupo. En este modo no se construye la multiresolución.

### ![](/icons/bool_subtract_circle.webp) Botón Booleano {#boolean-button}
Este botón realiza una operación booleana de polígonos con la biblioteca Manifold de Emmett Lalish.

### ![](/icons/bool_unite_circle.webp) Limpiar solapamientos {#clean-overlaps}
Cuando solo hay un objeto seleccionado, el botón `Booleano` se convierte en `Limpiar solapamientos`: fusiona las partes del objeto que se cruzan entre sí en una superficie limpia.


## ![](/icons/separate.webp) Separar {#separate}
Si tienes un solo objeto formado por varias partes desconectadas, puedes separarlo en varios objetos.
Puedes verlo como lo contrario de [Unir](#join).

La ventana `Separar...` ofrece tres formas de separar los objetos seleccionados:
* `Separar por Partes` - crea un objeto distinto para cada parte desconectada.
* `Separar por Grupos` - crea un objeto distinto para cada grupo de caras.
* `Separar por Capas` - crea objetos distintos para la malla base y para cada capa.

![](/videos/merge_separate.mp4)


## ![](/icons/plus.webp) Menú Añadir {#add-menu}

![](/images/scene_addmenu_overview.webp)

Este menú crea primitivas, grupos, cámaras, repetidores y luces.

Las primitivas son formas básicas que se ajustan mediante parámetros. Cuando la primitiva está a tu gusto, la "validas", lo que convierte esos parámetros en una malla de polígonos que se puede esculpir y pintar. Una vez validada, ya no se pueden ajustar los parámetros de la primitiva.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) En gizmo {#on-gizmo}
Coloca la nueva primitiva donde estén la forma seleccionada o el gizmo. Si está desactivado, la primitiva se coloca en el centro de la escena.

### ![](/icons/gizmo.webp) Seleccionar gizmo {#select-gizmo}
Cambia automáticamente a la herramienta gizmo al crear una nueva primitiva.

### ![](/icons/cog.webp) Avanzado {#add-advanced}

Este menú te permite elegir dónde se crean las nuevas primitivas, grupos y repetidores: sobre el objeto seleccionado, en el origen del mundo o en la posición del gizmo.


### UVs {#uvs}
La opción `UVs` junto al título Primitivo activa las UVs en las primitivas. Las UVs (a menudo llamadas coordenadas de textura) son datos adicionales que se usan en 3d para poder aplicar texturas a las superficies. Ocupan más memoria, pero en la mayoría de los dispositivos no debería preocuparte, salvo que trabajes con muchísimos polígonos (por ejemplo, 10 millones o más).

### Primitivas {#primitives}

| Primitiva      | Icono                                     | Descripción                                                                                                     |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Caja           | ![](/icons/cube.webp)                    | Un simple cubo; puedes controlar las divisiones en X, Y y Z                                                     |
| Esfera de quads | ![](/icons/circle.webp)                 | Una caja subdividida con `Proyectar en esfera` forzado, así que tiene una distribución regular de cuadrángulos, ideal para esculpir |
| Cilindro       | ![](/icons/cylinder.webp)                | Puedes añadir un agujero central al cilindro, por ejemplo para hacer un tubo hueco                              |
| Toro           | ![](/icons/torus.webp)                   | El toro puede ser un buen punto de partida para hacer anillos                                                   |
| Cono           | ![](/icons/cone.webp)                    | -                                                                                                               |
| Icosaedro      | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| Esfera UV      | ![](/icons/circle.webp)                  | Una esfera con una distribución irregular de polígonos, ver la [advertencia de abajo](#uv-sphere)               |
| Plano          | ![](/icons/rectangle.webp)               | Un simple plano; ten en cuenta que es la única primitiva que no está cerrada                                    |
| Texto          | ![](/icons/text.webp)                    | Texto en 3d, con fuente, estilo, alineación, profundidad y curvatura. `Fusionar letras` une las letras que se tocan |
| Tubo           | ![](/icons/tube.webp)                    | ver [Tubo](tools#tube)                                                                                          |
| Torno          | ![](/icons/lathe.webp)                   | ver [Torno](tools#lathe)                                                                                        |
| Triplanar      | ![](/icons/triplanar.webp)               | ver [Triplanar](#triplanar)                                                                                     |
| VDM            | ![](/icons/vdm.webp)                     | Un plano preparado para esculpir un sello de desplazamiento vectorial: incluye UVs y mira hacia la cámara       |
| Capturador de sombras | ![](/icons/material_shadow_catcher.webp) | ver [Capturador de sombras](#shadow-catcher)                                                             |
| Cabeza         | ![](/icons/face.webp)                    | Una cabeza sencilla con una capa para pasar de masculina a femenina                                             |

::: tip
Si te preguntas qué es la malla base que aparece al abrir Nomad: también es una caja subdividida.
Sin embargo, la malla base de Nomad no usa `Proyectar en esfera`, así que no es perfectamente redonda.
:::

### Barra de herramientas de la primitiva {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

Al crear una primitiva, aparece una barra de herramientas para controlar sus parámetros.

* `Validar` Convierte la primitiva en un objeto normal para poder esculpirla y pintarla.
* `Espejo` Coloca o quita un repetidor espejo por encima de la primitiva.
* `Todo` (icono del ojo) Elige qué controladores se muestran directamente sobre la primitiva para ajustar sus parámetros, por ejemplo el ancho del cubo o el radio del agujero de un cilindro: `Ninguno`, `Todo` o solo un tipo (radio, agujero, perfil...) según la primitiva.
* `División` El número de divisiones de la primitiva, aquí a lo largo de X para una caja.
* `Densidad constante` Cuando estiras la primitiva a lo largo de un eje con el gizmo, crecen su tamaño y sus divisiones en lugar de estirarse los polígonos, así que las caras siguen siendo cuadradas. Disponible en cajas, planos y cilindros.
* `...` Muestra el menú de la primitiva.

Algunas primitivas tienen opciones adicionales en la barra:

* `Esfera` La esfera se construye como un cubo subdividido, porque es mejor para esculpir, pero eso significa que no es perfectamente redonda. Esta opción acerca la forma a una esfera perfecta. El icosaedro también tiene esta opción.
* `Tapa` Activa o desactiva las tapas de los extremos de una forma; por ejemplo, un cilindro puede tener tapa arriba, abajo, en ambos lados o en ninguno.
* `Agujero` Crea un agujero que atraviesa el centro de la forma. Alterna entre sin agujero, agujero con un solo radio o agujero con un radio distinto arriba y abajo.
* `Radio` Elige si un cilindro tiene un solo radio o uno distinto arriba y abajo.
* `Disco` Elige si un plano tiene forma de cuadrilátero o de círculo.

La pequeña barra que hay debajo de la barra principal te permite cambiar entre el gizmo de la primitiva y el gizmo de transformación.

::: tip

Al pulsar el título de la barra, esta se mueve a la parte superior o inferior de la pantalla. Al pulsar la flecha de la esquina, se pliega.

:::


### Menú de la primitiva {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Contiene todos los parámetros de la primitiva seleccionada. Los parámetros son la descripción básica de una forma. Para describir un anillo, por ejemplo, darías su radio exterior, su radio interior y el número de polígonos.

La mayoría de los parámetros de las primitivas se explican por sí solos, y hay algunos comunes a todas las primitivas:

* `UVs` El pequeño botón UVs de la parte superior del menú activa o desactiva la creación de coordenadas UV
* `Validar` El pequeño botón de validar convierte la primitiva en un objeto normal para poder esculpirla y pintarla.
* `Caras máx.` Fija un límite de polígonos para el objeto, para evitar que el dispositivo se bloquee.
* `Postsubdivisión` Aplica el número de subdivisiones elegido desde la sección Multiresolución del menú Topología. Combinado con pocas divisiones de topología, sirve para crear primitivas suavizadas, con esquinas redondeadas. Por ejemplo, con las divisiones de topología de una caja a 2 y la postsubdivisión a 4, obtendrás una caja con esquinas suaves.
* `Subdivisión lineal` Fija cuántos niveles de subdivisión lineal se usan antes de pasar a la subdivisión suave normal. Sirve para controlar lo vivas o suaves que quedan las esquinas en las superficies subdivididas. Por ejemplo, pon las divisiones de topología de una caja a 2 y la postsubdivisión a 4, y luego prueba a cambiar la subdivisión lineal entre 0 y 4. Las esquinas de la caja pasarán de suaves a vivas.

### Topología {#topology}

Controla el número de polígonos de una primitiva. Normalmente los controles están vinculados, así que al cambiar el único regulador activo se ajustan todos los polígonos por igual. Puedes tocar el botón de desvincular para controlar por separado las divisiones X/Y/Z de una forma.

### Geometría {#geometry}

Controla el tamaño general de una primitiva, en unidades X/Y/Z para las formas cuadradas y en radio para las redondas.


### ![](/icons/circle.webp) Esfera UV {#uv-sphere}
::: warning
La esfera UV no es muy adecuada para esculpir, sobre todo en los polos.

Es preferible usar la [primitiva](#primitives) Esfera de quads, Caja o Icosaedro, con la opción `Proyectar en esfera`.

Ten en cuenta que la topología puede ser aceptable para esculpir si usas un valor muy bajo en los reguladores `División`.
Después puedes usar el regulador `Subdivisión general` para aumentar el número de polígonos.

Aunque no sirve para esculpir en general, es útil para los ojos: si giras la esfera para que los polos queden en la pupila, la distribución de los polígonos se adapta de forma natural para pintar y esculpir el iris y la pupila.
:::


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
Esta primitiva es especial: para dar forma a la geometría, debes usar la [herramienta Máscara](tools.md#mask) sobre ella.

![](/videos/triplanar.mp4)


::: tip
Toca dos veces un plano y la cámara se centrará en ese plano en concreto.
Eso sí, no funciona si giras la primitiva con el gizmo.
:::

Triplanar usa la información de máscara de 3 planos para rellenar una cuadrícula de vóxeles que luego se convierte en polígonos (gracias al [Remallado por vóxeles](topology.md#voxel-remesher)).

Cada plano tiene su propio plano de simetría.

::: warning
Cada vez que cambias el tamaño de la primitiva Triplanar, la calidad de la máscara pintada se degrada.

Por ahora no hay ninguna opción para "bloquear" la pintura en un solo plano, aunque quizá llegue en el futuro.
Puedes usar la [Topología conectada](stroke.md#connected-topology) para ayudarte un poco: si el cursor está justo sobre un plano, no afectará a los demás.
:::

### ![](/icons/material_shadow_catcher.webp) Capturador de sombras {#shadow-catcher}
Añade un plano con el material capturador de sombras. Consulta [Material capturador de sombras](material.md#shadow-catcher) para más detalles.


## Grupo/Cámara {#groupcamera}
### ![](/icons/share.webp) Grupo {#group}
Crea un objeto "vacío" del que pueden colgar otros objetos. Sirve simplemente para organizar la jerarquía: metes muchos objetos en un grupo y luego lo pliegas. Un grupo también puede ayudarte a mover objetos: colocas muchos objetos dentro de un grupo y luego mueves, giras o escalas el grupo con la herramienta gizmo.

### ![](/icons/camera.webp) Cámara {#add-view}
Crea una cámara.

## Repetidores {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Los repetidores son nodos que crean instancias de los objetos que cuelgan de ellos.

### ![](/icons/array.webp) Matriz {#array}
![](/images/scene_primitive_array.webp)

Los objetos que se hacen hijos de este nodo se pueden repetir como instancias en una cuadrícula. Cuando está seleccionado, tiene controles para:
* `Ajustar dentro` - si está activado, todas las copias se colocan dentro de los límites de la matriz; si no, los reguladores fijan el espacio entre copias
* `Cantidad X/Y/Z` - el número de instancias en cada eje
* `Tamaño X/Y/Z` - el tamaño de la cuadrícula en cada eje, o la distancia entre copias cuando `Ajustar dentro` está desactivado
* `Aleatorizar...` - añade variaciones aleatorias a las copias, ver [Aleatorizar](#curve) más abajo.

### ![](/icons/curve.webp) Curva {#curve}
![](/images/scene_primitive_curve.webp)
Crea una curva; los hijos de este nodo se repiten a lo largo de ella. Cuando está seleccionado, tiene controles para:
* `Curva` - edita la curva: añade puntos y mueve los puntos de la curva.
* `Mostrar` - muestra u oculta la curva y sus puntos.
* `Ajustar` - ajusta los puntos de la curva a otra geometría.
* `Sim` - edita la curva de forma simétrica.
* `Cerrado` - une el principio y el final de la curva, o la deja abierta.
* `B-spline` - hace que las instancias sigan la curva exactamente, o usa una interpolación B-spline, que da resultados más suaves.
* `Deformar` - dobla cada copia a lo largo de la curva para que se una a sus vecinas (`Suave` curva sus lados para que se unan sin ángulo).
* `Alinear` - gira las copias para que sigan la dirección de la curva.
* `Pivote` - el pivote de las copias: la propia curva (`Propia`) o sus hijos.
* `Cantidad` - el número de instancias. El botón de modo que hay al lado cambia a `Distancia`: un espaciado fijo entre copias, y la cantidad depende de la longitud de la curva.
* `Radio` - controles en cada punto de la curva para fijar la escala de las instancias.
* `Torsión` - controles en cada punto de la curva para fijar la torsión de las instancias.
* `Alternar` - gira una de cada dos copias alrededor de la curva: 90° para los eslabones de una cadena, 180° para hojas o dientes de cremallera, alrededor del `Eje` que elijas.
* `Espiral...` - enrolla las copias alrededor de la curva, en varias hebras (cuerda, trenza, cinta...).
* `Aleatorizar...` - añade variaciones aleatorias a las copias; cada fila puede, en cambio, sumar la misma cantidad en cada copia.

Debajo de la barra, la opción `(fusionar)` fusiona un punto con otro cuando lo arrastras sobre él. `IK` (cinemática inversa) te permite posar la curva: arrastra un punto y los puntos conectados lo siguen. Toca un punto para bloquearlo o desbloquearlo, o mantén pulsado para bloquearlos o desbloquearlos todos; los puntos bloqueados no se mueven.

### ![](/icons/radial.webp) Radial {#radial}
![](/images/scene_primitive_radial.webp)

Los hijos de este nodo se repiten en círculo. Mueve el objeto hijo para cambiar el radio de este repetidor. Cuando está seleccionado, tiene controles para:
* RadialX/Y/Z - estos botones fijan el eje radial y el número de instancias.



### ![](/icons/mirror.webp) Espejo {#mirror}
![](/images/scene_primitive_mirror.webp)

Los hijos de este nodo se reflejan respecto a un eje. Cuando está seleccionado, tiene controles para:
* Gizmo - activa el gizmo de transformación para fijar el centro del espejo, que también se puede girar y escalar. Cuando termines, vuelve a tocar Gizmo para ver los controles normales.
* X/Y/Z - fija el plano del espejo

### ![](/icons/surface.webp) Superficie {#surface}

Los hijos de este nodo se copian sobre la superficie de un objeto: una copia por cara, por arista o por vértice, o repartidas al azar. Cuando está seleccionado, tiene controles para:
* Modo - coloca las copias en las `Caras`, las `Aristas` o los vértices, o las reparte con `Dispersar`.
* Cada - una copia cada N caras, aristas o vértices. `Aleatorio` las elige al azar, y `Redistribuir` saca otra tanda aleatoria.
* Espaciado - al dispersar, la distancia mínima entre dos copias.
* Alinear - las copias se apoyan sobre la superficie siguiendo su normal, en lugar de mantener la orientación del original.
* Ajustar - proyecta el original sobre el punto más cercano de la superficie, y las copias lo siguen.
* Ajustar tamaño, Cizallamiento - escalan y estiran las copias según la forma de cada cara.
* Deformar - dobla cada copia sobre su cara, o a lo largo de su arista, para que las copias vecinas se unan sin huecos.

Todos los repetidores tienen un control `Validar`, que convierte el resultado del repetidor en objetos fijos y te pregunta cómo hacerlo:
* Unir hijos - las instancias se unen en un solo objeto
* Mantener instancias - las instancias siguen siendo instancias, pero ya no tienen el repetidor como "padre"
* Desinstanciar - las instancias se convierten en objetos únicos

`Aplanar todo` también valida los repetidores anidados dentro de este, de modo que cada copia se convierte en un objeto normal.

::: tip Consejo: Combinar repetidores
Los repetidores pueden colgar unos de otros, y puedes hacer varios objetos hijos de un repetidor, lo que permite crear efectos complejos.

![](/images/scene_repeater_combine.webp)
:::

::: tip Consejo: Pivotes de los repetidores

Algunos repetidores intentan fijar automáticamente el pivote de los objetos hijos, así que aunque los muevas o gires con la herramienta gizmo, no se moverán. Si necesitas evitarlo, inserta un grupo entre el repetidor y el hijo. Así podrás mover la forma hija independientemente del repetidor.
:::

## Luz {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Direccional {#directional}
Crea una luz direccional, una fuente de luz infinitamente lejana, como el sol.

### ![](/icons/panorama.webp) Entorno {#environment}
Crea una luz de entorno, que ilumina la escena a partir de una imagen que la rodea por completo (iluminación basada en imagen, como un HDRI).

### ![](/icons/spotlight.webp) Foco {#spot}
Crea un foco, con controles para la apertura y la suavidad del cono

### ![](/icons/light.webp) Punto {#point}
Crea una luz puntual

## ![](/icons/cog.webp) Avanzado {#advanced}
El botón `Avanzado`, abajo a la izquierda del panel, abre una ventana con dos pestañas: `General` y `Sincronizar`.

### ![](/icons/focus.webp) IU: Enfocar en el elemento al hacer doble toque {#focus-on-item}
Al tocar dos veces un elemento de la lista de la escena, la cámara se centra en él en la vista 3d.

### ![](/icons/eye_open.webp) Sincronizar visibilidad {#sync-visibility}
Si está activado, al usar el icono del ojo de un elemento seleccionado se ven afectados todos los elementos seleccionados.

### ![](/icons/bang.webp) Resaltar selección {#highlight}
Resalta los objetos seleccionados en la vista 3d cuando cambia la selección.

### ![](/icons/link.webp) Mostrar (Instancia) {#instance-show}
Muestra una cápsula de color a la izquierda de la lista de la escena para indicar las instancias.

### ![](/icons/preview.webp) Vistas previas de objetos {#object-previews}
Muestra una miniatura renderizada de cada objeto en la lista de la escena. Es lo mismo que el botón de vista previa que hay encima de la lista.

### Radio de soldadura {#weld-radius}
Bajo el título `Unir`, `Radio de soldadura de posición` y `Radio de soldadura de UV`: los puntos y las UVs más cercanos que estos radios se fusionan. Cada uno se puede desactivar con su casilla. Se aplica a Unir, Booleano, Recortar, Diezmar, los remallados y la importación de archivos.

### Iconos {#icons}
Fija el `Tamaño` mínimo y máximo y la `Opacidad` de los iconos de grupos, luces, cámaras y repetidores en la vista 3d.

### ![](/icons/hierarchy.webp) Líneas de jerarquía {#hierarchy-lines}
Muestra una línea entre cada padre y sus hijos en la vista 3d. Si está activado, también puedes ajustar:
* `Usar pivote de Nomad` - las líneas parten del pivote que usan las herramientas Transformar y Gizmo. Si está desactivado, usan el pivote base natural, que puede estar lejos del centro del objeto.
* `Espesor` - el grosor de las líneas. El botón junto al regulador les añade un contorno.
* El color de las líneas.

### ![](/icons/link.webp) Sincronizar {#sync}
La pestaña `Sincronizar` define, para cada operación (`Añadir`, `Eliminar`, `Bloquear`, `Clonar`, `Instancia`, `Desinstanciar`, `Unir`, `Separar` y `Booleano`), si se aplica a todas las instancias de la selección:
* `Auto` - sigue la casilla `Sincronizar` de la parte superior del menú Escena.
* `No` - solo los objetos seleccionados.
* `Sí` - siempre todas las instancias.

Por defecto, `Unir`, `Separar` y `Booleano` están en `Sí` y las demás en `Auto`. `Restablecer` recupera estos valores por defecto.

## Barra de herramientas inferior {#bottom-toolbar}
Estos iconos muestran u ocultan en la vista 3d los grupos, las luces, las cámaras, los repetidores y las líneas de jerarquía. Los iconos que aparecen en el lienzo se pueden tocar para seleccionarlos y editarlos directamente.
