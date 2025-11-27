# ![](/icons/history.webp) Historial
![](/images/history_overview.webp)

Como la mayoría de las herramientas de creación de contenido, puedes deshacer/rehacer todas las ediciones en Nomad.
Hay un límite en la cantidad de operaciones que se pueden deshacer, pero puedes controlar este comportamiento.

::: tip
Puedes usar gestos rápidos para deshacer/rehacer:
- Tocar con 2 dedos para deshacer
- Tocar con 3 dedos para rehacer
:::

## Historial
![](/images/history_history.webp)

Este panel muestra la pila de historial, indicando el número de pasos, el nombre de la operación y la cantidad de memoria que está usando ese paso.

## Ajustes
![](/images/history_settings.webp)

### Límite de historial (Mb)
Si la pila de historial excede este valor, las operaciones más antiguas se eliminarán para que el presupuesto de memoria se ajuste a este límite.


### Máximo de operaciones deshacibles
Puedes controlar el número máximo de operaciones.

## Restaurar cámara
Para cada operación, se guarda el punto de vista de la cámara.
Si activas esta opción, deshacer o rehacer una operación restablecerá la cámara al punto de vista guardado.

## Incluir acciones

* `Luces` - Cuando está desactivado, las operaciones de luz (aparte de los movimientos del gizmo) serán ignoradas por la pila de historial
* `Matcaps y HDRIs` - Cuando está desactivado, los cambios en matcaps y HDRIs serán ignorados por la pila de historial
* `PostProcess` - Cuando está desactivado, los cambios en las opciones de postprocesado serán ignorados por la pila de historial

## Estadísticas de memoria

Esta sección ofrece un desglose de la memoria utilizada por Nomad.
