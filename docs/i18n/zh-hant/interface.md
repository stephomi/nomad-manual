# ![](/icons/interface.webp) 介面選單 {#interface-menu}

此選單控制許多用來自訂 Nomad 介面的選項。 

![](/images/interface_overview2.webp)

Nomad 可以被客製化到相當深入的程度，此選單分��� 4 個區塊：Interface、Gesture、Bindings、Debug。

![](/images/interface_menu.webp)


::: tip
本頁介紹的是「介面選單」，不是介面本身！整體介面說明請見 [Getting Started](gettingstarted.md)。
:::

## 介面 {#interface}

Interface 區段讓你新增快捷鍵、建立浮動工具列，並控制 Nomad 使用者介面的顏色、大小與外觀。

![](/images/interface_overview3.webp)

### 新增捷徑（底部）... {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

底部工具列預設啟用以下快捷鍵：
* `Undo` - 復原上一個操作
* `Redo` - 回復上一個被復原的操作
* `Solo` - 暫時隱藏所有其他物件，只顯示被選取的物件。再次按下可還原所有物件。
* `X-ray` - 暫時將所有其他物件變為半透明，只保留被選取物件為實心。再次按下可還原預設材質。
* `Voxel remesh` - 使用上次使用的 voxel 解析度重新網格化目前物件。長按或向上滑動會叫出解析度滑桿與銳利邊緣切換。
* `Grid` - 切換顯示視圖格線。長按或向上滑動可變更格線顏色與不透明度。
* `Wireframe` - 切換線框覆蓋顯示。長按或向上滑動可變更線框顏色與不透明度。
* `Inspector` - 讓你在 Nomad 背景上檢視網格的屬性，例如 UV、烘焙貼圖與其他屬性。
* `Face Group` - 切換面群組覆蓋顯示，更多資訊見 [Tools->FaceGroup](tools.md#facegroup) 

此選單中還有其他常用快捷鍵可用，更多功能可在 bindings 按鈕中找到。

#### ![](/icons/more.webp) 綁定 {#bindings-list}

幾乎 Nomad 的所有功能都可以透過 bindings 按鈕加入快捷工具列。按下按鈕後會顯示 bindings 選單：

![](/images/interface_bindings_search.webp)

你可以透過上方圖示依分類搜尋，或使用搜尋欄依名稱尋找功能。點擊一個功能即可將其加入工具列，再次點擊則移除。

#### ![](/icons/list.webp) 順序 {#order}

這會顯示快捷鍵清單。長按並拖曳即可重新排序快捷鍵。

#### ![](/icons/reset.webp) 重設 {#reset}

Reset 會將底部工具列還原為預設設定。

### 新增捷徑（視窗）... + {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

點擊 + 會新增一個浮動工具列。在你按下 bindings 按鈕並加入一些快捷鍵之前，它不會顯示，之後你就可以讓它顯示出來。 

你可以建立多個工具列，每個工具列在此選單中都有以下選項：

* ![](/icons/checked.webp) `Visible` - 切換工具列的可見性
* ![](/icons/more.webp)`Bindings` - 顯示綁定視窗以選擇要加入或移除的功能。
* ![](/icons/list.webp)`Order` - 顯示重新排序工具列的選單。
* ![](/icons/reset.webp) `Reset` - 將工具列重設為預設狀態。
* ![](/icons/resize_bottom_right.webp) `Resize corner` - 在工具列右下角切換顯示調整大小的控制點。
* ![](/icons/sort_down.webp) `Collapsable` - 在右上角切換顯示收合控制點。
* ![](/icons/trash.webp) `Delete` - 刪除該工具列。

### 工具箱 {#toolbox}

Nomad 介面右側工具選單的相關選項。

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) 介面調整角 {#ui-resize-corner}

在工具列底部角落切換顯示調整大小的控制點。

#### 隱藏 {#hidden}
一般來說，上方列中的 toolbox 圖示會在「單一長直欄」與「多欄工具清單」之間切換。啟用此選項後，則會在「多欄清單」與「隱藏」之間切換。

#### 彩色 {#colored}
依工具類別為圖示加上顏色，例如所有遮罩工具為棕色、分割工具為紅色、平整工具為綠色等。

#### 列數：自動（>1） {#rows-auto-1}

#### 重設順序 {#reset-order}
將 toolbox 中的預設工具順序重設為預設值。自訂圖示會保留在清單末端。

### 預設樣式 {#presets}

![](/images/interface_presets.webp)

介面配色預設組合的集合。

#### 高對比按鈕 {#high-contrast-button}
按鈕的替代樣式，使啟用狀態更明顯。如果設為 Auto，當 UI 啟用/停用顏色對比度較低時，Nomad 會自動使用此模式。

#### 色彩元件／基礎色 {#color-widgetcolor-base}
介面中使用的主要顏色。

#### 透明面板、色彩面板、模糊強度 {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
啟用後，會出現額外選項來控制 Nomad 中選單與面板的外觀。可以調整它們的顏色、透明度與模糊強度。

::: tip
在小型裝置上，將色彩面板設為接近白色、透明且低模糊強度會很有幫助，如此一來選單就不會遮住場景。
:::

----

### 鏡像頂部列 {#mirror-top-bar}
反轉頂部選單列中選單的順序。

### 鏡像側邊列 {#mirror-side-bars}
交換側邊欄位置，使 toolbox 在左側、工具選項在右側。

### 鏡像底部列 {#mirror-bottom-bar}
將底部列移到右下角，並反轉按鈕順序。

### 材質顏色預覽 {#material-color-preview}
當你為材質選擇顏色時，會在目前選取的物件上顯示該材質的預覽。

----
### 游標懸停顯示說明視窗 {#help-popup-on-hover}

對於支援懸停的裝置，啟用後 Nomad 中以 ![](/icons/help.webp) 圖示表示的說明會在懸停時顯示，否則只會在點擊時顯示。

----

### 整體縮放 {#overall-scale}
所有 UI 元件的尺寸倍率。
### 面板寬度 {#panel-width}
選單與面板的寬度。
### 字體縮放 {#font-scale}
字型縮放比例。
### 垂直間距 {#vertical-spacing}
選單與面板中元素之間的垂直間距。
### 垂直間距（左側） {#vertical-spacing-left}
左側工具列中元素之間的垂直間距。

----

### 邊緣偏移 {#edge-offset}
只有在你在螢幕邊緣與按鈕互動有問題時才應調整這些數值。若這些滑桿為停用狀態，Nomad 會使用裝置本身回報的安全區域數值。

::: tip
當將 Nomad 移轉到新裝置（例如將 iPhone 12 換成 iPhone 15）時，請務必將 edge 選項重設為預設值！
:::

### 重設樣式 {#reset-style}
將所有 UI 元件重設為預設值。


## 手勢 {#gesture}
Gesture 選單控制手寫筆與手指點按如何操作 Nomad。

![](/images/interface_gesture.webp)

### 手勢選項 {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad 可以依輸入裝置限制操作。例如手指拖曳只能移動相機，而手寫筆拖曳只能雕刻。如果你有滑鼠或觸控板，也可以指定用來控制特定操作。

Nomad 目前允許你針對手指、手寫筆或滑鼠手勢的任意組合設定以下模式：

* Camera
* Sculpt
* Gizmo
* Material picking（透過長按）
* Select object


`Finger always smooths` - 可以設定平滑只在手指拖曳時生效。

### ![](/icons/tool_mask.webp) 遮罩 {#mask}

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - 啟用後，以下單點快捷手勢可在不需按住 Mask 按鈕的情況下使用。會啟用以下手勢：
* 點擊背景以反轉遮罩
* 點擊已遮罩區域以模糊遮罩
* 點擊未遮罩區域以銳化遮罩

### 切換 遮罩 <-> 選取遮罩 {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - 長按會在 Mask 與 SelMask 之間切換並開始新的筆劃。在筆劃結束時會重新選取先前的工具。 
* `Tool` - 長按並在不移動的情況下放開，以在 Mask 與 SelMask 之間切換。 

### ![](/icons/tool_hide.webp) 隱藏 {#hide}
![](/images/interface_gesture_hide.webp)

啟用 `One tap shortcuts` 後，使用 Hide 工具時可使用以下快捷手勢：
* 點擊一個面群組以將其隱藏
* 點擊空白區域以反轉隱藏的多邊形

### ![](/icons/finger3.webp) 三指 {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

如果你的裝置支援三指手勢，可在此設定該手勢的快捷功能。 

選項矩陣允許你將垂直與水平拖曳定義為不同的快捷功能。注意如果同一手勢被選給兩個選項，其中一個會被停用。

* `Rotate lighting` - 旋轉環境、燈光與 Matcap。
* `Tool Radius` - 調整工具半徑。
* `Tool Intensity` - 調整工具強度。 

### ![](/icons/fingerprint.webp) 歷史 2/3 {#history-23}
`History shortcuts` - 啟用後，以下手勢會生效：
* Undo - 兩指點擊
* Redo - 三指點擊

`Long press` - 啟用後，按住 2/3 指會快速連續執行復原/重做。

### 無障礙 {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Assistive window` 會顯示一個浮動工具列，用來控制拖曳、縮放、旋轉與相機操作。

### 相機 {#camera}
前往 `Camera` 選單的捷徑（相機選項原本在此處，後來移到 Camera 選單）。

### Apple Pencil 雙擊 -> 綁定 {#pencil-tap}

前往 `Bindings` 選單的捷徑（Pencil 單擊與雙擊選項原本在此處，現已移至 bindings 選單）。


## 按鍵綁定 {#bindings}
鍵盤與按鈕快捷鍵可以在 bindings 選單中定義：

![](/images/interface_bindings.webp)
若你的裝置有鍵盤，Nomad 中幾乎所有功能都可以綁定到鍵盤快捷鍵，也可以綁定到手寫筆上的額外按鈕，甚至是遊戲控制器。

要建立綁定，點擊功能旁的矩形，然後按下按鍵/按鈕。 

可透過上方分類圖示尋找功能，或使用搜尋列依名稱搜尋。 

可透過綁定名稱旁的核取方塊停用個別綁定。

### ![](/icons/more.webp) 內容選單 {#context-menu}
每個綁定後方的 ![](/icons/more.webp) 圖示會叫出內容選單：

![](/images/interface_bindings_context.webp)

* `Clone` - 複製該綁定
* `Reset` - 重設該綁定
* `Delete` - 刪除該綁定
* `Toggle shortcut on key tap` - 設定點按與長按是否視為不同操作。啟用後，點按會啟用該工具；長按則只在按鍵按住期間啟用該工具，放開後會回到前一個工具。在其他 3D 應用程式中有時稱為「sticky keys」。

### 進階 {#advanced}
Bindings 選單底部有一個齒輪選單提供進階選項：

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - 對於 mask、smooth、gizmo、hide、sub 等標準快捷鍵，點按會切換到該模式，但按住按鍵則會暫時切換到該模式，放開後會回到前一個模式。在其他 3D 應用程式中有時稱為「sticky keys」。
* `Toggle tool shortcuts` - 使用工具快捷鍵時，如果同一快捷鍵按兩次，會切換回前一個工具。如此一來你可以用同一熱鍵在兩個工具之間來回切換。
* `Invert Y (Zooming)` - 反轉縮放方向
* `Reset bindings` - 將所有綁定重設為預設值。


## iOS ⌘ 鍵盤快捷鍵顯示 {#ios-keyboard-shortcuts-display}

在有鍵盤的 iOS 裝置上，按住 ⌘（cmd）鍵會顯示快捷鍵清單。

Android 的鍵盤支援仍有些實驗性質。

![](/images/shortcuts.webp)


## 除錯 {#debug}
一些實驗性與除錯選項位於此選單。多數選項應維持預設值，僅在聯絡 Nomad 支援後再行調整。

![](/images/interface_debug.webp)
### UV {#uv}
* `Normalize Uvs` - Nomad 會將 UV 正規化到 [0-1] 貼圖格內。

### 四邊重拓撲 {#quad-remesh}
* `Instant Mesh` - 啟用 instant remesh 演算法
* `Quadriflow` - 另一種四邊形重新網格化方法。

### 繪製 {#render}
* `Heightmap` - 將檢視埠改為渲染場景深度。可用來建立筆刷用的 alpha 貼圖。
* `Refraction write depth (back)` - 具折射材質網格的背面會被寫入深度緩衝。
* `Flip Y (normal map)` - 在烘焙法線貼圖時反轉 y 通道，某些遊戲與算圖引擎需要此設定。
* `Angle weighted smooth normals` - 對平滑陰影計算方式的調整，可在某些情況下避免產生摺痕。

### 目標 FPS {#target-fps}
停用時，Nomad 會將每秒幀數與螢幕更新率同步。

啟用時，你可以設定 Nomad 要渲染的每秒幀數。

### 介面 {#debug-interface}
* `Top: layout` 
  * Collapse: 在小型裝置上，頂部列會收合成更多子選單。 
  * Scroll: 若你習慣在大螢幕上使用 Nomad 並偏好一般版面，啟用此選項會使用標準寬版頂部列，並可捲動。
  * Multiline: 將整個頂部選單顯示為多行。
* `Bottom: draggable popup` - 底部工具列有數個按鈕會跳出對話框。啟用此選項後，這些對話框可以被拖曳到螢幕其他位置。  
* `Toolbox: show all` - Nomad 會隱藏與目前選取物件無關的工具，例如在尚未驗證的基本體上會隱藏所有雕刻筆刷。啟用此選項後，這些工具會以停用狀態顯示，而不是被隱藏。
* `Toolbox: colored` - 依工具類型為 toolbox 圖示加上顏色。
* `Panel: Drop shadows` - 在選單與面板周圍繪製陰影。在某些舊裝置上可能影響效能。
* `Panel: Blending` - 除錯選項
* `Pointer: hovering dot` - 對於支援手寫筆懸停的裝置，在手寫筆懸停於選單與面板上時顯示一個小點。

### Gif 轉盤動畫 {#gif-turntable}
Nomad 可以匯出動畫 gif 轉盤。由於 gif 格式限制，品質較低，通常使用螢幕錄影會是更好的方法。

* `Duration` - 轉盤動畫的秒數長度
* `Rotation center` - 相機旋轉樞紐位置，也就是相機繞著場景哪個部分旋轉
* `Transparent background` - 對 gif 使用透明背景選項。注意 gif 只支援 1 bit 透明度，因此邊緣可能會有嚴重鋸齒。
* `Max frame sampling` - Nomad 的許多高品質渲染效果是透過合成多個影格達成。此滑桿設定要合成多少影格。
* `Export (GIF)` - 開始 gif 匯出流程。

### 後處理 {#post-process}
* `Filtering` - 除錯選項
* `Format` - 除錯選項
* `Buffer reuse` - 除錯選項

### 效能 {#performance}
* `Multicore general` - 除錯選項
* `Multicore sculpting` - 除錯選項
* `Partial Drawing` - 實驗性功能！當你只在高面數網格的一小部分進行雕刻時可使用。應能讓雕刻更順暢，但請勿啟用線框！此外在筆刷筆劃期間可能會產生視覺偽影。

### 功能 {#feature}
* `Flip quad split (on tap)` -  除錯選項
* `Join: merge radius` - 當網格合併時，如果頂點彼此足夠接近會自動焊接。你可以用此滑桿調整半徑。

### 除錯 {#dev}
* `Logs` - 跳出日誌檢視視窗
* `App review popup` - 除錯選項
* `FPS` - 在檢視埠統計資訊中加入每秒幀數計數器。