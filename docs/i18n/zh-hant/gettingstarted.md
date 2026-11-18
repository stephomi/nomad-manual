# ![](/icons/play.webp) 新手入門 {#getting-started}

## 歡迎使用 Nomad！ {#welcome-to-nomad}

Nomad 是一款 3d 雕刻應用程式，可以在許多裝置上使用，搭配支援壓力感應的觸控筆的平板電腦效果最好，例如 Apple iPad 加 Apple Pencil，或是 Samsung Galaxy Tab 加觸控筆。

它的靈感來自 ZBrush 和 Blender 等桌面雕刻軟體，著重在簡單易懂的介面，同時不犧牲功能。如果你用過 3d 雕刻軟體，會覺得 Nomad 非常熟悉。

如果這是你第一次接觸 3d 雕刻，先了解一些基礎會很有幫助。

::: tip 比較喜歡看影片？
YouTube 上現在有「非常多」新手教學影片，以下是幾個很棒的連結：

* [Dave Reed 的 Nomad Sculpt 速成課程（Nomad Sculpt Crash Course）](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Small Robot Studio 的 Nomad Sculpt 新手教學](https://www.youtube.com/watch?v=J644wXoTiww)
* [SouthernGFX 的 NOMAD FOR BEGINNERS 系列](https://www.youtube.com/watch?v=bEh0WxRoOmg)

很值得去看看這些創作者的頻道，他們經常發布新的教學。
:::

## 你的第一件雕刻 {#your-first-sculpt}

第一次開啟 Nomad 時，你會在畫面上看到一顆球體。只要用觸控筆在球體上拖曳，就能開始雕刻。對稱預設是開啟的，讓雕刻更輕鬆。

![](/videos/gettingstarted_01.mp4)

要讓筆刷變大或變小，請使用左側的半徑滑桿。

![](/videos/gettingstarted_02.mp4)

要讓筆刷變強或變弱，請使用左側的強度滑桿。

![](/videos/gettingstarted_03.mp4)

預設工具是 `黏土` 工具，它會在表面上增加材料。要從表面減去材料，請點左側的 `反向` 按鈕。要再次增加材料，就再點一次反向按鈕。

![](/videos/gettingstarted_04.mp4)

要讓表面變平滑，請點 `平滑` 按鈕。要回到一般雕刻，就再點一次平滑按鈕。

![](/videos/gettingstarted_05.mp4)

要繞著模型旋轉，請在模型以外的空白處拖曳。

![](/videos/gettingstarted_06.mp4)

要縮放，請使用雙指縮放（捏合）手勢。

![](/videos/gettingstarted_07.mp4)

要平移相機，請用兩根手指按住螢幕並拖曳。

![](/videos/gettingstarted_08.mp4)

如果做錯了，用兩根手指點一下就能復原，或使用左下角的復原按鈕。

![](/videos/gettingstarted_09.mp4)

::: tip 桌面版
在桌面版上，用 Alt/Option 鍵來控制相機：

* 在空白處用筆尖拖曳 = 旋轉相機
* Alt + 筆尖拖曳 = 平移
* Alt + 筆尖拖曳，然後放開 Alt = 縮放（和 ZBrush 相同）

如果你的 Wacom 繪圖板的筆上有 2 個以上的按鈕，可以在 Wacom 設定中這樣設定筆尖和按鈕：

* 筆尖 = 左鍵
* 下側按鈕 = 中鍵
* 上側按鈕 = 右鍵

這樣設定後，就能只用筆來操作相機：

* 按住上側按鈕並懸空移動 = 旋轉相機
* 按住下側按鈕並懸空移動 = 平移
:::

## 加上顏色 {#add-color}

Nomad 可以讓你在雕刻的表面上繪畫。在右側的工具選單中找到 `繪畫` 工具並點選它。左側工具列會出現一顆彩色球體，點一下就會開啟顏色選擇器。選好顏色後，就能在模型上繪畫了。

![](/videos/gettingstarted_10.mp4)

要擦除顏色，請點左側工具列上的 `擦除` 按鈕，然後在表面上擦拭。再點一次擦除按鈕，就能回到繪畫模式。

![](/videos/gettingstarted_11.mp4)

試著用黏土筆刷的增加／反向模式、平滑和繪畫，做出一顆簡單的卡通頭像：

![](/images/gettingstarted_head1.webp)

## 其他工具 {#other-tools}

工具盤裡有許多協助雕刻的工具。到目前為止，你已經用過黏土筆刷（預設的起始工具）、平滑和繪畫。因為平滑很常用，所以左側工具列上還有它的額外捷徑。

Nomad 的工具能做的事情非常多，從移動、褶皺、膨脹這類雕刻工具，到分割、裁切這類更像木工或金工的工具都有。更多資訊請參考[工具](tools.md)頁面。

試試用移動、褶皺、膨脹和平滑工具，為你的頭像加上更多細節，或改變它的形狀：

![](/images/gettingstarted_head2.webp)

現在你已經了解 Nomad 的基礎，接著來看看介面的其他部分。

## 介面 {#interface}

![](/images/interface_overview1.webp)

* `頂端選單` - 用來使用 Nomad 大部分功能的選單。左上方的選單主要是場景和物件相關功能，右上方的選單則和工具有關。在較小的螢幕上，這些選單會收合在一起以節省空間。
* `場景狀態` - 關於場景、目前物件、遮罩狀態和記憶體使用量的資訊。
* `導航器` - 顯示你正從哪一側看雕刻作品的輔助工具，也是切換不同視角的捷徑。點某一面，視角就會跳到那一側；拖曳導航器則會旋轉視角。點它旁邊的小圖示，可以讓目前物件填滿畫面、重設為預設的初始視角、鎖定相機，或切換格線。它的外觀（方塊、球體或座標軸指示）和位置可以在[設定](settings.md#snap-cube)中修改。
* `工具箱` - 可以在這個可捲動的區域中找到 Nomad 的工具。
* `左側工具列` - 大多數工具的半徑和強度滑桿、其他工具專屬的按鈕，以及對稱、工具的替代／反向模式、平滑、遮罩、隱藏、面群組、軸向變換和繪畫選項的捷徑。你可以在[介面](interface.md#side-bar)選單中重新排列這些捷徑。
* `底部工具列` - 常用功能的捷徑，說明如下。

::: tip 習慣用左手？
你可以把所有工具列的位置和排列順序左右鏡像，請參考[鏡像頂端列](interface.md#mirror-top-bar)及其他相關選項。
:::

## 底部工具列 {#bottom-toolbar}

![](/images/interface_bottom_toolbar.webp)

* `復原` - 取消上一個操作
* `重做` - 恢復上一個被復原的操作
* `歷史記錄` - 開啟歷史記錄選項，說明請見[歷史記錄](history.md)選單。
* `獨顯` - 切換只顯示目前物件，或顯示所有物件
* `X光` - 讓其他所有物件以 X 光模式算繪，目前物件則維持實心。長按或往上滑動，可以選擇 X 光的材質捕捉和顏色，以及要套用到哪些物件。
* `體素` - [體素重新網格化](topology.md#voxel-remesher)重新網格化按鈕的捷徑。長按或往上滑動會顯示體素重新網格化的選項，例如解析度。
* `世界格線` - 切換格線的顯示。長按或往上滑動會顯示格線的選項，例如顏色和吸附。
* `線框` - 切換線框疊加顯示。長按或往上滑動會顯示線框的選項。
* `檢查器` - 切換顯示目前網格的額外資料。預設會顯示 UV，長按或往上滑動則可以檢查其他存在的屬性，並選擇要顯示在背景上還是網格上。
* `除錯日誌` - 顯示或隱藏 Nomad 除錯日誌的視窗。
* `面群組` - 切換面群組的疊加顯示，請參考[面群組](tools.md#facegroup)工具。

你可以在[介面](interface.md#add-shortcuts-bottom)選單中新增、移除和重新排列這些捷徑。

## 下一步 {#next-steps}

接下來要學什麼，就看你自己和你的興趣了！以下是一些建議：

想進一步了解雕刻工具嗎？請前往[工具](tools.md)章節。

想匯出你的模型？或匯入模型來雕刻？還是想為作品製作圖片？請前往[檔案](files.md)章節。

想學習如何控制雕刻的細節嗎？請前往[拓樸](topology.md)章節，了解多解析度和網格簡化。

想處理更多物件？把簡單的物件和基本體組合成更大的場景？請前往[場景](scene.md)章節。

想了解 Nomad 的*一切*嗎？好選擇！這份手冊涵蓋了 Nomad 的所有功能，包含許多訣竅與技巧，上方還有很好用的搜尋功能。使用左側的導覽列來深入了解吧。

如果你比較喜歡看影片，Holger Schönischka 在 YouTube 上製作了大量的 Nomad 訣竅與技巧：https://www.youtube.com/@ProcreateFX/videos


## 取得協助 {#getting-help}

如果讀完手冊、看完教學影片後還有問題，有三個主要管道可以和其他 Nomad 使用者或 Nomad 的開發者交流：

* 前往論壇：[forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* 加入 Nomad 的 Discord 聊天室：[https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* 直接寄信給開發者：support@nomadsculpt.com
