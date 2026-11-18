# ![](/icons/paint.webp) Pintura {#painting}

Controla el color, la rugosidad y la metalicidad de los trazos de pintura, permite rellenar de golpe los atributos de pintura y define cómo interactúan las herramientas de pintura con las capas, las máscaras y las zonas ocultas.

![](/images/paint_overview.webp)  

## Visión general {#overview}

Nomad usa pintura de vértices PBR. ¿Qué significa esto?

### PBR {#pbr}
El PBR, o renderizado basado en la física (Physically Based Rendering), es una técnica de gráficos por ordenador muy extendida en cine, televisión, videojuegos y móviles. Al basar la iluminación en propiedades físicas y definir las superficies mediante color, rugosidad y metalicidad, se consigue una gran variedad de acabados fotorrealistas.

### Pintura de vértices {#vertex-painting}

La pintura de vértices significa que la información de pintura se guarda en los vértices del modelo, en lugar de en texturas. Como Nomad puede manejar modelos con cientos de miles, a menudo millones, de vértices, tus modelos pueden tener una pintura muy detallada: si puedes esculpir el detalle, también puedes pintarlo.

Esto también significa que pintar en Nomad no requiere un mapeado UV, un proceso a menudo lento y técnico en otras aplicaciones 3d. Muchas otras aplicaciones 3d no admiten tantos vértices como Nomad, pero Nomad también tiene buenas herramientas de horneado de texturas y de diezmado para ayudarte.

### Texturizado {#texturing}

Nomad admite texturas, pero tienen que venir en un modelo importado, o crearse horneando la pintura de vértices en texturas.

Una textura es simplemente una imagen, pero en 3d suele referirse a una imagen asignada a un objeto.
Para envolver un modelo con una imagen, el modelo necesita coordenadas de textura (UV).

