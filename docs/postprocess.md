# ![](/icons/postprocess.webp) Post process {#post-process}

This menu controls many aspects of Nomad to affect the look of the render.

![](/images/postprocess_overview_drac.webp)

Using post processing can substantially change the final look of your scene.

![](/images/postprocess_overview.webp)
*The same scene before and after post processing, no additional lights or material changes.*

Post process can impact the performance by a lot depending on your device.
There's a global `Post Process` checkbox to disable all the postprocess, so that you can quickly go back to sculpting/modeling without losing your presets.
For PBR rendering, [Ambient Occlusion](#ambient-occlusion-ssao), [Reflection](#reflection-ssr) and [Tone Mapping](#tone-mapping) should be enabled.

However, most of the time you want the post process to be disabled when you are sculpting, to focus on the shape itself of the rendering.


## Quality {#quality}

![](/images/postprocess_quality.webp)

These options improve the quality of the render, at the cost of performance.

### Max frame sampling {#max-frame-sampling}
Nomad will calculate a certain amount of post processing for a single frame render, which can look noisy. This control determines how many frames will be rendered, then blended together to remove most noisy artifacts. Some effects require no extra samples (eg color grading), while others like soft shadows and global illumination can require hundreds of samples to be noise free. 

In the viewport this can be seen whenever nomad is left alone, the image quality will gradually refine up to the max samples, then stop. Once it stops, Nomad does nothing, which saves battery. This number of calculations is also used in the render section of the [Files menu](files) when 'export png' is clicked.

The checkbox next to the slider turns frame sampling on or off.

### Render resolution {#resolution-multiplier}
This slider controls the resolution of the render. A value of x1.0 will mean the render's are done at the pixel resolution of the device. A value of x0.5 will render at half resolution, which will be fast but low quality. A value greater than 1 will render at a bigger size, then scale down. This result in higher quality, less noise, but longer render times.

It has a major impact on performance, so try to keep it at x1.25 or below. This value isn't saved in the settings, and the [Pixel Art](#pixel-art) effect overrides it.

### ![](/icons/intensity.webp) Max samples {#max-samples}

Improves the quality of the post process effects, at the cost of performance.

### ![](/icons/material_dithering.webp) Dithering {#dithering}

Dither pixels to reduce banding artifacts (in gradients or vignette for example). Usually this should be enabled, but can be turned off for specific operations (eg exporting depth maps or other data specific operations).

### ![](/icons/denoise.webp) Denoiser (oidn) {#oidn}

Apply a denoiser to the image once all the frames are accumulated. This can allow you to use much lower samples. Denoising is processor intensive, so only enable it if your image is noisy. It is not available on every device.

## Preset browser {#preset-browser}
![](/images/postprocess_presets.webp)
Clicking on the image below the `Post Process` title will display a collection of post processing presets. Use `New` to create a preset from your current settings. The built-in presets can only be cloned: to define your own, select one, click `Clone`, and make changes. When a preset has changes that aren't saved yet, it shows `Unsaved changes!`; to save, click the preset image, click again inside the preset browser, and choose `Save`.

## Shortcut bar {#shortcut-bar}
When the post process is enabled, a bar at the bottom of the menu lists every effect (`SSR`, `SSGI`, `SSAO`, `DoF`, `Bloom`...). Tap one to jump to its section. Effects that are turned off are greyed out, so the bar is also a quick summary of what the current preset does.

## ![](/icons/postprocess_ssr.webp) Reflection (SSR) {#reflection-ssr}
With this option, objects can reflect other objects in the scene, as long as the objects are visible on the screen.
If you have metallic and shiny objects in your scene, then this option should probably be used.
This option requires the [Lit (PBR)](shading.md#pbr) shading mode.


| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Global Illumination (SSGI) {#global-illumination-ssgi}

Global illumination simulates how light bounces between surfaces, eg a red wall will cast red onto a nearby white object. This can hugely enhance the realism of a render when used with ambient occlusion and reflections. Like reflections, it requires the [Lit (PBR)](shading.md#pbr) shading mode.

`Strength` - The intensity of the global illumination. 



| SSGI off                   | SSGI on                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_A spotlight is behind the sphere, aimed at the ceiling. With SSGI off, only the ceiling is lit. WIth SSGI on, light bounces from the ceiling to the walls to the sphere._

## ![](/icons/postprocess_ssao.webp) Ambient Occlusion (SSAO) {#ambient-occlusion-ssao}
Ambient occlusion will darken areas where the light has less chance of reaching (corners, etc).
The effect only depends on the model geometry.

* `Strength`- Intensity of the effect.
* `Size`- How widespread the effect is.
* `Thickness` - How much depth thickness is assumed for occluders, as a percentage of the `Size`.
* `Tint` - A color multiplied into the occlusion, used for creative effects.


| SSAO off                    | SSAO on                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO will be most visible in areas lit mainly by environment light. Areas that are under strong direct light will receive a much weaker AO effect.

:::

## ![](/icons/postprocess_dof.webp) Depth Of Field {#depth-of-field-dof}
Add a blur effect on the region that is outside the focus.

Simply tap on your model to change the focus point.

* `Aperture mode` - Drive the blur with a single camera aperture, instead of the two blur sliders below.
* `Aperture` (_aperture mode only_) - The f-number of the lens, like on a real camera. A lower value opens the lens and blurs more.
* `Far blur` - The amount of blurring to be applied on the far side of the focus point.
* `Near blur` - The amount of blurring to be applied between the focus point and the camera.


| DOF off                   | DOF focus on far ring       | DOF focus on close ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Bloom {#bloom}
Blooms will make the bright area of your scene glow.

* `Intensity` - strength of the effect.
* `Radius` - The spread of the effect.
* `Threshold` - How bright pixels have to be in the scene before they start to bloom. At 0 everything blooms, setting it high will allow only the brightest pixels to bloom.
* `Tint` - a color that can be added to bloom for creative effects.

| Bloom off                    | Bloom with radius 0         | Bloom with radius 1         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Tone Mapping {#tone-mapping}
Tone Mapping is an operation that will remap HDR values to the `[0, 1]` range.
If you don't use it (or select `None`), any color component higher than 1 will be clipped.
Any color variations above this range will then be lost.

* `None/Neutral/Agx/ACES` - which tonemapper to use. `None` does no remapping (but the other controls still work). The other options are similar to choosing different film stock, they will deal with overexposed values and colours in different ways. This is a very deep topic, lookup tone mapping, Agx, ACES for more info!
* `Exposure` - overall brightness of the images, similar to adjusting aperture on a camera. This can be a quick way to globally brighten or darken an image.
* `Saturation` - color strength. 1 is neutral, 0 is monochrome, values above 1 are increasingly saturated.
* `Contrast` - Make darks darker and lights lighter. Use carefully, it can introduce artifacts at high values.

Notice that with `Tone Mapping` disabled, some details disappear because the pixels are too bright.

| Tone Mapping off            | Tone Mapping on            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Tone mapping can enhance the effect of global illumination. If you turn the instensity of the environment map down, the primary light source up, can increase the tone mapping `Exposure` to see more of the bounce lighting effects.
:::

## ![](/icons/postprocess_tone_curve.webp) Color Grading {#color-grading}
Similar to the curves tool in Photoshop, this allows you to control the balance and distribution of color in the image. The `Main` control affects the entire color balance, the `Red`/`Green`/`Blue` controls allow for fine control. 

| Color Grading off             | Color Grading on             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Curvature {#curvature}
Detect where there are rapid changes in curvature, and apply a colour to those regions.

* `Factor` - overall intensity of the effect
* `Bump` - how much it will find sharp convex changes, and place the selected colour there (white by default)
* `Cavity` - how much it will detect concave changes, and place the selected colour there (black by default)
* `Thickness` - how wide the detected edges are.

Next to `Bump` and `Cavity`, a color swatch picks the color, and a small button picks how that color blends with the image.


| Curvature off                    | Curvature on                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Chromatic Aberration {#chromatic-aberration}
Simulate the lens artifacts with light being decomposed around the screen edges.

* `Strength` - how much the red/green/blue parts of the image get split towards the screen edges

| Chromatic off                 | Chromatic on                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Vignette {#vignette}
Simulate the lens artifacts by darkening the screen edges.

* `Size` - The size of a inverted ellipse placed over the image
* `Hardness` - How blurry or sharp the ellipse is mixed on top of the image.
* `Tint` - The color of the vignette, black by default.


| Vignette off                    | Vignette on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Grain {#grain}
Add a grain effect, it can help make the image a bit less artificial.

* `Strength` - the amount of grain/noise added to the image.


| Grain off                    | Grain on                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Sharpness {#sharpness}
A sharpen effect similar to that in Photoshop or photo processing apps.

* `Strength` - the amount of sharpening applied to the image.


| Sharpness off                  | Sharpness on                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Pixel Art {#pixel-art}
Simulate retro game pixel art. This effect overrides the [Render resolution](#resolution-multiplier).

* `Slider` - size of the pixels
* `Allow frame sampling` - if you get lots of black pixels, try turning this on. Without it, the pixel art effect turns off [frame sampling](#max-frame-sampling).

| Pixel off                   | Pixel on                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Scanline {#scanline}
Simulate the look of old CRT monitors.

* `Factor` - strength of the lines
* `Spacing` - size of the lines

| Scanline off                   | Scanline on                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |
