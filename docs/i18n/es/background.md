# ![](/icons/image.webp) Fondo {#background}

Este menú controla el color de fondo de Nomad y las imágenes de referencia que quieras usar.

![](/images/background_overview.webp)

## Tipo {#type}
![](/images/background_selector.webp)

Hay tres opciones para el fondo de la vista.

* `Entorno` - Muestra el mapa de entorno elegido en [Sombreado](shading.md). Puedes ajustarlo con los reguladores `Desenfoque` y `Exposición` (brillo). 
* `Color` - Un color plano que eliges tú
* `Degradado` - Una transición entre dos colores. El regulador `Factor` te permite desplazar el punto medio del degradado.  

### Tipo de degradado {#gradient-type}
Con `Degradado`, elige su forma:
* `Lineal` - Un degradado recto; su dirección se ajusta con el regulador `Ángulo`.
* `Radial` - Un degradado circular que parte del centro de la pantalla.
* `Cielo` - Un degradado anclado al horizonte del mundo, así que sigue a la cámara cuando miras hacia arriba o hacia abajo.

Cada color tiene un botón para restablecerlo y un cuentagotas, para tomar un color de la pantalla.

## ![](/icons/lock.webp) Sincronizar con bloqueo de cámara {#sync-on-camera-lock}
Cuando la cámara está bloqueada con el [Cubo de ajuste](settings.md#snap-cube), la imagen de referencia sigue el movimiento de la cámara, de modo que se mantiene alineada con tu escultura.

* `Permitir giro (Trackball)` - Permite que la cámara gire sobre sí misma al salir del bloqueo de cámara.
* `Restablecer vista al desbloquear` - Restablece la vista al salir del bloqueo de cámara.

## Imagen de referencia {#reference}

![](/images/background_reference.webp)

Puedes poner en el fondo la imagen que quieras para usarla como referencia. Pulsa `Importar...` para añadir una y luego marca `Imagen de referencia` para mostrarla.
Puedes cambiar su posición y su escala, por ejemplo si quieres llevarla a una esquina de la pantalla.

### ![](/icons/tool_transform.webp) Transformar {#transform}

Este botón te permite colocar la imagen de referencia de forma interactiva. Usa 2 dedos para desplazar, escalar y rotar la imagen de referencia hasta su sitio. `Restablecer configuración` devuelve la imagen a su colocación por defecto. La colocación final se refleja en los reguladores de abajo:

* `Superposición` - Al 0 % la imagen de referencia queda siempre detrás de tus objetos; al 100 %, delante. 
* `Opacidad` - Lo transparente que es la imagen.
* `Posprocesado` - Aplica los efectos de posprocesado a la imagen de referencia. Desactívalo para conservar los colores originales.
* `Posición X` / `Posición Y` - La posición X e Y de la imagen.
* `Escala` - La escala de la imagen.
* `Rotación` - La rotación de la imagen.


::: tip

Las cámaras y las imágenes de referencia están vinculadas. 

Esto significa que, si colocas tu imagen de referencia alineada con tu escultura y creas una cámara desde el [menú Cámara](camera.md), la posición, la rotación y la escala de la imagen de referencia se guardan también con la cámara. Puedes desactivar la imagen de referencia y girar hacia otro punto de vista. Cuando vuelvas a mirar a través de esa cámara, la imagen de referencia se activará con los ajustes que usaste.

¡Incluso puedes elegir imágenes distintas para cada cámara!

 ![](/videos/reference_camera.mp4)

:::
