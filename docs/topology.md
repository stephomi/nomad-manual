# ![](/icons/multires.webp) Topology {#topology}

This menu controls the topology of objects in Nomad, as well as tools to bake and transfer details between objects, and between textures.

![](/images/topology_overview.webp)

Nomad is based on polygons, it uses triangles and quads to handle the geometry.
By topology, we refer to both the number of faces but also the way points (vertices) are connected.

It's important to keep track of the topology, especially if you want to sculpt or paint fine details.

::: tip How to keep track of your topology?
You can display the [Wireframe](settings.md#wireframe) or simply disable [Smooth Shading](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

The topology menu of Nomad has several tabs, on two rows:

| Method                                | Icon                         | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Edit multiple levels of detail using subdivision                 |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | Recompute a new topology with uniform density                    |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | Add/Remove faces locally in real-time when sculpting or painting |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | Close holes, force manifold and convert to triplanar             |
| [Primitive](#primitive)               | ![](/icons/dot.webp)        | Primitive options                                                |
| [Decimate](#decimation)               | ![](/icons/decimate.webp)      | Reduce the number of faces while keeping the shape            |
| [Quad Remesh](#quad-remesh)           | ![](/icons/quad.webp)       | Rebuild the object with a clean quad layout                      |
| [UV Unwrap](#uv-unwrap)               | ![](/icons/uv.webp)         | Create UVs for texturing                                         |
| [Bake](#bake)                         | ![](/icons/bake.webp)       | Bake details and paint to textures, vertices or VDM stamps       |


## Polygon stats {#polygon-stats}

![](/images/topology_stats.webp)

The top section of every tab shows polygon counts for the selected object, and for the whole scene when it has more than one object. The columns are the number of vertices, triangles, quads (4 sided polygons) and UV coordinates (0 when the object has no UVs).

Tap on this section to list every object of the scene with its exact counts, including its number of face groups.

## ![](/icons/cog.webp) Gear menu {#gear-menu}
Some sections, like the ones in the [Quad Remesh](#quad-remesh) and [Bake](#bake) tabs, have extra options. Open them with the gear icon next to the section title.

## ![](/icons/multires.webp) Multiresolution {#multiresolution}

![](/images/topology_multires_menu.webp)

### What is multiresolution? {#what-is-multiresolution}
The multiresolution feature is useful for two main scenarios:
- The smooth subdivision algorithm to increase the polycount of your object
- Handle multiple level of resolution so that you can alternate between small and large scale edits

![](/videos/multiresolution.mp4)

#### Multiresolution Workflow {#multiresolution-workflow}
One important aspect of the multiresolution is that you can go back to a lower resolution, make changes on your object and then go back to the highest resolution without losing the high resolution details. All the high resolution details will be projected automatically.

[Layers](layers.md#layers) are available on every resolution.

::: warning
If you are using a tool that alters the topology of your object, you will lose all the other resolutions of your object!
You should always get a warning in case it should happen, for example when you are using:
- the [Voxel Remesher](#voxel-remesher)
- the [Dynamic Topology](#dynamic-topology)
- the [Trim tool](tools.md#trim)
- the [Split tool](tools.md#split)
:::


### Multiresolution slider {#multiresolution-slider}
This slider indicates the number of subdivision levels in the current object. If there are 6 vertical bars, there are 6 subdivision levels. The circle indicates the currently displayed subdivision level.

Small icons above the slider show which options (`Lock level 0`, `Linear`, `Sharp border`, `Keep triangles`) were used for each level.

### Reverse {#reverse}
When on the lowest subdivision level, the reverse button will attempt to create a level below the current one. Note that this generally can only happen if the object was created with subdivision to begin with, say in Nomad or in other 3d applications that multiresolution subdivision surfaces.

### Subdivide {#subdivide}
The *Subdivide* button will increase the number of polygons by 4, so make sure to keep an eye on the polycount as it can increase very quickly! Nomad asks for confirmation when the result would be very heavy.
One important aspect of *Subdivision Surface*  is that they will converge to a *Smooth Surface*.
To understand how it works, you can try the *Subdivide* button on an object with only a few polygons.

You can disable this *Smooth* behavior with the `Linear` option.

### Delete lower {#delete-lower}
If there are subdivisions below the currently displayed level, delete them. If you do this by accident, you can recreate them with the Reverse button.

### Delete higher {#delete-higher}
If there are subdivisions above the currently displayed level, delete them.

### ![](/icons/lock.webp) Lock level 0 {#lock-lv0}
Keep the shape of the lowest subdivision level when you sculpt on higher levels. Painting still carries down to level 0. This can be important if your object was generated in another application, and the base object has to remain unchanged.

This option is only available before the first subdivision. When it's off, large changes made at higher subdivision levels will move level 0.

### ![](/icons/linear.webp) Linear {#linear-subdivision}
Subdivide the mesh without applying any smoothing.

### ![](/icons/group.webp) Sharp border {#sharp-border}
If your object has face groups, enabling this option will keep the face group borders sharp. This can be set at each subdivision level (the subdivision slider will have a small icon above the level to indicate this).

### ![](/icons/triangle.webp) Keep triangles {#keep-triangles}
Most standard subdivision surface systems will attempt to convert all polygons to quads during a subdivision operation. This toggle will force the subdivision to use triangles instead.

::: tip

Subdivision will smooth all sharp edges by default. To keep edges slightly sharp, experiment with using `Linear` or `Sharp border` on the first 2 subdivide levels, then turn it off for the higher levels. This will create a semi-sharp subdivided mesh.

:::

### Show highest level {#show-highest-level}
Display the highest level with all its details while you sculpt a lower level. Handy to see the final result while you make large changes.

### Wireframe: Level 0 only {#wireframe-level-0-only}
When the [Wireframe](settings.md#wireframe) is on, only show the wireframe of the lowest level. The dense wireframe of the high levels can hide the shape.


## ![](/icons/voxel.webp) Voxel Remesher {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
When using the `Voxel Remesher`, the entire mesh will force the topology to have an uniform resolution, meaning all the polygons have more or less the same size. This is very useful when you don't want to think about topology and simply do free-form sculpting.

A typical sculpting workflow can start by using the `Voxel Remesher` to block-out a rough shape with a low resolution.
Simply hit the *Remesh* button once in a while when you are stretching the mesh too much to avoid too much distortion.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
As stated above, Nomad is a polygonal software, but the `Voxel Remesher` is one exception where another approach is used (temporarily) to perform the remeshing.

One big difference is that the voxel approach won't accept self intersection, so these will be resolved.
Also it doesn't support meshes with holes in them.

By holes, we don't mean the `genus hole` (`hole` of a donus), but instead mesh that are not `watertight`/`closed`.
Typically, what it means is that before applying the remeshing, every holes will be filled, similarly to the [Trim tool](tools.md#trim) or [Hole filling feature](#holes). The [Holes](#voxel-holes) option below chooses how.
:::

### ![](/icons/voxel.webp) Remesh {#voxel-remesh}
Execute the voxel remesh. Small icons on the button remind you which of the options below are on.

### Resolution {#voxel-resolution}
The size of the voxels used during the calculation, higher values give more detail. While changing this parameter a checkerboard pattern will be overlayed on the mesh to give a preview of the result.

The dropper picks the resolution from the density of the mesh where you tap. The cube button next to it switches the value to an `Edge length` in world units: the same value then gives the same detail on any object.

### Build multiresolution {#build-multiresolution}
Create lower multiresolution levels for the voxel remesh. If you use the checkerboard pattern to set a resolution, and set build multiresolution to 2, the final result will have detail that matches the resolution slider, and if you go to the multires tab, it will be at level 2, meaning you have lower resolution multires meshes at level 1 and level 0. This can be a good way to both generate a clean mesh with even polygons, and have a lower resolution control mesh.

It also runs faster and uses less memory at high resolutions. But with a low resolution and many levels, you'll lose details.

::: tip Tip: Build multiresolution and stable smoothing

This option can sometimes cause 'loops' in the geometry that can be difficult to smooth, causing little pimples. If this happens, enable 'Stable smoothing' in the smooth tool options. 

:::

### Thicken thin parts {#thicken-thin-parts}
Parts thinner than the voxels can break or vanish during the remesh. This option thickens them so they survive, higher values thicken more. It's not available with `Sharp edges` or `Sharp border`.

### Holes {#voxel-holes}
How holes are closed before remeshing:

* `Fill` - Each hole is closed on its own, from its border.
* `Shape` - Holes are closed by following the surrounding surface, and open pieces that overlap are joined.

### ![](/icons/angle.webp) Sharp edges {#keep-sharp-edges}
Snap the new points to sharp edges of the original mesh. It's mostly useful for simple primitive boolean operations, and it can introduce distortion.

### ![](/icons/group.webp) Sharp border {#voxel-sharp-border}
The new faces follow the face group borders, and a border stays sharp where the surface creases along it.

### ![](/icons/group_separate.webp) Keep groups separate {#keep-groups-separate}
Each face group is remeshed on its own: groups never merge, and each one stays a closed piece in its own group. Multiresolution is not built in this mode. It's available when the object has several face groups.

## ![](/icons/dynamic.webp) Dynamic Topology {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Multiresolution and voxel remeshing are common industry methods to control topology, but both require you to watch that you're not stretching polygons too far, or squeezing polgyons too tight. 

Dynamic Topology is an alternative method. As you sculpt, Nomad will adaptively add and remove polygons during the brush stroke, so carving in small details will add many small polygons where you need them, and smoothing elsewhere will take away polygons.

Note that dynamic topology will use triangle polygons rather than quads. This can look a little messy, but it's almost better to not look at the wireframe, just concentrate on making a nice looking sculpt without worrying about topology, then later you can use one of Nomad's other remeshing tools to generate a clean quad mesh.

See the video below in action.

![](/videos/dynamic.mp4)

### Enabled {#enabled}
Turn on dynamic topology. A DynTopo icon will be placed below the brush radius and intensity sliders to allow you to toggle Dyntopo per tool. It can have a noticeable impact on performance, and layers are updated correctly.

### Detail {#dyn-detail}
Control the amount of detail, its behavior changes based on the 'Detail based on...' selection, see below. In `Screen` mode, the label shows the target triangle size in pixels. In `Constant` mode, a dropper lets you pick the detail from the density of the mesh where you tap.

### Detail based on... {#detail-based-on}
| Method   | Description                                                     |
| :------: | :-------------------------------------------------------------: |
| Screen   | The level of detail will depend how big the object is on screen. The detail slider is 100% or higher for fine detail, making small triangles, or 1% for low detail, making big triangles.  |
| Radius   | The tool radius defines the amount of detail. Use a small tool radius, for fine detail, a big tool radius for low detail. The detail slider is a multiplier on this ratio.                     |
| Constant | The detail slider defines the amount of detail, and isn't affected by screen size or tool size. It's the same value as the [Detail](#all-detail) slider of `Remesh`.             |

::: tip TIP: Radius mode

To get a better sense of how radius mode works, start moving the detail slider with one finger, then at the same time change the tool radius with another finger. You will see how they are linked.

:::

### Prefer... {#prefer}
| Method  | Description       |
| :-----: | :---------------: |
| Speed   | Favor performance |
| Quality | Favor quality     |

When you favor `Quality`, the 2 main differences are:
- refinement is applied before sculpting, so you will get less interpolating artifact when painting or sculpting very small details
- refinement is running until it converges to the correct level of detail, in contrast to an incremental behavior.
 
That way, if you sculpt very small details or do quick strokes, the topology will always be refined as expected


### ![](/icons/pressure.webp) Use pressure on radius {#use-pressure-on-radius}
Only relevant if `Radius` is activated. When enabled, the level of detail will always reflect the brush size, even when the brush size is affected by pencil pressure.

### Use stroke falloff {#use-stroke-falloff}

Also include the brush falloff curve and alpha in the dyntopo calculations.

### Method {#method}
Choose how dynamic topology changes the mesh, both while you sculpt and when you use [Remesh](#dyn-remesh):

| Method         | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | It can add and remove faces, this is the mode used in the video above |
| Subdivision    | Add new faces only, it cannot remove faces                            |
| Decimation     | Remove faces only, it cannot add new faces                            |

### ![](/icons/shield.webp) Protect masked area {#protect-masked-area}
Enable masked areas protecting the topology from being changed.

### ![](/icons/normal.webp) Vertex extrapolation {#vertex-extrapolation}
Place the points on a smooth surface that follows the curvature around them, instead of flat on the existing faces.

### Detail {#all-detail}
The resolution used for the remesh operation. If Dyntopo is in 'Constant' mode, it will be the same value as the Detail slider at the top of this menu. The dropper picks the detail from the density of the mesh where you tap.

### Remesh {#dyn-remesh}
Execute a global remesh using the dyntopo algorithm. Usually you should use the [Voxel Remesher](#voxel-remesher) for full remeshing.

However one advantage over the voxels is that the mesh doesn't need to be closed, and the masked area will be protected, so you can have a better control on where to put more or less density.



## ![](/icons/topo_extra.webp) Misc {#misc}

![](/images/topology_misc_menu.webp)

This tab gathers tools to clean or convert the mesh: close its holes, force it to be manifold, or turn it into a triplanar.

### ![](/icons/hole.webp) Holes {#holes}
![](/images/topology_holes_menu.webp)
Most of the time, your object will probably be watertight, meaning the mesh is 'closed'.

If your object has holes, you can fill them.

![](/videos/hole_filling.mp4)

::: tip
When you run the Voxel remesher, all the holes are automatically closed, whether you are using it on 1 or multiple meshes.
:::

#### Close holes {#close-holes}
Execute the hole close action.

#### Options {#holes-gear-menu}
These options change how the holes are filled:

##### Face Group {#fill-face-group}
Choose the face group of the new faces:

* `Mixed` - A hole surrounded by a single face group reuses it, a hole touching several groups gets a new one.
* `New` - The filled holes get a new face group.
* `Reuse` - Each hole takes the face group that surrounds it the most.

##### Detail {#fill-detail}
The polygon density used to fill the hole. While dragging this slider a checkerboard pattern will be shown on the model, this will give an indication of the triangle size to use. The checkbox will disable this, and only use the existing points, which will usually create long thin triangles over the hole, which can be difficult to sculpt.

##### Bridge {#fill-non-manifold}
Fill a hole and the islands inside it as one surface, instead of filling each border on its own. A higher angle bridges more curved holes. The checkbox turns it off.

### ![](/icons/cog.webp) Force Manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Try to clean non manifold edges. It can be useful for external software that don't support edges that have more than 2 faces in common.

#### Clean {#clean}
Execute the clean action.

#### Options {#force-manifold-gear-menu}
This option changes how the mesh is cleaned:

##### Delete small faces {#delete-small-faces}
A threshold used to remove and join small polygons. Enable it with its checkbox.


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
![](/images/topology_triplanar_menu.webp)
Converts the mesh into a [triplanar](scene.md#triplanar) primitive.
You will likely lose a lot of detail in the process: layers, painting and multiresolution are lost too.

#### Force cubic {#force-cubic}
Enable the triplanar to be a cube. Otherwise the triplanar will fit to the closest bounding box around your object.

#### Convert {#convert}
Execute the triplanar action.

#### Resolution {#triplanar-resolution}
The resolution of the triplanar grid, higher values keep more detail.

## ![](/icons/decimate.webp) Decimate {#decimation}

![](/images/topology_decimation.webp)

Reduce the number of polygons by trying to keep as many details as possible, using triangle polygons.

This feature can be useful if you want to export for 3d printing.
However you should probably not use it if you want to continue sculpting on it, as it can produce uneven triangles.

Note that the masked areas won't be decimated.

![](/videos/decimate.mp4)

::: tip

Using the [Quadremesh tool](tools.md#quad-remesher) on high poly objects can take a long time to calculate, and give results that are hard to control. Pre-processing the mesh with [facegroups](tools.md#facegroup) and decimate will make Quadremesh run much faster, and allow much more control over topology.

* Facegroup the mesh to define your ideal quad flow.
* Facegroup relax to get smooth facegroup borders.
* Decimate. This will ensure you have no thin or distorted faces on the facegroup edge. Under `Preserve boundary`, ensure `Face Group` is enabled. This will make triangle edges follow your facegroup edges precisely.
* In the Quadremesh options ensure relax is disabled (as you have already relaxed the mesh) and you should get good results.

:::

### Decimate {#decimate}
Start the decimate operation.

The icons next to the decimate button show the options below, and let you toggle them. The percent indicates how strong that option is.

* ![](/icons/palette.webp)  `Preserve painting` - Place more triangles where there is painting detail.
* ![](/icons/triforce.webp) `Uniform faces` - Prefer making evenly sized triangles.
* ![](/icons/hole.webp)  `Hole` - Decimate will try to keep borders near open geometry and holes unchanged.
* ![](/icons/group.webp) `Face Group` - Decimate will try to keep face group borders unchanged.
* ![](/icons/uv.webp) `UV` - Decimate will try to keep UV borders unchanged.

### Target triangles {#target-triangles}
Set the target triangle count. The default value is 50%, the percent/target button will toggle between a percentage or an exact target poly count.

### Options {#decimate-gear-menu}
Each option has a checkbox to toggle it, and a value for its strength:

#### ![](/icons/palette.webp) Preserve painting {#preserve-painting}
The value will determine how accurately painting detail will be preserved. Higher values will preserve more painting. Set to 0 if you do not care about painting.

#### ![](/icons/triforce.webp) Uniform faces {#uniform-faces}
Higher values will output triangles with similar size.

#### Preserve boundary {#preserve-borders}
Stop borders from being decimated. Border weights can be set for `Hole`, `Face Group` or `UV` borders (`UV` needs an object with UVs).

## ![](/icons/quad.webp) Quad Remesh {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Rebuild the object with a clean quad layout. This tab has several remeshers, each with its own `Remesh` button, `Target quads` slider and gear menu. Try them on your object, they give quite different results!

### Quad Remesher {#quad-remesher}
The same remesher as the [Quad Remesher](tools.md#quad-remesher) tool, developed by [Exoside](https://exoside.com/). It's only available on some platforms, and needs a purchase: until then, the `Remesh` button shows a cart.

`Select tool` switches to the Quad Remesher tool, to draw guides and paint the density. The gear menu holds `Adaptive Quad Count`, `Adaptive Size` (at 100% the quad size follows the curvature, at 0% quads are uniform), `Auto-Detect Hard Edges` and `Reproject Vertex`.

::: tip
Where it's available, Quad Remesher generally gives the best results and the most control.
:::

### AutoRemesher {#autoremesher}
An alternative quad remesher, with options to adapt the quad size and shape to the surface.

#### ![](/icons/cog.webp) AutoRemesher gear menu {#autoremesher-gear-menu}
The gear menu has these advanced options:

##### Edge Scaling {#edge-scaling}
Scale the quad size, higher values produce larger quads.

##### Adaptivity {#adaptivity}
Adapt the quad density to the curvature. 0 produces uniform quads, 1 produces smaller quads in curved areas.

##### Anisotropy {#anisotropy}
Stretch quads along the flattest direction of the surface. 0 produces square quads, 1 produces elongated quads on tubes and ridges.

##### Sharp Edge {#sharp-edge}
Edges bent more than this angle are preserved as sharp features.

##### Smooth Normal {#smooth-normal}
0 keeps the surface faceted during the remeshing. Higher values smooth the surface by taking the vertex normals into account.

##### Max fill hole {#autoremesher-max-fill-hole}
The algorithm can sometimes produce unwanted holes. If a hole has fewer vertices than this value, then it will be filled.

### Instant Mesh {#quad-remesh-instant}
Remesh using the [Instant Meshes algorithm by Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). It will analyze the flow of a mesh and create clean quad topology.

#### Remesh {#instant-remesh}
Start the remesh operation.

#### Target quads {#target-quads}
The number of quad polygons the remesher will attempt to create.

#### ![](/icons/cog.webp) Instant Mesh gear menu {#quad-remesh-instant-gear-menu}
The gear menu has these advanced options:

##### Crease angle {#crease-angle}
A threshold of sharp corners that will try and help guide the remesh operation. Enable it with its checkbox.

##### Max fill hole {#max-fill-hole}
The algorithm can sometimes produce unwanted holes. If a hole has fewer vertices than this value, then it will be filled.

### QuadriFlow {#quadriflow}
Remesh using the QuadriFlow algorithm, another way to get a clean quad layout.

#### ![](/icons/cog.webp) QuadriFlow gear menu {#quadriflow-gear-menu}
The gear menu has these advanced options:

##### Preserve boundary {#quadriflow-preserve-boundary}
Protect hole boundaries.

##### Keep Sharp {#keep-sharp}
Align quads with the sharp edges of the surface.

##### Min Cost Flow {#min-cost-flow}
Use a minimum cost flow solver for the quad layout. Slower, but can produce a more regular topology.

## ![](/icons/uv.webp) UV Unwrap {#uv-unwrap}
Compute texture coordinates (UVs) for the selected object. Nomad has two methods, `UVAtlas` and `BFF`, each with its own `Unwrap` button.

![](/videos/unwrap.mp4)

::: tip UVs?
A common analogy for UV's is wrapping a gift; what is the best way to cut wrapping paper to completely cover an object, with no overlaps? 

Uv's are similar, but instead of cutting the paper, you cut the object. Imagine if your model was made of thin plastic, how would you cut your model apart to unwrap it to lie flat, paint on it in that flat state, then reassemble it?

Now imagine the surface of your model is made of stretchy lycra. You could stretch the model flat, or cut it, or a combination of both. But if you painted a checkerboard on the object when flattened, the checkerboard would be distorted when you reassemble it. Which is a better method, more cuts with less distortion, or less cuts with more distortion?

Uv's are instructions to tell 3d software how to 'cut and stretch' the object when applying textures. The UV Atlas tool generally uses a 'more cuts, less distortion' approach.


:::

::: tip UV's and Nomad and other apps

Most textured models you find online will be textured with UVs. Nomad can import and display this via the [material](material.md#textures) panel.

When models are made in Nomad, you can paint directly onto objects without UVs. If you need to export them to other apps, eg [Procreate](https://procreate.art/), you can 'bake' Nomad color information into textures via UVs. 

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
UVAtlas generally prefers making more islands with cuts, to minimise distortion.

#### Unwrap {#unwrap}
Calculate UVs for the selected object.

#### Options {#uvatlas-gear-menu}
The buttons next to `Unwrap`:

##### Face Group {#atlas-face-group}
When it shows `Yes`, face groups define the cuts for the UV's. This setting is shared with BFF.

##### Delete UVs {#delete-uvs}
The trash button deletes the UVs of the object.

##### Inspect {#uv-inspect}
Show the UVs of the object in the background.

#### Max Stretch {#max-stretch}
Low values create less distortion and more islands, high values create more distortion and less islands. 

#### Island Spacing {#island-spacing}
The amount of padding between the islands. Low values will waste less space, but will risk textures bleeding between islands. 

::: warning
Computing UVs can take some time, it is best to have a mesh with fewer than 100k vertices.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

BFF Uv's favour a 'less cuts, more distortion' approach. 

#### Options {#uv-bff-gear-menu}
The same `Face Group`, delete and `Inspect` buttons as [UVAtlas](#uvatlas-gear-menu) sit next to `Unwrap`.

##### Face Group {#bff-face-group}

Use facegroups to define the cuts for the UV's.

#### Cone count {#cone-count}
Define the number of main projections used. Lower values will produce fewer islands, but more distortion. Higher values take longer to compute.

#### Seamless patches {#seamless-patches}
Affects the layout of the uv patches, it can introduce important distortion. It works best with carefully created facegroups.

::: warning
BFF can create overlapping UVs if the mesh has handles (like the hole of a donut).
:::

### ![](/icons/preview.webp) Show UV after unwrap {#show-uv-after-unwrap}
Open the UV inspector view after unwrapping, so you can check the result right away.

### ![](/icons/bake.webp) Bake: Texture → Texture {#unwrap-bake-texture}
Only available when the material of the object has textures. When you unwrap it again, the textures are transferred onto the new UVs, so they still fit. Its resolution is `Auto` by default, matching the largest texture, or you can set it yourself.

## ![](/icons/bake.webp) Bake {#bake}
This tab transfers details and painting between objects, and between vertices and textures.

`From high-res` uses other objects as the source, the number in brackets is how many. Nomad picks them this way:

- all selected objects are used, and the main selected object is the target (strongest highlight in the [Scene](scene.md) menu)
- if only one object is selected, Nomad uses all visible objects instead
- if every other object is hidden (for example with Solo), the entire scene is used

### ![](/icons/bake.webp) Bake → Texture {#bake-texture}
![](/images/topology_bake_menu.webp)

Texture baking will create textures by projecting other visible objects in the scene into the uv's of the selected object. The object needs UVs.

Here is the typical workflow for baking:
- You have a mesh with fine details and painting
- Clone it
- Decimate it (set `Preserve painting` to 0)
- UV unwrap it
- Bake it!

You should now have a low-resolution mesh that retains most of the paint and details of your previous object.

After the operation, vertex colors will be moved in a new disabled layer, so they don't interfere with the textures.

#### From itself {#tex-from-itself}
Bake the object onto its own UVs: its painting becomes textures, and if it has multiresolution levels, the details of the highest level are baked onto the current one (a multires icon shows on the button then). This is simple to setup, but often you will require more control, in which case the next option is more useful.

#### From high-res {#tex-from-high-res}
Bake from the other objects to the selected object. The number in brackets indicate the number of other objects that will be used as high-res targets, and baked into the current low-res object with uv's. The other objects do not need to be similar in layout or topology to the object being baked, allowing for versatile bake workflows.

#### Resolution {#tex-bake-resolution}
The resolution of the baked texture. Bake textures are always square, so 1024 will create a 1024x1024 image. 

The buttons below are shortcuts for commonly used resolutions. For reference, 512x512 is relatively small, say for web graphics and simple geometry. 4096x4096 (4k for short) is for high quality renders.

#### Color, Roughness, Metalness, Normal, Displacement, Emissive, Opacity {#tex-normal-roughness-metalness-color-emissive-opacity}
These buttons determine which properties will be baked, each into separate maps. After the bake is complete, these will be added as textures to the material of the current object. `Displacement` bakes the height of the details as a displacement map.

#### ![](/icons/cog.webp) Bake gear menu {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
The gear menu has these advanced options:

##### Backup {#tex-backup}
To preview the baked textures, the object's paint information should be disabled. `Backup (Painting → Layer)` will transfer any paint information to a new layer as a backup so it can be easily enabled/disabled.

##### Use multires {#tex-use-multires}
For `From itself` on an object with multiresolution levels. Nomad reads the high resolution through the subdivision levels instead of casting rays: it's faster and free of projection errors. Turn it off to bake with the options below.

##### Smooth base {#tex-smooth-base}
For `Displacement` on an object with multiresolution levels. Measures the displacement from the subdivided base instead of its flat faces. Keep it on when the displacement map goes on a subdivided mesh, like Blender adaptive subdivision.

##### Search distance {#tex-cage-radius}
The maximum distance used to find the source surface. By default this distance is kept low to avoid artifacts, but can be increased if the target objects are far away from the bake object.

##### Projection {#tex-projection}
How the source surface is found:

* `Ray` - Project along the surface normal.
* `Ray + nearest` - Use the normal ray, then use the nearest surface if the ray misses.
* `Nearest` - Project to the closest point on the source surface.

##### Ray offset {#tex-ray-offset}
Adjust where the bake calculations start from on the bake object. A small offset from the surface avoids most common artifacts. If the target objects are very far away from the bake object, this offset might need to be increased. It isn't used by `Nearest`.


### ![](/icons/bake.webp) Reproject → Vertex {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Project sculpted details, painting, layers, textures into vertex values.

It can be thought of as the inverse of baking; if baking transfer vertex properties to textures, reproject transfers textures (and other properties)
 back into vertices.

::: tip
When using `Bake → Texture` or `Reproject → Vertex`, both the vertex colors and material textures will be taken into account.
:::

#### From itself {#vertex-from-itself}
Convert textures from the material into vertex values. This button will only be active if the object has UV's, and textures are active in the material.

::: tip TIP: Texture painting
Nomad doesn't directly support painting and editing textures, but very similar results can be achieved by projecting textures -> vertex values, painting on vertices, then bake vertex -> textures:

1. Setup a low poly object with UV's
1. Load textures into it's material
1. Subdivide it enough to paint on
1. `Reproject → Vertex` in `From itself` mode, now the texture has been converted to vertex values
1. Paint, smooth, smudge, stamp, do whatever edits you need
1. `Bake → Texture`, in `From itself` mode. Those edits are converted back into textures.
:::

#### From high-res {#vertex-from-high-res}
Convert the other objects into vertex values on the selected object. The number on this button indicates the number of source objects. This is mostly meant to be used on a high-resolution mesh as well, typically with a clean topology.

::: tip
Reprojecting other objects can be used not just for transferring color information from other objects, but to project vertices onto other objects, eg bandages can be projected onto a character.
:::

#### Vertices, Color, Roughness, Metalness, Opacity, Mask, Layers, Face Group {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
These buttons determine which properties will be projected to the selected object. `Layers` transfers the other layers onto the selected mesh.

#### ![](/icons/cog.webp) Reproject gear menu {#vertex-reproject-gear-menu}
The gear menu has these advanced options:

##### Opacity → Mask {#vertex-opacity-to-mask}
Turn the opacity of the source into mask on the selected object.

##### Iterations {#vertex-iterations}
How many times the relax operation should be applied during the reprojection. Only used when `Vertices` is on.

##### Relax {#vertex-relax}
The selected mesh can have its layout smoothed or relaxed a certain amount to better fit the reprojection targets. `Smooth` is better for high poly meshes, `Relax` is better for low poly meshes. `Auto` will let Nomad determine the best method.

##### Search distance {#vertex-cage-radius}
The maximum distance used to find the source surface. By default this distance is kept low to avoid artifacts, but can be increased if the target objects are far away from the selected object.

##### Projection {#vertex-projection}
How the source surface is found:

* `Ray` - Project along the surface normal.
* `Adaptive blend` - Blend the normal ray and nearest surface according to distance and `Ray preference`. If one misses, use the other.
* `Nearest` - Project to the closest point on the source surface.

##### Ray preference {#vertex-ray-bias}
Only for `Adaptive blend`. Higher values balance the blend toward the normal ray result, lower values toward the nearest point.

##### Ray offset {#ray-vertex-offset}
Adjust where the bake calculations start from on the selected object. A small offset from the surface avoids certain artifacts. If the target objects are very far away from the bake object, this offset might need to be increased. It isn't used by `Nearest`.

### ![](/icons/bake.webp) Bake → VDM {#bake-vdm}
Create a VDM (vector displacement) stamp from the selected object and add it to the VDM library. You'll be asked for a name.

Here is the typical workflow:
- Add a plane, or select `New VDM` in the VDM picker to add a configured one (the [VDM](scene.md#add-menu) primitive)
- Sculpt your shape on it, keeping the border flat
- Bake it!

The UVs of the plane define the square that is baked, so the object needs UVs. Pick the stamp size with `Resolution`, and choose with `Color`, `Roughness`, `Metalness` and `Opacity` what the stamp carries beside the displacement.

::: tip
Avoid DynTopo on the plane, it degrades its UVs and the stamp comes out distorted. Sculpting in a layer gives the most accurate result, since the flat plane is still there underneath. Painting also needs a layer, otherwise the material is stamped over the whole square instead of only where you painted.
:::

## ![](/icons/dot.webp) Primitive {#primitive}
Parameters for the selected primitive. Most of them are also available from the `…` button of the primitive viewport toolbar.

![](/images/topology_primitive_screenshot.webp)
