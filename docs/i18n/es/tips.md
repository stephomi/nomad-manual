# ![](/icons/manual.webp) Consejos {#tips}

[[toc]]

## Cómo empezar un modelo {#how-to-start-a-model}

Quienes empiezan en el esculpido 3D suelen preguntar cuál es la mejor forma de empezar un modelo. No hay una única mejor forma, distintas personas tienen preferencias distintas. Aquí tienes algunos de los enfoques más comunes.

### Esculpir sobre esfera, multires {#sculpt-on-sphere-multires}

El modelo por defecto cuando se inicia Nomad es la forma más común. Usa las herramientas mover, arcilla (clay), pliegue (crease) para empujar y tirar de la esfera hasta darle forma; usa los niveles de subdivisión bajos cuando quieras hacer cambios grandes rápidamente, y los niveles de subdivisión altos para el trabajo de detalle.

Un problema común es que a menudo te quedarás sin polígonos donde los necesitas, mientras que tendrás demasiados polígonos en otras zonas. Por ejemplo, si empujas la esfera por defecto hasta convertirla en un cuerpo completo, es probable que no tengas suficiente detalle para hacer los dedos, mientras que tendrás muchos polígonos desperdiciados en la parte trasera de la cabeza. Para formas mayormente esféricas como una cabeza, sin embargo, esto puede estar bien.

### Dyntopo {#dyntopo}

Al activar Dyntopo se añadirán y eliminarán polígonos de forma adaptativa mientras esculpes. Estos polígonos serán triángulos, y a los principiantes a menudo no les gusta la disposición desordenada comparada con el aspecto limpio de multires. ¡Vale la pena insistir! Si activas el sombreado suave, desactivas el modo alámbrico y dejas de preocuparte por la disposición, este modo puede dar una sensación muy similar a la arcilla. No olvides que si usas un pincel grande, o un pincel de suavizado, este modo también puede eliminar polígonos, así que la herramienta siempre se siente rápida y reactiva. Una vez que tengas una primera pasada del esculpido terminada, puedes clonarla y pasarla por quad remesher para obtener una buena disposición, y reproyectar los detalles originales en un nivel de subdivisión alto.

### Remallado de vóxeles {#voxel-remesh}

El remallado por vóxeles aplicará una topología mayormente basada en quads sobre tu escultura. Esta operación es rápida a resoluciones bajas, y puede usarse para reemplazar rápidamente polígonos estirados o excesivamente densos por una disposición de polígonos uniformemente espaciados. Esta puede ser una gran forma de empezar un cuerpo completo desde una esfera; por ejemplo, empiezas con una cabeza, la estiras para formar un cuello, remallas por vóxeles. Estiras un cuerpo, remallas por vóxeles, brazos, remallas por vóxeles, y así sucesivamente, hasta que tengas las formas básicas.

### Usar múltiples objetos {#use-multiple-objects}

Muchas guías de anatomía representan un cuerpo con esferas, cilindros y cubos simples. También puedes esculpir de esta forma en Nomad. Esto tiene la ventaja de permitirte hacer parentescos entre objetos en la jerarquía de la escena, de modo que puedas rotar el cuello y que la cabeza lo siga, por ejemplo. Poder usar la herramienta gizmo para traslaciones/rotaciones/escalados precisos también es muy útil, y además puedes definir pivotes por forma para que se muevan exactamente como esperas. Cuando los bloques básicos estén en el lugar correcto, puedes seleccionarlos todos y remallar por vóxeles o hacer booleanas para combinarlos en una única superficie para un esculpido más detallado.

Un truco útil para trabajar de esta manera es empezar con una esfera, escalarla hasta convertirla en una salchicha alargada, pulsar pivot, hacer clic en “bottom”, pulsar pivot de nuevo. Ahora tienes una parte del cuerpo que puede clonarse, trasladarse a lo largo de la longitud de la primera esfera, clonarse, rotarse, clonarse, deslizarse, clonarse, etc., para maquetar un cuerpo rápidamente.

### Tubos {#tubes}

La herramienta de tubos es una gran forma de empezar una escultura. Colas de reptiles, brazos, piernas, dedos, cejas, todo se puede esbozar rápidamente con la herramienta de tubos y luego editar fácilmente. También te permite modificar el perfil de la sección transversal, lo que permite cambios de forma rápidos. Puedes validar la forma para empezar a esculpir sobre ella, y remallar por vóxeles junto con otros objetos para obtener una malla de cuerpo completo.

### Usar otras apps {#use-other-apps}

