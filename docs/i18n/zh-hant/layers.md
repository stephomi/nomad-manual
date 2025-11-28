# ![](/icons/layer.webp) 圖層 {#layers}

此選單包含圖層堆疊，可用非破壞性的方式儲存物件的編輯內容，並提供多種組合與重複利用圖層的方法。

![](/images/layers_overview.webp) 

## 概述 {#overview}

Nomad 的圖層有多種用途。

繪畫資訊（顏色、粗糙度、金屬度、不透明度）與 2D 繪圖軟體中的圖層運作方式類似。你可以建立一個圖層並在模型上繪製。圖層可以開關顯示、調整不透明度、複製、在圖層堆疊中改變順序，以及調整其混合模式。

Nomad 也使用圖層來進行雕刻。圖層可以儲存細微細節（例如皺紋），也可以儲存大幅度變形，使其能像其他 3D 軟體中的 blendshape / shape key / morph target 一樣運作。舉例來說，你可以在不同圖層上雕出不同的臉部表情，然後透過調整圖層滑桿將它們混合成新的表情。

在這種情況下，圖層中儲存的變化是純加成的，與繪畫不同，圖層順序並不重要。

圖層可以透過 [Delete Layer](tools.md#delete-layer) 工具部分刪除，也可以利用圖層中儲存的各種資訊來建立遮罩。

![](/videos/layer.mp4)

::: tip
與多數雕刻軟體不同，更改網格拓樸不會丟失圖層。你可以使用 [Voxel Remesher](topology.md#voxel-remesher)、[Multiresolution](topology.md#multires) 或 [Trim](tools.md#trim) / [Split](tools.md#split) 工具，但請注意，使用 [Voxel Remesher](topology.md#voxel-remesher) 時，圖層品質會受到影響。
:::

::: tip
若將圖層用作 blendshape / morph target，[場景選單](scene.md#object-menu) 中有額外的圖層功能。你可以將圖層分離成物件，或將對應的物件合併回圖層。
:::
----

## 圖層選單 {#layer-menu}

![](/images/layers_menu.webp)

按下 `Add layer` 以建立新圖層。

每個圖層都有名稱、一個控制其強度／係數的滑桿，以及一些選項按鈕。

### 選項 {#options}

| 動作         | 圖示                         | 說明                                                |
| :----------: | :--------------------------: | :------------------------------------------------- |
| 顯示         | ![](/icons/eye_open.webp)   | 顯示／隱藏圖層                                     |
| 混合模式     | ![](/icons/opacity.webp)    | 類似 Photoshop 的混合模式。4 個圖示分別代表顏色、粗糙度、金屬度、不透明度的模式。 |
| 編輯名稱     | ![](/icons/pencil.webp)     | 編輯圖層名稱                                       |
| 刪除         | ![](/icons/trash.webp)      | 刪除圖層                                           |
| 複製         | ![](/icons/clone.webp)      | 複製圖層                                           |
| 向下合併     | ![](/icons/merge_down.webp) | 將圖層與下方圖層（或基礎網格）合併                 |
| 更多         | ![](/icons/more.webp)       | [更多...](#more) 選項                              |

若要將圖層移動到圖層堆疊中的其他位置，長按其名稱後拖曳。

### 更多… {#more}

「More...」按鈕會顯示目前圖層的額外選項：

![](/images/layers_more.webp) 

#### 通道係數 {#channel-factors}

這些控制項可讓你調整此圖層的雕刻／顏色／粗糙度／金屬度／不透明度的量。這些數值會與圖層強度滑桿相乘，例如：若圖層強度為 1，但顏色通道係數為 0.5，則顯示的顏色強度為 0.5。

`Offset` 控制圖層雕刻強度。顏色／粗糙度／金屬度會被限制在 0 到 1 之間，而 offset 則可以是任意正負值。 

::: tip
Offset 可以將一層凸起變成一層凹陷，或將微笑變成皺眉：
![](/videos/layer_happysad.mp4)


對稱的圖層可以被複製，然後用 del layer 分割成左右兩個形狀：
![](/videos/layer_leftright.mp4)

具有負 offset 係數的圖層可以烘焙成空白圖層，以建立新的正向形狀。

offset 係數大於 1 的正向圖層可以用來嘗試更極端的 blendshape。
:::

::: warning
目前圖層僅對三個通道（顏色／金屬度／粗糙度）共用一個不透明度通道。
如果你將多個每通道強度未設為最大值的圖層合併，最終結果可能會與預期不同。

未來也許會為每個通道提供獨立的 alpha 通道，以移除此限制。
:::


#### ![](/icons/tool_mask.webp) 遮罩 {#mask}
每個滑桿旁的遮罩按鈕會從該通道建立遮罩。類似繪圖軟體中使用圖層做選取，這讓你可以將圖層中已完成的工作重複用於其他操作。

#### ![](/icons/preview.webp) 預覽 {#preview}
![](/images/layers_preview.webp) 

啟用後，會預覽此圖層的抽取設定（見下一節）。

當啟用透視（xray）時，只有被抽取出的形狀會是實體，其餘部分會變為透明，對使用負向抽取高度時特別有用。

#### 萃取 {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

`Extract` 按鈕會將圖層內容複製成一個新物件，通常會使用下一節中指定的厚度。

`Closing action` 決定複製的方式：

* None - 只抽取該部分，不產生側面或填補任何孔洞。
* Fill - 以三角形填補孔洞並平滑。不要在平面表面使用此選項。
* Shell - 使用厚度數值與方向選項封閉抽取出的形狀。
* Layer - 抽取圖層差異。

#### ![](/icons/height.webp) 厚度 {#thickness}
![](/images/layers_thickness.webp) 

外殼擠出的深度。正值向表面外側成長，負值向表面內側成長。

此數值旁的正負號會設定擠出的方向：
* Minus ( - ) 從目前表面開始向下擠出。 
* Plus ( + ) 從目前表面開始向上擠出。
* PlusMinus ( ± ) 會讓擠出的上下兩面以相同距離遠離，使其有一半嵌入原始表面。

#### 平滑度 {#smoothness}
![](/images/layers_smoothness.webp) 

若要抽取的區域邊緣鋸齒狀，此滑桿會嘗試將邊緣模糊成較平滑的形狀。 

#### ![](/icons/height.webp) 邊緣迴圈（側邊） {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

當 closing action 為「Shell」時，此區段會顯示。 

`Auto Edge-loop (side)` 會自動計算外殼側面的邊迴圈數量，以產生接近正方形的多邊形。 

若停用，則由 `Division` 滑桿設定側面的分段數量。

_以上為「More...」子選單的全部內容。_

### 進階 {#advanced}
![](/images/layers_advanced.webp)

#### 保留頂層細節 {#keep-top-layers-details}

確保在下層做出大幅變形時，上層的小細節仍然可見。

預設情況下，若你在某圖層雕出細小皺紋，接著在基礎圖層做大幅修改，這些皺紋會被抹除。啟用此選項後，這些小細節會始終浮在下方的大變形之上。以下影片中可看到皺紋細節在預設情況下會被移除，而啟用「keep top layers details」後則會保留：

![](/videos/layers_details.mp4)


#### 介面：展開清單 {#ui-expand-list}

預設的圖層選單只顯示圖層可見性與不透明度。啟用此選項後，會展開每個圖層的完整控制項。

![](/images/layers_expand.webp)

#### 同步變換 {#sync-transform}

若啟用，所有未被選取的圖層會依據變形的旋轉、縮放、扭曲而一併調整。 

若其他圖層預期不應套用你目前的變形，請停用此選項。

當設為 `Auto` 時，只有可見的圖層會被調整。