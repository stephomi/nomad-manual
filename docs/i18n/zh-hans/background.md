# ![](/icons/image.webp) 背景 {#background}

此菜单用于控制 Nomad 的背景颜色，以及要使用的任何参考图像。

![](/images/background_overview.webp)

## 背景 {#type}
![](/images/background_selector.webp)

视口背景有三种选项。

* `Environment` - 显示在 [Shading](shading) 中选择的环境贴图。可以通过 Blur 和 Exposure（亮度）进行进一步控制。
* `Color` - 由你选择的一种纯色
* `Gradient` - 从上到下的颜色渐变。Factor 滑块可让你决定渐变的中点位置。  

## 参考图像 {#reference}

![](/images/background_reference.webp)

你可以在背景中添加任意图像作为参考使用。
你可以更改其位置和缩放，例如将其移动到屏幕角落。

### ![](/icons/tool_transform.webp) 变换 {#transform}

此按钮允许你以交互方式放置参考图像。使用两根手指平移、缩放、旋转参考图像到合适位置。最终的位置会反映在下面的滑块中：

* `Overlay` - 在 0% 时参考图像始终在物体后面，在 100% 时则在物体前面。 
* `Opacity` - 图像的透明度。
* `Position` - 图像的 X 和 Y 位置。
* `Rotation` - 图像旋转。
* `Scale` - 图像缩放。


::: tip

相机和参考图像是关联的。 

这意味着，如果你将参考图像对齐到你的雕塑上，当你在 [Camera 菜单](camera) 中创建一个相机时，参考图像的位置、旋转和缩放也会与该相机一起保存。你可以关闭参考图像，旋转到其他视图；当你再次通过该相机查看时，参考图像会以你之前设置的参数重新激活。

这甚至包括为不同相机选择不同的参考图像！

 ![](/videos/reference_camera.mp4)

:::