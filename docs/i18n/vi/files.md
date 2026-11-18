# ![](/icons/open.webp) Tệp tin {#files}

Menu tệp tin cho phép bạn lưu và mở các dự án Nomad, nhập và xuất mô hình 3d, xuất ảnh kết xuất, và liên kết Nomad với các ứng dụng khác. Menu có ba tab: `Tệp tin`, `Kết xuất` và `Liên kết`.

![](/images/file_menu.webp)

## Dự án {#project}
![](/images/file_project.webp)

Ảnh thu nhỏ ở trên cùng hiển thị dự án hiện tại, kèm theo dung lượng tệp, bản tự động lưu và lịch sử đã lưu bên cạnh. Chạm vào ảnh thu nhỏ để mở một trình duyệt nhỏ chứa các dự án của bạn, rồi chạm vào một dự án để mở menu cho phép mở, thêm, ghi đè, nhân bản, đổi tên hoặc xóa nó.

Khi dự án có thay đổi chưa được lưu, dòng `Thay đổi chưa lưu!` sẽ hiện dưới ảnh thu nhỏ.

### Phạm vi {#scope}
Trên máy tính, chọn nơi lưu các dự án của bạn:
* `Nội bộ` - Mặc định, giống như trên thiết bị di động. Dự án chỉ được lưu bên trong thư mục chính của Nomad.
* `Tại chỗ` - Khi bạn mở một dự án nằm ngoài thư mục Nomad, thao tác lưu sẽ ghi đè lên tệp gốc. Tự động lưu không hoạt động với những dự án bên ngoài này.

