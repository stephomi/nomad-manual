# ![](/icons/brush.webp) Stroke {#stroke}

---
![](/images/stroke_overview.webp) 

## Overview {#overview}

You can customize the stroke behavior of most tool brushes.
The settings should be similar to the ones present in 2d painting applications, however some options are specific to sculpting and 3d.

The options are split across 5 sub-menus:

| Name     | Icon                         | Description                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/brush.webp)      | Control how the stroke gets applied to the model                   |
| Alpha    | ![](/icons/alpha.webp)      | How a grey-scale texture is used for the brush stamp               |
| Falloff  | ![](/icons/falloff.webp)    | Control how the brush strength changes from the center to the edge |
| Filter   | ![](/icons/filter.webp)     | How the brush is affected by the model geometry                    |
| Pressure | ![](/icons/pressure.webp)   | Control stylus pressure response                                   |

::: tip
Not all stroke options apply for all tools. Stroke options that aren't used by the current tool will be disabled or hidden. 
:::


## ![](/icons/brush.webp) Stroke {#stroke-1}

### ![](/icons/radius.webp) Radius {#radius}

![](/images/stroke_radius.webp)

The radius options are global settings: they apply to every tool.

#### Space {#size}

* `Screen` - the radius is set in screen units. If you make the radius 100 pixels wide, it will stay 100 pixels wide regardless if you zoom in or out.
* `World (3d)` - the radius is set in 3d units. For example if you create a sphere and make the radius the same size as the sphere, the radius stays the same size as the sphere as you zoom in and out.

#### ![](/icons/link.webp) Sync shortcut {#sync-shortcut}

When enabled, the radius and silhouette settings are kept in sync when you switch to the shortcut brushes (`Smooth`, `Mask` or `Hide`). This way, a quick smooth or mask pass uses the same brush size as the tool you were using.

#### ![](/icons/link.webp) Share radius {#share-radius}

When enabled, all tools will use the same radius, the default is for each tool to have its own radius.


### Stroke type {#stroke-type}

![](/images/stroke_strokemode.webp)

Strokes can act in multiple modes:

