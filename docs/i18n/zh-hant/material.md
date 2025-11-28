# ![](/icons/material.webp) 材質 {#material}

此選單可讓你變更目前物件的材質、物件／材質的渲染屬性，並為材質指派貼圖。

![](/images/material_overview.webp)

材質決定物件的外觀，藉由控制它如何對光線與其他物件做出反應。物件的外觀由以下屬性控制：

* `Material type`
* `Color`
* `Roughness`
* `Metalness`
* `Opacity`
* `Reflectance`
* `Emissive/unlit`

這些屬性的不同組合可以達成從寫實、卡通到實驗風格等各種效果。

顏色、粗糙度、金屬度與不透明度都可以繪製，詳見 [Vertex Paint options](painting.md)。

材質類型、反射率、發光／不受光為材質屬性，說明如下。

此選單頂端的複製／貼上按鈕可讓你在物件之間複製材質。

請注意 Nomad 的算圖器是即時算圖器；雖然功能強大，但在某些效果上會優先考量速度而非精準度。 

## 材質類型 {#material-types}

![](/images/material_types.webp)

Nomad 的材質類型有 Opaque、Subsurface、Blending、Additive、Refraction、Dithering、Shadow Catcher。

### ![](/icons/material_opaque.webp) 不透明 {#opaque}
預設模式，將表面視為簡單材質，支援繪製顏色、粗糙度、金屬度與不透明度。

### ![](/icons/material_subsurface.webp) 次表面 {#subsurface}
此模式可模擬會讓光線在內部模糊與散射的材質，例如皮膚、蠟、玉石。

為獲得最佳效果，請切換到 PBR 陰影模式，並至少使用一盞平行光或聚光燈，環境光則建議偏暗。

`Depth` 控制光線從正面進入、在表面下方散射、再從正面表面射出的距離。這會讓硬陰影變柔和，並模糊表面細節。

`Translucency` 控制光線從前方穿到形體背面的散射程度，例如葉片背面透光，或耳朵被強烈背光時的效果。 

### ![](/icons/material_blending.webp) 混合 {#blending}

類似 Opaque，但支援不透明度滑桿，讓材質在實心與透明之間混合。這是單一滑桿控制的不透明度，相對於 Opaque 材質可繪製的不透明度。

::: warning
Blending 模式在複雜或互相交錯的形體上可能造成閃爍與跳動。
:::

### ![](/icons/material_additive.webp) 加成 {#additive}
使用此材質可以讓網格半透明。它類似 Blending 材質，但 Blending 會與周圍混合，而 Additive 則會永遠比後方物件更亮，適合用於光束、火焰、爆炸等明亮效果。

