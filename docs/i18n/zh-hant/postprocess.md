# ![](/icons/postprocess.webp) 後處理 {#post-process}

此選單控制 Nomad 中許多會影響最終渲染外觀的項目。

![](/images/postprocess_overview_drac.webp)

使用後期處理可以大幅改變場景的最終呈現效果。

![](/images/postprocess_overview.webp)
*同一個場景在啟用與停用後期處理時的差異，沒有額外的燈光或材質變更。*

後期處理可能會大幅影響效能，視你的裝置而定。
有一個全域勾選框可以停用所有後期處理，如此你可以快速回到雕刻／建模狀態，而不會遺失你的預設。
在 PBR 渲染中，建議啟用 [環境遮蔽](#ambient-occlusion-ssao)、[反射](#reflection-ssr) 和 [色調映射](#tone-mapping)。

然而，多數情況下在雕刻時你會希望關閉後期處理，以便專注在造型本身與基礎渲染。

## 品質 {#quality}

![](/images/postprocess_quality.webp)
### 最大影格取樣 {#max-frame-sampling}
Nomad 會對單一影格進行一定量的後期處理計算，這可能會看起來有雜訊。此控制項決定要渲染多少影格，並將它們混合在一起，以消除大部分的雜訊偽影。有些效果不需要額外取樣（例如色彩分級），而像是全域光照等效果可能需要數百個取樣才能達到無雜訊的結果。 

在視窗中，當 Nomad 被閒置時可以看到這點：影像品質會逐漸精緻化直到達到最大取樣數，然後停止。這個計算次數也會用在 [檔案選單](files) 的渲染區塊中，當按下「export png」時會套用。

### 解析度倍率 {#resolution-multiplier}
此滑桿控制後期處理的解析度。x1.0 代表以裝置的實際像素解析度進行渲染。x0.5 則會以一半解析度渲染，速度較快但品質較低。大於 1 的值會以更高解析度渲染，再縮小回來。這會帶來更高品質、更少雜訊，但渲染時間也會更長。

### 最大取樣數 {#max-samples}

這會提升後期處理的品質，但通常 `Full resolution` 的影響更大。 

### 降噪器（oidn） {#oidn}

對影像套用去雜訊處理。這可以讓你使用更低的取樣數。此功能僅在啟用 `Full Resolution` 時有效。請注意去雜訊會在所有取樣計算完成後才進行，且可能相當耗費處理器資源。

## 預設瀏覽器 {#preset-browser}
![](/images/postprocess_presets.webp)
點擊圖片會顯示一系列後期處理預設。若要定義自己的預設，先選擇一個，點擊「clone」，再進行修改。要儲存時，點擊預設圖片，再於預設瀏覽器內點擊一次，選擇「save」。

## 反射（SSR） {#reflection-ssr}
啟用此選項後，物件可以反射場景中其他物件，只要那些物件在螢幕上可見。
如果你的場景中有金屬或高光物件，通常應該啟用此選項。
此選項僅在 PBR 模式下有效。

| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## 全域光照（SSGI） {#global-illumination-ssgi}

全域光照模擬光線在表面之間的反彈，例如紅色牆面會將紅色光投射到附近的白色物體上。搭配環境遮蔽與反射使用時，可以大幅提升渲染的真實感。 

`Strength` - 全域光照的強度。 



| SSGI off                   | SSGI on                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_一盞聚光燈位於球體後方，指向天花板。關閉 SSGI 時，只有天花板被照亮。開啟 SSGI 時，光線會從天花板反彈到牆面再到球體。_

## 環境遮蔽（SSAO） {#ambient-occlusion-ssao}
環境遮蔽會讓光線較不易到達的區域變暗（例如角落等）。
此效果只取決於模型幾何形狀。

* `Strength` - 效果強度。
* `Size` - 效果的擴散範圍。
* `Curvature bias` - 效果對表面變化的敏感度。
* `Color` - 乘到遮蔽上的色彩，可用於創意效果。


| SSAO off                    | SSAO on                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO 在主要由環境光照亮的區域最為明顯。在強烈直射光下的區域，AO 效果會弱得多。

:::

## 景深（DOF） {#depth-of-field-dof}
在焦點以外的區域加入模糊效果。

只要在模型上點一下即可改變對焦點。

* `Far blur` - 焦點以外、遠離鏡頭一側的模糊量。
* `Near blur` - 焦點與鏡頭之間區域的模糊量。


| DOF off                   | DOF focus on far ring       | DOF focus on close ring    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## 光暈 {#bloom}
Bloom 會讓場景中明亮的區域產生發光效果。

* `Intensity` - 效果強度。
* `Radius` - 效果擴散範圍。
* `Threshold` - 場景中像素需要多亮才會開始產生光暈。數值設得低會讓幾乎所有東西都發光，設得高則只會讓最亮的像素產生光暈。
* `Color` - 可加入光暈的色彩染色，用於創意效果。

| Bloom off                    | Bloom with radius 0         | Bloom with radius 1         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## 色調映射 {#tone-mapping}
色調映射會將 HDR 數值重新映射到 `[0, 1]` 範圍。
如果不使用（或選擇 `none`），任何大於 1 的色彩分量都會被截斷。
超出此範圍的色彩變化將會遺失。

* `None/Neutral/Agx/ACES` - 要使用哪一種色調映射器。`None` 不做重新映射（但其他控制項仍然有效）。其他選項類似選擇不同的底片，它們會以不同方式處理過曝的亮度與顏色。這是個非常深的主題，可搜尋 tone mapping、Agx、ACES 以取得更多資訊！
* `Exposure` - 影像整體亮度，類似調整相機光圈。這是快速整體變亮或變暗影像的方式。
* `Saturation` - 色彩飽和度。1 為中性，0 為黑白，大於 1 則越來越飽和。
* `Contrast` - 讓暗部更暗、亮部更亮。請謹慎使用，過高的數值可能產生偽影。

注意在停用 `Tone Mapping` 時，有些細節會因像素過亮而消失。

| Tone Mapping off            | Tone Mapping on            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
色調映射可以加強全域光照的效果。如果你將環境貼圖的強度調低、主光源強度調高，再提高色調映射的 `exposure`，就能看見更多反彈光的效果。
:::

## 色彩分級 {#color-grading}
類似 Photoshop 中的曲線工具，可控制影像中色彩的平衡與分佈。`main` 控制整體色彩平衡，`red`／`green`／`blue` 則提供更細緻的單色通道控制。 

| Color Grading off             | Color Grading on             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## 曲率 {#curvature}
偵測曲率變化快速的區域，並在那些區域套用顏色。

* `Factor` - 效果整體強度
* `Bump` - 偵測凸出、銳利變化的程度，並在那裡放置所選顏色（預設為白色）
* `Cavity` - 偵測凹陷變化的程度，並在那裡放置所選顏色（預設為黑色）


| Curvature off                    | Curvature on                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## 色差 {#chromatic-aberration}
模擬鏡頭邊緣的色散偽影，讓光線在畫面邊緣被分解。

* `Strength` - 影像紅／綠／藍通道在畫面邊緣被分離的程度

| Chromatic off                 | Chromatic on                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## 暈影 {#vignette}
模擬鏡頭邊緣變暗的效果。

* `Size` - 疊加在影像上的反向橢圓大小
* `Hardness` - 此橢圓與影像混合時邊緣的柔和或銳利程度。


| Vignette off                    | Vignette on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## 顆粒 {#grain}
加入顆粒效果，可以讓影像看起來不那麼人工。

* `Strength` - 加入影像中的顆粒／雜訊量。


| Grain off                    | Grain on                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## 銳化 {#sharpness}
類似 Photoshop 或照片處理應用程式中的銳利化效果。

* `Strength` - 套用在影像上的銳利化強度。


| Sharpness off                  | Sharpness on                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## 像素藝術 {#pixel-art}
模擬復古遊戲的像素風格。

* `Slider` - 像素大小
* `Allow frame sampling` - 如果你看到很多黑色像素，試著開啟此選項，它會覆寫預設的取樣方式。

| Pixel off                   | Pixel on                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## 掃描線 {#scanline}
模擬老式 CRT 顯示器的外觀。

* `Factor` - 線條強度
* `Spacing` - 線條間距大小

| Scanline off                   | Scanline on                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |


## 抖動 {#dithering}

對像素進行抖動以減少色帶偽影。通常建議啟用，但在某些特定操作時可以關閉（例如匯出深度圖或其他資料專用輸出）。