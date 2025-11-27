# ![](/icons/material.webp) Material

Este menú te permite cambiar el material del objeto actual, las propiedades de renderizado del objeto/material y asignar texturas al material.

![](/images/material_overview.webp)

Los materiales definen cómo se ve un objeto, controlando cómo reacciona a la luz y a otros objetos. El aspecto de un objeto se controla mediante estas propiedades:

* `Material type`
* `Color`
* `Roughness`
* `Metalness`
* `Opacity`
* `Reflectance`
* `Emissive/unlit`

Las combinaciones de estas propiedades pueden lograr una gran variedad de resultados, desde fotorrealistas hasta caricaturescos o experimentales.

El color, la rugosidad, el metalness y la opacidad se pueden pintar; consulta las [opciones de Vertex Paint](painting.md) para más información.

El tipo de material, la reflectancia y emissive/unlit son propiedades del material explicadas a continuación.

Los botones de copiar/pegar en la parte superior de este menú te permiten copiar materiales de un objeto a otro.

Ten en cuenta que el motor de render de Nomad es en tiempo real; aunque es potente, prioriza la velocidad sobre la precisión para ciertos efectos. 

## Material types

![](/images/material_types.webp)

Los tipos de material de Nomad son Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Opaque
El modo predeterminado que trata las superficies como un material simple que admite color, rugosidad, metalness y opacidad pintados.

### ![](/icons/material_subsurface.webp) Subsurface
Este modo puede simular material que permite que la luz se difumine y disperse internamente, como piel, cera o jade.

Para obtener el mejor resultado, cambia al modo de sombreado PBR y usa al menos una luz direccional o puntual, idealmente con un entorno tenue.

`Depth` controla qué tan lejos se dispersa la luz desde la parte frontal, hacia debajo de la superficie y luego vuelve a salir por la superficie frontal. Esto tiene el efecto de suavizar las sombras duras y difuminar el detalle de la superficie.

`Translucency` controla cómo la luz se dispersa desde la parte frontal hacia la parte posterior de una forma, como la dispersión a través de la parte inferior de una hoja, o cuando las orejas están fuertemente retroiluminadas. 

### ![](/icons/material_blending.webp) Blending

Similar a Opaque, pero admite el control deslizante de opacidad para permitir que el material se mezcle entre sólido y transparente. Este es un control simple de opacidad mediante un único deslizador, frente a la opacidad pintable que admite el material opaco. 

::: warning
El modo Blending puede causar parpadeos y saltos en formas complejas o que se intersecan.
:::

### ![](/icons/material_additive.webp) Additive
Puedes hacer tu malla semitransparente con este material. Es similar al material blending, pero mientras blending se mezcla con su entorno, additive siempre será más brillante que los objetos que tenga detrás, lo que es bueno para efectos intensos como rayos de luz, fuego o explosiones.