Algunas personas prefieren empezar un modelo en otras aplicaciones, y eso también está bien. Herramientas como Blender o Valence permiten empezar modelos usando técnicas de low poly, que luego pueden importarse en Nomad para el esculpido.

### Usar los preajustes integrados {#use-the-built-in-presets}

En el menú de proyecto haz clic en `Preset...` en la parte superior derecha. Aquí encontrarás varias formas de cabeza y cuerpo de la Blender Foundation. Selecciona una que te guste, tócala de nuevo y añádela a tu escena. 

### Usar modelos en línea {#use-online-models}

Hay muchos modelos gratuitos disponibles en línea, por ejemplo polyhaven, sketchfab, turbosquid. Normalmente estos modelos pueden importarse en Nomad, y esculpirse directamente sobre ellos o usarse como referencia.

### ¡Sin reglas! {#no-rules}

En última instancia puedes usar cualquier combinación de estas técnicas, ¡o ninguna! Nomad es muy flexible en este sentido; usuarios avanzados podrían usar tubos para empezar, luego dyntopo, luego combinar con un pie descargado, luego hacer quad remesh a todo, y después multires para el detalle final. Lo que te funcione.

## Grupos de caras {#facegroups}

La herramienta de facegroups puede usarse para muchas cosas, como se explica en este vídeo de YouTube: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Este es un resumen en texto de las funciones tratadas en ese vídeo.

### ¿Por qué grupos de caras? {#why-facegroups}

Los facegroups te permiten organizar y seleccionar caras (en este manual se usan “caras” y “polígonos” de forma intercambiable). Esto es más fácil de explicar en comparación con las otras herramientas de selección y organización de Nomad. Nomad te permite crear objetos, nombrarlos, hacer parentescos entre ellos; es fácil crear una estructura de objetos para definir una habitación compuesta por suelo, paredes, silla, mesa, etc.

Para un personaje podrías hacer un bloque inicial usando objetos separados para cabeza, brazo, pierna, pero una vez que fusionas todas las piezas en una sola malla, esta estructura se pierde. Puedes trabajar en subsecciones de un personaje con máscaras, pero puede volverse tedioso tener que pintar una máscara para las manos, luego la nariz, luego las manos otra vez.

Aquí es donde los facegroups son útiles. Te permiten etiquetar caras de polígonos con un color, y luego poder seleccionar y manipular polígonos que tengan el mismo color. Ten en cuenta que el color de facegroup y el color de vértice son cosas distintas.

La analogía más cercana sería pintar colores en un mapa y luego poder seleccionar países o regiones basándote en el color.

Para cabezas de personajes podrías pintar zonas para marcar las cuencas de los ojos, la nariz, los labios, la barbilla, las orejas, y luego seleccionar fácilmente esas zonas más tarde. Para esculpido hard surface y mecánico puede ser útil definir paneles y secciones.

### Crear y editar grupos de caras {#creating-and-editing-facegroups}

Los facegroups pueden aplicarse con un pincel, donde cada nueva pasada crea un nuevo facegroup, o pueden seleccionar el facegroup bajo el cursor y extenderlo. También pueden crearse usando formas.

* Punto, auto-pick activado: un solo arrastre definirá un nuevo color de facegroup y lo asignará a las caras sobre las que arrastres. Cada nuevo arrastre definirá un nuevo facegroup. Un toque rellenará un nuevo facegroup.
* Punto, auto-pick desactivado: cuando el botón auto-pick está en su modo “sub”, Nomad seleccionará el facegroup bajo el cursor y lo aplicará durante el resto del arrastre. Esto es útil para refinar facegroups sin tener que seleccionarlos manualmente.

### Enmascarado {#masking}

Cuando la herramienta de máscara está activa y el botón de facegroup está activo en su barra de herramientas, tocar un facegroup lo enmascarará.


### Ocultar {#hiding}

Cuando la herramienta de ocultar está activa y el botón de facegroup está activo en su barra de herramientas, tocar un facegroup lo ocultará.

### Organización {#organizing}

Como se mencionó antes, los facegroups pueden usarse para organizar tu malla sin necesidad de crear objetos separados. Puede que no quieras dividir una cabeza en objetos separados para nariz, barbilla, orejas, pero es muy útil tenerlos definidos mediante facegroups.

### Regiones UV {#uv-regions}

La herramienta UV Atlas intentará definir costuras automáticamente, pero a veces pondrá costuras donde no las quieres. Si existen facegroups en un objeto, y la opción de facegroup está activa en las opciones de UV Atlas, usará los bordes de los facegroups como costuras UV en su lugar.

