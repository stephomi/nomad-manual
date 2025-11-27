# ![](/icons/multires.webp) 拓扑 

此菜单用于控制 Nomad 中物体的拓扑结构，以及在物体之间、纹理之间烘焙和传递细节的工具。

![](/images/topology_overview.webp)

Nomad 基于多边形，它使用三角形和四边形来处理几何体。
这里所说的拓扑，既包括面数���也包括点（顶点）之间的连接方式。

保持对拓扑的关注非常重要，尤其是在你想雕刻或绘制精细细节时。

::: tip 如何查看你的拓扑？
你可以显示[线框](settings.md#wireframe)，或者简单地关闭[平滑着色](settings.md#smooth-shading)。
:::

![](/images/topology_top.webp)

Nomad 的拓扑菜单包含以下几个部分：

| Method                                | Icon                         | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | 使用细分编辑多个细节层级                                         |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | 以均匀密度重新计算新的拓扑                                       |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | 在雕刻或绘制时实时局部增减面                                     |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | 多边形简化、UV、烘焙、重拓扑、重投射                             |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | 基元选项                                                         |


## Polygon stats

![](/images/topology_stats.webp)

拓扑菜单顶部会显示当前选中物体以及整个场景的多边形信息。数字依次表示：顶点总数、三角形总数以及四边形（四边多边形）总数。

点击这一栏会弹出场景中所有多边形物体的多边形统计列表。

## ![](/icons/multires.webp) Multiresolution

![](/images/topology_multires_menu.webp)

### 什么是 Multiresolution？
多分辨率功能主要用于两种场景：
- 使用平滑细分算法提升物体的多边形数量
- 管理多个分辨率层级，以便在大形体和小细节编辑之间自由切换

![](/videos/multiresolution.mp4)

#### Multiresolution 工作流程
多分辨率的一个重要特性是：你可以回到较低分辨率，对物体进行修改，然后再回到最高分辨率，而不会丢失高分辨率细节。所有高分辨率细节会被自动投射回来。

::: warning
如果你使用了会改变物体拓扑的工具，你将会失去该物体的所有其他分辨率层级！
一旦可能发生这种情况，你通常会收到警告，例如当你使用：
- [Voxel Remesher](#voxel-remesher)
- [Dynamic Topology](#dynamic-topology)
- [Trim 工具](tools.md#trim)
- [Split 工具](tools.md#split)
:::


### Multiresolution 滑块
该滑块表示当前物体的细分层级数量。如果有 6 条竖线，就表示有 6 个细分层级。圆点表示当前显示的细分层级。 

### Reverse
当处于最低细分层级时，Reverse 按钮会尝试在当前层级之下创建一个更低的层级。注意，这通常只在物体一开始就是通过细分创建的情况下才可能，比如在 Nomad 或其他支持多分辨率细分曲面的 3D 应用中。

### Subdivide
*Subdivide* 按钮会将多边形数量增加 4 倍，因此要注意多边形数量的增长速度非常快！
*Subdivision Surface* 的一个重要特性是，它会收敛到一个*平滑曲面*。
为了理解其工作方式，你可以在一个只有少量多边形的物体上尝试 *Subdivide* 按钮。

你可以勾选 `Linear subdivision` 选项来关闭这种*平滑*行为。

### Delete lower
如果当前显示层级之下还有更低的细分层级，则将其删除。如果误删，可以使用 Reverse 按钮重新创建。

### Delete higher
如果当前显示层级之上还有更高的细分层级，则将其删除。

### Linear subdivision
在细分网格时不进行平滑。

### Sharp border
如果物体有面组（facegroups），启用此选项会保持面组边界的锐利。该选项可以在每个细分层级单独设置（细分滑块上会在对应层级上方显示一个小图标作为标记）。

### Keep triangles
大多数标准细分曲面系统在细分时会尝试将所有多边形转换为四边形。启用此开关会强制细分继续使用三角形。

### Lock (LV0)

防止最低细分层级被修改。如果你的物体是在其他应用中生成的，并且基础网格必须保持不变，这一点非常重要。当此选项关闭时，在高层级进行的大幅修改会影响到 0 级。

::: tip 

细分默认会平滑所有锐利边缘。若想保留略微锐利的边缘，可以尝试在前两个细分层级使用 Linear subdivision 或 Sharp border，然后在更高层级关闭它们。这样可以得到半锐利的细分网格。

:::


## ![](/icons/voxel.webp) Voxel Remesher
![](/images/topology_voxel_menu.webp)
使用 `Voxel Remesher` 时，整个网格会被强制为统一分辨率的拓扑，也就是说所有多边形的尺寸大致相同。当你不想考虑拓扑、只想自由雕刻时，这非常有用。

一个典型的雕刻流程可以从使用低分辨率的 `Voxel Remesher` 来搭建粗略形体开始。
当你把网格拉伸得过多、产生严重变形时，只需不时点击 *Remesh* 按钮即可。

![](/videos/voxel_remesher.mp4)


::: tip Voxel？
如上所述，Nomad 是多边形软件，但 `Voxel Remesher` 是一个例外，它在执行重拓扑时会（临时）使用另一种体素方法。

一个重要区别是，体素方法不接受自相交，因此自相交会被自动处理。
此外，它不支持带孔的网格。

这里的孔并不是指 `genus hole`（如甜甜圈的“洞”），而是指网格不是 `watertight`/`closed` 的情况。
通常这意味着在应用重拓扑之前，所有孔都会被填补，类似于 [Trim 工具](tools.md#trim) 或[填洞功能](scene.md#hole-filling)。
:::

### Remesh
执行体素重拓扑。

### Resolution
用于计算的体素大小。在调整该参数时，网格上会显示棋盘格图案，以预览结果。

### Build multiresolution
为体素重拓扑结果创建更低的多分辨率层级。如果你使用棋盘格来设定分辨率，并将 Build multiresolution 设为 2，那么最终结果的细节会匹配分辨率滑块的值，并且在 multires 选项卡中会处于 2 级，这意味着在 1 级和 0 级会有更低分辨率的多分辨率网格。这是一个既能生成干净、均匀多边形网格，又能获得低分辨率控制网格的好方法。

::: tip 提示：Build multiresolution 与稳定平滑

该选项有时会在几何体中产生难以平滑的“环”，造成小凸起。如果出现这种情况，请在平滑工具选项中启用“Stable smoothing（稳定平滑）”。 

:::

### Keep sharp edges
启用后，新生成的点会尽量贴合原网格上的锐利边缘。这可能会引入一些变形。

## ![](/icons/dynamic.webp) Dynamic Topology

![](/images/topology_dyntopo_menu.webp)
多分辨率和体素重拓扑是业界常见的拓扑控制方法，但它们都要求你注意不要把多边形拉得太长或挤得太密。 

Dynamic Topology 是一种替代方法。在你雕刻时，Nomad 会在笔刷笔触过程中自适应地增减多边形：在雕刻小细节的地方会增加许多小多边形，而在其他区域平滑时则会减少多边形。

需要注意的是，动态拓扑会使用三角形而不是四边形。这在线框视图中可能看起来有些杂乱，但通常最好不要去看线框，只专注于做出好看的雕塑，而不用担心拓扑，之后再使用 Nomad 的其他重拓扑工具生成干净的四边形网格。

下面的视频展示了其实际效果。

![](/videos/dynamic.mp4)

### Enabled
开启动态拓扑。开启后，在笔刷半径和强度滑块下方会出现一个 DynTopo 图标，用于为每个工具单独切换 Dyntopo。

### Detail
控制细节量，其行为取决于“Detail based on...”的选择，见下文。

### Detail based on...
| Method   | Description                                                     |
| :------: | :-------------------------------------------------------------: |
| Screen   | 细节级别取决于物体在屏幕上的显示大小。Detail 滑块在 100% 或更高时用于精细细节（小三角形），在 1% 时用于低细节（大三角形）。  |
| Radius   | 工具半径决定细节量。小半径用于精细细节，大半径用于低细节。Detail 滑块是该比例的乘数。                     |
| Constant | Detail 滑块直接定义细节量，不受屏幕尺寸或工具尺寸影响。             |

::: tip 提示：Radius 模式

为了更好地理解 Radius 模式的工作方式，可以用一根手指拖动 Detail 滑块，同时用另一根手指改变工具半径。你会看到它们之间的联动关系。

:::

### Prefer...
| Method  | Description       |
| :-----: | :---------------: |
| Speed   | 优先性能          |
| Quality | 优先质量          |

当你选择 `Quality` 时，主要有两点不同：
- 细化会在雕刻之前进行，因此在绘制或雕刻非常细小的细节时，插值伪影会更少
- 细化会一直运行，直到收敛到正确的细节级别，而不是增量式行为
 
这样一来，即使你雕刻非常细小的细节或快速笔划，拓扑也总能按预期被细化。


### Use pressure on radius
仅在启用 `Radius` 模式时有效。启用后，即使笔刷大小受压感影响，细节级别也会始终反映当前笔刷大小。

### Use stroke falloff

在动态拓扑计算中同时考虑笔刷衰减曲线和 Alpha。

### Method
无论你是在[笔刷](#brush)上使用 `Dynamic Topology`，还是[全局](#global)使用，你都可以选择其工作模式：

| Method         | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | 既可以增加也可以删除面，这是上面视频中使用的模式                      |
| Subdivision    | 只增加新面，不能删除面                                               |
| Decimation     | 只删除面，不能增加面                                                 |

### Protect masked area
启用后，被遮罩区域的拓扑不会被修改。

### Vertex extrapolation


### Detail
用于重拓扑操作的分辨率。如果 Dyntopo 处于“Constant”模式，该值会与顶部 Detail 滑块相同。

### Remesh
使用动态拓扑算法执行全局重拓扑。通常对于完整重拓扑，你应优先使用 [Voxel Remesher](#voxel-remesher)。

不过，相比体素重拓扑，它的一个优势是会保护被遮罩区域，因此你可以更好地控制在哪些区域增加或减少密度。



## ![](/icons/topo_extra.webp) Misc

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) 齿轮菜单
此菜单中的许多工具都有额外选项，可通过标题旁的齿轮图标进入。

### Decimation

![](/images/topology_decimation.webp)

通过尽量保留细节来减少多边形数量，输出为三角形多边形。

如果你想导出用于 3D 打印，此功能会很有用。
但如果你还打算继续在其上雕刻，则不建议使用，因为它可能会产生不均匀的三角形。

注意，被遮罩区域不会被简化。

![](/videos/decimate.mp4)

::: tip

在高模上使用 [Quadremesh 工具](tools.md#quad-remesher) 计算时间可能很长，而且结果难以控制。先用[面组](tools.md#facegroup-1)和 Decimate 预处理网格，可以让 Quadremesh 运行得更快，并大幅提升对拓扑的控制。

* 使用面组为网格划分理想的四边形流向。
* 使用 Facegroup relax 平滑面组边界。
* 执行 Decimate。这样可以确保在面组边界上没有细长或扭曲的面。在 Decimate 设置中确保启用 facegroup，这会让三角形边精确跟随面组边界。
* 在 Quadremesh 选项中关闭 relax（因为你已经对网格做过 relax），通常可以得到不错的结果。

:::

#### Decimate
开始执行简化操作。

Decimate 按钮旁的图标用于切换影响简化的选项。图标旁的百分比表示该选项的权重，可在高级齿轮菜单中设置。

* ![](/icons/palette.webp)  `Preserve Painting` - 在绘制细节较多的区域放置更多三角形。
* ![](/icons/triforce.webp) `Uniform Faces` - 倾向于生成尺寸均匀的三角形。
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - 简化时尽量保持开放几何体和孔洞附近的边界不变。
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - 简化时尽量保持面组边界不变。
* ![](/icons/checkerboard.webp) `Preserve UV Borders` - 简化时尽量保持 UV 边界不变。

#### ![](/icons/cog.webp) Decimate 齿轮菜单
齿轮菜单包含以下高级选项：
##### Preserve painting
复选框用于启用/禁用该模式，数值决定绘制细节被保留的精确程度。数值越高，保留的绘制越多。如果你不关心绘制信息，将其设为 0。

##### Uniform faces
复选框用于启用/禁用该模式。数值越高，输出的三角形尺寸越接近。

##### Preserve borders
启用后，边界不会被简化。可以分别为 `Geometry`、`Face Group` 或 `UV` 边界设置权重。

#### Target triangles
设置目标三角形数量。默认值为 50%，百分比/目标按钮可在百分比和精确多边形数量之间切换。



### UV Unwrap - UVAtlas

![](/images/topology_uvatlas_menu.webp)
为当前网格计算纹理坐标（UV），通常会通过增加更多岛屿和切缝来尽量减少变形。

标题与齿轮菜单之间的小眼睛图标用于切换在物体上预览 UV。

![](/videos/unwrap.mp4)

#### Unwrap
为选中物体计算 UV，并在背景中显示。

#### Delete UVs
删除物体上的 UV。

#### ![](/icons/cog.webp) UVAtlas 齿轮菜单
齿轮菜单包含以下高级选项：

#### Face Group

使用面组来定义 UV 的切缝。

##### Max Stretch
数值较低会产生更少变形、更多岛屿；数值较高会产生更多变形、更少岛屿。 

##### Island spacing
岛屿之间的间距。数值较低会减少空间浪费，但会增加纹理在岛屿之间“渗色”的风险。 

::: warning
计算 UV 可能需要一些时间，最好将网格顶点数控制在 10 万以下。
:::

::: tip UV 是什么？
一个常见的类比是礼品包装：如何裁剪包装纸，才能在不重叠的情况下完全包裹一个物体？ 

UV 类似，但不是裁剪纸，而是裁剪物体本身。想象你的模型由薄塑料制成，你会如何切开它并将其摊平，在平面状态下进行绘制，然后再重新组装？

再想象模型表面由有弹性的莱卡布料构成。你可以把模型拉伸成平面，也可以切开，或两者结合。但如果你在摊平状态下在其上绘制棋盘格，重新组装后棋盘格会被拉伸变形。哪种方式更好：更多切缝、较少变形，还是更少切缝、较多变形？

UV 就是告诉 3D 软件在应用纹理时如何“切割和拉伸”物体的指令。UV Atlas 工具通常采用“更多切缝、较少变形”的策略。


:::

::: tip UV 与 Nomad 及其他应用

大多数你在网上找到的带纹理模型都是通过 UV 贴图来实现的。Nomad 可以通过[材质](material#textures)面板导入并显示这些纹理。

在 Nomad 中创建模型时，你可以在没有 UV 的情况下直接在物体上绘制。如果需要导出到其他应用（例如 [Procreate](https://procreate.art/)），可以通过 UV 将 Nomad 的颜色信息“烘焙”到纹理中。 

:::

### UV Unwrap - BFF
![](/images/topology_uvbff_menu.webp)

BFF UV 更偏向“切缝更少、变形更多”的策略。 

#### ![](/icons/cog.webp) UV BFF 齿轮菜单

#### Face Group

使用面组来定义 UV 的切缝。

##### Cone count
定义主要投影的数量。数值越低，岛屿越少，但变形越多。

##### Seamless patches
影响 UV 补丁的布局，在精心创建的面组配合下效果最佳。

### Bake -> texture 
![](/images/topology_bake_menu.webp)

纹理烘焙会将场景中其他可见物体投射到选中物体的 UV 上，从而生成纹理。

典型的烘焙流程如下：
- 你有一个带有精细细节和绘制的网格
- 克隆它
- 对其进行 Decimate（将 `Preserve painting` 设为 0）
- 为其进行 UV 展开
- 然后进行 Bake！

Nomad 默认会将场景中所有可见网格纳入计算。
你也可以使用 Solo 模式快速隐藏大部分其他网格。
如果没有其他可见物体，则会将整个场景纳入计算。

此时你应该得到一个低分辨率网格，但仍保留了原物体的大部分绘制和细节。

操作完成后，顶点颜色会被移动到一个新的禁用图层中，以免干扰纹理。

#### From itself
将当前物体最高多分辨率层级烘焙到最低层级。这种方式设置简单，但通常你会需要更多控制，此时下面的选项更有用。

#### From high-res ()
将场景中其他可见物体烘焙到选中物体上。括号中的数字表示将被用作高模目标的其他可见物体数量，这些物体会被烘焙到当前带 UV 的低模物体上。其他物体不需要在布局或拓扑上与被烘焙物体相似，从而支持灵活多样的烘焙流程。

#### Resolution
烘焙纹理的分辨率。烘焙纹理始终为正方形，因此 1024 会生成 1024x1024 的图像。 

下方按钮是常用分辨率的快捷方式。作为参考，512x512 相对较小，适合网页图形和简单几何体；4096x4096（简称 4k）适合高质量渲染。

#### ![](/icons/cog.webp) Bake 齿轮菜单
![](/images/topology_bake_gear_menu.webp)
齿轮菜单包含以下高级选项：

##### Normal, Roughness, Metalness, Color, Emissive, Opacity
这些复选框决定要烘焙哪些属性，每种属性会生成一张独立贴图。烘焙完成后，这些贴图会作为纹理添加到当前物体的材质中。

##### Backup
为了预览烘焙纹理，需要禁用物体的绘制信息。启用此选项会将所有绘制信息转移到一个新的图层作为备份，以便随时启用/禁用。

#### Cage radius
调整从烘焙物体发射射线以寻找目标物体的距离。默认情况下该距离较小，以避免伪影，但如果目标物体离烘焙物体较远，可以适当增大。

##### Ray offset
调整烘焙计算在烘焙物体上的起始位置。默认从表面外 5% 处开始，以避免大多数常见伪影。如果目标物体离烘焙物体非常远，可能需要增加该偏移量。


### Reproject to vertex

![](/images/topology_reproject_menu.webp)

将雕刻细节、绘制、图层、纹理投射为顶点属性。

可以将其视为烘焙的反向操作：如果烘焙是将顶点属性转移到纹理，那么重投射就是将纹理（及其他属性）
 转回顶点。

::: tip
在使用 `Bake to texture` 或 `Reproject to vertex` 时，顶点颜色和材质纹理都会被考虑在内。
:::

#### From itself
将材质中的纹理转换为顶点属性。仅当物体具有 UV 且材质中启用了纹理时，此按钮才会可用。

::: tip 提示：纹理绘制
Nomad 不直接支持对纹理进行绘制和编辑，但可以通过“纹理 -> 顶点”投射、在顶点上绘制、再“顶点 -> 纹理”烘焙的方式获得非常接近的效果：

1. 准备一个带 UV 的低模物体
1. 将纹理加载到其材质中
1. 对其进行足够的细分以便绘制
1. 在 `From itself` 模式下执行 `Reproject to vertex`，此时纹理已被转换为顶点属性
1. 进行绘制、平滑、涂抹、盖章等任意编辑
1. 在 `From itself` 模式下执行 `Bake to texture`，这些编辑会被转换回纹理。
:::

#### From high-res ()
将所有可见物体转换为选中物体上的顶点属性。按钮上的数字表示可见物体的数量。

::: tip
重投射其他物体不仅可以用于从其他物体转移颜色信息，还可以用于将顶点投射到其他物体上，例如将绷带投射到角色身上。
:::

#### ![](/icons/cog.webp) Reproject 齿轮菜单
齿轮菜单包含以下高级选项：

#### Vertices, Roughness, Metalness, Color, Opacity, Opacity->Mask, Mask, Layers, Face Group
这些复选框决定哪些属性会被投射到选中物体上。 

#### Relax
在重投射过程中，可以对选中网格的布局进行一定程度的平滑或放松，以更好地贴合目标。Smooth 更适合高模，Relax 更适合低模，Auto 则由 Nomad 自动选择最佳方式。

#### Iterations
在重投射过程中应用 Relax 操作的次数。

#### Cage radius
调整从选中物体发射射线以寻找目标物体的距离。默认情况下该距离较小，以避免伪影，但如果目标物体离烘焙物体较远，可以适当增大。

#### Ray bias
数值较低时更倾向于投射到目标表面最近点；数值较高时更倾向于沿表面法线方向的交点。 

#### Ray offset
调整重投射计算在选中物体上的起始位置。默认从表面外 5% 处开始，以避免某些伪影。如果目标物体离烘焙物体非常远，可能需要增加该偏移量。


### Quad Remesh - Instant
![](/images/topology_quadremesh_menu.webp)
使用 [Wenzel Jakob、Marco Tarini、Daniele Panozzo、Olga Sorkine-Hornung 的 Instant Meshes 算法](https://igl.ethz.ch/projects/instant-meshes/)进行重拓扑。它会分析网格流向并创建干净的四边形拓扑。

::: tip
在 iOS 和桌面平台上，[Quad remesher](tools#quad-remesher) 工具能提供更好的结果和更多控制。
:::

#### Remesh
开始执行 Instant Meshes 操作。

#### Target quads
Quad Remesh 尝试生成的四边形多边形数量。

#### ![](/icons/cog.webp) Quad Remesh Instant 齿轮菜单
齿轮菜单包含以下高级选项：

##### Crease angle
用于识别锐角的阈值，以帮助引导重拓扑操作。

#### Max fill hole
算法有时会产生不需要的孔洞。如果孔洞的顶点数小于该值，则会被填补。

### Holes
![](/images/topology_holes_menu.webp)
大多数情况下，你的物体应该是封闭的，即网格是“闭合”的。

如果物体存在孔洞，你可以将其填补。注意，这只对“简单”孔洞有效，不能将两个独立边界“焊接”在一起。

![](/videos/hole_filling.mp4)

::: tip
当你运行 Voxel remesher 时，所有孔洞都会被自动填补，无论你是对一个还是多个网格进行操作。
:::

#### Close holes
执行填洞操作。

#### ![](/icons/cog.webp) Holes 齿轮菜单
齿轮菜单包含以下高级选项：

##### Detail
用于填补孔洞的多边形密度。在拖动该滑块时，模型上会显示棋盘格图案，以指示将使用的三角形大小。勾选复选框会禁用该行为，只使用现有点，这通常会在孔洞上生成细长三角形，后续雕刻会比较困难。

##### Fill non-manifold
尝试填补非流形孔洞。

##### Face Group

在填洞时，是否为每个孔洞创建独立面组（Auto），或让所有孔洞共享一个面组（Off），或完全不创建面组（On）。

### Force Manifold
![](/images/topology_forcemanifold_menu.webp)
尝试清理非流形边。对于不支持一条边被超过两个面共享的外部软件，这会很有用。

#### Clean
执行清理操作。
#### ![](/icons/cog.webp) Force manifold 齿轮菜单
齿轮菜单包含以下高级选项：

#### Delete small faces
用于删除并合并小多边形的阈值。


### Triplanar
![](/images/topology_triplanar_menu.webp)
将网格转换为[三平面](scene.md#triplanar)基元。
在此过程中你很可能会丢失大量细节。

#### Force cubic
强制三平面为立方体。否则三平面会贴合物体的最小包围盒。

#### Convert
执行三平面转换操作。

#### Resolution
三平面操作中使用的体素大小。

## ![](/icons/dot.webp) Primitive
当前选中基元的参数。这些参数也可以在视口中的基元工具栏中访问。

![](/images/topology_primitive_screenshot.webp)
