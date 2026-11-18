# ![](/icons/symmetry.webp) Symmetry {#symmetry}

This menu controls how strokes will be repeated across a mirror plane, radially or as tiles, and ways to restore symmetry on non-symmetrical objects.

![](/images/symmetry_overview.webp) 

## Overview {#overview}
You can use symmetry in several ways:

* As a mirror, flipping work across X (left/right), Y (top/bottom), Z(back/front), or a combination. 
* Radial symmetry can be set on X Y Z with a number of repeats, eg sculpting a starfish. 
* Tiling repeats your strokes across the object, so the sculpt tiles seamlessly.
* Mirrors can operate around the origin (called world mode)  or around the center of an object (called local mode).
* Sculpts that started non-symmetrical can be forced to be symmetrical.

A shortcut to enable/disable symmetry can also be found on the left quick panel (*"Sym"*). The small 'L/W' indicates if Nomad is in Local or World symmetry mode. You can also long press or swipe to the center of screen to bring out a menu.

![](/images/symmetry_button.webp) 

The symmetry settings are saved with each object, and the menu title shows the name of the object you are editing.
The sculpting tools share the same on/off state, while the transform tools ([Transform](tools.md#transform) and [Gizmo](tools.md#gizmo)) have their own.

::: tip
The symmetry menu is mainly for controlling stroke symmetry. You can also mirror and repeat objects via [repeaters found in the scene menu](scene#repeaters). 
:::

## ![](/icons/symmetry.webp) Enabled {#enabled}
Toggle the mirror mode, this is the same as the `Sym` button in the left quick panel. A warning icon reminds you when it's off, and the menu also tells you when the current tool ignores symmetry.

## Planes {#planes}

Enable plane(s) of symmetry, and number of repeats for radial symmetry. Note that you don't have to just chose a single plane, you can have all 1, 2 or 3 planes enabled for complex symmetry.

The `Radial` row sets the repeat count for radial symmetry around each axis. Note that these also aren't restricted to a single axis, and can even work in combination with plane symmetry to generate detailed results very quickly. (The number of total repeats is limited to 200)

![](/videos/symmetry_demo.mp4) 

## Tile {#tile}

Repeat your strokes along an axis, at a regular distance, so the sculpt tiles seamlessly. Handy for patterns, bricks, or a texture you plan to repeat.

Turn tiling on for each axis with the `Tile` buttons, then set either a `Count` (how many repeats span the object) or a `Distance` (the space between two repeats). Tap the toggle on the left to switch between the two.

## Method {#method}
The mirror can either be `Local`, and move with the object, or be `World`, and not move. If you're not sure which mode you need, observe the mirror plane and radial indicators that are overlaid on the object. When in local mode, if you use the transform tools (`Gizmo` or `Transform`) and move the model, the mirror indicators will move as well. When in world mode, the mirror indicators will stay fixed, and the object will slide through them.

## Mirror {#mirroring}
![](/images/symmetry_mirroring.webp)

When sculpting near the symmetry planes, some brushes will have imperfect symmetry behavior. This section allows you to restore symmetry by copying one side of your sculpt to the other. 

`Direction` - The two arrow buttons next to the `Mirror` title determine which side will be copied to the other. Nomad calculates this from your current viewport, so the side stays the same on screen whichever way you look at the model.

![](/icons/shield.webp) `Mask` - The mask button lets you isolate what will be mirrored; masking the destination side will protect that region, masking the source side will stop that area from being mirrored to the destination. 

![](/icons/tool_hide.webp) `Hide` - When active, areas that are hidden on the source side will not be mirrored to the destination. 

`Mirror` (Keep topology) will try to identify if the topology is the same on both sides of the mirror, and if so, just move vertices. This is the more common scenario. Radial symmetry is ignored. If the topology isn't symmetrical, Nomad offers to enforce the mirroring with `Cut • Mirror` instead.

The `Cut` buttons cut the object along the symmetry plane(s). They change the topology, so they are more destructive than `Mirror`. The number on each button is how many objects you get:

* `Cut` - remove one side of the object.
* `Cut • Mirror` - cut the object, copy one side, mirror it to the other, and weld vertices along the mirror. Sometimes this method is required if the model is very different across the mirror.
* `Cut • Split` - cut the object and keep each side as a separate object.
* `Cut • Mirror • Split` - like `Cut • Mirror`, but each side becomes a separate object.

If several objects are selected, `Mirror` and [Flip object](#flip-object) apply to all of them.

### Flip object {#flip-object}
![](/images/symmetry_flip.webp)
Make the left side to the right side, and vice versa, along `X`, `Y` or `Z`. Similar in appearance to if you used the gizmo tool menu and set the scale to -1 on X.

## Reset and Edit {#reset-and-edit}

![](/images/symmetry_edit.webp)

It is possible to edit the symmetry location and orientation (but not recommended!). If needed, `World center` (`Object center` in local mode) and `Orientation` will reset the symmetry location and orientation to their default values.

Nomad usually knows where to put the symmetry plane. It is not recommended to adjust this manually, but the `Gizmo (Edit)` button allows this for advanced users. When this button is clicked, a gizmo is shown to let you translate and rotate the symmetry plane. If you want to restore the default center and orientation, use the reset buttons above.

`From pivot` places the symmetry plane on the pivot of the [Gizmo](tools.md#gizmo) tool. It is only available while the `Gizmo` tool is active.

The behavior of these options will change depending on what space (*Local/World*) you are in.
So if it doesn't work as you would expect, make sure to check if you are in the correct space.

::: tip
Editing the symmetry plane with the gizmo is a bit experimental, you probably shouldn't need it!
:::

## Show options {#show-options}
![](/images/symmetry_show.webp)


`Show line` and `Show plane` will toggle a viewport overlay of the symmetry locations. Note that turning off these options will only take effect when the symmetry menu is closed.
