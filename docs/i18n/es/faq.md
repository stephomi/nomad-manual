# ![](/icons/faq.webp) Preguntas frecuentes {#faq}

[[toc]]

## Plataforma {#platform}
### ¿Dónde están mis proyectos en el dispositivo? {#locate}
Los proyectos están en la carpeta `projects`, dentro de la carpeta principal de Nomad.

En iOS, puedes acceder a la carpeta de Nomad con la aplicación Archivos de iOS.

En Android, la carpeta de Nomad está en `Android/data/com.stephaneginier.nomad/files/`.  
En las versiones recientes de Android (10/11), ya no tienes acceso a la carpeta `Android/data`.
Puedes acceder a ella con una aplicación aparte, por ejemplo [esta](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### ¿Hay alguna forma de probar la beta? {#beta}
Para Windows y MacOS, puede haber una beta disponible en la [página de inicio](https://nomadsculpt.com).
<br>
Para iOS hay un TestFlight privado: visita el canal #beta-ios del [Discord](https://discord.com/invite/8h7BwpRz29).
<br>
La [demo web](https://nomadsculpt.com/demo) suele actualizarse con las últimas funciones.

### ¿Por qué hay una prueba gratuita en Android y no en iOS? {#android-trial}
Porque los dispositivos Android antiguos son malísimos (y algunos recientes también...), y no quería que la gente comprara la aplicación y se encontrara con una pantalla negra.
Pero el motivo principal es que tenía la impresión de que las aplicaciones de pago no son lo habitual en Android.

### ¿Cuál es la mejor tableta para usar Nomad? {#best-tablet}

En resumen: un iPad.

La respuesta algo más larga es 

> «El iPad más nuevo _que te puedas permitir_, salvo que de verdad odies a Apple, en cuyo caso la tableta Samsung más nueva que te puedas permitir. Para cualquier otra, pruébala antes.» 

La gente siempre quiere más información, así que aquí va un resumen.

Nomad funciona mejor en los iPad más recientes:

* Los iPad y los iPhone tienen acceso al complemento [Quad Remesher](tools#quad-remesher) de [Exoside](https://exoside.com/)
* los iPad recientes con el último lápiz admiten el [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0): puedes girar el lápiz sobre sí mismo en ciertas herramientas de Nomad. 
* el rendimiento de los últimos chips de la serie M es muy alto. 

El iPad más nuevo y más caro podrá renderizar imágenes finales muy rápido y te permitirá esculpir muchísimo detalle.

Sin embargo, la caída de rendimiento con los iPad más baratos y antiguos no es tan grande como la gente espera. Cualquier iPad compatible con el Apple Pencil ejecuta Nomad bastante bien. Por ejemplo:

* Un iPad Pro de 2023 maneja esculturas de 5 millones de polígonos con fluidez, y una imagen con calidad final se renderiza en 5 segundos.
* Un iPad Pro de 2015 maneja un objeto de 1,2 millones de polígonos con algo de retraso, y una imagen con calidad final se renderiza en 20 segundos.

Es una gran diferencia de rendimiento, pero también hay que tener en cuenta el precio:

* El iPad Pro de 2025 cuesta *2500 USD* nuevo y con todas las opciones. 
* El iPad Pro de 2023 cuesta actualmente *400 USD* en eBay.
* El iPad Pro de 2015 cuesta *250 USD* en eBay.

¿Merece la pena pagar 2100 USD más por 4 millones de polígonos extra y 15 segundos menos? Eso lo decides tú.

Los modelos que no son Pro pueden ser aún más baratos y ofrecen una gran variedad de tamaños y rendimientos para elegir. El iPad Air actual admite el lápiz de 2.ª generación con barrel roll y es bastante más barato que el Pro. El mercado de segunda mano y de reacondicionados ofrece todavía más opciones. 

Así que, sea cual sea tu presupuesto, deberías poder encontrar un iPad para ti. ¡Y recuerda que la mayoría de las esculturas no tienen millones de polígonos! Si te mantienes por debajo de 500 000 polígonos, incluso los iPad antiguos te dejarán esculpir con rapidez.

`¿Y Android?`

El rendimiento gráfico en Android está por debajo del de los iPad. Según el desarrollador de Nomad, «una Samsung Galaxy Tab S9 ejecuta Nomad un orden de magnitud más lento que un iPad Air». Dicho esto, muchos usuarios están muy contentos con sus tabletas Samsung: Nomad funciona bien para la mayor parte del esculpido. 

Con otras tabletas Android, ten cuidado. El rendimiento del hardware Android varía mucho, y no es fácil prever cómo funcionará Nomad.

Usa primero la versión gratuita de Nomad, sin guardado, para probarlo. 

`¿Y la memoria y el almacenamiento?`

La mayoría de los archivos de Nomad ocupan 100 MB o menos. Esto significa que casi cualquier tableta que compres hoy, iPad o Android, tendrá espacio de sobra para tus proyectos de Nomad.


### Compré Nomad para un dispositivo, ¿puedo usarlo en otro? {#multi-devices}
Siempre que use la misma tienda de aplicaciones y la misma cuenta, sí.

Por ejemplo, si lo compraste en la App Store de iOS, puedes usarlo en tus otros dispositivos iOS.

Si lo compraste para tu tableta Android en Google Play, puedes usarlo en tus otros dispositivos Android.

Sin embargo, si compraste Nomad en Android y luego te haces con un iPad, tendrás que volver a comprarlo.

Esto se debe a que Nomad no tiene su propio servidor de licencias ni un modelo de suscripción. No hay ningún acuerdo entre Apple, Google y AppGallery para compartir licencias. 


### ¿Cómo restauro mi compra? {#restore}
Google Play y AppGallery se encargan de la sincronización automáticamente.

- Ve al menú Acerca de (el icono de Nomad arriba a la izquierda) y pulsa `Restaurar compra`
- Comprueba que has iniciado sesión con la misma cuenta con la que compraste Nomad (en Google Play).
- Reinicia el dispositivo
- A veces hay que esperar un par de horas
- Asegúrate de que la aplicación Google Play está actualizada
- Reinstala Nomad (haz antes una [copia de seguridad de tus archivos](#locate) si no quieres perder nada)
- Puedes intentar comprar de nuevo para ver qué pasa (nota: no se puede comprar dos veces el mismo artículo con la misma cuenta)

:::tip
Puedes contactar conmigo en <support@nomadsculpt.com>, pero lo *único* que podré hacer es confirmar si un correo electrónico tiene una compra asociada.

Ten en cuenta que recibo con frecuencia avisos de licencias que no se actualizan bien tras cambiar de dispositivo.
No tengo ningún control sobre el pago ni sobre la sincronización de las cuentas: ¡de todo eso se encargan Google y AppGallery!

Al final la compra siempre se restaura, pero no está claro qué pasos acelerarían el proceso.
:::

::: warning
Los dispositivos Huawei recientes no tienen acceso a los servicios de Google.
En ese caso, tendrás que volver a comprar la aplicación en AppGallery (la tienda de aplicaciones de Huawei).
:::

### ¿Puedes traducir o corregir [mi-idioma]? {#locale}
Puedo añadir otro idioma con relativa facilidad, pero uso traducción por IA porque es mucho más fácil de mantener con las actualizaciones frecuentes.
Los archivos de traducción están [aquí](https://github.com/stephomi/nomad-translation).

## Funciones {#features}

### ¿Por qué no se mueve el gizmo? {#gizmo-not-moving}
Puede que tengas activado [Fijar en la barra de herramientas del menú izquierdo](tools#left-menu-toolbar). 

### ¿Se puede animar en Nomad? {#animate}
De momento no. Una línea de tiempo que pudiera animar las capas podría ser interesante, pero ahora mismo no está realmente prevista.  

Me gustaría admitir rigging/skinning en el futuro, pero plantea algunos retos (sobre todo la interacción con las herramientas de esculpido...), así que de momento no hay nada seguro.


### ¿Se puede hacer modelado low poly de verdad? {#lowpoly}
De momento no.
No es realmente el ámbito de Nomad *Sculpt*, pero quizá añada algunas herramientas en el futuro.


### ¿Se pueden hacer UV y texturizado? {#texturing}
Respuesta corta: sí. Respuesta larga: no directamente, pero hay varias formas de combinar las excelentes herramientas de pintura de vértices de Nomad con UV y texturas.

* Nomad te permite pintar el color, la rugosidad y las propiedades del material directamente en los vértices de tu escultura.
* Nomad admite un número de vértices muy alto, para que puedas pintar sin preocuparte por las UV.
* Nomad puede cargar texturas para usarlas en los pinceles, lo que permite estampar y pintar con texturas.
* Nomad puede cargar objetos con texturas ya asignadas, para renderizarlos.
* Nomad puede [desplegar las UV](topology.md#uv-unwrap-uvatlas) de objetos con menos polígonos.
* El color, la rugosidad y la metalicidad se pueden transferir de las texturas a los vértices con [las opciones de proyección](topology.md#reproject-to-vertex).
* El color, la rugosidad, la metalicidad y las normales se pueden hornear de los vértices a las texturas con [las opciones de horneado](topology.md#bake-texture)
* El horneado y la proyección se pueden hacer entre objetos sueltos o entre muchos objetos, o entre los niveles de subdivisión más alto y más bajo de un mismo objeto, lo que permite muchos flujos de trabajo de horneado y proyección.
* Después del horneado, al exportar un OBJ también se exportan las texturas, que puedes llevar a una aplicación como Procreate para pintar directamente sobre ellas.

### ¿Puedo grabar un vídeo de una plataforma giratoria? {#video}
De momento no está previsto, pero iOS tiene una [función de grabación de vídeo](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) muy fácil de usar.

En iOS, se hace deslizando hacia abajo desde la esquina superior izquierda y tocando el botón de grabar. Tendrás una cuenta atrás de 3 segundos: desliza el menú para que aparezca Nomad y usa la función de plataforma giratoria. Al terminar, vuelve a deslizar hacia abajo desde la esquina superior derecha y toca otra vez el botón de grabar. Edita el vídeo desde la fototeca para quitar lo que sobra al principio y al final.

### ¿Puedes añadir [mi-función-favorita] como botón principal? {#interface}
Sí, ahora la barra de herramientas inferior se puede personalizar desde el menú [Interfaz](interface.md#shortcuts), y también se pueden crear barras de herramientas flotantes.

### ¿Cuáles serán las próximas funciones? {#next-features}
Para la hoja de ruta a medio y largo plazo tengo muchas ideas, pero aún no lo sé.  

Corregir errores y mejorar las funciones existentes siempre tendrá más prioridad que añadir funciones nuevas.


### ¿Se puede hacer rigging en Nomad? {#rigging}
No, pero está previsto. De momento puedes emparentar formas y cambiar los puntos de pivote, lo que permite esculturas sencillas que se pueden posar.

### ¿Se pueden usar más de 4 luces? {#lights}
Puedes usar hasta 4 luces en móvil y hasta 6 en escritorio. Es una limitación del motor de render en tiempo real de Nomad. Se puede simular con objetos emisivos y la iluminación global del posprocesado, como se muestra en [este tutorial](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### ¿Se pueden importar herramientas de ZBrush? {#zbrush-import}
No, ZBrush usa un formato propietario. Deberías poder extraer los mapas alfa y usarlos en Nomad. 

### ¿Por qué los colores no coinciden con lo que pinté? ¿Por qué no consigo un blanco en el render? {#paint-pbr}
Imagina que haces una foto a una hoja de papel, otra a una lámpara de escritorio y otra al sol. Las cámaras y pantallas antiguas lo mostrarán todo «blanco». Los sistemas más modernos pueden mostrar la diferencia entre el blanco reflejado del papel, la luz emitida por una lámpara y el brillo intensísimo del sol.

Los gráficos por ordenador modernos intentan funcionar de forma parecida, imitando la física de la luz y de las superficies. Esto se llama `Renderizado basado en la física`, o PBR, y el renderizador PBR de Nomad se basa en ello. El resultado es realista y equilibrado, pero a menudo los colores pintados muy vivos se ven más oscuros.

Si necesitas que el render se parezca más a los colores pintados, puedes arreglarlo de formas no basadas en la física y de formas basadas en la física:

Sin PBR:
* `Usa el modo 'Sin iluminación' del menú Sombreado`. Los colores se muestran exactamente como los pintaste, pero también pierdes todo el sombreado. Práctico para comprobaciones rápidas y para un resultado más gráfico.
* `Usa el modo 'MatCap' del menú Sombreado`. Elige un matcap más claro, casi blanco, sin ningún tinte de color.

Con PBR:
* `Usa un entorno neutro`. Puedes [cambiar el entorno](shading.md#environment) por uno más neutro. Evita los entornos de interior, que suelen tener más color. Mejor un entorno exterior de día o de estudio.
* `Aumenta la iluminación`. Si estuvieras fotografiando un papel blanco en una habitación oscura, simplemente añadirías más luz. En la luz de entorno, sube el regulador de exposición hasta que los colores te parezcan correctos, o añade más luces con más intensidad.
* `Aumenta la exposición de la cámara`. Si la habitación oscura no tuviera más luces, podrías dejar el obturador abierto más tiempo o usar un ISO más sensible. En Nomad puedes conseguir algo parecido con el posprocesado. Ve a Posprocesado, actívalo, baja hasta Mapeo de tonos, actívalo y sube el regulador de exposición hasta que los colores te parezcan correctos.
* `Usa un color emisivo`. En el menú Material, puedes activar 'Emisivo' en las texturas, y el objeto parecerá una fuente de luz. Si activas la iluminación global en los ajustes de posprocesado, proyectará luz sobre los demás objetos de la escena. También puedes activar 'Siempre sin iluminación' para ese material, que da un aspecto parecido sin textura.

## Cierres inesperados {#crashes}

### ¡Se cierra cuando guardo o remallo mi modelo! {#crash-remesh}
Tu dispositivo se está quedando sin memoria (RAM).  
Para reducir el uso de memoria de tu escena, puedes usar algunas de las opciones de [Topología](topology.md) para reducir el número de polígonos.

::: tip RAM/almacenamiento
Lo que importa es la cantidad de RAM, no el almacenamiento (que suele ser mucho mayor).
:::


### ¡Se cierra cuando cargo mi proyecto! {#crash-load}
Si el archivo es pequeño, puedes enviármelo y le echaré un vistazo (por correo electrónico a <support@nomadsculpt.com>).

Si no, lo más probable es que el dispositivo se esté quedando sin memoria RAM.

- Asegúrate de cerrar las demás aplicaciones abiertas en tu dispositivo.
- Empieza un proyecto nuevo en Nomad en lugar de tener un proyecto abierto.
- Si sigue cerrándose, la única solución es cargar [tu archivo de proyecto](#locate) en un dispositivo con más memoria.

::: tip
Si tu dispositivo móvil no puede cargar el proyecto, prueba la [versión de escritorio](https://nomadsculpt.com). Puedes usarla gratis en modo Demo para importar y exportar proyectos, aunque solo tendrás unas pocas herramientas de edición.

Si tu proyecto usa [Capas](layers.md), quizá te convenga fusionarlas para reducir el uso de memoria.
:::

### ¡Se cierra al abrir Nomad! {#crash-start}
Si se cierra durante la carga, significa que Nomad tiene problemas con algún archivo de la carpeta de Nomad.

La mayoría de las veces ocurre porque el proyecto es pesado y, por desgracia, supera el límite de RAM.

Localiza la [carpeta de Nomad](#locate) y luego renombra o mueve algunos archivos para encontrar al culpable.

Primero, prueba a renombrar `settings.json`. Así dejará de cargar el último proyecto.

Si no funciona, prueba a sacar algunos archivos recientes de sus carpetas de recursos (`projects`, `matcaps`, `environments`, etc.).

También puedes renombrar las propias carpetas para que Nomad las ignore por completo.
Si renombras o mueves todos los archivos de la carpeta de Nomad, el resultado es el mismo que una instalación limpia.

::: tip
Cuando Nomad carga un archivo al arrancar, siempre lo mueve a la carpeta `can_be_deleted/`.
Si la operación sale bien, lo devuelve a su carpeta original.

Si se cierra antes de terminar la carga, Nomad arrancará bien la próxima vez, ya que ignora la carpeta `can_be_deleted/`.

Puedes volver a intentar cargar ese archivo si crees que puede funcionar.
:::
