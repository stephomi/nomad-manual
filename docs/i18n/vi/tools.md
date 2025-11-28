# ![](/icons/toolbox.webp) Công cụ {#tools}

![](/images/tools_menu.webp)

::: tip
Cuộn xuống [Công cụ](#tools-1) để xem mô tả từng công cụ.
:::

## Tổng quan {#overview}

Công cụ được chọn từ `Toolbox` bên phải, và điều khiển bằng `Tool Controls` bên trái. Các thiết lập bổ sung nằm trong menu `Settings`, biểu tượng đầu tiên ở góc trên bên phải.

Các công cụ cọ có điều khiển kích thước và cường độ. Các công cụ chọn có điều khiển cho nhiều kiểu chọn khác nhau. Phần dưới của bảng điều khiển công cụ có các phím tắt cho những thao tác dùng thường xuyên (Smooth, Mask, Hide, Gizmo, Color, Alpha).

Các công cụ của Nomad được tô màu trong hộp công cụ:

* <span class=brush>**Công cụ cọ**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**Công cụ di chuyển**</span> (Move, Drag)
* <span class=mask>**Công cụ mặt nạ**</span> (Mask, SelMask)
* <span class=paint>**Công cụ tô màu**</span> (Paint, Smudge)
* <span class=flatten>**Công cụ làm phẳng**</span> (Flatten, Planar)
* <span class=pinch>**Công cụ bóp**</span> (Crease, Pinch)
* <span class=selection>**Công cụ dựa trên vùng chọn**</span> nơi một mặt nạ 2D được vẽ trước, sau đó thao tác mới diễn ra (Trim, Split, Project)
* <span class=creation>**Công cụ tạo hình**</span> (Tube, Lathe, Insert)
* <span class=transform>**Công cụ biến đổi**</span> (Transform, Gizmo)
* <span class=misc>**Công cụ khác**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**Công cụ xem**</span>



Nhiều công cụ có thể được tùy biến với các hành vi cọ khác nhau, lực nhấn, kết cấu… thông qua menu [Stroke](stroke.md). 


### Điều khiển cọ {#brush-controls}

Thanh công cụ bên trái có các thanh trượt cho bán kính và cường độ, sau đó là các điều khiển riêng cho từng nhóm công cụ, được giải thích bên dưới.

![](/images/tool_left_panel.webp)

::: tip
Thanh trượt cường độ của nhiều công cụ có thể vượt quá 100%, rất đáng để thử nghiệm!
:::

### Chế độ phụ {#sub-mode}
Nút ngay dưới thanh trượt cường độ là nút `Sub`. Nhãn và chức năng của nó sẽ thay đổi theo từng công cụ, và khi nhấn sẽ kích hoạt một hành vi thay thế, thường là ngược lại. Ví dụ với [Paint](#paint) nó sẽ kích hoạt chế độ Erase, với [Crease](#crease) nó sẽ tạo cạnh nổi thay vì rãnh, v.v.

Mặc định nó hoạt động như nút giữ tạm; tức là bạn có thể giữ để tạm thời kích hoạt, khi thả ra nó sẽ tắt. Nếu bạn chạm một lần, chế độ sub sẽ được bật cố định.

### Phím tắt {#shortcuts}
Ở cuối thanh công cụ bên trái là các phím tắt cho [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Mặc định tất cả đều hoạt động như nút giữ tạm; tức là bạn có thể giữ để tạm thời kích hoạt, khi thả ra nó sẽ tắt. Nếu bạn chạm một lần, chế độ phím tắt đó sẽ được bật cố định.

### Điều khiển vùng chọn {#selection-controls}

Các công cụ [Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup) và [Hide](#hide) đều dùng các điều khiển tương tự để chọn vùng trên lưới.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - Hình vẽ tự do
* `Polygon` - Hình khép kín được xác định bởi tổ hợp đường cong và/hoặc đường thẳng. Xem [Chỉnh sửa hình](#shape-editing) bên dưới để biết thêm.
* `Curve` - (Chỉ Project) - Đường cong vẽ tự do cho thao tác chiếu
* `Path` - (Chỉ Project) - Đường cong xác định bởi các điểm. Xem [Chỉnh sửa hình](#shape-editing) bên dưới để biết thêm.
* `Line` - Kéo một đường để xác định một đoạn phẳng. Mặc định nó sẽ tác động lên lưới ngay lập tức, tắt auto validate nếu bạn không muốn vậy (nhấn giữ hoặc vuốt trên biểu tượng đường thẳng)
* `Rect` -  Kéo một đường chéo, điều này sẽ xác định các góc của hình chữ nhật. Nhấn giữ hoặc vuốt để hiện tùy chọn auto validate, ép thành hình vuông, và cho phép cú nhấp đầu tiên là tâm hình chữ nhật.
* `Ellipse` - Kéo một đường chéo, điều này sẽ xác định kích thước ellipse. Nhấn giữ hoặc vuốt để hiện tùy chọn auto validate, ép thành hình tròn, và cho phép cú nhấp đầu tiên là tâm ellipse.
* `Flip` - đảo mặt nạ hình, hoặc hướng của công cụ project.

Hầu hết công cụ có tùy chọn auto validate, nghĩa là thao tác sẽ diễn ra ngay khi bạn vẽ xong hình. Khi auto validate tắt, một nút xanh sẽ xuất hiện cạnh hình, nhấn nút này để thực thi thao tác. Điều này cho phép bạn chỉnh sửa hình, điều chỉnh góc nhìn, khi sẵn sàng dùng hình thì nhấn nút xanh.

### Chỉnh sửa hình dạng {#shape-editing}
Chỉnh sửa polygon và đường cong hoạt động tương tự nhau:

* Ban đầu, kéo một đường để tạo 2 điểm, sau đó kéo từ giữa đường để tạo polygon hoặc đường cong.
* Nhấp vào các điểm để chuyển đổi giữa trơn và nhọn. 
* Nhấp và kéo trên đoạn cong hoặc đoạn thẳng để tạo điểm mới.
* Để xóa một điểm, kéo điểm đó vào điểm lân cận cho đến khi nó chuyển màu đỏ.
* Biểu tượng thùng rác ở góc biểu tượng polygon hoặc path sẽ xóa hình.

### Menu Cài đặt {#settings-menu}

Nhiều công cụ có thiết lập bổ sung nằm trong menu settings, biểu tượng đầu tiên ở menu trên cùng bên phải:

![](/images/tools_settings_menu.webp)

## Công cụ {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Đất sét {#clay}
Công cụ Clay hữu ích để xây dựng khối điêu khắc. `Sub` sẽ loại bỏ vật liệu khỏi khối điêu khắc.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Cọ {#brush}
Cọ tiêu chuẩn. `Sub` sẽ loại bỏ vật liệu.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Di chuyển {#move}
Vùng dưới cọ sẽ dính vào cọ, cho phép biến dạng đàn hồi. Vùng chọn được giữ nguyên trong suốt thao tác move, nên nếu bạn di chuyển cọ đi xa rồi đưa nó về vị trí ban đầu, bạn sẽ không thấy biến dạng nào.

Chế độ sub là `Normal`, và sẽ di chuyển vùng dưới cọ theo pháp tuyến bề mặt.

Cọ này tốt cho cả biến dạng quy mô lớn và biến dạng nhỏ, chính xác.

#### Cài đặt Di chuyển {#move-settings}

* `Radius (Background)` - Khoảng cách tối đa từ mép mô hình mà bạn vẫn có thể điêu khắc, hữu ích khi làm việc trên đường viền (silhouette) của vật thể. 
* `Same-side vertex only` - Bỏ qua các đỉnh có hướng ngược với hướng biến dạng.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Kéo {#drag}
Vùng dưới cọ sẽ dính vào cọ, cho phép biến dạng đàn hồi. Không giống cọ Move, vùng chọn được cập nhật liên tục trong suốt nét vẽ, nên có thể tạo các đối tượng dài, dạng rắn, đặc biệt khi Dynamic Topology được bật.

Chế độ sub là `Normal`, và sẽ di chuyển vùng dưới cọ theo pháp tuyến bề mặt.

Cọ này phù hợp cho các thay đổi hình khối thoáng, mang tính cử chỉ.

#### Cài đặt Kéo {#drag-settings}

* `Radius (Background)` - Khoảng cách tối đa từ mép mô hình mà bạn vẫn có thể điêu khắc, hữu ích khi làm việc trên đường viền (silhouette) của vật thể. 
* `Same-side vertex only` - Bỏ qua các đỉnh có hướng ngược với hướng biến dạng.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Làm mịn {#smooth}
Làm mượt vùng bằng cách lấy trung bình vị trí các điểm. Công cụ này phụ thuộc mạnh vào mật độ polygon.
Nếu có nhiều polygon, hiệu quả làm mượt sẽ kém hơn.

Chế độ sub là `Relax`, chỉ làm mượt lưới (wireframe) nhưng cố giữ chi tiết hình học.

#### Cài đặt Làm mịn {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Nhóm mặt {#smooth-facegroup}

* `Relax` - Sẽ làm mượt biên của facegroup. Dùng cường độ lớn hơn 100% để làm mượt nhanh. `Auto` sẽ chỉ làm mượt nếu xem trước facegroup được bật, `Off` tắt, `On` bật. 

##### Điểm đỉnh (vertex) {#vertex}
* `Sticky vertex on border` - Với lưới có cạnh hở, ví dụ một mặt phẳng, có thể làm mượt các góc. Bật tùy chọn này sẽ khóa các cạnh hở.
* `Relax` - giống chế độ relax thay thế trong thanh công cụ bên trái.
* `Stable smoothing` - Cố gắng làm cho việc làm mượt độc lập với topology. Hoạt động tốt nhất với mật độ topology thay đổi và giá trị cường độ làm mượt cao.

##### Tô màu {#painting}
* `Screen Smoothing` - Dùng tùy chọn này để có làm mượt độc lập topology, ngay cả ở mật độ polygon cao.
* `Screen samples` - Chất lượng làm mượt, giá trị cao hơn sẽ mượt hơn nhưng chậm hơn.

::: tip
Mật độ polygon cao có thể yêu cầu tăng cường độ trên 100%. Giá trị rất cao (300%, 500%) cũng có thể hoạt động tốt như một công cụ điêu khắc, ép vùng dưới cọ phẳng và mượt rất nhanh, giống như đập đất sét bằng búa!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Mặt nạ {#mask}
Công cụ này cho phép bạn mask các đỉnh. Các đỉnh bị mask được bảo vệ khỏi điêu khắc hoặc tô màu. 

Chế độ sub là `Unmask`, và sẽ xóa nơi mặt nạ đã được tô.

Tương tự vùng chọn trong các chương trình vẽ 2D, mask có thể được tô bằng cọ, hoặc tạo bằng các vùng chọn hình, làm mờ hoặc làm sắc cạnh. 

Khác với chương trình 2D, chúng cũng có thể được tạo qua facegroup, và mask có thể dùng để tạo hình học mới thông qua các thao tác kiểu extrusion/extraction. 

![](/videos/tool_mask1.mp4)

 Một thanh công cụ sẽ xuất hiện ở trên cùng khung nhìn với các điều khiển bổ sung. 

![](/images/tool_mask_toolbar.webp)

Tiêu đề thanh có thể chạm để mở/thu gọn, hoặc chạm vào mũi tên ở góc trên bên phải để di chuyển nó lên trên hoặc xuống dưới giao diện.

| Action                                             | Description                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/cross_circle2.webp) Clear              | Xóa mask                                                                                   |
| ![](/icons/invert.webp)        Invert             | Đảo mask                                                                                   |
| ![](/icons/sharpen.webp)       Sharpen            | Làm sắc cạnh mask                                                                          |
| ![](/icons/blur.webp)          Blur               | Làm mờ cạnh mask                                                                           |
|                                 Blur ->            | Kéo trái/phải để làm mờ mask tương tác                                                    |
| ![](/icons/culling.webp)       Front              | Bật/tắt chỉ mask các đỉnh hướng về phía trước                                             |
|                                 Convert            | Chuyển mask thành facegroup                                                               |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | Khi bật, facegroup sẽ được hiển thị, chạm vào facegroup sẽ mask nó                        |
|                                 On tap (mask)      | Khi bật, chạm vào một 'đảo' mask hoặc không mask sẽ tô tràn đảo đó.                       |
| ![](/icons/vertex.webp)        Connected          | Khi bật, chỉ cho phép nét mask ảnh hưởng đến topology nối liền.                           |

##### Cử chỉ nhanh Mặt nạ {#mask-quick-gesture}
Bạn có thể thực hiện các cử chỉ kiểu zbrush khi giữ nút quick masking ở thanh bên trái:
| Action  | Gesture (hold lower-left shortcut) |
| :-----: | :--------------------------------: |
| Invert  | Chạm vào nền                       |
| Clear   | Kéo trên nền                       |
| Blur    | Chạm lên vùng đã mask              |
| Sharpen | Chạm lên vùng chưa mask            |


#### Cài đặt Mặt nạ {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - Menu thiết lập Mask chủ yếu dùng để tạo hình học từ mask. Vì vậy hành vi mặc định là xem trước hình học mới sẽ trông như thế nào. Bạn có thể chọn không xem trước, xem trước extract, xem trước split, và có hiển thị hình học này ở chế độ x-ray hay không.

##### Độ dày {#thickness}
* `Height` - Chiều cao của hình được extract. Biểu tượng Plus/Minus cho phép bạn chuyển vòng giữa extrusion ra ngoài, vào trong, hoặc ở giữa. 
* `Height/Height+Mask` - Chuyển giữa chiều cao cố định, hoặc để phần mask bị làm mờ ảnh hưởng đến chiều cao, cho phép tạo hình mềm và chiều cao thay đổi. 

##### Độ mượt {#smoothness}
Khi bật, sẽ làm mượt biên của hình được extract, hoạt động tốt hơn với số polygon cao. 
* `Iterations` - Lượng làm mượt áp dụng. Giá trị cao sẽ tạo cạnh cong rất mượt, nhưng sẽ bắt đầu lệch khỏi hình mask.
* `All/Sharp border/Borders only` - Làm mượt có thể hoạt động theo mọi hướng, làm mượt cả mặt bên và mặt trên của hình extract, hoặc làm mượt mặt trên và bên nhưng giữ cạnh sắc, hoặc chỉ làm mượt biên, giữ nguyên mặt trên.

##### Vòng cạnh (bên) {#edge-loop-side}
* `Auto Edge-loop (side)` - Sẽ tính toán số lượng chia trên mặt bên của hình extract để tạo polygon vuông khớp với polygon vùng mask. Khi tắt, bạn có thể tự đặt số edge loop bằng thanh trượt edge loop.

----

##### Tách lớp (Extract) {#extract}
* `Extract` - Tạo hình học được extract.
* `Closing action` - Cách extract hoạt động. 'None' sẽ nhân đôi polygon được mask thành hình mới. 'Fill' sẽ làm tương tự và cố vá mặt sau. 'Shell' sẽ extrude theo giá trị đặt trong 'thickness', và là mặc định.

::: tip

Nếu preview ở chế độ 'Extract' với 'X-ray' bật, việc nhấn nút Extract lúc đầu có thể gây nhầm lẫn. Vì menu đang hoạt động, nó sẽ cố xem trước một lần extract trên hình mới, và xray bề mặt gốc. Tuy nhiên vì bạn chưa có mask trên bề mặt mới, nó không thể xem trước extract, và Nomad sẽ cảnh báo 'Nothing to Extract!'. 

Điều này là bình thường, hãy đóng menu thiết lập mask để xem hình mới và hình gốc, và chọn lại bề mặt gốc nếu bạn cần xóa mask hoặc vẽ mask mới.
:::

##### Tách (Split) {#split-mask}
* `Split` - Sẽ extract cả vùng mask VÀ không mask thành các hình mới. 
* `Closing action (masked)` - Cách extract vùng mask hoạt động. 'None' sẽ nhân đôi polygon được mask thành hình mới. 'Fill' sẽ làm tương tự và cố vá mặt sau. 'Shell' sẽ extrude theo giá trị đặt trong 'thickness', và là mặc định.
* `Closing action (unmasked)` - Cách extract vùng không mask hoạt động. 'None' sẽ nhân đôi polygon được mask thành hình mới. 'Fill' sẽ làm tương tự và cố vá mặt sau. 'Shell' sẽ extrude theo giá trị đặt trong 'thickness', và là mặc định.
* `Sync border` - Đảm bảo biên giữa hai hình extract (mask và không mask) nằm sát nhau. Khi tắt, vì thao tác shell sẽ extrude mỗi mặt theo pháp tuyến riêng, có thể xuất hiện khe giữa hai hình.

##### Khắc (Carve) {#carve}
* `Carve` - Ở chế độ mặc định, hoạt động như thể bạn đã trim vào bề mặt theo giá trị 'thickness', giống như cắt một miếng vỏ cam. 



### ![](/icons/tool_maskSelector.webp) Chọn Mặt nạ {#selection-mask}
Công cụ này gần giống [Mask](#mask), điểm khác biệt chính là bạn không dùng stroke để tô mask, mà dùng [Điều khiển vùng chọn](#selection-controls).

Chế độ sub là `Unmask`, và sẽ xóa mask bằng điều khiển vùng chọn.

Selection mask dùng chung thiết lập công cụ với công cụ `Mask`.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Sơn {#paint}
Áp dụng màu và thuộc tính vật liệu. Để tìm hiểu thêm về vật liệu bạn có thể xem phần [Painting](painting.md).

Chế độ sub là `Erase` và sẽ xóa màu.

#### Cài đặt Sơn {#paint-settings}
* `Layer fitering` - Hoạt động giống khóa alpha layer trong photoshop hoặc procreate. Nếu bạn đang vẽ trên một layer, khi bật tùy chọn này, bạn chỉ có thể chỉnh nơi đã có màu; vùng chưa tô sẽ được bảo vệ.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Nhoè {#smudge}
Nhòe màu và thuộc tính vật liệu. Menu thiết lập Smudge có thanh trượt `Quality`, giá trị thấp hơn cho nét vẽ nhanh hơn.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Làm phẳng {#flatten}
Làm phẳng vùng bằng cách chiếu các điểm lên mặt phẳng trung bình.

Chế độ sub là `Fill` và sẽ xác định mặt phẳng dựa trên điểm cao nhất, có xu hướng kéo các điểm lên.

#### Cài đặt Làm phẳng {#flatten-settings}

* `Lock plane direction` - Dùng hướng mặt phẳng được tính ở cú nhấp đầu tiên. Mặc định tắt.
* `Lock plane origin`- Dùng cú nhấp đầu tiên làm tâm mặt phẳng. Mặc định tắt.

Khi một hoặc cả hai tùy chọn này tắt, Flatten có thể được làm sâu dần hoặc thay đổi góc mặt phẳng bằng các nét dài đi qua nhiều độ sâu và độ cong khác nhau. Kết hợp với các tùy chọn lấy mẫu vùng trong menu cọ có thể mang lại điều khiển rất chính xác.

::: tip
Khi làm việc ở vùng cong mạnh, ví dụ cố làm phẳng má nhưng công cụ cứ ảnh hưởng hai bên mũi, hãy thử tạo mask để bảo vệ vùng Flatten không nên tác động.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Mặt phẳng {#planar}
Làm phẳng các điểm bằng cách chiếu lên mặt phẳng trung bình, nhưng ít tích lũy hơn Flatten. Điều này tạo bề mặt cạnh cứng sạch hơn. Nét nhanh sẽ đẩy/kéo bề mặt nhiều hơn, nét chậm bắt đầu từ vùng đã phẳng và đi ra sẽ giữ mặt phẳng tốt hơn.

Chế độ sub là `Fill` và sẽ xác định mặt phẳng dựa trên điểm cao nhất, có xu hướng kéo các điểm lên.

Planar thực ra là cùng một công cụ với `Flatten`, nhưng bật `Lock plane direction`, nghĩa là nó sẽ tạo bề mặt cạnh cứng ổn định hơn, trong khi Flatten mang tính điêu khắc hơn và dùng để tạo vùng bán phẳng.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Tạo rãnh (Crease) {#crease}
Công cụ Crease hữu ích để điêu khắc các vết cắt hoặc lõm nhỏ.

Chế độ sub là `Invert`, và sẽ tạo rãnh nổi.

#### Cài đặt Tạo rãnh {#crease-settings}

* `Pinch factor` - Mức độ kéo các đỉnh sang ngang về phía nét cọ. Nếu pinch là 1 và offset là 0, bề mặt sẽ không thay đổi độ sâu, chỉ thay đổi topology, kéo cạnh về phía nét vẽ.
* `Offset factor` - Mức độ đẩy/kéo các đỉnh theo chiều sâu. Nếu pinch là 0 và offset là 1, sẽ tạo rãnh sâu hoặc vết lồi, nhưng trông răng cưa vì không đủ hình học được kéo về phía rãnh để định nghĩa cạnh và đáy rãnh chính xác.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Bóp (Pinch) {#pinch}
Công cụ này có thể dùng để làm sắc cạnh.

Chế độ sub là `Invert` và sẽ đẩy các đỉnh ra xa nhau.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Cắt gọt (Trim) {#trim}
Công cụ Trim hoạt động bằng cách loại bỏ một phần lưới, và cung cấp tùy chọn xử lý khoảng trống còn lại. Nó dùng [Điều khiển vùng chọn](#selection-controls) để xác định vùng cắt.

::: tip
Vì công cụ này chiếu từ camera, bạn sẽ nhận cảnh báo nếu camera ở chế độ phối cảnh (perspective).

Ở chế độ trực giao (orthographic), đường cắt qua lưới song song với hướng nhìn, đúng như mong đợi. Khi dùng camera phối cảnh, đường cắt sẽ khác nhau giữa phía gần và phía xa của vật thể.
:::

#### Cài đặt Cắt gọt {#trim-settings}

* `Stroke painting` - Nếu tô màu được bật trong menu Paint, vùng vá sẽ được tô bằng màu hiện tại.
* `Boolean` - vá lỗ cắt bằng vùng polygon quad. Vùng vá sẽ phẳng.
* `Legacy` - vá lỗ cắt bằng vùng tam giác. Vùng vá sẽ phẳng.
* `Fill` - vá lỗ bằng vùng tam giác. Vùng vá sẽ là bề mặt cong, như màng xà phòng.
* `None` - không vá lỗ.
* `Boolean Detail Shape` - Kích thước xấp xỉ của quad và tam giác dùng ở phía hình của đường cắt.
* `Boolean Detail Hole` - Kích thước xấp xỉ của tam giác hoặc polygon dùng ở vùng lỗ được vá. 
* `Legacy Detail` - Kích thước xấp xỉ của tam giác dùng cho đường cắt.
* `Legacy Hole smoothing` - Mức độ làm mượt tam giác ở vùng vá.
* `Legacy Threshold espilon` - Giá trị có thể điều chỉnh để cải thiện thuật toán vá lỗ legacy.
* `Fill Detail` - Kích thước xấp xỉ của tam giác dùng cho đường cắt.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Chia tách (Split) {#split}
Tương tự công cụ [Trim](#trim), ngoại trừ Trim loại bỏ vùng chọn, còn Split giữ vùng chọn thành đối tượng mới.

#### Cài đặt Chia tách {#split-settings}

* `Stroke painting` - Nếu tô màu được bật trong menu Paint, vùng vá sẽ được tô bằng màu hiện tại.
* `Boolean` - vá lỗ split bằng vùng polygon quad. Các vùng vá sẽ phẳng.
* `Legacy` - vá lỗ split bằng vùng tam giác. Các vùng vá sẽ phẳng.
* `Fill` - vá lỗ bằng vùng tam giác. Các vùng vá sẽ là bề mặt cong, như màng xà phòng.
* `None` - không vá lỗ.
* `Boolean Detail Shape` - Kích thước xấp xỉ của quad và tam giác dùng ở phía hình của split.
* `Boolean Detail Hole` - Kích thước xấp xỉ của tam giác hoặc polygon dùng ở vùng lỗ được vá. 
* `Legacy Detail` - Kích thước xấp xỉ của tam giác dùng cho split.
* `Legacy Hole smoothing` - Mức độ làm mượt tam giác ở vùng vá.
* `Legacy Threshold espilon` - Giá trị có thể điều chỉnh để cải thiện thuật toán vá lỗ legacy.
* `Fill Detail` - Kích thước xấp xỉ của tam giác dùng cho split.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Chiếu (Project) {#project}
Công cụ Project trông giống [Trim](#trim), nhưng không xóa hay tạo hình học, nó chỉ di chuyển các đỉnh để khớp với vùng chọn.

![](/videos/tool_project.mp4)

::: tip
Nếu bạn dùng Project trong một layer, bạn có thể trộn giữa hình gốc và hình đã project bằng thanh trượt layer.
:::

### ![](/icons/tool_layer.webp) Lớp (Layer) {#layer}
Nâng bề mặt lên, nhưng giới hạn chiều cao.

Nếu bạn giữ bút và tiếp tục tô trên một vùng, Layer sẽ nâng đến một chiều cao nhất định rồi không tăng nữa, khác với các công cụ khác sẽ tiếp tục tích lũy chiều cao.

Lưu ý mặc định giới hạn chỉ đặt theo từng nét! Nếu bạn bắt đầu nét mới, nó sẽ xây từ chiều cao bề mặt mới.

Để đặt chiều cao tối đa cố định qua nhiều nét, hãy dùng công cụ Layer với hệ thống [Layers](layers.md) của Nomad.

Tạo một layer, và dùng công cụ này. Chiều cao tối đa giờ được đặt từ layer, nên bạn có thể vẽ nhiều nét và chiều cao luôn như nhau.

`Sub` sẽ dùng độ sâu tối thiểu, tạo rãnh.

#### Cài đặt Lớp {#layer-settings}

* `Use layer data` - Khi bật, và khi một layer được chọn, dùng dữ liệu layer để đặt chiều cao tối đa.
* `Inflate`- Khi bật sẽ điều chỉnh hướng hoạt động của Layer để cho kết quả mượt hơn.
* `Relax (Normal)` - Mức độ làm mượt áp dụng lên pháp tuyến.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Thổi phồng (Inflate) {#inflate}
Di chuyển các đỉnh theo pháp tuyến riêng của chúng. `Sub` sẽ di chuyển các đỉnh theo pháp tuyến đảo ngược.

#### Cài đặt Thổi phồng {#inflate-setings}
* `Relax (Normal)` - Mức độ làm mượt áp dụng lên pháp tuyến.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Đẩy nhẹ (Nudge) {#nudge}
Di chuyển hoặc 'quệt' các điểm theo hướng nét vẽ.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Đóng dấu (Stamp) {#stamp}

Nhấp và kéo để nâng một vùng điêu khắc theo hình của Alpha đã chọn.

Đây đơn giản là [Brush](#brush) với kiểu stroke đặt thành `Lock + radius`. 

`Sub` sẽ đẩy stamp vào trong thay vì kéo ra khỏi bề mặt.

::: tip
Stamp thường hoạt động tốt nhất với hình học độ phân giải cao. Nếu bạn tìm trên mạng 'wrinkles alpha', 'pores alpha', 'scales alpha'… các texture alpha này kết hợp với Stamp là cách tuyệt vời để thêm chi tiết hữu cơ cho nhân vật.

Hai chế độ stroke hữu ích cho các mục đích khác nhau: 

* `Lock + radius` có *chiều cao* cố định, kéo sẽ chỉnh độ rộng và xoay của stamp. Tốt cho texture da cần cùng độ sâu/chiều cao, nhưng xoay và tỉ lệ khác nhau để tránh lặp.
* `Lock + intensity` có *độ rộng* cố định, kéo sẽ chỉnh xoay và chiều cao stamp. Tốt cho đinh tán, nơi tất cả phải cùng kích thước, nhưng xoay và chiều cao khác nhau. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Xoá Lớp {#delete-layer}
Công cụ này có thể reset layer cục bộ, bạn cần một layer đang hoạt động nếu không sẽ không có gì xảy ra.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Ống (Tube) {#tube}
Tạo ống bằng cách vẽ một đường cong. 
![](/images/tool_tube_new.webp)

Khi ống được tạo, đường dẫn có thể chỉnh sửa trong không gian 3D bằng các điều khiển tương tự [Chỉnh sửa hình](#shape-editing) và chỉnh sửa đường cong tiêu chuẩn. 

![](/videos/tool_tube.mp4)

#### Thanh công cụ bên trái của Ống {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Thanh bên trái có các tùy chọn sau:

* `Sync` - Nếu ống hiện tại là instance, và có node con của ống khác nhau giữa các instance, nút này sẽ đồng bộ lại chúng.
* `Snap` - Khi bật, chế độ curve và path sẽ bám lên các đối tượng khác khi bạn vẽ. Khi tắt, điểm đầu tiên sẽ bám, sau đó phần còn lại của ống sẽ được vẽ ở độ sâu đó. Nó có menu con nhỏ:
    * `Offset` - Đặt độ sâu bám; 0% sẽ cho giữa tiết diện ống bám lên bề mặt, giá trị dương nâng khỏi bề mặt, âm hạ xuống.
* `Curve` - Phác thảo tự do một ống. Có menu con nhỏ:
    * `Auto-validate` - Sẽ tạo ống ngay khi nét vẽ hoàn tất. Khi tắt, một vòng tròn xác nhận màu xanh sẽ hiện cạnh đường dẫn, nhấn để xác nhận, hoặc dùng liên kết `Reset` xuất hiện trong menu này để xóa đường dẫn.
    * `Closed` - biến ống thành vòng kín.
    * `Screen` - Chỉ có khi Auto-validate tắt. Khi bật, đường dẫn được 'ghim' lên màn hình, cho phép bạn di chuyển góc nhìn và đối tượng, còn đường dẫn giữ nguyên. Khi tắt, đường dẫn là một phần của cảnh 3D, và sẽ di chuyển theo camera và đối tượng.
    * `Accuracy` - Số điểm cong dùng để chuyển nét vẽ thành ống. 0% dùng ít điểm nhất nhưng bỏ qua thay đổi cong nhỏ. 100% rất chính xác và dùng nhiều điểm.
* `Path` - Tạo ống bằng cách nhấp để xác định điểm cong. Nhấn vòng tròn xanh để xác nhận đường dẫn. Có menu con nhỏ:
    * `B-spline` - Phương pháp vẽ đường cong thay thế, nơi điểm cong thường không nằm trực tiếp trên đường cong, nhưng có thể cho kết quả mượt hơn phương pháp mặc định.
    * `Closed` - biến ống thành vòng kín
    * `Screen` - Khi bật, đường dẫn được 'ghim' lên màn hình, cho phép bạn di chuyển góc nhìn và đối tượng, còn đường dẫn giữ nguyên. Khi tắt, đường dẫn là một phần của cảnh 3D, và sẽ di chuyển theo camera và đối tượng.

##### Thanh công cụ trên của Ống {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Khi một ống được chọn, một thanh công cụ sẽ xuất hiện ở trên cùng khung nhìn với các điều khiển bổ sung. Nhấp tiêu đề thanh để thu gọn/mở rộng, và nhấp mũi tên góc trên bên phải để di chuyển thanh lên trên hoặc xuống dưới khung nhìn.

* `Validate` - bake ống thành polygon thường để có thể điêu khắc.
* `Edit` - hiển thị các điểm cong để có thể thao tác
* `Mirror` - thêm mirror repeater làm cha của đường cong này
* `Snap` - bám các điểm cong vào bề mặt lân cận
* `Closed` - Nối đầu và cuối đường cong thành vòng kín
* `B-spline` - Chuyển giữa nội suy Catmull-rom và B-spline.
* `Cap` - Chuyển vòng giữa có nắp ở cả hai đầu ống, chỉ đầu hoặc chỉ cuối, hoặc không nắp.
* `Hole` - Thêm độ dày cho ống, biến nó thành ống rỗng. Chuyển vòng giữa có lỗ ở cả hai đầu, chỉ cuối, hoặc không lỗ. 
* `Radius` - Chuyển vòng giữa bán kính đồng nhất, bán kính ở đầu và cuối, hoặc bán kính theo từng điểm cong. Chỉnh bằng các tay cầm màu cam trên đường cong.
* `Twist` - Chuyển vòng giữa không xoắn, xoắn đồng nhất, xoắn ở đầu và cuối, hoặc xoắn theo từng điểm cong. Chỉnh bằng tay cầm màu hồng trên đường cong.
* `Profile` - Chuyển vòng giữa không profile (tức profile tròn), profile đồng nhất, profile ở đầu và cuối, hoặc profile theo từng điểm.
* `Profile edit` - Hiển thị trình chỉnh sửa profile. Hoạt động tương tự [Chỉnh sửa hình](#shape-editing), có thể lưu và tải preset profile, và có công tắc cho phép chỉnh profile trong không gian 3D.
* `Spiral` - Bật menu thêm xoắn xoắn ốc cho ống. Menu này có các tùy chọn `Twist Angle`, `Offset`, `Scale`, và `Angle offset`.
* `X Divisions` - số lượng chia quanh ống, 4 chia sẽ tạo ống vuông chẳng hạn. 
* `Constant density` - khi bật, sẽ giữ polygon vuông. Khi tắt, cho phép đặt `Y divisions` dọc theo chiều dài ống.
* `...` - Menu thiết lập Tube.

#### Bật/tắt xoá điểm đường cong {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Bên dưới thanh công cụ là công tắc xóa điểm cong. Khi bạn kéo một điểm cong gần điểm khác, nó sẽ chuyển màu đỏ, báo rằng nếu thả ra, điểm sẽ bị xóa. Nếu bạn đang chỉnh sửa nhỏ và không muốn xóa điểm, nút này sẽ tắt hành vi xóa điểm.

#### Cài đặt Ống {#tube-settings}
* `Primitive` - các nút cho phép bật/tắt UV, hoặc validate ống.
* `Post subdivision` - phím tắt đặt mức multiresolution trước khi validate.
* `Linear subdivision` - phím tắt đặt mức linear subdivision trước khi validate. 
* `Division X` - giống X Divisions trong thanh công cụ.
* `Division Y` - giống Y Divisions trong thanh công cụ.
* `Curve (Repeater)` - chuyển ống thành [Curve Repeater](scene.md#curve)

::: tip
Division là 4 và Post subdivision là 3 sẽ tạo ống đầu tròn mượt, tốt cho sâu, rắn, bộ phận cơ thể.
:::


### ![](/icons/tool_lathe.webp) Tiện (Lathe) {#lathe}
Tạo bề mặt xoay bằng cách vẽ một đường cong.

Công cụ này rất phù hợp cho các hình như bình, ly rượu.

![](/videos/tool_lathe.mp4)

#### Thanh công cụ bên trái của Tiện {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Thanh bên trái có các tùy chọn sau:

* `Sync` - Nếu Lathe hiện tại là instance, và có node con của Lathe khác nhau giữa các instance, nút này sẽ đồng bộ lại chúng.
* `Fixed` - Khi bật, tâm của Lathe được cố định và hiển thị trên màn hình. Đường tâm này có các điểm chỉnh có thể điều chỉnh. Khi tắt, tâm Lathe sẽ cập nhật động để khớp với đầu và cuối đường cong vẽ.
* `Curve` - Vẽ profile Lathe trong một nét. Có menu con nhỏ:
    * `Auto-validate` - Khi bật, Lathe sẽ được tạo khi nhấc bút khỏi màn hình. Khi tắt, một vòng tròn xanh cạnh đường cong có thể được nhấn để tạo Lathe. Đường cong có thể xóa bằng nút `Reset`.
    * `Closed` - Nối đầu và cuối đường cong thành vòng kín
    * `Screen` - Chỉ có khi Auto-validate tắt. Khi bật, đường dẫn được 'ghim' lên màn hình, cho phép bạn di chuyển góc nhìn và đối tượng, còn đường dẫn giữ nguyên. Khi tắt, đường dẫn là một phần của cảnh 3D, và sẽ di chuyển theo camera và đối tượng.
    * `Accuracy` - Số điểm cong dùng để chuyển nét vẽ thành ống. 0% dùng ít điểm nhất nhưng bỏ qua thay đổi cong nhỏ. 100% rất chính xác và dùng nhiều điểm.
* `Path` - Tạo Lathe bằng cách nhấp để xác định điểm cong. Nhấn vòng tròn xanh để xác nhận đường dẫn. Có menu con nhỏ:
    * `B-spline` - Phương pháp vẽ đường cong thay thế, nơi điểm cong thường không nằm trực tiếp trên đường cong, nhưng có thể cho kết quả mượt hơn phương pháp mặc định.
    * `Closed` - biến ống thành vòng kín
    * `Screen` - Khi bật, đường dẫn được 'ghim' lên màn hình, cho phép bạn di chuyển góc nhìn và đối tượng, còn đường dẫn giữ nguyên. Khi tắt, đường dẫn là một phần của cảnh 3D, và sẽ di chuyển theo camera và đối tượng.

#### Thanh công cụ trên của Tiện {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Khi một Lathe được chọn, một thanh công cụ sẽ xuất hiện ở trên cùng khung nhìn với các điều khiển bổ sung. Nhấp tiêu đề thanh để thu gọn/mở rộng, và nhấp mũi tên góc trên bên phải để di chuyển thanh lên trên hoặc xuống dưới khung nhìn.

* `Validate` - bake Lathe thành polygon thường để có thể điêu khắc.
* `Edit` - hiển thị các điểm cong để có thể thao tác
* `Mirror` - thêm mirror repeater làm cha của Lathe này
* `Snap` - bám các điểm cong vào bề mặt lân cận
* `Stable` - Khi bật, profile đường cong sẽ được gắn làm con của đường tâm Lathe. Khi tắt, đường tâm có thể chỉnh mà không di chuyển đường cong, cho phép tạo hình phức tạp hơn.
* `Focus` - Xoay góc nhìn để thấy profile đường cong phẳng hoàn toàn với camera.
* `Closed` - Nối đầu và cuối đường cong thành vòng kín
* `Cap` - Nếu Closed tắt, chuyển vòng giữa có nắp ở cả hai đầu ống, chỉ đầu hoặc chỉ cuối, hoặc không nắp.
* `Hole` - Thêm độ dày cho Lathe, biến nó thành ống rỗng. Chuyển vòng giữa có lỗ ở cả hai đầu, chỉ cuối, hoặc không lỗ. 
* `B-spline` - Chuyển giữa nội suy Catmull-rom và B-spline.
* `X Divisions` - số lượng chia quanh Lathe, 4 chia sẽ tạo profile vuông chẳng hạn. 
* `Constant density` - khi bật, sẽ giữ polygon vuông. Khi tắt, cho phép đặt `Y divisions` dọc theo chiều dài ống.
* `...` - Menu thiết lập Lathe.

#### Cài đặt Tiện {#lathe-settings}
* `Primitive` - các nút cho phép bật/tắt UV, hoặc validate ống.
* `Post subdivision` - phím tắt đặt mức multiresolution trước khi validate.
* `Linear subdivision` - phím tắt đặt mức linear subdivision trước khi validate. 
* `Division X` - giống X Divisions trong thanh công cụ.
* `Division Y` - giống Y Divisions trong thanh công cụ.
* `Curve (Repeater)` - chuyển profile đường cong thành [Curve Repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) Chèn (Insert) {#insert}
Đặt một đối tượng lên bề mặt đối tượng khác. Khi dùng nó giống công cụ Stamp, nhưng cho hình 3D đầy đủ.

Nếu bạn chọn một primitive từ thanh bên trái, thao tác nhấp-kéo trên bất kỳ bề mặt nào sẽ đặt primitive tại vị trí nhấp, kéo sẽ đặt kích thước. Khi kết thúc kéo, Insert sẽ chuyển sang chế độ [Transform](#transform).

Trong chế độ Instance, kéo sẽ tạo và trượt một instance mới trên bề mặt. Kích thước sẽ được sao chép từ hình đầu tiên, theo cách này bạn có thể đặt nhiều instance cùng kích thước của một đối tượng lên các bề mặt khác.

Bạn không chỉ insert primitive! Chọn *bất kỳ* hình nào trong outliner, nếu Insert ở chế độ Instance hoặc Clone, bạn có thể kéo bản sao của đối tượng được chọn lên bất kỳ bề mặt nào khác.

Nếu một đối tượng có pivot tùy chỉnh, nó sẽ được dùng làm điểm neo. Xem video bên dưới.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Biến đổi (Transform) {#transform}
Di chuyển/Xoay/Scale mô hình trực tiếp bằng 1 và 2 ngón tay, thường trên bề mặt đối tượng khác.

Công cụ được điều khiển bằng thanh bên trái, có 5 nút:

* `Snap` - bám mô hình lên các bề mặt khác
* `Group` - Nếu đối tượng được chọn có kết hợp object và instance, tùy chọn này cho phép bạn xác định hành vi công cụ.
* `Move` - Kéo một ngón sẽ di chuyển đối tượng. Khi Snap bật, sẽ trượt đối tượng dọc theo bề mặt dưới ngón tay.
* `Rotate` - Kéo một ngón sẽ xoay đối tượng. Khi Snap bật, sẽ xoay quanh pháp tuyến bề mặt dưới ngón tay.
* `Scale` - Kéo một ngón sẽ scale đối tượng.

Transform có thể dùng để thao tác nhanh 2 trong 3 chế độ bằng 2 ngón:

* Kéo đối tượng để đặt vị trí. Dừng di chuyển ngón thứ nhất, nhưng không nhấc khỏi màn hình.
* Chạm ngón thứ hai lên màn hình trong khi vẫn giữ ngón thứ nhất. Khi kéo ngón thứ hai, đối tượng sẽ scale.
* Nhấc ngón thứ hai, tiếp tục kéo ngón thứ nhất, đối tượng sẽ quay lại chế độ Move.

Bạn cũng có thể đổi chế độ thứ hai bằng cử chỉ chạm ngón thứ hai:

* Kéo đối tượng để đặt vị trí, dừng di chuyển, nhưng không nhấc ngón khỏi màn hình.
* Chạm ngón thứ hai trong khi giữ ngón thứ nhất
* Công cụ chuyển sang chế độ Rotate. Kéo ngón thứ nhất để đặt góc xoay.
* Chạm ngón thứ hai như trước, công cụ chuyển lại chế độ Move.

Điều này mang lại quy trình nhanh để nhân bản đối tượng trên đối tượng khác, ví dụ đá trên địa hình. Lưu ý nút Clone cũng nằm trong thanh bên trái để truy cập nhanh:

* Dùng Transform để di chuyển một hòn đá vào vị trí.
* Thả ra, nhấn nút Clone
* Di chuyển hòn đá này, xoay/scale nếu cần
* Thả ra, nhấn nút Clone
* Di chuyển hòn đá này, lặp lại.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Công cụ này cho phép bạn di chuyển, xoay và scale đối tượng, và thay đổi pivot của đối tượng.

Tay cầm trong khung nhìn có các tính năng sau:

* `Move` - Kéo trên đường+ mũi tên để di chuyển theo X/Y/Z. Kéo chấm màu đào ở giữa gizmo để tịnh tiến tự do trong không gian màn hình. Nhấp vào các ô vuông đỏ, xanh lá, xanh dương để tịnh tiến trên mặt phẳng X/Y/Z.
* `Rotate` - Kéo trên vòng tròn đỏ/xanh lá/xanh dương để xoay theo X/Y/Z. Kéo quả cầu trong các vòng tròn để xoay tự do.
* `Scale`- Kéo trên các chấm đỏ/xanh lá/xanh dương bên ngoài để scale theo X/Y/Z. Kéo trên các nón đỏ/xanh lá/xanh dương bên ngoài để scale trên mặt phẳng X/Y/Z. Kéo trên vòng tròn màu đào bên ngoài để scale đồng nhất.

![](/images/tool_gizmo.webp)

#### Nút và đỉnh {#nodes-and-vertices}

Mỗi đối tượng trong Nomad được tạo từ một node và các vertex:

* `Node` - 'tay cầm' của đối tượng, lưu trữ tịnh tiến, xoay, scale, gọi là ma trận biến đổi (transformation matrix).
* `Vertices` - Các điểm định nghĩa bề mặt đối tượng, lưu vị trí và thông tin tô màu.

Nếu bạn có một hộp đơn giản gồm 8 vertex, bạn có thể tịnh tiến nó bằng cách chỉnh ma trận biến đổi, hoặc chỉnh vị trí vertex. Khi điêu khắc bạn thường muốn chỉnh vertex, khi di chuyển đối tượng bằng gizmo, bạn thường muốn chỉnh node. Nomad cho phép làm cả hai. 

#### Thanh công cụ menu bên trái {#left-menu-toolbar}

Thanh công cụ bên trái điều khiển việc gizmo sẽ tác động lên node hay vertex, cũng như các chức năng khác:

* `Clone` - Tạo bản sao độc lập của đối tượng hiện tại, có thể kéo đi bằng gizmo.
* `Instance` - Tạo bản sao instance của đối tượng hiện tại. Các đối tượng được liên kết, nên thay đổi điêu khắc trên một đối tượng sẽ xuất hiện trên tất cả instance.
* `Group/Object/Vertex/Auto` - Đặt việc gizmo sẽ tác động lên node hay vertex của đối tượng. Chế độ 'auto' mặc định sẽ cố đoán tốt nhất. Nếu có nhiều đối tượng được cha-con trong một hierarchy, 'Object' chỉ di chuyển đối tượng hiện tại, đối tượng con giữ nguyên. Gizmo cũng có thể tính đến mask và đối xứng.
* `Pin` - Mặc định gizmo sẽ di chuyển đến pivot của đối tượng được chọn. Khi Pin bật, gizmo sẽ giữ nguyên vị trí hiện tại.
* `Align` - Chuyển giữa pivot căn theo đối tượng hiện tại, hoặc căn theo thế giới.
* `Snap rotation` - Bật việc xoay bị ràng buộc theo bước, giá trị bước được hiển thị và có thể chỉnh khi Snap bật.
* `Snap translation` - Bật việc tịnh tiến bị ràng buộc theo bước, giá trị bước được hiển thị và có thể chỉnh khi Snap bật.
* `Pivot` - Khi bật, gizmo có thể di chuyển và xoay mà không di chuyển đối tượng. Nó có menu bổ sung giải thích bên dưới.

#### Trục xoay (Pivot) {#pivot}
Khi chế độ Pivot bật, một menu hiển thị để cho phép thay đổi pivot nhanh:

**Reset** 
* `Center` - Di chuyển pivot đến tâm đối tượng
* `Bottom` - Di chuyển pivot đến đáy đối tượng
* `Align` - Reset xoay để căn theo thế giới.
* `Mask` - Di chuyển pivot đến tâm vùng không bị mask.

**On Tap**
* `None` - không làm gì khi chạm đối tượng
* `Normal` - Di chuyển và xoay pivot để căn theo nơi bề mặt được chạm
* `First` - Di chuyển (nhưng không xoay) pivot đến nơi bề mặt được chạm
* `Medial` - Di chuyển pivot đến giữa đối tượng, dưới nơi bề mặt được chạm.

#### Cài đặt Gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

##### Ma trận (Matrix) {#matrix}
* ![](/icons/target.webp) `Move origin` - Di chuyển đối tượng sao cho pivot của nó nằm ở tâm cảnh (origin).
* ![](/icons/bake.webp)  `Bake` - Đóng băng đối tượng tại vị trí hiện tại, và đặt giá trị translate/rotate về 0, scale về 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - Làm cho giá trị ma trận tương ứng với vị trí tay cầm gizmo trong thế giới.
* ![](/icons/reset.webp) `Reset` - Phím tắt đặt translate về 0, rotate về 0, scale về 1, di chuyển và xoay đối tượng.

::: tip Bake vs bake to pivot
Tạo một hộp, chọn công cụ Gizmo, mở và ghim menu thiết lập. Mặc định translate và rotate là 0, scale là 1.

Bật chế độ Pivot, di chuyển tay cầm sang một bên, tắt Pivot. Pivot đã thay đổi, nhưng lưu ý translate vẫn là 0. 

Nếu bạn muốn thấy pivot *thực sự* ở đâu, nhấn `Bake Pivot`. Lúc này giá trị translate cập nhật. Lưu ý hộp không di chuyển trong thao tác này, cũng như trong chế độ Pivot.

Di chuyển và xoay hộp đến đâu đó, rồi nhấn `Move Origin`. Nó di chuyển đối tượng sao cho pivot ở tâm thế giới, nhưng giữ nguyên xoay.

Nhấn `Reset`, và xoay sẽ được đặt về 0.

Di chuyển và xoay hộp lần nữa, lần này nhấn `Bake`. Pivot giữ nguyên, hộp giữ nguyên, nhưng translate và rotate được đặt về 0.

Hãy luyện vài lần! Hiểu rằng giá trị pivot bị ẩn, Nomad xử lý cho bạn, nhưng nếu cần đặt pivot đến vị trí thực trong không gian, Bake Pivot sẽ làm điều đó.

:::

* `Translation` - giá trị tịnh tiến X, Y, Z
* `Rotation` - giá trị xoay X, Y, Z
* `Scale` - Scale đồng nhất nếu bật, hoặc scale X, Y, Z nếu tắt.
* `Uniform scale` - Bật/tắt khả năng scale đồng nhất hoặc độc lập trên từng trục

-----

* `Compact` - chuyển bố cục gizmo để đặt các tay cầm phụ bên ngoài hoặc bên trong quả cầu xoay
* `Widget size` - kích thước gizmo
* `Thickness` - độ dày đường của gizmo
* `Opacity` - độ mờ gizmo
* `Hide on interaction` - bật/tắt việc tạm ẩn gizmo khi kéo

-----

* `Tangent roll threshold` - Điều khiển cách UI xoay hoạt động khi kéo trên vòng tròn để xoay theo X/Y/Z. Nếu giá trị là 0, xoay hoạt động như núm vặn, kéo gizmo theo vòng tròn. Nếu là 90, xoay hoạt động như kéo dây yo-yo; kéo theo đường thẳng về phía hoặc ra xa điểm nhấp đầu tiên. Giá trị giữa 0 và 90 sẽ kết hợp cả hai; dưới ngưỡng là chuyển động tuyến tính, trên ngưỡng là chuyển động tròn.
* `Numerical input` - khi bật, chạm một lần vào gizmo sẽ bật cửa sổ nhập giá trị chính xác cho trục widget được chạm.

::: warning
[Gizmo](#gizmo), [Translate](#translate), [Rotate](#rotate) và [Scale](#scale) dùng checkbox đối xứng riêng!

Mặc định đối xứng này tắt.
:::

Ở bên trái bạn có thể di chuyển pivot của gizmo, bạn có thể xem video bên dưới để thấy hoạt động.
Điều này đặc biệt hữu ích cho xoay, vì nó không thay đổi gì cho tịnh tiến.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Nhóm mặt (Facegroup) {#facegroup}

Facegroup cho phép bạn tổ chức đối tượng thành các mặt có màu khác nhau. Bạn có thể dùng các nhóm này theo nhiều cách trong Nomad:

* Phương pháp chọn nhanh cho mask
* Ẩn/hiện các phần của đối tượng
* Tổ chức đối tượng mà không cần tách thành nhiều phần
* Định nghĩa vùng UV
* Hướng dẫn quad remesher
* Điều khiển bổ sung cho các công cụ như Smooth.

#### Thanh công cụ bên trái của Nhóm mặt {#facegroup-left-toolbar}

* `Patch ` - Hiển thị các facegroup có sẵn dưới dạng patch. Patch không dùng có thể xóa. Chạm vào patch để đổi tên hoặc đổi màu. Biểu tượng dấu cộng cho phép tạo patch mới.
* `Dot` - Tô trên đối tượng để xác định facegroup. Khi '+ Face Group' bật, mỗi nét mới sẽ tự động tạo facegroup mới, hữu ích để nhanh chóng xác định vùng. Một cú chạm sẽ tô tràn vùng được chọn. Thanh trượt đặt bán kính Dot.
* `Relax` - Làm mượt biên facegroup. Rất hữu ích để định nghĩa cạnh sạch cho quad remeshing, hoặc để xác định panel cho mô hình hard surface. Thanh trượt điều khiển bán kính và cường độ Relax.
* `Shape selector` - Tạo facegroup bằng hình thay vì cọ, thông qua `Lock+Radius`, `Lasso`, `Polygon`, `Rect` và `Ellipse`. Xem [Shape Selector](#shape-selector) để biết thêm.
* `Auto-pick` - Khi bật, sẽ chọn patch tại nơi nét bắt đầu, và áp dụng patch đó cho phần còn lại của nét. Rất hữu ích để dọn dẹp vùng facegroup; nếu một facegroup lan quá xa, bật Auto-pick, bắt đầu nét từ nơi patch facegroup đúng, và kéo đến biên để gán lại patch đúng.

### ![](/icons/tool_hide.webp) Ẩn {#hide}
Ẩn hoặc cô lập các phần của đối tượng. 

Các chế độ chính được điều khiển từ menu bên trái:

* `Dot` - Tô trên đối tượng để ẩn các phần của đối tượng.
* `Shape selector` - Ẩn bằng hình thay vì cọ, thông qua `Lasso`, `Polygon`, `Line`, `Rect` và `Ellipse`. Xem [Shape Selector](#shape-selector) để biết thêm.
* `Show` - Đảo ngược thao tác, nên chế độ được chọn sẽ hiện thay vì ẩn các phần của đối tượng.

Một thanh công cụ sẽ xuất hiện ở trên cùng khung nhìn với các điều khiển bổ sung:

* `Clear` - Khôi phục đối tượng, tất cả phần ẩn sẽ hiện lại.
* `Invert` - Đổi chỗ phần ẩn và phần hiện.
* `Facegroup` - Dùng facegroup để nhanh chóng ẩn phần, chạm vào facegroup sẽ ẩn toàn bộ facegroup.
* `Mask` - Nếu có mask đang hoạt động, nhấn nút này sẽ ẩn phần bị mask.
* `Delete` - Xóa phần đang ẩn của đối tượng
* `Split` - Tách phần đang ẩn của đối tượng thành hình mới.

### ![](/icons/tool_measure.webp) Đo {#measure}
Kéo để đo khoảng cách giữa 2 điểm.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Công cụ này sẽ chuyển đối tượng được chọn thành topology quad sạch, với điều khiển mật độ, hướng cạnh, đối xứng. 

::: tip
Quad Remesher được phát triển bởi [Exoside](https://exoside.com/) cho iOS và desktop. 

Với iOS, đây là mua trong ứng dụng trong Nomad, thanh toán một lần 16 USD.

Với desktop, mua license từ [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Bạn có thể mua cho riêng Nomad desktop, hoặc license chéo cho tất cả ứng dụng desktop được hỗ trợ.

Nếu bạn đã sở hữu Quad Remesher cho ứng dụng desktop khác, bạn có thể [mua nâng cấp lên tất cả nền tảng với chi phí thấp hơn.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher không có trên Android. Android có thể dùng 'Quad Remesh - Instant' mã nguồn mở miễn phí trong menu Topology -> Misc, nhưng hãy hiểu bộ tính năng của nó rất hạn chế.
:::

When this tool is activated for the first time, it will ask if you want to enable it as an in-app purchase. Once active, the left and top toolbars will be enabled.

* `Dot` - Cọ này sẽ đặt mật độ mục tiêu. Cường độ 100% sẽ tô màu đỏ, nghĩa là dùng mật độ quad mục tiêu gấp đôi tại các vùng đó. Cường độ 0% sẽ tô màu lục lam, nghĩa là dùng một nửa mật độ quad mục tiêu tại các vùng đó. Cường độ 50% sẽ tô màu xám, nghĩa là dùng mật độ quad mục tiêu mặc định.
* `Smooth` - Làm mượt các vùng chuyển tiếp mật độ đỏ/xám/lục lam.
* `Curve` - Phác thảo các đường cong trên bề mặt khối điêu khắc, quad remesher sẽ dùng chúng làm đường dẫn cho hướng chảy cạnh (edge flow). Chạm vào một đường cong để xóa nó.
* `Path` - Vẽ các đường dẫn trên bề mặt khối điêu khắc, quad remesher sẽ dùng chúng làm đường dẫn cho hướng chảy cạnh. Chạm vào một đường dẫn để xóa nó. 
* `Rect` - Vẽ các hình chữ nhật trên bề mặt khối điêu khắc, quad remesher sẽ dùng chúng làm đường dẫn cho hướng chảy cạnh. Chạm vào một đường dẫn để xóa nó.
* `Ellipse` - Vẽ các hình elip trên bề mặt khối điêu khắc, quad remesher sẽ dùng chúng làm đường dẫn cho hướng chảy cạnh. Chạm vào một đường dẫn để xóa nó.

#### Thanh công cụ trên của Quad Remesher {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

Một thanh công cụ sẽ xuất hiện ở phía trên khung nhìn với các điều khiển bổ sung:


* `<Count>` - Nhấn vào đây để bắt đầu quá trình quad remesher, con số này cho biết số lượng quad mục tiêu sẽ là bao nhiêu.
* `Quads` - Đặt số lượng quad mục tiêu bằng cách trượt sang trái/phải, hoặc chạm để nhập chính xác một con số. Lưu ý đây là một giá trị định hướng hơn là con số cố định; các tùy chọn khác nhau trong quad remesher thường khiến kết quả không khớp chính xác với mục tiêu này.
* `Half` - Lối tắt để đặt số lượng mục tiêu bằng một nửa số poly hiện tại.
* `Same` - Lối tắt để đặt số lượng mục tiêu bằng đúng số poly hiện tại.
* `Guides` - hiển thị tổng số guide, hoặc chạm để xóa tất cả guide.
* `Density X` - chạm để xóa toàn bộ phần tô mật độ.
* `Density (painting)` - bật/tắt việc sử dụng phần tô mật độ.
* `Face Group` - bật/tắt việc sử dụng facegroup để điều hướng quad remesher.
* `Relax` - bật/tắt việc tự động làm mềm (relax) biên facegroup trong quá trình quad remeshing. Nếu bạn đã làm mềm/làm mượt biên facegroup rồi, hãy tắt tùy chọn này.
* `Relax Slider` - Thanh trượt lối tắt để làm mềm biên facegroup.
* `Hard Edges` - bật/tắt cố gắng giữ lại các cạnh cứng.
* `Reproject Vertex` - bật/tắt việc chiếu lại (reproject) bố cục mới lên lưới đầu vào.
* `Symmetry` - Bật/tắt để cho ra kết quả đối xứng. Lưu ý đối xứng luôn được tính quanh trục X của thế giới, nên hãy đảm bảo mô hình của bạn nằm tại gốc tọa độ nếu bạn muốn kết quả đối xứng.
* `...` - Menu cài đặt Quadremesher. 

#### Menu cài đặt Quad Remesher {#quad-remesher-settings-menu}

Hầu hết các cài đặt này đều có trong thanh công cụ phía trên.

* `<Count>, Half, Same` - Giống các nút Remesh, Half, Same trong thanh công cụ phía trên.
* `Target Quads` - Giống nút `Quads` trong thanh công cụ phía trên
* `Adaptive quad count` - bật/tắt việc dùng quad nhỏ hơn ở vùng có độ cong cao, và quad lớn hơn ở vùng có độ cong thấp.
* `Adaptive size` - Đặt mức độ thích ứng. 100% sẽ cho phép kích thước thích ứng tối đa, ở 0% các quad sẽ đồng nhất.
* `Auto-Detect Hard Edges` - bật/tắt việc điều chỉnh bố cục quad remesh để bám sát hơn các bề mặt sắc cạnh.
* `Density (painting)` - Giống nút `Density (painting)` trong thanh công cụ phía trên
* `Reproject Vertex` - bật/tắt việc chiếu lại bố cục mới lên lưới đầu vào.
* `Face Group` - Giống nút `Face Group` trong thanh công cụ phía trên
* `Relax Slider` - Thanh trượt lối tắt để làm mềm biên facegroup.

::: tip

Một “công thức” để có quad remesh tốt với ít lỗi nhất:

* Dùng Facegroup trên lưới để định nghĩa hướng chảy quad lý tưởng.
* Dùng Facegroup relax để làm mượt biên facegroup.
* Decimate. Điều này đảm bảo bạn không có mặt mỏng hoặc méo trên biên facegroup. Trong cài đặt decimate hãy đảm bảo đã bật facegroup. Việc này sẽ khiến cạnh tam giác bám chính xác theo biên facegroup. 

Trong tùy chọn quad remesh hãy đảm bảo đã tắt relax (vì bạn đã relax lưới rồi) và bạn sẽ có kết quả tốt.

:::

### ![](/icons/tool_select.webp) Chọn {#select}
Dùng các chế độ hình dạng để chọn đối tượng trong cảnh. `Unselect` sẽ loại bỏ đối tượng khỏi vùng chọn.

### ![](/icons/tool_view.webp) Xem {#view}
“Công cụ” này không làm gì cụ thể, nó chỉ là cách để xem mô hình mà không chỉnh sửa cảnh của bạn.


## Menu ngữ cảnh hộp công cụ {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Nhấp chuột phải hoặc nhấn giữ lâu vào một công cụ trong hộp công cụ sẽ mở menu ngữ cảnh. Menu này có các tùy chọn sau:

* `Save` - lưu mọi thay đổi bạn đã thực hiện với công cụ
* `Clone` - nhân bản công cụ thành một phím tắt công cụ mới
* `Last save` - quay lại phiên bản công cụ đã lưu trước đó
* `Icon` - thay đổi biểu tượng cho công cụ
* `Reset` - đặt lại công cụ về mặc định