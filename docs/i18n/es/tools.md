# ![](/icons/toolbox.webp) Herramientas

![](/images/tools_menu.webp)

::: tip
Salta a [Herramientas](#tools-1) para ver las descripciones de cada herramienta.
:::

## Visión general

Las herramientas se seleccionan desde la `Caja de herramientas` a la derecha y se controlan con los `Controles de herramienta` a la izquierda. Los ajustes adicionales se encuentran en el menú `Settings`, el primer icono en el menú superior derecho.

Las herramientas de pincel tienen controles para tamaño e intensidad. Las herramientas de selección tienen controles para varios estilos de selección. La parte inferior de los controles de herramienta tiene accesos directos para operaciones usadas con frecuencia (Smooth, Mask, Hide, Gizmo, Color, Alpha).

Las herramientas de Nomad están codificadas por color en la caja de herramientas:

* <span class=brush>**Herramientas de pincel**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**Herramientas de mover**</span> (Move, Drag)
* <span class=mask>**Herramientas de máscara**</span> (Mask, SelMask)
* <span class=paint>**Herramientas de pintura**</span> (Paint, Smudge)
* <span class=flatten>**Herramientas de aplanar**</span> (Flatten, Planar)
* <span class=pinch>**Herramientas de pinchar**</span> (Crease, Pinch)
* <span class=selection>**Herramientas basadas en selección**</span> donde primero se dibuja una máscara 2D y luego se realiza una operación (Trim, Split, Project)
* <span class=creation>**Herramientas de creación**</span> (Tube, Lathe, Insert)
* <span class=transform>**Herramientas de transformación**</span> (Transform, Gizmo)
* <span class=misc>**Herramientas varias**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**Herramienta de vista**</span>



Muchas de estas herramientas se pueden personalizar con diferentes comportamientos de pincel, presión, texturas, etc. mediante el menú [Stroke](stroke.md). 


### Controles del pincel

La barra de herramientas izquierda tiene deslizadores para radio e intensidad, y luego controles específicos de la categoría de herramienta, explicados a continuación.

![](/images/tool_left_panel.webp)

::: tip
El deslizador de intensidad para muchas herramientas puede ir por encima del 100 %, ¡vale la pena experimentar!
:::

### Sub mode
El botón directamente debajo del deslizador de intensidad es el botón `Sub`. Su etiqueta y función cambiarán con cada herramienta, y cuando se pulse invocará un comportamiento alternativo, normalmente opuesto. Por ejemplo, para [Paint](#paint) invocará un modo de borrado, para [Crease](#crease) creará bordes elevados en lugar de hendiduras, etc.

Por defecto funciona como un botón adhesivo; es decir, puedes mantenerlo pulsado para invocarlo temporalmente, y cuando lo sueltes se desactivará. Si lo tocas, el modo sub se activará de forma permanente.

### Atajos
En la parte inferior de la barra de herramientas izquierda hay accesos directos para [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Por defecto todos funcionan como botones adhesivos; es decir, puedes mantenerlos pulsados para invocarlos temporalmente, y cuando los sueltes se desactivarán. Si los tocas, ese modo de acceso directo se activará de forma permanente.

### Controles de selección

Las herramientas [Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup) y [Hide](#hide) usan controles similares para seleccionar áreas de la malla.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - Una forma dibujada a mano alzada
* `Polygon` - Una forma cerrada definida por una combinación de curvas y/o líneas rectas. Consulta [Edición de formas](#shape-editing) más abajo para más información.
* `Curve` - (solo Project) - Una curva a mano alzada para la proyección
* `Path` - (solo Project) - Una curva definida por puntos. Consulta [Edición de formas](#shape-editing) más abajo para más información.
* `Line` - Arrastra una línea para definir un segmento planar. Por defecto operará sobre la malla inmediatamente; desactiva la validación automática si no quieres esto (pulsación larga o deslizamiento sobre el icono de línea)
* `Rect` -  Arrastra una línea diagonal, esto definirá las esquinas de una forma rectangular. Pulsación larga o deslizamiento para mostrar opciones de validación automática, forzar forma cuadrada y que el primer clic sea el centro del rectángulo.
* `Ellipse` - Arrastra una línea diagonal, esto definirá el tamaño de una elipse. Pulsación larga o deslizamiento para mostrar opciones de validación automática, forzar forma circular y que el primer clic sea el centro de la elipse.
* `Flip` - invierte la máscara de la forma, o la dirección de la herramienta Project.

La mayoría de las herramientas tienen una opción de validación automática, lo que significa que la operación se realizará tan pronto como termines de dibujar la forma. Cuando la validación automática está desactivada, se dibujará un botón verde junto a la forma que ejecutará la operación. Esto te permite editar la forma, ajustar la vista y, cuando estés listo para usar la forma, pulsar el botón verde.

### Shape editing
La edición de polígonos y la edición de curvas se comportan de forma similar:

* Para empezar, arrastra una línea para definir 2 puntos, luego arrastra desde el centro de la línea para definir un polígono o curva.
* Haz clic en los puntos para alternar entre suave y afilado. 
* Haz clic y arrastra en las secciones de curva o línea para crear nuevos puntos.
* Para borrar un punto, arrastra un punto hacia su vecino hasta que se ponga rojo.
* El icono de papelera en la esquina del icono de polígono o path borrará la forma.

### Menú Settings

Muchas herramientas tienen ajustes extra que se encuentran en el menú Settings, el primer icono en el menú superior derecho:

![](/images/tools_settings_menu.webp)

## Tools

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Clay
La herramienta Clay es útil para construir tu escultura. `Sub` eliminará material de tu escultura.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Brush
El pincel estándar. `Sub` eliminará material.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Move
El área bajo el pincel se pegará al pincel, permitiendo una deformación elástica. La selección se mantiene durante el movimiento, así que si alejas el pincel y luego lo devuelves al punto de inicio, no verás deformación.

El modo sub es `Normal`, y moverá el área bajo el pincel a lo largo de la normal de la superficie.

Este pincel es bueno tanto para deformaciones a gran escala como para deformaciones pequeñas y cuidadosas.

#### Move Settings

* `Radius (Background)` - Qué tan lejos del borde de un modelo puedes estar y seguir esculpiendo, útil cuando se trabaja en la silueta de un objeto. 
* `Same-side vertex only` - Ignora vértices que apuntan en la dirección opuesta a la deformación.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Drag
El área bajo el pincel se pegará al pincel, permitiendo una deformación elástica. A diferencia del pincel Move, la selección se actualiza continuamente durante la pincelada, por lo que es posible hacer objetos largos y serpentiformes, especialmente cuando la Topología Dinámica está activada.

El modo sub es `Normal`, y moverá el área bajo el pincel a lo largo de la normal de la superficie.

Este pincel es bueno para cambios de forma más sueltos y gestuales.

#### Drag Settings

* `Radius (Background)` - Qué tan lejos del borde de un modelo puedes estar y seguir esculpiendo, útil cuando se trabaja en la silueta de un objeto. 
* `Same-side vertex only` - Ignora vértices que apuntan en la dirección opuesta a la deformación.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Smooth
Suaviza el área promediando las posiciones de los puntos. Esta herramienta depende mucho de la densidad de polígonos.
Así que si tienes muchos polígonos, el suavizado será menos efectivo.

El modo sub es `Relax`, que solo suaviza la malla (wireframe) pero intenta conservar los detalles geométricos.

#### Smooth settings

![](/images/tool_smooth_settings.webp)

##### Facegroup

* `Relax` - Suavizará los bordes de los facegroups. Usa intensidad mayor al 100 % para suavizar rápidamente los bordes. `Auto` solo suavizará si la previsualización de facegroup está activada, `Off` desactivará, `On` activará. 

##### Vertex
* `Sticky vertex on border` - Para mallas con bordes abiertos, por ejemplo un plano, es posible suavizar las esquinas. Activar esta opción bloqueará los bordes abiertos.
* `Relax` - lo mismo que el modo alternativo relax en la barra de herramientas izquierda.
* `Stable smoothing` - Intenta hacer que el suavizado sea independiente de la topología. Funciona mejor con densidad de topología variable y con un valor de intensidad de suavizado alto.

##### Painting
* `Screen Smoothing` - Usa esta opción para obtener un suavizado independiente de la topología, incluso con recuentos de polígonos altos.
* `Screen samples` - La calidad del suavizado; valores más altos serán más suaves, pero más lentos.

::: tip
Densidades de polígonos más altas pueden requerir subir la intensidad por encima del 100 %. Valores muy altos (300 %, 500 %) también pueden funcionar bien como herramienta de esculpido, forzando áreas a volverse planas y suaves rápidamente bajo el pincel, ¡como golpear arcilla con un mazo!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Mask
Esta herramienta te permite enmascarar vértices. Los vértices enmascarados están protegidos del esculpido o la pintura. 

El modo sub es `Unmask`, y borrará donde se haya pintado la máscara.

Similar a las selecciones en programas de pintura 2D, las máscaras se pueden pintar con un pincel o crear con selecciones de forma, difuminar o endurecer.

A diferencia de los programas de pintura 2D, también se pueden crear mediante facegroups, y las máscaras se pueden usar para crear nueva geometría mediante operaciones de extrusión/extracción. 

![](/videos/tool_mask1.mp4)

 Aparecerá una barra de herramientas en la parte superior del visor con controles adicionales. 

![](/images/tool_mask_toolbar.webp)

El título de la barra se puede tocar para expandir/contraer, o se puede tocar la flecha en la parte superior derecha para moverla a la parte superior o inferior de la interfaz.

| Acción                                            | Descripción                                                                               |
| :------------------------------------------------ | :---------------------------------------------------------------------------------------- |
| ![](/icons/cross_circle2.webp) Clear             | Limpia la máscara                                                                         |
| ![](/icons/invert.webp)        Invert            | Invierte la máscara                                                                       |
| ![](/icons/sharpen.webp)       Sharpen           | Endurece el borde de la máscara                                                           |
| ![](/icons/blur.webp)          Blur              | Difumina el borde de la máscara                                                           |
|                                 Blur ->           | Arrastra a izquierda/derecha para difuminar la máscara de forma interactiva               |
| ![](/icons/culling.webp)       Front             | Alterna para enmascarar solo vértices frontales                                           |
|                                 Convert           | Convierte la máscara en un facegroup                                                      |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | Cuando está activado se mostrarán los facegroups; al tocar uno se enmascarará             |
|                                 On tap (mask)     | Cuando está activado, tocar una 'isla' de polígonos enmascarados o no enmascarados la rellenará por inundación. |
| ![](/icons/vertex.webp)        Connected         | Cuando está activado solo permite que los trazos de máscara afecten topología conectada.  |

##### Mask Quick gesture
Puedes realizar gestos al estilo ZBrush mientras mantienes pulsado el botón de máscara rápida en la barra izquierda:
| Acción | Gesto (mantener atajo inferior izquierdo) |
| :----: | :----------------------------------------: |
| Invert | Tocar en el fondo                         |
| Clear  | Arrastrar en el fondo                     |
| Blur   | Tocar en área enmascarada                 |
| Sharpen| Tocar en área sin máscara                 |


#### Mask settings
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - El menú de ajustes de Mask se usa principalmente para crear geometría a partir de la máscara. Por ello, el comportamiento por defecto es previsualizar cómo se verá la nueva geometría. Puedes elegir no tener previsualización, una previsualización de extracción, una de división y si esta geometría se mostrará en modo rayos X.

##### Thickness
* `Height` - La altura de la forma extraída. El icono de Más/Menos te permite alternar entre una extrusión hacia afuera, hacia adentro o centrada. 
* `Height/Height+Mask` - Alterna entre que la altura sea constante o que las partes difuminadas de la máscara afecten a la altura, permitiendo formas suaves y de altura variable. 

##### Smoothness
Cuando está activo, suavizará el borde de la forma extraída; funciona mejor con recuentos de polígonos altos. 
* `Iterations` - La cantidad de suavizado aplicado. Valores altos producirán bordes curvos muy suaves, pero empezarán a desviarse de la forma de la máscara.
* `All/Sharp border/Borders only` - El suavizado puede funcionar en todas direcciones, suavizando tanto los lados como la parte superior de la forma extraída; o suavizar la parte superior y los lados pero mantener un borde afilado; o solo suavizar el borde, dejando la superficie superior sin cambios.

##### Edge loop (side)
* `Auto Edge-loop (side)` - Calculará la cantidad de divisiones en los lados de la forma extraída para crear polígonos cuadrados que coincidan con los polígonos del área enmascarada. Cuando está desactivado, puedes establecer tú mismo el número de edge loops con el deslizador correspondiente.

----

##### Extract
* `Extract` - Crea la geometría extraída.
* `Closing action` - Cómo debe comportarse Extract. 'None' duplicará los polígonos enmascarados en una nueva forma. 'Fill' hará lo mismo e intentará tapar la superficie posterior. 'Shell' extruirá según la cantidad establecida en 'thickness' y es el valor por defecto.

::: tip

Si la previsualización está en modo 'Extract' con 'X-ray' activado, pulsar el botón Extract puede resultar confuso al principio. Como el menú está activo, intentará previsualizar una extracción en tu nueva forma y poner en rayos X la superficie original. Sin embargo, como no tienes máscara en la nueva superficie, no puede previsualizar la extracción y Nomad te avisará con 'Nothing to Extract!'. 

Esto es normal; cierra el menú de ajustes de máscara para ver la nueva forma y la original, y vuelve a seleccionar la superficie original si necesitas limpiar la máscara o dibujar nuevas máscaras.
:::

##### Split
* `Split` - Extraerá tanto las regiones enmascaradas COMO las no enmascaradas en nuevas formas. 
* `Closing action (masked)` - Cómo debe comportarse la extracción de la parte enmascarada. 'None' duplicará los polígonos enmascarados en una nueva forma. 'Fill' hará lo mismo e intentará tapar la superficie posterior. 'Shell' extruirá según la cantidad establecida en 'thickness' y es el valor por defecto.
* `Closing action (unmasked)` - Cómo debe comportarse la extracción de la parte no enmascarada. 'None' duplicará los polígonos enmascarados en una nueva forma. 'Fill' hará lo mismo e intentará tapar la superficie posterior. 'Shell' extruirá según la cantidad establecida en 'thickness' y es el valor por defecto.
* `Sync border` - Garantiza que el borde entre las formas extraídas enmascaradas y no enmascaradas permanezca cercano. Cuando está desactivado, como la operación de shell extruirá cada cara a lo largo de su normal, puede formarse un hueco entre las formas.

##### Carve
* `Carve` - En modo por defecto, se comporta como si hubieras recortado la superficie según la cantidad de 'thickness', como cortar una sección de piel de naranja. 



### ![](/icons/tool_maskSelector.webp) Selection Mask
Esta herramienta es en su mayoría similar a la [herramienta Mask](#mask); la diferencia principal es que no usas trazos para pintar la máscara, sino los [Controles de selección](#selection-controls).

El modo sub es `Unmask`, y borrará la máscara usando los controles de selección.

Selection Mask comparte los mismos ajustes de herramienta que la herramienta `Mask`.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Paint
Aplica color y propiedades de material. Para aprender más sobre materiales puedes visitar la sección [Painting](painting.md).

El modo sub es `Erase` y eliminará la pintura.

#### Paint settings
* `Layer fitering` - Funciona como el bloqueo de alfa de capa en Photoshop o Procreate. Si estás pintando en una capa, cuando esto está activado solo puedes modificar donde ya existe pintura; las áreas sin pintar estarán protegidas.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Smudge
Emborróna color y propiedades de material. El menú de ajustes de Smudge contiene un deslizador `Quality`; valores más bajos significan trazos más rápidos.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Flatten
Aplana el área proyectando los puntos sobre el plano promedio.

El modo sub es `Fill` y definirá un plano establecido por el punto más alto, tendiendo a tirar de los puntos hacia arriba.

#### Flatten settings

* `Lock plane direction` - Usa la dirección del plano calculada en el primer clic. Por defecto está desactivado.
* `Lock plane origin`- Usa el primer clic como centro del plano. Por defecto está desactivado.

Cuando uno o ambos están desactivados, Flatten puede profundizarse gradualmente o alterar el ángulo del plano usando trazos largos que se mueven sobre diferentes profundidades y curvaturas. Esto, junto con las opciones de muestreo de área del menú Brush, puede ofrecer un control muy preciso.

::: tip
Cuando trabajes en áreas de alta curvatura, por ejemplo intentando aplanar las mejillas pero la herramienta sigue afectando los lados de la nariz, intenta crear una máscara para proteger las áreas que el pincel Flatten no debería afectar.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar
Hace que los puntos sean planares proyectándolos sobre el plano promedio, pero con menos acumulación que el pincel Flatten. Esto crea superficies limpias de borde duro. Trazos rápidos empujarán y tirarán más de la superficie; trazos más lentos que comienzan desde áreas ya planares y se expanden mantendrán mejor el plano.

El modo sub es `Fill` y definirá un plano establecido por el punto más alto, tendiendo a tirar de los puntos hacia arriba.

Planar es en realidad la misma herramienta que `Flatten`, pero con `Lock plane direction` activado, lo que significa que tenderá a crear superficies más estables y de borde duro, mientras que Flatten puede ser más escultórica y usarse para crear áreas semi-planas.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Crease
Las herramientas Crease pueden ser útiles para esculpir pequeños cortes o hendiduras.

El modo sub es `Invert`, y creará una hendidura elevada.

#### Crease Settings

* `Pinch factor` - Cuánto tirar de los vértices lateralmente hacia el pincel. Si Pinch está en 1 y Offset en 0, la superficie no tendrá cambios de profundidad, solo cambios de topología, tirando los bordes hacia el trazo.
* `Offset factor` - Cuánto empujar/tirar de los vértices en profundidad. Si Pinch está en 0 y Offset en 1, se crearán hendiduras profundas o abultamientos elevados, pero se verán dentados porque no se tira de suficiente geometría hacia la hendidura para definir con precisión los lados o el fondo.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Pinch
Esta herramienta se puede usar para afilar bordes.

El modo sub es `Invert` y separará los vértices.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Trim
La herramienta Trim funciona eliminando un trozo de tu malla y ofrece opciones sobre cómo procesar el hueco que queda. Usa los [Controles de selección](#selection-controls) para definir el recorte.

::: tip
Como esta herramienta proyecta desde la cámara, recibirás una advertencia si la cámara está en modo perspectiva.

En modo ortográfico, el corte realizado a través de la malla es paralelo a la vista, que es lo que la mayoría de la gente espera. Cuando se hace con una cámara en perspectiva, el corte se verá diferente en el lado lejano del objeto frente al lado cercano.
:::

#### Trim settings

* `Stroke painting` - Si la pintura está activada en el menú Paint, la región parcheada se rellenará con el color seleccionado actualmente.
* `Boolean` - rellena el agujero del recorte usando una región de polígonos quad. La región rellenada será plana.
* `Legacy` - rellena el agujero del recorte con una región triangulada. La región rellenada será plana.
* `Fill` - rellena el agujero con una región triangulada. La región rellenada será una superficie curva, como la película de una burbuja de jabón.
* `None` - no rellena el agujero.
* `Boolean Detail Shape` - El tamaño aproximado de los quads y triángulos usados en el lado de la forma del recorte.
* `Boolean Detail Hole` - El tamaño aproximado de los triángulos o polígonos usados en el agujero rellenado del recorte. 
* `Legacy Detail` - El tamaño aproximado de los triángulos usados en el recorte.
* `Legacy Hole smoothing` - Cuánto se relajan los triángulos en el área rellenada.
* `Legacy Threshold espilon` - Un valor que se puede ajustar para mejorar el algoritmo de relleno de agujeros legacy.
* `Fill Detail` - El tamaño aproximado de los triángulos usados en el recorte.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Split
Similar a la herramienta [Trim](#trim), excepto que mientras Trim descarta la selección, Split conservará la selección como un nuevo objeto.

#### Split settings

* `Stroke painting` - Si la pintura está activada en el menú Paint, la región parcheada se rellenará con el color seleccionado actualmente.
* `Boolean` - rellena el agujero del Split usando una región de polígonos quad. Las regiones rellenadas serán planas.
* `Legacy` - rellena el agujero del Split con una región triangulada. Las regiones rellenadas serán planas.
* `Fill` - rellena los agujeros con una región triangulada. Las regiones rellenadas serán superficies curvas, como la película de una burbuja de jabón.
* `None` - no rellena los agujeros.
* `Boolean Detail Shape` - El tamaño aproximado de los quads y triángulos usados en el lado de la forma del Split.
* `Boolean Detail Hole` - El tamaño aproximado de los triángulos o polígonos usados en el agujero rellenado del Split. 
* `Legacy Detail` - El tamaño aproximado de los triángulos usados en el Split.
* `Legacy Hole smoothing` - Cuánto se relajan los triángulos en el área rellenada.
* `Legacy Threshold espilon` - Un valor que se puede ajustar para mejorar el algoritmo de relleno de agujeros legacy.
* `Fill Detail` - El tamaño aproximado de los triángulos usados en el Split.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Project
La herramienta Project se parece a la herramienta [Trim](#trim), pero no borra ni crea geometría, solo mueve vértices para ajustarlos a la selección.

![](/videos/tool_project.mp4)

::: tip
Si usas Project mientras estás en una capa, puedes mezclar entre la forma original y la proyectada con el deslizador de la capa.
:::

### ![](/icons/tool_layer.webp) Layer
Eleva la superficie, pero limita la altura.

Si mantienes el lápiz apoyado y sigues pasando el pincel sobre un área, Layer elevará hasta cierta altura y no irá más allá, a diferencia de otras herramientas que seguirán acumulando altura.

Ten en cuenta que por defecto el límite solo se establece por trazo. Si comienzas un nuevo trazo, se construirá desde la nueva altura de la superficie.

Para establecer una altura máxima constante a lo largo de muchos trazos, usa la herramienta Layer con el sistema de [Layers](layers.md) de Nomad.

Crea una capa y usa esta herramienta. La altura máxima ahora se establece desde la capa, por lo que puedes aplicar muchos trazos de pincel y la altura siempre será la misma.

`Sub` usará una profundidad mínima, creando surcos.

#### Layer Settings

* `Use layer data` - Cuando está activo y hay una capa seleccionada, usa los datos de la capa para establecer la altura máxima.
* `Inflate`- Cuando está activo ajusta la dirección en la que trabaja Layer para obtener resultados más suaves.
* `Relax (Normal)` - La cantidad de suavizado aplicada a las normales.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Inflate
Mueve los vértices a lo largo de sus propias normales. `Sub` moverá los vértices a lo largo de su normal invertida.

#### Inflate Setings
* `Relax (Normal)` - La cantidad de suavizado aplicada a las normales.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Nudge
Mueve o 'emborróna' puntos en la dirección del trazo.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stamp

Haz clic y arrastra para elevar un área de la escultura con la forma del Alpha seleccionado.

Esto es simplemente la herramienta [Brush](#brush) con el tipo de trazo configurado en `Lock + radius`. 

`Sub` empujará el sello hacia dentro en lugar de sacarlo de la superficie.

::: tip
Stamp suele funcionar mejor con geometría de alta resolución. Si buscas en línea 'wrinkles alpha', 'pores alpha', 'scales alpha', etc., estas texturas alpha y Stamp pueden ser una gran forma de añadir detalle orgánico a una escultura de personaje.

Los dos modos de trazo son útiles para cosas diferentes. 

* `Lock + radius` tiene una *altura* fija; al arrastrar se ajusta el ancho y la rotación del sello. Bueno para texturas de piel donde necesitan tener la misma profundidad/altura, pero diferentes rotaciones y escalas para ocultar patrones repetidos.
* `Lock + intensity` tiene un *ancho* fijo; al arrastrar se ajusta la rotación y la altura del sello. Bueno para remaches, donde todos deben tener el mismo tamaño, pero diferentes rotaciones y alturas. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Delete Layer
Esta herramienta puede reiniciar capas localmente; necesitas una capa activa, de lo contrario no pasará nada.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tube
Crea un tubo dibujando una curva. 
![](/images/tool_tube_new.webp)

Una vez creado el tubo, la trayectoria se puede editar en el espacio 3D usando controles similares a las herramientas estándar de [Edición de formas](#shape-editing) y edición de curvas. 

![](/videos/tool_tube.mp4)

#### Tube left toolbar

![](/images/tool_tube_left_toolbar.webp)

La barra de herramientas izquierda tiene las siguientes opciones:

* `Sync` - Si el tubo actual es una instancia y hay nodos hijo del tubo que difieren entre las instancias, esto los resincronizará.
* `Snap` - Cuando está activo, los modos Curve y Path se ajustarán (snap) a otros objetos mientras dibujas. Cuando está inactivo, el primer punto se ajustará y luego el resto del tubo se dibujará a esa profundidad. Tiene un pequeño submenú:
    * `Offset` - Establece la profundidad del snap; 0 % hará que el centro de la sección transversal del tubo se ajuste a la superficie, valores positivos lo elevarán de la superficie, valores negativos lo bajarán.
* `Curve` - Dibuja un tubo a mano alzada. Tiene un pequeño submenú:
    * `Auto-validate` - Creará el tubo tan pronto como el trazo se complete. Cuando está desactivado, será visible un círculo verde de validación junto a la trayectoria de la curva; presiónalo para validar o usa el enlace `Reset` que aparece en este menú para eliminar la trayectoria.
    * `Closed` - convierte el tubo en un bucle.
    * `Screen` - Disponible solo cuando Auto-validate está desactivado. Cuando está activo, la trayectoria queda 'anclada' a la pantalla, permitiéndote mover la vista y el objeto mientras la trayectoria permanece en su sitio. Cuando está inactivo, la trayectoria forma parte de la escena 3D y se moverá con la cámara y los objetos.
    * `Accuracy` - Cuántos puntos de curva se usarán para convertir la trayectoria dibujada en un tubo. 0 % usará el menor número de puntos, pero omitirá pequeños cambios de curvatura; 100 % será muy preciso y usará muchos puntos.
* `Path` - Crea un tubo haciendo clic para definir puntos de curva. Toca el círculo verde para validar la trayectoria. Tiene un pequeño submenú:
    * `B-spline` - Un método alternativo de dibujo de curvas donde los puntos de curva normalmente no se sitúan directamente sobre la curva, pero puede producir resultados más suaves que el método por defecto.
    * `Closed` - convierte el tubo en un bucle
    * `Screen` - Cuando está activo, la trayectoria queda 'anclada' a la pantalla, permitiéndote mover la vista y el objeto mientras la trayectoria permanece en su sitio. Cuando está inactivo, la trayectoria forma parte de la escena 3D y se moverá con la cámara y los objetos.

##### Tube top toolbar
![](/images/tool_tube_toolbar.webp)
Cuando un tubo está seleccionado, aparecerá una barra de herramientas en la parte superior del visor con controles adicionales. Haz clic en el título de la barra para contraer/expandir la barra y haz clic en la flecha de la parte superior derecha para mover la barra a la parte superior o inferior del visor.

* `Validate` - hornea el tubo en polígonos regulares para que pueda ser esculpido.
* `Edit` - muestra los puntos de curva para que puedan ser manipulados
* `Mirror` - añade un repetidor de espejo como padre de esta curva
* `Snap` - ajusta (snap) los puntos de curva a superficies cercanas
* `Closed` - Une el inicio y el final de la curva para formar un bucle
* `B-spline` - Alterna entre interpolación Catmull-rom y B-spline.
* `Cap` - Alterna entre tapas en ambos extremos del tubo, solo en el inicio o el final, o sin tapas.
* `Hole` - Añade grosor al tubo, convirtiéndolo en una tubería. Alterna entre tener un agujero en ambos extremos, solo en el final o sin agujeros. 
* `Radius` - Alterna entre un radio uniforme, un radio en el inicio y el final o un radio por punto de curva. Se editan con manejadores naranjas en la curva.
* `Twist` - Alterna entre sin giro, un giro uniforme, un giro en el inicio y el final o un giro por punto de curva. Se editan con manejadores rosas en la curva.
* `Profile` - Alterna entre sin perfil (por lo que un perfil circular), un perfil uniforme, un perfil en el inicio y el final o un perfil por punto.
* `Profile edit` - Muestra un editor de perfil. Funciona de forma similar a las herramientas de [Edición de formas](#shape-editing), puede guardar y cargar preajustes de perfil y tiene un conmutador para permitirte editar el perfil en el espacio 3D.
* `Spiral` - Muestra un menú para añadir un giro en espiral al tubo. Este menú tiene opciones para `Twist Angle`, `Offset`, `Scale` y `Angle offset`.
* `X Divisions` - el número de divisiones alrededor del tubo; por ejemplo, 4 divisiones harán un tubo cuadrado. 
* `Constant density` - cuando está activo, mantendrá los polígonos cuadrados; cuando está desactivado, te permitirá establecer `Y divisions` a lo largo de la longitud del tubo.
* `...` - Menú de ajustes de Tube.

#### Curve point delete toggle

![](/images/tool_tube_delete_toggle.webp)

Debajo de la barra de herramientas hay un conmutador de borrado de puntos de curva. Cuando arrastras un punto de curva cerca de otro, se pondrá rojo, indicando que si lo sueltas el punto será borrado. Si estás haciendo ediciones pequeñas y no quieres borrar puntos, este botón desactivará el comportamiento de borrado de puntos.



#### Tube settings
* `Primitive` - botones que permiten activar/desactivar UVs o validar el tubo.
* `Post subdivision` - un acceso directo para establecer el nivel de multiresolución antes de validar.
* `Linear subdivision` - acceso directo para establecer el nivel de subdivisión lineal antes de validar. 
* `Division X` - igual que X Divisions en la barra de herramientas.
* `Division Y` - igual que Y Divisions en la barra de herramientas.
* `Curve (Repeater)` - convierte el tubo en un [Curve Repeater](scene.md#curve)

::: tip
Divisions en 4 y Post subdivision en 3 harán tubos de punta redondeada suaves, buenos para gusanos, serpientes, partes del cuerpo.
:::


### ![](/icons/tool_lathe.webp) Lathe
Crea una superficie de revolución dibujando una curva.

Esta herramienta es ideal para formas como jarrones, copas de vino.

![](/videos/tool_lathe.mp4)

#### Lathe left toolbar

![](/images/tool_lathe_left_toolbar.webp)

La barra de herramientas izquierda tiene las siguientes opciones:

* `Sync` - Si el Lathe actual es una instancia y hay nodos hijo del Lathe que difieren entre las instancias, esto los resincronizará.
* `Fixed` - Cuando está activado, el centro del Lathe es fijo y se muestra en pantalla. Esta línea central tiene puntos de edición que se pueden ajustar. Cuando está desactivado, el centro del Lathe se actualizará dinámicamente para coincidir con el inicio y el final de la curva dibujada.
* `Curve` - Dibuja el perfil del Lathe en un solo trazo. Tiene un pequeño submenú:
    * `Auto-validate` - Cuando está activado, el Lathe se creará cuando el lápiz se levante de la pantalla. Cuando está desactivado, se puede pulsar un círculo verde junto a la curva para crear el Lathe. La curva se puede borrar con el botón `Reset`.
    * `Closed` - Une el inicio y el final de la curva para formar un bucle
    * `Screen` - Disponible solo cuando Auto-validate está desactivado. Cuando está activo, la trayectoria queda 'anclada' a la pantalla, permitiéndote mover la vista y el objeto mientras la trayectoria permanece en su sitio. Cuando está inactivo, la trayectoria forma parte de la escena 3D y se moverá con la cámara y los objetos.
    * `Accuracy` - Cuántos puntos de curva se usarán para convertir la trayectoria dibujada en un tubo. 0 % usará el menor número de puntos, pero omitirá pequeños cambios de curvatura; 100 % será muy preciso y usará muchos puntos.
* `Path` - Crea un Lathe haciendo clic para definir puntos de curva. Toca el círculo verde para validar la trayectoria. Tiene un pequeño submenú:
    * `B-spline` - Un método alternativo de dibujo de curvas donde los puntos de curva normalmente no se sitúan directamente sobre la curva, pero puede producir resultados más suaves que el método por defecto.
    * `Closed` - convierte el tubo en un bucle
    * `Screen` - Cuando está activo, la trayectoria queda 'anclada' a la pantalla, permitiéndote mover la vista y el objeto mientras la trayectoria permanece en su sitio. Cuando está inactivo, la trayectoria forma parte de la escena 3D y se moverá con la cámara y los objetos.

#### Lathe top toolbar
![](/images/tool_lathe_top_toolbar.webp)

Cuando un Lathe está seleccionado, aparecerá una barra de herramientas en la parte superior del visor con controles adicionales. Haz clic en el título de la barra para contraer/expandir la barra y haz clic en la flecha de la parte superior derecha para mover la barra a la parte superior o inferior del visor.

* `Validate` - hornea el Lathe en polígonos regulares para que pueda ser esculpido.
* `Edit` - muestra los puntos de curva para que puedan ser manipulados
* `Mirror` - añade un repetidor de espejo como padre de este Lathe
* `Snap` - ajusta (snap) los puntos de curva a superficies cercanas
* `Stable` - Cuando está activado, el perfil de la curva se parenta a la línea central del Lathe. Cuando está desactivado, la línea central se puede editar y no moverá la curva, permitiendo formas más complejas.
* `Focus` - Rotará la vista para ver el perfil de la curva perfectamente plano a cámara.
* `Closed` - Une el inicio y el final de la curva para formar un bucle
* `Cap` - Si Closed está desactivado, alterna entre tapas en ambos extremos del tubo, solo en el inicio o el final, o sin tapas.
* `Hole` - Añade grosor al Lathe, convirtiéndolo en una tubería. Alterna entre tener un agujero en ambos extremos, solo en el final o sin agujeros. 
* `B-spline` - Alterna entre interpolación Catmull-rom y B-spline.
* `X Divisions` - el número de divisiones alrededor del Lathe; por ejemplo, 4 divisiones harán un Lathe de perfil cuadrado. 
* `Constant density` - cuando está activo, mantendrá los polígonos cuadrados; cuando está desactivado, te permitirá establecer `Y divisions` a lo largo de la longitud del tubo.
* `...` - Menú de ajustes de Lathe.

#### Lathe settings
* `Primitive` - botones que permiten activar/desactivar UVs o validar el tubo.
* `Post subdivision` - un acceso directo para establecer el nivel de multiresolución antes de validar.
* `Linear subdivision` - acceso directo para establecer el nivel de subdivisión lineal antes de validar. 
* `Division X` - igual que X Divisions en la barra de herramientas.
* `Division Y` - igual que Y Divisions en la barra de herramientas.
* `Curve (Repeater)` - convierte el perfil de la curva en un [Curve Repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) Insert
Coloca un objeto en la superficie de otro. En uso es similar a la herramienta Stamp, pero para formas 3D completas.

Si seleccionas una primitiva desde la barra de herramientas izquierda, un clic-arrastre sobre cualquier superficie colocará una primitiva donde hagas clic; el arrastre establecerá el tamaño. Una vez que termines de arrastrar, Insert cambiará al modo [Transform](#transform).

En modo Instance, arrastrar creará y deslizará una nueva instancia sobre la superficie. El tamaño se duplicará desde la primera forma; de este modo puedes colocar muchas instancias del mismo tamaño de un objeto sobre otras superficies.

¡No tienes que insertar solo primitivas! Selecciona *cualquier* forma en el outliner; si Insert está en modo Instance o Clone, puedes arrastrar copias del objeto seleccionado sobre cualquier otra superficie.

Si un objeto tiene un pivote personalizado, se usará como punto de anclaje. Ver vídeo abajo.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transform
Mueve/rota/escala un modelo directamente con 1 y 2 dedos, normalmente sobre la superficie de otro objeto.

La herramienta se controla con la barra de herramientas izquierda y tiene 5 botones:

* `Snap` - ajusta (snap) el modelo a otras superficies
* `Group` - Si el objeto seleccionado tiene una combinación de objetos e instancias, esto te permite determinar el comportamiento de la herramienta.
* `Move` - Arrastrar con un solo dedo moverá el objeto. Cuando Snap está activo, esto deslizará el objeto a lo largo de la superficie bajo tu dedo.
* `Rotate` - Arrastrar con un solo dedo rotará el objeto. Cuando Snap está activo, rotará alrededor de la normal de la superficie bajo tu dedo.
* `Scale` - Arrastrar con un solo dedo escalará el objeto.

Transform se puede usar para operar rápidamente 2 de estos modos usando 2 dedos:

* Arrastra un objeto para colocarlo. Deja de mover tu primer dedo, pero no lo levantes de la pantalla.
* Toca con tu segundo dedo en la pantalla mientras mantienes el primer dedo abajo. Al arrastrar el segundo dedo, el objeto se escalará.
* Levanta el segundo dedo y continúa arrastrando el primero; el objeto volverá a estar en modo Move.

También puedes cambiar el segundo modo con un gesto de toque del segundo dedo:

* Arrastra el objeto para colocarlo, deja de moverlo, pero no levantes tu dedo de la pantalla.
* Toca con tu segundo dedo mientras mantienes el primero abajo.
* La herramienta cambia al modo Rotate. Arrastra tu primer dedo para establecer la rotación.
* Toca con el segundo dedo como antes; la herramienta vuelve al modo Move.

Esto ofrece un flujo de trabajo rápido para clonar objetos sobre otro, por ejemplo rocas sobre un paisaje. Observa que el botón Clone también está en la barra de herramientas izquierda para un acceso fácil:

* Usa la herramienta Transform para mover una roca a su lugar.
* Suelta, pulsa el botón Clone
* Mueve esta roca, rota/escala según sea necesario
* Suelta, pulsa el botón Clone
* Mueve esta roca, repite.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo
Esta herramienta te permite mover, rotar y escalar objetos, y alterar los pivotes de los objetos.

El manipulador del visor tiene las siguientes características:

* `Move` - Arrastra en la línea+flecha para mover en X/Y/Z. Arrastra en el punto melocotón en el centro del gizmo para trasladar libremente en el espacio de pantalla. Haz clic en los cuadrados rojo, verde, azul para trasladar en los planos X/Y/Z.
* `Rotate` - Arrastra en los círculos rojo/verde/azul para rotar en X/Y/Z. Arrastra la esfera dentro de los círculos para rotación libre.
* `Scale`- Arrastra en los puntos exteriores rojo/verde/azul para escalar en X/Y/Z. Arrastra en los conos exteriores rojo/verde/azul para escalar en los planos X/Y/Z. Arrastra en el círculo melocotón exterior para escalar uniformemente.

![](/images/tool_gizmo.webp)

#### Nodes y vertices 

Cada objeto en Nomad está formado por un nodo y vértices:

* `Node` - El 'mango' del objeto, que almacena su traslación, rotación y escala, llamado matriz de transformación.
* `Vertices` - Los puntos que definen la superficie de un objeto; almacenan información de posición y pintura.

Si tienes una caja simple formada por 8 vértices, podrías trasladarla modificando su matriz de transformación o modificando las posiciones de los vértices. Al esculpir normalmente quieres modificar los vértices; al mover objetos con el gizmo, normalmente quieres modificar el nodo. Nomad te permite hacer ambas cosas. 

#### Left menu toolbar

La barra de herramientas izquierda controla si el gizmo trabajará sobre el nodo o los vértices, así como otras funciones:

* `Clone` - Crea una copia independiente del objeto actual, que se puede arrastrar con el gizmo.
* `Instance` - Crea una copia instanciada del objeto actual. Los objetos están vinculados, por lo que los cambios de esculpido en un objeto aparecerán en todos los objetos instanciados.
* `Group/Object/Vertex/Auto` - Establece si el gizmo afectará al nodo o a los vértices de un objeto. El modo 'Auto' por defecto intentará una mejor suposición. Si hay varios objetos jerarquizados como hijos, 'Object' solo moverá el objeto actual; los objetos hijo permanecerán estacionarios. El gizmo también puede tener en cuenta máscaras y simetría.
* `Pin` - Por defecto el gizmo se moverá al pivote del objeto seleccionado. Cuando Pin está activado, el gizmo permanecerá donde está.
* `Align` - Alterna entre el pivote alineado con el objeto actual o alineado con el mundo.
* `Snap rotation` - Activa que los valores de rotación se ajusten a incrementos; el valor de snap se muestra y puede editarse cuando Snap está activo.
* `Snap translation` - Activa que los valores de traslación se ajusten a incrementos; el valor de snap se muestra y puede editarse cuando Snap está activo.
* `Pivot` - Cuando está activado, el gizmo se puede mover y rotar sin mover el objeto. Tiene un menú extra explicado a continuación.

#### Pivot
Cuando el modo Pivot está activo, se muestra un menú para permitir cambios rápidos de pivote:

**Reset** 
* `Center` - Mueve el pivote al centro del objeto
* `Bottom` - Mueve el pivote a la parte inferior del objeto
* `Align` - Restablece las rotaciones para alinearlas con el mundo.
* `Mask` - Mueve el pivote al centro de la región sin máscara.

**On Tap**
* `None` - no hace nada cuando se toca el objeto
* `Normal` - Mueve y rota el pivote para alinearlo con el lugar donde se toca la superficie
* `First` - Mueve (pero no rota) el pivote al lugar donde se toca la superficie
* `Medial` - Mueve el pivote al centro del objeto, bajo el lugar donde se toca la superficie.

#### Gizmo settings

![](/images/tool_gizmo_settings.webp)

##### Matrix 
* ![](/icons/target.webp) `Move origin` - Mueve el objeto para que su pivote esté en el centro de la escena, llamado origen.
* ![](/icons/bake.webp)  `Bake` - Congela el objeto donde está actualmente y establece los valores de traslación/rotación en 0 y la escala en 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - Hace que los valores de la matriz correspondan a donde está el manipulador del gizmo en el mundo.
* ![](/icons/reset.webp) `Reset` - Un acceso directo que establece los valores de traslación en 0, los de rotación en 0 y la escala en 1, moviendo y rotando el objeto.

::: tip Bake vs bake to pivot
Crea una caja, selecciona la herramienta Gizmo, abre y fija el menú de ajustes. Por defecto los valores de traslación y rotación son 0, la escala es 1.

Activa el modo Pivot, mueve el manipulador a un lado, desactiva el modo Pivot. El pivote ha cambiado, pero observa que los valores de traslación siguen siendo 0. 

Si quieres ver dónde está el pivote *realmente*, haz clic en `Bake Pivot`. Ahora los valores de traslación se actualizan. Observa que la caja no se mueve durante esta operación, ni en modo Pivot.

Mueve y rota la caja a algún lugar y luego pulsa `Move Origin`. Mueve el objeto para que su pivote esté en el centro del mundo, pero deja la rotación sin cambios.

Haz clic en `Reset` y la rotación se establecerá también en 0.

Mueve y rota la caja de nuevo; esta vez haz clic en `Bake`. El pivote permanece donde está, la caja permanece donde está, pero los valores de traslación y rotación se establecen en 0.

¡Practica esto unas cuantas veces! Entiende que los valores del pivote están ocultos; Nomad se encarga de ello por ti, pero si necesitas establecer el pivote en ubicaciones reales en el espacio, Bake Pivot lo hará por ti.

:::

* `Translation` - los valores de traslación X, Y, Z
* `Rotation` - los valores de rotación X, Y, Z
* `Scale` - La escala uniforme si está activada, o la escala X, Y, Z si está desactivada.
* `Uniform scale` - Alterna la capacidad de escalar uniformemente o de forma independiente en cada eje

-----

* `Compact` - alterna el diseño del gizmo para colocar los manejadores extra fuera o dentro de la esfera de rotación
* `Widget size` - el tamaño del gizmo
* `Thickness` - el grosor de las líneas del gizmo
* `Opacity` - la opacidad del gizmo
* `Hide on interaction` - alterna si el gizmo debe ocultarse temporalmente cuando se arrastra

-----

* `Tangent roll threshold` - Controla cómo se comporta la interfaz de rotación al arrastrar en los manejadores de círculo para rotar en X/Y/Z. Si este valor es 0, la rotación funciona como un dial: arrastra el gizmo en círculos. Si este valor es 90, la rotación funciona como tirar de la cuerda de un yo-yo: arrastra en línea recta hacia o desde donde hiciste clic primero. Los valores entre 0 y 90 harán una combinación de ambos; por debajo del valor será el movimiento lineal, por encima será el movimiento circular.
* `Numerical input` - cuando está activado, un solo toque en el gizmo mostrará una ventana para introducir un valor exacto para el eje del widget tocado.

::: warning
Las herramientas [Gizmo](#gizmo), [Translate](#translate), [Rotate](#rotate) y [Scale](#scale) usan su propia casilla de simetría.

Por defecto esta simetría está desactivada.
:::

En la izquierda puedes mover el pivote del gizmo; puedes ver el vídeo de abajo en acción.
Esto es especialmente útil para la rotación, ya que no cambia nada para la traslación.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Facegroup

Los facegroups te permiten organizar tu objeto en caras de diferentes colores. Puedes usar estos grupos de muchas maneras en Nomad:

* Un método de selección rápida para máscaras
* Ocultar/mostrar secciones de tu objeto
* Organizar tu objeto sin tener que dividirlo en partes separadas
* Definir regiones UV
* Guiar el Quad Remesher
* Control adicional para herramientas como Smooth.

#### Facegroup left toolbar

* `Patch ` - Muestra los facegroups disponibles como parches. Los parches no usados se pueden borrar. Toca un parche para renombrarlo o cambiar su color. El icono de más te permite crear nuevos parches.
* `Dot` - Pinta sobre el objeto para definir facegroups. Cuando '+ Face Group' está activado, cada nuevo trazo creará automáticamente un nuevo facegroup, útil para definir regiones rápidamente. Un toque rellenará por inundación la región seleccionada. El deslizador establece el radio del punto.
* `Relax` - Suaviza los bordes de los facegroups. Muy útil para definir bordes limpios para Quad Remeshing o para definir paneles para modelado hard surface. Los deslizadores controlan el radio y la intensidad de la operación Relax.
* `Shape selector` - Crea facegroups con formas en lugar de un pincel, mediante `Lock+Radius`, `Lasso`, `Polygon`, `Rect` y `Ellipse`. Consulta [Shape Selector](#shape-selector) para más información.
* `Auto-pick` - Cuando está activado, seleccionará el parche donde comienza el trazo y aplicará ese parche para el resto del trazo. Muy útil para limpiar regiones de facegroups; si un facegroup se ha extendido demasiado, activa Auto-pick, comienza un trazo desde donde el parche de facegroup es correcto y arrastra hasta el borde para reasignar el parche correcto.

### ![](/icons/tool_hide.webp) Hide
Oculta o aísla partes del objeto. 

Los modos principales se controlan desde el menú izquierdo:

* `Dot` - Pincela sobre el objeto para ocultar partes del objeto.
* `Shape selector` -  Oculta con formas en lugar de un pincel, mediante `Lasso`, `Polygon`, `Line`, `Rect` y `Ellipse`. Consulta [Shape Selector](#shape-selector) para más información.
* `Show` - invierte la operación, de modo que el modo seleccionado mostrará en lugar de ocultar partes del objeto.

Aparecerá una barra de herramientas en la parte superior del visor con controles adicionales:

* `Clear` - Restaura el objeto; todas las partes ocultas se mostrarán.
* `Invert` - Intercambia las partes ocultas y visibles.
* `Facegroup` - Usa facegroups para ocultar rápidamente secciones; al tocar un facegroup se ocultará todo el facegroup.
* `Mask` - Si hay una máscara activa, al pulsar este botón se ocultará la sección enmascarada.
* `Delete` - Borra la parte oculta del objeto
* `Split` - Divide la parte oculta del objeto en una nueva forma.

### ![](/icons/tool_measure.webp) Measure
Arrastra para medir la distancia entre 2 puntos.

### ![](/icons/tool_remesh.webp) Quad Remesher

![](/images/tool_quadremesher.webp)

Esta herramienta convertirá el objeto seleccionado en una topología quad limpia, con controles para densidad, flujo de aristas y simetría. 

::: tip
Quad Remesher está desarrollado por [Exoside](https://exoside.com/) para iOS y escritorio. 

Para iOS es una compra integrada en la app dentro de Nomad, un pago único de 16 USD.

Para escritorio, compra una licencia en [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Puedes comprarla solo para Nomad de escritorio o una licencia cruzada para todas las apps de escritorio compatibles.

Si ya posees Quad Remesher para otra app de escritorio, puedes [comprar una actualización a todas las plataformas a menor coste.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher no está disponible para Android. Android puede usar el 'Quad Remesh - Instant' gratuito y de código abierto disponible en el menú Topology -> Misc, pero entiende que su conjunto de funciones es muy limitado.
:::

Cuando esta herramienta se activa por primera vez, preguntará si deseas habilitarla como una compra dentro de la aplicación. Una vez activa, las barras de herramientas izquierda y superior se habilitarán.

* `Dot` - Este pincel establecerá la densidad objetivo. Intensidad al 100% pintará en rojo, lo que usará el doble de la densidad de quads objetivo en esas regiones. Intensidad al 0% pintará en cian, lo que usará la mitad de la densidad de quads objetivo en esas regiones. Intensidad al 50% pintará en gris, lo que usará la densidad de quads objetivo predeterminada.
* `Smooth` - Suaviza las transiciones de densidad rojo/gris/cian.
* `Curve` - Dibuja curvas sobre la superficie del esculpido; Quad Remesher las usará como guías para el flujo de aristas. Toca una curva para eliminarla.
* `Path` - Dibuja trazos sobre la superficie del esculpido; Quad Remesher los usará como guías para el flujo de aristas. Toca un trazo para eliminarlo. 
* `Rect` - Dibuja rectángulos sobre la superficie del esculpido; Quad Remesher los usará como guías para el flujo de aristas. Toca un trazo para eliminarlo.
* `Ellipse` - Dibuja elipses sobre la superficie del esculpido; Quad Remesher las usará como guías para el flujo de aristas. Toca un trazo para eliminarlo.

#### Barra de herramientas superior de Quad Remesher
![](/images/tool_quadremesher_toolbar.webp)

Aparecerá una barra de herramientas en la parte superior de la vista con controles adicionales:


* `<Count>` - Haz clic para iniciar el proceso de Quad Remesher; este número indica cuál será el recuento objetivo de quads.
* `Quads` - Establece el recuento objetivo de quads deslizando a izquierda y derecha, o toca para fijar un número exacto. Ten en cuenta que esto es más una guía que un número fijo; los distintos controles de Quad Remesher a menudo harán que el resultado no coincida exactamente con este objetivo.
* `Half` - Un atajo para establecer el recuento objetivo a la mitad del recuento de polígonos actual.
* `Same` - Un atajo para establecer el recuento objetivo igual al recuento de polígonos actual.
* `Guides` - Indica el número total de guías, o tócalo para eliminar todas las guías.
* `Density X` - Toca para eliminar toda la pintura de densidad.
* `Density (painting)` - Conmutador para usar o ignorar la pintura de densidad.
* `Face Group` - Conmutador para usar o ignorar los grupos de caras para dirigir Quad Remesher.
* `Relax` - Conmutador para relajar automáticamente los bordes de los grupos de caras durante el remallado en quads. Si ya has relajado/suavizado los bordes de tus grupos de caras, desactiva esta opción.
* `Relax Slider` - Un deslizador de acceso rápido para relajar los bordes de los grupos de caras.
* `Hard Edges` - Conmutador para intentar mantener los bordes duros.
* `Reproject Vertex` - Conmutador para reproyectar la nueva distribución sobre la malla de entrada.
* `Symmetry` - Conmutador para habilitar un resultado simétrico. Ten en cuenta que la simetría siempre se calcula alrededor del eje X del mundo, así que asegúrate de que tu modelo esté en el origen si esperas un resultado simétrico.
* `...` - Menú de configuración de Quad Remesher. 

#### Menú de configuración de Quad Remesher

La mayoría de estos ajustes están disponibles en la barra de herramientas superior.

* `<Count>, Half, Same` - Igual que los botones Remesh, Half, Same en la barra de herramientas superior.
* `Target Quads` - Igual que el botón `Quads` en la barra de herramientas superior.
* `Adaptive quad count` - Conmutador para habilitar el uso de quads más pequeños en áreas de alta curvatura y quads más grandes en áreas de menor curvatura.
* `Adaptive size` - Establece el grado de adaptatividad. 100% permitirá el tamaño adaptativo máximo; al 0% los quads serán uniformes.
* `Auto-Detect Hard Edges` - Conmutador para adaptar la distribución del remallado en quads para seguir mejor las superficies afiladas.
* `Density (painting)` - Igual que el botón `Density (painting)` en la barra de herramientas superior.
* `Reproject Vertex` - Conmutador para reproyectar la nueva distribución sobre la malla de entrada.
* `Face Group` - Igual que el botón `Face Group` en la barra de herramientas superior.
* `Relax Slider` - Un deslizador de acceso rápido para relajar los bordes de los grupos de caras.

::: tip

Una receta para obtener un buen remallado en quads con artefactos mínimos:

* Crea grupos de caras en la malla para definir tu flujo de quads ideal.
* Relaja los grupos de caras para obtener bordes de grupo suaves.
* Decima. Esto garantizará que no tengas caras delgadas o distorsionadas en el borde de los grupos de caras. En los ajustes de decimación asegúrate de que la opción de grupos de caras esté habilitada. Esto hará que los bordes de triángulos sigan con precisión los bordes de tus grupos de caras. 

En las opciones de Quad Remesh asegúrate de que la relajación esté deshabilitada (ya que ya has relajado la malla) y deberías obtener buenos resultados.

:::

### ![](/icons/tool_select.webp) Select
Usa los modos de forma para seleccionar objetos en la escena. `Unselect` eliminará objetos de la selección.

### ![](/icons/tool_view.webp) View
Esta "herramienta" no hace nada en particular; es simplemente una forma de ver el modelo sin modificar tu escena.


## Menú contextual de la caja de herramientas

![](/images/tools_context_menu.webp)

Un clic derecho o una pulsación prolongada sobre una herramienta en la caja de herramientas mostrará un menú contextual. Este menú tiene las siguientes opciones:

* `Save` - guarda cualquier cambio que hayas hecho a la herramienta
* `Clone` - duplica la herramienta en un nuevo acceso directo de herramienta
* `Last save` - revierte a la versión previamente guardada de la herramienta
* `Icon` - cambia el icono de la herramienta
* `Reset` - restablece la herramienta a sus valores predeterminados
