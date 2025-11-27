# ![](/icons/faq.webp) 常見問題

[[toc]]

## 平台 
### 我的專案在裝置上的哪裡？
專案位於 Nomad 主資料夾裡的 `projects` 資料夾中。

在 iOS 上，你可以透過 iOS 的「檔案」App 存取 Nomad 資料夾。

在 Android 上，Nomad 資料夾位於 `Android/data/com.stephaneginier.nomad/files/`。  
在較新的 Android 版本（10/11）中，你已經無法再直接存取 `Android/data` 資料夾。
你可以透過額外的 App 來存取，例如[這個](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer)。
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### 有測試版可以試用嗎？
在 Windows 與 MacOS 上，測試版有時會在[首頁](https://nomadsculpt.com)提供。
<br>
在 iOS 上有私人 TestFlight，請到 [Discord](https://discord.com/invite/8h7BwpRz29) 的 #beta-ios 頻道。
<br>
[網頁示範版](https://nomadsculpt.com/demo) 通常會更新到最新功能。

### 為什麼 Android 有免費試用，但 iOS 沒有？
因為舊的 Android 裝置效能很差（有些新的也一樣……），我不希望大家花錢買了 App，打開卻只看到黑畫面。  
但主要原因是，我覺得在 Android 上付費 App 並不是常態。

### 跑 Nomad 最好的平板是什麼？

簡短結論：iPad。

稍微長一點的答案是：

> 「買 *你負擔得起* 的最新 iPad，如果你真的很討厭 Apple，那就買你負擔得起的最新 Samsung 平板。其他牌子，一定要先測試。」

大家總是想知道更多，所以這裡有個摘要。

Nomad 在較新的 iPad 上表現最好：

* iPad 和 iPhone 可以使用 [Exoside](https://exoside.com/) 的 [Quad Remesher](tools#quad-remesher) 外掛
* 新款 iPad 搭配最新的 Apple Pencil 支援 [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0)，在 Nomad 的某些工具中可以旋轉筆桿來操作
* 最新的 M 系列晶片效能非常快

最新、最貴的 iPad 可以非常快速地算圖，並讓你雕出非常高的細節。

不過，較便宜與較舊 iPad 的效能下降，沒有大家想像中那麼誇張。任何支援 Apple Pencil 的 iPad，跑 Nomad 通常都不錯。舉例來說：

* 2023 年的 iPad Pro 可以流暢處理 500 萬多邊形的雕塑，最終品質的圖片大約 5 秒就能算完。
* 2015 年的 iPad Pro 可以處理約 120 萬多邊形的物件，會有一點延遲，最終品質圖片大約 20 秒可以算完。

這是很大的效能差距，但你也要考慮價格：

* 2025 年的 iPad Pro 全配全新要 *2500 美元*。
* 2023 年的 iPad Pro 在 eBay 上目前約 *400 美元*。
* 2015 年的 iPad Pro 在 eBay 上約 *250 美元*。

多出 400 萬多邊形、快 15 秒，值不值得多花 2100 美元？這就看你自己了。

非 Pro 機種可以更便宜，並提供各種尺寸與效能選擇。現在的 iPad Air 支援第二代 Apple Pencil 與 barrel roll，而且比 Pro 便宜很多。二手與整新品市場選擇更多。

這代表無論你的預算如何，應該都能找到適合你的 iPad。也別忘了，大多數雕塑並不需要上百萬多邊形！如果你能把模型控制在 50 萬多邊形以下，即使是舊 iPad 也能讓你雕得很順。

`那 Android 呢？`

Android 的圖形效能普遍低於 iPad。根據 Nomad 開發者的說法：「Samsung Galaxy Tab S9 跑 Nomad 的速度，大約是 iPad Air 的十分之一。」  
儘管如此，很多使用者對自己的 Samsung 平板仍然很滿意，Nomad 在大多數雕刻情境下都能正常運作。

至於其他 Android 平板，就要小心了。Android 硬體效能差異很大，很難預測 Nomad 會跑得如何。

請務必先用免費、無法儲存的試用版 Nomad 測試。

`那記憶體與儲存空間呢？`

大多數 Nomad 檔案大約在 100MB 以下。這代表現在你能買到的幾乎任何平板，不論是 iPad 或 Android，在儲存空間上都足夠放很多 Nomad 專案。

### 我在一台裝置上買了 Nomad，可以在另一台裝置上用嗎？
只要是同一個商店、同一個帳號，就可以。

例如你在 iOS App Store 購買，就可以在你其他的 iOS 裝置上使用。

如果你在 Google Play 為 Android 平板購買，就可以在你其他 Android 裝置上使用。

但如果你是在 Android 上買的，之後又買了 iPad，那就必須再買一次。

這是因為 Nomad 沒有自己的授權伺服器或訂閱制。Apple/Google/AppGallery 之間也沒有任何授權共享的協議。

### 要怎麼恢復購買？
Google Play 和 AppGallery 都會自動處理同步。

- 到「關於」選單（左上角 Nomad 圖示），點選 `restore purchase`
- 再三確認你登入的是當初購買 Nomad 的同一個帳號（在 Google Play 上）
- 重新啟動裝置
- 有時你需要等幾個小時
- 確認 Google Play App 已更新到最新版本
- 重新安裝 Nomad（如果不想遺失任何東西，請先[備份你的檔案](#where-are-my-projects-located-on-my-device)）
- 你也可以嘗試再按一次購買看看會發生什麼事（注意：同一帳號無法購買同一項目兩次）

:::tip
你可以寫信到 <support@nomadsculpt.com> 聯絡我，但我*唯一*能做的，就是確認某個 email 是否有對應的購買紀錄。

我經常收到回報，說在換新裝置後授權沒有正確更新。  
付款與帳號同步完全由 Google/AppGallery 處理，我無法控制！

最後購買紀錄通常都會恢復，但目前還不清楚有哪些步驟可以加快這個過程。
:::

::: warning
較新的華為裝置無法使用 Google 服務。  
在這種情況下，你需要在 AppGallery（華為應用商店）重新購買 App。
:::

### 你可以翻譯或修正［我的語言］嗎？
我可以相對輕鬆地加入新的語言，但我主要依賴 AI 翻譯，這樣在定期更新時比較好維護。  
翻譯檔可以在[這裡](https://github.com/stephomi/nomad-translation)找到。

## 功能

### 為什麼操作軸（gizmo）不會動？
你可能在左側選單工具列中啟用了[釘選（pin）](tools#left-menu-toolbar)。

### Nomad 裡可以做動畫嗎？
目前不行。時間軸功能可以讓圖層做動畫，這會很有趣，但目前還沒有規劃。

我希望未來能支援骨架／綁定（rigging/skinning），但這會帶來不少挑戰（尤其是和雕刻工具的互動……），所以目前還不確定。

### 可以做真正的低多邊形建模嗎？
目前不行。  
這不太算是 Nomad *Sculpt* 的範疇，但也許未來我會提供一些相關工具。

### 可以做 UV 和貼圖嗎？
簡短回答：可以。詳細回答：不是直接做，但有好幾種方式可以把 Nomad 很強的頂點塗色工具，和 UV、貼圖結合起來使用。

* Nomad 允許你直接在雕塑的頂點上繪製顏色、粗糙度與材質屬性。
* Nomad 支援非常高的頂點數量，讓你在不考慮 UV 的情況下自由繪製。
* Nomad 可以載入貼圖作為筆刷使用，讓你能用貼圖蓋印或繪製。
* Nomad 可以載入已經指派好貼圖的物件，用於算圖。
* Nomad 可以對低多邊形物件進行 [UV 展開](topology.md#uv-unwrap)。
* 可以透過[投射選項](topology.md#reproject-to-vertex)，把貼圖中的顏色／粗糙度／金屬度轉到頂點上。
* 可以透過[烘焙選項](topology.md#bake-to-texture)，把頂點的顏色／粗糙度／金屬度／法線烘焙到貼圖上。
* 烘焙與投射可以在單一物件或多個物件之間進行，也可以在同一物件的最高與最低細分層級之間進行，支援多種烘焙與投射流程。
* 烘焙完成後，匯出 obj 也會一併匯出貼圖，你可以把它們帶到像 Procreate 這樣的 App 直接在貼圖上繪製。

### 可以錄製轉盤（turntable）影片嗎？
目前沒有規劃，iOS 本身有非常好用的[螢幕錄影功能](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados)。

在 iOS 上，你可以從左上角往下滑，點選錄影按鈕。會有 3 秒倒數，將控制中心往上滑關閉，回到 Nomad，使用轉盤功能。完成後，再從右上角往下滑，點選錄影按鈕停止。之後可以在相簿裡剪輯影片，刪除開頭與結尾多餘的片段。

### 可以把［我最愛的功能］加成頂層按鈕嗎？
可以，現在可以在[介面](interface.md)選單中自訂下方工具列，也可以建立浮動工具列。

### 接下來會有哪些新功能？
中長期的開發路線上我有很多想法，但目前還不確定。

修 Bug 與改進現有功能，永遠會比加入新功能優先。

### 可以在 Nomad 裡綁骨架嗎？
目前不行，但有規劃。現在你可以把物件彼此設為父子關係，並調整樞紐點，來做簡單可擺姿的雕塑。

### 可以用超過 4 個燈光嗎？
不行，這是 Nomad 即時算圖引擎的限制。  
你可以透過發光材質與後製中的全域光照來「假裝」更多燈光，如[這個教學](https://www.youtube.com/watch?v=QhrUGH7CuUA)所示。

### 可以匯入 Zbrush 的工具（tools）嗎？
不行，Zbrush 使用的是專有格式。  
你可以把 alpha 貼圖匯出來，在 Nomad 中使用。

### 為什麼顏色跟我畫的不一樣？為什麼算圖時無法得到純白？
想像一下：拍一張白紙的照片、一盞桌燈的照片、和太陽的照片。舊式相機與螢幕會把它們都顯示成「白色」。較新的系統則可以顯示出紙張反射的白、燈泡發出的光、以及太陽超亮的差異。

現代電腦圖學試圖用類似方式運作，模擬光線與材質的物理行為。這叫做 `物理式渲染`（Physically Based Rendering，PBR），Nomad 的 PBR 算圖就是基於這個概念。這樣看起來會更真實、平衡，但常常會讓你畫得很亮的顏色在畫面上變得比較暗。

如果你需要算圖結果更接近你畫的顏色，可以用「非物理式」與「物理式」兩種方式來調整：

非 PBR：
* `在光照選單中使用「Unlit（無光照）」模式`。顏色會完全照你畫的顯示，但也會失去所有明暗。適合快速檢查或較圖像化的輸出。
* `在光照選單中使用「Matcap」模式`。選擇一個較亮、主要是白色、沒有顏色偏移的 matcap。

PBR：
* `使用中性的環境光`。你可以[更換環境](shading.md#environment)為較中性的。避免使用室內環境，因為通常顏色偏重。改用日光戶外或攝影棚環境會比較好。
* `提高光照強度`。如果你在暗房裡拍白紙，只要加一盞燈就好。在環境光中，把曝光拉高到你覺得顏色正確為止，或是加更多單獨燈光並提高強度。
* `提高相機曝光`。如果暗房裡沒有額外燈光，你可以讓相機快門打開久一點，或提高 ISO。在 Nomad 中可以透過後製達到類似效果。到後製選單，啟用後製，往下找到 tone mapping，啟用，然後提高曝光滑桿，直到顏色看起來合適。
* `使用發光顏色（emissive）`。在材質選單中，你可以在貼圖下啟用「emissive」，讓物件看起來像光源。如果在後製設定中開啟全域光照，它會把光打到場景中的其他物件上。你也可以為該材質啟用「unlit」，在沒有貼圖的情況下達到類似效果。

## 當機

### 儲存或重新網格化（remesh）模型時會當機！
你的裝置記憶體（RAM）不足。  
要降低場景的記憶體使用量，你可以使用一些 [拓樸](topology.md) 選項來減少多邊形數量。

::: tip RAM／儲存空間
真正重要的是 RAM 的容量，不是儲存空間（儲存空間通常大得多）。
:::

### 載入專案時會當機！
如果檔案很小，你可以寄給我，我會幫你看一下（email：<support@nomadsculpt.com>）。

否則，很可能是裝置的 RAM 不足。

- 確認你已關閉裝置上其他正在執行的 App。
- 在 Nomad 中先開一個新專案，而不是直接在已有專案開啟的狀態下載入。
- 如果還是當機，唯一的解法就是把[你的專案檔](#where-are-my-projects-located-on-my-device)搬到記憶體較大的裝置上載入。

::: tip
在桌面瀏覽器上，你可以嘗試把檔案載入[這個網址](https://nomadsculpt.com/demo_save/)，簡化場景後再匯出。

有些瀏覽器會限制單一分頁可使用的 RAM 量，所以這個方法不一定有效。

如果你的專案有使用[圖層](layers.md)，你可能會想把它們壓扁（squash）來減少記憶體使用量。
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

### 一啟動 Nomad 就當機！
如果在載入時就當機，代表 Nomad 在讀取 Nomad 資料夾中的某個檔案時出了問題。

大多數情況下，是因為專案太大，不幸超過了 RAM 的上限。

先找到 [Nomad 資料夾](#where-are-my-projects-located-on-my-device)，然後重新命名或移動一些檔案，找出問題檔案。

首先，試著重新命名 `settings.json`。這樣就不會再自動載入上一次的專案。

如果還是不行，試著把最近的檔案從各自的資源資料夾（`projects`、`matcaps`、`environments` 等）移到外面。

你也可以直接重新命名這些資料夾，讓 Nomad 完全忽略它們。  
如果你把 Nomad 資料夾裡的所有檔案都重新命名或移走，效果就跟重新安裝一樣乾淨。

::: tip
當 Nomad 在啟動時載入檔案，它會先把檔案移到 `can_be_deleted/` 資料夾。  
如果載入成功，就會再把檔案移回原本的資料夾。

如果在載入完成前就當機，那 Nomad 在下一次啟動時就會順利啟動，因為它會忽略 `can_be_deleted/` 資料夾。

如果你覺得那個檔案有機會載入成功，可以再試著載入一次。
:::
