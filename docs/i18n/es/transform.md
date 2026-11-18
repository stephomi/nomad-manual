# ![](/icons/transform.webp) Transformar {#transform}

Este menú muestra en cifras la transformación del objeto seleccionado: dónde está, cómo está girado y escalado, y qué tamaño tiene. Escribe valores exactos, restablécelos u hornéalos en la malla.

![](/images/transform_overview.webp)

## Visión general {#overview}

Cada objeto tiene un nodo que guarda su traslación, rotación y escala (su matriz), además de sus vértices. Las herramientas [Gizmo](tools.md#gizmo) y [Transformar](tools.md#transform) cambian esa matriz cuando arrastras en la vista; este menú te permite leerla y escribir los valores directamente. Consulta [Nodos y vértices](tools.md#nodes-and-vertices) para ver la diferencia entre mover el nodo y mover los vértices.

Arrastra un valor a izquierda o derecha para cambiarlo, o tócalo para escribir un número. Los valores X, Y y Z se tiñen de rojo, verde y azul, como los ejes del gizmo.

::: tip
Escribir valores es práctico para colocar objetos con precisión, por ejemplo para poner varias piezas exactamente a la misma altura, o para devolver una rotación a un número redondo después de girar libremente con el gizmo.
:::

## Matriz {#matrix}

El título indica en qué espacio se expresan los valores: `local` (relativo al objeto padre) o `mundo`.

### Objeto y pivote {#object-pivot}

* `Objeto` - Los valores son la transformación propia del objeto.
* `Pivote` - Los valores mueven la selección desde su [pivote](tools.md#pivot), igual que las asas del gizmo: las filas marcan cero, y al cambiarlas la selección se mueve, gira o escala alrededor del pivote. Activa `Editar` (el icono del candado) para mover solo el pivote, sin que se muevan los objetos.

### Local y mundo {#local-world}

Cuando el objeto tiene un padre o hijos, o hay varios objetos seleccionados, puedes elegir en qué espacio se muestran los valores: `Local` (relativo al padre) o `Mundo`.

### Acciones {#actions}

| Acción        | Icono                         | Descripción |
| :-----------: | :---------------------------: | :---------- |
| Mover origen  | ![](/icons/target.webp)      | Lleva el objeto al origen del mundo. |
| Hornear       | ![](/icons/bake.webp)        | Aplica la matriz a los vértices y restablece la matriz. Visualmente no cambia nada, pero el origen del objeto pasa a ser el origen del mundo. |
| Pivote        | ![](/icons/gizmo.webp)       | Hornea el pivote en el objeto: el origen y la orientación del objeto pasan a ser los del pivote. Visualmente no cambia nada. |
| Editar        | ![](/icons/lock.webp)        | (Modo `Pivote`) Mueve solo el pivote. |
| Restablecer   | ![](/icons/reset.webp)       | Restablece la transformación a la identidad. En modo `Pivote`, en cambio, devuelve el pivote a su sitio. |

Si el objeto seleccionado tiene instancias, hornear pide confirmación, con una opción `Desinstanciar`: hornear cambia los vértices, que las instancias comparten.

### Traslación, rotación, escala {#translation-rotation-scale}

La posición, la rotación (en grados) y la escala del objeto, en X, Y y Z. Los dos botones al final de cada fila hornean en los vértices solo esa parte de la transformación, o la restablecen.

También aparece una fila `Cizallamiento` cuando el objeto está cizallado, por ejemplo después de escalar de forma no uniforme un padre girado.

### Escala uniforme {#uniform-scale}

Si está activada, la escala es un solo valor, igual en los tres ejes. Desactívala para escalar X, Y y Z por separado.

## Dimensión {#dimension}

El tamaño y el centro de la caja envolvente de la selección, en unidades del mundo. Con varios objetos seleccionados, abarca todos ellos.

* `Tamaño` - El ancho, el alto y la profundidad. Con el botón de enlace activado, al cambiar un tamaño los otros dos se escalan en la misma proporción, conservando las proporciones.
* `Centrada` - El centro de la caja envolvente. El botón de diana mueve la selección para que su centro quede en el origen del mundo.

::: tip
`Tamaño` es la forma más rápida de dar a un objeto un tamaño real, por ejemplo antes de una impresión 3d: indica la altura que quieres y el enlace conserva las proporciones.
:::
