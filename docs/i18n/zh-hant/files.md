# ![](/icons/open.webp) 檔案 {#files}

檔案選單可用來儲存與載入 Nomad 專案、匯入與匯出 3D 模型，以及匯出算圖影像。

![](/images/file_menu.webp)

## 專案 {#project}
![](/images/file_project.webp)

在此選單頂端會顯示上次儲存時的縮圖。點擊此縮圖會開啟一個迷你瀏覽器，在另一個專案上點兩下即可叫出迷你選單，用來開啟、加入、儲存、複製、重新命名或刪除該專案。

### ![](/icons/nomad.webp) 預設 {#preset}
存取一系列示範與角色元件。選取一個項目後，再次點選即可選擇「開啟」、「加入場景」或「複製」到你的專案資料夾中。

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) 儲存 {#save}
儲存 Nomad 專案。

### ![](/icons/save_as.webp) 另存新檔... {#save-as}
顯示專案瀏覽器，讓你以新名稱儲存 Nomad 專案。

### ![](/icons/pencil.webp) 重新命名 {#rename}
顯示文字框以重新命名目前專案。

### ![](/icons/open.webp) 開啟... {#open}
顯示專案瀏覽器以開啟專案。

### ![](/icons/add_file.webp) 加入至場景... {#add}
顯示專案瀏覽器，選取專案後，其內容會與目前場景合併。

### ![](/icons/trash.webp) 刪除... {#delete}
顯示專案瀏覽器，任何被選取的專案都會從檔案系統中刪除。

### ![](/icons/new_file.webp) 新建 {#new}
開始一個新專案，若有未儲存的變更，系統會詢問你是否要先儲存。

### ![](/icons/autosave.webp) 自動儲存... {#auto-save}
控制自動儲存選項的選單。

若啟用自動儲存，你可以設定一個計時器，讓提示視窗以固定間隔跳出。
Nomad 不在背景自動儲存的原因，是因為 3D 檔案可能相當龐大，在雕刻時會造成明顯的延遲。

另外，為了避免記憶體不足的問題，場景在儲存前通常會先被壓縮。
這個壓縮／解壓縮過程也會讓儲存動作變慢。

### 計時器彈出視窗 {#timer-pop-up}
設定計時器提示視窗出現的頻率。

### 彈出視窗逾時 {#popup-timeout}
啟用彈出視窗逾時。

### 捨棄自動儲存 {#discard-autosave}
若某個專案存在自動儲存檔，將會自動載入該檔案而不是原始專案。若不需要此行為，按下此按鈕會刪除自動儲存檔。之後載入時就會載入該專案最後一次手動儲存的版本。


## 匯入 {#import}

### ![](/icons/add_file.webp) 匯入 {#import-button}
用來匯入非 Nomad 專案的 3D 檔案。

當你將外部場景檔匯入 Nomad 時，可以選擇「匯入」或「加入」。

加入檔案只會將物件加入目前場景。
匯入檔案則會以新物件建立一個新的 Nomad 專案。

Nomad 可匯入以下格式：
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx，實驗性)

### ![](/icons/cog.webp) 進階 {#advanced}
顯示進階匯入選項：

### 專案 / glTF / OBJ / STL / FBX {#project-gltf-obj-stl-fbx}
#### 保留拓樸 {#keep-topology}
Nomad 預設在載入時會嘗試修正有問題的幾何。啟用此選項將阻止 Nomad 重新排序頂點／面、移除重複頂點／面、移除未使用頂點。

#### 略過貼圖 {#skip-textures}
對於支援貼圖的格式（如 glTF），略過貼圖載入。

### 專案 / glTF {#project-gltf}
#### 保留介面設定 {#keep-gui-settings}
啟用後會在 Nomad .nom 或 glTF 檔案中儲存 GUI 與專案設定。

### OBJ {#obj}
#### 依群組分割 OBJ {#split-obj-by-groups}
啟用後會將 OBJ 群組分割為獨立物件。

#### 色域 {#color-space}
將從 OBJ 解讀的色彩模式設定為 Linear、sRGB 或 Auto。

### PLY {#ply}
#### 色域 {#color-space-ply}
將從 PLY 解讀的色彩模式設定為 Linear、sRGB 或 Auto。