Nomad puede calcularlas [automáticamente](topology.md#uv-unwrap), pero no tienes mucho control sobre la calidad general.

::: tip
Un ejemplo de flujo de trabajo:
- Esculpe en Nomad y luego haz el [desplegado UV](topology.md#uv-unwrap)
- Si ya habías empezado a pintar en Nomad, puedes [transferir la pintura de vértices a texturas](topology.md#bake-texture)
- Exporta a Procreate
- Texturiza en Procreate
- Vuelve a exportar a Nomad para el render
:::

Esa es la visión general; ahora veamos las secciones del menú de pintura:


## Pintura de trazo {#stroke-painting}
![](/images/paint_intensity.webp)  

Activa la pintura para esta herramienta, algo útil si necesitas esculpir y pintar a la vez. Cuando una herramienta puede pintar pero esta casilla está desactivada, un icono de aviso junto al título te lo recuerda.

En las herramientas cuya función principal es pintar (por ejemplo Pintar, Difuminar o Máscara), esta casilla no existe.

### ![](/icons/opacity.webp) Intensidad de pintura {#paint-intensity}

Un regulador para usar una intensidad distinta de la intensidad principal de la herramienta.

El botón de reguladores que hay al lado añade a la barra lateral un regulador rápido de intensidad de pintura, para las herramientas que esculpen y pintan a la vez.

Los botones `Alfa`, `Disminución` y `Aleatorizar intensidad` deciden si esas funciones afectan a la pintura. Por ejemplo, puedes tener la aleatorización activada en la herramienta de arcilla sin que el color se aleatorice.

* `Alfa` - si está desactivado, la pintura ignora el alfa y cubre toda la zona del pincel. Con la herramienta VDM, este botón se sustituye por `Material del sello`, que activa o desactiva el material guardado en el sello.
* `Disminución` - si está desactivado, la pintura mantiene toda su intensidad hasta el borde del pincel.
* `Aleatorizar intensidad` - indica si la parte de intensidad del aleatorizador del trazo afecta a la pintura. La aleatorización de posición, rotación y escala siempre mueve el sello entero.

[Pintar todo](#paint-all) ignora estas opciones, aunque su variante triplanar sí usa el alfa.

### ![](/icons/link.webp) Material global {#global-material}
Si esta opción está activada, el material seleccionado será el mismo que en las demás herramientas. Ten en cuenta que solo tiene en cuenta los ajustes de rugosidad, metalicidad y color. Desactívala para darle a esta herramienta su propio material.


## Material {#material}
![](/images/paint_material.webp) 

El primer icono es una forma de vista previa del material. Arrastrar sobre la vista previa 3d del material la hace girar.

El segundo icono es una vista previa del trazo de pintura con las opciones de alfa y disminución seleccionadas.

### ![](/icons/falloff.webp) Curvas {#curves}

Abre un editor de curvas para las ranuras de textura de los [reguladores PBR](#pbr-sliders). Reasigna los valores de la textura antes de pintarlos, sin modificar el archivo de imagen. Un pequeño icono de curva en una ranura de textura indica que su curva se ha editado.

### ![](/icons/cog.webp) Opciones de material {#material-options}

El botón `Material` junto al título contiene dos ajustes.

`Vista previa en el visor` determina qué ocurre en el objeto seleccionado mientras cambias los reguladores de color, rugosidad, metalicidad, opacidad e intensidad:

* `Ninguno` - No se muestra ninguna vista previa en el modelo cuando ajustas las propiedades
* `Material` - Los valores del material se previsualizan en el objeto cuando ajustas las propiedades.
* `Triplanar` - El material se previsualiza como una proyección triplanar.

Las casillas de color, rugosidad, metalicidad y opacidad de debajo eligen qué canales sustituye el [Selector de material](#material-picker).

### ![](/icons/dropper.webp) Selector de material {#material-picker}

El cuentagotas toma el material que hay bajo el cursor, de cualquier objeto de la escena. Solo se sustituyen los canales marcados en las [Opciones de material](#material-options).

## Ajustes preestablecidos de material {#material-presets}
Al tocar la forma de vista previa 3d se abre un menú de materiales preestablecidos; puedes clonarlos para definir tus propios ajustes.

![](/images/paint_presets.webp) 

La opción `Incorporar texturas` guarda dentro del ajuste preestablecido una copia de las texturas que usa este material. Sin ella, el ajuste solo hace referencia a las texturas de la carpeta textures/ de Nomad. Actívala cuando quieras compartir un ajuste con texturas sin tener que enviar las texturas aparte.

`Incluir alfa` guarda también el alfa del pincel en el ajuste preestablecido de material.

## Reguladores PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

La pintura [PBR](shading.md#pbr) usa 4 canales:
- `Color` El color que se va a pintar. Con el cuentagotas puedes tomar el color de otras partes del modelo o de imágenes de referencia.
- `Rugosidad` Indica lo "rugosa" o "lisa" que es una superficie. Un valor bajo de rugosidad significa que los reflejos serán nítidos.
- `Metalicidad` Indica simplemente si la superficie es metálica o no. La mayoría de las veces el valor debería ser 0 % o 100 %; los valores intermedios deberían ser la excepción.
- `Opacidad` Cuánto se puede ver a través del material. En sentido estricto no forma parte de la especificación PBR, pero es útil en muchas situaciones. 1 es totalmente opaco y 0 es transparente. Ten en cuenta que la opacidad y la refracción son cosas distintas: en Nomad, la refracción se gestiona con el material de refracción.

Si seleccionas un material preestablecido, se pintan 3 canales a la vez (la opacidad suele quedar excluida a propósito). Así, en lugar de pintar solo 'rojo', puedes pintar 'un metal rojo y rugoso' o 'un plástico blanco y liso'.

El cuadrado es una ranura de textura: púlsalo para usar una textura en esa propiedad en lugar de un valor fijo. Una textura de color tiñe el color, mientras que una textura de rugosidad, metalicidad u opacidad sustituye el valor del regulador (su etiqueta aparece tachada para indicarlo). En la textura de opacidad, `Usar alfa como valor` lee el canal alfa de la textura en lugar de su valor en escala de grises.

Con la herramienta VDM, cuando el sello lleva su propio material, una ranura adicional lo muestra junto a la ranura de textura. Tócala para usar o ignorar ese canal del sello.

El icono del pincel junto a los reguladores rellena esa propiedad en todo el objeto.

La casilla activa o desactiva esa propiedad en concreto, de modo que puedes pintar solo el color, o solo la rugosidad y la opacidad, por ejemplo.

Aquí tienes algunos ejemplos de distintos valores de rugosidad y metalicidad:

|                | Metalicidad 0 %                   | Metalicidad 100 %            |
| :------------: | :-------------------------------: | :--------------------------: |
| Rugosidad 0 %  | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Rugosidad 50 % | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Rugosidad 100 % | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
La rugosidad y la metalicidad requieren el modo de sombreado [Iluminado (PBR)](shading.md#pbr). En el modo [MatCap](shading.md#matcap) o [Sin iluminación](shading.md#unlit) se ignoran, y el menú muestra un aviso.
:::

::: tip
Al usar texturas para pintar en PBR, suele ser útil cambiar a una herramienta como `Sello`, o usar el menú de trazo para elegir un modo distinto de punto, que puede emborronar la textura.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Plantéate activar el `Sombreado suave` [de forma global](settings.md#smooth-shading) o [por objeto](material.md#smooth-shading) si pintas una superficie metálica en un objeto con pocos polígonos.
:::

## ![](/icons/paint.webp) Pintar todo {#paint-all}

![](/images/paint_paint_all.webp)

Aplica el material actual a los objetos seleccionados, en modo estándar con `Pintar todo` o como proyección triplanar con `Pintar todo + Triplanar`. La variante triplanar no está disponible en los primitivos que no se han validado.

Se respetan las casillas junto a los reguladores de color, metalicidad, rugosidad y opacidad: las propiedades desactivadas no se rellenan.

Los botones adicionales controlan cómo se ve afectado el relleno. La mayoría muestran un porcentaje, y aparecen en gris cuando no tendrían ningún efecto:

| Icono                       | Descripción                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | Las zonas enmascaradas no se verán afectadas. |
| ![](/icons/tool_hide.webp) | Las zonas ocultas no se verán afectadas.      |
| ![](/icons/opacity.webp)   | Usa el factor de pintura de la herramienta indicado arriba. |
| ![](/icons/layer.webp)     | Las zonas sin pintar de una capa no se verán afectadas. |
| ![](/icons/triplanar.webp) | `Vértice`: la variante triplanar también desplaza la superficie con el alfa, según la intensidad de herramienta indicada. |
| ![](/icons/cog.webp)       | Abre los ajustes triplanares                  |

### ![](/icons/cog.webp) Ajustes triplanares {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Igual que con los [ajustes triplanares del menú de material](material.md#triplanar), puedes controlar la mezcla de las proyecciones, el mosaico y los desplazamientos.

Usa la casilla de vista previa de la parte superior de este menú para activar una vista previa permanente mientras ajustas los valores.