### ![](/icons/nomad.webp) Thiết lập sẵn {#preset}
Truy cập một bộ sưu tập các bản demo và bộ phận nhân vật. Chọn một mục, rồi chọn lại lần nữa để `Mở` nó hoặc `Thêm vào cảnh`. Bạn cũng có thể tải các mô hình miễn phí từ Poly Haven ngay trong trình duyệt này.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) Lịch sử... {#history}
Truy cập nhanh các tùy chọn lịch sử của dự án, chẳng hạn `Lưu lịch sử`, giúp giữ lại lịch sử hoàn tác khi dự án được lưu. Một huy hiệu màu xanh lá trên nút cho biết lịch sử đang được lưu cùng dự án. Xem [Lịch sử](history.md#save-history) để biết thêm chi tiết.

### ![](/icons/save.webp) Lưu {#save}
Lưu dự án Nomad. Nếu dự án chưa từng được lưu, bạn sẽ được hỏi tên.

### ![](/icons/save_as.webp) Lưu dưới dạng... {#save-as}
Lưu dự án dưới một tên mới, thành một dự án mới.

### ![](/icons/save_as.webp) Ghi đè... {#overwrite}
Mở trình duyệt dự án để lưu cảnh hiện tại đè lên một dự án khác. Bật `Chỉ bao gồm các đối tượng đã chọn` để chỉ lưu những đối tượng đã chọn thay vì toàn bộ cảnh. Trình duyệt cũng có nút `Lưu dưới dạng...` để lưu thành một dự án mới.

### ![](/icons/pencil.webp) Đổi tên {#rename}
Hiện một ô nhập văn bản để đổi tên dự án hiện tại.

### ![](/icons/open.webp) Mở... {#open}
Mở trình duyệt dự án để mở một dự án.

### ![](/icons/add_file.webp) Thêm vào cảnh... {#add}
Mở trình duyệt dự án; khi bạn chọn một dự án, nội dung của nó sẽ được gộp vào cảnh hiện tại.

### ![](/icons/trash.webp) Xóa... {#delete}
Mở trình duyệt dự án; mọi dự án bạn chọn sẽ bị xóa khỏi hệ thống tệp.

### ![](/icons/new_file.webp) Mới {#new}
Bắt đầu một dự án mới; nếu có thay đổi chưa lưu, bạn sẽ được yêu cầu xác nhận. Hộp xác nhận cho phép bạn `Giữ nguyên` hoặc `Đặt lại` các thiết lập `Nền`, `Môi trường`, `MatCap` và `X-quang`, đồng thời chọn xem dự án mới có dùng `Lưu lịch sử` hay không.

### ![](/icons/autosave.webp) Tự động lưu... {#auto-save}
Menu điều khiển các tùy chọn tự động lưu. Bật `Tự động lưu` để lưu dự án của bạn vào một tệp riêng theo khoảng thời gian đều đặn. Huy hiệu trên nút cho biết tính năng này đang bật hay tắt.

Lý do Nomad không lưu ngầm trong nền là vì tệp 3d có thể khá lớn, nên việc lưu có thể gây giật lag đáng kể khi bạn đang điêu khắc.

Ngoài ra, để tránh lỗi hết bộ nhớ, cảnh thường được nén trước khi lưu.
Việc nén/giải nén này cũng làm thao tác lưu chậm hơn.

### Khoảng thời gian lưu {#timer-pop-up}
Số phút Nomad chờ giữa các lần tự động lưu.

### Hiện đếm ngược {#popup-timeout}
Hiện đồng hồ đếm ngược trước mỗi lần tự động lưu, để bạn có thể hủy nếu đang làm dở việc gì đó. Khi tắt, Nomad sẽ lưu ngay khi bạn ngừng điêu khắc.

### ![](/icons/trash.webp) Bỏ qua tự động lưu {#discard-autosave}
Nếu một dự án có tệp tự động lưu, tệp đó sẽ tự động được mở thay cho dự án gốc. Nếu bạn không cần điều này, nút này sẽ xóa bản tự động lưu. Khi đó, mở tệp sẽ mở lần lưu thủ công gần nhất của dự án.

### ![](/icons/open.webp) Mở bản lưu cũ {#open-outdated-save}
Khi một dự án có cả bản tự động lưu và bản lưu thủ công, nút này sẽ mở bản cũ hơn trong hai bản (`Mở lưu tự động cũ không còn sử dụng` hoặc `Mở lưu thủ công cũ không còn sử dụng`), kèm theo ngày lưu. Rất tiện nếu bản lưu mới nhất không phải là bản bạn muốn.

### ![](/icons/storage.webp) Đã xóa gần đây... {#recently-deleted}
Nomad giữ lại dữ liệu của những dự án đã rời khỏi thư mục dự án, cùng các tệp bị thay thế khi nhập, trong một số ngày trước khi xóa vĩnh viễn. Những tệp nhập thất bại sẽ được giữ cho đến khi bạn xóa chúng. Danh sách này hiển thị chúng kèm dung lượng và ngày, để bạn có thể xóa từng tệp một hoặc xóa hết bằng `Xóa tất cả`.

## Nhập {#import}

### ![](/icons/add_file.webp) Nhập {#import-button}
Dùng để nhập các tệp 3d không phải là dự án Nomad.

Khi nhập một tệp cảnh bên ngoài vào Nomad, bạn có thể *thêm* nó vào, hoặc bắt đầu một dự án *mới* với nó.

Thêm một tệp sẽ đơn giản là thêm các đối tượng vào cảnh hiện tại.
Chọn `Mới` sẽ tạo một dự án Nomad mới chứa các đối tượng đó.

Cửa sổ nhập liệt kê mọi tệp bạn đã chọn, mỗi tệp có các tùy chọn nhập riêng. Ảnh cũng có thể được nhập theo cách này: với mỗi ảnh, chọn xem nó sẽ trở thành `HDRI`, `MatCap`, `Hình ảnh tham khảo`, `Alpha`, `Kết cấu` hay `VDM`.

Nomad có thể nhập các định dạng sau:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), trên những nền tảng có hỗ trợ

### ![](/icons/cog.webp) Cài đặt {#advanced}
Nút `Cài đặt...` bên cạnh ảnh thu nhỏ của dự án hiển thị các tùy chọn nhập chính. Các thiết lập này không được lưu lại, và cửa sổ nhập sẽ hiển thị những tùy chọn áp dụng cho các tệp bạn đang nhập.

### Mọi định dạng {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Giữ topologi {#keep-topology}
Mặc định, Nomad sẽ cố gắng sửa những hình học có vấn đề khi mở tệp. Bật tùy chọn này sẽ ngăn Nomad sắp xếp lại đỉnh/mặt, gộp các phần trùng lặp và xóa các đỉnh không dùng đến.

::: warning
Với `Giữ topologi`, các thao tác như Boolean, Join, Decimate hoặc Manifold có thể sẽ không gộp các đỉnh trùng lặp.
:::

#### ![](/icons/image.webp) Bỏ qua kết cấu {#skip-textures}
Không tải các kết cấu được nhúng trong tệp, với những định dạng hỗ trợ điều đó như glTF.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) Tải cài đặt UI {#keep-gui-settings}
Khi mở hoặc nhập một tệp dự án, tải tất cả các thiết lập giao diện đã được lưu trong đó.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) Tách OBJ theo nhóm {#split-obj-by-groups}
Tách các nhóm OBJ thành những đối tượng riêng biệt.

#### ![](/icons/vertex.webp) Hợp nhất các vị trí trùng lặp {#merge-duplicate-positions}
Gộp các đỉnh có cùng vị trí.

#### ![](/icons/uv.webp) Hợp nhất các UV trùng lặp {#merge-duplicate-uvs}
Gộp các tọa độ kết cấu có cùng UV.

#### ![](/icons/paint.webp) Không gian màu {#color-space}
Đặt chế độ màu dùng để đọc tệp là `Tự động`, `Tuyến tính` hoặc `sRGB`. Hãy thử chuyển đổi tùy chọn này nếu màu sắc trông không đúng.

#### ![](/icons/image.webp) Định dạng {#normal-format}
Định dạng normal map của các kết cấu: `Tự động`, `OpenGL (+Y)` hoặc `DirectX (-Y)`. Hãy thử định dạng còn lại nếu các chi tiết của normal map trông bị đảo ngược.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Không gian màu {#color-space-ply}
Đặt chế độ màu dùng để đọc tệp là `Tự động`, `Tuyến tính` hoặc `sRGB`.


### FBX {#fbx}
#### ![](/icons/uv.webp) Hợp nhất các UV trùng lặp {#merge-duplicate-uvs-fbx}
Gộp các tọa độ kết cấu có cùng UV.

#### ![](/icons/paint.webp) Không gian màu {#color-space-fbx}
Đặt chế độ màu dùng để đọc tệp là `Tự động`, `Tuyến tính` hoặc `sRGB`.

#### ![](/icons/image.webp) Định dạng {#normal-format-fbx}
Định dạng normal map của các kết cấu: `Tự động`, `OpenGL (+Y)` hoặc `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Không gian màu {#color-space-usd}
Đặt chế độ màu dùng để đọc tệp là `Tự động`, `Tuyến tính` hoặc `sRGB`.

#### ![](/icons/image.webp) Định dạng {#normal-format-usd}
Định dạng normal map của các kết cấu: `Tự động`, `OpenGL (+Y)` hoặc `DirectX (-Y)`.



## Xuất {#export}
Lưu sang một định dạng hình học 3d có thể dùng trong các phần mềm khác. 

![](/images/file_export.webp)

Mỗi định dạng tệp hỗ trợ những tính năng khác nhau, nên các tùy chọn có sẵn sẽ thay đổi theo loại tệp bạn chọn.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Màu đỉnh](#vertex-colors)      | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [PBR đỉnh](#pbr-paint)          | ✅     | Nomad ✅<br>Khác ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Tứ giác                         | ✅     | Nomad ✅<br>Khác ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Lớp](#layers)                  | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Đối tượng                       | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Nhóm mặt                        | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Phân cấp                        | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Đèn                             | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Kết cấu                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Khối cơ bản, Hậu kỳ, v.v.       | ✅     | Nomad ✅<br>Khác ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Nút xuất {#export-button}
Nhấn vào đây để xuất hình học với các thiết lập đã chọn. Nút này hiển thị định dạng đã chọn và dung lượng tệp ước tính. Trên Android, nút `Chia sẻ` bên cạnh sẽ gửi tệp thẳng sang một ứng dụng khác.

### Định dạng tệp {#file-format}
Chọn định dạng để xuất: `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` hoặc `USD`. NOMAD là định dạng riêng của Nomad, nó không mở được trong phần mềm khác, nên chủ yếu dùng để nhập lại vào Nomad.

### Bao gồm {#allvisibleselected}
Chọn những đối tượng sẽ được xuất: `Tất cả`, `Có thể nhìn thấy` hoặc `Đã chọn`. Con số bên cạnh mỗi tùy chọn cho biết có bao nhiêu đối tượng sẽ được xuất.

### Một tệp cho mỗi đối tượng {#one-file-per-object}
Xuất mỗi đối tượng thành một tệp riêng. Con số cho biết có bao nhiêu tệp sẽ được ghi ra.

### Loại {#type}
Khi việc xuất tạo ra nhiều tệp (một tệp cho mỗi đối tượng, hoặc OBJ kèm kết cấu), lưu chúng vào một `Thư mục` hoặc một tệp `Zip`. Một số ứng dụng (Google Drive, One Drive, v.v.) không hỗ trợ nhập thư mục, khi đó bạn có thể dùng Zip.

### Nhúng lịch sử {#embed-history}
Chỉ dành cho NOMAD. Đưa lịch sử hoàn tác vào trong tệp, lịch sử sẽ được khôi phục khi mở tệp trong Nomad. Tùy chọn này làm tăng dung lượng tệp, và yêu cầu toàn bộ cảnh được xuất thành một tệp duy nhất.

### Nhúng tài nguyên {#embed-assets}
Chỉ dành cho NOMAD. Đưa các matcap, môi trường và phông chữ tùy chỉnh của bạn vào tệp. Các tài nguyên có sẵn sẽ không được nhúng.

### Màu đỉnh {#vertex-colors}
Xuất màu đỉnh nếu định dạng tệp hỗ trợ. Một số phần mềm 3d đọc được chúng, nhưng không phải tất cả.

Với OBJ, bạn có thể chọn:
* `Không có` - Không có màu.
* `RGB` - Màu được ghi nối sau các đỉnh.
* `MRGB (ZBrush)` - Một cách khác để mã hóa màu, hỗ trợ cả dữ liệu mặt nạ.

### Không gian màu {#color-space-export}
Chỉ dành cho OBJ, với màu đỉnh `RGB`. Ghi màu theo dạng `Tuyến tính` hoặc `sRGB`.

### Sơn PBR {#pbr-paint}
Xuất độ nhám, độ kim loại và lớp sơn mặt nạ. Các phần mềm khác có thể bỏ qua dữ liệu này.
Màu đỉnh PBR được xuất dưới dạng các thuộc tính màu đỉnh phụ.
Các kênh được đóng gói như sau:

|             | Kênh     |
| :---------: | :------: |
| Độ nhám     | R        |
| Độ kim loại | G        |
| Mặt nạ      | B        |


### Các lớp {#layers}
Lớp được hỗ trợ thông qua morph target của glTF. Đây là tính năng được glTF hỗ trợ chính thức, nên nó cũng sẽ hoạt động trong các phần mềm khác.
Nomad cũng xuất màu, độ nhám và độ kim loại theo từng lớp, nhưng các phần mềm khác sẽ bỏ qua chúng.

### Vẽ lớp {#layer-painting}
Xuất phần sơn trên lớp, thường bị các phần mềm khác bỏ qua.

### Nhóm mặt {#face-group}
Xuất các nhóm mặt; đôi khi việc xuất này có thể gây trục trặc với phần mềm khác.

### Viết đối tượng {#write-objects}
Chỉ dành cho OBJ. Giữ các đối tượng tách riêng. Tắt nó để xuất mọi thứ thành một đối tượng duy nhất, ví dụ để dùng tính năng 'Mesh ID / Polygroup' của Substance Painter.

### Pháp tuyến {#normals}
Xuất thông tin pháp tuyến. Lưu ý rằng Nomad luôn tự tính pháp tuyến của riêng nó khi nhập các định dạng tệp khác.

### Tiếp tuyến {#tangents}
Xuất thông tin tiếp tuyến, được dùng nếu mô hình có normal map. 

### Kết cấu {#textures}
Nếu vật liệu có kết cấu, chúng sẽ được xuất. Lưu ý rằng việc này không bake kết cấu; bake được thực hiện qua các tùy chọn bake trong menu Tô pô.

### Định dạng {#fbx-format}
Chỉ dành cho FBX. `Nhị phân` nhỏ gọn hơn nhưng có thể không hoạt động trong mọi ứng dụng, còn `Ascii` là tệp văn bản.

### Nén {#compressed}
Chỉ dành cho FBX. Giảm dung lượng tệp, đổi lại việc xuất và nhập sẽ chậm hơn.

### Thiết lập sẵn {#usd-preset}
Chỉ dành cho USD. Chọn ứng dụng mà bạn xuất tệp để dùng: `OpenUSD`, `Apple`, `Procreate` hoặc `Zbrush`. Một số tùy chọn chỉ có sẵn với một số thiết lập sẵn.

### Thực thể {#instance}
Chỉ dành cho USD. Xuất các đối tượng thực thể (instance) dưới dạng thực thể, thay vì nhân bản hình học của chúng.

### Cho phép xiên {#allow-skew}
Chỉ dành cho USD. Cho phép độ xiên trong các ma trận biến đổi. Khi tắt, Nomad sẽ tách các phép biến đổi bị xiên thành các phép co giãn và xoay riêng biệt.

### Lặp lại {#repeater}
Chỉ dành cho USD. Xuất các bản sao do bộ lặp tạo ra dưới dạng thực thể.

### Gộp bản sao {#join-copies}
Mỗi đối tượng cùng các bản sao lặp lại của nó sẽ trở thành một đối tượng duy nhất.

::: tip Mẹo: Nhập độ nhám và độ kim loại vào Blender

Blender có thể nhập glTF/glb, nhưng không tự động hiểu các thuộc tính đỉnh dành cho độ kim loại và độ nhám. Để dùng chúng, trong trình chỉnh sửa vật liệu, hãy tạo một node Vertex Color, đặt thuộc tính của nó thành thuộc tính màu tiếp theo (thường là Col.001). Nối vào một node 'Separate XYZ', đưa X vào Roughness, và Y vào Metallic.

Video này minh họa quy trình:

![](/videos/blender_pbr.mp4)

::: 

::: tip Mẹo: Hỗ trợ tính năng USD

USD là một định dạng phức tạp, đặc tả của nó hỗ trợ rất nhiều tính năng, nhưng không phải phần mềm 3d nào cũng hỗ trợ hết. Ví dụ, OSX/iOS không hỗ trợ màu đỉnh.  Các chế độ thiết lập sẵn trong trình xuất USD cố gắng đoán mức tương thích tốt nhất với OpenUSD, Apple, Procreate, Zbrush.

::: 

## ![](/icons/screen.webp) Kết xuất {#render}

Xuất một ảnh là sự kết hợp của tất cả các thiết lập trong dự án (đèn, vật liệu, hậu kỳ, v.v.). 

![](/images/file_render.webp)
### ![](/icons/preview.webp) Xem trước {#preview}

Nút `Xem trước` bên cạnh tiêu đề menu làm giao diện trở nên trong suốt, giúp bạn xem trước bố cục khung hình của kết quả cuối cùng.

### ![](/icons/home.webp) Lấy nét {#focus}
Căn khung cảnh hoặc vùng chọn sao cho vừa với kích thước kết xuất. Chạm lần nữa để chuyển đổi giữa hai chế độ.

### ![](/icons/map.webp) Bản đồ chiều cao {#heightmap}
Kết xuất cảnh thành một bản đồ chiều cao thang xám nhìn từ camera, phần càng gần thì càng sáng. Bật tùy chọn này sẽ chuyển sang kích thước `Hình vuông` và căn khung vùng chọn. Một thanh nhỏ trong khung nhìn cho phép bạn chỉnh `Lấy nét` của dải chuyển màu.

Khi bật `Bản đồ chiều cao`, nút `Lưu dưới dạng alpha` sẽ xuất hiện bên cạnh nút xuất, để lưu ảnh kết xuất thành một alpha cọ mới thay vì xuất ra tệp.

### ![](/icons/opacity.webp) Nền trong suốt {#transparent-background}
Bật kênh alpha cho ảnh kết xuất, hữu ích khi muốn kết hợp ảnh kết xuất với các ảnh khác trong các chương trình 2d. Lưu ý rằng độ trong suốt một phần không được hỗ trợ.

### ![](/icons/sliders.webp) Hiển thị giao diện {#show-interface}
Đưa giao diện của Nomad vào ảnh kết xuất.

### Kích thước cuối cùng {#final-size}
Độ phân giải dùng cho ảnh kết xuất: `Màn hình`, `720`, `1080`, `4096`, `Hình vuông` hoặc `Tùy chỉnh`.

Khi menu Tệp tin đang mở, một khung viền nét đứt sẽ được vẽ trong khung nhìn để cho biết vùng kết xuất, nếu nó không khớp với độ phân giải màn hình.

### Chiều rộng / Chiều cao {#render-ratio}
Với `Tùy chỉnh`, đặt chiều rộng và chiều cao của ảnh. Nút liên kết giữa hai thanh trượt giữ nguyên tỷ lệ khi bạn thay đổi một trong hai. Với `Hình vuông`, chỉ có thể đặt chiều rộng.

### ![](/icons/export.webp) Xuất → PNG {#export-png}
Nhấn nút này để bắt đầu quá trình kết xuất. Khi hoàn tất, bạn có thể chọn cách lưu hoặc chia sẻ ảnh. Với kích thước rất lớn, Nomad sẽ yêu cầu xác nhận trước: hãy lưu dự án của bạn trước đó, phòng khi thiết bị hết bộ nhớ.

## ![](/icons/network.webp) Liên kết {#link}

Kết nối Nomad với một thiết bị hoặc ứng dụng khác, để gửi và nhận đối tượng, hoặc đồng bộ trực tiếp các chỉnh sửa của bạn. Một thiết bị làm máy chủ cho phiên làm việc, các thiết bị khác tham gia vào đó.

### Bật GoZ {#enable-goz}
Chỉ trên máy tính. Trao đổi lưới với ZBrush trên cùng máy tính này. `Gửi` nhập chúng vào ZBrush, `Nhận` nhập từ ZBrush đang chạy: `Lựa chọn` lấy subtool đang hoạt động, `Cảnh` lấy tất cả subtool. Bạn cũng có thể nhấn GoZ trong ZBrush bất cứ lúc nào.

### Chế độ {#link-mode}
* `Tắt` - Không liên kết.
* `Máy chủ` - Thiết bị này làm máy chủ cho phiên làm việc và chờ các thiết bị khác tham gia.
* `Tham gia` - Tìm các thiết bị ở gần, rồi chạm vào tên của máy chủ để tham gia.

Để liên kết hai Nomad, chọn `Máy chủ` trên một thiết bị và `Tham gia` trên các thiết bị còn lại. Để liên kết với Blender, Nomad nên là máy chủ: nút trợ giúp bên cạnh tiêu đề `Liên kết` sẽ hướng dẫn cách cài tiện ích Nomad Blender Link.

### ![](/icons/network.webp) Cổng mạng {#network-port}
Cổng mạng mà liên kết sử dụng. Chỉ thay đổi nó nếu một ứng dụng khác đã dùng cổng này.

### Gửi / Nhận {#send-get}
Khi đã kết nối, `Gửi` phần `Lựa chọn` của bạn hoặc toàn bộ `Cảnh` sang thiết bị kia, hoặc `Nhận` chúng từ thiết bị đó. `Thay thế` xóa cảnh hiện tại, rồi nhận cảnh của thiết bị kia.

### ![](/icons/link.webp) Đồng bộ trực tiếp {#live-sync}
Truyền các chỉnh sửa của bạn sang thiết bị kia ngay khi bạn làm việc. `Góc nhìn làm việc` cũng đồng bộ cả camera. `Chỉnh sửa cảnh` đặt thiết bị nào gửi các chỉnh sửa: `Tự động` trao quyền cho thiết bị có hoạt động gần nhất. Sau đó chọn những gì được đồng bộ: `Đối tượng và hình học`, `Vật liệu`, `Đèn`, `Camera`, và khi phía bên kia hỗ trợ, cả `Tô bóng` và `Hậu kỳ`.

::: tip
Các đối tượng có sẵn cần được `Gửi` hoặc `Nhận` một lần trước, để liên kết chúng trước khi đồng bộ trực tiếp có thể cập nhật chúng.
:::
