# ![](/icons/open.webp) Archivos

El menú de archivos te permite guardar y cargar proyectos de Nomad, importar y exportar modelos 3D y exportar imágenes renderizadas.

![](/images/file_menu.webp)

## Proyecto
![](/images/file_project.webp)

Se muestra una miniatura del último guardado en la parte superior de este menú. Al hacer clic en esta miniatura aparece un mini navegador; toca dos veces en otro proyecto para mostrar un mini menú para abrir, añadir, guardar, clonar, renombrar o borrar ese proyecto.

### ![](/icons/nomad.webp) Preajuste 
Accede a una colección de demostraciones y componentes de personajes. Selecciona uno y vuelve a seleccionarlo para elegir Abrir, Añadir a la escena o Clonar la entrada en tu carpeta de proyectos.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Guardar
Guarda el proyecto de Nomad.

### ![](/icons/save_as.webp) Guardar como...
Muestra el navegador de proyectos para permitirte guardar el proyecto de Nomad con un nombre nuevo.

### ![](/icons/pencil.webp) Renombrar
Muestra un cuadro de texto para renombrar el proyecto actual.

### ![](/icons/open.webp) Abrir...
Muestra el navegador de proyectos para abrir un proyecto.

### ![](/icons/add_file.webp) Añadir a la escena...
Muestra el navegador de proyectos; cuando se selecciona un proyecto, su contenido se fusionará con la escena actual.

### ![](/icons/trash.webp) Borrar...
Muestra el navegador de proyectos; cualquier proyecto seleccionado se borrará del sistema de archivos.

### ![](/icons/new_file.webp) Nuevo
Inicia un proyecto nuevo; si hay cambios sin guardar se te preguntará si quieres guardar.

### ![](/icons/autosave.webp) Autoguardado...
Menú para controlar las opciones de autoguardado.

Si activas el autoguardado, puedes configurar un temporizador para que aparezca una ventana emergente a intervalos regulares.
La razón por la que Nomad no guarda en segundo plano es porque los archivos 3D pueden ser bastante grandes, por lo que puede provocar un retraso significativo mientras esculpes.

Además, para evitar problemas de falta de memoria, la escena suele comprimirse antes de la operación de guardado.
Esta compresión/descompresión también ralentizará la operación de guardado.

### Ventana emergente del temporizador
Con qué frecuencia aparecerá la ventana emergente del temporizador.

### Tiempo de espera de la ventana emergente
Activa el tiempo de espera de la ventana emergente.

### Descartar autoguardado
Si existe un archivo de autoguardado para un proyecto, se cargará automáticamente en lugar del proyecto original. Si esto no es necesario, este botón borrará el autoguardado. Cargar el archivo entonces cargará el último guardado manual del proyecto.


## Importar

### ![](/icons/add_file.webp) Importar
Para importar archivos 3D que no sean proyectos de Nomad.

Cuando importas un archivo de escena externo a Nomad, puedes *importarlo* o *añadirlo*.

Añadir un archivo simplemente añadirá los objetos a la escena actual.
Importar un archivo creará un nuevo proyecto de Nomad con los nuevos objetos en él.

Nomad puede importar estos formatos:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx, experimental)

### ![](/icons/cog.webp) Avanzado
Muestra las opciones avanzadas de importación:

### Proyecto/ glTF / OBJ / STL / FBX
#### Conservar topología
Nomad, de forma predeterminada, intentará corregir la geometría problemática al cargar. Activar esto evitará que Nomad reordene vértices/caras, elimine duplicados de vértices/caras o elimine vértices sin usar.

#### Omitir texturas
Omite la carga de texturas para formatos que lo admiten, como glTF.

### Proyecto / glTF
#### Conservar ajustes de la interfaz
Activa el guardado de la interfaz gráfica y los ajustes del proyecto dentro del archivo .nom de Nomad o del archivo glTF.

### OBJ
#### Dividir OBJ por grupos
Activa la división de grupos OBJ en objetos separados.

#### Espacio de color
Establece el modo de color interpretado desde el OBJ como Lineal, sRGB o Automático.

