# ![](/icons/cog.webp) Settings {#reset-to-default}

The settings menu contains many options to control the appearance and behavior of Nomad.

![](/images/settings_overview.webp)

## Display settings {#display-settings}
This section contains quick launch shortcuts for most of the settings further down this menu.

![](/images/settings_display_settings.webp)

### Smooth Shading {#smooth-shading}
Toggle smooth and faceted shading. When faceted the polygons are shaded independently, so you can see the underlying topology.
It can be useful to see faceted shading during the sculpting stage, then change to smooth shading for rendering.

Disabling Smooth Shading improves performance a little bit.

### Outline {#outline-quick}
Toggle an outline on your current selection.

This is useful to get visual feedback on your current selected mesh(es) in case [Darken Unselected](#darken-unselected-objects) is disabled.

From a performance point of view, using [Darken Unselected](#darken-unselected-objects) is much better than using the outline solution.

### Grid {#grid-quick}
Toggle a background grid, useful for understanding object placement and scale.

### Two sided {#two-sided-quick}
Toggle two sided polygon display. All faces point in a certain direction.
Faces that are considered *backface* are the ones that point "away" from the camera viewpoint.

For example the startup simple sphere will have its faces point towards the outside.
If you move the camera inside the sphere you'll then see the backface of these faces.

Most of the time you shouldn't see the backface part of faces, so coloring them can help you detect potential issues or incorrect topology.

Disabling `two sided` rendering can improve rendering performance a bit.


### Wireframe {#wireframe-quick}
Toggle a wireframe overlay. 

Note that enabling wireframe will lower performance.

### Snap cube {#snap-cube-quick}
Toggle a helper icon in the corner of the scene, useful to orient yourself in space and quickly switch between front/back/left/right/top/bottom views.

### Show Painting {#show-painting}
Toggle paint display. The default paint used is a white non-metallic material, at 25% roughness.

### Use Hide {#use-hide}
Toggle the hide mode. When turned off it is still there, just deactivated. This button is disabled if you are currently using the hide tool.

### Show Mask {#show-mask}
Toggle the mask mode. When turned off it is still there, just deactivated. Press this button again to re-enable it.

If you need to hide the mask AND still have it be active, use the mask color below and set it to white. Remember to change it back to a gray when you're done!

Note that this button is disabled if you are currently using a mask tool. 

### Mask -> Opaque {#mask-opaque}
Mask -> opaque will ignore transparent vertices for masked mask. This is only relevant for vertex and texture opacity, face hidden by “hide” will still be hidden.

### Highlight {#highlight-quick}
Toggle the selection highlight flash. When selecting objects, temporarily flash the selected object hot pink for 500 miliseconds. The color and length of the flash can be customised below.

### Stats {#stats-quick}
Toggle the status display text in the 3d viewport. This displays information about your system memory, total scene vertex count, and the current selection vertex count.

----- 

### Darken Unselected objects {#darken-unselected-objects}
The objects that are not selected will be darkened so that the current selection can stand out.

### Mask {#mask}
The colour used for masking, by default a mid gray, multiplied against your object color. Set this to white to make the mask invisible, but remember to change it back to to a gray when done!

## ![](/icons/cursor.webp) Cursor {#cursor}

### Show circle while sculpting {#show-circle-while-sculpting}
Continue to show the brush radius when sculpting.

### Show small dot {#show-small-dot}
Display a dot at the center of the brush stroke while sculpting, or when the camera pivot is changed.

### Show rope stabilizer {#show-rope-stabilizer}
Draw a line to indicate the rope length when lazy rope stablizer is active in stroke settings.

## ![](/icons/cursor.webp) Indicator {#indicator}
![](/images/settings_indicator.webp)

Display visual indicator(s) for tutorials and screen captures.

The `Finger`, `Stylus` and `Mouse` buttons will enable displaying an icon when that type of input is detected.

### Color {#indicator-color}
The color of the indicator.

### Size/Icon/Circle {#indicator-shape}
Controls to adjust the size of the indicator and shapes within the indicator.

## ![](/icons/wireframe.webp) Wireframe {#wireframe}
![](/images/settings_wireframe.webp)
Activate the wireframe overlay.

### Target {#target}
Set if unselected objects will show wireframe, or only selected objects, or all objects.

### Hide {#hide}
Set if the wireframe will still be shown for hidden polygons.

### Multiresolution: Level 0 only {#multiresolution-level-0-only}
Multiresolution will show wireframes for level 0 darker, and higher levels progressively lighter. When enabled, this option will only show the level 0 wireframe.

### Color {#wireframe-color}
Set the color and opacity for wireframe.

## ![](/icons/grid.webp) Grid {#grid}
![](/images/settings_grid.webp)
Activate the grid.

### Color {#grid-color}
Set the grid color and opacity.

### Snap {#snap}
Enable snapping for curve based tools to the grid.

## ![](/icons/culling.webp)Two sided {#two-sided}
Enable seeing polygon faces from both sides.

### Backface Color {#backface-color}
Enable tinting of the backfaces, and the tint color.

## ![](/icons/outline.webp)Outline {#outline}
Enable an outline around the active object.

### Outline color, Thickness {#outline-color-thickness}
Set the color and thickness of the outline.


## ![](/icons/bang.webp) Highlight {#highlight}
Enable a short flash when the active object is changed.
### Color, Duration {#color-duration}
Set the color and length of time of the flash in milliseconds.

## ![](/icons/snap_cube.webp) Snap cube {#snap-cube}
![](/images/settings_snapcube.webp)

Display a helper icon in the corner of the scene, useful to quickly switch between front/back/left/right/top/bottom views. Tap on the sides of the cube to swap between orthographic views.

### Shape {#shape}
Choose between a cube, a sphere, or a gnomon shape for the snap cube.

### Restrict alignment {#restrict-alignment}
Enable camera rotation locking when dragging on the snap cube. When active, a drag motion on the snap cube will only go left/right or up/down.

### Size {#size}
Set the size of the snap cube.

### Flip 180 {#flip-180}
Enable a tap behavior so that if the view is snapped, tapping on the center of the cube will rotate the view 180 degrees. For example if the view is snapped to the front, tapping the view cube will rotate to the back view.

### Position {#snap-position}
Set which corner the snap cube will be in.


## ![](/icons/edit_radius_n.webp) Stats {#stats}
![](/images/settings_stats.webp)

Display information about your system memory, total scene vertex count, and the current selection vertex count.

### Position {#stats-position}
Set which corner the stats will be in.

## Primitive/Repeaters {#primitive-repeaters}
## Numerical input {#gizmo-input}
Allow numerical input when tapping the gizmo widgets.

## Multiresolution {#multires}
### Max vertices count {#multires-lowres-count}
Set a threshold to now allow a multires subdivide operation higher than this poly count, which would likely crash Nomad. The default is 10 million.
### Low resolution threshold {#multires-lowres-threshold}
A lower resolution of the mesh can be displayed when you move the camera. You can increase this value if you want to display a higher resolution of the mesh.

## Settings {#advanced}
### Reset to default {#reset}
Reset all the settings to their default values.