# ![](/icons/cog.webp) 设置 {#reset-to-default}

设置菜单包含许多用于控制 Nomad 外观和行为的选项。

![](/images/settings_overview.webp)

## 显示设置 {#display-settings}
本节包含本菜单下方大部分设置的快速启动快捷方式。

![](/images/settings_display_settings.webp)

### 平滑着色 {#smooth-shading}
在平滑着色和棱面着色之间切换。使用棱面着色时，多边形会被独立着色，因此你可以看到底层拓扑结构。
在雕刻阶段查看棱面着色会很有用，然后在渲染时切换回平滑着色。

禁用平滑着色会略微提升性能。

### 轮廓线 {#outline-quick}
切换当前选中对象的轮廓线显示。

当 [变暗未选中对象](#darken-unselected-objects) 被禁用时，这有助于获得当前选中网格的可视化反馈。

从性能角度来看，使用 [变暗未选中对象](#darken-unselected-objects) 比使用轮廓线方案要好得多。

### 网格 {#grid-quick}
切换背景网格显示，有助于理解对象的位置和比例。

### 双面 {#two-sided-quick}
切换多边形双面显示。所有面都有一个指向的方向。
被视为 *背面* 的面是那些“背向”相机视角的面。

例如，启动时的简单球体，其面会朝向外侧。
如果你将相机移动到球体内部，你就会看到这些面的背面。

大多数情况下你不应该看到面的背面，因此给它们上色可以帮助你发现潜在问题或错误的拓扑。

禁用 `双面` 渲染可以略微提升渲染性能。

### 线框 {#wireframe-quick}
切换线框叠加显示。

请注意，启用线框会降低性能。

### 捕捉方块 {#snap-cube-quick}
切换场景角落中的辅助图标，有助于在空间中为自己定向，并快速在前/后/左/右/上/下视图之间切换。

### 显示绘画 {#show-painting}
切换绘制显示。默认使用的是白色、非金属材质，粗糙度为 25%。

### 使用隐藏 {#use-hide}
切换隐藏模式。关闭时功能仍然存在，只是被停用。如果你当前正在使用隐藏工具，此按钮会被禁用。

### 显示遮罩 {#show-mask}
切换遮罩模式。关闭时功能仍然存在，只是被停用。再次按下此按钮可重新启用。

如果你需要隐藏遮罩但仍让其保持激活状态，请使用下面的遮罩颜色并将其设置为白色。完成后记得将其改回灰色！

请注意，如果你当前正在使用遮罩工具，此按钮会被禁用。

### 遮罩 -> 不透明 {#mask-opaque}
遮罩 -> 不透明 会在遮罩时忽略透明顶点。这只与顶点和纹理不透明度相关，被“隐藏”工具隐藏的面仍然会被隐藏。

### 高亮 {#highlight-quick}
切换选中高亮闪烁。当选择对象时，将选中对象以亮粉色短暂闪烁 500 毫秒。闪烁的颜色和时长可以在下方自定义。

### 统计信息 {#stats-quick}
切换 3D 视口中的状态文本显示。这里会显示系统内存、场景总顶点数以及当前选中对象的顶点数信息。

-----

### 变暗未选中对象 {#darken-unselected-objects}
未被选中的对象会被变暗，以便当前选中对象更加突出。

### 遮罩 {#mask}
用于遮罩的颜色，默认是中灰色，会与对象颜色相乘。将其设置为白色可以让遮罩不可见，但完成后记得改回灰色！

## ![](/icons/cursor.webp) 光标 {#cursor}

### 雕刻时显示圆圈 {#show-circle-while-sculpting}
在雕刻时持续显示笔刷半径。

### 显示小点 {#show-small-dot}
在雕刻时或相机枢轴改变时，在笔刷笔触中心显示一个小点。

### 显示绳索稳定器 {#show-rope-stabilizer}
当在笔触设置中启用惰性绳索稳定器时，绘制一条线来指示绳索长度。

## ![](/icons/cursor.webp) 指示器 {#indicator}
![](/images/settings_indicator.webp)

为教程和屏幕录制显示可视化指示器。

`手指`、`触控笔` 和 `鼠标` 按钮会在检测到对应输入类型时显示一个图标。

### 颜色 {#indicator-color}
指示器的颜色。

### 大小/图标/圆圈 {#indicator-shape}
用于调整指示器整体大小以及内部形状的控制项。

## ![](/icons/wireframe.webp) 线框 {#wireframe}
![](/images/settings_wireframe.webp)
启用线框叠加显示。

### 目标 {#target}
设置未选中对象是否显示线框，或仅选中对象显示，或所有对象都显示。

### 隐藏 {#hide}
设置线框是否仍会在被隐藏的多边形上显示。

### 多重分辨率：仅级别 0 {#multiresolution-level-0-only}
多重分辨率会将 0 级线框显示得更深色，更高等级则逐渐变浅。启用此选项时，只会显示 0 级线框。

### 颜色 {#wireframe-color}
设置线框的颜色和不透明度。

## ![](/icons/grid.webp) 网格 {#grid}
![](/images/settings_grid.webp)
启用网格。

### 颜色 {#grid-color}
设置网格颜色和不透明度。

### 捕捉 {#snap}
为基于曲线的工具启用对网格的吸附。

## ![](/icons/culling.webp)Two sided {#two-sided}
启用从两侧查看多边形面。

### 反面上色，反面颜色 {#backface-color}
启用背面着色以及背面着色的颜色。

## ![](/icons/outline.webp)Outline {#outline}
为活动对象启用轮廓线。

### 轮廓颜色，粗细 {#outline-color-thickness}
设置轮廓线的颜色和粗细。

## ![](/icons/bang.webp) 高亮 {#highlight}
在活动对象改变时启用短暂闪烁。
### 颜色，持续时间 {#color-duration}
以毫秒为单位设置闪烁的颜色和持续时间。

## ![](/icons/snap_cube.webp) 捕捉方块 {#snap-cube}
![](/images/settings_snapcube.webp)

在场景角落显示一个辅助图标，用于快速在前/后/左/右/上/下视图之间切换。点击立方体的各个面可在正交视图之间切换。

### 形状 {#shape}
为对齐立方体在立方体、球体或指示器（gnomon）形状之间进行选择。

### 限制对齐 {#restrict-alignment}
在拖动对齐立方体时启用相机旋转锁定。启用后，在对齐立方体上的拖动只会左右或上下移动。

### 大小 {#size}
设置对齐立方体的大小。

### 翻转 180 {#flip-180}
启用点击行为：当视图已对齐时，点击立方体中心会将视图旋转 180 度。例如，如果视图对齐到前视图，点击视图立方体会旋转到后视图。

### 位置 {#snap-position}
设置对齐立方体所在的角落。

## ![](/icons/edit_radius_n.webp) 统计信息 {#stats}
![](/images/settings_stats.webp)

显示系统内存、场景总顶点数以及当前选中对象顶点数的信息。

### 位置 {#stats-position}
设置统计信息显示所在的角落。

## 基元/重复器 {#primitive-repeaters}
## 数值输入 {#gizmo-input}
允许在点击 Gizmo 控件时进行数值输入。

## 多重分辨率 {#multires}
### 最大顶点数 {#multires-lowres-count}
设置一个阈值，不允许多重分辨率细分操作超过此多边形数量，否则可能导致 Nomad 崩溃。默认值为 1000 万。

### 低分辨率阈值 {#multires-lowres-threshold}
在你移动相机时可以显示网格的较低分辨率版本。如果你希望显示更高分辨率的网格，可以提高此数值。

## 设置 {#advanced}
### 重置为默认 {#reset}
将所有设置重置为默认值。