# ![](/icons/interface.webp) 界面菜单 

此菜单控制许多用于自定义 Nomad 界面的选项。 

![](/images/interface_overview2.webp)

Nomad 可以进行非常深入的自定义，本菜单分为 4 个部分：Interface、Gesture、Bindings、Debug。

![](/images/interface_menu.webp)


::: tip
本页介绍的是“界面菜单”，不是界面本身！整体界面说明见 [Getting Started](gettingstarted.md)。
:::

## Interface 

Interface 部分允许你添加快捷方式、创建浮动工具栏，并控制 Nomad 用户界面的颜色、尺寸和外观。

![](/images/interface_overview3.webp)

### Add shortcuts (bottom)...
![](/images/interface_shortcuts.webp)

底部工具栏默认启用以下快捷方式：
* `Undo` - 撤销上一步操作
* `Redo` - 恢复上一次被撤销的操作
* `Solo` - 临时隐藏其他所有对象，仅保留当前选中对象可见。再次点击恢复所有对象。
* `X-ray` - 临时将其他所有对象变为半透明，仅保留当前选中对象为实心。再次点击恢复默认材质。
* `Voxel remesh` - 使用上一次使用的体素分辨率对当前对象重新网格化。长按或向上滑动会弹出分辨率滑块和锐边开关。
* `Grid` - 切换视图网格显示。长按或向上滑动可以更改网格的颜色和不透明度。
* `Wireframe` - 切换线框叠加显示。长按或向上滑动可以更改线框的颜色和不透明度。
* `Inspector` - 允许你在 Nomad 背景上叠加查看网格的属性，如 UV、烘焙贴图及其他属性。
* `Face Group` - 切换面组叠加显示，更多信息见 [Tools->FaceGroup](tools.md#facegroup) 

此菜单中还提供其他常用快捷方式，更多功能可在 bindings 按钮中找到。

#### ![](/icons/more.webp) Bindings

Nomad 的几乎所有功能都可以通过 bindings 按钮添加到底部快捷工具栏。点击按钮会显示绑定菜单：

![](/images/interface_bindings_search.webp)

你可以通过顶部图标按类别搜索，或使用搜索框按名称查找功能。点击某个功能即可将其添加到工具栏，再次点击则将其移除。

#### ![](/icons/list.webp) Order

显示快捷方式列表。长按并拖动以重新排序快捷方式。

#### ![](/icons/reset.webp) Reset

Reset 会将底部工具栏恢复为默认设置。

### Add shortcuts (window)... +
![](/images/interface_add_shortcuts_window.webp)

点击 + 会添加一个浮动工具栏。在你点击 bindings 按钮并为其添加一些快捷方式之前，它是不可见的，添加后即可将其设为可见。 

你可以创建多个工具栏，每个工具栏在此菜单中都有以下选项：

* ![](/icons/checked.webp) `Visible` - 切换该工具栏的可见性
* ![](/icons/more.webp)`Bindings` - 显示绑定窗口，用于选择要添加到工具栏或从工具栏移除的功能。
* ![](/icons/list.webp)`Order` - 显示一个菜单以重新排序该工具栏。
* ![](/icons/reset.webp) `Reset` - 将该工具栏重置为默认状态。
* ![](/icons/resize_bottom_right.webp) `Resize corner` - 在工具栏右下角切换一个缩放控件。
* ![](/icons/sort_down.webp) `Collapsable` - 在右上角切换一个折叠控件。
* ![](/icons/trash.webp) `Delete` - 删除该工具栏。

### Toolbox

用于控制 Nomad 界面右侧工具菜单的选项。

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Ui Resize Corner

在工具栏底部角落切换一个缩放控件。

#### Hidden
通常顶部栏中的 toolbox 图标会在“单列长列表”和“多列工具列表”之间切换。启用此选项后，将在“多列列表”和“隐藏”之间切换。

#### Colored
按类别为图标着色，例如所有 Mask 工具为棕色，Split 工具为红色，Flatten 工具为绿色等。

#### Rows: Auto (>1)

#### Rows: Auto (>1)

#### Reset order
将 toolbox 中的默认工具恢复为默认顺序。自定义图标会保留在列表末尾。

### Presets

![](/images/interface_presets.webp)

一组界面颜色预设。

#### High-contrast button
按钮的另一种样式，使启用状态更明显。如果设置为 Auto，当启用/禁用状态的 UI 颜色对比度较低时，Nomad 会自动使用此模式。

#### Color widget/Color base
界面中使用的主色。

#### Transparent panel, Color panel, Blur strength
![](/images/interface_transparent.webp)
启用后，会出现额外选项，用于控制 Nomad 中菜单和面板的外观。可以调整它们的颜色、透明度和模糊强度。

::: tip
在小屏设备上，将颜色面板设为接近白色、半透明且低模糊强度，可以避免菜单遮挡场景。
:::

----

### Mirror top bar
反转顶部栏中菜单的顺序。

### Mirror side bars
交换侧边栏位置，使 toolbox 在左侧，工具选项在右侧。

### Mirror bottom bar
将底部栏移动到右下角，并反转按钮顺序。

### Material color preview
当你为材质选择颜色时，会在当前选中对象上显示该材质的预览。

----
### Help popup on hover

对于支持悬停的设备，控制 Nomad 中的上下文帮助（![](/icons/help.webp) 图标）是在悬停时显示，还是仅在点击时显示。

----

### Overall scale
对所有 UI 元素的尺寸进行整体缩放。

### Panel width
菜单和面板的宽度。

### Font scale
字体缩放。

### Vertical spacing
菜单和面板中元素之间的垂直间距。

### Vertical spacing (left)
左侧工具栏中元素之间的垂直间距。

----

### Edge offset
只有在你在屏幕边缘与按钮交互出现问题时才应修改这些值。如果这些滑块是禁用状态，Nomad 会使用设备自身返回的安全区域值。

::: tip
将 Nomad 迁移到新设备（例如从 iPhone 12 换到 iPhone 15）时，请务必将 Edge 选项重置为默认值！
:::

### Reset style
将所有 UI 元素重置为默认值。


## Gesture
Gesture 菜单控制手写笔和手指按压如何操控 Nomad。

![](/images/interface_gesture.webp)

### Gesture options
![](/images/interface_gesture_matrix.webp)

Nomad 可以根据输入设备限制操作。例如，手指拖动只能移动相机，而手写笔拖动只能雕刻。如果你有鼠标或触控板，也可以将其分配给特定操作。

Nomad 目前允许你为以下模式设置由手指、手写笔或鼠标手势的任意组合来控制：

* Camera
* Sculpt
* Gizmo
* Material picking（通过长按）
* Select object


`Finger always smooths` - 可以设置仅通过手指拖动来执行 Smooth。

### ![](/icons/tool_mask.webp) Mask

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - 启用后，无需按住 Mask 按钮即可使用以下单击快捷操作，将允许以下手势：
* 点击背景以反转 Mask
* 点击已 Mask 区域以模糊 Mask
* 点击未 Mask 区域以锐化 Mask

### Toggle Mask <-> SelMask
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - 长按会在 Mask 和 SelMask 之间切换并开始新的笔划。在笔划结束时，会重新选中之前的工具。 
* `Tool` - 长按并在不移动的情况下松开，以在 Mask 和 SelMask 之间切换。 

### ![](/icons/tool_hide.webp) Hide
![](/images/interface_gesture_hide.webp)

启用 `One tap shortcuts` 后，Hide 工具会支持以下快捷操作：
* 点击一个面组以隐藏它
* 点击空白区域以反转隐藏多边形

### ![](/icons/finger3.webp) Three fingers
![](/images/interface_gesture_threefingers.webp)

如果你的设备支持三指手势，可以为该手势配置快捷操作。 

选项矩阵允许你将垂直和水平拖动定义为不同的快捷操作。注意，如果同一手势被分配给两个选项，其中一个会被禁用。

* `Rotate lighting` - 旋转环境、灯光和 Matcap。
* `Tool Radius` - 调整工具半径。
* `Tool Intensity` - 调整工具强度。 

### ![](/icons/fingerprint.webp) History 2/3
`History shortcuts` - 启用后，以下手势生效：
* Undo - 两指点击
* Redo - 三指点击

`Long press` - 启用后，按住 2/3 根手指会快速连续撤销/重做。

### Accessibility 

![](/images/interface_gesture_accessibility.webp)

`Assistive window` 会弹出一个浮动工具栏，用于控制拖动、捏合、旋转和相机操作。

### Camera
跳转到 `Camera` 菜单的快捷方式（相机选项原本在此处，现已移至 Camera 菜单）。

### Pencil double tap -> Bindings 

跳转到 `Bindings` 菜单的快捷方式（Pencil 单击和双击选项原本在此处，现已移至 Bindings 菜单）。


## Bindings
可以在 Bindings 菜单中定义键盘和按钮快捷方式：

![](/images/interface_bindings.webp)
如果你的设备有键盘，Nomad 中几乎所有功能都可以绑定到键盘快捷键，也可以绑定到手写笔的额外按钮，甚至是游戏手柄。

要创建绑定，点击功能旁边的矩形，然后按下按键/按钮。 

可以通过顶部的类别图标查找功能，或通过搜索栏按名称查找。 

可以通过绑定名称旁的复选框禁用单个绑定。

### ![](/icons/more.webp) Context menu
每个绑定后面的 ![](/icons/more.webp) 图标会弹出一个上下文菜单：

![](/images/interface_bindings_context.webp)

* `Clone` - 克隆该绑定
* `Reset` - 重置该绑定
* `Delete` - 删除该绑定
* `Toggle shortcut on key tap` - 配置点击与长按是否区别对待。启用后，点击会激活该工具；长按则只在按住按键时激活该工具，松开后会返回到之前的工具。在其他 3D 软件中有时称为“粘滞键（sticky keys）”。

### Advanced
Bindings 菜单底部有一个齿轮菜单用于高级选项：

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - 对于 Mask、Smooth、Gizmo、Hide、Sub 等标准快捷键，点击会切换到该模式，而按住则会临时切换到该模式，松开后恢复到之前的模式。在其他 3D 软件中有时称为“粘滞键（sticky keys）”。
* `Toggle tool shortcuts` - 使用某个工具快捷键时，如果连续按两次同一快捷键，会在当前工具和上一个工具之间切换。这样你可以用同一个热键在两个工具之间来回切换。
* `Invert Y (Zooming)` - 反转缩放方向。
* `Reset bindings` - 将所有绑定重置为默认值。


## iOS ⌘ 键盘快捷键显示

在带键盘的 iOS 设备上，按住 ⌘（cmd）键会显示快捷键列表。

Android 的键盘支持仍然有些实验性质。

![](/images/shortcuts.webp)


## Debug
一些实验性和调试选项存放在此菜单中。许多选项应保持默认，仅在联系 Nomad 支持后再进行修改。

![](/images/interface_debug.webp)
### UV
* `Normalize Uvs` - Nomad 会将 UV 归一化到 [0-1] 贴图块内。

### Quad Remesh
* `Instant Mesh` - 启用 Instant Remesh 算法
* `Quadriflow` - 另一种四边形重拓扑方法。

### Render
* `Heightmap` - 将视口切换为渲染场景深度。可用于创建用于笔刷的 Alpha 贴图。
* `Refraction write depth (back)` - 折射网格的背面会写入深度缓冲。
* `Flip Y (normal map)` - 烘焙法线贴图时反转 Y 通道，一些游戏和渲染引擎需要此设置。
* `Angle weighted smooth normals` - 对平滑着色方式的调整，可在某些情况下避免产生折痕。

### Target FPS
禁用时，Nomad 会将帧率与显示器刷新率同步。

启用后，你可以设置 Nomad 渲染的目标帧率。

### Interface
* `Top: layout` 
  * Collapse: 在小屏设备上，顶部栏会折叠为更多子菜单。 
  * Scroll: 如果你习惯在大屏设备上使用 Nomad 并偏好正常布局，启用此项会使用标准的宽顶部栏，并允许横向滚动。
  * Multiline: 将整个顶部菜单显示为多行。
* `Bottom: draggable popup` - 底部工具栏中有多个按钮会弹出对话框。启用此选项后，这些对话框可以被拖动到屏幕其他位置。  
* `Toolbox: show all` - Nomad 会隐藏与当前选择无关的工具，例如在未验证的原始体上会隐藏所有雕刻笔刷。启用此选项后，这些工具会以禁用状态变暗显示，而不是被隐藏。
* `Toolbox: colored` - 按类型为 toolbox 图标着色。
* `Panel: Drop shadows` - 在菜单和面板周围绘制投影。在某些老设备上可能影响性能。
* `Panel: Blending` - 调试选项
* `Pointer: hovering dot` - 对于支持手写笔悬停的设备，在手写笔悬停于菜单和面板上时显示一个小点。

### Gif turntable
Nomad 可以导出旋转台动画 gif。由于 gif 格式的限制，画质较低。通常使用屏幕录制会更好。

* `Duration` - 旋转台动画的时长（秒）
* `Rotation center` - 相机枢轴的位置，即相机围绕场景中哪一部分旋转
* `Transparent background` - 为 gif 使用透明背景。注意 gif 仅支持 1 位透明度，因此边缘可能会出现严重锯齿。
* `Max frame sampling` - Nomad 的许多高质量渲染效果通过合成多帧实现。此滑块设置要合成的帧数。
* `Export (GIF)` - 开始 gif 导出流程。

### Post Process
* `Filtering` - 调试选项
* `Format` - 调试选项
* `Buffer reuse` - 调试选项

### Performance
* `Multicore general` - 调试选项
* `Multicore sculpting` - 调试选项
* `Partial Drawing` - 实验功能！当你只在高面数网格的局部区域雕刻时可使用。它应能让雕刻更流畅，但请不要启用线框显示！同时在笔刷笔划过程中可能会出现视觉伪影。

### Feature
* `Flip quad split (on tap)` -  调试选项
* `Join: merge radius` - 当网格合并时，如果顶点足够接近会自动焊接。你可以通过此滑块调整焊接半径。

### Debug
* `Logs` - 弹出日志视图
* `App review popup` - 调试选项
* `FPS` - 在视口统计信息中添加帧率计数器。
