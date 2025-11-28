# ![](/icons/pencil.webp) Nét vẽ {#stroke}

---
![](/images/stroke_overview.webp) 

## Tổng quan {#overview}

Bạn có thể tùy chỉnh hành vi nét vẽ của hầu hết các cọ công cụ.
Các thiết lập tương tự như trong các ứng dụng vẽ 2D, tuy nhiên một số tùy chọn là đặc thù cho điêu khắc và 3D.

Các tùy chọn được chia thành 5 menu con:

| Tên      | Biểu tượng                   | Mô tả                                                                 |
| :------: | :--------------------------: | :-------------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | Điều khiển cách nét vẽ được áp dụng lên mô hình                      |
| Alpha    | ![](/icons/alpha.webp)      | Cách một texture thang xám được dùng cho dấu cọ                      |
| Falloff  | ![](/icons/falloff.webp)    | Điều khiển cách độ mạnh cọ thay đổi từ tâm ra mép                    |
| Filter   | ![](/icons/filter.webp)     | Cách cọ bị ảnh hưởng bởi hình học của mô hình                        |
| Pressure | ![](/icons/pressure.webp)   | Điều khiển phản hồi theo lực nhấn bút                                |

::: tip
Không phải mọi tùy chọn nét vẽ đều áp dụng cho mọi công cụ. Các tùy chọn nét vẽ không được công cụ hiện tại sử dụng sẽ bị vô hiệu hoặc ẩn đi. 
:::


## Nét vẽ {#stroke-1}

### Bán kính {#radius}

![](/images/stroke_radius.webp)

#### Chia sẻ bán kính {#share-radius}

Khi bật, tất cả công cụ sẽ dùng chung một bán kính, mặc định là mỗi công cụ có bán kính riêng.

#### Kích thước {#size}

* Screen - bán kính được đặt theo đơn vị màn hình. Nếu bạn đặt bán kính rộng 100 pixel, nó sẽ luôn là 100 pixel bất kể bạn phóng to hay thu nhỏ.
* Constant (3d) - bán kính được đặt theo đơn vị 3D. Ví dụ nếu bạn tạo một hình cầu và đặt bán kính bằng kích thước hình cầu, bán kính sẽ giữ nguyên kích thước so với hình cầu khi bạn phóng to/thu nhỏ.


### Nét vẽ {#stroke-type}

![](/images/stroke_strokemode.webp)

Nét vẽ có thể hoạt động ở nhiều chế độ:

