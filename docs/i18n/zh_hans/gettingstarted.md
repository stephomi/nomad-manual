# 入门指南

## 欢迎使用 Nomad！

Nomad 是一款 3D 雕刻应用，可以在多种设备上运行，在配有压感手写笔的平板电脑上体验最佳，例如带 Apple Pencil 的 iPad，或带手写笔的三星 Galaxy Tab。

它的灵感来自桌面雕刻软件，如 ZBrush 和 Blender，重点是提供易于理解的界面，同时不牺牲功能。如果你之前用过 3D 雕刻软件，Nomad 会让你感到非常熟悉。

如果这是你第一次进行 3D 雕刻，那么先了解一些基础知识会很有帮助。

::: tip 更喜欢视频？
YouTube 上现在有大量的入门视频教程，这里是一些很好的链接：

* [Nomad Sculpt Crash Course by Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Nomad Sculpt Beginner tutorial by Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [NOMAD FOR BEGINNERS series by SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

值得去看看这些作者的主频道，他们经常发布新的教程。
:::

## 你的第一个雕刻

第一次启动 Nomad 时，你会在屏幕上看到一个球体。只需用手写笔在球体上拖动即可开始雕刻。默认启用了对称功能，以便更轻松地雕刻。

![](/videos/gettingstarted_01.mp4)

要让笔刷变大或变小，使用左侧的半径滑块。

![](/videos/gettingstarted_02.mp4)

要让笔刷变强或变弱，使用左侧的强度滑块。

![](/videos/gettingstarted_03.mp4)

默认工具是 `Clay tool`（粘土工具），它会向表面添加体积。要从表面减去体积，点击左侧的 `Sub` 按钮。要恢复为添加体积，再次点击 Sub 按钮。

![](/videos/gettingstarted_04.mp4)

要平滑表面，点击 `Smooth` 按钮。要返回普通雕刻模式，再次点击 Smooth 按钮。

![](/videos/gettingstarted_05.mp4)

要绕模型旋转视角，在模型外的空白区域拖动。

![](/videos/gettingstarted_06.mp4)

要缩放，使用双指捏合/放大手势。

![](/videos/gettingstarted_07.mp4)

要平移相机，用两根手指按住屏幕并拖动。

![](/videos/gettingstarted_08.mp4)

如果你操作失误，双指轻点可以撤销，或者使用左下角的撤销按钮。

![](/videos/gettingstarted_09.mp4)

::: tip 桌面版
在桌面端，alt/opt 键用于控制相机：

* 触控笔在空白区域拖动 = 旋转相机
* alt+触控笔拖动 = 平移
* alt+触控笔拖动，然后松开 alt = 缩放（与 ZBrush 相同）

对于带有两个或更多按键的 Wacom 手写笔，可在 Wacom 设置中将笔尖和按键配置为：

* 笔尖 = 左键单击
* 下摇杆键 = 中键单击
* 上摇杆键 = 右键单击

使用这些设置，你可以只用手写笔来操控相机：

* 上摇杆键 + 悬停移动 = 旋转相机
* 下摇杆键 + 悬停移动 = 平移
:::

## 添加颜色

Nomad 允许你在雕刻表面上进行绘画。在右侧工具菜单中找到 `Paint`（绘画）工具并点击。左侧工具栏会出现一个彩色球体。点击它，会弹出颜色选择器。选择一种颜色，然后在模型上绘画。

![](/videos/gettingstarted_10.mp4)

要擦除，点击左侧工具栏的 `Erase`（擦除）按钮，然后在表面上擦除。再次点击擦除按钮即可返回绘画模式。

![](/videos/gettingstarted_11.mp4)

使用粘土笔刷的添加/减去模式、平滑和绘画，试着做一个简单的卡通头：

![](/images/gettingstarted_head1.webp)

## 其他工具

工具面板中有许多有助于雕刻的工具。到目前为止，你已经使用了粘土笔刷（默认起始工具）、平滑和绘画。由于平滑使用频率很高，它在左侧工具栏中还有一个额外的快捷方式。

Nomad 中的工具可以完成各种各样的操作，从雕刻相关的工具（如移动、折痕、膨胀），到类似木工或金工的工具（如分割和修剪）。[Tools](tools.md) 页面有更多信息。

试着使用移动、折痕、膨胀和平滑工具，为你的头部增加更多细节，改变它的形状：

![](/images/gettingstarted_head2.webp)

现在你已经了解了 Nomad 的基础知识，接下来看看其余界面。

## 界面

![](/images/interface_overview1.webp)

* `顶部菜单` - 用于访问 Nomad 大部分功能的菜单。左上角菜单主要涵盖场景和对象相关功能，右上角菜单与工具相关。在较小屏幕上，这些菜单会折叠在一起以节省空间。
* `状态信息` - 关于场景、当前对象、遮罩状态和内存使用情况的信息。
* `导航立方体（Nav Cube）` - 帮助你了解当前从哪个方向观察雕刻，同时也是快速切换视图的快捷方式。点击立方体会将视图跳转到被点击的那一面。拖动立方体会旋转视图。点击立方体旁的小图标可以框选当前对象，或重置到默认主视图。
* `工具箱` - Nomad 的工具都在这个可滚动区域中。
* `左侧工具栏` - 大多数工具的半径和强度滑块、其他工具的上下文按钮，以及对称、工具的 alt/sub 模式、遮罩、平滑、Gizmo 和绘画选项的快捷方式。
* `底部工具栏` - 常用功能的快捷方式，详见下文说明。

::: tip 左撇子？
你可以镜像所有工具栏的位置和顺序，参见 [Mirror top bar](interface.md#mirror-top-bar) 以及其他相关选项。
:::

## 底部工具栏

![](/images/interface_bottom_toolbar.webp)

* `Undo` - 撤销上一次操作
* `Redo` - 恢复上一次被撤销的操作
* `History` - 访问历史记录选项，详见 [History](history.md) 菜单。
* `Solo` - 在仅显示当前对象和显示所有对象之间切换
* `X-Ray` - 让所有其他对象以透视（X 光）模式渲染，而当前对象保持实体显示。长按或向上滑动可以设置 X 光模式的颜色和不透明度。
* `Voxel` - [Voxel Remesher](topology.md#voxel-remesher) 体素重拓扑按钮的快捷方式。长按或向上滑动可以快速设置体素重拓扑质量。
* `Grid` - 切换网格显示。长按或向上滑动可以显示网格选项。
* `Wire` - 切换线框覆盖显示。长按或向上滑动可以显示线框选项。
* `Inspect` - 切换查看当前网格的额外数据。默认显示 UV，但长按或向上滑动可以在存在其他属性时进行检查，并选择是在背景中还是在网格上显示。

## 下一步

接下来学什么取决于你自己，以及你对什么感兴趣！这里有一些建议：

想进一步了解雕刻工具？前往 [Tools](tools.md) 章节。

想导出你的模型？或者导入模型进行雕刻？或者为你的雕刻创建图像？前往 [Files](files.md) 章节。

想进一步了解如何控制雕刻的细节？前往 [Topology](topology.md) 章节，学习多重分辨率和简化。

想使用更多对象？将简单对象和基本体组合成更大的场景？前往 [Scene](scene.md) 章节。

想要了解 Nomad 的*全部*内容？不错的选择！本手册涵盖 Nomad 的所有内容，包含大量技巧，并在顶部提供了强大的搜索功能。使用左侧的导航来了解更多。

如果你更喜欢视频，Holger Schönischka 在 YouTube 上制作了大量 Nomad 的技巧合集：https://www.youtube.com/@ProcreateFX/videos


## 获取帮助

如果在阅读手册和观看教程视频之后你仍然有问题，有三种主要方式可以与其他 Nomad 用户或 Nomad 的开发者交流：

* 访问论坛：[forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* 加入 Nomad 的 Discord 聊天：[https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* 直接联系开发者：support@nomadsculpt.com