Puedes establecer un valor de opacidad superior a 1, lo que significa que el objeto será más brillante.  
Puede ser útil si quieres usar el [bloom](postprocess.md#bloom) y el `threshold parameter` para hacer que solo este objeto brille como un objeto emisivo.

Este modo tiende a tener menos artefactos que [Blending](#blending) (transparencia independiente del orden).

### ![](/icons/material_refraction.webp) Refraction
Este modo se puede usar para simular material de vidrio. Debido a las limitaciones del tiempo real, la autorrefracción y la refracción en múltiples capas son algo limitadas.

La rugosidad pintada del modelo afecta lo borrosa que es la refracción.
De forma predeterminada, cada objeto creado en Nomad tiene una rugosidad de alrededor del 25%, por lo que la refracción no será perfecta sino un poco borrosa.
Puedes usar el botón `paint glossy` para repintar tu modelo con una rugosidad y metalness de 0 (los colores no se verán afectados).

Hay 2 rugosidades diferentes en juego: una controla lo borrosa que es la reflexión en la superficie y la otra controla el interior (refracción).  
Sin embargo, dado que solo hay un canal de rugosidad pintable en Nomad, tanto la rugosidad interior como la exterior compartirán el mismo valor.  
Para tener valores diferentes (por ejemplo, una piruleta con superficie nítida pero interior borroso) usa los deslizadores `Surface glossiness` e `Interior roughness` para anular la rugosidad pintada.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering
Hace el objeto semitransparente descartando algunos píxeles de forma aleatoria.

### ![](/icons/material_shadow_catcher.webp) Shadow Catcher

Hace el objeto invisible y solo recibe sombras. Útil para combinar renders de Nomad con otras imágenes. 

::: tip

Se puede encontrar más información sobre transparencia y modos de mezcla en https://support.fab.com/s/article/Transparency-Opacity

:::

## Controls

![](/images/material_controls.webp)

### Always unlit
Si está activado, el objeto ignorará PBR y Matcap y simplemente mostrará su color pintado sin sombreado.
Ten en cuenta que si usas [Additive](#additive), puedes pintar transparencia directamente usando color negro.

### Opacity
Qué tan sólido u opaco aparecerá un objeto; 100% es sólido, 0% es transparente. También puedes pintar la opacidad para un control más fino.

### Reflectance
Controla la cantidad de reflexión que recibirá el material para materiales no metálicos. La mayoría de las veces se debe usar el valor predeterminado (que corresponde al 4% estándar de luz reflejada en ángulo normal), pero se puede aumentar para potenciar reflejos y brillos, por ejemplo en los ojos de un personaje.

### Inverse culling
Invierte las normales de una superficie. Normalmente no es necesario, pero se puede usar si un modelo parece estar al revés o, en combinación con `Two sided` desactivado, se puede usar para crear interiores donde la pared más cercana a la cámara siempre esté oculta.

### Smooth Shading
Consulta la [opción global](settings.md#smooth-shading).  
El valor `Auto` usará la opción global.

### Two sided
Consulta la [opción global](settings.md#two-sided).  
El valor `Auto` usará la opción global.

### Coloured backface
Consulta la [opción global](settings#two-sided).
El valor `Auto` usará la opción global.

### Casts shadows
Por ahora `Auto` es lo mismo que `On`.
Los objetos transparentes también proyectan sombras (en un patrón de dithering para emular sombras mezcladas).  
Asegúrate de desactivar la proyección de sombras si tienes un objeto grande en tu escena que no necesita proyectar sombras (por ejemplo, un gran suelo).

### Recieve shadows
Por ahora `Auto` es lo mismo que `On`.

### Wireframe
Consulta la [opción global](settings.md#wireframe).  
El valor `Auto` usará la opción global.


## Textures

![](/images/material_textures.webp)

Si un objeto tiene UVs, entonces se pueden aplicar texturas al material además del color/rugosidad/metalness/opacidad por vértice. Normalmente son el resultado de un bake de texturas, pero también se pueden usar imágenes creadas fuera de Nomad.

Las texturas se pueden aplicar a

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Emissive

Al hacer clic en una ranura de textura aparecerá un selector. Después de que una textura se haya asignado a una ranura de material, al hacer clic de nuevo aparecerá un panel de textura:

### Texture panel options

![](/images/material_texture_panel.webp)

### Open
Seleccionar otra textura

### None
Eliminar la textura

### Opacity

Si la imagen tiene un canal alfa, esto te permitirá usarlo para Opacity o ignorarlo.

### ![](/icons/link.webp) Chain/Link icon 

El icono de enlace en las siguientes secciones, cuando está activado, hará que las opciones que se usen se compartan con las otras texturas (color, normal, roughness, metalness, opacity, emissive) que también tengan activado su icono de enlace. 

Esto te permite asegurarte de que, si tienes texturas alineadas, se mantendrán alineadas incluso si alteras parámetros o tipos de proyección.


### Projection
![](/images/material_projection.webp)

Define cómo se debe aplicar la textura al objeto.

* `Auto` - Si el objeto tiene uv's, UV; en caso contrario, Triplanar
* `UV` - Usa las coordenadas UV de la malla para aplicar la textura. Si la malla y la textura vienen de fuera de Nomad, o se van a exportar desde Nomad para usarse en otro lugar, UV es la opción correcta.
* `Triplanar` - Proyecta la textura a lo largo de los ejes X, Y, Z y mezcla las uniones. 

### Triplanar
![](/images/material_triplanar.webp)

Las proyecciones triplanares son una forma potente pero sencilla de aplicar texturas a objetos.

Triplanar es como tener 6 proyectores de vídeo con la misma imagen, proyectando sobre la parte frontal, trasera, izquierda, derecha, superior e inferior de tu objeto.

Esto luego se puede hornear en UVs o colores por vértice si es necesario.


![](/images/material_triplanar_example.webp)

#### Method

* `Local` - La proyección se moverá con la transformación del objeto
* `World` - La proyección permanece fija; mover el objeto lo deslizará a través de la proyección.

#### Hardness

Cómo se mezclan las proyecciones. 100% no hará mezcla y los bordes de las proyecciones serán nítidos. 0% mezclará los bordes en un ángulo amplio. El valor predeterminado es 90%, suficiente mezcla para ocultar los bordes y permitir que el resto de las proyecciones permanezcan nítidas.

### Uniform

Cuando está activado, se usa la misma dureza para todas las proyecciones. Cuando está desactivado, se exponen controles de dureza adicionales para las proyecciones X, Y, Z.


### Parameter
![](/images/material_parameter.webp)

#### Filtering
El método de filtrado de textura a usar; `Auto` es el valor predeterminado. Los métodos son `Nearest`, `Linear`, `Mipmap`. Nearest no hace filtrado, por lo que las texturas pueden presentar artefactos dentados cuando se ven de cerca. Linear y Mipmap hacen un mejor filtrado, por lo que las texturas aparecen borrosas en lugar de dentadas de cerca.

#### Tiling-X
Si el parámetro Scale es mayor que 1, haciendo que la textura sea más pequeña que las UVs del objeto, cómo se repetirá la textura a lo largo del eje X. `None` significa sin repeticiones. `Repeat` hará copias de la textura. `Mirror` hará copias de la textura, con cada segunda copia invertida, lo que puede ayudar a ocultar artefactos de repetición.

#### Tiling-Y
Igual que Tiling-X, pero para el eje Y.

### Transform
![](/images/material_transform.webp)

Transformaciones 2D adicionales aplicadas a la textura en el espacio UV. El botón de reinicio restablece los valores predeterminados; el icono de cadena (cuando se seleccionan texturas distintas del color) vinculará o desvinculará la transformación para que sea la misma que la de la textura de color.

#### Translation
El desplazamiento X e Y de la textura

#### Rotation
La rotación de la textura

#### Scale
La escala de la textura; números más grandes harán que la textura sea más pequeña en el objeto. Usa los deslizadores Tiling-X y Tiling-Y para controlar lo que ocurre.

### Uniform scale
Cuando está desactivado, Nomad mostrará controles separados para Scale-X y Scale-Y.
