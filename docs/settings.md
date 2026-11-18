# ![](/icons/cog.webp) Settings {#reset-to-default}

The settings menu contains many options to control the appearance and behavior of Nomad.

![](/images/settings_overview.webp)

The row of buttons at the top of the menu jumps straight to a section: `Cursor`, `Indicator`, `Wire`, `Grid`, `Two-sided`, `Outline`, `Highlight`, `Navigator`, `Stats`, `Handles`, `Shape`, `Repeaters` and `Multires`.

## Display settings {#display-settings}
This section contains quick launch shortcuts for most of the settings further down this menu.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Smooth shading {#smooth-shading}
Toggle smooth and faceted shading. When faceted the polygons are shaded independently, so you can see the underlying topology.
It can be useful to see faceted shading during the sculpting stage, then change to smooth shading for rendering.

Disabling Smooth Shading improves performance a little bit.

### ![](/icons/outline.webp) Outline {#outline-quick}
Toggle an outline on your current selection.

This is useful to get visual feedback on your current selected mesh(es) in case [Darken Unselected](#darken-unselected-objects) is disabled.

From a performance point of view, using [Darken Unselected](#darken-unselected-objects) is much better than using the outline solution.

### ![](/icons/grid.webp) Grid {#grid-quick}
Toggle a background grid, useful for understanding object placement and scale.

### ![](/icons/culling.webp) Two-sided {#two-sided-quick}
Toggle two sided polygon display. All faces point in a certain direction.
Faces that are considered *backface* are the ones that point "away" from the camera viewpoint.

For example the startup simple sphere will have its faces point towards the outside.
If you move the camera inside the sphere you'll then see the backface of these faces.

Most of the time you shouldn't see the backface part of faces, so coloring them can help you detect potential issues or incorrect topology.

Disabling `Two-sided` rendering can improve rendering performance a bit.


### ![](/icons/wireframe.webp) Wireframe {#wireframe-quick}
Toggle a wireframe overlay. 

Note that enabling wireframe will lower performance.

### ![](/icons/navigator.webp) Navigator {#snap-cube-quick}
Toggle a helper icon in the corner of the scene, useful to orient yourself in space and quickly switch between front/back/left/right/top/bottom views.

### ![](/icons/palette.webp) Show paint {#show-painting}
Toggle paint display. When it's off, objects are shown with a white non-metallic material, at 25% roughness, instead of their painting.

### ![](/icons/tool_hide.webp) Use Hide {#use-hide}
Toggle the hide mode. When turned off it is still there, just deactivated. This button is disabled if you are currently using the hide tool.

### ![](/icons/shield.webp) Show mask {#show-mask}
Toggle the mask mode. When turned off it is still there, just deactivated. Press this button again to re-enable it.

If you need to hide the mask AND still have it be active, use the mask color below and set it to white. Remember to change it back to a gray when you're done!

Note that this button is disabled if you are currently using a mask tool. 

### ![](/icons/shield.webp) Mask → Opaque {#mask-opaque}
`Mask → Opaque` will ignore transparent vertices for masked mask. This is only relevant for vertex and texture opacity, face hidden by “hide” will still be hidden. It is only available while `Show mask` is on.

### ![](/icons/bang.webp) Highlight {#highlight-quick}
Toggle the selection highlight flash. When selecting objects, temporarily flash the selected object for 500 milliseconds. The color and length of the flash can be customised below.

### ![](/icons/list.webp) Stats {#stats-quick}
Toggle the status display text in the 3d viewport. This displays information about your system memory, total scene vertex count, and the current selection vertex count.

----- 

### ![](/icons/cube.webp) Darken unselected objects {#darken-unselected-objects}
The objects that are not selected will be darkened so that the current selection can stand out.

### ![](/icons/shield.webp) Mask {#mask}
The colour used for masking, by default a mid gray, multiplied against your object color. Set this to white to make the mask invisible, but remember to change it back to to a gray when done!

## ![](/icons/cursor.webp) Cursor {#cursor}

### Circle {#show-circle-while-sculpting}
When to show the brush radius circle:

* `Auto` - show the circle, but hide it while you sculpt.
* `No` - never show the circle.
* `Yes` - always show the circle, even while sculpting.

### Show small dot {#show-small-dot}
Display a dot at the center of the brush stroke while sculpting, or when the camera pivot is changed.

### Show rope stabilizer {#show-rope-stabilizer}
Draw a line to indicate the rope length when [Lazy rope stabilizer](stroke.md#lazy-rope-stabilizer) is active in stroke settings.

### Show roll hint {#show-roll-hint}
Show the roll direction guide while you use a roll key binding.

### ![](/icons/radius.webp) Size {#dot-size}
The size of the small dot.

### Colors {#cursor-colors}
The cursor changes color depending on what you are doing: `Sculpt`, `Background` (hovering the background), `Mask`, `Smooth`, `Camera` and `Radius`. Each color can be customized here.

## ![](/icons/cursor.webp) Indicator {#indicator}
![](/images/settings_indicator.webp)

Display visual indicator(s) for tutorials and screen captures. Set it to `Yes` to turn it on (on iOS there is also an `Auto` option).

The `Finger`, `Stylus` and `Mouse` buttons will enable displaying an icon when that type of input is detected.

### Color {#indicator-color}
The color of the indicator.

### Size/Icon/Circle {#indicator-shape}
Controls to adjust the size of the indicator, and the opacity of the icon and circle within the indicator.

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

### Snap {#snap}
These options make the points of curve and shape based tools (`Lathe`, `Tube`, polygon and path shapes...) snap while you draw them:

* `Snap to grid` - snap to the grid.
* `Snap to points (aligned view)` - snap to nearby existing points when the camera is aligned to an axis.
* `Snap to points (free view)` - snap to nearby existing points when the camera is not aligned.

### Color {#grid-color}
Set the grid color and opacity. These options show up when the grid is visible.

`Vignette` fades the grid out toward its edges. `Snap division threshold` sets, in pixels, how dense the grid lines can get on screen before the grid switches to another subdivision level.

## ![](/icons/culling.webp)Two-sided {#two-sided}
Enable seeing polygon faces from both sides.

### Backface color {#backface-color}
`Colored backface` enables tinting of the backfaces, and `Backface color` sets the tint color.

## ![](/icons/outline.webp)Outline {#outline}
Enable an outline around the selected objects.

### Outline color, Thickness {#outline-color-thickness}
Set the color and `Thickness` of the outline.


## ![](/icons/bang.webp) Highlight {#highlight}
Enable a short flash when the selection changes.
### Color, Duration {#color-duration}
Set the color and length of time of the flash in milliseconds.

## ![](/icons/navigator.webp) Navigator {#snap-cube}
![](/images/settings_snapcube.webp)

Display a helper icon in the corner of the scene, useful to quickly switch between front/back/left/right/top/bottom views. Tap on its sides to swap between orthographic views.

### Shape {#shape}
Choose between a sphere, a cube, or a gnomon shape for the navigator.

### Restrict alignment {#restrict-alignment}
Align the snapping views to the world axes. When enabled, only the 6 main views are possible. On `Auto`, this restriction only applies when the camera is in `Turntable` mode.

### Size {#size}
Set the size of the navigator.

### Flip 180° {#flip-180}
Enable a tap behavior so that if the view is snapped, tapping on the center of the navigator will rotate the view 180 degrees. For example if the view is snapped to the front, tapping the navigator will rotate to the back view.

### Edges & corners {#edges-corners}
Add snapping views on the edges and corners (the amber zones). Not available with the gnomon shape.

### Turntable drag {#turntable-drag}
Dragging the navigator rotates without rolling the camera, and holds on each snapping view. Disable it to drag the navigator with the `Trackball` rotation instead. Either way, the drag stays horizontal or vertical. With a `Turntable` camera, the navigator always drags this way.

### Position {#snap-position}
Set which corner the navigator will be in.


## ![](/icons/list.webp) Stats {#stats}
![](/images/settings_stats.webp)

Display information about your system memory, total scene vertex count, and the current selection vertex count.

### Position {#stats-position}
Set which corner the stats will be in.

## ![](/icons/edit_radius.webp) Handle {#handle}
Settings for the handles you drag in the viewport, such as the gizmo.

### Numerical input {#gizmo-input}
Allow numerical input when tapping one of the gizmo controls.

### Hide on interaction {#hide-on-interaction}
Fade the gizmo while you interact with it, so it doesn't get in the way.

### ![](/icons/opacity.webp) Opacity {#handle-opacity}
The opacity of the handles.

## ![](/icons/shape_lasso.webp) Shape {#shape-settings}
How the shapes you draw with shape strokes (lasso, rectangle, curve...) look on screen.

### ![](/icons/opacity.webp) Fill, Outline {#shape-fill-outline}
The opacity of the inside of the shape and of the line around it.

### Colors {#shape-colors}
The shape color for each kind of tool: `Mask`, `Hide`, `Face Group` and `Trim`.

## ![](/icons/array.webp) Repeaters {#primitive-repeaters}
Limits for the copies made by [repeaters](scene#repeaters) (array, radial, curve, surface). They keep Nomad responsive when a repeater gets out of hand.

### ![](/icons/cube.webp) Max copies {#repeater-max-copies}
The most copies a single repeater makes. Nomad struggles with many objects, whatever their size.

### ![](/icons/cube.webp) Scene copies {#repeater-scene-copies}
The copy budget for the whole scene. A low poly copy costs little geometry but stays a full object, so this is the limit small copies reach first.

### ![](/icons/triangle.webp) Max faces {#repeater-max-faces}
The face budget for all the copies in the scene. Past it, the heaviest objects lose copies first.

## ![](/icons/multires.webp) Multiresolution {#multires}
### Max vertex count {#multires-lowres-count}
Set a threshold to not allow a multires subdivide operation higher than this vertex count, which would likely crash Nomad: Nomad doesn't check the available memory before subdividing. The default is 10 million.
### Low resolution threshold {#multires-lowres-threshold}
A lower resolution of the mesh can be displayed when you move the camera. You can increase this value if you want to display a higher resolution of the mesh.

## Settings {#advanced}
### ![](/icons/reset.webp) Reset to default {#reset}
Reset all the app preference settings to their default values.

Some resources are saved separately and are NOT reset: projects, key bindings, tool presets, HDR environments, MatCaps, alphas, brush textures and reference images. Everything saved with the project, such as lighting, post process or camera views, is kept intact too.
