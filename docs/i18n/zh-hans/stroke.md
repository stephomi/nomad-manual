# ![](/icons/pencil.webp) 笔触 {#stroke}

---
![](/images/stroke_overview.webp) 

## 概述 {#overview}

你可以自定义大多数工具画笔的笔触行为。
这些设置与 2D 绘画软件中的类似，不过也有一些是雕刻和 3D 特有的选项。

选项被分成 5 个子菜单：

| Name     | Icon                         | Description                                   |
| :------: | :--------------------------: | :-------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | 控制笔触如何应用到模型上                     |
| Alpha    | ![](/icons/alpha.webp)      | 灰度纹理如何用于画笔印章                     |
| Falloff  | ![](/icons/falloff.webp)    | 控制画笔强度从中心到边缘的变化               |
| Filter   | ![](/icons/filter.webp)     | 画笔如何受模型几何体影响                     |
| Pressure | ![](/icons/pressure.webp)   | 控制压感笔压力的响应                         |

::: tip
并非所有笔触选项都适用于所有工具。当前工具未使用的笔触选项会被禁用或隐藏。 
:::


## 笔触 {#stroke-1}

### 半径 {#radius}

![](/images/stroke_radius.webp)

#### 共享半径 {#share-radius}

启用后，所有工具将使用相同的半径；默认情况下，每个工具都有自己的半径。

#### 尺寸 {#size}

* Screen - 半径以屏幕单位设置。如果你将半径设为 100 像素宽，无论放大还是缩小，它都会保持 100 像素宽。
* Constant (3d) - 半径以 3D 单位设置。例如，如果你创建一个球体并将半径设为与球体同样大小，那么无论你如何缩放视图，半径都会保持与球体同样大小。


### 笔触 {#stroke-type}

![](/images/stroke_strokemode.webp)

笔触可以以多种模式工作：

