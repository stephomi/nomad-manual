# ![](/icons/postprocess.webp) Posprocesado {#post-process}

Este menú controla muchos aspectos de Nomad que influyen en el aspecto del render.

![](/images/postprocess_overview_drac.webp)

El posprocesado puede cambiar mucho el aspecto final de tu escena.

![](/images/postprocess_overview.webp)
*La misma escena antes y después del posprocesado, sin luces adicionales ni cambios de material.*

El posprocesado puede afectar mucho al rendimiento, según tu dispositivo.
Hay una casilla global `Posprocesado` que desactiva todo el posprocesado, para que puedas volver rápidamente a esculpir o modelar sin perder tus ajustes.
Para el render PBR conviene activar la [Oclusión ambiental](#ambient-occlusion-ssao), la [Reflexión](#reflection-ssr) y el [Mapeo de tonos](#tone-mapping).

Aun así, la mayor parte del tiempo querrás tener el posprocesado desactivado mientras esculpes, para centrarte en la forma en sí y no en el render.


## Calidad {#quality}

![](/images/postprocess_quality.webp)

Estas opciones mejoran la calidad del render a costa del rendimiento.

### Máx. muestreo de fotogramas {#max-frame-sampling}
Nomad calcula una cierta cantidad de posprocesado en el render de un solo fotograma, que puede verse con ruido. Este control determina cuántos fotogramas se renderizan y se mezclan después para eliminar la mayor parte del ruido. Algunos efectos no necesitan muestras adicionales (por ejemplo, la graduación de color), mientras que otros, como las sombras suaves y la iluminación global, pueden necesitar cientos de muestras para quedar sin ruido.

En la vista se nota cada vez que dejas Nomad quieto: la calidad de la imagen se va refinando poco a poco hasta el máximo de muestras y luego se detiene. Una vez detenido, Nomad no hace nada, lo que ahorra batería. Este número de cálculos también se usa en la sección de render del [menú Archivos](files) al pulsar 'exportar png'.

La casilla junto al regulador activa o desactiva el muestreo de fotogramas.

### Resolución de renderizado {#resolution-multiplier}
Este regulador controla la resolución del render. Un valor de x1.0 significa que se renderiza a la resolución en píxeles del dispositivo. Un valor de x0.5 renderiza a la mitad de resolución, lo que es rápido pero de baja calidad. Un valor mayor que 1 renderiza a un tamaño mayor y luego reduce la imagen. Esto da más calidad y menos ruido, pero los tiempos de render son más largos.

Tiene un gran impacto en el rendimiento, así que intenta mantenerlo en x1.25 o menos. Este valor no se guarda en los ajustes, y el efecto [Arte pixelado](#pixel-art) lo anula.

### ![](/icons/intensity.webp) Muestras máx. {#max-samples}

Mejora la calidad de los efectos de posprocesado a costa del rendimiento.

### ![](/icons/material_dithering.webp) Tramado {#dithering}

Aplica un tramado a los píxeles para reducir el efecto de bandas (en degradados o en la viñeta, por ejemplo). Normalmente conviene tenerlo activado, pero se puede desactivar para operaciones concretas (por ejemplo, al exportar mapas de profundidad u otras operaciones con datos específicos).

### ![](/icons/denoise.webp) Filtro de ruido (oidn) {#oidn}

Aplica un filtro de ruido a la imagen una vez acumulados todos los fotogramas. Esto te permite usar muchas menos muestras. Eliminar el ruido exige mucho al procesador, así que actívalo solo si tu imagen tiene ruido. No está disponible en todos los dispositivos.

## Explorador de ajustes preestablecidos {#preset-browser}
![](/images/postprocess_presets.webp)
Al pulsar la imagen bajo el título `Posprocesado` se muestra una colección de ajustes preestablecidos de posprocesado. Usa `Nuevo` para crear un ajuste a partir de tu configuración actual. Los ajustes integrados solo se pueden clonar: para definir los tuyos, selecciona uno, pulsa `Clonar` y haz los cambios. Cuando un ajuste tiene cambios sin guardar, muestra `¡Cambios no guardados!`; para guardarlo, pulsa la imagen del ajuste, pulsa de nuevo dentro del explorador y elige `Guardar`.

## Barra de atajos {#shortcut-bar}
Cuando el posprocesado está activado, una barra en la parte inferior del menú lista todos los efectos (`SSR`, `SSGI`, `SSAO`, `DoF`, `Resplandor`...). Toca uno para saltar a su sección. Los efectos desactivados aparecen en gris, así que la barra también resume de un vistazo lo que hace el ajuste actual.

## ![](/icons/postprocess_ssr.webp) Reflexión (SSR) {#reflection-ssr}
Con esta opción, los objetos pueden reflejar otros objetos de la escena, siempre que esos objetos se vean en la pantalla.
Si tienes objetos metálicos y brillantes en tu escena, probablemente te convenga usar esta opción.
Esta opción requiere el modo de sombreado [Iluminado (PBR)](shading.md#pbr).


| SSR desactivado            | SSR activado              |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Iluminación global (SSGI) {#global-illumination-ssgi}

La iluminación global simula cómo rebota la luz entre las superficies; por ejemplo, una pared roja proyecta un tono rojo sobre un objeto blanco cercano. Combinada con la oclusión ambiental y los reflejos, puede aumentar muchísimo el realismo de un render. Al igual que los reflejos, requiere el modo de sombreado [Iluminado (PBR)](shading.md#pbr).

`Fuerza` - La intensidad de la iluminación global.



| SSGI desactivado           | SSGI activado             |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Detrás de la esfera hay un foco que apunta al techo. Con SSGI desactivado, solo se ilumina el techo. Con SSGI activado, la luz rebota del techo a las paredes y de ahí a la esfera._

## ![](/icons/postprocess_ssao.webp) Oclusión ambiental (SSAO) {#ambient-occlusion-ssao}
La oclusión ambiental oscurece las zonas a las que es menos probable que llegue la luz (esquinas, etc.).
El efecto solo depende de la geometría del modelo.

* `Fuerza` - Intensidad del efecto.
* `Tamaño` - Lo extendido que está el efecto.
* `Espesor` - El grosor en profundidad que se supone a los objetos que tapan la luz, como porcentaje del `Tamaño`.
* `Tinte` - Un color que se multiplica en la oclusión, para efectos creativos.


| SSAO desactivado            | SSAO activado              |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
La AO se nota sobre todo en las zonas iluminadas principalmente por la luz del entorno. Las zonas bajo una luz directa intensa reciben un efecto de AO mucho más débil.

:::

## ![](/icons/postprocess_dof.webp) Profundidad de campo {#depth-of-field-dof}
Añade un desenfoque a la zona que queda fuera de foco.

Basta con tocar tu modelo para cambiar el punto de enfoque.

* `Modo de apertura` - Controla el desenfoque con una sola apertura de cámara, en lugar de con los dos reguladores de desenfoque de abajo.
* `Apertura` (_solo en modo de apertura_) - El número f del objetivo, como en una cámara real. Un valor más bajo abre el objetivo y desenfoca más.
* `Borrosidad lejana` - La cantidad de desenfoque que se aplica más allá del punto de enfoque.
* `Borrosidad cercana` - La cantidad de desenfoque que se aplica entre el punto de enfoque y la cámara.


| DOF desactivado           | DOF enfocado en el aro lejano | DOF enfocado en el aro cercano |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Resplandor {#bloom}
El resplandor hace que brillen las zonas claras de tu escena.

* `Intensidad` - la fuerza del efecto.
* `Radio` - La extensión del efecto.
* `Umbral` - Lo brillantes que tienen que ser los píxeles de la escena para empezar a resplandecer. Con 0 todo resplandece; con un valor alto, solo resplandecen los píxeles más brillantes.
* `Tinte` - un color que se puede añadir al resplandor para efectos creativos.

| Resplandor desactivado       | Resplandor con radio 0      | Resplandor con radio 1      |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Mapeo de tonos {#tone-mapping}
El mapeo de tonos es una operación que reasigna los valores HDR al rango `[0, 1]`.
Si no lo usas (o eliges `Ninguno`), cualquier componente de color mayor que 1 se recorta.
Cualquier variación de color por encima de este rango se pierde.

* `Ninguno/Neutral/Agx/ACES` - qué mapeador de tonos usar. `Ninguno` no reasigna nada (pero los demás controles siguen funcionando). Las demás opciones son como elegir distintos carretes de película: tratan de forma diferente los valores y colores sobreexpuestos. Es un tema muy amplio: ¡busca información sobre tone mapping, Agx y ACES para saber más!
* `Exposición` - el brillo general de la imagen, parecido a ajustar la apertura de una cámara. Es una forma rápida de aclarar u oscurecer toda la imagen.
* `Saturación` - la intensidad del color. 1 es neutro, 0 es monocromo, y los valores por encima de 1 están cada vez más saturados.
* `Contraste` - Oscurece las sombras y aclara las luces. Úsalo con cuidado: con valores altos puede generar artefactos.

Fíjate en que, con el `Mapeo de tonos` desactivado, algunos detalles desaparecen porque los píxeles son demasiado claros.

| Mapeo de tonos desactivado  | Mapeo de tonos activado    |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
El mapeo de tonos puede reforzar el efecto de la iluminación global. Si bajas la intensidad del mapa de entorno y subes la de la fuente de luz principal, puedes aumentar la `Exposición` del mapeo de tonos para ver más los efectos de la luz rebotada.
:::

## ![](/icons/postprocess_tone_curve.webp) Graduación de color {#color-grading}
Parecida a la herramienta de curvas de Photoshop, te permite controlar el equilibrio y la distribución del color en la imagen. El control `Principal` afecta a todo el equilibrio de color, y los controles `Rojo`/`Verde`/`Azul` permiten un ajuste fino.

| Graduación de color desactivada | Graduación de color activada |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Curvatura {#curvature}
Detecta dónde hay cambios bruscos de curvatura y aplica un color a esas zonas.

* `Factor` - la intensidad general del efecto
* `Relieve` - cuánto detecta los cambios convexos marcados para colocar ahí el color elegido (blanco por defecto)
* `Cavidad` - cuánto detecta los cambios cóncavos para colocar ahí el color elegido (negro por defecto)
* `Espesor` - la anchura de los bordes detectados.

Junto a `Relieve` y `Cavidad`, una muestra de color elige el color, y un pequeño botón elige cómo se mezcla ese color con la imagen.


| Curvatura desactivada            | Curvatura activada             |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Aberración cromática {#chromatic-aberration}
Simula el defecto de los objetivos en el que la luz se descompone cerca de los bordes de la pantalla.

* `Fuerza` - cuánto se separan las partes roja, verde y azul de la imagen hacia los bordes de la pantalla

| Aberración desactivada        | Aberración activada          |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Viñeta {#vignette}
Simula el defecto de los objetivos que oscurece los bordes de la pantalla.

* `Tamaño` - El tamaño de una elipse invertida colocada sobre la imagen
* `Dureza` - Lo difusa o nítida que se mezcla la elipse sobre la imagen.
* `Tinte` - El color de la viñeta, negro por defecto.


| Viñeta desactivada              | Viñeta activada                |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Grano {#grain}
Añade un efecto de grano, que puede ayudar a que la imagen parezca algo menos artificial.

* `Fuerza` - la cantidad de grano o ruido que se añade a la imagen.


| Grano desactivado            | Grano activado             |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Nitidez {#sharpness}
Un efecto de enfoque parecido al de Photoshop o al de las aplicaciones de edición de fotos.

* `Fuerza` - la cantidad de enfoque que se aplica a la imagen.


| Nitidez desactivada            | Nitidez activada             |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Arte pixelado {#pixel-art}
Simula el pixel art de los juegos retro. Este efecto anula la [Resolución de renderizado](#resolution-multiplier).

* `Regulador` - el tamaño de los píxeles
* `Permitir muestreo de fotogramas` - si te salen muchos píxeles negros, prueba a activarlo. Sin él, el efecto de arte pixelado desactiva el [muestreo de fotogramas](#max-frame-sampling).

| Píxeles desactivados        | Píxeles activados          |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Línea de exploración {#scanline}
Simula el aspecto de los antiguos monitores CRT.

* `Factor` - la intensidad de las líneas
* `Espaciado` - el tamaño de las líneas

| Líneas desactivadas            | Líneas activadas              |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |
