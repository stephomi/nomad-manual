# ![](/icons/history.webp) Historial {#history}
![](/images/history_overview.webp)

Como en la mayoría de las herramientas de creación de contenido, en Nomad puedes deshacer y rehacer cualquier edición.
El historial puede crecer mucho, así que tú decides cuánto se queda en memoria, cuánto se guarda en el almacenamiento y si se guarda con tu proyecto.

::: tip
Puedes usar gestos rápidos para deshacer y rehacer:
- Toque con 2 dedos para deshacer
- Toque con 3 dedos para rehacer
:::

## ![](/icons/history.webp) Historial {#history-panel}
![](/images/history_history.webp)

Este panel muestra la pila del historial: el número de pasos, el nombre de la operación, el objeto al que se aplicó y la memoria que ocupa ese paso.

Pulsa una entrada para volver atrás (o adelante) a ese estado. Mantén pulsada una entrada para borrar definitivamente esa entrada y todo el historial más antiguo, una forma rápida de liberar memoria cuando ya estés contento con tu escultura.

### ![](/icons/speed.webp) Reproducir {#replay}
El botón de reproducción, abajo a la izquierda, rebobina hasta la raíz y luego rehace las operaciones una a una: una forma divertida de ver cómo se construye tu escultura. El regulador ajusta la velocidad en operaciones por segundo. Vuelve a pulsar el botón para detenerla; también se detiene al deshacer o rehacer, o al pulsar una entrada.

Antes de empezar, una ventana emergente te permite elegir:
* `Reverso` - Deshace desde el estado actual hasta la raíz, en lugar de reproducir desde la raíz.
* `Restaurar cámara` - La cámara sigue las operaciones reproducidas, aunque [Restaurar cámara](#restore-camera) esté desactivado.
* `Suavizado de cámara` - La cámara se desliza suavemente entre las vistas en lugar de saltar de una a otra. Los valores altos dan una cámara más tranquila.

::: warning
La reproducción es experimental.
:::

## Incluir acciones {#include-actions}

Los iconos de la parte inferior del panel Historial eligen qué tipo de ediciones se registran en el historial:

| Acción       | Icono                         | Descripción                                                                         |
| :---------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Luces       | ![](/icons/light.webp)        | Ediciones de luces. Mover una luz con el Gizmo siempre se registra, ya que puede afectar a otros objetos de la jerarquía de la escena |
| Sombreado   | ![](/icons/sun.webp)          | El modo PBR, MatCap y Sin iluminación, los MatCaps y los HDRI                       |
| Posprocesado | ![](/icons/postprocess.webp) | Ediciones del posprocesado                                                          |
| Selección   | ![](/icons/tool_lattice.webp) | Ediciones de la selección del Enrejado, como clics, selecciones con lazo y deseleccionar |

## Configuración {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Restaurar cámara {#restore-camera}
Para cada operación se guarda el punto de vista de la cámara.
Si activas esta opción, al deshacer o rehacer una operación la cámara vuelve al punto de vista guardado.

### ![](/icons/history.webp) Guardar historial {#save-history}
Conserva el historial de deshacer al guardar el proyecto, para que siga ahí cuando lo vuelvas a abrir. Desactívalo para que tus archivos de proyecto ocupen menos.

### ![](/icons/ram.webp) Límite de RAM {#history-limit-mb}
La cantidad máxima de historial que se mantiene en la RAM. Los estados más antiguos se trasladan al almacenamiento y se vuelven a cargar cuando hacen falta; no se borran.

### ![](/icons/save.webp) Límite de almacenamiento {#storage-limit}
La cantidad máxima de almacenamiento que usa el historial de este proyecto. Cuando se alcanza el límite, las operaciones más antiguas se borran definitivamente.

::: tip
Un nuevo límite se aplica a partir de la siguiente edición, deshacer o rehacer.
:::

### ![](/icons/undo.webp) Aviso al deshacer {#maximum-undoable}
Retroceder más de este número de operaciones de una sola vez pide antes una confirmación. Si haces una edición después, todas las operaciones posteriores a ese punto se pierden, así que esto te protege de un toque accidental muy abajo en la lista.

## Estadísticas de memoria {#memory-stats}

Esta sección muestra un desglose de la memoria que usa Nomad.
