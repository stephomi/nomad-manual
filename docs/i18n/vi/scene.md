# ![](/icons/scene.webp) Cảnh 

Menu này cho phép bạn quản lý đối tượng, đèn, camera và repeater trong Nomad. Nó hiển thị cây phân cấp của cảnh dưới dạng tree-view, cho phép bạn chỉnh sửa nhiều khía cạnh của các đối tượng. Nó cũng cho phép bạn tạo đối tượng mới, cũng như gộp và tách đối tượng theo nhiều cách khác nhau.


![](/images/scene_menu_summary.webp)


## Thanh lối tắt
| Action                 | Icon                              | Description                                                                                                         |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Add...](#add-menu)    | ![](/icons/plus.webp)            | Hiển thị [Add Menu](#add-menu) để thêm một đối tượng vào cảnh                                                     |
| Delete                 | ![](/icons/trash.webp)           | Xoá đối tượng                                                                                                      |
| Lock                   | ![](/icons/lock.webp)            | Làm cho đối tượng không thể được chọn trong viewport. Vẫn có thể chọn từ tree view.                               |
| Join                   | ![](/icons/merge.webp)           | Gộp các đối tượng đã chọn thành một đối tượng duy nhất mà không thay đổi hình học                                 |
| Separate               | ![](/icons/diagonal.webp)        | Nếu một đối tượng được tạo từ nhiều “vỏ” polygon tách biệt, tách nó thành nhiều đối tượng riêng. Ngược lại với Join |
| [Boolean...](#boolean) | ![](/icons/subtract_circle.webp) | Hiển thị menu [Boolean](#boolean)                                                                                 |
| Clone                  | ![](/icons/clone.webp)           | Nhân bản đối tượng thành một đối tượng mới                                                                         |
| Instance               | ![](/icons/link.webp)            | Nhân bản đối tượng dưới dạng instance, để thay đổi modelling trên một đối tượng sẽ áp dụng cho tất cả instance    |
| Un-instance            | ![](/icons/unlink.webp)          | Chuyển một instance thành hình dạng độc lập, để thay đổi modelling không còn được sao chép sang các instance khác |
| Sync                   | ![](/icons/link.webp)            | Nếu các instance có con, đảm bảo tất cả instance chia sẻ cùng một cây con                                         |


## Tree view
![](/images/scene_treeview.webp) 

| Action       | Icon                       | Description              |
| :----------: | :------------------------: | :----------------------: |
| Select       | ![](/icons/checked.webp)  | Bật/tắt chọn             |
| Visible      | ![](/icons/eye_open.webp) | Bật/tắt hiển thị         |
| Menu         | ![](/icons/more.webp)     | Hiển thị menu đối tượng  |

::: tip TIP: Nhanh chóng chọn hoặc ẩn nhiều đối tượng

Chạm vào biểu tượng chọn để bật/tắt một đối tượng, hoặc kéo dọc trên cột chọn để chọn nhiều đối tượng. Có thể làm tương tự với cột hiển thị.

:::

### Thao tác với tree view

Nhấn giữ lâu trên một mục trong tree view cho đến khi nó chuyển sang màu vàng. Sau đó bạn có thể di chuyển nó lên hoặc xuống trong tree view, cũng như kéo nó lên trên một mục khác để biến nó thành con của mục đó.

Khi nhiều mục được chọn, hầu hết sẽ có màu vàng đậm, một mục sẽ có màu vàng nhạt hơn. Nhấn giữ và kéo mục màu vàng nhạt để di chuyển tất cả đối tượng cùng lúc.

Khi bạn chọn một mục cha, mặc định tất cả mục con cũng sẽ được chọn. Chạm vào biểu tượng của mục cha sẽ chuyển đổi giữa việc chỉ chọn cha, hoặc chọn cả cha và con.

### Menu đối tượng

Nhấn vào nút dấu ba chấm (...) cho một đối tượng trong tree view sẽ hiển thị menu đối tượng. 
Nhiều tuỳ chọn ở đây tương tự với thanh lối tắt phía trên, được lặp lại cho tiện.

|       Action        |                        Icon                        | Description                                                                                                                                                             |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      Instance       |               ![](/icons/link.webp)            | Nhân bản đối tượng dưới dạng instance, để thay đổi modelling trên một đối tượng sẽ áp dụng cho tất cả instance.                                                        |
|        Clone        |              ![](/icons/clone.webp)            | Nhân bản đối tượng thành một đối tượng mới                                                                                                                              |
|        Name         |              ![](/icons/pencil.webp)           | Đổi tên đối tượng                                                                                                                                                       |
|       Delete        |              ![](/icons/trash.webp)            | Xoá đối tượng                                                                                                                                                           |
|       Delete+       |            ![](/icons/removeNode.webp)         | Xoá đối tượng và toàn bộ con của nó                                                                                                                                     |
|     Un-instance     |              ![](/icons/unlink.webp)           | Chuyển một instance thành hình dạng độc lập, để thay đổi modelling không còn được sao chép sang các instance khác.                                                     |
|  Separate Topology  |             ![](/icons/separate.webp)          | Nếu một đối tượng được tạo từ nhiều “vỏ” polygon tách biệt, tách nó thành nhiều đối tượng riêng. Ngược lại với thao tác Join.                                          |
| Separate Face Group |            ![](/icons/faceGroup.webp)          | Nếu một đối tượng có nhiều face group, tách mesh thành nhiều đối tượng riêng.                                                                                          |
|   Separate Layers   |              ![](/icons/layer.webp)            | Nếu một đối tượng có layer, tách mỗi layer thành một đối tượng riêng. Hữu ích khi gửi blendshape sang ứng dụng khác.                                                   |
|   Join -> Layers    | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Nếu nhiều đối tượng được chọn và có topology khớp nhau, gộp các đối tượng đó thành layer cho đối tượng chính (các đối tượng còn lại sẽ bị xoá). Cũng hữu ích cho blendshape đến TỪ ứng dụng khác.<br><br> Lưu ý là các layer sẽ bị tắt theo mặc định. Bật chúng nếu bạn cần chỉnh slider của chúng. |




### Multiselection
Bạn có thể chọn nhiều đối tượng để phục vụ hai mục đích:
- dùng công cụ gizmo để di chuyển nhiều đối tượng cùng lúc
- gộp đối tượng bằng Join và các phép Boolean.

Bạn có thể làm điều này bằng cách bật checkbox `Multiselection`, rồi nhấp vào đối tượng trong danh sách.

::: tip Quick multiselection
Bạn cũng có thể multiselect trong viewport bằng cách giữ phím tắt `Smooth` và chạm vào một mesh khác.

Bạn có thể bỏ chọn một đối tượng bằng cách chạm lại vào nó (chỉ khi lựa chọn hiện tại có nhiều hơn một đối tượng).
:::

::: warning Tính năng gizmo bị giới hạn
Khi dùng multiselection, công cụ gizmo sẽ luôn bỏ qua masking.
Ngoài ra, scale theo X/Y/Z bị loại bỏ.

Lý do là multiselection chỉ cho phép biến đổi toàn mesh, không phải biến đổi theo từng vertex.
Điều này có thể được cải thiện trong tương lai.
:::


## Join
Tuỳ chọn này sẽ đơn giản tạo một mục đối tượng duy nhất từ nhiều đối tượng được chọn.

Bạn có thể xem ví dụ video trong phần [Separate](#separate).

## Boolean
![](/images/scene_boolean_menu.webp) 
Kết hợp các đối tượng thành một bề mặt duy nhất.

`Voxel merge` sẽ giữ lại thể tích của các đối tượng, và tính toán lại polygon mới phân bố đều trên bề mặt. Do có bước tính toán nên voxel merge có thể xử lý hình học phức tạp, nhưng có thể mất chi tiết nhỏ nếu độ phân giải mục tiêu không đủ cao.

`Boolean` sẽ cố gắng giữ nguyên bố cục polygon ban đầu, và khâu polygon tại vùng các đối tượng chồng lấp. Điều này có thể cho kết quả sạch và sắc nét hơn voxel merge, tuy nhiên nó yêu cầu mesh phải “kín nước” (watertight); không được có lỗ hoặc hình dạng lỗi. Nếu thao tác này thất bại, thường voxel merge sẽ hoạt động được.

### Các phép Boolean
Cả Voxel Merge và Boolean đều dùng trạng thái hiển thị của đối tượng để điều khiển phép toán:

#### Union
Cả hai đối tượng đều hiển thị sẽ tạo boolean **union**, lớp vỏ ngoài của các đối tượng được kết hợp, không có bề mặt bên trong. ![](/images/boolean_union.webp)

#### Subtract
Một đối tượng ẩn = boolean **subtract**, đối tượng ẩn sẽ bị trừ khỏi đối tượng hiển thị. ![](/images/boolean_subtract.webp)

#### Intersect
Cả hai đối tượng đều ẩn = boolean **intersection**, tạo một hình mới chỉ tại vùng hai đối tượng giao nhau. ![](/images/boolean_intersect.webp)


### Nút Voxel Merge
Nhấn nút này sẽ thực hiện thao tác voxel merge trên các đối tượng được chọn. Khi thực hiện trên một đối tượng đơn lẻ, nó sẽ retopo thành polygon phân bố đều, hữu ích khi đối tượng có polygon bị kéo giãn.

### Resolution
Độ phân giải của lưới voxel 3D dùng để tính toán. Khi giá trị này thay đổi, một mẫu caro sẽ phủ lên đối tượng để xem trước kích thước polygon.

### Build multiresolution
Tạo các mức multiresolution thấp hơn độ phân giải mục tiêu. Ví dụ nếu resolution là 400 và build multiresolution là 3, bạn sẽ có một mesh mới với khoảng 296.000 polygon, nhưng có 3 mức subdiv thấp hơn là 74.000, 18.000, 4.000.

### Keep sharp edges
Bật việc “snap” lưới voxel vào các cạnh. Hoạt động tốt nhất trên hình dạng đơn giản.

### Nút Boolean
Nhấn nút này sẽ thực hiện phép Boolean polygon dùng thư viện Manifold của Emmett Lalish. 


## Separate
Nếu bạn có một đối tượng đơn lẻ được tạo từ nhiều phần rời nhau, bạn có thể tách đối tượng này thành nhiều đối tượng. 
Có thể xem thao tác này như ngược lại với [Simple Merging](#simple-merge).

![](/videos/merge_separate.mp4)


## Add menu

![](/images/scene_addmenu_overview.webp)

Menu này sẽ tạo primitive, group, camera, repeater và đèn.

Primitive là các dạng hình cơ bản có thể điều chỉnh bằng tham số. Khi đã chỉnh primitive theo ý muốn, bạn “validate” nó, thao tác này sẽ chuyển các tham số thành mesh polygon có thể điêu khắc và tô màu. Primitive không thể chỉnh tham số sau khi đã validate.


![](/images/scene_addmenu_top.webp)

### On gizmo
Bật việc đặt primitive mới tại vị trí shape hoặc gizmo đang được chọn. Khi tắt, primitive sẽ được đặt ở tâm cảnh.

### Select gizmo
Bật việc tự động chuyển sang công cụ gizmo khi một primitive mới được tạo. 

### Advanced

Menu này cho phép bạn đặt tuỳ chọn về vị trí tạo primitive, group, repeater mới. Chúng có thể được tạo trên đối tượng đang chọn, tại gốc toạ độ thế giới, hoặc tại vị trí gizmo.


### UV's
Bật UV cho primitive. UV (thường gọi là texture coordinates) là dữ liệu bổ sung trong 3D để cho phép áp texture lên bề mặt. Chúng tốn thêm bộ nhớ, nhưng với hầu hết thiết bị thì không đáng lo trừ khi bạn dùng số polygon rất lớn (ví dụ 10 triệu polygon trở lên). 

### Primitives

| Primitive      | Icon                                      | Description                                                                                                     |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Box            | ![](/icons/cube.webp)                    | Hộp đơn giản, bạn có thể điều khiển số chia theo X, Y và Z                                                      |
| Sphere         | ![](/icons/circle.webp)                  | Để tiện thì gọi là Sphere nhưng thực ra là một box đã subdiv, với `Project on sphere` được bật bắt buộc        |
| Cylinder       | ![](/icons/cylinder.webp)                | Bạn có thể thêm lỗ ở giữa cho cylinder, ví dụ để tạo ống rỗng                                                   |
| Torus          | ![](/icons/torus.webp)                   | Torus là điểm khởi đầu tốt cho nhẫn                                                                            |
| Cone           | ![](/icons/cone.webp)                    | -                                                                                                               |
| Icosahedron    | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| UV-sphere      | ![](/icons/circle.webp)                  | Sphere với bố cục polygon không đều, xem [cảnh báo bên dưới](#uv-sphere)                                       |
| Plane          | ![](/icons/rectangle.webp)               | Plane đơn giản, lưu ý đây là primitive duy nhất không kín                                                       |
| Tube           | ![](/icons/tool_tube.webp)               | xem [Tube](tools#tube)                                                                                          |
| Lathe          | ![](/icons/tool_lathe.webp)              | xem [Lathe](tools#lathe)                                                                                        |
| Triplanar      | ![](/icons/triplanar.webp)               | xem [Triplanar](#triplanar)                                                                                     |
| Shadow Catcher | ![](/icons/material_shadow_catcher.webp) | xem [Shadow Catcher](#shadow-catcher)                                                                           |
| Head           | ![](/icons/face.webp)                    | Đầu đơn giản với một layer để blend giữa nam/nữ                                                                 |

::: tip
Nếu bạn thắc mắc mesh gốc khi mở Nomad là gì: đó cũng là một box đã subdiv.
Tuy nhiên mesh gốc trong Nomad không dùng `Project on sphere`, nghĩa là nó không tròn hoàn hảo.
:::

### Thanh công cụ Primitive

![](/images/scene_primitive_toolbar.gif)

Khi một primitive được tạo, một thanh công cụ sẽ xuất hiện để điều khiển tham số của nó.

* `Validate` Bake primitive thành đối tượng chuẩn để có thể điêu khắc và tô màu.
* `Edit` Bật/tắt hiển thị gizmo của primitive. Gizmo này hiển thị trực tiếp trên primitive để điều khiển tham số, ví dụ chiều rộng cube, hoặc bán kính lỗ của cylinder.
* `Mirror` Bật/tắt đặt một mirror repeater phía trên primitive.
* `...` Hiển thị menu primitive.

Các primitive khác nhau sẽ có thêm tuỳ chọn trên thanh công cụ:

* `Project` Sphere được tạo từ cube đã subdiv (tốt hơn cho sculpt), nhưng vì vậy nó không tròn hoàn hảo. Tuỳ chọn này sẽ ép hình dạng gần với sphere hoàn hảo hơn. Icosahedron cũng có tuỳ chọn này.
* `Cap` Bật/tắt nắp ở đầu hình, ví dụ cylinder có thể có nắp trên, nắp dưới, cả hai, hoặc không có.
* `Hole` Bật/tắt lỗ xuyên qua tâm hình. Sẽ chuyển qua các trạng thái: không lỗ, lỗ với một bán kính, hoặc lỗ với bán kính khác nhau ở trên và dưới.
* `Radius` Bật/tắt việc cylinder dùng một bán kính duy nhất, hoặc bán kính khác nhau ở trên và dưới.
* `Disk` Bật/tắt việc plane là hình 4 cạnh hay hình tròn.

Thanh công cụ nhỏ bên dưới thanh chính cho phép bạn chuyển giữa gizmo primitive và gizmo transform.

::: tip

Nhấp vào tiêu đề của thanh công cụ sẽ chuyển nó lên trên hoặc xuống dưới màn hình. Nhấp vào mũi tên ở góc sẽ thu gọn nó.

:::


### Menu Primitive

![](/images/scene_primitive_menu.webp)

Menu này chứa tất cả tham số cho primitive đang chọn. Tham số là mô tả cơ bản cho một hình. Ví dụ để mô tả một chiếc nhẫn, bạn sẽ mô tả bán kính ngoài, bán kính trong và số polygon.

Hầu hết tham số primitive khá dễ hiểu, và có một số tham số chung cho tất cả primitive:

* `UVs` Nút UV nhỏ ở đầu menu bật/tắt việc tạo toạ độ UV
* `Validate` Nút validate nhỏ sẽ bake primitive thành đối tượng chuẩn để có thể điêu khắc và tô màu.
* `Max faces` Đặt giới hạn trên cho số polygon trong đối tượng để tránh làm treo thiết bị.
* `Post subdivision` Bật số mức subdiv đã chọn từ phần multiresolution trong menu topology. Có thể dùng để tạo primitive bo tròn, mềm bằng cách kết hợp với số chia topology thấp. Ví dụ đặt box topology divisions là 2, và post subdivisions là 4, sẽ tạo box có góc bo tròn.
* `Linear subdivision` Đặt số mức linear subdivision trước khi dùng smooth subdivision thông thường. Có thể dùng để điều khiển độ sắc/mềm của góc trên bề mặt đã subdiv. Ví dụ đặt box topology divisions là 2, post subdivisions là 4, rồi thử đổi linear subdivisions từ 0 đến 4. Góc của box sẽ chuyển từ mềm sang sắc.

### Topology

Điều khiển số polygon trong primitive. Thường các điều khiển được liên kết, nên thay đổi một slider đang hoạt động sẽ điều chỉnh polygon đồng đều. Bạn có thể chạm nút unlink để điều khiển riêng số chia X/Y/Z trên hình.

### Geometry

Điều khiển kích thước tổng thể của primitive, theo đơn vị X/Y/Z cho hình vuông, và theo bán kính cho hình tròn.


### UV Sphere
::: warning
UV Sphere không phù hợp để sculpt, đặc biệt ở vùng cực (poles).

Hãy ưu tiên primitive [Sphere](#sphere), [Box](#box) hoặc [Icosahedron](#icosahedron) cùng với tuỳ chọn `Project on sphere`.

Lưu ý topology có thể chấp nhận được cho sculpt nếu bạn dùng giá trị rất thấp cho slider `Division`.
Sau đó bạn có thể dùng slider `Overall Subdivision` để tăng số polygon.

Dù không phù hợp cho sculpt tổng quát, nó hữu ích cho mắt; nếu bạn xoay sphere sao cho cực nằm tại vị trí đồng tử, bố cục polygon sẽ tự nhiên phù hợp để tô và sculpt mống mắt và đồng tử.
:::


### Triplanar
Primitive này đặc biệt ở chỗ bạn nên dùng [Masking tool](tools.md#mask) trên nó để tạo hình hình học.

![](/videos/triplanar.mp4)


::: tip
Nhấp đúp vào một plane và camera sẽ focus vào plane đó.
Tuy nhiên điều này sẽ không hoạt động nếu bạn xoay primitive bằng gizmo.
:::

Triplanar dùng thông tin mask từ 3 plane để lấp đầy một lưới voxel, sau đó được polygon hoá (nhờ [Voxel Remesher](topology.md#voxel-remeshere)).

Mỗi plane có mặt phẳng đối xứng riêng.

::: warning
Mỗi lần bạn cập nhật kích thước primitive Triplanar, chất lượng nét vẽ mask sẽ giảm.

Hiện chưa có tuỳ chọn “khoá” việc vẽ trên một plane duy nhất, nhưng có thể sẽ có trong tương lai.
Bạn có thể dùng [Connected Topology](stroke.md#connected-topology) để hỗ trợ phần nào, theo đó nếu con trỏ nằm chính xác trên một plane thì sẽ không ảnh hưởng đến các plane khác.
:::

### Shadow Catcher
Thêm một plane với vật liệu shadow catcher. Xem [Shadow Catcher material](material.md#shadow-catcher) để biết thêm chi tiết. 


## Group/Camera
### Group
Tạo một đối tượng “rỗng” (empty), bạn có thể cho các đối tượng khác làm con bên dưới. Có thể dùng để đơn giản hoá cây phân cấp bằng cách đặt nhiều đối tượng vào một group rồi thu gọn nó. Group cũng có thể dùng làm helper để di chuyển đối tượng; nhiều đối tượng có thể đặt dưới một group, rồi di chuyển, xoay, scale group bằng công cụ gizmo.

### Add view
Tạo một camera.

## Repeaters
![](/images/scene_primitive_repeaters.webp)

Repeater là các node tạo instance cho các đối tượng bên dưới nó. 

### Array
![](/images/scene_primitive_array.webp)

Khi các đối tượng là con của node này, chúng có thể được instance thành bố cục dạng lưới. Khi được chọn, nó có các điều khiển:
* Fit inside - chuyển giữa việc điều khiển kích thước lưới/hộp của array, hoặc điều khiển khoảng cách giữa các instance
* CountX/Y/Z - số instance trên mỗi trục
* OffsetX/Y/Z - khoảng cách giữa các instance khi fit inside được bật
* SizeX/Y/Z - chiều rộng/cao/sâu của toàn bộ lưới array khi fit inside được bật.

### Curve
![](/images/scene_primitive_curve.webp)
Node này tạo một đường cong, các con của node sẽ được lặp dọc theo đường cong. Khi được chọn, nó có các điều khiển:
* Edit - cho phép thêm điểm vào đường cong, và di chuyển các điểm trên đường cong.
* Snap - sẽ “snap” các điểm đường cong vào hình học khác
* Align - xoay các shape con để căn theo hướng của đường cong
* Count - số instance
* Closed - Bật/tắt việc nối điểm đầu và cuối của đường cong, hoặc để đường cong mở
* Radius - Bật điều khiển trên từng điểm đường cong để điều khiển scale của instance
* Twist - Bật điều khiển trên từng điểm đường cong để điều khiển xoay (twist) của instance 
* B-spline - Bật/tắt việc instance bám chính xác theo đường cong, hoặc dùng nội suy b-spline cho kết quả mượt hơn. 

### Radial
![](/images/scene_primitive_radial.webp)

Các con của node này sẽ được instance thành vòng tròn. Di chuyển đối tượng con để thay đổi bán kính repeater. Khi được chọn, nó có các điều khiển:
* RadialX/Y/Z - chọn các nút này để đặt trục quay tròn, và đặt số instance.



### Mirror
![](/images/scene_primitive_mirror.webp)

Các con của node này sẽ được phản chiếu qua một trục. Khi được chọn, nó có các điều khiển:
* Gizmo - bật gizmo transform để đặt tâm của mặt phẳng gương. Gizmo này cũng có thể xoay và scale. Khi xong, chạm lại gizmo để hiện các điều khiển chuẩn.
* X/Y/Z - đặt mặt phẳng gương

Tất cả repeater đều có điều khiển `Validate`, thao tác này sẽ bake kết quả của repeater, và hỏi cách thực hiện bake:
* Join children - các instance được gộp thành một đối tượng
* Keep instances - các instance vẫn là instance, nhưng không còn repeater làm “cha”
* Un-instances - các instance được chuyển thành đối tượng độc lập

::: tip Tip: Kết hợp repeater
Repeater có thể được cho làm con của repeater khác, và nhiều đối tượng có thể làm con của repeater, tạo ra hiệu ứng phức tạp.

![](/images/scene_repeater_combine.webp)
:::

::: tip Tip: Pivot của repeater

Một số repeater sẽ cố gắng tự động đặt pivot cho đối tượng con, nên ngay cả khi bạn di chuyển hoặc xoay chúng bằng gizmo, chúng sẽ không di chuyển. Nếu bạn cần ghi đè hành vi này, hãy chèn một group giữa repeater và đối tượng con. Khi đó bạn có thể di chuyển shape con độc lập với repeater.
:::

## Light

![](/images/scene_primitive_light.webp)

### Directional
Tạo directional light, nguồn sáng ở vô cực giống như mặt trời.

### Spot
Tạo spot light, với điều khiển độ rộng và độ mềm của hình nón sáng

### Point
Tạo point light

## Advanced
### Focus on item
Nhấp đúp vào một mục trong danh sách Scene sẽ đưa camera về tâm của mục đó trong khung nhìn 3D.

### Sync visibility
Dùng biểu tượng con mắt sẽ ảnh hưởng đến tất cả mục đang được chọn. 

### Instance: Show
Hiển thị một capsule màu ở bên trái danh sách scene để cho biết instance.


### Icons
Đặt kích thước và độ mờ của icon group, light, camera, mirror trong viewport

### Hierarchy lines
Hiển thị đường nối giữa cha và con trong viewport

## Bottom toolbar
Các icon này sẽ bật/tắt hiển thị Group, Light, Camera, Repeater và Hierarchy lines trong viewport.
