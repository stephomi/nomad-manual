# ![](/icons/layer.webp) 图层 {#layers}

此菜单包含图层堆栈，它是一种以非破坏性方式存储对象编辑的方法，并提供多种组合和重用图层的方式。

![](/images/layers_overview.webp) 

## 概述 {#overview}

Nomad 的图层有多种用途。

绘画信息（颜色、粗糙度、金属度、不透明度）与图层的工作方式类似于 2D 绘画软件。你可以创建一个图层并在模型上绘画。图层可以开关、调整不透明度、复制、在图层堆栈中改变顺序、调整混合模式。

Nomad 也使用图层来进行雕刻。图层可以存储细节（如皱纹），也可以存储大幅度的形变，使其类似于其他 3D 软件中的 blendshape/shape key/morph target。例如，你可以在不同图层上雕刻不同的面部表情，然后通过调整图层滑块将它们组合成新的表情。

在这种情况下，图层中存储的变化是纯加性的，图层顺序不像绘画那样重要。

图层可以通过 [Delete Layer](tools.md#delete-layer) 工具部分擦除，也可以用来基于图层中存储的不同信息创建遮罩。

![](/videos/layer.mp4)

::: tip
与大多数雕刻软件不同，更改网格拓扑不会丢弃图层。你可以使用 [Voxel Remesher](topology.md#voxel-remesher)、[Multiresolution](topology.md#multires) 或 [Trim](tools.md#trim)/[Split](tools.md#split) 工具，但请注意，当使用 [Voxel Remesher](topology.md#voxel-remesher) 时，图层质量会受到影响。
:::

::: tip
如果将图层用作 blendshape/morph target，[场景菜单](scene.md#object-menu) 中有额外的图层功能。你可以将图层拆分为对象，也可以将匹配的对象合并为图层。
:::
----

## 图层菜单 {#layer-menu}

![](/images/layers_menu.webp)

点击 `Add layer` 创建新图层。

每个图层都有名称、用于控制其强度/系数的滑块，以及选项按钮。

### 选项 {#options}

| 操作         | 图标                          | 描述                                                |
| :----------: | :---------------------------: | :------------------------------------------------- |
| 可见性       | ![](/icons/eye_open.webp)   | 显示/隐藏图层                                      |
| 混合模式     | ![](/icons/opacity.webp)    | Photoshop 风格的混合模式。4 个图标分别表示颜色、粗糙度、金属度、不透明度的模式。 |
| 编辑名称     | ![](/icons/pencil.webp)     | 编辑图层名称                                       |
| 删除         | ![](/icons/trash.webp)      | 删除图层                                           |
| 复制         | ![](/icons/clone.webp)      | 复制图层                                           |
| 向下合并     | ![](/icons/merge_down.webp) | 将当前图层与下方图层（或基础网格）合并             |
| 更多         | ![](/icons/more.webp)       | [More...](#more) 选项                              |

要将图层移动到图层堆栈中的其他位置，长按其名称并拖动。

### 更多… {#more}

“More...” 按钮会显示当前图层的额外选项：

![](/images/layers_more.webp) 

#### 通道系数 {#channel-factors}

这些控制项允许你缩放该图层的雕刻/颜色/粗糙度/金属度/不透明度的量。这些值会与图层强度滑块相乘，例如，如果图层强度为 1，而颜色通道系数为 0.5，则显示的颜色强度为 0.5。

`Offset` 控制图层雕刻强度。颜色/粗糙度/金属度被限制在 0 到 1 之间，而 Offset 可以是任意正负值。

::: tip
Offset 可以用来把一层凸起变成一层凹陷，或者把微笑变成皱眉：
![](/videos/layer_happysad.mp4)


一个对称图层可以被克隆，然后通过 del layer 分割成左右两个形状：
![](/videos/layer_leftright.mp4)

具有负 Offset 系数的图层可以烘焙成空图层，以此创建新的正向形状。

Offset 系数大于 1 的正向图层可以用来尝试更极端的 blendshape。
:::

::: warning
目前图层在颜色/金属度/粗糙度这 3 个通道上只共享一个不透明度通道。
如果你合并多个未满强度、且带有每通道强度设置的图层，最终结果可能会看起来不同。

未来也许会为每个通道提供独立的 alpha 通道，以消除这一限制。
:::


#### ![](/icons/tool_mask.webp) 蒙版 {#mask}
每个滑块旁边的遮罩按钮会从该通道创建一个遮罩。类似于在绘画软件中使用图层进行选区，这允许你将图层中完成的工作复用于其他操作。

#### ![](/icons/preview.webp) 预览 {#preview}
![](/images/layers_preview.webp) 

启用后，会预览该图层的提取设置（见下一节）。

当启用透视（xray）时，只有被提取的形状是实心的，其余部分会变为透明，这在使用负的提取高度时非常有用。

#### 提取 {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

`Extract` 按钮会将图层内容复制到一个新对象中，通常会使用下一节中用户指定的厚度。

`Closing action` 决定如何进行复制：

* None - 仅提取该部分，不生成侧面或填补任何孔洞。
* Fill - 用三角形填充孔洞并平滑。不要在平面表面上使用此选项。
* Shell - 使用厚度值和方向选项封闭提取形状。
* Layer - 提取图层差异。

#### ![](/icons/height.webp) 厚度 {#thickness}
![](/images/layers_thickness.webp) 

壳体拉伸的深度。正值向表面外侧生长，负值向表面内侧生长。

该数值旁边的加号/减号用于设置拉伸方向：
* Minus ( - ) 从当前表面开始向下拉伸。
* Plus ( + ) 从当前表面开始向上拉伸。
* PlusMinus ( ± ) 会将拉伸的顶部和底部等量推离，使其一半嵌入原始表面。

#### 平滑度 {#smoothness}
![](/images/layers_smoothness.webp) 

如果要提取区域的边缘比较锯齿状，此滑块会尝试将边缘模糊成更平滑的形状。

#### ![](/icons/height.webp) 边缘循环（侧面） {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

当 Closing action 为 “Shell” 时，此部分可见。

`Auto Edge-loop (side)` 会计算壳体侧面上的边循环数量，以生成方形多边形。

如果关闭自动，则 `Division` 滑块将设置侧面的分段数量。

_这里是 “More...” 子菜单的结尾。_

### 高级 {#advanced}
![](/images/layers_advanced.webp)

#### 保留顶层细节 {#keep-top-layers-details}

确保在对底部图层进行大幅修改时，顶部图层上的小细节仍然可见。

默认情况下，如果你在某一图层上雕刻了小皱纹，然后再对基础图层进行大幅修改，这些皱纹会被抹去。启用此开关后，这些小细节会始终浮在下方的大变化之上。在下面的视频中，可以看到皱纹细节在默认情况下会被移除，而启用 “keep top layers details” 后则会保留：

![](/videos/layers_details.mp4)


#### 界面：展开列表 {#ui-expand-list}

默认的图层菜单只允许你切换图层可见性和图层不透明度。启用此选项后，会为每个图层展开完整控制项。

![](/images/layers_expand.webp)

#### 同步变换 {#sync-transform}

启用后，所有未被选中的图层都会根据变换的旋转、缩放、扭曲进行相应调整。

如果其他图层不应使用你正在应用的新变换，请禁用此选项。

当设置为 `Auto` 时，只有可见图层会被调整。