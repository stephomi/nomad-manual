# ![](/icons/open.webp) Archivos {#files}

El menú Archivos te permite guardar y cargar proyectos de Nomad, importar y exportar modelos 3d, exportar imágenes renderizadas y conectar Nomad con otras aplicaciones. Tiene tres pestañas: `Archivos`, `Renderizado` y `Enlace`.

![](/images/file_menu.webp)

## Proyecto {#project}
![](/images/file_project.webp)

La miniatura de arriba muestra el proyecto actual, con el tamaño de su archivo, el guardado automático y el historial guardado al lado. Toca la miniatura para abrir un pequeño explorador de tus proyectos y, después, toca un proyecto para ver un menú con el que abrirlo, añadirlo, sobrescribirlo, clonarlo, renombrarlo o eliminarlo.

Cuando el proyecto tiene cambios que aún no se han guardado, aparece `¡Cambios no guardados!` bajo la miniatura.

### Alcance {#scope}
En escritorio, elige dónde se guardan tus proyectos:
* `Interno` - La opción por defecto, igual que en móvil. Los proyectos se guardan solo dentro de la carpeta principal de Nomad.
* `En origen` - Cuando abres un proyecto que está fuera de la carpeta de Nomad, al guardar se sobrescribe el archivo original. El guardado automático no funciona con estos proyectos externos.

