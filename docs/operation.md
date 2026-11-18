# ![](/icons/operation.webp) Operation {#operation}

This menu applies an operation to the whole surface of the selected objects at once: smooth, relax, polish, inflate, adjust the colors, blur or sharpen the paint and the mask.

![](/images/operation_overview.webp)

## Overview {#overview}

Where a brush works where you stroke, an operation works on every vertex of the selected objects in one go. The title shows the name of the object, or the number of objects when several are selected.

Each operation is a slider: drag it to the right to apply more, to the left to apply less (or the opposite operation, for sliders with an arrow on both sides). The slider goes back to zero once you release it, and each drag is a single step in the [History](history.md), so you can apply an operation several times in small doses.

::: tip
The operations are a quick way to clean up a whole mesh after a voxel remesh or a boolean: a little `Relax` evens out the triangles, a little `Smooth` removes the noise, without hunting for every spot with a brush.
:::

## Filters {#filters}

The buttons at the top restrict where the operations apply:

* `Mask` - Masked areas are left untouched.
* `Hide` - Hidden areas are left untouched.
* `Offset` - (With a [layer](layers.md) selected) Only the areas where the active layer holds sculpting are affected, so you can smooth or inflate the content of a layer without touching the rest.

## Smoothing {#smoothing}

* `Preserve volume` - Smooths without shrinking the surface. The cog button holds the `Shrink` and `Inflate` amounts used for it.
* `Preserve boundary` - Vertices on the boundary of the mesh (the edge of a hole) stay still.
* `Stable smoothing` - Tries to make the smoothing independent of the topology. It works best when the polygon density varies a lot.
* `Smooth` - Smooths the surface. Drag to the left to `Sharpen` it instead.
* ![](/icons/group.webp) `Smooth` - Smooths the borders between [face groups](tools.md#facegroup), straightening jagged group outlines. Drag to the left to sharpen them.
* `Relax` - Evens out the polygons, keeping the shape.
* ![](/icons/group.webp) `Relax` - Relaxes the polygons along the face group borders.
* `Keep corners` - With the face group `Smooth` and `Relax`, the borders stay fixed where they turn more than this angle, so the corners stay sharp while the sides smooth. Use its checkbox to turn it on.

## Polish {#polish}

Flattens the surface into clean facets, like the [Polish](tools.md#polish) tool. `Angle` sets which faces flatten together: faces that bend less than this angle become one facet. A lower angle keeps more creases and smaller facets.

## Inflate {#inflate}

Pushes the surface outward along its normals, or inward when you drag to the left. `Normal (Relax)` relaxes the polygons at the same time, so they don't stretch; use its checkbox to turn it off.

## Color adjustments {#color-adjustments}

Pick the channel to adjust, `Color`, `Roughness`, `Metalness`, `Opacity`, `Density` (the [Quad Remesher](tools.md#quad-remesher) density painting, when the object has some) or `Mask`, then:

* `Exposure` - Brightens or darkens the values.
* `Saturation` - (`Color` only) More or less vivid colors.
* `Contrast` - Spreads the values apart, or brings them closer together.
* `Hue` - Shifts the colors around the color wheel.

## Blur {#blur}

Blurs the selected channels across the surface: toggle `Color`, `Roughness`, `Metalness`, `Opacity`, `Density` or `Mask`, then drag `Blur`. Drag to the left to `Sharpen` instead.

For the mask, this is the same as the `Blur` slider of the [Mask](tools.md#mask) tool. Here you can blur the paint channels too.
