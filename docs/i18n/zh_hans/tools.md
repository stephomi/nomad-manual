# ![](/icons/toolbox.webp) 工具

![](/images/tools_menu.webp)

::: tip
向下跳转到 [工具](#tools-1) 查看各个工具的详细说明。
:::

## 概览

工具从右侧的 `Toolbox`（工具箱）中选择，并通过左侧的 `Tool Controls`（工具控制）进行调节。更多设置在右上角菜单的第一个图标 `Settings`（设置）中。

笔刷类工具有大小和强度控制。选择类工具有多种选择样式控制。工具控制面板底部有常用操作的快捷方式（Smooth、Mask、Hide、Gizmo、Color、Alpha）。

Nomad 的工具在工具箱中按颜色分类：

* <span class=brush>**笔刷工具**</span>（Clay、Brush、Smooth、Layer、Inflate、Nudge、Stamp、DelLayer）
* <span class=move>**移动工具**</span>（Move、Drag）
* <span class=mask>**遮罩工具**</span>（Mask、SelMask）
* <span class=paint>**绘画工具**</span>（Paint、Smudge）
* <span class=flatten>**压平工具**</span>（Flatten、Planar）
* <span class=pinch>**挤压工具**</span>（Crease、Pinch）
* <span class=selection>**基于选择的工具**</span>：先绘制 2D 遮罩，再执行操作（Trim、Split、Project）
* <span class=creation>**创建工具**</span>（Tube、Lathe、Insert）
* <span class=transform>**变换工具**</span>（Transform、Gizmo）
* <span class=misc>**杂项工具**</span>（Facegroup、Hide、Measure、Select）
* <span class=view>**视图工具**</span>



许多工具可以通过 [Stroke](stroke.md) 菜单自定义不同的笔刷行为、压感、纹理等。 


### 笔刷控制

左侧工具栏有半径和强度滑块，下面是各工具类别特定的控制，详见后文说明。

![](/images/tool_left_panel.webp)

::: tip
许多工具的强度滑块可以超过 100%，值得尝试！
:::

### Sub 模式
强度滑块正下方的按钮是 `Sub` 按钮。它的标签和功能会随工具变化，按下后会触发一个通常是相反的替代行为。例如对 [Paint](#paint) 来说会进入擦除模式，对 [Crease](#crease) 来说会生成凸起边而不是凹缝等。

默认情况下它是“按住生效”的按钮；也就是说按住时临时启用，松开即关闭。如果轻点一下，则会持续启用 Sub 模式。

### 快捷键
左侧工具栏底部有 [Smooth](#smooth)、[Mask](#mask)、[Hide](#hide)、[Gizmo](#gizmo)、[Color](painting.md#pbr-sliders)、[Alpha](stroke.md#alpha) 的快捷键。 

默认它们也都是“按住生效”的按钮；按住时临时启用，松开即关闭。如果轻点一下，该快捷模式会持续启用。

### 选择控制

[Selection Mask](#selection-mask)、[Trim](#trim)、[Split](#split)、[Project](#project)、[Facegroup](#facegroup) 和 [Hide](#hide) 工具都使用类似的控制来选择网格区域。

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - 自由手绘形状
* `Polygon` - 由曲线和/或直线组合围成的封闭形状。更多信息见下方 [Shape editing](#shape-editing)。
* `Curve` -（仅 Project）- 用于投射的自由曲线
* `Path` -（仅 Project）- 由点定义的曲线。更多信息见下方 [Shape editing](#shape-editing)。
* `Line` - 拖出一条线来定义一个平面切片。默认会立即对网格执行操作，如果不希望这样，可关闭自动确认（长按或在图标上滑动）。
* `Rect` - 拖出一条对角线，用以定义矩形的两个角。长按或滑动可显示选项：自动确认、强制为正方形、首点作为矩形中心。
* `Ellipse` - 拖出一条对角线，用以定义椭圆大小。长按或滑动可显示选项：自动确认、强制为圆形、首点作为椭圆中心。
* `Flip` - 反转形状遮罩，或反转 Project 工具的方向。

大多数工具都有自动确认选项，启用时操作会在你画完形状后立即执行。关闭自动确认时，形状旁会出现一个绿色按钮，用来执行操作。这样你可以在确认前编辑形状、调整视图，准备好后再按绿色按钮。

### 形状编辑
多边形编辑和曲线编辑的行为类似：

* 首先拖出一条线以定义两个点，然后从线段中点拖出以定义多边形或曲线。
* 点击点可在平滑和锐利之间切换。 
* 在曲线或线段上点击并拖动可创建新点。
* 删除点：将一个点拖向相邻点，直到它变红。
* 多边形或路径图标角上的垃圾桶图标会删除该形状。

### 设置菜单

许多工具有额外设置，位于右上角菜单的第一个图标的设置菜单中：

![](/images/tools_settings_menu.webp)

## 工具

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Clay
Clay 工具适合用来堆砌你的雕塑。`Sub` 会从雕塑中移除材料。

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Brush
标准笔刷。`Sub` 会移除材料。

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Move
笔刷下的区域会“粘”在笔刷上，实现弹性变形。移动过程中选择会保持，如果你把笔刷移开再移回起点，将不会看到变形。

Sub 模式为 `Normal`，会沿表面法线方向移动笔刷下的区域。

该笔刷适合大范围变形，也适合精细的小范围调整。

#### Move 设置

* `Radius (Background)` - 距离模型边缘多远仍可雕刻，对调整物体轮廓时很有用。 
* `Same-side vertex only` - 忽略朝向与变形方向相反的顶点。


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Drag
笔刷下的区域会“粘”在笔刷上，实现弹性变形。与 Move 不同的是，Drag 在笔划过程中会持续更新选择，因此可以拉出更长、蛇形的物体，尤其是在开启动态拓扑时。

Sub 模式为 `Normal`，会沿表面法线方向移动笔刷下的区域。

该笔刷适合更松散、具姿态感的形体调整。

#### Drag 设置

* `Radius (Background)` - 距离模型边缘多远仍可雕刻，对调整物体轮廓时很有用。 
* `Same-side vertex only` - 忽略朝向与变形方向相反的顶点。

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Smooth
通过平均点的位置来平滑区域。该工具高度依赖多边形密度。
如果多边形很多，平滑效果会较弱。

Sub 模式为 `Relax`，只平滑线框，同时尽量保留几何细节。

#### Smooth 设置

![](/images/tool_smooth_settings.webp)

##### Facegroup

* `Relax` - 会平滑 facegroup 的边界。使用大于 100% 的强度可以快速平滑边界。`Auto` 仅在启用 facegroup 预览时平滑，`Off` 关闭，`On` 启用。 

##### Vertex
* `Sticky vertex on border` - 对有开放边的网格（如平面），可以平滑掉角点。启用后会锁定开放边。
* `Relax` - 与左侧工具栏中的 relax 替代模式相同。
* `Stable smoothing` - 尝试让平滑与拓扑无关。对拓扑密度变化大且平滑强度较高时效果最佳。

##### Painting
* `Screen Smoothing` - 使用该选项可获得与拓扑无关的平滑，即使在高面数时也有效。
* `Screen samples` - 平滑质量，数值越高越平滑，但速度越慢。

::: tip
高多边形密度时可能需要将强度提高到 100% 以上。非常高的数值（300%、500%）也可以作为雕刻工具使用，在笔刷下快速打平并抚平区域，就像用木槌敲打黏土一样！
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Mask
该工具用于给顶点加遮罩。被遮罩的顶点不会受到雕刻或绘画影响。 

Sub 模式为 `Unmask`，会擦除已绘制的遮罩。

类似 2D 绘画软件中的选择，遮罩可以用笔刷绘制，也可以用形状选择、模糊或锐化。 

不同于 2D 软件，遮罩还可以通过 facegroup 创建，并可用于通过拉伸/抽取式操作创建新几何体。 

![](/videos/tool_mask1.mp4)

 视口顶部会出现一个带有额外控制的工具栏。 

![](/images/tool_mask_toolbar.webp)

点击工具栏标题可展开/折叠，点击右上角箭头可将其移动到界面顶部或底部。

| Action                                             | Description                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/cross_circle2.webp) Clear              | 清除遮罩                                                                                   |
| ![](/icons/invert.webp)        Invert             | 反转遮罩                                                                                   |
| ![](/icons/sharpen.webp)       Sharpen            | 锐化遮罩边缘                                                                               |
| ![](/icons/blur.webp)          Blur               | 模糊遮罩边缘                                                                               |
|                                 Blur ->            | 左右拖动以交互式模糊遮罩                                                                   |
| ![](/icons/culling.webp)       Front              | 仅对朝向前方的顶点加遮罩                                                                   |
|                                 Convert            | 将遮罩转换为 facegroup                                                                     |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | 启用后会显示 facegroup，点击一个 facegroup 会将其遮罩                                     |
|                                 On tap (mask)      | 启用后，点击一块“岛状”的遮罩或未遮罩多边形会对该岛进行填充式遮罩/反遮罩                  |
| ![](/icons/vertex.webp)        Connected          | 启用后仅允许遮罩笔划影响拓扑上连通的区域                                                  |

##### Mask 快速手势
按住左下角的快速遮罩按钮时，可以执行类似 ZBrush 的手势：
| Action  | Gesture (hold lower-left shortcut) |
| :-----: | :--------------------------------: |
| Invert  | 轻点背景                            |
| Clear   | 在背景上拖动                        |
| Blur    | 轻点已遮罩区域                      |
| Sharpen | 轻点未遮罩区域                      |


#### Mask 设置
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - Mask 设置菜单主要用于从遮罩创建几何体，因此默认会预览新几何体的外观。你可以选择无预览、抽取预览、分离预览，以及是否以 X-ray 模式显示该几何体。

##### Thickness
* `Height` - 抽取形状的高度。加号/减号图标可在向外拉伸、向内拉伸或居中三种模式间切换。 
* `Height/Height+Mask` - 在高度恒定与由遮罩模糊程度影响高度之间切换，从而允许创建柔和且高度变化的形状。 

##### Smoothness
启用后会平滑抽取形状的边界，在高多边形时效果更好。 
* `Iterations` - 平滑迭代次数。数值越高边缘越圆滑，但会偏离原遮罩形状。
* `All/Sharp border/Borders only` - 平滑可作用于所有方向（顶部和侧面）、顶部和侧面但保持锐利边缘，或仅平滑边界而不影响顶部表面。

##### Edge loop (side)
* `Auto Edge-loop (side)` - 自动计算抽取形状侧面的分段数量，使其形成与遮罩区域多边形匹配的方形多边形。关闭后可通过边循环滑块手动设置分段数。

----

##### Extract
* `Extract` - 创建抽取几何体。
* `Closing action` - 抽取的封口方式。`None` 会将被遮罩多边形复制为新形状；`Fill` 同样复制并尝试封住背面；`Shell` 会按 `thickness` 中设置的高度进行拉伸，是默认选项。

::: tip

如果预览模式为 `Extract` 且启用了 `X-ray`，点击 Extract 按钮一开始可能会让人困惑。由于菜单仍然激活，它会尝试在新形状上预览一次抽取，并将原始表面设为 X-ray。但因为新表面上没有遮罩，无法预览抽取，Nomad 会提示 “Nothing to Extract!”。 

这是正常现象，关闭 Mask 设置菜单即可查看新形状和原始形状，如需清除遮罩或绘制新遮罩，请重新选择原始表面。
:::

##### Split
* `Split` - 会将被遮罩和未遮罩区域都抽取为新形状。 
* `Closing action (masked)` - 遮罩部分的封口方式。`None` 会将被遮罩多边形复制为新形状；`Fill` 同样复制并尝试封住背面；`Shell` 会按 `thickness` 中设置的高度进行拉伸，是默认选项。
* `Closing action (unmasked)` - 未遮罩部分的封口方式。含义同上。
* `Sync border` - 确保遮罩和未遮罩抽取形状之间的边界保持接近。关闭时，由于壳体操作会沿各自法线拉伸面片，两形状之间可能出现缝隙。

##### Carve
* `Carve` - 默认模式下，相当于以 `thickness` 的深度在表面进行 Trim，就像切下一块橘子皮。 



### ![](/icons/tool_maskSelector.webp) Selection Mask
该工具与 [Mask 工具](#mask) 基本相同，主要区别在于不使用笔划绘制遮罩，而是使用 [Selection Controls](#selection-controls)。

Sub 模式为 `Unmask`，会通过选择控制擦除遮罩。

Selection Mask 与 `Mask` 工具共享相同的工具设置。

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Paint
应用颜色和材质属性。关于材质的更多内容可参见 [Painting](painting.md) 章节。

Sub 模式为 `Erase`，会移除绘制的颜色。

#### Paint 设置
* `Layer fitering` - 功能类似 Photoshop 或 Procreate 中图层的 Alpha 锁。当你在某一图层上绘画且启用该选项时，只能修改已有颜色的区域；未上色区域会被保护。

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Smudge
涂抹颜色和材质属性。Smudge 设置菜单中有一个 `Quality` 滑块，数值越低笔划越快。

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Flatten
通过将点投射到平均平面上来压平区域。

Sub 模式为 `Fill`，会以最高点定义平面，并倾向于将点向上拉。

#### Flatten 设置

* `Lock plane direction` - 使用第一次点击时计算出的平面方向。默认关闭。
* `Lock plane origin`- 使用第一次点击的位置作为平面中心。默认关闭。

当这两项任一或全部关闭时，可以通过长笔划跨越不同深度和曲率来逐步加深压平或改变平面角度。配合笔刷菜单中的区域采样选项，可以获得非常精确的控制。

::: tip
在高曲率区域工作时，例如想压平脸颊但工具总是影响到鼻侧，可以先创建遮罩保护不希望被 Flatten 影响的区域。
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar
通过将点投射到平均平面上使其共面，但比 Flatten 的堆积更少，从而产生更干净的硬边表面。快速笔划会更多地推拉表面，较慢且从已平面区域向外扩展的笔划会更好地保持平面。

Sub 模式为 `Fill`，会以最高点定义平面，并倾向于将点向上拉。

Planar 实际上与 `Flatten` 是同一工具，但启用了 `Lock plane direction`，因此更倾向于生成稳定、硬边的表面，而 Flatten 更具雕塑性，可用于创建半平面区域。

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Crease
Crease 工具适合雕刻小切口或凹痕。

Sub 模式为 `Invert`，会创建凸起的折痕。

#### Crease 设置

* `Pinch factor` - 顶点向笔划中心侧向拉拢的程度。如果 Pinch 为 1、Offset 为 0，表面不会产生深度变化，只会改变拓扑，将边拉向笔划。
* `Offset factor` - 顶点沿深度方向推/拉的程度。如果 Pinch 为 0、Offset 为 1，会产生很深的凹缝或凸起，但看起来会比较锯齿，因为没有足够几何体被拉向折痕来准确定义其侧面和底部。

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Pinch
该工具可用于锐化边缘。

Sub 模式为 `Invert`，会将顶点向外分散。

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Trim
Trim 工具通过移除网格的一部分工作，并提供如何处理留下的空洞的选项。它使用 [Selection controls](#selection-controls) 来定义切割区域。

::: tip
由于该工具是从相机方向投射的，如果相机处于透视模式，你会收到警告。

在正交模式下，对网格的切割与视图平行，这通常是用户预期的行为。在透视相机下，物体近端和远端的切割效果会不同。
:::

#### Trim 设置

* `Stroke painting` - 如果在 Paint 菜单中启用了绘画，填补区域会使用当前选中颜色填充。
* `Boolean` - 使用四边形多边形填补 Trim 的孔洞。填补区域为平面。
* `Legacy` - 使用三角形填补 Trim 的孔洞。填补区域为平面。
* `Fill` - 使用三角形填补孔洞。填补区域为弯曲表面，类似肥皂泡膜。
* `None` - 不填补孔洞。
* `Boolean Detail Shape` - Trim 形状侧面使用的四边形和三角形的大致尺寸。
* `Boolean Detail Hole` - Trim 填补孔洞区域使用的三角形或多边形的大致尺寸。 
* `Legacy Detail` - Trim 使用的三角形的大致尺寸。
* `Legacy Hole smoothing` - 填补区域三角形的放松程度。
* `Legacy Threshold espilon` - 可调节以改进传统孔洞填补算法的数值。
* `Fill Detail` - Trim 使用的三角形的大致尺寸。

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Split
与 [Trim](#trim) 工具类似，不同之处在于 Trim 会丢弃选择区域，而 Split 会将选择区域保留为新对象。

#### Split 设置

* `Stroke painting` - 如果在 Paint 菜单中启用了绘画，填补区域会使用当前选中颜色填充。
* `Boolean` - 使用四边形多边形填补 Split 的孔洞。填补区域为平面。
* `Legacy` - 使用三角形填补 Split 的孔洞。填补区域为平面。
* `Fill` - 使用三角形填补孔洞。填补区域为弯曲表面，类似肥皂泡膜。
* `None` - 不填补孔洞。
* `Boolean Detail Shape` - Split 形状侧面使用的四边形和三角形的大致尺寸。
* `Boolean Detail Hole` - Split 填补孔洞区域使用的三角形或多边形的大致尺寸。 
* `Legacy Detail` - Split 使用的三角形的大致尺寸。
* `Legacy Hole smoothing` - 填补区域三角形的放松程度。
* `Legacy Threshold espilon` - 可调节以改进传统孔洞填补算法的数值。
* `Fill Detail` - Split 使用的三角形的大致尺寸。

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Project
Project 工具看起来与 [Trim](#trim) 类似，但不会删除或创建几何体，只是移动顶点以符合选择形状。

![](/videos/tool_project.mp4)

::: tip
如果在某一图层中使用 Project，可以通过图层滑块在原始形状和投射形状之间进行混合。
:::

### ![](/icons/tool_layer.webp) Layer
抬高表面，但限制高度。

如果按住笔在同一区域反复刷，Layer 会抬高到某一高度后不再继续，而其他工具会持续累积高度。

注意默认情况下该限制是“每笔一次”的！如果开始新笔划，会从新的表面高度继续累积。

要在多笔之间设置恒定的最大高度，请将 Layer 工具与 Nomad 的 [Layers](layers.md) 系统配合使用。

创建一个图层并使用该工具。此时最大高度由图层设定，因此可以多次笔划而高度始终一致。

`Sub` 会使用最小深度，创建沟槽。

#### Layer 设置

* `Use layer data` - 启用时，若选中了某图层，会使用图层数据设定最大高度。
* `Inflate`- 启用时会调整 Layer 的作用方向以获得更平滑的结果。
* `Relax (Normal)` - 对法线应用的平滑量。

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Inflate
沿各自法线方向移动顶点。`Sub` 会沿反向法线移动顶点。

#### Inflate 设置
* `Relax (Normal)` - 对法线应用的平滑量。

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Nudge
沿笔划方向移动或“涂抹”点。

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stamp

点击并拖动，以当前 Alpha 的形状在雕塑上抬起一块区域。

这实际上是将 [Brush 工具](#brush) 的笔划类型设为 `Lock + radius` 的结果。 

`Sub` 会将印章压入表面而不是拉出。

::: tip
Stamp 通常在高分辨率几何体上效果最佳。如果在网上搜索 “wrinkles alpha”、“pores alpha”、“scales alpha” 等，这些 Alpha 纹理配合 Stamp 可以为角色雕塑快速添加有机细节。

两种笔划模式适用于不同场景： 

* `Lock + radius` 具有固定的*高度*，拖动时调整印章的宽度和旋转。适合皮肤纹理，需要相同深度/高度，但通过不同旋转和缩放来避免重复感。
* `Lock + intensity` 具有固定的*宽度*，拖动时调整印章的旋转和高度。适合铆钉等，需要相同尺寸但不同旋转和高度。 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Delete Layer
该工具可局部重置图层，必须有激活图层，否则不会发生任何事情。

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tube
通过绘制曲线创建一根管子。 
![](/images/tool_tube_new.webp)

创建 Tube 后，可以在 3D 空间中编辑路径，其控制方式与标准的 [Shape editing](#shape-editing) 和曲线编辑工具类似。 

![](/videos/tool_tube.mp4)

#### Tube 左侧工具栏

![](/images/tool_tube_left_toolbar.webp)

左侧工具栏包含以下选项：

* `Sync` - 如果当前 Tube 是实例化的，且 Tube 的子节点在实例之间存在差异，则会重新同步它们。
* `Snap` - 启用时，Curve 和 Path 模式在绘制时会吸附到其他物体上。关闭时，只有第一个点会吸附，之后的 Tube 会在该深度绘制。它有一个小的弹出菜单：
    * `Offset` - 设置吸附深度；0% 时管截面的中点会吸附到表面，正值会抬离表面，负值会压入表面。
* `Curve` - 自由绘制 Tube。它有一个小的弹出菜单：
    * `Auto-validate` - 在笔划结束时立即创建 Tube。关闭时，路径旁会出现绿色确认圆圈，点击以确认，或使用本菜单中的 `Reset` 链接删除路径。
    * `Closed` - 将 Tube 首尾连接成环。
    * `Screen` - 仅在关闭 Auto-validate 时可用。启用时，路径“固定”在屏幕上，你可以移动视图和物体而路径保持不动。关闭时，路径属于 3D 场景，会随相机和物体一起移动。
    * `Accuracy` - 将绘制路径转换为 Tube 时使用的曲线点数量。0% 使用最少点数，但会忽略小的曲率变化；100% 非常精确，会使用更多点。
* `Path` - 通过点击定义曲线点来创建 Tube。点击绿色圆圈确认路径。它有一个小的弹出菜单：
    * `B-spline` - 一种替代曲线绘制方式，曲线点通常不直接位于曲线上，但可比默认方式生成更平滑的结果。
    * `Closed` - 将 Tube 首尾连接成环
    * `Screen` - 启用时，路径“固定”在屏幕上，你可以移动视图和物体而路径保持不动。关闭时，路径属于 3D 场景，会随相机和物体一起移动。

##### Tube 顶部工具栏
![](/images/tool_tube_toolbar.webp)
选中 Tube 时，视口顶部会出现带有额外控制的工具栏。点击工具栏标题可折叠/展开，点击右上角箭头可将其移动到视口顶部或底部。

* `Validate` - 将 Tube 烘焙为普通多边形，以便雕刻。
* `Edit` - 显示曲线点以便编辑
* `Mirror` - 为该曲线添加一个镜像 Repeater 作为父节点
* `Snap` - 将曲线点吸附到附近表面
* `Closed` - 将曲线首尾连接成环
* `B-spline` - 在 Catmull-rom 和 B-spline 插值之间切换。
* `Cap` - 在 Tube 两端都封口、仅起点封口、仅终点封口或不封口之间循环切换。
* `Hole` - 为 Tube 添加厚度，将其变为管道。在两端都有孔、仅末端有孔或无孔之间循环切换。 
* `Radius` - 在统一半径、起点/终点半径或每个曲线点半径之间循环切换。可通过曲线上的橙色手柄编辑。
* `Twist` - 在无扭转、统一扭转、起点/终点扭转或每个曲线点扭转之间循环切换。可通过曲线上的粉色手柄编辑。
* `Profile` - 在无轮廓（即圆形截面）、统一轮廓、起点/终点轮廓或每点轮廓之间循环切换。
* `Profile edit` - 显示轮廓编辑器。其功能类似 [Shape editing](#shape-editing) 工具，可保存和加载轮廓预设，并有一个开关允许在 3D 空间中编辑轮廓。
* `Spiral` - 打开菜单为 Tube 添加螺旋扭转。该菜单包含 `Twist Angle`、`Offset`、`Scale` 和 `Angle offset` 选项。
* `X Divisions` - Tube 周向分段数，例如 4 段会生成方形截面的 Tube。 
* `Constant density` - 启用时保持多边形近似方形；关闭时可设置沿 Tube 长度方向的 `Y divisions`。
* `...` - Tube 设置菜单。

#### 曲线点删除开关

![](/images/tool_tube_delete_toggle.webp)

工具栏下方是曲线点删除开关。当你将一个曲线点拖近另一个点时，它会变红，表示松开后该点会被删除。如果你在做小范围编辑且不希望删除点，可关闭此按钮以禁用点删除行为。



#### Tube 设置
* `Primitive` - 用于启用/禁用 UV 或验证 Tube 的按钮。
* `Post subdivision` - 验证前设置多重分辨率级别的快捷方式。
* `Linear subdivision` - 验证前设置线性细分级别的快捷方式。 
* `Division X` - 与工具栏中的 X Divisions 相同。
* `Division Y` - 与工具栏中的 Y Divisions 相同。
* `Curve (Repeater)` - 将 Tube 转换为 [Curve Repeater](scene.md#curve)

::: tip
将 Divisions 设为 4、Post subdivision 设为 3，可以得到末端圆滑的 Tube，适合做虫子、蛇、身体部位等。
:::


### ![](/icons/tool_lathe.webp) Lathe
通过绘制曲线创建旋转体表面。

该工具非常适合制作花瓶、酒杯等形状。

![](/videos/tool_lathe.mp4)

#### Lathe 左侧工具栏

![](/images/tool_lathe_left_toolbar.webp)

左侧工具栏包含以下选项：

* `Sync` - 如果当前 Lathe 是实例化的，且 Lathe 的子节点在实例之间存在差异，则会重新同步它们。
* `Fixed` - 启用时，Lathe 的中心轴固定并显示在屏幕上。该中心线有可编辑的点。关闭时，Lathe 中心会动态更新以匹配所绘曲线的起点和终点。
* `Curve` - 一笔绘制 Lathe 轮廓。它有一个小的弹出菜单：
    * `Auto-validate` - 启用时，在笔离开屏幕后立即创建 Lathe。关闭时，曲线旁会出现绿色圆圈，点击以创建 Lathe。可通过 `Reset` 按钮删除曲线。
    * `Closed` - 将曲线首尾连接成环
    * `Screen` - 仅在关闭 Auto-validate 时可用。启用时，路径“固定”在屏幕上，你可以移动视图和物体而路径保持不动。关闭时，路径属于 3D 场景，会随相机和物体一起移动。
    * `Accuracy` - 将绘制路径转换为 Tube 时使用的曲线点数量。0% 使用最少点数，但会忽略小的曲率变化；100% 非常精确，会使用更多点。
* `Path` - 通过点击定义曲线点来创建 Lathe。点击绿色圆圈确认路径。它有一个小的弹出菜单：
    * `B-spline` - 一种替代曲线绘制方式，曲线点通常不直接位于曲线上，但可比默认方式生成更平滑的结果。
    * `Closed` - 将 Tube 首尾连接成环
    * `Screen` - 启用时，路径“固定”在屏幕上，你可以移动视图和物体而路径保持不动。关闭时，路径属于 3D 场景，会随相机和物体一起移动。

#### Lathe 顶部工具栏
![](/images/tool_lathe_top_toolbar.webp)

选中 Lathe 时，视口顶部会出现带有额外控制的工具栏。点击工具栏标题可折叠/展开，点击右上角箭头可将其移动到视口顶部或底部。

* `Validate` - 将 Lathe 烘焙为普通多边形，以便雕刻。
* `Edit` - 显示曲线点以便编辑
* `Mirror` - 为该 Lathe 添加一个镜像 Repeater 作为父节点
* `Snap` - 将曲线点吸附到附近表面
* `Stable` - 启用时，轮廓曲线会作为 Lathe 中心线的子节点。关闭时，可单独编辑中心线而不移动曲线，从而创建更复杂的形状。
* `Focus` - 将视图旋转到正对轮廓曲线。
* `Closed` - 将曲线首尾连接成环
* `Cap` - 当 Closed 关闭时，在两端封口、仅起点封口、仅终点封口或不封口之间循环切换。
* `Hole` - 为 Lathe 添加厚度，将其变为管道。在两端都有孔、仅末端有孔或无孔之间循环切换。 
* `B-spline` - 在 Catmull-rom 和 B-spline 插值之间切换。
* `X Divisions` - Lathe 周向分段数，例如 4 段会生成方形截面的 Lathe。 
* `Constant density` - 启用时保持多边形近似方形；关闭时可设置沿 Lathe 长度方向的 `Y divisions`。
* `...` - Lathe 设置菜单。

#### Lathe 设置
* `Primitive` - 用于启用/禁用 UV 或验证 Tube 的按钮。
* `Post subdivision` - 验证前设置多重分辨率级别的快捷方式。
* `Linear subdivision` - 验证前设置线性细分级别的快捷方式。 
* `Division X` - 与工具栏中的 X Divisions 相同。
* `Division Y` - 与工具栏中的 Y Divisions 相同。
* `Curve (Repeater)` - 将轮廓曲线转换为 [Curve Repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) Insert
在一个物体表面上放置另一个物体。使用方式类似 Stamp 工具，但作用于完整 3D 形状。

如果在左侧工具栏中选择一个 Primitive，在任意表面上点击并拖动会在点击处放置一个 Primitive，拖动决定其大小。拖动结束后，Insert 会自动切换到 [Transform](#transform) 模式。

在 Instance 模式下，拖动会在表面上创建并滑动一个新实例。大小会复制自第一个形状，这样可以在其他表面上放置许多相同大小的对象实例。

你不必只插入 Primitive！在大纲中选择*任意*形状，如果 Insert 处于 Instance 或 Clone 模式，你都可以在其他表面上拖动复制所选对象。

如果对象有自定义 Pivot，则会将其用作锚点。见下方视频。

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transform
用一指和两指直接在另一个物体表面上移动/旋转/缩放模型。

该工具通过左侧工具栏控制，有 5 个按钮：

* `Snap` - 将模型吸附到其他表面
* `Group` - 如果选中对象包含对象和实例的组合，可用此选项决定工具行为。
* `Move` - 单指拖动移动对象。启用 Snap 时，会沿手指下方表面滑动对象。
* `Rotate` - 单指拖动旋转对象。启用 Snap 时，会围绕手指下方表面的法线旋转。
* `Scale` - 单指拖动缩放对象。

Transform 可通过两指快速使用其中两种模式：

* 拖动物体进行放置。停止移动第一根手指，但不要抬起。
* 在保持第一根手指按下的同时，第二根手指触碰屏幕。拖动第二根手指会缩放对象。
* 抬起第二根手指，继续拖动第一根手指，对象会再次处于移动模式。

你也可以通过第二根手指的轻点手势切换第二模式：

* 拖动物体进行放置，停止移动，但不要抬起手指。
* 在保持第一根手指按下的同时，第二根手指轻点屏幕。
* 工具切换到旋转模式。拖动第一根手指设置旋转。
* 再次用第二根手指轻点，工具切回移动模式。

这为在另一个物体上克隆对象提供了快速工作流，例如在地形上布置岩石。注意左侧工具栏中也有 Clone 按钮，方便访问：

* 使用 Transform 工具将一块岩石移动到合适位置。
* 松手，按下 Clone 按钮
* 移动这块岩石，并根据需要旋转/缩放
* 松手，再按 Clone 按钮
* 移动下一块岩石，如此反复。

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo
该工具用于移动、旋转和缩放对象，以及修改对象的 Pivot。

视口中的 Gizmo 句柄具有以下功能：

* `Move` - 拖动带箭头的线在 X/Y/Z 方向移动。拖动 Gizmo 中间的桃色点在屏幕空间自由平移。点击红、绿、蓝色方块在 X/Y/Z 平面内平移。
* `Rotate` - 拖动红/绿/蓝色圆环在 X/Y/Z 轴旋转。拖动圆环内的球体进行自由旋转。
* `Scale`- 拖动外侧红/绿/蓝色点在 X/Y/Z 方向缩放。拖动外侧红/绿/蓝色圆锥在 X/Y/Z 平面内缩放。拖动外侧桃色圆环进行统一缩放。

![](/images/tool_gizmo.webp)

#### 节点与顶点 

Nomad 中的每个对象由节点和顶点组成：

* `Node` - 对象的“手柄”，存储平移、旋转、缩放，即变换矩阵。
* `Vertices` - 定义对象表面的点，存储位置和绘画信息。

如果你有一个由 8 个顶点组成的简单立方体，可以通过修改其变换矩阵来平移，也可以通过修改顶点位置来平移。雕刻时通常希望修改顶点，而用 Gizmo 移动物体时通常希望修改节点。Nomad 允许两种方式。 

#### 左侧菜单工具栏

左侧工具栏控制 Gizmo 是作用于节点还是顶点，以及其他功能：

* `Clone` - 创建当前对象的独立副本，可用 Gizmo 拖动。
* `Instance` - 创建当前对象的实例副本。对象之间是链接的，对其中一个对象的雕刻会出现在所有实例上。
* `Group/Object/Vertex/Auto` - 设置 Gizmo 作用于对象的节点还是顶点。默认的 `Auto` 模式会尝试自动判断。如果有多个对象以层级结构父子相连，`Object` 只会移动当前对象，子对象保持不动。Gizmo 也可以考虑遮罩和对称。
* `Pin` - 默认情况下 Gizmo 会移动到选中对象的 Pivot。启用 Pin 后，Gizmo 会保持在当前位置。
* `Align` - 在 Pivot 与当前对象对齐和与世界对齐之间切换。
* `Snap rotation` - 启用旋转值按步长吸附，启用时会显示并可编辑吸附步长。
* `Snap translation` - 启用平移值按步长吸附，启用时会显示并可编辑吸附步长。
* `Pivot` - 启用后，可以移动和旋转 Gizmo 而不移动对象。它有一个额外菜单，见下文。

#### Pivot
启用 Pivot 模式时，会显示一个菜单以便快速修改 Pivot：

**Reset** 
* `Center` - 将 Pivot 移动到对象中心
* `Bottom` - 将 Pivot 移动到对象底部
* `Align` - 将旋转重置为与世界对齐
* `Mask` - 将 Pivot 移动到未遮罩区域的中心

**On Tap**
* `None` - 点击对象时不执行任何操作
* `Normal` - 将 Pivot 移动并旋转到点击处的表面法线方向
* `First` - 将 Pivot 移动到点击处，但不旋转
* `Medial` - 将 Pivot 移动到对象在点击处下方的中间位置

#### Gizmo 设置

![](/images/tool_gizmo_settings.webp)

##### Matrix 
* ![](/icons/target.webp) `Move origin` - 将对象移动，使其 Pivot 位于场景中心（原点）。
* ![](/icons/bake.webp)  `Bake` - 将对象“冻结”在当前位置，并将平移/旋转值设为 0，缩放设为 1。
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - 让矩阵值与 Gizmo 句柄在世界中的位置一致。
* ![](/icons/reset.webp) `Reset` - 快捷方式，将平移值设为 0、旋转值设为 0、缩放设为 1，并移动/旋转对象。

::: tip Bake 与 Bake Pivot 的区别
创建一个立方体，选择 Gizmo 工具，打开并固定设置菜单。默认情况下平移和旋转为 0，缩放为 1。

启用 Pivot 模式，将句柄移动到一侧，然后关闭 Pivot 模式。Pivot 已改变，但注意平移值仍为 0。 

如果想看到 Pivot 的“真实”位置，点击 `Bake Pivot`。此时平移值会更新。注意在此操作以及 Pivot 模式下立方体都不会移动。

将立方体移动并旋转到某处，然后点击 `Move Origin`。对象会移动，使其 Pivot 位于世界中心，但旋转保持不变。

点击 `Reset`，旋转也会被设为 0。

再次移动并旋转立方体，这次点击 `Bake`。Pivot 保持不变，立方体保持不动，但平移和旋转值被设为 0。

多练习几次！理解 Pivot 值通常是隐藏的，Nomad 会帮你处理，但如果需要将 Pivot 设置到空间中的真实位置，`Bake Pivot` 可以做到这一点。

:::

* `Translation` - 平移 X、Y、Z 值
* `Rotation` - 旋转 X、Y、Z 值
* `Scale` - 启用统一缩放时为统一缩放值，否则为 X、Y、Z 缩放值
* `Uniform scale` - 在统一缩放和各轴独立缩放之间切换

-----

* `Compact` - 在将 Gizmo 的额外手柄放在旋转球外侧或内侧之间切换
* `Widget size` - Gizmo 的整体尺寸
* `Thickness` - Gizmo 线条粗细
* `Opacity` - Gizmo 透明度
* `Hide on interaction` - 拖动时是否临时隐藏 Gizmo

-----

* `Tangent roll threshold` - 控制拖动圆环进行 X/Y/Z 旋转时 UI 的行为。如果该值为 0，旋转像转动刻度盘一样，需要绕圈拖动 Gizmo；如果为 90，旋转像拉悠悠球的线一样，沿直线向点击点的径向拖动。介于 0 和 90 之间时，两种方式混合：低于该值为线性拖动，高于该值为圆周拖动。
* `Numerical input` - 启用后，单击 Gizmo 会弹出窗口以输入该轴的精确数值。

::: warning
[Gizmo](#gizmo)、[Translate](#translate)、[Rotate](#rotate) 和 [Scale](#scale) 使用它们各自的对称复选框！

默认情况下该对称是关闭的。
:::

左侧可以移动 Gizmo 的 Pivot，下面的视频展示了其效果。
这对旋转尤其有用，因为它不会改变平移。

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Facegroup

Facegroup 允许你将对象划分为不同颜色的面组。你可以在 Nomad 中以多种方式使用这些分组：

* 作为遮罩的快速选择方式
* 隐藏/显示对象的部分区域
* 在不拆分为多个部件的情况下组织对象
* 定义 UV 区域
* 引导 Quad Remesher
* 为 Smooth 等工具提供额外控制

#### Facegroup 左侧工具栏

* `Patch ` - 以色块形式显示可用的 Facegroup。未使用的色块可以删除。点击色块可重命名或更改颜色。加号图标可创建新色块。
* `Dot` - 在对象上绘制以定义 Facegroup。启用 `+ Face Group` 时，每次新笔划都会自动创建一个新的 Facegroup，适合快速划分区域。轻点会对选中区域进行填充。滑块设置点的半径。
* `Relax` - 平滑 Facegroup 的边界。对为 Quad Remesh 定义干净边界或为硬表面建模定义面板非常有用。滑块控制 Relax 操作的半径和强度。
* `Shape selector` - 使用形状而非笔刷创建 Facegroup，可用 `Lock+Radius`、`Lasso`、`Polygon`、`Rect` 和 `Ellipse`。更多信息见 [Shape Selector](#shape-selector)。
* `Auto-pick` - 启用后，会在笔划起始处选中对应色块，并在整个笔划中应用该色块。非常适合清理 Facegroup 区域；如果某个 Facegroup 延伸过远，启用 Auto-pick，从区域正确的地方开始笔划，拖到边界即可重新分配正确色块。

### ![](/icons/tool_hide.webp) Hide
隐藏或隔离对象的部分区域。 

主要模式通过左侧菜单控制：

* `Dot` - 在对象上刷动以隐藏部分区域。
* `Shape selector` - 使用形状而非笔刷隐藏，可用 `Lasso`、`Polygon`、`Line`、`Rect` 和 `Ellipse`。更多信息见 [Shape Selector](#shape-selector)。
* `Show` - 反转操作，使选中模式显示而非隐藏对象部分。

视口顶部会出现一个带有额外控制的工具栏：

* `Clear` - 恢复对象，显示所有隐藏部分。
* `Invert` - 交换隐藏和可见部分。
* `Facegroup` - 使用 Facegroup 快速隐藏区域，点击某个 Facegroup 会隐藏整个 Facegroup。
* `Mask` - 如果存在遮罩，点击该按钮会隐藏被遮罩部分。
* `Delete` - 删除对象的隐藏部分
* `Split` - 将对象的隐藏部分拆分为新形状。

### ![](/icons/tool_measure.webp) Measure
拖动以测量两点之间的距离。

### ![](/icons/tool_remesh.webp) Quad Remesher

![](/images/tool_quadremesher.webp)

该工具会将选中对象转换为干净的四边形拓扑布局，并提供密度、边流、对称等控制。 

::: tip
Quad Remesher 由 [Exoside](https://exoside.com/) 为 iOS 和桌面平台开发。 

在 iOS 中，它是 Nomad 内的一次性内购，价格为 16 美元（USD）。

在桌面平台，请从 [Exoside](https://exoside.com/quadremesher/quadremesher-buy/) 购买授权。你可以只为 Nomad 桌面版购买，或购买适用于所有支持桌面应用的跨平台授权。

如果你已经为其他桌面应用购买了 Quad Remesher，可以[以更低价格升级为全平台授权](https://exoside.com/quadremesher/quadremesher-upgrade/)。

Quad Remesher 不支持 Android。Android 可以使用拓扑 -> Misc 菜单下提供的免费开源 “Quad Remesh - Instant”，但请理解其功能非常有限。
:::

When this tool is activated for the first time, it will ask if you want to enable it as an in-app purchase. Once active, the left and top toolbars will be enabled.

* `Dot` - 该笔刷用于设置目标密度。强度为 100% 时会绘制为红色，在这些区域会使用目标四边形密度的两倍。强度为 0% 时会绘制为青色，在这些区域会使用目标四边形密度的一半。强度为 50% 时会绘制为灰色，会使用默认的目标四边形密度。
* `Smooth` - 平滑红/灰/青三种密度之间的过渡。
* `Curve` - 在雕刻表面上勾画曲线，Quad Remesher 会将这些曲线作为边流向的引导。点按一条曲线即可将其删除。
* `Path` - 在雕刻表面上绘制路径，Quad Remesher 会将这些路径作为边流向的引导。点按一条路径即可将其删除。
* `Rect` - 在雕刻表面上绘制矩形，Quad Remesher 会将这些矩形作为边流向的引导。点按一条路径即可将其删除。
* `Ellipse` - 在雕刻表面上绘制椭圆，Quad Remesher 会将这些椭圆作为边流向的引导。点按一条路径即可将其删除。

#### Quad remesher top toolbar
![](/images/tool_quadremesher_toolbar.webp)

视口顶部会出现一个工具栏，提供额外的控制选项：


* `<Count>` - 单击此按钮开始 Quad Remesher 过程，该数值表示目标四边形重拓扑数量。
* `Quads` - 通过左右滑动设置目标四边形数量，或点按以输入精确数值。注意这更像是一个参考值而非固定数值，Quad Remesher 上的各种控制选项通常会导致结果与该目标不完全一致。
* `Half` - 将目标数量设置为当前多边形数量一半的快捷方式。
* `Same` - 将目标数量设置为当前多边形数量的快捷方式。
* `Guides` - 显示引导线总数，或点按以删除所有引导线。
* `Density X` - 点按以移除所有密度绘制。
* `Density (painting)` - 切换是否使用密度绘制。
* `Face Group` - 切换是否使用面组来引导 Quad Remesher。
* `Relax` - 切换在四边形重拓扑过程中是否自动放松面组边界。如果你已经对面组边界进行了放松/平滑，请禁用此选项。
* `Relax Slider` - 用于放松面组边界的快捷滑块。
* `Hard Edges` - 切换是否尝试保持硬边。
* `Reproject Vertex` - 切换是否将新的拓扑布局重投影到输入网格上。
* `Symmetry` - 切换是否启用对称结果。注意对称始终围绕世界 X 轴计算，因此如果你期望得到对称结果，请确保模型位于原点。
* `...` - Quad Remesher 设置菜单。 

#### Quad remesher settings menu

这些设置中的大部分在顶部工具栏中也可以使用。

* `<Count>, Half, Same` - 与顶部工具栏中的 Remesh、Half、Same 按钮相同。
* `Target Quads` - 与顶部工具栏中的 `Quads` 按钮相同。
* `Adaptive quad count` - 切换是否在高曲率区域使用更小的四边形，在低曲率区域使用更大的四边形。
* `Adaptive size` - 设置自适应程度。100% 将允许最大自适应尺寸，0% 时四边形将保持均匀。
* `Auto-Detect Hard Edges` - 切换是否自动调整四边形重拓扑布局，以更好地跟随锐利表面。
* `Density (painting)` - 与顶部工具栏中的 `Density (painting)` 按钮相同。
* `Reproject Vertex` - 切换是否将新的拓扑布局重投影到输入网格上。
* `Face Group` - 与顶部工具栏中的 `Face Group` 按钮相同。
* `Relax Slider` - 用于放松面组边界的快捷滑块。

::: tip

获得高质量、伪影最少的四边形重拓扑的一个步骤配方：

* 使用面组对网格进行分组，以定义理想的四边形流向。
* 使用面组放松功能，使面组边界平滑。
* 进行简化（Decimate）。这将确保在面组边界上没有细长或扭曲的面。在简化设置中确保启用面组选项，这会让三角形边精确地沿着你的面组边界分布。 

在 Quad Remesher 选项中确保关闭 relax（因为你已经对网格进行了放松），这样通常可以获得良好的结果。

:::

### ![](/icons/tool_select.webp) Select
使用形状模式选择场景中的对象。`Unselect` 将从选择中移除对象。

### ![](/icons/tool_view.webp) View
此“工具”本身并不执行任何特殊操作，只是用于在不修改场景的情况下查看模型。


## Toolbox context menu

![](/images/tools_context_menu.webp)

在工具箱中的工具上右键单击或长按会弹出一个上下文菜单。该菜单包含以下选项：

* `Save` - 保存你对该工具所做的任何更改
* `Clone` - 将该工具复制为一个新的工具快捷方式
* `Last save` - 恢复到该工具上一次保存的版本
* `Icon` - 更改该工具的图标
* `Reset` - 将该工具重置为默认设置
