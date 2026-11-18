# ![](/icons/multires.webp) Topología {#topology}

Este menú controla la topología de los objetos en Nomad, e incluye herramientas para hornear y transferir detalles entre objetos, y entre texturas.

![](/images/topology_overview.webp)

Nomad trabaja con polígonos: usa triángulos y cuadrángulos para representar la geometría.
Cuando hablamos de topología, nos referimos tanto al número de caras como a la forma en que se conectan los puntos (vértices).

Es importante vigilar la topología, sobre todo si quieres esculpir o pintar detalles finos.

::: tip ¿Cómo vigilar la topología?
Puedes mostrar la [Malla alámbrica](settings.md#wireframe) o simplemente desactivar el [Sombreado suave](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

El menú Topología de Nomad tiene varias pestañas, repartidas en dos filas:

| Método                                | Icono                        | Descripción                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolución](#multiresolution)   | ![](/icons/multires.webp)   | Edita varios niveles de detalle mediante subdivisión             |
| [Remallado por vóxeles](#voxel-remesher) | ![](/icons/voxel.webp)   | Calcula una nueva topología de densidad uniforme                 |
| [Topología dinámica](#dynamic-topology) | ![](/icons/dynamic.webp)  | Añade o quita caras localmente y en tiempo real mientras esculpes o pintas |
| [Varios](#misc)                       | ![](/icons/topo_extra.webp) | Cierra agujeros, fuerza el manifold y convierte a triplanar      |
| [Primitivo](#primitive)               | ![](/icons/dot.webp)        | Opciones de la primitiva                                         |
| [Diezmar](#decimation)                | ![](/icons/decimate.webp)   | Reduce el número de caras conservando la forma                   |
| [Remallado de cuadrángulos](#quad-remesh) | ![](/icons/quad.webp)   | Reconstruye el objeto con una distribución limpia de cuadrángulos |
| [Desplegado UV](#uv-unwrap)           | ![](/icons/uv.webp)         | Crea UVs para texturizar                                         |
| [Hornear](#bake)                      | ![](/icons/bake.webp)       | Hornea detalles y pintura en texturas, vértices o sellos VDM     |


## Estadísticas de polígonos {#polygon-stats}

![](/images/topology_stats.webp)

La parte superior de cada pestaña muestra el número de polígonos del objeto seleccionado, y también el de toda la escena cuando hay más de un objeto. Las columnas indican el número de vértices, triángulos, cuadrángulos (polígonos de 4 lados) y coordenadas UV (0 si el objeto no tiene UVs).

Toca esta sección para ver la lista de todos los objetos de la escena con sus cifras exactas, incluido su número de grupos de caras.

## ![](/icons/cog.webp) Menú del engranaje {#gear-menu}
Algunas secciones, como las de las pestañas [Remallado de cuadrángulos](#quad-remesh) y [Hornear](#bake), tienen opciones adicionales. Ábrelas con el icono del engranaje que hay junto al título de la sección.

## ![](/icons/multires.webp) Multiresolución {#multiresolution}

![](/images/topology_multires_menu.webp)

### ¿Qué es la multiresolución? {#what-is-multiresolution}
La multiresolución resulta útil en dos situaciones principales:
- El algoritmo de subdivisión suave, para aumentar el número de polígonos del objeto
- Manejar varios niveles de resolución, para alternar entre retoques a pequeña y a gran escala

![](/videos/multiresolution.mp4)

#### Flujo de trabajo con multiresolución {#multiresolution-workflow}
Lo más interesante de la multiresolución es que puedes volver a una resolución más baja, hacer cambios en el objeto y regresar después a la resolución más alta sin perder los detalles finos. Todos los detalles de alta resolución se reproyectan automáticamente.

Las [Capas](layers.md#layers) están disponibles en todas las resoluciones.

::: warning
Si usas una herramienta que modifica la topología del objeto, ¡perderás todas sus demás resoluciones!
Nomad siempre debería avisarte antes de que ocurra, por ejemplo al usar:
- el [Remallado por vóxeles](#voxel-remesher)
- la [Topología dinámica](#dynamic-topology)
- la [herramienta Recortar](tools.md#trim)
- la [herramienta Dividir](tools.md#split)
:::


### Regulador de multiresolución {#multiresolution-slider}
Este regulador indica el número de niveles de subdivisión del objeto actual. Si hay 6 barras verticales, hay 6 niveles de subdivisión. El círculo marca el nivel de subdivisión que se muestra en ese momento.

Unos pequeños iconos encima del regulador indican qué opciones (`Bloquear nivel 0`, `Lineal`, `Borde nítido`, `Mantener triángulos`) se usaron en cada nivel.

### Reverso {#reverse}
Cuando estás en el nivel de subdivisión más bajo, el botón Reverso intenta crear un nivel por debajo del actual. Ten en cuenta que, por lo general, solo funciona si el objeto se creó a partir de una subdivisión, ya sea en Nomad o en otras aplicaciones 3d que usan superficies de subdivisión multiresolución.

### Subdividir {#subdivide}
El botón *Subdividir* multiplica por 4 el número de polígonos, así que vigila bien la cifra, ¡porque puede crecer muy deprisa! Nomad te pide confirmación cuando el resultado vaya a ser muy pesado.
Una característica importante de las *superficies de subdivisión* es que tienden hacia una *superficie suave*.
Para entender cómo funciona, prueba el botón *Subdividir* con un objeto de pocos polígonos.

Puedes desactivar este comportamiento *suave* con la opción `Lineal`.

### Eliminar inferior {#delete-lower}
Elimina las subdivisiones que haya por debajo del nivel mostrado. Si lo haces sin querer, puedes recrearlas con el botón Reverso.

### Eliminar superior {#delete-higher}
Elimina las subdivisiones que haya por encima del nivel mostrado.

### ![](/icons/lock.webp) Bloquear nivel 0 {#lock-lv0}
Conserva la forma del nivel de subdivisión más bajo mientras esculpes en los niveles superiores. La pintura sí se transmite al nivel 0. Puede ser importante si el objeto se creó en otra aplicación y el objeto base no debe cambiar.

Esta opción solo está disponible antes de la primera subdivisión. Si está desactivada, los cambios grandes hechos en niveles de subdivisión altos moverán el nivel 0.

### ![](/icons/linear.webp) Lineal {#linear-subdivision}
Subdivide la malla sin aplicar ningún suavizado.

### ![](/icons/group.webp) Borde nítido {#sharp-border}
Si el objeto tiene grupos de caras, esta opción mantiene nítidos los bordes entre grupos. Se puede ajustar en cada nivel de subdivisión (el regulador de subdivisión muestra un pequeño icono encima del nivel para indicarlo).

### ![](/icons/triangle.webp) Mantener triángulos {#keep-triangles}
La mayoría de los sistemas estándar de superficies de subdivisión intentan convertir todos los polígonos en cuadrángulos al subdividir. Esta opción obliga a la subdivisión a usar triángulos.

::: tip

Por defecto, la subdivisión suaviza todas las aristas vivas. Para conservarlas un poco marcadas, prueba a usar `Lineal` o `Borde nítido` en los 2 primeros niveles de subdivisión y desactívalo en los niveles superiores. Así obtendrás una malla subdividida semidefinida.

:::

### Mostrar nivel más alto {#show-highest-level}
Muestra el nivel más alto, con todos sus detalles, mientras esculpes en un nivel inferior. Muy práctico para ver el resultado final mientras haces cambios grandes.

### Malla alámbrica: Solo nivel 0 {#wireframe-level-0-only}
Cuando la [Malla alámbrica](settings.md#wireframe) está activada, muestra solo la del nivel más bajo. La malla alámbrica densa de los niveles altos puede tapar la forma.


## ![](/icons/voxel.webp) Remallado por vóxeles {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Al usar el `Remallado por vóxeles`, toda la malla pasa a tener una resolución uniforme, es decir, todos los polígonos tienen más o menos el mismo tamaño. Es muy útil cuando no quieres preocuparte por la topología y prefieres esculpir libremente.

Un flujo de trabajo típico puede empezar con el `Remallado por vóxeles` para encajar una forma aproximada a baja resolución.
Basta con pulsar el botón *Remallar* de vez en cuando, cuando estires demasiado la malla, para evitar que se deforme en exceso.

![](/videos/voxel_remesher.mp4)


::: tip ¿Vóxeles?
Como decíamos, Nomad es un programa basado en polígonos, pero el `Remallado por vóxeles` es una excepción: usa (temporalmente) otro enfoque para hacer el remallado.

Una gran diferencia es que el enfoque por vóxeles no admite autointersecciones, así que estas se resuelven.
Tampoco admite mallas con agujeros.

Por agujeros no nos referimos al `agujero topológico` (el `agujero` de un dónut), sino a las mallas que no son `estancas`/`cerradas`.
En la práctica, esto significa que antes de remallar se rellenan todos los agujeros, de forma parecida a la [herramienta Recortar](tools.md#trim) o a la [función de relleno de agujeros](#holes). La opción [Agujeros](#voxel-holes) de más abajo decide cómo.
:::

### ![](/icons/voxel.webp) Remallar {#voxel-remesh}
Ejecuta el remallado por vóxeles. Unos pequeños iconos en el botón te recuerdan qué opciones de las de abajo están activadas.

### Resolución {#voxel-resolution}
El tamaño de los vóxeles usados en el cálculo: los valores más altos dan más detalle. Mientras cambias este parámetro, se superpone un patrón de tablero de ajedrez sobre la malla para darte una vista previa del resultado.

El cuentagotas toma la resolución de la densidad de la malla en el punto que toques. El botón del cubo que hay al lado cambia el valor a una `Longitud del borde` en unidades del mundo: así, el mismo valor da el mismo detalle en cualquier objeto.

### Construir multiresolución {#build-multiresolution}
Crea niveles de multiresolución inferiores para el remallado por vóxeles. Si usas el tablero de ajedrez para fijar una resolución y pones Construir multiresolución a 2, el resultado final tendrá el detalle que marca el regulador de resolución y, si vas a la pestaña Multiresolución, estará en el nivel 2, es decir, tendrás mallas de multiresolución de menor resolución en los niveles 1 y 0. Es una buena forma de obtener a la vez una malla limpia con polígonos regulares y una malla de control de baja resolución.

Además, es más rápido y usa menos memoria a resoluciones altas. Pero con una resolución baja y muchos niveles, perderás detalles.

::: tip Consejo: Construir multiresolución y suavizado estable

A veces esta opción crea "bucles" en la geometría difíciles de suavizar, que dejan pequeños granitos. Si te ocurre, activa "Suavizado estable" en las opciones de la herramienta Suavizar.

:::

### Engrosar las partes finas {#thicken-thin-parts}
Las partes más finas que los vóxeles pueden romperse o desaparecer durante el remallado. Esta opción las engrosa para que sobrevivan; cuanto más alto el valor, más las engrosa. No está disponible con `Bordes nítidos` ni con `Borde nítido`.

### Agujeros {#voxel-holes}
Cómo se cierran los agujeros antes de remallar:

* `Rellenar` - Cada agujero se cierra por separado, a partir de su borde.
* `Forma` - Los agujeros se cierran siguiendo la superficie que los rodea, y las piezas abiertas que se solapan se unen.

### ![](/icons/angle.webp) Bordes nítidos {#keep-sharp-edges}
Ajusta los nuevos puntos a las aristas vivas de la malla original. Sobre todo es útil para operaciones booleanas sencillas entre primitivas, y puede introducir deformaciones.

### ![](/icons/group.webp) Borde nítido {#voxel-sharp-border}
Las nuevas caras siguen los bordes de los grupos de caras, y un borde se mantiene nítido allí donde la superficie forma un pliegue a lo largo de él.

### ![](/icons/group_separate.webp) Mantener grupos separados {#keep-groups-separate}
Cada grupo de caras se remalla por separado: los grupos nunca se fusionan, y cada uno queda como una pieza cerrada en su propio grupo. En este modo no se construye la multiresolución. Está disponible cuando el objeto tiene varios grupos de caras.

## ![](/icons/dynamic.webp) Topología dinámica {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
La multiresolución y el remallado por vóxeles son métodos habituales en la industria para controlar la topología, pero ambos te obligan a vigilar que no estires demasiado los polígonos ni los aprietes en exceso.

La topología dinámica es un método alternativo. Mientras esculpes, Nomad añade y quita polígonos de forma adaptativa durante el trazo: al tallar detalles pequeños se añaden muchos polígonos pequeños justo donde los necesitas, y al suavizar en otras zonas se eliminan polígonos.

Ten en cuenta que la topología dinámica usa triángulos en lugar de cuadrángulos. Puede verse algo desordenado, pero casi es mejor no mirar la malla alámbrica: céntrate en conseguir una escultura bonita sin preocuparte por la topología y, más adelante, usa alguna de las otras herramientas de remallado de Nomad para generar una malla limpia de cuadrángulos.

Mira el vídeo de abajo para verla en acción.

![](/videos/dynamic.mp4)

### Habilitado {#enabled}
Activa la topología dinámica. Aparecerá un icono DynTopo debajo de los reguladores de radio e intensidad del pincel, para activar o desactivar DynTopo en cada herramienta. Puede afectar notablemente al rendimiento, y las capas se actualizan correctamente.

### Detalle {#dyn-detail}
Controla la cantidad de detalle; su comportamiento cambia según lo elegido en "Detalle basado en...", ver abajo. En modo `Pantalla`, la etiqueta muestra el tamaño objetivo de los triángulos en píxeles. En modo `Constante`, un cuentagotas te permite tomar el detalle de la densidad de la malla en el punto que toques.

### Detalle basado en... {#detail-based-on}
| Método    | Descripción                                                     |
| :-------: | :-------------------------------------------------------------: |
| Pantalla  | El nivel de detalle depende del tamaño del objeto en la pantalla. Con el regulador de detalle al 100 % o más obtienes detalle fino, con triángulos pequeños; al 1 %, poco detalle, con triángulos grandes.  |
| Radio     | El radio de la herramienta define la cantidad de detalle. Usa un radio pequeño para el detalle fino y uno grande para poco detalle. El regulador de detalle actúa como multiplicador de esta relación.                     |
| Constante | El regulador de detalle define la cantidad de detalle, sin que influyan el tamaño en pantalla ni el de la herramienta. Es el mismo valor que el regulador [Detalle](#all-detail) de `Remallar`.             |

::: tip CONSEJO: Modo Radio

Para entender mejor cómo funciona el modo Radio, empieza a mover el regulador de detalle con un dedo y, al mismo tiempo, cambia el radio de la herramienta con otro dedo. Verás cómo están vinculados.

:::

### Preferir... {#prefer}
| Método    | Descripción               |
| :-------: | :-----------------------: |
| Velocidad | Prioriza el rendimiento   |
| Calidad   | Prioriza la calidad       |

Cuando priorizas la `Calidad`, hay 2 diferencias principales:
- el refinamiento se aplica antes de esculpir, así que aparecen menos artefactos de interpolación al pintar o esculpir detalles muy pequeños
- el refinamiento se repite hasta alcanzar el nivel de detalle correcto, en lugar de avanzar poco a poco.

Así, aunque esculpas detalles muy pequeños o hagas trazos rápidos, la topología siempre se refinará como esperas


### ![](/icons/pressure.webp) Aplicar presión sobre el radio {#use-pressure-on-radius}
Solo tiene efecto si `Radio` está activado. Si está activa, el nivel de detalle siempre reflejará el tamaño del pincel, incluso cuando la presión del lápiz modifique ese tamaño.

### Usar atenuación del trazo {#use-stroke-falloff}

Incluye también la curva de atenuación y el alfa del pincel en los cálculos de DynTopo.

### Método {#method}
Elige cómo modifica la malla la topología dinámica, tanto mientras esculpes como cuando usas [Remallar](#dyn-remesh):

| Método         | Descripción                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformidad    | Puede añadir y quitar caras; es el modo que se usa en el vídeo de arriba |
| Subdivisión    | Solo añade caras nuevas, no puede quitarlas                           |
| Diezmado       | Solo quita caras, no puede añadir caras nuevas                        |

### ![](/icons/shield.webp) Proteger área enmascarada {#protect-masked-area}
Hace que las zonas enmascaradas protejan la topología para que no cambie.

### ![](/icons/normal.webp) Extrapolación de vértices {#vertex-extrapolation}
Coloca los puntos sobre una superficie suave que sigue la curvatura que los rodea, en lugar de dejarlos planos sobre las caras existentes.

### Detalle {#all-detail}
La resolución usada para el remallado. Si DynTopo está en modo "Constante", será el mismo valor que el regulador Detalle de la parte superior de este menú. El cuentagotas toma el detalle de la densidad de la malla en el punto que toques.

### Remallar {#dyn-remesh}
Ejecuta un remallado global con el algoritmo de DynTopo. Normalmente conviene usar el [Remallado por vóxeles](#voxel-remesher) para remallar por completo.

Sin embargo, tiene una ventaja frente a los vóxeles: la malla no necesita estar cerrada y las zonas enmascaradas quedan protegidas, así que controlas mejor dónde poner más o menos densidad.



## ![](/icons/topo_extra.webp) Varios {#misc}

![](/images/topology_misc_menu.webp)

Esta pestaña reúne herramientas para limpiar o convertir la malla: cerrar sus agujeros, forzarla a ser manifold o convertirla en un triplanar.

### ![](/icons/hole.webp) Agujeros {#holes}
![](/images/topology_holes_menu.webp)
La mayoría de las veces, el objeto será estanco, es decir, la malla estará "cerrada".

Si el objeto tiene agujeros, puedes rellenarlos.

![](/videos/hole_filling.mp4)

::: tip
Cuando usas el remallado por vóxeles, todos los agujeros se cierran automáticamente, tanto si lo aplicas a 1 malla como a varias.
:::

#### Cerrar agujeros {#close-holes}
Ejecuta el cierre de agujeros.

#### Opciones {#holes-gear-menu}
Estas opciones cambian la forma de rellenar los agujeros:

##### Grupo de caras {#fill-face-group}
Elige el grupo de caras de las caras nuevas:

* `Mixto` - Un agujero rodeado por un solo grupo de caras lo reutiliza; un agujero que toca varios grupos recibe uno nuevo.
* `Nuevo` - Los agujeros rellenados reciben un grupo de caras nuevo.
* `Reutilizar` - Cada agujero toma el grupo de caras que más lo rodea.

##### Detalle {#fill-detail}
La densidad de polígonos usada para rellenar el agujero. Mientras arrastras este regulador se muestra un tablero de ajedrez sobre el modelo, que te da una idea del tamaño de triángulo que se usará. La casilla lo desactiva y usa solo los puntos existentes, lo que suele crear triángulos largos y finos sobre el agujero, difíciles de esculpir.

##### Puente {#fill-non-manifold}
Rellena un agujero y las islas que contiene como una sola superficie, en lugar de rellenar cada borde por separado. Un ángulo más alto permite unir agujeros más curvados. La casilla lo desactiva.

### ![](/icons/cog.webp) Forzar Manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Intenta limpiar las aristas no manifold. Puede ser útil para programas externos que no admiten aristas compartidas por más de 2 caras.

#### Limpiar {#clean}
Ejecuta la limpieza.

#### Opciones {#force-manifold-gear-menu}
Esta opción cambia la forma de limpiar la malla:

##### Eliminar caras pequeñas {#delete-small-faces}
Un umbral para eliminar y unir polígonos pequeños. Actívalo con su casilla.


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
![](/images/topology_triplanar_menu.webp)
Convierte la malla en una primitiva [triplanar](scene.md#triplanar).
Lo más probable es que pierdas mucho detalle en el proceso: también se pierden las capas, la pintura y la multiresolución.

#### Forzar cúbica {#force-cubic}
Hace que el triplanar sea un cubo. Si no, el triplanar se ajusta a la caja envolvente más próxima a tu objeto.

#### Convertir {#convert}
Ejecuta la conversión a triplanar.

#### Resolución {#triplanar-resolution}
La resolución de la cuadrícula del triplanar: los valores más altos conservan más detalle.

## ![](/icons/decimate.webp) Diezmar {#decimation}

![](/images/topology_decimation.webp)

Reduce el número de polígonos intentando conservar el máximo detalle posible, usando triángulos.

Esta función puede ser útil si quieres exportar para impresión 3d.
Sin embargo, probablemente no deberías usarla si quieres seguir esculpiendo el objeto, ya que puede generar triángulos irregulares.

Ten en cuenta que las zonas enmascaradas no se diezman.

![](/videos/decimate.mp4)

::: tip

Usar la [herramienta Quad Remesher](tools.md#quad-remesher) en objetos con muchos polígonos puede tardar mucho en calcularse y dar resultados difíciles de controlar. Preparar antes la malla con [grupos de caras](tools.md#facegroup) y diezmarla hará que Quad Remesher funcione mucho más rápido y te dará mucho más control sobre la topología.

* Crea grupos de caras en la malla para definir el flujo de cuadrángulos ideal.
* Relaja los grupos de caras para obtener bordes de grupo suaves.
* Diezma. Así te aseguras de no tener caras finas o deformadas en los bordes de los grupos. En `Conservar bordes`, comprueba que `Grupo de caras` está activado. Así, las aristas de los triángulos seguirán con precisión los bordes de tus grupos de caras.
* En las opciones de Quad Remesher, comprueba que la relajación está desactivada (ya has relajado la malla) y deberías obtener buenos resultados.

:::

### Diezmar {#decimate}
Inicia el diezmado.

Los iconos junto al botón Diezmar muestran las opciones de abajo y te permiten activarlas o desactivarlas. El porcentaje indica la intensidad de cada opción.

* ![](/icons/palette.webp)  `Conservar pintura` - Coloca más triángulos donde hay detalle de pintura.
* ![](/icons/triforce.webp) `Caras uniformes` - Da preferencia a triángulos de tamaño regular.
* ![](/icons/hole.webp)  `Agujero` - El diezmado intenta no modificar los bordes cercanos a geometría abierta y agujeros.
* ![](/icons/group.webp) `Grupo de caras` - El diezmado intenta no modificar los bordes de los grupos de caras.
* ![](/icons/uv.webp) `UV` - El diezmado intenta no modificar los bordes UV.

### Triángulos objetivo {#target-triangles}
Fija el número de triángulos objetivo. El valor por defecto es 50 %; el botón de porcentaje/objetivo alterna entre un porcentaje y un número exacto de polígonos.

### Opciones {#decimate-gear-menu}
Cada opción tiene una casilla para activarla y un valor para su intensidad:

#### ![](/icons/palette.webp) Conservar pintura {#preserve-painting}
El valor determina la precisión con que se conserva el detalle de la pintura. Los valores más altos conservan más pintura. Ponlo a 0 si la pintura no te importa.

#### ![](/icons/triforce.webp) Caras uniformes {#uniform-faces}
Los valores más altos generan triángulos de tamaño parecido.

#### Conservar bordes {#preserve-borders}
Evita que se diezmen los bordes. Puedes ajustar el peso de los bordes de tipo `Agujero`, `Grupo de caras` o `UV` (`UV` requiere un objeto con UVs).

## ![](/icons/quad.webp) Remallado de cuadrángulos {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Reconstruye el objeto con una distribución limpia de cuadrángulos. Esta pestaña tiene varios remalladores, cada uno con su propio botón `Remallar`, su regulador `Cuadrángulos objetivo` y su menú del engranaje. Pruébalos con tu objeto: ¡dan resultados bastante distintos!

### Quad Remesher {#quad-remesher}
El mismo remallador que la herramienta [Quad Remesher](tools.md#quad-remesher), desarrollado por [Exoside](https://exoside.com/). Solo está disponible en algunas plataformas y requiere una compra: hasta entonces, el botón `Remallar` muestra un carrito.

`Seleccionar herramienta` cambia a la herramienta Quad Remesher, para dibujar guías y pintar la densidad. El menú del engranaje incluye `Cantidad adaptativa de quads`, `Tamaño adaptativo` (al 100 % el tamaño de los cuadrángulos sigue la curvatura, al 0 % son uniformes), `Detectar bordes duros` y `Reproyectar vértice`.

::: tip
Donde está disponible, Quad Remesher suele dar los mejores resultados y el mayor control.
:::

### AutoRemesher {#autoremesher}
Un remallador de cuadrángulos alternativo, con opciones para adaptar el tamaño y la forma de los cuadrángulos a la superficie.

#### ![](/icons/cog.webp) Menú del engranaje de AutoRemesher {#autoremesher-gear-menu}
El menú del engranaje tiene estas opciones avanzadas:

##### Escala de aristas {#edge-scaling}
Escala el tamaño de los cuadrángulos: los valores más altos producen cuadrángulos más grandes.

##### Adaptabilidad {#adaptivity}
Adapta la densidad de cuadrángulos a la curvatura. Con 0 se obtienen cuadrángulos uniformes; con 1, cuadrángulos más pequeños en las zonas curvas.

##### Anisotropía {#anisotropy}
Estira los cuadrángulos en la dirección más plana de la superficie. Con 0 se obtienen cuadrángulos cuadrados; con 1, cuadrángulos alargados en tubos y crestas.

##### Arista definida {#sharp-edge}
Las aristas dobladas más allá de este ángulo se conservan como rasgos marcados.

##### Suavizar normales {#smooth-normal}
Con 0, la superficie se mantiene facetada durante el remallado. Los valores más altos suavizan la superficie teniendo en cuenta las normales de los vértices.

##### Relleno máximo de agujeros {#autoremesher-max-fill-hole}
A veces el algoritmo produce agujeros no deseados. Si un agujero tiene menos vértices que este valor, se rellena.

### Instant Mesh {#quad-remesh-instant}
Remalla con el [algoritmo Instant Meshes de Wenzel Jakob, Marco Tarini, Daniele Panozzo y Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Analiza el flujo de la malla y crea una topología limpia de cuadrángulos.

#### Remallar {#instant-remesh}
Inicia el remallado.

#### Cuadrángulos objetivo {#target-quads}
El número de cuadrángulos que el remallador intentará crear.

#### ![](/icons/cog.webp) Menú del engranaje de Instant Mesh {#quad-remesh-instant-gear-menu}
El menú del engranaje tiene estas opciones avanzadas:

##### Ángulo de pliegue {#crease-angle}
Un umbral de esquinas marcadas que ayuda a guiar el remallado. Actívalo con su casilla.

##### Relleno máximo de agujeros {#max-fill-hole}
A veces el algoritmo produce agujeros no deseados. Si un agujero tiene menos vértices que este valor, se rellena.

### QuadriFlow {#quadriflow}
Remalla con el algoritmo QuadriFlow, otra forma de obtener una distribución limpia de cuadrángulos.

#### ![](/icons/cog.webp) Menú del engranaje de QuadriFlow {#quadriflow-gear-menu}
El menú del engranaje tiene estas opciones avanzadas:

##### Conservar bordes {#quadriflow-preserve-boundary}
Protege los bordes de los agujeros.

##### Conservar aristas definidas {#keep-sharp}
Alinea los cuadrángulos con las aristas vivas de la superficie.

##### Flujo de coste mínimo {#min-cost-flow}
Usa un solucionador de flujo de coste mínimo para la distribución de cuadrángulos. Es más lento, pero puede dar una topología más regular.

## ![](/icons/uv.webp) Desplegado UV {#uv-unwrap}
Calcula las coordenadas de textura (UVs) del objeto seleccionado. Nomad tiene dos métodos, `UVAtlas` y `BFF`, cada uno con su propio botón `Desplegar`.

![](/videos/unwrap.mp4)

::: tip ¿UVs?
Una analogía habitual para las UVs es envolver un regalo: ¿cuál es la mejor forma de cortar el papel para cubrir por completo un objeto, sin solapamientos?

Las UVs son parecidas, pero en vez de cortar el papel, cortas el objeto. Imagina que tu modelo estuviera hecho de plástico fino: ¿cómo lo cortarías para desplegarlo en plano, pintarlo así y luego volver a montarlo?

Ahora imagina que la superficie del modelo es de licra elástica. Podrías estirarla hasta dejarla plana, cortarla o combinar ambas cosas. Pero si pintaras un tablero de ajedrez sobre el objeto aplanado, el tablero se vería deformado al volver a montarlo. ¿Qué método es mejor: más cortes con menos deformación, o menos cortes con más deformación?

Las UVs son instrucciones que le dicen al software 3d cómo "cortar y estirar" el objeto al aplicar texturas. La herramienta UVAtlas suele seguir el enfoque de "más cortes, menos deformación".


:::

::: tip Las UVs, Nomad y otras aplicaciones

La mayoría de los modelos texturizados que encontrarás en internet usan UVs. Nomad puede importarlas y mostrarlas desde el panel [Material](material.md#textures).

Con los modelos creados en Nomad, puedes pintar directamente sobre los objetos sin UVs. Si necesitas exportarlos a otras aplicaciones, como [Procreate](https://procreate.art/), puedes "hornear" la información de color de Nomad en texturas mediante UVs.

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
UVAtlas suele preferir crear más islas con cortes, para minimizar la deformación.

#### Desplegar {#unwrap}
Calcula las UVs del objeto seleccionado.

#### Opciones {#uvatlas-gear-menu}
Los botones junto a `Desplegar`:

##### Grupo de caras {#atlas-face-group}
Cuando muestra `Sí`, los grupos de caras definen los cortes de las UVs. Este ajuste se comparte con BFF.

##### Eliminar UVs {#delete-uvs}
El botón de la papelera elimina las UVs del objeto.

##### Inspeccionar {#uv-inspect}
Muestra las UVs del objeto en el fondo.

#### Estiramiento máximo {#max-stretch}
Los valores bajos crean menos deformación y más islas; los altos, más deformación y menos islas.

#### Espaciado entre islas {#island-spacing}
El margen entre las islas. Los valores bajos desperdician menos espacio, pero corres el riesgo de que las texturas se filtren de una isla a otra.

::: warning
Calcular las UVs puede llevar un tiempo; lo mejor es tener una malla de menos de 100k vértices.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

Las UVs de BFF siguen el enfoque de "menos cortes, más deformación".

#### Opciones {#uv-bff-gear-menu}
Junto a `Desplegar` están los mismos botones `Grupo de caras`, eliminar e `Inspeccionar` que en [UVAtlas](#uvatlas-gear-menu).

##### Grupo de caras {#bff-face-group}

Usa los grupos de caras para definir los cortes de las UVs.

#### Recuento de conos {#cone-count}
Define el número de proyecciones principales. Los valores bajos producen menos islas, pero más deformación. Los valores altos tardan más en calcularse.

#### Parches sin costuras {#seamless-patches}
Afecta a la distribución de los parches UV y puede introducir bastante deformación. Funciona mejor con grupos de caras creados con cuidado.

::: warning
BFF puede crear UVs superpuestas si la malla tiene asas (como el agujero de un dónut).
:::

### ![](/icons/preview.webp) Mostrar UVs tras desplegar {#show-uv-after-unwrap}
Abre la vista del inspector de UVs después de desplegar, para que compruebes el resultado al momento.

### ![](/icons/bake.webp) Hornear: Textura → Textura {#unwrap-bake-texture}
Solo está disponible cuando el material del objeto tiene texturas. Al volver a desplegarlo, las texturas se transfieren a las nuevas UVs para que sigan encajando. Su resolución es `Auto` por defecto, igual a la de la textura más grande, aunque puedes fijarla tú.

## ![](/icons/bake.webp) Hornear {#bake}
Esta pestaña transfiere detalles y pintura entre objetos, y entre vértices y texturas.

`Desde alta resolución` usa otros objetos como origen; el número entre paréntesis indica cuántos. Nomad los elige así:

- se usan todos los objetos seleccionados, y el objeto seleccionado principal es el destino (el más resaltado en el menú [Escena](scene.md))
- si solo hay un objeto seleccionado, Nomad usa en su lugar todos los objetos visibles
- si todos los demás objetos están ocultos (por ejemplo, con Individual), se usa toda la escena

### ![](/icons/bake.webp) Hornear → Textura {#bake-texture}
![](/images/topology_bake_menu.webp)

El horneado de texturas crea texturas proyectando los demás objetos visibles de la escena en las UVs del objeto seleccionado. El objeto necesita UVs.

Este es el flujo de trabajo típico para hornear:
- Tienes una malla con detalles finos y pintura
- Clónala
- Diézmala (pon `Conservar pintura` a 0)
- Despliega sus UVs
- ¡Hornéala!

Ahora deberías tener una malla de baja resolución que conserva la mayor parte de la pintura y los detalles del objeto original.

Tras la operación, los colores de vértice se mueven a una nueva capa desactivada, para que no interfieran con las texturas.

#### Desde sí mismo {#tex-from-itself}
Hornea el objeto en sus propias UVs: su pintura se convierte en texturas y, si tiene niveles de multiresolución, los detalles del nivel más alto se hornean en el nivel actual (en ese caso aparece un icono de multiresolución en el botón). Es fácil de preparar, pero a menudo necesitarás más control, y entonces la siguiente opción es más útil.

#### Desde alta resolución {#tex-from-high-res}
Hornea los demás objetos en el objeto seleccionado. El número entre paréntesis indica cuántos objetos se usarán como fuentes de alta resolución, que se hornearán en el objeto actual de baja resolución con UVs. Los demás objetos no necesitan tener una distribución ni una topología parecidas a las del objeto que se hornea, lo que permite flujos de horneado muy versátiles.

#### Resolución {#tex-bake-resolution}
La resolución de la textura horneada. Las texturas horneadas siempre son cuadradas, así que 1024 creará una imagen de 1024x1024.

Los botones de abajo son atajos para las resoluciones más usadas. Como referencia, 512x512 es bastante pequeña, por ejemplo para gráficos web y geometría sencilla. 4096x4096 (4k, para abreviar) es para renders de alta calidad.

#### Color, Rugosidad, Metalicidad, Normal, Desplazamiento, Emisivo, Opacidad {#tex-normal-roughness-metalness-color-emissive-opacity}
Estos botones determinan qué propiedades se hornean, cada una en un mapa distinto. Al terminar el horneado, se añaden como texturas al material del objeto actual. `Desplazamiento` hornea la altura de los detalles como mapa de desplazamiento.

#### ![](/icons/cog.webp) Menú del engranaje de Hornear {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
El menú del engranaje tiene estas opciones avanzadas:

##### Respaldo {#tex-backup}
Para previsualizar las texturas horneadas, hay que desactivar la pintura del objeto. `Respaldo (Pintura → Capa)` transfiere toda la pintura a una capa nueva como copia de seguridad, para poder activarla o desactivarla fácilmente.

##### Usar multirresolución {#tex-use-multires}
Para `Desde sí mismo` en un objeto con niveles de multiresolución. Nomad lee la alta resolución a través de los niveles de subdivisión en lugar de lanzar rayos: es más rápido y no tiene errores de proyección. Desactívalo para hornear con las opciones de abajo.

##### Base suave {#tex-smooth-base}
Para `Desplazamiento` en un objeto con niveles de multiresolución. Mide el desplazamiento desde la base subdividida en lugar de desde sus caras planas. Déjalo activado cuando el mapa de desplazamiento vaya a usarse sobre una malla subdividida, como con la subdivisión adaptativa de Blender.

##### Distancia de búsqueda {#tex-cage-radius}
La distancia máxima usada para encontrar la superficie de origen. Por defecto es pequeña para evitar artefactos, pero puedes aumentarla si los objetos de origen están lejos del objeto que se hornea.

##### Proyección {#tex-projection}
Cómo se encuentra la superficie de origen:

* `Rayo` - Proyecta siguiendo la normal de la superficie.
* `Rayo + más próximo` - Usa el rayo de la normal y, si no alcanza nada, la superficie más próxima.
* `Más próximo` - Proyecta sobre el punto más cercano de la superficie de origen.

##### Desfase del rayo {#tex-ray-offset}
Ajusta desde dónde parten los cálculos de horneado sobre el objeto que se hornea. Un pequeño desfase respecto a la superficie evita la mayoría de los artefactos habituales. Si los objetos de origen están muy lejos del objeto que se hornea, quizá tengas que aumentarlo. `Más próximo` no lo usa.


### ![](/icons/bake.webp) Reproyectar → Vértice {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Proyecta los detalles esculpidos, la pintura, las capas y las texturas en valores de vértice.

Puedes verlo como lo contrario del horneado: si el horneado transfiere las propiedades de los vértices a texturas, la reproyección transfiere las texturas (y otras propiedades)
 de vuelta a los vértices.

::: tip
Al usar `Hornear → Textura` o `Reproyectar → Vértice`, se tienen en cuenta tanto los colores de vértice como las texturas del material.
:::

#### Desde sí mismo {#vertex-from-itself}
Convierte las texturas del material en valores de vértice. Este botón solo está activo si el objeto tiene UVs y las texturas están activas en el material.

::: tip CONSEJO: Pintar texturas
Nomad no permite pintar ni editar texturas directamente, pero puedes conseguir resultados muy parecidos proyectando las texturas en valores de vértice, pintando sobre los vértices y horneando después los vértices en texturas:

1. Prepara un objeto con pocos polígonos y con UVs
1. Carga texturas en su material
1. Subdivídelo lo suficiente para poder pintar
1. `Reproyectar → Vértice` en modo `Desde sí mismo`: la textura se ha convertido en valores de vértice
1. Pinta, suaviza, difumina, estampa, haz todos los retoques que necesites
1. `Hornear → Textura`, en modo `Desde sí mismo`. Esos retoques se convierten de nuevo en texturas.
:::

#### Desde alta resolución {#vertex-from-high-res}
Convierte los demás objetos en valores de vértice sobre el objeto seleccionado. El número de este botón indica cuántos objetos de origen hay. Está pensado sobre todo para usarse también sobre una malla de alta resolución, normalmente con una topología limpia.

::: tip
Reproyectar otros objetos no solo sirve para transferir información de color, sino también para proyectar vértices sobre otros objetos; por ejemplo, puedes proyectar vendas sobre un personaje.
:::

#### Vértices, Color, Rugosidad, Metalicidad, Opacidad, Máscara, Capas, Grupo de caras {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Estos botones determinan qué propiedades se proyectan sobre el objeto seleccionado. `Capas` transfiere las demás capas a la malla seleccionada.

#### ![](/icons/cog.webp) Menú del engranaje de Reproyectar {#vertex-reproject-gear-menu}
El menú del engranaje tiene estas opciones avanzadas:

##### Opacidad → Máscara {#vertex-opacity-to-mask}
Convierte la opacidad del origen en máscara sobre el objeto seleccionado.

##### Iteraciones {#vertex-iterations}
Cuántas veces se aplica la relajación durante la reproyección. Solo se usa cuando `Vértices` está activado.

##### Relajar {#vertex-relax}
La distribución de la malla seleccionada se puede suavizar o relajar en cierta medida para ajustarse mejor a los objetos de origen. `Suavizar` es mejor para mallas con muchos polígonos, `Relajar` para mallas con pocos. `Automático` deja que Nomad elija el mejor método.

##### Distancia de búsqueda {#vertex-cage-radius}
La distancia máxima usada para encontrar la superficie de origen. Por defecto es pequeña para evitar artefactos, pero puedes aumentarla si los objetos de origen están lejos del objeto seleccionado.

##### Proyección {#vertex-projection}
Cómo se encuentra la superficie de origen:

* `Rayo` - Proyecta siguiendo la normal de la superficie.
* `Mezcla adaptativa` - Mezcla el rayo de la normal y la superficie más próxima según la distancia y la `Preferencia de rayo`. Si uno de los dos no alcanza nada, usa el otro.
* `Más próximo` - Proyecta sobre el punto más cercano de la superficie de origen.

##### Preferencia de rayo {#vertex-ray-bias}
Solo para `Mezcla adaptativa`. Los valores más altos inclinan la mezcla hacia el resultado del rayo de la normal; los más bajos, hacia el punto más próximo.

##### Desfase del rayo {#ray-vertex-offset}
Ajusta desde dónde parten los cálculos sobre el objeto seleccionado. Un pequeño desfase respecto a la superficie evita ciertos artefactos. Si los objetos de origen están muy lejos del objeto que se hornea, quizá tengas que aumentarlo. `Más próximo` no lo usa.

### ![](/icons/bake.webp) Hornear → VDM {#bake-vdm}
Crea un sello VDM (desplazamiento vectorial) a partir del objeto seleccionado y lo añade a la biblioteca de VDM. Se te pedirá un nombre.

Este es el flujo de trabajo típico:
- Añade un plano, o elige `VDM nuevo` en el selector de VDM para añadir uno ya configurado (la primitiva [VDM](scene.md#add-menu))
- Esculpe tu forma sobre él, manteniendo el borde plano
- ¡Hornéalo!

Las UVs del plano definen el cuadrado que se hornea, así que el objeto necesita UVs. Elige el tamaño del sello con `Resolución`, y decide con `Color`, `Rugosidad`, `Metalicidad` y `Opacidad` qué incluye el sello además del desplazamiento.

::: tip
Evita usar DynTopo sobre el plano: degrada sus UVs y el sello sale deformado. Esculpir en una capa da el resultado más preciso, ya que el plano sigue estando debajo. Pintar también requiere una capa; si no, el material se estampa sobre todo el cuadrado en lugar de solo donde pintaste.
:::

## ![](/icons/dot.webp) Primitivo {#primitive}
Parámetros de la primitiva seleccionada. La mayoría también están disponibles en el botón `…` de la barra de herramientas de la primitiva en la vista.

![](/images/topology_primitive_screenshot.webp)
