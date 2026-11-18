# ![](/icons/paint.webp) Painting {#painting}

Control the color, roughness, metalness of paint strokes, allow for flood filling of paint attributes, and how paint tools interact with layers, masks, hidden selections.

![](/images/paint_overview.webp)  

## Overview {#overview}

Nomad uses PBR vertex painting. What does this mean?

### PBR {#pbr}
PBR, or Physically Based Rendering is a popular computer graphics technique for film, television, games and mobile. By basing lights on physical properties, and defining surfaces through color, roughness, metalness, a wide variety of photoreal looks can be achieved.

### Vertex painting {#vertex-painting}

Vertex painting means that the paint information is stored in the vertices of the model, rather than in textures. Because Nomad can handle models with hundreds of thousands, often millions of vertices, your models should be able to have highly detailed surface paint; if you can sculpt the detail, you can also paint that detail.

This also means that painting in Nomad doesn't require UV mapping, often a slow and technical process in other 3d applications. Many other 3d applications don't support the high vertex counts that Nomad can, however Nomad also has good texture baking and decimation tools to help.

### Texturing {#texturing}

Nomad supports textures, but they have to be present in an imported model, or via baking vertex painting to textures. 

A texture is simply an image, but in the 3d context it usually refers to an image assigned to an object.
In order to wrap an image around a model, the model needs texture coordinates (UV).