### FBX {#fbx}
#### 色域 {#color-space-fbx}
將從 OBJ 解讀的色彩模式設定為 Linear、sRGB 或 Auto。



## 匯出 {#export}
儲存為可在其他軟體中使用的 3D 幾何格式。 

![](/images/file_export.webp)

不同檔案格式支援的功能不同，可用選項會依選取的檔案類型而改變。

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertex Colors](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex PBR](#vertex-pbr)       | ✅     | Nomad ✅<br>Other ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Other ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Layers](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objects                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Face Group                      | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchy                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lights                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Textures                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | Import ✅<br>Export ❌ |
| Primitives, Postprocess, etc    | ✅     | Nomad ✅<br>Other ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### 全部 / 可見 / 已選取 {#allvisibleselected}
作用中的按鈕狀態會決定哪些物件會被匯出。圖示旁的數字表示在該選項下會匯出的物件數量。

### 頂點色 {#vertex-colors}
若檔案格式支援，則匯出頂點色。

### PBR 繪製 {#pbr-paint}
PBR 頂點色會以次要頂點色屬性的形式匯出。
通道的打包方式如下：

|           | Channel  |
| :-------: | :------: |
| Roughness | R        |
| Metalness | G        |
| Masking   | B        |


### 圖層 {#layers}
圖層透過 glTF 的 morph target 來支援。
Nomad 也會匯出每個圖層的顏色、粗糙度與金屬度，但其他軟體通常會忽略這些資訊。

### 圖層繪製 {#layer-painting}
匯出圖層繪製，其他軟體通常會忽略。

### 面群組 {#face-group}
匯出面群組，匯出後有時可能會與其他軟體產生衝突。

### 法線 {#normals}
匯出法線資訊。請注意，Nomad 在匯入其他檔案格式時，始終會自行計算法線。

### 切線 {#tangents}
匯出切線資訊，當模型有法線貼圖時會使用。

### 貼圖 {#textures}
若材質中已加入貼圖，則會一併匯出。請注意這不會進行貼圖烘焙；烘焙需透過拓樸中的烘焙選項完成。

### 匯出按鈕 {#export-button}
點擊此按鈕，以目前選定的設定匯出幾何。

::: tip Tip: 將粗糙度與金屬度匯入 Blender

Blender 可以匯入 glTF/glb，但不會自動辨識金屬度與粗糙度的頂點屬性。若要使用它們，在材質編輯器中建立一個 Vertex Color 節點，將其屬性設為下一個色彩屬性（通常是 Col.001）。接上「Separate XYZ」節點，將 X 接到 Roughness，Y 接到 Metallic。

此影片示範了整個流程：

![](/videos/blender_pbr.mp4)

::: 

::: tip Tip: USD 功能支援情況

USD 是一種複雜格式，其規格支援許多功能，但並非所有 3D 軟體都支援。例如 OSX/iOS 就不支援頂點色。USD 匯出器中的預設模式會嘗試在 OpenUSD、Apple、Procreate、ZBrush 之間取得最佳相容性推測。

::: 

## 繪製 {#render}

匯出一張影像，內容為專案中所有設定（燈光、材質、後製等）的組合結果。 

![](/images/file_render.webp)
### 預覽 {#preview}

選單標題旁的小預覽按鈕會使工具列變暗，以便預覽最終效果。

### 透明背景 {#transparent-background}
為算圖啟用 Alpha 通道，方便在 2D 軟體中與其他影像合成。請注意不支援部分透明。

### 顯示介面 {#show-interface}
啟用後會在算圖中包含 Nomad 的使用者介面。

### 繪製比例 {#render-ratio}
對影像解析度的倍數係數。

### 最終尺寸 {#final-size}
算圖所使用的解析度。當選擇 `Custom` 時，寬度與高度滑桿會被啟用。 

當檔案選單啟用時，若算圖區域與螢幕解析度不符，檢視視窗中會畫出虛線框來表示算圖區域（請注意必須在橫向模式下才會正確）。

### 匯出 png {#export-png}
點擊此按鈕開始算圖流程。完成後你可以選擇如何儲存或分享影像。