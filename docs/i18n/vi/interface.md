# ![](/icons/sliders.webp) Menu Giao diện {#interface-menu}

Menu này chứa nhiều tùy chọn để tùy biến giao diện của Nomad.

![](/images/interface_overview2.webp)

Nomad có thể tùy biến khá sâu, menu này được chia thành 5 thẻ: Giao diện, Phím tắt, Cử chỉ, Ràng buộc, Gỡ lỗi.

![](/images/interface_menu.webp)


::: tip
Trang này nói về menu Giao diện, không phải bản thân giao diện! Giao diện tổng thể được mô tả trong [Bắt đầu](gettingstarted.md).
:::

## ![](/icons/sliders.webp) Giao diện {#interface}

Thẻ Giao diện điều chỉnh màu sắc, kích thước và bố cục của giao diện người dùng Nomad. Nó có hai thẻ con, `Diện mạo` và `Bố cục`.

![](/images/interface_overview3.webp)

### ![](/icons/palette.webp) Màu sắc {#presets}

![](/images/interface_presets.webp)

Thẻ con `Diện mạo` bắt đầu bằng một bộ màu cài đặt sẵn cho giao diện. Chạm vào một bộ để áp dụng, rồi tinh chỉnh bằng các tùy chọn bên dưới.

#### Nhấn và Nền tảng {#color-widgetcolor-base}
Các màu chính của giao diện: `Nhấn` cho nút đang chọn và thanh trượt, `Nền tảng` cho các bảng.

#### Độ đục chữ {#text-opacity}
Làm dịu chữ và biểu tượng trên nền các bảng.

#### Nút bật/tắt, Ô chọn, Thẻ {#high-contrast-button}
Kiểu của nút bật/tắt (`Mềm` hoặc `Đặc`), của ô chọn (`Bao viền`, `Nhấn` hoặc `Tô`) và của thẻ (`Gạch chân`, `Mềm` hoặc `Đặc`).

#### Công cụ có màu {#colored}
Tô màu biểu tượng theo nhóm, ví dụ mọi công cụ mặt nạ có màu nâu, công cụ cắt tách màu đỏ, công cụ làm phẳng màu xanh lá, v.v.

#### Bóng bảng {#material-color-preview}
Các bảng đổ bóng để nổi bật trên nền cảnh.

#### Bảng điều khiển trong suốt {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Khi bật, sẽ xuất hiện thêm tùy chọn để điều chỉnh giao diện của menu và bảng trong Nomad: `Màu bảng` đặt màu của chúng, `Độ mờ` quyết định cảnh phía sau bị làm mờ đến mức nào, và `Kính` thêm hiệu ứng khúc xạ ở viền cùng ánh phản chiếu, thấy rõ nhất khi độ mờ thấp.

::: tip
Trên thiết bị nhỏ, bạn nên đặt màu bảng gần như trắng, trong suốt và độ mờ thấp, để menu không che khuất cảnh.
:::

#### ![](/icons/reset.webp) Đặt lại diện mạo {#reset-style}
Đưa mọi tùy chọn diện mạo về giá trị mặc định.

### ![](/icons/panel_detach.webp) Bố cục {#layout}

Thẻ con `Bố cục` quyết định vị trí và kích thước của các thành phần.

#### Hộp công cụ {#toolbox}

Tùy chọn cho menu công cụ ở bên phải giao diện Nomad.

![](/images/interface_toolbox.webp)

##### ![](/icons/resize_bottom_right.webp) Thay đổi kích thước {#ui-resize-corner}

Bật/tắt tay nắm thay đổi kích thước ở góc dưới của hộp công cụ.

##### Ẩn {#hidden}
Thông thường, biểu tượng hộp công cụ trên thanh trên cùng sẽ chuyển giữa một cột dài duy nhất và danh sách công cụ nhiều cột. Tùy chọn này khiến nó chuyển giữa danh sách nhiều cột và trạng thái ẩn.

##### Đặt lại thứ tự {#reset-order}
Đưa các công cụ mặc định trong hộp công cụ về thứ tự ban đầu. Các biểu tượng tùy chỉnh vẫn nằm trong hộp công cụ, ở cuối danh sách.

#### Khu vực trên {#rows-auto-1}
`Đáp ứng` chọn cách thanh trên cùng xử lý khi không vừa màn hình, chủ yếu liên quan đến màn hình nhỏ: `Nhiều dòng` xếp các menu thành nhiều dòng, `Cuộn` giữ một dòng mà bạn có thể cuộn.