### Remallador en quads {#quad-remesher}

El plugin quad remesher normalmente hará fluir los bordes de forma agradable en tu modelo, pero puedes usar facegroups para ayudar a dirigirlo cuando la opción de facegroup está activada. Esto puede facilitar definir un flujo de bordes limpio alrededor de los ojos, un arco de ceja, labios, pliegue de la mejilla, por ejemplo.

### Filtrar con otras herramientas {#filter-with-other-tools}

Muchas herramientas tendrán opciones para ser conscientes de los facegroups, ya sea desde su menú principal de herramienta o mediante el menú stroke -> filtering. Por ejemplo, la herramienta de suavizado con intensidades por encima del 100% puede suavizar agresivamente el detalle dentro de un facegroup, pero mantener el borde del facegroup relativamente intacto.

### Relajar y suavizar bordes de grupos de caras {#relax-and-smooth-facegroup-borders}

La opción de relajar dentro de la herramienta de facegroup hace un excelente trabajo al suavizar los bordes de los facegroups mientras mantiene intactas otras características. Esta puede ser una gran forma de definir regiones de borde de facegroup suaves antes de hacer quad remesh.

## Limitaciones en tablet/móvil {#limitations-on-tabletmobile}

Las tablets y móviles actuales son muy potentes, pero tienen diferencias importantes respecto a los ordenadores de sobremesa y portátiles:

### Sin refrigeración activa {#no-active-cooling}

Los ordenadores tienen ventiladores y/o grandes disipadores para mantenerse fríos, y están diseñados para funcionar a altas temperaturas. El hardware móvil suele estar diseñado priorizando la delgadez, no ayudar a mantener fríos los componentes internos. Si Nomad se lleva a sus ajustes de máxima calidad (modo de iluminación PBR, materiales complejos, muchos objetos, muchas opciones de postprocesado activadas), esto puede sobrecalentar el dispositivo y agotar la batería muy rápidamente. 

Un enfoque mejor es usar un modo de iluminación matcap y usar un multiplicador de render más bajo (parte superior del menú de postprocesado). Estas elecciones mantendrán el dispositivo frío y te permitirán esculpir durante más tiempo.

### Memoria limitada {#limited-memory}

Nomad puede lograr resultados iguales a la mayoría de las aplicaciones de esculpido de escritorio, pero no puede doblar las leyes de la física. La mayoría de los ordenadores de sobremesa tienen el doble de memoria que los dispositivos móviles; las estaciones de trabajo construidas para animación 3D a menudo tienen 4x u 8x la memoria. Por ello, es bueno ser consciente de cuántos polígonos estás usando, hacer algunas pruebas en tu dispositivo para ver cuándo empieza a volverse lento. Casi todos los dispositivos que pueden ejecutar Nomad pueden manejar 1 millón de polígonos con bastante facilidad. Un iPad Pro M2 puede manejar 8 millones cómodamente; la gente ha probado en los últimos iPads y han llegado muy por encima de eso.

Dicho esto, solo los esculpidos más detallados necesitan más de 4 millones de polígonos; si estás haciendo objetos relativamente simples y te encuentras a menudo superando 500.000, 1 millón, 4 millones, ¡estás usando demasiados polígonos! Asegúrate de tener activado el modo de sombreado suave en las opciones.

### El SO es menos tolerante con apps intensivas {#os-is-less-forgiving-with-intensive-apps}

Apple y Android esperan que las apps guarden y carguen archivos pequeños muy rápidamente. También asumen que las apps pueden cambiar de tarea muy rápido. De nuevo, Nomad hace algunos trucos inteligentes para mantener los tamaños de archivo relativamente pequeños y guardarlos muy rápido, pero si el sistema operativo móvil decide que Nomad está tardando demasiado, simplemente lo matará antes de que termine su tarea. Esta es otra razón para mantener los archivos en el lado pequeño; es posible trabajar con esculpidos de 37 millones de polígonos como reportó un usuario en Discord, ¡pero no es recomendable!

## Trabajar en pantallas pequeñas {#working-on-small-screens}

Nomad está diseñado para funcionar en tablets, pero también funciona bien en teléfonos. Esculpir en una pantalla pequeña como la de un teléfono puede hacerse más fácil con algunos ajustes de interfaz y flujo de trabajo:

