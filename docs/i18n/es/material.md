# ![](/icons/material.webp) Material {#material}

Este menú te permite cambiar el material del objeto actual y las propiedades de render del objeto o del material, y asignar texturas al material.

![](/images/material_overview.webp)

Los materiales definen el aspecto de un objeto controlando cómo reacciona a la luz y a los demás objetos. El aspecto de un objeto depende de estas propiedades:

* `Tipo` de material
* `Color`
* `Rugosidad`
* `Metalicidad`
* `Opacidad`
* `Reflectancia`
* `Emisivo`/sin iluminación

Combinando estas propiedades puedes conseguir resultados muy variados, desde lo fotorrealista hasta lo caricaturesco o lo experimental.

El color, la rugosidad, la metalicidad y la opacidad se pueden pintar; consulta las [opciones de pintura de vértices](painting.md) para saber más.

El tipo de material, la reflectancia y el modo emisivo/sin iluminación son propiedades del material que se explican a continuación.

Los botones `Copiar` y `Pegar` de la parte superior de este menú te permiten copiar materiales de un objeto a otro.

Ten en cuenta que el motor de render de Nomad funciona en tiempo real: aunque es potente, prioriza la velocidad sobre la precisión en algunos efectos.

## Tipos de material {#material-types}

![](/images/material_types.webp)

Los tipos de material de Nomad son Opaco, Subsuperficie, Mezcla, Aditivo, Refracción, Tramado y Capturador de sombras.

### ![](/icons/material_opaque.webp) Opaco {#opaque}
El modo por defecto, que trata las superficies como un material sencillo que admite color, rugosidad, metalicidad y opacidad pintados. La opacidad pintada, una textura de opacidad o el canal alfa de la textura de color siguen haciendo que el objeto se transparente, mediante tramado. Solo se ignora el regulador principal de opacidad.

### ![](/icons/material_subsurface.webp) Subsuperficie {#subsurface}
Este modo simula materiales en los que la luz se difumina y se dispersa por dentro, como la piel, la cera o el jade.

Requiere el modo de sombreado PBR. Para obtener el mejor resultado, usa al menos una luz direccional o un foco, idealmente con un entorno tenue.

La muestra de color define el color de la luz dispersada.

`Profundidad` controla hasta dónde se dispersa la luz desde el frente, bajo la superficie y de nuevo hacia fuera por la superficie frontal. Esto suaviza las sombras duras y difumina los detalles de la superficie.

`Translucidez` controla cómo se dispersa la luz desde la parte delantera hasta la trasera de una forma, como cuando la luz atraviesa el envés de una hoja o cuando las orejas están muy iluminadas por detrás. Necesitas una luz que proyecte sombras para verlo.

### ![](/icons/material_blending.webp) Mezcla {#blending}

Parecido a Opaco, pero admite el regulador de opacidad para que el material pase de sólido a transparente. Es un simple regulador de opacidad, frente a la opacidad pintable que admite el material opaco.

::: warning
El modo de mezcla puede provocar parpadeos y saltos en formas complejas o que se intersecan.
:::

### ![](/icons/material_additive.webp) Aditivo {#additive}
Con este material puedes volver tu malla semitransparente. Se parece al material de mezcla, pero mientras que la mezcla se combina con lo que la rodea, el aditivo siempre es más brillante que los objetos que tiene detrás; va bien para efectos luminosos como rayos de luz, fuego o explosiones.

