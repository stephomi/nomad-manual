# ![](/icons/open.webp) Files {#files}

The files menu allows you to save and load nomad projects, import and export 3d models, export rendered images, and link Nomad with other apps. It has three tabs: `Files`, `Render` and `Link`.

![](/images/file_menu.webp)

## Project {#project}
![](/images/file_project.webp)

The thumbnail at the top shows the current project, with the size of its file, auto save and saved history next to it. Tap the thumbnail to bring up a mini browser of your projects, then tap a project to get a menu to open, add, overwrite, clone, rename or delete it.

When the project has changes that aren't saved yet, `Unsaved changes!` is shown under the thumbnail.

### Scope {#scope}
On desktop, choose where your projects are saved:
* `Internal` - The default, same as on mobile. Projects are saved only inside the main Nomad folder.
* `In Place` - When you open a project from outside the Nomad folder, saving overwrites the original file. Auto Save doesn't work for these external projects.

### ![](/icons/nomad.webp) Preset {#preset}
Access a collection of demos and character components. Select one, then select again to choose to `Open` it or `Add to scene`. You can also download free models from Poly Haven from this browser.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) History... {#history}
Quick access to the history options of the project, such as `Save history`, which keeps your undo history when the project is saved. A green badge on the button shows that the history is saved with the project. See [History](history.md#save-history) for details.

### ![](/icons/save.webp) Save {#save}
Save the Nomad project. If the project has never been saved, you'll be asked for a name.

### ![](/icons/save_as.webp) Save As... {#save-as}
Save the project under a new name, as a new project.

### ![](/icons/save_as.webp) Overwrite... {#overwrite}
Display the project browser to save the current scene over another project. Enable `Only include selected objects` to save just the selected objects instead of the whole scene. The browser also has a `Save As...` button to save as a new project instead.

### ![](/icons/pencil.webp) Rename {#rename}
Display a text box to rename the current project.

### ![](/icons/open.webp) Open... {#open}
Display the project browser to open a project.

### ![](/icons/add_file.webp) Add to scene... {#add}
Display the project browser, when a project is selected its contents will be merged with the current scene.

### ![](/icons/trash.webp) Delete... {#delete}
Display the project browser, any selected projects will be deleted from the file system.

### ![](/icons/new_file.webp) New {#new}
Start a new project, if there are unsaved changes you will be asked to confirm. The confirmation lets you `Keep` or `Reset` the `Background`, `Environment`, `MatCap` and `X-Ray` settings, and choose whether the new project uses `Save history`.

### ![](/icons/autosave.webp) Auto Save... {#auto-save}
Menu to control auto save options. Enable `Auto Save` to save your project in a separate file at regular intervals. The badge on the button shows whether it's on.

The reason why Nomad doesn't save in background is because 3d files can be pretty big so it can induce a significant lag while you are sculpting.

Additionally, to avoid out-of-memory issues the scene is typically compressed before the saving operation.
This compression/decompression will slow down the save operation as well.

### Save interval {#timer-pop-up}
How many minutes Nomad waits between auto saves.

### Show countdown {#popup-timeout}
Show a countdown before each auto save, so you can cancel it if you're in the middle of something. When disabled, Nomad saves as soon as you stop sculpting.

### ![](/icons/trash.webp) Discard Auto Save {#discard-autosave}
If an auto save file exists for a project, it will automatically be loaded instead of the original project. If this isn't required, this button will delete the autosave. Loading the file will then load the last manual save of the project.

### ![](/icons/open.webp) Open outdated save {#open-outdated-save}
When a project has both an auto save and a manual save, this button opens the older of the two (`Open outdated auto save` or `Open outdated manual save`), with its date. Handy if the latest save isn't the one you wanted.

### ![](/icons/storage.webp) Recently deleted... {#recently-deleted}
Nomad keeps the data of projects that left the projects folder, and files replaced by an import, for a number of days before deleting them for good. Files that failed to import stay until you delete them. This list shows them with their size and date, so you can delete them one by one or with `Delete all`.

## Import {#import}

### ![](/icons/add_file.webp) Import {#import-button}
For importing 3d files that aren't Nomad projects.

When you import an external scene file to Nomad, you can either *add* it or start a *new* project with it.

Adding a file will simply add the objects into the current scene.
Choosing `New` will create a new Nomad project with the new objects in it.

The import window lists every file you picked, with its own import options. Images can also be imported this way: choose for each one whether it becomes an `HDRI`, a `MatCap`, a `Reference`, an `Alpha`, `Textures` or a `VDM`.

Nomad can import these formats:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), on platforms that support it

### ![](/icons/cog.webp) Settings {#advanced}
The `Settings...` button next to the project thumbnail shows the main import options. These settings are not saved, and the import window shows the options that apply to the files you're importing.

### All formats {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Keep topology {#keep-topology}
Nomad by default will attempt to fix problem geometry on load. Enabling this will stop Nomad from vertex/face reordering, merging duplicates, and removing unused vertices.

::: warning
With `Keep topology`, operations such as Boolean, Join, Decimate or Manifold might not merge duplicate vertices.
:::

#### ![](/icons/image.webp) Skip textures {#skip-textures}
Do not load the textures embedded in the file, for formats that support it like glTF.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) Load UI settings {#keep-gui-settings}
When opening or importing a project file, load all the interface settings that were saved in it.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) Split OBJ by groups {#split-obj-by-groups}
Enable splitting OBJ groups into separate objects.

#### ![](/icons/vertex.webp) Merge duplicate positions {#merge-duplicate-positions}
Merge vertices that share the same position.

#### ![](/icons/uv.webp) Merge duplicate UVs {#merge-duplicate-uvs}
Merge texture coordinates that share the same UV.

#### ![](/icons/paint.webp) Color Space {#color-space}
Set the color mode interpreted from the file as `Auto`, `Linear`, or `sRGB`. Try to toggle this option if the colors seem incorrect.

#### ![](/icons/image.webp) Format {#normal-format}
The normal map format of the textures: `Auto`, `OpenGL (+Y)` or `DirectX (-Y)`. Try the other one if the details of the normal map look inverted.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Color Space {#color-space-ply}
Set the color mode interpreted from the file as `Auto`, `Linear`, or `sRGB`.


### FBX {#fbx}
#### ![](/icons/uv.webp) Merge duplicate UVs {#merge-duplicate-uvs-fbx}
Merge texture coordinates that share the same UV.

#### ![](/icons/paint.webp) Color Space {#color-space-fbx}
Set the color mode interpreted from the file as `Auto`, `Linear`, or `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-fbx}
The normal map format of the textures: `Auto`, `OpenGL (+Y)` or `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Color Space {#color-space-usd}
Set the color mode interpreted from the file as `Auto`, `Linear`, or `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-usd}
The normal map format of the textures: `Auto`, `OpenGL (+Y)` or `DirectX (-Y)`.



## Export {#export}
Save to a 3d geometry format that can be used in other software. 

![](/images/file_export.webp)

Different file formats support different features, the options available will change based on the selected file type.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertex Colors](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex PBR](#pbr-paint)        | ✅     | Nomad ✅<br>Other ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Other ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Layers](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objects                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Face Group                      | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchy                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lights                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Textures                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Primitives, Postprocess, etc    | ✅     | Nomad ✅<br>Other ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Export button {#export-button}
Click this to export the geometry using the selected settings. The button shows the selected format and an estimate of the file size. On Android, a `Share` button next to it sends the file straight to another app.

### File format {#file-format}
Pick the format to export: `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` or `USD`. NOMAD is Nomad's own format, it won't load in other software, so it's mostly for re-importing into Nomad.

### Include {#allvisibleselected}
Choose which objects will be exported: `All`, `Visible` or `Selected`. The number next to each option shows how many objects will be exported.

### One file per object {#one-file-per-object}
Export each object in its own file. The number shows how many files will be written.

### Type {#type}
When the export writes several files (one file per object, or OBJ with textures), save them in a `Folder` or a `Zip`. Some apps (Google Drive, One Drive, etc) don't support folder import, so you can use Zip instead.

### Embed history {#embed-history}
NOMAD only. Include the undo history inside the file, it will be restored when the file is opened in Nomad. It increases the file size, and needs the whole scene to be exported as a single file.

### Embed assets {#embed-assets}
NOMAD only. Include your custom matcaps, environments, and fonts in the file. Built-in assets are not embedded.

### Vertex colors {#vertex-colors}
Export vertex colors if supported by the file format. Some 3d software can read them, but not all.

For OBJ you can choose:
* `None` - No colors.
* `RGB` - Colors are appended after the vertices.
* `MRGB (ZBrush)` - An alternative way to encode color, which also supports mask data.

### Color Space {#color-space-export}
OBJ only, with `RGB` vertex colors. Write the colors as `Linear` or `sRGB`.

### PBR paint {#pbr-paint}
Export roughness, metalness and mask painting. Other software may ignore this data.
PBR vertex colors are exported as secondary vertex colors attributes.
The channels are packed in the following way:

|           | Channel  |
| :-------: | :------: |
| Roughness | R        |
| Metalness | G        |
| Masking   | B        |


### Layers {#layers}
Layers are supported through glTF morph targets. This is officially supported by glTF, so it should work in other software as well.
Nomad also exports per-layer colors, roughness and metalness but it will be ignored by other software.

### Layer painting {#layer-painting}
Export layer painting, usually ignored by other software.

### Face Group {#face-group}
Export facegroups, exporting can sometimes interfere with other software.

### Write Objects {#write-objects}
OBJ only. Keep objects separated. Disable it to export everything as a single object, for example to use the Substance Painter 'Mesh ID / Polygroup' feature.

### Normals {#normals}
Export normal information. Note that Nomad will always compute its own normals when importing other file formats.

### Tangents {#tangents}
Export tangent information, used if the model has normal maps. 

### Textures {#textures}
If textures have been added to the material, they will be exported. Note that this will not bake textures, that is done via the bake options in topology.

### Format {#fbx-format}
FBX only. `Binary` is smaller but might not work in every application, `Ascii` is a text file.

### Compressed {#compressed}
FBX only. Reduces file size at the cost of slower export and import.

### Preset {#usd-preset}
USD only. Pick the app you're exporting for: `OpenUSD`, `Apple`, `Procreate` or `Zbrush`. Some options are only available for some presets.

### Instance {#instance}
USD only. Export instanced objects as instances, instead of duplicating their geometry.

### Allow skew {#allow-skew}
USD only. Allow skew in the matrix transforms. When disabled, Nomad splits skewed transforms into separate scaling and rotating transforms.

### Repeater {#repeater}
USD only. Export the copies made by repeaters as instances.

### Join copies {#join-copies}
Each object and its repeater copies become a single object.

::: tip Tip: Import roughness and metalness to Blender

Blender can import glTF/glb, but doesn't automatically understand vertex attributes for metalness and roughness. To use them, in the material editor create a Vertex Color node, set its property to the next color attribute (usually Col.001). Connect a 'Separate XYZ' node, send X to roughness, and Y to Metallic.

This video shows the process:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tip: USD feature support

USD is a complex format, it's specification supports many features, but not all 3d software will support them. OSX/iOS don't support vertex color for example.  The preset modes within the USD exporter attempt a best guess at  compatibility with OpenUSD, Apple, Procreate, Zbrush.

::: 

## ![](/icons/screen.webp) Render {#render}

Export an image that is the combination of all the settings in the project (lights, materials, post processing etc). 

![](/images/file_render.webp)
### ![](/icons/preview.webp) Preview {#preview}

The `Preview` button next to the menu title makes the interface see-through, to help preview the framing of the final result.

### ![](/icons/home.webp) Focus {#focus}
Frame the scene or the selection so it fits the render size. Tap again to switch between the two.

### ![](/icons/map.webp) Heightmap {#heightmap}
Render the scene as a grayscale height map seen from the camera, the closest parts being the brightest. Enabling it switches to a `Square` size and frames the selection. A small bar in the viewport lets you adjust the `Focus` of the gradient.

When `Heightmap` is on, a `Save as alpha` button appears next to the export button, to save the render as a new brush alpha instead of exporting a file.

### ![](/icons/opacity.webp) Transparent background {#transparent-background}
Enable an alpha channel for the render, useful to combine the render with other images in 2d programs. Note that partial transparency is not supported.

### ![](/icons/sliders.webp) Show interface {#show-interface}
Enable including Nomad's UI in the render.

### Final size {#final-size}
The resolution to use for the render: `Screen`, `720`, `1080`, `4096`, `Square` or `Custom`.

When the File menu is active, a dashed overlay will be drawn in the viewport to indicate the render region if it does not match the screen resolution.

### Width / Height {#render-ratio}
With `Custom`, set the width and height of the image. The link button between the two sliders keeps the ratio when you change one of them. With `Square`, only the width can be set.

### ![](/icons/export.webp) Export → PNG {#export-png}
Click this button to start the render process. When complete you can then choose how to save or share the image. Very large sizes ask for a confirmation first: save your project before, in case your device runs out of memory.

## ![](/icons/network.webp) Link {#link}

Connect Nomad with another device or app, to send and receive objects, or to sync your edits live. One device hosts the session, the others join it.

### Enable GoZ {#enable-goz}
Desktop only. Exchange meshes with ZBrush on this computer. `Send` imports them into ZBrush, `Get` imports from the running ZBrush: `Selection` takes the active subtool, `Scene` takes all subtools. You can also press GoZ in ZBrush at any time.

### Mode {#link-mode}
* `Off` - No link.
* `Host` - This device hosts the session and waits for others to join.
* `Join` - Search the nearby devices, then tap the host's name to join it.

To link two Nomad, pick `Host` on one device and `Join` on the others. To link with Blender, Nomad should be the host: the help button next to the `Link` title shows how to install the Nomad Blender Link extension.

### ![](/icons/network.webp) Network port {#network-port}
The network port used by the link. Change it only if another app already uses it.

### Send / Get {#send-get}
Once connected, `Send` your `Selection` or the whole `Scene` to the other device, or `Get` them from it. `Replace` deletes the current scene, then gets the other device's scene.

### ![](/icons/link.webp) Live sync {#live-sync}
Stream your edits to the other device as you work. `Working view` also syncs the camera. `Edits` sets which device sends the edits: `Auto` gives the direction to the latest activity. Then choose what is synced: `Objects & geometry`, `Materials`, `Lights`, `Cameras`, and when the other side supports it, `Shading` and `PostProcess`.

::: tip
Existing objects need one `Send` or `Get` first, to link them before live sync can update them.
:::
