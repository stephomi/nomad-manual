# ![](/icons/image.webp) Fondo {#background}

Este menú controla el color de fondo de Nomad, así como cualquier imagen de referencia que se vaya a usar.

![](/images/background_overview.webp)

## Fondo {#type}
![](/images/background_selector.webp)

Hay tres opciones para el fondo de la vista.

* `Environment` - Muestra el mapa de entorno seleccionado en [Shading](shading). Esto se puede controlar adicionalmente con los controles de Blur y Exposure (brillo). 
* `Color` - Un color plano que puedes elegir.
* `Gradient` - Un degradado de color de arriba hacia abajo. El control deslizante Factor te permite determinar el punto medio del degradado.  

## Imagen de referencia {#reference}

![](/images/background_reference.webp)

Puedes añadir una imagen de tu elección en el fondo para usarla como referencia.
Puedes cambiar la posición y la escala, por ejemplo si quieres moverla a una esquina de la pantalla.

### ![](/icons/tool_transform.webp) Transformar {#transform}

Este botón te permitirá colocar la imagen de referencia de forma interactiva. Usa 2 dedos para desplazar, escalar y rotar la imagen de referencia hasta colocarla. La posición final se reflejará en los controles deslizantes de abajo:

* `Overlay` - al 0% la imagen de referencia siempre estará detrás de tus objetos, al 100% estará delante. 
* `Opacity` - Qué tan transparente es la imagen.
* `Position` - La posición X y Y de la imagen.
* `Rotation` - Rotación de la imagen.
* `Scale` - Escala de la imagen.


::: tip

Las cámaras y las imágenes de referencia están vinculadas. 

Esto significa que si configuras tu imagen de referencia para que se alinee con tu escultura, si creas una cámara desde el [menú Camera](camera), la posición, rotación y escala de la imagen de referencia también se almacenan con la cámara. Puedes desactivar la imagen de referencia, rotar a otra vista. Si vuelves a mirar a través de la cámara, la imagen de referencia se activará con los ajustes que usaste.

¡Esto incluso incluye elegir imágenes diferentes para cámaras diferentes!

 ![](/videos/reference_camera.mp4)

:::