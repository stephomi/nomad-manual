# ![](/icons/material.webp) Material {#material}

This menu allows you to change the material of the current object, render properties of the object/material, and assign textures to the material.

![](/images/material_overview.webp)

Materials define the how an object looks, by controlling how it reacts to light and to other objects. The look of an object is controlled by these properties:

* `Material type`
* `Color`
* `Roughness`
* `Metalness`
* `Opacity`
* `Reflectance`
* `Emissive/unlit`

Combinations of these properties can achieve a wide variety of results from photorealistic to cartoony to experimental.

Color, roughness, metalness and opacity can be painted, see [Vertex Paint options](painting.md) for more information.

Material type, reflectance, emssive/unlit are material properties explained below.

The `Copy` and `Paste` buttons at the top of this menu allow you to copy materials from one object to another.

Note that Nomad's renderer is a realtime renderer; while powerful, it favours speed over accuracy for certain effects. 

## Material types {#material-types}

![](/images/material_types.webp)

Nomad material types are Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Opaque {#opaque}
The default mode that treats surfaces as a simple material that supports painted color, roughness, metalness, opacity. Painted opacity, an opacity texture or the alpha channel of the color texture still make the object see-through, using dithering. Only the main opacity slider is ignored.

### ![](/icons/material_subsurface.webp) Subsurface {#subsurface}
This mode can simulate material that allows light to blur and scatter light internally like skin, wax, jade.

It requires the PBR shading mode. To get the best result, use at least one directional or spot light, ideally with a dim environment.

The color swatch sets the color of the scattered light.

`Depth` controls how far light scatters from the front, to under the surface, then out the front surface again. This has the effect of softening hard shadows, and blurring surface detail.

`Translucency` controls how light scatters from the front to the back of a shape, like like scattering through the underside of a leaf, or when ears are strongly backlit. You need a light that casts shadows to see it.

### ![](/icons/material_blending.webp) Blending {#blending}

Similar to Opaque, but supports the opacity slider to allow the material to mix between solid and transparent. This is a simple single slider for opacity, vs the paintable opacity supported by the opaque material. 

::: warning
Blending mode can cause flickering and popping in complex or intersecting shapes.
:::

### ![](/icons/material_additive.webp) Additive {#additive}
You can make your mesh semi-transparent with this material. It is similar to the blending material, but while blending will mix with its surroundings, additive will always be brighter than objects behind it, good for bright effects like light rays, fire, explosions.

You can set an opacity value higher than 1, which means the object will be brighter.  
It can be useful if you want to use [bloom](postprocess.md#bloom) and the `threshold parameter` to only make this object glow like an emissive object.

This mode tends to have less artifacts than [Blending](#blending) (order independent transparency).

### ![](/icons/material_refraction.webp) Refraction {#refraction}
This mode can be used to simulate glass material. It requires the PBR shading mode. Because of real time constraints, self-refraction and multi-layered refraction is somewhat limited.

The roughness painting of the model impacts how blurry the refraction is.
By default, every object created in Nomad has a roughness slightly around 25%, thus the refraction won't be perfect but a bit blurry.
You can use the `Paint glossy` button to repaint your model with a roughness and metalness of 0 (the colors won't be affected).

There are 2 different roughness at play, the one driving how blurry the reflection is on the surface, and the other one driving the interior (refraction).  
However, since there is only one painting roughness channel in Nomad, both interior and exterior roughness will share the same value.  
In order to have different values (for example a lollipop with sharp surface but blurry interior) you use the `Surface` and `Interior` sliders under `Override roughness` to override the painted roughness.

![](/videos/refraction.mp4)

#### Index of Refraction {#index-of-refraction}
How much the light bends when it enters the object. Higher values bend it more, like a thick lens.

#### Absorption {#absorption}
Simulate the light being absorbed as it travels through the volume, tinted by the color swatch, with `Factor` setting the strength. Thin parts are brighter because they let more light through, while thick areas are darker. Only an approximation of the object thickness is used, so the effect depends a lot on the shape.


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Make the object semi-transparent by discarding some pixels in a random fashion.

### ![](/icons/material_shadow_catcher.webp) Shadow Catcher {#shadow-catcher}

Make the object invisible, and only recieve shadows from lights. Useful to combine nomad renders with other images, usually on a plane. The color swatch sets the color of the shadow.

There must be a light casting shadows in the scene, otherwise the shadow catcher does nothing. The `Metalness → 0%` and `Metalness → 100%` buttons repaint the object: fully metallic, the shadow catcher can also reflect the scene when the [Reflection (SSR)](postprocess.md#reflection-ssr) post process is enabled.

::: tip

Further information about transparency and blending modes can be found at https://support.fab.com/s/article/Transparency-Opacity

:::

## Controls {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Always unlit {#always-unlit}
If enabled, the object will ignore PBR and Matcap and simply display its color painting without shading.
Note that if you use [Additive](#additive), you can paint transparency directly by using black color.

### Opacity {#opacity}
How solid or opaque an object will appear; 100% is solid, 0% is transparent. The slider is shown for the Blending, Additive, Dithering and Shadow Catcher types. You can also paint opacity for finer control.

### Pre-refract pass {#pre-refract-pass}
Blending and Additive only. Draw this transparent object before the refraction pass. Useful when a refractive object is in front of other transparent surfaces.

### Reflectance {#reflectance}
Controls the amount of reflection the material will receive for non-metallic materials. Most of the time the default value should be used (which corresponds to the standard 4% reflected light at normal angle), but can be increased to boost reflections and highlights in a characters eyes, for example. It requires the PBR shading mode.

### ![](/icons/culling.webp) Inverse culling {#inverse-culling}
Reverse the normals of a surface. Usually not required, but can be used if a model appears inside out, or in combination with `Two-sided` disabled, can be used to make interiors where the wall nearest the camera is always hidden.

The following options can be set to `Auto`, `No` or `Yes`. With `Auto`, the arrow shows the value that is actually used.

### ![](/icons/sphere_smooth.webp) Smooth shading {#smooth-shading}
See the [global option](settings.md#smooth-shading).  
`Auto` value will use the global option.

### ![](/icons/culling.webp) Two-sided {#two-sided}
Faces will be visible from both sides. See the [global option](settings.md#two-sided-quick).  
`Auto` value will use the global option.

### ![](/icons/culling.webp) Colored backface {#coloured-backface}
See the [global option](settings.md#two-sided-quick).
`Auto` value will use the global option.

### ![](/icons/shadow_cast.webp) Cast shadows {#casts-shadows}
Transparent objects also cast shadows (in a dithering pattern to emulate blended shadows).  
Make sure to disable shadow casting if you have a big object in your scene that doesn't need to cast shadows (for example a big floor).

### ![](/icons/shadow_receive.webp) Receive shadows {#recieve-shadows}
Whether shadows from other objects are drawn on this object.

### ![](/icons/wireframe.webp) Wireframe {#wireframe}
See the [global option](settings.md#wireframe).  
`Auto` value will use the global option.

### ![](/icons/trash.webp) Reset normals {#reset-normals}
Only shown when an imported object carries its own normals (for example with `Keep topology`). It removes them, so the shading uses the normals computed from the surface.


## Textures {#textures}

![](/images/material_textures.webp)

If an object has UVs, then textures can be applied to the material in addition to the vertex color/roughness/metalness/opacity. Usually these are the result of a texture bake, but images created outside of Nomad can also be used. `UV:✓` or `UV:✗` next to the title tells you whether the object has UVs.

Textures can be applied to

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Displacement
* Emissive

An `Occlusion` row also appears when an imported object has an occlusion texture, but Nomad doesn't use it.

The slider of each row sets how strongly its texture is applied, from not at all to fully. `Color` and `Emissive` also have a color swatch that tints the texture, and `Emissive` sets the glow strength.

`Displacement` sets how far the displacement map pushes the surface. Its `Apply` button moves the vertices by the displacement, then removes the map. The result goes into the active layer.

The palette button next to the title opens the material presets of the [painting](painting.md) menu: tap one to copy its textures onto the object. On desktop, imported images sync with their original file when you switch back to Nomad, and a sync button next to the title reloads them.

Clicking on a texture slot will bring up a selector. After a texture has been assigned to a material slot, clicking again will bring up a texture panel:

### Texture panel options {#texture-panel-options}

![](/images/material_texture_panel.webp)

The panel shows the image size and a preview of the texture.

### ![](/icons/open.webp) Open {#open}
Select another texture. On desktop, `Explore` shows the image file in your file browser.

### ![](/icons/circle_cross.webp) None {#none}
Remove the texture

### Opacity {#texture-opacity}

Color texture only. If the image has an alpha channel, this will allow you to use it for Opacity, or to ignore it.

### Format {#normal-format}
Normal texture only. Normal maps come in two flavors, `OpenGL (+Y)` and `DirectX (-Y)`. If the details look inverted, try the other one.

### Height {#displacement-height}
Displacement texture only.
* `Local` - The height grows and shrinks with the object scale.
* `World` - The height stays the same whatever the object scale.

### Multiply {#multiply}
Roughness, metalness and opacity textures only. Multiply the values of the texture. When it isn't 100%, the value is shown on the texture slot.

### ![](/icons/link.webp) Chain/Link icon {#chainlink-icon}

The link icon in the following sections, when enabled, will mean whatever options are used, will be shared with the other textures (color, normal, roughness, metalness, opacity, emissive) that also have their link icon enabled. 

This allows you to ensure if you have aligned textures, they will stay aligned even you alter parameters or projection types.


### Projection {#projection}
![](/images/material_projection.webp)

Set how the texture should be applied to the object.

* `Auto` - If the object has uv's, UV, otherwise Triplanar
* `UV` - Use the uv coordinates of the mesh to apply the texture. If the mesh and texture come from outside of Nomad, or are going to be exported from Nomad to use elsewhere, UV is the correct option.
* `Triplanar` - Project the texture along the X,Y,Z axis', and blend the seams. 

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Triplanar projections are a powerful yet simple way to apply textures to objects.

Triplanar is like having 6 video projectors all with the same image, shining onto the front, back, left, right, top and bottom of your object.

This can then be baked into UVs or vertex colors if needed.


![](/images/material_triplanar_example.webp)

#### Method {#method}

* `Local` - The projection will move with the object transform
* `World` - The projections stays fixed, moving the object will slide it through the projection.

#### Hardness {#hardness}

How the projections mix. 100% will do no blending, and the edges of the projections will be sharp. 0% will blend the edges over a wide angle. The default is 90%, enough mixing to hide the edges, and let the rest of the projections stay sharp.

### Uniform {#uniform}

When ticked, the same hardness is used for all projections. When unticked, extra hardness controls are exposed for X, Y, Z projections.


### Parameter {#parameter}
![](/images/material_parameter.webp)

#### Filtering {#filtering}
The texture filter method to use, `Auto` is the default, methods are `Nearest`, `Linear`, `Mipmap`. Nearest does no filtering, so textures can get jagged artifacts when viewed up close. Linear and Mipmap do better filtering, so textures appear blurred rather than jagged up close.

#### Tiling - X {#tiling-x}
If the Scale parameter is greater than 1, making the texture smaller than the object UVs, how will the texture be tiled along the X axis. `None` means no repeats. `Repeat` will do copies of the texture. `Mirror` will do copies of the texture, with every second copy reversed, which can help hide tiling artifacts.

#### Tiling - Y {#tiling-y}
Same as Tiling - X, but for the Y axis.

### Transform {#transform}
![](/images/material_transform.webp)

Extra 2d transformations applied to the texture in UV space. The reset button resets to defaults, the chain icon (when textures other than color are selected) will link or unlink the transform to be the same as the color texture.

#### Translation {#translation}
The X and Y offset of the texture

#### Rotation {#rotation}
The rotation of the texture

#### Scale {#scale}
The scale of the texture, bigger numbers will make the texture smaller on the object, use the Tiling - X and Tiling - Y options to control what happens.

### Uniform scale {#uniform-scale}
When turned off Nomad will show separate controls for Scale-X and Scale-Y.
