# ![](/icons/manual.webp) Consejos {#tips}

[[toc]]

## Cómo empezar un modelo {#how-to-start-a-model}

Quienes empiezan en la escultura 3d suelen preguntar cuál es la mejor forma de empezar un modelo. No hay una forma mejor: cada persona tiene sus preferencias. Estos son algunos de los enfoques más habituales.

### Esculpir sobre una esfera con multiresolución {#sculpt-on-sphere-multires}

El modelo por defecto al abrir Nomad es la forma más habitual. Usa las herramientas de mover, arcilla y pliegue para empujar y estirar la esfera hasta darle forma; usa los niveles de subdivisión bajos cuando quieras hacer cambios grandes rápidamente, y los niveles altos para el trabajo de detalle.

Un problema habitual es que a menudo te faltan polígonos donde los necesitas mientras te sobran en otras partes. Por ejemplo, si conviertes la esfera por defecto en un cuerpo entero, lo más probable es que no tengas detalle suficiente para los dedos, mientras desperdicias un montón de polígonos en la nuca. Aun así, para formas casi esféricas como una cabeza, puede funcionar bien.

### Topología dinámica {#dyntopo}

Al activar la topología dinámica, se añaden y quitan polígonos de forma adaptativa mientras esculpes. Estos polígonos son triángulos, y a quienes empiezan no suele gustarles su distribución desordenada comparada con el aspecto limpio de la multiresolución. ¡Merece la pena insistir! Si activas el sombreado suave, desactivas la malla alámbrica y te olvidas de la distribución, este modo da una sensación muy parecida a la arcilla. No olvides que, con un pincel grande o un pincel de suavizado, este modo también puede quitar polígonos, así que la herramienta siempre responde rápido. Cuando tengas terminada una primera pasada de la escultura, puedes clonarla, pasarla por Quad Remesher para obtener una buena distribución y reproyectar los detalles originales sobre un nivel de subdivisión alto.

### Remallado por vóxeles {#voxel-remesh}

El remallado por vóxeles aplica a tu escultura una topología basada casi siempre en cuadrángulos. Es una operación rápida a resoluciones bajas, y sirve para sustituir enseguida los polígonos estirados o demasiado densos por una distribución uniforme. Es una gran forma de empezar un cuerpo entero a partir de una esfera: por ejemplo, empiezas con una cabeza, estiras un cuello y haces un remallado por vóxeles. Estiras un cuerpo, remallado por vóxeles; los brazos, remallado por vóxeles, y así sucesivamente hasta tener las formas básicas.

### Usar varios objetos {#use-multiple-objects}

Muchas guías de anatomía representan el cuerpo con esferas, cilindros y cubos sencillos. En Nomad también puedes esculpir así. La ventaja es que puedes emparentar objetos en la jerarquía de la escena, de modo que, por ejemplo, si giras el cuello, la cabeza le sigue. También es muy útil poder usar la herramienta Gizmo para traslaciones, rotaciones y escalados precisos, y puedes fijar un pivote para cada forma, para que se mueva exactamente como esperas. Cuando los bloques básicos estén en su sitio, puedes seleccionarlos todos y unirlos en una sola superficie con un remallado por vóxeles o un booleano, para esculpir con más detalle.

Un truco práctico para trabajar así: empieza con una esfera, escálala hasta que parezca una salchicha alargada, pulsa Pivote, toca 'Inferior' y vuelve a pulsar Pivote. Ya tienes una parte del cuerpo que puedes clonar, desplazar a lo largo de la primera esfera, clonar, girar, clonar, deslizar, clonar, etc., para encajar un cuerpo rápidamente.

### Tubos {#tubes}

La herramienta Tubo es una forma estupenda de empezar una escultura. Colas de reptil, brazos, piernas, dedos, cejas: todo se puede esbozar rápidamente con la herramienta Tubo y editarse con facilidad después. También te permite modificar el perfil de la sección, para cambiar la forma rápidamente. Puedes validar la forma para empezar a esculpir sobre ella, y hacer un remallado por vóxeles junto con otros objetos para obtener la malla de un cuerpo entero.

### Usar otras aplicaciones {#use-other-apps}

Hay quien prefiere empezar un modelo en otras aplicaciones, y también está bien. Herramientas como Blender o Valence permiten empezar los modelos con técnicas low poly; después se pueden importar en Nomad para esculpirlos.

