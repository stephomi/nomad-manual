# ![](/icons/postprocess.webp) 后期处理 {#post-process}

此菜单控制 Nomad 中影响最终渲染效果的诸多选项。

![](/images/postprocess_overview_drac.webp)

使用后期处理可以大幅改变场景的最终观感。

![](/images/postprocess_overview.webp)
*同一场景在开启与关闭后期处理时的对比，没有增加灯光或修改材质。*

后期处理会对性能产生较大影响，具体取决于你的设备性能。  
有一个全局复选框可以一次性禁用所有后期处理，这样你可以快速回到雕刻/建模状态，而不会丢失预设。  
对于 PBR 渲染，[环境光遮蔽](#ambient-occlusion-ssao)、[反射](#reflection-ssr) 和 [色调映射](#tone-mapping) 应当启用。

不过，大多数情况下在雕刻时你会希望关闭后期处理，以便专注于形体本身而不是渲染效果。


## 质量 {#quality}

![](/images/postprocess_quality.webp)
### 最大帧采样 {#max-frame-sampling}
Nomad 会对单帧渲染计算一定数量的后期处理，这在初始时可能会显得有些噪点。该选项决定要渲染多少帧并将其混合，以消除大部分噪点伪影。某些效果不需要额外采样（例如色彩分级），而像全局光照这样的效果可能需要数百个采样才能无噪点。

在视图中，当你停止操作时可以看到这一点：图像质量会逐渐细化，直到达到最大采样数后停止。这个计算次数同样用于 [文件菜单](files) 的渲染部分，当点击“export png”时会使用。

### 分辨率倍率 {#resolution-multiplier}
此滑块控制后期处理的分辨率。  
值为 x1.0 表示按设备的像素分辨率进行渲染。  
值为 x0.5 表示以一半分辨率渲染，速度快但质量低。  
大于 1 的值会以更高分辨率渲染再缩小，这会带来更高质量、更少噪点，但渲染时间更长。

### 最大采样数 {#max-samples}

提高后期处理的质量，但通常 `Full resolution` 的影响更大。 

### 去噪器（oidn） {#oidn}

对图像应用降噪，这可以让你使用更低的采样数。仅在启用 `Full Resolution` 时有效。注意降噪是在所有采样计算完成后进行的，可能会比较耗费处理器资源。

## 预设浏览器 {#preset-browser}
![](/images/postprocess_presets.webp)
点击图像会显示一组后期处理预设。要定义自己的预设：先选择一个，点击“clone（克隆）”，再进行修改。要保存时，点击预设图像，再在预设浏览器中点击一次，然后选择“save（保存）”。


## 反射（SSR） {#reflection-ssr}

启用该选项后，物体可以反射场景中其他物体，只要这些物体在屏幕上可见。  
如果场景中有金属或高光物体，通常应启用此选项。  
此选项仅在 PBR 模式下有效。


| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## 全局光照（SSGI） {#global-illumination-ssgi}

全局光照模拟光线在表面之间的反弹，例如红色墙面会将红色反射到附近的白色物体上。与环境光遮蔽和反射配合使用时，可以极大提升渲染的真实感。 

`Strength` - 全局光照的强度。 



| SSGI off                   | SSGI on                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_一个聚光灯位于球体后方，指向天花板。关闭 SSGI 时，只有天花板被照亮。开启 SSGI 时，光线从天花板反弹到墙面再到球体。_

## 环境遮蔽（SSAO） {#ambient-occlusion-ssao}

环境光遮蔽会使光线不易到达的区域（如角落等）变暗。  
该效果只依赖模型几何形状。

* `Strength` - 效果强度。
* `Size` - 效果影响范围。
* `Curvature bias` - 相对于表面变化的敏感度。
* `Color` - 乘入遮蔽效果的色彩，用于创意效果。


| SSAO off                    | SSAO on                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO 在主要由环境光照亮的区域最为明显。处于强烈直射光下的区域会获得更弱的 AO 效果。

:::

## 景深（DOF） {#depth-of-field-dof}

对焦点以外的区域添加模糊效果。

轻点模型即可改变对焦点。

* `Far blur` - 焦点之后（远处）区域的模糊程度。
* `Near blur` - 焦点与相机之间（近处）区域的模糊程度。


| DOF off                   | DOF focus on far ring       | DOF focus on close ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## 泛光 {#bloom}

Bloom 会让场景中明亮区域产生发光效果。

* `Intensity` - 效果强度。
* `Radius` - 效果扩散范围。
* `Threshold` - 像素在开始产生辉光前需要达到的亮度。值低时几乎所有东西都会发光，值高时只有最亮的像素会发光。
* `Color` - 可添加到辉光中的色彩，用于创意效果。

| Bloom off                    | Bloom with radius 0         | Bloom with radius 1         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## 色调映射 {#tone-mapping}

色调映射会将 HDR 数值重新映射到 `[0, 1]` 范围。  
如果不使用（或选择 `none`），任何大于 1 的颜色分量都会被裁剪，超出该范围的色彩变化将会丢失。

* `None/Neutral/Agx/ACES` - 选择使用哪种色调映射器。`None` 不做重新映射（但其他控制仍然生效）。其他选项类似于选择不同的胶片，它们会以不同方式处理过曝的亮度和颜色。这是一个非常深入的话题，可搜索 tone mapping、Agx、ACES 了解更多信息。
* `Exposure` - 图像整体亮度，类似相机光圈调节。是快速整体提亮或压暗图像的方式。
* `Saturation` - 色彩饱和度。1 为中性，0 为黑白，大于 1 时饱和度逐渐增强。
* `Contrast` - 提升明暗对比，让暗部更暗、亮部更亮。需谨慎使用，过高会引入伪影。

注意在关闭 `Tone Mapping` 时，一些细节会因为像素过亮而消失。

| Tone Mapping off            | Tone Mapping on            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
色调映射可以增强全局光照的效果。如果降低环境贴图强度、提高主光源强度，再增加色调映射的 `exposure`，可以更好地看到反弹光效果。
:::

## 颜色分级 {#color-grading}

类似 Photoshop 中的曲线工具，它允许你控制图像中的色彩平衡与分布。`main` 控制整体色彩平衡，`red`/`green`/`blue` 控制则用于精细调整。 

| Color Grading off             | Color Grading on             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## 曲率 {#curvature}

检测曲率变化剧烈的区域，并在这些区域上应用颜色。

* `Factor` - 效果整体强度
* `Bump` - 检测凸起（凸面）锐利变化的程度，并在这些区域应用所选颜色（默认白色）
* `Cavity` - 检测凹陷（凹面）变化的程度，并在这些区域应用所选颜色（默认黑色）


| Curvature off                    | Curvature on                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## 色差 {#chromatic-aberration}

模拟镜头边缘的色散伪影，即光线在屏幕边缘被分解。

* `Strength` - 图像红/绿/蓝通道在屏幕边缘被分离的程度

| Chromatic off                 | Chromatic on                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## 暗角 {#vignette}

通过使屏幕边缘变暗来模拟镜头暗角伪影。

* `Size` - 覆盖在图像上的反向椭圆大小
* `Hardness` - 椭圆与图像混合时边缘的柔和或锐利程度


| Vignette off                    | Vignette on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## 颗粒 {#grain}

添加颗粒效果，可以让图像看起来不那么“数字化”。

* `Strength` - 添加到图像中的颗粒/噪点强度。


| Grain off                    | Grain on                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## 锐化 {#sharpness}

类似 Photoshop 或照片处理应用中的锐化效果。

* `Strength` - 应用于图像的锐化强度。


| Sharpness off                  | Sharpness on                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## 像素艺术 {#pixel-art}

模拟复古游戏的像素画风格。

* `Slider` - 像素大小
* `Allow frame sampling` - 如果出现大量黑色像素，尝试开启此选项，它会覆盖默认采样方式。

| Pixel off                   | Pixel on                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## 扫描线 {#scanline}

模拟老式 CRT 显示器的观感。

* `Factor` - 扫描线强度
* `Spacing` - 扫描线间距（大小）

| Scanline off                   | Scanline on                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |


## 抖动 {#dithering}

对像素进行抖动以减少色带伪影。通常应保持启用，但在某些特定操作（例如导出深度图或其他数据相关操作）时可以关闭。