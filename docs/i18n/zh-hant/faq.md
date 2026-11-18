# ![](/icons/faq.webp) 常見問題 {#faq}

[[toc]]

## 平台 {#platform}
### 我的專案存放在裝置的哪裡？ {#locate}
專案位於 Nomad 主資料夾內的 `projects` 資料夾。

在 iOS 上，您可以用 iOS 的「檔案」App 存取 Nomad 資料夾。

在 Android 上，Nomad 資料夾位於 `Android/data/com.stephaneginier.nomad/files/`。  
在較新的 Android 版本（10/11）上，您已經無法直接存取 `Android/data` 資料夾了。
您可以透過另一個應用程式存取，例如 [這一個](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer)。
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### 有辦法參加 Beta 測試嗎？ {#beta}
Windows 和 MacOS 可能會在 [官方網站](https://nomadsculpt.com) 上提供 Beta 版。
<br>
iOS 有私人的 TestFlight，請到 [Discord](https://discord.com/invite/8h7BwpRz29) 的 #beta-ios 頻道。
<br>
[網頁示範版](https://nomadsculpt.com/demo) 通常會更新到最新的功能。

### 為什麼 Android 有免費試用，iOS 卻沒有？ {#android-trial}
因為舊的 Android 裝置很糟（有些新的也是……），我不希望有人買了 App，打開卻只看到一片黑畫面。
不過主要的原因是，我覺得付費的 Android App 並不是常態。

### 執行 Nomad 最好的平板是哪一款？ {#best-tablet}

簡單說：iPad。

稍微長一點的答案是 

> 「您_負擔得起_的最新款 iPad；除非您真的很討厭 Apple，那就選您負擔得起的最新款 Samsung 平板。其他的，請先測試。」 

大家總是想知道更多，所以這裡做個整理。

Nomad 在較新的 iPad 上執行得最好：

* iPad 和 iPhone 可以使用 [Quad Remesher](tools#quad-remesher) 外掛，由 [Exoside](https://exoside.com/) 開發
* 支援最新款 Apple Pencil 的新 iPad 支援 [筆身旋轉](https://www.youtube.com/watch?v=XcDQazDYpo0)，在 Nomad 的某些工具中可以轉動筆身來操作。 
* 最新的 M 系列晶片效能非常快。 

市面上最新、最貴的 iPad 能非常快速地算繪最終影像，也能讓您雕刻大量的細節。

不過，較便宜和較舊的 iPad 效能下降的幅度，並沒有大家想像的那麼大。任何支援 Apple Pencil 的 iPad 都能相當順暢地執行 Nomad。例如：

* 2023 年的 iPad Pro 可以流暢地處理 500 萬個多邊形的雕刻作品，一張最終品質的影像 5 秒就能算繪完成。
* 2015 年的 iPad Pro 可以處理 120 萬個多邊形的物件，稍微有點卡頓，一張最終品質的影像需要 20 秒算繪。

效能差距很大，但您也得把價格考慮進去：

* 2025 年的 iPad Pro 全新、選配全上要 *2500 美元*。 
* 2023 年的 iPad Pro 目前在 eBay 上大約 *400 美元*。
* 2015 年的 iPad Pro 在 eBay 上大約 *250 美元*。

多 400 萬個多邊形、省下 15 秒，值得多花 2100 美元嗎？這就由您決定了。

非 Pro 的型號還可以更便宜，尺寸和效能的選擇也很多。目前的 iPad Air 支援具備筆身旋轉功能的第二代 Apple Pencil，價格也比 Pro 便宜許多。二手和整新機市場還有更多選擇。 

也就是說，不管預算多少，您應該都能找到適合自己的 iPad。另外別忘了，大多數雕刻作品都用不到幾百萬個多邊形！只要能控制在 50 萬個多邊形以下，即使是舊的 iPad 也能讓您流暢地雕刻。

`那 Android 呢？`

Android 的圖形效能比 iPad 差。根據 Nomad 開發者的說法：「Samsung Galaxy Tab S9 執行 Nomad 的速度，比 iPad Air 慢了一個數量級」。話雖如此，很多使用者對他們的 Samsung 平板都很滿意，大部分的雕刻工作 Nomad 都能順利執行。 

至於其他 Android 平板，請小心。Android 硬體的效能差異很大，很難預測 Nomad 會跑得如何。

請先用 Nomad 無法存檔的免費版本測試看看。 

`那記憶體和儲存空間呢？`

大部分的 Nomad 檔案都在 100MB 以下。也就是說，現在買的幾乎任何平板，不論是 iPad 還是 Android，都有足夠的空間存放您的 Nomad 專案。


### 我在一台裝置上買了 Nomad，可以在另一台裝置上使用嗎？ {#multi-devices}
只要使用同一個 App 商店和同一個帳號，就可以。

例如，如果您是在 iOS App Store 購買的，就可以在您其他的 iOS 裝置上使用。

如果您是在 Google Play 上為 Android 平板購買的，就可以在您其他的 Android 裝置上使用。

但是，如果您在 Android 上買了 Nomad，之後又買了 iPad，就需要再買一次。

這是因為 Nomad 沒有自己的授權伺服器或訂閱制。Apple、Google、AppGallery 之間也沒有共用授權的協議。 


### 如何恢復我的購買項目？ {#restore}
Google Play 和 AppGallery 都會自動處理同步。

- 進入「關於」選單（左上角的 Nomad 圖示），然後點 `恢復購買項目`
- 再次確認您登入的是購買 Nomad 時使用的同一個帳號（在 Google Play 上）。
- 重新啟動裝置
- 有時需要等上幾個小時
- 確認 Google Play 應用程式已更新到最新版本
- 重新安裝 Nomad（如果不想遺失任何東西，請記得先 [備份您的檔案](#locate)）
- 您可以試著再購買一次，看看會發生什麼事（注意：同一個帳號無法重複購買同一個項目）

:::tip
您可以寫信到 <support@nomadsculpt.com> 和我聯絡，但我*唯一*能做的，就是確認某個電子郵件是否有對應的購買紀錄。

請注意，我經常收到換了新裝置之後授權沒有正確更新的回報。
付款和帳號同步完全不在我的控制範圍內，這些都是由 Google/AppGallery 處理的！

購買項目最後一定都會恢復，但要怎麼加快這個過程，目前並不清楚。
:::

::: warning
較新的華為裝置無法使用 Google 服務。
這種情況下，您需要在 AppGallery（華為應用程式商店）上重新購買 App。
:::

### 可以翻譯或修正 [我的語言] 嗎？ {#locale}
新增一種語言對我來說相對容易，但我是依靠 AI 翻譯，因為這樣在經常更新時比較好處理。
翻譯檔案可以在 [這裡](https://github.com/stephomi/nomad-translation) 找到。

## 功能 {#features}

### 為什麼軸向變換 Gizmo 動不了？ {#gizmo-not-moving}
您可能在 [左側選單工具列中啟用了釘住](tools#left-menu-toolbar)。 

### 可以在 Nomad 裡做動畫嗎？ {#animate}
目前還不行。能為圖層做動畫的時間軸功能也許會很有趣，但目前並沒有具體的計畫。  

我希望未來能支援骨架綁定／蒙皮，但這會帶來一些挑戰（特別是和雕刻工具之間的互動……），所以目前還不確定。


### 可以做正規的低多邊形建模嗎？ {#lowpoly}
目前還不行。
這其實不在 Nomad *Sculpt* 的範圍內，不過未來也許會提供一些工具。


### 可以做 UV 和貼圖嗎？ {#texturing}
簡短的回答：可以。詳細的回答：不能直接做，但有好幾種方式可以把 Nomad 出色的頂點繪畫工具和 UV、貼圖結合起來。

* Nomad 可以把顏色、粗糙度和材質屬性直接繪製在雕刻作品的頂點中。
* Nomad 支援非常高的頂點數，讓您繪畫時不必擔心 UV。
* Nomad 可以載入貼圖用在筆刷上，用貼圖來蓋印和繪畫。
* Nomad 可以載入已經指定好貼圖的物件，用於算繪。
* Nomad 可以為多邊形較少的物件做 [UV 展開](topology.md#uv-unwrap-uvatlas)。
* 顏色、粗糙度、金屬度可以透過 [投影選項](topology.md#reproject-to-vertex) 從貼圖轉移到頂點。
* 顏色、粗糙度、金屬度、法線可以透過 [烘焙選項](topology.md#bake-texture) 從頂點烘焙到貼圖
* 烘焙和投影可以在單一物件或多個物件之間進行，也可以在單一物件的最高與最低細分層級之間進行，支援各種烘焙和投影的工作流程。
* 烘焙之後，匯出 OBJ 時也會一併匯出貼圖，可以拿到像 Procreate 這樣的 App 中直接在貼圖上繪畫。

### 可以錄製轉盤展示影片嗎？ {#video}
目前沒有計畫，iOS 有一個非常好用的 [螢幕錄製功能](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados)。

在 iOS 上，從左上角往下滑，然後點錄製按鈕。它會倒數 3 秒，把選單滑開回到 Nomad，然後使用轉盤功能。完成後，再從右上角往下滑，並再點一次錄製按鈕。到照片圖庫中編輯影片，剪掉開頭和結尾多餘的片段。

### 可以把 [您最愛的功能] 做成頂層按鈕嗎？ {#interface}
可以，下方工具列現在可以在 [介面](interface.md#shortcuts) 選單中自訂，也可以建立浮動工具列了。

### 接下來會有哪些功能？ {#next-features}
對於中長期的規劃，我有很多想法，但還沒有決定。  

修正錯誤和改善現有功能，永遠會比新增功能更優先。


### 可以在 Nomad 裡做骨架綁定嗎？ {#rigging}
不行，但已經在計畫中。目前您可以把形狀設定父子關係並調整軸心，做出可以簡單擺姿勢的雕刻作品。

### 可以使用超過 4 盞燈嗎？ {#lights}
行動裝置上最多可以使用 4 盞燈，桌面版最多 6 盞。這是 Nomad 內建即時算繪引擎的限制。可以用自發光物件搭配後製中的全域光照來模擬更多燈光，如 [這個教學](https://www.youtube.com/watch?v=QhrUGH7CuUA) 所示

### 可以匯入 Zbrush 的工具嗎？ {#zbrush-import}
不行，Zbrush 使用的是專有格式。不過您應該可以把 Alpha 貼圖取出來，在 Nomad 中使用。 

### 為什麼顏色和我畫的不一樣？為什麼算繪時無法呈現白色？ {#paint-pbr}
想像一下分別拍攝一張紙、一盞檯燈和太陽。舊式的相機和螢幕會把它們全都拍成「白色」。較現代的系統則能呈現出紙張反射的白、檯燈發出的光，以及超亮的太陽之間的差別。

現代的電腦圖學也嘗試用類似的方式運作，模擬光線與表面的物理特性。這稱為 `基於物理的算繪`，也就是 PBR，而 Nomad 的 PBR 算繪器就是以此為基礎。這樣看起來寫實又平衡，但塗上的鮮豔顏色往往會顯得比較暗。

如果需要讓算繪結果更接近塗上的顏色，可以用非物理和基於物理兩種方式來解決：

非 PBR：
* `使用著色選單中的「不受光」模式`。顏色會完全照塗上的樣子顯示，但也會失去所有明暗。適合快速檢查，以及較偏平面設計風格的輸出。
* `使用著色選單中的「材質捕捉」模式`。選擇較亮、以白色為主、沒有色偏的 MatCap。

PBR：
* `使用中性的環境`。您可以 [更換環境](shading.md#environment)，改用比較中性的環境。避免使用室內環境，因為它們通常色彩較重。建議改用白天的戶外或攝影棚環境。
* `加強光照`。如果在暗房裡拍一張白紙，您自然會多加一點光。在環境光上調高曝光滑桿，直到顏色看起來對了；或是加入更多個別的燈光，並提高它們的強度。
* `提高相機曝光`。如果暗房裡沒有多餘的燈，您可以讓相機的快門開久一點，或使用更高的 ISO 感光度。在 Nomad 中，可以用後製達到類似的效果。進入後製，啟用它，往下找到色調映射，啟用，然後調高曝光滑桿，直到顏色看起來對了。
* `使用自發光顏色`。在材質選單中，您可以在貼圖下方啟用「自發光」，讓物件看起來像一個光源。如果在後製設定中開啟全域光照，它還會把光投射到場景中的其他物件上。您也可以為那個材質啟用「一律不受光」，不用貼圖也能得到類似的效果。

## 當機 {#crashes}

### 儲存或重新網格化模型時當機了！ {#crash-remesh}
您的裝置記憶體（RAM）不足了。  
若要減少場景的記憶體用量，可以使用一些 [拓樸](topology.md) 選項來減少多邊形的數量。

::: tip RAM／儲存空間
重要的是 RAM 的大小，而不是儲存空間（儲存空間通常大得多）。
:::


### 載入專案時當機了！ {#crash-load}
如果檔案不大，您可以寄給我，我會看一下（請寄到 <support@nomadsculpt.com>）。

否則，裝置很可能是 RAM 記憶體不足。

- 確認已關閉裝置上其他開著的 App。
- 在 Nomad 中開始一個新專案，而不是在已開啟專案的狀態下載入。
- 如果還是當機，唯一的辦法就是在記憶體更大的裝置上載入 [您的專案檔](#locate)。

::: tip
如果行動裝置無法載入專案，可以試試 [桌面版](https://nomadsculpt.com)。您可以在示範模式下免費使用它來匯入和匯出專案，不過只有少數幾個編輯工具可以使用。

如果您的專案使用了 [圖層](layers.md)，可以考慮把圖層合併，以減少記憶體用量。
:::

### 啟動 Nomad 時當機了！ {#crash-start}
如果在載入時當機，表示 Nomad 在處理 Nomad 資料夾中的某個檔案時遇到了困難。

大多數情況是因為專案太大，很遺憾地超出了 RAM 的上限。

找到 [Nomad 資料夾](#locate)，然後重新命名或移動一些檔案，找出問題的來源。

首先，試著重新命名 `settings.json`。這樣它就不會再載入上一個專案。

如果沒用，試著把一些最近的檔案移出它們各自的資源資料夾（`projects`、`matcaps`、`environments` 等）。

您也可以直接重新命名這些資料夾，讓 Nomad 完全忽略它們。
如果把 Nomad 資料夾中的所有檔案都重新命名或移走，效果就和全新安裝一樣。

::: tip
Nomad 在啟動時載入檔案，一律會先把檔案移到 `can_be_deleted/` 資料夾。
如果載入成功，就會把它移回原本的資料夾。

如果在載入完成前當機，Nomad 下次啟動時就能順利開啟，因為它會忽略 `can_be_deleted/` 資料夾。

如果您認為這個檔案這次可能載入成功，可以直接試著再載入一次。
:::
