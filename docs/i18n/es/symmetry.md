# ![](/icons/symmetry.webp) Simetría

Este menú controla cómo se repetirán los trazos a través de un plano de espejo o de forma radial, y las formas de restaurar la simetría en objetos no simétricos.

![](/images/symmetry_overview.webp) 

## Descripción general 
Puedes usar la simetría de varias maneras:

* Como un espejo, invirtiendo el trabajo a través de X (izquierda/derecha), Y (arriba/abajo), Z (detrás/delante), o una combinación. 
* La simetría radial se puede configurar en X Y Z con un número de repeticiones, por ejemplo, esculpir una estrella de mar. 
* Los espejos pueden operar alrededor del origen (llamado modo mundo) o alrededor del centro de un objeto (llamado modo local).
* Esculturas que comenzaron siendo no simétricas pueden forzarse a ser simétricas.

Un atajo para activar/desactivar la simetría también se puede encontrar en el panel rápido de la izquierda (*"Sym"*). La pequeña 'L/W' indica si Nomad está en modo de simetría Local o Mundo. También puedes hacer una pulsación larga o deslizar hacia el centro de la pantalla para mostrar un menú.

![](/images/symmetry_button.webp) 

Esta es una opción global, por lo que el estado se mantendrá entre las diferentes herramientas.
Las únicas excepciones son las herramientas de transformación ([Mover](#translate), [Rotar](#rotate), [Escalar](#scale) y [Gizmo](#gizmo)) que tienen su propio estado de simetría.

::: tip
El menú de simetría es principalmente para controlar la simetría de los trazos. También puedes reflejar y repetir objetos mediante [repetidores que se encuentran en el menú de escena](scene#repeaters). 
:::

## Enabled
Activa el modo espejo, es lo mismo que el botón `Sym` en el panel rápido de la izquierda. 

## Planes

Activa plano(s) de simetría y el número de repeticiones para la simetría radial. Ten en cuenta que no tienes que elegir solo un plano; puedes tener 1, 2 o los 3 planos activados para una simetría compleja.

El eje y el recuento de repeticiones para la simetría radial. Ten en cuenta que estos tampoco están restringidos a un solo eje, e incluso pueden funcionar en combinación con la simetría de plano para generar resultados detallados muy rápidamente. (El número total de repeticiones está limitado a 150)

![](/videos/symmetry_demo.mp4) 

## Method
El espejo puede ser 'Local', y moverse con el objeto, o ser 'World' (Mundo), y no moverse. Si no estás seguro de qué modo necesitas, observa el plano de espejo y los indicadores radiales que se superponen sobre el objeto. En modo local, si usas el gizmo de transformación y mueves el modelo, los indicadores del espejo también se moverán. En modo mundo, los indicadores del espejo permanecerán fijos y el objeto se deslizará a través de ellos.

## Mirroring
![](/images/symmetry_mirroring.webp)

Al esculpir cerca de los planos de simetría, algunos pinceles tendrán un comportamiento de simetría imperfecto. Esta sección te permite restaurar la simetría copiando un lado de tu escultura al otro. 


`Direction` - Los botones `<<` y `>>` determinan qué lado se copiará al otro. Nomad calcula esto desde tu vista actual, así que, por ejemplo, al configurarlo en `<<` siempre copiará desde la derecha de la pantalla hacia la izquierda de la pantalla.

![](/icons/shield.webp) `Mask` - El botón de máscara te permite aislar lo que se reflejará; enmascarar el lado de destino protegerá esa región, enmascarar el lado de origen evitará que esa área se refleje en el destino. 

![](/icons/tool_hide.webp) `Hide` - Cuando está activo, las áreas que estén ocultas en el lado de origen no se reflejarán en el destino. 

`Mirror` intentará identificar si la topología es la misma en ambos lados del espejo y, de ser así, solo moverá vértices. Este es el escenario más común.

`Split & Mirror` esencialmente cortará el objeto a lo largo del espejo, copiará un lado, lo reflejará al otro y soldará los vértices a lo largo del espejo. Es una opción más destructiva y eliminará la multirresolución, pero a veces este método es necesario si el modelo es muy diferente a través del espejo.

### Flip object
![](/images/symmetry_flip.webp)
Hace que el lado izquierdo pase a ser el derecho y viceversa. Similar en apariencia a si usaras el menú de la herramienta gizmo y establecieras la escala en -1 en X.

## Reset and Edit

![](/images/symmetry_edit.webp)

Es posible editar la ubicación y la orientación de la simetría (¡pero no se recomienda!). Si es necesario, `World center` y `Orientation` restablecerán la ubicación y la orientación de la simetría a sus valores predeterminados.

Nomad normalmente sabe dónde colocar el plano de simetría. No se recomienda ajustar esto manualmente, pero el botón `Gizmo (Edit)` permite hacerlo a usuarios avanzados. Cuando se hace clic en este botón, se muestra un gizmo que permite trasladar y rotar el plano de simetría. Si quieres restaurar el centro y la orientación predeterminados, los botones `object center` y `orientation` lo harán.

El comportamiento de estas opciones cambiará dependiendo de en qué espacio (*Local/World*) te encuentres.
Así que si no funciona como esperas, asegúrate de comprobar si estás en el espacio correcto.

::: tip
¡El botón `Gizmo (Edit)` está intencionadamente atenuado como recordatorio de que probablemente no deberías usarlo!
:::

## Show options
![](/images/symmetry_show.webp)


`Show line` y `Show plane` activarán o desactivarán una superposición en la vista de las ubicaciones de simetría. Ten en cuenta que desactivar estas opciones solo tendrá efecto cuando el menú de simetría esté cerrado.
