# ![](/icons/faq.webp) 常见问题 {#faq}

[[toc]]

## 平台 {#platform}
### 我设备上的项目存储在哪里？ {#locate}
项目位于 Nomad 主文件夹中的 `projects` 文件夹内。

在 iOS 上，你可以通过 iOS 的“文件”应用访问 Nomad 文件夹。

在 Android 上，Nomad 文件夹位于 `Android/data/com.stephaneginier.nomad/files/`。  
在较新的 Android 版本（10/11）中，你将无法再访问 `Android/data` 文件夹。
你可以通过单独的应用访问它，例如[这个](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer)。
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### 有没有方式参与测试版？ {#beta}
对于 Windows 和 MacOS，测试版可能会在[主页](https://nomadsculpt.com)提供。
<br>
对于 iOS，有一个私有 TestFlight，前往 [Discord](https://discord.com/invite/8h7BwpRz29) 的 #beta-ios 频道。
<br>
[网页版演示](https://nomadsculpt.com/demo)通常会更新到最新功能。

### 为什么 Android 上有免费试用，但 iOS 上没有？ {#android-trial}
因为旧的 Android 设备表现很差（有些新设备也一样……），我不希望人们买了应用却只看到一片黑屏。
但主要原因是我觉得在 Android 上付费应用并不是常态。

### 哪款平板最适合运行 Nomad？ {#best-tablet}

简短结论：一台 iPad。

稍微长一点的回答是：

> “买一台你*买得起的*最新 iPad，除非你真的很讨厌苹果，那就买一台你买得起的最新三星平板。其他任何设备，都先测试再说。”

大家总是想要更多信息，所以这里有个总结。

Nomad 在较新的 iPad 上运行效果最佳：

* iPad 和 iPhone 可以使用 [Exoside](https://exoside.com/) 的 [Quad Remesher](tools#quad-remesher) 插件
* 支持最新 Apple Pencil 的新款 iPad 支持[笔身旋转（barrel roll）](https://www.youtube.com/watch?v=XcDQazDYpo0)，你可以在 Nomad 的某些工具中通过旋转手写笔来操作。
* 最新的 M 系列芯片性能非常快。

最新、最贵的 iPad 可以非常快速地渲染最终图像，并让你雕刻大量细节。

不过，随着 iPad 变旧、变便宜，性能下降并没有大家想象中那么严重。任何支持 Apple Pencil 的 iPad 都能很好地运行 Nomad。比如：

* 2023 年的 iPad Pro 可以流畅处理 500 万面多边形的雕塑，最终质量的图像可以在 5 秒内渲染完成。
* 2015 年的 iPad Pro 可以在有一点卡顿的情况下处理 120 万面多边形的物体，最终质量的图像可以在 20 秒内渲染完成。

性能差距很大，但你也要考虑价格：

* 2025 年的 iPad Pro 全部选配后全新价格约为 *2500 美元*。
* 2023 年的 iPad Pro 目前在 eBay 上约 *400 美元*。
* 2015 年的 iPad Pro 在 eBay 上约 *250 美元*。

多出 400 万面多边形并节省 15 秒时间是否值 2100 美元？这取决于你自己。

非 Pro 型号会更便宜，同时在尺寸和性能上提供更多选择。当前的 iPad Air 支持带笔身旋转的第二代 Apple Pencil，而且比 Pro 便宜很多。二手和翻新市场还有更多选择。

这意味着无论你的预算如何，你都应该能找到适合自己的 iPad。并且要记住，大多数雕塑并不是几百万面多边形！如果你能把面数控制在 50 万以下，即使是老 iPad 也能让你雕刻得很流畅。

`那 Android 呢？`

Android 的图形性能低于 iPad。根据 Nomad 开发者的说法，“一台三星 Galaxy Tab S9 运行 Nomad 的速度会比一台 iPad Air 慢一个数量级”。话虽如此，很多用户对自己的三星平板非常满意，对大多数雕刻工作来说 Nomad 运行得还不错。

对于其他 Android 平板，要多加小心。Android 硬件性能差异很大，很难预测 Nomad 的运行情况。

请先使用免费的“无法保存”版本的 Nomad 进行测试。

`那内存和存储呢？`

大多数 Nomad 文件通常在 100MB 以内。这意味着如今你买到的几乎任何平板，无论是 iPad 还是 Android，在存储空间上都足够放下你的 Nomad 项目。

### 我在一台设备上购买了 Nomad，可以在另一台设备上使用吗？ {#multi-devices}
只要使用的是同一个应用商店和同一个账号，就可以。

例如，如果你在 iOS App Store 上购买了它，你可以在其他 iOS 设备上使用。

如果你在 Google Play 上为 Android 平板购买了它，你可以在其他 Android 设备上使用。

但是，如果你在 Android 上购买了 Nomad，然后又买了一台 iPad，那你需要重新购买。

这是因为 Nomad 没有自己的授权服务器或订阅模式。Apple/Google/AppGallery 之间也没有处理授权共享的协议。

### 如何恢复我的购买？ {#restore}
Google Play 和 AppGallery 都会自动处理同步。

- 进入“关于”菜单（左上角 Nomad 图标），点击 `restore purchase`（恢复购买）
- 再三确认你登录的是购买 Nomad 时使用的同一个账号（在 Google Play 上）
- 重启设备
- 有时你需要等待几个小时
- 确保 Google Play 应用是最新版本
- 重新安装 Nomad（如果不想丢失任何内容，请务必先[备份你的文件](#where-are-my-projects-located-on-my-device)）
- 你可以尝试再次购买以查看会发生什么（注意：同一账号无法购买同一项目两次）

:::tip
你可以通过 <support@nomadsculpt.com> 联系我，但我*唯一*能做的就是确认某个邮箱是否有相关购买记录。

请注意，我经常收到关于在更换新设备后授权没有正确更新的反馈。
我对支付和账号同步没有任何控制权，这一切都由 Google/AppGallery 处理！

最终购买总是会被恢复，但目前尚不清楚有哪些步骤可以加快这一过程。
:::

::: warning
新的华为设备无法使用 Google 服务。
在这种情况下，你需要在 AppGallery（华为应用商店）上重新购买应用。
:::

### 你们可以翻译或修正我的语言吗？ {#locale}
我可以比较容易地添加另一种语言，但我主要依赖 AI 翻译，因为这样在日常更新时更容易维护。
翻译文件可以在[这里](https://github.com/stephomi/nomad-translation)找到。

## 功能 {#features}

### 为什么操作控件（gizmo）不移动？ {#gizmo-not-moving}
你可能在[左侧菜单工具栏](tools#left-menu-toolbar)中启用了“固定（pin）”。

### 能在 Nomad 里做动画吗？ {#animate}
目前不行。一个可以为图层制作动画的时间轴功能会很有趣，但目前并没有真正计划。

我希望未来能支持绑定/蒙皮，但这会带来一些挑战（尤其是与雕刻工具的交互……），所以目前还不确定。

### 能做真正的低多边形建模吗？ {#lowpoly}
目前不行。
这并不完全属于 Nomad *Sculpt* 的范围，但也许未来我会提供一些相关工具。

### 能做 UV 和贴图吗？ {#texturing}
简短回答：可以。详细回答：不能直接做，但有多种方式可以将 Nomad 出色的顶点绘制工具与 UV 和贴图结合使用。

* Nomad 允许你将颜色、粗糙度、材质属性直接绘制到雕塑的顶点上。
* Nomad 允许非常高的顶点数量，这样你可以在不考虑 UV 的情况下进行绘制。
* Nomad 可以加载用作笔刷的贴图，从而实现用贴图进行印章和绘画。
* Nomad 可以加载已经预先分配好贴图的物体，用于渲染。
* Nomad 可以对低多边形物体进行 [UV 展开](topology.md#uv-unwrap)。
* 可以通过[投射选项](topology.md#reproject-to-vertex)将颜色/粗糙度/金属度从贴图转移到顶点。
* 可以通过[烘焙选项](topology.md#bake-to-texture)将颜色/粗糙度/金属度/法线从顶点烘焙到贴图。
* 烘焙和投射可以在单个物体或多个物体之间进行，也可以在单个物体的最高和最低细分级别之间进行，从而支持多种烘焙和投射工作流程。
* 烘焙完成后，导出 obj 时也会导出贴图，你可以将其导入 Procreate 等应用直接在贴图上绘制。

### 我可以录制转台视频吗？ {#video}
目前没有计划，iOS 自带一个非常易用的[视频录制功能](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados)。

在 iOS 上，你可以从屏幕右上角向下滑动，然后点击录制按钮。它会给你 3 秒倒计时，期间把菜单滑走以显示 Nomad，然后使用转台功能。完成后，再次从右上角向下滑动并点击录制按钮停止录制。然后在照片库中编辑视频，删除开头和结尾多余的片段。

### 可以把我喜欢的功能添加成顶层按钮吗？ {#interface}
可以，现在可以在[界面](interface.md)菜单中自定义底部工具栏，也可以创建浮动工具栏。

### 接下来会加入哪些功能？ {#next-features}
中长期路线图上我有很多想法，但目前还不确定。

修复 Bug 和改进现有功能永远会比添加新功能优先。

### 可以在 Nomad 里做骨骼绑定吗？ {#rigging}
不可以，但已经在计划中。目前你可以将形状进行父子关联并修改枢轴点，从而实现简单的可摆姿雕塑。

### 可以使用超过 4 盏灯吗？ {#lights}
不可以，这是 Nomad 实时渲染引擎的限制。可以通过使用自发光物体和后期处理中的全局光照来“伪造”更多灯光，如[本教程](https://www.youtube.com/watch?v=QhrUGH7CuUA)所示。

### 可以导入 ZBrush 的工具（Tool）吗？ {#zbrush-import}
不可以，Zbrush 使用的是专有格式。你应该可以导出其中的 Alpha 贴图并在 Nomad 中使用。

### 为什么渲染出来的颜色和我绘制的不一致？为什么在渲染中得不到纯白色？ {#paint-pbr}
想象一下拍一张白纸的照片、一盏台灯的照片和太阳的照片。老式相机和屏幕会把它们都显示成“白色”。更现代的系统则可以区分纸张反射的白、灯发出的光以及太阳的超亮。

现代计算机图形学尝试以类似方式工作，模拟光线和表面的物理特性。这被称为 `基于物理的渲染（PBR）`，Nomad 的 PBR 渲染器就是基于这一点。它看起来更真实、平衡，但往往会让明亮的绘制颜色看起来更暗。

如果你需要渲染结果更接近你绘制的颜色，可以通过非 PBR 和 PBR 两种方式来调整：

非 PBR：
* `在灯光菜单中使用 “Unlit（无光照）” 模式`。颜色会完全按你绘制的方式显示，但你也会失去所有明暗关系。适合快速检查和更图形化的输出。
* `在灯光菜单中使用 “Matcap” 模式`。选择一个更亮、主要为白色且没有颜色偏移的 Matcap。

PBR：
* `使用中性环境`。你可以[更换环境](shading.md#environment)为更中性的环境。避免使用室内环境，因为它们往往颜色偏重。优先选择日光户外或摄影棚环境。
* `增强灯光`。如果你在黑暗房间里拍白纸的照片，你会简单地增加光源。在环境光中，调高曝光滑块直到颜色开始让你感觉合适，或者添加更多强度更高的单独灯光。
* `提高相机曝光`。如果黑暗房间里没有额外灯光，你可以让相机延长快门时间或提高 ISO。在 Nomad 中，你可以通过后期处理实现类似效果。进入后期处理，启用，然后找到色调映射（tone mapping），启用，并提高曝光滑块直到颜色感觉合适。
* `使用自发光颜色`。在材质菜单中，你可以在贴图下启用“emissive（自发光）”，这会让物体看起来像光源。如果在后期处理中开启全局光照，它会向场景中的其他物体投射光线。你也可以为该材质启用“unlit（无光照）”，在没有贴图的情况下实现类似效果。

## 崩溃 {#crashes}

### 保存或重拓扑（remesh）模型时会崩溃！ {#crash-remesh}
你的设备内存（RAM）不足。  
要减少场景中的内存使用量，你可以使用一些 [拓扑](topology.md) 选项来减少多边形数量。

::: tip RAM/存储
关键是 RAM 的容量，而不是存储空间（存储通常大得多）。
:::

### 加载项目时会崩溃！ {#crash-load}
如果文件很小，你可以发给我，我会看一下（通过邮件 <support@nomadsculpt.com>）。

否则设备很可能是 RAM 内存不足。

- 确保关闭设备上所有其他已打开的应用。
- 在 Nomad 中新建一个项目，而不是在已有项目打开的情况下操作。
- 如果仍然崩溃，唯一的解决方案是在一台内存更大的设备上加载[你的项目文件](#where-are-my-projects-located-on-my-device)。

::: tip
在桌面浏览器上，你可以尝试在[这个链接](https://nomadsculpt.com/demo_save/)中加载你的文件，然后在简化场景后再导出。

有些浏览器会限制单个标签页可使用的 RAM 数量，因此这种方法可能会失效。

如果你的项目使用了[图层](layers.md)，你可能需要将它们合并以减少内存占用。
:::

<!-- ::: tip
Additionally, for legacy glb.lz4 file format, you can try the following:

1. If your project is using [Layers](layers.md), enable the `Merge layers` option before loading the project.
The option can be found in the `Files -> Settings` sub menu.
Layers can take a lot of memory, merging them at loading can help reduce the memory peak usage.

2. Decompress your [project](#where-are-my-projects-located-on-my-device) (`.glb.lz4` to `.glb`).
On windows, you need to download [LZ4](https://github.com/lz4/lz4/releases).
On MacOS, you can use the command line.
With homebrew, simply do `brew install lz4` and then `lz4 myproject.glb.lz4`.

3. Try to load the `.glb` file directly into Nomad again.

4. If it still crashes at loading, you can open the file on any 3d desktop software that supports `glTF`.
::: -->

### 启动 Nomad 时会崩溃！ {#crash-start}
如果在加载时崩溃，说明 Nomad 在处理 Nomad 文件夹中的某个文件时遇到了问题。

大多数情况下，这是因为项目太大，不幸地超过了 RAM 限制。

找到 [Nomad 文件夹](#where-are-my-projects-located-on-my-device)，然后通过重命名或移动一些文件来找出问题文件。

首先，尝试重命名 `settings.json`。这样可以阻止它加载上一次打开的项目。

如果仍然不行，尝试将一些最近的文件从各自的资源文件夹（`projects`、`matcaps`、`environments` 等）中移出。

你也可以直接重命名这些文件夹，这样 Nomad 会完全忽略它们。
如果你重命名或移走 Nomad 文件夹中的所有文件，效果等同于一次干净安装。

::: tip
当 Nomad 在启动时加载某个文件时，它总是会先将该文件移动到 `can_be_deleted/` 文件夹。
如果操作成功，再将其移回原始文件夹。

如果在加载完成前崩溃，那么 Nomad 在下一次启动时会成功启动，因为它会忽略 `can_be_deleted/` 文件夹。

如果你认为该文件有可能成功加载，可以再尝试加载一次。
:::