Puedes poner un valor de opacidad mayor que 1, lo que hará que el objeto sea más brillante.  
Es útil si quieres usar el [resplandor](postprocess.md#bloom) y el parámetro `Umbral` para que solo este objeto brille, como un objeto emisivo.

Este modo suele tener menos artefactos que [Mezcla](#blending) (transparencia independiente del orden).

### ![](/icons/material_refraction.webp) Refracción {#refraction}
Este modo sirve para simular cristal. Requiere el modo de sombreado PBR. Por las limitaciones del tiempo real, la autorrefracción y la refracción en varias capas son algo limitadas.

La rugosidad pintada del modelo influye en lo borrosa que se ve la refracción.
Por defecto, todos los objetos creados en Nomad tienen una rugosidad de alrededor del 25 %, así que la refracción no será perfecta, sino algo borrosa.
Puedes usar el botón `Pintar brillo` para repintar el modelo con una rugosidad y una metalicidad de 0 (los colores no se ven afectados).

Intervienen 2 rugosidades distintas: la que decide lo borroso que es el reflejo en la superficie y la que decide el interior (la refracción).  
Sin embargo, como Nomad solo tiene un canal de rugosidad pintada, la rugosidad interior y la exterior comparten el mismo valor.  
Para tener valores distintos (por ejemplo, una piruleta con la superficie nítida pero el interior borroso), usa los reguladores `Superficie` e `Interior` de `Anular rugosidad` para sustituir la rugosidad pintada.

![](/videos/refraction.mp4)

#### Índice de refracción {#index-of-refraction}
Cuánto se desvía la luz al entrar en el objeto. Los valores altos la desvían más, como una lente gruesa.

#### Absorción {#absorption}
Simula la luz absorbida mientras atraviesa el volumen, teñida por la muestra de color, con `Factor` para ajustar la fuerza. Las partes finas son más claras porque dejan pasar más luz, y las zonas gruesas son más oscuras. Solo se usa una aproximación del grosor del objeto, así que el efecto depende mucho de la forma.


### ![](/icons/material_dithering.webp) Tramado {#dithering}
Vuelve el objeto semitransparente descartando algunos píxeles de forma aleatoria.

### ![](/icons/material_shadow_catcher.webp) Capturador de sombras {#shadow-catcher}

Vuelve el objeto invisible y hace que solo reciba las sombras de las luces. Es útil para combinar renders de Nomad con otras imágenes, normalmente sobre un plano. La muestra de color define el color de la sombra.

Tiene que haber en la escena una luz que proyecte sombras; si no, el capturador de sombras no hace nada. Los botones `Metalicidad → 0%` y `Metalicidad → 100%` repintan el objeto: si es totalmente metálico, el capturador de sombras también puede reflejar la escena cuando el posprocesado [Reflexión (SSR)](postprocess.md#reflection-ssr) está activado.

::: tip

Encontrarás más información sobre la transparencia y los modos de mezcla en https://support.fab.com/s/article/Transparency-Opacity

:::

## Controles {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Siempre sin iluminación {#always-unlit}
Si está activado, el objeto ignora el PBR y el MatCap, y muestra simplemente el color pintado sin sombreado.
Ten en cuenta que, si usas [Aditivo](#additive), puedes pintar la transparencia directamente con el color negro.

### Opacidad {#opacity}
Lo sólido u opaco que se ve un objeto: 100 % es sólido y 0 % es transparente. El regulador aparece en los tipos Mezcla, Aditivo, Tramado y Capturador de sombras. También puedes pintar la opacidad para un control más fino.

### Paso de prerefracción {#pre-refract-pass}
Solo Mezcla y Aditivo. Dibuja este objeto transparente antes del paso de refracción. Es útil cuando un objeto con refracción está delante de otras superficies transparentes.

### Reflectancia {#reflectance}
Controla cuánto refleja el material en los materiales no metálicos. La mayoría de las veces conviene usar el valor por defecto (que corresponde al 4 % estándar de luz reflejada en ángulo normal), pero puedes subirlo para reforzar los reflejos y los brillos de los ojos de un personaje, por ejemplo. Requiere el modo de sombreado PBR.

### ![](/icons/culling.webp) Descarte inverso {#inverse-culling}
Invierte las normales de una superficie. Normalmente no hace falta, pero puede usarse si un modelo se ve del revés o, combinado con `Dos caras` desactivado, para crear interiores en los que la pared más cercana a la cámara siempre queda oculta.

Las siguientes opciones pueden ponerse en `Auto`, `No` o `Sí`. Con `Auto`, la flecha muestra el valor que se usa realmente.

### ![](/icons/sphere_smooth.webp) Sombreado suave {#smooth-shading}
Consulta la [opción global](settings.md#smooth-shading).  
El valor `Auto` usa la opción global.

### ![](/icons/culling.webp) Dos caras {#two-sided}
Las caras se ven por los dos lados. Consulta la [opción global](settings.md#two-sided-quick).  
El valor `Auto` usa la opción global.

### ![](/icons/culling.webp) Cara posterior coloreada {#coloured-backface}
Consulta la [opción global](settings.md#two-sided-quick).
El valor `Auto` usa la opción global.

### ![](/icons/shadow_cast.webp) Proyectar sombras {#casts-shadows}
Los objetos transparentes también proyectan sombras (con un patrón de tramado para imitar sombras mezcladas).  
Recuerda desactivar la proyección de sombras si tienes en la escena un objeto grande que no necesita proyectarlas (por ejemplo, un suelo grande).

### ![](/icons/shadow_receive.webp) Recibir sombras {#recieve-shadows}
Indica si las sombras de otros objetos se dibujan sobre este objeto.

### ![](/icons/wireframe.webp) Malla alámbrica {#wireframe}
Consulta la [opción global](settings.md#wireframe).  
El valor `Auto` usa la opción global.

### ![](/icons/trash.webp) Restablecer normales {#reset-normals}
Solo aparece cuando un objeto importado trae sus propias normales (por ejemplo, con `Mantener topología`). Las elimina, de modo que el sombreado usa las normales calculadas a partir de la superficie.


## Texturas {#textures}

![](/images/material_textures.webp)

Si un objeto tiene UV, puedes aplicar texturas al material además del color, la rugosidad, la metalicidad y la opacidad de los vértices. Normalmente son el resultado de un horneado de texturas, pero también puedes usar imágenes creadas fuera de Nomad. `UV:✓` o `UV:✗` junto al título te indica si el objeto tiene UV.

Se pueden aplicar texturas a

* Color
* Normal
* Rugosidad
* Metalicidad
* Opacidad
* Desplazamiento
* Emisivo

También aparece una fila `Oclusión` cuando un objeto importado tiene una textura de oclusión, pero Nomad no la usa.

El regulador de cada fila define con cuánta fuerza se aplica su textura, desde nada hasta del todo. `Color` y `Emisivo` tienen además una muestra de color que tiñe la textura, y `Emisivo` define la intensidad del brillo.

`Desplazamiento` define cuánto empuja la superficie el mapa de desplazamiento. Su botón `Aplicar` mueve los vértices según el desplazamiento y luego elimina el mapa. El resultado va a la capa activa.

El botón de la paleta junto al título abre los materiales preestablecidos del menú de [pintura](painting.md): toca uno para copiar sus texturas en el objeto. En escritorio, las imágenes importadas se sincronizan con su archivo original cuando vuelves a Nomad, y un botón de sincronización junto al título las recarga.

Al pulsar una ranura de textura se abre un selector. Cuando ya hay una textura asignada a una ranura del material, al pulsar de nuevo se abre un panel de textura:

### Opciones del panel de textura {#texture-panel-options}

![](/images/material_texture_panel.webp)

El panel muestra el tamaño de la imagen y una vista previa de la textura.

### ![](/icons/open.webp) Abrir {#open}
Selecciona otra textura. En escritorio, `Explorar` muestra el archivo de imagen en tu explorador de archivos.

### ![](/icons/circle_cross.webp) Ninguno {#none}
Quita la textura

### Opacidad {#texture-opacity}

Solo en la textura de color. Si la imagen tiene un canal alfa, te permite usarlo como opacidad o ignorarlo.

### Formato {#normal-format}
Solo en la textura normal. Los mapas de normales tienen dos variantes, `OpenGL (+Y)` y `DirectX (-Y)`. Si los detalles se ven invertidos, prueba la otra.

### Altura {#displacement-height}
Solo en la textura de desplazamiento.
* `Local` - La altura crece y disminuye con la escala del objeto.
* `Mundo` - La altura no cambia, sea cual sea la escala del objeto.

### Multiplicar {#multiply}
Solo en las texturas de rugosidad, metalicidad y opacidad. Multiplica los valores de la textura. Cuando no está al 100 %, el valor aparece en la ranura de textura.

### ![](/icons/link.webp) Icono de cadena/enlace {#chainlink-icon}

Cuando el icono de enlace de las siguientes secciones está activado, las opciones que uses se comparten con las demás texturas (color, normal, rugosidad, metalicidad, opacidad, emisivo) que también tengan su icono de enlace activado.

Así te aseguras de que, si tienes texturas alineadas, sigan alineadas aunque cambies los parámetros o los tipos de proyección.


### Proyección {#projection}
![](/images/material_projection.webp)

Define cómo se aplica la textura al objeto.

* `Auto` - UV si el objeto tiene UV; si no, Triplanar
* `UV` - Usa las coordenadas UV de la malla para aplicar la textura. Si la malla y la textura vienen de fuera de Nomad, o se van a exportar desde Nomad para usarlas en otro sitio, UV es la opción correcta.
* `Triplanar` - Proyecta la textura a lo largo de los ejes X, Y y Z, y funde las costuras.

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Las proyecciones triplanares son una forma potente y sencilla de aplicar texturas a los objetos.

Una proyección triplanar es como tener 6 proyectores de vídeo con la misma imagen, apuntando a la parte delantera, trasera, izquierda, derecha, superior e inferior de tu objeto.

Si hace falta, el resultado se puede hornear después en UV o en colores de vértice.


![](/images/material_triplanar_example.webp)

#### Método {#method}

* `Local` - La proyección se mueve con la transformación del objeto
* `Mundo` - Las proyecciones quedan fijas: al mover el objeto, este se desliza a través de la proyección.

#### Dureza {#hardness}

Cómo se mezclan las proyecciones. Con 100 % no hay mezcla y los bordes de las proyecciones son nítidos. Con 0 % los bordes se funden en un ángulo amplio. El valor por defecto es 90 %: mezcla suficiente para ocultar los bordes, mientras el resto de las proyecciones sigue nítido.

### Uniforme {#uniform}

Si está marcado, se usa la misma dureza para todas las proyecciones. Si no, aparecen controles de dureza adicionales para las proyecciones X, Y y Z.


### Parámetro {#parameter}
![](/images/material_parameter.webp)

#### Filtrado {#filtering}
El método de filtrado de textura que se usa. `Auto` es el valor por defecto; los métodos son `Más próximo`, `Lineal` y `Mipmap`. Más próximo no aplica ningún filtrado, así que las texturas pueden verse dentadas de cerca. Lineal y Mipmap filtran mejor, así que de cerca las texturas se ven borrosas en lugar de dentadas.

#### Mosaico - X {#tiling-x}
Si el parámetro Escala es mayor que 1, la textura queda más pequeña que las UV del objeto; esta opción decide cómo se repite la textura a lo largo del eje X. `Ninguno` significa sin repeticiones. `Repetir` hace copias de la textura. `Espejo` hace copias de la textura invirtiendo una de cada dos, lo que ayuda a disimular los artefactos de repetición.

#### Mosaico - Y {#tiling-y}
Igual que Mosaico - X, pero para el eje Y.

### Transformar {#transform}
![](/images/material_transform.webp)

Transformaciones 2d adicionales aplicadas a la textura en el espacio UV. El botón de restablecer vuelve a los valores por defecto, y el icono de cadena (cuando hay seleccionadas texturas distintas de la de color) vincula o desvincula la transformación para que sea la misma que la de la textura de color.

#### Traslación {#translation}
El desplazamiento X e Y de la textura

#### Rotación {#rotation}
La rotación de la textura

#### Escala {#scale}
La escala de la textura: cuanto mayor es el número, más pequeña se ve la textura en el objeto; usa las opciones Mosaico - X y Mosaico - Y para controlar lo que ocurre.

### Escala uniforme {#uniform-scale}
Si está desactivada, Nomad muestra controles separados para Escala X y Escala Y.
