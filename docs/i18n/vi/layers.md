# ![](/icons/layer.webp) Lớp {#layers}

This menu contains the layer stack, a way to store edits to your object in a non destructive way, and many ways to combine and repurpose layers.

![](/images/layers_overview.webp) 

## Tổng quan {#overview}

Các layer trong Nomad có nhiều mục đích khác nhau.

Thông tin tô màu (Color, Roughness, Metalness, Opacity) hoạt động với layer tương tự như trong các phần mềm vẽ 2D. Bạn có thể tạo một layer và tô màu lên mô hình. Layer có thể được bật/tắt, điều chỉnh độ mờ (opacity), nhân bản, thay đổi thứ tự trong ngăn xếp layer, thay đổi chế độ hòa trộn (blending mode).

Nomad cũng sử dụng layer cho điêu khắc. Một layer có thể lưu các chi tiết nhỏ như nếp nhăn, hoặc lưu các thay đổi lớn, cho phép chúng hoạt động giống như blendshape/shape key/morph target trong các phần mềm 3D khác. Ví dụ, bạn có thể điêu khắc các biểu cảm khuôn mặt khác nhau trên các layer khác nhau, rồi điều chỉnh thanh trượt của layer để kết hợp chúng thành các biểu cảm mới.

Trong trường hợp này, các thay đổi được lưu trong layer là hoàn toàn cộng dồn, thứ tự layer không quan trọng như với tô màu.

