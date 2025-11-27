# ![](/icons/sun.webp) 著色（Shading）

此選單控制 Nomad 使用的著色模式、燈光屬性，以及環境光／Matcap 的屬性。

![](/images/shading_overview.webp)



你可以在多種渲染模式之間切換：

| Mode                        | Meaning                    | Description                                                     |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Physically Based Rendering | 使用金屬度／粗糙度進行繪製                                      |
| [Matcap](#matcap)           | Material Capture           | 雕刻時使用，比 PBR 佔用更少 GPU/CPU                            |
| [Unlit](#unlit)             | Surface Color              | 只顯示表面顏色，不含任何打光或陰影                             |
| [Object Id](#object-id)      | Object ID                  | 每個物件給予隨機顏色，適合後續在繪圖軟體中使用                 |
| [Instance Id](#instance-id)  | Instance ID                | 每個實例給予隨機顏色，方便識別共用網格                         |

若想進一步了解金屬度與粗糙度，請參考 [Vertex Paint](painting.md) 章節。

---

![](/images/shading_second.webp)

### Face Group
覆蓋顯示面群（facegroup）顏色。面群是多邊形的顏色選取區塊，可使用 [Face group](tools#facegroup) 工具建立，大多數基本物件也會自動產生面群。

部分工具在面群可見時，會自動依面群進行篩選。

### Show paint
Nomad 可以在雕塑的頂點上儲存顏色、粗糙度與金屬度。你可以用此核取方塊全域切換這些屬性的顯示。

注意：若同時有頂點屬性與貼圖，且兩者皆啟用，最終結果會是兩者數值相乘。

### Show mask
切換 [mask 工具](tools#mask) 的灰階遮罩覆蓋顯示。停用時遮罩也會一併停用，方便暫時不受遮罩影響地快速修改；之後再啟用即可繼續使用原本的遮罩。

### Use Hide

切換隱藏面顯示。注意：這只在你「不」使用 Hide 工具時有效！

### Use textures

Nomad 允許在 [material](material) 選單中為物件指定貼圖。若有指定貼圖，可用此核取方塊全域切換貼圖顯示。







### PBR 與燈光概觀
本手冊不會深入解說實體化（Physically Based）渲染的理論。

有一點很重要：燈光與材質是完全分離的。  
也就是說，你可以獨立繪製物件的顏色、粗糙度與金屬度，而打光則獨立處理。  
這讓你可以先專心繪製物件，再之後調整燈光，而不會破壞整體外觀。

燈光僅在 [PBR 模式](#pbr) 下可用。  
基於效能考量，最多只能使用 4 盞燈。

::: tip
你可以匯入包含超過 4 盞燈的 glTF 檔案，Nomad 會保留所有燈光，  
但效能可能會大幅下降。
:::

::: tip
你可以將物件設為 Unlit/Emissive（不受光／自發光），再在 [post process](postprocess) 選單中啟用全域光照，以此「假裝」有更多燈光。
:::

### 燈光類型概觀

目前支援的燈光類型如下：

| Mode                        | Description                                             | Can cast shadows                                       |
| :-------------------------: | :-----------------------------------------------------: | :----------------------------------------------------: |
| [Directional](#directional) | 無限遠的太陽光                                         | yes                                                    |
| [Environment](#environment) | 與環境 HDR 對應的遠距環境光                            | yes                                                    |
| [Spot](#spot)               | 圓錐形聚光燈				                            | Yes                                                    |
| [Point](#point)             | 全向點光源                                             | Yes, but only through less robust screen-space shadows |

#### Directional
從無限遠處發出光線，強度均勻。  
在場景中的 3D 位置無關緊要，只有方向會影響結果。

你可以將此燈光附加到相機，如此可維持一致的打光。  
例如可用來做輪廓光（rim light）：一盞從角色背後、朝向相機照射的強光，並在你旋轉相機時，始終維持在角色背後。

#### Environment light
使用 [environment hdr](#environment) 可以得到整體柔和的環境光，但若 HDR 中有非常強烈、銳利的光源，其產生的陰影通常會非常柔和，甚至幾乎看不見。  
搭配一盞 Directional light 可以改善，但要手動對齊兩者方向並不容易。

此燈光會自動幫你完成這件事：  
它會自動旋轉，對齊 HDR 中最亮的區域，接著你可以獨立控制其強度與角度（陰影柔和度）。

#### Spot
聚光燈會沿單一方向發光，並受圓錐形範圍限制。

#### Point
點光源會向所有方向發光。  
目前點光源不支援陰影。

#### Shadows
`normal bias` 選項可用來減少常見的陰影瑕疵（acne／peter-panning）。

陰影品質取決於物件相對於整個場景的尺寸。  
若場景中有不需要投射陰影的大型物件（例如一大片平面），請在其 [材質設定](material.md#cast-shadows) 中關閉投射陰影，以提升品質與效能。

## Lights

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Lights checkbox

切換場景中所有直接光源的啟用與否。



### Add light

在場景中新增一盞燈，最多 4 盞。新增燈光後，會顯示燈光清單與按鈕，並在視窗上方加入燈光工具列。

![](/images/shading_lights_icons.webp)

* 文字顯示燈光名稱與亮度。
* 眼睛圖示切換可見度。
* 鉛筆圖示可重新命名燈光。
* 垃圾桶圖示刪除燈光。
* 複製圖示會複製燈光。
* 三個點的圖示會開啟完整燈光編輯器。大部分功能也可從視窗中的工具列操作。

### ![](/icons/spotlight.webp)  Icons

切換在視窗中顯示燈光圖示。

### Light toolbar
![](/images/shading_lights_toolbar.webp) 

選取燈光時，此工具列會出現在視窗上方。

* Show 切換燈光可見度。
* Directional/Environment/Spot/Point 變更燈光類型。點擊可循環切換，長按可開啟選單。
* Intensity 控制燈光強度，數值可高於 1.0，用於非常強烈的光源，搭配後製中的全域光照特別有用。
* 點擊色票會開啟顏色選擇器。Nomad 提供多種選色方式，其中「色溫（Kelvin）」控制可自然地選擇冷／暖光。
* Shadow 切換陰影。
* Size 設定燈光寬度。較寬的燈光會產生較柔和的陰影、較柔和的打光，以及較寬的高光。
* ... 會開啟額外控制項。

### Light extra controls

![](/images/shading_extra_controls.webp) 

注意：部分選項僅適用於特定燈光類型。

* `Clone` 複製燈光。
* `Recenter` 將燈光移回原點。
* `Delete` 刪除燈光。
* `Directional/Environment/Spot/Point` 可變更燈光類型。
* 點擊 `colour swatch`（色票）會開啟顏色選擇器。
* `Intensity` 控制燈光強度。
* `Attachment`（僅 Directional）設定燈光附加到世界或相機。  
  例如：若你在角色背後使用 Directional light 作為輪廓光，當 Attachment 設為 camera 時，旋轉相機時燈光會始終維持在角色背後。
* `Angle`（Directional 與 Environment）為燈光的視覺大小，可想像成太陽在天空中的大小。角度越大，陰影越柔和，高光越寬。
* `Softness`（僅 Spotlight）控制聚光燈圓錐邊緣的銳利度。0 為非常銳利的邊緣，1 為非常柔和，從邊緣到中心有漸層。在視窗中，可拖曳聚光燈圓錐上的藍色小點來互動調整 Softness。
* `Cone angle`（僅 Spotlight）控制聚光燈的擴散角度。角度小時是非常細的光束，170 則是非常寬的光束。在視窗中，可拖曳橘色小點來互動調整圓錐角度。
* `Shadow` 切換目前燈光的陰影。
* `Shadow map` 與 `screenspace` 是兩種不同的陰影計算方式，一般而言 Shadow map 較穩定可靠。
* `Contact` 調整陰影的計算方式。陰影在電腦圖學中是困難問題，容易產生各種瑕疵。你可以為場景中最重要的燈光選擇較精確的陰影計算方式，此選項決定是由 Nomad 自動選擇最重要的燈光，或由使用者手動指定。
* `Tolerance` 若陰影出現瑕疵（例如陰影與物體表面看起來沒有貼合，或陰影內有雜訊與條紋），調整此值通常能改善問題。


## Environment

![](/images/shading_environment.webp)

現實世界中的光線來自四面八方：天空的藍、草地的綠、建築物的紅……這些來自「環境」的光線，可以用環境貼圖來模擬。

Nomad 內建多種室內與室外環境貼圖，具有不同色調與亮度。  
可以多試幾種，看看哪一種最能凸顯你雕塑的細節。

點擊圖片可開啟環境貼圖瀏覽器。在該對話框中選擇「Import...」即可載入自訂貼圖。  
建議使用高動態範圍（HDR）影像，latlong 或 equirectangular 格式，副檔名為 .hdr 或 .exr。  
[www.polyhaven.com](https://polyhaven.com/hdris) 提供大量免費環境貼圖，一般來說 1k HDR 貼圖在品質與容量之間有不錯的平衡。

### Exposure
調整環境貼圖的亮度。  
環境貼圖在搭配一般燈光時常常會過亮，降低曝光可以取得較佳平衡，特別是在 [Post Process](postprocess) 中啟用全域光照時。

### Rotation

由於環境貼圖捕捉的是四面八方的光線，你可以旋轉它，以取得與雕塑最契合的反射與整體打光。

### Attached to camera
將環境貼圖附加到相機。

這會強制打光方向隨相機固定，對雕刻過程特別有幫助，因為光線不會隨場景旋轉而改變。

## ![](/icons/sphere_smooth.webp) Matcap

![](/images/shading_matcap.webp)

如同名稱所示（MATerial CAPture），Matcap 在單一影像中同時包含了打光與材質資訊。  
由於材質本身已包含在 Matcap 中，粗糙度與金屬度的繪製通道會被忽略。  
繪製顏色會與 Matcap 相乘，也就是說：若 Matcap 是黑色／灰色，即使使用白色繪製也不會變得更亮。

藝術家常在雕刻階段偏好此模式，因為它能讓人專注在形體與幾何本身。

點擊球體會開啟影像瀏覽器。你也可以加入自己的 Matcap：  
一般來說，任何球體的照片、渲染，甚至是繪畫，只要裁成正方形並緊貼球體邊緣即可使用。  
網路上有許多 Matcap 資源，其中一個實用的資源是 [nidorx matcap library](https://github.com/nidorx/matcaps)。

### Use global Matcap

通常藝術家會為整個雕塑使用單一 Matcap，但若關閉此切換，每個物件都可以有自己的 Matcap。  
這可以用於風格化表現，創造強烈的視覺效果。

::: tip
關閉此選項，然後為角色的眼睛使用眼球圖片作為 Matcap！
:::

### Rotation
Matcap 是一種特殊形式的環境貼圖，因此同樣可以旋轉。  
你也可以在任何時候於視窗中使用三指左右拖曳來旋轉 Matcap。



## ![](/icons/circle_fill.webp) Unlit

此模式只會顯示表面顏色。  
在你想確認物件表面顏色是否如預期，而不想被燈光、陰影、反射、透明度干擾時特別有用。

此模式也可用於非寫實渲染，達成平面、卡通風格的效果。

## ![](/icons/cube.webp) Object ID

忽略所有打光與表面資訊，每個物件以獨特的純色著色。  
若同時輸出一張 PBR 渲染與一張 Object ID 圖，在繪圖軟體中即可依顏色選取區域，對特定物件進行色彩校正。

注意：這些顏色也會出現在 [Scene 選單的樹狀檢視](scene#tree-view) 中。

### Randomise id

產生一組新的隨機顏色。

## ![](/icons/link.webp) Instance ID

與 Object ID 類似，但同一個實例群組會使用相同顏色。

### Randomise id

產生一組新的隨機顏色。
