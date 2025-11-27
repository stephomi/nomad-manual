# ![](/icons/open.webp) Tệp

Menu Tệp cho phép bạn lưu và tải dự án Nomad, nhập và xuất mô hình 3D, và xuất ảnh render.

![](/images/file_menu.webp)

## Dự án
![](/images/file_project.webp)

Một hình thu nhỏ của lần lưu gần nhất được hiển thị ở đầu menu này. Nhấn vào hình thu nhỏ này sẽ mở một trình duyệt mini, chạm hai lần vào một dự án khác để mở menu mini cho phép Mở, Thêm, Lưu, Nhân bản, Đổi tên, Xóa dự án đó.

### ![](/icons/nomad.webp) Preset 
Truy cập bộ sưu tập bản demo và các thành phần nhân vật. Chọn một mục, sau đó chọn lại để chọn Mở, Thêm vào Cảnh hoặc Nhân bản mục đó vào thư mục dự án của bạn.

![](/images/file_preset_preview.webp)

### ![](/icons/save.webp) Save
Lưu dự án Nomad.

### ![](/icons/save_as.webp) Save As...
Hiển thị trình duyệt dự án để cho phép bạn lưu dự án Nomad với tên mới.

### ![](/icons/pencil.webp) Rename
Hiển thị hộp văn bản để đổi tên dự án hiện tại.

### ![](/icons/open.webp) Open...
Hiển thị trình duyệt dự án để mở một dự án.

### ![](/icons/add_file.webp) Add to scene...
Hiển thị trình duyệt dự án, khi một dự án được chọn, nội dung của nó sẽ được trộn vào cảnh hiện tại.

### ![](/icons/trash.webp) Delete...
Hiển thị trình duyệt dự án, mọi dự án được chọn sẽ bị xóa khỏi hệ thống tệp.

### ![](/icons/new_file.webp) New
Bắt đầu một dự án mới, nếu có thay đổi chưa lưu bạn sẽ được hỏi có muốn lưu hay không.

### ![](/icons/autosave.webp) Auto Save...
Menu điều khiển các tùy chọn tự động lưu.

Nếu bạn bật tự động lưu, bạn có thể thiết lập bộ hẹn giờ để một cửa sổ bật lên xuất hiện theo chu kỳ.
Lý do Nomad không lưu nền là vì tệp 3D có thể khá lớn nên có thể gây giật đáng kể trong khi bạn đang điêu khắc.

Ngoài ra, để tránh lỗi tràn bộ nhớ, cảnh thường được nén trước khi thực hiện thao tác lưu.
Việc nén/giải nén này cũng sẽ làm chậm thao tác lưu.

### Timer pop up
Tần suất cửa sổ hẹn giờ bật lên sẽ xuất hiện.

### Popup timeout
Bật thời gian chờ cho cửa sổ bật lên.

### Discard autosave
Nếu tồn tại tệp tự động lưu cho một dự án, nó sẽ tự động được tải thay cho dự án gốc. Nếu không cần điều này, nút này sẽ xóa tệp tự động lưu. Việc tải tệp sau đó sẽ tải lần lưu thủ công gần nhất của dự án.


## Import

### ![](/icons/add_file.webp) Import
Dùng để nhập các tệp 3D không phải là dự án Nomad.

Khi bạn nhập một tệp cảnh bên ngoài vào Nomad, bạn có thể *import* (nhập) hoặc *add* (thêm) nó.

Thêm một tệp sẽ chỉ thêm các đối tượng vào cảnh hiện tại.
Nhập một tệp sẽ tạo một dự án Nomad mới với các đối tượng mới trong đó.

Nomad có thể nhập các định dạng sau:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx, experimental)

### ![](/icons/cog.webp) Advanced
Hiển thị các tùy chọn nhập nâng cao:

### Project/ glTF / OBJ / STL / FBX
#### Keep topology
Mặc định Nomad sẽ cố gắng sửa hình học lỗi khi tải. Bật tùy chọn này sẽ ngăn Nomad sắp xếp lại đỉnh/mặt, xóa các đỉnh/mặt trùng lặp, xóa các đỉnh không dùng.

#### Skip textures
Bỏ qua việc tải texture cho các định dạng hỗ trợ như glTF.

### Project / glTF
#### Keep gui settings
Bật lưu cài đặt giao diện và cài đặt dự án trong tệp Nomad .nom hoặc glTF.

### OBJ
#### Split OBJ by groups
Bật tách các nhóm OBJ thành các đối tượng riêng biệt.

#### Color Space
Đặt chế độ màu được diễn giải từ obj là Linear, sRGB, hoặc Auto.

### PLY
#### Color Space
Đặt chế độ màu được diễn giải từ ply là Linear, sRGB, hoặc Auto.


