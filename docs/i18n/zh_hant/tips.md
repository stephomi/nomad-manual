# ![](/icons/manual.webp) 提示

[[toc]]

## 如何開始建立模型

3D 雕刻的初學者常會問，開始一個模型的最佳方式是什麼。並沒有唯一的最佳方式，不同的人有不同的偏好。以下是幾種較常見的做法。

### 在球體上雕刻，使用 Multires

Nomad 啟動時的預設模型就是最常見的方式。使用 Move、Clay、Crease 工具推拉球體塑形；當你想快速做大改動時，用較低的細分等級；做細節時則使用較高的細分等級。

常見的問題是：你常會在需要多邊形的地方不夠用，而在其他地方又太多。比如說，如果你把預設球體拉成一個全身，通常會發現手指不夠細節，但頭後面卻浪費了很多多邊形。不過對於像頭這種大致呈球形的物體，這種方式是可以的。

### Dyntopo

啟用 Dyntopo 後，系統會在你雕刻時自動適應性地新增與刪除多邊形。這些多邊形會是三角形，初學者常會不喜歡這種相較於 Multires「乾淨」外觀而言較為雜亂的拓樸。值得多試一試！如果你開啟 Smooth Shading、關閉 Wireframe，並停止在意拓樸的外觀，這個模式可以帶來非常接近黏土的手感。別忘了，如果你使用大筆刷或 Smooth 筆刷，這個模式也會刪除多邊形，因此工具總是感覺快速且靈敏。一旦你完成第一輪雕刻，可以複製一份，丟進 Quad Remesher 取得漂亮的拓樸，再把原本的細節重投影到高細分等級上。

### Voxel Remesh

Voxel Remesh 會在你的雕刻上套用以四邊形為主的拓樸。這個操作在較低解析度時很快，可用來迅速把被拉伸過頭或過度密集的多邊形，替換成均勻分布的拓樸。這是從球體開始做全身的一個好方法；例如你先做出頭部，拉出脖子後做一次 Voxel Remesh；再拉出身體，Voxel Remesh；拉出手臂，Voxel Remesh，如此反覆，直到你得到基本形體。

### 使用多個物件

許多解剖學教學會用簡單的球體、圓柱、立方體來表示身體。你也可以在 Nomad 中用這種方式雕刻。這樣做的好處是可以在場景階層中把物件做父子關係，例如旋轉脖子時，頭會跟著動。能夠使用 Gizmo 工具做精準的平移／旋轉／縮放也非常實用，而且你可以為每個形狀設定 Pivot，讓它們依照預期方式移動。當基本方塊都放在正確位置後，你可以全選並做 Voxel Remesh 或布林運算，把它們合併成單一表面以進行更細緻的雕刻。

這種工作方式的一個小技巧是：從一個球體開始，把它縮放成拉長的香腸狀，按 Pivot，點擊「Bottom」，再按一次 Pivot。現在你有了一個身體部位，可以複製它，沿著第一個球體的長度平移、再複製、旋轉、再複製、滑動、再複製……等，很快就能排出一個身體。

### Tubes

Tube 工具是開始雕刻的好方法。爬蟲類尾巴、手臂、腿、手指、眉毛，都可以用 Tube 工具快速勾勒，之後也很容易編輯。它還允許你修改橫截面輪廓，讓你能快速改變形狀。你可以 Validate 這個形狀開始在上面雕刻，並與其他物件一起做 Voxel Remesh，得到完整的身體網格。

### 使用其他應用程式

有些人喜歡在其他應用程式中開始建立模型，這也完全沒問題。像 Blender 或 Valence 這類工具可以用 Low Poly 技法開始建模，之後再匯入 Nomad 進行雕刻。

### 使用內建預設

從 Project 選單右上角點擊 `Preset...`。這裡可以找到多個來自 Blender Foundation 的頭部與身體預設形狀。選擇一個你喜歡的，再點一次，把它加入場景。

### 使用線上模型

線上有許多免費模型，例如 polyhaven、sketchfab、turbosquid。通常這些模型可以匯入 Nomad，直接在上面雕刻，或當作參考使用。

### 沒有規則！

最終你可以任意組合這些技巧，或完全不用！Nomad 在這方面非常彈性，進階使用者可能會先用 Tubes 起形，再用 Dyntopo，接著與下載來的腳部模型結合，然後整體做 Quad Remesh，最後用 Multires 做最終細節。只要對你有用，就是好方法。

## Facegroups

Facegroup 工具可以用在許多地方，下列 YouTube 影片有詳細說明：https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

這裡是影片中功能的文字摘要。

### 為什麼要用 Facegroups？

Facegroups 讓你可以整理與選取面（本手冊中「faces」與「polygons」可互換使用）。相較於 Nomad 其他選取與組織工具，這比較容易解釋。Nomad 讓你建立物件、命名、做父子關係，很容易用一組物件來定義一個房間：地板、牆壁、椅子、桌子等等。