### Usar los preajustes incluidos {#use-the-built-in-presets}

En el menú [Archivos](files.md), toca `Preajuste…` a la izquierda de la sección del proyecto. Ahí encontrarás varios preajustes de cabezas y cuerpos de la Blender Foundation. Elige uno que te guste, tócalo otra vez y añádelo a tu escena. 

### Usar modelos de internet {#use-online-models}

Hay muchos modelos gratuitos en internet, por ejemplo en Poly Haven, Sketchfab o TurboSquid. Normalmente se pueden importar en Nomad y esculpir directamente sobre ellos, o usarlos como referencia.

### ¡Sin reglas! {#no-rules}

Al final puedes combinar estas técnicas como quieras, ¡o no usar ninguna! Nomad es muy flexible en este sentido: un usuario avanzado puede empezar con tubos, seguir con la topología dinámica, combinarlo con un pie descargado, pasarlo todo por Quad Remesher y terminar con la multiresolución para el detalle final. Lo que mejor te funcione.

## Grupos de caras {#facegroups}

La herramienta Grupo de caras sirve para muchas cosas, como se explica en este vídeo de YouTube: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Aquí tienes un resumen escrito de las funciones que trata el vídeo.

### ¿Para qué sirven los grupos de caras? {#why-facegroups}

Los grupos de caras te permiten organizar y seleccionar caras (en este manual, «caras» y «polígonos» significan lo mismo). Es más fácil explicarlo comparándolo con las demás herramientas de selección y organización de Nomad. Nomad te permite crear objetos, ponerles nombre y emparentarlos: es fácil crear una estructura de objetos para definir una habitación formada por suelo, paredes, silla, mesa, etc.

Para un personaje, puedes hacer un primer encaje con objetos separados para la cabeza, los brazos y las piernas, pero en cuanto fusionas todas las piezas en una sola malla, esa estructura se pierde. Puedes trabajar en zonas concretas del personaje con máscaras, pero acaba siendo pesado pintar una máscara para las manos, luego para la nariz, luego otra vez para las manos.

Aquí es donde los grupos de caras resultan útiles. Te permiten etiquetar caras de polígonos con un color, y después seleccionar y manipular los polígonos que tienen el mismo color. Ten en cuenta que el color del grupo de caras y el color de vértices son cosas distintas.

La analogía más cercana sería pintar colores en un mapa para luego poder seleccionar países o regiones según su color.

En la cabeza de un personaje, podrías pintar zonas para marcar las cuencas de los ojos, la nariz, los labios, la barbilla y las orejas, y seleccionarlas fácilmente más tarde. En el esculpido de superficies duras y piezas mecánicas, puede servir para definir paneles y secciones.

### Crear y editar grupos de caras {#creating-and-editing-facegroups}

Los grupos de caras se pueden aplicar con un pincel, en el que cada trazo nuevo crea un grupo de caras nuevo, o se puede tomar el grupo de caras que hay bajo el cursor y extenderlo. También se pueden crear con formas.

* Punto, modo por defecto: cada arrastre define un nuevo color de grupo de caras y lo asigna a las caras por las que pasas. Cada nuevo arrastre define un nuevo grupo de caras. Un toque rellena un grupo de caras nuevo.
* Punto, modo `Elegir`: cuando el botón `Elegir` de la barra de herramientas izquierda está activo, Nomad toma el grupo de caras que hay bajo el cursor y lo aplica durante el resto del arrastre. Es útil para afinar los grupos de caras sin tener que seleccionarlos a mano.

### Máscara {#masking}

Con la herramienta Máscara activa y el botón de grupo de caras activado en su barra de herramientas, al tocar un grupo de caras se le aplica la máscara.


### Ocultar {#hiding}

Con la herramienta Ocultar activa y el botón de grupo de caras activado en su barra de herramientas, al tocar un grupo de caras se oculta.

### Organizar {#organizing}

Como hemos dicho antes, los grupos de caras sirven para organizar tu malla sin necesidad de crear objetos separados. Puede que no quieras dividir una cabeza en objetos separados para la nariz, la barbilla y las orejas, pero sí es muy útil tenerlas definidas con grupos de caras.

### Regiones UV {#uv-regions}

La herramienta UV Atlas intenta definir las costuras automáticamente, pero a veces las pone donde no quieres. Si un objeto tiene grupos de caras y la opción de grupos de caras está activa en las opciones de UV Atlas, usará los bordes de los grupos de caras como costuras UV.

