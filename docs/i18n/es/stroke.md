# ![](/icons/brush.webp) Trazo {#stroke}

---
![](/images/stroke_overview.webp) 

## Descripción general {#overview}

Puedes personalizar el comportamiento del trazo de la mayoría de los pinceles de las herramientas.
Los ajustes se parecen a los de las aplicaciones de pintura 2d, aunque algunas opciones son propias del esculpido y del 3d.

Las opciones se reparten en 5 submenús:

| Nombre   | Icono                        | Descripción                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Trazo    | ![](/icons/brush.webp)      | Controla cómo se aplica el trazo sobre el modelo                   |
| Alfa     | ![](/icons/alpha.webp)      | Cómo se usa una textura en escala de grises para la estampa del pincel |
| Disminución | ![](/icons/falloff.webp) | Controla cómo cambia la fuerza del pincel del centro al borde      |
| Filtro   | ![](/icons/filter.webp)     | Cómo afecta la geometría del modelo al pincel                      |
| Presión  | ![](/icons/pressure.webp)   | Controla la respuesta a la presión del lápiz                       |

::: tip
No todas las opciones de trazo se aplican a todas las herramientas. Las que la herramienta actual no usa aparecen desactivadas u ocultas. 
:::


## ![](/icons/brush.webp) Trazo {#stroke-1}

### ![](/icons/radius.webp) Radio {#radius}

![](/images/stroke_radius.webp)

Las opciones de radio son ajustes globales: se aplican a todas las herramientas.

#### Espacio {#size}

* `Pantalla` - el radio se mide en unidades de pantalla. Si le das un radio de 100 píxeles, seguirá midiendo 100 píxeles tanto si acercas como si alejas la vista.
* `Mundo (3D)` - el radio se mide en unidades 3d. Por ejemplo, si creas una esfera y le das al radio el mismo tamaño que la esfera, el radio seguirá teniendo el tamaño de la esfera aunque acerques o alejes la vista.

#### ![](/icons/link.webp) Sincronizar atajo {#sync-shortcut}

Si está activado, el radio y los ajustes de silueta se mantienen sincronizados al cambiar a los pinceles de atajo (`Suavizar`, `Máscara` u `Ocultar`). Así, una pasada rápida de suavizado o de máscara usa el mismo tamaño de pincel que la herramienta con la que estabas trabajando.

#### ![](/icons/link.webp) Compartir radio {#share-radius}

Si está activado, todas las herramientas usan el mismo radio. Por defecto, cada herramienta tiene su propio radio.


### Tipo de trazo {#stroke-type}

![](/images/stroke_strokemode.webp)

Los trazos pueden funcionar de varios modos:

