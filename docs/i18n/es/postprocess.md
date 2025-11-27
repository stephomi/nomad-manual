# ![](/icons/postprocess.webp) Post proceso 

Este menú controla muchos aspectos de Nomad que afectan el aspecto del render.

![](/images/postprocess_overview_drac.webp)

Usar post proceso puede cambiar sustancialmente el aspecto final de tu escena.

![](/images/postprocess_overview.webp)
*La misma escena antes y después del post proceso, sin luces adicionales ni cambios de material.*

El post proceso puede impactar mucho el rendimiento dependiendo de tu dispositivo.
Hay una casilla global para desactivar todo el post proceso, de modo que puedas volver rápidamente a esculpir/modelar sin perder tus preajustes.
Para el renderizado PBR, se deberían activar [Oclusión ambiental](#ambient-occlusion-ssao), [Reflexión](#reflection-ssr) y [Mapeo de tonos](#tone-mapping).

Sin embargo, la mayoría del tiempo querrás que el post proceso esté desactivado mientras esculpes, para centrarte en la forma misma del modelo.

## Calidad

![](/images/postprocess_quality.webp)
### Muestreo máximo por fotograma
Nomad calculará cierta cantidad de post proceso para un solo fotograma de render, lo que puede verse ruidoso. Este control determina cuántos fotogramas se renderizarán y luego se mezclarán para eliminar la mayoría de los artefactos de ruido. Algunos efectos no requieren muestras extra (por ejemplo, corrección de color), mientras que otros como la iluminación global pueden requerir cientos de muestras para quedar libres de ruido. 

En la vista se puede ver cuando Nomad se deja quieto: la calidad de la imagen se irá refinando gradualmente hasta alcanzar el máximo de muestras y luego se detendrá. Esta cantidad de cálculos también se usa en la sección de render del [menú Archivos](files) cuando se hace clic en “export png”.

### Multiplicador de resolución
Este control deslizante controla la resolución del post proceso. Un valor de x1.0 significa que los renders se hacen a la resolución en píxeles del dispositivo. Un valor de x0.5 renderizará a media resolución, lo que será rápido pero de baja calidad. Un valor mayor que 1 renderizará a un tamaño más grande y luego reducirá la escala. Esto da como resultado mayor calidad, menos ruido, pero tiempos de render más largos.

### Muestras máximas

Esto aumentará la calidad del post proceso, pero en general `Resolución completa` tendrá más impacto. 

### Resolución completa
Cuando está activado, forzará el multiplicador de resolución a x1.0

### Eliminador de ruido (oidn)

Aplica un eliminador de ruido a la imagen. Esto te permite usar muchas menos muestras. Solo funciona si `Resolución completa` está activado. Ten en cuenta que la eliminación de ruido ocurre después de que se han calculado todas las muestras y puede ser intensiva para el procesador.

## Navegador de preajustes
![](/images/postprocess_presets.webp)
Al hacer clic en la imagen se mostrará una colección de preajustes de post proceso. Para definir tus propios preajustes, selecciona uno, haz clic en “clone”, realiza cambios. Para guardar, haz clic en la imagen del preajuste, vuelve a hacer clic dentro del navegador de preajustes y elige “save”.

## Reflexión (SSR)
Con esta opción, los objetos pueden reflejar otros objetos de la escena, siempre que los objetos sean visibles en la pantalla.
Si tienes objetos metálicos y brillantes en tu escena, entonces probablemente deberías usar esta opción.
Esta opción solo es efectiva con el modo PBR.


| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## Iluminación global (SSGI)

La iluminación global simula cómo la luz rebota entre superficies; por ejemplo, una pared roja proyectará rojo sobre un objeto blanco cercano. Esto puede mejorar enormemente el realismo de un render cuando se usa junto con oclusión ambiental y reflexiones. 

`Strength` - La intensidad de la iluminación global. 



| SSGI off                   | SSGI on                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Un foco está detrás de la esfera, apuntando al techo. Con SSGI desactivado, solo se ilumina el techo. Con SSGI activado, la luz rebota del techo a las paredes y a la esfera._

## Oclusión ambiental (SSAO)
La oclusión ambiental oscurecerá las áreas donde la luz tiene menos posibilidades de llegar (esquinas, etc.).
El efecto solo depende de la geometría del modelo.

* `Strength`- Intensidad del efecto.
* `Size`- Qué tan extendido está el efecto.
* `Curvature bias` - Qué tan sensible es el efecto en relación con la variación de la superficie.
* `Color` - Un tinte multiplicado en la oclusión, usado para efectos creativos.


| SSAO off                    | SSAO on                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
La AO será más visible en áreas iluminadas principalmente por la luz del entorno. Las áreas que están bajo una luz directa fuerte recibirán un efecto de AO mucho más débil.

:::

## Profundidad de campo (DOF)
Añade un efecto de desenfoque en la región que está fuera del foco.

Simplemente toca tu modelo para cambiar el punto de enfoque.

* `Far blur` - La cantidad de desenfoque que se aplicará en el lado lejano del punto de enfoque.
* `Near blur` - La cantidad de desenfoque que se aplicará entre el punto de enfoque y la cámara.


| DOF off                   | DOF focus on far ring       | DOF focus on close ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## Bloom
El bloom hará que las áreas brillantes de tu escena resplandezcan.

* `Intensity` - Fuerza del efecto.
* `Radius` - La extensión del efecto.
* `Threshold` - Qué tan brillantes deben ser los píxeles en la escena antes de que empiecen a hacer bloom. Ajustar este valor bajo hará que todo tenga bloom; ajustarlo alto permitirá que solo los píxeles más brillantes tengan bloom.
* `Color` - Un tinte que se puede añadir al bloom para efectos creativos.

| Bloom off                    | Bloom con radio 0           | Bloom con radio 1           |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## Tone Mapping
Tone Mapping es una operación que volverá a asignar valores HDR al rango `[0, 1]`.
Si no lo usas (o seleccionas `none`), cualquier componente de color mayor que 1 será recortado.
Cualquier variación de color por encima de este rango se perderá.

* `None/Neutral/Agx/ACES` - qué tonemapper usar. `None` no hace reasignación (pero los otros controles siguen funcionando). Las otras opciones son similares a elegir diferentes tipos de película; tratarán los valores y colores sobreexpuestos de diferentes maneras. Este es un tema muy profundo, busca información sobre tone mapping, Agx, ACES para más detalles.
* `Exposure` - brillo general de las imágenes, similar a ajustar la apertura en una cámara. Puede ser una forma rápida de aclarar u oscurecer globalmente una imagen.
* `Saturation` - intensidad del color. 1 es neutro, 0 es monocromo, valores por encima de 1 son cada vez más saturados.
* `Contrast` - hace los oscuros más oscuros y los claros más claros. Úsalo con cuidado, puede introducir artefactos con valores altos.

Observa que con `Tone Mapping` desactivado, algunos detalles desaparecen porque los píxeles son demasiado brillantes.

| Tone Mapping off            | Tone Mapping on            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
El tone mapping puede realzar el efecto de la iluminación global. Si bajas la intensidad del mapa de entorno y subes la fuente de luz principal, puedes aumentar la `exposure` del tone mapping para ver más de los efectos de luz rebotada.
:::

## Color Grading
Similar a la herramienta de curvas en Photoshop, esto te permite controlar el equilibrio y la distribución del color en la imagen. El control `main` afecta a todo el equilibrio de color, los controles `red`/`green`/`blue` permiten un control fino. 

| Color Grading off             | Color Grading on             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## Curvature
Detecta dónde hay cambios rápidos en la curvatura y aplica un color a esas regiones.

* `Factor` - intensidad general del efecto
* `Bump` - cuánto detectará cambios convexos pronunciados y colocará el color seleccionado allí (blanco por defecto)
* `Cavity` - cuánto detectará cambios cóncavos y colocará el color seleccionado allí (negro por defecto)


| Curvature off                    | Curvature on                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## Chromatic Aberration
Simula los artefactos de lente con la luz descomponiéndose alrededor de los bordes de la pantalla.

* `Strength` - cuánto se separan las partes roja/verde/azul de la imagen hacia los bordes de la pantalla

| Chromatic off                 | Chromatic on                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## Vignette
Simula los artefactos de lente oscureciendo los bordes de la pantalla.

* `Size` - el tamaño de una elipse invertida colocada sobre la imagen
* `Hardness` - cuán borrosa o nítida se mezcla la elipse sobre la imagen.


| Vignette off                    | Vignette on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## Grain
Añade un efecto de grano; puede ayudar a que la imagen se vea un poco menos artificial.

* `Strength` - la cantidad de grano/ruido añadido a la imagen.


| Grain off                    | Grain on                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## Sharpness
Un efecto de enfoque similar al de Photoshop o aplicaciones de procesado de fotos.

* `Strength` - la cantidad de enfoque aplicada a la imagen.


| Sharpness off                  | Sharpness on                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## Pixel Art
Simula pixel art de juegos retro.

* `Slider` - tamaño de los píxeles
* `Allow frame sampling` - si obtienes muchos píxeles negros, prueba a activar esto, lo que anulará el muestreo por defecto.

| Pixel off                   | Pixel on                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## Scanline
Simula el aspecto de los antiguos monitores CRT.

* `Factor` - intensidad de las líneas
* `Spacing` - tamaño de las líneas

| Scanline off                   | Scanline on                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |


## Dithering

Difumina (dither) los píxeles para reducir artefactos de bandas. Normalmente esto debería estar activado, pero puede desactivarse para operaciones específicas (por ejemplo, exportar mapas de profundidad u otras operaciones específicas de datos).
