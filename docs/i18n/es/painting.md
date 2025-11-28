# ![](/icons/paint.webp) Pintura {#painting}

Controla el color, la rugosidad, la metalicidad de las pinceladas, permite el relleno global de atributos de pintura y cómo las herramientas de pintura interactúan con capas, máscaras y selecciones ocultas.

![](/images/paint_overview.webp)  

## Visión general {#overview}

Nomad usa pintura de vértices PBR. ¿Qué significa esto?

### PBR {#pbr}
PBR, o Renderizado Basado en Física (Physically Based Rendering), es una técnica popular de gráficos por computadora para cine, televisión, videojuegos y móviles. Al basar las luces en propiedades físicas y definir las superficies mediante color, rugosidad y metalicidad, se puede lograr una amplia variedad de apariencias fotorrealistas.

### Pintura de vértices {#vertex-painting}

Pintura de vértices significa que la información de pintura se almacena en los vértices del modelo, en lugar de en texturas. Como Nomad puede manejar modelos con cientos de miles, a menudo millones de vértices, tus modelos deberían poder tener pintura de superficie muy detallada; si puedes esculpir el detalle, también puedes pintarlo.

Esto también significa que pintar en Nomad no requiere mapeo UV, a menudo un proceso lento y técnico en otras aplicaciones 3D. Muchas otras aplicaciones 3D no soportan los altos recuentos de vértices que maneja Nomad; sin embargo, Nomad también tiene buenas herramientas de bakeo de texturas y de diezmado para ayudar.

### Texturizado {#texturing}

Nomad soporta texturas, pero estas tienen que estar presentes en un modelo importado, o mediante el bakeo de pintura de vértices a texturas. 

Una textura es simplemente una imagen, pero en el contexto 3D normalmente se refiere a una imagen asignada a un objeto.
Para envolver una imagen alrededor de un modelo, el modelo necesita coordenadas de textura (UV).