Layer có thể được xóa một phần bằng công cụ [Delete Layer](tools.md#delete-layer), và layer cũng có thể được dùng để tạo mask dựa trên các loại thông tin khác nhau được lưu trong layer.

![](/videos/layer.mp4)

::: tip
Không giống hầu hết phần mềm điêu khắc khác, thay đổi topology của mesh sẽ không làm mất layer. Bạn có thể dùng [Voxel Remesher](topology.md#voxel-remesher), [Multiresolution](topology.md#multires) hoặc các công cụ [Trim](tools.md#trim)/[Split](tools.md#split), nhưng lưu ý rằng khi dùng [Voxel Remesher](topology.md#voxel-remesher), chất lượng của layer sẽ bị ảnh hưởng.
:::

::: tip
Nếu dùng layer cho blendshape/morph target, sẽ có thêm chức năng layer trong [scene menu](scene.md#object-menu). Bạn có thể tách layer thành các đối tượng, và kết hợp các đối tượng tương ứng trở lại thành layer.
:::
----

## Menu lớp {#layer-menu}

![](/images/layers_menu.webp)

Nhấn `Add layer` để tạo một layer mới.

Mỗi layer có một tên, một thanh trượt để điều khiển độ mạnh/hệ số của nó, và các nút tùy chọn.

### Tùy chọn {#options}

| Action       | Icon                         | Description                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Visible      | ![](/icons/eye_open.webp)   | Hiện/ẩn layer                                       |
| Blend Mode   | ![](/icons/opacity.webp)    | Chế độ hòa trộn kiểu Photoshop. 4 biểu tượng thể hiện chế độ cho Color, Roughness, Metalness, Opacity. |
| Edit Name    | ![](/icons/pencil.webp)     | Chỉnh sửa tên layer                                 |
| Delete       | ![](/icons/trash.webp)      | Xóa layer                                           |
| Duplicate    | ![](/icons/clone.webp)      | Nhân bản layer                                      |
| Merge Down   | ![](/icons/merge_down.webp) | Gộp layer với layer bên dưới (hoặc mesh gốc)       |
| More         | ![](/icons/more.webp)       | Tùy chọn [More...](#more)                          |

Để di chuyển một layer đến vị trí khác trong ngăn xếp layer, nhấn giữ vào tên của nó rồi kéo.

### Thêm... {#more}

Nút 'More...' sẽ hiển thị thêm các tùy chọn cho layer hiện tại:

![](/images/layers_more.webp) 

#### Hệ số kênh {#channel-factors}

Các điều khiển này cho phép bạn nhân tỉ lệ lượng sculpt/color/roughness/metalness/opacity cho layer. Các giá trị này được nhân với giá trị thanh trượt hệ số layer, ví dụ nếu độ mạnh của layer là 1, nhưng hệ số kênh màu (color channel factor) là 0.5, thì màu hiển thị sẽ ở mức 0.5.

`Offset` điều khiển độ mạnh sculpt của layer. Trong khi color/roughness/metalness bị giới hạn trong khoảng 0 đến 1, offset có thể là bất kỳ giá trị nào, cả dương lẫn âm. 

::: tip
Offset có thể được dùng để biến một layer lồi (bumps) thành một layer lõm (cavities), hoặc biến nụ cười thành cái nhăn mặt:
![](/videos/layer_happysad.mp4)


Một layer đối xứng có thể được nhân bản rồi tách thành các hình dạng trái/phải bằng del layer:
![](/videos/layer_leftright.mp4)

Các layer với hệ số offset âm có thể được bake xuống thành các layer rỗng để tạo các hình dạng dương mới.

Các layer với hệ số offset dương lớn hơn 1 có thể được dùng để thử nghiệm các blendshape cực đoan hơn.
:::

::: warning
Hiện tại các layer chỉ dùng chung một kênh opacity cho cả 3 kênh (color/metalness/roughness).
Nếu bạn gộp nhiều layer với cường độ theo kênh (per-channel intensity) không ở mức tối đa, kết quả cuối cùng có thể trông khác đi.

Có thể trong tương lai, mỗi kênh sẽ có kênh alpha riêng để loại bỏ giới hạn này.
:::


#### ![](/icons/tool_mask.webp) Mặt nạ {#mask}
Nút mask bên cạnh mỗi thanh trượt sẽ tạo một mask từ kênh đó. Tương tự như việc dùng layer để tạo vùng chọn trong các phần mềm vẽ, điều này cho phép bạn tái sử dụng công việc đã làm trong một layer cho các thao tác khác.

#### ![](/icons/preview.webp) Xem trước {#preview}
![](/images/layers_preview.webp) 

Khi bật, sẽ xem trước thiết lập extract cho layer này (xem phần tiếp theo).

Khi bật xray, chỉ phần hình dạng được extract sẽ là đặc, phần còn lại của hình sẽ được làm trong suốt, hữu ích nếu bạn đang dùng chiều cao extract âm.

#### Trích xuất {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Nút `Extract` sẽ nhân bản nội dung của layer thành một đối tượng mới, thường với độ dày do người dùng chỉ định ở phần tiếp theo.

`Closing action` quyết định cách thực hiện việc nhân bản:

* None - Chỉ extract phần đó, không tạo cạnh bên hay lấp lỗ.
* Fill - Lỗ được lấp và làm mượt bằng tam giác. Không dùng tùy chọn này cho bề mặt phẳng.
* Shell - Đóng kín hình dạng được extract với giá trị độ dày và tùy chọn hướng.
* Layer - Extract phần chênh lệch của layer.

#### ![](/icons/height.webp) Độ dày {#thickness}
![](/images/layers_thickness.webp) 

Độ sâu của phần shell extrusion. Giá trị dương đẩy ra khỏi bề mặt, giá trị âm đẩy vào trong bề mặt.

Nút cộng/trừ bên cạnh giá trị này sẽ đặt hướng extrusion:
* Minus ( - ) sẽ bắt đầu từ bề mặt hiện tại và extrude xuống dưới. 
* Plus ( + ) sẽ bắt đầu từ bề mặt hiện tại và extrude lên trên.
* PlusMinus ( ± ) sẽ đẩy cả mặt trên và dưới của extrusion ra xa với lượng bằng nhau, nên nó sẽ nằm chìm một nửa trong bề mặt gốc.

#### Độ mượt {#smoothness}
![](/images/layers_smoothness.webp) 

Nếu cạnh của vùng cần extract bị răng cưa, thanh trượt này sẽ cố gắng làm mờ cạnh để tạo hình dạng mượt hơn. 

#### ![](/icons/height.webp) Vòng lặp cạnh (bên) {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Phần này chỉ hiển thị khi closing action là 'Shell'. 

`Auto Edge-loop (side)` sẽ tính số edge loop dọc theo cạnh bên của shell để tạo polygon vuông. 

Nếu tắt, thanh trượt `Division` sẽ đặt số lượng phân chia trên các cạnh bên.

_Đây là phần kết thúc của submenu 'More...'._

### Nâng cao {#advanced}
![](/images/layers_advanced.webp)

#### Giữ chi tiết lớp trên cùng {#keep-top-layers-details}

Đảm bảo các chi tiết nhỏ trên các layer phía trên vẫn hiển thị khi có các thay đổi lớn ở các layer phía dưới.

Mặc định, nếu bạn điêu khắc các nếp nhăn nhỏ trên một layer, rồi quay lại tạo các thay đổi lớn trên layer gốc, các nếp nhăn sẽ bị mất. Bật tùy chọn này sẽ cho phép các chi tiết nhỏ đó luôn nổi phía trên các thay đổi lớn bên dưới. Trong video sau, hãy xem cách chi tiết nếp nhăn bị xóa theo mặc định, nhưng vẫn hiển thị khi 'keep top layers details' được bật:

![](/videos/layers_details.mp4)


#### Giao diện: Mở rộng danh sách {#ui-expand-list}

Menu layer mặc định cho phép bạn bật/tắt hiển thị layer và chỉnh opacity của layer. Bật tùy chọn này sẽ mở rộng toàn bộ điều khiển cho mọi layer.

![](/images/layers_expand.webp)

#### Đồng bộ biến đổi {#sync-transform}

Nếu bật, tất cả các layer không được chọn sẽ được điều chỉnh tùy theo phép biến đổi xoay, tỉ lệ, skew. 

Tắt tùy chọn này nếu các layer khác được dùng mà không cần áp dụng phép biến đổi mới mà bạn đang thực hiện.

Khi đặt ở `Auto`, chỉ các layer đang hiển thị mới được điều chỉnh.