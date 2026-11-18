# ![](/icons/sun.webp) Shading {#shading}

This menu controls the shading modes used by Nomad, lighting properties, the environment and matcap, and the fog.

![](/images/shading_overview.webp)



You can choose between several rendering modes:

| Mode                        | Meaning                    | Description                                                     |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Lit (PBR)](#pbr)           | Physically Based Rendering | Lights, shadows, environment, and painted metalness/roughness   |
| [MatCap](#matcap)           | Material Capture           | Fast mode for sculpting, with lower gpu/cpu use than PBR        |
| [Unlit](#unlit)             | Surface Color              | Surface color only with no shading or lighting                  |
| [Object ID](#object-id)     | Object ID                  | A random color per object, useful for painting applications.    |
| [Instance ID](#instance-id) | Instance ID                | A random color per instance, useful to identify shared meshes   |

If you want to learn more about metalness and roughness, see the [Vertex Paint](painting.md) section.

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) Face Group {#face-group}
Overlay facegroup colours. Facegroups are coloured selections of polygons that can be created with the [Face group](tools#facegroup) tool, and are made automatically with most of the primitives.

Some tools will automatically filter by facegroups when facegroups are visible.

### ![](/icons/palette.webp) Show paint {#show-paint}
Nomad can store color, roughness, metalness in the verticies of your sculpt. You can toggle the display of these properties globally with this checkbox.

Note that if you have both vertex properties and textures, and both are enabled, the values will be multiplied together.

### ![](/icons/shield.webp) Show mask {#show-mask}
Toggle the grayscale mask overlay of the [mask tools](tools#mask). When this is disabled, the mask is also disabled, useful for making quick changes without the mask, then you can enable it again and not lose your mask.

### ![](/icons/tool_hide.webp) Use Hide {#use-hide}

Toggle hidden faces. Note this only works if you are NOT in the hide tool!

### ![](/icons/image.webp) Use textures {#use-textures}

Nomad allows for textures to be assigned to objects from the [material](material) menu. If textures are assigned they be toggled globally with this checkbox.

You can't create or edit textures inside Nomad, but textures from imported files work. Opacity textures work in Lit, MatCap and Unlit, normal maps in Lit and MatCap, color in Lit and Unlit, and emissive, roughness and metalness in Lit only. The button is greyed out when the scene has no texture.

### PBR and lights overview {#pbr}
This manual won't dive into the details about Physically Based Rendering.

One important thing to keep in mind is that lighting and material are fully separated.
It means you can paint your object color, roughness and metalness while the lighting is handled independently.
It allows you to paint your object and then tweak the lighting later, without breaking the overall look of your model.

Lights, the environment and the fog are only available with [PBR mode](#pbr).
For performance reasons, you are limited to 4 lights on mobile and 6 on desktop.

::: tip
You can load a glTF file with more lights in it and Nomad will keep all of them.
However it won't necessarily perform well.
:::

::: tip
You can fake many lights by making objects unlit/emissive, then enable global illumination in the [post process](postprocess) menu.
:::

### Light types overview {#light-types-overview}

Here are the type of lights currently supported:

| Mode                        | Description                                             | Can cast shadows |
| :-------------------------: | :-----------------------------------------------------: | :--------------: |
| [Directional](#directional) | Infinitely far away sun light                           | Yes              |
| [Environment](#env-light)   | A distant light that is matched to the environment HDR  | Yes              |
| [Spot](#spot)               | Cone shaped lights                                      | Yes              |
| [Point](#point)             | Omni-directional point of light                         | Yes              |

#### ![](/icons/sun.webp) Directional {#directional}
It emits light from infinitely far away, with a uniform intensity.
It's 3d position in the scene doesn't matter, only its orientation does.

You can attach this light to the camera, that way it has consistent lighting.  
For example you can use it to make a rim light (a strong light that emits from the back of your model, pointing towards the camera) that always lights the back of your model.

#### ![](/icons/panorama.webp) Environment light {#env-light}
Using a [environment hdr](#environment) works well for overall soft lighting, but if there is a strong sharp light visible in the HDR, the shadow created by it will be very soft, often not visible at all. Using a directional light in combination with the environment HDR can help, but it can be difficult to get them aligned.

This light does the work for you. The light will automatically be rotated to align with the brightest part of the HDR, then you can control its intensity and angle (shadow softness) separately. 

#### ![](/icons/spotlight.webp) Spot {#spot}
Spot light emits light in a single direction, restricted by a cone shape.

#### ![](/icons/light.webp) Point {#point}
Point light will emit light in every direction, and it can cast shadows too.

#### Shadows {#shadows}
Each light can cast shadows, and you can pick how they are computed in its [settings](#light-extra-controls). If you see shadow artifacts, the `Tolerance` sliders there can help.

The quality of the shadows depends on the size of the objects relative to the entire scene.  
If you have a big object in your scene that doesn't need to cast shadows (for example a big plane), make sure to disable shadow casting in its [material settings](material.md#casts-shadows).

## ![](/icons/sun.webp) Lights {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Lights checkbox {#lights-checkbox}

Toggle all the direct lights in the scene.



### Add light {#add-light}

Add a light to the scene, up to 4 lights on mobile and 6 on desktop. When a light is added, the light list is displayed with buttons, and a light toolbar is added to the top of the viewport.

![](/images/shading_lights_icons.webp)

* The text shows the name of the light and the brightness. Tap it to select the light.
* The eye icon toggles visibility.
* The pencil icon allows you to rename the light.
* The trash icon will delete a light.
* The copy icon will duplicate a light. 
* The 3 dots icon will bring up a full light editor. Most of this functionality is also available from the toolbar that appears in the viewport. 

You can also drag a light in the list to reorder it.

### ![](/icons/spotlight.webp)  Icons {#icons}

Toggle the display of light icons in the viewport

### Light toolbar {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

This toolbar will appear at the top of the viewport when a light is selected.

* `Visible` will toggle the light visibility.
* Directional/Environment/Spot/Point will change the light type. Tap to cycle, or long press to see a menu.
* Intensity controls light strength, value can go above 1.0 for very intense lights, useful when used with Global Illumination in Post Process
* The color swatch when clicked will bring up a color selector. Nomad offers several ways to choose color. Kelvin control offers a natural way to select warm/cool lighting.
* Shadow will toggle shadows.
* Angle (_directional and environment_) or Size (_spot and point_) sets the width of a light. Wider lights will cast soft shadows, soft lighting, and a softer highlight on objects.
* Attachment (_directional only_), Cone angle and Softness (_spot only_) are described in the [light editor](#light-extra-controls) below.
* ... will bring up `Clone`, `Recenter` and `Delete`, along with the shadow settings.

### Light extra controls {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

The 3 dots icon of a light in the list opens its full editor. Note that some options are specific to certain light types.

* `Directional/Environment/Spot/Point` allow you to change the light type.
* The `colour swatch` when clicked will bring up a color selector. 
* `Intensity` controls light strength.
* `Attachment` (_directional only_) will set the light to be parented to the world (`Fixed`), or to be parented to the camera (`Camera`). Eg if you use a directional light behind your character as a rim light, when attachment as camera is selected, rotating the camera will always have the light behind the character.
* `Softness` (_spotlight only_) controls the sharpness of the edge of the spotlight cone. 0 is a very sharp edge. 1 is very soft, with a gradient to the center of the light cone. In the viewport, the small blue dot on the spotlight cone can be used to set softness interactively.
* `Cone angle` (_spotlight only_) controls the spread angle of the spotlight. A small angle is a very thin beam of light, 170 is a very wide spread of light. In the viewport, the orange dot can be used to set the cone angle interactively.
* `Angle` (_directional and environment only_) is the apparent size of the light, think of it as how big the sun appears in the sky. Bigger angles will cast softer shadows and wider highlights.
* `Size` (_spot and point only_) is the width of the light. Bigger lights cast softer shadows.
* `Shadow` will toggle shadows for the current light.
* The shadow type picks how shadows are calculated. A `Shadow map` renders the scene from the light, so it also shadows geometry the camera can't see. `Screenspace` only uses what is already visible on screen: it's cheaper, but experimental. Generally the shadow map is more reliable.
* `Tolerance` (_screenspace only_): if shadow artifacts are visible (either shadows don't appear to contact surfaces, or there's noise and patterns within shadows), adjusting tolerance can help fix those issues.
* `Contact` adds more precise shadows over short distances, where objects touch. With `Auto`, only the most dominant light in the scene gets contact shadows; `No` and `Yes` force it off or on for this light. Its `Tolerance` slider works like the one above.

The `...` button of the viewport toolbar holds the same shadow settings, plus:

* `Clone` will duplicate the light.
* `Recenter` will move the light in front of the camera, keeping its orientation.
* `Delete` will delete the light.


## ![](/icons/panorama.webp) Environment {#environment}

![](/images/shading_environment.webp)

Light in the real world comes from all directions; the blue of the sky, the green of the grass, the red of a building, all this light from the 'environment' can be simulated with an environment map. 

Use the checkbox next to the title to turn the environment lighting on or off.

Nomad comes with several example environment maps for indoor and outdoor areas, with different tints and brightness levels. Try different maps to see which brings out the most detail in your sculpts.

Tap on the image to see the available environment maps. From that dialog choose `Import...` to load your own. It's best to use High Dynamic Range (HDR) images, in the latlong or equirectangular format, as either .hdr or .exr files. The browser can also download environments straight from [Poly Haven](https://polyhaven.com/hdris), which has a good collection of free environment maps.

### Exposure {#env-exposure}
Adjust the brightness of the environment map. Often the maps can be too bright when used with regular lights, turning the exposure down can help balance, especially when used with Global Illumination in the [Post Process](postprocess) settings.

### Rotation {#env-rotation}

Becaue environment maps capture light from all directions, you can rotate them to get the reflections and overall lighting to combine well with your sculpt. You can also rotate the environment by dragging 3 fingers horizontally on the viewport.

### Attached to camera {#env-attached}
Attach the environment to the camera.

It will force the lighting to be consistent, which can be useful during sculpting.

### Blur (background) {#env-background-blur}
This slider only shows when the [background](background.md) is set to the environment. It blurs the environment image behind your model, without changing the lighting.


## ![](/icons/fog.webp) Fog {#fog}

Fog adds atmospheric depth to your scene and makes light beams visible. Enable it with the checkbox next to the title. Like lights and the environment, it is only available in [Lit (PBR)](#pbr) mode.

::: tip Stronger light beams
Lower the fog `Environment`, and use a bright spot or point light. Increase `Density` until the fog is clearly visible. For visible beams in thinner fog, set `Scattering Direction` to a high positive value and aim the camera toward the light.
:::

### Color {#fog-color}
The color of the fog and of the light it scatters.

### Density {#fog-density}
How quickly the fog thickens with distance.

### Max Opacity {#fog-opacity}
Limits how much the fog can cover the scene, even at high density.

### Scattering Direction {#fog-scattering}
The direction in which the fog scatters light (also called anisotropy). Positive values brighten the fog when you look toward a light, negative values when you look away, and zero scatters light evenly in every direction.

### ![](/icons/panorama.webp) Environment {#fog-environment}
How much the [environment](#environment) lights the fog. It is greyed out when the environment is turned off.

### Noise {#fog-noise}
Mixes noise into the fog to break it into patches, without changing its overall density. When noise is above 0, a `Size` slider sets the size of the pattern.

### Shape {#fog-shape}
Where the fog fills the scene:

* `Uniform` - fills the whole scene.
* `Vertical` - keeps the fog inside a vertical band with soft edges. The `Bottom` and `Top` sliders set the height of its lower and upper edges, and their eye button shows the band in the viewport while you adjust them.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

As the name suggests (MATerial CAPture), a matcap takes care of both the lighting and material information in a single image.
Since the material itself is already present in the matcap, roughness and metalness painting channel will be ignored.
The painting color will be multiplied against the matcap, meaning if you have a black/gray matcap, using white paint won't make it brighter.

Artists tend to favor this mode for sculpting purposes since they allow them to focus on the shape and geometry itself.

Tapping on the sphere will bring up an image browser. You can also add your own matcap, generally any photo, render, even a painting of a sphere that has been cropped tightly into a square can be used. Many matcap libraries are available online, a useful resource is the [nidorx matcap library](https://github.com/nidorx/matcaps).

### Use global MatCap {#matcap-global}

Usually artists will use a single matcap for the entire sculpt, but if this toggle is disabled, the selected object can have its own matcap. This can be used artistically to get striking results.

::: tip
Disable this option, and use an image of an eyeball for your characters eyes!
:::

### Rotation {#matcap-rotation}
A matcap is a specialised form of an environment map, so like an environment map, it can be rotated. You can also do this at any time in the viewport by dragging with 3 fingers left and right.

The lock button next to the slider locks the rotation, so a 3 fingers drag won't turn the matcap by accident.



## ![](/icons/circle_fill.webp) Unlit {#unlit}

This mode will only show the surface color. It can be useful for checking the surface color of your objects are what you expect, without being distracted by lights, shadows, reflecton, transparency. 

This mode can also be used for non-photoreal renders, achieving a flat, cartoony look.

## ![](/icons/cube.webp) Object ID {#object-id}

All lighting and surface information is ignored, and each object is shaded with a unique flat color. If this is rendered alongside a PBR render, this can be used in a painting program to select by color, and thus be able to do color corrections on specific objects.

Note that these colors will also appear in the [Scene menu tree view](scene#tree-view).

### Randomize id {#object-random}

Generate a new set of random colors. 

## ![](/icons/link.webp) Instance ID {#instance-id}

Same as Object ID, but instances will have the same color. 

### Randomize id {#instance-random}

Generate a new set of random colors. 