Nomad puede [calcularlas automáticamente](topology.md#uv-unwrap), pero no tienes mucho control sobre la calidad general.

::: tip
Un ejemplo de flujo de trabajo:
- Esculpir en Nomad, luego hacer [UV unwrap](topology.md#uv-unwrap)
- Si ya empezaste a pintar en Nomad puedes [transferir la pintura de vértices a texturas](topology.md#bake-vertex-colors-to-texture)
- Exportar a Procreate
- Texturizar en Procreate
- Exportar de vuelta a Nomad para fines de renderizado
:::

Esa es la visión general, ahora exploremos las secciones del menú de pintura:


## Pintura por trazos {#stroke-painting}
![](/images/paint_intensity.webp)  

Activa la pintura para esta herramienta, útil si necesitas esculpir y pintar al mismo tiempo.

Para las herramientas donde la pintura es la función principal (p. ej. Paint, Smudge, Mask), esta casilla no existe.

### Intensidad de la pintura {#paint-intensity}

Un deslizador que te permite usar una intensidad diferente a la intensidad principal de la herramienta.

Las casillas `Alpha`, `Falloff` y `Randomize` determinan si esas funciones afectarán a la pintura. Por ejemplo, podrías tener aleatorización activada para la herramienta Clay, pero el color no se aleatorizará.


## Material {#material}
![](/images/paint_material.webp) 

El primer icono es una forma de vista previa de material. Al arrastrar sobre la vista previa 3D del material lo rotarás. 

El segundo icono es una vista previa de la pincelada con el alfa y el falloff seleccionados.

El botón de vista previa junto al título Material te permite alternar entre None, Material o Triplanar. Esto determina lo que sucederá cuando cambies interactivamente las propiedades de pintura:

* `None` - No se mostrará ninguna vista previa en el modelo cuando ajustes propiedades
* `Material` - Los valores del material se previsualizarán en el objeto cuando ajustes propiedades. Si usas texturas y el modelo tiene UVs, se usarán los UVs.
* `Triplanar` - El material se previsualizará como una proyección Triplanar. 

El cuentagotas se puede usar para muestrear todas las propiedades de un objeto en tu escena.

## Ajustes preestablecidos de material {#material-presets}
Al tocar la forma de vista previa 3D aparecerá un menú de preajustes de materiales; estos se pueden clonar para definir tus propios preajustes.

![](/images/paint_presets.webp) 

Las opciones `Embed Textures` y `Alpha`, cuando están activadas, almacenarán cualquier textura usada por este material dentro del preajuste. Esto se explica más abajo.

## Deslizadores PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

La pintura [PBR](shading.md#pbr) usa 4 canales:
- `Color` El color que se va a pintar. El cuentagotas se puede usar para seleccionar color de otras partes del modelo o de imágenes de referencia.
- `Roughness` Indica cuán "rugosa" o "suave" es una superficie. Un valor bajo de rugosidad significa que los reflejos serán nítidos.
- `Metalness` Simplemente indica si la superficie es metálica o no. El valor debería ser 0% o 100% la mayor parte del tiempo; los valores intermedios deberían ser excepcionales.
- `Opacity` Cuánto se puede ver a través del material. Estrictamente hablando no forma parte de la especificación PBR, pero es útil en muchas situaciones. 1 es completamente opaco, 0 es transparente. Ten en cuenta que opacidad y refracción son cosas diferentes; la refracción en Nomad se maneja mediante el material de refracción. 

Si seleccionas un preajuste de material, se pintan 3 canales simultáneamente (la opacidad a menudo se excluye intencionadamente). Esto significa que en lugar de simplemente pintar "rojo", puedes estar pintando "un metal rojo rugoso" o "un plástico blanco liso".

El cuadrado es una ranura de textura; púlsalo para usar una textura para esa propiedad en lugar de un valor sólido.

El icono de pincel junto a los deslizadores rellenará por completo esa propiedad en tu objeto.

La casilla activará o desactivará esa propiedad en particular, de modo que podrías pintar solo color, o solo rugosidad y opacidad, por ejemplo. 

Aquí hay algunos ejemplos de diferentes propiedades de rugosidad y metalicidad:

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Solo se admite el color en el modo [Matcap rendering](shading.md#matcap); la metalicidad y la rugosidad se ignoran.
:::

::: tip
Cuando uses texturas para pintura PBR, a menudo es útil cambiar a algo como la herramienta `Stamp`, o usar el menú Stroke para usar un modo distinto de Dot, que puede emborronar la textura.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Podrías considerar activar `Smooth Shading` [globalmente](settings.md#smooth-shading) o [por objeto](material.md#smooth-shading) si estás pintando una superficie metálica en un objeto con un recuento de polígonos bajo.
:::

## Pintar todo {#paint-all}

![](/images/paint_paint_all.webp)

Aplica el material actual al objeto, ya sea en modo estándar con 'Paint All', o como una proyección Triplanar.

Se respetan las casillas junto a los deslizadores de color/metalness/roughness/opacity; cualquier propiedad desactivada no se rellenará.

Los botones adicionales controlan cómo se puede seguir afectando el Paint All:

| Icon                        | Descripción                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/tool_mask.webp) | Las áreas enmascaradas no se verán afectadas. |
| ![](/icons/tool_hide.webp) | Las áreas ocultas no se verán afectadas.      |
| ![](/icons/opacity.webp)   | Usar el factor de pintura de la herramienta de arriba. |
| ![](/icons/layer.webp)     | Las áreas no pintadas de una capa no se verán afectadas. |
| ![](/icons/triplanar.webp) | Indicador de ajustes de triplanar             |
| ![](/icons/cog.webp)       | Abrir los ajustes de Triplanar                |

### Ajustes triplanares {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

De forma similar a los [ajustes de triplanar en el menú Material](material.md#triplanar), puedes controlar la mezcla de las proyecciones, el teselado (tiling) y los desplazamientos. 

Usa la casilla de vista previa en la parte superior de este menú para activar una vista previa persistente mientras ajustas los valores.

## Material global {#global-material}
Si esta opción está activada, el material seleccionado será el mismo que el de las otras herramientas. Ten en cuenta que solo tiene en cuenta los ajustes de rugosidad, metalicidad y color.