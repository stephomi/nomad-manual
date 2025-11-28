# ![](/icons/history.webp) Historial {#history}
![](/images/history_overview.webp)

Como la mayoría de las herramientas de creación de contenido, puedes deshacer/rehacer todas las ediciones en Nomad.
Hay un límite en la cantidad de operaciones que se pueden deshacer, pero puedes controlar este comportamiento.

::: tip
Puedes usar gestos rápidos para deshacer/rehacer:
- Tocar con 2 dedos para deshacer
- Tocar con 3 dedos para rehacer
:::

## Historial {#history-panel}
![](/images/history_history.webp)

Este panel muestra la pila de historial, indicando el número de pasos, el nombre de la operación y la cantidad de memoria que está usando ese paso.

## Ajustes {#settings}
![](/images/history_settings.webp)

### Límite del historial (Mb) {#history-limit-mb}
Si la pila de historial excede este valor, las operaciones más antiguas se eliminarán para que el presupuesto de memoria se ajuste a este límite.


### Máximo de deshacer {#maximum-undoable}
Puedes controlar el número máximo de operaciones.

## Restaurar cámara {#restore-camera}
Para cada operación, se guarda el punto de vista de la cámara.
Si activas esta opción, deshacer o rehacer una operación restablecerá la cámara al punto de vista guardado.

## Incluir acciones {#include-actions}

* `Luces` - Cuando está desactivado, las operaciones de luz (aparte de los movimientos del gizmo) serán ignoradas por la pila de historial
* `Matcaps y HDRIs` - Cuando está desactivado, los cambios en matcaps y HDRIs serán ignorados por la pila de historial
* `PostProcess` - Cuando está desactivado, los cambios en las opciones de postprocesado serán ignorados por la pila de historial

## Estadísticas de memoria {#memory-stats}

Esta sección ofrece un desglose de la memoria utilizada por Nomad.