### ![](/icons/nomad.webp) Preajuste {#preset}
Accede a una colección de demos y de piezas para personajes. Selecciona una y vuelve a seleccionarla para elegir entre `Abrir` y `Añadir a la escena`. Desde este explorador también puedes descargar modelos gratuitos de Poly Haven.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) Historial... {#history}
Acceso rápido a las opciones de historial del proyecto, como `Guardar historial`, que conserva tu historial de deshacer al guardar el proyecto. Una insignia verde en el botón indica que el historial se guarda con el proyecto. Consulta [Historial](history.md#save-history) para más detalles.

### ![](/icons/save.webp) Guardar {#save}
Guarda el proyecto de Nomad. Si el proyecto nunca se ha guardado, se te pedirá un nombre.

### ![](/icons/save_as.webp) Guardar como... {#save-as}
Guarda el proyecto con otro nombre, como un proyecto nuevo.

### ![](/icons/save_as.webp) Sobrescribir... {#overwrite}
Muestra el explorador de proyectos para guardar la escena actual encima de otro proyecto. Activa `Solo objetos seleccionados` para guardar solo los objetos seleccionados en lugar de toda la escena. El explorador también tiene un botón `Guardar como...` para guardar como un proyecto nuevo.

### ![](/icons/pencil.webp) Renombrar {#rename}
Muestra un cuadro de texto para renombrar el proyecto actual.

### ![](/icons/open.webp) Abrir... {#open}
Muestra el explorador de proyectos para abrir un proyecto.

### ![](/icons/add_file.webp) Añadir a la escena... {#add}
Muestra el explorador de proyectos; al seleccionar un proyecto, su contenido se fusiona con la escena actual.

### ![](/icons/trash.webp) Eliminar... {#delete}
Muestra el explorador de proyectos; los proyectos que selecciones se eliminan del sistema de archivos.

### ![](/icons/new_file.webp) Nuevo {#new}
Empieza un proyecto nuevo; si hay cambios sin guardar, se te pedirá que lo confirmes. La confirmación te permite `Mantener` o `Restablecer` los ajustes de `Fondo`, `Entorno`, `MatCap` y `Rayos X`, y elegir si el proyecto nuevo usa `Guardar historial`.

### ![](/icons/autosave.webp) Guardado automático... {#auto-save}
Menú con las opciones de guardado automático. Activa `Guardado automático` para guardar tu proyecto en un archivo aparte a intervalos regulares. La insignia del botón indica si está activado.

Nomad no guarda en segundo plano porque los archivos 3d pueden ser bastante pesados, y eso podría provocar un retraso notable mientras esculpes.

Además, para evitar problemas de falta de memoria, la escena normalmente se comprime antes de guardarla.
Esta compresión y descompresión también ralentiza el guardado.

### Intervalo de guardado {#timer-pop-up}
Cuántos minutos espera Nomad entre dos guardados automáticos.

### Mostrar cuenta atrás {#popup-timeout}
Muestra una cuenta atrás antes de cada guardado automático, para que puedas cancelarlo si estás en mitad de algo. Si está desactivado, Nomad guarda en cuanto dejas de esculpir.

### ![](/icons/trash.webp) Descartar guardado automático {#discard-autosave}
Si existe un archivo de guardado automático para un proyecto, se carga automáticamente en lugar del proyecto original. Si no lo necesitas, este botón elimina el guardado automático. Al cargar el archivo se cargará entonces el último guardado manual del proyecto.

### ![](/icons/open.webp) Abrir guardado anterior {#open-outdated-save}
Cuando un proyecto tiene a la vez un guardado automático y un guardado manual, este botón abre el más antiguo de los dos (`Abrir guardado automático anterior` o `Abrir guardado manual anterior`), con su fecha. Muy práctico si el último guardado no es el que querías.

### ![](/icons/storage.webp) Eliminado recientemente... {#recently-deleted}
Nomad conserva durante unos días los datos de los proyectos que han salido de la carpeta de proyectos y los archivos sustituidos por una importación, antes de eliminarlos definitivamente. Los archivos que no se pudieron importar se quedan hasta que los elimines. Esta lista los muestra con su tamaño y su fecha, para que puedas eliminarlos uno a uno o con `Eliminar todo`.

## Importar {#import}

### ![](/icons/add_file.webp) Importar {#import-button}
Para importar archivos 3d que no son proyectos de Nomad.

Al importar un archivo de escena externo en Nomad, puedes *añadirlo* o empezar un proyecto *nuevo* con él.

Si lo añades, los objetos simplemente se suman a la escena actual.
Si eliges `Nuevo`, se crea un proyecto de Nomad nuevo con esos objetos.

La ventana de importación lista todos los archivos que hayas elegido, cada uno con sus propias opciones de importación. Las imágenes también se pueden importar así: elige para cada una si será un `HDRI`, un `MatCap`, una `Referencia`, un `Alfa`, `Texturas` o un `VDM`.

Nomad puede importar estos formatos:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), en las plataformas que lo admiten

### ![](/icons/cog.webp) Configuración {#advanced}
El botón `Configuración...` junto a la miniatura del proyecto muestra las principales opciones de importación. Estos ajustes no se guardan, y la ventana de importación muestra las opciones que se aplican a los archivos que estás importando.

### Todos los formatos {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Mantener topología {#keep-topology}
Por defecto, Nomad intenta reparar la geometría problemática al cargarla. Si activas esta opción, Nomad no reordena vértices ni caras, no fusiona duplicados y no elimina los vértices sin usar.

::: warning
Con `Mantener topología`, operaciones como Booleano, Unir, Diezmar o Manifold podrían no fusionar los vértices duplicados.
:::

#### ![](/icons/image.webp) Omitir texturas {#skip-textures}
No carga las texturas incrustadas en el archivo, en los formatos que lo admiten, como glTF.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) Cargar ajustes de la interfaz {#keep-gui-settings}
Al abrir o importar un archivo de proyecto, carga todos los ajustes de la interfaz que se guardaron en él.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) Dividir OBJ por grupos {#split-obj-by-groups}
Separa los grupos del OBJ en objetos distintos.

#### ![](/icons/vertex.webp) Fusionar posiciones duplicadas {#merge-duplicate-positions}
Fusiona los vértices que comparten la misma posición.

#### ![](/icons/uv.webp) Fusionar UV duplicados {#merge-duplicate-uvs}
Fusiona las coordenadas de textura que comparten el mismo UV.

#### ![](/icons/paint.webp) Espacio de color {#color-space}
Indica cómo se interpreta el color del archivo: `Auto`, `Lineal` o `sRGB`. Prueba a cambiar esta opción si los colores no se ven bien.

#### ![](/icons/image.webp) Formato {#normal-format}
El formato de los mapas de normales de las texturas: `Auto`, `OpenGL (+Y)` o `DirectX (-Y)`. Prueba el otro si los detalles del mapa de normales se ven invertidos.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Espacio de color {#color-space-ply}
Indica cómo se interpreta el color del archivo: `Auto`, `Lineal` o `sRGB`.


### FBX {#fbx}
#### ![](/icons/uv.webp) Fusionar UV duplicados {#merge-duplicate-uvs-fbx}
Fusiona las coordenadas de textura que comparten el mismo UV.

#### ![](/icons/paint.webp) Espacio de color {#color-space-fbx}
Indica cómo se interpreta el color del archivo: `Auto`, `Lineal` o `sRGB`.

#### ![](/icons/image.webp) Formato {#normal-format-fbx}
El formato de los mapas de normales de las texturas: `Auto`, `OpenGL (+Y)` o `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Espacio de color {#color-space-usd}
Indica cómo se interpreta el color del archivo: `Auto`, `Lineal` o `sRGB`.

#### ![](/icons/image.webp) Formato {#normal-format-usd}
El formato de los mapas de normales de las texturas: `Auto`, `OpenGL (+Y)` o `DirectX (-Y)`.



## Exportar {#export}
Guarda en un formato de geometría 3d que se puede usar en otros programas. 

![](/images/file_export.webp)

Cada formato de archivo admite funciones distintas, así que las opciones disponibles cambian según el tipo de archivo elegido.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Colores de vértices](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [PBR de vértices](#pbr-paint)   | ✅     | Nomad ✅<br>Otros ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quads                           | ✅     | Nomad ✅<br>Otros ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Capas](#layers)                | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objetos                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Grupo de caras                  | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Jerarquía                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Luces                           | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Texturas                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Primitivas, posprocesado, etc.  | ✅     | Nomad ✅<br>Otros ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Botón Exportar {#export-button}
Tócalo para exportar la geometría con los ajustes elegidos. El botón muestra el formato elegido y una estimación del tamaño del archivo. En Android, un botón `Compartir` al lado envía el archivo directamente a otra aplicación.

### Formato de archivo {#file-format}
Elige el formato de exportación: `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` o `USD`. NOMAD es el formato propio de Nomad y no se abre en otros programas, así que sirve sobre todo para volver a importar en Nomad.

### Incluir {#allvisibleselected}
Elige qué objetos se exportan: `Todo`, `Visible` o `Seleccionados`. El número junto a cada opción indica cuántos objetos se exportarán.

### Un archivo por objeto {#one-file-per-object}
Exporta cada objeto en su propio archivo. El número indica cuántos archivos se escribirán.

### Tipo {#type}
Cuando la exportación escribe varios archivos (un archivo por objeto, o un OBJ con texturas), los guarda en una `Carpeta` o en un `Zip`. Algunas aplicaciones (Google Drive, One Drive, etc.) no admiten importar carpetas, así que puedes usar Zip en su lugar.

### Incrustar historial {#embed-history}
Solo NOMAD. Incluye el historial de deshacer dentro del archivo; se restaura al abrir el archivo en Nomad. Aumenta el tamaño del archivo y necesita que toda la escena se exporte en un único archivo.

### Incrustar recursos {#embed-assets}
Solo NOMAD. Incluye en el archivo tus matcaps, entornos y fuentes personalizados. Los recursos incluidos de serie no se incrustan.

### Colores de vértices {#vertex-colors}
Exporta los colores de vértices si el formato de archivo lo admite. Algunos programas 3d pueden leerlos, pero no todos.

Para OBJ puedes elegir:
* `Ninguno` - Sin colores.
* `RGB` - Los colores se añaden a continuación de los vértices.
* `MRGB (ZBrush)` - Otra forma de codificar el color, que también admite los datos de máscara.

### Espacio de color {#color-space-export}
Solo OBJ, con colores de vértices `RGB`. Escribe los colores en `Lineal` o en `sRGB`.

### Pintura PBR {#pbr-paint}
Exporta la pintura de rugosidad, metalicidad y máscara. Otros programas pueden ignorar estos datos.
Los colores de vértices PBR se exportan como atributos de color de vértices secundarios.
Los canales se empaquetan así:

|           | Canal    |
| :-------: | :------: |
| Rugosidad | R        |
| Metalicidad | G      |
| Máscara   | B        |


### Capas {#layers}
Las capas se exportan mediante los morph targets de glTF. glTF lo admite oficialmente, así que debería funcionar también en otros programas.
Nomad también exporta los colores, la rugosidad y la metalicidad de cada capa, pero los demás programas los ignorarán.

### Pintura de capa {#layer-painting}
Exporta la pintura de las capas, que normalmente ignoran los demás programas.

### Grupo de caras {#face-group}
Exporta los grupos de caras; a veces pueden dar problemas en otros programas.

### Escribir objetos {#write-objects}
Solo OBJ. Mantiene los objetos separados. Desactívalo para exportarlo todo como un único objeto, por ejemplo para usar la función 'Mesh ID / Polygroup' de Substance Painter.

### Normales {#normals}
Exporta la información de normales. Ten en cuenta que Nomad siempre calcula sus propias normales al importar otros formatos de archivo.

### Tangencias {#tangents}
Exporta la información de tangentes, que se usa si el modelo tiene mapas de normales. 

### Texturas {#textures}
Si se han añadido texturas al material, se exportan. Ten en cuenta que esto no hornea texturas: eso se hace con las opciones de horneado de Topología.

### Formato {#fbx-format}
Solo FBX. `Binario` ocupa menos, pero puede no funcionar en todas las aplicaciones; `ASCII` es un archivo de texto.

### Comprimido {#compressed}
Solo FBX. Reduce el tamaño del archivo a cambio de una exportación y una importación más lentas.

### Preajuste {#usd-preset}
Solo USD. Elige la aplicación a la que va destinada la exportación: `OpenUSD`, `Apple`, `Procreate` o `Zbrush`. Algunas opciones solo están disponibles con ciertos preajustes.

### Instancia {#instance}
Solo USD. Exporta los objetos instanciados como instancias, en lugar de duplicar su geometría.

### Permitir cizallamiento {#allow-skew}
Solo USD. Permite el cizallamiento en las matrices de transformación. Si está desactivado, Nomad separa las transformaciones con cizallamiento en transformaciones de escala y de rotación independientes.

### Repetidor {#repeater}
Solo USD. Exporta como instancias las copias creadas por los repetidores.

### Unir copias {#join-copies}
Cada objeto y las copias de su repetidor pasan a ser un único objeto.

::: tip Consejo: importar la rugosidad y la metalicidad en Blender

Blender puede importar glTF/glb, pero no interpreta automáticamente los atributos de vértice de metalicidad y rugosidad. Para usarlos, crea un nodo Vertex Color en el editor de materiales y pon en su propiedad el siguiente atributo de color (normalmente Col.001). Conecta un nodo 'Separate XYZ', envía X a Roughness e Y a Metallic.

Este vídeo muestra el proceso:

![](/videos/blender_pbr.mp4)

::: 

::: tip Consejo: compatibilidad de funciones en USD

USD es un formato complejo: su especificación admite muchas funciones, pero no todos los programas 3d las admiten. OSX/iOS no admiten el color de vértices, por ejemplo. Los modos de preajuste del exportador USD intentan acercarse lo más posible a la compatibilidad con OpenUSD, Apple, Procreate y Zbrush.

::: 

## ![](/icons/screen.webp) Renderizado {#render}

Exporta una imagen que combina todos los ajustes del proyecto (luces, materiales, posprocesado, etc.). 

![](/images/file_render.webp)
### ![](/icons/preview.webp) Vista previa {#preview}

El botón `Vista previa` junto al título del menú vuelve transparente la interfaz, para que puedas comprobar el encuadre del resultado final.

### ![](/icons/home.webp) Centrar {#focus}
Encuadra la escena o la selección para que quepa en el tamaño del render. Vuelve a tocar para alternar entre las dos.

### ![](/icons/map.webp) Mapa de alturas {#heightmap}
Renderiza la escena como un mapa de alturas en escala de grises visto desde la cámara, en el que las partes más cercanas son las más claras. Al activarlo se pasa a un tamaño `Cuadrado` y se encuadra la selección. Una pequeña barra en el visor te permite ajustar el `Centrar` del degradado.

Con el `Mapa de alturas` activado, aparece un botón `Guardar como alfa` junto al botón de exportar, para guardar el render como un nuevo alfa de pincel en lugar de exportar un archivo.

### ![](/icons/opacity.webp) Fondo transparente {#transparent-background}
Añade un canal alfa al render, útil para combinarlo con otras imágenes en programas 2d. Ten en cuenta que no se admite la transparencia parcial.

### ![](/icons/sliders.webp) Mostrar interfaz {#show-interface}
Incluye la interfaz de Nomad en el render.

### Tamaño final {#final-size}
La resolución del render: `Pantalla`, `720`, `1080`, `4096`, `Cuadrado` o `Personalizado`.

Con el menú Archivos activo, se dibuja un contorno discontinuo en el visor para indicar la zona del render si no coincide con la resolución de la pantalla.

### Ancho / Altura {#render-ratio}
Con `Personalizado`, fija el ancho y la altura de la imagen. El botón de enlace entre los dos reguladores mantiene la proporción al cambiar uno de ellos. Con `Cuadrado`, solo se puede ajustar el ancho.

### ![](/icons/export.webp) Exportar → PNG {#export-png}
Toca este botón para iniciar el render. Al terminar, puedes elegir cómo guardar o compartir la imagen. Los tamaños muy grandes piden antes una confirmación: guarda tu proyecto antes, por si tu dispositivo se queda sin memoria.

## ![](/icons/network.webp) Enlace {#link}

Conecta Nomad con otro dispositivo o aplicación para enviar y recibir objetos, o para sincronizar tus cambios en directo. Un dispositivo hace de anfitrión de la sesión y los demás se unen a ella.

### Activar GoZ {#enable-goz}
Solo en escritorio. Intercambia mallas con ZBrush en este ordenador. `Enviar` las importa en ZBrush y `Obtener` importa desde el ZBrush abierto: `Selección` toma el subtool activo y `Escena` toma todos los subtools. También puedes pulsar GoZ en ZBrush en cualquier momento.

### Modo {#link-mode}
* `Desactivado` - Sin enlace.
* `Anfitrión` - Este dispositivo hace de anfitrión de la sesión y espera a que otros se unan.
* `Unirse` - Busca los dispositivos cercanos y luego toca el nombre del anfitrión para unirte.

Para enlazar dos Nomad, elige `Anfitrión` en un dispositivo y `Unirse` en los demás. Para enlazar con Blender, Nomad debe ser el anfitrión: el botón de ayuda junto al título `Enlace` explica cómo instalar la extensión Nomad Blender Link.

### ![](/icons/network.webp) Puerto de red {#network-port}
El puerto de red que usa el enlace. Cámbialo solo si otra aplicación ya lo usa.

### Enviar / Obtener {#send-get}
Una vez conectado, puedes `Enviar` tu `Selección` o toda la `Escena` al otro dispositivo, u `Obtener` las suyas. `Reemplazar` elimina la escena actual y luego obtiene la escena del otro dispositivo.

### ![](/icons/link.webp) Sincronización en directo {#live-sync}
Transmite tus cambios al otro dispositivo mientras trabajas. `Vista de trabajo` sincroniza también la cámara. `Ediciones de la escena` indica qué dispositivo envía los cambios: `Auto` da la dirección según la actividad más reciente. Después elige qué se sincroniza: `Objetos y geometría`, `Materiales`, `Luces`, `Cámaras` y, cuando el otro lado lo admite, `Sombreado` y `Posprocesado`.

::: tip
Los objetos existentes necesitan primero un `Enviar` u `Obtener` para enlazarlos, antes de que la sincronización en directo pueda actualizarlos.
:::
