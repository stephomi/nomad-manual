# ![](/icons/cog.webp) Cài đặt 

Menu cài đặt chứa nhiều tùy chọn để điều khiển giao diện và hành vi của Nomad.

![](/images/settings_overview.webp)

## Cài đặt hiển thị
Phần này chứa các phím tắt khởi chạy nhanh cho hầu hết các cài đặt ở phía dưới menu này.

![](/images/settings_display_settings.webp)

### Tô mịn (Smooth Shading) 
Bật/tắt chế độ tô mịn và tô dạng mặt phẳng. Khi ở dạng mặt phẳng, các đa giác được tô độc lập, vì vậy bạn có thể thấy rõ topo bên dưới.
Việc xem tô dạng mặt phẳng có thể hữu ích trong giai đoạn điêu khắc, sau đó chuyển sang tô mịn để render.

Tắt Smooth Shading cải thiện hiệu năng một chút.

### Viền (Outline)
Bật/tắt đường viền quanh lựa chọn hiện tại của bạn.

Điều này hữu ích để nhận phản hồi trực quan về mesh đang được chọn trong trường hợp [Làm tối đối tượng không được chọn](#darken-unselected-objects) bị tắt.

Về mặt hiệu năng, sử dụng [Làm tối đối tượng không được chọn](#darken-unselected-objects) tốt hơn nhiều so với giải pháp dùng viền.

### Lưới (Grid)
Bật/tắt lưới nền, hữu ích để hiểu vị trí và tỉ lệ của đối tượng.

### Hai mặt (Two sided)
Bật/tắt hiển thị đa giác hai mặt. Tất cả các mặt đều hướng theo một hướng nhất định.
Các mặt được xem là *mặt sau (backface)* là những mặt hướng “ra xa” khỏi điểm nhìn của camera.

Ví dụ, hình cầu đơn giản khi khởi động sẽ có các mặt hướng ra bên ngoài.
Nếu bạn di chuyển camera vào bên trong hình cầu, bạn sẽ thấy mặt sau của các mặt này.

Hầu hết thời gian bạn không nên thấy phần mặt sau của các mặt, vì vậy tô màu chúng có thể giúp bạn phát hiện các vấn đề tiềm ẩn hoặc topo không đúng.

Tắt render `two sided` có thể cải thiện hiệu năng render một chút.


### Khung dây (Wireframe)
Bật/tắt lớp phủ khung dây. 

Lưu ý rằng bật khung dây sẽ làm giảm hiệu năng.

### Khối định hướng (Snap cube)
Bật/tắt biểu tượng trợ giúp ở góc khung cảnh, hữu ích để định hướng trong không gian và nhanh chóng chuyển giữa các góc nhìn trước/sau/trái/phải/trên/dưới.

### Hiển thị tô màu (Show Painting)
Bật/tắt hiển thị tô màu. Vật liệu mặc định được dùng là vật liệu trắng không kim loại, với độ nhám 25%.

### Dùng ẩn (Use Hide)
Bật/tắt chế độ ẩn. Khi tắt, nó vẫn tồn tại nhưng bị vô hiệu hóa. Nút này bị khóa nếu bạn đang dùng công cụ ẩn.

### Hiển thị mặt nạ (Show Mask)
Bật/tắt chế độ mặt nạ. Khi tắt, nó vẫn tồn tại nhưng bị vô hiệu hóa. Nhấn lại nút này để bật lại.

Nếu bạn cần ẩn mặt nạ NHƯNG vẫn muốn nó còn hiệu lực, hãy dùng màu mặt nạ bên dưới và đặt nó thành màu trắng. Hãy nhớ đổi lại thành màu xám khi xong việc!

Lưu ý rằng nút này bị khóa nếu bạn đang dùng công cụ mặt nạ. 

### Mask -> Opaque
Mask -> opaque sẽ bỏ qua các đỉnh trong suốt đối với mặt nạ đã được mask. Điều này chỉ liên quan đến độ trong suốt của vertex và texture, các mặt bị ẩn bởi “hide” vẫn sẽ bị ẩn.

### Nháy sáng (Highlight)
Bật/tắt hiệu ứng nháy sáng khi chọn. Khi chọn đối tượng, đối tượng được chọn sẽ nháy màu hồng đậm trong 500 mili giây. Màu và thời lượng nháy có thể tùy chỉnh bên dưới.

### Thống kê (Stats)
Bật/tắt hiển thị trạng thái dạng chữ trong khung nhìn 3D. Phần này hiển thị thông tin về bộ nhớ hệ thống, tổng số đỉnh trong cảnh, và số đỉnh của lựa chọn hiện tại.

----- 

### Làm tối đối tượng không được chọn
Các đối tượng không được chọn sẽ bị làm tối để lựa chọn hiện tại nổi bật hơn.

### Mặt nạ (Mask)
Màu dùng cho mặt nạ, mặc định là xám trung tính, được nhân với màu đối tượng của bạn. Đặt màu này thành trắng để làm mặt nạ vô hình, nhưng hãy nhớ đổi lại thành màu xám khi xong việc!

## ![](/icons/cursor.webp) Con trỏ

### Hiện vòng tròn khi điêu khắc
Tiếp tục hiển thị bán kính cọ khi điêu khắc.

### Hiện chấm nhỏ
Hiển thị một chấm ở tâm nét cọ khi điêu khắc, hoặc khi điểm xoay của camera thay đổi.

### Hiện dây ổn định
Vẽ một đường để chỉ độ dài dây khi chế độ ổn định dây (lazy rope stabilizer) được bật trong cài đặt stroke.

## ![](/icons/cursor.webp) Chỉ báo (Indicator)
![](/images/settings_indicator.webp)

Hiển thị các chỉ báo trực quan cho hướng dẫn và ghi hình màn hình.

Các nút `Finger`, `Stylus` và `Mouse` sẽ bật hiển thị biểu tượng khi phát hiện loại đầu vào tương ứng.

### Màu (Color)
Màu của chỉ báo.

### Kích thước/Biểu tượng/Vòng tròn (Size/Icon/Circle)
Các điều khiển để chỉnh kích thước của chỉ báo và các hình dạng bên trong chỉ báo.

## ![](/icons/wireframe.webp) Khung dây (Wireframe)
![](/images/settings_wireframe.webp)
Bật lớp phủ khung dây.

### Mục tiêu (Target)
Đặt xem các đối tượng không được chọn có hiển thị khung dây hay không, hoặc chỉ đối tượng được chọn, hoặc tất cả đối tượng.

### Ẩn (Hide)
Đặt xem khung dây có tiếp tục hiển thị cho các đa giác bị ẩn hay không.

### Đa phân giải: Chỉ cấp 0 (Multiresolution: Level 0 only)
Đa phân giải sẽ hiển thị khung dây cho cấp 0 đậm hơn, và các cấp cao hơn nhạt dần. Khi bật, tùy chọn này sẽ chỉ hiển thị khung dây cấp 0.

### Màu (Color)
Đặt màu và độ trong suốt cho khung dây.

## ![](/icons/grid.webp) Lưới (Grid)
![](/images/settings_grid.webp)
Bật lưới.

### Màu (Color)
Đặt màu và độ trong suốt của lưới.

### Bám lưới (Snap)
Bật bám lưới cho các công cụ dựa trên đường cong.

## ![](/icons/culling.webp)Two sided
Bật khả năng nhìn thấy các mặt đa giác từ cả hai phía.

### Tô màu mặt sau, Màu mặt sau (Color Backface, Backface Color)
Bật tô màu cho các mặt sau, và đặt màu tô.

## ![](/icons/outline.webp)Outline
Bật đường viền quanh đối tượng đang hoạt động.

### Màu viền, Độ dày (Outline color, Thickness)
Đặt màu và độ dày của đường viền.


## ![](/icons/bang.webp) Highlight
Bật nháy sáng ngắn khi đối tượng đang hoạt động thay đổi.
### Màu, Thời lượng (Color, Duration)
Đặt màu và thời lượng nháy tính bằng mili giây.

## ![](/icons/snap_cube.webp) Khối định hướng (Snap cube)
![](/images/settings_snapcube.webp)

Hiển thị biểu tượng trợ giúp ở góc khung cảnh, hữu ích để nhanh chóng chuyển giữa các góc nhìn trước/sau/trái/phải/trên/dưới. Chạm vào các mặt của khối để chuyển giữa các góc nhìn trực giao.

### Hình dạng (Shape)
Chọn giữa hình khối, hình cầu, hoặc dạng gnomon cho khối định hướng.

### Hạn chế căn chỉnh (Restrict alignment)
Bật khóa xoay camera khi kéo trên khối định hướng. Khi bật, thao tác kéo trên khối định hướng sẽ chỉ đi trái/phải hoặc lên/xuống.

### Kích thước (Size)
Đặt kích thước của khối định hướng.

### Lật 180 (Flip 180)
Bật hành vi chạm sao cho nếu góc nhìn đang được “snap”, chạm vào tâm khối sẽ xoay góc nhìn 180 độ. Ví dụ nếu góc nhìn đang ở phía trước, chạm vào khối sẽ xoay sang góc nhìn phía sau.

### Vị trí (Position)
Đặt góc mà khối định hướng sẽ nằm trong đó.


## ![](/icons/edit_radius_n.webp) Thống kê (Stats)
![](/images/settings_stats.webp)

Hiển thị thông tin về bộ nhớ hệ thống, tổng số đỉnh trong cảnh, và số đỉnh của lựa chọn hiện tại.

### Vị trí (Position)
Đặt góc mà phần thống kê sẽ nằm trong đó.

## Primtive/Repeaters
## Nhập số (Numerical input)
Cho phép nhập số khi chạm vào các widget của gizmo.

## Đa phân giải (Multiresolution)
### Giới hạn số đỉnh tối đa (Max vertices count)
Đặt ngưỡng để không cho phép thao tác chia nhỏ đa phân giải vượt quá số đa giác này, vì có thể làm Nomad bị crash. Mặc định là 10 triệu.
### Ngưỡng độ phân giải thấp (Low resolution threshold)
Một độ phân giải thấp hơn của mesh có thể được hiển thị khi bạn di chuyển camera. Bạn có thể tăng giá trị này nếu muốn hiển thị độ phân giải cao hơn của mesh.

## Cài đặt (Settings)
### Đặt lại mặc định (Reset to default)
Đặt lại tất cả cài đặt về giá trị mặc định.
