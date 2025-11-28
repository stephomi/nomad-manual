# ![](/icons/sun.webp) Sombreado {#shading}

Este menú controla los modos de sombreado usados por Nomad, las propiedades de iluminación y las propiedades de la luz de entorno/matcap.

![](/images/shading_overview.webp)



Puedes elegir entre varios modos de renderizado:

| Modo                        | Significado                     | Descripción                                                     |
| :-------------------------: | :-----------------------------: | :-------------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Renderizado Físicamente Basado  | Pintado con metalicidad/aspereza                                |
| [Matcap](#matcap)           | Captura de Material             | Usado durante el esculpido con menor uso de gpu/cpu que PBR     |
| [Unlit](#unlit)             | Color de Superficie             | Solo color de superficie sin sombreado ni iluminación           |
| [Object Id](#object-id)      | ID de Objeto                    | Un color aleatorio por objeto, útil para aplicaciones de pintado |
| [Instance Id](#instance-id)  | ID de Instancia                 | Un color aleatorio por instancia, útil para identificar mallas compartidas |

Si quieres aprender más sobre metalicidad y aspereza, consulta la sección [Pintura de vértices](painting.md).

---

![](/images/shading_second.webp)

### Grupo de caras {#face-group}
Superponer colores de grupos de caras. Los grupos de caras son selecciones coloreadas de polígonos que pueden crearse con la herramienta [Face group](tools#facegroup), y se generan automáticamente con la mayoría de las primitivas.

Algunas herramientas filtrarán automáticamente por grupos de caras cuando estos sean visibles.

### Mostrar pintura {#show-paint}
Nomad puede almacenar color, aspereza y metalicidad en los vértices de tu escultura. Puedes alternar la visualización de estas propiedades globalmente con esta casilla.

Ten en cuenta que si tienes tanto propiedades de vértice como texturas, y ambas están activadas, los valores se multiplicarán entre sí.

### Mostrar máscara {#show-mask}
Activa la superposición de máscara en escala de grises de las [herramientas de máscara](tools#mask). Cuando esto está desactivado, la máscara también se desactiva, lo que es útil para hacer cambios rápidos sin la máscara; luego puedes activarla de nuevo sin perderla.

### Usar ocultar {#use-hide}

Alterna las caras ocultas. Ten en cuenta que esto solo funciona si NO estás en la herramienta de ocultar (hide).

### Usar texturas {#use-textures}

Nomad permite asignar texturas a los objetos desde el menú de [material](material). Si se asignan texturas, pueden activarse o desactivarse globalmente con esta casilla.







### Resumen de PBR y luces {#pbr}
Este manual no profundizará en los detalles del Renderizado Físicamente Basado.

Algo importante a tener en cuenta es que la iluminación y el material están completamente separados.
Esto significa que puedes pintar el color, la aspereza y la metalicidad de tu objeto mientras la iluminación se gestiona de forma independiente.
Te permite pintar tu objeto y luego ajustar la iluminación más tarde, sin romper el aspecto general de tu modelo.

Las luces solo están disponibles con el [modo PBR](#pbr).
Por razones de rendimiento, estás limitado a solo 4 luces.

::: tip
Puedes cargar un archivo glTF con más de 4 luces y Nomad las conservará todas.
Sin embargo, no necesariamente tendrá buen rendimiento.
:::

::: tip
Puedes simular muchas luces haciendo objetos sin iluminación/emisivos y luego activar la iluminación global en el menú de [postproceso](postprocess).
:::

### Resumen de tipos de luz {#light-types-overview}

Estos son los tipos de luces actualmente soportados:

| Modo                        | Descripción                                             | Puede proyectar sombras                                |
| :-------------------------: | :-----------------------------------------------------: | :----------------------------------------------------: |
| [Directional](#directional) | Luz solar infinitamente lejana                          | Sí                                                     |
| [Environment](#environment) | Luz distante que coincide con el entorno HDR           | Sí                                                     |
| [Spot](#spot)               | Luces en forma de cono				                    | Sí                                                     |
| [Point](#point)             | Punto de luz omnidireccional                           | Sí, pero solo mediante sombras en espacio de pantalla menos robustas |

#### Direccional {#directional}
Emite luz desde una distancia infinita, con intensidad uniforme.
Su posición 3D en la escena no importa, solo su orientación.

Puedes adjuntar esta luz a la cámara, de modo que tenga una iluminación consistente.  
Por ejemplo, puedes usarla para crear una luz de contorno (una luz intensa que emite desde la parte trasera de tu modelo, apuntando hacia la cámara) que siempre ilumine la parte trasera de tu modelo.

#### Luz de entorno {#env-light}
Usar un [HDR de entorno](#environment) funciona bien para una iluminación suave general, pero si hay una luz fuerte y definida visible en el HDR, la sombra creada por ella será muy suave, a menudo nada visible. Usar una luz direccional en combinación con el HDR de entorno puede ayudar, pero puede ser difícil alinearlas.

Esta luz hace el trabajo por ti. La luz se rotará automáticamente para alinearse con la parte más brillante del HDR, luego podrás controlar su intensidad y ángulo (suavidad de la sombra) por separado. 

#### Foco {#spot}
La luz puntual tipo foco emite luz en una sola dirección, restringida por una forma de cono.

#### Punto {#point}
La luz puntual emitirá luz en todas las direcciones.  
Por el momento, la luz puntual no admite sombras.

#### Sombras {#shadows}
La opción `normal bias` puede usarse para reducir artefactos de sombras comunes (acné/peter-panning).

La calidad de las sombras depende del tamaño de los objetos en relación con toda la escena.  
Si tienes un objeto grande en tu escena que no necesita proyectar sombras (por ejemplo, un gran plano), asegúrate de desactivar la proyección de sombras en sus [ajustes de material](material.md#cast-shadows).

## Luces {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Casilla de luces {#lights-checkbox}

Activa o desactiva todas las luces directas de la escena.



### Añadir luz {#add-light}

Añade una luz a la escena, hasta un máximo de 4. Cuando se añade una luz, se muestra la lista de luces con botones y se añade una barra de herramientas de luz en la parte superior de la vista.

![](/images/shading_lights_icons.webp)

* El texto muestra el nombre de la luz y el brillo.
* El icono de ojo alterna la visibilidad.
* El icono de lápiz permite renombrar la luz.
* El icono de papelera eliminará una luz.
* El icono de copia duplicará una luz. 
* El icono de 3 puntos abrirá un editor completo de luz. Gran parte de esta funcionalidad también está disponible desde la barra de herramientas que aparece en la vista. 

### ![](/icons/spotlight.webp)  Iconos {#icons}

Alterna la visualización de los iconos de luz en la vista.

### Barra de herramientas de luces {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Esta barra aparecerá en la parte superior de la vista cuando se seleccione una luz.

* Show alterna la visibilidad de la luz.
* Directional/Environment/Spot/Point cambiará el tipo de luz. Toca para ciclar o mantén pulsado para ver un menú.
* Intensity controla la fuerza de la luz; el valor puede ir por encima de 1.0 para luces muy intensas, útil cuando se usa con Iluminación Global en Postproceso.
* Al hacer clic en la muestra de color se abrirá un selector de color. Nomad ofrece varias formas de elegir color. El control Kelvin ofrece una forma natural de seleccionar iluminación cálida/fría.
* Shadow alterna las sombras.
* Size establece el ancho de una luz. Las luces más anchas proyectarán sombras suaves, iluminación suave y un brillo más suave en los objetos.
* ... abrirá controles adicionales.

### Controles extra de luz {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Ten en cuenta que algunas opciones son específicas de ciertos tipos de luz.

* `Clone` duplicará la luz.
* `Recenter` moverá la luz de nuevo al origen.
* `Delete` eliminará la luz.
* `Directional/Environment/Spot/Point` permiten cambiar el tipo de luz.
* La `muestra de color` al hacer clic abrirá un selector de color. 
* `Intensity` controla la fuerza de la luz.
* `Attachment` (_solo direccional_) establecerá si la luz está asociada al mundo o a la cámara. Por ejemplo, si usas una luz direccional detrás de tu personaje como luz de contorno, cuando se selecciona attachment como cámara, al rotar la cámara la luz siempre quedará detrás del personaje.
* `Angle` (_solo direccional y de entorno_) es el tamaño aparente de la luz; piensa en él como lo grande que parece el sol en el cielo. Ángulos mayores proyectarán sombras más suaves y brillos más amplios.
* `Softness` (_solo foco_) controla la nitidez del borde del cono del foco. 0 es un borde muy nítido. 1 es muy suave, con un degradado hacia el centro del cono de luz. En la vista, el pequeño punto azul en el cono del foco puede usarse para ajustar la suavidad de forma interactiva.
* `Cone angle` (_solo foco_) controla el ángulo de apertura del foco. Un ángulo pequeño es un haz de luz muy fino, 170 es una dispersión de luz muy amplia. En la vista, el punto naranja puede usarse para ajustar el ángulo del cono de forma interactiva.
* `Shadow` alternará las sombras para la luz actual.
* `Shadow map` y `screenspace` son diferentes formas de calcular sombras; en general, shadow map es más fiable.
* `Contact` ajusta cómo se calculan las sombras. Las sombras son un problema difícil en gráficos por computadora y pueden causar artefactos en el renderizado. Se pueden seleccionar sombras más precisas para la luz más importante de una escena; este control determina si la luz más importante se selecciona automáticamente por Nomad o por el usuario.
* `Tolerance` si son visibles artefactos de sombras (ya sea que las sombras no parezcan contactar con las superficies, o haya ruido y patrones dentro de las sombras), ajustar la tolerancia puede ayudar a solucionar esos problemas.


## Entorno {#environment}

![](/images/shading_environment.webp)

La luz en el mundo real viene de todas direcciones; el azul del cielo, el verde de la hierba, el rojo de un edificio, toda esta luz del “entorno” puede simularse con un mapa de entorno. 

Nomad incluye varios mapas de entorno de ejemplo para interiores y exteriores, con diferentes tonos y niveles de brillo. Prueba distintos mapas para ver cuál resalta más detalle en tus esculturas.

Toca la imagen para ver los mapas de entorno disponibles. Desde ese diálogo elige “Import...” para cargar los tuyos. Es mejor usar imágenes de Alto Rango Dinámico (HDR), en formato latlong o equirectangular, como archivos .hdr o .exr. [www.polyhaven.com](https://polyhaven.com/hdris) tiene una buena colección de mapas de entorno gratuitos para usar; en general, los mapas hdr de 1k son de buen tamaño y buena calidad.

### Exposición {#env-exposure}
Ajusta el brillo del mapa de entorno. A menudo los mapas pueden ser demasiado brillantes cuando se usan con luces normales; bajar la exposición puede ayudar a equilibrar, especialmente cuando se usa con Iluminación Global en los ajustes de [Postproceso](postprocess).

### Rotación {#env-rotation}

Como los mapas de entorno capturan luz desde todas direcciones, puedes rotarlos para conseguir que los reflejos y la iluminación general combinen bien con tu escultura.

### Unido a la cámara {#env-attached}
Adjunta el entorno a la cámara.

Forzará a que la iluminación sea consistente, lo que puede ser útil durante el esculpido.


## ![](/icons/sphere_smooth.webp) Matcap {#matcap}

![](/images/shading_matcap.webp)

Como sugiere el nombre (MATerial CAPture), un matcap se encarga tanto de la información de iluminación como de material en una sola imagen.
Dado que el material en sí ya está presente en el matcap, los canales de pintado de aspereza y metalicidad se ignorarán.
El color de pintado se multiplicará contra el matcap, lo que significa que si tienes un matcap negro/gris, usar pintura blanca no lo hará más brillante.

Los artistas suelen preferir este modo para esculpir, ya que les permite centrarse en la forma y la geometría en sí.

Al tocar la esfera se abrirá un explorador de imágenes. También puedes añadir tu propio matcap; en general, cualquier foto, render, incluso una pintura de una esfera recortada ajustadamente en un cuadrado puede usarse. Hay muchas bibliotecas de matcaps disponibles en línea; un recurso útil es la [biblioteca de matcaps de nidorx](https://github.com/nidorx/matcaps).

### Usar Matcap global {#matcap-global}

Normalmente los artistas usarán un solo matcap para toda la escultura, pero si esta opción está desactivada, cada objeto puede tener su propio matcap. Esto puede usarse artísticamente para obtener resultados llamativos.

::: tip
¡Desactiva esta opción y usa una imagen de un globo ocular para los ojos de tus personajes!
:::

### Rotación {#matcap-rotation}
Un matcap es una forma especializada de mapa de entorno, así que, como un mapa de entorno, puede rotarse. También puedes hacerlo en cualquier momento en la vista arrastrando con 3 dedos hacia la izquierda y la derecha.



## ![](/icons/circle_fill.webp) Sin iluminación {#unlit}

Este modo solo mostrará el color de la superficie. Puede ser útil para comprobar que el color de superficie de tus objetos es el que esperas, sin distracciones de luces, sombras, reflejos o transparencia. 

Este modo también puede usarse para renders no fotorrealistas, logrando un aspecto plano y caricaturesco.

## ![](/icons/cube.webp) ID de objeto {#object-id}

Se ignora toda la información de iluminación y superficie, y cada objeto se sombrea con un color plano único. Si esto se renderiza junto con un render PBR, puede usarse en un programa de pintura para seleccionar por color y así poder hacer correcciones de color en objetos específicos.

Ten en cuenta que estos colores también aparecerán en la [vista de árbol del menú Escena](scene#tree-view).

### Aleatorizar ID {#object-random}

Genera un nuevo conjunto de colores aleatorios. 

## ![](/icons/link.webp) ID de instancia {#instance-id}

Igual que Object ID, pero las instancias tendrán el mismo color. 

### Aleatorizar ID {#instance-random}

Genera un nuevo conjunto de colores aleatorios.