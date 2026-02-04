# ![](/icons/multires.webp) Topología {#topology}

Este menú controla la topología de los objetos en Nomad, así como las herramientas para hornear y transferir detalles entre objetos y entre texturas.

![](/images/topology_overview.webp)

Nomad está basado en polígonos, utiliza triángulos y quads para manejar la geometría.
Por topología nos referimos tanto al número de caras como a la forma en que los puntos (vértices) están conectados.

Es importante hacer un seguimiento de la topología, especialmente si quieres esculpir o pintar detalles finos.

::: tip How to keep track of your topology?
You can display the [Wireframe](settings.md#wireframe) or simply disable [Smooth Shading](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

El menú de topología de Nomad tiene varias secciones:

| Method                                | Icon                         | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Edit multiple levels of detail using subdivision                 |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | Recompute a new topology with uniform density                    |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | Add/Remove faces locally in real-time when sculpting or painting |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | Decimation, UVs, baking, remeshing, reprojection                 |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | Primitive options                                                |


## Estadísticas de polígonos {#polygon-stats}

![](/images/topology_stats.webp)

La sección superior del menú de topología muestra información de polígonos para el objeto seleccionado y para toda la escena. Los números muestran el número total de vértices, el número total de triángulos y el número total de quads (polígonos de 4 lados).

Al tocar esta sección aparecerá una lista de estadísticas de polígonos para todos los objetos poligonales de la escena.

## ![](/icons/multires.webp) Multirresolución {#multiresolution}

![](/images/topology_multires_menu.webp)

### ¿Qué es la multirresolución? {#what-is-multiresolution}
The multiresolution feature is useful for two main scenarios:
- The smooth subdivision algorithm to increase the polycount of your object
- Handle multiple level of resolution so that you can alternate between small and large scale edits

![](/videos/multiresolution.mp4)

#### Flujo de trabajo de multirresolución {#multiresolution-workflow}
One important aspect of the multiresolution is that you can go back to a lower resolution, make changes on your object and then go back to the highest resolution without losing the high resolution details. All the high resolution details will be projected automatically.

::: warning
If you are using a tool that alters the topology of your object, you will lose all the other resolutions of your object!
You should always get a warning in case it should happen, for example when you are using:
- the [Voxel Remesher](#voxel-remesher)
- the [Dynamic Topology](#dynamic-topology)
- the [Trim tool](tools.md#trim)
- the [Split tool](tools.md#split)
:::


### Deslizador de multirresolución {#multiresolution-slider}
Este deslizador indica el número de niveles de subdivisión en el objeto actual. Si hay 6 barras verticales, hay 6 niveles de subdivisión. El círculo indica el nivel de subdivisión que se muestra actualmente. 

### Invertir {#reverse}
Cuando estás en el nivel de subdivisión más bajo, el botón Reverse intentará crear un nivel por debajo del actual. Ten en cuenta que esto generalmente solo puede ocurrir si el objeto se creó con subdivisión desde el principio, por ejemplo en Nomad o en otras aplicaciones 3D que usan superficies de subdivisión multirresolución.

### Subdividir {#subdivide}
El botón *Subdivide* aumentará el número de polígonos por 4, ¡así que asegúrate de vigilar el recuento de polígonos ya que puede aumentar muy rápido!
Un aspecto importante de *Subdivision Surface* es que convergen hacia una *Smooth Surface*.
Para entender cómo funciona, puedes probar el botón *Subdivide* en un objeto con solo unos pocos polígonos.

Puedes desactivar este comportamiento *Smooth* marcando la opción `Linear subdivision`.

### Eliminar nivel inferior {#delete-lower}
Si hay subdivisiones por debajo del nivel mostrado actualmente, las elimina. Si haces esto por accidente, puedes recrearlas con el botón Reverse.

### Eliminar nivel superior {#delete-higher}
Si hay subdivisiones por encima del nivel mostrado actualmente, las elimina.

### Subdivisión lineal {#linear-subdivision}
Subdivide la malla sin aplicar suavizado.

### Borde duro {#sharp-border}
Si tu objeto tiene facegroups, al activar esta opción se mantendrán afilados los bordes de los facegroups. Esto se puede configurar en cada nivel de subdivisión (el deslizador de subdivisión tendrá un pequeño icono encima del nivel para indicarlo).

### Mantener triángulos {#keep-triangles}
La mayoría de los sistemas estándar de superficies de subdivisión intentarán convertir todos los polígonos en quads durante una operación de subdivisión. Este conmutador forzará a la subdivisión a usar triángulos en su lugar.

### Bloquear (LV0) {#lock-lv0}

Evita que el nivel de subdivisión más bajo sea modificado. Esto puede ser importante si tu objeto fue generado en otra aplicación y el objeto base debe permanecer sin cambios. Cuando esta opción está desactivada, los cambios grandes realizados en niveles de subdivisión superiores moverán el nivel 0.

::: tip 

Subdivision will smooth all sharp edges by default. To keep edges slightly sharp, experiment with using linear subdivision or Sharp border on the first 2 subdivide levels, then turn it off for the higher levels. This will create a semi-sharp subdivided mesh.

:::


## ![](/icons/voxel.webp) Remallado por vóxeles {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Al usar el `Voxel Remesher`, toda la malla forzará a que la topología tenga una resolución uniforme, lo que significa que todos los polígonos tienen más o menos el mismo tamaño. Esto es muy útil cuando no quieres pensar en la topología y simplemente hacer esculpido libre.

Un flujo de trabajo típico de esculpido puede comenzar usando el `Voxel Remesher` para bloquear una forma aproximada con baja resolución.
Simplemente pulsa el botón *Remesh* de vez en cuando cuando estés estirando demasiado la malla para evitar demasiada distorsión.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
As stated above, Nomad is a polygonal software, but the `Voxel Remesher` is one exception where another approach is used (temporarily) to perform the remeshing.

One big difference is that the voxel approach won't accept self intersection, so these will be resolved.
Also it doesn't support meshes with holes in them.

By holes, we don't mean the `genus hole` (`hole` of a donus), but instead mesh that are not `watertight`/`closed`.
Typically, what it means is that before applying the remeshing, every holes will be filled, similarly to the [Trim tool](tools.md#trim) or [Hole filling feature](scene.md#hole-filling).
:::

### Remallar {#voxel-remesh}
Ejecuta el remallado voxel.

### Resolución {#voxel-resolution}
El tamaño de los vóxeles usados durante el cálculo. Mientras cambias este parámetro se superpondrá un patrón de tablero de ajedrez sobre la malla para dar una vista previa del resultado.

### Construir multirresolución {#build-multiresolution}
Crea niveles de multirresolución inferiores para el remallado voxel. Si usas el patrón de tablero para establecer una resolución y configuras build multiresolution en 2, el resultado final tendrá detalle que coincida con el deslizador de resolución, y si vas a la pestaña multires estará en el nivel 2, lo que significa que tienes mallas multires de menor resolución en el nivel 1 y nivel 0. Esta puede ser una buena forma de generar tanto una malla limpia con polígonos uniformes como una malla de control de menor resolución.

::: tip Tip: Build multiresolution and stable smoothing

This option can sometimes cause 'loops' in the geometry that can be difficult to smooth, causing little pimples. If this happens, enable 'Stable smoothing' in the smooth tool options. 

:::

### Mantener bordes duros {#keep-sharp-edges}
Activa el ajuste de los nuevos puntos a los bordes afilados de la malla original. Puede introducir distorsión.

## ![](/icons/dynamic.webp) Topología dinámica {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
La multirresolución y el remallado voxel son métodos habituales en la industria para controlar la topología, pero ambos requieren que vigiles que no estés estirando demasiado los polígonos o comprimiéndolos demasiado.

Dynamic Topology es un método alternativo. Mientras esculpes, Nomad añadirá y eliminará polígonos de forma adaptativa durante la pincelada, de modo que al tallar pequeños detalles se añadirán muchos polígonos pequeños donde los necesites, y al suavizar en otras zonas se eliminarán polígonos.

Ten en cuenta que Dynamic Topology usará polígonos triangulares en lugar de quads. Esto puede verse un poco desordenado, pero casi es mejor no mirar el wireframe, solo concentrarte en hacer una escultura con buen aspecto sin preocuparte por la topología, y luego usar una de las otras herramientas de remallado de Nomad para generar una malla limpia de quads.

Mira el vídeo de abajo en acción.

![](/videos/dynamic.mp4)

### Activado {#enabled}
Activa Dynamic Topology. Se colocará un icono DynTopo debajo de los deslizadores de radio e intensidad del pincel para permitirte activar o desactivar Dyntopo por herramienta.

### Detalle {#dyn-detail}
Controla la cantidad de detalle; su comportamiento cambia según la selección de 'Detail based on...', ver más abajo.

### Detalle basado en... {#detail-based-on}
| Method   | Description                                                     |
| :------: | :-------------------------------------------------------------: |
| Screen   | The level of detail will depend how big the object is on screen. The detail slider is 100% or higher for fine detail, making small triangles, or 1% for low detail, making big triangles.  |
| Radius   | The tool radius defines the amount of detail. Use a small tool radius, for fine detail, a big tool radius for low detail. The detail slider is a multiplier on this ratio.                     |
| Constant | The detail slider defines the amount of detail, and isn't affected by screen size or tool size.             |

::: tip TIP: Radius mode

To get a better sense of how radius mode works, start moving the detail slider with one finger, then at the same time change the tool radius with another finger. You will see how they are linked.

:::

### Preferir... {#prefer}
| Method  | Description       |
| :-----: | :---------------: |
| Speed   | Favor performance |
| Quality | Favor quality     |

Cuando favoreces `Quality`, las 2 diferencias principales son:
- el refinamiento se aplica antes de esculpir, por lo que obtendrás menos artefactos de interpolación al pintar o esculpir detalles muy pequeños
- el refinamiento se ejecuta hasta que converge al nivel de detalle correcto, en contraste con un comportamiento incremental.
 
De este modo, si esculpes detalles muy pequeños o haces trazos rápidos, la topología siempre se refinará como se espera.


### Usar presión en el radio {#use-pressure-on-radius}
Solo es relevante si `Radius` está activado. Cuando está activado, el nivel de detalle siempre reflejará el tamaño del pincel, incluso cuando el tamaño del pincel esté afectado por la presión del lápiz.

### Usar caída del trazo {#use-stroke-falloff}

También incluye la curva de caída del pincel y el alfa en los cálculos de dyntopo.

### Método {#method}
Tanto si estás usando `Dynamic Topology` en tu [Brush](#brush) como [Globalmente](#global), puedes elegir en qué modo opera:

| Method         | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | It can add and remove faces, this is the mode used in the video above |
| Subdivision    | Add new faces only, it cannot remove faces                            |
| Decimation     | Remove faces only, it cannot add new faces                            |

### Proteger zona enmascarada {#protect-masked-area}
Activa que las áreas enmascaradas protejan la topología de ser modificada.

### Extrapolación de vértices {#vertex-extrapolation}


### Detalle {#all-detail}
La resolución usada para la operación de remallado. Si Dyntopo está en modo 'Constant', será el mismo valor que el deslizador Detail en la parte superior de este menú.

### Remallar {#dyn-remesh}
Ejecuta un remallado global usando el algoritmo de dyntopo. Normalmente deberías usar el [Voxel Remesher](#voxel-remesher) para remallados completos.

Sin embargo, una ventaja sobre los vóxeles es que el área enmascarada estará protegida, por lo que puedes tener un mejor control sobre dónde poner más o menos densidad.



## ![](/icons/topo_extra.webp) Varios {#misc}

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) Menú de engranaje {#gear-menu}
Muchas de las herramientas de este menú tienen opciones adicionales. Se puede acceder a ellas mediante el icono de engranaje junto al título de la sección.

### Diezmado {#decimation}

![](/images/topology_decimation.webp)

Reduce el número de polígonos intentando mantener la mayor cantidad posible de detalles, usando polígonos triangulares.

Esta función puede ser útil si quieres exportar para impresión 3D.
Sin embargo, probablemente no deberías usarla si quieres seguir esculpiendo sobre el modelo, ya que puede producir triángulos irregulares.

Ten en cuenta que las áreas enmascaradas no se decimarán.

![](/videos/decimate.mp4)

::: tip

Using the [Quadremesh tool](tools.md#quad-remesher) on high poly objects can take a long time to calculate, and give results that are hard to control. Pre-processing the mesh with [facegroups](tools.md#facegroup-1) and decimate will make Quadremesh run much faster, and allow much more control over topology.

* Facegroup the mesh to define your ideal quad flow.
* Facegroup relax to get smooth facegroup borders.
* Decimate. This will ensure you have no thin or distorted faces on the facegroup edge. In the decimate settings ensure facegroup is enabled. This will make triangle edges follow your facegroup edges precisely.
* In the Quadremesh options ensure relax is disabled (as you have already relaxed the mesh) and you should get good results.

:::

#### Diezmar {#decimate}
Inicia la operación de decimación.

Los iconos junto al botón decimate te permiten activar o desactivar opciones que afectan a la decimación. El porcentaje indica cuán fuerte es esa opción y se puede configurar en el menú avanzado del engranaje.

* ![](/icons/palette.webp)  `Preserve Painting` - Coloca más triángulos donde haya detalle de pintura.
* ![](/icons/triforce.webp) `Uniform Faces` - Prefiere crear triángulos de tamaño uniforme.
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - Decimate intentará mantener sin cambios los bordes cerca de geometría abierta y agujeros.
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - Decimate intentará mantener sin cambios los bordes de los facegroups.
* ![](/icons/uv.webp) `Preserve UV Borders` - Decimate intentará mantener sin cambios los bordes de las UV.

#### ![](/icons/cog.webp) Menú de engranaje de Diezmado {#decimate-gear-menu}
El menú de engranaje tiene estas opciones avanzadas:
##### Conservar pintura {#preserve-painting}
La casilla activará o desactivará este modo; el valor determinará cuán fielmente se preservará el detalle de pintura. Valores más altos preservarán más pintura. Ponlo a 0 si no te importa la pintura.


##### Caras uniformes {#uniform-faces}
La casilla activará o desactivará este modo. Valores más altos producirán triángulos de tamaño similar.

##### Conservar bordes {#preserve-borders}
Actívalo para evitar que se decimen los bordes. Se pueden seleccionar pesos de borde para bordes de `Geometry`, `Face Group` o `UV`.

#### Triángulos objetivo {#target-triangles}
Establece el recuento objetivo de triángulos. El valor por defecto es 50%; el botón percent/target alternará entre un porcentaje o un recuento exacto de polígonos objetivo.



### Desplegado UV - UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
Calcula coordenadas de textura (UVs) para la malla actual, generalmente prefiriendo crear más islas con cortes para minimizar la distorsión.

El pequeño icono de ojo entre el título del menú y el menú de engranaje alternará la previsualización de las UV en el objeto.

![](/videos/unwrap.mp4)

#### Desplegar {#unwrap}
Calcula las UVs para el objeto seleccionado, que se mostrarán en el fondo.

#### Borrar UVs {#delete-uvs}
Elimina las UVs del objeto.

#### ![](/icons/cog.webp) Menú de engranaje de UVAtlas {#uvatlas-gear-menu}
El menú de engranaje tiene estas opciones avanzadas:

#### Grupo de caras {#atlas-face-group}

Usa facegroups para definir los cortes de las UV.

##### Estiramiento máximo {#max-stretch}
Valores bajos crean menos distorsión y más islas; valores altos crean más distorsión y menos islas. 

##### Espaciado de islas {#island-spacing}
La cantidad de espacio entre las islas. Valores bajos desperdiciarán menos espacio, pero arriesgarán que las texturas se mezclen entre islas. 

::: warning
Calcular UVs puede llevar algo de tiempo; es mejor tener una malla con menos de 100k vértices.
:::

::: tip UVs?
A common analogy for UV's is wrapping a gift; what is the best way to cut wrapping paper to completely cover an object, with no overlaps? 

Uv's are similar, but instead of cutting the paper, you cut the object. Imagine if your model was made of thin plastic, how would you cut your model apart to unwrap it to lie flat, paint on it in that flat state, then reassemble it?

Now imagine the surface of your model is made of stretchy lycra. You could stretch the model flat, or cut it, or a combination of both. But if you painted a checkerboard on the object when flattened, the checkerboard would be distorted when you reassemble it. Which is a better method, more cuts with less distortion, or less cuts with more distortion?

Uv's are instructions to tell 3d software how to 'cut and stretch' the object when applying textures. The UV Atlas tool generally uses a 'more cuts, less distortion' approach.


:::

::: tip UV's and Nomad and other apps

Most textured models you find online will be textured with UVs. Nomad can import and display this via the [material](material#textures) panel.

When models are made in Nomad, you can paint directly onto objects without UVs. If you need to export them to other apps, eg [Procreate](https://procreate.art/), you can 'bake' Nomad color information into textures via UVs. 

:::

### Desplegado UV - BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

Las UV BFF favorecen un enfoque de 'menos cortes, más distorsión'. 

#### ![](/icons/cog.webp) Menú de engranaje de UV BFF {#uv-bff-gear-menu}

#### Grupo de caras {#bff-face-group}

Usa facegroups para definir los cortes de las UV.

##### Recuento de conos {#cone-count}
Define el número de proyecciones principales usadas. Valores más bajos producirán menos islas, pero más distorsión.

##### Parches sin costuras {#seamless-patches}
Afecta al diseño de los parches de UV; funciona mejor con facegroups creados cuidadosamente.

### Bake -> textura {#bake-texture}
![](/images/topology_bake_menu.webp)

El horneado de texturas creará texturas proyectando otros objetos visibles de la escena en las UV del objeto seleccionado.

Este es el flujo de trabajo típico para hornear:
- Tienes una malla con detalles finos y pintura
- La clonas
- La decimas (pon `Preserve painting` a 0)
- Le haces UV unwrap
- ¡La horneas!

Nomad, por defecto, tendrá en cuenta todas las mallas visibles de la escena.
También puedes usar el modo Solo para ocultar rápidamente la mayoría de las otras mallas.
Si no hay otros objetos visibles, entonces tendrá en cuenta toda la escena.

Ahora deberías tener una malla de baja resolución que conserva la mayor parte de la pintura y los detalles de tu objeto anterior.

Después de la operación, los colores de vértice se moverán a una nueva capa desactivada, para que no interfieran con las texturas.

#### Desde sí mismo {#tex-from-itself}
Hornea el nivel de multirresolución más alto al nivel más bajo en el objeto actual. Esto es sencillo de configurar, pero a menudo necesitarás más control, en cuyo caso la siguiente opción es más útil.

#### Desde alta resolución () {#tex-from-high-res}
Hornea desde los otros objetos visibles de la escena al objeto seleccionado. El número entre paréntesis indica el número de otros objetos visibles que se usarán como objetivos de alta resolución y se hornearán en el objeto actual de baja resolución con UV. Los otros objetos no necesitan ser similares en disposición o topología al objeto que se está horneando, lo que permite flujos de trabajo de horneado versátiles.

#### Resolución {#tex-bake-resolution}
La resolución de la textura horneada. Las texturas horneadas siempre son cuadradas, por lo que 1024 creará una imagen de 1024x1024. 

Los botones de abajo son accesos directos para resoluciones de uso común. Como referencia, 512x512 es relativamente pequeña, por ejemplo para gráficos web y geometría simple. 4096x4096 (4k en corto) es para renders de alta calidad.

#### ![](/icons/cog.webp) Menú de engranaje de Bake {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
El menú de engranaje tiene estas opciones avanzadas:

##### Normal, Rugosidad, Metalicidad, Color, Emisión, Opacidad {#tex-normal-roughness-metalness-color-emissive-opacity}
Estas casillas determinarán qué propiedades se hornearán, cada una en mapas separados. Una vez completado el horneado, se añadirán como texturas al material del objeto actual.

##### Copia de seguridad {#tex-backup}
Para previsualizar las texturas horneadas, la información de pintura del objeto debe estar desactivada. Esta opción transferirá cualquier información de pintura a una nueva capa como copia de seguridad para que pueda activarse o desactivarse fácilmente.

#### Radio de la jaula {#tex-cage-radius}
Ajusta qué tan lejos del objeto de horneado se envían los rayos para buscar objetos objetivo. Por defecto, esta distancia se mantiene baja para evitar artefactos, pero se puede aumentar si los objetos objetivo están lejos del objeto de horneado.

##### Desplazamiento de rayo {#tex-ray-offset}
Ajusta desde dónde comienzan los cálculos de horneado en el objeto de horneado. Por defecto comienzan al 5% fuera de la superficie, lo que evita la mayoría de los artefactos comunes. Si los objetos objetivo están muy lejos del objeto de horneado, este desplazamiento podría necesitar aumentarse.


### Reproyectar a vértices {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Proyecta detalles esculpidos, pintura, capas y texturas en valores de vértice.

Se puede considerar como el inverso del horneado; si el horneado transfiere propiedades de vértice a texturas, la reproyección transfiere texturas (y otras propiedades)
 de vuelta a los vértices.

::: tip
When using `Bake to texture` or `Reproject to vertex`, both the vertex colors and material textures will be taken into account.
:::

#### Desde sí mismo {#vertex-from-itself}
Convierte texturas del material en valores de vértice. Este botón solo estará activo si el objeto tiene UV y hay texturas activas en el material.

::: tip TIP: Texture painting
Nomad doesn't directly support painting and editing textures, but very similar results can be achieved by projecting textures -> vertex values, painting on vertices, then bake vertex -> textures:

1. Setup a low poly object with UV's
1. Load textures into it's material
1. Subdivide it enough to paint on
1. `Reproject to vertex` in `From itself` mode, now the texture has been converted to vertex values
1. Paint, smooth, smudge, stamp, do whatever edits you need
1. `Bake to texture`, in `From itself` mode. Those edits are converted back into textures.
:::

#### Desde alta resolución () {#vertex-from-high-res}
Convierte cualquier objeto visible en valores de vértice sobre el objeto seleccionado. El número de este botón indica el número de objetos visibles.

::: tip
Reprojecting other objects can be used not just for transferring color information from other objects, but to project vertices onto other objects, eg bandages can be projected onto a character.
:::

#### ![](/icons/cog.webp) Menú de engranaje de Reproyección {#vertex-reproject-gear-menu}
El menú de engranaje tiene estas opciones avanzadas:

#### Vértices, Rugosidad, Metalicidad, Color, Opacidad, Opacidad->Máscara, Máscara, Capas, Grupo de caras {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Estas casillas determinan qué propiedades se proyectarán sobre el objeto seleccionado. 

#### Relajar {#vertex-relax}
La malla seleccionada puede tener su disposición suavizada o relajada cierta cantidad para ajustarse mejor a los objetivos de reproyección. Smooth es mejor para mallas de alta resolución. Relax es mejor para mallas de baja resolución. Auto permitirá que Nomad determine el mejor método.

#### Iteraciones {#vertex-iterations}
Cuántas veces debe aplicarse la operación de relajación durante la reproyección.

#### Radio de la jaula {#vertex-cage-radius}
Ajusta qué tan lejos del objeto seleccionado se envían los rayos para buscar objetos objetivo. Por defecto, esta distancia se mantiene baja para evitar artefactos, pero se puede aumentar si los objetos objetivo están lejos del objeto de horneado.

#### Sesgo del rayo {#vertex-ray-bias}
Valores bajos favorecerán la proyección al punto más cercano en la superficie objetivo. Valores altos favorecerán un punto de intersección usando la normal de la superficie. 

#### Desplazamiento de rayo {#ray-vertex-offset}
Ajusta desde dónde comienzan los cálculos de horneado en el objeto seleccionado. Por defecto comienzan al 5% fuera de la superficie, lo que evita ciertos artefactos. Si los objetos objetivo están muy lejos del objeto de horneado, este desplazamiento podría necesitar aumentarse.


### Remallado Quad - Instant {#quad-remesh-instant}
![](/images/topology_quadremesh_menu.webp)
Remalla usando el [algoritmo Instant Meshes de Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Analizará el flujo de una malla y creará una topología limpia de quads.

::: tip
On iOS and desktop, the [Quad remesher](tools#quad-remesher) tool gives better results and more control.
:::

#### Remallar {#instant-remesh}
Inicia la operación de Instant Meshes.

#### Quads objetivo {#target-quads}
El número de polígonos quad que Quad Remesh intentará crear.

#### ![](/icons/cog.webp) Menú de engranaje de Remallado Quad Instant {#quad-remesh-instant-gear-menu}
El menú de engranaje tiene estas opciones avanzadas:

##### Ángulo de pliegue {#crease-angle}
Un umbral de esquinas afiladas que intentará ayudar a guiar la operación de remallado.

#### Relleno máximo de agujeros {#max-fill-hole}
El algoritmo a veces puede producir agujeros no deseados. Si un agujero tiene menos vértices que este valor, entonces se rellenará.

### Agujeros {#holes}
![](/images/topology_holes_menu.webp)
La mayoría de las veces, tu objeto probablemente será hermético, lo que significa que la malla está 'cerrada'.

Si tu objeto tiene agujeros, puedes rellenarlos. Ten en cuenta que solo funciona en agujeros 'ingenuos'; por tanto, no puede 'soldar' dos bordes separados.

![](/videos/hole_filling.mp4)

::: tip
When you run the Voxel remesher, all the holes are automatically closed, whether you are using it on 1 or multiple meshes.
:::

#### Cerrar agujeros {#close-holes}
Ejecuta la acción de cierre de agujeros.

#### ![](/icons/cog.webp) Menú de engranaje de Agujeros {#holes-gear-menu}
El menú de engranaje tiene estas opciones avanzadas:

##### Detalle {#fill-detail}
La densidad de polígonos usada para rellenar el agujero. Mientras arrastras este deslizador se mostrará un patrón de tablero de ajedrez en el modelo, lo que dará una indicación del tamaño de triángulo a usar. La casilla desactivará esto y solo usará los puntos existentes, lo que normalmente creará triángulos largos y delgados sobre el agujero, que pueden ser difíciles de esculpir.

##### Rellenar no-manifold {#fill-non-manifold}
Intenta rellenar agujeros no manifold.

##### Grupo de caras {#fill-face-group}

Al rellenar agujeros, ¿debería cada agujero obtener su propio facegroup (Auto), deberían compartir todos un facegroup (Off), o no crear facegroups (On)?

### Forzar Manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Intenta limpiar aristas no manifold. Puede ser útil para software externo que no soporta aristas que tienen más de 2 caras en común.

#### Limpiar {#clean}
Ejecuta la acción de limpieza.
#### ![](/icons/cog.webp) Menú de engranaje de Forzar manifold {#force-manifold-gear-menu}
El menú de engranaje tiene estas opciones avanzadas:

#### Eliminar caras pequeñas {#delete-small-faces}
Un umbral usado para eliminar y unir polígonos pequeños.


### Triplanar {#triplanar}
![](/images/topology_triplanar_menu.webp)
Convierte la malla en una primitiva [triplanar](scene.md#triplanar).
Probablemente perderás muchos detalles en el proceso.

#### Forzar cúbico {#force-cubic}
Hace que el triplanar sea un cubo. De lo contrario, el triplanar se ajustará a la caja envolvente más cercana alrededor de tu objeto.

#### Convertir {#convert}
Ejecuta la acción triplanar.

#### Resolución {#triplanar-resolution}
El tamaño de vóxel usado en la operación triplanar.

## ![](/icons/dot.webp) Primitiva {#primitive}
Parámetros para la primitiva seleccionada. Estos también están disponibles en la barra de herramientas de la vista de primitivas.

![](/images/topology_primitive_screenshot.webp)