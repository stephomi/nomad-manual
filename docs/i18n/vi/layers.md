# ![](/icons/layer.webp) Lớp {#layers}

Menu này chứa ngăn xếp lớp, một cách lưu các chỉnh sửa trên đối tượng mà không phá hủy dữ liệu, cùng nhiều cách để kết hợp và tái sử dụng các lớp.

![](/images/layers_overview.webp) 

## Tổng quan {#overview}

Lớp trong Nomad phục vụ nhiều mục đích.

Thông tin vẽ (Màu sắc, Độ nhám, Độ kim loại, Độ mờ đục) hoạt động với lớp giống như trong các ứng dụng vẽ 2d. Bạn có thể tạo một lớp và vẽ lên mô hình. Lớp có thể bật hoặc tắt, chỉnh độ mờ đục, nhân đôi, đổi thứ tự trong ngăn xếp lớp, và đổi chế độ hòa trộn.

Nomad cũng dùng lớp cho điêu khắc. Một lớp có thể lưu những chi tiết nhỏ như nếp nhăn, hoặc lưu những thay đổi lớn, giúp chúng hoạt động như blendshape/shape key/morph target trong các ứng dụng 3d khác. Ví dụ, bạn có thể điêu khắc các biểu cảm khuôn mặt khác nhau trên các lớp khác nhau, rồi chỉnh thanh trượt của các lớp để kết hợp chúng thành những biểu cảm mới.

Trong trường hợp này, các thay đổi lưu trong lớp chỉ đơn thuần được cộng dồn, thứ tự lớp không quan trọng như với phần vẽ.