### Quad Remesher {#quad-remesher}

El complemento Quad Remesher suele hacer fluir bien las aristas por tu modelo, pero puedes usar los grupos de caras para guiarlo cuando la opción de grupos de caras está activada. Así es fácil definir un flujo de aristas limpio alrededor de los ojos, del arco de las cejas, de los labios o de un pliegue de la mejilla, por ejemplo.

### Filtrar con otras herramientas {#filter-with-other-tools}

Muchas herramientas tienen opciones para tener en cuenta los grupos de caras, ya sea en su menú principal o en el menú Trazo -> Filtro. Por ejemplo, la herramienta Suavizar con una intensidad superior al 100 % puede borrar con fuerza el detalle dentro de un grupo de caras, manteniendo el borde del grupo prácticamente intacto.

### Relajar y suavizar los bordes de los grupos de caras {#relax-and-smooth-facegroup-borders}

La opción `Relajar` de la herramienta Grupo de caras suaviza de maravilla los bordes de los grupos de caras sin tocar el resto de los rasgos. Es una gran forma de definir bordes de grupos de caras suaves antes de pasar por Quad Remesher.

## Limitaciones en tableta y móvil {#limitations-on-tabletmobile}

Las tabletas y los móviles actuales son muy potentes, pero tienen diferencias importantes con los ordenadores de sobremesa y los portátiles:

### Sin refrigeración activa {#no-active-cooling}

Los ordenadores tienen ventiladores o grandes disipadores para mantenerse frescos, y están diseñados para funcionar a altas temperaturas. El hardware móvil suele diseñarse ante todo para ser fino, no para ayudar a refrigerar sus componentes. Si llevas Nomad a sus ajustes de máxima calidad (modo de iluminación PBR, materiales complejos, muchos objetos, muchas opciones de posprocesado activadas), el dispositivo puede sobrecalentarse y la batería agotarse muy rápido. 

Es mejor usar el modo de iluminación MatCap y una `Resolución de renderizado` más baja (arriba del todo en el menú Posprocesado). Así el dispositivo se mantiene fresco y puedes esculpir durante más tiempo.

### Memoria limitada {#limited-memory}

Nomad puede conseguir resultados a la altura de la mayoría de las aplicaciones de escultura de escritorio, ¡pero no puede saltarse las leyes de la física! La mayoría de los ordenadores tienen el doble de memoria que los dispositivos móviles, y las estaciones de trabajo para animación 3d suelen tener 4 u 8 veces más. Por eso conviene estar atento a cuántos polígonos usas: haz algunas pruebas en tu dispositivo para ver cuándo empieza a ir lento. Casi todos los dispositivos capaces de ejecutar Nomad manejan 1 millón de polígonos sin problema. Un iPad Pro M2 maneja 8 millones con soltura, y hay quien ha probado en los últimos iPad con bastantes más.

Dicho esto, solo las esculturas más detalladas necesitan más de 4 millones de polígonos; si haces objetos relativamente sencillos y a menudo pasas de 500 000, 1 millón o 4 millones, ¡estás usando demasiados polígonos! Asegúrate de tener activado el `Sombreado suave` en la [Configuración](settings.md).

### El sistema es menos tolerante con las aplicaciones exigentes {#os-is-less-forgiving-with-intensive-apps}

Apple y Android esperan que las aplicaciones guarden y carguen archivos pequeños muy rápido. También dan por hecho que las aplicaciones pueden cambiar de tarea muy rápido. Nomad usa algunos trucos ingeniosos para que los archivos sean relativamente pequeños y se guarden muy rápido, pero si el sistema móvil decide que Nomad tarda demasiado, simplemente lo cierra antes de que termine su tarea. Es otro motivo para mantener los archivos más bien pequeños: se puede trabajar con esculturas de 37 millones de polígonos, como contó un usuario en Discord, ¡pero no es recomendable!

## Trabajar en pantallas pequeñas {#working-on-small-screens}

Nomad está pensado para tabletas, pero también funciona bien en teléfonos. Esculpir en una pantalla pequeña como la de un teléfono resulta más fácil con algunos ajustes en la interfaz y en tu forma de trabajar:

