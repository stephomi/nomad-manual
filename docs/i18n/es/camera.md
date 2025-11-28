# ![](/icons/camera.webp) Cámara {#camera}

Este menú te permite crear y modificar cámaras, así como controlar cómo interactúas con ellas.

![](/images/camera_overview2.webp)

Las cámaras en Nomad tienen varios usos:

* Configurar vistas para esculpir desde ángulos precisos
* Usarlas como una cámara fotográfica para encuadrar tus objetos
* Como una cámara en primera persona para navegar por tu escena
* Como una cámara ortográfica para juegos isométricos o renderizados de estilo industrial.

## Controlar la cámara {#control}

### Rotación {#rotation}
Giras la cámara arrastrando *un* dedo sobre el fondo.
Si arrastras el dedo sobre tu modelo, en su lugar comenzará la operación de esculpido.

::: tip ¿Puedo rotar la cámara si no puedo acceder al fondo?
Sí, puedes poner *dos* dedos en la pantalla – como si quisieras iniciar un gesto de desplazamiento/zoom – y luego soltar *un* dedo.
:::

### Enfoque / Reinicio {#focus}
*Toca dos veces* sobre el modelo para enfocar el punto elegido.
Si *tocas dos veces* en el fondo, la cámara enfocará la malla seleccionada.

### Traslación {#translation}
Moviendo *dos* dedos, puedes desplazar (panear) la cámara.

### Zoom {#zooming}
Usando el gesto de pellizco puedes acercar/alejar la vista.

### Giro {#rolling}
Puedes *girar* la vista rotando *dos* dedos.
::: warning
Este gesto solo está disponible para el modo de rotación `trackball`.
:::

### Controles de escritorio {#desktop}

En escritorio, la tecla alt/opt se usa para controlar la cámara:

* arrastrar con la punta en un espacio vacío = rotar la cámara
* alt+arrastrar con la punta = desplazar (pan)
* alt+arrastrar con la punta, luego soltar alt = zoom (igual que en ZBrush)

Con tabletas Wacom que tienen 2 o más botones en el lápiz, usa la configuración de Wacom para configurar la punta y los botones así:

* punta = clic izquierdo
* balancín inferior = clic central
* balancín superior = clic derecho

Con esas configuraciones, puedes manipular la cámara solo con el lápiz:

* balancín superior y movimiento en el aire = rotar la cámara
* balancín inferior y movimiento en el aire = desplazar (pan)

## Controles de la cámara {#camera-controls}

![](/images/camera_list.webp)

### Vistas {#views}
Puedes guardar puntos de vista de cámara usando `Add View`.
Si haces clic en el nombre de la vista, la cámara restaurará esa vista.

::: tip
Una vista guardada almacenará los ajustes de [Tipo de proyección](#projection-type) y también la [Imagen de referencia](background.md).  
Puede ser útil si quieres alternar entre vistas de referencia frontal/izquierda/trasera con diferentes fondos.
:::

| Acción      | Icono                         | Descripción                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibilidad | ![](/icons/eye_open.webp)    | Alternar la cámara. Las cámaras ocultas se omitirán con los botones anterior/siguiente |
| Nombre      |                               | Seleccionar la cámara                                                       |
| Imagen      | ![](/icons/image.webp)       | Miniatura de una imagen de referencia si está vinculada a la cámara        |
| Actualizar vista | ![](/icons/update_view.webp) | Actualizar la vista guardada con el punto de vista actual           |
| Editar nombre    | ![](/icons/pencil.webp)      | Editar el nombre de la cámara                                        |
| Eliminar         | ![](/icons/trash.webp)       | Eliminar la cámara                                                   |

### ![](/icons/tool_view.webp) Añadir vista {#add}
Crear una nueva cámara basada en la vista actual.

### ![](/icons/camera.webp) Iconos {#icons-test}

Alternar si los iconos de cámara son visibles en el visor. Si una cámara está seleccionada, su icono siempre es visible.

### Tipo de proyección {#projection}
Puedes cambiar el `Field of View` (FOV / distancia focal) de tu cámara.
Normalmente se recomienda usar un FOV bajo para esculpir, ya que puede ayudar con las proporciones.  
También puedes usar el modo `Orthographic`, que es más o menos similar a un FOV igual a 0.

### Primera persona {#fps}
Activa que el pivote esté directamente en la cámara, en lugar de en la escultura. Arrastrar un dedo sobre el fondo mantendrá fija la posición de la cámara, pero cambiará la rotación, de forma similar a cómo funcionan los juegos en primera persona. Útil al esculpir entornos en lugar de objetos individuales.

![](/images/camera_rotation_ortho_view.webp)

### Tipo de rotación {#rotation-type}
Por defecto la cámara usa el modo de rotación `Turntable`.
Significa que solo tienes dos grados de libertad; es más intuitivo, pero en algunos casos querrás más flexibilidad.  
Puedes cambiar a `Trackball`, y podrás *girar* la vista rotando *dos* dedos en el visor. En escritorio hay un modo alternativo de trackball que puede resultar más familiar para algunos usuarios.

### Ajuste ortográfico {#orthographic}

Cuando está activado, si tienes un teclado, mantener pulsada la tecla Shift mientras rotas la vista ajustará la cámara a la vista frontal/trasera/superior/inferior/izquierda/derecha más cercana y hará la cámara ortográfica. La cámara también se hará ortográfica cuando se haga clic en el cubo de vista para ajustar a frontal/trasera/izquierda/derecha/superior/inferior.

### Restablecer vista {#reset}

Mover la cámara al frente y ajustar la escena para que encaje en la vista.

### Encajar vista {#snap}
Ajustar a la vista frontal/trasera/izquierda/derecha/superior/inferior más cercana. Si ya estás en una de esas vistas, al hacer clic de nuevo se ajustará 180 grados al lado opuesto.

### Velocidad {#speed}

Si sientes que la cámara se mueve demasiado lento o demasiado rápido, puedes establecer un multiplicador de velocidad para `rotation`, `translation` y `zooming`. Útil si tu escultura es muy grande o muy pequeña.

### Resumen del pivote {#pivot}

Cuando rotas la cámara puedes ver un pequeño punto rosa, este es tu punto de pivote de cámara.  
Es muy importante entender dónde está tu pivote para no perderte ni frustrarte con la cámara.

Por defecto el pivote se actualiza mediante estas operaciones:
- doble toque en el modelo
- doble toque en el fondo (el nuevo pivote estará en el centro de tu malla)
- poner *dos* dedos en la pantalla (pan/zoom/roll) actualizará el pivote al centro de los *dos* dedos

### Actualizar pivote... {#update-pivot}

Puedes personalizar aún más la actualización del pivote con estas opciones:

* When camera starts moving 
* Allow air pivot
* When double tapping
* Sculpt (stroke)

::: tip
Cuando te acostumbres, puedes ocultar el punto rosa (de ayuda) si vas al menú de [Settings](settings.md).
:::

### Doble toque en objeto {#dtap-object}
Cuando `Focus` está activado, tocar dos veces moverá el pivote al objeto tocado.

### Doble toque en fondo {#dtap-tap-background}
Cuando está activado, establece el pivote para que sea uno de Selección, Escena, o alternar entre ellos.