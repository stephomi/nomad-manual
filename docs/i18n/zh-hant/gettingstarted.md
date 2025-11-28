# 入門指南 {#getting-started}

## 歡迎使用 Nomad！ {#welcome-to-nomad}

Nomad 是一款 3D 雕刻應用程式，可在多種裝置上運作，並在搭配具壓力感應的觸控筆之平板��腦上表現最佳，例如搭配 Apple Pencil 的 iPad，或搭配觸控筆的 Samsung Galaxy Tab。

它的靈感來自桌面雕刻軟體，如 ZBrush 和 Blender，重點在於提供容易理解的介面，同時不犧牲功能。如果你曾使用過 3D 雕刻軟體，Nomad 會讓你感到非常熟悉。

如果這是你第一次進行 3D 雕刻，先了解一些基礎概念會很有幫助。

::: tip 比較喜歡影片？
YouTube 上現在有非常多入門教學影片，以下是幾個很棒的連結：

* [Nomad Sculpt Crash Course by Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Nomad Sculpt Beginner tutorial by Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [NOMAD FOR BEGINNERS series by SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

很值得去看看這些創作者的主頻道，他們經常發布新的教學。
:::

## 你的第一個雕刻作品 {#your-first-sculpt}

第一次啟動 Nomad 時，你會在畫面上看到一個球體。只要用觸控筆在球體上拖曳，就能開始雕刻。為了讓雕刻更容易，預設會啟用對稱功能。

![](/videos/gettingstarted_01.mp4)

要讓筆刷變大或變小，使用左側的半徑滑桿。

![](/videos/gettingstarted_02.mp4)

要讓筆刷變強或變弱，使用左側的強度滑桿。

![](/videos/gettingstarted_03.mp4)

預設工具是 `Clay tool`，會在表面上「堆加」材質。若要從表面「減去」材質，點選左側的 `Sub` 按鈕。若要再改回堆加，請再次點選 Sub 按鈕。

![](/videos/gettingstarted_04.mp4)

若要平滑表面，點選 `Smooth` 按鈕。若要回到一般雕刻模式，再次點選 Smooth 按鈕。

![](/videos/gettingstarted_05.mp4)

若要繞著模型旋轉視角，在模型外的空白區域拖曳。

![](/videos/gettingstarted_06.mp4)

若要縮放，使用兩指縮放／捏合手勢。

![](/videos/gettingstarted_07.mp4)

若要平移相機，在螢幕上按住兩指並拖曳。

![](/videos/gettingstarted_08.mp4)

如果操作失誤，兩指輕點即可復原，或使用左下角的復原按鈕。

![](/videos/gettingstarted_09.mp4)

::: tip 桌面版
在桌面版中，alt/opt 鍵用來控制相機：

* tip 在空白處拖曳 = 旋轉相機
* alt+tip 拖曳 = 平移
* alt+tip 拖曳，然後放開 alt = 縮放（與 ZBrush 相同）

若使用具有兩個或以上按鍵的 Wacom 手寫筆，可在 Wacom 設定中將筆尖與按鍵設定如下：

* tip = 左鍵點擊
* 下方搖桿鍵 = 中鍵點擊
* 上方搖桿鍵 = 右鍵點擊

使用這些設定後，你可以只用手寫筆就操作相機：

* 上方搖桿鍵 + 懸停移動 = 旋轉相機
* 下方搖桿鍵 + 懸停移動 = 平移
:::

## 新增顏色 {#add-color}

Nomad 允許你在雕刻表面上進行繪畫。在右側工具選單中找到 `Paint` 工具並點選。左側工具列會出現一個彩色球體。點選它會打開顏色選擇器。選擇一個顏色，然後在模型上繪畫。

![](/videos/gettingstarted_10.mp4)

若要擦除，點選左側工具列上的 `Erase` 按鈕，然後在表面上擦除。再次點選 Erase 按鈕即可回到繪畫模式。

![](/videos/gettingstarted_11.mp4)

使用 clay 筆刷的加／減模式、平滑與繪畫，試著做出一個簡單的卡通頭：

![](/images/gettingstarted_head1.webp)

## 其他工具 {#other-tools}

工具面板中有許多有助於雕刻的工具。到目前為止，你已經使用了 clay 筆刷（預設啟動工具）、平滑與繪畫。由於平滑非常常用，它在左側工具列中有額外的快捷鍵。

Nomad 中的工具可以做各式各樣的事，從與雕刻相關的工具，如移動（move）、摺痕（crease）、膨脹（inflate），到像分割（split）與修剪（trim）這類更像木工或金工的工具。[Tools](tools.md) 頁面有更多資訊。

試著使用 move、crease、inflate 和 smooth 工具，為你的頭部增加更多細節、改變形狀：

![](/images/gettingstarted_head2.webp)

現在你已經了解 Nomad 的基本操作，接下來看看其餘的介面。

## 介面 {#interface}

![](/images/interface_overview1.webp)

* `Top menus` - 用來存取大部分 Nomad 功能的選單。左上方選單主要涵蓋場景與物件相關功能，右上方選單則與工具相關。在較小的螢幕上，這些選單會合併以節省空間。
* `Stats` - 顯示場景資訊、目前物件、遮罩狀態與記憶體使用量。
* `Nav Cube` - 協助顯示你正從哪一側觀看雕刻，同時也是快速切換視角的捷徑。點選立方體會將視角跳到被點選的那一面。拖曳立方體會旋轉視角。點選立方體旁的小圖示可框選目前物件，或重設到預設主視角。
* `Toolbox` - Nomad 的工具可在此可捲動區域中取得。
* `Left toolbar` - 大多數工具的半徑與強度滑桿、其他工具的情境按鈕，以及對稱、工具 alt/sub 模式、遮罩、平滑、gizmo 與繪畫選項的快捷鍵。
* `Bottom toolbar` - 常用功能的快捷鍵，於下方說明。

::: tip 左撇子？
你可以鏡像所有工具列的位置與順序，請參考 [Mirror top bar](interface.md#mirror-top-bar) 以及其他相關選項。
:::

## 底部工具列 {#bottom-toolbar}

![](/images/interface_bottom_toolbar.webp)

* `Undo` - 還原上一個操作
* `Redo` - 回復上一個復原操作
* `History` - 存取歷史紀錄選項，詳見 [History](history.md) 選單。
* `Solo` - 切換只顯示目前物件或顯示所有物件
* `X-Ray` - 讓其他所有物件以 X 光模式顯示，而目前物件維持實體顯示。長按或向上滑動可設定 X 光模式的顏色與不透明度。
* `Voxel` - [Voxel Remesher](topology.md#voxel-remesher) 體素重拓樸按鈕的快捷鍵。長按或向上滑動可顯示設定體素重拓樸品質的快捷選項。
* `Grid` - 切換顯示網格。長按或向上滑動可顯示網格相關選項。
* `Wire` - 切換線框覆蓋顯示。長按或向上滑動可顯示線框相關選項。
* `Inspect` - 切換檢視目前網格的額外資料。預設會顯示 UV，但長按或向上滑動可讓你檢視其他（若存在的）屬性，並選擇顯示在背景或網格上。

## 下一步 {#next-steps}

接下來要學什麼取決於你，以及你對什麼有興趣！以下是一些建議：

想更了解雕刻工具？前往 [Tools](tools.md) 章節。

想匯出你的模型？或匯入模型來進行雕刻？或為你的雕刻建立圖片？前往 [Files](files.md) 章節。

想更了解如何控制雕刻的細節？前往 [Topology](topology.md) 章節，學習多重解析度（multires）與簡化（decimation）。

想要使用更多物件？將簡單物件與基本形狀組合成更大的場景？前往 [Scene](scene.md) 章節。

想要了解 Nomad 的「所有一切」嗎？不錯的選擇！本手冊涵蓋 Nomad 的全部內容，包含許多技巧與提示，並在頂部提供強大的搜尋功能。使用左側的導覽來進一步學習。

如果你偏好影片，Holger Schönischka 在 YouTube 上製作了大量 Nomad 的技巧與教學影片：https://www.youtube.com/@ProcreateFX/videos


## 取得協助 {#getting-help}

如果在閱讀手冊與觀看教學影片後仍有疑問，有三種主要方式可以與其他 Nomad 使用者或 Nomad 開發者交流：

* 造訪論壇：[forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* 加入 Nomad 的 Discord 聊天：[https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* 直接聯絡開發者：support@nomadsculpt.com