# ![](/icons/multires.webp) Tô-pô-lô-gy 

Menu này điều khiển tô-pô-lô-gy của các đối tượng trong Nomad, cũng như các công cụ để bake và chuyển chi tiết giữa các đối tượng, và giữa các texture.

![](/images/topology_overview.webp)

Nomad dựa trên polygon, nó dùng tam giác (triangles) và tứ giác (quads) để xử lý hình học.
Khi nói về tô-pô-lô-gy, ta nói đến cả số lượng mặt và cách các điểm (vertices) được nối với nhau.

Việc theo dõi tô-pô-lô-gy rất quan trọng, đặc biệt nếu bạn muốn điêu khắc hoặc tô vẽ các chi tiết nhỏ.

::: tip Làm sao để theo dõi tô-pô-lô-gy?
Bạn có thể hiển thị [Wireframe](settings.md#wireframe) hoặc đơn giản là tắt [Smooth Shading](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Menu topology của Nomad có vài phần:

| Method                                | Icon                         | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Chỉnh sửa nhiều mức độ chi tiết bằng cách subdivision           |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | Tính lại tô-pô-lô-gy mới với mật độ đồng đều                    |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | Thêm/Bớt mặt cục bộ theo thời gian thực khi điêu khắc hoặc tô   |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | Giảm đa giác, UV, baking, remeshing, reprojection               |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | Tùy chọn primitive                                               |


## Polygon stats

![](/images/topology_stats.webp)

Phần trên cùng của menu topology hiển thị thông tin polygon cho đối tượng được chọn và toàn bộ cảnh. Các con số cho biết tổng số vertices, tổng số tam giác và tổng số quads (polygon 4 cạnh).

Chạm vào phần này sẽ hiển thị danh sách thống kê polygon cho tất cả đối tượng polygon trong cảnh.

## ![](/icons/multires.webp) Multiresolution

![](/images/topology_multires_menu.webp)

### Multiresolution là gì?
Tính năng multiresolution hữu ích cho hai trường hợp chính:
- Thuật toán smooth subdivision để tăng số polygon của đối tượng
- Quản lý nhiều mức độ phân giải để bạn có thể luân phiên giữa chỉnh sửa lớn và nhỏ

![](/videos/multiresolution.mp4)

#### Quy trình Multiresolution
Một điểm quan trọng của multiresolution là bạn có thể quay lại mức phân giải thấp hơn, chỉnh sửa đối tượng rồi quay lại mức phân giải cao nhất mà không mất chi tiết độ phân giải cao. Tất cả chi tiết độ phân giải cao sẽ được project lại tự động.

::: warning
Nếu bạn dùng công cụ làm thay đổi tô-pô-lô-gy của đối tượng, bạn sẽ mất tất cả các mức phân giải khác của đối tượng!
Bạn sẽ luôn nhận được cảnh báo nếu điều này sắp xảy ra, ví dụ khi bạn dùng:
- [Voxel Remesher](#voxel-remesher)
- [Dynamic Topology](#dynamic-topology)
- [Trim tool](tools.md#trim)
- [Split tool](tools.md#split)
:::


### Thanh trượt Multiresolution
Thanh trượt này cho biết số mức subdivision trong đối tượng hiện tại. Nếu có 6 thanh dọc, nghĩa là có 6 mức subdivision. Vòng tròn cho biết mức subdivision đang được hiển thị. 

### Reverse
Khi đang ở mức subdivision thấp nhất, nút reverse sẽ cố gắng tạo thêm một mức bên dưới mức hiện tại. Lưu ý là điều này thường chỉ thực hiện được nếu đối tượng ban đầu được tạo bằng subdivision, ví dụ trong Nomad hoặc các phần mềm 3D khác có multiresolution subdivision surfaces.

### Subdivide
Nút *Subdivide* sẽ tăng số polygon lên gấp 4, vì vậy hãy chú ý polycount vì nó có thể tăng rất nhanh!
Một điểm quan trọng của *Subdivision Surface* là chúng sẽ hội tụ về một *Smooth Surface*.
Để hiểu cách hoạt động, bạn có thể thử nút *Subdivide* trên một đối tượng chỉ có vài polygon.

Bạn có thể tắt hành vi *Smooth* này bằng cách bật tùy chọn `Linear subdivision`.

### Delete lower
Nếu có các subdivision bên dưới mức đang hiển thị, xóa chúng. Nếu lỡ tay, bạn có thể tạo lại bằng nút Reverse.

### Delete higher
Nếu có các subdivision phía trên mức đang hiển thị, xóa chúng.

### Linear subdivision
Subdivide mesh mà không áp dụng smoothing.

### Sharp border
Nếu đối tượng có facegroup, bật tùy chọn này sẽ giữ biên facegroup sắc. Có thể đặt riêng cho từng mức subdivision (thanh trượt subdivision sẽ có một biểu tượng nhỏ phía trên mức đó để biểu thị).

### Keep triangles
Hầu hết hệ thống subdivision surface tiêu chuẩn sẽ cố gắng chuyển tất cả polygon thành quads trong quá trình subdivision. Tùy chọn này sẽ buộc subdivision dùng tam giác thay vì quads.

### Lock (LV0)

Ngăn mức subdivision thấp nhất bị chỉnh sửa. Điều này quan trọng nếu đối tượng được tạo từ ứng dụng khác và mesh gốc phải giữ nguyên. Khi tắt tùy chọn này, các thay đổi lớn ở mức subdivision cao hơn sẽ làm di chuyển level 0.

::: tip 

Subdivision sẽ làm mượt mọi cạnh sắc theo mặc định. Để giữ cạnh hơi sắc, hãy thử dùng linear subdivision hoặc Sharp border ở 2 mức subdivide đầu tiên, rồi tắt ở các mức cao hơn. Điều này sẽ tạo ra mesh subdivide nửa-sắc.

:::


## ![](/icons/voxel.webp) Voxel Remesher
![](/images/topology_voxel_menu.webp)
Khi dùng `Voxel Remesher`, toàn bộ mesh sẽ bị buộc có tô-pô-lô-gy với độ phân giải đồng đều, nghĩa là tất cả polygon có kích thước xấp xỉ nhau. Điều này rất hữu ích khi bạn không muốn nghĩ về tô-pô-lô-gy và chỉ muốn điêu khắc tự do.

Một quy trình điêu khắc điển hình có thể bắt đầu bằng việc dùng `Voxel Remesher` để block-out hình dạng thô với độ phân giải thấp.
Thỉnh thoảng chỉ cần nhấn nút *Remesh* khi bạn kéo giãn mesh quá nhiều để tránh biến dạng quá mức.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Như đã nói, Nomad là phần mềm polygonal, nhưng `Voxel Remesher` là ngoại lệ khi tạm thời dùng một cách tiếp cận khác để remesh.

Một khác biệt lớn là cách tiếp cận voxel không chấp nhận tự giao cắt, nên các vùng tự giao cắt sẽ được xử lý.
Ngoài ra nó không hỗ trợ mesh có lỗ.

Ở đây, lỗ không phải là `genus hole` (`lỗ` của bánh donut), mà là mesh không `watertight`/`closed`.
Thông thường, điều đó có nghĩa là trước khi remesh, mọi lỗ sẽ được lấp lại, tương tự [Trim tool](tools.md#trim) hoặc [tính năng Hole filling](scene.md#hole-filling).
:::

### Remesh
Thực hiện voxel remesh.

### Resolution
Kích thước voxel dùng trong quá trình tính toán. Khi thay đổi tham số này, một mẫu caro sẽ phủ lên mesh để xem trước kết quả.

### Build multiresolution
Tạo các mức multiresolution thấp hơn cho voxel remesh. Nếu bạn dùng mẫu caro để đặt độ phân giải, và đặt build multiresolution là 2, kết quả cuối sẽ có chi tiết khớp với thanh trượt resolution, và nếu bạn vào tab multires, nó sẽ ở level 2, nghĩa là bạn có các mesh multires độ phân giải thấp hơn ở level 1 và level 0. Đây là cách tốt để vừa tạo mesh sạch với polygon đều, vừa có mesh điều khiển độ phân giải thấp.

::: tip Tip: Build multiresolution và stable smoothing

Tùy chọn này đôi khi có thể tạo các 'vòng lặp' trong hình học khó làm mượt, gây ra các nốt nhỏ. Nếu gặp trường hợp này, hãy bật 'Stable smoothing' trong tùy chọn công cụ smooth. 

:::

### Keep sharp edges
Bật việc snap các điểm mới vào cạnh sắc trên mesh gốc. Có thể gây biến dạng.

## ![](/icons/dynamic.webp) Dynamic Topology

![](/images/topology_dyntopo_menu.webp)
Multiresolution và voxel remeshing là các phương pháp phổ biến trong ngành để kiểm soát tô-pô-lô-gy, nhưng cả hai đều yêu cầu bạn chú ý không kéo giãn polygon quá xa hoặc nén polygon quá chặt. 

Dynamic Topology là một phương pháp thay thế. Khi bạn điêu khắc, Nomad sẽ tự động thêm và bớt polygon trong lúc vẽ, nên khắc chi tiết nhỏ sẽ thêm nhiều polygon nhỏ ở nơi cần, và smooth ở chỗ khác sẽ bớt polygon.

Lưu ý dynamic topology sẽ dùng polygon tam giác thay vì quads. Điều này có thể trông hơi rối, nhưng tốt nhất là đừng nhìn wireframe, chỉ tập trung tạo sculpt đẹp mà không lo về tô-pô-lô-gy, rồi sau đó bạn có thể dùng một trong các công cụ remesh khác của Nomad để tạo quad mesh sạch.

Xem video bên dưới để thấy hoạt động.

![](/videos/dynamic.mp4)

### Enabled
Bật dynamic topology. Một biểu tượng DynTopo sẽ được đặt dưới thanh trượt bán kính và cường độ brush để cho phép bật/tắt Dyntopo theo từng công cụ.

### Detail
Điều khiển lượng chi tiết, hành vi thay đổi dựa trên lựa chọn 'Detail based on...', xem bên dưới.

### Detail based on...
| Method   | Description                                                     |
| :------: | :-------------------------------------------------------------: |
| Screen   | Mức chi tiết phụ thuộc vào kích thước đối tượng trên màn hình. Thanh trượt detail là 100% hoặc cao hơn cho chi tiết mịn (tam giác nhỏ), hoặc 1% cho chi tiết thấp (tam giác lớn).  |
| Radius   | Bán kính công cụ xác định lượng chi tiết. Bán kính nhỏ cho chi tiết mịn, bán kính lớn cho chi tiết thấp. Thanh trượt detail là hệ số nhân của tỉ lệ này.                     |
| Constant | Thanh trượt detail xác định lượng chi tiết, không bị ảnh hưởng bởi kích thước màn hình hay kích thước công cụ.             |

::: tip TIP: Chế độ Radius

Để hiểu rõ hơn cách chế độ radius hoạt động, hãy bắt đầu di chuyển thanh trượt detail bằng một ngón tay, đồng thời thay đổi bán kính công cụ bằng ngón khác. Bạn sẽ thấy chúng liên kết với nhau thế nào.

:::

### Prefer...
| Method  | Description       |
| :-----: | :---------------: |
| Speed   | Ưu tiên hiệu năng |
| Quality | Ưu tiên chất lượng     |

Khi ưu tiên `Quality`, có 2 khác biệt chính:
- refinement được áp dụng trước khi điêu khắc, nên bạn sẽ ít bị artefact nội suy khi tô hoặc điêu khắc chi tiết rất nhỏ
- refinement chạy cho đến khi hội tụ về mức chi tiết đúng, trái ngược với hành vi tăng dần.
 
Nhờ vậy, nếu bạn điêu khắc chi tiết rất nhỏ hoặc stroke nhanh, tô-pô-lô-gy luôn được refine như mong đợi


### Use pressure on radius
Chỉ liên quan nếu `Radius` được bật. Khi bật, mức chi tiết sẽ luôn phản ánh kích thước brush, ngay cả khi kích thước brush bị ảnh hưởng bởi lực bút.

### Use stroke falloff

Bao gồm cả đường cong falloff của brush và alpha vào tính toán dyntopo.

### Method
Dù bạn dùng `Dynamic Topology` trên [Brush](#brush) hay [Global](#global), bạn có thể chọn chế độ hoạt động:

| Method         | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | Có thể thêm và bớt mặt, đây là chế độ dùng trong video ở trên        |
| Subdivision    | Chỉ thêm mặt mới, không thể bớt mặt                                   |
| Decimation     | Chỉ bớt mặt, không thể thêm mặt                                       |

### Protect masked area
Bật bảo vệ vùng được mask khỏi việc thay đổi tô-pô-lô-gy.

### Vertex extrapolation


### Detail
Độ phân giải dùng cho thao tác remesh. Nếu Dyntopo ở chế độ 'Constant', nó sẽ là cùng giá trị với thanh trượt Detail ở đầu menu này.

### Remesh
Thực hiện remesh toàn cục bằng thuật toán dyntopo. Thông thường bạn nên dùng [Voxel Remesher](#voxel-remesher) cho remesh toàn phần.

Tuy nhiên một ưu điểm so với voxel là vùng được mask sẽ được bảo vệ, nên bạn có thể kiểm soát tốt hơn nơi cần nhiều hay ít mật độ.



## ![](/icons/topo_extra.webp) Misc

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) Gear menu
Nhiều công cụ trong menu này có tùy chọn nâng cao. Có thể truy cập qua biểu tượng bánh răng cạnh tiêu đề phần.

### Decimation

![](/images/topology_decimation.webp)

Giảm số polygon bằng cách cố giữ càng nhiều chi tiết càng tốt, sử dụng polygon tam giác.

Tính năng này hữu ích nếu bạn muốn xuất để in 3D.
Tuy nhiên bạn có lẽ không nên dùng nếu muốn tiếp tục điêu khắc, vì nó có thể tạo ra tam giác không đều.

Lưu ý vùng được mask sẽ không bị decimate.

![](/videos/decimate.mp4)

::: tip

Dùng [Quadremesh tool](tools.md#quad-remesher) trên đối tượng high poly có thể mất nhiều thời gian tính toán và cho kết quả khó kiểm soát. Tiền xử lý mesh bằng [facegroups](tools.md#facegroup-1) và decimate sẽ giúp Quadremesh chạy nhanh hơn nhiều và cho phép kiểm soát tô-pô-lô-gy tốt hơn.

* Tạo facegroup cho mesh để định nghĩa luồng quad lý tưởng.
* Facegroup relax để làm mượt biên facegroup.
* Decimate. Điều này đảm bảo không có mặt mỏng hoặc méo ở cạnh facegroup. Trong cài đặt decimate hãy đảm bảo bật facegroup. Điều này sẽ làm cạnh tam giác bám chính xác theo cạnh facegroup.
* Trong tùy chọn Quadremesh hãy đảm bảo tắt relax (vì bạn đã relax mesh rồi) và bạn sẽ có kết quả tốt.

:::

#### Decimate
Bắt đầu thao tác decimate.

Các biểu tượng cạnh nút decimate cho phép bật/tắt các tùy chọn ảnh hưởng đến decimation. Phần trăm cho biết độ mạnh của tùy chọn và có thể đặt trong menu bánh răng nâng cao.

* ![](/icons/palette.webp)  `Preserve Painting` - Đặt nhiều tam giác hơn ở nơi có chi tiết tô vẽ.
* ![](/icons/triforce.webp) `Uniform Faces` - Ưu tiên tạo tam giác kích thước đồng đều.
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - Decimate sẽ cố giữ biên gần hình học mở và lỗ không đổi.
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - Decimate sẽ cố giữ biên facegroup không đổi.
* ![](/icons/checkerboard.webp) `Preserve UV Borders` - Decimate sẽ cố giữ biên UV không đổi.

#### ![](/icons/cog.webp) Decimate gear menu
Menu bánh răng có các tùy chọn nâng cao sau:
##### Preserve painting
Checkbox bật/tắt chế độ này, giá trị xác định độ chính xác khi giữ chi tiết tô vẽ. Giá trị cao giữ painting nhiều hơn. Đặt 0 nếu bạn không quan tâm painting.


##### Uniform faces
Checkbox bật/tắt chế độ này. Giá trị cao sẽ tạo tam giác kích thước tương tự nhau.

##### Preserve borders
Bật để ngăn biên bị decimate. Có thể chọn trọng số biên cho biên `Geometry`, `Face Group` hoặc `UV`.

#### Target triangles
Đặt số tam giác mục tiêu. Giá trị mặc định là 50%, nút percent/target sẽ chuyển giữa phần trăm hoặc số poly mục tiêu chính xác.



### UV Unwrap - UVAtlas

![](/images/topology_uvatlas_menu.webp)
Tính toán tọa độ texture (UV) cho mesh hiện tại, thường ưu tiên tạo nhiều island với đường cắt để giảm méo.

Biểu tượng con mắt nhỏ giữa tiêu đề menu và menu bánh răng sẽ bật/tắt xem trước UV trên đối tượng.

![](/videos/unwrap.mp4)

#### Unwrap
Tính UV cho đối tượng được chọn, sẽ hiển thị ở nền.

#### Delete UVs
Xóa UV trên đối tượng.

#### ![](/icons/cog.webp) UVAtlas gear menu
Menu bánh răng có các tùy chọn nâng cao sau:

#### Face Group

Dùng facegroup để định nghĩa đường cắt cho UV.

##### Max Stretch
Giá trị thấp tạo ít méo và nhiều island, giá trị cao tạo nhiều méo và ít island. 

##### Island spacing
Lượng khoảng cách giữa các island. Giá trị thấp ít lãng phí không gian hơn nhưng dễ bị lem texture giữa các island. 

::: warning
Tính UV có thể mất thời gian, tốt nhất là mesh có ít hơn 100k vertices.
:::

::: tip UVs?
Một ví dụ thường dùng cho UV là gói quà; đâu là cách tốt nhất để cắt giấy gói để phủ kín một vật thể mà không bị chồng lấn? 

UV cũng tương tự, nhưng thay vì cắt giấy, bạn cắt chính đối tượng. Hãy tưởng tượng model của bạn làm bằng nhựa mỏng, bạn sẽ cắt nó ra sao để trải phẳng, tô vẽ trên trạng thái phẳng đó, rồi lắp lại?

Giờ hãy tưởng tượng bề mặt model làm bằng vải co giãn lycra. Bạn có thể kéo dãn model cho phẳng, hoặc cắt, hoặc kết hợp cả hai. Nhưng nếu bạn tô một họa tiết caro khi nó phẳng, họa tiết sẽ bị méo khi lắp lại. Cách nào tốt hơn, nhiều đường cắt ít méo, hay ít đường cắt nhiều méo?

UV là tập hướng dẫn cho phần mềm 3D biết cách 'cắt và kéo dãn' đối tượng khi áp dụng texture. Công cụ UV Atlas thường dùng cách 'nhiều cắt, ít méo'.


:::

::: tip UV và Nomad và các ứng dụng khác

Hầu hết model có texture bạn tìm trên mạng sẽ được tô bằng UV. Nomad có thể import và hiển thị qua bảng [material](material#textures).

Khi model được tạo trong Nomad, bạn có thể tô trực tiếp lên đối tượng mà không cần UV. Nếu cần xuất sang ứng dụng khác, ví dụ [Procreate](https://procreate.art/), bạn có thể 'bake' thông tin màu của Nomad vào texture thông qua UV. 

:::

### UV Unwrap - BFF
![](/images/topology_uvbff_menu.webp)

UV BFF ưu tiên cách tiếp cận 'ít cắt, nhiều méo'. 

#### ![](/icons/cog.webp) UV BFF gear menu

#### Face Group

Dùng facegroup để định nghĩa đường cắt cho UV.

##### Cone count
Xác định số lượng hướng chiếu chính được dùng. Giá trị thấp tạo ít island hơn nhưng nhiều méo hơn.

##### Seamless patches
Ảnh hưởng đến bố cục các mảng UV, hoạt động tốt nhất với facegroup được tạo cẩn thận.

### Bake -> texture 
![](/images/topology_bake_menu.webp)

Texture baking sẽ tạo texture bằng cách project các đối tượng khác đang hiển thị trong cảnh vào UV của đối tượng được chọn.

Quy trình điển hình cho baking:
- Bạn có một mesh với chi tiết mịn và painting
- Clone nó
- Decimate (đặt `Preserve painting` về 0)
- UV unwrap
- Bake!

Nomad mặc định sẽ tính đến mọi mesh hiển thị trong cảnh.
Bạn cũng có thể dùng chế độ Solo để nhanh chóng ẩn hầu hết mesh khác.
Nếu không có đối tượng nào khác hiển thị, nó sẽ tính toàn bộ cảnh.

Giờ bạn sẽ có một mesh độ phân giải thấp giữ lại hầu hết màu và chi tiết của đối tượng trước đó.

Sau thao tác, vertex color sẽ được chuyển sang một layer mới bị tắt, để không gây nhiễu với texture.

#### From itself
Bake mức multiresolution cao nhất xuống mức thấp nhất trên đối tượng hiện tại. Cách này dễ thiết lập, nhưng thường bạn sẽ cần nhiều kiểm soát hơn, khi đó tùy chọn tiếp theo hữu ích hơn.

#### From high-res ()
Bake từ các đối tượng khác đang hiển thị trong cảnh vào đối tượng được chọn. Con số trong ngoặc cho biết số đối tượng hiển thị khác sẽ được dùng làm mục tiêu high-res và được bake vào đối tượng low-res hiện tại có UV. Các đối tượng khác không cần giống về bố cục hay tô-pô-lô-gy với đối tượng được bake, cho phép quy trình bake linh hoạt.

#### Resolution
Độ phân giải của texture được bake. Texture bake luôn là hình vuông, nên 1024 sẽ tạo ảnh 1024x1024. 

Các nút bên dưới là phím tắt cho các độ phân giải thường dùng. Tham khảo: 512x512 tương đối nhỏ, dùng cho đồ họa web và hình học đơn giản. 4096x4096 (gọi tắt 4k) dùng cho render chất lượng cao.

#### ![](/icons/cog.webp) Bake gear menu
![](/images/topology_bake_gear_menu.webp)
Menu bánh răng có các tùy chọn nâng cao sau:

##### Normal, Roughness, Metalness, Color, Emissive, Opacity
Các checkbox này quyết định thuộc tính nào sẽ được bake, mỗi loại vào một map riêng. Sau khi bake xong, chúng sẽ được thêm làm texture vào material của đối tượng hiện tại.

##### Backup
Để xem trước texture đã bake, thông tin paint của đối tượng nên được tắt. Tùy chọn này sẽ chuyển mọi thông tin paint sang một layer mới làm bản sao lưu để có thể bật/tắt dễ dàng.

#### Cage radius
Điều chỉnh khoảng cách từ đối tượng bake mà các tia được bắn ra để tìm đối tượng mục tiêu. Mặc định khoảng cách này thấp để tránh artefact, nhưng có thể tăng nếu đối tượng mục tiêu ở xa đối tượng bake.

##### Ray offset
Điều chỉnh vị trí bắt đầu tính toán bake trên đối tượng bake. Mặc định bắt đầu từ vị trí cách bề mặt 5%, giúp tránh hầu hết artefact phổ biến. Nếu đối tượng mục tiêu rất xa đối tượng bake, offset này có thể cần tăng.


### Reproject to vertex

![](/images/topology_reproject_menu.webp)

Project chi tiết điêu khắc, painting, layer, texture vào giá trị vertex.

Có thể xem như ngược lại với baking; nếu baking chuyển thuộc tính vertex sang texture, thì reproject chuyển texture (và thuộc tính khác)
 ngược lại vào vertex.

::: tip
Khi dùng `Bake to texture` hoặc `Reproject to vertex`, cả vertex color và material texture đều được tính đến.
:::

#### From itself
Chuyển texture từ material thành giá trị vertex. Nút này chỉ hoạt động nếu đối tượng có UV và texture đang bật trong material.

::: tip TIP: Texture painting
Nomad không hỗ trợ trực tiếp việc tô và chỉnh sửa texture, nhưng có thể đạt kết quả tương tự bằng cách project texture -> vertex, tô trên vertex, rồi bake vertex -> texture:

1. Chuẩn bị một đối tượng low poly có UV
1. Nạp texture vào material của nó
1. Subdivide đủ để có mật độ vertex phù hợp để tô
1. `Reproject to vertex` ở chế độ `From itself`, giờ texture đã được chuyển thành giá trị vertex
1. Tô, smooth, smudge, stamp, chỉnh sửa tùy ý
1. `Bake to texture` ở chế độ `From itself`. Các chỉnh sửa đó được chuyển ngược lại thành texture.
:::

#### From high-res ()
Chuyển mọi đối tượng hiển thị thành giá trị vertex trên đối tượng được chọn. Con số trên nút này cho biết số đối tượng hiển thị.

::: tip
Reproject đối tượng khác không chỉ dùng để chuyển thông tin màu từ đối tượng khác, mà còn để project vertex lên đối tượng khác, ví dụ băng quấn có thể được project lên nhân vật.
:::

#### ![](/icons/cog.webp) Reproject gear menu
Menu bánh răng có các tùy chọn nâng cao sau:

#### Vertices, Roughness, Metalness, Color, Opacity, Opacity->Mask, Mask, Layers, Face Group
Các checkbox này quyết định thuộc tính nào sẽ được project lên đối tượng được chọn. 

#### Relax
Mesh được chọn có thể được làm mượt hoặc relax bố cục một mức nào đó để khớp tốt hơn với mục tiêu reprojection. Smooth phù hợp với mesh high poly. Relax phù hợp với mesh low poly. Auto sẽ để Nomad tự chọn phương pháp tốt nhất.

#### Iterations
Số lần thao tác relax được áp dụng trong quá trình reprojection.

#### Cage radius
Điều chỉnh khoảng cách từ đối tượng được chọn mà các tia được bắn ra để tìm đối tượng mục tiêu. Mặc định khoảng cách này thấp để tránh artefact, nhưng có thể tăng nếu đối tượng mục tiêu ở xa đối tượng bake.

#### Ray bias
Giá trị thấp ưu tiên project đến điểm gần nhất trên bề mặt mục tiêu. Giá trị cao ưu tiên điểm giao nhau theo pháp tuyến bề mặt. 

#### Ray offset
Điều chỉnh vị trí bắt đầu tính toán bake trên đối tượng được chọn. Mặc định bắt đầu từ vị trí cách bề mặt 5%, giúp tránh một số artefact. Nếu đối tượng mục tiêu rất xa, offset này có thể cần tăng.


### Quad Remesh - Instant
![](/images/topology_quadremesh_menu.webp)
Remesh bằng [thuật toán Instant Meshes của Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Nó sẽ phân tích flow của mesh và tạo tô-pô-lô-gy quad sạch.

::: tip
Trên iOS và desktop, công cụ [Quad remesher](tools#quad-remesher) cho kết quả tốt hơn và nhiều kiểm soát hơn.
:::

#### Remesh
Bắt đầu thao tác instant meshes.

#### Target quads
Số polygon quad mà quad remesh sẽ cố gắng tạo.

#### ![](/icons/cog.webp) Quad Remesh Instant gear menu
Menu bánh răng có các tùy chọn nâng cao sau:

##### Crease angle
Ngưỡng góc sắc sẽ cố gắng hỗ trợ dẫn hướng thao tác remesh.

#### Max fill hole
Thuật toán đôi khi có thể tạo lỗ không mong muốn. Nếu lỗ có ít vertex hơn giá trị này, nó sẽ được lấp.

### Holes
![](/images/topology_holes_menu.webp)
Hầu hết thời gian, đối tượng của bạn có lẽ sẽ watertight, nghĩa là mesh 'đóng kín'.

Nếu đối tượng có lỗ, bạn có thể lấp chúng. Lưu ý nó chỉ hoạt động với lỗ 'ngây thơ', do đó không thể 'weld' hai biên tách biệt.

![](/videos/hole_filling.mp4)

::: tip
Khi bạn chạy Voxel remesher, mọi lỗ sẽ tự động được lấp, dù bạn dùng trên 1 hay nhiều mesh.
:::

#### Close holes
Thực hiện thao tác lấp lỗ.

#### ![](/icons/cog.webp) Holes gear menu
Menu bánh răng có các tùy chọn nâng cao sau:

##### Detail
Mật độ polygon dùng để lấp lỗ. Khi kéo thanh trượt này, một mẫu caro sẽ hiển thị trên model, cho biết kích thước tam giác sẽ dùng. Checkbox sẽ tắt điều này và chỉ dùng các điểm hiện có, thường tạo tam giác dài mỏng trên lỗ, khó điêu khắc.

##### Fill non-manifold
Cố gắng lấp lỗ non-manifold.

##### Face Group

Khi lấp lỗ, mỗi lỗ nên có facegroup riêng (Auto), hay tất cả dùng chung một facegroup (Off), hay không tạo facegroup (On).

### Force Manifold
![](/images/topology_forcemanifold_menu.webp)
Cố gắng làm sạch các cạnh non-manifold. Hữu ích cho phần mềm ngoài không hỗ trợ cạnh có hơn 2 mặt chung.

#### Clean
Thực hiện thao tác clean.
#### ![](/icons/cog.webp) Force manifold gear menu
Menu bánh răng có các tùy chọn nâng cao sau:

#### Delete small faces
Ngưỡng dùng để xóa và nối các polygon nhỏ.


### Triplanar
![](/images/topology_triplanar_menu.webp)
Chuyển mesh thành primitive [triplanar](scene.md#triplanar).
Bạn có thể sẽ mất nhiều chi tiết trong quá trình này.

#### Force cubic
Buộc triplanar là hình lập phương. Nếu không, triplanar sẽ khớp với bounding box gần nhất bao quanh đối tượng.

#### Convert
Thực hiện thao tác triplanar.

#### Resolution
Kích thước voxel dùng trong thao tác triplanar.

## ![](/icons/dot.webp) Primitive
Tham số cho primitive được chọn. Chúng cũng có trong thanh công cụ primitive trong viewport.

![](/images/topology_primitive_screenshot.webp)
