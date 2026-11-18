# ![](/icons/symmetry.webp) Simetría {#symmetry}

Este menú controla cómo se repiten los trazos a través de un plano de espejo, de forma radial o en mosaico, y ofrece formas de restaurar la simetría en objetos que no son simétricos.

![](/images/symmetry_overview.webp) 

## Visión general {#overview}
Puedes usar la simetría de varias formas:

* Como espejo, reflejando el trabajo en X (izquierda/derecha), Y (arriba/abajo), Z (detrás/delante) o en una combinación de ellos.
* La simetría radial se puede ajustar en X Y Z con un número de repeticiones, por ejemplo para esculpir una estrella de mar.
* El mosaico repite tus trazos a lo largo del objeto, para que la escultura encaje sin costuras.
* Los espejos pueden funcionar alrededor del origen (modo mundo) o alrededor del centro de un objeto (modo local).
* Las esculturas que empezaron sin simetría se pueden volver simétricas a la fuerza.

En el panel rápido de la izquierda también hay un atajo para activar o desactivar la simetría (*"Sim"*). La pequeña 'L/W' indica si Nomad está en modo de simetría Local o Mundo. También puedes mantenerlo pulsado o deslizar hacia el centro de la pantalla para abrir un menú.

![](/images/symmetry_button.webp) 

Los ajustes de simetría se guardan con cada objeto, y el título del menú muestra el nombre del objeto que estás editando.
Las herramientas de escultura comparten el mismo estado activado/desactivado, mientras que las herramientas de transformación ([Transformar](tools.md#transform) y [Gizmo](tools.md#gizmo)) tienen el suyo propio.

::: tip
El menú de simetría sirve sobre todo para controlar la simetría de los trazos. También puedes reflejar y repetir objetos con los [repetidores del menú de escena](scene#repeaters).
:::

## ![](/icons/symmetry.webp) Activado {#enabled}
Activa o desactiva el modo espejo; es lo mismo que el botón `Sim` del panel rápido de la izquierda. Un icono de aviso te lo recuerda cuando está desactivado, y el menú también te indica cuando la herramienta actual ignora la simetría.

## Planos {#planes}

Activa los planos de simetría y el número de repeticiones de la simetría radial. No tienes por qué elegir un solo plano: puedes activar 1, 2 o los 3 planos para una simetría compleja.

La fila `Radial` define el número de repeticiones de la simetría radial alrededor de cada eje. Tampoco se limita a un solo eje, e incluso puede combinarse con la simetría de planos para obtener resultados detallados muy rápido. (El número total de repeticiones está limitado a 200).

![](/videos/symmetry_demo.mp4) 

## Mosaico {#tile}

Repite tus trazos a lo largo de un eje, a una distancia regular, para que la escultura encaje sin costuras. Es útil para patrones, ladrillos o una textura que piensas repetir.

Activa el mosaico en cada eje con los botones `Mosaico` y define una `Cantidad` (cuántas repeticiones caben en el objeto) o una `Distancia` (el espacio entre dos repeticiones). Toca el interruptor de la izquierda para cambiar entre ambas.

## Método {#method}
El espejo puede ser `Local`, y moverse con el objeto, o `Mundo`, y quedarse fijo. Si no sabes qué modo necesitas, fíjate en los indicadores del plano de espejo y radiales superpuestos sobre el objeto. En modo local, si usas las herramientas de transformación (`Gizmo` o `Transformar`) y mueves el modelo, los indicadores de espejo se mueven con él. En modo mundo, los indicadores se quedan fijos y el objeto se desliza a través de ellos.

## Espejo {#mirroring}
![](/images/symmetry_mirroring.webp)

Al esculpir cerca de los planos de simetría, algunos pinceles no tienen una simetría perfecta. Esta sección te permite restaurar la simetría copiando un lado de la escultura en el otro.

`Dirección` - Los dos botones de flecha junto al título `Espejo` determinan qué lado se copia en el otro. Nomad lo calcula a partir de la vista actual, así que el lado sigue siendo el mismo en pantalla, mires el modelo desde donde lo mires.

![](/icons/shield.webp) `Máscara` - El botón de máscara te permite aislar lo que se va a reflejar: enmascarar el lado de destino protege esa zona, y enmascarar el lado de origen impide que esa zona se refleje en el destino.

![](/icons/tool_hide.webp) `Ocultar` - Si está activo, las zonas ocultas del lado de origen no se reflejan en el destino.

`Espejo` (Mantener topología) intenta detectar si la topología es la misma a ambos lados del espejo y, si es así, simplemente mueve los vértices. Es el caso más habitual. La simetría radial se ignora. Si la topología no es simétrica, Nomad te ofrece forzar el reflejo con `Cortar • Espejo`.

Los botones `Cortar` cortan el objeto por el plano o los planos de simetría. Cambian la topología, así que son más destructivos que `Espejo`. El número de cada botón indica cuántos objetos obtienes:

* `Cortar` - elimina un lado del objeto.
* `Cortar • Espejo` - corta el objeto, copia un lado, lo refleja en el otro y suelda los vértices a lo largo del espejo. A veces este método es necesario si el modelo es muy distinto a cada lado del espejo.
* `Cortar • Dividir` - corta el objeto y conserva cada lado como un objeto independiente.
* `Cortar • Espejo • Dividir` - como `Cortar • Espejo`, pero cada lado se convierte en un objeto independiente.

Si hay varios objetos seleccionados, `Espejo` y [Voltear objeto](#flip-object) se aplican a todos ellos.

### Voltear objeto {#flip-object}
![](/images/symmetry_flip.webp)
Pasa el lado izquierdo a la derecha y viceversa, en `X`, `Y` o `Z`. El resultado se parece a usar el menú de la herramienta gizmo y poner la escala a -1 en X.

## Restablecer y editar {#reset-and-edit}

![](/images/symmetry_edit.webp)

Es posible editar la posición y la orientación de la simetría (¡aunque no se recomienda!). Si hace falta, `Centro del mundo` (`Centro del objeto` en modo local) y `Orientación` restablecen la posición y la orientación de la simetría a sus valores por defecto.

Normalmente Nomad sabe dónde colocar el plano de simetría. No se recomienda ajustarlo a mano, pero el botón `Editar gizmo` lo permite a los usuarios avanzados. Al pulsarlo, aparece un gizmo para mover y girar el plano de simetría. Si quieres recuperar el centro y la orientación por defecto, usa los botones de restablecer de arriba.

`Desde pivote` coloca el plano de simetría en el pivote de la herramienta [Gizmo](tools.md#gizmo). Solo está disponible mientras la herramienta `Gizmo` está activa.

El comportamiento de estas opciones cambia según el espacio (*Local/Mundo*) en el que estés.
Así que, si no funciona como esperas, comprueba que estás en el espacio correcto.

::: tip
Editar el plano de simetría con el gizmo es algo experimental: ¡lo más probable es que no lo necesites!
:::

## Opciones de visualización {#show-options}
![](/images/symmetry_show.webp)


`Mostrar línea` y `Mostrar plano` muestran u ocultan en la vista una superposición con la posición de la simetría. Ten en cuenta que, al desactivar estas opciones, el cambio solo se aplica cuando se cierra el menú de simetría.
