# ![](/icons/sun.webp) Sombreado {#shading}

Este menú controla los modos de sombreado que usa Nomad, las propiedades de la iluminación, el entorno y el matcap, y la niebla.

![](/images/shading_overview.webp)



Puedes elegir entre varios modos de renderizado:

| Modo                        | Significado                | Descripción                                                     |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Iluminado (PBR)](#pbr)     | Renderizado basado en la física | Luces, sombras, entorno y metalicidad/rugosidad pintadas   |
| [MatCap](#matcap)           | Captura de material        | Modo rápido para esculpir, que usa menos gpu/cpu que el PBR     |
| [Sin iluminación](#unlit)   | Color de superficie        | Solo el color de la superficie, sin sombreado ni iluminación    |
| [ID de objeto](#object-id)  | ID de objeto               | Un color aleatorio por objeto, útil en aplicaciones de pintura. |
| [ID de instancia](#instance-id) | ID de instancia        | Un color aleatorio por instancia, útil para identificar mallas compartidas |

Si quieres saber más sobre la metalicidad y la rugosidad, consulta la sección [Pintura de vértices](painting.md).

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) Grupo de caras {#face-group}
Superpone los colores de los grupos de caras. Los grupos de caras son selecciones de polígonos con color que se crean con la herramienta [Grupo de caras](tools#facegroup), y que la mayoría de las primitivas generan automáticamente.

Algunas herramientas filtran automáticamente por grupos de caras cuando estos están visibles.

### ![](/icons/palette.webp) Mostrar pintura {#show-paint}
Nomad puede guardar el color, la rugosidad y la metalicidad en los vértices de tu escultura. Con esta casilla puedes mostrar u ocultar estas propiedades de forma global.

Ten en cuenta que si tienes a la vez propiedades de vértice y texturas, y ambas están activadas, sus valores se multiplican.

### ![](/icons/shield.webp) Mostrar máscara {#show-mask}
Muestra u oculta la superposición en escala de grises de las [herramientas de máscara](tools#mask). Al desactivarla, también se desactiva la máscara: es útil para hacer cambios rápidos sin la máscara y luego volver a activarla sin perderla.

### ![](/icons/tool_hide.webp) Usar Ocultar {#use-hide}

Activa o desactiva las caras ocultas. ¡Ten en cuenta que solo funciona si NO estás en la herramienta Ocultar!

### ![](/icons/image.webp) Utilizar texturas {#use-textures}

Nomad permite asignar texturas a los objetos desde el menú [Material](material). Si hay texturas asignadas, puedes activarlas o desactivarlas de forma global con esta casilla.

No puedes crear ni editar texturas dentro de Nomad, pero las texturas de los archivos importados funcionan. Las texturas de opacidad funcionan en Iluminado, MatCap y Sin iluminación; los mapas de normales, en Iluminado y MatCap; el color, en Iluminado y Sin iluminación; y la emisión, la rugosidad y la metalicidad, solo en Iluminado. El botón aparece en gris cuando la escena no tiene ninguna textura.

### PBR y luces: descripción general {#pbr}
Este manual no entra en detalle en el renderizado basado en la física.

Algo importante que hay que tener en cuenta es que la iluminación y el material están totalmente separados.
Esto significa que puedes pintar el color, la rugosidad y la metalicidad de tu objeto mientras la iluminación se gestiona de forma independiente.
Así puedes pintar tu objeto y ajustar la iluminación más tarde, sin estropear el aspecto general de tu modelo.

Las luces, el entorno y la niebla solo están disponibles en [modo PBR](#pbr).
Por motivos de rendimiento, estás limitado a 4 luces en móvil y 6 en escritorio.

::: tip
Puedes cargar un archivo glTF con más luces y Nomad las conservará todas.
Eso sí, el rendimiento no tiene por qué ser bueno.
:::

::: tip
Puedes simular muchas luces haciendo que algunos objetos sean emisivos o sin iluminación, y activando luego la iluminación global en el menú [Posprocesado](postprocess).
:::

### Tipos de luces: descripción general {#light-types-overview}

Estos son los tipos de luces que se admiten actualmente:

| Modo                        | Descripción                                             | Puede proyectar sombras |
| :-------------------------: | :-----------------------------------------------------: | :--------------: |
| [Direccional](#directional) | Luz solar situada infinitamente lejos                   | Sí               |
| [Entorno](#env-light)       | Una luz lejana alineada con el HDR del entorno          | Sí               |
| [Foco](#spot)               | Luces en forma de cono                                  | Sí               |
| [Punto](#point)             | Punto de luz omnidireccional                            | Sí               |

#### ![](/icons/sun.webp) Direccional {#directional}
Emite luz desde una distancia infinita, con una intensidad uniforme.
Su posición 3d en la escena no importa, solo cuenta su orientación.

Puedes vincular esta luz a la cámara para que la iluminación sea siempre la misma.  
Por ejemplo, puedes usarla para crear una luz de contorno (una luz intensa que sale de detrás de tu modelo, apuntando hacia la cámara) que ilumine siempre la parte trasera de tu modelo.

#### ![](/icons/panorama.webp) Luz de entorno {#env-light}
Usar un [HDR de entorno](#environment) funciona bien para una iluminación general suave, pero si en el HDR se ve una luz intensa y marcada, la sombra que crea será muy suave, y a menudo ni siquiera se verá. Combinar una luz direccional con el HDR del entorno puede ayudar, pero cuesta alinearlas.

Esta luz hace el trabajo por ti. Gira automáticamente para alinearse con la parte más brillante del HDR, y luego puedes controlar por separado su intensidad y su ángulo (la suavidad de la sombra). 

#### ![](/icons/spotlight.webp) Foco {#spot}
El foco emite luz en una sola dirección, limitada por una forma de cono.

#### ![](/icons/light.webp) Punto {#point}
La luz puntual emite luz en todas las direcciones, y también puede proyectar sombras.

#### Sombras {#shadows}
Cada luz puede proyectar sombras, y puedes elegir cómo se calculan en sus [ajustes](#light-extra-controls). Si ves artefactos en las sombras, los reguladores `Tolerancia` de ahí pueden ayudar.

La calidad de las sombras depende del tamaño de los objetos en relación con toda la escena.  
Si tienes en la escena un objeto grande que no necesita proyectar sombras (por ejemplo, un plano grande), desactiva la proyección de sombras en sus [ajustes de material](material.md#casts-shadows).

## ![](/icons/sun.webp) Luces {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Casilla de las luces {#lights-checkbox}

Activa o desactiva todas las luces directas de la escena.



### Agregar luz {#add-light}

Añade una luz a la escena, hasta 4 luces en móvil y 6 en escritorio. Al añadir una luz, aparece la lista de luces con sus botones, y se añade una barra de herramientas de luz en la parte superior del visor.

![](/images/shading_lights_icons.webp)

* El texto muestra el nombre de la luz y su brillo. Tócalo para seleccionar la luz.
* El icono del ojo la muestra u oculta.
* El icono del lápiz te permite renombrar la luz.
* El icono de la papelera elimina la luz.
* El icono de copiar duplica la luz. 
* El icono de los 3 puntos abre el editor completo de la luz. La mayoría de sus funciones también están en la barra de herramientas que aparece en el visor. 

También puedes arrastrar una luz en la lista para cambiar su orden.

### ![](/icons/spotlight.webp)  Iconos {#icons}

Muestra u oculta los iconos de las luces en el visor

### Barra de herramientas de luz {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Esta barra de herramientas aparece en la parte superior del visor cuando hay una luz seleccionada.

* `Visible` muestra u oculta la luz.
* Direccional/Entorno/Foco/Punto cambia el tipo de luz. Toca para pasar de uno a otro, o mantén pulsado para ver un menú.
* La intensidad controla la fuerza de la luz; el valor puede superar 1,0 para luces muy intensas, algo útil con la iluminación global del Posprocesado
* Al tocar la muestra de color se abre un selector de color. Nomad ofrece varias formas de elegir el color. El control en Kelvin es una forma natural de elegir una iluminación cálida o fría.
* Sombra activa o desactiva las sombras.
* Ángulo (_direccional y entorno_) o Tamaño (_foco y punto_) fija la anchura de una luz. Las luces más anchas proyectan sombras suaves, una iluminación suave y un brillo más suave sobre los objetos.
* Vinculación (_solo direccional_), Ángulo de cono y Suavidad (_solo foco_) se describen más abajo, en el [editor de luz](#light-extra-controls).
* ... muestra `Clonar`, `Volver a centrar` y `Eliminar`, junto con los ajustes de sombra.

### Controles adicionales de luz {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

El icono de los 3 puntos de una luz en la lista abre su editor completo. Ten en cuenta que algunas opciones son propias de ciertos tipos de luz.

* `Direccional/Entorno/Foco/Punto` te permite cambiar el tipo de luz.
* Al tocar la `muestra de color` se abre un selector de color. 
* `Intensidad` controla la fuerza de la luz.
* `Vinculación` (_solo direccional_) vincula la luz al mundo (`Fija`) o a la cámara (`Cámara`). Por ejemplo, si usas una luz direccional detrás de tu personaje como luz de contorno, con la vinculación a la cámara la luz seguirá detrás del personaje aunque gires la cámara.
* `Suavidad` (_solo foco_) controla la nitidez del borde del cono del foco. 0 es un borde muy nítido. 1 es muy suave, con un degradado hacia el centro del cono de luz. En el visor, el puntito azul del cono del foco permite ajustar la suavidad de forma interactiva.
* `Ángulo de cono` (_solo foco_) controla la apertura del foco. Un ángulo pequeño es un haz de luz muy fino; 170 es una luz muy abierta. En el visor, el punto naranja permite ajustar el ángulo del cono de forma interactiva.
* `Ángulo` (_solo direccional y entorno_) es el tamaño aparente de la luz: piensa en lo grande que se ve el sol en el cielo. Los ángulos más grandes proyectan sombras más suaves y brillos más anchos.
* `Tamaño` (_solo foco y punto_) es la anchura de la luz. Las luces más grandes proyectan sombras más suaves.
* `Sombra` activa o desactiva las sombras de la luz actual.
* El tipo de sombra indica cómo se calculan las sombras. Un `Mapa de sombras` renderiza la escena desde la luz, así que también sombrea la geometría que la cámara no ve. `Espacio de pantalla` solo usa lo que ya está visible en pantalla: es más ligero, pero experimental. En general, el mapa de sombras es más fiable.
* `Tolerancia` (_solo espacio de pantalla_): si se ven artefactos en las sombras (las sombras no parecen tocar las superficies, o hay ruido y patrones dentro de ellas), ajustar la tolerancia puede ayudar a corregirlos.
* `Contacto` añade sombras más precisas a distancias cortas, donde los objetos se tocan. Con `Auto`, solo la luz más dominante de la escena tiene sombras de contacto; `No` y `Sí` lo fuerzan para esta luz. Su regulador `Tolerancia` funciona como el de arriba.

El botón `...` de la barra de herramientas del visor reúne los mismos ajustes de sombra, además de:

* `Clonar` duplica la luz.
* `Volver a centrar` mueve la luz delante de la cámara, conservando su orientación.
* `Eliminar` elimina la luz.


## ![](/icons/panorama.webp) Entorno {#environment}

![](/images/shading_environment.webp)

En el mundo real, la luz llega de todas las direcciones: el azul del cielo, el verde de la hierba, el rojo de un edificio... Toda esta luz del «entorno» se puede simular con un mapa de entorno. 

Usa la casilla junto al título para activar o desactivar la iluminación del entorno.

Nomad incluye varios mapas de entorno de ejemplo, de interior y de exterior, con distintos tonos y niveles de brillo. Prueba varios mapas para ver cuál resalta mejor los detalles de tus esculturas.

Toca la imagen para ver los mapas de entorno disponibles. En esa ventana, elige `Importar...` para cargar los tuyos. Lo mejor es usar imágenes de alto rango dinámico (HDR), en formato latlong o equirrectangular, como archivos .hdr o .exr. El explorador también puede descargar entornos directamente de [Poly Haven](https://polyhaven.com/hdris), que tiene una buena colección de mapas de entorno gratuitos.

### Exposición {#env-exposure}
Ajusta el brillo del mapa de entorno. A menudo los mapas resultan demasiado brillantes junto con luces normales; bajar la exposición ayuda a equilibrarlos, sobre todo con la iluminación global de los ajustes de [Posprocesado](postprocess).

### Rotación {#env-rotation}

Como los mapas de entorno capturan la luz de todas las direcciones, puedes girarlos para que los reflejos y la iluminación general encajen bien con tu escultura. También puedes girar el entorno arrastrando 3 dedos en horizontal sobre el visor.

### Vincular a la cámara {#env-attached}
Vincula el entorno a la cámara.

Así la iluminación se mantiene siempre igual, algo que puede ser útil mientras esculpes.

### Desenfoque (fondo) {#env-background-blur}
Este regulador solo aparece cuando el [fondo](background.md) usa el entorno. Desenfoca la imagen del entorno detrás de tu modelo, sin cambiar la iluminación.


## ![](/icons/fog.webp) Niebla {#fog}

La niebla añade profundidad atmosférica a tu escena y hace visibles los haces de luz. Actívala con la casilla junto al título. Como las luces y el entorno, solo está disponible en el modo [Iluminado (PBR)](#pbr).

::: tip Haces de luz más marcados
Baja el `Entorno` de la niebla y usa un foco o una luz puntual brillante. Aumenta la `Densidad` hasta que la niebla se vea con claridad. Para ver los haces en una niebla más fina, pon la `Dirección de dispersión` en un valor positivo alto y orienta la cámara hacia la luz.
:::

### Color {#fog-color}
El color de la niebla y de la luz que dispersa.

### Densidad {#fog-density}
La rapidez con la que la niebla se espesa con la distancia.

### Opacidad máxima {#fog-opacity}
Limita cuánto puede cubrir la niebla la escena, incluso con una densidad alta.

### Dirección de dispersión {#fog-scattering}
La dirección en la que la niebla dispersa la luz (también llamada anisotropía). Los valores positivos aclaran la niebla cuando miras hacia una luz, los negativos cuando miras en sentido contrario, y cero dispersa la luz por igual en todas las direcciones.

### ![](/icons/panorama.webp) Entorno {#fog-environment}
Cuánto ilumina el [entorno](#environment) la niebla. Aparece en gris cuando el entorno está desactivado.

### Ruido {#fog-noise}
Mezcla ruido en la niebla para dividirla en manchas, sin cambiar su densidad general. Cuando el ruido está por encima de 0, un regulador `Tamaño` fija el tamaño del patrón.

### Forma {#fog-shape}
Dónde llena la niebla la escena:

* `Uniforme` - llena toda la escena.
* `Vertical` - mantiene la niebla dentro de una franja vertical de bordes suaves. Los reguladores `Inferior` y `Superior` fijan la altura de sus bordes inferior y superior, y su botón del ojo muestra la franja en el visor mientras los ajustas.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

Como su nombre indica (MATerial CAPture, captura de material), un matcap reúne en una sola imagen la información de iluminación y de material.
Como el propio material ya está en el matcap, los canales de pintura de rugosidad y metalicidad se ignoran.
El color de pintura se multiplica por el matcap, así que si tienes un matcap negro o gris, pintar de blanco no lo aclarará.

Los artistas suelen preferir este modo para esculpir, porque les permite centrarse en la forma y la geometría en sí.

Al tocar la esfera se abre un explorador de imágenes. También puedes añadir tu propio matcap: en general sirve cualquier foto, render o incluso pintura de una esfera recortada justo en un cuadrado. Hay muchas bibliotecas de matcaps en internet; un buen recurso es la [biblioteca de matcaps de nidorx](https://github.com/nidorx/matcaps).

### Utilizar el MatCap global {#matcap-global}

Normalmente se usa un solo matcap para toda la escultura, pero si desactivas esta opción, el objeto seleccionado puede tener su propio matcap. Se puede usar de forma artística para conseguir resultados llamativos.

::: tip
¡Desactiva esta opción y usa la imagen de un globo ocular para los ojos de tus personajes!
:::

### Rotación {#matcap-rotation}
Un matcap es una forma especial de mapa de entorno, así que, como un mapa de entorno, se puede girar. También puedes hacerlo en cualquier momento en el visor arrastrando 3 dedos a izquierda y derecha.

El botón del candado junto al regulador bloquea la rotación, para que un arrastre con 3 dedos no gire el matcap por accidente.



## ![](/icons/circle_fill.webp) Sin iluminación {#unlit}

Este modo solo muestra el color de la superficie. Puede ser útil para comprobar que el color de la superficie de tus objetos es el que esperas, sin que te distraigan las luces, las sombras, los reflejos o la transparencia. 

Este modo también sirve para renders no fotorrealistas, con un aspecto plano de dibujo animado.

## ![](/icons/cube.webp) ID de objeto {#object-id}

Se ignora toda la información de iluminación y de superficie, y cada objeto se sombrea con un color plano único. Si se renderiza junto a un render PBR, se puede usar en un programa de pintura para seleccionar por color y así hacer correcciones de color en objetos concretos.

Ten en cuenta que estos colores también aparecen en la [vista de árbol del menú Escena](scene#tree-view).

### Aleatorizar ID {#object-random}

Genera un nuevo conjunto de colores aleatorios. 

## ![](/icons/link.webp) ID de instancia {#instance-id}

Igual que ID de objeto, pero las instancias tienen el mismo color. 

### Aleatorizar ID {#instance-random}

Genera un nuevo conjunto de colores aleatorios.
