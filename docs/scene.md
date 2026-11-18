# ![](/icons/scene.webp) Scene {#scene}

This menu lets you manage objects, lights, cameras and repeaters in Nomad. It displays the scene hierarchy as a tree-view, allowing you to modify many aspects of your objects. It also lets you create new objects, as well as combine and split objects in various ways.


![](/images/scene_menu_summary.webp)


## Shortcut bar {#shortcut-bar}
| Action                 | Icon                              | Description                                                                                                         |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Add...](#add-menu)    | ![](/icons/plus.webp)            | Display the [Add Menu](#add-menu) to add an object to the scene                                                     |
| Delete                 | ![](/icons/trash.webp)           | Delete the selected objects. Their children are kept.                                                               |
| Lock                   | ![](/icons/lock.webp)            | Make the selected objects unselectable in the viewport. They can still be selected from the tree view. Locking a group locks everything under it. Tap again to unlock. |
| [Join](#join)          | ![](/icons/merge.webp)           | Join the selected objects into a single object with no geometry changes                                             |
| [Split...](#separate)  | ![](/icons/separate.webp)        | Display the [Split](#separate) popup, to break an object into several objects. The reverse of the join operation    |
| [Boolean...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Display the [Boolean](#boolean) popup                                                                          |
| Clone                  | ![](/icons/clone.webp)           | Duplicate the selected objects into new objects                                                                     |
| Instance               | ![](/icons/link.webp)            | Duplicate the selected objects as instances, so modelling changes to one are made to all instances.                 |
| Un-instance            | ![](/icons/unlink.webp)          | Convert an instance to a unique shape, so modelling changes are no longer copied to other instances                 |
| Sync                   | ![](/icons/checked.webp)         | When checked, operations apply to every instance of the selected objects, not only to the selected ones. It's only available when the selection contains instances. The [Sync tab](#sync) of the `Advanced` popup sets which operations follow this checkbox. |

::: tip
When an operation will also affect the other instances, a small link icon shows on its button.
:::


## Tree view {#tree-view}
![](/images/scene_treeview.webp) 

The tree view lists the objects, groups, repeaters, lights and cameras of the scene. Next to a mesh name you'll see its vertex count, with a colored layer icon when it has layers. Each row has these buttons:

| Action       | Icon                       | Description              |
| :----------: | :------------------------: | :----------------------: |
| Name         | ![](/icons/pencil.webp)   | Rename the object. If it's selected, all the selected objects are renamed at once, with a number added. Long press to rename it along with its children. |
| Select       | ![](/icons/checked.webp)  | Toggle select/unselected |
| Visible      | ![](/icons/eye_open.webp) | Toggle visibility        |
| Menu         | ![](/icons/more.webp)     | Display the [object menu](#object-menu) |

::: tip TIP: Quickly select or hide many objects

Tap the select icon to toggle a single object, or drag vertically on the select column to select many objects. The same can be done with the visible column.

Long press the select or visible icon to affect the children as well.

:::

### Tree view header {#tree-view-header}

The row above the list has a few helpers:

* ![](/icons/sort_down.webp) - collapse or expand all the groups at once.
* ![](/icons/preview.webp) - toggle the `Object previews`, a small rendered thumbnail for each object of the list.
* ![](/icons/search.webp) - filter the list by name.

### Tree view manipulation {#tree-view-manipulation}

Long press on an item in the tree view until it's highlighted. You can then move it up or down in the tree view, as well as drag it over another item to make it a child of that item.

When many items are selected, one of them is the main selection and is drawn brighter. Long press and drag one of them to move all the selected objects at once.

When you select a parent item, by default all the child items will also be selected. Tapping the parent again will toggle between selecting just the parent, or the parent and children.

Double tap an item to focus the camera on it (see [Advanced](#focus-on-item)).

### Object menu {#object-menu}

Clicking the ellipsis button (...) for an object in the tree view will show the object menu. 
Many of these options are similar to the shortcut bar at the top, repeated for convenience.

|       Action        |                        Icon                        | Description                                                                                                                                                             |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Name         |              ![](/icons/pencil.webp)           | Change the name of the object                                                                                                                                           |
|     Un-instance     |              ![](/icons/unlink.webp)           | Convert an instance to a unique shape, so modelling changes are no longer copied to other instances.                                                                    |
|      Instance       |               ![](/icons/link.webp)            | Duplicate the object as an instance, so modelling changes to one are made to all instances.                                                                             |
|        Clone        |              ![](/icons/clone.webp)            | Duplicate the object into a new object                                                                                                                                  |
|       Delete        |              ![](/icons/trash.webp)            | Delete the object. Its children are kept, unless `Children` is checked.                                                                                                 |
|      Children       |            ![](/icons/hierarchy.webp)          | When checked, `Instance`, `Clone` and `Delete` also act on the object's children.                                                                                      |
|   Split by Parts    |             ![](/icons/separate.webp)          | If an object is made up of disconnected parts, create a separate object for each of them. The reverse of the join operation.                                           |
|   Split by Groups   |            ![](/icons/group.webp)          | If an object has multiple face groups, create a separate object for each face group.                                                                                       |
|   Split by Layers   |              ![](/icons/layer.webp)            | If an object has layers, create separate objects for the base mesh and each layer. Useful for sending blendshapes to other applications.                               |
|   Join → Layers     | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | If multiple objects are selected and have matching topology, merge those objects into layers for the primary object (the other objects will be deleted). Again, useful for blendshapes coming FROM other applications.<br><br> Note that the layers will be disabled by default. Enable them if you need to adjust their sliders. |
|  Curve (Repeater)   |              ![](/icons/curve.webp)            | Only for a tube or a lathe: add a [Curve](#curve) repeater that follows the same curve, as a child of the object.                                                      |
|        Tube         |             ![](/icons/tube.webp)              | For a lathe, add a [tube](tools.md#tube) that follows its profile, as a child. For a cylinder, a cone or a torus, convert it into a tube of the same shape, so you can bend it along a curve. |




### Multiselection {#multiselection}
You can select multiple objects to help achieve two things:
- using the gizmo tool to move several objects at once
- merge objects using join and boolean operations.

In the tree view, tap the select icon of each object, or drag along the select column. When tapping names, hold the `Mask` shortcut (or `Ctrl` on a keyboard) to add or remove a single object, or hold the `Smooth` shortcut (or `Shift`) to select every object between the current one and the one you tap.

::: tip Quick multiselection
You can also multiselect in the viewport by holding the `Smooth` shortcut (or `Shift`) and tapping on another mesh.

You can deselect an object by tapping on it again (only if your selection has more than one object).
:::

The gizmo moves all the selected objects together, see [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Join {#join}
This option will simply make one single object entry from multiple selected objects.
Points and UVs closer than the [weld radius](#weld-radius) are merged.

You can see an example in video in the [Split](#separate) section.

## ![](/icons/bool_subtract_circle.webp) Boolean {#boolean}
![](/images/scene_boolean_menu.webp) 
Combine objects into a single surface.

`Voxel merge` will retain the volume of the objects, and calculate new evenly spaced polygons on the surface. Because of the calculation step a voxel merge can handle complex geometry, but can lose fine detail if the target resolution isn't high enough.

`Boolean` will attempt to leave the polygons in their original layout, and stitch the polygons where objects overlap. This can make much cleaner and sharper results than a voxel merge, however it requires 'watertight' meshes; there cannot be holes or malformed shapes in the objects. If this fails, usually a voxel merge will work.

### Boolean operations {#boolean-operations}
Both Voxel merge and Boolean will use object visibility to control the operation, as the reminders at the bottom of the popup say:

#### Union {#union}
Both objects visible will create a boolean **union**, the outer skin of the objects are combined, with no interior surfaces. ![](/images/boolean_union.webp)

#### Subtract {#subtract}
One object invisible = boolean **subtract**, the invisible object will be subtracted from the visible object. ![](/images/boolean_subtract.webp)

#### Intersect {#intersect}
Both objects invisible = boolean **intersection**, create a new shape only where the two objects overlap. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Voxel merge {#voxel-merge-button}
Pressing this button will do a voxel merge operation on the selected objects. When done on a single object it will retopologize into evenly spaced polygons, useful for when an object has stretched polygons. The options below work like the [Voxel Remesher](topology.md#voxel-remesher) ones.

### Resolution {#resolution}
The resolution of the voxel 3d grid used to do the calculation. When this value is changed, a checkerboard pattern is overlayed on the object to preview the size of the polygons.

The picker next to the slider takes the detail from the mesh density under your finger. The button beside it switches the slider to `Edge length`, a size in the world: the same value gives the same detail on any object.

### Build multiresolution {#build-multiresolution}
Create multiresolution levels below your target resolution. So if your resolution is 400 and build multiresolution is 3, you will get a new mesh with say 296,000 polygons, but there will be 3 subdiv levels lower at about 74,000, 18,500 and 4,600.

### Thicken thin parts {#thicken-thin-parts}
Thickens the parts that are too thin for the voxel grid, so they don't break apart. It's not available with `Sharp edges` or `Sharp border`.

### Holes {#holes}
How holes in open objects are closed before the merge:
* `Fill` - each hole is closed on its own, from its border.
* `Shape` - holes are closed by following the surrounding surface, and open pieces that overlap are joined.

### ![](/icons/angle.webp) Keep sharp edges {#keep-sharp-edges}
The `Sharp edges` button snaps the voxel mesh to the sharp edges of the objects. This works best on simple shapes, and it can introduce distortion in some areas.

### ![](/icons/group.webp) Sharp border {#sharp-border}
The new faces follow the face group borders, and a border stays sharp where the surface creases along it.

### ![](/icons/group_separate.webp) Keep groups separate {#keep-groups-separate}
Each face group is remeshed on its own: groups never merge, and each one stays a closed piece in its own group. Multiresolution is not built in this mode.

### ![](/icons/bool_subtract_circle.webp) Boolean button {#boolean-button}
Pressing this button will do a polygon boolean operation using the Manifold library by Emmett Lalish. 

### ![](/icons/bool_unite_circle.webp) Clean Overlaps {#clean-overlaps}
When only one object is selected, the `Boolean` button becomes `Clean Overlaps`: it merges the parts of the object that cross each other into a clean surface.


## ![](/icons/separate.webp) Split {#separate}
If you have a single object based on several disconnected parts, you can split this object into several objects. 
This can be seen as the opposite of [Join](#join).

The `Split...` popup has three ways to split the selected objects:
* `Split by Parts` - create a separate object for each disconnected part.
* `Split by Groups` - create a separate object for each face group.
* `Split by Layers` - create separate objects for the base mesh and each layer.

![](/videos/merge_separate.mp4)


## ![](/icons/plus.webp) Add menu {#add-menu}

![](/images/scene_addmenu_overview.webp)

This menu will create primitives, groups, cameras, repeaters, and lights.

Primitives are basic shape types that can be adjusted using parameters. Once you have the primitive adjusted to your needs, you then 'validate' it, which bakes those parameters down into a polygon mesh that can be sculpted and painted. A primitive cannot have its parameters adjusted after it has been validated.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) On gizmo {#on-gizmo}
Enable putting the new primitive where the current selected shape or gizmo is. When disabled, the primitive will be placed at the center of the scene.

### ![](/icons/gizmo.webp) Select gizmo {#select-gizmo}
Enable automatically switching to the gizmo tool when a new primitive is created. 

### ![](/icons/cog.webp) Advanced {#add-advanced}

This menu allows you to set your preference for where new primitives, groups, repeaters will be created. They can be on the selected object, at the world origin, or at the location of the gizmo.


### UV's {#uvs}
The `UVs` toggle next to the Primitive title enables UV's on primitives. UV's (often called texture coordinates), are extra data used in 3d to allow textures to be applied to surfaces. They take up more memory, but for most devices this shouldn't be a concern unless you're getting into very high poly counts (eg 10 million polys or more). 

### Primitives {#primitives}

| Primitive      | Icon                                      | Description                                                                                                     |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Box            | ![](/icons/cube.webp)                    | It's a simple cube, you can control the division in X, Y and Z                                                  |
| Quad Sphere    | ![](/icons/circle.webp)                  | A subdivided box, with the `Project on sphere` forced, so it has an even quad layout that is good for sculpting |
| Cylinder       | ![](/icons/cylinder.webp)                | You can add a center hole for the cylinder primitive, for example to make an hollow pipe                        |
| Torus          | ![](/icons/torus.webp)                   | The torus can be a good starting point for rings                                                                |
| Cone           | ![](/icons/cone.webp)                    | -                                                                                                               |
| Icosahedron    | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| UV Sphere      | ![](/icons/circle.webp)                  | A sphere with uneven poly layout, see [Warning below](#uv-sphere)                                               |
| Plane          | ![](/icons/rectangle.webp)               | It's a simple plane, note that this is the only primitive that is not closed                                    |
| Text           | ![](/icons/text.webp)                    | 3d text, with a font, a style, an alignment, a depth and a bend. `Merge letters` fuses letters that touch       |
| Tube           | ![](/icons/tube.webp)                    | see [Tube](tools#tube)                                                                                          |
| Lathe          | ![](/icons/lathe.webp)                   | see [Lathe](tools#lathe)                                                                                        |
| Triplanar      | ![](/icons/triplanar.webp)               | see [Triplanar](#triplanar)                                                                                     |
| VDM            | ![](/icons/vdm.webp)                     | A plane set up to sculpt a vector displacement stamp: it includes UVs and faces the camera                      |
| Shadow Catcher | ![](/icons/material_shadow_catcher.webp) | see [Shadow Catcher](#shadow-catcher)                                                                           |
| Head           | ![](/icons/face.webp)                    | A simple head with a layer to blend between male/female                                                         |

::: tip
If you wonder what is the base mesh when you launch Nomad: this is a subdivided box as well.
However the base mesh in Nomad doesn't use `Project on sphere`, meaning it is not perfectly round.
:::

### Primitive Toolbar {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

Once a primitive is created, a toolbar will appear to control it's parameters.

* `Validate` Bake the primitive into a standard object so it can be sculpted and painted.
* `Mirror` Toggle placing a mirror repeater above the primitive.
* `All` (eye icon) Choose which handles are shown directly on the primitive to control its parameters, eg the cube width, or a cylinder hole radius: `None`, `All`, or only one kind (radius, hole, profile...) depending on the primitive.
* `Division` The number of divisions of the primitive, here along X for a box.
* `Constant density` When you stretch the primitive along one axis with the gizmo, its size and divisions grow instead of the polygons stretching, so the faces stay square. Available on boxes, planes and cylinders.
* `...` Displays the primitive menu.

Different primitives will have extra options on the toolbar:

* `Sphere` The sphere is constructed as a subdivided cube, as this is better for sculpting, but this means it is not perfectly round. This option will force the shape closer to a perfect sphere. The icosahedron shares this option.
* `Cap` Toggle end caps on a shape, eg a cylinder can have caps on top, or bottom, or both, or none.
* `Hole` Toggle a hole to be created through the center of a shape. This will cycle through no holes, hole with a single radius, or hole with different radius at top and bottom.
* `Radius` Toggle if a cylinder should have a single radius, or a different radius at its top and bottom.
* `Disk` Toggle if a plane should be a 4 sided shape, or a circle shape.

The small toolbar below the main toolbar will let you toggle between the primitive gizmo and the transform gizmo.

::: tip

Clicking on the title of the toolbar will toggle it to the top or bottom of the display. Clicking on the arrow in the corner will collapse it.

:::


### Primitive menu {#primitive-menu}

![](/images/scene_primitive_menu.webp)

This contains all the parameters for the selected primitive. Parameters are the basic descriptions for a shape. To describe a ring, for example, you would describe it's outer, radius, its inner radius, and the number of polygons.

Most primitive parameters should be self-explanatory, and there are some common parameters shared across all primitives:

* `UVs` The small UVs button at the top of the menu will toggle the creation of UV coordinates
* `Validate` The small validate button will bake the primitive into a standard object so it can be sculpted and painted.
* `Max faces` Set an upper limit on the amount of polygons in the object to avoid crashing your device.
* `Post subdivision` Enable the chosen number of subdivisions from the multiresolution section of the topology menu. This can be used to make smoothed, soft cornered primitives in combination with low topology divisions. For example, setting a box topology divisions to 2, and post subdivisions to 4, will make a box with smooth corners.
* `Linear subdivision` Set how many levels of linear subdivision to use before using regular smooth subdivision. This can be used to control how sharp or soft the corners are on the subdivided surfaces. Eg, set a box topology divisions to 2, post subdivisions to 4, then try changing the linear subdivisions between 0 and 4. The corners of the box will go from soft to sharp.

### Topology {#topology}

This controls the number of polygons in a primitive. Usually the controls are linked, so changing the one active slider will adjust all the polygons evenly. You can tap the unlink button, and control the X/Y/Z divisions on a shape separately.

### Geometry {#geometry}

This controls the overall size of a primitive, in X/Y/Z units for square shapes, and in radius for round shapes.


### ![](/icons/circle.webp) UV Sphere {#uv-sphere}
::: warning
The UV Sphere is not well suited for sculpting, especially on the poles.

Please prefer the Quad Sphere, Box or Icosahedron [primitive](#primitives), along with the `Project on sphere` option.

Note that the topology can be acceptable for sculpting if you use a very low value for the `Division` sliders.
You can then use the `Overall Subdivision` slider to raise the number of polygons.

While not suitable for general sculpting, it is useful for eyes; if you rotate the sphere so that the poles sit at the pupil, the polygon layout will naturally fit to paint and sculpt the iris and pupil.
:::


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
This primitive is special in that you should use the [Masking tool](tools.md#mask) on it to shape the geometry.

![](/videos/triplanar.mp4)


::: tip
Double-tap on a plane and the camera will focus on this particular plane.
This won't work if you rotate the primitive with the gizmo though.
:::

Triplanar is using the mask information from 3 planes to fill a voxel grid that is then polygonized (thanks to the [Voxel Remesher](topology.md#voxel-remesher)).

Each plane has its own symmetry plane.

::: warning
Each time you update the size of the Triplanar primitive, the quality of the mask painting will degrade.

For now there is no option to 'lock' the painting on a single plane, but maybe it will come in the future.
You can use the [Connected Topology](stroke.md#connected-topology) to help a little bit, in that if your cursor lies precisely on one plane it won't impact the other planes.
:::

### ![](/icons/material_shadow_catcher.webp) Shadow Catcher {#shadow-catcher}
Add a plane with the shadow catcher material. See [Shadow Catcher material](material.md#shadow-catcher) for more details. 


## Group/Camera {#groupcamera}
### ![](/icons/share.webp) Group {#group}
Create an 'empty' object, that you can parent other objects underneath. This can be used to simply organise the hierarchy by putting many objects under a group, then closing it. A group can also be used as a helper for moving objects; many objects can be placed under a group, and then the group moved, rotated, scaled with the gizmo tool.

### ![](/icons/camera.webp) Camera {#add-view}
Create a camera.

## Repeaters {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Repeaters are nodes that make instances of objects below it. 

### ![](/icons/array.webp) Array {#array}
![](/images/scene_primitive_array.webp)

When objects are made children of this node, they can be instanced into a grid layout. When selected, it has controls for:
* `Fit inside` - when on, all the copies are placed inside the array's bounds; when off, the sliders set the space between copies
* `Count X/Y/Z` - the number of instances on each axis
* `Size X/Y/Z` - the size of the grid along each axis, or the distance between copies when `Fit inside` is off
* `Randomize...` - adds random variations to the copies, see [Randomize](#curve) below.

### ![](/icons/curve.webp) Curve {#curve}
![](/images/scene_primitive_curve.webp)
This will create a curve, children of this node will be repeated along the curve. When selected, it has controls for:
* `Curve` - edit the curve: add points to the curve, and move points on the curve.
* `Show` - show or hide the curve and its points.
* `Snap` - snap curve points to other geometry.
* `Sym` - edit the curve symmetrically.
* `Closed` - toggle the curve to join the start and end, or to be an open curve.
* `B-spline` - toggle the instances to follow the curve exactly, or use b-spline interpolation which has smoother results.
* `Warp` - bend each copy along the curve, so the copies meet their neighbors (`Smooth` bends their sides so they meet without an angle).
* `Align` - rotate the copies to follow the direction of the curve.
* `Pivot` - the pivot of the copies: the curve itself (`Self`) or its children.
* `Count` - the number of instances. The mode button next to it switches to `Distance`: a fixed spacing between the copies, the count follows the curve length.
* `Radius` - controls on each curve point to set the scale of the instances.
* `Rotate` - controls on each curve point to set the twist rotation of the instances.
* `Alternate` - turn every other copy around the curve: 90° for chain links, 180° for leaves or zipper teeth, around the `Axis` you choose.
* `Spiral...` - wind the copies around the curve, in several strands (rope, braid, ribbon...).
* `Randomize...` - add random variations to the copies; each row can instead add the same amount at each copy.

Below the toolbar, the `(merge)` toggle merges a point into another when you drag it onto it. `IK` (inverse kinematics) lets you pose the curve: drag a point and the connected points follow. Tap a point to lock or unlock it, long press to lock or unlock all of them; locked points stay in place.

### ![](/icons/radial.webp) Radial {#radial}
![](/images/scene_primitive_radial.webp)

Children of this node will be instanced into a circle. Move the child object to alter the radius of this repeater. When selected, it has controls for:
* RadialX/Y/Z - selecting these buttons will set the radial axis, and set the number of instances.



### ![](/icons/mirror.webp) Mirror {#mirror}
![](/images/scene_primitive_mirror.webp)

Children of this node will be mirrored across an axis. When selected it has controls for:
* Gizmo - enable the transform gizmo to set the center of the mirror. This can also be rotated and scaled. When done, tap gizmo again to reveal the standard controls.
* X/Y/Z - set the mirror plane

### ![](/icons/surface.webp) Surface {#surface}

Children of this node are copied onto the surface of an object: one copy per face, per edge or per vertex, or scattered at random. When selected, it has controls for:
* Mode - place the copies on the `Faces`, the `Edges` or the vertices, or `Scatter` them.
* Every - one copy every N faces, edges or vertices. `Random` picks them at random instead, and `Shuffle` draws another random set.
* Spacing - when scattering, the minimum distance between two copies.
* Align - the copies stand on the surface, following its normal, instead of keeping the orientation of the original.
* Snap - project the original onto the nearest surface point, the copies follow.
* Fit size, Skew - scale and stretch the copies to the shape of each face.
* Warp - bend each copy onto its face, or along its edge, so neighboring copies meet without gaps.

All the repeaters have a `Validate` control, which will bake the results of the repeater, and will ask how to perform the bake:
* Join children - the instances are joined into a single object
* Keep instances - the instances remain as instances, but no longer have the repeater 'parent'
* Un-instance - the instances are converted into unique objects

`Flatten all` also bakes the repeaters nested inside this one, so every copy becomes a plain object.

::: tip Tip: Combine repeaters
Repeaters can be parented under each other, and several objects can be made children of repeaters, leading to complex effects.

![](/images/scene_repeater_combine.webp)
:::

::: tip Tip: Repeater pivots

Some repeaters will try to auto-pivot the child objects, so even if you move or rotate them with the gizmo tool, they won't move. If you need to override this behavior, insert a group in between the repeater and the child. Now you can move the child shape independently of the repeater.
:::

## Light {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Directional {#directional}
Create a directional light, an infinitely far away light source like the sun.

### ![](/icons/panorama.webp) Environment {#environment}
Create an environment light, which lights the scene from an image all around it (image-based lighting, like an HDRI).

### ![](/icons/spotlight.webp) Spot {#spot}
Create a spot light, with controls over the cone width, softness

### ![](/icons/light.webp) Point {#point}
Create a point light

## ![](/icons/cog.webp) Advanced {#advanced}
The `Advanced` button at the bottom left of the panel opens a popup with two tabs: `General` and `Sync`.

### ![](/icons/focus.webp) UI: Focus on item on double tap {#focus-on-item}
Double tapping an item in the Scene list will center the camera on that item in the 3d view.

### ![](/icons/eye_open.webp) Sync visibility {#sync-visibility}
When enabled, using the eye icon of a selected item will impact all the selected items. 

### ![](/icons/bang.webp) Highlight {#highlight}
Highlights the selected objects in the viewport when the selection changes.

### ![](/icons/link.webp) Show (Instance) {#instance-show}
Display a colour capsule on the left of the scene list to show instances.

### ![](/icons/preview.webp) Object previews {#object-previews}
Show a rendered thumbnail for each object in the scene list. It's the same as the preview button above the list.

### Weld radius {#weld-radius}
Under the `Join` title, `Position Weld Radius` and `UV Weld Radius`: points and UVs closer than these radiuses are merged. Each can be turned off with its checkbox. This applies to Join, Boolean, Trim, Decimate, remeshing and file import.

### Icons {#icons}
Set the min and max `Size` and the `Opacity` of the group, light, camera and repeater icons in the viewport.

### ![](/icons/hierarchy.webp) Hierarchy lines {#hierarchy-lines}
Display a line between parent and its children in the viewport. When enabled, you can also set:
* `Use Nomad pivot` - the lines start from the pivot used by the Transform and Gizmo tools. When disabled, they use the natural base pivot, which can be far from the object's center.
* `Thickness` - the width of the lines. The button next to the slider adds a contour to them.
* The color of the lines.

### ![](/icons/link.webp) Sync {#sync}
The `Sync` tab sets, for each operation (`Add`, `Delete`, `Lock`, `Clone`, `Instance`, `Un-instance`, `Join`, `Split` and `Boolean`), whether it applies to every instance of the selection:
* `Auto` - follow the `Sync` checkbox at the top of the scene menu.
* `No` - only the selected objects.
* `Yes` - always every instance.

By default `Join`, `Split` and `Boolean` are on `Yes` and the others on `Auto`. `Reset` brings back these defaults.

## Bottom toolbar {#bottom-toolbar}
These icons will toggle visibility of Group, Light, Camera, Repeater and Hierarchy lines in the viewport. Icons displayed on the canvas can be tapped to select and edit them directly.