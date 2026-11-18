# ![](/icons/operation.webp) Operación {#operation}

Este menú aplica una operación a toda la superficie de los objetos seleccionados de una sola vez: suavizar, relajar, pulir, inflar, ajustar los colores, desenfocar o enfocar la pintura y la máscara.

![](/images/operation_overview.webp)

## Visión general {#overview}

Mientras que un pincel actúa donde pasas el trazo, una operación actúa sobre todos los vértices de los objetos seleccionados de una vez. El título muestra el nombre del objeto, o el número de objetos cuando hay varios seleccionados.

Cada operación es un regulador: arrástralo a la derecha para aplicar más, o a la izquierda para aplicar menos (o la operación contraria, en los reguladores con una flecha a cada lado). El regulador vuelve a cero en cuanto lo sueltas, y cada arrastre es un solo paso en el [Historial](history.md), así que puedes aplicar una operación varias veces en pequeñas dosis.

::: tip
Las operaciones son una forma rápida de limpiar una malla entera después de un remallado por vóxeles o de una booleana: un poco de `Relajar` iguala los triángulos y un poco de `Suavizar` elimina el ruido, sin tener que buscar cada zona con un pincel.
:::

## Filtros {#filters}

Los botones de arriba limitan dónde se aplican las operaciones:

* `Máscara` - Las zonas enmascaradas no se modifican.
* `Ocultar` - Las zonas ocultas no se modifican.
* `Desplazamiento` - (Con una [capa](layers.md) seleccionada) Solo se ven afectadas las zonas donde la capa activa contiene escultura, así que puedes suavizar o inflar el contenido de una capa sin tocar el resto.

## Suavizado {#smoothing}

* `Conservar volumen` - Suaviza sin encoger la superficie. El botón del engranaje contiene las cantidades de `Encoger` e `Inflar` que se usan para ello.
* `Conservar bordes` - Los vértices del borde de la malla (el contorno de un agujero) no se mueven.
* `Suavizado estable` - Intenta que el suavizado no dependa de la topología. Funciona mejor cuando la densidad de polígonos varía mucho.
* `Suavizar` - Suaviza la superficie. Arrastra a la izquierda para `Enfocar` en su lugar.
* ![](/icons/group.webp) `Suavizar` - Suaviza los bordes entre [grupos de caras](tools.md#facegroup) y endereza los contornos dentados de los grupos. Arrastra a la izquierda para hacerlos más nítidos.
* `Relajar` - Iguala los polígonos y conserva la forma.
* ![](/icons/group.webp) `Relajar` - Relaja los polígonos a lo largo de los bordes de los grupos de caras.
* `Conservar esquinas` - Con `Suavizar` y `Relajar` de los grupos de caras, los bordes se quedan fijos donde giran más de este ángulo, de modo que las esquinas siguen nítidas mientras los lados se suavizan. Actívalo con su casilla.

## Pulir {#polish}

Aplana la superficie en facetas limpias, como la herramienta [Pulir](tools.md#polish). `Ángulo` decide qué caras se aplanan juntas: las caras que se doblan menos que este ángulo forman una sola faceta. Un ángulo menor conserva más pliegues y facetas más pequeñas.

## Inflar {#inflate}

Empuja la superficie hacia fuera a lo largo de sus normales, o hacia dentro si arrastras a la izquierda. `Normal (Relajar)` relaja los polígonos a la vez para que no se estiren; desactívalo con su casilla.

## Ajustes de color {#color-adjustments}

Elige el canal que quieres ajustar, `Color`, `Rugosidad`, `Metalicidad`, `Opacidad`, `Densidad` (la pintura de densidad de [Quad Remesher](tools.md#quad-remesher), si el objeto la tiene) o `Máscara`, y luego:

* `Exposición` - Aclara u oscurece los valores.
* `Saturación` - (Solo `Color`) Colores más o menos vivos.
* `Contraste` - Separa los valores entre sí o los acerca.
* `Matiz` - Desplaza los colores por la rueda de color.

## Desenfoque {#blur}

Desenfoca los canales seleccionados por la superficie: activa `Color`, `Rugosidad`, `Metalicidad`, `Opacidad`, `Densidad` o `Máscara` y arrastra `Desenfoque`. Arrastra a la izquierda para `Enfocar` en su lugar.

Para la máscara, es lo mismo que el regulador `Desenfocar` de la herramienta [Máscara](tools.md#mask). Aquí también puedes desenfocar los canales de pintura.
