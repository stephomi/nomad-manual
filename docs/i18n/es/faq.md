# ![](/icons/faq.webp) Preguntas frecuentes {#faq}

[[toc]]

## Plataforma {#platform}
### ¿Dónde se encuentran mis proyectos en mi dispositivo? {#locate}
Los proyectos se encuentran en la carpeta `projects` dentro de la carpeta principal de Nomad.

En iOS, puedes acceder a la carpeta de Nomad con la app Archivos de iOS.

En Android, la carpeta de Nomad está en `Android/data/com.stephaneginier.nomad/files/`.  
En las versiones recientes de Android (10/11), ya no tienes acceso a la carpeta `Android/data`.
Puedes acceder a ella mediante una app aparte, por ejemplo [esta](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### ¿Hay alguna forma de probar la beta? {#beta}
Para Windows y MacOS, puede haber una beta disponible en la [Página principal](https://nomadsculpt.com).
<br>
Para iOS hay un TestFlight privado, visita el [Discord](https://discord.com/invite/8h7BwpRz29) en el canal #beta-ios.
<br>
La [Demo web](https://nomadsculpt.com/demo) suele actualizarse con las últimas funciones.

### ¿Por qué hay una prueba gratuita en Android pero no en iOS? {#android-trial}
Porque los dispositivos Android antiguos son malos (y algunos recientes también...), y no quería que la gente comprara la app y se encontrara con una pantalla en negro.
Pero la razón principal es que sentía que las apps de pago en Android no son realmente la norma.

### ¿Cuál es la mejor tableta para ejecutar Nomad? {#best-tablet}

Resumen rápido: Un iPad.

La respuesta un poco más larga es 

> "El iPad más nuevo _que puedas permitirte_, a menos que realmente odies Apple, en cuyo caso la tablet Samsung más nueva que puedas permitirte. Cualquier otra cosa, pruébala primero." 

La gente siempre quiere más información, así que aquí va un resumen.

Nomad funciona mejor en iPads más nuevos:

* Los iPads y iPhones pueden acceder al plugin [Quad Remesher](tools#quad-remesher) de [Exoside](https://exoside.com/)
* Los iPads recientes con el último lápiz son compatibles con el [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), puedes girar el lápiz en ciertas herramientas de Nomad. 
* El rendimiento de los últimos chips de la serie M es muy rápido. 

El iPad más nuevo y caro disponible podrá renderizar imágenes finales muy rápido y te permitirá esculpir con mucho detalle.

Sin embargo, la caída de rendimiento con iPads más baratos y antiguos no es tan mala como la gente espera. Cualquier iPad que admita Apple Pencil ejecuta Nomad bastante bien. Por ejemplo:

* Un iPad Pro de 2023 puede manejar esculturas de 5 millones de polígonos y seguir siendo fluido; una imagen de calidad final puede renderizarse en 5 segundos.
* Un iPad Pro de 2015 puede manejar un objeto de 1,2 millones de polígonos con algo de lag; una imagen de calidad final puede renderizarse en 20 segundos.

Es una gran diferencia de rendimiento, pero también hay que tener en cuenta el precio:

* El iPad Pro de 2025 cuesta *2500 USD* nuevo con todas las opciones. 
* El iPad Pro de 2023 cuesta actualmente *400 USD* en eBay.
* El iPad Pro de 2015 cuesta *250 USD* en eBay.

¿Merece la pena pagar 2100 USD más por 4 millones de polígonos extra y ahorrar 15 segundos? Eso depende de ti.

Los modelos no Pro pueden ser aún más baratos y ofrecer una amplia variedad de tamaños y rendimientos entre los que elegir. El iPad Air actual admite el lápiz de 2.ª generación con barrel roll y es considerablemente más barato que el Pro. El mercado de segunda mano y reacondicionados ofrece aún más opciones. 

Esto significa que, sea cual sea tu presupuesto, deberías poder encontrar un iPad para ti. Y recuerda que la mayoría de las esculturas no tienen millones de polígonos. Si puedes mantenerte por debajo de 500.000 polígonos, incluso los iPads antiguos te permitirán esculpir con rapidez.

`¿Y qué pasa con Android?`

El rendimiento gráfico de Android está por debajo del de los iPads. Según el desarrollador de Nomad, "Una Samsung Galaxy Tab S9 ejecutará Nomad un orden de magnitud más lento que un iPad Air". Dicho esto, muchos usuarios están muy contentos con sus tablets Samsung; Nomad funciona bien para la mayoría de las esculturas. 

Para otras tablets Android, ten cuidado. El hardware Android puede variar mucho en rendimiento, no es fácil predecir cómo funcionará Nomad.

Por favor, usa primero la versión gratuita sin guardado de Nomad para hacer pruebas. 

`¿Y la memoria y el almacenamiento?`

La mayoría de los archivos de Nomad suelen ser de 100 MB o menos. Esto significa que casi cualquier tablet que compres hoy en día, ya sea iPad o Android, tendrá espacio de sobra para tus proyectos de Nomad.


### Compré Nomad para un dispositivo, ¿puedo usarlo en otro dispositivo? {#multi-devices}
Mientras use la misma tienda de apps y la misma cuenta, sí.

Por ejemplo, si lo compraste en la App Store de iOS, puedes usarlo en tus otros dispositivos iOS.

Si lo compraste para tu tablet Android en Google Play, puedes usarlo en tus otros dispositivos Android.

Sin embargo, si compraste Nomad en Android y luego consigues un iPad, tendrás que comprarlo de nuevo.

Esto se debe a que Nomad no tiene su propio servidor de licencias ni modelo de suscripción. No hay ningún acuerdo entre Apple/Google/AppGallery para gestionar el uso compartido de licencias. 


### ¿Cómo restauro mi compra? {#restore}
Google Play y AppGallery gestionan la sincronización automáticamente.

- Ve al menú About (icono de Nomad arriba a la izquierda) y pulsa `restore purchase`
- Comprueba dos veces que has iniciado sesión con la misma cuenta que usaste para comprar Nomad (en Google Play).
- Reinicia el dispositivo
- A veces hay que esperar un par de horas
- Asegúrate de que la aplicación Google Play está actualizada
- Reinstala Nomad (asegúrate de [hacer copia de seguridad de tus archivos](#where-are-my-projects-located-on-my-device) si no quieres perder nada)
- Puedes intentar comprar de nuevo para ver qué ocurre (nota: no puedes comprar dos veces el mismo artículo con la misma cuenta)

:::tip
Puedes contactarme en <support@nomadsculpt.com> pero lo *único* que podré hacer es confirmar si un correo electrónico tiene una compra asociada.

Ten en cuenta que recibo informes con regularidad sobre licencias que no se actualizan correctamente tras adquirir un nuevo dispositivo.
No tengo ningún control sobre el pago ni la sincronización de cuentas, todo lo gestiona Google/AppGallery.

Al final la compra siempre se restaura, pero los pasos necesarios para acelerar el proceso no están claros.
:::

::: warning
Los dispositivos Huawei recientes no tienen acceso a los servicios de Google.
En ese caso tendrás que comprar la app de nuevo en AppGallery (la tienda de apps de Huawei).
:::

### ¿Puedes traducir o corregir [mi-idioma]? {#locale}
Puedo añadir otro idioma con relativa facilidad, pero dependo de la traducción por IA ya que es mucho más fácil de gestionar para las actualizaciones periódicas.
Los archivos de traducción se pueden encontrar [aquí](https://github.com/stephomi/nomad-translation).

## Funciones {#features}

### ¿Por qué no se mueve el gizmo? {#gizmo-not-moving}
Puede que tengas [pin activado en la barra de herramientas del menú izquierdo](tools#left-menu-toolbar). 

### ¿Se puede animar dentro de Nomad? {#animate}
Por ahora no. Una línea de tiempo que pudiera animar las capas podría ser interesante, pero no está realmente planeada por el momento.  

Me gustaría admitir rigging/skinning en el futuro, pero plantea algunos desafíos (en particular la interacción con las herramientas de esculpido...), así que por ahora no hay nada seguro.


### ¿Se puede hacer un modelado low‑poly adecuado? {#lowpoly}
Por ahora no.
Esto no entra realmente en el ámbito de Nomad *Sculpt*, pero quizá proporcione algunas herramientas en el futuro.


### ¿Se pueden hacer UV y texturizado? {#texturing}
Respuesta corta: Sí. Respuesta larga: No directamente, pero hay varias formas de combinar las excelentes herramientas de pintura por vértices de Nomad con UVs y texturas.

* Nomad te permite pintar color, rugosidad y propiedades de material directamente en los vértices de tu escultura.
* Nomad permite recuentos de vértices muy altos para que puedas pintar sin preocuparte por las UVs.
* Nomad puede cargar texturas para usarlas en pinceles, lo que permite estampar y pintar con texturas.
* Nomad puede cargar objetos que ya tengan texturas asignadas, para fines de renderizado.
* Nomad puede hacer [despliegue UV](topology.md#uv-unwrap) de objetos de baja poligonización.
* El color/rugosidad/metallicidad se pueden transferir de texturas a vértices mediante [las opciones de proyección](topology.md#reproject-to-vertex).
* El color/rugosidad/metallicidad/normales se pueden hornear de vértices a texturas mediante [las opciones de horneado](topology.md#bake-to-texture)
* El horneado y la proyección se pueden gestionar entre objetos individuales o muchos objetos, o entre los niveles de subdivisión más alto y más bajo de un solo objeto, lo que permite una variedad de flujos de trabajo de horneado y proyección.
* Después de hornear, al exportar un obj también se exportarán las texturas, que se pueden llevar a una app como Procreate para pintar directamente sobre las texturas.

### ¿Puedo grabar un vídeo de giro (turntable)? {#video}
No está previsto por ahora, iOS tiene una [función de grabación de vídeo](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) que es muy fácil de usar.

En iOS, se hace deslizando hacia abajo desde la parte superior izquierda y tocando el botón de grabar. Te dará una cuenta atrás de 3 segundos, desliza el menú para ocultarlo y mostrar Nomad, y usa la función de turntable. Cuando termines, desliza de nuevo hacia abajo desde la parte superior derecha y toca el botón de grabar otra vez. Edita el vídeo desde la fototeca para eliminar el metraje sobrante al principio y al final.

### ¿Puedes añadir [insert-favorite-feature] como un botón de nivel superior? {#interface}
Sí, ahora se puede personalizar la barra de herramientas inferior desde el menú de [interfaz](interface.md), y ahora se pueden crear barras de herramientas flotantes.

### ¿Cuáles son las próximas funciones? {#next-features}
Para la hoja de ruta a medio/largo plazo tengo muchas ideas pero aún no lo sé.  

La corrección de errores y la mejora de las funciones existentes siempre tendrán mayor prioridad que añadir nuevas funciones.


### ¿Se puede hacer rigging en Nomad? {#rigging}
No, pero está previsto. Por ahora puedes agrupar formas como padre/hijo y modificar puntos de pivote, lo que permite esculturas simples posables.

### ¿Se pueden usar más de 4 luces? {#lights}
No, es una limitación del motor de renderizado en tiempo real de Nomad. Es posible simularlo usando objetos emisivos e iluminación global en postproceso, como se muestra en [este tutorial](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### ¿Se pueden importar herramientas de ZBrush? {#zbrush-import}
No, Zbrush usa un formato propietario. Deberías poder extraer los mapas de alfa y usarlos en Nomad. 

### ¿Por qué los colores no coinciden con lo que pinté? ¿Por qué no puedo obtener blanco en el render? {#paint-pbr}
Imagina hacer una foto de una hoja de papel, otra de una lámpara de escritorio y otra del sol. Las cámaras y pantallas antiguas simplemente las mostrarán todas como “blanco”. Los sistemas más modernos pueden mostrar la diferencia entre el blanco reflejado del papel, la luz emitida de una lámpara y el superbrillo del sol.

Los gráficos por ordenador modernos intentan funcionar de forma similar, emulando la física de la luz y las superficies. Esto se llama `renderizado físicamente basado`, o PBR, y el renderizador PBR de Nomad se basa en esto. Esto se ve realista y equilibrado, pero a menudo los colores muy brillantes pintados aparecerán más oscuros.

Si necesitas que el render se acerque más a los colores pintados, puedes solucionarlo de formas tanto no físicamente basadas como físicamente basadas:

No PBR:
* `Usa el modo 'Unlit' en el menú de iluminación`. Los colores se mostrarán exactamente como se pintaron, pero también perderás todo sombreado. Útil para comprobaciones rápidas y resultados más gráficos.
* `Usa el modo 'Matcap' en el menú de iluminación`. Elige un matcap más brillante que sea mayormente blanco, sin tinte de color.

PBR:
* `Usa un entorno neutro`. Puedes [cambiar el entorno](shading.md#environment) a uno más neutro. Evita los entornos interiores, ya que tienden a ser más coloreados. Prefiere un entorno exterior de luz diurna o de estudio.
* `Aumenta la iluminación`. Si estuvieras haciendo una foto de papel blanco en una habitación oscura, simplemente añadirías más luz. En la luz de entorno, sube el deslizador de exposición hasta que los colores empiecen a parecerte correctos, o añade más luces individuales con más intensidad.
* `Aumenta la exposición de la cámara`. Si la habitación oscura no tuviera luces extra, podrías hacer que la cámara mantuviera el obturador abierto más tiempo o usar un ISO más sensible. En Nomad puedes lograr un resultado similar con el postproceso. Ve a post process, actívalo, baja hasta tone mapping, actívalo y sube el deslizador de exposición hasta que los colores se sientan bien.
* `Usa color emisivo`. En el menú de material, puedes activar “emissive” en texturas, lo que hará que un objeto parezca una fuente de luz. Si activas la iluminación global en los ajustes de postproceso, proyectará luz sobre otros objetos de la escena. También puedes activar “unlit” para ese material, lo que logrará un aspecto similar sin textura.

## Fallos {#crashes}

### ¡Se bloquea cuando guardo o remallo mi modelo! {#crash-remesh}
Tu dispositivo se está quedando sin memoria (RAM).  
Para reducir el uso de memoria en tu escena, puedes usar algunas de las opciones de [Topología](topology.md) para reducir el número de polígonos.

::: tip RAM/Almacenamiento
Lo que importa es la cantidad de RAM, no el almacenamiento (que suele ser mucho mayor).
:::


### ¡Se bloquea cuando cargo mi proyecto! {#crash-load}
Si el archivo es pequeño, puedes enviármelo y le echaré un vistazo (por correo electrónico a <support@nomadsculpt.com>).

De lo contrario, probablemente el dispositivo se esté quedando sin memoria RAM.

- Asegúrate de cerrar cualquier otra app abierta en tu dispositivo.
- Inicia un proyecto nuevo en Nomad en lugar de tener un proyecto abierto actualmente.
- Si sigue bloqueándose, la única solución es cargar [tu archivo de proyecto](#where-are-my-projects-located-on-my-device) en un dispositivo con más memoria.

::: tip
En un navegador de escritorio, puedes intentar cargar tu archivo [en esta URL](https://nomadsculpt.com/demo_save/) y luego exportarlo de nuevo tras simplificar tu escena.

Algunos navegadores limitan la cantidad de RAM que puede usar una sola pestaña, así que es posible que esta técnica no funcione.

Si tu proyecto usa [Capas](layers.md), quizá quieras aplanarlas para reducir el uso de memoria.
:::

<!-- ::: tip
Additionally, for legacy glb.lz4 file format, you can try the following:

1. If your project is using [Layers](layers.md), enable the `Merge layers` option before loading the project.
The option can be found in the `Files -> Settings` sub menu.
Layers can take a lot of memory, merging them at loading can help reduce the memory peak usage.

2. Decompress your [project](#where-are-my-projects-located-on-my-device) (`.glb.lz4` to `.glb`).
On windows, you need to download [LZ4](https://github.com/lz4/lz4/releases).
On MacOS, you can use the command line.
With homebrew, simply do `brew install lz4` and then `lz4 myproject.glb.lz4`.

3. Try to load the `.glb` file directly into Nomad again.

4. If it still crashes at loading, you can open the file on any 3d desktop software that supports `glTF`.
::: -->

### ¡Se bloquea cuando inicio Nomad! {#crash-start}
Si se bloquea al cargar, significa que Nomad tiene problemas con algún archivo presente en la carpeta de Nomad.

La mayoría de las veces ocurre porque el proyecto es pesado y, por desgracia, superará el límite de RAM.

Localiza la [carpeta de Nomad](#where-are-my-projects-located-on-my-device) y luego cambia el nombre o mueve algunos archivos para encontrar el culpable.

Primero, intenta renombrar `settings.json`. De ese modo dejará de cargar el último proyecto.

Si no funciona, intenta mover algunos archivos recientes fuera de sus carpetas de recursos respectivas (`projects`, `matcaps`, `environments`, etc).

También puedes renombrar las carpetas para que Nomad las ignore por completo.
Si renombras o mueves todos los archivos de la carpeta de Nomad, obtendrás el mismo resultado que con una instalación limpia.

::: tip
Cuando Nomad carga un archivo al inicio, siempre mueve el archivo a la carpeta `can_be_deleted/`.
Si la operación tiene éxito, entonces se mueve de nuevo a su carpeta original.

Si se bloquea antes de que termine la carga, Nomad se iniciará correctamente en el siguiente arranque, ya que ignora la carpeta `can_be_deleted/`.

Simplemente puedes intentar cargar este archivo de nuevo si crees que puede tener éxito.
:::