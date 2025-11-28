# ![](/icons/pencil.webp) Trazo {#stroke}

---
![](/images/stroke_overview.webp) 

## Descripción general {#overview}

Puedes personalizar el comportamiento del trazo de la mayoría de los pinceles de herramientas.
Los ajustes deberían ser similares a los presentes en aplicaciones de pintura 2D, aunque algunas opciones son específicas de esculpido y 3D.

Las opciones se dividen en 5 submenús:

| Nombre   | Icono                        | Descripción                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | Controla cómo se aplica el trazo al modelo                         |
| Alpha    | ![](/icons/alpha.webp)      | Cómo se usa una textura en escala de grises para la huella del pincel |
| Falloff  | ![](/icons/falloff.webp)    | Controla cómo cambia la fuerza del pincel desde el centro al borde |
| Filter   | ![](/icons/filter.webp)     | Cómo afecta la geometría del modelo al pincel                      |
| Pressure | ![](/icons/pressure.webp)   | Controla la respuesta a la presión del lápiz                       |

::: tip
No todas las opciones de trazo se aplican a todas las herramientas. Las opciones de trazo que no use la herramienta actual se desactivarán u ocultarán. 
:::


## Trazo {#stroke-1}

### Radio {#radius}

![](/images/stroke_radius.webp)

#### Compartir radio {#share-radius}

Cuando está activado, todas las herramientas usarán el mismo radio; de forma predeterminada, cada herramienta tiene su propio radio.

#### Tamaño {#size}

* Screen: el radio se define en unidades de pantalla. Si haces el radio de 100 píxeles de ancho, se mantendrá en 100 píxeles independientemente de si haces zoom dentro o fuera.
* Constant (3d): el radio se define en unidades 3D. Por ejemplo, si creas una esfera y haces el radio del mismo tamaño que la esfera, el radio se mantendrá del mismo tamaño que la esfera al acercar o alejar el zoom.


### Trazo {#stroke-type}

![](/images/stroke_strokemode.webp)

Los trazos pueden funcionar en varios modos:

