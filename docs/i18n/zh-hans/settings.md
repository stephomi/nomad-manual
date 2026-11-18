# ![](/icons/cog.webp) 设置 {#reset-to-default}

设置菜单包含许多选项，用来控制 Nomad 的外观和行为。

![](/images/settings_overview.webp)

菜单顶部的一排按钮可以直接跳转到对应部分：`光标`、`指示器`、`线框`、`网格`、`双面显示`、`轮廓`、`高亮`、`导航器`、`显示场景状态`、`手柄`、`形状`、`重复器` 和 `多分辨率`。

## 显示设置 {#display-settings}
这一部分提供了快捷开关，对应本菜单下方的大部分设置。

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) 平滑阴影 {#smooth-shading}
在平滑着色和多边形面着色之间切换。使用面着色时，每个多边形会单独着色，因此您可以看到底层的拓扑结构。
在雕刻阶段使用面着色会很有帮助，到渲染时再切换为平滑着色。

关闭平滑阴影可以稍微提升性能。

### ![](/icons/outline.webp) 轮廓 {#outline-quick}
开启或关闭当前所选对象的轮廓。

在关闭了[使未选对象变暗](#darken-unselected-objects)的情况下，这可以帮助您直观地看出当前选中了哪些网格。

从性能角度来看，使用[使未选对象变暗](#darken-unselected-objects)比使用轮廓要好得多。

### ![](/icons/grid.webp) 网格 {#grid-quick}
开启或关闭背景网格，有助于判断物体的位置和比例。

### ![](/icons/culling.webp) 双面显示 {#two-sided-quick}
开启或关闭多边形的双面显示。每个面都朝向某个方向。
被视为*背面*的面，就是背对相机视角的那些面。

例如，启动时的简单球体，它的面都朝向外侧。
如果把相机移到球体内部，您看到的就是这些面的背面。

大多数情况下，您不应该看到面的背面，所以给背面着色可以帮助您发现潜在的问题或错误的拓扑。

关闭 `双面显示` 渲染可以稍微提升渲染性能。


### ![](/icons/wireframe.webp) 线框 {#wireframe-quick}
开启或关闭线框叠加显示。

请注意，开启线框会降低性能。

### ![](/icons/navigator.webp) 导航器 {#snap-cube-quick}
在场景角落显示一个辅助图标，帮助您在空间中辨别方向，并快速切换前/后/左/右/上/下视图。

### ![](/icons/palette.webp) 显示绘画 {#show-painting}
开启或关闭绘画的显示。关闭时，物体不显示绘画，而是以白色、非金属、粗糙度 25% 的材质显示。

### ![](/icons/tool_hide.webp) 使用隐藏 {#use-hide}
开启或关闭隐藏模式。关闭后隐藏仍然存在，只是暂时停用。如果您正在使用隐藏工具，这个按钮会被禁用。

### ![](/icons/shield.webp) 显示蒙版 {#show-mask}
开启或关闭蒙版模式。关闭后蒙版仍然存在，只是暂时停用。再次按下这个按钮即可重新启用。

如果您需要隐藏蒙版、同时又让它保持生效，可以把下面的蒙版颜色设为白色。用完后记得把它改回灰色！

请注意，如果您正在使用蒙版工具，这个按钮会被禁用。

### ![](/icons/shield.webp) 蒙版 → 不透明 {#mask-opaque}
`蒙版 → 不透明` 会让蒙版忽略透明的顶点。这只与顶点和纹理的不透明度有关，被“隐藏”的面仍然保持隐藏。只有在 `显示蒙版` 开启时才可用。

### ![](/icons/bang.webp) 高亮 {#highlight-quick}
开启或关闭选择时的高亮闪烁。选择物体时，所选物体会短暂闪烁 500 毫秒。闪烁的颜色和时长可以在下方自定义。

### ![](/icons/list.webp) 显示场景状态 {#stats-quick}
开启或关闭 3d 视口中的状态文字。它会显示系统内存、整个场景的顶点总数以及当前所选对象的顶点数等信息。

----- 

### ![](/icons/cube.webp) 使未选对象变暗 {#darken-unselected-objects}
未选中的物体会变暗，让当前所选对象更加突出。

### ![](/icons/shield.webp) 蒙版 {#mask}
蒙版使用的颜色，默认为中灰色，会与物体颜色相乘。设为白色可以让蒙版不可见，但用完后记得把它改回灰色！

## ![](/icons/cursor.webp) 光标 {#cursor}

### 圆形 {#show-circle-while-sculpting}
何时显示笔刷半径圆圈：

* `自动` - 显示圆圈，但雕刻时隐藏。
* `否` - 从不显示圆圈。
* `是` - 始终显示圆圈，雕刻时也显示。

### 显示指示点 {#show-small-dot}
雕刻时，或更改相机旋转中心时，在笔触中心显示一个小点。

### 显示稳定线 {#show-rope-stabilizer}
当笔触设置中启用了[拉绳稳定器](stroke.md#lazy-rope-stabilizer)时，绘制一条线来表示拉绳的长度。

### 显示滚转提示 {#show-roll-hint}
使用滚转快捷键时，显示滚转方向的引导。

### ![](/icons/radius.webp) 尺寸 {#dot-size}
小点的大小。

### 颜色 {#cursor-colors}
光标会根据您正在进行的操作改变颜色：`雕刻`、`背景`（悬停在背景上时）、`蒙版`、`平滑`、`相机` 和 `半径`。每种颜色都可以在这里自定义。

## ![](/icons/cursor.webp) 指示器 {#indicator}
![](/images/settings_indicator.webp)

为教程和屏幕录制显示可视化的指示器。设为 `是` 即可开启（iOS 上还有 `自动` 选项）。

启用 `手指`、`触控笔` 和 `鼠标` 按钮后，检测到对应类型的输入时就会显示一个图标。

### 颜色 {#indicator-color}
指示器的颜色。

### 尺寸/图标/圆形 {#indicator-shape}
用于调整指示器的大小，以及指示器中图标和圆圈的不透明度。

## ![](/icons/wireframe.webp) 线框 {#wireframe}
![](/images/settings_wireframe.webp)
启用线框叠加显示。

### 目标 {#target}
设置是让未选中的物体也显示线框，还是只有选中的物体显示，或者所有物体都显示。

### 隐藏 {#hide}
设置被隐藏的多边形是否仍然显示线框。

### 多分辨率：仅限级别 0 {#multiresolution-level-0-only}
多分辨率下，级别 0 的线框颜色较深，更高级别的线框逐渐变浅。启用这个选项后，只显示级别 0 的线框。

### 颜色 {#wireframe-color}
设置线框的颜色和不透明度。

## ![](/icons/grid.webp) 网格 {#grid}
![](/images/settings_grid.webp)
启用网格。

### 吸附 {#snap}
这些选项让基于曲线和形状的工具（`车削`、`圆管`、多边形和路径形状……）在绘制时让点吸附：

* `吸附到网格` - 吸附到网格上。
* `吸附到点（对齐视图）` - 当相机与某个轴对齐时，吸附到附近已有的点上。
* `吸附到点（自由视图）` - 当相机没有对齐时，吸附到附近已有的点上。

### 颜色 {#grid-color}
设置网格的颜色和不透明度。这些选项在网格可见时才会显示。

`晕影` 会让网格朝边缘逐渐淡出。`网格分割阈值` 以像素为单位，设置网格线在屏幕上可以变得多密，超过后网格会切换到另一个细分级别。

## ![](/icons/culling.webp)双面显示 {#two-sided}
可以从两侧看到多边形的面。

### 背面颜色 {#backface-color}
`背面着色` 用于给背面着色，`背面颜色` 设置着色的颜色。

## ![](/icons/outline.webp)轮廓 {#outline}
在选中的物体周围显示轮廓。

### 轮廓颜色、厚度 {#outline-color-thickness}
设置轮廓的颜色和 `厚度`。


## ![](/icons/bang.webp) 高亮 {#highlight}
在选择发生变化时短暂闪烁一下。
### 颜色、时长 {#color-duration}
设置闪烁的颜色和持续时间（毫秒）。

## ![](/icons/navigator.webp) 导航器 {#snap-cube}
![](/images/settings_snapcube.webp)

在场景角落显示一个辅助图标，用来快速切换前/后/左/右/上/下视图。轻点它的各个面即可在正交视图之间切换。

### 形状 {#shape}
为导航器选择球体、立方体或坐标轴（gnomon）形状。

### 限制对齐 {#restrict-alignment}
让吸附视图与世界坐标轴对齐。启用后，只能使用 6 个主视图。设为 `自动` 时，只有当相机处于 `转盘` 模式时才会应用这个限制。

### 尺寸 {#size}
设置导航器的大小。

### 翻转180° {#flip-180}
启用一种轻点行为：如果视图处于吸附状态，轻点导航器中心会把视图旋转 180 度。例如，视图吸附在正面时，轻点导航器会转到背面视图。

### 边和角 {#edges-corners}
在边和角上添加吸附视图（琥珀色区域）。坐标轴形状不支持此选项。

### 转盘式拖动 {#turntable-drag}
拖动导航器时旋转视图但不让相机滚转，并在每个吸附视图上停留。关闭后，拖动导航器会改用 `轨迹球` 方式旋转。无论哪种方式，拖动都只沿水平或垂直方向进行。如果相机使用 `转盘` 模式，导航器始终以这种方式拖动。

### 位置 {#snap-position}
设置导航器位于哪个角落。


## ![](/icons/list.webp) 显示场景状态 {#stats}
![](/images/settings_stats.webp)

显示系统内存、整个场景的顶点总数以及当前所选对象的顶点数等信息。

### 位置 {#stats-position}
设置状态信息位于哪个角落。

## ![](/icons/edit_radius.webp) 手柄 {#handle}
在视口中拖动的手柄（例如轴向变换控件）的相关设置。

### 数值输入 {#gizmo-input}
轻点轴向变换控件的某个部分时，允许输入数值。

### 自动隐藏 {#hide-on-interaction}
操作轴向变换控件时让它淡出，以免挡住视线。

### ![](/icons/opacity.webp) 不透明度 {#handle-opacity}
手柄的不透明度。

## ![](/icons/shape_lasso.webp) 形状 {#shape-settings}
用形状笔触（套索、矩形、曲线……）绘制的形状在屏幕上的显示方式。

### ![](/icons/opacity.webp) 填充、轮廓 {#shape-fill-outline}
形状内部及其外围线条的不透明度。

### 颜色 {#shape-colors}
每类工具的形状颜色：`蒙版`、`隐藏`、`面组` 和 `裁切`。

## ![](/icons/array.webp) 重复器 {#primitive-repeaters}
[重复器](scene#repeaters)（阵列、环形、曲线、表面）所生成副本的上限。当重复器失控时，这些上限能让 Nomad 保持流畅。

### ![](/icons/cube.webp) 最大副本数 {#repeater-max-copies}
单个重复器最多生成的副本数。无论物体大小，物体数量一多 Nomad 就会吃力。

### ![](/icons/cube.webp) 场景副本数 {#repeater-scene-copies}
整个场景的副本总配额。低面数的副本几何量很小，但仍然是一个完整的物体，所以小副本最先触及的就是这个上限。

### ![](/icons/triangle.webp) 面数限量 {#repeater-max-faces}
场景中所有副本的面数总配额。超出后，最重的物体会最先减少副本。

## ![](/icons/multires.webp) 多分辨率 {#multires}
### 最大顶点数量 {#multires-lowres-count}
设置一个阈值，不允许多分辨率细分操作超过这个顶点数，否则很可能导致 Nomad 崩溃：Nomad 在细分之前不会检查可用内存。默认值为 1000 万。
### 最低分辨率阈值 {#multires-lowres-threshold}
移动相机时，可以显示网格的较低分辨率版本。如果您希望显示更高分辨率的网格，可以调高这个值。

## 设置 {#advanced}
### ![](/icons/reset.webp) 恢复默认设置 {#reset}
将应用的所有偏好设置恢复为默认值。

有些资源是单独保存的，不会被重置：项目、快捷键、工具预设、HDR 环境、MatCap、Alpha、笔刷纹理和参考图像。随项目一起保存的所有内容，例如灯光、后期处理或相机视图，也都会保持不变。