* Un toque con 4 dedos alternará toda la interfaz, dándote más espacio para esculpir.
* Un arrastre con 3 dedos hacia arriba y hacia abajo cambiará el radio del pincel.
* La escala de la interfaz puede hacerse más pequeña para que quepan más botones si tienes buena vista, o más grande si tienes mala vista.
* Los menús más anchos a veces pueden estorbar a la escultura; puedes hacerlos transparentes y sin desenfoque para permitirte ver la escultura bajo el menú.
* Si esculpes con el dedo, usa la opción de desplazamiento (offset) para mover el centro del pincel un poco lejos de tu dedo.
* Estas y muchas más opciones pueden encontrarse en el [menú Interface](./interface.md). 


## Deformador Inflar o Pico {#inflate-or-peak-deformer}

Muchas aplicaciones 3D incluyen un deformador de inflado, que empuja todos los vértices a lo largo de su normal en una cantidad controlable. Aunque Nomad actualmente carece de deformadores, es posible emular este comportamiento con el pincel de inflado:

* Selecciona el pincel de inflado (inflate)
* En el [menú Stroke](./stroke.md#stroke) cambia el método de trazo a `Lock + Radius`
* Haz el radio del pincel más grande que tu escultura; aleja la cámara de la escultura si es necesario.
* Haz clic y luego arrastra un trazo sobre la superficie de tu objeto; cuando el radio sea mayor que el objeto, toda la forma se inflará de manera uniforme en una cantidad fija.
* Ajusta la intensidad del pincel para controlar la cantidad de inflado.
* Usa máscaras si es necesario para proteger o reducir el efecto del inflado en ciertas áreas.

## Eliminar bultos o 'granitos' tras una operación de remallado de vóxeles {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

El remallado por vóxeles es excelente para crear polígonos uniformemente espaciados, pero a veces crea una topología que causará pequeños bultos o granos al suavizar. Por ejemplo:

* Usa el pincel de pliegue (crease) en la esfera por defecto y haz un remolino.
* Remalla por vóxeles con “build multiresolution at 3”.
* Suaviza con alta intensidad.
* Aparecen artefactos (más fácil de ver con un material matcap de alto contraste):

![](/videos/tip_pimples_before.mp4)

Para arreglarlo mediante esculpido, prueba la opción `Stable smoothing` en los ajustes de suavizado. Esto puede manejar la disposición de topología irregular del remallado por vóxeles y obtener resultados limpios.

![](/videos/tip_pimples_stable_smooth.mp4)

Para arreglar la topología en sí, usa una nueva primitiva, o las herramientas de quad remesh, o un modelador 3D externo, y proyecta el detalle desde la malla original a la nueva mediante `Topology -> Misc -> Reproject`. 

![](/videos/tip_pimples_reproject.mp4)

## Iluminación diurna {#daylight-lighting}

El render PBR por defecto es, como su nombre sugiere, físicamente basado, lo que puede hacer que, como una foto digital sin procesar, se vea un poco deslavado y plano. Las luces y el postprocesado de Nomad pueden usarse para hacer que los renders se vean más vibrantes.

Aquí hay un render por defecto; veamos si podemos hacerlo ver mejor:
![](/images/tips_lighting_default.webp)

Activar el postprocesado y el tonemapping puede añadir brillo y contraste:

![](/images/tips_lighting_tonemap.webp)

Para centrarnos en las luces, la luz de entorno por defecto es buena para esculpir, pero puede mejorarse para un render final. Una forma de pensar en esto es separar la luz directa (por ejemplo, el sol) de la luz de entorno (por ejemplo, la luz del azul del cielo, el suelo). Al reducir la luz de entorno y rotarla, se empieza a capturar cómo debería verse la iluminación si el sujeto estuviera en una zona sombreada:

![](/images/tips_lighting_env.webp)

Se puede añadir una luz directa y aumentar su intensidad para simular una luz solar dura. Equilibrar esto con la luz de entorno logrará un resultado agradable:

![](/images/tips_lighting_sunlight.webp)

Los personajes pueden beneficiarse de cambiar su material a subsurface y colocar un foco detrás del personaje apuntando a las orejas para hacer que brillen:

![](/images/tips_lighting_sss.webp)

¡Luego experimenta con el resto de los ajustes de postprocesado! Global Illumination y Ambient Occlusion ayudan con una iluminación más realista. Curvature y Sharpen pueden ayudar a resaltar más detalle en la escultura. Chromatic Aberration, Depth of Field, Grain, Bloom, Vignette ayudan a simular efectos de cámara. Ten en cuenta que a medida que se activan funciones, es necesario ajustar la iluminación y otros valores de postprocesado para compensar.

Aquí está el render con un conjunto completo de ajustes de postprocesado:
![](/images/tips_lighting_final.webp)