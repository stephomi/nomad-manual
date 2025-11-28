# ![](/icons/toolbox.webp) 工具 {#tools}

![](/images/tools_menu.webp)

::: tip
直接跳到下方的 [工具](#tools-1) 查看各個工具的詳細說明。
:::

## 概覽 {#overview}

工具從右側的 `Toolbox`（工具箱）中選擇，並透過左側的 `Tool Controls`（工具控制）來操作。額外設定位於右上角選單中第一個圖示的 `Settings`（設定）選單。

筆刷類工具有尺寸與強度控制。選取類工具有多種選取模式控制。工具控制面板底部有常用操作的快捷鍵（Smooth、Mask、Hide、Gizmo、Color、Alpha）。

Nomad 的工具在工具箱中以顏色區分：

* <span class=brush>**筆刷工具**</span>（Clay、Brush、Smooth、Layer、Inflate、Nudge、Stamp、DelLayer）
* <span class=move>**移動工具**</span>（Move、Drag）
* <span class=mask>**遮罩工具**</span>（Mask、SelMask）
* <span class=paint>**塗色工具**</span>（Paint、Smudge）
* <span class=flatten>**平面化工具**</span>（Flatten、Planar）
* <span class=pinch>**夾緊工具**</span>（Crease、Pinch）
* <span class=selection>**選取型工具**</span>：先繪製 2D 遮罩，再執行操作（Trim、Split、Project）
* <span class=creation>**建立工具**</span>（Tube、Lathe、Insert）
* <span class=transform>**變形工具**</span>（Transform、Gizmo）
* <span class=misc>**其他工具**</span>（Facegroup、Hide、Measure、Select）
* <span class=view>**檢視工具**</span>



許多工具可以透過 [Stroke](stroke.md) 選單自訂不同的筆刷行為、壓力、材質貼圖等。 


### 畫筆控制 {#brush-controls}

左側工具列有半徑與強度滑桿，接著是各工具類別專屬的控制，說明如下。

![](/images/tool_left_panel.webp)

::: tip
許多工具的強度滑桿可以超過 100%，值得多加嘗試！
:::

### 子模式 {#sub-mode}
強度滑桿正下方的按鈕是 `Sub` 按鈕。它的標籤與功能會依工具而變化，按下後會啟用另一種、通常是相反的行為。例如對 [Paint](#paint) 來說會啟用擦除模式；對 [Crease](#crease) 則會產生凸起邊緣而不是凹縫等。

預設情況下它是「黏性按鈕」：也就是說你按住不放時會暫時啟用，放開就會關閉；若是輕點一下，Sub 模式會被永久啟用。

### 快捷鍵 {#shortcuts}
左側工具列底部有 [Smooth](#smooth)、[Mask](#mask)、[Hide](#hide)、[Gizmo](#gizmo)、[Color](painting.md#pbr-sliders)、[Alpha](stroke.md#alpha) 的快捷鍵。 

預設它們同樣是「黏性按鈕」：按住不放時暫時啟用，放開即關閉；輕點一下則會永久啟用該快捷模式。

### 選取控制 {#selection-controls}

[Selection Mask](#selection-mask)、[Trim](#trim)、[Split](#split)、[Project](#project)、[Facegroup](#facegroup) 與 [Hide](#hide) 工具都使用類似的控制來選取網格區域。

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - 自由手繪形狀
* `Polygon` - 由曲線與／或直線組成的封閉形狀。更多資訊見下方的 [Shape editing](#shape-editing)。
* `Curve` -（僅 Project）- 投影用的自由手繪曲線
* `Path` -（僅 Project）- 由點定義的曲線。更多資訊見下方的 [Shape editing](#shape-editing)。
* `Line` - 拖曳一條線來定義一個平面切割區段。預設會立即對網格執行操作，若不希望如此，可關閉自動驗證（長按或滑動線段圖示）。
* `Rect` - 拖曳一條對角線，定義矩形的兩個角。長按或滑動可顯示選項：自動驗證、強制為正方形、以及第一點作為矩形中心。
* `Ellipse` - 拖曳一條對角線，定義橢圓大小。長按或滑動可顯示選項：自動驗證、強制為圓形、以及第一點作為橢圓中心。
* `Flip` - 反轉形狀遮罩，或反轉 Project 工具的方向。

大多數工具都有自動驗證選項，啟用時在你畫完形狀後會立刻執行操作。當自動驗證關閉時，形狀旁會出現一個綠色按鈕，用來執行操作。這樣你可以先編輯形狀、調整視角，準備好後再按綠色按鈕使用該形狀。

### 形狀編輯 {#shape-editing}
多邊形編輯與曲線編輯的行為相似：

* 一開始拖曳一條線來定義兩個點，然後從線段中間拖出來以定義多邊形或曲線。
* 點擊節點可在平滑與銳利之間切換。 
* 在曲線或線段上點擊並拖曳可建立新的節點。
* 要刪除節點，將該節點拖曳到相鄰節點上，直到變紅為止。
* 多邊形或路徑圖示角落的垃圾桶圖示會刪除整個形狀。

### 設定選單 {#settings-menu}

許多工具有額外設定，位於右上角選單第一個圖示的設定選單中：

![](/images/tools_settings_menu.webp)

## 工具 {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) 黏土 {#clay}
Clay 工具適合用來堆疊、建立你的雕塑形體。`Sub` 會從雕塑上移除材質。

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) 畫筆 {#brush}
標準筆刷。`Sub` 會移除材質。

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) 移動 {#move}
筆刷底下的區域會「黏」在筆刷上，產生彈性變形。移動期間選取會被維持，所以如果你把筆刷移開，再移回原處，就不會看到任何變形。

Sub 模式是 `Normal`，會沿著表面法線方向移動筆刷底下的區域。

此筆刷適合大範圍變形，也適合細緻的小幅度變形。

#### 移動設定 {#move-settings}

* `Radius (Background)` - 距離模型邊緣多遠仍可雕刻，對於調整物體輪廓時很有用。 
* `Same-side vertex only` - 忽略朝向與變形方向相反的頂點。


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) 拖曳 {#drag}
筆刷底下的區域會「黏」在筆刷上，產生彈性變形。與 Move 筆刷不同的是，Drag 筆刷在筆劃過程中會持續更新選取區域，因此特別是在啟用動態拓樸（Dynamic Topology）時，可以拉出較長、像蛇一樣的形狀。

Sub 模式是 `Normal`，會沿著表面法線方向移動筆刷底下的區域。

此筆刷適合較鬆散、具姿態感的形體變化。

#### 拖曳設定 {#drag-settings}

* `Radius (Background)` - 距離模型邊緣多遠仍可雕刻，對於調整物體輪廓時很有用。 
* `Same-side vertex only` - 忽略朝向與變形方向相反的頂點。

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) 平滑 {#smooth}
透過平均點的位置來平滑該區域。此工具高度依賴多邊形密度。
如果多邊形很多，平滑效果會較不明顯。

Sub 模式是 `Relax`，只會平滑線框（拓樸），並盡量保留幾何細節。

#### 平滑設定 {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### 面群組 {#smooth-facegroup}

* `Relax` - 會平滑 facegroup 的邊界。使用大於 100% 的強度可以快速平滑邊界。`Auto` 只會在啟用 facegroup 預覽時平滑；`Off` 關閉；`On` 強制啟用。 

##### 頂點 {#vertex}
* `Sticky vertex on border` - 對於有開放邊界的網格（例如平面），預設可以把角落也平滑掉。啟用此選項會鎖定開放邊界。
* `Relax` - 與左側工具列中的 Relax 替代模式相同。
* `Stable smoothing` - 嘗試讓平滑效果與拓樸無關。對於拓樸密度變化大、且平滑強度值高時效果最佳。

##### 繪畫 {#painting}
* `Screen Smoothing` - 使用此選項可在高多邊形數量下，仍獲得與拓樸無關的平滑效果。
* `Screen samples` - 平滑品質，數值越高越平滑，但速度較慢。

::: tip
較高的多邊形密度可能需要將強度提高到 100% 以上。非常高的數值（300%、500%）也可以作為雕刻工具使用，能快速將筆刷下的區域打平、變光滑，就像用木槌敲打黏土一樣！
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) 遮罩 {#mask}
此工具可對頂點進行遮罩。被遮罩的頂點不會受到雕刻或塗色影響。 

Sub 模式是 `Unmask`，會擦除已繪製的遮罩。

類似 2D 繪圖軟體中的選取，遮罩可以用筆刷繪製，也可以用形狀選取、模糊或銳化。 

不同於 2D 軟體，遮罩也可以透過 facegroup 建立，並可用來透過擠出／抽取類操作建立新幾何。 

![](/videos/tool_mask1.mp4)

 視窗上方會出現一個工具列，提供額外控制。 

![](/images/tool_mask_toolbar.webp)

工具列標題可點擊以展開／收合，右上角的箭頭可將工具列移到介面頂部或底部。

| Action                                             | Description                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/cross_circle2.webp) Clear              | 清除遮罩                                                                                   |
| ![](/icons/invert.webp)        Invert             | 反轉遮罩                                                                                   |
| ![](/icons/sharpen.webp)       Sharpen            | 銳化遮罩邊緣                                                                               |
| ![](/icons/blur.webp)          Blur               | 模糊遮罩邊緣                                                                               |
|                                 Blur ->            | 左右拖曳以即時調整遮罩模糊程度                                                             |
| ![](/icons/culling.webp)       Front              | 僅對前向頂點套用遮罩                                                                       |
|                                 Convert            | 將遮罩轉換為 facegroup                                                                     |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | 啟用時會顯示 facegroup，點擊 facegroup 會將其整個遮罩                                     |
|                                 On tap (mask)      | 啟用時，點擊遮罩或未遮罩的「島」會對該島進行填滿式遮罩或反遮罩                             |
| ![](/icons/vertex.webp)        Connected          | 啟用時，僅允許遮罩筆劃影響拓樸上連通的區域                                                 |

##### 遮罩快速手勢 {#mask-quick-gesture}
在按住左側工具列的快速遮罩按鈕時，可以使用類似 ZBrush 的手勢：
| Action  | Gesture (hold lower-left shortcut) |
| :-----: | :--------------------------------: |
| Invert  | 在背景上點一下                      |
| Clear   | 在背景上拖曳                        |
| Blur    | 在已遮罩區域點一下                  |
| Sharpen | 在未遮罩區域點一下                  |


#### 遮罩設定 {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - Mask 設定選單主要用來從遮罩建立幾何，因此預設會預覽新幾何的樣子。你可以選擇不預覽、抽取預覽、分割預覽，以及是否以 X-ray 模式顯示此幾何。

##### 厚度 {#thickness}
* `Height` - 抽取形狀的高度。加號／減號圖示可在向外擠出、向內擠出或以遮罩面為中心三種模式間切換。 
* `Height/Height+Mask` - 在高度固定與讓模糊遮罩影響高度之間切換，後者可產生柔和且高度變化的形狀。 

##### 平滑度 {#smoothness}
啟用時會平滑抽取形狀的邊界，在高多邊形數量下效果更佳。 
* `Iterations` - 平滑次數。數值越高邊緣越圓滑，但會逐漸偏離原本遮罩形狀。
* `All/Sharp border/Borders only` - 平滑可作用於所有方向（側面與頂面都平滑）、僅平滑但保留銳利邊緣，或只平滑邊界、保持頂面不變。

##### 邊緣迴圈（側面） {#edge-loop-side}
* `Auto Edge-loop (side)` - 自動計算抽取形狀側面的分段數，使其形成接近方形的多邊形，並與遮罩區域的多邊形大小相符。關閉時可用 Edge loop 滑桿自行設定側面分段數。

----

##### 擠出 {#extract}
* `Extract` - 建立抽取後的幾何。
* `Closing action` - 控制抽取後原網格的處理方式。`None` 會將被遮罩的多邊形複製成新形狀；`Fill` 會同時嘗試封補背面；`Shell` 會依「Thickness」中的高度進行擠出，是預設值。

::: tip

若預覽模式為 `Extract` 且啟用 `X-ray`，按下 Extract 按鈕一開始可能會讓人困惑。因為設定選單仍開啟，系統會嘗試在新形狀上預覽抽取，並將原始表面設為 X-ray。但由於新表面上沒有遮罩，無法預覽抽取，Nomad 會顯示「Nothing to Extract!」的警告。 

這是正常現象。關閉 Mask 設定選單即可看到新形狀與原始形狀，再選取原始表面以清除或重新繪製遮罩。
:::

##### 分割 {#split-mask}
* `Split` - 會將被遮罩與未遮罩區域都抽取成新形狀。 
* `Closing action (masked)` - 控制遮罩區域抽取後原網格的處理方式。`None` 會將被遮罩多邊形複製成新形狀；`Fill` 會同時嘗試封補背面；`Shell` 會依「Thickness」中的高度進行擠出，是預設值。
* `Closing action (unmasked)` - 控制未遮罩區域抽取後原網格的處理方式。`None` 會將未遮罩多邊形複製成新形狀；`Fill` 會同時嘗試封補背面；`Shell` 會依「Thickness」中的高度進行擠出，是預設值。
* `Sync border` - 確保遮罩與未遮罩抽取形狀之間的邊界保持接近。關閉時，由於 Shell 操作會沿各自法線擠出，每個面可能導致兩形狀之間出現縫隙。

##### 鏤刻 {#carve}
* `Carve` - 預設模式下，行為類似以「Thickness」的高度向內 Trim 表面，就像切下一片橘子皮。 



### ![](/icons/tool_maskSelector.webp) 選取遮罩 {#selection-mask}
此工具與 [Mask 工具](#mask) 大致相同，主要差異在於不使用筆劃繪製遮罩，而是使用 [Selection Controls](#selection-controls)。

Sub 模式是 `Unmask`，會使用選取控制來擦除遮罩。

Selection Mask 與 `Mask` 工具共用相同的工具設定。

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) 上色 {#paint}
套用顏色與材質屬性。想了解更多材質資訊，請參考 [Painting](painting.md) 章節。

Sub 模式是 `Erase`，會移除塗色。

#### 上色設定 {#paint-settings}
* `Layer fitering` - 功能類似 Photoshop 或 Procreate 的圖層 Alpha Lock。當你在某圖層上繪製且啟用此選項時，只能修改已上色區域；未上色區域會受到保護。

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) 塗抹 {#smudge}
推抹顏色與材質屬性。Smudge 設定選單中有 `Quality` 滑桿，數值越低筆劃越快。

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) 壓平 {#flatten}
將區域投影到平均平面上以使其變平。

Sub 模式是 `Fill`，會以最高點定義平面，並傾向將點往上拉。

#### 壓平設定 {#flatten-settings}

* `Lock plane direction` - 使用第一次點擊計算出的平面方向。預設關閉。
* `Lock plane origin`- 使用第一次點擊的位置作為平面中心。預設關閉。

當這兩項任一或兩者都關閉時，可以透過長筆劃跨越不同深度與曲率，逐步加深 Flatten 效果或改變平面角度。搭配筆刷選單中的取樣區域選項，可以非常精準地控制。

::: tip
在高曲率區域工作時，例如想要壓平臉頰但工具總是影響到鼻側，可以先建立遮罩保護不希望被 Flatten 影響的區域。
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) 平面 {#planar}
將點投影到平均平面上使其共平面，但累積效果比 Flatten 筆刷少。這會產生更乾淨的硬邊表面。快速筆劃會較明顯地推拉表面，較慢且從已平面區域向外延伸的筆劃則能更好地維持平面。

Sub 模式是 `Fill`，會以最高點定義平面，並傾向將點往上拉。

Planar 實際上與 `Flatten` 是同一工具，但預設啟用 `Lock plane direction`，因此更傾向產生穩定、硬邊的表面，而 Flatten 則較具雕塑性，可用來建立半平面區域。

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) 摺痕 {#crease}
Crease 工具適合雕刻細小的切縫或凹痕。

Sub 模式是 `Invert`，會產生凸起的摺線。

#### 摺痕設定 {#crease-settings}

* `Pinch factor` - 頂點向筆劃兩側收攏的程度。當 Pinch 為 1、Offset 為 0 時，表面不會有深度變化，只會有拓樸變化，邊緣會被拉向筆劃。
* `Offset factor` - 頂點沿深度方向推／拉的程度。當 Pinch 為 0、Offset 為 1 時，會產生很深的凹縫或凸起，但由於沒有足夠幾何被拉向摺線，邊與底部會顯得鋸齒狀。

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) 捏合 {#pinch}
此工具可用來銳化邊緣。

Sub 模式是 `Invert`，會將頂點向外推開。

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) 修剪 {#trim}
Trim 工具會從網格中移除一塊區域，並提供多種方式處理留下的空洞。它使用 [Selection controls](#selection-controls) 來定義切割區域。

::: tip
由於此工具是從相機方向投影，你在透視模式下使用時會收到警告。

在正交模式下，對網格的切割與視角平行，通常符合使用者預期；若在透視相機下操作，物體近側與遠側的切面會看起來不同。
:::

#### 修剪設定 {#trim-settings}

* `Stroke painting` - 若在 Paint 選單中啟用塗色，補洞區域會填滿目前選取的顏色。
* `Boolean` - 使用四邊形區域填補 Trim 產生的洞。補洞區域會是平面。
* `Legacy` - 使用三角形區域填補 Trim 產生的洞。補洞區域會是平面。
* `Fill` - 使用三角形區域填補洞。補洞區域會是彎曲表面，類似肥皂泡膜。
* `None` - 不填補洞。
* `Boolean Detail Shape` - Trim 形狀側面所使用四邊形與三角形的大致尺寸。
* `Boolean Detail Hole` - Trim 補洞區域所使用三角形或多邊形的大致尺寸。 
* `Legacy Detail` - Trim 所使用三角形的大致尺寸。
* `Legacy Hole smoothing` - 補洞區域三角形的放鬆（平滑）程度。
* `Legacy Threshold espilon` - 可調整以改善舊版補洞演算法的數值。
* `Fill Detail` - Trim 補洞所使用三角形的大致尺寸。

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) 分割 {#split}
與 [Trim](#trim) 工具類似，不同之處在於 Trim 會丟棄選取區域，而 Split 會將選取區域保留為新物件。

#### 分割設定 {#split-settings}

* `Stroke painting` - 若在 Paint 選單中啟用塗色，補洞區域會填滿目前選取的顏色。
* `Boolean` - 使用四邊形區域填補 Split 產生的洞。補洞區域會是平面。
* `Legacy` - 使用三角形區域填補 Split 產生的洞。補洞區域會是平面。
* `Fill` - 使用三角形區域填補洞。補洞區域會是彎曲表面，類似肥皂泡膜。
* `None` - 不填補洞。
* `Boolean Detail Shape` - Split 形狀側面所使用四邊形與三角形的大致尺寸。
* `Boolean Detail Hole` - Split 補洞區域所使用三角形或多邊形的大致尺寸。 
* `Legacy Detail` - Split 所使用三角形的大致尺寸。
* `Legacy Hole smoothing` - 補洞區域三角形的放鬆（平滑）程度。
* `Legacy Threshold espilon` - 可調整以改善舊版補洞演算法的數值。
* `Fill Detail` - Split 補洞所使用三角形的大致尺寸。

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) 投射 {#project}
Project 工具看起來與 [Trim](#trim) 類似，但不會刪除或建立任何幾何，只會移動頂點以符合選取形狀。

![](/videos/tool_project.mp4)

::: tip
若在某個 Layer 中使用 Project，可以透過圖層滑桿在原始形狀與投影後形狀之間做混合。
:::

### ![](/icons/tool_layer.webp) 圖層 {#layer}
抬高表面，但限制高度。

若你持續按住筆刷在同一區域來回塗抹，Layer 只會抬高到某個高度就不再增加；其他工具則會持續累積高度。

注意預設情況下，這個限制是「每一筆劃」各自計算！若開始新的筆劃，會從新的表面高度繼續往上堆。

若要在多筆劃之間維持固定最大高度，請搭配 Nomad 的 [Layers](layers.md) 系統使用 Layer 工具。

建立一個 Layer，並使用此工具。此時最大高度由該 Layer 決定，你可以畫很多筆劃，高度都會維持一致。

`Sub` 會使用最小深度，產生凹槽。

#### 圖層設定 {#layer-settings}

* `Use layer data` - 啟用時，若有選取某個 Layer，會使用該 Layer 的資料來設定最大高度。
* `Inflate`- 啟用時會調整 Layer 的作用方向，以獲得更平滑的結果。
* `Relax (Normal)` - 套用在法線上的平滑程度。

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) 膨脹 {#inflate}
沿各自的法線方向移動頂點。`Sub` 則會沿反向法線移動頂點。

#### 膨脹設定 {#inflate-setings}
* `Relax (Normal)` - 套用在法線上的平滑程度。

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) 推動 {#nudge}
沿筆劃方向移動或「塗抹」點。

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) 印章 {#stamp}

點擊並拖曳，以目前選取的 Alpha 形狀在雕塑上凸起一塊區域。

這其實就是 [Brush 工具](#brush)，筆劃類型設定為 `Lock + radius`。 

`Sub` 會將 Stamp 壓入表面，而不是從表面拉出。

::: tip
Stamp 通常在高解析幾何上效果最佳。若你在網路上搜尋「wrinkles alpha」、「pores alpha」、「scales alpha」等，這些 Alpha 貼圖搭配 Stamp 可以快速為角色雕塑加入有機細節。

兩種筆劃模式適用於不同情境： 

* `Lock + radius` 具有固定「高度」，拖曳時調整的是 Stamp 的寬度與旋轉。適合皮膚紋理，需要深度一致但旋轉與縮放不同，以避免重複感。
* `Lock + intensity` 具有固定「寬度」，拖曳時調整的是 Stamp 的旋轉與高度。適合鉚釘等元素，需要尺寸一致但高度與旋轉可變。 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) 刪除圖層 {#delete-layer}
此工具可局部重設 Layer，必須有啟用中的 Layer，否則不會有任何效果。

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) 管狀 {#tube}
透過繪製曲線來建立 Tube。 
![](/images/tool_tube_new.webp)

Tube 建立後，可以在 3D 空間中編輯路徑，操作方式與一般的 [Shape editing](#shape-editing) 與曲線編輯工具類似。 

![](/videos/tool_tube.mp4)

#### 管狀左側工具列 {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

左側工具列包含以下選項：

* `Sync` - 若目前 Tube 是實例（instance），且 Tube 的子節點在各實例間有所差異，按下此按鈕會重新同步它們。
* `Snap` - 啟用時，Curve 與 Path 模式在繪製時會吸附到其他物件表面。關閉時，只有第一個點會吸附，其餘 Tube 會以該深度繪製。它有一個小的展開選單：
    * `Offset` - 設定吸附深度；0% 代表 Tube 橫截面的中心會貼在表面上，正值會將 Tube 往外抬起，負值則會往內壓入。
* `Curve` - 以自由手繪方式畫出 Tube。它有一個小的展開選單：
    * `Auto-validate` - 筆劃完成後立即建立 Tube。關閉時，曲線路徑旁會出現綠色驗證圓圈，按下即可建立，或使用此選單中的 `Reset` 連結刪除路徑。
    * `Closed` - 將 Tube 首尾相接成環狀。
    * `Screen` - 僅在關閉 Auto-validate 時可用。啟用時，路徑會「釘」在螢幕上，你可以移動視角與物件，路徑仍保持在畫面位置；關閉時，路徑是 3D 場景的一部分，會隨相機與物件移動。
    * `Accuracy` - 將繪製路徑轉換為 Tube 時使用的曲線點數量。0% 使用最少點數，可能忽略細微曲率變化；100% 則非常精準，使用較多點。
* `Path` - 透過點擊建立曲線點來建立 Tube。點擊綠色圓圈以驗證路徑。它有一個小的展開選單：
    * `B-spline` - 另一種曲線繪製方式，曲線點通常不直接落在曲線上，但可產生比預設方法更平滑的結果。
    * `Closed` - 將 Tube 首尾相接成環狀
    * `Screen` - 啟用時，路徑會「釘」在螢幕上，你可以移動視角與物件，路徑仍保持在畫面位置；關閉時，路徑是 3D 場景的一部分，會隨相機與物件移動。

##### 管狀頂部工具列 {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
選取 Tube 時，視窗上方會出現工具列提供額外控制。點擊工具列標題可展開／收合，點擊右上角箭頭可將工具列移到視窗頂部或底部。

* `Validate` - 將 Tube 烘焙為一般多邊形，以便雕刻。
* `Edit` - 顯示曲線點以便操作
* `Mirror` - 在此曲線上方新增 Mirror Repeater 作為父節點
* `Snap` - 將曲線點吸附到附近表面
* `Closed` - 將曲線首尾相接成環狀
* `B-spline` - 在 Catmull-rom 與 B-spline 插值間切換。
* `Cap` - 在兩端封口、僅起點封口、僅終點封口或不封口之間切換。
* `Hole` - 為 Tube 加上厚度，轉為 Pipe。可在兩端開孔、僅終點開孔或不開孔之間切換。 
* `Radius` - 在單一半徑、起點與終點各一半徑、或每個曲線點各自半徑之間切換。這些半徑可透過曲線上的橘色控制柄編輯。
* `Twist` - 在無扭轉、單一扭轉、起點與終點各一扭轉、或每個曲線點各自扭轉之間切換。這些扭轉可透過曲線上的粉紅色控制柄編輯。
* `Profile` - 在無 Profile（即圓形截面）、單一 Profile、起點與終點各一 Profile、或每個點各自 Profile 之間切換。
* `Profile edit` - 顯示 Profile 編輯器。其操作類似 [Shape editing](#shape-editing) 工具，可儲存與載入 Profile 預設，並有一個切換可讓你在 3D 空間中編輯 Profile。
* `Spiral` - 顯示加入螺旋扭轉的選單。此選單包含 `Twist Angle`、`Offset`、`Scale` 與 `Angle offset`。
* `X Divisions` - Tube 周向分段數，例如 4 段會產生方形 Tube。 
* `Constant density` - 啟用時會維持多邊形接近正方形；關閉時可自行設定沿 Tube 長度方向的 `Y divisions`。
* `...` - Tube 設定選單。

#### 曲線點刪除切換 {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

工具列下方有一個曲線點刪除切換。當你將曲線點拖曳到另一點附近時，該點會變紅，表示放開後會被刪除。若你只想做小幅編輯而不想刪除點，可關閉此按鈕以停用刪除行為。



#### 管狀設定 {#tube-settings}
* `Primitive` - 按鈕可啟用／停用 UV，或將 Tube 驗證（Validate）。
* `Post subdivision` - 在驗證前設定多重解析度層級的捷徑。
* `Linear subdivision` - 在驗證前設定線性細分層級的捷徑。 
* `Division X` - 與工具列中的 X Divisions 相同。
* `Division Y` - 與工具列中的 Y Divisions 相同。
* `Curve (Repeater)` - 將 Tube 轉換為 [Curve Repeater](scene.md#curve)

::: tip
將 Divisions 設為 4、Post subdivision 設為 3，可產生平滑、圓頭的 Tube，適合做蟲、蛇、身體部位等。
:::


### ![](/icons/tool_lathe.webp) 車削 {#lathe}
透過繪製曲線來建立旋轉曲面。

此工具非常適合製作花瓶、酒杯等形狀。

![](/videos/tool_lathe.mp4)

#### 車削左側工具列 {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

左側工具列包含以下選項：

* `Sync` - 若目前 Lathe 是實例，且 Lathe 的子節點在各實例間有所差異，按下此按鈕會重新同步它們。
* `Fixed` - 啟用時，Lathe 的中心線會固定並顯示在畫面上。此中心線有可調整的控制點。關閉時，Lathe 的中心會動態更新，以符合所繪曲線的起點與終點。
* `Curve` - 以單一筆劃繪製 Lathe 的 Profile。它有一個小的展開選單：
    * `Auto-validate` - 啟用時，筆從螢幕抬起後會立即建立 Lathe。關閉時，曲線旁會出現綠色圓圈可按下建立 Lathe，曲線可透過 `Reset` 按鈕刪除。
    * `Closed` - 將曲線首尾相接成環狀
    * `Screen` - 僅在關閉 Auto-validate 時可用。啟用時，路徑會「釘」在螢幕上，你可以移動視角與物件，路徑仍保持在畫面位置；關閉時，路徑是 3D 場景的一部分，會隨相機與物件移動。
    * `Accuracy` - 將繪製路徑轉換為 Tube 時使用的曲線點數量。0% 使用最少點數，可能忽略細微曲率變化；100% 則非常精準，使用較多點。
* `Path` - 透過點擊建立曲線點來建立 Lathe。點擊綠色圓圈以驗證路徑。它有一個小的展開選單：
    * `B-spline` - 另一種曲線繪製方式，曲線點通常不直接落在曲線上，但可產生比預設方法更平滑的結果。
    * `Closed` - 讓 Tube 成為封閉環狀
    * `Screen` - 啟用時，路徑會「釘」在螢幕上，你可以移動視角與物件，路徑仍保持在畫面位置；關閉時，路徑是 3D 場景的一部分，會隨相機與物件移動。

#### 車削頂部工具列 {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

選取 Lathe 時，視窗上方會出現工具列提供額外控制。點擊工具列標題可展開／收合，點擊右上角箭頭可將工具列移到視窗頂部或底部。

* `Validate` - 將 Lathe 烘焙為一般多邊形，以便雕刻。
* `Edit` - 顯示曲線點以便操作
* `Mirror` - 在此 Lathe 上方新增 Mirror Repeater 作為父節點
* `Snap` - 將曲線點吸附到附近表面
* `Stable` - 啟用時，曲線 Profile 會被設為 Lathe 中心線的子節點；關閉時，可獨立編輯中心線而不影響曲線，方便建立更複雜形狀。
* `Focus` - 將視角旋轉到能正面觀看曲線 Profile 的角度。
* `Closed` - 將曲線首尾相接成環狀
* `Cap` - 當 Closed 關閉時，在兩端封口、僅起點封口、僅終點封口或不封口之間切換。
* `Hole` - 為 Lathe 加上厚度，轉為 Pipe。可在兩端開孔、僅終點開孔或不開孔之間切換。 
* `B-spline` - 在 Catmull-rom 與 B-spline 插值間切換。
* `X Divisions` - Lathe 旋轉方向的分段數，例如 4 段會產生方形 Profile 的 Lathe。 
* `Constant density` - 啟用時會維持多邊形接近正方形；關閉時可自行設定沿 Tube 長度方向的 `Y divisions`。
* `...` - Lathe 設定選單。

#### 車削設定 {#lathe-settings}
* `Primitive` - 按鈕可啟用／停用 UV，或將 Tube 驗證（Validate）。
* `Post subdivision` - 在驗證前設定多重解析度層級的捷徑。
* `Linear subdivision` - 在驗證前設定線性細分層級的捷徑。 
* `Division X` - 與工具列中的 X Divisions 相同。
* `Division Y` - 與工具列中的 Y Divisions 相同。
* `Curve (Repeater)` - 將曲線 Profile 轉換為 [Curve Repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) 插入 {#insert}
將物件放置在另一個物件表面上。使用方式類似 Stamp 工具，但作用於完整 3D 形狀。

若你從左側工具列選擇一個 Primitive，在任何表面上點擊並拖曳會在點擊處放置一個 Primitive，拖曳距離決定大小。拖曳結束後，Insert 會自動切換到 [Transform](#transform) 模式。

在 Instance 模式下，拖曳會建立並滑動新的實例於表面上。大小會複製自第一個形狀，如此可以在其他表面上放置許多相同尺寸的物件實例。

你不必只插入 Primitive！在 Outliner 中選取「任何」形狀，只要 Insert 處於 Instance 或 Clone 模式，就可以將選取物件的複本拖曳到其他表面上。

若物件有自訂 Pivot，則會以該 Pivot 作為錨點。見下方影片。

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) 變形 {#transform}
以一指與兩指直接在畫面上移動／旋轉／縮放模型，通常是沿著其他物件表面操作。

此工具由左側工具列控制，包含 5 個按鈕：

* `Snap` - 將模型吸附到其他表面
* `Group` - 若選取物件包含物件與實例的組合，可在此決定工具的行為。
* `Move` - 單指拖曳會移動物件。啟用 Snap 時，會沿著手指下方的表面滑動。
* `Rotate` - 單指拖曳會旋轉物件。啟用 Snap 時，會繞著手指下方表面的法線旋轉。
* `Scale` - 單指拖曳會縮放物件。

Transform 可透過兩指快速操作兩種模式：

* 拖曳物件以放置位置。停止移動第一根手指，但不要抬起。
* 在第一根手指仍貼著螢幕時，放下第二根手指並拖曳。物件會縮放。
* 抬起第二根手指，繼續拖曳第一根手指，物件會回到 Move 模式。

你也可以透過第二根手指的點擊手勢切換第二模式：

* 拖曳物件放置位置，停止移動，但不要抬起第一根手指。
* 在第一根手指按住的情況下，用第二根手指點一下螢幕
* 工具會切換到 Rotate 模式。拖曳第一根手指以設定旋轉。
* 再次用第二根手指點一下，工具會切回 Move 模式。

這提供了在另一物體上複製物件的快速流程，例如在地形上散佈岩石。注意 Clone 按鈕也在左側工具列，方便使用：

* 使用 Transform 工具將一顆石頭移到合適位置。
* 放開，按下 Clone 按鈕
* 移動這顆石頭，依需要旋轉／縮放
* 放開，再按 Clone 按鈕
* 移動下一顆石頭，如此重複。

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) 控制器 {#gizmo}
此工具可用來移動、旋轉與縮放物件，以及調整物件的 Pivot。

視窗中的 Gizmo 控制柄具有以下功能：

* `Move` - 拖曳線段＋箭頭可沿 X/Y/Z 軸移動。拖曳 Gizmo 中央的桃色點可在螢幕空間自由平移。點擊紅、綠、藍色方塊可在 X/Y/Z 平面上平移。
* `Rotate` - 拖曳紅／綠／藍色圓圈可沿 X/Y/Z 軸旋轉。拖曳圓圈內的球體可自由旋轉。
* `Scale`- 拖曳外側紅／綠／藍色點可沿 X/Y/Z 軸縮放。拖曳外側紅／綠／藍色圓錐可在 X/Y/Z 平面縮放。拖曳外側桃色圓圈可等比縮放。

![](/images/tool_gizmo.webp)

#### 節點與頂點 {#nodes-and-vertices}

Nomad 中的每個物件都由節點與頂點組成：

* `Node` - 物件的「控制柄」，儲存平移、旋轉、縮放等資訊，稱為 Transformation Matrix。
* `Vertices` - 定義物件表面的點，儲存位置與塗色資訊。

若你有一個由 8 個頂點組成的立方體，可以透過修改 Transformation Matrix 來平移它，也可以直接修改頂點位置。雕刻時通常希望修改頂點；用 Gizmo 移動物件時通常希望修改節點。Nomad 允許兩者皆可。 

#### 左側選單工具列 {#left-menu-toolbar}

左側工具列控制 Gizmo 是作用在節點還是頂點，以及其他功能：

* `Clone` - 建立目前物件的獨立複本，可用 Gizmo 拖曳移動。
* `Instance` - 建立目前物件的實例複本。物件之間是連結的，在其中一個物件上的雕刻變化會同步到所有實例。
* `Group/Object/Vertex/Auto` - 設定 Gizmo 會影響物件的節點或頂點。預設的 `Auto` 模式會嘗試做出最佳判斷。若有多個物件以階層方式成為子物件，`Object` 只會移動目前物件，子物件會保持不動。Gizmo 也可以考慮遮罩與對稱。
* `Pin` - 預設情況下，Gizmo 會移動到選取物件的 Pivot。啟用 Pin 後，Gizmo 會停留在目前位置。
* `Align` - 在物件對齊 Pivot 與世界座標對齊 Pivot 之間切換。
* `Snap rotation` - 啟用旋轉角度的對齊，對齊增量會顯示並可在啟用時編輯。
* `Snap translation` - 啟用平移距離的對齊，對齊增量會顯示並可在啟用時編輯。
* `Pivot` - 啟用時，可以移動與旋轉 Gizmo 而不移動物件本身。啟用後會出現額外選單，說明如下。

#### 樞軸 {#pivot}
啟用 Pivot 模式時，會顯示一個選單以快速調整 Pivot：

**Reset** 
* `Center` - 將 Pivot 移到物件中心
* `Bottom` - 將 Pivot 移到物件底部
* `Align` - 將旋轉重設為與世界座標對齊
* `Mask` - 將 Pivot 移到未遮罩區域的中心

**On Tap**
* `None` - 點擊物件時不做任何事
* `Normal` - 將 Pivot 移動並旋轉到點擊的表面位置與法線方向
* `First` - 將 Pivot 移動（不旋轉）到點擊的表面位置
* `Medial` - 將 Pivot 移到物件在該點下方的幾何中心

#### 控制器設定 {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

##### 矩陣 {#matrix}
* ![](/icons/target.webp) `Move origin` - 將物件移動，使其 Pivot 位於場景中心（原點）。
* ![](/icons/bake.webp)  `Bake` - 將物件目前位置「凍結」，並將平移／旋轉設為 0、縮放設為 1。
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - 讓 Matrix 的數值對應到 Gizmo 控制柄在世界中的實際位置。
* ![](/icons/reset.webp) `Reset` - 快速將平移設為 0、旋轉設為 0、縮放設為 1，並移動與旋轉物件。

::: tip Bake 與 Bake to Pivot 的差異
建立一個 Box，選取 Gizmo 工具，打開並釘住設定選單。預設平移與旋轉為 0，縮放為 1。

啟用 Pivot 模式，將控制柄移到一側，關閉 Pivot 模式。Pivot 已改變，但平移數值仍為 0。 

若想看到 Pivot 的「真實」位置，點擊 `Bake Pivot`。此時平移數值會更新。注意 Box 在此操作中並未移動，Pivot 模式下也不會移動。

再將 Box 移動並旋轉到某處，然後點擊 `Move Origin`。物件會移動，使其 Pivot 位於世界中心，但旋轉保持不變。

點擊 `Reset`，旋轉也會被設為 0。

再度移動並旋轉 Box，這次點擊 `Bake`。Pivot 位置不變，Box 也不動，但平移與旋轉數值會被設為 0。

多練習幾次！理解 Pivot 數值其實是隱藏的，Nomad 會幫你處理，但若需要將 Pivot 設到空間中的實際位置，`Bake Pivot` 就是用來做這件事的。

:::

* `Translation` - 平移 X、Y、Z 數值
* `Rotation` - 旋轉 X、Y、Z 數值
* `Scale` - 啟用等比縮放時為單一數值，關閉時為 X、Y、Z 三軸縮放。
* `Uniform scale` - 切換是否等比縮放或可獨立縮放各軸

-----

* `Compact` - 切換 Gizmo 佈局，將額外控制柄放在旋轉球體內側或外側
* `Widget size` - Gizmo 大小
* `Thickness` - Gizmo 線條粗細
* `Opacity` - Gizmo 透明度
* `Hide on interaction` - 切換拖曳時是否暫時隱藏 Gizmo

-----

* `Tangent roll threshold` - 控制拖曳圓圈把手時旋轉 UI 的行為。若此值為 0，旋轉像轉盤一樣，需繞圈拖曳；若為 90，旋轉像拉溜溜球的線，沿直線向內或向外拖曳。介於 0 與 90 之間時，會同時具備兩種行為：低於該值為線性拖曳，高於該值為圓周拖曳。
* `Numerical input` - 啟用時，單擊 Gizmo 上的控制柄會跳出視窗，可輸入精確數值。

::: warning
[Gizmo](#gizmo)、[Translate](#translate)、[Rotate](#rotate) 與 [Scale](#scale) 各自有獨立的對稱勾選框！

預設這些對稱是關閉的。
:::

左側你可以移動 Gizmo 的 Pivot，下方影片展示實際操作。
這對旋轉特別有用，因為不會改變平移。

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) 面群組 {#facegroup}

Facegroup 讓你將物件的面區分為不同顏色的群組。你可以在 Nomad 中以多種方式使用這些群組：

* 作為遮罩的快速選取方式
* 隱藏／顯示物件的部分區域
* 在不拆分為多個物件的情況下組織模型
* 定義 UV 區域
* 引導 Quad Remesher
* 為 Smooth 等工具提供額外控制

#### 面群組左側工具列 {#facegroup-left-toolbar}

* `Patch ` - 以色塊顯示可用的 Facegroup。未使用的色塊可刪除。點擊色塊可重新命名或更改顏色。加號圖示可建立新色塊。
* `Dot` - 在物件上塗抹以定義 Facegroup。啟用 `+ Face Group` 時，每一筆新筆劃都會自動建立新的 Facegroup，適合快速劃分區域。輕點會對選取區域進行填滿。滑桿控制筆刷半徑。
* `Relax` - 平滑 Facegroup 邊界。對於為 Quad Remeshing 定義乾淨邊界，或在硬表面建模中定義面板非常有用。滑桿控制 Relax 的半徑與強度。
* `Shape selector` - 使用形狀而非筆刷來建立 Facegroup，可選 `Lock+Radius`、`Lasso`、`Polygon`、`Rect` 與 `Ellipse`。更多資訊見 [Shape Selector](#shape-selector)。
* `Auto-pick` - 啟用時，會自動選取筆劃起始處的色塊，並在整個筆劃中套用該色塊。對整理 Facegroup 區域非常有用；若某個 Facegroup 延伸太遠，啟用 Auto-pick，從正確區域開始筆劃，拖曳到邊界即可重新指派正確色塊。

### ![](/icons/tool_hide.webp) 隱藏 {#hide}
隱藏或隔離物件的部分區域。 

主要模式由左側選單控制：

* `Dot` - 在物件上塗抹以隱藏部分區域。
* `Shape selector` - 使用形狀而非筆刷來隱藏，可選 `Lasso`、`Polygon`、`Line`、`Rect` 與 `Ellipse`。更多資訊見 [Shape Selector](#shape-selector)。
* `Show` - 反轉操作，使選取模式改為顯示而非隱藏物件部分。

視窗上方會出現工具列提供額外控制：

* `Clear` - 還原物件，顯示所有被隱藏部分。
* `Invert` - 交換隱藏與顯示的部分。
* `Facegroup` - 使用 Facegroup 快速隱藏區域，點擊某個 Facegroup 會隱藏整個群組。
* `Mask` - 若有啟用遮罩，點擊此按鈕會隱藏被遮罩區域。
* `Delete` - 刪除被隱藏的物件部分
* `Split` - 將被隱藏部分分離為新形狀。

### ![](/icons/tool_measure.webp) 測量 {#measure}
拖曳以量測兩點之間的距離。

### ![](/icons/tool_remesh.webp) 四邊形重拓樸 {#quad-remesher}

![](/images/tool_quadremesher.webp)

此工具會將選取物件轉換為乾淨的四邊形拓樸，並提供密度、邊流（edge flow）、對稱等控制。 

::: tip
Quad Remesher 由 [Exoside](https://exoside.com/) 為 iOS 與桌面平台開發。 

在 iOS 中，它是 Nomad 內的內購項目，一次性付費 16 美元。

在桌面平台，請至 [Exoside](https://exoside.com/quadremesher/quadremesher-buy/) 購買授權。你可以只購買 Nomad 桌面版，或購買適用於所有支援桌面應用程式的跨平台授權。

若你已擁有其他桌面應用程式的 Quad Remesher 授權，可[以較低價格升級為全平台授權](https://exoside.com/quadremesher/quadremesher-upgrade/)。

Quad Remesher 不支援 Android。Android 可使用 Topology -> Misc 選單下的免費開源工具「Quad Remesh - Instant」，但請理解其功能非常有限。
:::

When this tool is activated for the first time, it will ask if you want to enable it as an in-app purchase. Once active, the left and top toolbars will be enabled.

* `Dot` - 這個筆刷會設定目標密度。強度為 100% 時會以紅色繪製，代表在這些區域使用兩倍的目標四邊形密度。強度為 0% 時會以青色繪製，代表在這些區域使用一半的目標四邊形密度。強度為 50% 時會以灰色繪製，代表使用預設的目標四邊形密度。
* `Smooth` - 平滑紅色／灰色／青色的密度過渡。
* `Curve` - 在雕塑表面上勾勒曲線，四邊形重拓撲會使用這些曲線作為邊流向的引導。點擊一條曲線可將其刪除。
* `Path` - 在雕塑表面上繪製路徑，四邊形重拓撲會使用這些路徑作為邊流向的引導。點擊一條路徑可將其刪除。
* `Rect` - 在雕塑表面上繪製矩形，四邊形重拓撲會使用這些矩形作為邊流向的引導。點擊一條路徑可將其刪除。
* `Ellipse` - 在雕塑表面上繪製橢圓，四邊形重拓撲會使用這些橢圓作為邊流向的引導。點擊一條路徑可將其刪除。

#### 四邊形重拓樸頂部工具列 {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

在視窗頂部會出現一個工具列，提供額外的控制項：


* `<Count>` - 點擊此處開始四邊形重拓撲流程，此數值表示目標四邊形重拓撲的數量。
* `Quads` - 向左或向右拖曳以設定目標四邊形數量，或點擊以輸入精確數值。請注意這比較像是參考值而非固定數字，四邊形重拓撲上的各種控制項通常會導致結果無法與此目標完全一致。
* `Half` - 將目標數量設為目前多邊形數量一半的快捷鍵。
* `Same` - 將目標數量設為目前多邊形數量的快捷鍵。
* `Guides` - 顯示導引總數，或點擊以刪除所有導引。
* `Density X` - 點擊以移除所有密度繪製。
* `Density (painting)` - 切換是否使用密度繪製。
* `Face Group` - 切換是否使用面群組來引導四邊形重拓撲。
* `Relax` - 切換在四邊形重拓撲期間是否自動放鬆面群組邊界。如果你已經放鬆／平滑過面群組邊界，請停用此選項。
* `Relax Slider` - 用於放鬆面群組邊界的快捷滑桿。
* `Hard Edges` - 切換是否嘗試維持硬邊。
* `Reproject Vertex` - 切換是否將新的拓撲重新投射回輸入網格。
* `Symmetry` - 切換是否啟用對稱結果。請注意對稱一律是以世界 X 軸為中心計算，因此若你期望得到對稱結果，請確保模型位於原點。
* `...` - 四邊形重拓撲設定選單。 

#### 四邊形重拓樸設定選單 {#quad-remesher-settings-menu}

大多數這些設定也可以在頂部工具列中找到。

* `<Count>, Half, Same` - 與頂部工具列中的 Remesh、Half、Same 按鈕相同。
* `Target Quads` - 與頂部工具列中的 `Quads` 按鈕相同。
* `Adaptive quad count` - 切換是否在高曲率區域使用較小四邊形、在低曲率區域使用較大四邊形。
* `Adaptive size` - 設定自適應程度。100% 會允許最大自適應尺寸，0% 則會讓四邊形大小一致。
* `Auto-Detect Hard Edges` - 切換是否自動調整四邊形重拓撲佈局，以更好地貼合銳利表面。
* `Density (painting)` - 與頂部工具列中的 `Density (painting)` 按鈕相同。
* `Reproject Vertex` - 切換是否將新的拓撲重新投射回輸入網格。
* `Face Group` - 與頂部工具列中的 `Face Group` 按鈕相同。
* `Relax Slider` - 用於放鬆面群組邊界的快捷滑桿。

::: tip

獲得良好且瑕疵最少的四邊形重拓撲的一個流程建議：

* 先為網格建立面群組，以定義理想的四邊形流向。
* 使用面群組放鬆功能，讓面群組邊界變得平滑。
* 進行多邊形簡化（Decimate）。這會確保在面群組邊界上不會有狹長或變形的面。在簡化設定中請確保啟用面群組選項。這會讓三角形邊緣精確地沿著你的面群組邊界排列。 

在四邊形重拓撲選項中，請確保關閉 relax（因為你已經先放鬆過網格），如此應能得到良好的結果。

:::

### ![](/icons/tool_select.webp) 選取 {#select}
使用各種形狀模式來選取場景中的物件。`Unselect` 會將物件從選取集中移除。

### ![](/icons/tool_view.webp) 檢視 {#view}
這個「工具」本身不會做任何特別的事，它只是讓你可以在不修改場景的情況下檢視模型。


## 工具箱內容選單 {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

在工具箱中的工具上按右鍵或長按會叫出一個內容選單。此選單包含以下選項：

* `Save` - 儲存你對該工具所做的任何變更
* `Clone` - 將該工具複製為新的工具捷徑
* `Last save` - 還原到該工具上一次儲存的版本
* `Icon` - 更改該工具的圖示
* `Reset` - 將該工具重設為預設值