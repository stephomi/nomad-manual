# ![](/icons/scene.webp) Cảnh {#scene}

Menu này giúp bạn quản lý các đối tượng, đèn, máy ảnh và trình lặp lại trong Nomad. Nó hiển thị cấu trúc phân cấp của cảnh dưới dạng cây, cho phép bạn thay đổi nhiều khía cạnh của đối tượng. Bạn cũng có thể tạo đối tượng mới, cũng như gộp và tách đối tượng theo nhiều cách khác nhau.


![](/images/scene_menu_summary.webp)


## Thanh phím tắt {#shortcut-bar}
| Thao tác               | Biểu tượng                        | Mô tả                                                                                                               |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Thêm...](#add-menu)   | ![](/icons/plus.webp)            | Mở [Menu Thêm](#add-menu) để thêm một đối tượng vào cảnh                                                            |
| Xóa                    | ![](/icons/trash.webp)           | Xóa các đối tượng đang chọn. Các mục con của chúng vẫn được giữ lại.                                                |
| Khóa                   | ![](/icons/lock.webp)            | Khiến các đối tượng đang chọn không thể chọn được trong khung nhìn. Bạn vẫn có thể chọn chúng từ cây phân cấp. Khóa một nhóm sẽ khóa mọi thứ bên trong nó. Chạm lần nữa để mở khóa. |
| [Gộp lại](#join)       | ![](/icons/merge.webp)           | Gộp các đối tượng đang chọn thành một đối tượng duy nhất mà không thay đổi hình khối                                |
| [Tách...](#separate)   | ![](/icons/separate.webp)        | Mở cửa sổ [Tách](#separate), để chia một đối tượng thành nhiều đối tượng. Ngược lại với thao tác gộp                |
| [Boolean...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Mở cửa sổ [Boolean](#boolean)                                                                                  |
| Nhân bản               | ![](/icons/clone.webp)           | Nhân bản các đối tượng đang chọn thành đối tượng mới                                                                |
| Thực thể               | ![](/icons/link.webp)            | Nhân bản các đối tượng đang chọn dưới dạng thực thể, để thay đổi hình dạng trên một bản sẽ áp dụng cho mọi thực thể. |
| Bỏ thực thể            | ![](/icons/unlink.webp)          | Biến một thực thể thành hình dạng độc lập, để thay đổi hình dạng không còn được sao chép sang các thực thể khác     |
| Đồng bộ                | ![](/icons/checked.webp)         | Khi được đánh dấu, các thao tác áp dụng cho mọi thực thể của các đối tượng đang chọn, chứ không chỉ cho các đối tượng được chọn. Tùy chọn này chỉ có khi vùng chọn chứa thực thể. [Thẻ Đồng bộ](#sync) trong cửa sổ `Nâng cao` quyết định những thao tác nào làm theo ô chọn này. |

::: tip
Khi một thao tác cũng sẽ ảnh hưởng đến các thực thể khác, một biểu tượng liên kết nhỏ sẽ hiện trên nút của nó.
:::


## Cây phân cấp {#tree-view}
![](/images/scene_treeview.webp) 

Cây phân cấp liệt kê các đối tượng, nhóm, trình lặp lại, đèn và máy ảnh của cảnh. Bên cạnh tên một lưới, bạn sẽ thấy số đỉnh của nó, kèm một biểu tượng lớp có màu nếu lưới có lớp. Mỗi hàng có các nút sau:

| Thao tác     | Biểu tượng                 | Mô tả                    |
| :----------: | :------------------------: | :----------------------: |
| Tên          | ![](/icons/pencil.webp)   | Đổi tên đối tượng. Nếu đối tượng đang được chọn, mọi đối tượng đang chọn sẽ được đổi tên cùng lúc, kèm theo một con số. Nhấn lâu để đổi tên cả đối tượng lẫn các mục con của nó. |
| Chọn         | ![](/icons/checked.webp)  | Chọn/bỏ chọn             |
| Có thể thấy  | ![](/icons/eye_open.webp) | Bật/tắt hiển thị         |
| Menu         | ![](/icons/more.webp)     | Mở [menu đối tượng](#object-menu) |

::: tip MẸO: Chọn hoặc ẩn nhanh nhiều đối tượng

Chạm vào biểu tượng chọn để chọn/bỏ chọn một đối tượng, hoặc kéo dọc theo cột chọn để chọn nhiều đối tượng. Bạn cũng có thể làm tương tự với cột hiển thị.

Nhấn lâu vào biểu tượng chọn hoặc hiển thị để tác động cả lên các mục con.

:::

### Thanh đầu cây phân cấp {#tree-view-header}

Hàng phía trên danh sách có vài công cụ hỗ trợ:

* ![](/icons/sort_down.webp) - thu gọn hoặc mở rộng tất cả các nhóm cùng lúc.
* ![](/icons/preview.webp) - bật/tắt `Xem trước đối tượng`, một hình thu nhỏ được render cho mỗi đối tượng trong danh sách.
* ![](/icons/search.webp) - lọc danh sách theo tên.

### Sắp xếp cây phân cấp {#tree-view-manipulation}

Nhấn lâu vào một mục trong cây phân cấp cho đến khi nó được tô sáng. Sau đó bạn có thể di chuyển nó lên hoặc xuống, hoặc kéo nó thả lên một mục khác để biến nó thành mục con của mục đó.

Khi nhiều mục được chọn, một trong số đó là mục chọn chính và được hiển thị sáng hơn. Nhấn lâu và kéo một trong số chúng để di chuyển tất cả các đối tượng đang chọn cùng lúc.

Khi bạn chọn một mục cha, theo mặc định tất cả các mục con cũng sẽ được chọn. Chạm vào mục cha lần nữa để chuyển giữa chỉ chọn mục cha, hoặc chọn cả mục cha lẫn mục con.

Chạm đúp vào một mục để máy ảnh tập trung vào nó (xem [Nâng cao](#focus-on-item)).

### Menu đối tượng {#object-menu}

Bấm vào nút ba chấm (...) của một đối tượng trong cây phân cấp sẽ mở menu đối tượng.
Nhiều tùy chọn trong đó giống với thanh phím tắt ở trên cùng, được lặp lại cho tiện.

|       Thao tác      |                     Biểu tượng                     | Mô tả                                                                                                                                                                   |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Tên          |              ![](/icons/pencil.webp)           | Đổi tên đối tượng                                                                                                                                                       |
|     Bỏ thực thể     |              ![](/icons/unlink.webp)           | Biến một thực thể thành hình dạng độc lập, để thay đổi hình dạng không còn được sao chép sang các thực thể khác.                                                        |
|      Thực thể       |               ![](/icons/link.webp)            | Nhân bản đối tượng dưới dạng thực thể, để thay đổi hình dạng trên một bản sẽ áp dụng cho mọi thực thể.                                                                  |
|      Nhân bản       |              ![](/icons/clone.webp)            | Nhân bản đối tượng thành một đối tượng mới                                                                                                                              |
|        Xóa          |              ![](/icons/trash.webp)            | Xóa đối tượng. Các mục con của nó vẫn được giữ lại, trừ khi `Mục con` được đánh dấu.                                                                                    |
|      Mục con        |            ![](/icons/hierarchy.webp)          | Khi được đánh dấu, `Thực thể`, `Nhân bản` và `Xóa` cũng tác động lên các mục con của đối tượng.                                                                         |
|   Tách theo Phần    |             ![](/icons/separate.webp)          | Nếu một đối tượng gồm nhiều phần rời nhau, tạo một đối tượng riêng cho mỗi phần. Ngược lại với thao tác gộp.                                                            |
|   Tách theo Nhóm    |            ![](/icons/group.webp)          | Nếu một đối tượng có nhiều nhóm mặt, tạo một đối tượng riêng cho mỗi nhóm mặt.                                                                                              |
|   Tách theo Lớp     |              ![](/icons/layer.webp)            | Nếu một đối tượng có lớp, tạo các đối tượng riêng cho lưới gốc và cho từng lớp. Hữu ích để gửi blendshape sang ứng dụng khác.                                          |
|   Gộp lại → Lớp     | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Nếu nhiều đối tượng được chọn và có tô pô giống nhau, gộp các đối tượng đó thành các lớp của đối tượng chính (các đối tượng còn lại sẽ bị xóa). Một lần nữa, hữu ích cho blendshape đến TỪ các ứng dụng khác.<br><br> Lưu ý rằng các lớp sẽ bị tắt theo mặc định. Hãy bật chúng nếu bạn cần chỉnh thanh trượt của chúng. |
|  Đường cong (Lặp lại) |            ![](/icons/curve.webp)            | Chỉ dành cho ống hoặc khối tiện: thêm một trình lặp lại [Đường cong](#curve) đi theo cùng đường cong đó, làm mục con của đối tượng.                                    |
|        Ống          |             ![](/icons/tube.webp)              | Với khối tiện, thêm một [ống](tools.md#tube) đi theo biên dạng của nó, làm mục con. Với hình trụ, hình nón hoặc vòng xuyến, biến nó thành một ống có cùng hình dạng, để bạn có thể uốn nó theo một đường cong. |




### Chọn nhiều {#multiselection}
Bạn có thể chọn nhiều đối tượng để làm hai việc:
- dùng công cụ gizmo để di chuyển nhiều đối tượng cùng lúc
- gộp các đối tượng bằng thao tác gộp và boolean.

Trong cây phân cấp, chạm vào biểu tượng chọn của từng đối tượng, hoặc kéo dọc theo cột chọn. Khi chạm vào tên, hãy giữ phím tắt `Mặt nạ` (hoặc `Ctrl` trên bàn phím) để thêm hoặc bỏ một đối tượng, hoặc giữ phím tắt `Làm mịn` (hoặc `Shift`) để chọn mọi đối tượng nằm giữa đối tượng hiện tại và đối tượng bạn chạm vào.

::: tip Chọn nhiều nhanh
Bạn cũng có thể chọn nhiều đối tượng ngay trong khung nhìn bằng cách giữ phím tắt `Làm mịn` (hoặc `Shift`) và chạm vào một lưới khác.

Bạn có thể bỏ chọn một đối tượng bằng cách chạm vào nó lần nữa (chỉ khi vùng chọn có nhiều hơn một đối tượng).
:::

Gizmo di chuyển tất cả các đối tượng đang chọn cùng nhau, xem [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Gộp lại {#join}
Tùy chọn này đơn giản là tạo một mục đối tượng duy nhất từ nhiều đối tượng đang chọn.
Các điểm và UV nằm gần nhau hơn [bán kính hàn](#weld-radius) sẽ được hợp nhất.

Bạn có thể xem video ví dụ trong phần [Tách](#separate).

## ![](/icons/bool_subtract_circle.webp) Boolean {#boolean}
![](/images/scene_boolean_menu.webp) 
Kết hợp các đối tượng thành một bề mặt duy nhất.

`Kết hợp voxel` giữ lại thể tích của các đối tượng và tính toán các đa giác mới phân bố đều trên bề mặt. Nhờ bước tính toán này, kết hợp voxel xử lý được hình khối phức tạp, nhưng có thể mất chi tiết nhỏ nếu độ phân giải mục tiêu không đủ cao.

`Boolean` sẽ cố giữ nguyên bố cục đa giác ban đầu và khâu các đa giác lại ở chỗ các đối tượng chồng lên nhau. Cách này có thể cho kết quả gọn và sắc nét hơn nhiều so với kết hợp voxel, nhưng nó đòi hỏi lưới 'kín nước': các đối tượng không được có lỗ hay hình dạng lỗi. Nếu nó thất bại, kết hợp voxel thường sẽ làm được.

### Các phép boolean {#boolean-operations}
Cả Kết hợp voxel lẫn Boolean đều dùng trạng thái hiển thị của đối tượng để điều khiển phép toán, như lời nhắc ở cuối cửa sổ:

#### Hợp {#union}
Cả hai đối tượng đều hiển thị sẽ tạo phép **hợp** boolean: lớp vỏ ngoài của các đối tượng được kết hợp, không còn bề mặt bên trong. ![](/images/boolean_union.webp)

#### Trừ {#subtract}
Một đối tượng bị ẩn = phép **trừ** boolean: đối tượng bị ẩn sẽ bị trừ khỏi đối tượng hiển thị. ![](/images/boolean_subtract.webp)

#### Giao {#intersect}
Cả hai đối tượng đều bị ẩn = phép **giao** boolean: tạo một hình mới chỉ ở phần hai đối tượng chồng lên nhau. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Kết hợp voxel {#voxel-merge-button}
Nhấn nút này sẽ thực hiện kết hợp voxel trên các đối tượng đang chọn. Khi dùng trên một đối tượng duy nhất, nó sẽ dựng lại tô pô với các đa giác phân bố đều, hữu ích khi đối tượng có đa giác bị kéo giãn. Các tùy chọn bên dưới hoạt động giống các tùy chọn của [Remesh voxel](topology.md#voxel-remesher).

### Độ phân giải {#resolution}
Độ phân giải của lưới voxel 3d dùng để tính toán. Khi giá trị này thay đổi, một họa tiết bàn cờ sẽ được phủ lên đối tượng để xem trước kích thước đa giác.

Ống nhỏ giọt bên cạnh thanh trượt lấy mức chi tiết theo mật độ lưới dưới ngón tay bạn. Nút bên cạnh nó chuyển thanh trượt sang `Độ dài cạnh`, một kích thước trong thế giới: cùng một giá trị sẽ cho cùng mức chi tiết trên mọi đối tượng.

### Tạo dựng đa độ phân giải {#build-multiresolution}
Tạo các cấp đa phân giải bên dưới độ phân giải mục tiêu. Ví dụ, nếu độ phân giải là 400 và tạo dựng đa độ phân giải là 3, bạn sẽ có một lưới mới với khoảng 296.000 đa giác, cùng 3 cấp phân chia thấp hơn với khoảng 74.000, 18.500 và 4.600 đa giác.

### Làm dày phần mỏng {#thicken-thin-parts}
Làm dày những phần quá mỏng so với lưới voxel, để chúng không bị đứt rời. Tùy chọn này không dùng được cùng `Cạnh sắc` hoặc `Biên sắc nét`.

### Lỗ {#holes}
Cách đóng các lỗ của đối tượng hở trước khi kết hợp:
* `Lấp đầy` - mỗi lỗ được đóng riêng, bắt đầu từ đường biên của nó.
* `Hình dạng` - các lỗ được đóng theo bề mặt xung quanh, và các mảnh hở chồng lên nhau sẽ được nối lại.

### ![](/icons/angle.webp) Giữ lại các cạnh sắc nét {#keep-sharp-edges}
Nút `Cạnh sắc` làm lưới voxel bám vào các cạnh sắc của đối tượng. Nó hoạt động tốt nhất với hình dạng đơn giản, và có thể gây méo ở một số vùng.

### ![](/icons/group.webp) Biên sắc nét {#sharp-border}
Các mặt mới đi theo đường biên giữa các nhóm mặt, và đường biên giữ sắc nét ở những chỗ bề mặt gấp khúc dọc theo nó.

### ![](/icons/group_separate.webp) Giữ các nhóm riêng {#keep-groups-separate}
Mỗi nhóm mặt được tái tạo lưới riêng: các nhóm không bao giờ hợp nhất, và mỗi nhóm là một mảnh khép kín thuộc nhóm của riêng nó. Ở chế độ này không tạo đa phân giải.

### ![](/icons/bool_subtract_circle.webp) Nút Boolean {#boolean-button}
Nhấn nút này sẽ thực hiện phép boolean trên đa giác, dùng thư viện Manifold của Emmett Lalish.

### ![](/icons/bool_unite_circle.webp) Làm sạch chồng lấn {#clean-overlaps}
Khi chỉ có một đối tượng được chọn, nút `Boolean` trở thành `Làm sạch chồng lấn`: nó hợp nhất các phần của đối tượng cắt xuyên qua nhau thành một bề mặt gọn gàng.


## ![](/icons/separate.webp) Tách {#separate}
Nếu bạn có một đối tượng gồm nhiều phần rời nhau, bạn có thể tách nó thành nhiều đối tượng.
Có thể xem đây là thao tác ngược với [Gộp lại](#join).

Cửa sổ `Tách...` có ba cách để tách các đối tượng đang chọn:
* `Tách theo Phần` - tạo một đối tượng riêng cho mỗi phần rời nhau.
* `Tách theo Nhóm` - tạo một đối tượng riêng cho mỗi nhóm mặt.
* `Tách theo Lớp` - tạo các đối tượng riêng cho lưới gốc và cho từng lớp.

![](/videos/merge_separate.mp4)


## ![](/icons/plus.webp) Menu Thêm {#add-menu}

![](/images/scene_addmenu_overview.webp)

Menu này tạo hình cơ bản, nhóm, máy ảnh, trình lặp lại và đèn.

Hình cơ bản là các loại hình dạng cơ bản có thể điều chỉnh bằng thông số. Khi đã chỉnh hình cơ bản theo ý muốn, bạn 'hoàn tất' nó, tức là bake các thông số đó thành một lưới đa giác có thể điêu khắc và vẽ. Sau khi đã hoàn tất, bạn không thể chỉnh thông số của hình cơ bản nữa.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) Trên Gizmo {#on-gizmo}
Đặt hình cơ bản mới tại vị trí của hình đang chọn hoặc của gizmo. Khi tắt, hình cơ bản sẽ được đặt ở tâm cảnh.

### ![](/icons/gizmo.webp) Chọn Gizmo {#select-gizmo}
Tự động chuyển sang công cụ gizmo khi một hình cơ bản mới được tạo.

### ![](/icons/cog.webp) Nâng cao {#add-advanced}

Menu này cho phép bạn chọn nơi tạo hình cơ bản, nhóm và trình lặp lại mới. Chúng có thể nằm trên đối tượng đang chọn, tại gốc tọa độ thế giới, hoặc tại vị trí của gizmo.


### UV {#uvs}
Nút bật/tắt `UVs` bên cạnh tiêu đề Hình cơ bản sẽ bật UV cho hình cơ bản. UV (thường gọi là tọa độ kết cấu) là dữ liệu bổ sung dùng trong 3d để dán kết cấu lên bề mặt. Chúng tốn thêm bộ nhớ, nhưng với hầu hết thiết bị thì không đáng lo, trừ khi số đa giác của bạn rất cao (ví dụ từ 10 triệu đa giác trở lên).

### Hình cơ bản {#primitives}

| Hình cơ bản    | Biểu tượng                                | Mô tả                                                                                                           |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Hộp            | ![](/icons/cube.webp)                    | Một khối lập phương đơn giản, bạn có thể điều chỉnh số phân chia theo X, Y và Z                                 |
| Quả cầu Hình lập phương | ![](/icons/circle.webp)         | Một hộp đã được phân chia, luôn bật `Chiếu lên mặt cầu`, nên có bố cục tứ giác đều, rất hợp để điêu khắc         |
| Hình trụ       | ![](/icons/cylinder.webp)                | Bạn có thể thêm lỗ ở tâm cho hình trụ, ví dụ để làm một ống rỗng                                                 |
| Vòng xuyến     | ![](/icons/torus.webp)                   | Vòng xuyến có thể là điểm khởi đầu tốt cho những chiếc nhẫn                                                     |
| Hình nón       | ![](/icons/cone.webp)                    | -                                                                                                               |
| Khối hai mươi mặt | ![](/icons/icosahedron.webp)          | -                                                                                                               |
| Quả cầu UV     | ![](/icons/circle.webp)                  | Một quả cầu có bố cục đa giác không đều, xem [Cảnh báo bên dưới](#uv-sphere)                                    |
| Mặt phẳng      | ![](/icons/rectangle.webp)               | Một mặt phẳng đơn giản, lưu ý đây là hình cơ bản duy nhất không khép kín                                        |
| Văn bản        | ![](/icons/text.webp)                    | Chữ 3d, với phông chữ, kiểu chữ, căn lề, độ sâu và độ uốn cong. `Gộp chữ cái` hợp nhất các chữ cái chạm nhau    |
| Ống            | ![](/icons/tube.webp)                    | xem [Ống](tools#tube)                                                                                           |
| Tiện           | ![](/icons/lathe.webp)                   | xem [Tiện](tools#lathe)                                                                                         |
| Triplanar      | ![](/icons/triplanar.webp)               | xem [Triplanar](#triplanar)                                                                                     |
| VDM            | ![](/icons/vdm.webp)                     | Một mặt phẳng được thiết lập sẵn để điêu khắc dấu vector displacement: nó có UV và hướng về phía máy ảnh        |
| Bộ bắt bóng    | ![](/icons/material_shadow_catcher.webp) | xem [Bộ bắt bóng](#shadow-catcher)                                                                              |
| Đầu            | ![](/icons/face.webp)                    | Một chiếc đầu đơn giản, với một lớp để chuyển đổi giữa nam/nữ                                                   |

::: tip
Nếu bạn thắc mắc lưới gốc khi mở Nomad là gì: đó cũng là một hộp đã được phân chia.
Tuy nhiên lưới gốc của Nomad không dùng `Chiếu lên mặt cầu`, nghĩa là nó không tròn hoàn hảo.
:::

### Thanh công cụ hình cơ bản {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

Khi một hình cơ bản được tạo, một thanh công cụ sẽ xuất hiện để điều chỉnh thông số của nó.

* `Hoàn tất` Bake hình cơ bản thành một đối tượng thông thường để có thể điêu khắc và vẽ.
* `Phản chiếu` Bật/tắt việc đặt một trình lặp lại phản chiếu phía trên hình cơ bản.
* `Tất cả` (biểu tượng con mắt) Chọn những tay nắm nào được hiển thị trực tiếp trên hình cơ bản để điều chỉnh thông số, ví dụ chiều rộng của khối lập phương hay bán kính lỗ của hình trụ: `Không có`, `Tất cả`, hoặc chỉ một loại (bán kính, lỗ, biên dạng...) tùy theo hình cơ bản.
* `Phân chia` Số phân chia của hình cơ bản, ở đây là theo trục X của một hộp.
* `Mật độ không đổi` Khi bạn kéo giãn hình cơ bản theo một trục bằng gizmo, kích thước và số phân chia sẽ tăng lên thay vì đa giác bị kéo giãn, nên các mặt vẫn vuông. Có trên hộp, mặt phẳng và hình trụ.
* `...` Mở menu hình cơ bản.

Mỗi loại hình cơ bản sẽ có thêm tùy chọn riêng trên thanh công cụ:

* `Quả cầu` Quả cầu được dựng từ một khối lập phương đã phân chia, vì cách này tốt hơn cho điêu khắc, nhưng cũng có nghĩa là nó không tròn hoàn hảo. Tùy chọn này ép hình dạng gần với một quả cầu hoàn hảo hơn. Khối hai mươi mặt cũng có tùy chọn này.
* `Nắp` Bật/tắt nắp ở hai đầu của hình, ví dụ hình trụ có thể có nắp ở trên, ở dưới, cả hai, hoặc không có.
* `Lỗ` Bật/tắt việc tạo một lỗ xuyên qua tâm của hình. Tùy chọn này lần lượt chuyển giữa không có lỗ, lỗ với một bán kính duy nhất, hoặc lỗ với bán kính khác nhau ở trên và dưới.
* `Bán kính` Chọn hình trụ có một bán kính duy nhất, hay bán kính khác nhau ở trên và dưới.
* `Đĩa` Chọn mặt phẳng là hình 4 cạnh hay hình tròn.

Thanh công cụ nhỏ bên dưới thanh công cụ chính cho phép bạn chuyển giữa gizmo của hình cơ bản và gizmo biến đổi.

::: tip

Bấm vào tiêu đề của thanh công cụ sẽ chuyển nó lên trên cùng hoặc xuống dưới cùng màn hình. Bấm vào mũi tên ở góc sẽ thu gọn nó.

:::


### Menu hình cơ bản {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Menu này chứa mọi thông số của hình cơ bản đang chọn. Thông số là những mô tả cơ bản của một hình dạng. Ví dụ, để mô tả một chiếc nhẫn, bạn sẽ mô tả bán kính ngoài, bán kính trong và số đa giác của nó.

Phần lớn thông số của hình cơ bản đều dễ hiểu, và có một số thông số chung cho mọi hình cơ bản:

* `UVs` Nút UVs nhỏ ở đầu menu bật/tắt việc tạo tọa độ UV
* `Hoàn tất` Nút hoàn tất nhỏ sẽ bake hình cơ bản thành một đối tượng thông thường để có thể điêu khắc và vẽ.
* `Mặt tối đa` Đặt giới hạn trên cho số đa giác của đối tượng để tránh làm thiết bị bị treo.
* `Hậu phân chia` Áp dụng số lần phân chia đã chọn từ phần đa phân giải của menu Tô pô. Có thể dùng để tạo hình cơ bản mượt, bo góc mềm khi kết hợp với số phân chia tô pô thấp. Ví dụ, đặt số phân chia tô pô của hộp là 2 và hậu phân chia là 4 sẽ tạo ra một hộp có góc bo mượt.
* `Phân khu tuyến tính` Đặt số cấp phân chia tuyến tính dùng trước khi áp dụng phân chia mượt thông thường. Có thể dùng để điều chỉnh độ sắc hay mềm của các góc trên bề mặt phân chia. Ví dụ, đặt số phân chia tô pô của hộp là 2, hậu phân chia là 4, rồi thử thay đổi phân chia tuyến tính từ 0 đến 4. Các góc của hộp sẽ chuyển từ mềm sang sắc.

### Cấu trúc {#topology}

Phần này điều chỉnh số đa giác của một hình cơ bản. Thông thường các điều khiển được liên kết với nhau, nên thay đổi một thanh trượt sẽ điều chỉnh đều mọi đa giác. Bạn có thể chạm vào nút bỏ liên kết để điều chỉnh riêng số phân chia X/Y/Z của hình.

### Hình học {#geometry}

Phần này điều chỉnh kích thước tổng thể của hình cơ bản, theo đơn vị X/Y/Z cho hình vuông vức, và theo bán kính cho hình tròn.


### ![](/icons/circle.webp) Quả cầu UV {#uv-sphere}
::: warning
Quả cầu UV không phù hợp lắm để điêu khắc, nhất là ở hai cực.

Bạn nên dùng [hình cơ bản](#primitives) Quả cầu Hình lập phương, Hộp hoặc Khối hai mươi mặt, cùng với tùy chọn `Chiếu lên mặt cầu`.

Lưu ý rằng tô pô có thể chấp nhận được để điêu khắc nếu bạn dùng giá trị rất thấp cho các thanh trượt `Phân chia`.
Sau đó bạn có thể dùng thanh trượt `Phân chia tổng thể` để tăng số đa giác.

Dù không hợp để điêu khắc nói chung, nó lại rất hữu ích cho mắt: nếu bạn xoay quả cầu sao cho hai cực nằm ở con ngươi, bố cục đa giác sẽ tự nhiên phù hợp để vẽ và điêu khắc mống mắt và con ngươi.
:::


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
Hình cơ bản này đặc biệt ở chỗ bạn nên dùng [công cụ Mặt nạ](tools.md#mask) trên nó để tạo hình.

![](/videos/triplanar.mp4)


::: tip
Chạm đúp vào một mặt phẳng và máy ảnh sẽ tập trung vào mặt phẳng đó.
Tuy nhiên cách này sẽ không hoạt động nếu bạn xoay hình cơ bản bằng gizmo.
:::

Triplanar dùng thông tin mặt nạ từ 3 mặt phẳng để lấp đầy một lưới voxel, rồi lưới voxel đó được chuyển thành đa giác (nhờ [Remesh voxel](topology.md#voxel-remesher)).

Mỗi mặt phẳng có mặt phẳng đối xứng riêng.

::: warning
Mỗi lần bạn thay đổi kích thước của hình cơ bản Triplanar, chất lượng của mặt nạ đã vẽ sẽ giảm đi.

Hiện chưa có tùy chọn để 'khóa' việc vẽ trên một mặt phẳng duy nhất, nhưng có thể sẽ có trong tương lai.
Bạn có thể dùng [Kết nối hình học](stroke.md#connected-topology) để đỡ phần nào: nếu con trỏ nằm chính xác trên một mặt phẳng, nó sẽ không ảnh hưởng đến các mặt phẳng khác.
:::

### ![](/icons/material_shadow_catcher.webp) Bộ bắt bóng {#shadow-catcher}
Thêm một mặt phẳng dùng vật liệu bộ bắt bóng. Xem [Vật liệu Bộ bắt bóng](material.md#shadow-catcher) để biết thêm chi tiết.


## Nhóm/Máy ảnh {#groupcamera}
### ![](/icons/share.webp) Nhóm lại {#group}
Tạo một đối tượng 'rỗng' mà bạn có thể đặt các đối tượng khác làm con của nó. Có thể dùng để sắp xếp cấu trúc phân cấp cho gọn, bằng cách đặt nhiều đối tượng vào một nhóm rồi thu gọn nhóm lại. Nhóm cũng có thể dùng để hỗ trợ di chuyển đối tượng: đặt nhiều đối tượng vào một nhóm, rồi di chuyển, xoay, thu phóng nhóm đó bằng công cụ gizmo.

### ![](/icons/camera.webp) Máy ảnh {#add-view}
Tạo một máy ảnh.

## Trình lặp lại {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Trình lặp lại là các nút tạo thực thể cho những đối tượng nằm bên dưới chúng.

### ![](/icons/array.webp) Mảng {#array}
![](/images/scene_primitive_array.webp)

Khi các đối tượng được đặt làm con của nút này, chúng có thể được nhân thành thực thể theo dạng lưới. Khi được chọn, nút này có các điều khiển:
* `Thích hợp bên trong` - khi bật, mọi bản sao được đặt bên trong giới hạn của mảng; khi tắt, các thanh trượt đặt khoảng cách giữa các bản sao
* `Số lượng X/Y/Z` - số thực thể trên mỗi trục
* `Kích thước X/Y/Z` - kích thước của lưới theo mỗi trục, hoặc khoảng cách giữa các bản sao khi `Thích hợp bên trong` tắt
* `Ngẫu nhiên...` - thêm biến thể ngẫu nhiên cho các bản sao, xem [Ngẫu nhiên](#curve) bên dưới.

### ![](/icons/curve.webp) Đường cong {#curve}
![](/images/scene_primitive_curve.webp)
Tạo một đường cong, các mục con của nút này sẽ được lặp lại dọc theo đường cong. Khi được chọn, nút này có các điều khiển:
* `Đường cong` - chỉnh sửa đường cong: thêm điểm vào đường cong và di chuyển các điểm trên đó.
* `Hiển thị` - hiện hoặc ẩn đường cong và các điểm của nó.
* `Snap` - bám các điểm của đường cong vào hình khối khác.
* `Đối Xứng` - chỉnh sửa đường cong theo đối xứng.
* `Đóng` - chuyển đường cong giữa dạng nối điểm đầu với điểm cuối, hoặc dạng hở.
* `B-spline` - chọn để các thực thể đi đúng theo đường cong, hoặc dùng nội suy b-spline cho kết quả mượt hơn.
* `Uốn theo mặt` - uốn từng bản sao theo đường cong, để các bản sao khớp với bản bên cạnh (`Mượt` uốn hai bên của chúng để chúng gặp nhau mà không tạo góc).
* `Căn chỉnh` - xoay các bản sao theo hướng của đường cong.
* `Trục xoay` - trục xoay của các bản sao: chính đường cong (`Đường cong`) hoặc các mục con của nó.
* `Số lượng` - số thực thể. Nút chế độ bên cạnh chuyển sang `Khoảng cách`: khoảng cách cố định giữa các bản sao, khi đó số lượng thay đổi theo chiều dài đường cong.
* `Bán kính` - điều khiển trên mỗi điểm của đường cong để đặt tỷ lệ của các thực thể.
* `Xoắn` - điều khiển trên mỗi điểm của đường cong để đặt góc xoắn của các thực thể.
* `Xen kẽ` - xoay cứ mỗi bản sao thứ hai quanh đường cong: 90° cho mắt xích, 180° cho lá cây hay răng khóa kéo, quanh `Trục` mà bạn chọn.
* `Xoắn ốc...` - quấn các bản sao quanh đường cong thành nhiều sợi (dây thừng, bím tóc, dải băng...).
* `Ngẫu nhiên...` - thêm biến thể ngẫu nhiên cho các bản sao; mỗi hàng cũng có thể thay vào đó cộng thêm cùng một lượng ở mỗi bản sao.

Bên dưới thanh công cụ, nút `(Gộp)` sẽ hợp nhất một điểm vào điểm khác khi bạn kéo nó lên điểm đó. `IK` (động học ngược) cho phép bạn tạo dáng cho đường cong: kéo một điểm và các điểm nối với nó sẽ đi theo. Chạm vào một điểm để khóa hoặc mở khóa nó, nhấn lâu để khóa hoặc mở khóa tất cả; các điểm bị khóa sẽ giữ nguyên vị trí.

### ![](/icons/radial.webp) Đối xứng tâm {#radial}
![](/images/scene_primitive_radial.webp)

Các mục con của nút này sẽ được nhân thành thực thể theo vòng tròn. Di chuyển đối tượng con để thay đổi bán kính của trình lặp lại này. Khi được chọn, nút này có các điều khiển:
* RadialX/Y/Z - chọn các nút này để đặt trục xoay vòng và số thực thể.



### ![](/icons/mirror.webp) Phản chiếu {#mirror}
![](/images/scene_primitive_mirror.webp)

Các mục con của nút này sẽ được phản chiếu qua một trục. Khi được chọn, nút này có các điều khiển:
* Gizmo - bật gizmo biến đổi để đặt tâm phản chiếu. Bạn cũng có thể xoay và thu phóng nó. Khi xong, chạm vào gizmo lần nữa để hiện lại các điều khiển thông thường.
* X/Y/Z - đặt mặt phẳng phản chiếu

### ![](/icons/surface.webp) Bề mặt {#surface}

Các mục con của nút này được sao chép lên bề mặt của một đối tượng: mỗi mặt, mỗi cạnh hoặc mỗi đỉnh một bản sao, hoặc rải ngẫu nhiên. Khi được chọn, nút này có các điều khiển:
* Chế độ - đặt các bản sao trên `Mặt`, `Cạnh` hoặc đỉnh, hoặc `Rải` chúng.
* Mỗi - một bản sao cứ mỗi N mặt, cạnh hoặc đỉnh. `Ngẫu nhiên` chọn chúng một cách ngẫu nhiên, và `Xáo trộn` tạo một bộ ngẫu nhiên khác.
* Khoảng cách - khi rải, khoảng cách tối thiểu giữa hai bản sao.
* Căn chỉnh - các bản sao đứng trên bề mặt, theo pháp tuyến của nó, thay vì giữ hướng của bản gốc.
* Bám - chiếu bản gốc lên điểm gần nhất trên bề mặt, các bản sao sẽ đi theo.
* Khớp kích thước, Xiên - thu phóng và kéo giãn các bản sao theo hình dạng của từng mặt.
* Uốn theo mặt - uốn từng bản sao theo mặt của nó, hoặc dọc theo cạnh của nó, để các bản sao kề nhau khớp liền không có khe hở.

Mọi trình lặp lại đều có điều khiển `Hoàn tất`, dùng để bake kết quả của trình lặp lại, và sẽ hỏi bạn muốn bake theo cách nào:
* Kết hợp các mục con - các thực thể được gộp thành một đối tượng duy nhất
* Giữ thực thể - các thực thể vẫn là thực thể, nhưng không còn trình lặp lại làm 'cha'
* Bỏ thực thể - các thực thể được chuyển thành các đối tượng độc lập

`Làm phẳng tất cả` cũng bake cả các trình lặp lại lồng bên trong trình này, nên mọi bản sao đều trở thành đối tượng thông thường.

::: tip Mẹo: Kết hợp các trình lặp lại
Các trình lặp lại có thể lồng vào nhau, và nhiều đối tượng có thể làm con của trình lặp lại, tạo ra những hiệu ứng phức tạp.

![](/images/scene_repeater_combine.webp)
:::

::: tip Mẹo: Trục xoay của trình lặp lại

Một số trình lặp lại sẽ tự đặt trục xoay cho các đối tượng con, nên dù bạn di chuyển hay xoay chúng bằng công cụ gizmo, chúng cũng không nhúc nhích. Nếu cần thay đổi hành vi này, hãy chèn một nhóm vào giữa trình lặp lại và đối tượng con. Khi đó bạn có thể di chuyển hình con độc lập với trình lặp lại.
:::

## Ánh sáng {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Có hướng {#directional}
Tạo một đèn có hướng, nguồn sáng ở xa vô tận giống như mặt trời.

### ![](/icons/panorama.webp) Môi trường {#environment}
Tạo một đèn môi trường, chiếu sáng cảnh từ một hình ảnh bao quanh (chiếu sáng dựa trên hình ảnh, như HDRI).

### ![](/icons/spotlight.webp) Đèn rọi {#spot}
Tạo một đèn rọi, có thể điều chỉnh độ rộng hình nón và độ mềm

### ![](/icons/light.webp) Điểm {#point}
Tạo một đèn điểm

## ![](/icons/cog.webp) Nâng cao {#advanced}
Nút `Nâng cao` ở góc dưới bên trái bảng mở một cửa sổ có hai thẻ: `Chung` và `Đồng bộ`.

### ![](/icons/focus.webp) Giao diện: Tập trung vào mục khi nhấp đúp {#focus-on-item}
Chạm đúp vào một mục trong danh sách Cảnh sẽ đưa máy ảnh về giữa mục đó trong khung nhìn 3d.

### ![](/icons/eye_open.webp) Đồng bộ hóa khả năng hiển thị {#sync-visibility}
Khi bật, dùng biểu tượng con mắt của một mục đang chọn sẽ tác động lên mọi mục đang chọn.

### ![](/icons/bang.webp) Nổi bật {#highlight}
Tô sáng các đối tượng đang chọn trong khung nhìn khi vùng chọn thay đổi.

### ![](/icons/link.webp) Hiển thị (Thực thể) {#instance-show}
Hiển thị một dải màu ở bên trái danh sách cảnh để đánh dấu các thực thể.

### ![](/icons/preview.webp) Xem trước đối tượng {#object-previews}
Hiển thị một hình thu nhỏ được render cho mỗi đối tượng trong danh sách cảnh. Giống như nút xem trước phía trên danh sách.

### Bán kính hàn {#weld-radius}
Dưới tiêu đề `Gộp lại` có `Bán kính hàn vị trí` và `Bán kính hàn UV`: các điểm và UV nằm gần nhau hơn các bán kính này sẽ được hợp nhất. Mỗi bán kính có thể tắt bằng ô chọn của nó. Thiết lập này áp dụng cho Gộp lại, Boolean, Cắt, Tinh giảm, tái tạo lưới và nhập tệp.

### Biểu tượng {#icons}
Đặt `Kích thước` tối thiểu và tối đa cùng `Độ mờ đục` của các biểu tượng nhóm, đèn, máy ảnh và trình lặp lại trong khung nhìn.

### ![](/icons/hierarchy.webp) Đường phân cấp {#hierarchy-lines}
Hiển thị một đường nối giữa mục cha và các mục con của nó trong khung nhìn. Khi bật, bạn có thể đặt thêm:
* `Sử dụng trục Nomad` - các đường bắt đầu từ trục xoay mà công cụ Biến Đổi và Gizmo sử dụng. Khi tắt, chúng dùng trục xoay gốc tự nhiên, có thể nằm xa tâm đối tượng.
* `Độ dày` - độ rộng của các đường. Nút bên cạnh thanh trượt thêm viền cho chúng.
* Màu của các đường.

### ![](/icons/link.webp) Đồng bộ {#sync}
Thẻ `Đồng bộ` quyết định, với từng thao tác (`Thêm`, `Xóa`, `Khóa`, `Nhân bản`, `Thực thể`, `Bỏ thực thể`, `Gộp lại`, `Tách` và `Boolean`), liệu nó có áp dụng cho mọi thực thể của vùng chọn hay không:
* `Tự động` - làm theo ô chọn `Đồng bộ` ở đầu menu Cảnh.
* `Không` - chỉ các đối tượng đang chọn.
* `Có` - luôn luôn mọi thực thể.

Theo mặc định, `Gộp lại`, `Tách` và `Boolean` được đặt là `Có`, còn lại là `Tự động`. `Đặt lại` khôi phục các giá trị mặc định này.

## Thanh công cụ dưới cùng {#bottom-toolbar}
Các biểu tượng này bật/tắt hiển thị của Nhóm, Đèn, Máy ảnh, Trình lặp lại và Đường phân cấp trong khung nhìn. Bạn có thể chạm vào các biểu tượng hiển thị trên khung vẽ để chọn và chỉnh sửa chúng trực tiếp.
