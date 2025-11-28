# ![](/icons/interface.webp) Menu Giao diện {#interface-menu}

Menu này điều khiển nhiều tùy chọn để tùy biến giao diện của Nomad. 

![](/images/interface_overview2.webp)

Nomad có thể được tùy biến khá sâu, menu này được chia thành 4 phần: Interface, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
Trang này nói về menu giao diện, không phải chính giao diện! Giao diện tổng thể được mô tả trong [Bắt đầu](gettingstarted.md).
:::

## Giao diện {#interface}

Phần interface cho phép bạn thêm phím tắt, tạo thanh công cụ nổi, và điều khiển màu sắc, kích thước, diện mạo của giao diện người dùng Nomad.

![](/images/interface_overview3.webp)

### Thêm phím tắt (dưới cùng)... {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Thanh công cụ phía dưới có các phím tắt này được bật theo mặc định:
* `Undo` - hoàn tác thao tác trước đó
* `Redo` - khôi phục thao tác vừa được hoàn tác
* `Solo` - Tạm thời ẩn mọi đối tượng khác, chỉ để lại đối tượng đang được chọn hiển thị. Nhấn lại để khôi phục tất cả đối tượng.
* `X-ray` - Tạm thời làm tất cả đối tượng khác bán trong suốt, chỉ để lại đối tượng đang chọn là đặc. Nhấn lại để khôi phục vật liệu mặc định.
* `Voxel remesh` - Remesh đối tượng hiện tại bằng độ phân giải voxel được dùng lần gần nhất. Nhấn giữ lâu hoặc vuốt lên sẽ hiện thanh trượt độ phân giải và công tắc cạnh sắc.
* `Grid` - Bật/tắt lưới nhìn. Nhấn giữ lâu hoặc vuốt lên sẽ cho phép bạn thay đổi màu và độ mờ của lưới.
* `Wireframe` - Bật/tắt lớp phủ wireframe. Nhấn giữ lâu hoặc vuốt lên sẽ cho phép bạn thay đổi màu và độ mờ của wireframe.
* `Inspector` - cho phép bạn xem các thuộc tính của mesh như UV, texture bake, và các thuộc tính khác, được phủ lên nền của Nomad.
* `Face Group` - Bật/tắt lớp phủ facegroup, xem thêm trong [Tools->FaceGroup](tools.md#facegroup) 

Các phím tắt thường dùng khác có sẵn trong menu này, nhiều phím hơn nữa có thể tìm thấy trong nút bindings.

#### ![](/icons/more.webp) Gán phím {#bindings-list}

Hầu như mọi chức năng của Nomad đều có thể được thêm vào thanh phím tắt thông qua nút bindings. Một menu bindings sẽ hiện ra khi nút được bấm:

![](/images/interface_bindings_search.webp)

Bạn có thể tìm theo danh mục qua các biểu tượng ở trên cùng, hoặc dùng ô tìm kiếm để tìm chức năng theo tên. Bấm vào một chức năng để thêm nó vào thanh công cụ. Bấm lại để gỡ nó ra.

#### ![](/icons/list.webp) Thứ tự {#order}

Thao tác này sẽ hiển thị danh sách các phím tắt. Nhấn giữ rồi kéo để sắp xếp lại thứ tự phím tắt.

#### ![](/icons/reset.webp) Đặt lại {#reset}

Reset sẽ khôi phục thanh công cụ phía dưới về thiết lập mặc định.

### Thêm phím tắt (cửa sổ)... + {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Bấm dấu + sẽ thêm một thanh công cụ nổi. Nó sẽ không hiển thị cho đến khi bạn bấm nút bindings và thêm một số phím tắt vào đó, sau đó bạn có thể bật hiển thị.

Bạn có thể tạo nhiều thanh công cụ, mỗi thanh có các tùy chọn sau trong menu này:

* ![](/icons/checked.webp) `Visible` - Bật/tắt hiển thị cho thanh công cụ
* ![](/icons/more.webp)`Bindings` - Hiện cửa sổ binding để chọn chức năng thêm vào hoặc gỡ khỏi thanh công cụ.
* ![](/icons/list.webp)`Order` - Hiện menu để sắp xếp lại thanh công cụ.
* ![](/icons/reset.webp) `Reset` - Đặt lại thanh công cụ về trạng thái mặc định.
* ![](/icons/resize_bottom_right.webp) `Resize corner` - Bật/tắt tay nắm đổi kích thước ở góc dưới bên phải thanh công cụ.
* ![](/icons/sort_down.webp) `Collapsable` - Bật/tắt tay nắm thu gọn ở góc trên bên phải.
* ![](/icons/trash.webp) `Delete` - Xóa thanh công cụ.

### Hộp công cụ {#toolbox}

Các tùy chọn cho menu công cụ ở bên phải giao diện Nomad.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Góc đổi kích thước UI {#ui-resize-corner}

Bật/tắt tay nắm đổi kích thước ở góc dưới của thanh công cụ.

#### Ẩn {#hidden}
Thông thường biểu tượng toolbox trên thanh trên cùng sẽ chuyển đổi giữa một cột dài đơn, hoặc danh sách nhiều cột các công cụ. Tùy chọn này sẽ chuyển đổi giữa danh sách nhiều cột, hoặc ẩn hoàn toàn.

#### Tô màu {#colored}
Tô màu biểu tượng theo danh mục, ví dụ tất cả công cụ mask màu nâu, công cụ split màu đỏ, công cụ flatten màu xanh lá, v.v.

#### Hàng: Tự động (>1) {#rows-auto-1}

#### Đặt lại thứ tự {#reset-order}
Đặt lại các công cụ mặc định trong toolbox về thứ tự mặc định. Biểu tượng tùy chỉnh sẽ vẫn ở trong toolbox ở cuối danh sách.


### Mẫu cài sẵn {#presets}

![](/images/interface_presets.webp)

Một tập hợp preset màu cho giao diện.

#### Nút tương phản cao {#high-contrast-button}
Một kiểu nút thay thế giúp nút dễ thấy hơn khi được bật. Nếu đặt ở Auto, Nomad sẽ dùng chế độ này khi độ tương phản màu UI giữa trạng thái bật/tắt thấp.

#### Bộ chọn màu/Màu cơ bản {#color-widgetcolor-base}
Các màu chính được dùng trong giao diện.

#### Bảng trong suốt, Bảng màu, Độ mờ {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Khi bật, các tùy chọn bổ sung sẽ xuất hiện để điều khiển cách menu và panel hiển thị trong Nomad. Màu sắc, độ trong suốt và mức độ mờ có thể được điều chỉnh.

::: tip
Trên thiết bị nhỏ, có thể hữu ích khi làm panel màu gần trắng, trong suốt, và độ mờ thấp, để menu không che khuất cảnh.
:::

----

### Phản chiếu thanh trên {#mirror-top-bar}
Đảo ngược thứ tự menu trên thanh trên cùng.

### Phản chiếu thanh bên {#mirror-side-bars}
Hoán đổi thanh bên để toolbox nằm bên trái, tùy chọn công cụ nằm bên phải.

### Phản chiếu thanh dưới {#mirror-bottom-bar}
Di chuyển thanh dưới cùng sang góc dưới bên phải, và đảo ngược thứ tự nút.

### Xem trước màu vật liệu {#material-color-preview}
Khi bạn chọn màu cho một material, bản xem trước của material này sẽ được hiển thị trên đối tượng đang được chọn.

----
### Hộp trợ giúp khi rê chuột {#help-popup-on-hover}

Đối với thiết bị hỗ trợ hover, bật để phần trợ giúp ngữ cảnh trong Nomad được biểu diễn bằng biểu tượng ![](/icons/help.webp) sẽ xuất hiện khi hover, hoặc chỉ khi bấm.

----

### Tỉ lệ tổng thể {#overall-scale}
Hệ số nhân kích thước cho tất cả phần tử UI.
### Chiều rộng bảng {#panel-width}
Độ rộng của menu và panel.
### Tỉ lệ phông chữ {#font-scale}
Tỉ lệ phông chữ.
### Giãn cách dọc {#vertical-spacing}
Khoảng cách giữa các phần tử trong menu và panel.
### Giãn cách dọc (trái) {#vertical-spacing-left}
Khoảng cách giữa các phần tử trong thanh công cụ bên trái.

----

### Lề cạnh {#edge-offset}
Bạn chỉ nên thay đổi các giá trị này nếu gặp vấn đề khi tương tác với các nút ở mép màn hình. Nếu các thanh trượt này bị vô hiệu, Nomad sẽ dùng giá trị vùng an toàn do chính thiết bị trả về.

::: tip
Khi chuyển Nomad sang thiết bị mới (ví dụ thay iPhone 12 bằng iPhone 15), hãy nhớ đặt lại tùy chọn cạnh về mặc định!
:::

### Đặt lại kiểu {#reset-style}
Đặt lại tất cả phần tử UI về giá trị mặc định.


## Cử chỉ {#gesture}
Menu gesture điều khiển cách bút và ngón tay điều khiển Nomad.

![](/images/interface_gesture.webp)

### Tùy chọn cử chỉ {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad có thể giới hạn thao tác dựa trên thiết bị nhập. Ví dụ kéo bằng ngón tay chỉ có thể di chuyển camera, trong khi kéo bằng bút chỉ có thể sculpt. Nếu bạn có chuột hoặc trackpad, chúng cũng có thể được gán để điều khiển các thao tác cụ thể.

Hiện tại Nomad cho phép bạn đặt các chế độ này được điều khiển bằng bất kỳ tổ hợp gesture ngón tay, bút hoặc chuột nào:

* Camera
* Sculpt
* Gizmo
* Chọn material (bằng nhấn giữ lâu)
* Chọn đối tượng


`Finger always smooths` - Smooth có thể được đặt chỉ hoạt động với kéo bằng ngón tay.

### ![](/icons/tool_mask.webp) Mask {#mask}

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Bật các phím tắt một chạm sau đây mà không cần giữ nút mask. Nó sẽ cho phép các gesture sau:
* chạm vào nền để đảo ngược mask
* chạm vào vùng đã mask để làm mờ mask
* chạm vào vùng chưa mask để làm sắc nét mask

### Chuyển Mask <-> SelMask {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - Nhấn giữ lâu sẽ chuyển đổi giữa Mask và SelMask và bắt đầu một stroke mới. Khi kết thúc stroke, công cụ trước đó sẽ được chọn lại. 
* `Tool` - Nhấn giữ lâu và thả ra mà không di chuyển để chuyển giữa Mask và SelMask. 

### ![](/icons/tool_hide.webp) Hide {#hide}
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` sẽ bật các phím tắt sau với công cụ hide:
* Chạm vào một face group để ẩn nó
* Chạm vào vùng trống để đảo ngược các polygon bị ẩn

### ![](/icons/finger3.webp) Ba ngón tay {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Nếu thiết bị của bạn hỗ trợ gesture 3 ngón, hãy cấu hình phím tắt cho gesture đó. 

Ma trận tùy chọn cho phép bạn định nghĩa kéo dọc và kéo ngang như các phím tắt riêng. Lưu ý nếu cùng một gesture được chọn cho 2 tùy chọn, một trong hai sẽ bị vô hiệu.

* `Rotate lighting` - Xoay môi trường, đèn, và Matcap.
* `Tool Radius` - Chỉnh bán kính công cụ.
* `Tool Intensity` - Chỉnh cường độ công cụ. 

### ![](/icons/fingerprint.webp) Lịch sử 2/3 {#history-23}
`History shortcuts` - khi bật, các gesture sau sẽ hoạt động:
* Undo - chạm bằng 2 ngón
* Redo - chạm bằng 3 ngón

`Long press` - khi bật, giữ 2/3 ngón tay sẽ hoàn tác/làm lại nhanh liên tục.

### Hỗ trợ tiếp cận {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Assistive window` sẽ hiện một thanh công cụ nổi để điều khiển thao tác kéo, pinch, roll và camera.

### Camera {#camera}
Phím tắt để đi tới menu `Camera` (các tùy chọn camera trước đây nằm ở đây, nhưng đã được chuyển sang menu camera).

### Nhấp đôi bút Pencil -> Gán phím {#pencil-tap}

Phím tắt để đi tới menu `Bindings` (tùy chọn Pencil tap và double tap trước đây nằm ở đây, nhưng đã được chuyển sang menu bindings).


## Gán phím {#bindings}
Phím tắt bàn phím và nút có thể được định nghĩa từ menu bindings:

![](/images/interface_bindings.webp)
Gần như mọi chức năng trong Nomad đều có thể được gán cho phím tắt bàn phím nếu thiết bị của bạn có bàn phím, hoặc cho các nút phụ trên bút stylus, hoặc thậm chí tay cầm gamepad.

Để tạo một binding, bấm vào hình chữ nhật cạnh chức năng, rồi nhấn phím/nút. 

Tìm chức năng qua các biểu tượng danh mục ở trên cùng, hoặc qua thanh tìm kiếm để tìm theo tên. 

Các binding riêng lẻ có thể bị vô hiệu qua ô checkbox cạnh tên binding.

### ![](/icons/more.webp) Menu ngữ cảnh {#context-menu}
Biểu tượng ![](/icons/more.webp) sau mỗi binding sẽ mở menu ngữ cảnh:

![](/images/interface_bindings_context.webp)

* `Clone` - Nhân bản binding
* `Reset` - Đặt lại binding
* `Delete` - Xóa binding
* `Toggle shortcut on key tap` - Cấu hình xem nhấn chạm và nhấn giữ có được xử lý khác nhau hay không. Khi bật, một lần chạm sẽ kích hoạt công cụ. Nhấn giữ sẽ kích hoạt công cụ chỉ trong khi phím được giữ, khi thả sẽ quay lại công cụ trước đó. Đôi khi được gọi là 'sticky keys' trong các ứng dụng 3D khác.

### Nâng cao {#advanced}
Ở cuối menu bindings là menu bánh răng cho các tùy chọn nâng cao:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - Một lần chạm các phím tắt chuẩn cho mask, smooth, gizmo, hide, sub sẽ chuyển sang chế độ đó, nhưng giữ phím sẽ chuyển sang chế độ đó tạm thời, rồi khi thả phím, chế độ sẽ trở lại chế độ trước. Đôi khi được gọi là 'sticky keys' trong các ứng dụng 3D khác.
* `Toggle tool shortcuts` - Khi dùng một trong các phím tắt công cụ, nếu cùng phím tắt được nhấn hai lần, nó sẽ chuyển về công cụ trước đó. Bằng cách này bạn có thể liên tục chuyển qua lại giữa hai công cụ bằng cùng một phím nóng.
* `Invert Y (Zooming)` - Đảo chiều zoom
* `Reset bindings` - đặt lại tất cả binding về mặc định.


## iOS ⌘ Hiển thị phím tắt bàn phím {#ios-keyboard-shortcuts-display}

Trên thiết bị iOS có bàn phím, giữ phím ⌘ (cmd) để hiển thị danh sách phím tắt.

Hỗ trợ bàn phím trên Android vẫn còn hơi thử nghiệm.

![](/images/shortcuts.webp)


## Gỡ lỗi {#debug}
Một số tùy chọn thử nghiệm và debug được lưu trong menu này. Nhiều tùy chọn trong số này nên được để ở mặc định, và chỉ thay đổi sau khi liên hệ hỗ trợ Nomad.

![](/images/interface_debug.webp)
### UV {#uv}
* `Normalize Uvs` - Nomad sẽ chuẩn hóa UV bên trong tile [0-1].

### Quad Remesh {#quad-remesh}
* `Instant Mesh` - Bật thuật toán remesh tức thời
* `Quadriflow` - Một phương pháp quad remesh thay thế.

### Kết xuất {#render}
* `Heightmap` - Đổi viewport để render độ sâu của cảnh. Có thể dùng để tạo alpha map dùng cho brush.
* `Refraction write depth (back)` - Mặt sau của mesh khúc xạ sẽ được ghi vào depth buffer.
* `Flip Y (normal map)` - Đảo kênh y khi bake normal map, cần thiết cho một số engine game và render.
* `Angle weighted smooth normals` - Điều chỉnh cách hoạt động của smooth shading có thể tránh nếp gấp trong một số trường hợp.

### FPS mục tiêu {#target-fps}
Khi tắt, Nomad sẽ đồng bộ số khung hình mỗi giây với tần số làm tươi màn hình của bạn.

Khi bật, bạn có thể đặt số khung hình mỗi giây mà Nomad sẽ render.

### Giao diện {#debug-interface}
* `Top: layout` 
  * Collapse: Trên thiết bị nhỏ, thanh trên cùng sẽ thu gọn thành nhiều menu con hơn. 
  * Scroll: Nếu bạn quen dùng Nomad trên màn hình lớn và thích bố cục bình thường, bật tùy chọn này sẽ dùng thanh trên cùng rộng tiêu chuẩn, và có thể cuộn.
  * Multiline: Hiển thị toàn bộ menu trên cùng trên nhiều dòng.
* `Bottom: draggable popup` - Thanh công cụ dưới cùng có một số nút bật lên hộp thoại. Nếu tùy chọn này được bật, các hộp thoại đó có thể được di chuyển đến vị trí khác trên màn hình.  
* `Toolbox: show all` - Nomad sẽ ẩn các công cụ không liên quan đến lựa chọn hiện tại, ví dụ tất cả brush sculpt bị ẩn trên primitive chưa validate. Tùy chọn này sẽ làm mờ công cụ bị vô hiệu thay vì ẩn chúng.
* `Toolbox: colored` - Tô màu biểu tượng toolbox dựa trên loại của chúng.
* `Panel: Drop shadows` - Vẽ bóng đổ quanh menu và panel. Trên một số thiết bị cũ điều này có thể ảnh hưởng hiệu năng.
* `Panel: Blending` - Tùy chọn debug
* `Pointer: hovering dot` - Với thiết bị hỗ trợ hover bằng bút, hiển thị một chấm khi bút hover trên menu và panel.

### Gif quay bàn xoay {#gif-turntable}
Nomad có thể xuất một gif turntable động. Lưu ý do giới hạn của định dạng gif nên chất lượng thấp. Ghi màn hình thường là phương pháp tốt hơn.

* `Duration` - thời lượng turntable tính bằng giây
* `Rotation center` - vị trí trục quay của camera, do đó là phần cảnh mà camera sẽ quay quanh
* `Transparent background` - Dùng tùy chọn nền trong suốt cho gif. Lưu ý gif chỉ hỗ trợ trong suốt 1 bit, nên viền có thể bị răng cưa nặng.
* `Max frame sampling` - Nhiều hiệu ứng render chất lượng cao của Nomad đến từ việc kết hợp nhiều khung hình. Thanh trượt này đặt số khung hình tối đa để kết hợp.
* `Export (GIF)` - bắt đầu quá trình xuất gif.

### Hậu kỳ {#post-process}
* `Filtering` - Tùy chọn debug
* `Format` - Tùy chọn debug
* `Buffer reuse` - Tùy chọn debug

### Hiệu năng {#performance}
* `Multicore general` - Tùy chọn debug
* `Multicore sculpting` - Tùy chọn debug
* `Partial Drawing` - Tính năng thử nghiệm! Dùng nếu bạn đang sculpt một phần tương đối nhỏ của mesh đa giác cao. Nó sẽ giúp sculpt mượt hơn, nhưng bạn không nên bật wireframe! Ngoài ra nó có thể gây ra lỗi hiển thị trong khi stroke brush.

### Tính năng {#feature}
* `Flip quad split (on tap)` -  Tùy chọn debug
* `Join: merge radius` - Các vertex sẽ tự động được hàn nếu đủ gần nhau khi mesh được nối. Bạn có thể điều chỉnh bán kính bằng thanh trượt này.

### Gỡ lỗi {#dev}
* `Logs` - Bật popup xem log
* `App review popup` - Tùy chọn debug
* `FPS` - thêm bộ đếm khung hình mỗi giây vào thống kê viewport.