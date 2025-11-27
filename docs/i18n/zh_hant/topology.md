# ![](/icons/multires.webp) 拓撲（Topology） 

此選單用來控制 Nomad 中物件的拓撲結構，以及在物件之間、材質貼圖之間烘焙與轉移細節的工具。

![](/images/topology_overview.webp)

Nomad 是以多邊形為基礎的軟體，使用三角形與四邊形來處理幾何。
所謂拓撲，指的是面數量以及點（頂點）彼此連接的方式。

如果你想雕刻或繪製細緻的細節，持續關注拓撲狀況非常重要。

::: tip 如何檢視你的拓撲？
你可以顯示[線框](settings.md#wireframe)，或是簡單地關閉[平滑著色](settings.md#smooth-shading)。
:::

![](/images/topology_top.webp)

Nomad 的拓撲選單包含數個區塊：

| Method                                | Icon                         | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | 使用細分來編輯多個細節層級                                      |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | 以均勻密度重新計算新的拓撲                                      |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | 在雕刻或繪畫時即時局部新增／刪除面                              |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | 簡化、多重 UV、烘焙、重拓撲、重投射                             |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | 基元（Primitive）選項                                           |


## Polygon stats（多邊形統計）

![](/images/topology_stats.webp)

拓撲選單頂部會顯示目前選取物件與整個場景的多邊形資訊。數字分別代表頂點總數、三角形總數與四邊形（四邊多邊形）總數。

點擊這個區域會顯示場景中所有多邊形物件的詳細統計列表。

## ![](/icons/multires.webp) Multiresolution（多重解析度）

![](/images/topology_multires_menu.webp)

### 什麼是 Multiresolution？
Multiresolution 功能主要用於兩種情境：
- 使用平滑細分演算法來提高物件的多邊形數
- 管理多個解析度層級，以便在大範圍與小細節編輯之間切換

![](/videos/multiresolution.mp4)

#### Multiresolution 工作流程
Multiresolution 的一個關鍵特性是：你可以回到較低解析度修改物件，再切回最高解析度而不會失去高解析度細節。所有高解析度細節會自動被重新投射。

::: warning
如果你使用會改變物件拓撲的工具，你會失去該物件所有其他解析度層級！
通常在發生這種情況前會跳出警告，例如當你使用：
- [Voxel Remesher](#voxel-remesher)
- [Dynamic Topology](#dynamic-topology)
- [Trim 工具](tools.md#trim)
- [Split 工具](tools.md#split)
:::


### Multiresolution 滑桿
此滑桿顯示目前物件的細分層級數量。如果有 6 個垂直小條，就代表有 6 個細分層級。圓點代表目前顯示的細分層級。 

### Reverse
當處於最低細分層級時，Reverse 按鈕會嘗試在其下方建立一個更低層級。通常只有在物件一開始就是以細分方式建立（例如在 Nomad 或其他支援多重解析度細分曲面的 3D 軟體中）時才有可能成功。

### Subdivide
*Subdivide* 按鈕會將多邊形數量增加為原本的 4 倍，因此請留意多邊形數，因為它會非常快速地成長！
*Subdivision Surface* 的一個重要特性是：它會收斂成一個*平滑曲面*。
為了理解其運作方式，你可以在一個只有少量多邊形的物件上嘗試按幾次 *Subdivide*。

你可以勾選 `Linear subdivision` 來關閉這種*平滑*行為。

### Delete lower
刪除目前顯示層級以下的所有細分層級。如果誤刪，可以使用 Reverse 重新建立。

### Delete higher
刪除目前顯示層級以上的所有細分層級。

### Linear subdivision
在不進行平滑的情況下細分網格。

### Sharp border
如果物件有 Facegroup，啟用此選項會保留 Facegroup 邊界的銳利度。此設定可針對每個細分層級分別調整（細分滑桿上會在該層級上方顯示一個小圖示）。

### Keep triangles
大多數標準細分曲面系統在細分時會嘗試將所有多邊形轉換為四邊形。啟用此選項會強制細分時保留三角形。

### Lock (LV0)

防止最低細分層級被修改。如果你的物件是由其他應用程式產生，且基礎模型必須維持不變，這點特別重要。當此選項關閉時，在高層級做的大幅變形會影響到第 0 層。

::: tip 

細分預設會平滑所有銳利邊緣。若想保留略為銳利的邊，可以嘗試在前兩個細分層級使用 Linear subdivision 或 Sharp border，然後在更高層級關閉它們。這樣會得到一個半銳利的細分網格。

:::


## ![](/icons/voxel.webp) Voxel Remesher
![](/images/topology_voxel_menu.webp)
使用 `Voxel Remesher` 時，整個網格會被強制重建為均勻解析度的拓撲，也就是所有多邊形大小大致相同。當你不想煩惱拓撲、只想自由雕刻時，這非常實用。

典型的雕刻流程可以從使用低解析度的 `Voxel Remesher` 來封鎖出粗略形狀開始。
當你把網格拉扯得太變形時，只要偶爾按一下 *Remesh*，就能避免過度扭曲。

![](/videos/voxel_remesher.mp4)


::: tip 什麼是 Voxel？
如前所述，Nomad 是多邊形軟體，但 `Voxel Remesher` 是一個例外，它在重拓撲過程中（暫時）採用另一種方法。

一個重要差異是：Voxel 方法不接受自我交錯（self intersection），因此這些交錯會被自動修正。
此外，它也不支援有洞的網格。

這裡所說的洞並不是指「屬性洞」（例如甜甜圈的中空），而是指網格不是「密封／封閉」（watertight/closed）。
實務上，這代表在執行重拓撲前，所有洞都會被填補，類似於 [Trim 工具](tools.md#trim) 或[補洞功能](scene.md#hole-filling)。
:::

### Remesh
執行 Voxel 重拓撲。

### Resolution
計算時所使用的 Voxel 尺寸。調整此參數時，網格上會顯示棋盤格圖案，作為結果解析度的預覽。

### Build multiresolution
為 Voxel 重拓撲結果建立較低的 Multiresolution 層級。如果你使用棋盤格來設定解析度，並將 Build multiresolution 設為 2，最終結果會在目前解析度上保留細節，並在 Multires 分頁中顯示為第 2 層，同時在第 1 層與第 0 層擁有較低解析度的 Multires 網格。這是同時產生乾淨、均勻多邊形網格與低解析度控制網格的好方法。

::: tip 提示：Build multiresolution 與 Stable smoothing

此選項有時會在幾何上產生難以平滑的小「環圈」，造成小凸點。如果發生這種情況，請在 Smooth 工具選項中啟用「Stable smoothing」。 

:::

### Keep sharp edges
啟用後，新頂點會嘗試貼合原始網格上的銳利邊緣，但可能會引入變形。

## ![](/icons/dynamic.webp) Dynamic Topology（動態拓撲）

![](/images/topology_dyntopo_menu.webp)
Multiresolution 與 Voxel 重拓撲是業界常見的拓撲控制方法，但兩者都需要你留意不要把多邊形拉得太長或擠得太密。 

Dynamic Topology 是另一種選擇。當你雕刻時，Nomad 會在筆刷筆劃過程中自動地局部新增或刪除多邊形：在雕刻細節處會增加許多小多邊形，而在平滑其他區域時則會移除多邊形。

請注意，Dynamic Topology 使用的是三角形而非四邊形。線框看起來可能有點雜亂，但通常最好不要太在意線框，只要專注在做出好看的雕塑即可，之後再用 Nomad 其他重拓撲工具產生乾淨的四邊形網格。

可參考下方影片示範。

![](/videos/dynamic.mp4)

### Enabled
開啟 Dynamic Topology。啟用後，筆刷半徑與強度滑桿下方會出現 DynTopo 圖示，可讓你針對每個工具個別切換 Dyntopo。

### Detail
控制細節量，其行為會依據下方「Detail based on...」的選擇而改變。

### Detail based on...
| Method   | Description                                                     |
| :------: | :-------------------------------------------------------------: |
| Screen   | 細節等級取決於物件在螢幕上的顯示大小。Detail 滑桿在 100% 以上時為高細節（小三角形），在 1% 時為低細節（大三角形）。  |
| Radius   | 筆刷半徑決定細節量。小半徑代表高細節，大半徑代表低細節。Detail 滑桿則是此比例的乘數。                     |
| Constant | Detail 滑桿直接決定細節量，不受螢幕大小或筆刷大小影響。             |

::: tip 提示：Radius 模式

為了更好理解 Radius 模式的運作方式，可以一指拖動 Detail 滑桿，同時用另一指改變筆刷半徑，你會看到兩者之間的關聯。

:::

### Prefer...
| Method  | Description       |
| :-----: | :---------------: |
| Speed   | 偏重效能          |
| Quality | 偏重品質          |

當偏重 `Quality` 時，主要有兩點差異：
- 細化會在雕刻前先執行，因此在繪製或雕刻非常細小的細節時，插值產生的偽影會較少
- 細化會持續運算直到收斂到正確的細節層級，而不是漸進式地一點一點增加
 
如此一來，即使你雕刻非常細小的細節或快速筆劃，拓撲也會如預期地被細化。


### Use pressure on radius
僅在 `Radius` 模式下有意義。啟用後，即使筆刷大小受壓力影響，細節等級仍會反映實際筆刷大小。

### Use stroke falloff

在 Dyntopo 計算中一併考慮筆刷衰減曲線與 Alpha。

### Method
無論你在[筆刷](#brush)或[全域](#global)上使用 `Dynamic Topology`，都可以選擇其運作模式：

| Method         | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | 可同時新增與刪除面，這也是上方影片中使用的模式                        |
| Subdivision    | 只新增面，無法刪除面                                                 |
| Decimation     | 只刪除面，無法新增面                                                 |

### Protect masked area
啟用後，被遮罩的區域在拓撲上不會被改變。

### Vertex extrapolation


### Detail
用於重拓撲操作的解析度。如果 Dyntopo 處於「Constant」模式，這裡的值會與上方 Detail 滑桿相同。

### Remesh
使用 Dyntopo 演算法執行全域重拓撲。一般來說，完整重拓撲建議使用 [Voxel Remesher](#voxel-remesher)。

不過，相較於 Voxel 的一個優點是：遮罩區域會被保護，因此你可以更精準地控制哪些地方要增加或減少密度。



## ![](/icons/topo_extra.webp) Misc（其他）

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) 齒輪選單
此選單中的許多工具都有進階選項，可透過區塊標題旁的齒輪圖示開啟。

### Decimation（簡化）

![](/images/topology_decimation.webp)

在盡量保留細節的前提下，使用三角形多邊形來減少多邊形數量。

此功能在你想匯出做 3D 列印時很有用。
但如果你還打算繼續在其上雕刻，通常不建議使用，因為它可能產生不均勻的三角形。

被遮罩的區域不會被簡化。

![](/videos/decimate.mp4)

::: tip

在高多邊形物件上使用 [Quadremesh 工具](tools.md#quad-remesher) 可能需要很長的計算時間，而且結果不易控制。先用 [Facegroup](tools.md#facegroup-1) 與 Decimate 做前處理，可以讓 Quadremesh 跑得更快，也能大幅提升拓撲控制度。

* 先用 Facegroup 規劃出理想的四邊形流向。
* 使用 Facegroup relax 讓 Facegroup 邊界更平滑。
* 執行 Decimate。這會確保在 Facegroup 邊界上不會有過薄或扭曲的面。在 Decimate 設定中啟用 Facegroup，讓三角形邊緣精準貼合 Facegroup 邊界。
* 在 Quadremesh 選項中關閉 relax（因為你已經先放鬆過網格），通常就能得到不錯的結果。

:::

#### Decimate
開始執行簡化操作。

Decimate 按鈕旁的圖示可切換影響簡化的各種選項。圖示旁的百分比代表該選項的強度，可在進階齒輪選單中設定。

* ![](/icons/palette.webp)  `Preserve Painting` - 在有繪畫細節的地方保留較多三角形。
* ![](/icons/triforce.webp) `Uniform Faces` - 優先產生大小均勻的三角形。
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - 儘量保持開放幾何與洞口附近的邊界不變。
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - 儘量保持 Facegroup 邊界不變。
* ![](/icons/checkerboard.webp) `Preserve UV Borders` - 儘量保持 UV 邊界不變。

#### ![](/icons/cog.webp) Decimate 齒輪選單
齒輪選單包含以下進階選項：
##### Preserve painting
勾選可啟用此模式，數值決定繪畫細節被保留的精準度。數值越高，保留的繪畫越多。如果不在意繪畫，可設為 0。


##### Uniform faces
勾選可啟用此模式。數值越高，輸出的三角形大小越接近。

##### Preserve borders
啟用後，邊界不會被簡化。可針對 `Geometry`、`Face Group` 或 `UV` 邊界分別設定權重。

#### Target triangles
設定目標三角形數量。預設為 50%，按下百分比／目標按鈕可在百分比與精確多邊形數之間切換。



### UV Unwrap - UVAtlas

![](/images/topology_uvatlas_menu.webp)
為目前網格計算貼圖座標（UV），通常會偏向產生較多島嶼與切割，以減少變形。

標題與齒輪選單之間的小眼睛圖示可切換在物件上預覽 UV。

![](/videos/unwrap.mp4)

#### Unwrap
為選取物件計算 UV，結果會顯示在背景中。

#### Delete UVs
刪除物件上的 UV。

#### ![](/icons/cog.webp) UVAtlas 齒輪選單
齒輪選單包含以下進階選項：

#### Face Group

使用 Facegroup 來定義 UV 的切割邊。

##### Max Stretch
數值低時變形較少、島嶼較多；數值高時變形較多、島嶼較少。 

##### Island spacing
島嶼之間的間距。數值低時空間利用率較高，但較容易發生貼圖在島嶼之間互相滲色。 

::: warning
計算 UV 可能需要一些時間，建議網格頂點數低於 100k。
:::

::: tip 什麼是 UV？
常見的比喻是包裝禮物：要如何裁切包裝紙，才能在不重疊的情況下完整包覆一個物體？ 

UV 類似這個概念，但不是裁切紙，而是裁切物體本身。想像你的模型是由薄塑膠做成，你會如何切開它、攤平成一片來上色，再重新組裝回去？

再想像模型表面是有彈性的萊卡布料。你可以把它拉平、切開，或兩者並用。但如果你在攤平狀態下畫上棋盤格，重新組裝後棋盤格就會變形。那麼，是多切幾刀、少變形好，還是少切幾刀、多變形好？

UV 就是告訴 3D 軟體在套用貼圖時，該如何「切割與拉伸」物體表面的指令。UV Atlas 工具大致採用「多切割、少變形」的策略。


:::

::: tip UV 與 Nomad 及其他軟體

大多數你在網路上找到的貼圖模型都會使用 UV。Nomad 可以透過[材質面板](material#textures)匯入並顯示這些貼圖。

在 Nomad 中建立模型時，你可以直接在沒有 UV 的物件上繪畫。如果需要匯出到其他軟體，例如 [Procreate](https://procreate.art/)，可以透過 UV 將 Nomad 的顏色資訊「烘焙」成貼圖。 

:::

### UV Unwrap - BFF
![](/images/topology_uvbff_menu.webp)

BFF UV 採取「少切割、多變形」的策略。 

#### ![](/icons/cog.webp) UV BFF 齒輪選單

#### Face Group

使用 Facegroup 來定義 UV 的切割邊。

##### Cone count
定義主要投影的數量。數值越低，島嶼越少但變形越大。

##### Seamless patches
影響 UV 區塊的排布方式，搭配精心建立的 Facegroup 效果最佳。

### Bake -> texture 
![](/images/topology_bake_menu.webp)

貼圖烘焙會將場景中其他可見物件投射到選取物件的 UV 上，產生貼圖。

典型的烘焙流程如下：
- 你有一個帶有細節與繪畫的高模
- 複製一份
- 對複製品進行 Decimate（將 `Preserve painting` 設為 0）
- 對複製品進行 UV Unwrap
- 然後進行 Bake！

Nomad 預設會將場景中所有可見網格納入計算。
你也可以使用 Solo 模式快速隱藏大部分其他網格。
如果沒有其他可見物件，則會將整個場景納入計算。

完成後，你會得到一個低解析度網格，但仍保留原物件大部分的繪畫與細節。

操作完成後，頂點顏色會被移到一個新的停用圖層，以免干擾貼圖。

#### From itself
將目前物件最高 Multires 層級烘焙到最低層級。這種方式設定簡單，但若你需要更多控制，下一個選項會更實用。

#### From high-res ()
將場景中其他可見物件烘焙到選取物件上。括號中的數字代表會被當作高模目標的可見物件數量，這些物件會被烘焙到目前帶有 UV 的低模上。其他物件不需要在佈局或拓撲上與被烘焙物件相似，因此可以支援多種彈性的烘焙流程。

#### Resolution
烘焙貼圖的解析度。貼圖一律為正方形，因此 1024 代表 1024x1024 影像。 

下方按鈕是常用解析度的快捷鍵。作為參考，512x512 相對較小，適合網頁圖形與簡單幾何；4096x4096（簡稱 4k）則適合高品質渲染。

#### ![](/icons/cog.webp) Bake 齒輪選單
![](/images/topology_bake_gear_menu.webp)
齒輪選單包含以下進階選項：

##### Normal, Roughness, Metalness, Color, Emissive, Opacity
這些勾選框決定要烘焙哪些屬性，每種屬性會輸出到各自的貼圖中。烘焙完成後，這些貼圖會自動加入目前物件材質的貼圖欄位。

##### Backup
為了預覽烘焙貼圖，物件原本的繪畫資訊必須被停用。啟用此選項會將任何繪畫資訊轉移到新的圖層作為備份，方便隨時啟用／停用。

#### Cage radius
調整從烘焙物件發射射線搜尋目標物件的距離。預設距離較小，以避免偽影，但若目標物件離烘焙物件較遠，可適度增加。

##### Ray offset
調整烘焙計算在烘焙物件上開始的位置。預設從表面外側 5% 處開始，可避免大多數常見偽影。如果目標物件離烘焙物件非常遠，可能需要增加此偏移量。


### Reproject to vertex

![](/images/topology_reproject_menu.webp)

將雕刻細節、繪畫、圖層、貼圖等投射回頂點屬性。

可以把它視為烘焙的反向操作：烘焙是將頂點屬性轉成貼圖，而重投射則是將貼圖（與其他屬性）轉回頂點。

::: tip
使用 `Bake to texture` 或 `Reproject to vertex` 時，頂點顏色與材質貼圖都會被一併考慮。
:::

#### From itself
將材質中的貼圖轉換為頂點屬性。此按鈕只有在物件具有 UV 且材質中啟用了貼圖時才會可用。

::: tip 提示：貼圖繪製
Nomad 不直接支援在貼圖上繪製與編輯，但可以透過「貼圖 -> 頂點」與「頂點 -> 貼圖」的投射流程達到類似效果：

1. 準備一個帶有 UV 的低多邊形物件
1. 將貼圖載入其材質
1. 將其細分到足夠繪畫的密度
1. 在 `From itself` 模式下執行 `Reproject to vertex`，此時貼圖會被轉成頂點屬性
1. 進行繪畫、平滑、塗抹、蓋章等各種編輯
1. 在 `From itself` 模式下執行 `Bake to texture`，這些編輯會再度被轉回貼圖
:::

#### From high-res ()
將任何可見物件轉換為選取物件上的頂點屬性。按鈕上的數字代表可見物件數量。

::: tip
重投射其他物件不僅能用來轉移顏色資訊，也可以用來將頂點投射到其他物件上，例如將繃帶投射貼合到角色身上。
:::

#### ![](/icons/cog.webp) Reproject 齒輪選單
齒輪選單包含以下進階選項：

#### Vertices, Roughness, Metalness, Color, Opacity, Opacity->Mask, Mask, Layers, Face Group
這些勾選框決定哪些屬性會被投射到選取物件上。 

#### Relax
在重投射過程中，可對選取網格的佈局進行一定程度的平滑或放鬆，以更好貼合目標。Smooth 適合高多邊形網格；Relax 適合低多邊形網格；Auto 則交由 Nomad 自動判斷最佳方式。

#### Iterations
在重投射過程中，Relax 操作要執行的次數。

#### Cage radius
調整從選取物件發射射線搜尋目標物件的距離。預設距離較小，以避免偽影，但若目標物件離烘焙物件較遠，可適度增加。

#### Ray bias
數值較低時會偏向投射到目標表面上最近的點；數值較高時則偏向沿著表面法線方向的交點。 

#### Ray offset
調整重投射計算在選取物件上開始的位置。預設從表面外側 5% 處開始，可避免某些偽影。如果目標物件離選取物件非常遠，可能需要增加此偏移量。


### Quad Remesh - Instant
![](/images/topology_quadremesh_menu.webp)
使用 [Wenzel Jakob、Marco Tarini、Daniele Panozzo、Olga Sorkine-Hornung 所提出的 Instant Meshes 演算法](https://igl.ethz.ch/projects/instant-meshes/)進行重拓撲。它會分析網格流向並建立乾淨的四邊形拓撲。

::: tip
在 iOS 與桌面版上，[Quad remesher 工具](tools#quad-remesher)能提供更好的結果與更多控制。
:::

#### Remesh
開始執行 Instant Meshes 操作。

#### Target quads
Quad Remesh 嘗試產生的四邊形多邊形數量。

#### ![](/icons/cog.webp) Quad Remesh Instant 齒輪選單
齒輪選單包含以下進階選項：

##### Crease angle
用來判斷銳利角度的閾值，會嘗試利用這些資訊來引導重拓撲。

#### Max fill hole
演算法有時會產生不想要的洞。如果某個洞的頂點數少於此數值，就會被自動填補。

### Holes（洞）
![](/images/topology_holes_menu.webp)
大多數情況下，你的物件應該是密封的，也就是網格是「封閉」的。

如果物件有洞，可以使用此功能填補。請注意它只適用於「單純」的洞，無法將兩個獨立邊界「焊接」在一起。

![](/videos/hole_filling.mp4)

::: tip
當你執行 Voxel Remesher 時，所有洞都會自動被封閉，無論你是對單一或多個網格操作。
:::

#### Close holes
執行補洞動作。

#### ![](/icons/cog.webp) Holes 齒輪選單
齒輪選單包含以下進階選項：

##### Detail
用來填補洞口的多邊形密度。拖動此滑桿時，模型上會顯示棋盤格圖案，作為三角形大小的參考。勾選旁邊的核取方塊則會停用此功能，僅使用現有頂點，通常會在洞口上產生又長又細的三角形，較難雕刻。

##### Fill non-manifold
嘗試填補非流形（non-manifold）的洞。

##### Face Group

在補洞時，每個洞是否要各自建立一個 Facegroup（Auto）、全部共用一個 Facegroup（Off），或完全不建立 Facegroup（On）。

### Force Manifold
![](/images/topology_forcemanifold_menu.webp)
嘗試清理非流形邊。對於不支援一條邊同時被兩個以上面共用的外部軟體來說很有用。

#### Clean
執行清理動作。
#### ![](/icons/cog.webp) Force manifold 齒輪選單
齒輪選單包含以下進階選項：

#### Delete small faces
用來刪除並合併過小多邊形的閾值。


### Triplanar
![](/images/topology_triplanar_menu.webp)
將網格轉換為[三平面（triplanar）](scene.md#triplanar)基元。
在此過程中你很可能會失去大量細節。

#### Force cubic
強制三平面為立方體。否則三平面會貼合物件的最小包圍盒。

#### Convert
執行三平面轉換。

#### Resolution
三平面操作中所使用的 Voxel 尺寸。

## ![](/icons/dot.webp) Primitive
目前選取基元的參數。這些參數也可以在視窗中的基元工具列中找到。

![](/images/topology_primitive_screenshot.webp)
