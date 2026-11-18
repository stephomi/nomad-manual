# ![](/icons/transform.webp) Transform {#transform}

This menu shows the transformation of the selected object as numbers: where it is, how it's rotated and scaled, and how big it is. Type exact values, reset them, or bake them into the mesh.

![](/images/transform_overview.webp)

## Overview {#overview}

Every object has a node that stores its translation, rotation and scale (its matrix), on top of its vertices. The [Gizmo](tools.md#gizmo) and [Transform](tools.md#transform) tools change that matrix when you drag in the viewport; this menu lets you read it and type the values instead. See [Nodes and vertices](tools.md#nodes-and-vertices) for the difference between moving the node and moving the vertices.

Drag a value left or right to change it, or tap it to type a number. The X, Y and Z values are tinted red, green and blue, like the gizmo axes.

::: tip
Typing values is handy to place objects precisely, for example to put several parts at the exact same height, or to bring back a rotation to a round number after a free rotation with the gizmo.
:::

## Matrix {#matrix}

The title tells you which space the values are expressed in: `local` (relative to the parent object) or `world`.

### Object and Pivot {#object-pivot}

* `Object` - The values are the object's own transformation.
* `Pivot` - The values drive the selection from its [pivot](tools.md#pivot), the same way the gizmo handles do: the rows read zero, and changing them moves, rotates or scales the selection around the pivot. Turn on `Edit` (the lock icon) to move the pivot alone, the objects stand still.

### Local and World {#local-world}

When the object has a parent or children, or several objects are selected, you can pick in which space to show the values: `Local` (relative to the parent) or `World`.

### Actions {#actions}

| Action        | Icon                          | Description |
| :-----------: | :---------------------------: | :---------- |
| Move origin   | ![](/icons/target.webp)      | Move the object to the world origin. |
| Bake          | ![](/icons/bake.webp)        | Apply the matrix to the vertices and reset the matrix. Visually, nothing changes, but the object's origin is now the world origin. |
| Pivot         | ![](/icons/gizmo.webp)       | Bake the pivot into the object: the object's origin and orientation become those of the pivot. Visually, nothing changes. |
| Edit          | ![](/icons/lock.webp)        | (`Pivot` mode) Move the pivot alone. |
| Reset         | ![](/icons/reset.webp)       | Reset the transformation to identity. In `Pivot` mode it puts the pivot back in place instead. |

When the selected object has instances, baking asks for confirmation, with an `Un-instance` option: baking changes the vertices, which instances share.

### Translation, Rotation, Scale {#translation-rotation-scale}

The position, rotation (in degrees) and scale of the object, on X, Y and Z. The two buttons at the end of each row bake only that part of the transformation into the vertices, or reset it.

A `Skew` row also shows up when the object is skewed, for example after a non uniform scale of a rotated parent.

### Uniform scale {#uniform-scale}

When enabled, the scale is a single value, the same on all three axes. Disable it to scale X, Y and Z separately.

## Dimension {#dimension}

The size and center of the selection's bounding box, in world units. With several objects selected, it covers them all.

* `Size` - The width, height and depth. With the link button on, changing one size scales the other two by the same amount, keeping the proportions.
* `Center` - The center of the bounding box. The target button moves the selection so its center is at the world origin.

::: tip
`Size` is the quickest way to give an object a real-world size, for example before a 3d print: set the height you want and the link keeps the proportions.
:::
