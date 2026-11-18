# ![](/icons/image.webp) Background {#background}

This menu controls the background color of Nomad, as well as any reference images to be used.

![](/images/background_overview.webp)

## Type {#type}
![](/images/background_selector.webp)

There are three options for the viewport background.

* `Environment` - Show the environment map selected in [Shading](shading.md). This can be further controlled with the `Blur` and `Exposure` (brightness) sliders. 
* `Color` - A flat color that you can choose
* `Gradient` - A ramp between two colors. The `Factor` slider lets you move the midpoint of the gradient.  

### Gradient type {#gradient-type}
With `Gradient`, choose its shape:
* `Linear` - A straight gradient, its direction is set by the `Angle` slider.
* `Radial` - A circular gradient starting from the center of the screen.
* `Sky` - A gradient anchored to the world horizon, so it follows the camera as you look up and down.

Each color has a reset button and a color picker, to pick a color from the screen.

## ![](/icons/lock.webp) Sync on camera lock {#sync-on-camera-lock}
When the camera is locked with the [Snap cube](settings.md#snap-cube), the reference image follows the camera movement, so it stays lined up with your sculpt.

* `Allow roll (trackball)` - Allow the camera to roll when you leave the camera lock.
* `Reset view on unlock` - Reset the view when you leave the camera lock.

## Reference Image {#reference}

![](/images/background_reference.webp)

You can add an image of your choice on the background to be used for reference. Tap `Import...` to add one, then tick `Reference image` to show it.
You can change the position and scale, for example if you want to move it to the screen corner.

### ![](/icons/tool_transform.webp) Transform {#transform}

This button will let you place the reference image interactively. Use 2 fingers to pan, scale, rotate the reference image into place. `Reset settings` puts the image back to its default placement. The final placement will be reflected in the sliders below:

* `Overlay` - at 0% the reference image will always be behind your objects, at 100% it is in front. 
* `Opacity` - How transparent the image is.
* `Post process` - Apply the post process effects on the reference image. Disable it to keep the original colors.
* `Position X` / `Position Y` - The X and Y position of the image.
* `Scale` - Image scale.
* `Rotation` - Image rotation.


::: tip

Cameras and reference images are linked. 

This means if you setup your reference image to line up with your sculpt, if you create a camera from the [Camera menu](camera.md), the reference image position, rotation, scale are also stored with the camera. You can turn off the reference image, rotate to another viewport. If you look through the camera again, the reference image will be activated with the settings you used.

This even includes choosing different images for different cameras!

 ![](/videos/reference_camera.mp4)

:::