Nomad can compute [them automatically](topology.md#uv-unwrap) but you don't have much control on the overall quality.

::: tip
One example of workflow:
- Sculpt on Nomad, then [UV unwrap](topology.md#uv-unwrap)
- If you already started to paint in Nomad you can [transfer the vertex painting to textures](topology.md#bake-texture)
- Export to Procreate
- Texture in Procreate
- Export back to Nomad for rendering purpose
:::

That's the overview, now lets explore the sections of the painting menu:


## Stroke painting {#stroke-painting}
![](/images/paint_intensity.webp)  

Enable painting for this tool, useful if you need to sculpt and paint at the same time. When a tool can paint but this checkbox is off, a warning icon next to the title reminds you.

For tools where painting is the primary function (eg Paint, Smudge, Mask), this checkbox doesn't exist.

### ![](/icons/opacity.webp) Paint intensity {#paint-intensity}

A slider to allow you to use a different intensity to the primary tool intensity.

The sliders button next to it adds a quick paint intensity slider to the side bar, for tools that sculpt and paint at the same time.

The `Alpha`, `Falloff` and `Randomize intensity` buttons determine if those features will affect painting. Eg you could have randomize enabled for the clay tool, but color won't be randomized.

* `Alpha` - when disabled, painting ignores the alpha and covers the entire brush area. With the VDM tool, this button is replaced by `Stamp material`, which turns on or off the material stored in the stamp.
* `Falloff` - when disabled, painting stays at full intensity up to the brush edge.
* `Randomize intensity` - whether the intensity part of the stroke randomizer affects painting. Position, rotation and scale randomization always move the whole stamp.

These options are ignored by [Paint all](#paint-all), but the alpha is used by its triplanar variant.

### ![](/icons/link.webp) Global material {#global-material}
If this option is enabled, the selected material will be the same as the other tools. Note that it only takes into account roughness, metalness and color settings. Disable it to give this tool its own material.


## Material {#material}
![](/images/paint_material.webp) 

The first icon is a material preview shape. Dragging on the 3d material preview will rotate it. 

The second icon is a preview of the paint stroke with the selected alpha and falloff options.

### ![](/icons/falloff.webp) Curves {#curves}

Opens a curve editor for the texture slots of the [PBR sliders](#pbr-sliders). It remaps the texture values before they are painted, without touching the image file. A small curve icon on a texture slot tells you its curve has been edited.

### ![](/icons/cog.webp) Material options {#material-options}

The `Material` button next to the title holds two settings.

`Material viewport preview` determines what will happen on the selected object while you change the color, roughness, metalness, opacity and intensity sliders:

* `None` - No preview will be shown on the model when you adjust properties
* `Material` - The material values will be previewed on the object when you adjust properties.
* `Triplanar` - The material will be previewed as a Triplanar projection. 

The color, roughness, metalness and opacity checkboxes below choose which channels the [Material picker](#material-picker) replaces.

### ![](/icons/dropper.webp) Material picker {#material-picker}

The eyedropper picks the material under the cursor, from any object in your scene. Only the channels checked in the [Material options](#material-options) are replaced.

## Material Presets {#material-presets}
Tapping the 3d preview shape will bring up a preset menu of materials, these can be cloned to define your own presets.

![](/images/paint_presets.webp) 

The `Embed textures` toggle stores a copy of the textures used by this material inside the preset. Without it, the preset only references the textures in the Nomad textures/ folder. Turn it on when you want to share a textured preset without sending its textures separately.

`Include Alpha` also saves the brush alpha in the material preset.

## PBR sliders {#pbr-sliders}
![](/images/paint_sliders.webp) 

[PBR](shading.md#pbr) painting uses 4 channels:
- `Color` The color that will be painted. The eyedropper can be used to select color from other parts of the model, or from reference images.
- `Roughness` It tells how "rough" or "smooth" a surface is. A low value for the roughness means that the reflections will be sharp.
- `Metalness` It simply tells if the surface is metallic or not. The value should be either 0% or 100% most of the time, in-between values should be exceptional.
- `Opacity` How much the material can be seen through. Strictly speaking it is not part of the PBR specification, but it is useful in many situations. 1 is fully opaque, 0 is transparent. Note that  opacity and refraction are different things, refraction in nomad is handled via the refraction material. 

If you select a material preset, 3 channels are painted simultaneously (opacity is often intentionally excluded). This means that instead of just painting 'red', you can be painting 'a red rough metal' or 'a white smooth plastic'.

The square is a texture slot, click it to to use a texture for that property instead of a solid value. A color texture tints the color, while a roughness, metalness or opacity texture replaces the slider value (its label is struck out to show it). For the opacity texture, `Use Alpha as Value` reads the texture's alpha channel instead of its grayscale value.

With the VDM tool, when the stamp carries its own material, an extra slot shows it next to the texture slot. Tap it to use or ignore that channel of the stamp.

The brush icon next to the sliders will flood fill that property over your object.

The checkbox will enable or disable that particular property, so you could only paint colour, or only paint roughness and opacity, for example. 

Here are some examples of different roughness and metalness properties:

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Roughness and metalness require the [Lit (PBR)](shading.md#pbr) shading mode. In [MatCap](shading.md#matcap) or [Unlit](shading.md#unlit) mode they are ignored, and the menu shows a warning.
:::

::: tip
When using textures for pbr painting, it's often useful to swap to something like the `Stamp` tool, or use the stroke menu to use a mode other than dot, which can smear the texture.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
You might consider turning on `Smooth Shading` [globally](settings.md#smooth-shading) or [per-object](material.md#smooth-shading) if you are painting a metallic surface on on object with a lower polycount.
:::

## ![](/icons/paint.webp) Paint all {#paint-all}

![](/images/paint_paint_all.webp)

Apply the current material to the selected objects, either in standard mode with `Paint all`, or as a Triplanar projection with `Paint all + Triplanar`. The triplanar variant isn't available on primitives that haven't been validated.

The checkboxes next to the color/metalness/roughness/opacity sliders are respected, any disabled properties will no be filled.

The extra buttons control how the paint all can be further affected. Most show a percentage, and they are greyed out when they would have no effect:

| Icon                        | Description                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | Masked areas won't be affected.               |
| ![](/icons/tool_hide.webp) | Hidden areas won't be affected.               |
| ![](/icons/opacity.webp)   | Use the tool painting factor above.           |
| ![](/icons/layer.webp)     | Unpainted areas of a layer won't be affected. |
| ![](/icons/triplanar.webp) | `Vertex`: the triplanar variant also offsets the surface with the alpha, by the tool intensity shown. |
| ![](/icons/cog.webp)       | Open the Triplanar settings                   |

### ![](/icons/cog.webp) Triplanar settings {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Similar to the [triplanar settings in the material menu](material.md#triplanar), you can control the blending of the projections, tiling and offsets. 

Use the preview checkbox at the top of this menu to enable a persistent preview while adjusting values.