### ![](/icons/stroke_dot.webp) Punto {#dot}
Arrastra como un trazo de pintura normal. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Rodar {#roll}
El alfa del pincel se rotará para seguir la dirección del trazo, útil para hacer puntadas de tela. 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lock + radius
 Estampa un trazo de pincel con **_altura_** fija. Al arrastrar se define la escala y la rotación.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) Bloqueo + intensidad {#lock-intensity}
Estampa un trazo de pincel con **_radio_** fijo. Al arrastrar se define la altura y la rotación.
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

Las herramientas `Move` y `Drag` tienen sus propias 3 opciones:

### ![](/icons/snake.webp) Arrastrar {#drag}

Seguirá actualizando lo que está dentro del radio del pincel durante el trazo. Un trazo rápido dejará la superficie atrás, mientras que un trazo lento sujetará el material, creando formas más largas. Este es el modo predeterminado para la herramienta `Drag`. Con `Dynamic Topology` se puede usar para hacer extrusiones tipo serpiente. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Agarrar {#grab}
Seleccionará lo que esté dentro del radio del pincel cuando se inicie el pincel, y mantendrá esa selección. Esto es útil para operaciones de mover más precisas, ya que puedes ajustar cuidadosamente la distancia del movimiento y no mover accidentalmente más de lo que seleccionaste originalmente. Este es el modo predeterminado para la herramienta `Move`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Bloqueo + radio (arrastrar) {#lock-radius-drag}
Se ignora el radio definido por el usuario y se establece dinámicamente en función de lo lejos que se arrastre el trazo desde el punto de inicio. Distancia pequeña = radio pequeño, distancia mayor = radio más grande. Usa el control deslizante de intensidad para controlar la forma del falloff. Útil para bloquear formas orgánicas gomosas.
![](/videos/stroke_lockradius_drag.mp4) 



### Ajustar intensidad del espaciado {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Los trazos con un espaciado bajo (menor al 50 %) pueden acumularse rápidamente, produciendo trazos más intensos que con valores de espaciado más altos. Este interruptor compensará esto, de modo que los trazos tengan aproximadamente la misma intensidad independientemente del espaciado.

### Espaciado del trazo {#stroke-spacing}
Qué tan separados se aplican cada una de las huellas del pincel durante una operación de arrastre. Los valores inferiores al 100 % se superpondrán, dando la apariencia de un trazo continuo. Los valores superiores al 100 % empezarán a dejar huecos, útil para esculpir detalles como costuras o cremalleras.

### Estabilizador de cuerda perezosa {#lazy-rope-stabilizer}
Los trazos se retrasarán respecto a la posición del puntero una cierta distancia. Esto se puede usar para dibujar líneas suaves.
![](/videos/stroke_lazy_rope.mp4) 

### Suavizado del trazo {#stroke-smoothing}
Promedia múltiples posiciones del puntero para obtener un trazo más suave.
Con valores altos, el trazo se retrasará respecto al puntero pero eventualmente lo alcanzará.
Esto es útil para dibujar líneas suaves.

### Ajuste de radio {#snap-radius}
Ajusta el inicio del trazo al final del trazo anterior. El radio determina a qué distancia se busca el final del trazo anterior. Esto puede ser útil al dibujar líneas largas y continuas, haciendo pausas frecuentes.

### ![](/icons/silhouette.webp) Silueta {#silhouette}
![](/images/stroke_silhouette.webp)
De forma predeterminada, los trazos solo afectarán a la superficie del modelo dentro del radio del pincel. Cuando la silueta está activada, el trazo se proyectará a través de todo el modelo. Esto puede ser muy útil al hacer el bloqueo inicial de un modelo, o para formas que requieren que los lados permanezcan perpendiculares.

La dirección de proyección se puede establecer explícitamente; el método predeterminado “Closest” detectará el mejor ángulo en relación con la vista. 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp) Aleatorizar {#randomize}

![](/images/stroke_randomize.webp)

La intensidad, traslación, rotación y escala del trazo se pueden aleatorizar de forma independiente. Esto se puede usar para crear una variedad de efectos; por ejemplo, aleatorizar con la herramienta de pintura puede crear color moteado, o aleatorizar con la herramienta de pliegue puede usarse para crear detalles de piel.

![](/videos/stroke_randomize.mp4) 

### Desplazamiento del trazo {#stroke-offset}

Aplica un desplazamiento constante al trazo. Esto es útil en pantallas pequeñas donde tu dedo cubriría el trazo. 


## ![](/icons/alpha.webp) Alfa {#alpha}
![](/images/stroke_alpha.webp) 

El `Alpha` es una textura que modulará el comportamiento de tu pincel.
Es una imagen en escala de grises, donde los píxeles negros significan sin deformación y los píxeles blancos deformación completa.

Haz clic en la imagen del alfa para cambiarla.

Haz clic en la vista previa del material para cargar un alfa desde un preset de material. También puedes guardar presets de material aquí y elegir incrustar texturas con la herramienta.

::: tip
La textura nunca se redimensiona, por lo que las texturas grandes pueden ralentizar el rendimiento.
:::

### Invertir píxeles {#invert-pixels}
Esto invertirá los valores de la imagen, de modo que los píxeles negros se volverán blancos y los blancos se volverán negros.

::: tip

Los alfas integrados que se incluyen con Nomad no se pueden invertir.

:::

### Escalado {#scaling}

El tamaño del pincel en Nomad es un círculo con un radio definido por el usuario. Las texturas suelen ser cuadradas o rectangulares; los parámetros de `Scaling` te permiten decidir cómo debe encajar la textura dentro del círculo. Para una textura cuadrada, un valor de 0.7 encajará dentro del círculo. Un valor de 1 escalará la textura más grande para que el círculo quepa dentro, recortando los bordes.

![](/images/alpha_scaling.webp) 

Al activar `Scaling - Y` podrás estirar el alfa verticalmente.

![](/images/alpha_scaling_y.webp) 

### Rotación {#rotation}

La textura alfa se rotará para seguir la dirección del trazo. Puedes añadir un desplazamiento de rotación y, si el icono de candado está activado, la textura permanecerá bloqueada a esta rotación relativa a la pantalla.

### Mosaico {#tiling}
![](/images/stroke_tiling.webp) 

Con qué frecuencia se repite la textura dentro del perfil del pincel. Los modos de repetición te permiten limitar a una sola textura dentro del trazo, texturas repetidas o en espejo, donde cada segunda textura se invierte para crear patrones o ayudar a hacer texturas sin costuras.

![](/videos/alpha_tiling.mp4) 



### Valor medio {#mid-value}

De forma predeterminada, los píxeles negros significarán sin deformación y los píxeles blancos significarán deformación positiva completa, así que, por ejemplo, un pincel de arcilla con una textura alfa de rocas solo tirará de la superficie hacia afuera donde el alfa no sea negro.

Si quieres que el pincel empuje la superficie hacia adentro, o que tanto empuje como tire, puedes modificar el valor medio. Así, si estableces el valor en 0.5, un gris medio en el alfa no hará nada, un valor negro empujará hacia adentro y el blanco tirará hacia afuera.




## Degradación {#falloff}

![](/images/falloff_menu.webp) 

Esto es similar al [Alpha](#alpha), excepto que controlas la intensidad con una única curva. Esto se combina con el alfa para que puedas usar una textura para el detalle y el falloff para controlar el desvanecimiento del borde y la intensidad en el centro de la herramienta.

Cuando la curva está en la parte superior, hay deformación completa; cuando está en la parte inferior, el pincel no tiene efecto.

Puedes pensar en la curva como una sección transversal de la punta del pincel. La sección inferior da una vista previa de cómo se vería una sola “estampación” del pincel en la superficie del modelo, y si hay una textura alfa para el pincel, también se mostrará para previsualizar cómo interactuarán el falloff y el alfa.

### Preajuste {#preset}
Con esto seleccionado, al hacer clic en el gráfico de la curva aparecerá un menú de presets. Las curvas redondeadas darán resultados más suaves; las curvas angulares tendrán resultados más marcados. El botón `Sub` en la barra de herramientas izquierda invertirá efectivamente el falloff, de modo que la parte superior de la curva empuje hacia la superficie en lugar de tirar hacia afuera, o viceversa.

### Catmull-Rom {#catmull-rom}
Cuando está seleccionado, el usuario puede dibujar sus propias curvas de falloff. El editor de curvas funciona igual que las curvas en el resto de Nomad:

* Haz clic en la curva para crear un nuevo punto
* Arrastra un punto para reposicionarlo
* Haz clic en un punto para alternar entre afilado y suave
* Arrastra un punto sobre un punto vecino para eliminarlo

### B-spline {#b-spline}
Cuando está seleccionado, el usuario puede dibujar sus propias curvas de falloff. El editor funciona igual que Catmull-Rom, pero los puntos de la curva influyen en la curva en lugar de estar directamente sobre ella, lo que puede ayudar a crear formas de curva más suaves.

El editor de curvas tiene 3 botones:

| Elemento | Icono                        | Descripción                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | Expande el editor de curvas                  |
| Reset    | ![](/icons/reset.webp)     | Revierte la curva al estado predeterminado   |
| Symmetry | ![](/icons/symmetric.webp) | Muestra la curva como una “punta de pincel” simétrica |


### Influencia {#influence}

* Sphere (3d): la influencia se calcula tomando la distancia desde el vértice al centro del pincel.
* Circle (2d): el vértice se proyecta primero en el plano del área, antes de tomar su distancia al centro del pincel. Esto es similar a cómo se muestrean los alfas. 
* Cylinder: la influencia se proyecta a través del área como un cilindro, usado por el modo Silhouette de abajo.

### Silueta {#silhouette-1}
De forma predeterminada, los trazos solo afectarán a la superficie del modelo dentro del radio del pincel. Cuando la silueta está activada, el trazo se proyectará a través de todo el modelo. Esto puede ser muy útil al hacer el bloqueo inicial de un modelo, o para formas que requieren que los lados permanezcan perpendiculares.



## Filtro {#filter}

![](/images/filter_menu.webp) 

### Acumular trazo {#accumulate-stroke}
Activa que no haya límite en cuánto material se puede añadir/eliminar por trazo. Por ejemplo, la herramienta `Clay` tiene esto activado, por lo que el material puede seguir acumulándose, mientras que la herramienta `Brush` lo tiene desactivado, de modo que los trazos dejarán de añadir material si sigues pasando el mismo trazo sobre la misma región de la malla. 

### Solo vértice de frente {#front-facing-vertex-only}
Esta opción ignorará los vértices que miran hacia atrás.
Puede ser útil si quieres pintar parte de una geometría delgada sin afectar al otro lado.
También funciona para esculpir, pero podrías experimentar algunos artefactos.

### Permitir topología dinámica {#allow-dynamic-topology}
Esta opción solo está disponible si tu malla está en modo [Dynamic Topology](topology.md#dynamic-topology). Puedes desactivar o activar la topología dinámica por herramienta.

### Topología conectada {#connected-topology}
Activa esculpir solo los vértices que están conectados a la superficie que tocas con la herramienta. Por ejemplo, cuando se usa con la herramienta `Move`, esto te permitirá mover una parte incluso si se cruza con otra parte.
![](/videos/connected_topology.mp4)

### Proteger área {#protect-area}
![](/images/filter_protect_area.webp) 

Estas opciones impedirán que las herramientas afecten a partes de tu malla bajo diversas condiciones. 

La opción “Auto” significa que, si tienes ocultar, máscara o facegroup visible en el menú [Shading](shading), estarán protegidos, pero si están desactivados en ese menú, la protección se deshabilita.

* `All`: alterna para definir si los filtros de protección son globales o por herramienta.
* `Hide`: si partes de la malla están ocultas con la herramienta de ocultar, define si deben estar protegidas.
* `Mask`: si partes de la malla están enmascaradas, define si deben estar protegidas.
* `Facegroup`: define si solo puedes usar una herramienta dentro del primer facegroup tocado.


### Mantener bordes marcados {#keep-sharp-edges}
Excluye puntos cuyos normales difieran demasiado de la normal de la superficie.

Cambiará cómo se calcula el área del plano (Area sampling).

Esta opción puede ser útil para herramientas basadas en aplanar, o si quieres colorear una superficie mayormente plana sin desbordamiento.

![](/videos/filter_keep_sharp_edges.mp4)

### Muestreo de área {#area-sampling}
Algunos pinceles u opciones de trazo requieren una normal de plano y una posición de plano en la superficie para funcionar.

Puedes controlar cómo calcular este plano promedio configurando el área de muestreo como una proporción del radio de la herramienta.

Al 100 %, se tienen en cuenta todos los puntos dentro del círculo de selección.

Al 0 %, solo se tiene en cuenta el vértice o triángulo más cercano. Estos valores pueden vincularse tanto para `Normal radius` como para `Position radius`, o desbloquearse y configurarse de forma independiente.


### Enmascarado de profundidad {#depth-masking}
![](/images/stroke_depthmask.webp)

Excluye puntos que estén por encima o por debajo de cierta distancia del plano calculado (Area sampling).

Esto se puede usar para pintar solo en regiones abultadas o solo en regiones de cavidad.

El gráfico representa una sección transversal de la superficie; la línea horizontal es donde está la superficie, el círculo representa el radio de falloff de la pintura relativo por encima y por debajo de la superficie. `Height offset` es un porcentaje por encima o por debajo de la superficie donde comenzar el cálculo de enmascarado. `Top area` y `Bottom area` te permiten escalar el falloff por encima y por debajo del punto de desplazamiento.

#### Ejemplo: Pintar en cavidades {#example-paint-in-cavities}
Para pintar solo regiones de cavidad, establece el desplazamiento de altura en -100 % y ajusta el control deslizante de top area de modo que se aleje de la línea horizontal. Esto significa que el primer clic establece la profundidad “cero” y luego solo se verán afectadas las áreas por debajo de esta profundidad.

![](/videos/stroke_depth_cavity.mp4)

#### Ejemplo: Pintar en salientes {#example-paint-on-bumps}
Para pintar solo en zonas altas, establece el desplazamiento de altura en +90 %, de modo que la parte inferior del círculo se cruce con la línea horizontal por una pequeña cantidad. Cuando hagas clic en la parte superior de una zona “alta”, esto establecerá la profundidad, de modo que se pintará cualquier cosa a esa profundidad, más un poco por debajo, y cualquier cosa por encima de ella. Las cavidades profundas se omitirán.
![](/videos/stroke_depth_bump.mp4)


## Presión {#pressure}
![](/images/pressure_menu.webp) 

Controla cómo la presión del lápiz/estilo afecta a los pinceles.

De forma predeterminada, `Use global settings` está activado, lo que significa que todos los pinceles compartirán los mismos valores de presión.

### Presión - Radio {#pressure-radius}

Esta curva controla cómo la presión afecta al radio del pincel. El valor predeterminado es una relación lineal, por lo que, si tu lápiz tiene una respuesta suave, el cambio de radio también debería sentirse suave. Dicho esto, muchos lápices tienen una respuesta no lineal, que puedes compensar con esta curva. Por ejemplo, si el radio no parece llegar a su valor máximo con alta presión, usa un preset de curva como “out-pow3”, con una curva que se incline hacia arriba, para aumentar el radio antes.

Este diálogo es similar a la visualización de la curva de falloff; puedes usar un preset tocando la ventana de la curva o dibujar tus propias curvas con los modos Catmull-Rom y B-Spline.

Si quieres un radio constante, desactiva esta sección.

### Presión - Intensidad {#pressure-intensity}

Similar al control deslizante de radio, pero para controlar la intensidad. Si quieres una intensidad constante, desactiva esta sección.

### Suavizado de la presión {#pressure-smoothing}

Promedia los eventos de presión del lápiz para obtener resultados más suaves.