### PLY
#### Espacio de color
Establece el modo de color interpretado desde el PLY como Lineal, sRGB o Automático.


### FBX
#### Espacio de color
Establece el modo de color interpretado desde el OBJ como Lineal, sRGB o Automático.



## Exportar
Guarda en un formato de geometría 3D que pueda usarse en otro software. 

![](/images/file_export.webp)

Los distintos formatos de archivo admiten diferentes funciones; las opciones disponibles cambiarán según el tipo de archivo seleccionado.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertex Colors](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex PBR](#vertex-pbr)       | ✅     | Nomad ✅<br>Other ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Other ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Layers](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objects                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Face Group                      | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchy                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lights                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Textures                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | Import ✅<br>Export ❌ |
| Primitives, Postprocess, etc    | ✅     | Nomad ✅<br>Other ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### Todo/Visible/Seleccionado
El estado activo del botón establecerá qué objetos se exportarán. El número junto a los iconos indica cuántos objetos se exportarán para esa opción.

### Colores de vértice
Exporta colores de vértice si el formato de archivo lo admite.

### Pintura PBR
Los colores de vértice PBR se exportan como atributos secundarios de colores de vértice.
Los canales se empaquetan de la siguiente manera:

|           | Canal   |
| :-------: | :-----: |
| Rugosidad | R       |
| Metalidad | G       |
| Enmascar. | B       |


### Capas
Las capas son compatibles mediante objetivos de morph de glTF.
Nomad también exporta colores, rugosidad y metalidad por capa, pero serán ignorados por otros programas.

### Pintura de capas
Exporta la pintura de capas, normalmente ignorada por otros programas.

### Grupo de caras
Exporta grupos de caras; la exportación a veces puede interferir con otros programas.

### Normales
Exporta información de normales. Ten en cuenta que Nomad siempre calculará sus propias normales al importar otros formatos de archivo.

### Tangentes
Exporta información de tangentes, usada si el modelo tiene mapas de normales. 

### Texturas
Si se han añadido texturas al material, se exportarán. Ten en cuenta que esto no hornea texturas; eso se hace mediante las opciones de horneado en topología.

### Botón Exportar
Haz clic en esto para exportar la geometría usando los ajustes seleccionados.

::: tip Tip: Importar rugosidad y metalidad en Blender

Blender puede importar glTF/glb, pero no interpreta automáticamente los atributos de vértice para metalidad y rugosidad. Para usarlos, en el editor de materiales crea un nodo Vertex Color, establece su propiedad en el siguiente atributo de color (normalmente Col.001). Conecta un nodo 'Separate XYZ', envía X a Roughness y Y a Metallic.

Este vídeo muestra el proceso:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tip: Compatibilidad de funciones USD

USD es un formato complejo; su especificación admite muchas funciones, pero no todo el software 3D las admite. macOS/iOS, por ejemplo, no admiten color de vértice. Los modos preestablecidos dentro del exportador USD intentan una mejor aproximación de compatibilidad con OpenUSD, Apple, Procreate y ZBrush.

::: 

## Renderizar

Exporta una imagen que es la combinación de todos los ajustes del proyecto (luces, materiales, postprocesado, etc.). 

![](/images/file_render.webp)
### Vista previa

El pequeño botón de vista previa junto al título del menú atenuará las barras de herramientas para ayudar a previsualizar el resultado final.

### Fondo transparente
Activa un canal alfa para el render, útil para combinar el render con otras imágenes en programas 2D. Ten en cuenta que la transparencia parcial no es compatible.

### Mostrar interfaz
Activa la inclusión de la interfaz de Nomad en el render.

### Proporción de render
Un multiplicador sobre la resolución de la imagen.

### Tamaño final
La resolución que se usará para el render. Cuando se selecciona `Personalizado`, se activarán los deslizadores de ancho y alto. 

Cuando el menú Archivo está activo, se dibujará una superposición discontinua en el visor para indicar la región de render si no coincide con la resolución de la pantalla (ten en cuenta que debes estar en modo apaisado para que esto sea correcto).

### Exportar png
Haz clic en este botón para iniciar el proceso de renderizado. Cuando termine, podrás elegir cómo guardar o compartir la imagen.
