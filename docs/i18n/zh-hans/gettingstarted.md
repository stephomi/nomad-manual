# ![](/icons/play.webp) 入门 {#getting-started}

## 欢迎使用 Nomad！ {#welcome-to-nomad}

Nomad 是一款 3d 雕刻应用，可以在多种设备上运行，在配有压感触控笔的平板上体验最好，例如 Apple iPad 配 Apple Pencil，或者带触控笔的 Samsung Galaxy Tab。

它的灵感来自 ZBrush 和 Blender 这类桌面雕刻软件，注重让界面简单易懂，同时又不牺牲功能。如果您以前用过 3d 雕刻软件，会觉得 Nomad 非常熟悉。

如果这是您第一次接触 3d 雕刻，先了解一些基础知识会很有帮助。

::: tip 更喜欢看视频？
现在 YouTube 上有大量面向新手的视频教程，这里推荐几个很棒的：

* [Nomad Sculpt Crash Course（Dave Reed）](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Nomad Sculpt Beginner tutorial（Small Robot Studio）](https://www.youtube.com/watch?v=J644wXoTiww)
* [NOMAD FOR BEGINNERS 系列（SouthernGFX）](https://www.youtube.com/watch?v=bEh0WxRoOmg)

值得去这些创作者的主频道看看，他们经常发布新教程。
:::

## 您的第一个雕刻 {#your-first-sculpt}

第一次启动 Nomad 时，屏幕上会有一个球体。只要用触控笔在球体上拖动，就可以开始雕刻了。对称默认是开启的，让雕刻更轻松。

![](/videos/gettingstarted_01.mp4)

要调大或调小笔刷，请使用左侧的半径滑块。

![](/videos/gettingstarted_02.mp4)

要让笔刷更强或更弱，请使用左侧的强度滑块。

![](/videos/gettingstarted_03.mp4)

默认工具是 `黏土` 工具，它会在表面上堆加。要从表面上削减，请轻点左侧的 `反向` 按钮。要恢复堆加，再轻点一次反向按钮即可。

![](/videos/gettingstarted_04.mp4)

要平滑表面，请轻点 `平滑` 按钮。要回到正常雕刻，再轻点一次平滑按钮即可。

![](/videos/gettingstarted_05.mp4)

要绕着模型旋转，请在模型外的空白处拖动。

![](/videos/gettingstarted_06.mp4)

要缩放视图，请使用双指捏合手势。

![](/videos/gettingstarted_07.mp4)

要平移相机，请用两根手指按住屏幕并拖动。

![](/videos/gettingstarted_08.mp4)

如果操作失误，双指轻点即可撤销，也可以使用左下角的撤销按钮。

![](/videos/gettingstarted_09.mp4)

::: tip 桌面版
在桌面版上，alt/opt 键用来控制相机：

* 笔尖在空白处拖动 = 旋转相机
* alt + 笔尖拖动 = 平移
* alt + 笔尖拖动，然后松开 alt = 缩放（与 ZBrush 相同）

如果您使用的 Wacom 数位板的笔上有 2 个或更多按键，可以在 Wacom 设置中这样配置笔尖和按键：

* 笔尖 = 左键单击
* 下侧按键 = 中键单击
* 上侧按键 = 右键单击

这样设置后，只用笔就能操作相机：

* 按住上侧按键并悬停移动 = 旋转相机
* 按住下侧按键并悬停移动 = 平移
:::

## 添加颜色 {#add-color}

Nomad 可以在雕刻作品的表面上绘画。在右侧的工具菜单中找到 `绘画` 工具并点击它。左侧工具栏上会出现一个彩色小球。点击它会弹出颜色选择器。选好颜色，就可以在模型上绘画了。

![](/videos/gettingstarted_10.mp4)

要擦除，请轻点左侧工具栏上的 `擦除` 按钮，然后在表面上擦除。再轻点一次擦除按钮即可回到绘画模式。

![](/videos/gettingstarted_11.mp4)

用黏土笔刷的堆加/削减模式、平滑和绘画，试试看能不能做出一个简单的卡通头像：

![](/images/gettingstarted_head1.webp)

## 其他工具 {#other-tools}

工具面板中有许多帮助雕刻的工具。到目前为止，您已经用过黏土笔刷（默认的起始工具）、平滑和绘画。由于平滑非常常用，左侧工具栏中还有它的额外快捷方式。

Nomad 的工具能做的事情非常多，既有移动、折痕、膨胀这类与雕刻相关的工具，也有分割和裁切这类更像木工或金工工具的工具。更多信息请参阅[工具](tools.md)页面。

试试用移动、折痕、膨胀和平滑工具为头像添加更多细节，改变它的形状：

![](/images/gettingstarted_head2.webp)

现在您已经了解了 Nomad 的基础知识，下面来看看界面的其余部分。

## 界面 {#interface}

![](/images/interface_overview1.webp)

* `顶部菜单` - 通过这些菜单可以使用 Nomad 的大部分功能。左上方的菜单主要涉及场景和物体功能，右上方的菜单与工具相关。在较小的屏幕上，这些菜单会折叠在一起以节省空间。
* `显示场景状态` - 关于场景、当前物体、蒙版状态和内存使用的信息。
* `导航立方体` - 一个辅助工具，显示您正在看雕刻作品的哪一面，同时也是跳转到不同视图的快捷方式。轻点立方体会把视图跳转到被点的那一面，拖动立方体则会旋转视图。轻点立方体旁的小图标，可以框选当前物体、重置为默认的初始视图、锁定相机或开关网格。在应用中它叫作 `方位视图`，它的外观和位置可以在[设置](settings.md#snap-cube)中修改。
* `工具箱` - 可以在这个可滚动区域中找到 Nomad 的工具。
* `左侧工具栏` - 大多数工具的半径和强度滑块、其他工具的上下文相关按钮，以及对称、工具的反向模式、平滑、蒙版、隐藏、面组、轴向变换和绘画选项的快捷方式。您可以在[界面](interface.md#side-bar)菜单中调整这些快捷方式的顺序。
* `底部工具栏` - 常用功能的快捷方式，下面会逐一说明。

::: tip 左撇子？
您可以镜像所有工具栏的位置和顺序，参见[翻转顶部菜单栏](interface.md#mirror-top-bar)及其他相关选项。
:::

## 底部工具栏 {#bottom-toolbar}

![](/images/interface_bottom_toolbar.webp)

* `撤销` - 撤销上一步操作
* `重做` - 恢复上一次撤销的操作
* `历史记录` - 打开历史记录选项，详见[历史记录](history.md)菜单。
* `独显` - 切换只显示当前物体，还是显示所有物体
* `X光` - 让其他所有物体以 X 光模式显示，而当前物体保持实心。长按或向上轻扫可以选择 X 光使用的材质捕捉和颜色，以及它应用于哪些物体。
* `体素` - [体素网格重构](topology.md#voxel-remesher)中重构按钮的快捷方式。长按或向上轻扫会显示体素网格重构的选项，例如分辨率。
* `世界网格` - 开关网格显示。长按或向上轻扫会显示网格的选项，例如颜色和吸附。
* `线框` - 开关线框叠加显示。长按或向上轻扫会显示线框的选项。
* `检查器` - 开关显示当前网格的额外数据。默认显示 UV，长按或向上轻扫可以查看其他已有的属性，并选择在背景上还是在网格上显示。
* `调试日志` - 显示或隐藏 Nomad 的调试日志窗口。
* `面组` - 开关面组叠加显示，参见[面组](tools.md#facegroup)工具。

您可以在[界面](interface.md#add-shortcuts-bottom)菜单中添加、移除这些快捷方式并调整它们的顺序。

## 下一步 {#next-steps}

接下来学什么，完全取决于您和您感兴趣的内容！这里有一些建议：

想深入了解雕刻工具？请前往[工具](tools.md)部分。

想导出模型？或者导入模型来雕刻？或者为雕刻作品生成图像？请前往[文件](files.md)部分。

想进一步学习如何控制雕刻作品的细节？请前往[拓扑](topology.md)部分，了解多分辨率和网格简化。

想处理更多物体？把简单物体和基本体组合成更大的场景？请前往[场景](scene.md)部分。

想了解 Nomad 的*一切*？好选择！这本手册涵盖了 Nomad 的全部内容，包含大量技巧和窍门，顶部还有很好用的搜索功能。使用左侧的导航来了解更多吧。

如果您更喜欢看视频，Holger Schönischka 在 YouTube 上制作了大量 Nomad 技巧合集：https://www.youtube.com/@ProcreateFX/videos


## 获取帮助 {#getting-help}

如果读完手册、看完教程视频后仍有疑问，有三种主要方式可以和其他 Nomad 用户或 Nomad 的开发者交流：

* 访问论坛：[forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* 加入 Nomad 的 Discord 聊天：[https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* 直接发邮件联系开发者：support@nomadsculpt.com
