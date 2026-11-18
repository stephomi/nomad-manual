# ![](/icons/toolbox.webp) Herramientas {#tools}

![](/images/tools_menu.webp)

::: tip
Baja hasta [Herramientas](#tools-1) para ver la descripción de cada herramienta.
:::

## Visión general {#overview}

Las herramientas se eligen en la `Caja de herramientas` de la derecha y se controlan con los controles de herramienta de la izquierda. Encontrarás más ajustes en el menú `Herramienta`, en el menú de arriba a la derecha.

Las herramientas de pincel tienen controles de tamaño e intensidad. Las herramientas de selección tienen controles para varios estilos de selección. La parte inferior de los controles de herramienta tiene accesos directos a operaciones de uso frecuente (Suavizar, Máscara, Ocultar, Grupo de caras, Gizmo, Color, Alfa).

Las herramientas de Nomad tienen un código de colores en la caja de herramientas (desactiva `Herramientas con color` en el menú [Interfaz](interface.md) para tener etiquetas sin color):

* <span class=brush>**Herramientas de pincel**</span> (Arcilla, Brocha, Suavizar, Capa, Inflar, Eli. capa, Quad Remesher)
* <span class=move>**Herramientas de movimiento**</span> (Mover, Arrastrar, Elástico, Desplazar)
* <span class=mask>**Herramienta de máscara**</span> (Máscara)
* <span class=paint>**Herramientas de pintura**</span> (Pintar, Difuminar)
* <span class=flatten>**Herramientas de aplanado**</span> (Aplanar, Planar, Pulir)
* <span class=pinch>**Herramientas de pellizco**</span> (Pliegue, Pellizcar)
* <span class=stamp>**Herramientas de sello**</span> (Sello, VDM)
* <span class=selection>**Herramientas basadas en selección**</span>, en las que primero se dibuja una máscara 2d y luego se aplica una operación (Recortar, Dividir, Proyectar)
* <span class=creation>**Herramientas de creación**</span> (Tubo, Torno, Insertar)
* <span class=transform>**Herramientas de transformación**</span> (Transformar, Gizmo, Organizar, Enrejado)
* <span class=misc>**Herramientas varias**</span> (Grupo de caras, Ocultar)
* <span class=view>**Herramientas de vista**</span> (Vista, Medir, Seleccionar)



Muchas de estas herramientas se pueden personalizar con distintos comportamientos de pincel, presión, texturas, etc. desde el menú [Trazo](stroke.md). 


### Controles del pincel {#brush-controls}

La barra de herramientas de la izquierda tiene reguladores de radio e intensidad, y luego controles propios de cada categoría de herramienta, que se explican más abajo.

![](/images/tool_left_panel.webp)

::: tip
En muchas herramientas, el regulador de intensidad puede pasar del 100 %. ¡Vale la pena experimentar!
:::

### Modo Sub {#sub-mode}
El botón situado justo debajo del regulador de intensidad es el botón `Sub`. Su etiqueta y su función cambian con cada herramienta, y al pulsarlo activa un comportamiento alternativo, normalmente el opuesto. Por ejemplo, en [Pintar](#paint) activa un modo de borrado, y en [Pliegue](#crease) crea bordes en relieve en lugar de pliegues, etc.

Por defecto funciona como un botón temporal: puedes mantenerlo pulsado para activarlo momentáneamente y, al soltarlo, se desactiva. Si lo tocas una vez, el modo Sub queda activado de forma permanente.

### Accesos directos {#shortcuts}
En la parte inferior de la barra de herramientas de la izquierda están los accesos directos a [Suavizar](#smooth), [Máscara](#mask), [Ocultar](#hide), [Grupo de caras](#facegroup), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders) y [Alfa](stroke.md#alpha). 

Por defecto, todos funcionan como botones temporales: puedes mantenerlos pulsados para activarlos momentáneamente y, al soltarlos, se desactivan. Si tocas uno una vez, ese modo queda activado de forma permanente.

### Controles de selección {#selection-controls}

Las herramientas [Máscara](#mask), [Pintar](#paint), [Recortar](#trim), [Dividir](#split), [Proyectar](#project), [Grupo de caras](#facegroup), [Ocultar](#hide) y [Seleccionar](#select) usan controles parecidos para seleccionar zonas de la malla.

![](/images/tools_shape_selector_panel.webp)

Pulsa el botón de forma de la barra de herramientas de la izquierda (muestra la forma actual, `Lazo` por defecto) para abrir una ventana emergente con las formas. En las herramientas que también funcionan con un pincel (Máscara, Pintar, Grupo de caras, Ocultar), esa misma ventana incluye también los tipos de trazo.

* `Vista` - Sin forma: la herramienta no hace nada en particular, como el modo cámara.
* `Lazo` - Una forma dibujada a mano alzada
* `Polígono` - Una forma cerrada definida por una combinación de curvas y/o líneas rectas. Consulta [Edición de formas](#shape-editing) más abajo para saber más.
* `Curva` - (Solo Proyectar) - Una curva a mano alzada para la proyección
* `Ruta` - (Solo Proyectar) - Una curva definida por puntos. Consulta [Edición de formas](#shape-editing) más abajo para saber más.
* `Línea` - Arrastra una línea para definir un corte plano. Por defecto actúa sobre la malla de inmediato; cambia la opción `Editar` si no quieres que sea así (mantén pulsado o desliza sobre el icono de la línea)
* `Banda` - Una franja entre dos guías paralelas, con un degradado que la atraviesa. `Extender` mantiene el valor completo más allá de la guía lejana en lugar de detenerse en la banda, y `Invertir` cambia la guía desde la que empieza el degradado.
* `Rect` - Arrastra una línea diagonal que define las esquinas de un rectángulo. Mantén pulsado o desliza para mostrar la opción `Editar`, `Cuadrado` para forzar un cuadrado y `Centrado` para que el primer clic sea el centro del rectángulo.
* `Elipse` - Arrastra una línea diagonal que define el tamaño de una elipse. Mantén pulsado o desliza para mostrar la opción `Editar`, `Círculo` para forzar un círculo y `Centrado` para que el primer clic sea el centro de la elipse.
* `Voltear` - Invierte la máscara de la forma, o la dirección de la herramienta Proyectar.

La mayoría de las herramientas tienen una opción `Editar` que decide qué pasa cuando terminas de dibujar la forma:
* `Editar: desactivado` - La operación se aplica en cuanto sueltas.
* `Editar: activado` - La forma sigue siendo editable. Junto a ella aparece un botón verde que ejecuta la operación. Así puedes retocar la forma y ajustar la vista, y cuando la tengas lista, pulsar el botón verde.
* `Editar: mantener` - La operación se aplica al soltar, salvo que mantengas el dedo al final del trazo para seguir editando la forma.

### Edición de formas {#shape-editing}
La edición de polígonos y la de curvas funcionan de forma parecida:

* Para empezar, arrastra una línea para definir 2 puntos y luego tira desde el centro de la línea para formar un polígono o una curva.
* Toca los puntos para alternar entre suave y anguloso. 
* Toca y arrastra sobre los tramos de curva o de línea para crear puntos nuevos.
* Para borrar un punto, arrástralo sobre su vecino hasta que se ponga rojo.
* El icono de la papelera, en la esquina del icono del polígono o de la ruta, borra la forma.

### Menú de configuración {#settings-menu}

Muchas herramientas tienen ajustes adicionales en el menú `Herramienta`, en el menú de arriba a la derecha. El menú aparece en gris en las herramientas que no tienen ajustes adicionales.

![](/images/tools_settings_menu.webp)

## Herramientas {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)    <br> [Arcilla](#clay)    | ![](/icons/tool_brush.webp)   <br> [Brocha](#brush)    | ![](/icons/tool_move.webp)       <br> [Mover](#move)             | ![](/icons/tool_drag.webp)      <br> [Arrastrar](#drag)      | ![](/icons/tool_elastic.webp)   <br> [Elástico](#elastic)    | ![](/icons/tool_smooth.webp)  <br> [Suavizar](#smooth) |
| ![](/icons/tool_mask.webp)    <br> [Máscara](#mask)    | ![](/icons/tool_paint.webp)   <br> [Pintar](#paint)    | ![](/icons/tool_smudge.webp)     <br> [Difuminar](#smudge)       | ![](/icons/tool_flatten.webp)   <br> [Aplanar](#flatten)     | ![](/icons/tool_planar.webp)    <br> [Planar](#planar)       | ![](/icons/tool_polish.webp)  <br> [Pulir](#polish)    |
| ![](/icons/tool_crease.webp)  <br> [Pliegue](#crease)  | ![](/icons/tool_pinch.webp)   <br> [Pellizcar](#pinch) | ![](/icons/tool_trim.webp)       <br> [Recortar](#trim)          | ![](/icons/tool_split.webp)     <br> [Dividir](#split)       | ![](/icons/tool_project.webp)   <br> [Proyectar](#project)   | ![](/icons/tool_layer.webp)   <br> [Capa](#layer)      |
| ![](/icons/tool_inflate.webp) <br> [Inflar](#inflate)  | ![](/icons/tool_nudge.webp)   <br> [Desplazar](#nudge) | ![](/icons/tool_stamp.webp)      <br> [Sello](#stamp)            | [VDM](#vdm)                                                  | ![](/icons/tool_clearLayer.webp) <br> [Eli. capa](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tubo](#tube)       |
| ![](/icons/tool_lathe.webp)   <br> [Torno](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insertar](#insert) | ![](/icons/tool_transform.webp)  <br> [Transformar](#transform)  | ![](/icons/tool_gizmo.webp)     <br> [Gizmo](#gizmo)         | ![](/icons/tool_faceGroup.webp) <br> [Grupo de caras](#facegroup) | ![](/icons/tool_hide.webp)    <br> [Ocultar](#hide)    |
| ![](/icons/tool_measure.webp) <br> [Medir](#measure)   | [Organizar](#arrange)                                    | ![](/icons/tool_remesh.webp)     <br> [Quad Remesher](#quad-remesher) | ![](/icons/tool_select.webp)    <br> [Seleccionar](#select)  | ![](/icons/tool_lattice.webp)   <br> [Enrejado](#lattice)    | ![](/icons/tool_view.webp)    <br> [Vista](#view)      |

------

### ![](/icons/tool_clay.webp) Arcilla {#clay}
La herramienta Arcilla sirve para ir construyendo tu escultura. `Sub` quita material de la escultura.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Brocha {#brush}
El pincel estándar. `Sub` quita material.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Mover {#move}
La zona bajo el pincel se queda pegada a él, lo que permite una deformación elástica. La selección se mantiene durante el movimiento: si alejas el pincel y luego lo devuelves a donde empezaste, no verás ninguna deformación.

El modo Sub es `Normal`, y mueve la zona bajo el pincel a lo largo de la normal de la superficie.

Este pincel va bien tanto para deformaciones a gran escala como para pequeñas deformaciones cuidadosas.

#### Configuración de Mover {#move-settings}

* `Radio (Fondo)` - A qué distancia del borde de un modelo puedes estar y seguir esculpiendo; útil cuando trabajas la silueta de un objeto. Desmárcalo para agarrar solo cuando empiezas sobre el modelo.
* `Solo vértice del mismo lado` - Ignora los vértices que apuntan en dirección opuesta a la deformación.
* `Dirección` - La usa el modo Sub `Normal` y decide si al arrastrar empujas o tiras de la superficie:
    * `Automático` - Elige por ti uno de los dos métodos de abajo, según el ángulo de la normal de la superficie.
    * `Normal 3D` - Compara la posición del puntero en la pantalla con la normal de la superficie vista desde la cámara.
    * `XY` - Usa la posición del puntero en la pantalla (arriba/abajo, izquierda/derecha) para decidir si empujar o tirar.
    * `Umbral` - Con `Automático`, el ángulo límite que decide qué método se usa.
* `Velocidad de giro` - Puedes torcer la zona agarrada mientras la mueves: gira dos dedos, gira el cuerpo de tu lápiz o mantén una tecla modificadora (Alt, Ctrl, Shift o Cmd) mientras arrastras con el ratón. Hay un regulador para los dedos, otro para el lápiz y otro para el ratón; desmarca uno para desactivar esa entrada.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Arrastrar {#drag}
La zona bajo el pincel se queda pegada a él, lo que permite una deformación elástica. A diferencia del pincel Mover, la selección se actualiza continuamente durante el trazo, así que puedes crear formas alargadas, como serpientes, sobre todo con la topología dinámica activada.

El modo Sub es `Normal`, y mueve la zona bajo el pincel a lo largo de la normal de la superficie.

Este pincel va bien para cambios de forma más sueltos y gestuales.

#### Configuración de Arrastrar {#drag-settings}

Arrastrar tiene los mismos ajustes que [Mover](#move-settings): `Radio (Fondo)`, `Solo vértice del mismo lado`, `Dirección` y `Velocidad de giro`.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_elastic.webp) Elástico {#elastic}
Agarra y estira la superficie como [Mover](#move), pero con una deformación elástica: en lugar de detenerse en el borde del pincel, el tirón se atenúa suavemente con la distancia a lo largo del objeto, un poco como al estirar goma. El radio del pincel define lo amplio que es el tirón.

El modo Sub es `Normal`, y mueve la zona bajo el pincel a lo largo de la normal de la superficie.

Este pincel va bien para grandes cambios de proporciones, suaves, que se mantienen lisos.

#### Configuración de Elástico {#elastic-settings}

Elástico tiene los mismos ajustes que [Mover](#move-settings), salvo `Solo vértice del mismo lado`. `Radio (Fondo)` está desactivado por defecto.

### ![](/icons/tool_smooth.webp) Suavizar {#smooth}
Suaviza la zona promediando la posición de los puntos. Esta herramienta depende mucho de la densidad de polígonos.
Así que, si tienes muchos polígonos, el suavizado será menos eficaz.

El modo Sub es `Relajar`, que solo suaviza la malla de alambre pero intenta conservar los detalles geométricos.

#### Configuración de Suavizar {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Grupo de caras {#smooth-facegroup}

* `Relajar` - Suaviza los bordes de los grupos de caras. Usa una intensidad superior al 100 % para suavizar los bordes rápidamente. `Automático` suaviza solo si la vista previa de grupos de caras está activada, `No` lo desactiva y `Sí` lo activa. 

##### Vértice {#vertex}
* `Conservar volumen` - Suaviza sin encoger la superficie, para que suavizar una y otra vez no desinfle tus formas. El botón del engranaje que tiene al lado guarda las cantidades de `Encoger` e `Inflar` que se usan para ello.
* `Conservar bordes` - En mallas con bordes abiertos, por ejemplo un plano, es posible que las esquinas se suavicen hasta desaparecer. Con esta opción activada, los vértices del borde de la malla se quedan quietos.
* `Suavizado estable` - Intenta que el suavizado no dependa de la topología. Funciona mejor con densidades de topología variables y con una intensidad de suavizado alta.
* `Relajar` - Lo mismo que el modo alternativo Relajar de la barra de herramientas de la izquierda.

##### Pintura {#painting}
* `Suavizado de pantalla` - Usa esta opción para obtener un suavizado independiente de la topología, incluso con muchos polígonos. `Automático`, `No` o `Sí`.
* `Muestras de pantalla` - La calidad del suavizado: los valores altos suavizan más, pero son más lentos.

::: tip
Con densidades de polígonos altas puede que necesites subir la intensidad por encima del 100 %. Los valores muy altos (300 %, 500 %) también funcionan bien como herramienta de escultura: obligan a las zonas a quedar planas y lisas rápidamente bajo el pincel, ¡como golpear arcilla con un mazo!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Máscara {#mask}
Esta herramienta te permite enmascarar vértices. Los vértices enmascarados quedan protegidos al esculpir o pintar. 

El modo Sub es `Quitar máscara`, y borra donde se ha pintado la máscara.

Igual que las selecciones en los programas de pintura 2d, las máscaras se pueden pintar con un pincel o crear con formas de selección (`Lazo`, `Rect`, `Banda`...), y también desenfocar o enfocar. Elige el pincel o la forma en la ventana emergente de trazo de la barra de herramientas de la izquierda; consulta [Controles de selección](#selection-controls).

A diferencia de los programas de pintura 2d, también se pueden crear a partir de grupos de caras, y las máscaras sirven para crear geometría nueva con operaciones de tipo extrusión o extracción. 

![](/videos/tool_mask1.mp4)

 En la parte superior de la vista aparece una barra de herramientas con controles adicionales. 

![](/images/tool_mask_toolbar.webp)

Puedes tocar el título de la barra para desplegarla o plegarla, o tocar la flecha de arriba a la derecha para llevarla a la parte superior o inferior de la interfaz.

| Acción                                             | Descripción                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Limpiar todo       | Borra la máscara de todos los objetos. Cuando hay otros objetos también enmascarados, un botón `Borrar` adicional borra solo la de los objetos seleccionados |
| ![](/icons/invert.webp)        Invertir           | Invierte la máscara                                                                        |
| ![](/icons/sharpen.webp)       Enfocar            | Hace más nítido el borde de la máscara                                                     |
| ![](/icons/blur.webp)          Desenfocar         | Desenfoca el borde de la máscara                                                           |
| ![](/icons/outline.webp)       Borde              | Enmascara el borde abierto de la malla, como el canto de un plano o el contorno de un agujero |
| ![](/icons/blur.webp)          Desenfocar ->      | Arrastra a la derecha para desenfocar la máscara y a la izquierda para enfocarla            |
| ![](/icons/circle_plus.webp)   Expandir ->        | Arrastra a la derecha para expandir la zona enmascarada y a la izquierda para encogerla      |
| ![](/icons/intensity.webp)     Reforzar ->        | Arrastra a la derecha para reforzar la máscara y a la izquierda para atenuarla, sin cambiar su forma |
| ![](/icons/dig.webp)           Cavidad ->         | Reconstruye la máscara a partir de la curvatura de la superficie: arrastra a la derecha para que solo las cavidades sigan pintables, y a la izquierda para que solo lo sean los relieves |
| ![](/icons/culling.webp)       Frontal            | Actívalo para enmascarar solo los vértices orientados hacia delante                        |
| ![](/icons/eye_open.webp)      Visible            | Con formas, actívalo para ignorar los vértices ocultos detrás de otras superficies         |
|                                 Convertir          | Convierte la máscara en un grupo de caras                                                  |
| ![](/icons/group_to_mask.webp) Pulsación única (grupo de caras) | Al activarlo se muestran los grupos de caras, y tocar un grupo de caras lo enmascara |
|                                 Pulsación única (máscara) | Al activarlo, tocar una 'isla' de polígonos enmascarados o sin enmascarar rellena toda esa isla. |
| ![](/icons/connect.webp)       Conectada          | Al activarlo, los trazos de máscara solo afectan a la topología conectada.                 |

##### Gestos rápidos de máscara {#mask-quick-gesture}
Puedes hacer gestos al estilo de ZBrush mientras mantienes pulsado el botón de máscara rápida de la barra de herramientas de la izquierda:
| Acción     | Gesto (mantén pulsado el acceso directo de abajo a la izquierda) |
| :--------: | :--------------------------------: |
| Invertir   | Toca el fondo                      |
| Borrar     | Arrastra sobre el fondo            |
| Desenfocar | Toca una zona enmascarada          |
| Enfocar    | Toca una zona sin enmascarar       |


#### Configuración de Máscara {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

La configuración de Máscara sirve sobre todo para crear geometría a partir de la máscara. Las pestañas de arriba eligen la operación: [Extraer](#extract), [Dividir](#split-mask) o [Tallar](#carve). Las opciones de debajo cambian según la operación.

* `Vista previa` - Muestra cómo quedará la nueva geometría mientras ajustas los parámetros.
* `Rayos X` - Qué objetos se dibujan en rayos X durante la vista previa: `Ninguno`, `No seleccionados`, `Seleccionados` o `Todo`.

##### Extraer {#extract}
* `Extraer` - Crea la geometría extraída como un objeto nuevo.
* `Acción de cierre` - Cómo se cierra la forma extraída. `Ninguno` duplica los polígonos enmascarados en una forma nueva y la deja abierta. `Rellenar` hace lo mismo y además rellena y suaviza el agujero de la parte trasera (no lo uses en superficies planas). `Carcasa` cierra la forma usando el valor de `Altura`, y es la opción por defecto.

::: tip

Si la vista previa está activada con rayos X, pulsar el botón Extraer puede confundir al principio. Como el menú sigue activo, intenta mostrar una vista previa de extracción sobre tu nueva forma y pone en rayos X la superficie original. Pero como la nueva superficie no tiene máscara, no puede mostrar la vista previa, y Nomad te avisa con 'Nothing to Extract!'. 

Es normal: cierra el menú de configuración de la máscara para ver la nueva forma y la original, y vuelve a seleccionar la superficie original si necesitas borrar la máscara o dibujar máscaras nuevas.
:::

##### Dividir {#split-mask}
* `Dividir` - Extrae tanto las zonas enmascaradas COMO las no enmascaradas en formas nuevas. 
* `Acción de cierre` (enmascarada) - Cómo se cierra la parte enmascarada, con las mismas opciones `Ninguno`, `Rellenar` y `Carcasa` que en Extraer.
* `Acción de cierre` (no enmascarada) - Cómo se cierra la parte no enmascarada, con las mismas opciones.

##### Tallar {#carve}
* `Tallar` - Actúa como si hubieras recortado la superficie hacia dentro en la cantidad de `Altura`, como quien corta un trozo de piel de naranja. La `Altura` no puede ser 0.

##### Altura {#thickness}
* `Altura` - La altura de la forma extraída. El botón Más/Menos alterna entre una extrusión hacia fuera, hacia dentro o a ambos lados. 

##### Suavidad {#smoothness}
Si está activa, suaviza la forma extraída; funciona mejor con muchos polígonos. 
* `Todo` / `Solo bordes` - Suaviza toda la forma, o solo sus bordes, sin tocar la forma de la superficie superior.
* `Iteraciones` - Con `Todo`, la cantidad de suavizado aplicada. Los valores altos dan bordes curvos muy suaves, pero empiezan a alejarse de la forma de la máscara.
* `Pared` - Con `Solo bordes`, la cantidad de suavizado de las paredes. Su botón alterna entre Relajar, que conserva las esquinas marcadas, y Suavizar, que también las redondea.
* `Interior` - Con `Solo bordes`, cuánto se uniformiza la superficie superior. Su botón alterna entre Relajar, que conserva los detalles esculpidos y solo uniformiza la dirección de extrusión (así los detalles dejan de crear picos), y Suavizar, que suaviza la propia superficie.

##### Lados {#edge-loop-side}
* `Recto` - Paredes lisas a los lados de la forma extraída.
* `Bisel` - (Solo Extraer con `Carcasa`) Un borde inclinado en el canto delantero. `Bisel` define su ancho, en % de `Altura` o en unidades del mundo (el botón de al lado cambia entre ambos), `Divisiones del bisel` lo subdivide (`Automático` por defecto), y una curva te permite dar forma a su perfil.
* `Perfil` - Da forma a las paredes con una curva de perfil, con un `Ancho` en % de `Altura` o en unidades del mundo.
* `Máscara` - La altura sigue a la máscara: las partes desenfocadas de la máscara tienen menos altura, lo que permite formas suaves y de altura variable.
* `Divisiones de pared` - El número de bucles de aristas en los lados. Con `Automático`, Nomad elige el número de divisiones que da polígonos cuadrados acordes con los polígonos de la zona enmascarada.



### ![](/icons/tool_maskSelector.webp) Máscara de selección {#selection-mask}
La herramienta Máscara de selección (Sel. máscara) ahora forma parte de la [herramienta Máscara](#mask). Para enmascarar con formas en lugar de un trazo de pincel, elige una forma (`Lazo`, `Polígono`, `Rect`...) en la ventana emergente de trazo de la herramienta Máscara; consulta [Controles de selección](#selection-controls).

El modo Sub `Quitar máscara` también funciona con formas, y borra la máscara dentro de la forma.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Pintar {#paint}
Aplica color y propiedades de material. Para saber más sobre los materiales, visita la sección [Pintura](painting.md).

El modo Sub es `Borrar`, y quita la pintura.

Además de los trazos de pincel, Pintar también puede rellenar formas (`Lazo`, `Rect`, `Banda`...); consulta [Controles de selección](#selection-controls).

#### Configuración de Pintar {#paint-settings}
* `Filtrado de capas` - Funciona como el bloqueo de transparencia de capa de Photoshop o Procreate. Si pintas en una capa con esta opción activada, solo puedes modificar donde ya hay pintura; las zonas sin pintar quedan protegidas. Solo está disponible cuando hay una capa seleccionada.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Difuminar {#smudge}
Difumina el color y las propiedades de material. El menú de configuración de Difuminar tiene un regulador de `Calidad`: los valores bajos hacen los trazos más rápidos.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Aplanar {#flatten}
Aplana la zona proyectando los puntos sobre el plano medio.

El modo Sub es `Rellenar`: define un plano a partir del punto más alto y tiende a tirar de los puntos hacia arriba.

#### Configuración de Aplanar {#flatten-settings}

* `Bloquear dirección del plano` - Usa la dirección del plano calculada en el primer clic. Está desactivado por defecto.
* `Bloquear origen del plano` - Usa el primer clic como centro del plano. Está desactivado por defecto, y solo se puede activar junto con `Bloquear dirección del plano`.

Cuando una de estas opciones, o las dos, están desactivadas, puedes ir hundiendo el aplanado poco a poco o cambiar el ángulo del plano con trazos largos que pasen por distintas profundidades y curvaturas. Junto con las opciones de muestreo de zona del menú del pincel, esto ofrece un control muy preciso.

::: tip
Cuando trabajes en zonas de mucha curvatura, por ejemplo al aplanar las mejillas mientras la herramienta no para de afectar a los lados de la nariz, prueba a crear una máscara para proteger las zonas que el pincel Aplanar no debe tocar.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar {#planar}
Vuelve planos los puntos proyectándolos sobre el plano medio, pero acumulando menos que el pincel Aplanar. Así se obtienen superficies de aristas vivas más limpias. Los trazos rápidos empujan y tiran más de la superficie; los trazos lentos que empiezan en zonas ya planas y avanzan hacia fuera mantienen mejor el plano.

El modo Sub es `Rellenar`: define un plano a partir del punto más alto y tiende a tirar de los puntos hacia arriba.

En realidad, Planar es la misma herramienta que `Aplanar`, pero con `Bloquear dirección del plano` activado, así que tiende a crear superficies más estables y de aristas vivas, mientras que Aplanar es más escultórico y sirve para crear zonas semiplanas.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_polish.webp) Pulir {#polish}
Otro miembro de la familia Aplanar, preparado para pulir superficies hasta dejarlas como planos limpios. Es la misma herramienta que `Aplanar`, con otros valores por defecto de [Trazo](stroke.md): `Rastro`, `Filtro de normales por área` y `Filtro de profundidad` están activados.

El modo Sub es `Rellenar`, como en Aplanar.

Pulir tiene los mismos ajustes que [Aplanar](#flatten-settings): `Bloquear dirección del plano` y `Bloquear origen del plano`.

### ![](/icons/tool_crease.webp) Pliegue {#crease}
Las herramientas de pliegue son útiles para esculpir pequeños cortes o hendiduras.

El modo Sub es `Invertir`, y crea un pliegue en relieve.

#### Configuración de Pliegue {#crease-settings}

* `Factor de pellizco` - Cuánto se atraen los vértices de lado hacia el pincel. Con el pellizco a 1 y el desplazamiento a 0, la superficie no cambia de profundidad, solo de topología: las aristas se atraen hacia el trazo.
* `Factor de desplazamiento` - Cuánto se empujan o se tiran los vértices en profundidad. Con el pellizco a 0 y el desplazamiento a 1, se crean pliegues profundos o hendiduras en relieve, pero se ven dentados porque no se atrae suficiente geometría hacia el pliegue para definir con precisión sus lados o su fondo.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Pellizcar {#pinch}
Esta herramienta sirve para afilar aristas.

El modo Sub es `Invertir`, y separa los vértices.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Recortar {#trim}
La herramienta Recortar elimina un trozo de tu malla y ofrece opciones para tratar el hueco que queda. Usa los [Controles de selección](#selection-controls) para definir el recorte.

El modo Sub es `Voltear`, e invierte la forma, de modo que se elimina el otro lado.

::: tip
Como esta herramienta proyecta desde la cámara, recibirás un aviso si la cámara está en modo perspectiva.

En modo ortográfico, el corte a través de la malla es paralelo a la vista, que es lo que se suele esperar. Con una cámara en perspectiva, el corte se verá distinto en el lado lejano del objeto que en el cercano.
:::

#### Configuración de Recortar {#trim-settings}

Los ajustes están agrupados en `Relleno de agujero`:

* `Pintura de trazo` - Si la pintura está activada en el menú de pintura, la zona parcheada se rellena con el color seleccionado.
* `Booleano` - Rellena el agujero del recorte con una zona de quads. La zona rellenada queda plana.
* `Legado` - Rellena el agujero del recorte con una zona triangulada. La zona rellenada queda plana.
* `Rellenar` - Rellena el agujero con una zona triangulada. La zona rellenada es una superficie curva, como la película de una pompa de jabón.
* `Ninguno` - No rellena el agujero.

Con `Booleano`, la sección `Detalle` tiene:

* `Forma` - El tamaño aproximado de los quads y triángulos usados en el lado de la forma del recorte.
* `Agujeros` - El tamaño aproximado de los triángulos o polígonos usados en el agujero rellenado del recorte. El botón de enlace junto a `Detalle` lo mantiene sincronizado con `Forma`; desenlázalo para ajustarlo por separado.
* `Conservar topología` - No suaviza ni simplifica el borde del corte, y conserva la topología original de la malla cerca de las caras enmascaradas y ocultas.

Con `Legado`:

* `Detalle` - El tamaño aproximado de los triángulos usados en el recorte.
* `Suavidad del agujero` - Cuánto se relajan los triángulos en la zona rellenada.
* `Epsilon de umbral` - Un valor que puedes ajustar para mejorar el algoritmo de relleno de agujeros heredado.

Con `Rellenar`:

* `Detalle` - El tamaño aproximado de los triángulos usados en el recorte.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Dividir {#split}
Parecida a la herramienta [Recortar](#trim), salvo que, mientras Recortar descarta la selección, Dividir la conserva como un objeto nuevo.

El modo Sub es `Dividir`: cada trozo se conserva como su propio objeto, de modo que las formas que se solapan (por ejemplo con simetría) se cortan en piezas separadas en lugar de unirse en una sola.

#### Configuración de Dividir {#split-settings}

Dividir tiene los mismos ajustes de `Relleno de agujero` que [Recortar](#trim-settings): `Pintura de trazo`, los métodos `Booleano`, `Legado`, `Rellenar` y `Ninguno`, y sus opciones de `Detalle`.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Proyectar {#project}
La herramienta Proyectar se parece a la herramienta [Recortar](#trim), pero no borra ni crea geometría: solo mueve los vértices para que se ajusten a la selección.

![](/videos/tool_project.mp4)

::: tip
Si usas Proyectar dentro de una capa, puedes mezclar entre la forma original y la proyectada con el regulador de la capa.
:::

### ![](/icons/tool_layer.webp) Capa {#layer}
Eleva la superficie, pero limitando la altura.

Si mantienes el lápiz apoyado y sigues pasando por una zona, Capa sube hasta cierta altura y no pasa de ahí, mientras que otras herramientas siguen acumulando altura.

¡Ten en cuenta que, por defecto, el límite solo se aplica por trazo! Si empiezas un trazo nuevo, se construirá a partir de la nueva altura de la superficie.

Para fijar una altura máxima constante a lo largo de muchos trazos, usa la herramienta Capa con el sistema de [Capas](layers.md) de Nomad.

Crea una capa y usa esta herramienta. Ahora la altura máxima la define la capa, así que puedes dar muchos trazos y la altura será siempre la misma.

`Sub` usa una profundidad mínima y crea surcos.

#### Configuración de Capa {#layer-settings}

* `Usar datos de capa` - Si está activo y hay una capa seleccionada, usa los datos de la capa para fijar la altura máxima. Un aviso te lo recuerda cuando no hay ninguna capa seleccionada.
* `Inflar` - Si está activo, ajusta la dirección en la que trabaja Capa para obtener resultados más suaves.
* `Relajar (Normal)` - Con `Inflar` activado, la cantidad de suavizado aplicada a las normales.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_inflate.webp) Inflar {#inflate}
Mueve los vértices a lo largo de sus propias normales. `Sub` mueve los vértices a lo largo de su normal invertida.

#### Configuración de Inflar {#inflate-setings}
* `Relajar (Normal)` - La cantidad de suavizado aplicada a las normales.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Desplazar {#nudge}
Mueve o 'arrastra' los puntos en la dirección del trazo.

El modo Sub es `Pliegue`, y empuja un pliegue de material a lo largo del trazo: un bulto delante del pincel y un hundimiento detrás.

#### Configuración de Desplazar {#nudge-settings}
* `Suavizar` - Cuánto se suaviza la zona bajo el pincel mientras la desplazas, lo que mantiene limpia la superficie arrastrada.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Sello {#stamp}

Haz clic y arrastra para elevar una zona de la escultura con la forma del alfa seleccionado.

Es simplemente la [herramienta Brocha](#brush) con el tipo de trazo `Bloqueo + radio`. 

`Sub` hunde el sello en lugar de sacarlo de la superficie.

::: tip
Sello suele funcionar mejor con geometría de alta resolución. Si buscas en internet 'wrinkles alpha', 'pores alpha', 'scales alpha', etc., esas texturas alfa junto con Sello pueden ser una gran forma de añadir detalle orgánico a la escultura de un personaje.

Los dos modos de trazo sirven para cosas distintas. 

* `Bloqueo + radio` tiene una *altura* fija, y al arrastrar ajustas el ancho y la rotación del sello. Va bien para texturas de piel, que necesitan la misma profundidad/altura pero distintas rotaciones y escalas para disimular los patrones repetidos.
* `Bloqueo + intensidad` tiene un *ancho* fijo, y al arrastrar ajustas la rotación y la altura del sello. Va bien para remaches, que deben tener todos el mismo tamaño pero distintas rotaciones y alturas. 

:::

![](/videos/tool_stamp.mp4)

### ![](/icons/tool_vdm.webp) VDM {#vdm}

Estampa un mapa de desplazamiento vectorial (VDM). A diferencia de un alfa, que solo puede empujar la superficie hacia arriba o hacia abajo, un VDM guarda una forma 3d completa, así que puede estampar salientes como orejas, cuernos u hojas enroscadas. Funciona como [Sello](#stamp), con los mismos modos de trazo `Bloqueo + radio` y `Bloqueo + intensidad`.

`Sub` (`Invertir`) invierte la profundidad del sello, para hundirlo en la superficie como un molde.

El VDM se elige en el menú [Alfa](stroke.md#alpha), que también tiene un regulador de `Altura` para escalar solo la altura del sello, sin cambiar su desplazamiento lateral.

El botón `Crear` de la barra de herramientas de la izquierda te permite hacer tus propios sellos:

* `VDM nuevo...` - Añade un plano preparado para esculpir un VDM. Esculpe tu forma sobre él y luego hornéala con `Topología -> Hornear -> VDM`: Nomad añade el nuevo sello a la biblioteca de VDM y lo selecciona.
* `Capturar VDM` - (Experimental) Arrastra sobre la superficie de un modelo para tomar esa zona y convertirla en un sello VDM. `Tolerancia` aplana suavemente el borde de la captura.

::: tip
Evita DynTopo al esculpir un plano VDM: daña las UV del plano y deforma el sello. Mantén también la escultura lejos del borde del plano, o el sello mostrará un borde duro.
:::


### ![](/icons/tool_clearLayer.webp) Eliminar capa {#delete-layer}
Esta herramienta restablece las capas localmente; necesitas una capa activa o no pasará nada. Borra los datos esculpidos de la capa, y también su pintura cuando la pintura está activada.

El modo Sub es `Invertir`, y refuerza ligeramente la capa en lugar de borrarla.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tubo {#tube}
Crea un tubo dibujando una curva. 
![](/images/tool_tube_new.webp)

Una vez creado el tubo, puedes editar su trayectoria en el espacio 3d con controles parecidos a los de la [Edición de formas](#shape-editing) estándar y a las herramientas de edición de curvas. 

![](/videos/tool_tube.mp4)

#### Barra de herramientas izquierda de Tubo {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

La barra de herramientas de la izquierda tiene estas opciones:

* `Sincronizar` - Si el tubo actual está instanciado y hay nodos hijos del tubo que difieren entre las instancias, esto los vuelve a sincronizar.
* `Ajustar` - Si está activo, los modos curva y ruta se ajustan a otros objetos mientras dibujas. Si está inactivo, el primer punto se ajusta y el resto del tubo se dibuja a esa profundidad.
* `Desplazamiento` - Define la profundidad del ajuste: con 0 % el centro de la sección del tubo se ajusta a la superficie, los valores positivos lo elevan sobre la superficie y los negativos lo hunden. 100 % equivale al radio del tubo.
* `Vista` - Ningún modo de dibujo, para que puedas mover la cámara libremente.
* `Curva` - Dibuja un tubo a mano alzada. Tiene un pequeño menú desplegable:
    * `Editar` - Qué pasa cuando terminas el trazo (consulta [Controles de selección](#selection-controls)): crear el tubo al momento, mantener la curva editable con un círculo verde de validación al lado, o `Editar: mantener` al final del trazo para seguir editando.
    * `Cerrado` - Convierte el tubo en un bucle.
    * `Seguir dibujando` - Después de validar un tubo, te quedas en la herramienta para dibujar el siguiente.
    * `Precisión` - Cuántos puntos de curva se usan para convertir el trazo dibujado en un tubo. Con 0 % se usa el menor número de puntos, pero se pierden los pequeños cambios de curvatura del trazo. Con 100 % es muy preciso y se usan muchos puntos.
* `Ruta` - Crea un tubo tocando para definir los puntos de la curva. Pulsa el círculo verde para validar la ruta. Tiene un pequeño menú desplegable:
    * `B-spline` - Un método alternativo de dibujo de curvas en el que los puntos de control no suelen quedar sobre la curva, pero que puede dar resultados más suaves que el método por defecto.
    * `Cerrado` - Convierte el tubo en un bucle
    * `Pantalla` - Si está activo, la ruta queda 'clavada' a la pantalla, así que puedes mover la vista y el objeto y la ruta se queda en su sitio. Si está inactivo, la ruta forma parte de la escena 3d y se mueve con la cámara y los objetos.
* `Sección` - La curva se convierte en un anillo alrededor de la forma, cortado a través de sus dos puntos en la dirección desde la que mirabas.

##### Barra de herramientas superior de Tubo {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Cuando hay un tubo seleccionado, aparece en la parte superior de la vista una barra de herramientas con controles adicionales. Toca el título de la barra para plegarla o desplegarla, y la flecha de arriba a la derecha para llevarla a la parte superior o inferior de la vista.

* `Validar` - Convierte el tubo en polígonos normales para poder esculpirlo.
* `Editar` - Muestra los puntos de la curva para poder manipularlos
* `Espejo` - Añade un repetidor espejo como padre de esta curva
* `Ajustar` - Ajusta los puntos de la curva a las superficies cercanas
* `Cerrado` - Une el principio y el final de la curva para formar un bucle
* `B-spline` - Alterna entre la interpolación Catmull-Rom y B-spline.
* `Tapa` - Alterna entre tapas en los dos extremos del tubo, solo al principio o al final, o sin tapas.
* `Agujero` - Da grosor al tubo y lo convierte en una tubería. Alterna entre un agujero en los dos extremos, solo en el final, o sin agujeros. 
* `Radio` - Alterna entre un radio uniforme, un radio al principio y al final, o un radio por punto de curva. Se editan con los tiradores naranjas de la curva.
* `Torsión` - Alterna entre sin torsión, una torsión uniforme, una torsión al principio y al final, o una torsión por punto de curva. Se editan con los tiradores rosas de la curva.
* `Perfil` - Alterna entre sin perfil (es decir, un perfil circular), un perfil uniforme, un perfil al principio y al final, o un perfil por punto.
* `Editar perfil` - Muestra un editor de perfil. Funciona de forma parecida a las herramientas de [Edición de formas](#shape-editing), puede guardar y cargar perfiles predefinidos y tiene un interruptor para editar el perfil en el espacio 3d.
* `Espiral` - Abre un menú para añadir una torsión en espiral al tubo. Este menú tiene las opciones `Ángulo de torsión`, `Desplazamiento`, `Escala` y `Desfase angular`.
* `División X` - El número de divisiones alrededor del tubo; por ejemplo, 4 divisiones dan un tubo cuadrado. 
* `Densidad constante` - Si está activa, mantiene los polígonos cuadrados. Si está desactivada, puedes definir la `División Y` a lo largo del tubo.
* `...` - Menú de configuración del tubo.

#### Interruptor de borrado de puntos de curva {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Debajo de la barra de herramientas hay un interruptor de borrado de puntos de curva. Cuando arrastras un punto de curva cerca de otro, se pone rojo para indicar que, si lo sueltas, el punto se borrará. Si estás haciendo retoques pequeños y no quieres borrar puntos, este botón desactiva el borrado de puntos.



#### Configuración de Tubo {#tube-settings}
* `Primitivo` - Botones para activar o desactivar las UV, o para validar el tubo.
* `Postsubdivisión` - Un atajo para fijar el nivel de multiresolución antes de validar.
* `Subdivisión lineal` - Un atajo para fijar el nivel de subdivisión lineal antes de validar. 
* `División X` - Lo mismo que División X en la barra de herramientas.
* `División Y` - Lo mismo que División Y en la barra de herramientas.
* `Curva (Repetidor)` - Convierte el tubo en un [repetidor de curva](scene.md#curve)

::: tip
Con 4 divisiones y la postsubdivisión a 3 obtendrás tubos suaves con las puntas redondeadas, ideales para gusanos, serpientes o partes del cuerpo.
:::


### ![](/icons/tool_lathe.webp) Torno {#lathe}
Crea una superficie de revolución dibujando una curva.

Esta herramienta es ideal para formas como jarrones o copas de vino.

![](/videos/tool_lathe.mp4)

#### Barra de herramientas izquierda de Torno {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

La barra de herramientas de la izquierda tiene estas opciones:

* `Sincronizar` - Si el torno actual está instanciado y hay nodos hijos del torno que difieren entre las instancias, esto los vuelve a sincronizar.
* `Fijo` - Si está activado, el centro del torno queda fijo y se muestra en pantalla. Esta línea central tiene puntos de edición que puedes ajustar. Si está desactivado, el centro del torno se actualiza dinámicamente para coincidir con el principio y el final de la curva dibujada.
* `Vista` - Ningún modo de dibujo, para que puedas mover la cámara libremente.
* `Curva` - Dibuja el perfil del torno de un solo trazo. Tiene un pequeño menú desplegable:
    * `Editar` - Qué pasa cuando levantas el lápiz (consulta [Controles de selección](#selection-controls)): crear el torno al momento, mantener la curva editable con un círculo verde al lado para crear el torno, o `Editar: mantener` al final del trazo para seguir editando.
    * `Cerrado` - Une el principio y el final de la curva para formar un bucle
    * `Seguir dibujando` - Después de validar un torno, te quedas en la herramienta para dibujar el siguiente.
    * `Precisión` - Cuántos puntos de curva se usan para convertir el trazo dibujado en un tubo. Con 0 % se usa el menor número de puntos, pero se pierden los pequeños cambios de curvatura del trazo. Con 100 % es muy preciso y se usan muchos puntos.
* `Ruta` - Crea un torno tocando para definir los puntos de la curva. Pulsa el círculo verde para validar la ruta. Tiene un pequeño menú desplegable:
    * `B-spline` - Un método alternativo de dibujo de curvas en el que los puntos de control no suelen quedar sobre la curva, pero que puede dar resultados más suaves que el método por defecto.
    * `Cerrado` - Convierte el tubo en un bucle
    * `Pantalla` - Si está activo, la ruta queda 'clavada' a la pantalla, así que puedes mover la vista y el objeto y la ruta se queda en su sitio. Si está inactivo, la ruta forma parte de la escena 3d y se mueve con la cámara y los objetos.

#### Barra de herramientas superior de Torno {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Cuando hay un torno seleccionado, aparece en la parte superior de la vista una barra de herramientas con controles adicionales. Toca el título de la barra para plegarla o desplegarla, y la flecha de arriba a la derecha para llevarla a la parte superior o inferior de la vista.

* `Validar` - Convierte el torno en polígonos normales para poder esculpirlo.
* `Editar` - Muestra los puntos de la curva para poder manipularlos
* `Espejo` - Añade un repetidor espejo como padre de este torno
* `Ajustar` - Ajusta los puntos de la curva a las superficies cercanas
* `Estable` - Si está activado, el perfil de la curva se emparenta con la línea central del torno. Si está desactivado, puedes editar la línea central sin mover la curva, lo que permite formas más complejas.
* `Centrar` - Gira la vista para ver el perfil de la curva perfectamente de frente a la cámara.
* `Cerrado` - Une el principio y el final de la curva para formar un bucle
* `Tapa` - Si Cerrado está desactivado, alterna entre tapas en los dos extremos del tubo, solo al principio o al final, o sin tapas.
* `Agujero` - Da grosor al torno y lo convierte en una tubería. Alterna entre un agujero en los dos extremos, solo en el final, o sin agujeros. 
* `B-spline` - Alterna entre la interpolación Catmull-Rom y B-spline.
* `División X` - El número de divisiones alrededor del torno; por ejemplo, 4 divisiones dan un torno de perfil cuadrado. 
* `Densidad constante` - Si está activa, mantiene los polígonos cuadrados. Si está desactivada, puedes definir la `División Y` a lo largo del tubo.
* `...` - Menú de configuración del torno.

#### Configuración de Torno {#lathe-settings}
* `Primitivo` - Botones para activar o desactivar las UV, o para validar el tubo.
* `Postsubdivisión` - Un atajo para fijar el nivel de multiresolución antes de validar.
* `Subdivisión lineal` - Un atajo para fijar el nivel de subdivisión lineal antes de validar. 
* `División X` - Lo mismo que División X en la barra de herramientas.
* `División Y` - Lo mismo que División Y en la barra de herramientas.
* `Curva (Repetidor)` - Convierte el perfil de la curva en un [repetidor de curva](scene.md#curve)

### ![](/icons/tool_insert.webp) Insertar {#insert}
Coloca un objeto sobre la superficie de otro. Al usarlo se parece a la herramienta Sello, pero con formas 3d completas.

Si eliges un primitivo en la barra de herramientas de la izquierda, al hacer clic y arrastrar sobre cualquier superficie colocas un primitivo donde haces clic, y el arrastre define el tamaño. Cuando terminas de arrastrar, Insertar pasa al modo [Transformar](#transform).

En el modo Instancia, al arrastrar se crea una nueva instancia y se desliza sobre la superficie. El tamaño se copia de la primera forma; así puedes colocar muchas instancias del mismo tamaño de un objeto sobre otras superficies.

¡No tienes por qué insertar solo primitivos! Selecciona *cualquier* forma en la lista de la escena: si Insertar está en modo Instancia o Clonar, puedes arrastrar copias del objeto seleccionado sobre cualquier otra superficie.

Si un objeto tiene un pivote personalizado, se usará como punto de anclaje. Mira el vídeo de abajo.

La barra de herramientas de la izquierda también tiene `Vista`, para mover la cámara sin insertar nada, y `Sincronizar`: cuando el objeto de destino está instanciado, el nuevo objeto se añade también en todas las demás instancias.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transformar {#transform}
Mueve, rota o escala un modelo directamente con 1 y 2 dedos, normalmente sobre la superficie de otro objeto.

La barra de herramientas de la izquierda tiene estos botones:

* `Clonar` / `Instancia` - Hace una copia o una instancia del objeto; consulta la barra de herramientas del [Gizmo](#left-menu-toolbar).
* `Mover` - Al arrastrar con un dedo mueves el objeto. Con el ajuste activo, el objeto se desliza por la superficie que hay bajo tu dedo.
* `Rotar` - Al arrastrar con un dedo rotas el objeto. Con el ajuste activo, rota alrededor de la normal de la superficie que hay bajo tu dedo.
* `Escala` - Al arrastrar con un dedo escalas el objeto.

Una barra de herramientas en la parte superior de la vista tiene:

* `Objetivo` - Si la herramienta mueve el objeto, su grupo o sus vértices, igual que en el [Gizmo](#left-menu-toolbar).
* `Ajustar` - Ajusta el modelo sobre otras superficies.
* `Superficie` / `Vértice` - Con `Ajustar`, se ajusta a la superficie o al vértice más cercano.

Con Transformar puedes manejar 2 de estos modos rápidamente usando 2 dedos:

* Arrastra un objeto para colocarlo. Deja de mover el primer dedo, pero no lo levantes de la pantalla.
* Apoya el segundo dedo en la pantalla sin levantar el primero. Al arrastrar el segundo dedo, el objeto se escala.
* Levanta el segundo dedo y sigue arrastrando el primero: el objeto vuelve a estar en modo mover.

También puedes cambiar el segundo modo con un toque del segundo dedo:

* Arrastra el objeto para colocarlo, deja de moverlo, pero no levantes el dedo de la pantalla.
* Toca con el segundo dedo sin levantar el primero
* La herramienta pasa al modo rotación. Arrastra el primer dedo para ajustar la rotación.
* Toca con el segundo dedo como antes y la herramienta vuelve al modo mover.

Así tienes un flujo de trabajo rápido para clonar objetos sobre otro, por ejemplo rocas sobre un paisaje. Fíjate en que el botón de clonar también está en la barra de herramientas de la izquierda, a mano:

* Usa la herramienta Transformar para colocar una roca.
* Suelta y pulsa el botón de clonar
* Mueve esta roca y rótala o escálala si hace falta
* Suelta y pulsa el botón de clonar
* Mueve esta roca, y repite.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Esta herramienta te permite mover, rotar y escalar objetos, y modificar sus pivotes.

El manipulador de la vista tiene estas funciones:

* `Mover` - Arrastra la línea con flecha para mover en X/Y/Z. Arrastra el punto melocotón del centro del gizmo para trasladar libremente en el espacio de pantalla. Arrastra los cuadrados rojo, verde y azul para trasladar en los planos X/Y/Z.
* `Rotar` - Arrastra los círculos rojo, verde y azul para rotar en X/Y/Z. Arrastra la esfera dentro de los círculos para rotar libremente.
* `Escala` - Arrastra los puntos exteriores rojo, verde y azul para escalar en X/Y/Z. Arrastra los conos exteriores rojo, verde y azul para escalar en los planos X/Y/Z. Arrastra el círculo exterior melocotón para escalar de forma uniforme.

![](/images/tool_gizmo.webp)

#### Nodos y vértices {#nodes-and-vertices}

Todo objeto de Nomad está formado por un nodo y vértices:

* `Nodo` - El 'asa' del objeto, que guarda su traslación, rotación y escala, lo que se llama su matriz de transformación.
* `Vértices` - Los puntos que definen la superficie de un objeto; guardan la posición y la información de pintura.

Si tienes una caja sencilla formada por 8 vértices, puedes trasladarla modificando su matriz de transformación o modificando la posición de los vértices. Al esculpir, normalmente quieres modificar los vértices; al mover objetos con el gizmo, normalmente quieres modificar el nodo. Nomad te permite hacer las dos cosas. 

#### Barras de herramientas del Gizmo {#left-menu-toolbar}

La barra de herramientas de la izquierda tiene:

* `Clonar` - Hace una copia independiente del objeto actual, que puedes alejar arrastrándola con el gizmo.
* `Instancia` - Hace una copia instanciada del objeto actual. Los objetos están vinculados, así que lo que esculpas en uno aparecerá en todos los objetos instanciados.
* `Pivote` - (Icono de candado, en lugar del botón `Sub`) Si está activado, puedes mover y rotar el gizmo sin mover el objeto. Como `Sub`, mantenlo pulsado para un cambio rápido o tócalo para dejarlo activado.

Una barra de herramientas en la parte superior de la vista tiene el resto de controles:

* `Objetivo` - Define si el gizmo afecta al nodo o a los vértices de un objeto:
    * `Automático` - La opción por defecto: funciona como `Grupo`, pero si la malla tiene máscara o la simetría está activada, funciona como `Vértice`.
    * `Vértice` - Aplica la transformación a los vértices, teniendo en cuenta la máscara y la simetría. No funciona con primitivos sin validar, y las instancias también se ven afectadas.
    * `Objeto` - Mueve solo el objeto actual, ignorando la simetría y la máscara. Los objetos hijos se quedan quietos.
    * `Grupo` - Mueve el objeto y el resto de su jerarquía, ignorando la simetría y la máscara.
    * `Instancia` - (Objeto y Grupo) Lo mismo, pero todas las instancias del objeto se mueven con él.
* `Pivote` - Una ventana emergente para colocar el pivote rápidamente, explicada [más abajo](#pivot).
* `Todo` / `Mover` / `Rotar` / `Escala` - Muestra todos los manipuladores del gizmo, o solo los de mover, rotar o escalar.
* `Fijar` - Por defecto, el gizmo se coloca en el pivote del objeto seleccionado. Con Fijar activado, el gizmo se queda donde está.
* `Alinear` - Alterna entre alinear el pivote con el objeto actual o con el mundo.
* `Ajustar` (rotación) - Hace que los valores de rotación salten por incrementos; el valor de ajuste se muestra y se puede editar mientras el ajuste está activo. Su opción `Imán` hace que la rotación se pegue a un paso al cruzarlo y luego vuelva a moverse libremente; desactívala para saltar de paso en paso.
* `Ajustar` (traslación) - Hace que los valores de traslación salten por incrementos; el valor de ajuste se muestra y se puede editar mientras el ajuste está activo.

#### ![](/icons/reset.webp) Pivote {#pivot}
La ventana emergente `Pivote` de la barra superior permite cambiar el pivote rápidamente. La posición y la orientación del pivote controlan el gizmo.

**Restablecer** 
* `Auto` - Centro del objeto, alineado con su transformación.
* `Centrada` - Lleva el pivote al centro del objeto, conservando su orientación.
* `Inferior` - Lleva el pivote al centro inferior del objeto. Tócalo otra vez para usar la caja delimitadora del mundo.
* `Superior` - Lleva el pivote al centro superior del objeto. Tócalo otra vez para usar la caja delimitadora del mundo.
* `Objeto` - Lleva el pivote al origen del objeto, alineado con su transformación.
* `Máscara` - Lleva el pivote al centro de la zona sin enmascarar. Tócalo otra vez para pasar a la zona enmascarada.
* `Alinear` - Restablece las rotaciones para alinearlas con el mundo, conservando la posición.
* `Vista` - Alinea el pivote con la vista actual, conservando la posición. Después no sigue a la cámara.

**Pulsación única (modo Pivote)**

Solo está activo mientras `Pivote` está activado, y define qué pasa cuando tocas una vez la superficie de la malla:
* `Ninguno` - No hace nada al tocar el objeto
* `Normal` - Mueve y rota el pivote para alinearlo con el punto de la superficie que tocas
* `Primera` - Mueve (sin rotar) el pivote al punto de la superficie que tocas
* `Media` - Lleva el pivote al centro del objeto, bajo el punto de la superficie que tocas.

#### Configuración del Gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

* `Compacto` - Cambia la disposición del gizmo para poner los manipuladores adicionales fuera o dentro de la esfera de rotación
* `Tamaño del widget` - El tamaño del gizmo
* `Espesor` - El grosor de las líneas del gizmo
* `Opacidad` - La opacidad del gizmo
* `Ocultar en interacción` - Define si el gizmo se oculta temporalmente mientras lo arrastras

-----

* `Umbral de balanceo tangente` - Controla cómo se comporta la rotación al arrastrar los manipuladores circulares para rotar en X/Y/Z. Con un valor de 0, la rotación funciona como un dial: arrastras el gizmo en círculos. Con un valor de 90, funciona como tirar de la cuerda de un yoyó: arrastras en línea recta acercándote o alejándote del punto donde hiciste clic primero. Los valores entre 0 y 90 combinan ambos: por debajo del valor, movimiento lineal; por encima, movimiento circular.
* `Entrada numérica` - Si está activada, un solo toque en el gizmo abre una ventana para introducir un valor exacto en el eje tocado.

::: warning
¡Las herramientas [Gizmo](#gizmo) y [Transformar](#transform) usan su propia casilla de simetría, independiente de la simetría de escultura!

Por defecto, esta simetría está desactivada.
:::

##### Matriz {#matrix}
Los valores exactos de transformación del objeto ya no están en la configuración del Gizmo: se han trasladado al menú `Transformar`, en el menú de arriba a la derecha. Su sección `Matriz` tiene:

* ![](/icons/target.webp) `Mover origen` - Mueve el objeto para que su pivote quede en el centro de la escena, lo que se llama el origen.
* ![](/icons/bake.webp)  `Hornear` - Congela el objeto donde está y pone los valores de traslación y rotación a 0 y la escala a 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Pivote` - Hornea el pivote: hace que los valores de la matriz correspondan a la posición del manipulador del gizmo en el mundo.
* ![](/icons/reset.webp) `Restablecer` - Un atajo que pone los valores de traslación a 0, los de rotación a 0 y la escala a 1, moviendo y rotando el objeto.

::: tip Hornear frente a hornear el pivote
Crea una caja, elige la herramienta Gizmo, y abre y fija el menú `Transformar`. Por defecto, la traslación y la rotación están a 0 y la escala a 1.

Activa el modo pivote, mueve el manipulador hacia un lado y desactiva el modo pivote. El pivote ha cambiado, pero fíjate en que los valores de traslación siguen a 0. 

Si quieres ver dónde está *realmente* el pivote, pulsa el botón de hornear `Pivote`. Ahora los valores de traslación se actualizan. Fíjate en que la caja no se mueve durante esta operación, ni en el modo pivote.

Mueve y rota la caja a otro sitio y luego pulsa `Mover origen`. El objeto se mueve para que su pivote quede en el centro del mundo, pero la rotación no cambia.

Pulsa `Restablecer` y la rotación también se pondrá a 0.

Vuelve a mover y rotar la caja, y esta vez pulsa `Hornear`. El pivote se queda donde está, la caja se queda donde está, pero los valores de traslación y rotación se ponen a 0.

¡Practícalo unas cuantas veces! Entiende que los valores del pivote están ocultos y que Nomad se encarga de ellos por ti, pero si necesitas colocar el pivote en posiciones reales del espacio, hornear el pivote lo hace por ti.

:::

* `Traslación` - Los valores de traslación X, Y, Z
* `Rotación` - Los valores de rotación X, Y, Z
* `Escala` - La escala uniforme si está activada, o la escala X, Y, Z si está desactivada.
* `Cizallamiento` - Los valores de cizallamiento X, Y, Z; solo se muestran cuando el objeto ya está cizallado
* `Escala uniforme` - Alterna entre escalar de forma uniforme o de forma independiente en cada eje

A la izquierda puedes mover el pivote del gizmo; puedes verlo en acción en el vídeo de abajo.
Es especialmente útil para la rotación, ya que no cambia nada para la traslación.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Grupo de caras {#facegroup}

Los grupos de caras te permiten organizar tu objeto en caras de distintos colores. Puedes usar estos grupos de muchas formas en Nomad:

* Un método rápido de selección para las máscaras
* Ocultar o mostrar partes de tu objeto
* Organizar tu objeto sin tener que dividirlo en piezas separadas
* Definir regiones UV
* Guiar al remallado de quads
* Un control adicional para herramientas como Suavizar.

#### Barra de herramientas izquierda de Grupo de caras {#facegroup-left-toolbar}

* `Grupo` - El botón muestra el grupo de caras actual. Tócalo para ver los grupos de caras disponibles como muestras y elegir uno. Toca una muestra para cambiarle el nombre o el color, o para borrarla. `Eliminar no utilizados` borra las muestras que no se usan y `Restablecer` las borra todas. El icono del más te permite crear muestras nuevas.
* `Punto` - Pinta sobre el objeto para definir grupos de caras. Si '+ Grupo de caras' está activado, cada trazo nuevo crea automáticamente un grupo de caras nuevo, algo útil para definir regiones rápidamente. Un toque rellena la región seleccionada. El regulador define el radio del punto.
* `Relajar` - Suaviza los bordes de los grupos de caras. Muy útil para definir bordes limpios para el remallado de quads, o para definir paneles en el modelado de superficies duras. Los reguladores controlan el radio y la intensidad del relajado.
* Formas - Crea grupos de caras con formas en lugar de un pincel, mediante `Bloqueo + radio`, `Lazo`, `Polígono`, `Línea`, `Rect` y `Elipse`. Consulta [Controles de selección](#selection-controls) para saber más.
* `Elegir` - El modo Sub. Si está activado, toma la muestra de la zona donde empieza el trazo y la aplica durante el resto del trazo. Muy útil para ordenar las regiones de grupos de caras: si un grupo de caras se ha extendido demasiado, activa `Elegir`, empieza un trazo desde donde la muestra del grupo de caras es correcta y arrastra hasta el borde para reasignar la muestra correcta.

#### Barra de herramientas superior de Grupo de caras {#facegroup-top-toolbar}

Una barra de herramientas en la parte superior de la vista tiene controles adicionales:

* `Relajar (Todo)` - Arrastra para relajar a la vez los bordes de todos los grupos de caras.
* `Frontal` / `Visible` / `Conectada` - Los mismos filtros de trazo que en la barra de [Máscara](#mask).
* `Desde normales` - Crea grupos de caras según el ángulo entre caras. La ventana emergente tiene el `Ángulo` y te permite omitir los grupos pequeños según su `Recuento de caras` o su `Área de superficie`, con una `Vista previa` antes de validar.
* `Desde partes` - Crea un grupo de caras por cada parte desconectada.
* `Desde UV` - Crea un grupo de caras por cada isla UV.
* `Desde máscara` - Crea un grupo de caras a partir de la zona enmascarada.
* `Pulsación única` - Elige qué hace un toque sobre un grupo de caras: rellenarlo con el grupo de caras actual, ocultarlo, enmascararlo o ponerlo en `Pose` (el grupo tocado y lo que hay más allá quedan sin máscara, y el gizmo se coloca en la articulación, con un regulador `Desenfocar` para la máscara). Un segundo interruptor `Pulsación única`, disponible cuando la malla tiene máscara, limita el toque a las caras del mismo lado de la máscara.
* Botones `Borrar` de las herramientas [Ocultar](#hide) y [Máscara](#mask), para mostrar todo de nuevo o borrar la máscara sin salir de la herramienta.

#### Configuración de Grupo de caras {#facegroup-settings}

El menú `Herramienta` extrae grupos de caras a objetos nuevos, con las mismas opciones que `Extraer` en la [configuración de Máscara](#mask-settings). El botón `Grupo de caras` de arriba elige qué grupos se extraen, y hay un regulador `Separación` adicional: desplaza cada borde hacia dentro a lo largo de la superficie, y un valor negativo lo desplaza hacia fuera para que se solapen. Para paneles vecinos, usa la mitad de la separación deseada.

### ![](/icons/tool_hide.webp) Ocultar {#hide}
Oculta o aísla partes del objeto. 

Los modos principales se controlan desde el menú de la izquierda:

* `Punto` - Pinta sobre el objeto para ocultar partes de él.
* Formas - Oculta con formas en lugar de un pincel, mediante `Lazo`, `Polígono`, `Línea`, `Rect` y `Elipse`. Consulta [Controles de selección](#selection-controls) para saber más.
* `Mostrar` - El modo Sub: invierte la operación, de modo que el modo seleccionado muestra partes del objeto en lugar de ocultarlas.

En la parte superior de la vista aparece una barra de herramientas con controles adicionales:

* `Limpiar todo` - Restaura los objetos: todas las partes ocultas vuelven a mostrarse. Cuando otros objetos también tienen partes ocultas, un botón `Borrar` adicional solo restaura los objetos seleccionados.
* `Invertir` - Intercambia las partes ocultas y las visibles.
* `Eliminar` - Elimina la parte oculta del objeto
* `Dividir` - Separa la parte oculta del objeto en una forma nueva.
* `Frontal` / `Visible` / `Conectada` - Los mismos filtros de trazo que en la barra de [Máscara](#mask).
* `Pulsación única` (grupo de caras) - Usa los grupos de caras para ocultar partes rápidamente: tocar un grupo de caras lo oculta entero.
* `Pulsación única` (máscara) - Si hay una máscara activa, al tocar se oculta la parte enmascarada.

### ![](/icons/tool_measure.webp) Medir {#measure}
Arrastra para medir la distancia entre 2 puntos. Una vez colocados, puedes arrastrar los extremos para ajustar la medida.

La barra de herramientas de la izquierda elige cómo se mide la distancia:

* `Línea` - Una línea recta entre los dos puntos.
* `Superficie` - La distancia a lo largo de la superficie, siguiendo el corte que pasa por los dos puntos visto desde la cámara.
* `Sección` - El perímetro de la sección que pasa por los dos puntos, como una cinta métrica alrededor de un brazo.
* `Vértice` - Ajusta los extremos al vértice más cercano.
* `Proporción áurea` - Muestra un punto amarillo en el punto de la proporción áurea de la medida.
* El botón `?` muestra el volumen, el área de superficie y el tamaño de los objetos seleccionados.

### ![](/icons/tool_arrange.webp) Organizar {#arrange}
Alinea y distribuye varios objetos a la vez, como las herramientas de alineación de una aplicación de diseño 2d. Selecciona primero los objetos; con un solo objeto, Organizar trabaja en cambio sobre sus partes separadas. Se dibuja una caja alrededor de la selección: arrastra sus tiradores para escalarla.

Una barra de herramientas en la parte superior de la vista tiene los controles:

* `Mundo` / `Pantalla` - Organiza según los ejes del mundo, o según la pantalla (izquierda, derecha, arriba, abajo).
* `Alinear` - Alinea los objetos por su mínimo, su centro o su máximo, en cada eje.
* `Distribuir` - Reparte los objetos de forma uniforme entre los dos de los extremos, según su mínimo, su centro o su máximo. Necesita al menos 3 objetos.
* `Línea` - Coloca los objetos en fila a lo largo de un eje.
* `Cuadrícula` - Coloca los objetos en una cuadrícula, con un número de objetos en `X`, `Y` y `Z`.
* `Círculo` - (Solo Mundo) Coloca los objetos en círculo alrededor del eje `X`, `Y` o `Z`.
* `Esfera` - (Solo Mundo) Coloca los objetos sobre una esfera.

`Línea`, `Cuadrícula`, `Círculo` y `Esfera` tienen todos un regulador de `Espaciado` para la separación entre los objetos.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Esta herramienta convierte el objeto seleccionado en una topología limpia de quads, con controles de densidad, flujo de aristas y simetría. 

::: tip
Quad Remesher lo desarrolla [Exoside](https://exoside.com/) para iOS y escritorio. 

En iOS es una compra dentro de la app de Nomad, un pago único de 16 USD.

En escritorio, compra una licencia en [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Puedes comprarla solo para Nomad de escritorio, o una licencia cruzada para todas las aplicaciones de escritorio compatibles.

Si ya tienes Quad Remesher para otra aplicación de escritorio, puedes [comprar una actualización a todas las plataformas por menos dinero.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher no está disponible en Android. En Android puedes usar los remalladores libres y de código abierto de la pestaña de topología [Remallado de cuadrángulos](topology.md#quad-remesh) (AutoRemesher, Instant Mesh, QuadriFlow), pero ten en cuenta que sus funciones son más limitadas.
:::

Mientras Quad Remesher no esté desbloqueado, la barra de herramientas superior empieza con un botón de carrito en lugar de los botones de remallado. En iOS abre la compra dentro de la app. En escritorio muestra `Desbloquear (comprar, restaurar, prueba)`, que comprueba tu licencia de Exoside (o inicia la prueba). Una vez activo, se habilitan las barras de herramientas izquierda y superior.

* `Punto` - Este pincel define la densidad objetivo. Con la intensidad al 100 % pinta en rojo, lo que usa el doble de la densidad de quads objetivo en esas zonas. Con la intensidad al 0 % pinta en cian, lo que usa la mitad de la densidad de quads objetivo en esas zonas. Con la intensidad al 50 % pinta en gris, lo que usa la densidad de quads objetivo por defecto.
* `Suavizar` - Suaviza las transiciones de densidad entre rojo, gris y cian.
* `Difuminar` - Difumina la pintura de densidad.
* `Curva` - Dibuja curvas sobre la superficie de la escultura; Quad Remesher las usa como guías para el flujo de aristas. Toca una curva para borrarla.
* `Ruta` - Dibuja rutas sobre la superficie de la escultura; Quad Remesher las usa como guías para el flujo de aristas. Toca una ruta para borrarla. 
* `Rect` - Dibuja rectángulos sobre la superficie de la escultura; Quad Remesher los usa como guías para el flujo de aristas. Toca uno para borrarlo.
* `Elipse` - Dibuja elipses sobre la superficie de la escultura; Quad Remesher las usa como guías para el flujo de aristas. Toca una para borrarla.

#### Barra de herramientas superior de Quad Remesher {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

En la parte superior de la vista aparece una barra de herramientas con controles adicionales:


* `<Número>` - Pulsa aquí para iniciar el remallado de quads; este número indica cuántos quads tendrá el remallado como objetivo.
* `Quads` - Define el número de quads objetivo deslizando a izquierda y derecha, o toca para introducir un número exacto. Ten en cuenta que es más una guía que un número fijo: los distintos controles de Quad Remesher harán a menudo que el resultado no coincida exactamente con este objetivo.
* `Mitad` - Un atajo para fijar el objetivo en la mitad del número actual de polígonos.
* `Mismo` - Un atajo para fijar el objetivo en el número actual de polígonos.
* `Guías` - Activa o desactiva el uso de las guías. Cuando hay guías, un segundo botón `Guías` muestra su número; tócalo para borrarlas todas.
* `Densidad` - Activa o desactiva el uso de la pintura de densidad. Cuando hay pintura de densidad, un segundo botón `Densidad` la elimina.
* `Grupo de caras` - Activa o desactiva el uso de los grupos de caras para guiar a Quad Remesher.
* `Relajar` - Activa o desactiva el relajado automático de los bordes de los grupos de caras durante el remallado. Si ya has relajado o suavizado los bordes de tus grupos de caras, desactiva esta opción.
* `Regulador Relajar` - Un regulador de acceso directo para relajar los bordes de los grupos de caras.
* `Bordes duros` - Actívalo para intentar conservar las aristas vivas.
* `Reproyectar vértice` - Actívalo para reproyectar la nueva topología sobre la malla de entrada.
* `Sim` - Actívalo para obtener un resultado simétrico. Ten en cuenta que la simetría siempre se calcula respecto al eje X del mundo, así que asegúrate de que tu modelo está en el origen si esperas un resultado simétrico.
* `...` - Ventana emergente de configuración de Quad Remesher. 

#### Menú de configuración de Quad Remesher {#quad-remesher-settings-menu}

El botón `...` al final de la barra superior abre una ventana emergente con el resto de ajustes:

* `Cantidad adaptativa de quads` - Actívalo para usar quads más pequeños en las zonas de mucha curvatura y más grandes en las de poca curvatura.
* `Tamaño adaptativo` - Define el grado de adaptación. Con 100 % la adaptación de tamaño es máxima; con 0 % los quads son uniformes.

::: tip

Una receta para conseguir un buen remallado de quads con pocos artefactos:

* Crea grupos de caras en la malla para definir tu flujo de quads ideal.
* Relaja los grupos de caras para obtener bordes suaves entre ellos.
* Diezma. Así te aseguras de que no queden caras finas o deformadas en los bordes de los grupos de caras. En los ajustes de Diezmar, asegúrate de que el grupo de caras está activado. Así las aristas de los triángulos seguirán con precisión los bordes de tus grupos de caras. 

En las opciones del remallado de quads, asegúrate de que Relajar está desactivado (ya has relajado la malla) y deberías obtener buenos resultados.

:::

### ![](/icons/tool_select.webp) Seleccionar {#select}
Usa los modos de forma (`Lazo`, `Rect`, `Elipse`) para seleccionar objetos de la escena. `Deseleccionar` quita objetos de la selección.

### ![](/icons/tool_lattice.webp) Enrejado {#lattice}
Deforma un objeto con una jaula de puntos de control a su alrededor, en lugar de esculpir su superficie. Al mover unos pocos puntos de la jaula, todo el objeto se dobla, se retuerce o se estira de forma suave; ideal para ajustar proporciones o posar sin tocar la topología. La deformación sigue activa hasta que la validas.

La barra de herramientas de la izquierda elige cómo editas la jaula:

* `Puntos` - Arrastra directamente los puntos y las aristas de la jaula. Toca un punto para seleccionarlo.
* `Vista` - Mueve la cámara sin editar la jaula.
* `Relajar` - Un pincel que relaja los puntos de la jaula que tiene debajo.
* `Elástico` - Un pincel que tira de los puntos de la jaula con una atenuación elástica, como la herramienta [Elástico](#elastic).
* `Gizmo` - Mueve, rota y escala los puntos seleccionados con el gizmo. Su modo Sub es `Pivote`.
* `Lazo` - Selecciona puntos de la jaula con un lazo; `Deseleccionar` los quita de la selección.

La ventana emergente de formas también tiene `Radio suave`, que hace que al arrastrar un punto se muevan también los puntos vecinos (en celdas de la retícula; 0 mueve solo la selección), e `Invertir selección`.

Una barra de herramientas en la parte superior de la vista tiene:

* `Validar` - Aplica la deformación al objeto y quita la jaula.
* `Restablecer` - Quita la jaula y su deformación.
* `Opacidad` - La opacidad con la que se muestra la jaula.
* `Lado del espejo` - Con simetría, alterna qué lado del espejo de la jaula se muestra y se puede elegir, con su propia `Opacidad` para el lado oculto.
* `Puntos de la retícula` - Qué puntos de la jaula se pueden mover: la retícula completa, la superficie y el punto central, o solo la superficie.
* `Rigidez` - Lo rígida que es la deformación, de suave (0 %) a rígida y lineal (100 %).
* `Atenuación` - Hasta dónde se atenúa la deformación fuera de la jaula.
* `Alinear` - Alinea la jaula con el objeto o con el mundo.
* `X`, `Y`, `Z` `División` - El número de celdas de la jaula en cada eje. El botón de modo que tienen al lado define cómo se relacionan: `x = y = z` usa el mismo número en los 3 ejes, `Uniforme` mantiene la misma separación entre puntos en todos los ejes, y `Personalizado` te permite ajustar cada eje libremente.

#### Configuración de Enrejado {#lattice-settings}
* `Velocidad de giro` - Las mismas opciones de giro que la herramienta [Mover](#move-settings), usadas al arrastrar los puntos de la jaula.

### ![](/icons/tool_view.webp) Vista {#view}
Esta "herramienta" no hace nada en particular: es simplemente una forma de ver el modelo sin modificar la escena.

#### Configuración de Vista {#view-settings}
Mientras la herramienta Vista está activa, estos ajustes sustituyen algunas opciones de visualización, para que tengas una vista limpia al presentar o revisar tu modelo:

* `Primitivo (Editar)`, `Repetidor (Editar)`, `Luz (Editar)`, `Cámara (Editar)` - Permiten editar primitivos, repetidores, luces y cámaras en la vista mientras estás en la herramienta Vista. Desactívalos para no mover sus manipuladores sin querer.
* `Acceso directo a la cámara (siempre)` - Muestra siempre los botones de acceso directo a la cámara en la vista.
* `Mostrar máscara`, `Contorno`, `Oscurecer mallas no seleccionadas` - Muestra la máscara, el contorno de los objetos seleccionados u oscurece los objetos no seleccionados. `Automático` sigue tu ajuste habitual; `No` y `Sí` lo fuerzan.
* `Mostrar línea (Simetría)`, `Mostrar plano (Simetría)` - Muestra la línea o el plano de simetría, con las mismas opciones `Automático`, `No` y `Sí`.
* `Icono` - Muestra en la vista los iconos de los grupos, repetidores, luces, cámaras y la jerarquía, con las mismas opciones.


## Menú contextual de la caja de herramientas {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Un clic derecho o una pulsación larga sobre una herramienta de la caja de herramientas abre un menú contextual. Este menú tiene estas opciones:

* `Guardar` - Guarda los cambios que hayas hecho en la herramienta
* `Clonar` - Duplica la herramienta en un nuevo acceso directo de herramienta
* `Último guardado` - Vuelve a la versión guardada anteriormente de la herramienta
* `Icono` - Cambia el icono de la herramienta. Cuando la herramienta tiene un icono personalizado, este botón lo quita.
* `→ ...` - Mueve la herramienta a otra carpeta de la caja de herramientas, o a una nueva
* `Restablecer` - Restablece la herramienta a sus valores por defecto

Las herramientas clonadas también tienen `Renombrar` y `Eliminar`.