### ![](/icons/stroke_dot.webp) Chấm {#dot}
Kéo như một nét vẽ sơn thông thường. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Lăn {#roll}
Alpha của cọ sẽ xoay theo hướng nét vẽ, hữu ích để tạo đường chỉ vải. 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lock + radius
Đóng dấu một nét cọ với **_chiều cao_** cố định. Kéo để đặt tỉ lệ và góc xoay.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) Khóa + cường độ {#lock-intensity}
Đóng dấu một nét cọ với **_bán kính_** cố định. Kéo để đặt chiều cao và góc xoay.
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

Công cụ `Move` và `Drag` có 3 tùy chọn riêng:

### ![](/icons/snake.webp) Kéo {#drag}

Sẽ liên tục cập nhật những gì nằm trong bán kính cọ trong suốt nét vẽ. Một nét vẽ nhanh sẽ để bề mặt lại phía sau, trong khi nét chậm sẽ giữ vật liệu, tạo ra các hình dạng dài hơn. Đây là chế độ mặc định cho công cụ `Drag`. Với `Dynamic Topology` điều này có thể dùng để tạo các khối đùn giống rắn. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Nắm {#grab}
Sẽ chọn những gì nằm trong bán kính cọ khi bắt đầu nét vẽ, và giữ nguyên vùng chọn đó. Điều này hữu ích cho các thao tác di chuyển chính xác hơn, vì bạn có thể điều chỉnh cẩn thận khoảng cách di chuyển và không vô tình di chuyển nhiều hơn vùng đã chọn ban đầu. Đây là chế độ mặc định cho công cụ `Move`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Khóa + bán kính (kéo) {#lock-radius-drag}
Bán kính do người dùng đặt sẽ bị bỏ qua, và được đặt động dựa trên khoảng cách kéo nét vẽ so với điểm bắt đầu. Khoảng cách nhỏ = bán kính nhỏ, khoảng cách lớn = bán kính lớn. Dùng thanh trượt cường độ để điều khiển hình dạng falloff. Hữu ích để chặn khối các hình dạng hữu cơ, mềm dẻo.
![](/videos/stroke_lockradius_drag.mp4) 



### Điều chỉnh cường độ khoảng cách {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Các nét vẽ với khoảng cách dấu thấp (dưới 50%) có thể tích lũy nhanh, tạo nét mạnh hơn so với giá trị khoảng cách cao. Tùy chọn này sẽ bù trừ, để các nét có cường độ xấp xỉ như nhau bất kể khoảng cách dấu.

### Khoảng cách nét vẽ {#stroke-spacing}
Khoảng cách giữa mỗi dấu cọ được áp dụng trong khi kéo. Giá trị dưới 100% sẽ chồng lấp, tạo cảm giác nét liên tục. Giá trị trên 100% sẽ bắt đầu tạo khoảng trống, hữu ích để điêu khắc chi tiết như đường chỉ may hoặc khóa kéo.

### Dây ổn định (lazy rope) {#lazy-rope-stabilizer}
Nét vẽ sẽ trễ so với vị trí con trỏ một khoảng nhất định. Có thể dùng để vẽ đường mượt.
![](/videos/stroke_lazy_rope.mp4) 

### Làm mượt nét vẽ {#stroke-smoothing}
Lấy trung bình nhiều vị trí con trỏ để có nét vẽ mượt hơn.
Với giá trị cao, nét vẽ sẽ trễ so với con trỏ nhưng cuối cùng sẽ bắt kịp.
Hữu ích để vẽ đường mượt.

### Bán kính bắt dính {#snap-radius}
Bắt đầu nét vẽ mới dính vào điểm kết thúc của nét trước. Bán kính xác định khoảng cách tìm điểm kết thúc nét trước. Hữu ích khi vẽ các đường dài liên tục nhưng thường xuyên tạm dừng.

### ![](/icons/silhouette.webp) Silhouette {#silhouette}
![](/images/stroke_silhouette.webp)
Mặc định, nét vẽ chỉ ảnh hưởng bề mặt mô hình trong bán kính cọ. Khi bật silhouette, nét vẽ sẽ được chiếu xuyên suốt toàn bộ mô hình. Điều này rất hữu ích khi chặn khối ban đầu cho mô hình, hoặc cho các hình dạng cần các mặt bên giữ vuông góc.

Hướng chiếu có thể được đặt tường minh, phương pháp mặc định 'Closest' sẽ phát hiện góc tốt nhất tương đối với góc nhìn. 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp) Ngẫu nhiên {#randomize}

![](/images/stroke_randomize.webp)

Cường độ, tịnh tiến, xoay và tỉ lệ của nét vẽ đều có thể được ngẫu nhiên hóa. Điều này có thể dùng để tạo nhiều hiệu ứng, ví dụ randomize với công cụ paint có thể tạo màu loang lổ, hoặc randomize với công cụ crease có thể dùng để tạo chi tiết da.

![](/videos/stroke_randomize.mp4) 

### Độ lệch nét vẽ {#stroke-offset}

Áp dụng một độ lệch cố định cho nét vẽ. Hữu ích cho màn hình nhỏ nơi ngón tay bạn che mất nét vẽ. 


## ![](/icons/alpha.webp) Alpha {#alpha}
![](/images/stroke_alpha.webp) 

`Alpha` là một texture sẽ điều biến hành vi cọ.
Đó là một ảnh thang xám, trong đó pixel đen nghĩa là không biến dạng và pixel trắng là biến dạng tối đa.

Nhấn vào ảnh alpha để thay đổi nó.

Nhấn vào phần xem trước vật liệu để tải alpha từ preset vật liệu. Bạn cũng có thể lưu preset vật liệu tại đây, và chọn nhúng texture cùng với công cụ.

::: tip
Texture không bao giờ bị đổi kích thước, nên texture lớn có thể làm chậm hiệu năng.
:::

### Đảo ngược điểm ảnh {#invert-pixels}
Đảo ngược giá trị ảnh, pixel đen thành trắng và trắng thành đen.

::: tip

Các alpha tích hợp đi kèm Nomad không thể bị đảo ngược.

:::

### Tỷ lệ {#scaling}

Kích thước cọ trong Nomad là một hình tròn với bán kính do người dùng đặt. Texture thường là hình vuông hoặc chữ nhật, các tham số `Scaling` cho phép bạn quyết định texture sẽ khớp với hình tròn như thế nào. Với texture vuông, giá trị 0.7 sẽ vừa khít trong hình tròn. Giá trị 1 sẽ phóng texture lớn hơn để hình tròn nằm bên trong, cắt bớt các cạnh.

![](/images/alpha_scaling.webp) 

Bật `Scaling - Y` sẽ cho phép bạn kéo giãn alpha theo chiều dọc.

![](/images/alpha_scaling_y.webp) 

### Xoay {#rotation}

Texture alpha sẽ xoay theo hướng nét vẽ. Bạn có thể thêm một góc xoay bù, và nếu biểu tượng khóa được bật, texture sẽ giữ cố định góc xoay này tương đối với màn hình.

### Lặp ô (tiling) {#tiling}
![](/images/stroke_tiling.webp) 

Tần suất lặp lại texture trong biên dạng cọ. Các chế độ tiling cho phép giới hạn một texture duy nhất trong nét vẽ, hoặc lặp lại nhiều texture, hoặc lặp đối xứng nơi mỗi texture thứ hai bị lật để tạo hoa văn hoặc giúp tạo texture liền mạch.

![](/videos/alpha_tiling.mp4) 



### Giá trị trung gian {#mid-value}

Mặc định, pixel đen nghĩa là không biến dạng, và pixel trắng nghĩa là biến dạng dương tối đa, ví dụ, một cọ clay với texture alpha đá sẽ chỉ kéo bề mặt ra nơi alpha không đen.

Nếu bạn muốn cọ đẩy bề mặt vào, hoặc vừa đẩy vào VỪA kéo ra, bạn có thể chỉnh mid value. Nếu đặt giá trị 0.5, vùng xám trung tính trong alpha sẽ không làm gì, giá trị đen sẽ đẩy vào, trắng sẽ kéo ra.




## Độ rơi (Falloff) {#falloff}

![](/images/falloff_menu.webp) 

Tương tự [Alpha](#alpha), ngoại trừ việc bạn điều khiển cường độ bằng một đường cong. Nó được kết hợp với alpha để bạn có thể dùng texture cho chi tiết, và falloff để điều khiển độ mờ mép và cường độ ở tâm cọ.

Khi đường cong ở phía trên, đó là biến dạng tối đa, khi ở phía dưới cọ không có tác dụng.

Bạn có thể hình dung đường cong như một lát cắt qua đầu cọ. Phần dưới cho xem trước một 'dấu' cọ đơn lẻ sẽ trông thế nào trên bề mặt mô hình, và nếu cọ có texture alpha, nó cũng sẽ được hiển thị để xem trước cách falloff và alpha tương tác.

### Mẫu dựng sẵn {#preset}
Khi chọn mục này, nhấn vào biểu đồ đường cong sẽ mở menu preset. Đường cong bo tròn cho kết quả mềm hơn, đường cong góc cạnh cho kết quả sắc hơn. Nút `Sub` trong thanh công cụ bên trái sẽ đảo ngược falloff, nên đỉnh đường cong sẽ đẩy vào bề mặt thay vì kéo ra, hoặc ngược lại.

### Catmull-Rom {#catmull-rom}
Khi chọn, người dùng có thể tự vẽ đường cong falloff. Trình chỉnh sửa đường cong hoạt động giống các đường cong khác trong Nomad:

* Nhấn vào đường cong để tạo điểm mới
* Kéo một điểm để di chuyển
* Nhấn vào điểm để chuyển giữa nhọn và mượt
* Kéo một điểm chồng lên điểm lân cận để xóa nó

### B-spline {#b-spline}
Khi chọn, người dùng có thể tự vẽ đường cong falloff. Trình chỉnh sửa hoạt động giống Catmull-Rom, nhưng các điểm ảnh hưởng đến đường cong thay vì nằm trực tiếp trên đường, giúp tạo hình đường cong mượt hơn.

Trình chỉnh sửa đường cong có 3 nút:

| Mục      | Biểu tượng                   | Mô tả                                       |
| :------: | :-------------------------: | :-----------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | Mở rộng trình chỉnh sửa đường cong          |
| Reset    | ![](/icons/reset.webp)     | Đưa đường cong về trạng thái mặc định       |
| Symmetry | ![](/icons/symmetric.webp) | Hiển thị đường cong như 'đầu cọ' đối xứng   |


### Ảnh hưởng {#influence}

* Sphere (3d) - Ảnh hưởng được tính bằng khoảng cách từ đỉnh (vertex) đến tâm cọ.
* Circle (2d) - Đỉnh được chiếu lên mặt phẳng vùng tác động trước, rồi mới lấy khoảng cách đến tâm cọ. Tương tự cách alpha được lấy mẫu. 
* Cylinder - Ảnh hưởng được chiếu xuyên qua vùng tác động như một hình trụ, được dùng bởi chế độ Silhouette bên dưới.

### Silhouette {#silhouette-1}
Mặc định, nét vẽ chỉ ảnh hưởng bề mặt mô hình trong bán kính cọ. Khi bật silhouette, nét vẽ sẽ được chiếu xuyên suốt toàn bộ mô hình. Điều này rất hữu ích khi chặn khối ban đầu cho mô hình, hoặc cho các hình dạng cần các mặt bên giữ vuông góc.



## Bộ lọc {#filter}

![](/images/filter_menu.webp) 

### Tích lũy nét vẽ {#accumulate-stroke}
Bật không giới hạn lượng vật liệu có thể thêm/bớt mỗi nét. Ví dụ công cụ `Clay` bật tùy chọn này, nên vật liệu có thể tiếp tục tích tụ, trong khi công cụ `Brush` tắt, nên nét vẽ sẽ ngừng thêm vật liệu nếu bạn tiếp tục đi lại trên cùng vùng lưới. 

### Chỉ đỉnh hướng ra trước {#front-facing-vertex-only}
Tùy chọn này sẽ bỏ qua các đỉnh quay lưng.
Hữu ích nếu bạn muốn tô một phần hình học mỏng mà không ảnh hưởng mặt bên kia.
Nó cũng hoạt động với điêu khắc nhưng có thể xuất hiện một số artefact.

### Cho phép topology động {#allow-dynamic-topology}
Tùy chọn này chỉ khả dụng nếu lưới của bạn ở chế độ [Dynamic Topology](topology.md#dynamic-topology). Bạn có thể bật/tắt dynamic topology theo từng công cụ.

### Topology được nối {#connected-topology}
Chỉ điêu khắc các đỉnh được liên kết với bề mặt bạn chạm bằng công cụ. Ví dụ khi dùng với công cụ `Move`, điều này cho phép bạn di chuyển một phần ngay cả khi nó giao nhau với phần khác.
![](/videos/connected_topology.mp4)

### Bảo vệ vùng {#protect-area}
![](/images/filter_protect_area.webp) 

Các tùy chọn này sẽ ngăn công cụ ảnh hưởng các phần của lưới trong những điều kiện khác nhau. 

Tùy chọn 'Auto' nghĩa là nếu bạn có hide, mask, hoặc facegroup hiển thị trong menu [Shading](shading), chúng sẽ được bảo vệ, nhưng nếu chúng bị tắt trong menu đó, bảo vệ sẽ bị vô hiệu.

* `All` - Bật/tắt để đặt các bộ lọc bảo vệ là toàn cục hay theo từng công cụ.
* `Hide` - Nếu một phần lưới bị ẩn bằng công cụ hide, đặt xem chúng có được bảo vệ hay không.
* `Mask` - Nếu một phần lưới bị mask, đặt xem chúng có được bảo vệ hay không.
* `Facegroup` - Đặt xem bạn chỉ có thể dùng công cụ trong facegroup đầu tiên được chạm hay không.


### Giữ cạnh sắc {#keep-sharp-edges}
Loại trừ các điểm có pháp tuyến khác quá nhiều so với pháp tuyến bề mặt.

Nó sẽ thay đổi cách tính mặt phẳng vùng (Area sampling).

Tùy chọn này hữu ích cho các công cụ dựa trên làm phẳng, hoặc nếu bạn muốn tô màu một bề mặt gần như phẳng mà không bị lem.

![](/videos/filter_keep_sharp_edges.mp4)

### Lấy mẫu vùng {#area-sampling}
Một số cọ hoặc tùy chọn nét vẽ cần một pháp tuyến mặt phẳng và vị trí mặt phẳng trên bề mặt để hoạt động.

Bạn có thể điều khiển cách tính mặt phẳng trung bình này bằng cách đặt vùng lấy mẫu theo tỉ lệ bán kính công cụ.

Ở 100%, mọi điểm trong vòng tròn chọn đều được tính.

Ở 0%, chỉ đỉnh hoặc tam giác gần nhất được tính. Các giá trị này có thể được liên kết cho cả `Normal radius` và `Position radius`, hoặc tách ra và đặt độc lập.


### Mặt nạ độ sâu {#depth-masking}
![](/images/stroke_depthmask.webp)

Loại trừ các điểm nằm trên hoặc dưới một khoảng cách nhất định so với mặt phẳng đã tính (Area sampling).

Điều này có thể dùng để tô chỉ trên vùng lồi, hoặc chỉ trên vùng hõm.

Biểu đồ biểu diễn lát cắt ngang bề mặt; đường ngang là vị trí bề mặt, vòng tròn biểu diễn bán kính falloff tô màu tương đối phía trên và dưới bề mặt. `Height offset` là phần trăm trên hoặc dưới bề mặt để bắt đầu tính mask. `Top area` và `Bottom area` cho phép bạn tỉ lệ hóa falloff phía trên và dưới điểm offset.

#### Ví dụ: Tô trong hốc {#example-paint-in-cavities}
Để chỉ tô vùng hốc, đặt height offset -100%, và chỉnh thanh trượt top area sao cho nó cách xa đường ngang. Điều này nghĩa là cú nhấp đầu tiên đặt độ sâu 'zero', và chỉ các vùng dưới độ sâu này mới bị ảnh hưởng.

![](/videos/stroke_depth_cavity.mp4)

#### Ví dụ: Tô trên chỗ lồi {#example-paint-on-bumps}
Để chỉ tô vùng cao, đặt height offset +90%, sao cho đáy vòng tròn cắt đường ngang một đoạn nhỏ. Khi bạn nhấp lên đỉnh vùng 'cao', điều này sẽ đặt độ sâu, để mọi thứ ở độ sâu đó, cộng một chút bên dưới, và mọi thứ cao hơn, sẽ được tô. Các hốc sâu sẽ bị bỏ qua.
![](/videos/stroke_depth_bump.mp4)


## Lực nhấn {#pressure}
![](/images/pressure_menu.webp) 

Điều khiển cách lực nhấn bút/stylus ảnh hưởng đến cọ.

Mặc định `Use global settings` được bật, nghĩa là mọi cọ sẽ chia sẻ cùng giá trị pressure.

### Lực nhấn - Bán kính {#pressure-radius}

Đường cong này điều khiển cách bán kính cọ bị ảnh hưởng bởi lực nhấn. Mặc định là quan hệ tuyến tính, nên nếu stylus của bạn phản hồi mượt, thay đổi bán kính cũng sẽ cảm giác mượt. Tuy vậy, nhiều stylus có phản hồi phi tuyến, bạn có thể bù trừ bằng đường cong này. Ví dụ, nếu bán kính không đạt giá trị tối đa ở lực nhấn cao, hãy dùng preset đường cong như 'out-pow3', với độ cong hướng lên, để tăng bán kính sớm hơn.

Hộp thoại này tương tự hiển thị đường cong falloff, bạn có thể dùng preset bằng cách chạm vào cửa sổ đường cong, hoặc tự vẽ đường với chế độ Catmull-Rom và B-Spline.

Nếu bạn muốn bán kính cố định, hãy tắt mục này.

### Lực nhấn - Cường độ {#pressure-intensity}

Tương tự thanh trượt bán kính, nhưng để điều khiển cường độ. Nếu bạn muốn cường độ cố định, hãy tắt mục này.

### Làm mượt lực nhấn {#pressure-smoothing}

Lấy trung bình các sự kiện lực nhấn stylus để có kết quả mượt hơn.