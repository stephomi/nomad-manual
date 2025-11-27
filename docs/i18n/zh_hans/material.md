# ![](/icons/material.webp) 材质

此菜单允许你更改当前对象的材质、对象/材质的渲染属性，并为材质分配纹理。

![](/images/material_overview.webp)

材质定义了对象的外观方式，即它如何对光线和其他对象作出反应。对象的外观由以下属性控制：

* `材质类型`
* `颜色`
* `粗糙度`
* `金属度`
* `不透明度`
* `反射率`
* `自发光/无光照`

通过组合这些属性，可以实现从写实、卡通到实验性在内的各种效果。

颜色、粗糙度、金属度和不透明度都可以进行绘制，更多信息参见 [顶点绘制选项](painting.md)。

材质类型、反射率、自发光/无光照是材质属性，详见下文说明。

此菜单顶部的复制/粘贴按钮允许你在对象之间复制材质。

请注意 Nomad 的渲染器是实时渲染器；虽然功能强大，但在某些效果上会优先考虑速度而非绝对精确。

## 材质类型

![](/images/material_types.webp)

Nomad 的材质类型包括：不透明、次表面、混合、加色、折射、抖动、阴影捕捉器。

### ![](/icons/material_opaque.webp) Opaque（不透明）
默认模式，将表面视为简单材质，支持颜色、粗糙度、金属度和不透明度的绘制。

### ![](/icons/material_subsurface.webp) Subsurface（次表面）
此模式可以模拟允许光线在内部模糊和散射的材质，如皮肤、蜡、玉石。

为了获得最佳效果，请切换到 PBR 着色模式，并至少使用一个平行光或聚光灯，理想情况下配合较暗的环境光。

`Depth` 控制光线从正面进入、在表面下方散射、再从正面表面射出的距离。这会软化硬阴影并模糊表面细节。

`Translucency` 控制光线从前向后穿过形体的散射效果，比如叶片背面的透光，或耳朵被强烈背光时的透光。

### ![](/icons/material_blending.webp) Blending（混合）

与不透明类似，但支持不透明度滑块，使材质可以在实心与透明之间混合。它是一个简单的单一不透明度滑块，相比之下，不透明材质支持可绘制的不透明度。

::: warning
混合模式在复杂或相互交叉的形体中可能会产生闪烁和跳变。
:::

### ![](/icons/material_additive.webp) Additive（加色）
使用此材质可以让网格半透明。它类似于混合材质，但混合会与周围环境相互混合，而加色总是比其后方的对象更亮，适合用于光束、火焰、爆炸等明亮效果。