你可以將不透明度設為大於 1，代表物件會更亮。  
若你想使用 [bloom](postprocess.md#bloom) 與 `threshold parameter` 只讓此物件像發光物一樣發亮，這會很有用。

此模式通常比 [Blending](#blending) 有更少的瑕疵（順序無關透明度）。

### ![](/icons/material_refraction.webp) 折射 {#refraction}
此模式可用來模擬玻璃材質。由於即時運算的限制，自我折射與多層折射有一定限制。

模型上繪製的粗糙度會影響折射的模糊程度。  
在預設情況下，Nomad 中建立的每個物件粗糙度約為 25%，因此折射不會完全清晰，而是略為模糊。  
你可以使用 `paint glossy` 按鈕，以粗糙度與金屬度為 0 重新繪製模型（顏色不會被影響）。

這裡有兩種不同的粗糙度：一種控制表面反射的模糊程度，另一種控制內部（折射）的模糊程度。  
然而，由於 Nomad 只有一個繪製粗糙度通道，內部與外部粗糙度會共用同一數值。  
若要使用不同數值（例如棒棒糖有銳利表面但模糊內部），可以使用 `Surface glossiness` 與 `Interior roughness` 滑桿覆寫繪製的粗糙度。

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) 抖動 {#dithering}
以隨機方式捨棄部分像素，讓物件呈現半透明。

### ![](/icons/material_shadow_catcher.webp) 陰影捕捉 {#shadow-catcher}

讓物件本身不可見，只接收陰影。適合將 Nomad 的算圖與其他影像合成。 

::: tip

關於透明度與混合模式的更多資訊可見：https://support.fab.com/s/article/Transparency-Opacity

:::

## 控制 {#controls}

![](/images/material_controls.webp)

### 總是無光照 {#always-unlit}
啟用後，物件會忽略 PBR 與 Matcap，只顯示其顏色繪製結果而不進行打光陰影。  
注意若你使用 [Additive](#additive)，可以直接用黑色來繪製透明度。

### 不透明度 {#opacity}
控制物件看起來多實心或多透明；100% 為完全實心，0% 為完全透明。你也可以繪製不透明度以取得更細緻的控制。

### 反射率 {#reflectance}
控制非金屬材質所接收的反射量。大多數情況下應使用預設值（對應標準的法線角度 4% 反射光），但也可以提高來加強反射與高光，例如角色眼睛的高光。

### 反向裁剪 {#inverse-culling}
反轉表面法線。通常不需要，但若模型看起來是「裡外顛倒」，或搭配關閉 `Two sided` 使用時，可用來製作內部空間，讓最靠近鏡頭的那面牆永遠被隱藏。

### 平滑陰影 {#smooth-shading}
參見 [全域選項](settings.md#smooth-shading)。  
`Auto` 會使用全域設定。

### 雙面 {#two-sided}
參見 [全域選項](settings.md#two-sided)。  
`Auto` 會使用全域設定。

### 著色背面 {#coloured-backface}
參見 [全域選項](settings#two-sided)。  
`Auto` 會使用全域設定。

### 投射陰影 {#casts-shadows}
目前 `Auto` 與 `On` 相同。  
透明物件也會投射陰影（以抖動圖樣模擬混合陰影）。  
若場景中有大型物件不需要投射陰影（例如大地板），請務必關閉其陰影投射。

### 接收陰影 {#recieve-shadows}
目前 `Auto` 與 `On` 相同。

### 線框 {#wireframe}
參見 [全域選項](settings.md#wireframe)。  
`Auto` 會使用全域設定。


## 貼圖 {#textures}

![](/images/material_textures.webp)

若物件具有 UV，則可在頂點顏色／粗糙度／金屬度／不透明度之外，將貼圖套用到材質上。這些貼圖通常來自貼圖烘焙，但也可以使用 Nomad 以外製作的影像。

可套用貼圖的通道有：

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Emissive

點擊貼圖槽會開啟選擇器。當貼圖已指派到材質槽後，再次點擊會開啟貼圖面板：

### 貼圖面板選項 {#texture-panel-options}

![](/images/material_texture_panel.webp)

### 開啟 {#open}
選擇另一張貼圖

### 無 {#none}
移除貼圖

### 不透明度 {#texture-opacity}

若影像具有 alpha 通道，此選項可讓你決定是否將其用於不透明度，或忽略它。

### ![](/icons/link.webp) 鏈結圖示 {#chainlink-icon}

以下各節中的連結圖示啟用時，代表所使用的選項會與其他也啟用連結圖示的貼圖（color、normal、roughness、metalness、opacity、emissive）共享。 

這可確保若你有對齊好的多張貼圖，在變更參數或投影類型時仍能保持對齊。


### 投影 {#projection}
![](/images/material_projection.webp)

設定貼圖如何套用到物件上。

* `Auto` - 若物件有 UV，則使用 UV，否則使用 Triplanar
* `UV` - 使用網格的 UV 座標套用貼圖。若網格與貼圖來自 Nomad 以外，或將從 Nomad 匯出到其他軟體使用，UV 是正確選項。
* `Triplanar` - 沿 X、Y、Z 軸投射貼圖，並混合接縫。 

### 三平面 {#triplanar}
![](/images/material_triplanar.webp)

Triplanar 投影是一種強大且簡單的貼圖套用方式。

Triplanar 就像有 6 台投影機投射同一張影像，分別照射在物件的前、後、左、右、上、下六個面。

若有需要，之後可以將其烘焙成 UV 或頂點顏色。


![](/images/material_triplanar_example.webp)

#### 方法 {#method}

* `Local` - 投影會跟隨物件變換一起移動
* `World` - 投影固定在世界座標，移動物件會讓物件在投影中滑動。

#### 硬度 {#hardness}

控制各投影之間如何混合。100% 代表不做混合，投影邊緣會很銳利。0% 則會在大角度範圍內混合邊緣。預設為 90%，足以隱藏邊緣，同時讓其餘部分保持銳利。

### 統一 {#uniform}

勾選時，所有投影使用相同的硬度。取消勾選時，會額外顯示 X、Y、Z 投影各自的硬度控制。


### 參數 {#parameter}
![](/images/material_parameter.webp)

#### 過濾 {#filtering}
要使用的貼圖過濾方式，`Auto` 為預設，方法有 `Nearest`、`Linear`、`Mipmap`。Nearest 不做過濾，因此貼圖在近距離觀看時可能出現鋸齒狀瑕疵。Linear 與 Mipmap 則有較佳的過濾效果，貼圖在近距離會偏模糊而非鋸齒。

#### 平鋪-X {#tiling-x}
當 Scale 參數大於 1、使貼圖在 UV 上比物件更小時，控制貼圖在 X 軸上的平鋪方式。`None` 代表不重複。`Repeat` 會重複貼圖。`Mirror` 會重複貼圖，且每隔一個重複會反轉，可幫助隱藏平鋪痕跡。

#### 平鋪-Y {#tiling-y}
與 Tiling-X 相同，但作用於 Y 軸。

### 變換 {#transform}
![](/images/material_transform.webp)

在 UV 空間中對貼圖施加額外的 2D 變換。重設按鈕會將數值重設為預設值，連結圖示（當選擇的不是 color 貼圖時）可將此變換與 color 貼圖的變換連結或解除連結。

#### 位移 {#translation}
貼圖在 X 與 Y 方向的位移。

#### 旋轉 {#rotation}
貼圖的旋轉角度。

#### 縮放 {#scale}
貼圖的縮放值，數值越大，貼圖在物件上看起來越小，可搭配 Tiling-X 與 Tiling-Y 控制平鋪行為。

### 統一縮放 {#uniform-scale}
關閉時，Nomad 會顯示獨立的 Scale-X 與 Scale-Y 控制。