#### Phản chiếu thanh trên cùng {#mirror-top-bar}
Đảo ngược thứ tự các menu trên thanh trên cùng.

#### Phản chiếu thanh bên {#mirror-side-bars}
Đổi chỗ các thanh bên, để hộp công cụ nằm bên trái còn tùy chọn công cụ nằm bên phải.

#### Phản chiếu thanh dưới cùng {#mirror-bottom-bar}
Chuyển thanh dưới cùng sang góc dưới bên phải và đảo ngược thứ tự các nút.

#### ![](/icons/move.webp) Kéo bảng {#drag-panel}
Một bảng nổi luôn có thể di chuyển bằng cách kéo thanh tiêu đề của nó, tùy chọn này cho phép bạn kéo cả phần thân. Ở chế độ `Tự động`, ngón tay hoặc bút chỉ di chuyển bảng khi thao tác kéo theo chiều ngang nhiều hơn chiều dọc, nên kéo dọc vẫn cuộn được nội dung. Đặt thành `Có` để kéo được cả bằng chuột, theo mọi hướng.

#### ![](/icons/pencil.webp) Sử dụng Hộp Thoại của Nomad {#use-nomad-dialog}
Hiển thị hộp thoại nhập văn bản riêng của Nomad thay vì hộp thoại của hệ thống khi bạn nhập tên hoặc giá trị.

#### ![](/icons/stylus.webp) Chấm khi rê bút {#hover-dot}
Hiển thị một chấm nhỏ trên giao diện khi phát hiện bút đang rê phía trên màn hình.

#### ![](/icons/help.webp) Cửa sổ bật trợ giúp khi di chuột {#help-popup-on-hover}

Với thiết bị hỗ trợ rê con trỏ, tùy chọn này quyết định phần trợ giúp theo ngữ cảnh của Nomad, đánh dấu bằng biểu tượng ![](/icons/help.webp), sẽ hiện ra khi rê con trỏ hay chỉ khi bấm vào.

#### Tỷ lệ tổng thể {#overall-scale}
Hệ số nhân kích thước cho mọi thành phần giao diện.
#### Chiều rộng bảng {#panel-width}
Độ rộng của menu và bảng.
#### Tỷ lệ phông chữ {#font-scale}
Thay đổi cỡ chữ.
#### Khoảng cách dọc {#vertical-spacing}
Khoảng cách giữa các thành phần trong menu và bảng.
#### Khoảng cách dọc (trái) {#vertical-spacing-left}
Khoảng cách giữa các thành phần trên thanh công cụ bên trái.

#### Độ lệch cạnh {#edge-offset}
Bạn chỉ nên thay đổi các giá trị này nếu gặp khó khăn khi bấm các nút sát mép màn hình. Nếu các thanh trượt này bị tắt, Nomad sẽ dùng giá trị vùng an toàn do chính thiết bị cung cấp.

::: tip
Khi chuyển Nomad sang thiết bị mới (ví dụ thay iPhone 12 bằng iPhone 15), hãy nhớ đặt lại các tùy chọn cạnh về mặc định!
:::

#### ![](/icons/reset.webp) Đặt lại bố cục {#reset-layout}
Đưa mọi tùy chọn bố cục về giá trị mặc định.

## ![](/icons/window.webp) Phím tắt {#shortcuts}

Thẻ Phím tắt chọn những nút nhanh nào xuất hiện quanh khung nhìn, và cho phép bạn tự tạo các thanh công cụ nổi.

### Thanh bên {#side-bar}
Các nút công cụ nhanh ở cuối thanh bên trái: `Làm mịn`, `Mặt nạ`, `Ẩn`, `Nhóm mặt` và `Gizmo`. Kéo chúng để thay đổi thứ tự.