### ![](/icons/stroke_dot.webp) Punto {#dot}
Arrastra como en un trazo de pintura normal. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Rodar {#roll}
El alfa del pincel gira para seguir la dirección del trazo, algo muy útil para hacer costuras en tela. 
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Bloqueo + radio {#lock-radius}
Estampa un trazo con una **_altura_** fija. Al arrastrar ajustas la escala y la rotación.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Bloqueo + intensidad {#lock-intensity}
Estampa un trazo con un **_radio_** fijo. Al arrastrar ajustas la altura y la rotación.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
Los modos `Bloqueo + radio` y `Bloqueo + intensidad` ignoran los ajustes de [Presión](#pressure), ya que el propio arrastre fija el tamaño y la fuerza.
:::

![](/images/stroke_strokemodemove.webp)

Las herramientas `Mover` y `Arrastrar` tienen sus propias 3 opciones:

### ![](/icons/snake.webp) Arrastrar {#drag}

Actualiza continuamente lo que queda dentro del radio del pincel durante el trazo. Un trazo rápido deja atrás la superficie, mientras que uno lento sujeta el material y crea formas más alargadas. Es el modo por defecto de la herramienta `Arrastrar`. Con la `Topología dinámica` sirve para hacer extrusiones en forma de serpiente. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Agarre {#grab}
Selecciona lo que queda dentro del radio del pincel al empezar el trazo y conserva esa selección. Es útil para movimientos más precisos, ya que puedes ajustar con cuidado la distancia del desplazamiento sin mover por accidente más de lo que habías seleccionado. Es el modo por defecto de la herramienta `Mover`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Bloqueo + radio (arrastre) {#lock-radius-drag}
Se ignora el radio que hayas elegido: se ajusta sobre la marcha según lo lejos que arrastres el trazo desde el punto de partida. Poca distancia = radio pequeño, más distancia = radio más grande. Usa el regulador de intensidad para controlar la forma de la atenuación. Muy útil para encajar formas orgánicas y gomosas.
![](/videos/stroke_lockradius_drag.mp4) 

Otras herramientas muestran aquí sus propios tipos de trazo, por ejemplo `Relajar`, `Suavizar` y `Difuminar` para las herramientas de suavizado, o formas como `Lazo` y `Curva` para las herramientas basadas en selección. Se describen con cada [herramienta](tools.md).


### Ajustar intensidad por espaciado {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Los trazos con un espaciado bajo (menos del 50 %) se acumulan rápido y resultan más intensos que con valores de espaciado más altos. Esta opción lo compensa, de modo que los trazos tienen más o menos la misma intensidad sea cual sea el espaciado.

### Espaciado de trazos {#stroke-spacing}
La distancia entre cada estampa del pincel mientras arrastras. Los valores por debajo del 100 % se solapan y dan la apariencia de un trazo continuo. Los valores por encima del 100 % empiezan a dejar huecos, algo útil para esculpir detalles como costuras o cremalleras.

### Estabilidad del trazo {#lazy-rope-stabilizer}
El trazo sigue al puntero con un cierto retraso de distancia. Sirve para dibujar líneas suaves.
![](/videos/stroke_lazy_rope.mp4) 

### Suavidad del trazo {#stroke-smoothing}
Promedia varias posiciones del puntero para obtener un trazo más suave.
Con valores altos, el trazo se queda por detrás del puntero, pero acaba alcanzándolo.
Es útil para dibujar líneas suaves.

### Radio de ajuste {#snap-radius}
Une el trazo al anterior cuando el puntero empieza cerca de donde terminó el último trazo. El radio indica a qué distancia se busca el final del trazo anterior. Resulta útil para dibujar líneas largas y continuas haciendo pausas frecuentes.

### ![](/icons/trail.webp) Rastro {#trail}

Si está activado, cada nueva estampa vuelve a aplicar también los puntos más recientes del trazo que quedan detrás. `Recuento de rastros` fija cuántos puntos se vuelven a aplicar, `Intensidad del rastro` su fuerza y `Radio del rastro` cuánto más grandes se hacen.

El rastro solo funciona con el tipo de trazo `Punto`, y no con la [influencia de la atenuación](#influence) `Cresta`.

### ![](/icons/silhouette.webp) Silueta {#silhouette}
![](/images/stroke_silhouette.webp)
Por defecto, los trazos solo afectan a la superficie del modelo que queda dentro del radio del pincel. Con la silueta activada, el trazo se proyecta a través de todo el modelo. Es muy útil para el encaje inicial de un modelo, o para formas cuyos lados deben quedar perpendiculares.

Puedes elegir la dirección de proyección:

* `X`, `Y`, `Z` - proyecta a lo largo de un eje fijo.
* `Vista` - proyecta en la dirección de la cámara.
* `Si está fijado` - proyecta en la dirección de la cámara, pero solo mientras la cámara está fijada a una vista. Si no, el trazo es un trazo normal.
* `Más cercano` - proyecta a lo largo del eje más cercano a la dirección de la cámara. Es la opción por defecto.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Aleatorizar {#randomize}

![](/images/stroke_randomize.webp)

La `Intensidad`, el `Desplazamiento`, la `Rotación` y la `Escala` del trazo se pueden aleatorizar por separado. Usa la casilla de cada fila para activarla o desactivarla. Con esto se consiguen muchos efectos: por ejemplo, aleatorizar con la herramienta de pintura crea un color moteado, y aleatorizar con la herramienta de pliegue sirve para crear detalles de piel.

`Período (más lento)` fija la duración del ciclo aleatorio: auméntalo para variaciones lentas y suaves, redúcelo para un ruido rápido. El botoncito junto a cada fila escala el período solo para esa fila.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Aleatorizar - HSV {#randomize-hsv}

En las herramientas que pintan, también se pueden aleatorizar el `Matiz`, la `Saturación` y el `Valor` del color de pintura, con su propio período. Ideal para añadir variaciones de color sutiles a la piel o la piedra.

### Desplazamiento de trazo {#stroke-offset}

Aplica un desplazamiento constante al trazo para que el dedo no lo tape. Es útil en pantallas pequeñas. Es un ajuste global: actívalo con su casilla y se aplica a todas las herramientas.


## ![](/icons/alpha.webp) Alfa {#alpha}
![](/images/stroke_alpha.webp) 

El `Alfa` es una textura que modula el comportamiento del pincel.
Es una imagen en escala de grises, en la que los píxeles negros significan ninguna deformación y los blancos, deformación completa.

Toca la imagen del alfa para cambiarla. Además de los alfas incluidos y los que importes tú, la lista de alfas también puede descargar mapas de desplazamiento de Poly Haven.

Toca la vista previa del material para cargar un alfa desde un preajuste de material. Aquí también puedes guardar preajustes de material y elegir si incrustar las texturas con la herramienta.

::: tip
La textura nunca se redimensiona, así que las texturas grandes pueden ralentizar el rendimiento.
:::

### ![](/icons/blend_contrast.webp) Corregir alfa {#invert-pixels}
El botón `Corregir...` de un alfa importado abre una ventana que corrige la propia imagen: su valor medio, la inversión de los píxeles (el negro pasa a blanco y el blanco a negro), una rotación de 90° y un volteo horizontal o vertical. El archivo de imagen se reescribe, así que las demás aplicaciones también ven la imagen corregida.

::: tip

Los alfas incluidos con Nomad no se pueden corregir.

:::

### Proyección {#projection}

Cómo se proyecta el alfa sobre el modelo:

* `Superficie` - el alfa se apoya en la superficie bajo el pincel y sigue su orientación.
* `Pantalla` - el alfa se proyecta directamente desde la vista.
* `Mosaico` - el alfa se proyecta desde la vista y se queda fijo mientras pintas encima, como una plantilla, de modo que un patrón repetido encaja sin costuras. La rotación queda bloqueada y la presión del lápiz no cambia el tamaño del patrón.
* `Triplanar` - el alfa se proyecta a lo largo de los 3 ejes. Las opciones de escala, rotación y mosaico de abajo se sustituyen por los ajustes de textura triplanar.

### ![](/icons/diagonal.webp) Escala {#scaling}

En Nomad, el pincel es un círculo con el radio que tú elijas. Las texturas suelen ser cuadradas o rectangulares, y los parámetros de `Escala` te permiten decidir cómo encaja la textura dentro del círculo. Para una textura cuadrada, un valor de 0,7 la hace caber dentro del círculo. Un valor de 1 agranda la textura para que sea el círculo el que quepa dentro, recortando los bordes.

![](/images/alpha_scaling.webp) 

Al activar `Escala Y` puedes estirar el alfa en vertical. El primer regulador pasa entonces a ser `Escala X`.

![](/images/alpha_scaling_y.webp) 

`Voltear horizontalmente` refleja el alfa de izquierda a derecha.

### Rotación {#rotation}

La textura del alfa gira para seguir la dirección del trazo. Puedes añadir un desfase de rotación y, si el icono del candado está activado, la textura se queda bloqueada en esa rotación respecto a la pantalla.

El botón del lápiz que hay al lado gira el alfa cuando haces rodar el lápiz sobre sí mismo (barrel roll), con los trazos `Bloqueo + radio` y `Bloqueo + intensidad` mientras la rotación está desbloqueada. Solo funciona con lápices que lo admitan.

### Mosaico {#tiling}
![](/images/stroke_tiling.webp) 

La frecuencia con que se repite la textura dentro del perfil del pincel. Los modos `Mosaico - X` y `Mosaico - Y` te permiten limitarte a una sola textura en el trazo (`Ninguno`), repetirla (`Repetir`) o reflejarla, volteando una de cada dos texturas para crear patrones o ayudar a hacer texturas sin costuras (`Espejo`). Están disponibles con el trazo `Rodar`, con la proyección `Mosaico` o con un `Mosaico` mayor que 1.

`Ajuste ceñido (imágenes no cuadradas)` solo importa con alfas y texturas de pincel no cuadradas. Si está activado, cada imagen forma su mosaico por su cuenta, sin espacios. Desactívalo para mantener sincronizados el alfa y las demás imágenes cuando sus proporciones son distintas.

![](/videos/alpha_tiling.mp4) 



### Valor medio {#mid-value}

Por defecto, los píxeles negros significan ninguna deformación y los blancos, deformación positiva completa. Por ejemplo, un pincel de arcilla con una textura de alfa de rocas solo levantará la superficie donde el alfa no sea negro.

Si quieres que el pincel hunda la superficie, o que la hunda Y la levante a la vez, puedes modificar el valor medio. Si lo pones a 0,5, un gris medio en el alfa no hace nada, el negro hunde y el blanco levanta.

Dos botones te ayudan a encontrar el valor adecuado: el botón cuadrado lee el valor medio en el borde de la imagen, y el cuentagotas te permite elegirlo sobre el propio alfa.




## ![](/icons/falloff.webp) Disminución {#falloff}

![](/images/falloff_menu.webp) 

Funciona como el [Alfa](#alpha), salvo que la intensidad se controla con una sola curva. Se combina con el alfa, de modo que puedes usar una textura para el detalle y la atenuación para controlar el desvanecimiento del borde y la intensidad en el centro de la herramienta.

Cuando la curva está arriba, la deformación es completa; cuando está abajo, el pincel no tiene efecto.

Puedes ver la curva como un corte transversal de la punta del pincel. La sección inferior muestra una vista previa de cómo quedaría una sola «estampa» del pincel sobre la superficie del modelo y, si el pincel tiene una textura de alfa, también la muestra, para que veas cómo interactúan la atenuación y el alfa.

### ![](/icons/fx.webp) Preajuste {#preset}
Con `Preajuste...` seleccionado, al tocar el gráfico de la curva aparece un menú de preajustes. Las curvas redondeadas dan resultados más suaves y las angulosas, más marcados. El botón `Sub` de la barra de herramientas izquierda invierte en la práctica la atenuación: la parte alta de la curva hunde la superficie en lugar de levantarla, o al revés.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
Con esta opción puedes dibujar tus propias curvas de atenuación. El editor de curvas funciona igual que las curvas del resto de Nomad:

* Toca la curva para crear un punto nuevo
* Arrastra un punto para moverlo
* Toca un punto para alternar entre anguloso y suave
* Arrastra un punto sobre un punto vecino para eliminarlo

### ![](/icons/curve_bspline.webp) B-spline {#b-spline}
Con esta opción puedes dibujar tus propias curvas de atenuación. El editor funciona igual que Catmull-Rom, pero los puntos influyen en la curva en lugar de estar directamente sobre ella, lo que ayuda a crear formas de curva más suaves.

### ![](/icons/curve_bevel.webp) Bisel {#bevel}
Los puntos se unen con líneas rectas, con esquinas redondeadas cuyo tamaño depende de la nitidez de cada punto. Muy práctico para pinceles de punta plana con un bisel limpio en el borde.

El editor de curvas tiene 3 botones:

| Elemento | Icono                       | Descripción                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximizar | ![](/icons/maximize.webp) | Amplía el editor de curvas                   |
| Restablecer | ![](/icons/reset.webp)  | Devuelve la curva a su estado por defecto    |
| Simetría | ![](/icons/symmetric.webp) | Muestra la curva como una «punta de pincel» simétrica |


### Influencia {#influence}

* `Esfera` (3d) - La influencia se calcula a partir de la distancia entre el vértice y el centro del pincel.
* `Círculo` (2d) - El vértice se proyecta primero sobre el plano del área y luego se mide su distancia al centro del pincel. Es parecido a como se muestrean los alfas. 
* `Cilindro` - La influencia se proyecta a través del área como un cilindro. Equivale a activar la [Silueta](#silhouette-1) de abajo.
* `Cresta` - La atenuación se mide a lo ancho del trazo, de modo que la curva pasa a ser el corte transversal de todo el trazo. El botón `Sim` refleja entonces el perfil a ambos lados del trazo: editas un lado y el otro le sigue. Si está desactivado, la curva va del lado izquierdo del trazo a su lado derecho. No está disponible para las herramientas basadas en aplanar.

### ![](/icons/silhouette.webp) Silueta {#silhouette-1}
Por defecto, los trazos solo afectan a la superficie del modelo que queda dentro del radio del pincel. Con la silueta activada, el trazo se proyecta a través de todo el modelo. Es muy útil para el encaje inicial de un modelo, o para formas cuyos lados deben quedar perpendiculares. Tiene las mismas opciones de proyección que la [Silueta](#silhouette) de la pestaña Trazo.



## ![](/icons/filter.webp) Filtro {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Acumular trazo {#accumulate-stroke}
Quita el límite a la cantidad de materia que se puede añadir o quitar en cada trazo. Por ejemplo, la herramienta `Arcilla` lo tiene activado, así que el material puede seguir acumulándose, mientras que la herramienta `Brocha` lo tiene desactivado: el trazo deja de añadir material si sigues pasando el mismo trazo por la misma zona de la malla. 

### ![](/icons/culling.webp) Solo vértice frontal {#front-facing-vertex-only}
Esta opción ignora los vértices orientados hacia atrás.
Puede ser útil si quieres pintar una parte de una geometría fina sin afectar al otro lado.
También funciona al esculpir, pero puede que aparezcan algunos artefactos.

### ![](/icons/eye_open.webp) Solo vértices visibles {#visible-vertex-only}
Ignora los vértices ocultos detrás de otras superficies, vistos desde la cámara. Esta opción aparece en los trazos de forma (lazo, rectángulo...) de las herramientas de máscara, de pintura, `Grupo de caras` y `Ocultar`.

### ![](/icons/dynamic.webp) Permitir topología dinámica {#allow-dynamic-topology}
Esta opción solo está disponible si tu malla está en modo [Topología dinámica](topology.md#dynamic-topology). Puedes desactivar o activar la topología dinámica para cada herramienta.

### ![](/icons/connect.webp) Topología conectada {#connected-topology}
Esculpe solo los vértices unidos a la superficie que tocas con la herramienta. Por ejemplo, con la herramienta `Mover` te permite mover una parte aunque se cruce con otra.
![](/videos/connected_topology.mp4)

### Proteger área {#protect-area}
![](/images/filter_protect_area.webp) 

Estas opciones impiden que las herramientas afecten a partes de la malla en distintas situaciones. Cada una se puede poner en `Auto`, `No` o `Sí`, y la flechita muestra a qué equivale `Auto` en ese momento.

* `Ocultar` - Si hay partes de la malla ocultas con la herramienta Ocultar, indica si deben protegerse. En `Auto`, las caras ocultas se protegen, salvo que su malla alámbrica esté visible (consulta los ajustes de [Malla alámbrica](settings.md#wireframe)).
* `Máscara` - Si hay partes de la malla con máscara, indica si deben protegerse. En `Auto`, las partes con máscara se protegen mientras la máscara está visible en el menú [Sombreado](shading).
* `Grupo de caras` - Indica si solo puedes usar la herramienta dentro del primer grupo de caras que tocas. En `Auto`, depende de si los grupos de caras están visibles en el menú [Sombreado](shading).

El botón `(Todo)` indica si estas protecciones son globales, compartidas por todas las herramientas, o propias de cada herramienta.


### Muestreo de área {#area-sampling}
Algunos pinceles u opciones de trazo necesitan la normal y la posición de un plano sobre la superficie para funcionar.

Puedes controlar cómo se calcula este plano medio fijando el área de muestreo como una proporción del radio de la herramienta.

Al 100 %, se tienen en cuenta todos los puntos dentro del círculo de selección.

Al 0 %, solo se tiene en cuenta el vértice o triángulo más cercano. Estos valores pueden ir vinculados para `Radio normal` y `Radio de posición`, o desbloquearse y ajustarse por separado.

### Filtro de normales por área {#keep-sharp-edges}
Excluye los puntos cuyas normales se desvían demasiado de la normal de la superficie.

Cambia la forma en que se calcula el plano del área (Muestreo de área), así que es útil sobre todo con las herramientas basadas en arcilla o en aplanar, o si quieres colorear una superficie casi plana sin desbordarte.

Los ángulos `Mín.` y `Máx.` controlan la transición entre los puntos excluidos y los afectados por completo, como muestra el pequeño disco de color que hay al lado.

![](/videos/filter_keep_sharp_edges.mp4)

### Filtro de normales con caída {#falloff-normal-filter}
Igual que el [Filtro de normales por área](#keep-sharp-edges), excluye los puntos cuyas normales se desvían demasiado de la normal de la superficie, pero actúa sobre la atenuación del pincel en lugar de sobre el cálculo del plano. Es útil para pintar pliegues o relieves.


### Filtro de profundidad {#depth-masking}
![](/images/stroke_depthmask.webp)

Excluye los puntos que quedan por encima o por debajo de cierta distancia del plano calculado (Muestreo de área).

Sirve para pintar solo en las zonas con relieve, o solo en las cavidades.

El gráfico representa un corte transversal de la superficie: la línea horizontal es donde está la superficie, y el círculo representa el radio de atenuación de la pintura por encima y por debajo de ella. `Desplazamiento de altura` es un porcentaje por encima o por debajo de la superficie a partir del cual empieza el cálculo de la máscara. Con `Atenuación de profundidad` activada, `Área superior` y `Área inferior` te permiten escalar la atenuación por encima y por debajo del punto de desplazamiento.

#### Ejemplo: pintar en las cavidades {#example-paint-in-cavities}
Para pintar solo las cavidades, pon el desplazamiento de altura en -100 % y ajusta el regulador del área superior para que se separe de la línea horizontal. Así, el primer toque fija la profundidad «cero» y solo se ven afectadas las zonas por debajo de esa profundidad.

![](/videos/stroke_depth_cavity.mp4)

#### Ejemplo: pintar en los relieves {#example-paint-on-bumps}
Para pintar solo las zonas altas, pon el desplazamiento de altura en +90 %, de modo que la parte inferior del círculo corte un poco la línea horizontal. Al tocar la parte superior de una zona «alta», se fija la profundidad, y se pinta todo lo que esté a esa profundidad, un poco por debajo, y todo lo que esté más alto. Las cavidades profundas se saltan.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Presión {#pressure}
![](/images/pressure_menu.webp) 

Controla cómo afecta la presión del lápiz a los pinceles.

### Utilizar configuración global {#use-global-settings}

Por defecto, `Utilizar configuración global` está activado, lo que significa que todos los pinceles comparten los mismos valores de presión. Desmárcalo para que la herramienta actual tenga sus propios ajustes de presión.

### ![](/icons/radius.webp) Radio {#pressure-radius}

Esta curva controla cómo afecta la presión al radio del pincel. Por defecto, la relación es lineal, así que si tu lápiz tiene una respuesta suave, el cambio de radio también debería sentirse suave. Dicho esto, muchos lápices tienen una respuesta no lineal, que puedes compensar con esta curva. Por ejemplo, si te parece que el radio no llega a su valor máximo con una presión alta, usa un preajuste de curva como «out-pow3», con una curvatura hacia arriba, para que el radio aumente antes.

Esta ventana se parece a la de la curva de atenuación: puedes usar un preajuste tocando la ventana de la curva, o dibujar tus propias curvas con los modos `Catmull-Rom`, `B-spline` y `Bisel`.

Si quieres un radio constante, desactiva esta sección.

### ![](/icons/intensity.webp) Intensidad {#pressure-intensity}

Igual que la curva del radio, pero para controlar la intensidad. Si quieres una intensidad constante, desactiva esta sección.

### Limitar presión al 100% {#limit-pressure}

Garantiza que la presión del lápiz nunca supere el 100 %. Es un ajuste global.

### Suavizado de presión {#pressure-smoothing}

Promedia los eventos de presión del lápiz para obtener resultados más suaves.
