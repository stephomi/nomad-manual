# ![](/icons/toolbox.webp) Công cụ {#tools}

![](/images/tools_menu.webp)

::: tip
Kéo xuống phần [Công cụ](#tools-1) để xem mô tả của từng công cụ.
:::

## Tổng quan {#overview}

Bạn chọn công cụ trong `Hộp công cụ` ở bên phải, và điều khiển nó bằng `Điều khiển công cụ` ở bên trái. Các cài đặt bổ sung nằm trong menu `Công cụ`, ở menu góc trên bên phải.

Các công cụ cọ có điều khiển kích thước và cường độ. Các công cụ chọn vùng có điều khiển cho nhiều kiểu chọn khác nhau. Phần dưới cùng của thanh điều khiển công cụ có các phím tắt cho những thao tác hay dùng (Làm mịn, Mặt nạ, Ẩn, Nhóm mặt, Gizmo, Màu sắc, Alpha).

Các công cụ của Nomad được tô màu theo nhóm trong hộp công cụ (tắt `Công cụ có màu` trong menu [Giao diện](interface.md) nếu muốn nhãn đơn sắc):

* <span class=brush>**Công cụ cọ**</span> (Đất sét, Cọ, Làm mịn, Lớp, Bơm phồng, Xóa Lớp, Quad Remesher)
* <span class=move>**Công cụ di chuyển**</span> (Di chuyển, Kéo, Đàn hồi, Thúc nhẹ)
* <span class=mask>**Công cụ mặt nạ**</span> (Mặt nạ)
* <span class=paint>**Công cụ vẽ màu**</span> (Vẽ, Bôi nhòe)
* <span class=flatten>**Công cụ làm phẳng**</span> (Làm phẳng, Phẳng, Đánh bóng)
* <span class=pinch>**Công cụ nhéo**</span> (Rãnh sắc, Nhéo)
* <span class=stamp>**Công cụ dấu**</span> (Dấu Triện, VDM)
* <span class=selection>**Công cụ dựa trên vùng chọn**</span>: bạn vẽ một mặt nạ 2d trước, rồi một thao tác mới được thực hiện (Cắt, Tách, Chiếu)
* <span class=creation>**Công cụ tạo hình**</span> (Ống, Tiện, Chèn)
* <span class=transform>**Công cụ biến đổi**</span> (Biến Đổi, Gizmo, Sắp xếp, Lattice)
* <span class=misc>**Công cụ khác**</span> (Nhóm mặt, Ẩn)
* <span class=view>**Công cụ xem**</span> (Xem, Đo, Chọn)



Nhiều công cụ trong số này có thể tùy chỉnh với hành vi cọ, áp lực, họa tiết khác nhau... qua menu [Nét vẽ](stroke.md). 


### Điều khiển cọ {#brush-controls}

Thanh công cụ bên trái có các thanh trượt bán kính và cường độ, tiếp theo là các điều khiển riêng của từng nhóm công cụ, được giải thích bên dưới.

![](/images/tool_left_panel.webp)

::: tip
Thanh trượt cường độ của nhiều công cụ có thể vượt quá 100%, rất đáng để thử!
:::

### Chế độ phụ {#sub-mode}
Nút nằm ngay dưới thanh trượt cường độ là nút `Trừ`. Nhãn và chức năng của nó thay đổi theo từng công cụ, và khi nhấn sẽ kích hoạt một hành vi thay thế, thường là ngược lại. Ví dụ với [Vẽ](#paint), nó bật chế độ Xóa, với [Rãnh sắc](#crease), nó tạo ra các gờ nổi thay vì rãnh...

Mặc định, nó hoạt động như một nút giữ: bạn có thể nhấn giữ để tạm thời kích hoạt, và khi buông tay thì nó tắt. Nếu bạn chạm vào nó, chế độ phụ sẽ được bật cố định.

### Phím tắt {#shortcuts}
Ở cuối thanh công cụ bên trái là các phím tắt cho [Làm mịn](#smooth), [Mặt nạ](#mask), [Ẩn](#hide), [Nhóm mặt](#facegroup), [Gizmo](#gizmo), [Màu sắc](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Mặc định, tất cả đều hoạt động như nút giữ: bạn có thể nhấn giữ để tạm thời kích hoạt, và khi buông tay thì nó tắt. Nếu bạn chạm vào, chế độ của phím tắt đó sẽ được bật cố định.

### Điều khiển vùng chọn {#selection-controls}

Các công cụ [Mặt nạ](#mask), [Vẽ](#paint), [Cắt](#trim), [Tách](#split), [Chiếu](#project), [Nhóm mặt](#facegroup), [Ẩn](#hide) và [Chọn](#select) đều dùng những điều khiển tương tự nhau để chọn các vùng trên lưới.

![](/images/tools_shape_selector_panel.webp)

Chạm vào nút hình dạng ở thanh công cụ bên trái (nút này hiển thị hình dạng hiện tại, mặc định là `Dây thòng lọng`) để mở cửa sổ bật lên chứa các hình dạng. Với những công cụ cũng hoạt động bằng cọ (Mặt nạ, Vẽ, Nhóm mặt, Ẩn), cửa sổ này còn chứa cả các kiểu nét vẽ.

* `Xem` - Không có hình dạng, công cụ không làm gì đặc biệt, giống như chế độ máy ảnh.
* `Dây thòng lọng` - Một hình dạng vẽ tay tự do
* `Đa giác` - Một hình khép kín được tạo bởi sự kết hợp của các đường cong và/hoặc đường thẳng. Xem [Chỉnh sửa hình dạng](#shape-editing) bên dưới để biết thêm.
* `Đường Cong` - (Chỉ với Chiếu) - Một đường cong vẽ tay tự do dùng cho phép chiếu
* `Đường dẫn` - (Chỉ với Chiếu) - Một đường cong được xác định bởi các điểm. Xem [Chỉnh sửa hình dạng](#shape-editing) bên dưới để biết thêm.
* `Đường thẳng` - Kéo một đường để xác định một đoạn phẳng. Mặc định nó sẽ tác động lên lưới ngay lập tức, hãy đổi tùy chọn `Chỉnh sửa` nếu bạn không muốn vậy (nhấn giữ hoặc vuốt trên biểu tượng đường thẳng)
* `Dải` - Một dải nằm giữa hai đường dẫn song song, với một dải chuyển cường độ trên nó. `Kéo dài` giữ nguyên giá trị tối đa ở phía bên kia đường dẫn xa thay vì dừng lại ở dải, `Đảo` đổi đường dẫn mà dải chuyển bắt đầu.
* `Hình chữ nhật` - Kéo một đường chéo để xác định các góc của hình chữ nhật. Nhấn giữ hoặc vuốt để hiện tùy chọn `Chỉnh sửa`, `Hình vuông` để ép thành hình vuông, và `Căn giữa` để điểm nhấp đầu tiên là tâm của hình chữ nhật.
* `Hình elip` - Kéo một đường chéo để xác định kích thước của hình elip. Nhấn giữ hoặc vuốt để hiện tùy chọn `Chỉnh sửa`, `Hình tròn` để ép thành hình tròn, và `Căn giữa` để điểm nhấp đầu tiên là tâm của hình elip.
* `Lật` - Đảo ngược mặt nạ của hình dạng, hoặc hướng của công cụ Chiếu.

Hầu hết công cụ có tùy chọn `Chỉnh sửa`, quyết định điều gì xảy ra khi bạn vẽ xong hình dạng:
* `Sửa: tắt` - Thao tác được thực hiện ngay khi bạn buông tay.
* `Sửa: bật` - Hình dạng vẫn có thể chỉnh sửa. Một nút màu xanh lá xuất hiện cạnh hình dạng, dùng để thực hiện thao tác. Nhờ vậy bạn có thể chỉnh hình dạng, điều chỉnh góc nhìn, và khi đã sẵn sàng thì nhấn nút xanh lá.
* `Sửa: giữ` - Thao tác được thực hiện khi bạn buông tay, trừ khi bạn giữ yên ở cuối nét vẽ để tiếp tục chỉnh sửa hình dạng.

### Chỉnh sửa hình dạng {#shape-editing}
Việc chỉnh sửa đa giác và đường cong hoạt động tương tự nhau:

* Để bắt đầu, kéo một đường để xác định 2 điểm, rồi kéo từ giữa đường đó ra để tạo đa giác hoặc đường cong.
* Nhấp vào các điểm để chuyển đổi giữa mềm và sắc. 
* Nhấp và kéo trên các đoạn cong hoặc thẳng để tạo điểm mới.
* Để xóa một điểm, kéo nó vào điểm bên cạnh cho đến khi nó chuyển sang màu đỏ.
* Biểu tượng thùng rác ở góc của biểu tượng đa giác hoặc đường dẫn sẽ xóa hình dạng.

### Menu cài đặt {#settings-menu}

Nhiều công cụ có cài đặt bổ sung nằm trong menu `Công cụ`, ở menu góc trên bên phải. Menu này bị làm mờ với những công cụ không có cài đặt bổ sung.

![](/images/tools_settings_menu.webp)

## Công cụ {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)    <br> [Đất sét](#clay)       | ![](/icons/tool_brush.webp)   <br> [Cọ](#brush)     | ![](/icons/tool_move.webp)       <br> [Di chuyển](#move)              | ![](/icons/tool_drag.webp)      <br> [Kéo](#drag)           | ![](/icons/tool_elastic.webp)   <br> [Đàn hồi](#elastic)     | ![](/icons/tool_smooth.webp)  <br> [Làm mịn](#smooth)   |
| ![](/icons/tool_mask.webp)    <br> [Mặt nạ](#mask)       | ![](/icons/tool_paint.webp)   <br> [Vẽ](#paint)     | ![](/icons/tool_smudge.webp)     <br> [Bôi nhòe](#smudge)          | ![](/icons/tool_flatten.webp)   <br> [Làm phẳng](#flatten)     | ![](/icons/tool_planar.webp)    <br> [Phẳng](#planar)       | ![](/icons/tool_polish.webp)  <br> [Đánh bóng](#polish)   |
| ![](/icons/tool_crease.webp)  <br> [Rãnh sắc](#crease)   | ![](/icons/tool_pinch.webp)   <br> [Nhéo](#pinch)     | ![](/icons/tool_trim.webp)       <br> [Cắt](#trim)              | ![](/icons/tool_split.webp)     <br> [Tách](#split)         | ![](/icons/tool_project.webp)   <br> [Chiếu](#project)     | ![](/icons/tool_layer.webp)   <br> [Lớp](#layer)     |
| ![](/icons/tool_inflate.webp) <br> [Bơm phồng](#inflate) | ![](/icons/tool_nudge.webp)   <br> [Thúc nhẹ](#nudge)     | ![](/icons/tool_stamp.webp)      <br> [Dấu Triện](#stamp)            | [VDM](#vdm)                                                  | ![](/icons/tool_clearLayer.webp) <br> [Xóa Lớp](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Ống](#tube)       |
| ![](/icons/tool_lathe.webp)   <br> [Tiện](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Chèn](#insert)   | ![](/icons/tool_transform.webp)  <br> [Biến Đổi](#transform)    | ![](/icons/tool_gizmo.webp)     <br> [Gizmo](#gizmo)         | ![](/icons/tool_faceGroup.webp) <br> [Nhóm mặt](#facegroup) | ![](/icons/tool_hide.webp)    <br> [Ẩn](#hide)       |
| ![](/icons/tool_measure.webp) <br> [Đo](#measure) | [Sắp xếp](#arrange)                                      | ![](/icons/tool_remesh.webp)     <br> [Quad Remesher](#quad-remesher) | ![](/icons/tool_select.webp)    <br> [Chọn](#select)       | ![](/icons/tool_lattice.webp)   <br> [Lattice](#lattice)     | ![](/icons/tool_view.webp)    <br> [Xem](#view)       |

------

### ![](/icons/tool_clay.webp) Đất sét {#clay}
Công cụ Đất sét rất hữu ích để đắp dần khối cho bản điêu khắc. `Trừ` sẽ lấy bớt vật liệu khỏi bản điêu khắc.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Cọ {#brush}
Cọ tiêu chuẩn. `Trừ` sẽ lấy bớt vật liệu.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Di chuyển {#move}
Vùng dưới cọ sẽ dính vào cọ, cho phép biến dạng đàn hồi. Vùng chọn được giữ nguyên trong suốt quá trình di chuyển, nên nếu bạn kéo cọ ra xa rồi đưa nó trở lại điểm bắt đầu, bạn sẽ không thấy biến dạng nào.

Chế độ phụ là `Pháp tuyến`, sẽ di chuyển vùng dưới cọ theo pháp tuyến của bề mặt.

Cọ này phù hợp cả với biến dạng lớn lẫn những biến dạng nhỏ cần sự cẩn thận.

#### Cài đặt Di chuyển {#move-settings}

* `Bán kính (Nền)` - Bạn có thể ở cách mép mô hình bao xa mà vẫn điêu khắc được, hữu ích khi làm việc với đường bao của đối tượng. Bỏ chọn để chỉ kéo khi bạn bắt đầu trên mô hình.
* `Chỉ đỉnh cùng phía` - Bỏ qua các đỉnh hướng ngược chiều với biến dạng.
* `Hướng` - Được dùng bởi chế độ phụ `Pháp tuyến`, nó quyết định thao tác kéo sẽ đẩy hay kéo bề mặt:
    * `Tự động` - Tự chọn một trong hai phương pháp bên dưới cho bạn, dựa trên góc của pháp tuyến bề mặt.
    * `Pháp tuyến 3D` - So sánh vị trí con trỏ trên màn hình với pháp tuyến bề mặt khi nhìn từ máy ảnh.
    * `XY` - Dùng vị trí con trỏ trên màn hình (lên/xuống, trái/phải) để quyết định đẩy hay kéo.
    * `Ngưỡng` - Với `Tự động`, đây là giới hạn góc quyết định phương pháp nào được dùng.
* `Tốc độ xoay` - Bạn có thể vặn xoắn vùng đang kéo trong lúc di chuyển nó: xoay hai ngón tay, xoay thân bút, hoặc giữ một phím bổ trợ (Alt, Ctrl, Shift hoặc Cmd) khi kéo bằng chuột. Mỗi loại ngón tay, bút và chuột có một thanh trượt riêng; bỏ chọn một thanh để tắt kiểu nhập đó.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Kéo {#drag}
Vùng dưới cọ sẽ dính vào cọ, cho phép biến dạng đàn hồi. Khác với cọ Di chuyển, vùng chọn được cập nhật liên tục trong suốt nét vẽ, nên bạn có thể tạo ra những hình dài như con rắn, nhất là khi bật Tô pô động (DynTopo).

Chế độ phụ là `Pháp tuyến`, sẽ di chuyển vùng dưới cọ theo pháp tuyến của bề mặt.

Cọ này phù hợp với những thay đổi hình dạng phóng khoáng, theo cảm hứng.

#### Cài đặt Kéo {#drag-settings}

Kéo có các cài đặt giống như [Di chuyển](#move-settings): `Bán kính (Nền)`, `Chỉ đỉnh cùng phía`, `Hướng` và `Tốc độ xoay`.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_elastic.webp) Đàn hồi {#elastic}
Nắm và kéo bề mặt như [Di chuyển](#move), nhưng với biến dạng đàn hồi: thay vì dừng lại ở mép cọ, lực kéo giảm dần mượt mà theo khoảng cách trên khắp đối tượng, hơi giống như kéo giãn cao su. Bán kính cọ quyết định độ rộng của vùng bị kéo.

Chế độ phụ là `Pháp tuyến`, sẽ di chuyển vùng dưới cọ theo pháp tuyến của bề mặt.

Cọ này phù hợp với những thay đổi tỷ lệ lớn, mềm mại mà vẫn giữ được bề mặt mượt.

#### Cài đặt Đàn hồi {#elastic-settings}

Đàn hồi có các cài đặt giống như [Di chuyển](#move-settings), ngoại trừ `Chỉ đỉnh cùng phía`. `Bán kính (Nền)` mặc định bị tắt.

### ![](/icons/tool_smooth.webp) Làm mịn {#smooth}
Làm mịn vùng bằng cách lấy trung bình vị trí các điểm. Công cụ này phụ thuộc rất nhiều vào mật độ đa giác.
Vì vậy nếu bạn có nhiều đa giác, việc làm mịn sẽ kém hiệu quả hơn.

Chế độ phụ là `Thư giãn`, chỉ làm mịn khung lưới nhưng cố gắng giữ lại các chi tiết hình học.

#### Cài đặt Làm mịn {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Nhóm mặt {#smooth-facegroup}

* `Thư giãn` - Làm mịn đường biên của các nhóm mặt. Dùng cường độ lớn hơn 100% để làm mịn đường biên thật nhanh. `Tự động` chỉ làm mịn khi chế độ xem trước nhóm mặt được bật, `Không` sẽ tắt, `Có` sẽ bật. 

##### Đỉnh {#vertex}
* `Bảo toàn thể tích` - Làm mịn mà không làm co bề mặt, nên làm mịn nhiều lần cũng không khiến hình bị xẹp. Nút bánh răng bên cạnh chứa các giá trị `Thu nhỏ` và `Bơm phồng` dùng cho việc này.
* `Bảo vệ đường viền` - Với các lưới có cạnh hở, ví dụ một mặt phẳng, các góc có thể bị làm mịn mất. Bật tùy chọn này sẽ giữ cố định các đỉnh nằm trên đường biên của lưới.
* `Làm mịn ổn định` - Cố gắng làm cho việc làm mịn không phụ thuộc vào tô pô. Tùy chọn này hoạt động tốt nhất khi mật độ tô pô không đồng đều và với giá trị cường độ làm mịn cao.
* `Thư giãn` - Giống với chế độ thay thế Thư giãn trên thanh công cụ bên trái.

##### Sơn {#painting}
* `Làm mịn màn hình` - Dùng tùy chọn này để làm mịn không phụ thuộc vào tô pô, kể cả khi số đa giác rất cao. `Tự động`, `Không` hoặc `Có`.
* `Mẫu màn hình` - Chất lượng làm mịn, số càng cao thì càng mịn nhưng càng chậm.

::: tip
Với mật độ đa giác cao, bạn có thể cần tăng cường độ lên trên 100%. Các giá trị rất cao (300%, 500%) cũng có thể dùng rất tốt như một công cụ điêu khắc, buộc các vùng dưới cọ nhanh chóng trở nên phẳng và mịn, giống như đập đất sét bằng búa gỗ!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Mặt nạ {#mask}
Công cụ này cho phép bạn che mặt nạ các đỉnh. Các đỉnh bị che mặt nạ sẽ được bảo vệ khỏi việc điêu khắc hay vẽ màu. 

Chế độ phụ là `Gỡ mặt nạ`, sẽ xóa mặt nạ ở những chỗ đã vẽ.

Giống như vùng chọn trong các phần mềm vẽ 2d, mặt nạ có thể được vẽ bằng cọ, hoặc tạo bằng các hình dạng chọn vùng (`Dây thòng lọng`, `Hình chữ nhật`, `Dải`...), làm mờ hay làm sắc. Chọn cọ hoặc hình dạng trong cửa sổ nét vẽ của thanh công cụ bên trái, xem [Điều khiển vùng chọn](#selection-controls).

Khác với các phần mềm vẽ 2d, mặt nạ còn có thể được tạo từ các nhóm mặt, và có thể dùng để tạo hình học mới qua các thao tác kiểu đùn/tách khối. 

![](/videos/tool_mask1.mp4)

 Một thanh công cụ sẽ xuất hiện ở phía trên khung nhìn với các điều khiển bổ sung. 

![](/images/tool_mask_toolbar.webp)

Bạn có thể chạm vào tiêu đề của thanh để mở rộng/thu gọn, hoặc chạm vào mũi tên ở góc trên bên phải để chuyển nó lên trên hoặc xuống dưới giao diện.

| Thao tác                                           | Mô tả                                                                                      |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Xóa tất cả         | Xóa mặt nạ trên mọi đối tượng. Khi các đối tượng khác cũng có mặt nạ, một nút `Xóa` bổ sung chỉ xóa mặt nạ của các đối tượng đang chọn |
| ![](/icons/invert.webp)        Đảo ngược          | Đảo ngược mặt nạ                                                                           |
| ![](/icons/sharpen.webp)       Làm sắc            | Làm sắc mép mặt nạ                                                                         |
| ![](/icons/blur.webp)          Làm mờ             | Làm mờ mép mặt nạ                                                                          |
| ![](/icons/outline.webp)       Đường viền         | Che mặt nạ đường biên hở của lưới, như mép của một mặt phẳng hay vành của một lỗ           |
| ![](/icons/blur.webp)          Làm mờ ->          | Kéo sang phải để làm mờ mặt nạ, sang trái để làm sắc                                       |
| ![](/icons/circle_plus.webp)   Mở rộng ->         | Kéo sang phải để mở rộng vùng mặt nạ, sang trái để thu nhỏ                                 |
| ![](/icons/intensity.webp)     Tăng cường ->      | Kéo sang phải để tăng độ mạnh của mặt nạ, sang trái để giảm, mà không đổi hình dạng của nó |
| ![](/icons/dig.webp)           Khoang ->          | Tạo lại mặt nạ từ độ cong của bề mặt: kéo sang phải để chỉ các chỗ lõm còn vẽ được, sang trái để chỉ các chỗ lồi còn vẽ được |
| ![](/icons/culling.webp)       Mặt trước          | Bật/tắt để chỉ che mặt nạ các đỉnh hướng về phía trước                                     |
| ![](/icons/eye_open.webp)      Có thể thấy        | Với các hình dạng, bật/tắt để bỏ qua các đỉnh bị che khuất sau những bề mặt khác           |
|                                 Chuyển đổi         | Chuyển mặt nạ thành một nhóm mặt                                                           |
| ![](/icons/group_to_mask.webp) Chạm đơn (nhóm mặt) | Khi bật, các nhóm mặt sẽ được hiển thị, chạm vào một nhóm mặt sẽ che mặt nạ nhóm đó        |
|                                 Chạm đơn (mặt nạ)  | Khi bật, chạm vào một "đảo" đa giác có mặt nạ hoặc không có mặt nạ sẽ tô kín đảo đó.       |
| ![](/icons/connect.webp)       Đã kết nối         | Khi bật, nét vẽ mặt nạ chỉ tác động lên phần tô pô được kết nối.                           |

##### Cử chỉ nhanh cho Mặt nạ {#mask-quick-gesture}
Bạn có thể thực hiện các cử chỉ kiểu ZBrush trong khi giữ nút mặt nạ nhanh ở thanh công cụ bên trái:
| Thao tác  | Cử chỉ (giữ phím tắt ở góc dưới bên trái) |
| :-------: | :---------------------------------------: |
| Đảo ngược | Chạm vào nền                              |
| Xóa       | Kéo trên nền                              |
| Làm mờ    | Chạm vào vùng có mặt nạ                   |
| Làm sắc   | Chạm vào vùng không có mặt nạ             |


#### Cài đặt Mặt nạ {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

Cài đặt Mặt nạ chủ yếu dùng để tạo hình học từ mặt nạ. Các thẻ ở phía trên chọn thao tác: [Chiết xuất](#extract), [Tách](#split-mask) hoặc [Chạm khắc](#carve). Các tùy chọn bên dưới thay đổi theo thao tác.

* `Xem trước` - Hiển thị hình học mới sẽ trông như thế nào trong khi bạn điều chỉnh cài đặt.
* `X-quang` - Những đối tượng nào được vẽ ở chế độ x-quang khi xem trước: `Không có`, `Không được chọn`, `Đã chọn` hoặc `Tất cả`.

##### Chiết xuất {#extract}
* `Chiết xuất` - Tạo phần hình học được chiết xuất thành một đối tượng mới.
* `Hành động đóng` - Cách khép kín hình được chiết xuất. `Không có` sẽ nhân bản các đa giác có mặt nạ thành một hình mới và để hở. `Lấp đầy` cũng làm như vậy, đồng thời lấp và làm mịn lỗ ở mặt sau (đừng dùng trên bề mặt phẳng). `Lớp vỏ` sẽ khép kín hình bằng giá trị `Chiều cao`, và là lựa chọn mặc định.

::: tip

Nếu bật xem trước cùng x-quang, việc nhấn nút Chiết xuất lúc đầu có thể gây khó hiểu. Vì menu vẫn đang mở, nó sẽ cố xem trước một lần chiết xuất trên hình mới của bạn, và hiển thị bề mặt gốc ở chế độ x-quang. Tuy nhiên vì hình mới không có mặt nạ, nó không thể xem trước việc chiết xuất, và Nomad sẽ cảnh báo bạn 'Không có gì để trích xuất!'. 

Điều này là bình thường, hãy đóng menu cài đặt mặt nạ để xem hình mới và hình gốc, rồi chọn lại bề mặt gốc nếu bạn cần xóa mặt nạ hoặc vẽ mặt nạ mới.
:::

##### Tách {#split-mask}
* `Tách` - Sẽ chiết xuất cả vùng có mặt nạ LẪN vùng không có mặt nạ thành các hình mới. 
* `Hành động đóng` (có mặt nạ) - Cách khép kín phần có mặt nạ, với các lựa chọn `Không có`, `Lấp đầy` và `Lớp vỏ` giống như Chiết xuất.
* `Hành động đóng` (không có mặt nạ) - Cách khép kín phần không có mặt nạ, với các lựa chọn tương tự.

##### Chạm khắc {#carve}
* `Chạm khắc` - Hoạt động như thể bạn đã cắt sâu vào bề mặt một khoảng bằng `Chiều cao`, giống như cắt một miếng vỏ cam. `Chiều cao` không thể bằng 0.

##### Chiều cao {#thickness}
* `Chiều cao` - Chiều cao của hình được chiết xuất. Nút Cộng/Trừ cho phép bạn chuyển vòng giữa đùn ra ngoài, đùn vào trong, hoặc cả hai phía. 

##### Độ mịn {#smoothness}
Khi bật, hình được chiết xuất sẽ được làm mịn, hoạt động tốt hơn với số đa giác cao. 
* `Tất cả` / `Chỉ các biên` - Làm mịn toàn bộ hình, hoặc chỉ đường biên của nó, giữ nguyên hình dạng mặt trên.
* `Các lần lặp lại` - Với `Tất cả`, đây là mức độ làm mịn được áp dụng. Giá trị cao sẽ tạo ra các cạnh cong rất mịn, nhưng sẽ bắt đầu lệch khỏi hình dạng của mặt nạ.
* `Thành` - Với `Chỉ các biên`, mức độ làm mịn trên các thành bên. Nút của nó chuyển giữa Thư giãn, giữ lại các góc cứng, và Làm mịn, làm tròn cả các góc.
* `Mặt trong` - Với `Chỉ các biên`, mức độ làm đều mặt trên. Nút của nó chuyển giữa Thư giãn, giữ lại các chi tiết điêu khắc và chỉ làm đều hướng đùn (để chi tiết không tạo ra gai nhọn), và Làm mịn, làm mịn chính bề mặt đó.

##### Mặt bên {#edge-loop-side}
* `Thẳng` - Các thành bên phẳng trơn của hình được chiết xuất.
* `Vát` - (Chỉ với Chiết xuất dùng `Lớp vỏ`) Một viền nghiêng ở mép trước. `Vát` đặt độ rộng của nó, theo % của `Chiều cao` hoặc theo đơn vị thế giới (nút bên cạnh dùng để chuyển đổi), `Phân đoạn vát` chia nhỏ viền (mặc định là `Tự động`), và một đường cong cho phép bạn tạo dáng mặt cắt của nó.
* `Biên dạng` - Tạo dáng các thành bên bằng một đường cong biên dạng, với `Chiều rộng` theo % của `Chiều cao` hoặc theo đơn vị thế giới.
* `Mặt nạ` - Chiều cao đi theo mặt nạ: những phần mặt nạ bị làm mờ sẽ có chiều cao thấp hơn, cho phép tạo các hình mềm mại với chiều cao thay đổi.
* `Phân đoạn thành` - Số vòng cạnh trên các thành bên. Với `Tự động`, Nomad chọn số phân đoạn sao cho các đa giác vuông vắn, khớp với đa giác của vùng có mặt nạ.



### ![](/icons/tool_maskSelector.webp) Mặt nạ chọn vùng {#selection-mask}
Công cụ Mặt nạ chọn vùng (Chọn Mặt Nạ) giờ là một phần của [công cụ Mặt nạ](#mask). Để che mặt nạ bằng hình dạng thay vì nét cọ, hãy chọn một hình dạng (`Dây thòng lọng`, `Đa giác`, `Hình chữ nhật`...) trong cửa sổ nét vẽ của công cụ Mặt nạ, xem [Điều khiển vùng chọn](#selection-controls).

Chế độ phụ `Gỡ mặt nạ` cũng dùng được với các hình dạng, và sẽ xóa mặt nạ bên trong hình.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Vẽ {#paint}
Áp màu và các thuộc tính vật liệu. Để tìm hiểu thêm về vật liệu, bạn có thể xem phần [Sơn](painting.md).

Chế độ phụ là `Xóa`, sẽ xóa lớp sơn.

Ngoài các nét cọ, Vẽ còn có thể tô kín các hình dạng (`Dây thòng lọng`, `Hình chữ nhật`, `Dải`...), xem [Điều khiển vùng chọn](#selection-controls).

#### Cài đặt Vẽ {#paint-settings}
* `Bộ lọc lớp` - Hoạt động giống như khóa alpha của lớp trong Photoshop hay Procreate. Nếu bạn đang vẽ trên một lớp và bật tùy chọn này, bạn chỉ có thể chỉnh sửa những chỗ đã có sơn; các vùng chưa sơn sẽ được bảo vệ. Tùy chọn này chỉ khả dụng khi có một lớp được chọn.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Bôi nhòe {#smudge}
Bôi nhòe màu và các thuộc tính vật liệu. Menu cài đặt của Bôi nhòe có thanh trượt `Chất lượng`, giá trị thấp hơn nghĩa là nét vẽ nhanh hơn.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Làm phẳng {#flatten}
Làm phẳng vùng bằng cách chiếu các điểm lên mặt phẳng trung bình.

Chế độ phụ là `Đổ đầy`, sẽ xác định một mặt phẳng theo điểm cao nhất, và có xu hướng kéo các điểm lên.

#### Cài đặt Làm phẳng {#flatten-settings}

* `Khóa hướng mặt phẳng` - Dùng hướng mặt phẳng được tính ở lần nhấp đầu tiên. Mặc định tùy chọn này bị tắt.
* `Khóa gốc mặt phẳng`- Dùng điểm nhấp đầu tiên làm tâm của mặt phẳng. Mặc định tùy chọn này bị tắt, và chỉ có thể bật cùng với `Khóa hướng mặt phẳng`.

Khi một hoặc cả hai tùy chọn này bị tắt, bạn có thể làm phẳng sâu dần hoặc thay đổi góc của mặt phẳng bằng những nét dài đi qua các độ sâu và độ cong khác nhau. Kết hợp với các tùy chọn lấy mẫu theo vùng trong menu cọ, cách này cho phép điều khiển rất chính xác.

::: tip
Khi làm việc ở những vùng có độ cong lớn, ví dụ muốn làm phẳng gò má nhưng công cụ cứ ảnh hưởng đến hai bên sống mũi, hãy thử tạo một mặt nạ để bảo vệ những vùng mà cọ làm phẳng không nên chạm tới.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Phẳng {#planar}
Làm các điểm nằm trên cùng một mặt phẳng bằng cách chiếu lên mặt phẳng trung bình, nhưng ít bị đắp dồn hơn cọ Làm phẳng. Nhờ đó tạo ra các bề mặt cạnh cứng gọn gàng hơn. Những nét nhanh sẽ đẩy và kéo bề mặt nhiều hơn, còn những nét chậm bắt đầu từ vùng đã phẳng rồi lan ra sẽ giữ mặt phẳng tốt hơn.

Chế độ phụ là `Đổ đầy`, sẽ xác định một mặt phẳng theo điểm cao nhất, và có xu hướng kéo các điểm lên.

Thực ra Phẳng chính là công cụ `Làm phẳng`, nhưng bật sẵn `Khóa hướng mặt phẳng`, nghĩa là nó có xu hướng tạo ra bề mặt cạnh cứng ổn định hơn, trong khi Làm phẳng mang tính điêu khắc hơn và có thể dùng để tạo các vùng bán phẳng.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_polish.webp) Đánh bóng {#polish}
Một thành viên khác của họ Làm phẳng, được thiết lập để đánh bóng bề mặt thành các mặt phẳng gọn gàng. Đây là cùng công cụ `Làm phẳng`, với các mặc định [Nét vẽ](stroke.md) khác: `Vệt kéo bút`, `Bộ lọc pháp tuyến theo vùng` và `Bộ lọc độ sâu` được bật.

Chế độ phụ là `Đổ đầy`, giống như Làm phẳng.

Đánh bóng có các cài đặt giống như [Làm phẳng](#flatten-settings): `Khóa hướng mặt phẳng` và `Khóa gốc mặt phẳng`.

### ![](/icons/tool_crease.webp) Rãnh sắc {#crease}
Công cụ Rãnh sắc hữu ích để điêu khắc các vết cắt hoặc vết lõm nhỏ.

Chế độ phụ là `Đảo ngược`, sẽ tạo ra một gờ nổi.

#### Cài đặt Rãnh sắc {#crease-settings}

* `Hệ số nhúm` - Mức độ kéo các đỉnh sang ngang về phía cọ. Nếu nhúm ở mức 1 và độ lệch ở mức 0, bề mặt sẽ không thay đổi độ sâu mà chỉ thay đổi tô pô, kéo các cạnh về phía nét vẽ.
* `Hệ số độ lệch` - Mức độ đẩy/kéo các đỉnh theo chiều sâu. Nếu nhúm ở mức 0 và độ lệch ở mức 1, sẽ tạo ra rãnh sâu hoặc gờ nổi, nhưng trông sẽ lởm chởm vì không đủ hình học được kéo về phía rãnh để định hình chính xác hai bên hay đáy rãnh.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Nhéo {#pinch}
Công cụ này có thể dùng để làm sắc các cạnh.

Chế độ phụ là `Đảo ngược`, sẽ đẩy các đỉnh tách xa nhau.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Cắt {#trim}
Công cụ Cắt hoạt động bằng cách loại bỏ một phần của lưới, và cho bạn các tùy chọn để xử lý khoảng trống còn lại. Nó dùng [Điều khiển vùng chọn](#selection-controls) để xác định vùng cắt.

Chế độ phụ là `Lật`, sẽ đảo ngược hình dạng, để phía bên kia bị loại bỏ.

::: tip
Vì công cụ này chiếu từ máy ảnh, bạn sẽ nhận được cảnh báo nếu máy ảnh đang ở chế độ phối cảnh.

Ở chế độ trực giao, vết cắt xuyên qua lưới song song với góc nhìn, đúng như điều mọi người thường mong đợi. Khi dùng máy ảnh phối cảnh, vết cắt sẽ trông khác nhau ở phía xa và phía gần của đối tượng.
:::

#### Cài đặt Cắt {#trim-settings}

Các cài đặt được gom trong `Lấp chỗ trống`:

* `Vẽ nét` - Nếu tính năng vẽ màu được bật trong menu Sơn, vùng được vá sẽ được tô bằng màu đang chọn.
* `Boolean` - Lấp lỗ của vết cắt bằng một vùng đa giác tứ giác. Vùng được lấp sẽ phẳng.
* `Cũ` - Lấp lỗ của vết cắt bằng một vùng tam giác. Vùng được lấp sẽ phẳng.
* `Lấp đầy` - Lấp lỗ bằng một vùng tam giác. Vùng được lấp sẽ là một bề mặt cong, giống như màng bong bóng xà phòng.
* `Không có` - Không lấp lỗ.

Với `Boolean`, phần `Chi tiết` có:

* `Hình dạng` - Kích thước gần đúng của các tứ giác và tam giác dùng ở phía hình dạng của vết cắt.
* `Lỗ` - Kích thước gần đúng của các tam giác hoặc đa giác dùng trên lỗ được lấp. Nút liên kết cạnh `Chi tiết` giữ giá trị này đồng bộ với `Hình dạng`, bỏ liên kết để đặt riêng.
* `Bảo toàn cấu trúc liên kết` - Không làm mịn và đơn giản hóa đường biên của vết cắt, giữ nguyên tô pô gốc của lưới gần các mặt bị che mặt nạ hoặc bị ẩn.

Với `Cũ`:

* `Chi tiết` - Kích thước gần đúng của các tam giác dùng trên vết cắt.
* `Làm mịn lỗ` - Mức độ thư giãn các tam giác trên vùng được lấp.
* `Ngưỡng epsilon` - Một giá trị có thể điều chỉnh để cải thiện thuật toán lấp lỗ kiểu cũ.

Với `Lấp đầy`:

* `Chi tiết` - Kích thước gần đúng của các tam giác dùng trên vết cắt.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Tách {#split}
Tương tự công cụ [Cắt](#trim), chỉ khác là trong khi Cắt loại bỏ vùng chọn, Tách sẽ giữ vùng chọn thành một đối tượng mới.

Chế độ phụ là `Chia`: mỗi mảnh được giữ thành một đối tượng riêng, nên các hình chồng lên nhau (ví dụ khi dùng đối xứng) sẽ được cắt thành các phần riêng biệt thay vì gộp thành một.

#### Cài đặt Tách {#split-settings}

Tách có các cài đặt `Lấp chỗ trống` giống như [Cắt](#trim-settings): `Vẽ nét`, các phương pháp `Boolean`, `Cũ`, `Lấp đầy` và `Không có`, cùng các tùy chọn `Chi tiết` của chúng.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Chiếu {#project}
Công cụ Chiếu trông giống công cụ [Cắt](#trim), nhưng nó không xóa hay tạo hình học nào, mà chỉ di chuyển các đỉnh để khớp theo vùng chọn.

![](/videos/tool_project.mp4)

::: tip
Nếu bạn dùng Chiếu khi đang ở trong một lớp, bạn có thể pha trộn giữa hình gốc và hình đã chiếu bằng thanh trượt của lớp.
:::

### ![](/icons/tool_layer.webp) Lớp {#layer}
Nâng bề mặt lên, nhưng giới hạn chiều cao.

Nếu bạn giữ bút trên màn hình và tiếp tục quét qua một vùng, Lớp sẽ nâng lên đến một độ cao nhất định rồi dừng lại, trong khi các công cụ khác sẽ tiếp tục đắp thêm chiều cao.

Lưu ý rằng mặc định giới hạn này chỉ áp dụng cho từng nét vẽ! Nếu bạn bắt đầu một nét mới, nó sẽ đắp tiếp từ độ cao bề mặt mới.

Để đặt chiều cao tối đa cố định qua nhiều nét vẽ, hãy dùng công cụ Lớp cùng với hệ thống [Lớp](layers.md) của Nomad.

Tạo một lớp, rồi dùng công cụ này. Chiều cao tối đa giờ được đặt theo lớp, nên bạn có thể vẽ nhiều nét mà chiều cao vẫn luôn như nhau.

`Trừ` sẽ dùng độ sâu tối thiểu, tạo ra các rãnh.

#### Cài đặt Lớp {#layer-settings}

* `Sử dụng dữ liệu lớp` - Khi bật, và khi có một lớp được chọn, dùng dữ liệu của lớp để đặt chiều cao tối đa. Một cảnh báo sẽ nhắc bạn khi chưa có lớp nào được chọn.
* `Bơm phồng`- Khi bật, điều chỉnh hướng tác động của Lớp để có kết quả mịn hơn.
* `Thư giãn (Pháp tuyến)` - Khi bật `Bơm phồng`, đây là mức độ làm mịn áp dụng lên các pháp tuyến.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_inflate.webp) Bơm phồng {#inflate}
Di chuyển các đỉnh theo pháp tuyến của chính chúng. `Trừ` sẽ di chuyển các đỉnh theo pháp tuyến đảo ngược.

#### Cài đặt Bơm phồng {#inflate-setings}
* `Thư giãn (Pháp tuyến)` - Mức độ làm mịn áp dụng lên các pháp tuyến.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Thúc nhẹ {#nudge}
Di chuyển hoặc 'miết' các điểm theo hướng của nét vẽ.

Chế độ phụ là `Nếp gấp`, sẽ đẩy một nếp gấp vật liệu dọc theo nét vẽ: một chỗ phồng phía trước cọ, một chỗ lõm phía sau.

#### Cài đặt Thúc nhẹ {#nudge-settings}
* `Làm mịn` - Mức độ làm mịn vùng dưới cọ trong khi bạn thúc nó, giúp bề mặt bị miết luôn sạch sẽ.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Dấu Triện {#stamp}

Nhấp và kéo để nâng một vùng của bản điêu khắc theo hình dạng của Alpha đang chọn.

Đây đơn giản là [công cụ Cọ](#brush) với kiểu nét vẽ đặt là `Khóa + bán kính`. 

`Trừ` sẽ ấn dấu lõm vào thay vì kéo nổi lên khỏi bề mặt.

::: tip
Dấu Triện thường cho kết quả tốt nhất với hình học độ phân giải cao. Nếu bạn tìm trên mạng 'wrinkles alpha', 'pores alpha', 'scales alpha'..., các họa tiết alpha này kết hợp với Dấu Triện có thể là cách tuyệt vời để thêm chi tiết tự nhiên cho bản điêu khắc nhân vật.

Hai chế độ nét vẽ hữu ích cho những việc khác nhau. 

* `Khóa + bán kính` có *chiều cao* cố định, thao tác kéo điều chỉnh độ rộng và góc xoay của dấu. Phù hợp với họa tiết da, khi chúng cần cùng độ sâu/chiều cao nhưng khác góc xoay và tỷ lệ để che đi các mẫu lặp lại.
* `Khóa + cường độ` có *độ rộng* cố định, thao tác kéo điều chỉnh góc xoay và chiều cao của dấu. Phù hợp với đinh tán, khi tất cả phải cùng kích thước nhưng khác góc xoay và chiều cao. 

:::

![](/videos/tool_stamp.mp4)

### ![](/icons/tool_vdm.webp) VDM {#vdm}

Đóng dấu một bản đồ dịch chuyển vector (VDM). Khác với alpha, vốn chỉ có thể đẩy bề mặt lên hoặc xuống, VDM lưu trữ cả một hình 3d hoàn chỉnh, nên nó có thể đóng dấu những phần nhô ra như tai, sừng hay lá cuộn. Nó hoạt động giống như [Dấu Triện](#stamp), với cùng các chế độ nét vẽ `Khóa + bán kính` và `Khóa + cường độ`.

`Trừ` (`Đảo ngược`) sẽ lật độ sâu của dấu, để ấn nó vào bề mặt như một chiếc khuôn.

Bản thân VDM được chọn trong menu [Alpha](stroke.md#alpha), nơi cũng có thanh trượt `Chiều cao` để chỉ thay đổi tỷ lệ chiều cao của dấu, giữ nguyên độ dịch chuyển sang ngang.

Nút `Tạo` ở thanh công cụ bên trái cho phép bạn tự làm dấu của riêng mình:

* `VDM mới...` - Thêm một mặt phẳng được thiết lập sẵn để điêu khắc VDM. Điêu khắc hình của bạn trên đó, rồi bake nó bằng `Tô pô -> Bake -> VDM`: Nomad sẽ thêm dấu mới vào thư viện VDM và chọn nó.
* `Thu VDM` - (Thử nghiệm) Kéo trên bề mặt của một mô hình để lấy vùng đó và biến nó thành một dấu VDM. `Dung sai` làm phẳng mượt mà đường biên của vùng được lấy.

::: tip
Tránh dùng DynTopo khi điêu khắc trên mặt phẳng VDM, nó làm hỏng UV của mặt phẳng và làm méo dấu. Cũng hãy giữ phần điêu khắc cách xa đường biên của mặt phẳng, nếu không dấu sẽ lộ ra một cạnh cứng.
:::


### ![](/icons/tool_clearLayer.webp) Xóa Lớp {#delete-layer}
Công cụ này có thể đặt lại các lớp một cách cục bộ, bạn cần có một lớp đang hoạt động, nếu không sẽ chẳng có gì xảy ra. Nó xóa dữ liệu điêu khắc của lớp, và cả lớp sơn khi tính năng vẽ màu được bật.

Chế độ phụ là `Đảo ngược`, sẽ tăng nhẹ độ mạnh của lớp thay vì xóa nó.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Ống {#tube}
Tạo một ống bằng cách vẽ một đường cong. 
![](/images/tool_tube_new.webp)

Khi ống đã được tạo, đường dẫn có thể được chỉnh sửa trong không gian 3d bằng các điều khiển tương tự như công cụ [Chỉnh sửa hình dạng](#shape-editing) tiêu chuẩn và công cụ chỉnh sửa đường cong. 

![](/videos/tool_tube.mp4)

#### Thanh công cụ bên trái của Ống {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Thanh công cụ bên trái có các tùy chọn sau:

* `Đồng bộ` - Nếu ống hiện tại là thực thể, và có các nút con của ống khác nhau giữa các thực thể, tùy chọn này sẽ đồng bộ lại chúng.
* `Snap` - Khi bật, các chế độ đường cong và đường dẫn sẽ bám vào các đối tượng khác khi bạn vẽ. Khi tắt, chỉ điểm đầu tiên được bám, phần còn lại của ống sẽ được vẽ ở độ sâu đó.
* `Độ dịch chuyển` - Đặt độ sâu của điểm bám; 0% sẽ cho tâm mặt cắt của ống bám vào bề mặt, giá trị dương sẽ nâng nó lên khỏi bề mặt, giá trị âm sẽ hạ nó xuống. 100% bằng bán kính của ống.
* `Xem` - Không ở chế độ vẽ, để bạn có thể di chuyển máy ảnh tự do.
* `Đường Cong` - Phác thảo ống tự do. Nó có một menu nhỏ bật ra:
    * `Chỉnh sửa` - Điều gì xảy ra khi bạn kết thúc nét vẽ, xem [Điều khiển vùng chọn](#selection-controls): tạo ống ngay lập tức, giữ đường cong ở trạng thái chỉnh sửa được với một vòng tròn xác nhận màu xanh lá bên cạnh, hoặc `Giữ` ở cuối nét vẽ để tiếp tục chỉnh sửa.
    * `Đóng` - Biến ống thành một vòng khép kín.
    * `Vẽ tiếp` - Sau khi xác nhận một ống, vẫn ở lại công cụ để vẽ ống tiếp theo.
    * `Độ chính xác` - Số điểm đường cong được dùng để chuyển đường đã vẽ thành ống. 0% sẽ dùng ít điểm nhất, nhưng sẽ bỏ sót những thay đổi độ cong nhỏ của đường. 100% sẽ rất chính xác, và dùng nhiều điểm.
* `Đường dẫn` - Tạo ống bằng cách nhấp để xác định các điểm của đường cong. Chạm vào vòng tròn xanh lá để xác nhận đường dẫn. Nó có một menu nhỏ bật ra:
    * `B-spline` - Một cách vẽ đường cong khác, trong đó các điểm đường cong thường không nằm ngay trên đường cong, nhưng có thể cho kết quả mượt hơn cách mặc định.
    * `Đóng` - Biến ống thành một vòng khép kín
    * `Màn hình` - Khi bật, đường dẫn được 'ghim' vào màn hình, cho phép bạn di chuyển góc nhìn và đối tượng trong khi đường dẫn vẫn giữ nguyên vị trí. Khi tắt, đường dẫn là một phần của cảnh 3d, và sẽ di chuyển cùng máy ảnh và các đối tượng.
* `Mặt cắt` - Đường cong trở thành một vòng bao quanh hình, cắt qua hai điểm của nó theo hướng mà bạn đang nhìn.

##### Thanh công cụ phía trên của Ống {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Khi một ống được chọn, một thanh công cụ sẽ xuất hiện ở phía trên khung nhìn với các điều khiển bổ sung. Nhấp vào tiêu đề của thanh để thu gọn/mở rộng, và nhấp vào mũi tên ở góc trên bên phải để chuyển thanh lên trên hoặc xuống dưới khung nhìn.

* `Hoàn tất` - Bake ống thành các đa giác thông thường để có thể điêu khắc.
* `Chỉnh sửa` - Hiển thị các điểm của đường cong để có thể thao tác với chúng
* `Gương` - Thêm một bộ lặp gương làm cha của đường cong này
* `Snap` - Bám các điểm đường cong vào các bề mặt gần đó
* `Đóng` - Nối điểm đầu và điểm cuối của đường cong thành một vòng khép kín
* `B-spline` - Chuyển đổi giữa nội suy Catmull-rom và B-spline.
* `Nắp` - Chuyển vòng giữa có nắp ở cả hai đầu ống, chỉ ở đầu hoặc cuối, hoặc không có nắp.
* `Lỗ` - Thêm độ dày cho ống, biến nó thành một đường ống rỗng. Chuyển vòng giữa có lỗ ở cả hai đầu, chỉ ở đầu cuối, hoặc không có lỗ. 
* `Bán kính` - Chuyển vòng giữa bán kính đồng đều, bán kính ở đầu và cuối, hoặc bán kính cho từng điểm của đường cong. Chúng được chỉnh bằng các tay cầm màu cam trên đường cong.
* `Quấn` - Chuyển vòng giữa không xoắn, xoắn đồng đều, xoắn ở đầu và cuối, hoặc xoắn cho từng điểm của đường cong. Chúng được chỉnh bằng các tay cầm màu hồng trên đường cong.
* `Biên dạng` - Chuyển vòng giữa không có biên dạng (tức biên dạng tròn), biên dạng đồng đều, biên dạng ở đầu và cuối, hoặc biên dạng cho từng điểm.
* `Chỉnh sửa biên dạng` - Hiển thị trình chỉnh sửa biên dạng. Nó hoạt động tương tự công cụ [Chỉnh sửa hình dạng](#shape-editing), có thể lưu và tải các biên dạng thiết lập sẵn, và có nút bật/tắt cho phép bạn chỉnh sửa biên dạng trong không gian 3d.
* `Xoắn ốc` - Bật/tắt menu để thêm độ xoắn ốc cho ống. Menu này có các tùy chọn `Góc quấn`, `Độ lệch`, `Tỷ lệ` và `Độ lệch góc`.
* `Phân chia X` - Số phân đoạn quanh ống, ví dụ 4 phân đoạn sẽ tạo ra một ống vuông. 
* `Mật độ không đổi` - Khi bật, sẽ giữ cho các đa giác vuông vắn. Khi tắt, cho phép bạn đặt `Phân chia Y` dọc theo chiều dài của ống.
* `...` - Menu cài đặt Ống.

#### Nút bật/tắt xóa điểm đường cong {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Bên dưới thanh công cụ là nút bật/tắt xóa điểm đường cong. Khi bạn kéo một điểm đường cong lại gần điểm khác, nó sẽ chuyển sang màu đỏ, báo hiệu rằng nếu buông tay thì điểm đó sẽ bị xóa. Nếu bạn đang chỉnh sửa nhỏ và không muốn xóa điểm, nút này sẽ tắt hành vi xóa điểm.



#### Cài đặt Ống {#tube-settings}
* `Hình cơ bản` - Các nút cho phép bật/tắt UV, hoặc xác nhận ống.
* `Hậu phân chia` - Lối tắt để đặt cấp đa độ phân giải trước khi xác nhận.
* `Phân khu tuyến tính` - Lối tắt để đặt cấp phân chia tuyến tính trước khi xác nhận. 
* `Phân chia X` - Giống như Phân chia X trên thanh công cụ.
* `Phân chia Y` - Giống như Phân chia Y trên thanh công cụ.
* `Đường cong (Lặp lại)` - Chuyển ống thành một [Bộ lặp đường cong](scene.md#curve)

::: tip
Đặt Phân chia ở 4 và Hậu phân chia ở 3 sẽ tạo ra các ống tròn mịn với đầu bo tròn, phù hợp cho giun, rắn hay các bộ phận cơ thể.
:::


### ![](/icons/tool_lathe.webp) Tiện {#lathe}
Tạo một bề mặt tròn xoay bằng cách vẽ một đường cong.

Công cụ này rất hợp với các hình như bình hoa, ly rượu.

![](/videos/tool_lathe.mp4)

#### Thanh công cụ bên trái của Tiện {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Thanh công cụ bên trái có các tùy chọn sau:

* `Đồng bộ` - Nếu hình tiện hiện tại là thực thể, và có các nút con của hình tiện khác nhau giữa các thực thể, tùy chọn này sẽ đồng bộ lại chúng.
* `Cố định` - Khi bật, tâm của hình tiện được cố định và hiển thị trên màn hình. Đường tâm này có các điểm chỉnh sửa có thể điều chỉnh. Khi tắt, tâm của hình tiện sẽ tự động cập nhật để khớp với điểm đầu và điểm cuối của đường cong đã vẽ.
* `Xem` - Không ở chế độ vẽ, để bạn có thể di chuyển máy ảnh tự do.
* `Đường Cong` - Vẽ biên dạng của hình tiện trong một nét. Nó có một menu nhỏ bật ra:
    * `Chỉnh sửa` - Điều gì xảy ra khi bạn nhấc bút, xem [Điều khiển vùng chọn](#selection-controls): tạo hình tiện ngay lập tức, giữ đường cong ở trạng thái chỉnh sửa được với một vòng tròn xanh lá bên cạnh để tạo hình tiện, hoặc `Giữ` ở cuối nét vẽ để tiếp tục chỉnh sửa.
    * `Đóng` - Nối điểm đầu và điểm cuối của đường cong thành một vòng khép kín
    * `Vẽ tiếp` - Sau khi xác nhận một hình tiện, vẫn ở lại công cụ để vẽ hình tiếp theo.
    * `Độ chính xác` - Số điểm đường cong được dùng để chuyển đường đã vẽ thành ống. 0% sẽ dùng ít điểm nhất, nhưng sẽ bỏ sót những thay đổi độ cong nhỏ của đường. 100% sẽ rất chính xác, và dùng nhiều điểm.
* `Đường dẫn` - Tạo hình tiện bằng cách nhấp để xác định các điểm của đường cong. Chạm vào vòng tròn xanh lá để xác nhận đường dẫn. Nó có một menu nhỏ bật ra:
    * `B-spline` - Một cách vẽ đường cong khác, trong đó các điểm đường cong thường không nằm ngay trên đường cong, nhưng có thể cho kết quả mượt hơn cách mặc định.
    * `Đóng` - Biến ống thành một vòng khép kín
    * `Màn hình` - Khi bật, đường dẫn được 'ghim' vào màn hình, cho phép bạn di chuyển góc nhìn và đối tượng trong khi đường dẫn vẫn giữ nguyên vị trí. Khi tắt, đường dẫn là một phần của cảnh 3d, và sẽ di chuyển cùng máy ảnh và các đối tượng.

#### Thanh công cụ phía trên của Tiện {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Khi một hình tiện được chọn, một thanh công cụ sẽ xuất hiện ở phía trên khung nhìn với các điều khiển bổ sung. Nhấp vào tiêu đề của thanh để thu gọn/mở rộng, và nhấp vào mũi tên ở góc trên bên phải để chuyển thanh lên trên hoặc xuống dưới khung nhìn.

* `Hoàn tất` - Bake hình tiện thành các đa giác thông thường để có thể điêu khắc.
* `Chỉnh sửa` - Hiển thị các điểm của đường cong để có thể thao tác với chúng
* `Gương` - Thêm một bộ lặp gương làm cha của hình tiện này
* `Snap` - Bám các điểm đường cong vào các bề mặt gần đó
* `Ổn định` - Khi bật, biên dạng đường cong sẽ là con của đường tâm của hình tiện. Khi tắt, đường tâm có thể được chỉnh sửa mà không làm di chuyển đường cong, cho phép tạo những hình phức tạp hơn.
* `Lấy nét` - Xoay góc nhìn để thấy biên dạng đường cong nằm phẳng hoàn toàn trước máy ảnh.
* `Đóng` - Nối điểm đầu và điểm cuối của đường cong thành một vòng khép kín
* `Nắp` - Nếu Đóng bị tắt, chuyển vòng giữa có nắp ở cả hai đầu ống, chỉ ở đầu hoặc cuối, hoặc không có nắp.
* `Lỗ` - Thêm độ dày cho hình tiện, biến nó thành một đường ống rỗng. Chuyển vòng giữa có lỗ ở cả hai đầu, chỉ ở đầu cuối, hoặc không có lỗ. 
* `B-spline` - Chuyển đổi giữa nội suy Catmull-rom và B-spline.
* `Phân chia X` - Số phân đoạn quanh hình tiện, ví dụ 4 phân đoạn sẽ tạo ra một hình tiện có biên dạng vuông. 
* `Mật độ không đổi` - Khi bật, sẽ giữ cho các đa giác vuông vắn. Khi tắt, cho phép bạn đặt `Phân chia Y` dọc theo chiều dài của ống.
* `...` - Menu cài đặt Tiện.

#### Cài đặt Tiện {#lathe-settings}
* `Hình cơ bản` - Các nút cho phép bật/tắt UV, hoặc xác nhận ống.
* `Hậu phân chia` - Lối tắt để đặt cấp đa độ phân giải trước khi xác nhận.
* `Phân khu tuyến tính` - Lối tắt để đặt cấp phân chia tuyến tính trước khi xác nhận. 
* `Phân chia X` - Giống như Phân chia X trên thanh công cụ.
* `Phân chia Y` - Giống như Phân chia Y trên thanh công cụ.
* `Đường cong (Lặp lại)` - Chuyển biên dạng đường cong thành một [Bộ lặp đường cong](scene.md#curve)

### ![](/icons/tool_insert.webp) Chèn {#insert}
Đặt một đối tượng lên bề mặt của một đối tượng khác. Cách dùng tương tự công cụ Dấu Triện, nhưng dành cho các hình 3d hoàn chỉnh.

Nếu bạn chọn một hình cơ bản từ thanh công cụ bên trái, nhấp và kéo trên bất kỳ bề mặt nào sẽ đặt hình cơ bản tại chỗ bạn nhấp, còn thao tác kéo sẽ quyết định kích thước. Khi bạn kéo xong, Chèn sẽ chuyển sang chế độ [Biến Đổi](#transform).

Ở chế độ Thực thể, thao tác kéo sẽ tạo một thực thể mới và trượt nó trên bề mặt. Kích thước được sao chép từ hình đầu tiên, nhờ vậy bạn có thể đặt nhiều thực thể cùng kích thước của một đối tượng lên các bề mặt khác.

Bạn không chỉ chèn được hình cơ bản! Hãy chọn *bất kỳ* hình nào trong danh sách đối tượng, nếu Chèn đang ở chế độ Thực thể hoặc Nhân bản, bạn có thể kéo các bản sao của đối tượng đang chọn lên bất kỳ bề mặt nào khác.

Nếu một đối tượng có trục tùy chỉnh, trục đó sẽ được dùng làm điểm neo. Xem video bên dưới.

Thanh công cụ bên trái còn có `Xem`, để di chuyển máy ảnh mà không chèn gì, và `Đồng bộ`: khi đối tượng đích là thực thể, đối tượng mới cũng được thêm vào tất cả các thực thể khác.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Biến Đổi {#transform}
Di chuyển/Xoay/Thay đổi tỷ lệ mô hình trực tiếp bằng 1 hoặc 2 ngón tay, thường là trên bề mặt của một đối tượng khác.

Thanh công cụ bên trái có các nút sau:

* `Nhân bản` / `Thực thể` - Tạo một bản sao hoặc một thực thể của đối tượng, xem thanh công cụ [Gizmo](#left-menu-toolbar).
* `Di Chuyển` - Kéo bằng một ngón tay sẽ di chuyển đối tượng. Khi bật bám, thao tác này sẽ trượt đối tượng dọc theo bề mặt dưới ngón tay bạn.
* `Xoay` - Kéo bằng một ngón tay sẽ xoay đối tượng. Khi bật bám, đối tượng sẽ xoay quanh pháp tuyến của bề mặt dưới ngón tay bạn.
* `Tỷ lệ` - Kéo bằng một ngón tay sẽ thay đổi tỷ lệ đối tượng.

Một thanh công cụ ở phía trên khung nhìn có:

* `Mục tiêu` - Công cụ sẽ di chuyển đối tượng, nhóm của nó, hay các đỉnh của nó, giống như với [Gizmo](#left-menu-toolbar).
* `Snap` - Bám mô hình lên các bề mặt khác.
* `Bề mặt` / `Đỉnh` - Với `Snap`, bám lên bề mặt, hoặc lên đỉnh gần nhất.

Biến Đổi có thể dùng 2 chế độ này thật nhanh bằng 2 ngón tay:

* Kéo một đối tượng để đặt nó. Dừng di chuyển ngón tay thứ nhất, nhưng đừng nhấc nó khỏi màn hình.
* Chạm ngón tay thứ hai lên màn hình trong khi vẫn giữ ngón thứ nhất. Khi kéo ngón thứ hai, đối tượng sẽ thay đổi tỷ lệ.
* Nhấc ngón thứ hai lên, rồi tiếp tục kéo ngón thứ nhất, đối tượng sẽ trở lại chế độ di chuyển.

Bạn cũng có thể đổi chế độ thứ hai bằng cử chỉ chạm ngón tay thứ hai:

* Kéo đối tượng để đặt nó, dừng di chuyển, nhưng đừng nhấc ngón tay khỏi màn hình.
* Chạm ngón tay thứ hai trong khi vẫn giữ ngón thứ nhất
* Công cụ chuyển sang chế độ xoay. Kéo ngón thứ nhất để đặt góc xoay.
* Chạm ngón thứ hai như trước, công cụ sẽ chuyển lại chế độ di chuyển.

Đây là một quy trình nhanh để nhân bản các đối tượng lên một đối tượng khác, ví dụ rải đá trên một vùng địa hình. Lưu ý rằng nút nhân bản cũng nằm trên thanh công cụ bên trái để dễ truy cập:

* Dùng công cụ biến đổi để di chuyển một hòn đá vào vị trí.
* Buông tay, nhấn nút nhân bản
* Di chuyển hòn đá này, xoay/thay đổi tỷ lệ nếu cần
* Buông tay, nhấn nút nhân bản
* Di chuyển hòn đá này, và cứ thế lặp lại.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Công cụ này cho phép bạn di chuyển, xoay và thay đổi tỷ lệ đối tượng, cũng như thay đổi trục của đối tượng.

Tay cầm trong khung nhìn có các tính năng sau:

* `Di chuyển` - Kéo trên đường thẳng có mũi tên để di chuyển theo X/Y/Z. Kéo chấm màu hồng đào ở giữa gizmo để dịch chuyển tự do trong không gian màn hình. Nhấp vào các ô vuông đỏ, xanh lá, xanh dương để dịch chuyển trên các mặt phẳng X/Y/Z.
* `Xoay` - Kéo trên các vòng tròn đỏ/xanh lá/xanh dương để xoay theo X/Y/Z. Kéo khối cầu bên trong các vòng tròn để xoay tự do.
* `Tỷ lệ`- Kéo các chấm đỏ/xanh lá/xanh dương bên ngoài để thay đổi tỷ lệ theo X/Y/Z. Kéo các hình nón đỏ/xanh lá/xanh dương bên ngoài để thay đổi tỷ lệ trên các mặt phẳng X/Y/Z. Kéo vòng tròn màu hồng đào bên ngoài để thay đổi tỷ lệ đồng đều.

![](/images/tool_gizmo.webp)

#### Nút và đỉnh {#nodes-and-vertices}

Mỗi đối tượng trong Nomad được tạo thành từ một nút và các đỉnh:

* `Nút` - 'Tay cầm' của đối tượng, lưu trữ vị trí, góc xoay và tỷ lệ của nó, gọi là ma trận biến đổi.
* `Điểm đỉnh` - Các điểm xác định bề mặt của đối tượng, chúng lưu trữ thông tin vị trí và màu sơn.

Nếu bạn có một khối hộp đơn giản gồm 8 đỉnh, bạn có thể dịch chuyển nó bằng cách sửa ma trận biến đổi, hoặc bằng cách sửa vị trí các đỉnh. Khi điêu khắc, bạn thường muốn sửa các đỉnh, còn khi di chuyển đối tượng bằng gizmo, bạn thường muốn sửa nút. Nomad cho phép bạn làm cả hai. 

#### Các thanh công cụ của Gizmo {#left-menu-toolbar}

Thanh công cụ bên trái có:

* `Nhân bản` - Tạo một bản sao độc lập của đối tượng hiện tại, có thể kéo ra chỗ khác bằng gizmo.
* `Thực thể` - Tạo một bản sao dạng thực thể của đối tượng hiện tại. Các đối tượng được liên kết với nhau, nên những thay đổi điêu khắc trên một đối tượng sẽ xuất hiện trên tất cả các thực thể.
* `Trục` - (Biểu tượng ổ khóa, ở vị trí của nút `Trừ`) Khi bật, bạn có thể di chuyển và xoay gizmo mà không làm di chuyển đối tượng. Giống như `Trừ`, hãy giữ để đổi nhanh, hoặc chạm để giữ nó bật.

Một thanh công cụ ở phía trên khung nhìn chứa các điều khiển còn lại:

* `Mục tiêu` - Đặt gizmo sẽ tác động lên nút hay các đỉnh của đối tượng:
    * `Tự động` - Mặc định, hoạt động giống như `Nhóm`, nhưng nếu lưới có mặt nạ hoặc đối xứng đang bật, nó hoạt động giống như `Đỉnh`.
    * `Đỉnh` - Áp dụng phép biến đổi lên các đỉnh, có tính đến mặt nạ và đối xứng. Nó không hoạt động trên các hình cơ bản chưa xác nhận, và các thực thể cũng bị ảnh hưởng.
    * `Đối tượng` - Chỉ di chuyển đối tượng hiện tại, bỏ qua đối xứng và mặt nạ. Các đối tượng con vẫn đứng yên.
    * `Nhóm` - Di chuyển đối tượng cùng phần còn lại của cây phân cấp của nó, bỏ qua đối xứng và mặt nạ.
    * `Thực thể` - (Đối tượng và Nhóm) Giống như trên, nhưng mọi thực thể của đối tượng cũng di chuyển theo.
* `Trục` - Một cửa sổ bật lên để đặt trục nhanh, được giải thích [bên dưới](#pivot).
* `Tất cả` / `Di chuyển` / `Xoay` / `Tỷ lệ` - Hiển thị tất cả tay cầm của gizmo, hoặc chỉ các tay cầm di chuyển, xoay hoặc tỷ lệ.
* `Ghim` - Mặc định gizmo sẽ di chuyển đến trục của đối tượng được chọn. Khi bật ghim, gizmo sẽ ở yên tại vị trí hiện tại.
* `Căn Chỉnh` - Chuyển đổi giữa trục được căn theo đối tượng hiện tại, hoặc được căn theo thế giới.
* `Snap` (xoay) - Bật làm tròn giá trị xoay theo bước, giá trị bước được hiển thị và có thể chỉnh khi bật snap. Tùy chọn `Nam châm` của nó khiến góc xoay dính vào một bước khi đi qua, rồi lại xoay tự do; tắt nó đi để nhảy từ bước này sang bước khác.
* `Snap` (dịch chuyển) - Bật làm tròn giá trị dịch chuyển theo bước, giá trị bước được hiển thị và có thể chỉnh khi bật snap.

#### ![](/icons/reset.webp) Trục {#pivot}
Cửa sổ bật lên `Trục` trên thanh công cụ phía trên cho phép thay đổi trục nhanh chóng. Vị trí và hướng của trục quyết định gizmo.

**Đặt lại** 
* `Tự động` - Tâm của đối tượng, căn theo phép biến đổi của nó.
* `Giữa` - Di chuyển trục đến tâm của đối tượng, giữ nguyên hướng.
* `Đáy` - Di chuyển trục đến tâm đáy của đối tượng. Chạm lần nữa để dùng hộp bao theo thế giới.
* `Trên` - Di chuyển trục đến tâm đỉnh của đối tượng. Chạm lần nữa để dùng hộp bao theo thế giới.
* `Đối tượng` - Di chuyển trục đến gốc của đối tượng, căn theo phép biến đổi của nó.
* `Mặt nạ` - Di chuyển trục đến tâm của vùng không có mặt nạ. Chạm lần nữa để chuyển sang vùng có mặt nạ.
* `Căn chỉnh` - Đặt lại góc xoay để căn theo thế giới, giữ nguyên vị trí.
* `Góc nhìn` - Căn trục theo góc nhìn hiện tại, giữ nguyên vị trí. Sau đó nó không đi theo máy ảnh nữa.

**Chạm một lần (chế độ Trục)**

Chỉ hoạt động khi `Trục` đang bật, nó quyết định điều gì xảy ra khi bạn chạm một lần lên bề mặt lưới:
* `Không có` - Không làm gì khi chạm vào đối tượng
* `Pháp tuyến` - Di chuyển và xoay trục để căn theo điểm được chạm trên bề mặt
* `Đầu tiên` - Di chuyển (nhưng không xoay) trục đến điểm được chạm trên bề mặt
* `Giữa` - Di chuyển trục vào giữa đối tượng, ngay dưới điểm được chạm trên bề mặt.

#### Cài đặt Gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

* `Gọn gàng` - Chuyển bố cục gizmo để đặt các tay cầm phụ bên ngoài hoặc bên trong khối cầu xoay
* `Kích thước Gizmo` - Kích thước của gizmo
* `Độ dày` - Kích thước các đường nét trên gizmo
* `Độ mờ đục` - Độ mờ đục của gizmo
* `Ẩn khi tương tác` - Bật/tắt việc tạm ẩn gizmo khi đang kéo nó

-----

* `Ngưỡng lăn tiếp tuyến` - Điều khiển cách giao diện xoay hoạt động khi kéo các tay cầm vòng tròn để xoay theo X/Y/Z. Nếu giá trị này là 0, việc xoay hoạt động như một núm vặn, hãy kéo gizmo theo vòng tròn. Nếu giá trị này là 90, việc xoay hoạt động như kéo sợi dây của con yo-yo; kéo theo đường thẳng lại gần hoặc ra xa điểm bạn nhấp đầu tiên. Các giá trị từ 0 đến 90 sẽ kết hợp cả hai; dưới giá trị đó là chuyển động thẳng, trên giá trị đó là chuyển động tròn.
* `Nhập số` - Khi bật, chạm một lần vào gizmo sẽ mở một cửa sổ để nhập giá trị chính xác cho trục của tay cầm được chạm.

::: warning
Các công cụ [Gizmo](#gizmo) và [Biến Đổi](#transform) dùng ô đánh dấu đối xứng riêng, tách biệt với đối xứng khi điêu khắc!

Mặc định đối xứng này bị tắt.
:::

##### Ma trận {#matrix}
Các giá trị biến đổi chính xác của đối tượng không còn nằm trong cài đặt Gizmo nữa: chúng đã được chuyển sang menu `Biến Đổi`, ở menu góc trên bên phải. Phần `Ma trận` của menu này có:

* ![](/icons/target.webp) `Di chuyển về gốc` - Di chuyển đối tượng sao cho trục của nó nằm ở tâm của cảnh, gọi là gốc tọa độ.
* ![](/icons/bake.webp)  `Bake` - Cố định đối tượng tại vị trí hiện tại, và đặt các giá trị dịch chuyển/xoay về 0, tỷ lệ về 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Trục` - Bake trục: làm cho các giá trị ma trận tương ứng với vị trí của tay cầm gizmo trong thế giới.
* ![](/icons/reset.webp) `Thiết lập lại` - Lối tắt đặt các giá trị dịch chuyển về 0, góc xoay về 0, tỷ lệ về 1, làm di chuyển và xoay đối tượng.

::: tip Bake và bake theo trục
Tạo một khối hộp, chọn công cụ Gizmo, mở và ghim menu `Biến Đổi`. Mặc định giá trị dịch chuyển và xoay là 0, tỷ lệ là 1.

Bật chế độ trục, di chuyển tay cầm sang một bên, rồi tắt chế độ trục. Trục đã thay đổi, nhưng hãy để ý rằng giá trị dịch chuyển vẫn là 0. 

Nếu bạn muốn xem trục *thực sự* nằm ở đâu, hãy nhấp nút bake `Trục`. Giờ các giá trị dịch chuyển mới được cập nhật. Lưu ý rằng khối hộp không hề di chuyển trong thao tác này, cũng như trong chế độ trục.

Di chuyển và xoay khối hộp đến một chỗ nào đó, rồi chạm `Di chuyển về gốc`. Nó di chuyển đối tượng sao cho trục nằm ở tâm thế giới, nhưng giữ nguyên góc xoay.

Nhấp `Thiết lập lại`, và góc xoay cũng sẽ được đặt về 0.

Di chuyển và xoay khối hộp lần nữa, lần này nhấp `Bake`. Trục ở nguyên chỗ cũ, khối hộp cũng ở nguyên chỗ cũ, nhưng các giá trị dịch chuyển và xoay được đặt về 0.

Hãy luyện tập vài lần! Bạn sẽ hiểu rằng các giá trị của trục được ẩn đi, Nomad lo việc đó cho bạn, nhưng nếu bạn cần đặt trục vào những vị trí thực trong không gian, bake trục sẽ làm điều đó cho bạn.

:::

* `Dịch chuyển` - Các giá trị dịch chuyển X, Y, Z
* `Xoay` - Các giá trị xoay X, Y, Z
* `Tỷ lệ` - Tỷ lệ đồng nhất nếu tùy chọn đó được bật, hoặc tỷ lệ X, Y, Z nếu bị tắt.
* `Xiên` - Các giá trị xiên (shear) X, Y, Z, chỉ hiển thị khi đối tượng đã bị xiên
* `Tỷ lệ đồng nhất` - Bật/tắt khả năng thay đổi tỷ lệ đồng đều hoặc độc lập trên từng trục

Ở bên trái, bạn có thể di chuyển trục của gizmo, hãy xem video bên dưới để thấy cách hoạt động.
Điều này đặc biệt hữu ích cho phép xoay, vì nó không thay đổi gì với phép dịch chuyển.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Nhóm mặt {#facegroup}

Nhóm mặt cho phép bạn sắp xếp đối tượng thành các mặt có màu khác nhau. Bạn có thể dùng các nhóm này theo nhiều cách trong Nomad:

* Một cách chọn nhanh để tạo mặt nạ
* Ẩn/hiện các phần của đối tượng
* Sắp xếp đối tượng mà không cần tách nó thành các phần riêng biệt
* Xác định các vùng UV
* Hướng dẫn quad remesher
* Thêm khả năng điều khiển cho các công cụ như Làm mịn.

#### Thanh công cụ bên trái của Nhóm mặt {#facegroup-left-toolbar}

* `Nhóm` - Nút này hiển thị nhóm mặt hiện tại. Chạm vào để hiển thị các nhóm mặt có sẵn dưới dạng ô màu và chọn một nhóm. Chạm vào một ô để đổi tên, đổi màu hoặc xóa nó. `Xóa Không Dùng` xóa các ô không được dùng, `Đặt lại` xóa tất cả. Biểu tượng dấu cộng cho phép bạn tạo ô mới.
* `Điểm` - Vẽ lên đối tượng để xác định các nhóm mặt. Khi bật '+ Nhóm mặt', mỗi nét vẽ mới sẽ tự động tạo một nhóm mặt mới, hữu ích để chia vùng nhanh chóng. Chạm một lần sẽ tô kín vùng được chọn. Thanh trượt đặt bán kính của điểm.
* `Thư giãn` - Làm mịn đường biên của các nhóm mặt. Rất hữu ích để tạo các cạnh gọn gàng cho quad remesh, hoặc để xác định các tấm cho mô hình bề mặt cứng (hard surface). Các thanh trượt điều khiển bán kính và cường độ của thao tác thư giãn.
* Hình dạng - Tạo nhóm mặt bằng hình dạng thay vì cọ, qua `Khóa + bán kính`, `Dây thòng lọng`, `Đa giác`, `Đường thẳng`, `Hình chữ nhật` và `Hình elip`. Xem [Điều khiển vùng chọn](#selection-controls) để biết thêm.
* `Chọn` - Chế độ phụ. Khi bật, nó sẽ lấy ô màu tại chỗ nét vẽ bắt đầu, và áp dụng ô đó cho phần còn lại của nét vẽ. Rất hữu ích để chỉnh gọn các vùng nhóm mặt; nếu một nhóm mặt lan quá xa, hãy bật `Chọn`, bắt đầu nét vẽ từ chỗ ô nhóm mặt đang đúng, và kéo đến đường biên để gán lại đúng ô.

#### Thanh công cụ phía trên của Nhóm mặt {#facegroup-top-toolbar}

Một thanh công cụ ở phía trên khung nhìn có các điều khiển bổ sung:

* `Thư giãn (Tất cả)` - Kéo để thư giãn đường biên của tất cả các nhóm mặt cùng lúc.
* `Mặt trước` / `Có thể thấy` / `Đã kết nối` - Các bộ lọc nét vẽ giống như trên thanh công cụ của [Mặt nạ](#mask).
* `Từ pháp tuyến` - Tạo nhóm mặt dựa trên góc giữa các mặt. Cửa sổ bật lên có `Góc`, và cho phép bạn bỏ qua các nhóm nhỏ dựa trên `Số lượng mặt` hoặc `Diện tích bề mặt`, kèm `Xem trước` trước khi bạn xác nhận.
* `Từ các phần` - Tạo một nhóm mặt cho mỗi phần rời nhau.
* `Từ UV` - Tạo một nhóm mặt cho mỗi đảo UV.
* `Từ mặt nạ` - Tạo một nhóm mặt từ vùng có mặt nạ.
* `Chạm đơn` - Chọn điều gì xảy ra khi chạm vào một nhóm mặt: tô nó bằng nhóm mặt hiện tại, ẩn nó, che mặt nạ nó, hoặc tạo `Tư thế` cho nó (nhóm được chạm và phần nằm phía sau nó được gỡ mặt nạ, và gizmo được đặt tại khớp nối, với thanh trượt `Làm mờ` cho mặt nạ). Một nút `Chạm đơn` thứ hai, có khi lưới đang có mặt nạ, giới hạn thao tác chạm vào các mặt nằm cùng phía của mặt nạ.
* Các nút `Xóa` cho công cụ [Ẩn](#hide) và [Mặt nạ](#mask), để hiện lại mọi thứ hoặc xóa mặt nạ mà không cần rời công cụ.

#### Cài đặt Nhóm mặt {#facegroup-settings}

Menu `Công cụ` chiết xuất các nhóm mặt thành đối tượng mới, với các tùy chọn giống như `Chiết xuất` trong [Cài đặt Mặt nạ](#mask-settings). Nút `Nhóm mặt` ở phía trên chọn những nhóm nào được chiết xuất, và có thêm thanh trượt `Khe hở`: nó dời từng đường biên vào trong dọc theo bề mặt, giá trị âm sẽ dời ra ngoài để chồng lên nhau. Với các tấm nằm cạnh nhau, hãy dùng một nửa khe hở mong muốn.

### ![](/icons/tool_hide.webp) Ẩn {#hide}
Ẩn hoặc tách riêng các phần của đối tượng. 

Các chế độ chính được điều khiển từ menu bên trái:

* `Điểm` - Quét cọ lên đối tượng để ẩn các phần của nó.
* Hình dạng -  Ẩn bằng hình dạng thay vì cọ, qua `Dây thòng lọng`, `Đa giác`, `Đường thẳng`, `Hình chữ nhật` và `Hình elip`. Xem [Điều khiển vùng chọn](#selection-controls) để biết thêm.
* `Hiển thị` - Chế độ phụ, đảo ngược thao tác, để chế độ đang chọn sẽ hiện thay vì ẩn các phần của đối tượng.

Một thanh công cụ sẽ xuất hiện ở phía trên khung nhìn với các điều khiển bổ sung:

* `Xóa tất cả` - Khôi phục các đối tượng, mọi phần bị ẩn sẽ được hiện lại. Khi các đối tượng khác cũng có phần bị ẩn, một nút `Xóa` bổ sung chỉ khôi phục các đối tượng đang chọn.
* `Đảo ngược` - Hoán đổi phần bị ẩn và phần không bị ẩn.
* `Xóa` - Xóa phần bị ẩn của đối tượng
* `Tách` - Tách phần bị ẩn của đối tượng thành một hình mới.
* `Mặt trước` / `Có thể thấy` / `Đã kết nối` - Các bộ lọc nét vẽ giống như trên thanh công cụ của [Mặt nạ](#mask).
* `Chạm đơn` (nhóm mặt) - Dùng nhóm mặt để ẩn nhanh các phần, chạm vào một nhóm mặt sẽ ẩn toàn bộ nhóm mặt đó.
* `Chạm đơn` (mặt nạ) - Nếu có mặt nạ, chạm vào sẽ ẩn phần có mặt nạ.

### ![](/icons/tool_measure.webp) Đo {#measure}
Kéo để đo khoảng cách giữa 2 điểm. Khi đã đặt xong, bạn có thể kéo các điểm đầu mút để điều chỉnh phép đo.

Thanh công cụ bên trái chọn cách đo khoảng cách:

* `Đường thẳng` - Một đường thẳng giữa hai điểm.
* `Bề mặt` - Khoảng cách dọc theo bề mặt, theo đường cắt đi qua hai điểm khi nhìn từ máy ảnh.
* `Mặt cắt` - Chu vi của mặt cắt đi qua hai điểm, giống như dùng thước dây đo vòng quanh cánh tay.
* `Đỉnh` - Bám các điểm đầu mút vào đỉnh gần nhất.
* `Tỷ lệ vàng` - Hiển thị một chấm vàng tại điểm tỷ lệ vàng của phép đo.
* Nút `?` hiển thị thể tích, diện tích bề mặt và kích thước của các đối tượng được chọn.

### ![](/icons/tool_arrange.webp) Sắp xếp {#arrange}
Xếp thẳng hàng và bố trí nhiều đối tượng cùng lúc, giống như các công cụ căn chỉnh của một ứng dụng thiết kế 2d. Hãy chọn các đối tượng trước; với một đối tượng duy nhất, Sắp xếp sẽ làm việc trên các phần rời của nó. Một khung được vẽ bao quanh vùng chọn, kéo các tay cầm của khung để thay đổi tỷ lệ.

Một thanh công cụ ở phía trên khung nhìn có các điều khiển:

* `Thế giới` / `Màn hình` - Sắp xếp theo các trục của thế giới, hoặc theo màn hình (trái, phải, trên, dưới).
* `Căn Chỉnh` - Căn các đối tượng theo mép nhỏ nhất, tâm hoặc mép lớn nhất của chúng, trên từng trục.
* `Phân bố` - Giãn các đối tượng đều nhau giữa hai đối tượng ngoài cùng, theo mép nhỏ nhất, tâm hoặc mép lớn nhất. Cần ít nhất 3 đối tượng.
* `Đường thẳng` - Xếp các đối tượng thành một hàng dọc theo một trục.
* `Lưới` - Xếp các đối tượng thành lưới, với số đối tượng theo `X`, `Y` và `Z`.
* `Hình tròn` - (Chỉ với Thế giới) Xếp các đối tượng thành vòng tròn quanh trục `X`, `Y` hoặc `Z`.
* `Hình cầu` - (Chỉ với Thế giới) Xếp các đối tượng phủ trên một hình cầu.

`Đường thẳng`, `Lưới`, `Hình tròn` và `Hình cầu` đều có thanh trượt `Khoảng cách` cho khoảng hở giữa các đối tượng.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Công cụ này sẽ chuyển đối tượng được chọn thành bố cục tô pô tứ giác gọn gàng, với các điều khiển cho mật độ, luồng cạnh và đối xứng. 

::: tip
Quad Remesher được [Exoside](https://exoside.com/) phát triển cho iOS và máy tính. 

Trên iOS, đây là một gói mua trong ứng dụng Nomad, thanh toán một lần 16 USD.

Trên máy tính, hãy mua giấy phép từ [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Bạn có thể mua giấy phép chỉ cho Nomad trên máy tính, hoặc giấy phép chéo cho tất cả các ứng dụng máy tính được hỗ trợ.

Nếu bạn đã sở hữu Quad Remesher cho một ứng dụng máy tính khác, bạn có thể [mua bản nâng cấp cho tất cả nền tảng với chi phí thấp hơn.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher không có trên Android. Android có thể dùng các công cụ remesh mã nguồn mở miễn phí trong thẻ tô pô [Tái định hình tứ giác](topology.md#quad-remesh) (AutoRemesher, Instant Mesh, QuadriFlow), nhưng hãy hiểu rằng bộ tính năng của chúng hạn chế hơn.
:::

Cho đến khi Quad Remesher được mở khóa, thanh công cụ phía trên bắt đầu bằng một nút giỏ hàng thay vì các nút remesh. Trên iOS, nút này mở giao dịch mua trong ứng dụng. Trên máy tính, nó hiển thị `Mở khóa (mua, khôi phục, thử nghiệm)`, dùng để kiểm tra giấy phép Exoside của bạn (hoặc bắt đầu dùng thử). Khi đã kích hoạt, thanh công cụ bên trái và phía trên sẽ được bật.

* `Điểm` - Cọ này đặt mật độ mục tiêu. Cường độ 100% sẽ vẽ màu đỏ, dùng gấp đôi mật độ tứ giác mục tiêu ở những vùng đó. Cường độ 0% sẽ vẽ màu lục lam, dùng một nửa mật độ tứ giác mục tiêu ở những vùng đó. Cường độ 50% sẽ vẽ màu xám, dùng mật độ tứ giác mục tiêu mặc định.
* `Làm mịn` - Làm mịn các vùng chuyển tiếp mật độ đỏ/xám/lục lam.
* `Bôi nhòe` - Bôi nhòe phần vẽ mật độ.
* `Đường Cong` - Phác thảo các đường cong trên bề mặt bản điêu khắc, quad remesher sẽ dùng chúng làm đường dẫn cho luồng cạnh. Chạm vào một đường cong để xóa nó.
* `Đường dẫn` - Vẽ các đường dẫn trên bề mặt bản điêu khắc, quad remesher sẽ dùng chúng làm đường dẫn cho luồng cạnh. Chạm vào một đường dẫn để xóa nó. 
* `Hình chữ nhật` - Vẽ các hình chữ nhật trên bề mặt bản điêu khắc, quad remesher sẽ dùng chúng làm đường dẫn cho luồng cạnh. Chạm vào một đường dẫn để xóa nó.
* `Hình elip` - Vẽ các hình elip trên bề mặt bản điêu khắc, quad remesher sẽ dùng chúng làm đường dẫn cho luồng cạnh. Chạm vào một đường dẫn để xóa nó.

#### Thanh công cụ phía trên của Quad Remesher {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

Một thanh công cụ sẽ xuất hiện ở phía trên khung nhìn với các điều khiển bổ sung:


* `<Count>` - Nhấp vào đây để bắt đầu quá trình quad remesh, con số này cho biết số tứ giác mục tiêu sẽ là bao nhiêu.
* `Tứ giác` - Đặt số tứ giác mục tiêu bằng cách trượt sang trái và phải, hoặc chạm để nhập một số chính xác. Lưu ý rằng đây chỉ là con số định hướng chứ không cố định, các điều khiển khác nhau của quad remesher thường khiến kết quả không khớp chính xác với mục tiêu này.
* `Một Nửa` - Lối tắt để đặt số mục tiêu bằng một nửa số đa giác hiện tại.
* `Giống Nhau` - Lối tắt để đặt số mục tiêu bằng số đa giác hiện tại.
* `Hướng Dẫn` - Bật/tắt để dùng hoặc bỏ qua các đường dẫn. Khi có đường dẫn, một nút `Hướng Dẫn` thứ hai hiển thị số lượng của chúng, chạm vào để xóa tất cả.
* `Mật Độ` - Bật/tắt để dùng hoặc bỏ qua phần vẽ mật độ. Khi có phần vẽ mật độ, một nút `Mật Độ` thứ hai sẽ xóa nó.
* `Nhóm mặt` - Bật/tắt để dùng hoặc bỏ qua các nhóm mặt trong việc định hướng quad remesher.
* `Thư giãn` - Bật/tắt để tự động thư giãn đường biên nhóm mặt trong khi quad remesh. Nếu bạn đã thư giãn/làm mịn đường biên nhóm mặt rồi, hãy tắt tùy chọn này.
* `Thanh trượt Thư giãn` - Thanh trượt lối tắt để thư giãn đường biên nhóm mặt.
* `Cạnh cứng` - Bật/tắt để cố gắng giữ lại các cạnh cứng.
* `Chiếu lại Điểm Đỉnh` - Bật/tắt để chiếu lại bố cục mới lên lưới đầu vào.
* `Đối Xứng` - Bật/tắt để có kết quả đối xứng. Lưu ý rằng đối xứng luôn được tính quanh trục x của thế giới, vì vậy hãy đảm bảo mô hình nằm ở gốc tọa độ nếu bạn muốn có kết quả đối xứng.
* `...` - Cửa sổ cài đặt Quad Remesher. 

#### Menu cài đặt Quad Remesher {#quad-remesher-settings-menu}

Nút `...` ở cuối thanh công cụ phía trên mở một cửa sổ chứa các cài đặt còn lại:

* `Số Lượng Tứ Giác Thích Ứng` - Bật/tắt việc dùng tứ giác nhỏ hơn ở vùng có độ cong cao, và tứ giác lớn hơn ở vùng có độ cong thấp.
* `Kích Thước Thích Ứng` - Đặt mức độ thích ứng. 100% cho phép kích thước thích ứng tối đa, ở 0% các tứ giác sẽ đồng đều.

::: tip

Công thức để có một lần quad remesh tốt với ít lỗi nhất:

* Chia nhóm mặt cho lưới để xác định luồng tứ giác lý tưởng của bạn.
* Thư giãn nhóm mặt để có đường biên nhóm mặt mượt.
* Tinh giảm. Bước này đảm bảo không có mặt nào mỏng hoặc bị méo ở mép nhóm mặt. Trong cài đặt tinh giảm, hãy đảm bảo nhóm mặt được bật. Nhờ đó các cạnh tam giác sẽ đi theo chính xác các cạnh nhóm mặt của bạn. 

Trong các tùy chọn quad remesh, hãy đảm bảo thư giãn bị tắt (vì bạn đã thư giãn lưới rồi) và bạn sẽ có kết quả tốt.

:::

### ![](/icons/tool_select.webp) Chọn {#select}
Dùng các chế độ hình dạng (`Dây thòng lọng`, `Hình chữ nhật`, `Hình elip`) để chọn các đối tượng trong cảnh. `Bỏ chọn` sẽ loại các đối tượng khỏi vùng chọn.

### ![](/icons/tool_lattice.webp) Lattice {#lattice}
Biến dạng một đối tượng bằng một lồng điểm điều khiển bao quanh nó, thay vì điêu khắc bề mặt. Di chuyển vài điểm của lồng sẽ uốn cong, vặn xoắn hoặc kéo giãn toàn bộ đối tượng một cách mượt mà, rất hợp để chỉnh tỷ lệ hoặc tạo dáng mà không động đến tô pô. Biến dạng vẫn có thể chỉnh sửa cho đến khi bạn xác nhận.

Thanh công cụ bên trái chọn cách bạn chỉnh sửa lồng:

* `Điểm` - Kéo trực tiếp các điểm và cạnh của lồng. Chạm vào một điểm để chọn nó.
* `Xem` - Di chuyển máy ảnh mà không chỉnh sửa lồng.
* `Thư giãn` - Một cọ làm thư giãn các điểm của lồng nằm dưới nó.
* `Đàn hồi` - Một cọ kéo các điểm của lồng với độ suy giảm đàn hồi, giống như công cụ [Đàn hồi](#elastic).
* `Gizmo` - Di chuyển, xoay và thay đổi tỷ lệ các điểm được chọn bằng gizmo. Chế độ phụ của nó là `Trục`.
* `Dây thòng lọng` - Chọn các điểm của lồng bằng dây thòng lọng, `Bỏ chọn` sẽ loại chúng khỏi vùng chọn.

Cửa sổ hình dạng còn có `Bán kính mềm`, cho phép thao tác kéo điểm làm di chuyển cả các điểm lân cận (tính theo ô lưới, 0 chỉ di chuyển vùng chọn), và `Đảo ngược lựa chọn`.

Một thanh công cụ ở phía trên khung nhìn có:

* `Hoàn tất` - Áp dụng biến dạng lên đối tượng và xóa lồng.
* `Đặt lại` - Xóa lồng cùng biến dạng của nó.
* `Độ mờ đục` - Độ mờ đục khi hiển thị lồng.
* `Mặt gương` - Khi dùng đối xứng, chuyển vòng giữa các phía gương của lồng được hiển thị và có thể chọn, với `Độ mờ đục` riêng cho phía bị ẩn.
* `Điểm lưới` - Những điểm nào của lồng có thể di chuyển: toàn bộ lưới, bề mặt và điểm trung tâm, hoặc chỉ bề mặt.
* `Độ cứng` - Mức độ cứng của biến dạng, từ mềm mại (0%) đến cứng và tuyến tính (100%).
* `Độ suy giảm` - Biến dạng giảm dần xa đến đâu bên ngoài lồng.
* `Căn Chỉnh` - Căn lồng theo đối tượng, hoặc theo thế giới.
* `X`, `Y`, `Z` `Phân chia` - Số ô của lồng trên mỗi trục. Nút chế độ bên cạnh quyết định cách chúng liên hệ với nhau: `x = y = z` dùng cùng một số trên cả 3 trục, `Đồng nhất` giữ khoảng cách giữa các điểm như nhau trên mọi trục, và `Tùy chỉnh` cho phép bạn đặt tự do từng trục.

#### Cài đặt Lattice {#lattice-settings}
* `Tốc độ xoay` - Các tùy chọn xoay giống như công cụ [Di chuyển](#move-settings), dùng khi kéo các điểm của lồng.

### ![](/icons/tool_view.webp) Xem {#view}
"Công cụ" này không làm gì đặc biệt, nó đơn giản là cách để xem mô hình mà không làm thay đổi cảnh của bạn.

#### Cài đặt Xem {#view-settings}
Khi công cụ Xem đang hoạt động, các cài đặt này sẽ ghi đè một số tùy chọn hiển thị, để bạn có được góc nhìn gọn gàng khi trình bày hoặc kiểm tra mô hình:

* `Hình cơ bản (Chỉnh sửa)`, `Lặp lại (Chỉnh sửa)`, `Ánh sáng (Chỉnh sửa)`, `Máy ảnh (Chỉnh sửa)` - Cho phép chỉnh sửa hình cơ bản, bộ lặp, đèn và máy ảnh trong khung nhìn khi đang ở công cụ Xem. Tắt chúng để tránh vô tình di chuyển các tay cầm của chúng.
* `Phím tắt camera (luôn luôn)` - Luôn hiển thị các nút phím tắt máy ảnh trên khung nhìn.
* `Hiển thị mặt nạ`, `Bao viền`, `Làm tối các đối tượng không được chọn` - Hiển thị mặt nạ, đường viền của các đối tượng được chọn, hoặc làm tối các đối tượng không được chọn. `Tự động` theo cài đặt thường dùng của bạn, `Không` và `Có` thì ép buộc.
* `Hiển thị đường (Đối xứng)`, `Hiển thị mặt phẳng (Đối xứng)` - Hiển thị đường hoặc mặt phẳng đối xứng, với cùng các lựa chọn `Tự động`, `Không` và `Có`.
* `Biểu tượng` - Hiển thị biểu tượng của các nhóm, bộ lặp, đèn, máy ảnh và cây phân cấp trong khung nhìn, với cùng các lựa chọn.


## Menu ngữ cảnh của hộp công cụ {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Nhấp chuột phải hoặc nhấn giữ một công cụ trong hộp công cụ sẽ mở ra một menu ngữ cảnh. Menu này có các tùy chọn sau:

* `Lưu` - Lưu mọi thay đổi bạn đã thực hiện với công cụ
* `Nhân bản` - Nhân bản công cụ thành một lối tắt công cụ mới
* `Lưu lần cuối` - Quay về phiên bản đã lưu trước đó của công cụ
* `Biểu tượng` - Đổi biểu tượng của công cụ. Khi công cụ có biểu tượng tùy chỉnh, nút này sẽ xóa nó.
* `→ ...` - Chuyển công cụ vào một thư mục khác của hộp công cụ, hoặc một thư mục mới
* `Đặt lại` - Đặt lại công cụ về mặc định

Các công cụ đã nhân bản còn có `Đổi tên` và `Xóa`.