### Thanh dưới cùng {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Chạm vào một phím tắt để thêm nó vào thanh dưới cùng, hoặc để gỡ nó ra. Các phím tắt sau được bật theo mặc định:
* `Hoàn tác` - hoàn tác thao tác trước đó
* `Làm lại` - khôi phục thao tác vừa hoàn tác
* `Solo` - Tạm thời ẩn mọi đối tượng khác, chỉ để lại đối tượng đang chọn. Nhấn lần nữa để hiện lại tất cả các đối tượng.
* `X-quang` - Tạm thời làm mọi đối tượng khác bán trong suốt, chỉ để đối tượng đang chọn đặc. Nhấn lần nữa để khôi phục vật liệu mặc định.
* `Voxel` - Tái tạo lưới cho đối tượng hiện tại bằng độ phân giải voxel dùng lần trước. Nhấn lâu hoặc vuốt lên sẽ hiện thanh trượt độ phân giải và nút bật/tắt cạnh sắc.
* `Lưới` - Bật/tắt lưới khung nhìn. Nhấn lâu hoặc vuốt lên để thay đổi màu và độ đục của lưới.
* `Khung lưới` - Bật/tắt lớp phủ khung lưới. Nhấn lâu hoặc vuốt lên để thay đổi màu và độ đục của khung lưới.
* `Kiểm tra` - cho phép bạn xem các thuộc tính của lưới như UV, kết cấu đã bake và các thuộc tính khác, phủ lên nền của Nomad.
* `Nhóm mặt` - Bật/tắt lớp phủ nhóm mặt, xem thêm tại [Công cụ->Nhóm mặt](tools.md#facegroup)

Các phím tắt hay dùng khác cũng có sẵn: `Bao viền`, `Chiếu` (phối cảnh hoặc trực giao), `MatCap`, `DynTopo`, cùng các nút `Phân chia`, `Đảo ngược` và cấp độ của [Đa phân giải](topology.md#multiresolution).

#### ![](/icons/more.webp) Ràng buộc {#bindings-list}

Gần như mọi chức năng của Nomad đều có thể được thêm vào thanh dưới cùng qua nút ràng buộc, nút này cũng cho biết thanh đang chứa bao nhiêu phím tắt. Khi bấm vào nút, menu ràng buộc sẽ hiện ra:

![](/images/interface_bindings_search.webp)

Bạn có thể tìm theo nhóm qua các biểu tượng ở trên cùng, hoặc dùng ô tìm kiếm để tìm chức năng theo tên. Bấm vào một chức năng để thêm nó vào thanh công cụ. Bấm lần nữa để gỡ nó ra.

#### ![](/icons/eye_open.webp) Có thể thấy {#order}

Hiện hoặc ẩn toàn bộ thanh dưới cùng.

#### ![](/icons/reset.webp) Đặt lại {#reset}

Đặt lại sẽ đưa thanh dưới cùng về thiết lập mặc định.

### Cửa sổ nổi {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Bấm dấu + sẽ thêm một thanh công cụ nổi. Nó sẽ chưa hiển thị cho đến khi bạn bấm nút ràng buộc và thêm vài phím tắt vào, sau đó bạn có thể cho nó hiển thị.

Bạn có thể tạo nhiều thanh công cụ, mỗi thanh có một hàng với các tùy chọn sau:

* Kéo tay nắm ở bên trái một hàng để sắp xếp lại các thanh công cụ.
* `Tên` - Tên của thanh công cụ.
* `Có thể thấy` - Bật/tắt hiển thị thanh công cụ.
* `Thanh` - Hiển thị thanh tiêu đề trên thanh công cụ.
* `Chế độ thu gọn` - Giữ thanh công cụ trên màn hình khi giao diện được thu gọn.
* `Ràng buộc` - Mở cửa sổ ràng buộc để chọn chức năng thêm vào hoặc gỡ khỏi thanh công cụ.
* `Xóa` - Xóa thanh công cụ.

## ![](/icons/gesture.webp) Cử chỉ {#gesture}
Menu Cử chỉ quyết định cách ngón tay, bút, chuột và bàn di chuột điều khiển Nomad.

![](/images/interface_gesture.webp)

### Tùy chọn cử chỉ {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad có thể giới hạn các thao tác theo thiết bị nhập. Ví dụ, kéo bằng ngón tay chỉ di chuyển máy ảnh, còn kéo bằng bút chỉ để điêu khắc. Nếu bạn có chuột hoặc bàn di chuột, bạn cũng có thể gán chúng cho những thao tác cụ thể.

Mỗi hàng là một thao tác: bật/tắt `Ngón tay`, `Bút cảm ứng` và `Chuột` để chọn thiết bị nhập nào được thực hiện thao tác đó.

* `Máy ảnh` - Di chuyển máy ảnh.
* `Chỉnh sửa nút` - Kéo các tay nắm hiển thị trên khung vẽ, ví dụ để chỉnh sửa một hình cơ bản, một đường cong, một trình lặp lại hoặc một đèn.
* `Điêu khắc` - Điêu khắc bằng các cọ. Những công cụ có hàng riêng bên dưới sẽ làm theo hàng đó.
* `Chọn đối tượng` - Chạm vào một đối tượng để chọn nó.
* `Chọn vật liệu` - Nhấn lâu trên khung vẽ để lấy màu hoặc vật liệu dưới con trỏ. Chỉ hoạt động khi cọ hiện tại có bật tính năng vẽ màu.
* `Chạm đơn` - Các phím tắt chạm của những công cụ như Mặt nạ, Ẩn và Nhóm mặt (xem bên dưới).
* `Sơn` - Công cụ Vẽ và Bôi nhòe.
* `Mặt nạ` - Công cụ Mặt nạ.
* `Mặt` - Công cụ Ẩn và Nhóm mặt.
* `Tạo` - Công cụ Ống, Tiện và Chèn.
* `Cắt` - Công cụ Cắt, Tách và Chiếu.
* `Chọn` - Công cụ Chọn và Đo.
* `Gizmo` - Công cụ Gizmo và Lattice.
* `Biến đổi` - Công cụ Biến Đổi và Sắp xếp.

::: tip
Một thiết lập phổ biến trên máy tính bảng là chỉ cho bút điêu khắc và vẽ, còn ngón tay dành để điều khiển máy ảnh. Nhờ vậy lòng bàn tay hay một ngón tay vô tình chạm vào sẽ không bao giờ để lại nét vẽ trên mô hình.
:::

### ![](/icons/tool_smooth.webp) Ngón tay luôn làm mượt {#finger-always-smooths}
Khi bật, ngón tay của bạn luôn làm mượt khi một công cụ điêu khắc đang hoạt động, bất kể cọ nào. Bật tùy chọn này sẽ bỏ `Ngón tay` khỏi hàng `Điêu khắc`, nên bút dùng để điêu khắc còn ngón tay dùng để làm mượt.

### Nét vẽ ngoài bề mặt {#allow-air-stroke}
Cho phép bắt đầu nét vẽ ngay cả khi con trỏ chạm xuống bên ngoài lưới. Chọn các công cụ được áp dụng: `Công cụ` (mọi cọ khác), `Làm mịn`, `Mặt nạ` và `Ẩn`. Tùy chọn này chỉ hoạt động với thiết bị nhập có thể điêu khắc nhưng không di chuyển máy ảnh, nên các nút này bị tắt cho đến khi một thiết bị nhập của bạn được thiết lập như vậy.

### ![](/icons/stroke.webp) Bắt dính nét vẽ {#stroke-snap}
Giữ yên con trỏ ở cuối nét vẽ để nắn nó thành một đường thẳng hoặc một đường cong mượt. Tiếp tục kéo để xoay và thu phóng nét đã nắn quanh điểm bắt đầu của nó.

`Thời gian giữ` đặt khoảng thời gian bạn phải giữ yên trước khi nét vẽ được nắn, hoặc trước khi một hình chuyển sang chế độ chỉnh sửa.

### ![](/icons/stylus.webp) Sử dụng các mẫu đầu vào bổ sung {#use-extra-input-samples}
Dùng các mẫu đầu vào bổ sung do thiết bị cung cấp. Hãy tắt nếu nét vẽ bị răng cưa hoặc lực nhấn hoạt động không đúng. Tùy chọn này không hiển thị trên iOS.

### ![](/icons/tool_mask.webp) Mặt nạ {#mask}

![](/images/interface_gesture_mask.webp)

`Phím tắt một lần chạm` - Bật các phím tắt một lần chạm sau mà không cần giữ nút mặt nạ. Nó cho phép các cử chỉ:
* chạm vào nền để đảo ngược mặt nạ
* chạm vào vùng đã phủ mặt nạ để làm mờ mặt nạ
* chạm vào vùng chưa phủ mặt nạ để làm sắc nét mặt nạ

#### Nhấn lâu {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)

Nhấn lâu khi dùng công cụ Mặt nạ sẽ chuyển giữa cọ mặt nạ và dây thòng lọng (Chọn Mặt Nạ):
* `Nhấn lâu - Điêu khắc` - Nhấn lâu rồi tiếp tục kéo: nét vẽ được tạo bằng chế độ còn lại, và chế độ trước sẽ quay lại khi kết thúc nét.
* `Nhấn lâu - Chuyển đổi` - Nhấn lâu rồi thả ra mà không di chuyển để chuyển qua lại giữa hai chế độ.

### ![](/icons/tool_smooth.webp) Làm mịn {#smooth}
`Nhấn lâu - Dây thòng lọng` - Nhấn lâu khi dùng công cụ Làm mịn sẽ chuyển sang công cụ Chọn trong suốt nét vẽ chọn.

### ![](/icons/tool_hide.webp) Ẩn {#hide}
![](/images/interface_gesture_hide.webp)

`Phím tắt một lần chạm` sẽ bật các phím tắt sau cho công cụ Ẩn:
* Chạm vào một nhóm mặt để ẩn nó
* Chạm vào khoảng trống để đảo ngược các đa giác bị ẩn

### ![](/icons/finger3.webp) Ba ngón tay {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Nếu thiết bị của bạn hỗ trợ cử chỉ 3 ngón tay, hãy thiết lập phím tắt cho cử chỉ đó.

Ma trận tùy chọn cho phép bạn gán kéo dọc và kéo ngang thành các phím tắt riêng, hoặc chọn `Không` để tắt. Lưu ý rằng nếu cùng một cử chỉ được chọn cho 2 tùy chọn, một trong số đó sẽ bị tắt và tên của nó bị gạch ngang.

* `Xoay ánh sáng` - Xoay môi trường, đèn và MatCap.
* `Bán kính công cụ` - Chỉnh bán kính công cụ.
* `Cường độ công cụ` - Chỉnh cường độ công cụ.

### ![](/icons/fingerprint.webp) Lịch sử 2/3 {#history-23}
`Phím tắt lịch sử` - khi bật, các cử chỉ sau sẽ hoạt động:
* Hoàn tác - chạm bằng 2 ngón tay
* Làm lại - chạm bằng 3 ngón tay

`Nhấn lâu` - khi bật, giữ 2/3 ngón tay trên màn hình sẽ hoàn tác/làm lại liên tục.

### ![](/icons/mouse.webp) Bánh xe chuột {#mouse-wheel}
`Tốc độ (thu phóng 3d)` đặt tốc độ thu phóng khung nhìn bằng bánh xe, còn `Tốc độ (giao diện 2d)` đặt tốc độ cuộn menu và bảng. Nút dấu trừ bên cạnh mỗi thanh trượt đảo ngược chiều.

### ![](/icons/fingerprint.webp) Bàn di chuột {#trackpad}
Trên máy Mac, `Hai ngón tay` chọn tác dụng của hai ngón tay trên bàn di chuột. Chụm ngón luôn để thu phóng, xoay ngón luôn để nghiêng khung nhìn.
* `Tắt` - Cuộn bằng hai ngón tay để thu phóng, giống bánh xe chuột. Các ngón tay không được nhận diện riêng lẻ.
* `Di chuyển` - Hai ngón tay để di chuyển khung nhìn, nhấc một ngón lên để xoay quanh. Giống như trên máy tính bảng.
* `Xoay quỹ đạo` - Hai ngón tay để xoay quanh khung nhìn, nhấc một ngón lên để di chuyển.

### Trợ năng {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Cửa sổ trợ giúp` sẽ mở một thanh công cụ nổi để điều khiển các thao tác kéo, chụm, nghiêng và máy ảnh.

### Máy ảnh {#camera}
Lối tắt đến menu `Máy ảnh` (các tùy chọn máy ảnh trước đây nằm ở đây, nhưng đã được chuyển sang menu Máy ảnh).

### Nhấn đúp bút chì -> Ràng buộc {#pencil-tap}

Lối tắt đến menu `Ràng buộc`, nơi bạn đặt tác dụng của thao tác nhấn đúp Pencil. Ngoài iOS, nó hiển thị là `Nút bút chì → Ràng buộc`, dành cho nút trên bút.

### Từ chối lòng bàn tay {#palm-rejection}
Trên điện thoại và máy tính bảng, bỏ qua những lần chạm có diện tích tiếp xúc lớn hơn `Ngưỡng kích thước tối đa`, như lòng bàn tay đặt lên màn hình. Tính năng này có thể không hoạt động trên mọi thiết bị, nên hãy tắt nó nếu bạn gặp khó khăn khi thao tác trên khung vẽ.


## ![](/icons/keyboard.webp) Ràng buộc {#bindings}
Phím tắt bàn phím và nút bấm có thể được thiết lập trong menu Ràng buộc:

![](/images/interface_bindings.webp)
Gần như mọi chức năng của Nomad đều có thể gán cho phím tắt bàn phím nếu thiết bị của bạn có bàn phím, cho các nút phụ trên bút, hoặc thậm chí cho tay cầm chơi game.

Để tạo một ràng buộc, bấm vào ô chữ nhật bên cạnh chức năng, rồi nhấn phím/nút mong muốn.

Tìm chức năng qua các biểu tượng nhóm ở trên cùng, hoặc qua thanh tìm kiếm để tìm theo tên.

Bạn có thể tắt từng ràng buộc bằng ô chọn bên cạnh tên ràng buộc. Nhấn lâu vào ô chọn rồi kéo để sắp xếp lại danh sách.

Khi hai ràng buộc đang bật dùng cùng một phím tắt, biểu tượng ![](/icons/help.webp) sẽ hiện bên cạnh chúng, liệt kê các chức năng bị trùng.

### ![](/icons/more.webp) Menu ngữ cảnh {#context-menu}
Biểu tượng ![](/icons/more.webp) sau mỗi ràng buộc sẽ mở một menu ngữ cảnh:

![](/images/interface_bindings_context.webp)

* `Nhân bản` - Nhân bản ràng buộc, ví dụ để gán cho một chức năng phím tắt thứ hai.
* `Đặt lại` - Đặt lại ràng buộc
* `Xóa` - Xóa ràng buộc. Chỉ thực hiện được khi chức năng có nhiều hơn một ràng buộc.

Bên dưới chúng, một số ràng buộc có thêm tùy chọn:

* `Phím dính` - Với phím tắt công cụ và phím tắt nhanh (Mặt nạ, Làm mịn, Gizmo, Ẩn, Nhóm mặt, Thêm/Trừ), chọn cách nhấn phím để chuyển công cụ. `Tự động` dùng giá trị mặc định đặt trong tùy chọn [Nâng cao](#advanced).
  * `Giữ` - Giữ phím để dùng công cụ, thả ra để quay về công cụ trước.
  * `Chuyển đổi` - Nhấn một lần để chuyển công cụ.
  * `Nhấn nhanh` - Giữ để dùng công cụ tạm thời, hoặc nhấn nhanh để chuyển sang công cụ đó.
* `Giữ đảo ngược` - Với phím tắt nhanh, chọn việc thả phím đang giữ có luôn quay về công cụ trước hay không, kể cả khi công cụ đó vốn đã đang hoạt động.
* `Chuyển đổi công cụ trước` - Với phím tắt công cụ, nhấn phím tắt của công cụ hiện tại sẽ quay về công cụ dùng lần trước. Cần đặt `Phím dính` là `Chuyển đổi` hoặc `Nhấn nhanh`.
* `Vị trí` - Với phím tắt cửa sổ nổi, mở cửa sổ ở vị trí cũ (`Giữ lại trước đó`) hoặc dưới con trỏ (`Trên con trỏ`).
* `Tịnh tiến (khi thả phím)` / `Thu phóng (khi thả phím)` - Với ràng buộc thu phóng và di chuyển máy ảnh, chuyển sang chế độ còn lại khi bạn thả phím.
* Hướng kéo - Với `Quay ánh sáng`, `Bán Kính Công Cụ` và `Cường Độ Công Cụ`, chọn kéo ngang hoặc kéo dọc.
* `Đồng bộ` - Với các chức năng thêm, nhân bản hoặc tạo thực thể cho đối tượng, chọn có đồng bộ kết quả hay không. Mặc định, nó dùng giá trị đồng bộ đặt trong menu Cảnh.
* `Trên Nền` - Với phím tắt nhanh Làm mịn và Mặt nạ, kéo trên nền trong khi giữ phím để vẽ dây thòng lọng: dây thòng lọng chọn cho Làm mịn, dây thòng lọng mặt nạ cho Mặt nạ.
* `Cưỡng ép camera` - Với các ràng buộc máy ảnh, vẫn di chuyển máy ảnh ngay cả khi cùng phím tắt đó cũng được dùng cho một ràng buộc khác, thường là phím tắt công cụ hoặc Thêm/Trừ.
* `Xoay tuyến tính` - Với ràng buộc nghiêng, nghiêng khung nhìn bằng thao tác kéo ngang, dọc hoặc chéo thay vì di chuyển quanh trục xoay.

::: tip
Với `Nhấn nhanh`, một phím làm được cả hai việc: giữ nó để làm mịn hoặc phủ mặt nạ nhanh rồi quay lại cọ của bạn khi thả ra, hoặc chạm để ở lại công cụ đó.
:::

### ![](/icons/cog.webp) Nâng cao {#advanced}
Ở cuối menu Ràng buộc có một menu bánh răng cho các tùy chọn nâng cao:

![](/images/interface_bindings_advanced.webp)

* `Phím tắt nhanh` - Giá trị mặc định của `Phím dính` và `Giữ đảo ngược` cho các phím tắt Mặt nạ, Làm mịn, Gizmo, Ẩn, Nhóm mặt và Thêm/Trừ.
* `Phím tắt công cụ` - Giá trị mặc định của `Phím dính` và `Chuyển đổi công cụ trước` cho các phím tắt công cụ. Với `Chuyển đổi công cụ trước`, bạn có thể liên tục chuyển qua lại giữa hai công cụ bằng cùng một phím tắt.
* `Cửa sổ phím tắt` - Chế độ `Phím dính` của các phím tắt mở cửa sổ nổi.
* `Lật thu phóng Y` - Đảo ngược chiều kéo dọc khi thu phóng bằng ràng buộc.
* `Xoay tuyến tính` - Nghiêng khung nhìn bằng thao tác kéo ngang, dọc hoặc chéo thay vì di chuyển quanh trục xoay.
* `SpaceMouse` - Bật hỗ trợ 3Dconnexion SpaceMouse. Trên một số hệ thống sẽ có thêm tùy chọn: thứ nó di chuyển (`Đối tượng`, `Máy ảnh`, `Góc nhìn thứ nhất`, `Drone`), `Tự động cập nhật tâm xoay` để chuyển tâm xoay đến bề mặt dưới con trỏ khi bắt đầu di chuyển, cùng tốc độ `Dịch`, `Phóng to thu nhỏ` và `Xoay`.
* `Vùng chết (trôi)` - Dành cho bộ điều khiển `Tay cầm chơi game`, `Joystick` và `Nút`. Hãy tăng các giá trị này nếu máy ảnh tự di chuyển khi bạn không chạm vào bộ điều khiển.
* `Bán Kính Công Cụ` - Cách thao tác kéo bằng ràng buộc bán kính thay đổi kích thước cọ (`Hình tròn`, `Giữa` hoặc `dx`), rồi mức mà các ràng buộc bán kính cộng thêm (tính bằng điểm ảnh) hoặc nhân lên sau mỗi lần nhấn.
* `Cường Độ Công Cụ` - Mức mà các ràng buộc cường độ cộng thêm hoặc nhân lên sau mỗi lần nhấn.
* `Máy ảnh - Tốc độ` - Tốc độ `Dịch` và `Xoay` của các ràng buộc di chuyển và xoay khung nhìn.
* `Đặt lại các ràng buộc` - đưa mọi ràng buộc về mặc định.
* `Đặt lại thứ tự` - khôi phục thứ tự mặc định của danh sách ràng buộc.


## Hiển thị phím tắt bàn phím ⌘ trên iOS {#ios-keyboard-shortcuts-display}

Trên thiết bị iOS có bàn phím, giữ phím ⌘ (cmd) để hiển thị danh sách phím tắt.

Hỗ trợ bàn phím trên Android vẫn còn hơi thử nghiệm.

![](/images/shortcuts.webp)


## ![](/icons/bug.webp) Gỡ lỗi {#debug}
Menu này chứa một số tùy chọn thử nghiệm và gỡ lỗi. Phần lớn các tùy chọn này nên để mặc định, và chỉ thay đổi sau khi đã liên hệ với bộ phận hỗ trợ của Nomad. Các biểu tượng ở trên cùng giúp nhảy nhanh đến từng phần.

![](/images/interface_debug.webp)
### ![](/icons/uv.webp) UV {#uv}
* `Bình thường hóa UVs` - Nomad sẽ chuẩn hóa UV của lưới đang chọn vào trong ô [0-1].

### ![](/icons/sun.webp) Tô bóng {#render}
* `Ghi độ sâu khúc xạ (mặt sau)` - Mặt sau của các lưới khúc xạ sẽ được ghi vào bộ đệm độ sâu.
* `Pháp tuyến mượt có trọng số góc` - Một điều chỉnh trong cách tô bóng mượt hoạt động, có thể tránh vết gấp trong một số trường hợp.

### ![](/icons/speed.webp) Mục tiêu FPS {#target-fps}
Khi tắt, Nomad sẽ đồng bộ số khung hình mỗi giây với tần số quét của màn hình.

Khi bật, bạn có thể đặt số khung hình mỗi giây mà Nomad sẽ render.

### ![](/icons/window.webp) Giao diện {#debug-interface}
* `Hộp công cụ: hiện tất cả` - Nomad ẩn những công cụ không liên quan đến vùng chọn hiện tại, ví dụ mọi cọ điêu khắc đều bị ẩn trên hình cơ bản chưa hoàn tất. Tùy chọn này làm mờ các công cụ không dùng được thay vì ẩn chúng.

Các tùy chọn giao diện khác từng nằm ở đây nay đã chuyển sang thẻ [Giao diện](#interface).

### ![](/icons/turntable.webp) Đĩa xoay {#gif-turntable}
Nomad có thể xuất ảnh gif động xoay tròn mô hình. Lưu ý rằng do giới hạn của định dạng gif, chất lượng sẽ thấp. Quay màn hình thường là cách tốt hơn.

* `Thời lượng` - độ dài của vòng xoay, tính bằng giây
* `Lấy mẫu khung tối đa` - Nhiều hiệu ứng render chất lượng cao của Nomad đến từ việc kết hợp nhiều khung hình với nhau. Thanh trượt này đặt số khung hình được kết hợp, và ô chọn của nó dùng để bật hoặc tắt.
* `Trung tâm xoay` - điểm mà máy ảnh xoay quanh: `Giữ nguyên hiện tại` giữ trục xoay hiện tại, `(0, 0, 0)` dùng tâm thế giới, `Cảnh` dùng tâm của cảnh.
* `Nền trong suốt` - Dùng tùy chọn trong suốt cho gif. Lưu ý rằng gif chỉ hỗ trợ độ trong suốt 1 bit, nên viền có thể bị răng cưa nặng.
* `Xuất (GIF)` - bắt đầu xuất gif.

### ![](/icons/postprocess.webp) Hậu kỳ {#post-process}
* `Lọc` - Tùy chọn gỡ lỗi
* `Định dạng` - Tùy chọn gỡ lỗi
* `Dùng lại bộ đệm` - Tùy chọn gỡ lỗi

### ![](/icons/ram.webp) Hiệu suất {#performance}
* `Đa luồng: chung` - Tùy chọn gỡ lỗi
* `Đa luồng: điêu khắc` - Tùy chọn gỡ lỗi
* `Vẽ bản lặp bằng thực thể` - Vẽ mọi bản sao của một trình lặp lại trong một lệnh vẽ duy nhất. Tùy chọn gỡ lỗi.

### ![](/icons/star.webp) Tính năng {#feature}
* `nom: nén đa phân giải` - Giảm dung lượng của các dự án và tệp xuất từ Nomad có dùng đa phân giải. Các phiên bản Nomad cũ hơn không mở được những tệp này. Tùy chọn này có thể sẽ bị gỡ bỏ và được bật mặc định trong tương lai.
* `Đảo đường chéo tứ giác (khi chạm)` - Tùy chọn gỡ lỗi

### ![](/icons/bug.webp) Gỡ lỗi {#dev}
* `Nhật ký` - Mở cửa sổ xem nhật ký
* `Ghi nhật ký sự kiện` - Ghi các sự kiện con trỏ của bạn (ngón tay, bút, chuột) vào cửa sổ nhật ký, để tìm hiểu các vấn đề về thiết bị nhập.
* `FPS` - thêm bộ đếm khung hình mỗi giây vào thống kê của khung nhìn.
* `Cửa sổ đánh giá ứng dụng` - Tùy chọn gỡ lỗi, trên iOS và Android.

### ![](/icons/image.webp) Biểu tượng tùy chỉnh {#custom-icons}
Thay biểu tượng của Nomad bằng các tệp png của riêng bạn.
* `Nhập biểu tượng` - Nhập các tệp png vào `tmp_session/icons`. Mỗi tệp sẽ thay thế biểu tượng gốc cùng tên. Chúng sẽ bị bỏ khi Nomad khởi động lại.
* `Xuất biểu tượng công cụ` - Sao chép các biểu tượng gốc `tool_<tool>.png` vào `tmp_session/icons`, không ghi đè. Bạn có thể chỉnh sửa chúng ở đó và áp dụng bằng `Tải lại biểu tượng`.
* `Tải lại biểu tượng` - Áp dụng các biểu tượng từ `tmp_session/icons`.

### Tái định hình tứ giác {#quad-remesh}
Các tùy chọn tái định hình tứ giác không còn nằm trong menu này: xem [Tái định hình tứ giác](topology.md#quad-remesh-instant) trong menu Tô pô và công cụ [Quad Remesher](tools.md#quad-remesher).

### Tạo ảnh nhỏ cho cửa hàng {#make-store-thumbnails}
Render ảnh chụp màn hình ở các kích thước phù hợp với iOS App Store.
