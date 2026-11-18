# ![](/icons/cog.webp) Cài đặt {#reset-to-default}

Menu cài đặt chứa nhiều tùy chọn để điều khiển giao diện và cách hoạt động của Nomad.

![](/images/settings_overview.webp)

Hàng nút ở đầu menu đưa bạn thẳng đến từng phần: `Con trỏ`, `Chỉ báo`, `Dây`, `Lưới`, `Hai mặt`, `Bao viền`, `Nổi bật`, `Bộ điều hướng`, `Thống kê`, `Tay cầm`, `Hình dạng`, `Trình lặp lại` và `Đa độ phân giải`.

## Cài đặt hiển thị {#display-settings}
Phần này chứa các lối tắt nhanh cho hầu hết các cài đặt nằm phía dưới trong menu.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Tô bóng mượt {#smooth-shading}
Chuyển giữa tô bóng mượt và tô bóng theo mặt. Khi tô bóng theo mặt, mỗi đa giác được tô bóng riêng, nên bạn có thể thấy cấu trúc tô pô bên dưới.
Tô bóng theo mặt có thể hữu ích trong giai đoạn điêu khắc, rồi chuyển sang tô bóng mượt khi render.

Tắt Tô bóng mượt giúp cải thiện hiệu năng một chút.

### ![](/icons/outline.webp) Bao viền {#outline-quick}
Bật/tắt đường bao viền quanh vùng đang chọn.

Tùy chọn này giúp bạn nhận biết lưới (hoặc các lưới) đang được chọn trong trường hợp [Làm tối các đối tượng không được chọn](#darken-unselected-objects) bị tắt.

Về mặt hiệu năng, dùng [Làm tối các đối tượng không được chọn](#darken-unselected-objects) tốt hơn nhiều so với dùng đường bao viền.

### ![](/icons/grid.webp) Lưới {#grid-quick}
Bật/tắt lưới nền, giúp bạn hình dung vị trí và tỷ lệ của các đối tượng.

### ![](/icons/culling.webp) Hai mặt {#two-sided-quick}
Bật/tắt hiển thị đa giác hai mặt. Mỗi mặt đều hướng về một phía nhất định.
Những mặt được coi là *mặt sau* là những mặt hướng "ra xa" điểm nhìn của camera.

Ví dụ, quả cầu đơn giản lúc khởi động có các mặt hướng ra ngoài.
Nếu bạn đưa camera vào trong quả cầu, bạn sẽ thấy mặt sau của các mặt này.

Phần lớn thời gian bạn không nên nhìn thấy mặt sau của các mặt, vì vậy tô màu cho chúng có thể giúp bạn phát hiện các vấn đề tiềm ẩn hoặc tô pô sai.

Tắt hiển thị `Hai mặt` có thể cải thiện hiệu năng hiển thị một chút.


### ![](/icons/wireframe.webp) Khung lưới {#wireframe-quick}
Bật/tắt lớp phủ khung lưới.

Lưu ý rằng bật khung lưới sẽ làm giảm hiệu năng.

### ![](/icons/navigator.webp) Bộ điều hướng {#snap-cube-quick}
Bật/tắt một biểu tượng trợ giúp ở góc cảnh, giúp bạn định hướng trong không gian và nhanh chóng chuyển giữa các góc nhìn trước/sau/trái/phải/trên/dưới.

### ![](/icons/palette.webp) Hiển thị vẽ {#show-painting}
Bật/tắt hiển thị phần vẽ. Khi tắt, các đối tượng hiển thị với vật liệu trắng không kim loại, độ nhám 25%, thay vì màu đã vẽ.

### ![](/icons/tool_hide.webp) Sử dụng ẩn {#use-hide}
Bật/tắt chế độ ẩn. Khi tắt, phần ẩn vẫn còn đó, chỉ là không có hiệu lực. Nút này bị vô hiệu hóa khi bạn đang dùng công cụ ẩn.

### ![](/icons/shield.webp) Hiển thị mặt nạ {#show-mask}
Bật/tắt chế độ mặt nạ. Khi tắt, mặt nạ vẫn còn đó, chỉ là không có hiệu lực. Nhấn nút này lần nữa để bật lại.

Nếu bạn cần ẩn mặt nạ NHƯNG vẫn giữ nó hoạt động, hãy dùng màu mặt nạ bên dưới và đặt thành trắng. Nhớ đổi lại thành xám khi xong việc nhé!

Lưu ý rằng nút này bị vô hiệu hóa khi bạn đang dùng một công cụ mặt nạ.

### ![](/icons/shield.webp) Mặt nạ → Không trong suốt {#mask-opaque}
`Mặt nạ → Không trong suốt` sẽ bỏ qua các đỉnh trong suốt khi áp mặt nạ. Tùy chọn này chỉ liên quan đến độ mờ đục của đỉnh và của kết cấu; các mặt bị ẩn bằng “ẩn” vẫn sẽ bị ẩn. Nó chỉ khả dụng khi `Hiển thị mặt nạ` đang bật.

### ![](/icons/bang.webp) Nổi bật {#highlight-quick}
Bật/tắt hiệu ứng nháy sáng khi chọn. Khi bạn chọn đối tượng, đối tượng được chọn sẽ nháy sáng trong 500 mili giây. Bạn có thể tùy chỉnh màu và thời lượng nháy ở bên dưới.

### ![](/icons/list.webp) Thống kê {#stats-quick}
Bật/tắt dòng chữ thông tin trạng thái trong khung nhìn 3d. Nó hiển thị thông tin về bộ nhớ hệ thống, tổng số đỉnh trong cảnh và số đỉnh của vùng đang chọn.

----- 

### ![](/icons/cube.webp) Làm tối các đối tượng không được chọn {#darken-unselected-objects}
Các đối tượng không được chọn sẽ bị làm tối để vùng đang chọn nổi bật lên.

### ![](/icons/shield.webp) Mặt nạ {#mask}
Màu dùng cho mặt nạ, mặc định là xám trung tính, được nhân với màu của đối tượng. Đặt thành trắng để mặt nạ trở nên vô hình, nhưng nhớ đổi lại thành xám khi xong việc nhé!

## ![](/icons/cursor.webp) Con trỏ {#cursor}

### Hình tròn {#show-circle-while-sculpting}
Khi nào hiển thị vòng tròn bán kính cọ:

* `Tự động` - hiện vòng tròn, nhưng ẩn đi khi bạn điêu khắc.
* `Không` - không bao giờ hiện vòng tròn.
* `Có` - luôn hiện vòng tròn, kể cả khi đang điêu khắc.

### Hiển thị điểm nhỏ {#show-small-dot}
Hiển thị một chấm nhỏ ở tâm nét cọ khi điêu khắc, hoặc khi tâm xoay của camera thay đổi.

### Hiển thị bộ ổn định dây {#show-rope-stabilizer}
Vẽ một đường thể hiện độ dài sợi dây khi [bộ ổn định dây lười](stroke.md#lazy-rope-stabilizer) đang bật trong cài đặt nét vẽ.

### Hiện gợi ý nghiêng camera {#show-roll-hint}
Hiện hướng dẫn chiều nghiêng khi bạn dùng một phím tắt nghiêng camera.

### ![](/icons/radius.webp) Kích thước {#dot-size}
Kích thước của chấm nhỏ.

### Màu sắc {#cursor-colors}
Con trỏ đổi màu tùy theo việc bạn đang làm: `Điêu khắc`, `Nền` (khi rê chuột trên nền), `Mặt nạ`, `Làm mịn`, `Máy ảnh` và `Bán kính`. Bạn có thể tùy chỉnh từng màu ở đây.

## ![](/icons/cursor.webp) Chỉ báo {#indicator}
![](/images/settings_indicator.webp)

Hiển thị chỉ báo trực quan cho các video hướng dẫn và quay màn hình. Đặt thành `Có` để bật (trên iOS còn có lựa chọn `Tự động`).

Các nút `Ngón tay`, `Bút cảm ứng` và `Chuột` sẽ hiển thị một biểu tượng khi phát hiện loại đầu vào tương ứng.

### Màu sắc {#indicator-color}
Màu của chỉ báo.

### Kích thước/Biểu tượng/Hình tròn {#indicator-shape}
Các điều khiển để chỉnh kích thước của chỉ báo, và độ mờ đục của biểu tượng và hình tròn bên trong chỉ báo.

## ![](/icons/wireframe.webp) Khung lưới {#wireframe}
![](/images/settings_wireframe.webp)
Bật lớp phủ khung lưới.

### Mục tiêu {#target}
Chọn hiển thị khung lưới cho các đối tượng không được chọn, chỉ các đối tượng được chọn, hay tất cả các đối tượng.

### Ẩn {#hide}
Chọn có hiển thị khung lưới cho các đa giác bị ẩn hay không.

### Đa phân giải: Chỉ cấp độ 0 {#multiresolution-level-0-only}
Đa phân giải hiển thị khung lưới của cấp 0 đậm hơn, và các cấp cao hơn nhạt dần. Khi bật, tùy chọn này chỉ hiển thị khung lưới của cấp 0.

### Màu sắc {#wireframe-color}
Đặt màu và độ mờ đục cho khung lưới.

## ![](/icons/grid.webp) Lưới {#grid}
![](/images/settings_grid.webp)
Bật lưới.

### Bắt dính {#snap}
Các tùy chọn này giúp các điểm của công cụ dạng đường cong và hình dạng (`Tiện`, `Ống`, hình đa giác và đường dẫn...) bắt dính khi bạn vẽ:

* `Bắt dính vào lưới` - bắt dính vào lưới.
* `Bắt dính vào điểm (chế độ xem căn chỉnh)` - bắt dính vào các điểm có sẵn ở gần khi camera được căn theo một trục.
* `Bắt dính vào điểm (chế độ xem tự do)` - bắt dính vào các điểm có sẵn ở gần khi camera không được căn theo trục.

### Màu sắc {#grid-color}
Đặt màu và độ mờ đục của lưới. Các tùy chọn này xuất hiện khi lưới đang hiển thị.

`Tối góc` làm lưới mờ dần về phía các mép. `Ngưỡng chia snap` đặt (tính bằng điểm ảnh) mật độ tối đa của các đường lưới trên màn hình trước khi lưới chuyển sang một cấp chia khác.

## ![](/icons/culling.webp)Hai mặt {#two-sided}
Cho phép nhìn thấy các mặt đa giác từ cả hai phía.

### Màu sắc mặt sau {#backface-color}
`Mặt sau có màu` bật việc nhuộm màu cho mặt sau, và `Màu sắc mặt sau` đặt màu nhuộm.

## ![](/icons/outline.webp)Bao viền {#outline}
Bật đường bao viền quanh các đối tượng được chọn.

### Màu bao viền, Độ dày {#outline-color-thickness}
Đặt màu và `Độ dày` của đường bao viền.


## ![](/icons/bang.webp) Nổi bật {#highlight}
Bật hiệu ứng nháy sáng ngắn khi vùng chọn thay đổi.
### Màu sắc, Thời lượng {#color-duration}
Đặt màu và thời lượng nháy sáng, tính bằng mili giây.

## ![](/icons/navigator.webp) Bộ điều hướng {#snap-cube}
![](/images/settings_snapcube.webp)

Hiển thị một biểu tượng trợ giúp ở góc cảnh, giúp nhanh chóng chuyển giữa các góc nhìn trước/sau/trái/phải/trên/dưới. Chạm vào các mặt của nó để chuyển giữa các góc nhìn trực giao.

### Hình dạng {#shape}
Chọn hình dạng cho bộ điều hướng: hình cầu, hình lập phương hoặc hệ trục (gnomon).

### Giới hạn căn chỉnh {#restrict-alignment}
Căn các góc nhìn bắt dính theo các trục thế giới. Khi bật, chỉ có thể dùng 6 góc nhìn chính. Ở chế độ `Tự động`, giới hạn này chỉ áp dụng khi camera ở chế độ `Bàn xoay`.

### Kích thước {#size}
Đặt kích thước của bộ điều hướng.

### Lật 180° {#flip-180}
Bật hành vi chạm: nếu góc nhìn đang được bắt dính, chạm vào tâm bộ điều hướng sẽ xoay góc nhìn 180 độ. Ví dụ, nếu góc nhìn đang bắt dính ở phía trước, chạm vào bộ điều hướng sẽ xoay sang góc nhìn phía sau.

### Cạnh và góc {#edges-corners}
Thêm các góc nhìn bắt dính ở các cạnh và góc (các vùng màu hổ phách). Không khả dụng với hình dạng hệ trục.

### Kéo kiểu bàn xoay {#turntable-drag}
Kéo bộ điều hướng sẽ xoay mà không làm nghiêng camera, và dừng lại ở mỗi góc nhìn bắt dính. Tắt đi để kéo bộ điều hướng theo kiểu xoay `Bi lăn`. Dù chọn cách nào, thao tác kéo vẫn chỉ theo chiều ngang hoặc dọc. Với camera `Bàn xoay`, bộ điều hướng luôn được kéo theo kiểu này.

### Vị trí {#snap-position}
Chọn góc màn hình đặt bộ điều hướng.


## ![](/icons/list.webp) Thống kê {#stats}
![](/images/settings_stats.webp)

Hiển thị thông tin về bộ nhớ hệ thống, tổng số đỉnh trong cảnh và số đỉnh của vùng đang chọn.

### Vị trí {#stats-position}
Chọn góc màn hình đặt phần thống kê.

## ![](/icons/edit_radius.webp) Tay cầm {#handle}
Cài đặt cho các tay cầm bạn kéo trong khung nhìn, chẳng hạn gizmo.

### Nhập số {#gizmo-input}
Cho phép nhập số khi chạm vào một trong các điều khiển của gizmo.

### Ẩn khi tương tác {#hide-on-interaction}
Làm mờ gizmo khi bạn đang thao tác với nó, để nó không cản tầm nhìn.

### ![](/icons/opacity.webp) Độ mờ {#handle-opacity}
Độ mờ đục của các tay cầm.

## ![](/icons/shape_lasso.webp) Hình dạng {#shape-settings}
Cách các hình bạn vẽ bằng nét vẽ dạng hình (lasso, chữ nhật, đường cong...) hiển thị trên màn hình.

### ![](/icons/opacity.webp) Phần tô, Đường viền {#shape-fill-outline}
Độ mờ đục của phần bên trong hình và của đường bao quanh nó.

### Màu sắc {#shape-colors}
Màu của hình cho từng loại công cụ: `Mặt nạ`, `Ẩn`, `Nhóm mặt` và `Cắt`.

## ![](/icons/array.webp) Trình lặp lại {#primitive-repeaters}
Giới hạn số bản sao do [trình lặp lại](scene#repeaters) tạo ra (mảng, xuyên tâm, đường cong, bề mặt). Chúng giúp Nomad luôn phản hồi nhanh khi một trình lặp lại vượt tầm kiểm soát.

### ![](/icons/cube.webp) Bản sao tối đa {#repeater-max-copies}
Số bản sao nhiều nhất mà một trình lặp lại tạo ra. Nomad gặp khó khăn với số lượng lớn đối tượng, dù kích thước của chúng thế nào.

### ![](/icons/cube.webp) Bản sao trong cảnh {#repeater-scene-copies}
Hạn mức bản sao cho toàn bộ cảnh. Một bản sao ít đa giác tốn ít hình học nhưng vẫn là một đối tượng đầy đủ, nên đây là giới hạn mà các bản sao nhỏ sẽ chạm tới đầu tiên.

### ![](/icons/triangle.webp) Mặt tối đa {#repeater-max-faces}
Hạn mức số mặt cho tất cả bản sao trong cảnh. Khi vượt quá, các đối tượng nặng nhất sẽ bị bớt bản sao trước.

## ![](/icons/multires.webp) Đa phân giải {#multires}
### Số lượng điểm đỉnh tối đa {#multires-lowres-count}
Đặt một ngưỡng để không cho phép thao tác chia nhỏ đa phân giải vượt quá số đỉnh này, vì điều đó có thể khiến Nomad bị treo: Nomad không kiểm tra bộ nhớ còn trống trước khi chia nhỏ. Mặc định là 10 triệu.
### Ngưỡng độ phân giải thấp {#multires-lowres-threshold}
Một phiên bản độ phân giải thấp hơn của lưới có thể được hiển thị khi bạn di chuyển camera. Bạn có thể tăng giá trị này nếu muốn hiển thị lưới ở độ phân giải cao hơn.

## Cài đặt {#advanced}
### ![](/icons/reset.webp) Đặt lại mặc định {#reset}
Đặt lại mọi cài đặt ưu tiên của ứng dụng về giá trị mặc định.

Một số tài nguyên được lưu riêng và KHÔNG bị đặt lại: dự án, phím tắt, thiết lập sẵn của công cụ, môi trường HDR, MatCap, alpha, kết cấu cọ và ảnh tham chiếu. Mọi thứ được lưu cùng dự án, như ánh sáng, hậu kỳ hay các góc nhìn camera, cũng được giữ nguyên.