Bạn có thể xóa một phần của lớp bằng công cụ [Xóa Lớp](tools.md#delete-layer), và cũng có thể dùng lớp để tạo mặt nạ dựa trên các thông tin khác nhau được lưu trong lớp.

![](/videos/layer.mp4)

::: tip
Khác với hầu hết phần mềm điêu khắc, thay đổi tô pô của lưới sẽ không làm mất các lớp. Bạn có thể dùng [Remesh voxel](topology.md#voxel-remesher), [Đa phân giải](topology.md#multiresolution) hoặc các công cụ [Cắt](tools.md#trim)/[Tách](tools.md#split), nhưng lưu ý rằng khi dùng [Remesh voxel](topology.md#voxel-remesher), chất lượng của lớp sẽ bị ảnh hưởng.
:::

::: tip
Nếu bạn dùng lớp làm blendshape/morph target, [menu Cảnh](scene.md#object-menu) có thêm các tính năng cho lớp: bạn có thể tách các lớp thành đối tượng riêng, và gộp các đối tượng tương ứng thành lớp.
:::
----

## Menu lớp {#layer-menu}

![](/images/layers_menu.webp)

Tiêu đề hiển thị tên của đối tượng được chọn. Lớp không khả dụng cho các hình cơ bản, vì vậy hãy hoàn tất hình cơ bản trước.

Nhấn `Thêm lớp` để tạo một lớp mới. `Gộp các lớp` gộp mọi lớp vào lưới gốc; con số cạnh biểu tượng của nó cho biết có bao nhiêu lớp.

Mỗi lớp có một tên, một thanh trượt điều khiển độ mạnh/hệ số, và các nút tùy chọn. Chạm vào một lớp để biến nó thành lớp đang hoạt động: mọi thao tác điêu khắc và vẽ sẽ đi vào lớp đó. Chạm vào `Nền tảng` để quay lại làm việc trên lưới gốc.

### ![](/icons/sort_right.webp) Mở rộng danh sách {#ui-expand-list}

Theo mặc định, danh sách lớp chỉ hiển thị chế độ hiển thị, chế độ hòa trộn và độ mạnh của mỗi lớp, còn lớp đang hoạt động được mở rộng với đầy đủ điều khiển. Mũi tên bên trái tiêu đề sẽ mở rộng đầy đủ điều khiển cho mọi lớp.

![](/images/layers_expand.webp)

### Tùy chọn {#options}

| Thao tác     | Biểu tượng                   | Mô tả                                               |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Có thể thấy  | ![](/icons/eye_open.webp)   | Hiện/ẩn lớp                                         |
| Chế độ hòa trộn | ![](/icons/opacity.webp) | Chế độ hòa trộn kiểu Photoshop. 4 biểu tượng hiển thị chế độ cho Màu sắc, Độ nhám, Độ kim loại, Độ mờ đục. |
| Đổi tên      | ![](/icons/pencil.webp)     | Sửa tên lớp                                         |
| Xóa          | ![](/icons/trash.webp)      | Xóa lớp                                             |
| Nhân bản     | ![](/icons/clone.webp)      | Nhân đôi lớp                                        |
| Ghép dưới    | ![](/icons/merge_down.webp) | Ghép lớp với lớp bên dưới (hoặc lưới gốc)           |
| Thêm         | ![](/icons/more.webp)       | Tùy chọn [Thêm...](#more)                           |

Khi một lớp không được mở rộng, `Đổi tên`, `Xóa`, `Nhân bản` và `Ghép dưới` nằm trong menu [Thêm...](#more) của nó.

Để chuyển một lớp sang vị trí khác trong ngăn xếp lớp, nhấn giữ trên tên của nó rồi kéo.

### Nền tảng {#base}

Nút 3 chấm của hàng `Nền tảng` chuyển phần vẽ của lưới gốc sang một lớp mới, bằng nút `Nền tảng → Lớp`. Lưới gốc sau đó được đặt lại về vật liệu nền. Rất tiện khi bạn đã vẽ nhiều trước khi tạo bất kỳ lớp nào.

* Các nút mặt nạ và ẩn bên cạnh giữ nguyên các vùng bị che mặt nạ và bị ẩn.
* `Chiết xuất` - các kênh cần chuyển: `Màu sắc`, `Độ mờ`, `Độ nhám` và `Độ kim loại`.
* `Vật liệu nền` - nếu bật, chỉ những giá trị khác với vật liệu này mới được chuyển. Đặt nó bằng các thanh trượt, hoặc lấy từ mô hình bằng ống hút màu.

### ![](/icons/more.webp) Thêm... {#more}

Nút 'Thêm...' hiển thị các tùy chọn bổ sung cho lớp hiện tại, trong hai thẻ: cài đặt (biểu tượng bánh răng) và chiết xuất (biểu tượng khối lập phương).

![](/images/layers_more.webp) 

#### Các yếu tố kênh {#channel-factors}

Các điều khiển này cho phép bạn điều chỉnh lượng điêu khắc/màu/độ nhám/độ kim loại/độ mờ đục của lớp. Các giá trị này được nhân với thanh trượt hệ số của lớp, nên ví dụ nếu độ mạnh của lớp là 1 mà hệ số kênh màu là 0.5, thì màu hiển thị sẽ ở độ mạnh 0.5.

`Độ lệch` điều khiển độ mạnh điêu khắc của lớp. Trong khi màu/độ nhám/độ kim loại bị giới hạn trong khoảng 0 đến 1, độ lệch có thể là bất kỳ giá trị nào, cả dương lẫn âm.

::: tip
Độ lệch có thể biến một lớp chỗ lồi thành một lớp chỗ lõm, hay một nụ cười thành cái cau mày:
![](/videos/layer_happysad.mp4)


Một lớp đối xứng có thể được nhân bản rồi tách thành hai hình trái/phải bằng Xóa Lớp:
![](/videos/layer_leftright.mp4)

Các lớp có hệ số độ lệch âm có thể được bake xuống các lớp trống để tạo ra những hình khối dương mới.

Các lớp có hệ số độ lệch dương lớn hơn 1 có thể dùng để thử nghiệm những blendshape cực đoan hơn.
:::

::: warning
Hiện tại, các lớp chỉ dùng chung một kênh độ mờ đục cho cả 3 kênh (màu/độ kim loại/độ nhám).
Nếu bạn gộp nhiều lớp có cường độ theo từng kênh chưa ở mức tối đa, kết quả cuối cùng có thể trông khác đi.

Có thể trong tương lai, mỗi kênh sẽ có kênh alpha riêng để loại bỏ giới hạn này.
:::


#### ![](/icons/shield.webp) Mặt nạ {#mask}
Nút mặt nạ cạnh mỗi thanh trượt sẽ tạo mặt nạ từ kênh đó. Tương tự việc dùng lớp để tạo vùng chọn trong các ứng dụng vẽ, nó cho phép bạn tái sử dụng công sức đã làm trong một lớp cho các thao tác khác.

#### ![](/icons/preview.webp) Xem trước {#preview}
![](/images/layers_preview.webp) 

Các tùy chọn sau nằm trong thẻ chiết xuất của menu 'Thêm...'.

Khi bật, nó sẽ xem trước các cài đặt chiết xuất của lớp này (xem phần tiếp theo).

`X-quang` chọn những đối tượng được làm trong suốt khi xem trước (`Không có`, `Không được chọn`, `Đã chọn` hoặc `Tất cả`), để hình được chiết xuất vẫn hiển thị đặc. Nó hữu ích khi bạn dùng chiều cao chiết xuất âm.

#### ![](/icons/mask_extract.webp) Chiết xuất {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Nút `Chiết xuất` sẽ nhân đôi nội dung của lớp thành một đối tượng mới, thường kèm một độ dày do bạn chỉ định ở phần tiếp theo.

`Hành động đóng` quyết định cách thực hiện việc nhân đôi:

* `Không có` - Chỉ chiết xuất phần đó, không tạo thành bên hay lấp lỗ nào.
* `Lấp đầy` - Lỗ được lấp đầy và làm mịn bằng các tam giác. Đừng dùng tùy chọn này cho các bề mặt phẳng.
* `Lớp vỏ` - Đóng hình được chiết xuất theo giá trị độ dày và các tùy chọn hướng.
* `Lớp` - Chiết xuất phần chênh lệch của lớp.

#### ![](/icons/height.webp) Chiều cao {#thickness}
![](/images/layers_thickness.webp) 

Độ sâu của phần đùn lớp vỏ. Giá trị dương mọc ra khỏi bề mặt, giá trị âm lún vào trong bề mặt. Nó bị ẩn khi hành động đóng là `Lớp`.

Dấu cộng/trừ cạnh giá trị này đặt hướng của phần đùn:
* Trừ ( - ) bắt đầu từ bề mặt hiện tại và đùn xuống.
* Cộng ( + ) bắt đầu từ bề mặt hiện tại và đùn lên.
* Cộng trừ ( ± ) đẩy mặt trên và mặt dưới của phần đùn ra xa đều nhau, nên nó sẽ nằm lún một nửa trong bề mặt gốc.

#### Mặt bên {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Phần này hiển thị khi hành động đóng là `Lớp vỏ`.

`Phân đoạn thành` đặt số phân đoạn dọc theo các thành bên của lớp vỏ. Khi bật nút `Tự động` của nó, Nomad sẽ tự tính số vòng cạnh cần tạo để có các đa giác vuông vức.

#### Sự mượt mà {#smoothness}
![](/images/layers_smoothness.webp) 

Nếu các cạnh của vùng cần chiết xuất bị răng cưa, hãy bật tùy chọn này để làm mịn chúng thành hình đẹp hơn. `Tất cả` làm mịn toàn bộ bề mặt được chiết xuất, `Chỉ các biên` làm mịn các cạnh của nó. `Các lần lặp lại` đặt độ mạnh của việc làm mịn.

_Đây là phần cuối của menu con 'Thêm...'._

### ![](/icons/cog.webp) Nâng cao {#advanced}
![](/images/layers_advanced.webp)

Nút `Nâng cao` ở cuối menu xuất hiện khi đối tượng đã có lớp.

#### Giữ chi tiết các lớp trên cùng {#keep-top-layers-details}

Đảm bảo các chi tiết nhỏ trên những lớp phía trên vẫn hiển thị khi bạn thực hiện những thay đổi lớn ở các lớp bên dưới. Trong khi điêu khắc, biến dạng đến từ các lớp trên cùng sẽ bị bỏ qua, nhưng chi tiết của chúng vẫn hiển thị. Tùy chọn này chỉ hoạt động tốt nếu các lớp trên cùng chứa những chi tiết tương đối nhỏ.

Theo mặc định, nếu bạn điêu khắc những nếp nhăn nhỏ trên một lớp, rồi thay đổi lớn ở lớp nền, các nếp nhăn sẽ bị mất. Bật tùy chọn này cho phép những chi tiết nhỏ đó luôn nằm trên các thay đổi lớn bên dưới. Trong video sau, hãy xem nếp nhăn bị xóa mất theo mặc định, nhưng vẫn hiển thị khi bật 'Giữ chi tiết các lớp trên cùng':

![](/videos/layers_details.mp4)


#### Đồng bộ biến đổi {#sync-transform}

Khi bật, mọi lớp không được chọn sẽ được điều chỉnh theo phép biến đổi xoay, tỷ lệ, xiên khi bạn dùng công cụ Gizmo hoặc Biến Đổi. Nó có thể là `Tự động`, `Không` hoặc `Có`.

Tắt tùy chọn này nếu các lớp khác cần được dùng mà không có phép biến đổi mới mà bạn đang áp dụng.

Khi đặt là `Tự động`, chỉ các lớp đang hiển thị mới được điều chỉnh.
