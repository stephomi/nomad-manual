# ![](/icons/pencil.webp) 筆劃 {#stroke}

---
![](/images/stroke_overview.webp) 

## 概述 {#overview}

你可以自訂大多數工具筆刷的筆畫行為。
這些設定與 2D 繪畫軟體中的選項類似，但有些選項是雕刻與 3D 專用的。

這些選項被分成 5 個子選單：

| Name     | Icon                         | Description                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | 控制筆畫如何套用到模型上                                            |
| Alpha    | ![](/icons/alpha.webp)      | 灰階貼圖如何用於筆刷印章                                            |
| Falloff  | ![](/icons/falloff.webp)    | 控制筆刷強度從中心到邊緣的變化                                      |
| Filter   | ![](/icons/filter.webp)     | 筆刷如何受到模型幾何形狀的影響                                      |
| Pressure | ![](/icons/pressure.webp)   | 控制手寫筆壓力的回應                                                |

::: tip
不是所有筆畫選項都適用於所有工具。當前工具未使用的筆畫選項會被停用或隱藏。 
:::


## 筆劃 {#stroke-1}

### 半徑 {#radius}

![](/images/stroke_radius.webp)

#### 共用半徑 {#share-radius}

啟用後，所有工具會共用同一個半徑；預設則是每個工具有自己的半徑。

#### 尺寸 {#size}

* Screen - 半徑以螢幕單位設定。如果你將半徑設為 100 像素寬，無論放大或縮小都會維持 100 像素寬。
* Constant (3d) - 半徑以 3D 單位設定。舉例來說，如果你建立一個球體並將半徑設為與球體同大小，無論放大或縮小，半徑都會維持與球體同樣大小。


### 筆劃 {#stroke-type}

![](/images/stroke_strokemode.webp)

筆畫可以以多種模式運作：

