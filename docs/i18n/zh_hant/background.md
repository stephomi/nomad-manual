# ![](/icons/image.webp) 背景

此選單用來控制 Nomad 的背景顏色，以及要使用的參考圖片。

![](/images/background_overview.webp)

## Background 
![](/images/background_selector.webp)

視窗背景有三種選項：

* `Environment` - 顯示在 [Shading](shading) 中選擇的環境貼圖。可以進一步使用 Blur 和 Exposure（亮度）控制。
* `Color` - 由你選擇的單一純色。
* `Gradient` - 從上到下的顏色漸層。Factor 滑桿可用來決定漸層的中間位置。  

## Reference Image

![](/images/background_reference.webp)

你可以在背景中加入任意圖片作為參考使用。
你可以變更位置與縮放，例如將它移動到螢幕角落。

### ![](/icons/tool_transform.webp) Transform 

這個按鈕可以讓你以互動方式放置參考圖片。使用兩指拖曳、縮放、旋轉，將參考圖片移到合適的位置。最終的位置會反映在下方的滑桿中：

* `Overlay` - 設為 0% 時，參考圖片永遠在物件後方；設為 100% 時，則在物件前方。
* `Opacity` - 圖片的透明度。
* `Position` - 圖片的 X 與 Y 位置。
* `Rotation` - 圖片旋轉角度。
* `Scale` - 圖片縮放比例。


::: tip

相機與參考圖片是連動的。 

這代表如果你將參考圖片對齊你的雕塑，當你從 [Camera 選單](camera) 建立一個相機時，參考圖片的位置、旋轉與縮放也會一併儲存在該相機中。你可以關閉參考圖片、旋轉到其他視角；當你再次透過該相機觀看時，參考圖片會以你先前設定的方式重新啟用。

甚至可以為不同的相機選擇不同的圖片！

 ![](/videos/reference_camera.mp4)

:::
