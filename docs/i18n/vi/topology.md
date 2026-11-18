# ![](/icons/multires.webp) Tô pô {#topology}

Menu này quản lý tô pô của các đối tượng trong Nomad, cùng với các công cụ để bake và chuyển chi tiết giữa các đối tượng, cũng như giữa các kết cấu (texture).

![](/images/topology_overview.webp)

Nomad làm việc với đa giác: hình khối được tạo nên từ các tam giác và tứ giác.
Khi nói đến tô pô, chúng ta muốn nói cả số lượng mặt lẫn cách các điểm (đỉnh) được nối với nhau.

Bạn nên luôn để mắt đến tô pô, nhất là khi muốn điêu khắc hay vẽ những chi tiết nhỏ.

::: tip Làm sao để theo dõi tô pô?
Bạn có thể bật [Khung lưới](settings.md#wireframe) hoặc đơn giản là tắt [Tô bóng mượt](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Menu Tô pô của Nomad có nhiều thẻ, xếp trên hai hàng:

| Phương pháp                           | Biểu tượng                   | Mô tả                                                            |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Đa phân giải](#multiresolution)      | ![](/icons/multires.webp)   | Chỉnh sửa nhiều cấp độ chi tiết nhờ phép phân chia               |
| [Remesh voxel](#voxel-remesher)       | ![](/icons/voxel.webp)      | Tính lại một tô pô mới có mật độ đồng đều                        |
| [Tô pô động](#dynamic-topology)       | ![](/icons/dynamic.webp)    | Thêm/bớt mặt tại chỗ, theo thời gian thực khi điêu khắc hoặc vẽ  |
| [Khác](#misc)                         | ![](/icons/topo_extra.webp) | Đóng lỗ, buộc manifold và chuyển thành Triplanar                 |
| [Hình cơ bản](#primitive)             | ![](/icons/dot.webp)        | Tùy chọn của hình cơ bản                                         |
| [Tinh giảm](#decimation)              | ![](/icons/decimate.webp)      | Giảm số mặt mà vẫn giữ được hình dạng                         |
| [Tái định hình tứ giác](#quad-remesh) | ![](/icons/quad.webp)       | Dựng lại đối tượng với bố cục tứ giác gọn gàng                   |
| [Unwrap UV](#uv-unwrap)               | ![](/icons/uv.webp)         | Tạo UV để dán kết cấu                                            |
| [Bake](#bake)                         | ![](/icons/bake.webp)       | Bake chi tiết và màu vẽ sang kết cấu, đỉnh hoặc dấu VDM          |


## Thống kê đa giác {#polygon-stats}

![](/images/topology_stats.webp)

Phần trên cùng của mỗi thẻ hiển thị số đa giác của đối tượng đang chọn, và của toàn bộ cảnh khi cảnh có nhiều hơn một đối tượng. Các cột lần lượt là số đỉnh, số tam giác, số tứ giác (đa giác 4 cạnh) và số tọa độ UV (bằng 0 khi đối tượng không có UV).

Chạm vào phần này để xem danh sách mọi đối tượng trong cảnh kèm số liệu chính xác của chúng, bao gồm cả số nhóm mặt.

## ![](/icons/cog.webp) Menu bánh răng {#gear-menu}
Một số phần, chẳng hạn trong thẻ [Tái định hình tứ giác](#quad-remesh) và [Bake](#bake), có thêm tùy chọn. Mở chúng bằng biểu tượng bánh răng cạnh tiêu đề của phần đó.

## ![](/icons/multires.webp) Đa phân giải {#multiresolution}

![](/images/topology_multires_menu.webp)

### Đa phân giải là gì? {#what-is-multiresolution}
Tính năng đa phân giải hữu ích trong hai trường hợp chính:
- Dùng thuật toán phân chia mượt để tăng số đa giác của đối tượng
- Quản lý nhiều cấp độ phân giải, để bạn có thể chuyển qua lại giữa chỉnh sửa ở quy mô nhỏ và quy mô lớn

![](/videos/multiresolution.mp4)

#### Quy trình làm việc với đa phân giải {#multiresolution-workflow}
Điểm quan trọng của đa phân giải là bạn có thể quay về một cấp độ thấp hơn, chỉnh sửa đối tượng, rồi trở lại cấp độ cao nhất mà không mất chi tiết ở độ phân giải cao. Mọi chi tiết ở độ phân giải cao sẽ được tự động chiếu lại.

[Lớp](layers.md#layers) dùng được ở mọi cấp độ phân giải.

::: warning
Nếu bạn dùng một công cụ làm thay đổi tô pô của đối tượng, bạn sẽ mất tất cả các cấp độ phân giải khác của nó!
Nomad luôn cảnh báo bạn trước khi điều đó xảy ra, ví dụ khi bạn dùng:
- [Remesh voxel](#voxel-remesher)
- [Tô pô động](#dynamic-topology)
- [Công cụ Cắt](tools.md#trim)
- [Công cụ Tách](tools.md#split)
:::


### Thanh trượt đa phân giải {#multiresolution-slider}
Thanh trượt này cho biết đối tượng hiện tại có bao nhiêu cấp độ phân chia. Nếu có 6 vạch dọc thì có 6 cấp độ phân chia. Vòng tròn đánh dấu cấp độ đang được hiển thị.

Các biểu tượng nhỏ phía trên thanh trượt cho biết những tùy chọn nào (`Khóa cấp độ 0`, `Tuyến tính`, `Biên sắc nét`, `Giữ tam giác`) đã được dùng cho từng cấp độ.

### Đảo ngược {#reverse}
Khi đang ở cấp độ phân chia thấp nhất, nút đảo ngược sẽ thử tạo một cấp độ thấp hơn cấp hiện tại. Lưu ý rằng việc này thường chỉ thành công nếu ngay từ đầu đối tượng đã được tạo bằng phép phân chia, chẳng hạn trong Nomad hoặc trong các ứng dụng 3d khác hỗ trợ bề mặt phân chia đa phân giải.

### Phân chia {#subdivide}
Nút *Phân chia* sẽ nhân số đa giác lên 4 lần, vì vậy hãy để ý số đa giác vì nó có thể tăng rất nhanh! Nomad sẽ hỏi xác nhận khi kết quả quá nặng.
Một đặc điểm quan trọng của *bề mặt phân chia* là chúng sẽ hội tụ về một *bề mặt mượt*.
Để hiểu cách nó hoạt động, bạn có thể thử nút *Phân chia* trên một đối tượng chỉ có vài đa giác.

Bạn có thể tắt hiệu ứng *làm mượt* này bằng tùy chọn `Tuyến tính`.

### Xóa cấp thấp hơn {#delete-lower}
Xóa các cấp độ phân chia nằm dưới cấp đang hiển thị, nếu có. Nếu lỡ tay xóa, bạn có thể tạo lại chúng bằng nút Đảo ngược.

### Xóa cấp cao hơn {#delete-higher}
Xóa các cấp độ phân chia nằm trên cấp đang hiển thị, nếu có.

### ![](/icons/lock.webp) Khóa cấp độ 0 {#lock-lv0}
Giữ nguyên hình dạng của cấp độ phân chia thấp nhất khi bạn điêu khắc ở các cấp cao hơn. Màu vẽ thì vẫn được truyền xuống cấp độ 0. Điều này có thể quan trọng nếu đối tượng được tạo trong một ứng dụng khác và lưới gốc phải được giữ nguyên.

Tùy chọn này chỉ có trước lần phân chia đầu tiên. Khi nó tắt, những thay đổi lớn ở các cấp cao hơn sẽ làm dịch chuyển cấp độ 0.

### ![](/icons/linear.webp) Tuyến tính {#linear-subdivision}
Phân chia lưới mà không làm mượt.

### ![](/icons/group.webp) Biên sắc nét {#sharp-border}
Nếu đối tượng có nhóm mặt, bật tùy chọn này sẽ giữ sắc nét đường biên giữa các nhóm mặt. Bạn có thể đặt tùy chọn này riêng cho từng cấp độ phân chia (thanh trượt sẽ hiện một biểu tượng nhỏ phía trên cấp độ đó).

### ![](/icons/triangle.webp) Giữ tam giác {#keep-triangles}
Hầu hết các hệ thống bề mặt phân chia thông dụng sẽ cố chuyển mọi đa giác thành tứ giác khi phân chia. Tùy chọn này buộc phép phân chia dùng tam giác thay vào đó.

::: tip

Mặc định, phép phân chia sẽ làm mượt mọi cạnh sắc. Để giữ cạnh hơi sắc, hãy thử dùng `Tuyến tính` hoặc `Biên sắc nét` cho 2 cấp phân chia đầu tiên, rồi tắt chúng ở các cấp cao hơn. Bạn sẽ có một lưới phân chia bán sắc nét.

:::

### Hiện cấp cao nhất {#show-highest-level}
Hiển thị cấp độ cao nhất với đầy đủ chi tiết trong khi bạn điêu khắc ở một cấp thấp hơn. Rất tiện để xem kết quả cuối cùng khi bạn thực hiện các thay đổi lớn.

### Khung lưới: Chỉ cấp độ 0 {#wireframe-level-0-only}
Khi [Khung lưới](settings.md#wireframe) đang bật, chỉ hiển thị khung lưới của cấp thấp nhất. Khung lưới dày đặc của các cấp cao có thể che mất hình dạng.


## ![](/icons/voxel.webp) Remesh voxel {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Khi dùng `Remesh voxel`, toàn bộ lưới sẽ được buộc có một độ phân giải đồng đều, nghĩa là mọi đa giác có kích thước xấp xỉ nhau. Điều này rất hữu ích khi bạn không muốn bận tâm đến tô pô mà chỉ muốn điêu khắc tự do.

Một quy trình điêu khắc điển hình có thể bắt đầu bằng `Remesh voxel` để dựng khối thô ở độ phân giải thấp.
Thỉnh thoảng hãy bấm nút *Tái tạo lưới* khi bạn kéo giãn lưới quá nhiều, để tránh bị méo.

![](/videos/voxel_remesher.mp4)


::: tip Voxel là gì?
Như đã nói ở trên, Nomad là phần mềm làm việc với đa giác, nhưng `Remesh voxel` là một ngoại lệ: nó dùng (tạm thời) một cách tiếp cận khác để tái tạo lưới.

Một khác biệt lớn là cách tiếp cận voxel không chấp nhận các phần tự giao nhau, nên chúng sẽ được hợp nhất.
Nó cũng không hỗ trợ lưới có lỗ.

Lỗ ở đây không phải là `genus hole` (cái `lỗ` của bánh donut), mà là lưới không `kín nước`/`khép kín`.
Nói cách khác, trước khi tái tạo lưới, mọi lỗ sẽ được lấp đầy, tương tự như [công cụ Cắt](tools.md#trim) hoặc [tính năng lấp lỗ](#holes). Tùy chọn [Lỗ](#voxel-holes) bên dưới cho phép chọn cách lấp.
:::

### ![](/icons/voxel.webp) Tái tạo lưới {#voxel-remesh}
Thực hiện remesh voxel. Các biểu tượng nhỏ trên nút nhắc bạn những tùy chọn nào bên dưới đang bật.

### Độ phân giải {#voxel-resolution}
Kích thước voxel dùng trong phép tính, giá trị càng cao thì càng nhiều chi tiết. Trong khi bạn thay đổi thông số này, một họa tiết bàn cờ sẽ được phủ lên lưới để xem trước kết quả.

Ống nhỏ giọt lấy độ phân giải theo mật độ lưới tại chỗ bạn chạm. Nút hình khối bên cạnh chuyển giá trị sang `Độ dài cạnh` tính theo đơn vị thế giới: khi đó cùng một giá trị sẽ cho cùng mức chi tiết trên mọi đối tượng.

### Tạo dựng đa độ phân giải {#build-multiresolution}
Tạo các cấp đa phân giải thấp hơn cho kết quả remesh voxel. Nếu bạn dùng họa tiết bàn cờ để chọn độ phân giải và đặt tùy chọn này là 2, kết quả cuối cùng sẽ có chi tiết khớp với thanh trượt độ phân giải, và trong thẻ Đa phân giải nó sẽ ở cấp 2, nghĩa là bạn có thêm các lưới đa phân giải thấp hơn ở cấp 1 và cấp 0. Đây là một cách hay để vừa có lưới gọn gàng với các đa giác đều nhau, vừa có một lưới điều khiển ở độ phân giải thấp.

Ở độ phân giải cao, nó còn chạy nhanh hơn và tốn ít bộ nhớ hơn. Nhưng với độ phân giải thấp và nhiều cấp, bạn sẽ mất chi tiết.

::: tip Mẹo: Tạo dựng đa độ phân giải và làm mịn ổn định

Tùy chọn này đôi khi tạo ra các "vòng" trong hình khối, khó làm mịn và gây ra những nốt sần nhỏ. Nếu gặp trường hợp này, hãy bật 'Làm mịn ổn định' trong tùy chọn của công cụ Làm mịn.

:::

### Làm dày phần mỏng {#thicken-thin-parts}
Những phần mỏng hơn kích thước voxel có thể bị đứt hoặc biến mất khi remesh. Tùy chọn này làm dày chúng để chúng được giữ lại, giá trị càng cao thì càng dày. Tùy chọn này không dùng được cùng `Cạnh sắc` hoặc `Biên sắc nét`.

### Lỗ {#voxel-holes}
Cách đóng các lỗ trước khi tái tạo lưới:

* `Lấp đầy` - Mỗi lỗ được đóng riêng, bắt đầu từ đường biên của nó.
* `Hình dạng` - Các lỗ được đóng theo bề mặt xung quanh, và các mảnh hở chồng lên nhau sẽ được nối lại.

### ![](/icons/angle.webp) Cạnh sắc {#keep-sharp-edges}
Bám các điểm mới vào cạnh sắc của lưới ban đầu. Tùy chọn này chủ yếu hữu ích cho các phép boolean với hình cơ bản đơn giản, và có thể gây méo.

### ![](/icons/group.webp) Biên sắc nét {#voxel-sharp-border}
Các mặt mới đi theo đường biên giữa các nhóm mặt, và đường biên giữ sắc nét ở những chỗ bề mặt gấp khúc dọc theo nó.

### ![](/icons/group_separate.webp) Giữ các nhóm riêng {#keep-groups-separate}
Mỗi nhóm mặt được tái tạo lưới riêng: các nhóm không bao giờ hợp nhất, và mỗi nhóm là một mảnh khép kín thuộc nhóm của riêng nó. Ở chế độ này không tạo đa phân giải. Tùy chọn này có khi đối tượng có nhiều nhóm mặt.

## ![](/icons/dynamic.webp) Tô pô động {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Đa phân giải và remesh voxel là những cách kiểm soát tô pô phổ biến trong ngành, nhưng cả hai đều đòi hỏi bạn phải để ý để không kéo giãn đa giác quá mức, hay ép chúng quá chặt.

Tô pô động là một cách khác. Khi bạn điêu khắc, Nomad sẽ tự thêm và bớt đa giác trong lúc bạn đưa nét cọ, nên khi khắc chi tiết nhỏ, nhiều đa giác nhỏ sẽ được thêm đúng chỗ cần, còn khi làm mịn ở chỗ khác thì đa giác sẽ được bớt đi.

Lưu ý rằng tô pô động dùng đa giác tam giác chứ không phải tứ giác. Trông có thể hơi lộn xộn, nhưng tốt nhất là đừng nhìn khung lưới, cứ tập trung tạo một tác phẩm đẹp mà không lo về tô pô, sau đó bạn có thể dùng một công cụ tái tạo lưới khác của Nomad để có lưới tứ giác gọn gàng.

Xem video bên dưới để thấy nó hoạt động.

![](/videos/dynamic.mp4)

### Kích hoạt {#enabled}
Bật tô pô động. Một biểu tượng DynTopo sẽ xuất hiện bên dưới thanh trượt bán kính và cường độ của cọ, để bạn bật/tắt DynTopo cho từng công cụ. Nó có thể ảnh hưởng đáng kể đến hiệu năng, và các lớp vẫn được cập nhật chính xác.

### Chi tiết {#dyn-detail}
Điều chỉnh mức chi tiết; cách hoạt động thay đổi theo lựa chọn 'Chi tiết dựa trên...', xem bên dưới. Ở chế độ `Màn hình`, nhãn hiển thị kích thước tam giác mục tiêu tính bằng điểm ảnh. Ở chế độ `Hằng số`, một ống nhỏ giọt cho phép bạn lấy mức chi tiết theo mật độ lưới tại chỗ bạn chạm.

### Chi tiết dựa trên... {#detail-based-on}
| Phương pháp | Mô tả                                                           |
| :---------: | :-------------------------------------------------------------: |
| Màn hình    | Mức chi tiết phụ thuộc vào kích thước của đối tượng trên màn hình. Đặt thanh trượt chi tiết từ 100% trở lên cho chi tiết tinh, tạo tam giác nhỏ, hoặc 1% cho chi tiết thấp, tạo tam giác lớn.  |
| Bán kính    | Bán kính công cụ quyết định mức chi tiết. Dùng bán kính nhỏ cho chi tiết tinh, bán kính lớn cho chi tiết thấp. Thanh trượt chi tiết là hệ số nhân của tỷ lệ này.                     |
| Hằng số     | Thanh trượt chi tiết quyết định mức chi tiết, không phụ thuộc vào kích thước màn hình hay kích thước công cụ. Đây cũng chính là giá trị của thanh trượt [Chi tiết](#all-detail) trong phần `Tái tạo lưới`.             |

::: tip MẸO: Chế độ Bán kính

Để hiểu rõ hơn cách chế độ bán kính hoạt động, hãy dùng một ngón tay kéo thanh trượt chi tiết, đồng thời dùng ngón khác thay đổi bán kính công cụ. Bạn sẽ thấy chúng liên kết với nhau thế nào.

:::

### Ưu tiên... {#prefer}
| Phương pháp | Mô tả                   |
| :---------: | :---------------------: |
| Tốc độ      | Ưu tiên hiệu năng       |
| Chất lượng  | Ưu tiên chất lượng      |

Khi bạn ưu tiên `Chất lượng`, có 2 khác biệt chính:
- việc tinh chỉnh lưới được thực hiện trước khi điêu khắc, nên khi vẽ hay điêu khắc chi tiết rất nhỏ sẽ ít lỗi nội suy hơn
- việc tinh chỉnh chạy cho đến khi đạt đúng mức chi tiết, thay vì tăng dần từng bước.
 
Nhờ vậy, dù bạn điêu khắc chi tiết rất nhỏ hay đưa nét nhanh, tô pô vẫn luôn được tinh chỉnh như mong đợi


### ![](/icons/pressure.webp) Sử dụng áp lực trên bán kính {#use-pressure-on-radius}
Chỉ có tác dụng khi chế độ `Bán kính` được chọn. Khi bật, mức chi tiết luôn khớp với kích thước cọ, kể cả khi kích thước cọ thay đổi theo lực nhấn bút.

### Sử dụng sự suy giảm nét {#use-stroke-falloff}

Đưa cả đường cong suy giảm và alpha của cọ vào phép tính của DynTopo.

### Phương pháp {#method}
Chọn cách tô pô động thay đổi lưới, cả khi bạn điêu khắc lẫn khi bạn dùng [Tái tạo lưới](#dyn-remesh):

| Phương pháp     | Mô tả                                                                 |
| :-------------: | :-------------------------------------------------------------------: |
| Đồng nhất hóa   | Có thể thêm và bớt mặt, đây là chế độ dùng trong video ở trên         |
| Chia tách       | Chỉ thêm mặt mới, không thể bớt mặt                                   |
| Tinh giảm       | Chỉ bớt mặt, không thể thêm mặt mới                                   |

### ![](/icons/shield.webp) Bảo vệ khu vực đã che {#protect-masked-area}
Giữ cho tô pô của vùng đã phủ mặt nạ không bị thay đổi.

### ![](/icons/normal.webp) Ngoại suy đỉnh {#vertex-extrapolation}
Đặt các điểm lên một bề mặt mượt theo độ cong xung quanh, thay vì nằm phẳng trên các mặt sẵn có.

### Chi tiết {#all-detail}
Độ phân giải dùng cho thao tác tái tạo lưới. Nếu DynTopo ở chế độ 'Hằng số', giá trị này trùng với thanh trượt Chi tiết ở đầu menu. Ống nhỏ giọt lấy mức chi tiết theo mật độ lưới tại chỗ bạn chạm.

### Tái tạo lưới {#dyn-remesh}
Tái tạo toàn bộ lưới bằng thuật toán của DynTopo. Thông thường bạn nên dùng [Remesh voxel](#voxel-remesher) để tái tạo toàn bộ lưới.

Tuy vậy, so với voxel, nó có ưu điểm là lưới không cần khép kín, và vùng đã phủ mặt nạ sẽ được bảo vệ, nên bạn kiểm soát tốt hơn chỗ nào dày đặc hơn, chỗ nào thưa hơn.



## ![](/icons/topo_extra.webp) Khác {#misc}

![](/images/topology_misc_menu.webp)

Thẻ này tập hợp các công cụ để dọn dẹp hoặc chuyển đổi lưới: đóng các lỗ, buộc lưới thành manifold, hoặc biến nó thành một Triplanar.

### ![](/icons/hole.webp) Lỗ {#holes}
![](/images/topology_holes_menu.webp)
Phần lớn thời gian, đối tượng của bạn sẽ kín nước, nghĩa là lưới 'khép kín'.

Nếu đối tượng có lỗ, bạn có thể lấp chúng.

![](/videos/hole_filling.mp4)

::: tip
Khi bạn chạy Remesh voxel, mọi lỗ đều tự động được đóng lại, dù bạn dùng nó trên 1 hay nhiều lưới.
:::

#### Đóng lỗ {#close-holes}
Thực hiện việc đóng lỗ.

#### Tùy chọn {#holes-gear-menu}
Các tùy chọn này thay đổi cách lấp lỗ:

##### Nhóm mặt {#fill-face-group}
Chọn nhóm mặt cho các mặt mới:

* `Hỗn hợp` - Lỗ được bao quanh bởi một nhóm mặt duy nhất sẽ dùng lại nhóm đó, lỗ tiếp giáp nhiều nhóm sẽ có nhóm mới.
* `Mới` - Các lỗ được lấp sẽ có nhóm mặt mới.
* `Tái sử dụng` - Mỗi lỗ nhận nhóm mặt bao quanh nó nhiều nhất.

##### Chi tiết {#fill-detail}
Mật độ đa giác dùng để lấp lỗ. Khi bạn kéo thanh trượt này, một họa tiết bàn cờ sẽ hiện trên mô hình, cho biết kích thước tam giác sẽ dùng. Ô chọn sẽ tắt tính năng này và chỉ dùng các điểm sẵn có, thường tạo ra những tam giác dài và mảnh phủ qua lỗ, khó điêu khắc.

##### Bắc cầu {#fill-non-manifold}
Lấp một lỗ cùng các đảo bên trong nó thành một bề mặt duy nhất, thay vì lấp riêng từng đường biên. Góc càng lớn thì càng bắc cầu được những lỗ cong hơn. Ô chọn dùng để tắt tùy chọn này.

### ![](/icons/cog.webp) Buộc manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Cố gắng dọn các cạnh không manifold. Hữu ích cho những phần mềm khác không hỗ trợ cạnh dùng chung cho hơn 2 mặt.

#### Làm sạch {#clean}
Thực hiện việc làm sạch.

#### Tùy chọn {#force-manifold-gear-menu}
Tùy chọn này thay đổi cách làm sạch lưới:

##### Xóa các mặt nhỏ {#delete-small-faces}
Ngưỡng dùng để xóa và gộp các đa giác nhỏ. Bật nó bằng ô chọn tương ứng.


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
![](/images/topology_triplanar_menu.webp)
Chuyển lưới thành một hình cơ bản [Triplanar](scene.md#triplanar).
Bạn có thể sẽ mất khá nhiều chi tiết trong quá trình này: lớp, màu vẽ và đa phân giải cũng bị mất.

#### Buộc hình khối {#force-cubic}
Buộc Triplanar là một khối lập phương. Nếu không, Triplanar sẽ khớp với hộp bao gần nhất quanh đối tượng.

#### Chuyển đổi {#convert}
Thực hiện việc chuyển sang Triplanar.

#### Độ phân giải {#triplanar-resolution}
Độ phân giải của lưới Triplanar, giá trị càng cao thì giữ được càng nhiều chi tiết.

## ![](/icons/decimate.webp) Tinh giảm {#decimation}

![](/images/topology_decimation.webp)

Giảm số đa giác trong khi cố giữ càng nhiều chi tiết càng tốt, bằng cách dùng đa giác tam giác.

Tính năng này hữu ích khi bạn muốn xuất để in 3d.
Tuy nhiên, bạn không nên dùng nó nếu còn muốn tiếp tục điêu khắc, vì nó có thể tạo ra các tam giác không đều.

Lưu ý rằng vùng đã phủ mặt nạ sẽ không bị tinh giảm.

![](/videos/decimate.mp4)

::: tip

Dùng [công cụ Quad Remesher](tools.md#quad-remesher) trên đối tượng nhiều đa giác có thể mất nhiều thời gian tính toán và cho kết quả khó kiểm soát. Xử lý trước lưới bằng [nhóm mặt](tools.md#facegroup) và tinh giảm sẽ giúp Quad Remesher chạy nhanh hơn nhiều và cho bạn kiểm soát tô pô tốt hơn hẳn.

* Chia nhóm mặt trên lưới để xác định hướng chạy tứ giác lý tưởng của bạn.
* Làm giãn nhóm mặt (relax) để có đường biên nhóm mặt mượt mà.
* Tinh giảm. Bước này đảm bảo không có mặt mỏng hay méo ở biên nhóm mặt. Trong `Bảo vệ đường viền`, hãy chắc chắn `Nhóm mặt` được bật. Nhờ đó các cạnh tam giác sẽ bám chính xác theo biên nhóm mặt.
* Trong tùy chọn của Quad Remesher, hãy tắt relax (vì bạn đã làm giãn lưới rồi), và bạn sẽ có kết quả tốt.

:::

### Tinh giảm {#decimate}
Bắt đầu thao tác tinh giảm.

Các biểu tượng bên cạnh nút tinh giảm thể hiện các tùy chọn bên dưới, và cho phép bạn bật/tắt chúng. Con số phần trăm cho biết tùy chọn đó mạnh đến mức nào.

* ![](/icons/palette.webp)  `Bảo tồn vẽ` - Đặt nhiều tam giác hơn ở những chỗ có chi tiết vẽ.
* ![](/icons/triforce.webp) `Mặt đồng nhất` - Ưu tiên tạo các tam giác có kích thước đều nhau.
* ![](/icons/hole.webp)  `Lỗ` - Cố giữ nguyên các đường biên gần phần hở và lỗ.
* ![](/icons/group.webp) `Nhóm mặt` - Cố giữ nguyên đường biên giữa các nhóm mặt.
* ![](/icons/uv.webp) `UV` - Cố giữ nguyên đường biên UV.

### Hướng đến hình tam giác {#target-triangles}
Đặt số tam giác mục tiêu. Giá trị mặc định là 50%, nút phần trăm/mục tiêu cho phép chuyển giữa tỷ lệ phần trăm và số đa giác chính xác.

### Tùy chọn {#decimate-gear-menu}
Mỗi tùy chọn có một ô chọn để bật/tắt, và một giá trị cho độ mạnh:

#### ![](/icons/palette.webp) Bảo tồn vẽ {#preserve-painting}
Giá trị này quyết định chi tiết vẽ được giữ lại chính xác đến đâu. Giá trị càng cao thì càng giữ được nhiều màu vẽ. Đặt về 0 nếu bạn không quan tâm đến màu vẽ.

#### ![](/icons/triforce.webp) Mặt đồng nhất {#uniform-faces}
Giá trị càng cao thì các tam giác tạo ra càng có kích thước tương đồng.

#### Bảo vệ đường viền {#preserve-borders}
Ngăn các đường biên bị tinh giảm. Bạn có thể đặt trọng số cho biên `Lỗ`, `Nhóm mặt` hoặc `UV` (`UV` cần đối tượng có UV).

## ![](/icons/quad.webp) Tái định hình tứ giác {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Dựng lại đối tượng với bố cục tứ giác gọn gàng. Thẻ này có nhiều trình tái tạo lưới, mỗi trình có nút `Tái tạo lưới`, thanh trượt `Hướng đến hình tứ giác` và menu bánh răng riêng. Hãy thử chúng trên đối tượng của bạn, kết quả khá khác nhau đấy!

### Quad Remesher {#quad-remesher}
Cùng trình tái tạo lưới với công cụ [Quad Remesher](tools.md#quad-remesher), do [Exoside](https://exoside.com/) phát triển. Nó chỉ có trên một số nền tảng và cần mua thêm: cho đến lúc đó, nút `Tái tạo lưới` hiển thị biểu tượng giỏ hàng.

`Chọn công cụ` chuyển sang công cụ Quad Remesher, để vẽ đường dẫn hướng và vẽ mật độ. Menu bánh răng chứa `Số Lượng Tứ Giác Thích Ứng`, `Kích Thước Thích Ứng` (ở 100% kích thước tứ giác theo độ cong, ở 0% các tứ giác đều nhau), `Tự Động Phát Hiện Cạnh Cứng` và `Chiếu lại Điểm Đỉnh`.

::: tip
Ở những nơi có sẵn, Quad Remesher thường cho kết quả tốt nhất và khả năng kiểm soát cao nhất.
:::

### AutoRemesher {#autoremesher}
Một trình tái tạo lưới tứ giác khác, với các tùy chọn để điều chỉnh kích thước và hình dạng tứ giác theo bề mặt.

#### ![](/icons/cog.webp) Menu bánh răng của AutoRemesher {#autoremesher-gear-menu}
Menu bánh răng có các tùy chọn nâng cao sau:

##### Tỷ lệ cạnh {#edge-scaling}
Thay đổi kích thước tứ giác, giá trị càng cao thì tứ giác càng lớn.

##### Độ thích ứng {#adaptivity}
Điều chỉnh mật độ tứ giác theo độ cong. 0 cho tứ giác đều nhau, 1 cho tứ giác nhỏ hơn ở những vùng cong.

##### Tính dị hướng {#anisotropy}
Kéo dài tứ giác theo hướng phẳng nhất của bề mặt. 0 cho tứ giác vuông, 1 cho tứ giác thuôn dài trên các phần hình ống và gờ.

##### Cạnh sắc {#sharp-edge}
Các cạnh bị gập nhiều hơn góc này sẽ được giữ lại như những đường sắc nét.

##### Làm mượt pháp tuyến {#smooth-normal}
0 giữ bề mặt có các mặt phẳng rõ rệt khi tái tạo lưới. Giá trị cao hơn làm mượt bề mặt bằng cách tính đến pháp tuyến của các đỉnh.

##### Lấp đầy lỗ tối đa {#autoremesher-max-fill-hole}
Thuật toán đôi khi tạo ra những lỗ không mong muốn. Nếu một lỗ có ít đỉnh hơn giá trị này, nó sẽ được lấp.

### Instant Mesh {#quad-remesh-instant}
Tái tạo lưới bằng [thuật toán Instant Meshes của Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Nó phân tích hướng chạy của lưới và tạo ra tô pô tứ giác gọn gàng.

#### Tái tạo lưới {#instant-remesh}
Bắt đầu thao tác tái tạo lưới.

#### Hướng đến hình tứ giác {#target-quads}
Số đa giác tứ giác mà trình tái tạo lưới sẽ cố gắng tạo ra.

#### ![](/icons/cog.webp) Menu bánh răng của Instant Mesh {#quad-remesh-instant-gear-menu}
Menu bánh răng có các tùy chọn nâng cao sau:

##### Góc gấp nếp {#crease-angle}
Ngưỡng góc sắc, giúp định hướng thao tác tái tạo lưới. Bật nó bằng ô chọn tương ứng.

##### Lấp đầy lỗ tối đa {#max-fill-hole}
Thuật toán đôi khi tạo ra những lỗ không mong muốn. Nếu một lỗ có ít đỉnh hơn giá trị này, nó sẽ được lấp.

### QuadriFlow {#quadriflow}
Tái tạo lưới bằng thuật toán QuadriFlow, một cách khác để có bố cục tứ giác gọn gàng.

#### ![](/icons/cog.webp) Menu bánh răng của QuadriFlow {#quadriflow-gear-menu}
Menu bánh răng có các tùy chọn nâng cao sau:

##### Bảo vệ đường viền {#quadriflow-preserve-boundary}
Bảo vệ đường biên của các lỗ.

##### Giữ cạnh sắc {#keep-sharp}
Căn các tứ giác theo cạnh sắc của bề mặt.

##### Luồng chi phí tối thiểu {#min-cost-flow}
Dùng bộ giải luồng chi phí tối thiểu cho bố cục tứ giác. Chậm hơn, nhưng có thể cho tô pô đều đặn hơn.

## ![](/icons/uv.webp) Unwrap UV {#uv-unwrap}
Tính tọa độ kết cấu (UV) cho đối tượng đang chọn. Nomad có hai phương pháp, `UVAtlas` và `BFF`, mỗi phương pháp có nút `Khai triển UV` riêng.

![](/videos/unwrap.mp4)

::: tip UV là gì?
Một cách ví von quen thuộc cho UV là gói quà: làm sao cắt giấy gói để bọc kín một món đồ mà không bị chồng lên nhau?

UV cũng tương tự, nhưng thay vì cắt giấy, bạn cắt chính đối tượng. Hãy tưởng tượng mô hình của bạn làm bằng nhựa mỏng: bạn sẽ cắt nó ra sao để trải phẳng, vẽ lên nó khi đang phẳng, rồi ghép lại như cũ?

Giờ hãy tưởng tượng bề mặt mô hình làm bằng vải thun co giãn. Bạn có thể kéo căng cho phẳng, hoặc cắt, hoặc kết hợp cả hai. Nhưng nếu bạn vẽ một bàn cờ lên đối tượng khi nó đang trải phẳng, bàn cờ sẽ bị méo khi bạn ghép lại. Cách nào tốt hơn: cắt nhiều mà ít méo, hay cắt ít mà méo nhiều?

UV là chỉ dẫn cho phần mềm 3d biết cách 'cắt và kéo giãn' đối tượng khi dán kết cấu. Công cụ UVAtlas thường theo hướng 'cắt nhiều, ít méo'.


:::

::: tip UV với Nomad và các ứng dụng khác

Phần lớn các mô hình có kết cấu bạn tìm thấy trên mạng đều được dán kết cấu bằng UV. Nomad có thể nhập và hiển thị chúng qua bảng [vật liệu](material.md#textures).

Với các mô hình làm trong Nomad, bạn có thể vẽ trực tiếp lên đối tượng mà không cần UV. Nếu cần xuất sang ứng dụng khác, ví dụ [Procreate](https://procreate.art/), bạn có thể 'bake' thông tin màu của Nomad vào kết cấu thông qua UV.

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
UVAtlas thường ưu tiên cắt ra nhiều đảo hơn để giảm méo.

#### Khai triển UV {#unwrap}
Tính UV cho đối tượng đang chọn.

#### Tùy chọn {#uvatlas-gear-menu}
Các nút bên cạnh `Khai triển UV`:

##### Nhóm mặt {#atlas-face-group}
Khi nút hiển thị `Có`, các nhóm mặt sẽ quyết định đường cắt UV. Thiết lập này dùng chung với BFF.

##### Xóa UV {#delete-uvs}
Nút thùng rác xóa UV của đối tượng.

##### Kiểm tra {#uv-inspect}
Hiển thị UV của đối tượng ở nền.

#### Độ giãn tối đa {#max-stretch}
Giá trị thấp tạo ít méo hơn và nhiều đảo hơn, giá trị cao tạo nhiều méo hơn và ít đảo hơn.

#### Khoảng cách giữa các đảo {#island-spacing}
Khoảng đệm giữa các đảo. Giá trị thấp ít lãng phí diện tích hơn, nhưng dễ khiến kết cấu bị lem sang đảo bên cạnh.

::: warning
Tính UV có thể mất khá nhiều thời gian, tốt nhất là dùng lưới có ít hơn 100k đỉnh.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

UV của BFF theo hướng 'cắt ít, méo nhiều'.

#### Tùy chọn {#uv-bff-gear-menu}
Bên cạnh `Khai triển UV` cũng có các nút `Nhóm mặt`, xóa và `Kiểm tra` giống như [UVAtlas](#uvatlas-gear-menu).

##### Nhóm mặt {#bff-face-group}

Dùng nhóm mặt để xác định đường cắt UV.

#### Số lượng nón {#cone-count}
Xác định số phép chiếu chính được dùng. Giá trị thấp tạo ít đảo hơn nhưng méo nhiều hơn. Giá trị cao tốn nhiều thời gian tính hơn.

#### Mảnh vá không đường nối {#seamless-patches}
Ảnh hưởng đến cách sắp xếp các mảnh UV, và có thể gây méo đáng kể. Nó hoạt động tốt nhất với các nhóm mặt được tạo cẩn thận.

::: warning
BFF có thể tạo UV chồng lên nhau nếu lưới có "quai" (như lỗ của bánh donut).
:::

### ![](/icons/preview.webp) Hiển thị UV sau khi unwrap {#show-uv-after-unwrap}
Mở trình xem UV sau khi unwrap, để bạn kiểm tra kết quả ngay.

### ![](/icons/bake.webp) Bake: Kết cấu → Kết cấu {#unwrap-bake-texture}
Chỉ có khi vật liệu của đối tượng có kết cấu. Khi bạn unwrap lại, các kết cấu sẽ được chuyển sang UV mới để vẫn khớp. Độ phân giải mặc định là `Tự động`, bằng kết cấu lớn nhất, hoặc bạn có thể tự đặt.

## ![](/icons/bake.webp) Bake {#bake}
Thẻ này chuyển chi tiết và màu vẽ giữa các đối tượng, cũng như giữa đỉnh và kết cấu.

`Từ độ phân giải cao` lấy các đối tượng khác làm nguồn, con số trong ngoặc là số lượng của chúng. Nomad chọn chúng như sau:

- mọi đối tượng đang chọn đều được dùng, và đối tượng chọn chính là đích (được tô sáng rõ nhất trong menu [Cảnh](scene.md))
- nếu chỉ có một đối tượng được chọn, Nomad dùng tất cả các đối tượng đang hiển thị
- nếu mọi đối tượng khác đều bị ẩn (ví dụ bằng Solo), toàn bộ cảnh sẽ được dùng

### ![](/icons/bake.webp) Bake → Kết cấu {#bake-texture}
![](/images/topology_bake_menu.webp)

Bake kết cấu sẽ tạo kết cấu bằng cách chiếu các đối tượng đang hiển thị khác trong cảnh vào UV của đối tượng đang chọn. Đối tượng cần có UV.

Đây là quy trình bake điển hình:
- Bạn có một lưới với chi tiết và màu vẽ tinh xảo
- Nhân bản nó
- Tinh giảm bản sao (đặt `Bảo tồn vẽ` về 0)
- Unwrap UV cho nó
- Bake thôi!

Giờ bạn đã có một lưới độ phân giải thấp giữ được phần lớn màu vẽ và chi tiết của đối tượng ban đầu.

Sau thao tác này, màu đỉnh sẽ được chuyển vào một lớp mới đang tắt, để không xung đột với kết cấu.

#### Từ đối tượng này {#tex-from-itself}
Bake đối tượng vào chính UV của nó: màu vẽ trở thành kết cấu, và nếu đối tượng có các cấp đa phân giải, chi tiết của cấp cao nhất sẽ được bake vào cấp hiện tại (khi đó nút sẽ hiện biểu tượng đa phân giải). Cách này dễ thiết lập, nhưng thường bạn cần kiểm soát nhiều hơn, khi đó tùy chọn tiếp theo sẽ hữu ích hơn.

#### Từ độ phân giải cao {#tex-from-high-res}
Bake từ các đối tượng khác sang đối tượng đang chọn. Con số trong ngoặc cho biết số đối tượng khác sẽ được dùng làm nguồn độ phân giải cao, để bake vào đối tượng độ phân giải thấp có UV hiện tại. Các đối tượng khác không cần có bố cục hay tô pô giống đối tượng được bake, nên bạn có thể linh hoạt trong quy trình bake.

#### Độ phân giải {#tex-bake-resolution}
Độ phân giải của kết cấu được bake. Kết cấu bake luôn là hình vuông, nên 1024 sẽ tạo ảnh 1024x1024.

Các nút bên dưới là phím tắt cho những độ phân giải hay dùng. Để tham khảo, 512x512 khá nhỏ, phù hợp cho đồ họa web và hình khối đơn giản. 4096x4096 (gọi tắt là 4k) dành cho render chất lượng cao.

#### Màu sắc, Độ nhám, Độ kim loại, Pháp tuyến, Dịch chuyển, Phát sáng, Độ mờ {#tex-normal-roughness-metalness-color-emissive-opacity}
Các nút này quyết định những thuộc tính nào sẽ được bake, mỗi thuộc tính vào một map riêng. Khi bake xong, chúng sẽ được thêm làm kết cấu vào vật liệu của đối tượng hiện tại. `Dịch chuyển` bake độ cao của chi tiết thành một displacement map.

#### ![](/icons/cog.webp) Menu bánh răng của Bake {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Menu bánh răng có các tùy chọn nâng cao sau:

##### Sao lưu {#tex-backup}
Để xem trước kết cấu đã bake, thông tin màu vẽ của đối tượng cần được tắt. `Sao lưu (Vẽ tranh → Lớp)` sẽ chuyển mọi thông tin màu vẽ sang một lớp mới để dự phòng, nhờ đó bạn có thể dễ dàng bật/tắt nó.

##### Dùng đa độ phân giải {#tex-use-multires}
Dành cho `Từ đối tượng này` trên đối tượng có các cấp đa phân giải. Nomad đọc độ phân giải cao qua các cấp phân chia thay vì chiếu tia: nhanh hơn và không có lỗi chiếu. Tắt nó đi để bake bằng các tùy chọn bên dưới.

##### Nền mịn {#tex-smooth-base}
Dành cho `Dịch chuyển` trên đối tượng có các cấp đa phân giải. Đo độ dịch chuyển từ lưới gốc đã phân chia thay vì từ các mặt phẳng của nó. Hãy bật khi displacement map được dùng trên một lưới phân chia, như adaptive subdivision của Blender.

##### Khoảng cách tìm kiếm {#tex-cage-radius}
Khoảng cách tối đa dùng để tìm bề mặt nguồn. Mặc định khoảng cách này được giữ thấp để tránh lỗi, nhưng có thể tăng lên nếu các đối tượng nguồn ở xa đối tượng được bake.

##### Phép chiếu {#tex-projection}
Cách tìm bề mặt nguồn:

* `Tia` - Chiếu dọc theo pháp tuyến bề mặt.
* `Tia + gần nhất` - Dùng tia theo pháp tuyến, rồi dùng bề mặt gần nhất nếu tia không trúng.
* `Gần nhất` - Chiếu tới điểm gần nhất trên bề mặt nguồn.

##### Dịch chuyển tia {#tex-ray-offset}
Điều chỉnh điểm bắt đầu phép tính bake trên đối tượng được bake. Một khoảng lệch nhỏ khỏi bề mặt giúp tránh hầu hết các lỗi thường gặp. Nếu các đối tượng nguồn ở rất xa đối tượng được bake, có thể cần tăng khoảng lệch này. `Gần nhất` không dùng đến nó.


### ![](/icons/bake.webp) Chiếu lại → Đỉnh {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Chiếu chi tiết điêu khắc, màu vẽ, lớp, kết cấu thành giá trị đỉnh.

Có thể coi đây là phép ngược của bake: nếu bake chuyển thuộc tính đỉnh sang kết cấu, thì chiếu lại chuyển kết cấu (và các thuộc tính khác)
 trở lại đỉnh.

::: tip
Khi dùng `Bake → Kết cấu` hoặc `Chiếu lại → Đỉnh`, cả màu đỉnh lẫn kết cấu của vật liệu đều được tính đến.
:::

#### Từ đối tượng này {#vertex-from-itself}
Chuyển kết cấu của vật liệu thành giá trị đỉnh. Nút này chỉ hoạt động khi đối tượng có UV và kết cấu đang được bật trong vật liệu.

::: tip MẸO: Vẽ kết cấu
Nomad không hỗ trợ trực tiếp việc vẽ và chỉnh sửa kết cấu, nhưng bạn có thể đạt kết quả rất giống bằng cách chiếu kết cấu -> giá trị đỉnh, vẽ trên đỉnh, rồi bake đỉnh -> kết cấu:

1. Chuẩn bị một đối tượng ít đa giác có UV
1. Nạp kết cấu vào vật liệu của nó
1. Phân chia đủ để vẽ lên được
1. `Chiếu lại → Đỉnh` ở chế độ `Từ đối tượng này`, giờ kết cấu đã được chuyển thành giá trị đỉnh
1. Vẽ, làm mịn, bôi nhòe, đóng dấu, chỉnh sửa gì tùy ý
1. `Bake → Kết cấu` ở chế độ `Từ đối tượng này`. Những chỉnh sửa đó sẽ được chuyển ngược lại thành kết cấu.
:::

#### Từ độ phân giải cao {#vertex-from-high-res}
Chuyển các đối tượng khác thành giá trị đỉnh trên đối tượng đang chọn. Con số trên nút cho biết số đối tượng nguồn. Tính năng này chủ yếu dành cho lưới cũng có độ phân giải cao, thường với tô pô gọn gàng.

::: tip
Chiếu lại các đối tượng khác không chỉ dùng để chuyển thông tin màu từ chúng, mà còn để chiếu đỉnh lên các đối tượng khác, ví dụ chiếu băng gạc lên một nhân vật.
:::

#### Điểm đỉnh, Màu sắc, Độ nhám, Độ kim loại, Độ mờ, Mặt nạ, Lớp, Nhóm mặt {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Các nút này quyết định những thuộc tính nào sẽ được chiếu sang đối tượng đang chọn. `Lớp` chuyển các lớp của đối tượng khác sang lưới đang chọn.

#### ![](/icons/cog.webp) Menu bánh răng của Chiếu lại {#vertex-reproject-gear-menu}
Menu bánh răng có các tùy chọn nâng cao sau:

##### Độ mờ → Mặt nạ {#vertex-opacity-to-mask}
Biến độ mờ của nguồn thành mặt nạ trên đối tượng đang chọn.

##### Các lần lặp lại {#vertex-iterations}
Số lần áp dụng thao tác làm giãn trong khi chiếu lại. Chỉ dùng khi `Điểm đỉnh` đang bật.

##### Thư giãn {#vertex-relax}
Bố cục của lưới đang chọn có thể được làm mịn hoặc làm giãn ở một mức độ nhất định để khớp hơn với các đối tượng nguồn. `Làm mịn` phù hợp hơn với lưới nhiều đa giác, `Thư giãn` phù hợp hơn với lưới ít đa giác. `Tự động` để Nomad tự chọn cách tốt nhất.

##### Khoảng cách tìm kiếm {#vertex-cage-radius}
Khoảng cách tối đa dùng để tìm bề mặt nguồn. Mặc định khoảng cách này được giữ thấp để tránh lỗi, nhưng có thể tăng lên nếu các đối tượng nguồn ở xa đối tượng đang chọn.

##### Phép chiếu {#vertex-projection}
Cách tìm bề mặt nguồn:

* `Tia` - Chiếu dọc theo pháp tuyến bề mặt.
* `Hỗn hợp thích ứng` - Pha trộn tia theo pháp tuyến và bề mặt gần nhất dựa trên khoảng cách và `Ưu tiên tia`. Nếu một cách không trúng, dùng cách còn lại.
* `Gần nhất` - Chiếu tới điểm gần nhất trên bề mặt nguồn.

##### Ưu tiên tia {#vertex-ray-bias}
Chỉ dành cho `Hỗn hợp thích ứng`. Giá trị cao nghiêng kết quả pha trộn về phía tia theo pháp tuyến, giá trị thấp nghiêng về điểm gần nhất.

##### Dịch chuyển tia {#ray-vertex-offset}
Điều chỉnh điểm bắt đầu phép tính trên đối tượng đang chọn. Một khoảng lệch nhỏ khỏi bề mặt giúp tránh một số lỗi. Nếu các đối tượng nguồn ở rất xa đối tượng được bake, có thể cần tăng khoảng lệch này. `Gần nhất` không dùng đến nó.

### ![](/icons/bake.webp) Bake → VDM {#bake-vdm}
Tạo một dấu VDM (vector displacement) từ đối tượng đang chọn và thêm nó vào thư viện VDM. Bạn sẽ được hỏi đặt tên.

Đây là quy trình điển hình:
- Thêm một mặt phẳng, hoặc chọn `VDM mới` trong bộ chọn VDM để thêm một mặt phẳng đã được thiết lập sẵn (hình cơ bản [VDM](scene.md#add-menu))
- Điêu khắc hình dạng lên đó, giữ phần viền phẳng
- Bake thôi!

UV của mặt phẳng xác định vùng hình vuông được bake, nên đối tượng cần có UV. Chọn kích thước dấu bằng `Độ phân giải`, và chọn bằng `Màu sắc`, `Độ nhám`, `Độ kim loại` và `Độ mờ` những gì dấu mang theo ngoài độ dịch chuyển.

::: tip
Tránh dùng DynTopo trên mặt phẳng, nó làm hỏng UV và dấu sẽ bị méo. Điêu khắc trên một lớp cho kết quả chính xác nhất, vì mặt phẳng phẳng vẫn còn nguyên bên dưới. Vẽ màu cũng cần một lớp, nếu không vật liệu sẽ được đóng dấu lên toàn bộ hình vuông thay vì chỉ ở chỗ bạn đã vẽ.
:::

## ![](/icons/dot.webp) Hình cơ bản {#primitive}
Thông số của hình cơ bản đang chọn. Phần lớn chúng cũng có trong nút `…` trên thanh công cụ của hình cơ bản trong khung nhìn.

![](/images/topology_primitive_screenshot.webp)