### ![](/icons/stroke_dot.webp) 点 {#dot}
像普通绘画笔触一样拖动。 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) 滚动 {#roll}
画笔 Alpha 会根据笔触方向旋转，适合制作布料缝线等效果。 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lock + radius
以固定的**_高度_**盖章式绘制笔触。拖动用于设置缩放和旋转。
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) 锁定 + 强度 {#lock-intensity}
以固定的**_半径_**盖章式绘制笔触。拖动用于设置高度和旋转。
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

`Move` 和 `Drag` 工具有它们自己的 3 个选项：

### ![](/icons/snake.webp) 拖拽 {#drag}

在笔触过程中会持续更新笔刷半径内的内容。快速拖动会把表面甩在后面，而缓慢拖动会“抓住”材料，形成更长的形状。这是 `Drag` 工具的默认模式。配合 `Dynamic Topology` 可以用来制作类似蛇的拉伸形状。 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) 抓取 {#grab}
在开始笔触时选中笔刷半径内的内容，并保持该选择。这对于更精确的移动操作很有用，你可以仔细调整移动距离，而不会不小心移动超过最初选中的部分。这是 `Move` 工具的默认模式。
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) 锁定 + 半径（拖拽） {#lock-radius-drag}
会忽略用户设置的半径，而是根据笔触从起点拖动的距离动态设置半径。距离小 = 半径小，距离大 = 半径大。使用强度滑块控制衰减形状。适合用于铺设有机的、橡胶般的形体。
![](/videos/stroke_lockradius_drag.mp4) 



### 调整间距强度 {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

间距较小（低于 50%）的笔触会快速叠加，使笔触比高间距值时更强烈。启用此开关后会对其进行补偿，使得无论间距如何，笔触强度都大致相同。

### 笔触间距 {#stroke-spacing}
在拖动操作中，每次应用画笔印章之间的间隔。低于 100% 的值会产生重叠，看起来像连续笔触。大于 100% 的值会开始出现间隙，适合雕刻缝线或拉链等细节。

### 懒惰绳稳定器 {#lazy-rope-stabilizer}
笔触会在指针位置后方一定距离“跟随”。可用于绘制平滑的线条。
![](/videos/stroke_lazy_rope.mp4) 

### 笔触平滑 {#stroke-smoothing}
对多个指针位置取平均以获得更平滑的笔触。
在高数值下，笔触会落后于指针，但最终会追上。
这对于绘制平滑线条很有用。

### 吸附半径 {#snap-radius}
将新笔触的起点吸附到上一个笔触的终点。半径决定搜索上一个笔触终点的距离范围。这在绘制长的连续线条、但需要频繁停顿时很有用。

### ![](/icons/silhouette.webp) 轮廓 {#silhouette}
![](/images/stroke_silhouette.webp)
默认情况下，笔触只会影响画笔半径内的模型表面。启用轮廓（silhouette）后，笔触会沿投影方向贯穿整个模型。这在模型初期块状塑形，或需要保持侧面垂直的形状时非常有用。

投影方向可以显式设置，默认的 “Closest” 方法会根据视图自动检测最佳角度。 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp) 随机化 {#randomize}

![](/images/stroke_randomize.webp)

可以分别随机化笔触的强度、平移、旋转和缩放。可用于创建多种效果，例如配合绘画工具随机化可以产生斑驳的颜色，配合折痕工具随机化可以用来制作皮肤细节。

![](/videos/stroke_randomize.mp4) 

### 笔触偏移 {#stroke-offset}

对笔触应用一个恒定偏移。这在小屏幕上很有用，因为你的手指可能会挡住笔触。 


## ![](/icons/alpha.webp) Alpha {#alpha}
![](/images/stroke_alpha.webp) 

`Alpha` 是一种用来调制画笔行为的纹理。
它是一张灰度图像，其中黑色像素表示无变形，白色像素表示完全变形。

点击 Alpha 图像可以更换它。

点击材质预览可以从材质预设中加载 Alpha。你也可以在这里保存材质预设，并选择是否将纹理嵌入到工具中。

::: tip
纹理不会被重新采样，因此大尺寸纹理可能会降低性能。
:::

### 反转像素 {#invert-pixels}
反转图像的数值，使黑色像素变为白色，白色像素变为黑色。

::: tip

Nomad 自带的内置 Alpha 无法被反转。

:::

### 缩放 {#scaling}

Nomad 中的画笔大小是一个具有用户定义半径的圆。纹理通常是正方形或矩形，`Scaling` 参数允许你决定纹理如何适配这个圆。对于正方形纹理，值为 0.7 时纹理会完整地落在圆内。值为 1 时纹理会被放大到刚好包住圆，边缘会被裁剪。

![](/images/alpha_scaling.webp) 

启用 `Scaling - Y` 可以在垂直方向拉伸 Alpha。

![](/images/alpha_scaling_y.webp) 

### 旋转 {#rotation}

Alpha 纹理会根据笔触方向旋转。你可以添加一个旋转偏移，如果启用锁定图标，纹理会相对于屏幕保持该固定旋转。

### 平铺 {#tiling}
![](/images/stroke_tiling.webp) 

控制纹理在画笔轮廓内重复的频率。平铺模式允许你限制为笔触内单个纹理、重复纹理，或镜像模式（每隔一个纹理翻转），以创建图案或帮助制作无缝纹理。

![](/videos/alpha_tiling.mp4) 



### 中间值 {#mid-value}

默认情况下，黑色像素表示无变形，白色像素表示完全正向变形，例如，一个带岩石 Alpha 纹理的粘土画笔只会在 Alpha 非黑色的地方将表面向外拉出。

如果你希望画笔向内推表面，或者同时向内推和向外拉，可以调整中间值（mid value）。例如将其设为 0.5 时，Alpha 中的中灰不会产生效果，黑色会向内推，白色会向外拉。




## 衰减 {#falloff}

![](/images/falloff_menu.webp) 

这与 [Alpha](#alpha) 类似，但你是用一条单独的曲线来驱动强度。它会与 Alpha 组合，这样你可以用纹理控制细节，用衰减控制工具中心和边缘的渐变与强度。

当曲线在顶部时表示完全变形，在底部时画笔没有效果。

你可以把这条曲线理解为画笔尖端的剖面。底部区域预览的是画笔在模型表面上单次“盖章”的效果，如果画笔有 Alpha 纹理，也会一并显示，以预览衰减与 Alpha 如何交互。

### 预设 {#preset}
选中该模式时，点击曲线图会弹出预设菜单。圆滑的曲线会产生更柔和的效果，棱角分明的曲线会产生更锐利的效果。左侧工具栏中的 `Sub` 按钮会反转衰减，使曲线顶部改为向内推表面而不是向外拉，或反之。

### Catmull-Rom {#catmull-rom}
选中后，用户可以自行绘制衰减曲线。曲线编辑器的操作与 Nomad 其他地方的曲线相同：

* 点击曲线创建新点
* 拖动点以重新定位
* 点击点在锐利与平滑之间切换
* 将一点拖到相邻点上以删除它

### B-spline {#b-spline}
选中后，用户同样可以自行绘制衰减曲线。编辑器操作与 Catmull-Rom 相同，但控制点影响曲线而不直接落在曲线上，这有助于创建更平滑的曲线形状。

曲线编辑器有 3 个按钮：

| Item     | Icon                        | Description                         |
| :------: | :-------------------------: | :---------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | 展开曲线编辑器                     |
| Reset    | ![](/icons/reset.webp)     | 将曲线恢复到默认状态               |
| Symmetry | ![](/icons/symmetric.webp) | 以对称“画笔尖端”方式显示曲线       |


### 影响 {#influence}

* Sphere (3d) - 影响范围通过顶点到画笔中心的距离计算。
* Circle (2d) - 先将顶点投影到区域平面，再计算其到画笔中心的距离。这与 Alpha 的采样方式类似。 
* Cylinder - 影响范围沿区域以圆柱方式投射，被下面的 Silhouette 模式使用。

### 轮廓 {#silhouette-1}
默认情况下，笔触只会影响画笔半径内的模型表面。启用轮廓（silhouette）后，笔触会沿投影方向贯穿整个模型。这在模型初期块状塑形，或需要保持侧面垂直的形状时非常有用。



## 过滤器 {#filter}

![](/images/filter_menu.webp) 

### 累积笔触 {#accumulate-stroke}
启用后，单次笔触中可添加/移除的体积不设上限。例如 `Clay` 工具启用了该选项，因此可以不断堆积材料；而 `Brush` 工具禁用了该选项，因此在同一笔触反复划过网格同一区域时，将停止继续添加材料。 

### 仅面向前方顶点 {#front-facing-vertex-only}
该选项会忽略背向的顶点。
如果你想只在薄几何体的一侧绘制而不影响另一侧，这会很有用。
它同样适用于雕刻，但可能会出现一些伪影。

### 允许动态拓扑 {#allow-dynamic-topology}
该选项仅在网格处于 [Dynamic Topology](topology.md#dynamic-topology) 模式时可用。你可以为每个工具单独启用或禁用动态拓扑。

### 连通拓扑 {#connected-topology}
仅对与工具接触表面相连的顶点进行雕刻。例如配合 `Move` 工具使用时，即使某部分与另一部分相交，你也可以只移动其中一部分。
![](/videos/connected_topology.mp4)

### 保护区域 {#protect-area}
![](/images/filter_protect_area.webp) 

这些选项会在不同条件下阻止工具影响网格的某些部分。 

“Auto” 选项表示：如果你在 [Shading](shading) 菜单中启用了隐藏、遮罩或面组可见性，它们会被保护；如果在该菜单中关闭，则不再保护。

* `All` - 切换保护过滤器是全局的还是按工具单独设置。
* `Hide` - 如果网格部分被 Hide 工具隐藏，设置它们是否应被保护。
* `Mask` - 如果网格部分被遮罩，设置它们是否应被保护。
* `Facegroup` - 设置是否只能在首次接触到的面组内使用工具。


### 保持锐利边缘 {#keep-sharp-edges}
排除法线与表面法线差异过大的点。

这会改变平面区域（Area sampling）的计算方式。

该选项对基于平面的工具很有用，或者当你想在大致平坦的表面上上色而不产生溢出时很有帮助。

![](/videos/filter_keep_sharp_edges.mp4)

### 区域采样 {#area-sampling}
某些画笔或笔触选项需要一个平面法线和一个平面位置来与表面配合工作。

你可以通过设置采样区域相对于工具半径的比例来控制如何计算这个平均平面。

在 100% 时，选择圆内的所有点都会被考虑。

在 0% 时，只考虑最近的顶点或三角形。这些数值可以为 `Normal radius` 和 `Position radius` 绑定，也可以解锁并分别设置。


### 深度遮罩 {#depth-masking}
![](/images/stroke_depthmask.webp)

排除距离计算平面（Area sampling）高于或低于某个距离的点。

这可以用于只在凸起区域绘制，或只在凹陷区域绘制。

图表表示表面的剖面；水平线是表面位置，圆圈表示相对于表面上下的绘制衰减半径。`Height offset` 是相对于表面的百分比，用于确定开始进行遮罩计算的高度。`Top area` 和 `Bottom area` 允许你分别缩放偏移点以上和以下的衰减。

#### 示例：在凹槽中绘制 {#example-paint-in-cavities}
若只在凹陷区域绘制，将高度偏移设为 -100%，并调整 top area 滑块，使其远离水平线。这意味着第一次点击会设置“零”深度，然后只有低于该深度的区域会受到影响。

![](/videos/stroke_depth_cavity.mp4)

#### 示例：在凸起处绘制 {#example-paint-on-bumps}
若只在高处绘制，将高度偏移设为 +90%，使圆底部与水平线略有交叉。当你点击某个“高”区域顶部时，这会设置深度，使得该深度及略低于它、以及高于它的区域会被绘制，而深凹处会被跳过。
![](/videos/stroke_depth_bump.mp4)


## 压感 {#pressure}
![](/images/pressure_menu.webp) 

控制压感笔压力如何影响画笔。

默认启用 `Use global settings`，表示所有画笔共享同一套压力设置。

### 压感 - 半径 {#pressure-radius}

该曲线控制画笔半径如何受压力影响。默认是线性关系，如果你的压感笔响应平滑，那么半径变化也应感觉平滑。不过，许多压感笔的响应并非线性，你可以通过这条曲线进行补偿。例如，如果在高压力下半径似乎达不到最大值，可以使用类似 “out-pow3” 的预设曲线（向上弯曲），以更早增加半径。

该对话框与衰减曲线显示类似，你可以通过点击曲线窗口使用预设，或使用 Catmull-Rom 和 B-Spline 模式绘制自己的曲线。

如果你希望半径恒定，可以禁用此部分。

### 压感 - 强度 {#pressure-intensity}

与半径曲线类似，但用于控制强度。如果你希望强度恒定，可以禁用此部分。

### 压感平滑 {#pressure-smoothing}

对压感笔压力事件进行平均，以获得更平滑的结果。