對角色來說，你可能一開始用頭、手臂、腿等分開的物件做 Block-out，但一旦你把所有部件合併成單一網格，這個結構就消失了。你可以用 Mask 來處理角色的局部，但一直重複為手、鼻子、再為手上 Mask 會變得很累人。

這就是 Facegroups 派上用場的地方。它讓你用顏色標記多邊形面，之後就能選取並操作同色的多邊形。注意：Facegroup 顏色與 Vertex Color 是不同的東西。

最接近的比喻是：在地圖上塗上不同顏色，之後可以依顏色選取國家或區域。

對角色頭部來說，你可以塗出眼窩、鼻子、嘴唇、下巴、耳朵等區域，之後就能輕鬆選取這些區塊。對硬表面與機械雕刻來說，定義面板與分區也很有用。

### 建立與編輯 Facegroups

Facegroups 可以用筆刷套用，每一筆新的筆劃會建立一個新的 Facegroup；也可以選取游標下的 Facegroup 並延伸它。也可以用幾何形狀來建立。

* Dot，Auto-pick 啟用時——單次拖曳會定義一個新的 Facegroup 顏色，並指派給你拖過的面。每次新的拖曳都會定義一個新的 Facegroup。輕點一下會做 Flood Fill，建立新的 Facegroup。
* Dot，Auto-pick 關閉時——當 Auto-pick 按鈕處於「sub」模式時，Nomad 會選取游標下的 Facegroup，並在之後的拖曳中套用它。這對於在不手動切換 Facegroup 的情況下，細修 Facegroups 很有用。

### Masking

當 Mask 工具啟用，且工具列上的 Facegroup 按鈕啟用時，輕點一個 Facegroup 會將其加上 Mask。

### Hiding

當 Hide 工具啟用，且工具列上的 Facegroup 按鈕啟用時，輕點一個 Facegroup 會將其隱藏。

### 組織管理

如前所述，Facegroups 可以用來整理你的網格，而不需要拆成多個物件。你可能不想把頭拆成鼻子、下巴、耳朵等獨立物件，但用 Facegroups 定義它們會非常實用。

### UV 區域

UV Atlas 工具會嘗試自動定義接縫，但有時會把接縫放在你不想要的位置。如果物件上已經有 Facegroups，且在 UV Atlas 選項中啟用了 Facegroup 選項，它就會改用 Facegroup 邊界作為 UV 接縫。

### Quad Remesher

Quad Remesher 外掛通常會在你的模型上產生流暢的邊流向，但當啟用 Facegroup 選項時，你可以用 Facegroups 來引導它。這讓你很容易定義乾淨的邊流，例如繞著眼睛、眉骨、嘴唇、臉頰折線等。

### 與其他工具搭配過濾

許多工具都有 Facegroup 感知選項，可能在主要工具選單中，或在 Stroke -> Filtering 選單中。例如 Smooth 工具在強度超過 100% 時，可以在 Facegroup 內部強力抹平細節，但相對保留 Facegroup 邊界。

### 放鬆與平滑 Facegroup 邊界

Facegroup 工具中的 Relax 選項能在保留其他特徵的情況下，出色地平滑 Facegroup 邊界。這是 Quad Remesh 前定義平滑 Facegroup 邊界區域的好方法。

## 平板／手機的限制

現今的平板與手機非常強大，但與桌上型電腦與筆電相比仍有重要差異：

### 沒有主動散熱

電腦有風扇與／或大型散熱片來保持冷卻，並設計成可在高溫下長時間運作。行動裝置的硬體通常優先追求輕薄，而不是幫助內部散熱。如果 Nomad 被推到最高品質設定（PBR 照明模式、複雜材質、許多物件、啟用許多後製選項），這既會讓裝置過熱，也會非常快速地耗電。

較好的做法是使用 Matcap 照明模式，並使用較低的 Render Multiplier（在 Post Process 選單頂部）。這些選擇會讓裝置保持涼爽，讓你能雕刻更久。

### 記憶體有限

Nomad 可以達到與多數桌面雕刻軟體相同的成果，但它無法違反物理定律！大多數桌上型電腦的記憶體是行動裝置的兩倍，為 3D 動畫打造的工作站往往有 4 倍或 8 倍的記憶體。因此，留意你使用了多少多邊形是很重要的；在你的裝置上做些測試，看看什麼時候開始變卡。幾乎所有能跑 Nomad 的裝置都能輕鬆處理 100 萬多邊形。M2 iPad Pro 可以舒適地處理 800 萬，使用者也在最新 iPad 上測試過遠高於這個數字。

話雖如此，只有最細緻的雕刻才需要超過 400 萬多邊形；如果你做的是相對簡單的物件，卻常常超過 50 萬、100 萬、400 萬，那就是你用太多多邊形了！請確認在選項中啟用了 Smooth Shaded 模式。

