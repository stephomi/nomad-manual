# ![](/icons/layer.webp) Layers {#layers}

This menu contains the layer stack, a way to store edits to your object in a non destructive way, and many ways to combine and repurpose layers.

![](/images/layers_overview.webp) 

## Overview {#overview}

Nomad layers serve multiple purposes.

Paint information (Color, Roughness, Metalness, Opacity) work with layers similar to 2d paint applications. A layer can be created and paint applied to a model. The layer can be toggled on or off, have its opacity adjusted, the layer can be duplicated, its order can be changed in the layer stack, its blending mode adjusted.

Nomad also uses layers for sculpting. A layer can store fine details like wrinkles, or it can store large changes, allowing them to function like blendshapes/shape keys/morph targets in other 3d applications. For example you could sculpt different facial expressions on different layers, and adjust the layer sliders to combine them into new expressions.

In this case the changes stored in a layer are purely additive, layer order doesn't matter like it does for paint.

Layers can be partially erased via the [Delete Layer](tools.md#delete-layer) tool, and layers can also be used to create masks based on the different information stored in the layer.

![](/videos/layer.mp4)

::: tip
Unlike most sculpting software, changing the topology of a mesh will not discard the layers. You can use the [Voxel Remesher](topology.md#voxel-remesher), the [Multiresolution](topology.md#multiresolution) or the [Trim](tools.md#trim)/[Split](tools.md#split) tools, but note that when using [Voxel Remesher](topology.md#voxel-remesher), the quality of the layer will be impacted.
:::

::: tip
If using layers for blendshapes/morph targets, there is extra layer functionality in the [scene menu](scene.md#object-menu). you can separate layers into objects, and combine matching objects into layers.
:::
----

## Layer menu {#layer-menu}

![](/images/layers_menu.webp)

The title shows the name of the selected object. Layers aren't available on primitives, so validate the primitive first.

Press `Add layer` to create a new layer. `Merge layers` merges every layer into the base mesh, the number next to its icon is how many layers there are.

Each layer has a name, a slider to control it's strength/factor, and option buttons. Tap a layer to make it the active one: sculpting and painting go into that layer. Tap `Base` to work on the base mesh again.

### ![](/icons/sort_right.webp) Expand list {#ui-expand-list}

By default, the layer list only shows the visibility, blend mode and strength of each layer, and the active layer is expanded with its full controls. The arrow on the left of the title expands the full controls for every layer.

![](/images/layers_expand.webp)

### Options {#options}

| Action       | Icon                         | Description                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Visible      | ![](/icons/eye_open.webp)   | Show/hide the layer                                 |
| Blend Mode   | ![](/icons/opacity.webp)    | The photoshop style blending mode. The 4 icons display the modes for Color, Roughness, Metalness, Opacity.                                 |
| Edit Name    | ![](/icons/pencil.webp)     | Edit the layer name                                 |
| Delete       | ![](/icons/trash.webp)      | Delete the layer                                    |
| Duplicate    | ![](/icons/clone.webp)      | Duplicate the layer                                 |
| Merge Down   | ![](/icons/merge_down.webp) | Merge the layer with the lower layer (or base mesh) |
| More         | ![](/icons/more.webp)       | [More...](#more) options                            |

When a layer isn't expanded, `Edit Name`, `Delete`, `Duplicate` and `Merge Down` are found in its [More...](#more) menu.

To move a layer to another part of the layer stack, press and hold on its name, then drag.

### Base {#base}

The 3 dots button of the `Base` row moves the paint of the base mesh into a new layer, with the `Base → Layer` button. The base is then reset to the background material. This is handy when you painted a lot before creating any layer.

* The mask and hide buttons next to it leave masked and hidden areas untouched.
* `Extract` - the channels to move: `Color`, `Opacity`, `Roughness` and `Metalness`.
* `Background material` - if enabled, only the values that differ from this material are moved. Set it with the sliders, or pick it from the model with the eyedropper.

### ![](/icons/more.webp) More... {#more}

The 'More...' button will show extra options for the current layer, in two tabs: the settings (cog icon), and the extraction (cube icon).

![](/images/layers_more.webp) 

#### Channel factors {#channel-factors}

These controls let you scale the amount of sculpt/color/roughness/metalness/opacity for the layer. These values are multiplied against the layer factor slider, so for example if the layer strength is 1, but the color channel factor is 0.5, then the color displayed will be at 0.5 strength.

`Offset` controls the layer sculpt strength. While color/roughness/metalness are clamped between 0 and 1, offset can be any value, both positive and negative. 

::: tip
Offset can be used to turn a layer of bumps into a layer of cavities, or a smile into a frown:
![](/videos/layer_happysad.mp4)


A symmetrical layer can be cloned and then split into left/right shapes with the [`DelLayer`](tools.md#delete-layer) tool:
![](/videos/layer_leftright.mp4)

Layers with negative offset factors can be baked down to empty layers to make new positive shapes.

Layers with positive offset factors above 1 can be used to experiment with more extreme blendshapes.
:::

::: warning
At the moment layers only share a single opacity channel for all 3 channels (color/metalness/roughness).
If you merge multiple layers with per-channel intensity that aren't at full intensity, it's possible that the final result will look different.

Maybe in the future, each channel will have its own alpha channel to remove this limitation.
:::


#### ![](/icons/shield.webp) Mask {#mask}
The mask button next to each slider will create a mask from that channel. Similar to using layers to make selections in painting applications, this allows you to reuse work you have done in a layer for other operations.

#### ![](/icons/preview.webp) Preview {#preview}
![](/images/layers_preview.webp) 

The following options are in the extraction tab of the 'More...' menu.

When enabled, will preview the extract settings for this layer (see the next section).

`X-Ray` picks which objects are made transparent during the preview (`None`, `Unselected`, `Selected` or `All`), so the extracted shape stays solid. It's useful if you are using negative extraction heights.

#### ![](/icons/mask_extract.webp) Extract {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

The `Extract` button will duplicate the contents of the layer into a new object, usually with a user specifed thickness set by the next section.

`Closing action` determines how the duplication is done:

* `None` - Simply extract the part, do not try to generate sides or fill any holes.
* `Fill` - Hole is filled and smoothed with triangles. Do not use this option for flat surfaces.
* `Shell` - Close the extracted shape with the thickness value and direction options.
* `Layer` - Extract the layer difference.

#### ![](/icons/height.webp) Height {#thickness}
![](/images/layers_thickness.webp) 

The depth of the shell extrusion. Positive values grow out of the surface, negative values grow into the surface. It is hidden when the closing action is `Layer`.

The plus/minus next to this value will set the direction of the extrusion:
* Minus ( - ) will start from the current surface and extrude down. 
* Plus ( + ) will start from the current surface and extrude up.
* PlusMinus ( ± ) will push the top and bottom of the extrusion away by equal amounts, so it will be halfway embedded in the original surface.

#### Sides {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

This section is visible when the closing action is `Shell`. 

`Wall divisions` sets the number of divisions along the shell sides. With its `Auto` toggle on, Nomad calculates the number of edge loops to create square polygons.

#### Smoothness {#smoothness}
![](/images/layers_smoothness.webp) 

If the edges of the region to be extracted are jagged, enable this option to smooth them into a nicer shape. `All` smooths the whole extracted surface, `Borders only` smooths its edges. `Iterations` sets how strong the smoothing is.

_This is the end of the 'More...' submenu._

### ![](/icons/cog.webp) Advanced {#advanced}
![](/images/layers_advanced.webp)

The `Advanced` button at the bottom of the menu appears once the object has layers.

#### Keep top layers details {#keep-top-layers-details}

Ensure that small details on higher layers remain visible when large changes are made to lower changes. While you sculpt, the deformation coming from the top layers is ignored, but their details stay visible. It only works well if those top layers hold relatively small details. Turning it on asks for a confirmation first.

By default if you sculpt small wrinkles on a layer, then go and make large changes to the base layer, the wrinkles will be lost. Enabling this toggle will allow those small details to always float above the lower large changes. In the following video, see how the wrinkle detail gets removed by default, but remains visible when 'keep top layers details' is enabled:

![](/videos/layers_details.mp4)


#### Sync transform {#sync-transform}

When on, all the unselected layers will be adjusted depending on the transform rotation, scale, skew, when you use the Gizmo or Transform tools. It can be `Auto`, `No` or `Yes`.

Disable this option if the other layers are meant to be used without the new transform that you are applying.

When set on `Auto`, only the visible layers will be adjusted.