### ![](/icons/stroke_dot.webp) 點 {#dot}
像一般繪畫筆畫一樣拖曳。 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) 滾動 {#roll}
筆刷的 alpha 會依筆畫方向旋轉，適合用來製作布料縫線。 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lock + radius
以固定的**_高度_**蓋印筆刷筆畫。拖曳會設定縮放與旋轉。
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) 鎖定 + 強度 {#lock-intensity}
以固定的**_半徑_**蓋印筆刷筆畫。拖曳會設定高度與旋轉。
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

`Move` 與 `Drag` 工具有各自的 3 種選項：

### ![](/icons/snake.webp) 拖曳 {#drag}

在筆畫期間會持續更新筆刷半徑內的內容。快速筆畫會讓表面被甩在後面，而慢速筆畫會抓住材質，形成較長的形狀。這是 `Drag` 工具的預設模式。搭配 `Dynamic Topology` 時，可以用來製作類似蛇的擠出形狀。 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) 抓取 {#grab}
在開始筆畫時會選取筆刷半徑內的內容，並維持該選取範圍。這對於較精準的移動操作很有用，你可以仔細調整移動距離，而不會不小心移動超出原本選取的範圍。這是 `Move` 工具的預設模式。
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) 鎖定 + 半徑（拖曳） {#lock-radius-drag}
會忽略使用者設定的半徑，並依拖曳距離自動設定半徑。距離小 = 半徑小，距離大 = 半徑大。使用強度滑桿控制衰減形狀。適合用來粗略塑造有彈性的有機形狀。
![](/videos/stroke_lockradius_drag.mp4) 



### 調整間距強度 {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

間距較低（低於 50%）的筆畫會快速累積，使筆畫比高間距時更強烈。啟用此切換後會進行補償，讓不同間距下的筆畫強度大致相同。

### 筆劃間距 {#stroke-spacing}
在拖曳操作時，每個筆刷印章之間的距離。低於 100% 的數值會重疊，看起來像連續筆畫。高於 100% 則會開始出現間隔，適合雕刻像縫線或拉鍊之類的細節。

### 慢速繩狀穩定器 {#lazy-rope-stabilizer}
筆畫會落後指標位置一段距離。可用來畫出平滑的線條。
![](/videos/stroke_lazy_rope.mp4) 

### 筆劃平滑 {#stroke-smoothing}
平均多個指標位置以獲得更平滑的筆畫。
在高數值下，筆畫會落後指標，但最終會追上。
這對於繪製平滑線條很有幫助。

### 吸附半徑 {#snap-radius}
將新筆畫的起點吸附到前一筆畫的終點。半徑決定搜尋前一筆畫終點的距離範圍。這在繪製長而連續、但中間常常暫停的線條時很有用。

### ![](/icons/silhouette.webp) 剪影 {#silhouette}
![](/images/stroke_silhouette.webp)
預設情況下，筆畫只會影響筆刷半徑內的模型表面。啟用 silhouette 後，筆畫會投射穿過整個模型。這在模型初期打形，或需要側面保持垂直的形狀時非常有用。

投射方向可以明確設定，預設的「Closest」方法會依視角自動偵測最佳角度。 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp) 隨機化 {#randomize}

![](/images/stroke_randomize.webp)

可以分別隨機化筆畫的強度、平移、旋轉與縮放。這可用來創造各種效果，例如搭配 paint 工具的隨機化可產生斑駁的顏色，或搭配 crease 工具可用來製作皮膚細節。

![](/videos/stroke_randomize.mp4) 

### 筆劃偏移 {#stroke-offset}

對筆畫套用固定偏移量。這對於小螢幕裝置很有用，避免手指遮住筆畫。 


## ![](/icons/alpha.webp) Alpha {#alpha}
![](/images/stroke_alpha.webp) 

`Alpha` 是一張會調變筆刷行為的貼圖。
它是一張灰階影像，黑色像素代表沒有變形，白色像素代表完全變形。

點擊 alpha 圖片即可更換。

點擊材質預覽可以從材質預設中載入 alpha。你也可以在此儲存材質預設，並選擇是否將貼圖一併嵌入工具中。

::: tip
貼圖不會被重新取樣，因此過大的貼圖可能會降低效能。
:::

### 反轉像素 {#invert-pixels}
反轉影像的數值，黑色像素會變成白色，白色像素會變成黑色。

::: tip

Nomad 內建附帶的 alpha 無法被反轉。

:::

### 縮放 {#scaling}

Nomad 中的筆刷大小是一個具有使用者定義半徑的圓形。貼圖通常是正方形或長方形，`Scaling` 參數讓你決定貼圖如何填入這個圓形。對於正方形貼圖，數值 0.7 會讓貼圖完整落在圓內。數值 1 則會將貼圖放大到圓形被包在貼圖內部，邊緣會被裁切。

![](/images/alpha_scaling.webp) 

啟用 `Scaling - Y` 可以在垂直方向拉伸 alpha。

![](/images/alpha_scaling_y.webp) 

### 旋轉 {#rotation}

alpha 貼圖會依筆畫方向旋轉。你可以加入旋轉偏移量，如果鎖頭圖示啟用，貼圖會相對螢幕維持鎖定在該旋轉角度。

### 平鋪 {#tiling}
![](/images/stroke_tiling.webp) 

控制貼圖在筆刷輪廓內重複的頻率。平鋪模式可以限制筆畫內只出現單一貼圖、重複貼圖，或鏡像貼圖（每隔一個貼圖翻轉），以建立圖樣或幫助製作無縫貼圖。

![](/videos/alpha_tiling.mp4) 



### 中間值 {#mid-value}

預設情況下，黑色像素代表沒有變形，白色像素代表完全正向變形，例如：使用 clay 筆刷搭配岩石 alpha 貼圖時，只會在 alpha 非黑色的地方將表面往外拉。

如果你希望筆刷將表面往內推，或同時往內推與往外拉，可以調整 mid value。當你將數值設為 0.5 時，alpha 中的中灰不會產生變形，黑色會往內推，白色會往外拉。




## 衰減 {#falloff}

![](/images/falloff_menu.webp) 

這與 [Alpha](#alpha) 類似，但你是用一條曲線來驅動強度。它會與 alpha 結合，因此你可以用貼圖提供細節，再用 falloff 控制工具中心與邊緣的漸層與強度。

當曲線在上方時代表完全變形，在下方時筆刷沒有作用。

你可以把這條曲線想像成筆刷尖端的剖面。下方區域會預覽單次「蓋印」筆刷在模型表面上的效果，如果筆刷有 alpha 貼圖，也會一併顯示，以預覽 falloff 與 alpha 如何互相影響。

### 預設 {#preset}
選取此項時，點擊曲線圖會開啟預設選單。圓滑的曲線會產生較柔和的結果，稜角分明的曲線則會產生較銳利的結果。左側工具列中的 `Sub` 按鈕會反轉 falloff，因此曲線頂端會改為往內推而不是往外拉，或反之。

### Catmull-Rom {#catmull-rom}
選取後，使用者可以自行繪製 falloff 曲線。曲線編輯器的操作方式與 Nomad 其他地方的曲線相同：

* 點擊曲線以建立新控制點
* 拖曳控制點以重新定位
* 點擊控制點在銳利與平滑之間切換
* 將控制點拖曳到鄰近點上以刪除

### B-spline {#b-spline}
選取後，使用者同樣可以自行繪製 falloff 曲線。編輯方式與 Catmull-Rom 相同，但控制點是影響曲線而非直接落在曲線上，有助於建立更平滑的曲線形狀。

曲線編輯器有 3 個按鈕：

| Item     | Icon                        | Description                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | 展開曲線編輯器                                |
| Reset    | ![](/icons/reset.webp)     | 將曲線還原為預設狀態                          |
| Symmetry | ![](/icons/symmetric.webp) | 以對稱「筆刷尖端」的方式顯示曲線              |


### 影響力 {#influence}

* Sphere (3d) - 影響力是依頂點到筆刷中心的距離計算。
* Circle (2d) - 會先將頂點投影到作用平面，再計算其到筆刷中心的距離。這與 alpha 的取樣方式類似。 
* Cylinder - 影響力會以圓柱方式穿過作用區域，供下方的 Silhouette 模式使用。

### 剪影 {#silhouette-1}
預設情況下，筆畫只會影響筆刷半徑內的模型表面。啟用 silhouette 後，筆畫會投射穿過整個模型。這在模型初期打形，或需要側面保持垂直的形狀時非常有用。



## 過濾器 {#filter}

![](/images/filter_menu.webp) 

### 累積筆劃 {#accumulate-stroke}
啟用後，單一筆畫在可新增／移除的材質量上不設上限。例如 `Clay` 工具有啟用此選項，因此材質可以持續堆疊；而 `Brush` 工具則停用此選項，因此在同一區域反覆移動同一筆畫時，最終會停止繼續增加材質。 

### 僅前向頂點 {#front-facing-vertex-only}
此選項會忽略背向的頂點。
如果你想只在薄幾何體的一側繪製而不影響另一側，會很有用。
雕刻時也能使用，但可能會出現一些偽影。

### 允許動態拓樸 {#allow-dynamic-topology}
此選項只在你的網格處於 [Dynamic Topology](topology.md#dynamic-topology) 模式時可用。你可以針對每個工具啟用或停用動態拓樸。

### 連通拓樸 {#connected-topology}
只雕刻與你用工具接觸到的表面相連的頂點。例如搭配 `Move` 工具使用時，即使某部分與另一部分相交，你仍可以只移動其中一部分。
![](/videos/connected_topology.mp4)

### 保護區域 {#protect-area}
![](/images/filter_protect_area.webp) 

這些選項會在各種條件下阻止工具影響網格的部分區域。 

「Auto」選項表示：如果你在 [Shading](shading) 選單中啟用了 hide、mask 或 facegroup 顯示，它們就會被保護；若在該選單中關閉，則保護也會停用。

* `All` - 切換保護篩選是全域套用，還是每個工具各自設定。
* `Hide` - 若部分網格被 hide 工具隱藏，設定是否要保護這些區域。
* `Mask` - 若部分網格被遮罩，設定是否要保護這些區域。
* `Facegroup` - 設定是否只能在第一個接觸到的面群組內使用工具。


### 保持銳利邊緣 {#keep-sharp-edges}
排除法線與表面法線差異過大的點。

這會改變平面區域（Area sampling）的計算方式。

此選項對於以平面為基礎的工具很有用，或當你想在大致平坦的表面上上色而避免顏色外溢時也很實用。

![](/videos/filter_keep_sharp_edges.mp4)

### 區域取樣 {#area-sampling}
某些筆刷或筆畫選項需要一個平面法線與平面位置來運作。

你可以透過將取樣區域設定為工具半徑的比例，來控制如何計算這個平均平面。

在 100% 時，選取圓內的所有點都會被納入計算。

在 0% 時，只會考慮最近的頂點或三角形。`Normal radius` 與 `Position radius` 的數值可以連動，也可以解鎖後分別設定。


### 深度遮罩 {#depth-masking}
![](/images/stroke_depthmask.webp)

排除距離計算平面（Area sampling）高於或低於某一距離的點。

這可以用來只在凸起區域上色，或只在凹陷區域上色。

圖表代表表面的剖面；水平線是表面位置，圓形代表相對於表面上下的筆刷衰減半徑。`Height offset` 是相對於表面、開始進行遮罩計算的百分比位置。`Top area` 與 `Bottom area` 則用來調整在 offset 點之上與之下的衰減比例。

#### 範例：在凹槽中繪畫 {#example-paint-in-cavities}
若只想在凹陷區域上色，將 height offset 設為 -100%，並調整 top area 滑桿，使其遠離水平線。這表示第一次點擊會設定「零」深度，之後只有低於此深度的區域會受到影響。

![](/videos/stroke_depth_cavity.mp4)

#### 範例：在凸起處繪畫 {#example-paint-on-bumps}
若只想在高處上色，將 height offset 設為 +90%，讓圓形底部僅稍微與水平線相交。當你點擊某個「高」區域頂部時，會設定該深度，使得該深度、略低於該深度，以及高於該深度的區域會被上色，而深凹處則會被略過。
![](/videos/stroke_depth_bump.mp4)


## 壓力 {#pressure}
![](/images/pressure_menu.webp) 

控制手寫筆／觸控筆壓力如何影響筆刷。

預設啟用 `Use global settings`，表示所有筆刷共用同一組壓力設定。

### 壓力 - 半徑 {#pressure-radius}

此曲線控制筆刷半徑如何受壓力影響。預設是線性關係，因此如果你的手寫筆壓力回應平順，半徑變化也應該會感覺平順。不過，許多手寫筆的回應並非線性，你可以用這條曲線來補償。例如，如果在高壓力時半徑感覺無法達到最大值，可以使用像「out-pow3」這類向上彎曲的預設曲線，讓半徑較早增大。

此對話框與 falloff 曲線顯示類似，你可以點擊曲線視窗使用預設，或使用 Catmull-Rom 與 B-Spline 模式自行繪製曲線。

如果你想要固定半徑，可以停用此區段。

### 壓力 - 強度 {#pressure-intensity}

與 radius 曲線類似，但用來控制強度。如果你想要固定強度，可以停用此區段。

### 壓力平滑 {#pressure-smoothing}

對手寫筆壓力事件取平均，以獲得更平滑的結果。