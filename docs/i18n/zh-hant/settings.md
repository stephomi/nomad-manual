# ![](/icons/cog.webp) 設定 {#reset-to-default}

設定選單包含許多選項，用來控制 Nomad 的外觀與行為。

![](/images/settings_overview.webp)

## 顯示設定 {#display-settings}
此區塊包含本選單中大多數設定的快速啟動捷徑。

![](/images/settings_display_settings.webp)

### 平滑陰影 {#smooth-shading}
切換平滑與稜角陰影。當使用稜角陰影時，多邊形會各自獨立著色，因此可以看見底層拓樸結構。  
在雕刻階段使用稜角陰影有助於觀察結構，之後再切換回平滑陰影用於渲染。

停用平滑陰影可以略微提升效能。

### 外框 {#outline-quick}
切換目前選取物件的外框顯示。

當 [變暗未選取物件](#darken-unselected-objects) 被停用時，這有助於取得目前選取網格的視覺回饋。

從效能角度來看，使用 [變暗未選取物件](#darken-unselected-objects) 會比使用外框方式好得多。

### 格線 {#grid-quick}
切換背景網格顯示，有助於理解物件的位置與比例。

### 雙面 {#two-sided-quick}
切換多邊形雙面顯示。所有面都會朝向某個方向。  
被視為 *背面（backface）* 的，是那些「背向」攝影機視角的面。

例如啟動時的簡單球體，其面會朝向外側。  
若將攝影機移動到球體內部，就會看到這些面的背面。

大多數情況下你不應該看到面的背面，因此將其著色可以幫助你偵測潛在問題或錯誤的拓樸。

停用 `two sided` 繪製可以略微提升渲染效能。

### 線框 {#wireframe-quick}
切換線框覆蓋顯示。

請注意，啟用線框會降低效能。

### 對齊方塊 {#snap-cube-quick}
在場景角落顯示一個輔助圖示，有助於在空間中定位自己，並快速切換前/後/左/右/上/下視角。

### 顯示繪畫 {#show-painting}
切換塗裝顯示。預設使用的是白色、非金屬材質，粗糙度為 25%。

### 使用隱藏 {#use-hide}
切換隱藏模式。關閉時功能仍存在，只是被停用。若你目前正在使用隱藏工具，此按鈕會被停用。

### 顯示遮罩 {#show-mask}
切換遮罩模式。關閉時遮罩仍存在，只是被停用。再次按下此按鈕即可重新啟用。

若你需要「隱藏遮罩但仍保持其作用」，請使用下方的遮罩顏色並將其設為白色。完成後記得改回灰色！

請注意，若你目前正在使用遮罩工具，此按鈕會被停用。

### 遮罩 -> 不透明 {#mask-opaque}
Mask -> opaque 會在遮罩時忽略透明頂點。這只與頂點與貼圖透明度相關，被「隱藏（hide）」的面仍然會保持隱藏。

### 高亮 {#highlight-quick}
切換選取高亮閃爍效果。當選取物件時，會將被選物件以亮粉紅色短暫閃爍 500 毫秒。閃爍的顏色與時間長度可在下方自訂。

### 統計 {#stats-quick}
切換 3D 視窗中的狀態文字顯示。這會顯示系統記憶體、整個場景的總頂點數，以及目前選取物件的頂點數。

----- 

### 變暗未選取物件 {#darken-unselected-objects}
未被選取的物件會被變暗，以便讓目前選取的物件更突出。

### 遮罩 {#mask}
遮罩所使用的顏色，預設為中灰色，會與物件顏色相乘。將其設為白色可讓遮罩不可見，但完成後記得改回灰色！

## ![](/icons/cursor.webp) 游標 {#cursor}

### 雕刻時顯示圓圈 {#show-circle-while-sculpting}
在雕刻時持續顯示筆刷半徑。

### 顯示小點 {#show-small-dot}
在雕刻時，或當相機樞紐點改變時，在筆刷筆劃中心顯示一個小點。

### 顯示繩索穩定器 {#show-rope-stabilizer}
當筆劃設定中啟用 lazy rope 穩定器時，繪製一條線來表示繩索長度。

## ![](/icons/cursor.webp) 指示器 {#indicator}
![](/images/settings_indicator.webp)

為教學與螢幕錄製顯示視覺指示器。

`Finger`、`Stylus` 與 `Mouse` 按鈕會在偵測到該類輸入時顯示對應圖示。

### 顏色 {#indicator-color}
指示器的顏色。

### 大小/圖示/圓圈 {#indicator-shape}
用來調整指示器本身及其內部形狀的大小。

## ![](/icons/wireframe.webp) 線框 {#wireframe}
![](/images/settings_wireframe.webp)
啟用線框覆蓋顯示。

### 目標 {#target}
設定未選取物件是否顯示線框、只顯示選取物件，或是所有物件都顯示。

### 隱藏 {#hide}
設定被隱藏的多邊形是否仍顯示線框。

### 多重解析度：僅第 0 層 {#multiresolution-level-0-only}
多重解析度會將第 0 級的線框顯示得較深色，較高等級則會逐漸變淡。啟用此選項時，只會顯示第 0 級的線框。

### 顏色 {#wireframe-color}
設定線框的顏色與不透明度。

## ![](/icons/grid.webp) 格線 {#grid}
![](/images/settings_grid.webp)
啟用網格。

### 顏色 {#grid-color}
設定網格的顏色與不透明度。

### 吸附 {#snap}
啟用曲線類工具對網格的吸附。

## ![](/icons/culling.webp)雙面 {#two-sided}
啟用從兩側皆可看到多邊形面。

### 反面著色，反面顏色 {#backface-color}
啟用背面著色，以及背面著色的顏色。

## ![](/icons/outline.webp)外框 {#outline}
啟用在作用中物件周圍顯示外框。

### 外框顏色，粗細 {#outline-color-thickness}
設定外框的顏色與粗細。

## ![](/icons/bang.webp) 高亮 {#highlight}
啟用在作用中物件變更時的短暫閃爍效果。
### 顏色，持續時間 {#color-duration}
以毫秒為單位設定閃爍的顏色與持續時間。

## ![](/icons/snap_cube.webp) 對齊方塊 {#snap-cube}
![](/images/settings_snapcube.webp)

在場景角落顯示一個輔助圖示，可快速切換前/後/左/右/上/下視角。點擊方塊各面可切換正交視圖。

### 形狀 {#shape}
為對齊方塊選擇立方體、球體或指示軸（gnomon）形狀。

### 限制對齊 {#restrict-alignment}
啟用在拖曳對齊方塊時鎖定相機旋轉。啟用後，在對齊方塊上的拖曳動作只會左右或上下移動。

### 大小 {#size}
設定對齊方塊的大小。

### 翻轉 180 {#flip-180}
啟用點擊行為：當視角已對齊時，點擊方塊中心會將視角旋轉 180 度。  
例如視角已對齊到前視圖時，點擊方塊會旋轉到後視圖。

### 位置 {#snap-position}
設定對齊方塊所在的畫面角落。

## ![](/icons/edit_radius_n.webp) 統計 {#stats}
![](/images/settings_stats.webp)

顯示系統記憶體、整個場景的總頂點數，以及目前選取物件的頂點數。

### 位置 {#stats-position}
設定統計資訊顯示所在的畫面角落。

## 基元/重複器 {#primitive-repeaters}
## 數值輸入 {#gizmo-input}
允許在點擊操作軸（gizmo）元件時進行數值輸入。

## 多重解析度 {#multires}
### 最大頂點數 {#multires-lowres-count}
設定一個門檻值，避免多重解析度細分操作超過此多邊形數量，否則可能導致 Nomad 當機。預設為 1000 萬。

### 低解析度閾值 {#multires-lowres-threshold}
在移動攝影機時可以顯示較低解析度的網格。若希望顯示較高解析度的網格，可以提高此數值。

## 設定 {#advanced}
### 重設為預設值 {#reset}
將所有設定重設為預設值。