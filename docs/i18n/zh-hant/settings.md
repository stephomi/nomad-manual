# ![](/icons/cog.webp) 設定 {#reset-to-default}

設定選單包含許多控制 Nomad 外觀和行為的選項。

![](/images/settings_overview.webp)

選單上方的那排按鈕可以直接跳到某個區塊：`游標`、`指示器`、`線框`、`格線`、`雙面顯示`、`輪廓`、`反白`、`導航器`、`顯示場景狀態`、`控制柄`、`形狀`、`重複器` 和 `多解析度`。

## 顯示設定 {#display-settings}
這一區提供快速開關，對應這個選單下方大部分的設定。

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) 平滑著色 {#smooth-shading}
在平滑著色和多面著色之間切換。多面著色時，每個多邊形會各自著色，所以你能看出底下的拓樸。
在雕刻階段用多面著色，到算繪時再切換成平滑著色，會很有幫助。

停用平滑著色可以稍微提升效能。

### ![](/icons/outline.webp) 輪廓 {#outline-quick}
切換目前選取物件的輪廓。

當[使未選物件變暗](#darken-unselected-objects)停用時，這能讓你清楚看出目前選取了哪些網格。

從效能的角度來看，使用[使未選物件變暗](#darken-unselected-objects)比使用輪廓好得多。

### ![](/icons/grid.webp) 格線 {#grid-quick}
切換背景格線，有助於了解物件的位置和比例。

### ![](/icons/culling.webp) 雙面顯示 {#two-sided-quick}
切換多邊形的雙面顯示。每個面都朝向某個方向。
被視為*背面*的面，就是朝向「遠離」相機視點方向的面。

例如，啟動時的簡單球體，它的面都是朝外的。
如果把相機移到球體內部，你就會看到這些面的背面。

大多數時候你不應該看到面的背面，所以為背面上色可以幫你發現潛在的問題或錯誤的拓樸。

停用 `雙面顯示` 算繪可以稍微提升算繪效能。


### ![](/icons/wireframe.webp) 線框 {#wireframe-quick}
切換線框疊加顯示。

注意，啟用線框會降低效能。

### ![](/icons/navigator.webp) 導航器 {#snap-cube-quick}
切換場景角落的輔助圖示，有助於在空間中辨別方向，並快速在正面／背面／左側／右側／上方／下方視角之間切換。

### ![](/icons/palette.webp) 顯示繪畫 {#show-painting}
切換繪畫的顯示。關閉時，物件會以白色、非金屬、粗糙度 25% 的材質顯示，而不是它的繪畫。

### ![](/icons/tool_hide.webp) 使用隱藏 {#use-hide}
切換隱藏模式。關閉時隱藏的設定依然存在，只是暫時停用。如果你正在使用隱藏工具，這個按鈕會停用。

### ![](/icons/shield.webp) 顯示遮罩 {#show-mask}
切換遮罩模式。關閉時遮罩依然存在，只是暫時停用。再按一次這個按鈕即可重新啟用。

如果你想隱藏遮罩，「同時」又讓它保持作用，可以把下方的遮罩顏色設為白色。用完記得改回灰色！

注意，如果你正在使用遮罩工具，這個按鈕會停用。

### ![](/icons/shield.webp) 遮罩 → 不透明 {#mask-opaque}
`遮罩 → 不透明` 會在遮罩時忽略透明的頂點。這只和頂點及貼圖的不透明度有關，被「隱藏」的面仍然會保持隱藏。只有在 `顯示遮罩` 開啟時才能使用。

### ![](/icons/bang.webp) 反白 {#highlight-quick}
切換選取時的反白閃爍。選取物件時，被選取的物件會暫時閃爍 500 毫秒。閃爍的顏色和長度可以在下方自訂。

### ![](/icons/list.webp) 顯示場景狀態 {#stats-quick}
切換 3d 視窗中的狀態文字顯示。它會顯示系統記憶體、場景總頂點數，以及目前選取物件的頂點數等資訊。

----- 

### ![](/icons/cube.webp) 使未選物件變暗 {#darken-unselected-objects}
未選取的物件會變暗，讓目前選取的物件更突出。

### ![](/icons/shield.webp) 遮罩 {#mask}
遮罩使用的顏色，預設是中灰色，會和物件的顏色相乘。設為白色可以讓遮罩看不見，但用完記得改回灰色！

## ![](/icons/cursor.webp) 游標 {#cursor}

### 圓形 {#show-circle-while-sculpting}
何時顯示筆刷半徑的圓圈：

* `自動` - 顯示圓圈，但雕刻時隱藏。
* `否` - 永遠不顯示圓圈。
* `是` - 永遠顯示圓圈，雕刻時也一樣。

### 顯示指示點 {#show-small-dot}
雕刻時，或相機軸心改變時，在筆觸中心顯示一個小點。

### 顯示穩定線 {#show-rope-stabilizer}
在筆觸設定中啟用[拉繩穩定器](stroke.md#lazy-rope-stabilizer)時，畫出一條線來表示拉繩的長度。

### 顯示滾轉提示 {#show-roll-hint}
使用滾轉的按鍵綁定時，顯示滾轉方向的導引。

### ![](/icons/radius.webp) 尺寸 {#dot-size}
小點的大小。

### 顏色 {#cursor-colors}
游標會依你正在做的事情改變顏色：`雕刻`、`背景`（游標停在背景上時）、`遮罩`、`平滑`、`相機` 和 `半徑`。每種顏色都可以在這裡自訂。

## ![](/icons/cursor.webp) 指示器 {#indicator}
![](/images/settings_indicator.webp)

為教學影片和螢幕錄影顯示視覺指示器。設為 `是` 即可開啟（在 iOS 上還有 `自動` 選項）。

`手指`、`觸控筆` 和 `滑鼠` 按鈕會在偵測到該類型的輸入時顯示圖示。

### 顏色 {#indicator-color}
指示器的顏色。

### 尺寸／圖示／圓形 {#indicator-shape}
調整指示器大小，以及指示器內圖示和圓圈不透明度的控制項。

## ![](/icons/wireframe.webp) 線框 {#wireframe}
![](/images/settings_wireframe.webp)
啟用線框疊加顯示。

### 目標 {#target}
設定線框要顯示在未選取的物件、只顯示在選取的物件，還是所有物件上。

### 隱藏 {#hide}
設定被隱藏的多邊形是否仍然顯示線框。

### 多解析度：僅限層級 0 {#multiresolution-level-0-only}
多解析度會讓層級 0 的線框顯示得較深，越高的層級則逐漸變淺。啟用這個選項時，只會顯示層級 0 的線框。

### 顏色 {#wireframe-color}
設定線框的顏色和不透明度。

## ![](/icons/grid.webp) 格線 {#grid}
![](/images/settings_grid.webp)
啟用格線。

### 吸附 {#snap}
這些選項會讓以曲線和形狀為基礎的工具（`車削`、`圓管`、多邊形和路徑形狀…）在繪製時吸附點：

* `吸附到格線` - 吸附到格線上。
* `吸附到點（對齊視圖）` - 相機對齊某個軸時，吸附到附近既有的點。
* `吸附到點（自由視圖）` - 相機沒有對齊時，吸附到附近既有的點。

### 顏色 {#grid-color}
設定格線的顏色和不透明度。格線可見時才會顯示這些選項。

`暈影` 會讓格線往邊緣逐漸淡出。`吸附分割臨界值` 以像素為單位，設定格線在螢幕上可以多密，超過後就會切換到另一個細分層級。

## ![](/icons/culling.webp)雙面顯示 {#two-sided}
讓多邊形的面從兩側都能看見。

### 背面顏色 {#backface-color}
`背面著色` 會為背面染上顏色，`背面顏色` 則設定染色的顏色。

## ![](/icons/outline.webp)輪廓 {#outline}
在選取的物件周圍顯示輪廓。

### 輪廓顏色、厚度 {#outline-color-thickness}
設定輪廓的顏色和 `厚度`。


## ![](/icons/bang.webp) 反白 {#highlight}
選取變更時短暫閃爍一下。
### 顏色、持續時間 {#color-duration}
設定閃爍的顏色和時間長度（毫秒）。

## ![](/icons/navigator.webp) 導航器 {#snap-cube}
![](/images/settings_snapcube.webp)

在場景角落顯示輔助圖示，方便快速在正面／背面／左側／右側／上方／下方視角之間切換。點它的各面，就能在正交視角之間切換。

### 形狀 {#shape}
選擇導航器的形狀：球體、方塊或座標軸指示（gnomon）。

### 限制對齊 {#restrict-alignment}
讓吸附的視角對齊世界座標軸。啟用時，只能使用 6 個主要視角。設為 `自動` 時，只有在相機處於 `轉盤` 模式時才會套用這個限制。

### 尺寸 {#size}
設定導航器的大小。

### 翻轉180° {#flip-180}
啟用一種點選行為：當視角已吸附時，點導航器的中心會讓視角旋轉 180 度。例如視角吸附在正面時，點一下導航器就會轉到背面視角。

### 邊和角 {#edges-corners}
在邊和角上（琥珀色區域）加上吸附視角。座標軸指示形狀無法使用。

### 轉盤式拖曳 {#turntable-drag}
拖曳導航器時只旋轉而不滾轉相機，並會在每個吸附視角停住。停用後，拖曳導航器會改用 `軌跡球` 旋轉。不論哪一種，拖曳都會保持水平或垂直。相機為 `轉盤` 模式時，導航器總是以這種方式拖曳。

### 位置 {#snap-position}
設定導航器要放在哪個角落。


## ![](/icons/list.webp) 顯示場景狀態 {#stats}
![](/images/settings_stats.webp)

顯示系統記憶體、場景總頂點數，以及目前選取物件的頂點數等資訊。

### 位置 {#stats-position}
設定場景狀態要放在哪個角落。

## ![](/icons/edit_radius.webp) 控制柄 {#handle}
你在視窗中拖曳的控制柄（例如軸向變換）的相關設定。

### 數值輸入 {#gizmo-input}
點選軸向變換的某個控制項時，允許輸入數值。

### 自動隱藏 {#hide-on-interaction}
操作軸向變換時讓它淡出，以免擋住視線。

### ![](/icons/opacity.webp) 不透明度 {#handle-opacity}
控制柄的不透明度。

## ![](/icons/shape_lasso.webp) 形狀 {#shape-settings}
用形狀筆觸（套索、矩形、曲線…）畫出的形狀在螢幕上的樣子。

### ![](/icons/opacity.webp) 填色、輪廓 {#shape-fill-outline}
形狀內部和外圍線條的不透明度。

### 顏色 {#shape-colors}
各類工具的形狀顏色：`遮罩`、`隱藏`、`面群組` 和 `裁切`。

## ![](/icons/array.webp) 重複器 {#primitive-repeaters}
[重複器](scene#repeaters)（陣列、徑向、曲線、表面）所產生副本的上限。當重複器失控時，這些上限能讓 Nomad 保持流暢。

### ![](/icons/cube.webp) 最大副本數 {#repeater-max-copies}
單一重複器最多能產生的副本數。物件一多，不論大小，Nomad 都會變得吃力。

### ![](/icons/cube.webp) 場景副本數 {#repeater-scene-copies}
整個場景的副本預算。低面數的副本幾何量雖小，但仍是完整的物件，所以小副本通常最先碰到這個上限。

### ![](/icons/triangle.webp) 面數限量 {#repeater-max-faces}
場景中所有副本的面數預算。超過時，最重的物件會最先減少副本。

## ![](/icons/multires.webp) 多解析度 {#multires}
### 最大頂點數量 {#multires-lowres-count}
設定一個臨界值，不允許多解析度細分超過這個頂點數，否則很可能讓 Nomad 當機：Nomad 在細分前不會檢查可用的記憶體。預設值是 1000 萬。
### 最低解析度臨界值 {#multires-lowres-threshold}
移動相機時，可以顯示較低解析度的網格。如果你想顯示解析度更高的網格，可以調高這個數值。

## 設定 {#advanced}
### ![](/icons/reset.webp) 還原預設設定 {#reset}
把應用程式所有的偏好設定重設為預設值。

有些資源是另外儲存的，「不會」被重設：專案、按鍵綁定、工具預設、HDR 環境、材質捕捉、Alpha、筆刷貼圖和參考圖片。所有隨專案一起儲存的內容，例如燈光、後製或相機視角，也都會完整保留。