### FBX
#### Color Space
Đặt chế độ màu được diễn giải từ obj là Linear, sRGB, hoặc Auto.



## Export
Lưu sang định dạng hình học 3D có thể dùng trong phần mềm khác. 

![](/images/file_export.webp)

Các định dạng tệp khác nhau hỗ trợ các tính năng khác nhau, các tùy chọn khả dụng sẽ thay đổi dựa trên loại tệp được chọn.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Vertex Colors](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [Vertex PBR](#vertex-pbr)       | ✅     | Nomad ✅<br>Other ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Other ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Layers](#layers)               | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objects                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Face Group                      | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarchy                       | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lights                          | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Textures                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | Import ✅<br>Export ❌ |
| Primitives, Postprocess, etc    | ✅     | Nomad ✅<br>Other ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### All/Visible/Selected
Trạng thái nút đang kích hoạt sẽ quyết định đối tượng nào được xuất. Con số bên cạnh các biểu tượng cho biết có bao nhiêu đối tượng sẽ được xuất cho tùy chọn đó.

### Vertex colors
Xuất màu đỉnh nếu được định dạng tệp hỗ trợ.

### PBR Paint
Màu đỉnh PBR được xuất như các thuộc tính màu đỉnh thứ cấp.
Các kênh được đóng gói theo cách sau:

|           | Channel  |
| :-------: | :------: |
| Roughness | R        |
| Metalness | G        |
| Masking   | B        |


### Layers
Layer được hỗ trợ thông qua glTF morph targets.
Nomad cũng xuất màu, độ nhám (roughness) và độ kim loại (metalness) theo từng layer nhưng sẽ bị phần mềm khác bỏ qua.

### Layer painting
Xuất tô màu layer, thường bị phần mềm khác bỏ qua.

### Face Group
Xuất facegroup, việc xuất đôi khi có thể gây xung đột với phần mềm khác.

### Normals
Xuất thông tin pháp tuyến. Lưu ý Nomad sẽ luôn tự tính lại pháp tuyến khi nhập các định dạng tệp khác.

### Tangents
Xuất thông tin tiếp tuyến, dùng nếu mô hình có normal map. 

### Textures
Nếu texture đã được thêm vào vật liệu, chúng sẽ được xuất. Lưu ý điều này không bake texture, việc đó được thực hiện qua các tùy chọn bake trong topology.

### Export button
Nhấn nút này để xuất hình học với bộ cài đặt đã chọn.

::: tip Tip: Import roughness and metalness to Blender

Blender có thể nhập glTF/glb, nhưng không tự động hiểu thuộc tính đỉnh cho metalness và roughness. Để sử dụng chúng, trong trình chỉnh sửa vật liệu hãy tạo một nút Vertex Color, đặt thuộc tính của nó thành thuộc tính màu tiếp theo (thường là Col.001). Kết nối một nút 'Separate XYZ', gửi X tới Roughness, và Y tới Metallic.

Video này minh họa quy trình:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tip: USD feature support

USD là một định dạng phức tạp, đặc tả của nó hỗ trợ nhiều tính năng, nhưng không phải phần mềm 3D nào cũng hỗ trợ chúng. Ví dụ OSX/iOS không hỗ trợ màu đỉnh. Các chế độ preset trong bộ xuất USD cố gắng đoán tốt nhất về khả năng tương thích với OpenUSD, Apple, Procreate, Zbrush.

::: 

## Render

Xuất một hình ảnh là sự kết hợp của tất cả cài đặt trong dự án (đèn, vật liệu, hậu kỳ, v.v.). 

![](/images/file_render.webp)
### Preview

Nút xem trước nhỏ cạnh tiêu đề menu sẽ làm mờ thanh công cụ để giúp xem trước kết quả cuối cùng.

### Transparent background
Bật kênh alpha cho ảnh render, hữu ích để kết hợp render với ảnh khác trong các chương trình 2D. Lưu ý không hỗ trợ độ trong suốt một phần.

### Show interface
Bật bao gồm giao diện Nomad trong ảnh render.

### Render ratio
Hệ số nhân cho độ phân giải hình ảnh.

### Final size
Độ phân giải dùng cho ảnh render. Khi chọn `Custom`, các thanh trượt chiều rộng và chiều cao sẽ được bật. 

Khi menu File đang hoạt động, một khung gạch đứt sẽ được vẽ trong vùng nhìn để chỉ vùng render nếu nó không khớp với độ phân giải màn hình (lưu ý bạn phải ở chế độ ngang để điều này chính xác).

### Export png
Nhấn nút này để bắt đầu quá trình render. Khi hoàn tất, bạn có thể chọn cách lưu hoặc chia sẻ hình ảnh.