* Un toque con 4 dedos muestra u oculta toda la interfaz, para dejarte más espacio para esculpir.
* Arrastrar 3 dedos arriba y abajo cambia el radio del pincel
* Puedes reducir la escala de la interfaz para que quepan más botones si tienes buena vista, ¡o agrandarla si no la tienes tanto!
* Los menús más anchos a veces tapan la escultura: puedes hacerlos transparentes y sin desenfoque para ver la escultura debajo del menú.
* Si esculpes con el dedo, usa la opción [`Desplazamiento de trazo`](stroke.md#stroke-offset) para alejar un poco el centro del pincel de tu dedo.
* Encontrarás estas y muchas más opciones en el [menú Interfaz](./interface.md). 


## Deformador de inflado o de picos {#inflate-or-peak-deformer}

Muchas aplicaciones 3d tienen un deformador de inflado que empuja todos los vértices a lo largo de su normal una cantidad ajustable. Aunque Nomad todavía no tiene deformadores, puedes imitar este comportamiento con el pincel Inflar:

* Selecciona el pincel Inflar
* En el [menú Trazo](./stroke.md#stroke), cambia el modo de trazo a `Bloqueo + radio`
* Haz el radio del pincel más grande que tu escultura; aleja la cámara de la escultura si hace falta.
* Toca y arrastra un trazo sobre la superficie del objeto: cuando el radio es más grande que el objeto, toda la forma se infla por igual una cantidad fija.
* Ajusta la intensidad del pincel para controlar cuánto se infla
* Usa una máscara si hace falta para proteger ciertas zonas o reducir en ellas el efecto del inflado.

## Eliminar bultos o «granos» tras un remallado por vóxeles {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

El remallado por vóxeles va muy bien para crear polígonos repartidos de forma uniforme, pero a veces genera una topología que provoca pequeños bultos o granos al suavizar. Por ejemplo:

* Usa el pincel Pliegue sobre la esfera por defecto y haz una espiral
* Haz un remallado por vóxeles con `Construir multiresolución` a 3
* Suaviza con una intensidad alta
* aparecen artefactos (se ven mejor con un material matcap de alto contraste):

![](/videos/tip_pimples_before.mp4)

Para corregirlo esculpiendo, prueba la opción `Suavizado estable` en los ajustes de Suavizar. Gestiona bien la topología irregular del remallado por vóxeles y da resultados limpios.

![](/videos/tip_pimples_stable_smooth.mp4)

Para corregir la propia topología, usa una primitiva nueva, las herramientas de Quad Remesher o un modelador 3d externo, y proyecta el detalle de la malla original sobre la nueva con `Topología -> Hornear -> Reproyectar → Vértice`. 

![](/videos/tip_pimples_reproject.mp4)

## Iluminación de luz diurna {#daylight-lighting}

El render PBR por defecto está, como su nombre indica, basado en la física, y al igual que una foto digital sin procesar, puede verse algo apagado y plano. Las luces y el posprocesado de Nomad sirven para que los renders se vean más vivos.

Este es un render por defecto; veamos si podemos mejorarlo:
![](/images/tips_lighting_default.webp)

Activar el posprocesado y el mapeo de tonos añade brillo y contraste:

![](/images/tips_lighting_tonemap.webp)

En cuanto a las luces, la luz de entorno por defecto va bien para esculpir, pero se puede mejorar para un render final. Una forma de verlo es separar la luz directa (por ejemplo, el sol) de la luz de entorno (por ejemplo, la luz del azul del cielo o del suelo). Al reducir la luz de entorno y girarla, empezamos a captar cómo sería la iluminación si el sujeto estuviera en una zona de sombra:

![](/images/tips_lighting_env.webp)

Se puede añadir una luz directa y subir su intensidad para simular una luz solar intensa. Equilibrarla con la luz de entorno da un resultado agradable:

![](/images/tips_lighting_sunlight.webp)

A los personajes les sienta bien cambiar su material a subsuperficie y colocar un foco detrás del personaje apuntando a las orejas para que brillen:

![](/images/tips_lighting_sss.webp)

¡Después, experimenta con el resto de los ajustes de posprocesado! La iluminación global y la oclusión ambiental ayudan a lograr una iluminación más realista. La curvatura y el enfoque ayudan a resaltar el detalle de la escultura. La aberración cromática, la profundidad de campo, el grano, el resplandor y la viñeta simulan efectos de cámara. Ten en cuenta que, a medida que activas funciones, hay que ajustar la iluminación y los demás valores de posprocesado para compensar.

Este es el render con todos los retoques de posprocesado:
![](/images/tips_lighting_final.webp)
