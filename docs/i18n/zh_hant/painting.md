# ![](/icons/paint.webp) 繪畫  

控制筆觸的顏色、粗糙度、金屬度，支援填滿繪畫屬性，以及設定繪畫工具如何與圖層、遮罩、隱藏選取互動。

![](/images/paint_overview.webp)  

## 概覽

Nomad 使用 PBR 頂點繪畫。這是什麼意思？

### PBR
PBR（Physically Based Rendering，物理式渲染）是一種廣泛用於電影、電視、遊戲與行動裝置的電腦圖學技術。透過以物理特性為基礎的光源，以及以顏色、粗糙度、金屬度來定義表面，可以達成各種寫實的視覺效果。

### 頂點繪畫

頂點繪畫代表繪畫資訊是儲存在模型的頂點上，而不是貼圖中。由於 Nomad 能處理數十萬、甚至數百萬頂點的模型，你的模型可以擁有非常細緻的表面塗裝；只要能雕出細節，就能為那些細節上色。

這也代表在 Nomad 中繪畫不需要 UV 展開，而 UV 展開在其他 3D 軟體中通常是又慢又技術性的流程。許多其他 3D 軟體無法支援像 Nomad 這樣高的頂點數，不過 Nomad 也提供良好的貼圖烘焙與多邊形簡化工具來協助。

### 貼圖

Nomad 支援貼圖，但必須是匯入模型時就已包含，或是透過將頂點繪畫烘焙成貼圖來取得。 

貼圖基本上就是一張圖片，但在 3D 情境中通常指的是指派給物件的圖片。
要把圖片包覆在模型上，模型需要有貼圖座標（UV）。

Nomad 可以[自動計算 UV](topology.md#uv-unwrap)，但你無法對整體品質有太多控制。

::: tip
一種可能的工作流程：
- 在 Nomad 中雕刻，然後進行 [UV 展開](topology.md#uv-unwrap)
- 如果你已經在 Nomad 中開始上色，可以[將頂點顏色轉成貼圖](topology.md#bake-vertex-colors-to-texture)
- 匯出到 Procreate
- 在 Procreate 中繪製貼圖
- 再匯回 Nomad 進行最後的渲染
:::

以上是概覽，接下來說明繪畫選單的各個部分：


## 筆觸繪畫
![](/images/paint_intensity.webp)  

為此工具啟用繪畫功能，當你需要同時雕刻與上色時很有用。

對於以繪畫為主要功能的工具（例如 Paint、Smudge、Mask），就不會出現這個勾選框。

### 繪畫強度

此滑桿可讓你使用與主要工具強度不同的繪畫強度。

`Alpha`、`Falloff` 和 `Randomize` 勾選框決定這些功能是否會影響繪畫。  
例如你可以在 Clay 工具啟用隨機化，但顏色不會被隨機化。


## 材質
![](/images/paint_material.webp) 

第一個圖示是材質預覽形狀。拖曳 3D 材質預覽可以旋轉它。 

第二個圖示是套用目前 Alpha 與 Falloff 選項後的筆觸預覽。

Material 標題旁的預覽按鈕可在 None、Material 或 Triplanar 間切換。這會決定你在互動調整繪畫屬性時會發生什麼事：

* `None` - 調整屬性時，模型上不會顯示預覽
* `Material` - 調整屬性時，會在物件上預覽材質數值。如果你使用貼圖且模型有 UV，會使用 UV
* `Triplanar` - 會以三平面投影方式預覽材質 

滴管可以用來從場景中的物件取樣所有屬性。

## 材質預設
點擊 3D 預覽形狀會開啟材質預設選單，你可以複製預設來建立自己的預設。

![](/images/paint_presets.webp) 

啟用 `Embed Textures` 與 `Alpha` 切換時，會將此材質使用的任何貼圖儲存在預設中。詳細說明見下文。

## PBR 滑桿
![](/images/paint_sliders.webp) 

[PBR](shading.md#pbr) 繪畫使用 4 個通道：
- `Color` 將被繪製的顏色。可以使用滴管從模型其他部分或參考圖片取色。
- `Roughness` 表示表面有多「粗糙」或「光滑」。粗糙度越低，反射越銳利。
- `Metalness` 表示表面是否為金屬。數值大多應為 0% 或 100%，介於中間的數值應屬少數情況。
- `Opacity` 表示材質的透明程度。嚴格來說它不屬於 PBR 規格的一部分，但在許多情況下很實用。1 為完全不透明，0 為完全透明。請注意，不透明度與折射是不同概念，Nomad 中的折射是透過 refraction 材質處理。 

如果你選擇一個材質預設，會同時繪製 3 個通道（不透明度通常刻意排除）。  
這代表你不只是單純畫「紅色」，而是可以畫出「紅色粗糙金屬」或「白色光滑塑膠」。

方形區塊是貼圖插槽，點擊即可為該屬性使用貼圖，而不是單一數值。

滑桿旁的筆刷圖示會將該屬性填滿整個物件。

勾選框可以啟用或停用該屬性，因此你可以只畫顏色，或只畫粗糙度與不透明度等等。 

以下是不同粗糙度與金屬度組合的範例：

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
在 [Matcap 渲染](shading.md#matcap) 模式下只支援顏色，金屬度與粗糙度會被忽略。
:::

::: tip
在使用貼圖進行 PBR 繪畫時，通常很適合切換到像是 `Stamp` 工具，或在筆觸選單中使用非 Dot 的模式，以避免將貼圖抹糊。

![](/videos/paint_color_texture.mp4)  
:::

::: tip
如果你在多邊形數較低的物件上繪製金屬表面，可以考慮啟用 `Smooth Shading`，不論是[全域](settings.md#smooth-shading)或[每個物件](material.md#smooth-shading)設定。
:::

## Paint all（全部上色）

![](/images/paint_paint_all.webp)

將目前材質套用到整個物件，可使用一般模式的「Paint All」，或以三平面投影方式套用。

會遵守顏色／金屬度／粗糙度／不透明度滑桿旁的勾選框，任何被停用的屬性都不會被填滿。

下方額外按鈕可控制 Paint All 如何進一步受到影響：

| Icon                        | Description                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/tool_mask.webp) | 不會影響被遮罩的區域。                         |
| ![](/icons/tool_hide.webp) | 不會影響被隱藏的區域。                         |
| ![](/icons/opacity.webp)   | 使用上方工具的繪畫強度。                       |
| ![](/icons/layer.webp)     | 不會影響圖層中尚未被繪製的區域。               |
| ![](/icons/triplanar.webp) | 三平面投影設定指示圖示                         |
| ![](/icons/cog.webp)       | 開啟三平面投影設定                             |

### 三平面投影設定
![](/images/paint_triplanar_settings.webp)

與[材質選單中的三平面投影設定](material.md#triplanar)類似，你可以控制投影之間的混合、平鋪與偏移。 

使用此選單頂端的預覽勾選框，可在調整數值時啟用持續預覽。

## 全域材質
若啟用此選項，所選材質會與其他工具共用。請注意，它只會套用粗糙度、金屬度與顏色設定。