### ![](/icons/stroke_dot.webp) Dot {#dot}
Drag like a regular paint stroke. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Roll {#roll}
The brush alpha is rolled out along the stroke, like a patterned paint roller: it repeats end to end and follows the direction of the stroke. Useful for making fabric stitches. 
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Lock + radius {#lock-radius}
Stamp a brush stroke with fixed **_height_**. Drag will set the scale and rotation.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Lock + intensity {#lock-intensity}
Stamp a brush stroke with fixed **_radius_**. Drag will set height and rotation.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
The `Lock + radius` and `Lock + intensity` modes ignore the [Pressure](#pressure) settings, since the drag already sets the size and strength.
:::

![](/images/stroke_strokemodemove.webp)

The `Move` and `Drag` tools have their own 3 options. With all of them, the intensity sets how far the surface follows your pointer: at 100% it stays under it, at 50% (the default for `Move`) it goes half as far.

### ![](/icons/snake.webp) Drag {#drag}

Will keep updating what is inside the brush radius during the stroke. A fast stroke will leave the surface behind, while a slow stroke will hold onto material, making longer shapes. This is the default mode for the `Drag` tool. With `Dynamic Topology` this can be used to make snake like extrusions (with the `Move` tool, raise the intensity to 100% for this). 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Grab {#grab}
Will select what is inside the brush radius when the brush is started, and keep that selection. This is useful for more precise move operations, as you can carefully adjust the distance of the move and not accidentally move more than you originally selected. This is the default mode for the `Move` tool.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Lock + radius (drag) {#lock-radius-drag}
The user radius is ignored, and is set dynamically based on how far the stroke is dragged away from the starting point. A small distance=small radius, a larger distance = bigger radius. Useful for blocking in organic rubbery shapes.
![](/videos/stroke_lockradius_drag.mp4) 

Some other tools list their own stroke types here, for example `Relax`, `Smooth` and `Smudge` for the smoothing tools, or shapes such as `Lasso` and `Curve` for the selection-based tools. They are described with each [tool](tools.md).


### Adjust spacing intensity {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Strokes with a low spacing (lower than 50%) can accumulate quickly, making more intense strokes than higher spacing values. This toggle will compensate for this, so strokes will be of approximately the same intensity regardless of spacing.

### Stroke spacing {#stroke-spacing}
How far apart to apply each brush stroke during a drag operation. Values lower than 100% will overlap, giving the appearance of a continuous stroke. Values greater than 100% will start to leave gaps, useful for sculpting detail like stitching or zippers.

### Lazy rope stabilizer {#lazy-rope-stabilizer}
Strokes will lag behind the pointer position by a certain distance. This can be used to draw smooth lines.
![](/videos/stroke_lazy_rope.mp4) 

### Stroke smoothing {#stroke-smoothing}
Average multiple pointer positions to get a smoother stroke.
With high values, the stroke will lag behind the pointer but will eventually catch up.
This is useful for drawing smooth lines.

### Snap radius {#snap-radius}
Snap the stroke to the previous one when the pointer starts close to where the last stroke ended. The radius determines how far to look for the end of the previous stroke. This can be useful when drawing long continuous lines, while doing frequent pauses.

### ![](/icons/trail.webp) Trail {#trail}

When enabled, each new stamp also reapplies the most recent points of the stroke behind it. `Trail count` sets how many points are reapplied, `Trail intensity` how strong they are, and `Trail radius` how much bigger they get.

Trail only works with the `Dot` stroke type, and not with the `Ridge` [falloff influence](#influence).

### ![](/icons/silhouette.webp) Silhouette {#silhouette}
![](/images/stroke_silhouette.webp)
By default strokes will only affect the model surface within the brush radius. When silhouette is enabled, the stroke will be projected through the entire model. This can be very useful when doing the initial blocking out of a model, or for shapes that require the sides to remain perpendicular.

The projection direction can be set explicitly:

* `X`, `Y`, `Z` - project along a fixed axis.
* `View` - project along the camera direction.
* `If snapped` - project along the camera direction, but only while the camera is snapped to a view. Otherwise the stroke stays a regular one.
* `Closest` - project along the axis closest to the camera direction. This is the default.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Randomize {#randomize}

![](/images/stroke_randomize.webp)

The `Intensity`, `Offset`, `Rotation` and `Scale` of the stroke can each be randomized. Use the checkbox of a row to turn it on or off. This can be used to create a range of effects, eg randomize with the paint tool can create mottled color, or randomize with the crease tool can be used to create skin detail.

`Period (slower)` sets the length of the random cycle: increase it for slow, rolling variations, decrease it for rapid noise. The small button next to each row scales the period for that row only.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Randomize - HSV {#randomize-hsv}

For tools that paint, the `Hue`, `Saturation` and `Value` of the paint color can be randomized too, with their own period. Great for adding subtle color variation to skin or stone.

### Stroke offset {#stroke-offset}

Apply a constant offset on the stroke, so that your finger doesn't cover it. This is useful on small screens. It is a global setting: enable it with its checkbox, and it applies to every tool.


## ![](/icons/alpha.webp) Alpha {#alpha}
![](/images/stroke_alpha.webp) 

The `Alpha` is a texture that will modulate your brush behavior.
It's a grayscale image, where black pixels mean no deformation and white pixels full deformation.

Click on the alpha image to change it. Besides the built in alphas and your own imports, the alpha list can also download displacement maps from Poly Haven.

Click on the material preview to load an alpha from a material preset. You can also save material presets here, and choose to embed textures with the tool.

::: tip
The texture is never resized, so large textures can slow down performance.
:::

### ![](/icons/blend_contrast.webp) Fix alpha {#invert-pixels}
The `Fix...` button on an imported alpha opens a popup that corrects the image itself: its mid value, inverting the pixels (black becomes white and white becomes black), a 90° rotation, and a horizontal or vertical flip. The image file is rewritten, so other apps see the corrected image too.

::: tip

The built in alphas that ship with Nomad cannot be fixed.

:::

### Projection {#projection}

How the alpha is projected onto the model:

* `Surface` - the alpha lies on the surface under the brush, following its orientation.
* `Screen` - the alpha is projected straight from the view.
* `Tile` - the alpha is projected from the view and stays in place while you paint over it, like a stencil, so a repeating pattern joins up seamlessly. The rotation is locked, and pen pressure doesn't change the pattern size.
* `Triplanar` - the alpha is projected along the 3 axes. The scaling, rotation and tiling options below are replaced by the triplanar texture settings.

### ![](/icons/diagonal.webp) Scaling {#scaling}

The brush size in Nomad is a circle with a user defined radius. Textures are often square or rectangular, the `Scaling` parameters let you decide how the texture should fit within the circle. For a square texture, a value of 0.7 will fit within the circle. A value of 1 will scale the texture larger so that the circle fits inside, clipping the edges.

![](/images/alpha_scaling.webp) 

Enabling `Scaling Y` will allow you to stretch the alpha vertically. The first slider then becomes `Scaling X`.

![](/images/alpha_scaling_y.webp) 

`Flip horizontally` mirrors the alpha left to right.

### Rotation {#rotation}

The alpha texture will be rotated to follow the direction of the stroke. You can add a rotation offset, and if the lock icon is enabled, the texture will stay locked to this rotation relative to the screen.

The pen button next to it rotates the alpha when you roll your stylus (barrel roll), with the `Lock + radius` and `Lock + intensity` strokes while the rotation is unlocked. It only works with stylus hardware that supports it.

### Tiling {#tiling}
![](/images/stroke_tiling.webp) 

How often the texture repeats within the brush profile. The `Tiling - X` and `Tiling - Y` modes allow you to limit to a single texture within the stroke (`None`), or repeated textures (`Repeat`), or mirrored where every second texture is flipped to create patterns or help make seamless textures (`Mirror`). They are available with the `Roll` stroke, the `Tile` projection, or a `Tiling` above 1.

`Tight fit (non-square images)` only matters for non-square alpha and brush textures. When enabled, each image tiles on its own with no spacing. Disable it to keep the alpha and the other images in sync when their aspect ratios differ.

![](/videos/alpha_tiling.mp4) 



### Mid value {#mid-value}

By default black pixels will mean no deformation, and white pixels will mean full positive deformation, so for example, a clay brush with a alpha texture of rocks will only pull the surface out where the alpha is not black.

If you want the brush to push the surface in, or both push in AND pull out, you can modify the mid value. So if you set the value to 0.5, a middle gray in the alpha will do nothing, a black value will push in, white will pull out.

Two buttons help you find the right value: the square button reads the mid value from the border of the image, and the picker lets you pick it on the alpha itself.




## ![](/icons/falloff.webp) Falloff {#falloff}

![](/images/falloff_menu.webp) 

This is similar to the [Alpha](#alpha), except that you drive the intensity with a single curve. This is combined with the alpha so that you can use a texture for detail, and falloff to control the edge fading and intensity at the center of the tool.

When the curve is on the top, this is full deformation, when it's at the bottom the brush has no effect.

You can think of the curve as a cross section through the tip of the brush. The bottom section gives a preview of a what a single 'stamp' of the brush would look like on the model surface, and if there is an alpha texture for the brush, this will be shown too to preview how the falloff and alpha will interact.

### ![](/icons/fx.webp) Preset {#preset}
With `Preset...` selected, clicking on the curve graph will bring up a menu of presets. Rounded curves will give softer results, angular curves will have sharper results. The `Sub` button in the left toolbar will effectively reverse the falloff, so the top of the curve will push into the surface instead of pulling out, or vice versa.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
When selected, the user can draw their own falloff curves. The curve editor works the same as curves in the rest of Nomad:

* Click on the curve to create a new point
* Drag a point to reposition it
* Click on a point to toggle between sharp and smooth
* Drag a point into a neighbor point to remove it

### ![](/icons/curve_bspline.webp) B-spline {#b-spline}
When selected, the user can draw their own falloff curves. The editor works the same as Catmull-Rom, but curve points influence the curve instead of being directly on the curve, which can help in creating smoother curve shapes.

### ![](/icons/curve_bevel.webp) Bevel {#bevel}
The points are joined by straight lines, with rounded corners whose size depends on each point's sharpness. Handy for flat-topped brushes with a clean bevel at the edge.

The curve editor has 3 buttons:

| Item     | Icon                        | Description                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | Expand the curve editor                      |
| Reset    | ![](/icons/reset.webp)     | Revert the curve to the default state        |
| Symmetry | ![](/icons/symmetric.webp) | Display the curve as a symmetric 'brush tip' |


### Influence {#influence}

* `Sphere` (3d) - Influence is computed by taking the distance from the vertex to the brush's center.
* `Circle` (2d) - The vertex is first projected on the area plane, before taking its distance to the brush's center. This is similar to how alphas are sampled. 
* `Cylinder` - The influence is projected through the area as a cylinder. This is the same as enabling [Silhouette](#silhouette-1) below.
* `Ridge` - The falloff is measured across the stroke, so the curve becomes the cross-section of the whole stroke. The `Sym` button then mirrors the profile across the stroke: edit one side and the other follows. When it's off, the curve goes from the left side of the stroke to its right side. Not available for the flatten-based tools.

### ![](/icons/silhouette.webp) Silhouette {#silhouette-1}
By default strokes will only affect the model surface within the brush radius. When silhouette is enabled, the stroke will be projected through the entire model. This can be very useful when doing the initial blocking out of a model, or for shapes that require the sides to remain perpendicular. It has the same projection options as the [Silhouette](#silhouette) of the Stroke tab.



## ![](/icons/filter.webp) Filter {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Accumulate stroke {#accumulate-stroke}
Enable no limit to how much matter can be added/removed per stroke. Eg the `Clay` tool has this enabled, so material can keep building up, while the `Brush` tool has this disabled, so strokes will stop adding material if you keep moving the same stroke over the same region of the mesh. 

### ![](/icons/culling.webp) Front-facing vertex only {#front-facing-vertex-only}
This option will ignore back facing vertices.
It can be useful if you want to paint part of a thin geometry without impacting the other side.
It also works for sculpting but you might experience some artifacts.

### ![](/icons/eye_open.webp) Visible vertex only {#visible-vertex-only}
Ignore vertices hidden behind other surfaces, as seen from the camera. This option shows up for shape strokes (lasso, rectangle...) of the masking, painting, `Face Group` and `Hide` tools.

### ![](/icons/dynamic.webp) Allow dynamic topology {#allow-dynamic-topology}
This option is only available if your mesh is in [Dynamic Topology](topology.md#dynamic-topology) mode. You can disable or enable dynamic topology per tool.

### ![](/icons/connect.webp) Connected topology {#connected-topology}
Enable only sculpting the vertices that are linked to the surface you touch with the tool. For example when used with the `Move` tool, this will allow you to move a part even if it intersects with another part.
![](/videos/connected_topology.mp4)

### Protect area {#protect-area}
![](/images/filter_protect_area.webp) 

These options will stop tools affecting parts of your mesh under various conditions. Each one can be set to `Auto`, `No` or `Yes`, and the small arrow shows what `Auto` currently resolves to.

* `Hide` - If parts of the mesh are hidden with the hide tool, set if they should be protected. On `Auto`, hidden faces are protected, unless their wireframe is visible (see the [Wireframe](settings.md#wireframe) settings).
* `Mask` - If parts of the mesh are masked, set if they should be protected. On `Auto`, masked parts are protected while the mask is visible in the [Shading](shading) menu.
* `Face Group` - Set if you can only use a tool within the first touched face group. On `Auto`, this follows whether face groups are visible in the [Shading](shading) menu.

The `(All)` button sets if these protections are global, shared by all tools, or set per tool.


### Area sampling {#area-sampling}
Some brushes or stroke options require a plane normal and a plane position to the surface in order to work.

You can control how to compute this average plane by setting the sampling area as a ratio of the tool radius.

At 100%, every point inside the selection circle is taken into account.

At 0%, only the nearest vertex or triangle is taken into account. These values can be linked for both `Normal radius` and `Position radius`, or unlocked and set independently.

### Area Normal Filter {#keep-sharp-edges}
Exclude points whose normals deviate too much from the surface normal.

It will change how the plane area is computed (Area sampling), so it's mostly useful for clay or flatten-based tools.

The `Min` and `Max` angles control the fade between excluded and fully affected points, as shown by the small colored disc next to them.

### Falloff Normal Filter {#falloff-normal-filter}
Like the [Area Normal Filter](#keep-sharp-edges), it excludes points whose normals deviate too much from the surface normal, but it acts on the brush falloff instead of the plane computation. It's the one to use when painting: color stays on one side of a sharp edge instead of spilling over it, and it helps when painting creases or bumps. `Min` and `Max` work the same way.

![](/videos/filter_keep_sharp_edges.mp4)


### Depth filter {#depth-masking}
![](/images/stroke_depthmask.webp)

Exclude points that are above or below a certain distance of the computed plane (Area sampling).

This can be used to paint only on bumpy regions, or only on cavity regions.

The graph represents a cross section of the surface; the horizontal line is where the surface is, the circle represents the paint falloff radius relative above and below the surface. `Height offset` is a percentage above or below the surface to start the masking calculation. With `Depth falloff` enabled, `Top area` and `Bottom area` allow you to scale the falloff above and below the offset point.

#### Example: Paint in cavities {#example-paint-in-cavities}
To paint only cavity regions, leave the height offset at 0%, enable `Depth falloff` and lower `Top area` to about 10%, so that only what sits below the surface gets painted. Set [Area sampling](#area-sampling) to 100%: the plane then rests on the top of the surface instead of dropping into each groove.

![](/videos/stroke_depth_cavity.mp4)

#### Example: Paint on bumps {#example-paint-on-bumps}
To only paint in high regions, set the height offset to about +50%, with `Depth falloff` off and [Area sampling](#area-sampling) at 100%. The plane follows the overall surface, so anything at its height or above gets painted, and deep cavities are skipped.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Pressure {#pressure}
![](/images/pressure_menu.webp) 

Control how the stylus/pen pressure affects the brushes.

### Use global settings {#use-global-settings}

By default `Use global settings` is enabled, meaning all brushes will share the same pressure values. Uncheck it to give the current tool its own pressure settings.

### ![](/icons/radius.webp) Radius {#pressure-radius}

This curve controls how the brush radius is affected by pressure. The default is a linear relationship, so if your stylus has a smooth response, then the radius change should also feel smooth. That said, many stylii have a non-linear response, which you can compensate for with this curve. For example, if the radius doesn't feel like it gets to its maximum value at high pressure, use a curve preset like 'out-pow3', with a bend that aims up, to increase radius earlier.

This dialog is similar to the falloff curve display, you can use a preset by tapping on the curve window, or draw your own curves with the `Catmull-Rom`, `B-spline` and `Bevel` modes.

If you want constant radius, disable this section.

### ![](/icons/intensity.webp) Intensity {#pressure-intensity}

Similar to the radius curve, but for controlling intensity. If you want constant intensity, disable this section.

### Limit pressure at 100% {#limit-pressure}

Make sure the stylus pressure never goes over 100%. This is a global setting.

### Pressure smoothing {#pressure-smoothing}

Average the stylus pressure events for smoother results.