### 作業系統對高負載應用較不寬容

Apple 與 Android 預期應用程式會非常快速地儲存與載入小檔案，也假設應用程式可以非常快速地在前後景切換。Nomad 雖然用了不少技巧來保持檔案相對小且快速儲存，但如果行動作業系統認為 Nomad 花太久時間，它就會在任務完成前直接把它殺掉。這是另一個讓檔案保持較小的理由；有使用者在 Discord 回報曾處理 3700 萬多邊形的雕刻，但並不建議這麼做！

## 在小螢幕上工作

Nomad 是為平板設計的，但在手機上也能很好地運作。在手機這樣的小螢幕上雕刻，可以透過一些 UI 與流程調整來變得更輕鬆：

* 四指輕點會切換整個 UI，讓你有更多雕刻空間。
* 三指上下拖曳會改變筆刷半徑。
* 如果你視力好，可以把 UI 縮小以容納更多按鈕；如果視力不好，可以放大 UI。
* 寬版選單有時會擋住雕刻，你可以把它們設為透明且不模糊，讓你能看到選單下方的雕刻。
* 如果用手指雕刻，可以使用 Offset 選項，讓筆刷中心稍微偏離你的手指。
* 這些以及更多選項都可以在 [Interface menu](./interface.md) 中找到。

## Inflate 或 Peak 變形器

許多 3D 應用程式都有 Inflate 變形器，可以讓所有頂點沿著其法線方向推動一個可控制的距離。Nomad 目前雖然沒有變形器，但可以用 Inflate 筆刷模擬這種行為：

* 選擇 Inflate 筆刷
* 在 [Stroke menu](./stroke.md#stroke) 中把 Stroke Method 改成 `Lock + Radius`
* 把筆刷半徑調得比你的雕刻還大，如有需要可把相機拉遠。
* 在物件表面點擊並拖曳一筆；當半徑大於物件時，整個形狀會以固定量均勻膨脹。
* 調整筆刷強度來控制膨脹量
* 如有需要，可使用 Mask 來保護或減弱某些區域的 Inflate 效果。

## 移除 Voxel Remesh 產生的凸起或「粉刺」

Voxel Remesh 很適合產生均勻分布的多邊形，但有時會產生某種拓樸，使得在 Smooth 時出現小凸起或粉刺。例如：

* 在預設球體上用 Crease 筆刷畫一個漩渦
* 使用「Build Multiresolution at 3」做 Voxel Remesh
* 用高強度 Smooth
* 會出現瑕疵（用高對比 Matcap 材質更容易看見）：

![](/videos/tip_pimples_before.mp4)

要用雕刻方式修正，試試 Smooth 設定中的 `Stable smoothing` 選項。它可以處理 Voxel Remesh 不均勻的拓樸，得到乾淨的結果。

![](/videos/tip_pimples_stable_smooth.mp4)

若要修正拓樸本身，可以使用新的 Primitive、Quad Remesh 工具，或外部 3D 建模軟體，然後透過 `Topology -> Misc -> Reproject` 把原始網格的細節投影到新網格上。

![](/videos/tip_pimples_reproject.mp4)

## 日光打光

預設的 PBR Render 顧名思義是「物理為本」，就像未經處理的數位照片，看起來可能有點灰、平淡。Nomad 的燈光與後製可以讓渲染看起來更鮮明。

以下是預設渲染，我們來看看能不能讓它更好看：
![](/images/tips_lighting_default.webp)

啟用 Post Processing 與 Tonemapping 可以增加亮度與對比：

![](/images/tips_lighting_tonemap.webp)

接著專注在燈光上。預設的 Environment Light 很適合雕刻，但可以為最終渲染做些改進。一種思考方式是把直接光（例如太陽）與環境光（例如天空的藍光、地面的反光）分開來看。透過降低 Environment Light 並旋轉它，可以開始模擬主體位於陰影區時的光線樣貌：

![](/images/tips_lighting_env.webp)

再加入一盞 Direct Light，並提高其強度來模擬強烈日光。把它與 Environment Light 做平衡，可以得到令人愉悅的結果：

![](/images/tips_lighting_sunlight.webp)

角色可以透過把材質改成 Subsurface，並在角色後方放一盞 Spotlight 對準耳朵，讓耳朵發光而受益：

![](/images/tips_lighting_sss.webp)

接著就可以嘗試其他後製設定！Global Illumination 與 Ambient Occlusion 有助於更真實的打光。Curvature 與 Sharpen 可以幫助凸顯雕刻細節。Chromatic Aberration、Depth of Field、Grain、Bloom、Vignette 則用來模擬相機效果。注意，隨著功能啟用，燈光與其他後製數值也需要調整來做補償。

以下是套用完整後製調整後的渲染：
![](/images/tips_lighting_final.webp)
