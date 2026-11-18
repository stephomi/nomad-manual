# ![](/icons/camera.webp) Cámara {#camera}

Este menú te permite crear y modificar cámaras, y también controlar cómo interactúas con ellas.

![](/images/camera_overview2.webp)

Las cámaras de Nomad tienen varios usos:

* Preparar vistas para esculpir desde ángulos precisos
* Usarlas como una cámara de fotos para encuadrar tus objetos
* como cámara en primera persona para recorrer tu escena
* como cámara ortográfica para juegos isométricos o renders de estilo industrial.

## Controlar la cámara {#control}

### Rotación {#rotation}
La cámara se gira arrastrando *un* dedo sobre el fondo.
Si arrastras el dedo sobre tu modelo, en cambio, empezarás a esculpir.

::: tip ¿Puedo girar la cámara si no llego al fondo?
Sí: pon *dos* dedos en la pantalla, como si fueras a hacer un gesto de desplazamiento o zoom, y luego levanta *uno* de ellos.
:::

### Centrar / Restablecer {#focus}
*Pulsa dos veces* sobre el modelo para centrar la vista en el punto tocado.
Si *pulsas dos veces* en el fondo, la cámara se centra en la malla seleccionada o en toda la escena; consulta [Pulsar dos veces en el fondo](#dtap-tap-background).


### Traslación {#translation}
Moviendo *dos* dedos puedes desplazar la cámara.


### Zoom {#zooming}
Con el gesto de pellizcar puedes acercar o alejar la vista.


### Inclinación {#rolling}
Puedes *inclinar* la vista girando *dos* dedos.
::: warning
Este gesto solo está disponible en los modos de rotación `Trackball`.
:::

### Controles de escritorio {#desktop}

En escritorio, la tecla alt/opt sirve para controlar la cámara:

* arrastrar con la punta en el espacio vacío = girar la cámara
* alt + arrastrar con la punta = desplazar
* alt + arrastrar con la punta y luego soltar alt = zoom (igual que en zbrush)

Con las tabletas Wacom cuyo lápiz tiene 2 botones o más, configura la punta y los botones así en los ajustes de Wacom:

* punta = clic izquierdo
* botón inferior = clic central
* botón superior = clic derecho

Con estos ajustes puedes manejar la cámara solo con el lápiz:

* botón superior y mover el lápiz sin tocar = girar la cámara
* botón inferior y mover el lápiz sin tocar = desplazar

## Controles de la cámara {#camera-controls}

![](/images/camera_list.webp)

### Vistas {#views}
Puedes guardar puntos de vista de la cámara con `Añadir vista`.
Si pulsas en el nombre de la vista, la cámara recupera esa vista.


::: tip
Una vista guardada conserva los ajustes de [Tipo de proyección](#projection) y también la [imagen de referencia](background.md).  
Es útil si quieres alternar entre vistas de referencia frontal, izquierda y trasera con fondos distintos.
:::

| Acción      | Icono                         | Descripción                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibilidad | ![](/icons/eye_open.webp)    | Activa o desactiva la cámara. Los botones anterior/siguiente se saltan las cámaras ocultas |
| Nombre      |                               | Selecciona la cámara                                                        |
| Imagen      | ![](/icons/image.webp)       | Una miniatura de la imagen de referencia, si está vinculada a la cámara     |
| Proyección  | ![](/icons/perspective.webp) | La proyección de la cámara, con su campo de visión cuando está en perspectiva |
| Actualizar vista | ![](/icons/update_view.webp) | Actualiza la vista guardada con el punto de vista actual               |
| Editar nombre | ![](/icons/pencil.webp)    | Edita el nombre de la cámara                                                |
| Eliminar    | ![](/icons/trash.webp)       | Elimina la cámara                                                           |

### ![](/icons/camera_add.webp) Añadir vista {#add}
Crea una cámara nueva a partir de la vista actual.

### ![](/icons/camera.webp) Iconos {#icons-test}

Muestra u oculta los iconos de las cámaras en la vista. El botón aparece junto a `Añadir vista` en cuanto tienes una cámara. Si hay una cámara seleccionada, su icono siempre se ve.

### Tipo de proyección {#projection}
Elige entre `Perspectiva` y `Ortográfica`.

En perspectiva, puedes cambiar el `Campo de visión vertical` (FoV) de la cámara. Encima del regulador se muestra la distancia focal equivalente en una cámara de 35 mm, algo práctico si estás acostumbrado a la fotografía.
Para esculpir se suele recomendar un FOV bajo, ya que ayuda con las proporciones.  
El modo `Ortográfica` equivale más o menos a un FOV igual a 0.

### Primera persona {#fps}
Solo en perspectiva. Coloca el pivote directamente sobre la cámara en lugar de sobre la escultura. Al arrastrar un dedo sobre el fondo, la posición de la cámara queda fija y solo cambia su rotación, como en los juegos en primera persona. Es útil cuando esculpes entornos en lugar de objetos sueltos.

![](/images/camera_rotation_ortho_view.webp)

### Tipo de rotación {#rotation-type}
Por defecto, la cámara usa el modo de rotación `Plataforma giratoria`.
Esto significa que solo tienes dos grados de libertad; es más intuitivo, pero en algunos casos querrás más flexibilidad.  
Puedes cambiar a `Trackball` y así podrás *inclinar* la vista girando *dos* dedos sobre ella. Hay dos modos `Trackball`: el primero hace rodar la vista como una bola bajo tu dedo, mientras que el segundo (el del icono de flechas) gira la vista según el movimiento horizontal y vertical de tu arrastre, lo que a algunos usuarios les resultará más familiar.

### Ajuste ortográfico {#orthographic}

Si está activado y tienes un teclado, mantener pulsada la tecla shift mientras giras la vista ajusta la cámara a la vista frontal, trasera, superior, inferior, izquierda o derecha más cercana, y la vuelve ortográfica. La cámara también se vuelve ortográfica al pulsar el cubo de vista para saltar a la vista frontal, trasera, izquierda, derecha, superior o inferior.

### Restablecer vista {#reset}

Lleva la cámara al frente y encuadra la escena en la vista

### Ajustar vista {#snap}
Ajusta la vista a la vista frontal, trasera, izquierda, derecha, superior o inferior más cercana. Si ya estás en una de ellas, al pulsar de nuevo salta 180 grados al lado opuesto.

### Velocidad {#speed}

Si notas que la cámara se mueve demasiado despacio o demasiado rápido, puedes ajustar un multiplicador de velocidad para `Rotación`, `Zoom` y `Traslación`. Es útil si tu escultura es muy grande o muy pequeña.

### El pivote {#pivot}

Al girar la cámara verás un pequeño punto rosa: es el punto de pivote de la cámara.  
Es muy importante entender dónde está el pivote para no perderte ni frustrarte con la cámara.

Por defecto, el pivote se actualiza con estas acciones:
- pulsar dos veces sobre el modelo
- pulsar dos veces en el fondo (el nuevo pivote estará en el centro de tu malla)
- poner *dos* dedos en la pantalla (desplazar/zoom/inclinar) coloca el pivote en el centro de los *dos* dedos

### Actualizar pivote... {#update-pivot}

Puedes personalizar aún más cuándo se actualiza el pivote con estas opciones:

* `Al mover la cámara` - Actualiza el pivote cuando empiezas a mover la cámara.
* `Permitir pivote en el aire` - Permite un nuevo pivote aunque hagas zoom fuera de la superficie del objeto. Requiere `Al mover la cámara`.
* `Al pulsar dos veces` - Actualiza el pivote de rotación cuando pulsas dos veces sobre la superficie del objeto.
* `Esculpir` (Trazo) - Actualiza el pivote cuando esculpes.

::: tip
Cuando te acostumbres, puedes ocultar el punto rosa (de ayuda) desde el menú [Configuración](settings.md).
:::

### Centrar vista al alejar {#center-view-when-zooming-out}
Al alejar la vista, la cámara no se desplaza hacia los lados: solo retrocede, así que la vista se mantiene centrada.

### Pulsar dos veces en el objeto {#dtap-object}
Si está activado, al pulsar dos veces sobre un objeto la cámara se centra en el punto tocado.

### Pulsar dos veces en el fondo {#dtap-tap-background}
Si está activado, al pulsar dos veces en el fondo la cámara se centra en:
* `Selección` - Los objetos seleccionados.
* `Escena` - Toda la escena.
* `Activar/desactivar` - Alterna entre las dos opciones con cada doble pulsación. Hay dos opciones `Activar/desactivar`, que se diferencian en cuál va primero, como muestran sus iconos.