你可以将不透明度设置为大于 1，这意味着对象会更亮。  
如果你想使用 [泛光](postprocess.md#bloom) 和 `threshold 参数` 只让该对象像自发光对象一样发光，这会很有用。

此模式通常比 [Blending](#blending) 产生更少的伪影（顺序无关透明度）。

### ![](/icons/material_refraction.webp) Refraction（折射）
此模式可用于模拟玻璃材质。由于实时渲染的限制，自身折射和多层折射会有一定限制。

模型的粗糙度绘制会影响折射的模糊程度。  
默认情况下，在 Nomad 中创建的每个对象粗糙度大约为 25%，因此折射不会完全清晰，而是略微模糊。  
你可以使用 `paint glossy` 按钮将模型重新绘制为粗糙度和金属度为 0（颜色不会受影响）。

这里有两种不同的粗糙度：一种控制表面反射的模糊程度，另一种控制内部（折射）的模糊程度。  
然而，由于 Nomad 中只有一个粗糙度绘制通道，内部和外部粗糙度会共享同一数值。  
若要让它们不同（例如棒棒糖：表面清晰但内部模糊），可以使用 `Surface glossiness` 和 `Interior roughness` 滑块覆盖绘制的粗糙度。

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering（抖动）
通过随机丢弃部分像素让对象半透明。

### ![](/icons/material_shadow_catcher.webp) Shadow Catcher（阴影捕捉器）

让对象本身不可见，只接收阴影。用于将 Nomad 渲染与其他图像合成时非常有用。

::: tip

关于透明度和混合模式的更多信息可参见 https://support.fab.com/s/article/Transparency-Opacity

:::

## 控件

![](/images/material_controls.webp)

### Always unlit（始终无光照）
启用后，对象将忽略 PBR 和 Matcap，仅显示其颜色绘制，不进行明暗着色。  
注意如果你使用 [Additive](#additive)，可以通过绘制黑色直接绘制透明度。

### Opacity（不透明度）
控制对象看起来有多实心或不透明；100% 为完全实心，0% 为完全透明。你也可以通过绘制不透明度获得更精细的控制。

### Reflectance（反射率）
控制非金属材质接收反射的强度。大多数情况下应使用默认值（对应标准的法线方向 4% 反射光），但可以提高以增强角色眼睛中的反射和高光等效果。

### Inverse culling（反向剔除）
反转表面的法线。通常不需要，但当模型看起来“里外反转”时可以使用，或与关闭 `Two sided` 结合使用，用于制作内部空间，使靠近相机的一面墙始终被隐藏。

### Smooth Shading（平滑着色）
参见 [全局选项](settings.md#smooth-shading)。  
`Auto` 值将使用全局选项。

### Two sided（双面）
参见 [全局选项](settings.md#two-sided)。  
`Auto` 值将使用全局选项。

### Coloured backface（背面着色）
参见 [全局选项](settings#two-sided)。  
`Auto` 值将使用全局选项。

### Casts shadows（投射阴影）
目前 `Auto` 与 `On` 相同。  
透明对象也会投射阴影（以抖动模式模拟混合阴影）。  
如果场景中有不需要投射阴影的大型对象（例如大地面），请务必关闭其阴影投射。

### Recieve shadows（接收阴影）
目前 `Auto` 与 `On` 相同。

### Wireframe（线框）
参见 [全局选项](settings.md#wireframe)。  
`Auto` 值将使用全局选项。


## 纹理

![](/images/material_textures.webp)

如果对象具有 UV，则可以在顶点颜色/粗糙度/金属度/不透明度之外，将纹理应用到材质上。通常这些纹理来自烘焙，但也可以使用在 Nomad 之外创建的图像。

纹理可以应用到：

* Color（颜色）
* Normal（法线）
* Roughness（粗糙度）
* Metalness（金属度）
* Opacity（不透明度）
* Emissive（自发光）

点击纹理槽会弹出选择器。将纹理分配给材质槽后，再次点击会弹出纹理面板：

### 纹理面板选项

![](/images/material_texture_panel.webp)

### Open
选择另一张纹理

### None
移除纹理

### Opacity（不透明度）

如果图像具有 alpha 通道，此选项允许你将其用于不透明度，或忽略它。

### ![](/icons/link.webp) Chain/Link 图标 

以下部分中的链接图标启用时，表示所使用的选项会在其他同样启用链接图标的纹理（颜色、法线、粗糙度、金属度、不透明度、自发光）之间共享。

这可以确保当你有对齐好的多张纹理时，即使更改参数或投影类型，它们仍能保持对齐。


### Projection（投影）
![](/images/material_projection.webp)

设置纹理如何应用到对象上。

* `Auto` - 如果对象有 UV，则使用 UV，否则使用三平面
* `UV` - 使用网格的 UV 坐标来应用纹理。如果网格和纹理来自 Nomad 之外，或将从 Nomad 导出到其他软件使用，UV 是正确的选项。
* `Triplanar` - 沿 X、Y、Z 轴投射纹理，并对接缝进行混合。

### Triplanar（三平面）
![](/images/material_triplanar.webp)

三平面投影是一种功能强大但简单的纹理应用方式。

三平面就像有 6 台投影仪使用同一张图像，分别投射到对象的前、后、左、右、上、下六个方向。

如有需要，可以将其烘焙为 UV 或顶点颜色。


![](/images/material_triplanar_example.webp)

#### Method（方式）

* `Local` - 投影会随对象变换一起移动
* `World` - 投影固定在世界空间中，移动对象会让对象在投影中“滑动”。

#### Hardness（硬度）

控制各个投影之间的混合方式。100% 表示不进行混合，投影边缘会很锐利。0% 会在较大角度范围内混合边缘。默认值为 90%，足以隐藏边缘，同时让其余区域保持清晰。

### Uniform（统一）

勾选时，所有投影使用相同的硬度。取消勾选时，会为 X、Y、Z 投影分别显示额外的硬度控制。

### Parameter（参数）
![](/images/material_parameter.webp)

#### Filtering（过滤）
纹理过滤方式，`Auto` 为默认值，可选方式有 `Nearest`、`Linear`、`Mipmap`。  
Nearest 不做过滤，因此纹理在近距离观察时可能出现锯齿伪影。Linear 和 Mipmap 过滤效果更好，纹理在近距离会显得略微模糊而非锯齿。

#### Tiling-X（平铺-X）
当 Scale 参数大于 1，使纹理相对于对象 UV 变小时，控制纹理在 X 轴上的平铺方式。`None` 表示不重复。`Repeat` 会重复平铺纹理。`Mirror` 会重复平铺纹理，但每隔一块会镜像翻转，有助于隐藏平铺伪影。

#### Tiling-Y（平铺-Y）
与 Tiling-X 相同，但作用于 Y 轴。

### Transform（变换）
![](/images/material_transform.webp)

在 UV 空间中对纹理应用额外的二维变换。重置按钮会恢复默认值，当选择的纹理不是颜色纹理时，链条图标可将其变换与颜色纹理的变换链接或取消链接。

#### Translation（平移）
纹理在 X 和 Y 方向上的偏移量。

#### Rotation（旋转）
纹理的旋转角度。

#### Scale（缩放）
纹理的缩放值，数值越大，纹理在对象上看起来越小。使用 Tiling-X 和 Tiling-Y 滑块控制平铺行为。

### Uniform scale（统一缩放）
关闭后，Nomad 会显示独立的 Scale-X 和 Scale-Y 控件。
