# ![](/icons/sun.webp) Tô bóng {#shading}

Menu này điều khiển các chế độ tô bóng mà Nomad sử dụng, các thuộc tính chiếu sáng, môi trường và matcap, cùng sương mù.

![](/images/shading_overview.webp)



Bạn có thể chọn giữa nhiều chế độ hiển thị:

| Chế độ                      | Ý nghĩa                         | Mô tả                                                                 |
| :-------------------------: | :-----------------------------: | :-------------------------------------------------------------------: |
| [Chiếu sáng (PBR)](#pbr)    | Kết xuất dựa trên vật lý        | Đèn, bóng đổ, môi trường, cùng độ kim loại/độ nhám đã vẽ              |
| [MatCap](#matcap)           | Chụp vật liệu (Material Capture)| Chế độ nhanh để điêu khắc, tốn ít gpu/cpu hơn PBR                     |
| [Không sáng](#unlit)        | Màu bề mặt                      | Chỉ có màu bề mặt, không có tô bóng hay chiếu sáng                    |
| [ID vật thể](#object-id)    | ID vật thể                      | Mỗi vật thể một màu ngẫu nhiên, hữu ích cho các ứng dụng vẽ.          |
| [ID thực thể](#instance-id) | ID thực thể                     | Mỗi thực thể một màu ngẫu nhiên, hữu ích để nhận ra các lưới dùng chung |

Nếu bạn muốn tìm hiểu thêm về độ kim loại và độ nhám, hãy xem phần [Vẽ đỉnh](painting.md).

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) Nhóm mặt {#face-group}
Hiển thị màu của các nhóm mặt. Nhóm mặt là những vùng chọn đa giác được tô màu, có thể tạo bằng công cụ [Nhóm mặt](tools#facegroup), và được tạo tự động với hầu hết các khối cơ bản.

Một số công cụ sẽ tự động lọc theo nhóm mặt khi nhóm mặt đang hiển thị.

### ![](/icons/palette.webp) Hiển thị vẽ {#show-paint}
Nomad có thể lưu màu, độ nhám và độ kim loại trong các đỉnh của tác phẩm điêu khắc. Bạn có thể bật/tắt việc hiển thị các thuộc tính này cho toàn bộ cảnh bằng ô đánh dấu này.

Lưu ý rằng nếu bạn có cả thuộc tính đỉnh lẫn kết cấu, và cả hai đều được bật, các giá trị sẽ được nhân với nhau.

### ![](/icons/shield.webp) Hiển thị mặt nạ {#show-mask}
Bật/tắt lớp phủ mặt nạ thang xám của các [công cụ mặt nạ](tools#mask). Khi tắt, mặt nạ cũng bị vô hiệu hóa. Điều này hữu ích khi bạn muốn chỉnh nhanh mà không bị mặt nạ cản trở, sau đó bật lại mà không mất mặt nạ của mình.

### ![](/icons/tool_hide.webp) Sử dụng ẩn {#use-hide}

Bật/tắt các mặt bị ẩn. Lưu ý rằng tùy chọn này chỉ hoạt động khi bạn KHÔNG ở trong công cụ ẩn!

### ![](/icons/image.webp) Sử dụng các kết cấu {#use-textures}

Nomad cho phép gán kết cấu cho các đối tượng từ menu [vật liệu](material). Nếu có kết cấu được gán, bạn có thể bật/tắt chúng cho toàn bộ cảnh bằng ô đánh dấu này.

Bạn không thể tạo hay chỉnh sửa kết cấu trong Nomad, nhưng kết cấu từ các tệp đã nhập vẫn hoạt động. Kết cấu độ trong suốt hoạt động ở chế độ Chiếu sáng, MatCap và Không sáng; normal map ở Chiếu sáng và MatCap; màu ở Chiếu sáng và Không sáng; còn phát sáng, độ nhám và độ kim loại chỉ ở Chiếu sáng. Nút sẽ bị làm mờ khi cảnh không có kết cấu nào.

### Tổng quan về PBR và đèn {#pbr}
Hướng dẫn này sẽ không đi sâu vào chi tiết của kết xuất dựa trên vật lý (Physically Based Rendering).

Một điều quan trọng cần nhớ là chiếu sáng và vật liệu hoàn toàn tách biệt.
Điều đó có nghĩa là bạn có thể vẽ màu, độ nhám và độ kim loại cho đối tượng, trong khi chiếu sáng được xử lý độc lập.
Nhờ vậy bạn có thể vẽ đối tượng rồi chỉnh ánh sáng sau, mà không làm hỏng diện mạo tổng thể của mô hình.

Đèn, môi trường và sương mù chỉ có sẵn trong [chế độ PBR](#pbr).
Vì lý do hiệu năng, bạn bị giới hạn ở 4 đèn trên thiết bị di động và 6 đèn trên máy tính.

::: tip
Bạn có thể mở một tệp glTF có nhiều đèn hơn và Nomad sẽ giữ lại tất cả.
Tuy nhiên hiệu năng có thể sẽ không tốt.
:::

::: tip
Bạn có thể giả lập nhiều đèn bằng cách làm cho các đối tượng không sáng/phát sáng, rồi bật chiếu sáng toàn cầu trong menu [hậu kỳ](postprocess).
:::

### Tổng quan về các loại đèn {#light-types-overview}

Đây là các loại đèn hiện được hỗ trợ:

| Chế độ                      | Mô tả                                                        | Có thể đổ bóng   |
| :-------------------------: | :----------------------------------------------------------: | :--------------: |
| [Có hướng](#directional)    | Ánh sáng mặt trời ở xa vô tận                                | Có               |
| [Môi trường](#env-light)    | Một nguồn sáng ở xa, khớp với HDR của môi trường             | Có               |
| [Đèn rọi](#spot)            | Đèn có hình nón                                              | Có               |
| [Điểm](#point)              | Điểm sáng tỏa ra mọi hướng                                   | Có               |

#### ![](/icons/sun.webp) Có hướng {#directional}
Đèn này phát ra ánh sáng từ một nơi xa vô tận, với cường độ đồng đều.
Vị trí 3d của nó trong cảnh không quan trọng, chỉ hướng của nó là quan trọng.

Bạn có thể gắn đèn này vào camera, để ánh sáng luôn nhất quán.  
Ví dụ, bạn có thể dùng nó để tạo ánh sáng viền (rim light, một nguồn sáng mạnh chiếu từ phía sau mô hình, hướng về phía camera) luôn chiếu sáng phía sau mô hình của bạn.

#### ![](/icons/panorama.webp) Đèn môi trường {#env-light}
Dùng một [HDR môi trường](#environment) rất phù hợp cho ánh sáng tổng thể dịu nhẹ, nhưng nếu trong HDR có một nguồn sáng mạnh và gắt, bóng đổ do nó tạo ra sẽ rất mờ, thường còn không thấy được. Kết hợp một đèn có hướng với HDR môi trường có thể giúp ích, nhưng khá khó để căn chúng khớp với nhau.

Đèn này sẽ làm việc đó thay bạn. Đèn sẽ tự động được xoay để khớp với phần sáng nhất của HDR, sau đó bạn có thể điều chỉnh riêng cường độ và góc của nó (độ mềm của bóng). 

#### ![](/icons/spotlight.webp) Đèn rọi {#spot}
Đèn rọi phát ra ánh sáng theo một hướng duy nhất, giới hạn trong một hình nón.

#### ![](/icons/light.webp) Điểm {#point}
Đèn điểm phát ra ánh sáng theo mọi hướng, và nó cũng có thể đổ bóng.

#### Bóng đổ {#shadows}
Mỗi đèn đều có thể đổ bóng, và bạn có thể chọn cách tính bóng trong phần [cài đặt](#light-extra-controls) của nó. Nếu bạn thấy bóng bị lỗi hiển thị, các thanh trượt `Dung sai` ở đó có thể giúp ích.

Chất lượng bóng đổ phụ thuộc vào kích thước của các đối tượng so với toàn bộ cảnh.  
Nếu trong cảnh có một đối tượng lớn không cần đổ bóng (ví dụ một mặt phẳng lớn), hãy nhớ tắt đổ bóng trong [cài đặt vật liệu](material.md#casts-shadows) của nó.

## ![](/icons/sun.webp) Đèn {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Ô đánh dấu Đèn {#lights-checkbox}

Bật/tắt tất cả các đèn trực tiếp trong cảnh.



### Thêm đèn {#add-light}

Thêm một đèn vào cảnh, tối đa 4 đèn trên thiết bị di động và 6 đèn trên máy tính. Khi thêm đèn, danh sách đèn sẽ hiển thị cùng các nút, và một thanh công cụ đèn sẽ được thêm vào phía trên khung nhìn.

![](/images/shading_lights_icons.webp)

* Dòng chữ hiển thị tên và độ sáng của đèn. Chạm vào nó để chọn đèn.
* Biểu tượng con mắt bật/tắt hiển thị.
* Biểu tượng bút chì cho phép bạn đổi tên đèn.
* Biểu tượng thùng rác sẽ xóa đèn.
* Biểu tượng sao chép sẽ nhân bản đèn. 
* Biểu tượng 3 chấm sẽ mở trình chỉnh sửa đèn đầy đủ. Hầu hết các chức năng này cũng có trên thanh công cụ xuất hiện trong khung nhìn. 

Bạn cũng có thể kéo một đèn trong danh sách để sắp xếp lại thứ tự.

### ![](/icons/spotlight.webp)  Biểu tượng {#icons}

Bật/tắt hiển thị biểu tượng đèn trong khung nhìn

### Thanh công cụ đèn {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Thanh công cụ này sẽ xuất hiện ở phía trên khung nhìn khi một đèn được chọn.

* `Có thể thấy` sẽ bật/tắt hiển thị đèn.
* Có hướng/Môi trường/Đèn rọi/Điểm sẽ thay đổi loại đèn. Chạm để chuyển lần lượt, hoặc nhấn giữ để xem menu.
* Cường độ điều khiển độ mạnh của đèn; giá trị có thể vượt quá 1.0 cho những đèn rất mạnh, hữu ích khi dùng với Chiếu sáng toàn cầu trong Hậu kỳ
* Nhấn vào ô màu sẽ mở bộ chọn màu. Nomad cung cấp nhiều cách để chọn màu. Điều khiển Kelvin cho bạn một cách tự nhiên để chọn ánh sáng ấm/lạnh.
* Bóng sẽ bật/tắt bóng đổ.
* Góc (_có hướng và môi trường_) hoặc Kích thước (_đèn rọi và điểm_) đặt độ rộng của đèn. Đèn càng rộng sẽ đổ bóng càng mềm, ánh sáng càng dịu, và vùng phản chiếu sáng trên đối tượng càng mềm.
* Gắn kèm (_chỉ đèn có hướng_), Góc nón và Mềm mại (_chỉ đèn rọi_) được mô tả trong phần [trình chỉnh sửa đèn](#light-extra-controls) bên dưới.
* ... sẽ hiện ra `Nhân bản`, `Đặt lại vị trí` và `Xóa`, cùng với các thiết lập bóng đổ.

### Điều khiển bổ sung của đèn {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Biểu tượng 3 chấm của một đèn trong danh sách sẽ mở trình chỉnh sửa đầy đủ của nó. Lưu ý rằng một số tùy chọn chỉ dành cho một số loại đèn nhất định.

* `Có hướng/Môi trường/Đèn rọi/Điểm` cho phép bạn thay đổi loại đèn.
* Nhấn vào `ô màu` sẽ mở bộ chọn màu. 
* `Cường độ` điều khiển độ mạnh của đèn.
* `Gắn kèm` (_chỉ đèn có hướng_) đặt đèn làm con của thế giới (`Cố định`), hoặc làm con của camera (`Máy quay`). Ví dụ, nếu bạn dùng một đèn có hướng phía sau nhân vật làm ánh sáng viền, khi chọn gắn kèm vào camera, xoay camera thì đèn vẫn luôn ở phía sau nhân vật.
* `Mềm mại` (_chỉ đèn rọi_) điều khiển độ sắc nét của mép hình nón đèn rọi. 0 là mép rất sắc. 1 là rất mềm, với dải chuyển dần về tâm hình nón ánh sáng. Trong khung nhìn, bạn có thể dùng chấm nhỏ màu xanh dương trên hình nón đèn rọi để chỉnh độ mềm trực tiếp.
* `Góc nón` (_chỉ đèn rọi_) điều khiển góc mở của đèn rọi. Góc nhỏ là một chùm sáng rất mảnh, 170 là ánh sáng tỏa rất rộng. Trong khung nhìn, bạn có thể dùng chấm màu cam để chỉnh góc nón trực tiếp.
* `Góc` (_chỉ đèn có hướng và môi trường_) là kích thước biểu kiến của đèn, hãy hình dung nó như độ lớn của mặt trời khi nhìn trên bầu trời. Góc càng lớn sẽ đổ bóng càng mềm và vùng phản chiếu sáng càng rộng.
* `Kích thước` (_chỉ đèn rọi và điểm_) là độ rộng của đèn. Đèn càng lớn đổ bóng càng mềm.
* `Bóng` sẽ bật/tắt bóng đổ cho đèn hiện tại.
* Loại bóng chọn cách tính bóng đổ. `Bản đồ bóng` kết xuất cảnh từ phía đèn, nên nó cũng đổ bóng cả những hình học mà camera không nhìn thấy. `Không gian màn hình` chỉ dùng những gì đã hiển thị trên màn hình: nó nhẹ hơn, nhưng còn đang thử nghiệm. Nhìn chung, bản đồ bóng đáng tin cậy hơn.
* `Dung sai` (_chỉ không gian màn hình_): nếu thấy bóng bị lỗi hiển thị (bóng có vẻ không chạm vào bề mặt, hoặc có nhiễu và hoa văn lạ trong bóng), việc chỉnh dung sai có thể giúp khắc phục.
* `Liên hệ` thêm bóng chính xác hơn ở những khoảng cách ngắn, nơi các đối tượng chạm vào nhau. Với `Tự động`, chỉ đèn chiếm ưu thế nhất trong cảnh mới có bóng tiếp xúc; `Không` và `Có` buộc tắt hoặc bật nó cho đèn này. Thanh trượt `Dung sai` của nó hoạt động giống như thanh trượt ở trên.

Nút `...` của thanh công cụ trong khung nhìn chứa các thiết lập bóng đổ tương tự, cùng với:

* `Nhân bản` sẽ nhân bản đèn.
* `Đặt lại vị trí` sẽ di chuyển đèn ra trước camera, giữ nguyên hướng của nó.
* `Xóa` sẽ xóa đèn.


## ![](/icons/panorama.webp) Môi trường {#environment}

![](/images/shading_environment.webp)

Ánh sáng trong thế giới thực đến từ mọi hướng; màu xanh của bầu trời, màu xanh lá của cỏ, màu đỏ của một tòa nhà, tất cả ánh sáng từ 'môi trường' này có thể được mô phỏng bằng một bản đồ môi trường. 

Dùng ô đánh dấu bên cạnh tiêu đề để bật hoặc tắt chiếu sáng môi trường.

Nomad đi kèm nhiều bản đồ môi trường mẫu cho không gian trong nhà và ngoài trời, với các sắc độ và mức độ sáng khác nhau. Hãy thử nhiều bản đồ để xem bản đồ nào làm nổi bật chi tiết tác phẩm điêu khắc của bạn nhất.

Chạm vào ảnh để xem các bản đồ môi trường có sẵn. Từ hộp thoại đó, chọn `Nhập...` để tải bản đồ của riêng bạn. Tốt nhất nên dùng ảnh dải tương phản động cao (HDR), ở định dạng latlong hay equirectangular, dưới dạng tệp .hdr hoặc .exr. Trình duyệt cũng có thể tải môi trường trực tiếp từ [Poly Haven](https://polyhaven.com/hdris), nơi có một bộ sưu tập bản đồ môi trường miễn phí rất tốt.

### Độ phơi sáng {#env-exposure}
Điều chỉnh độ sáng của bản đồ môi trường. Các bản đồ thường có thể quá sáng khi dùng cùng đèn thông thường; giảm độ phơi sáng có thể giúp cân bằng, đặc biệt khi dùng với Chiếu sáng toàn cầu trong phần thiết lập [Hậu kỳ](postprocess).

### Xoay {#env-rotation}

Vì bản đồ môi trường ghi lại ánh sáng từ mọi hướng, bạn có thể xoay chúng để phản chiếu và ánh sáng tổng thể hòa hợp tốt với tác phẩm điêu khắc. Bạn cũng có thể xoay môi trường bằng cách kéo ngang 3 ngón tay trên khung nhìn.

### Gắn vào camera {#env-attached}
Gắn môi trường vào camera.

Điều này buộc ánh sáng luôn nhất quán, có thể hữu ích trong lúc điêu khắc.

### Làm mờ (nền) {#env-background-blur}
Thanh trượt này chỉ hiện khi [nền](background.md) được đặt là môi trường. Nó làm mờ ảnh môi trường phía sau mô hình, mà không thay đổi ánh sáng.


## ![](/icons/fog.webp) Sương mù {#fog}

Sương mù thêm chiều sâu không khí cho cảnh và làm các chùm sáng hiện ra rõ ràng. Bật nó bằng ô đánh dấu bên cạnh tiêu đề. Giống như đèn và môi trường, nó chỉ có sẵn ở chế độ [Chiếu sáng (PBR)](#pbr).

::: tip Chùm sáng rõ hơn
Giảm `Môi trường` của sương mù, và dùng một đèn rọi hoặc đèn điểm thật sáng. Tăng `Mật Độ` cho đến khi sương mù hiện rõ. Để thấy chùm sáng trong lớp sương mỏng hơn, đặt `Hướng tán xạ` ở một giá trị dương cao và hướng camera về phía đèn.
:::

### Màu sắc {#fog-color}
Màu của sương mù và của ánh sáng mà nó tán xạ.

### Mật Độ {#fog-density}
Tốc độ sương mù dày lên theo khoảng cách.

### Độ mờ tối đa {#fog-opacity}
Giới hạn mức độ sương mù có thể che phủ cảnh, ngay cả khi mật độ cao.

### Hướng tán xạ {#fog-scattering}
Hướng mà sương mù tán xạ ánh sáng (còn gọi là tính dị hướng). Giá trị dương làm sương mù sáng hơn khi bạn nhìn về phía đèn, giá trị âm khi bạn nhìn ra xa đèn, còn giá trị bằng không tán xạ ánh sáng đều theo mọi hướng.

### ![](/icons/panorama.webp) Môi trường {#fog-environment}
Mức độ [môi trường](#environment) chiếu sáng sương mù. Tùy chọn này bị làm mờ khi môi trường bị tắt.

### Nhiễu {#fog-noise}
Trộn nhiễu vào sương mù để chia nó thành từng mảng, mà không thay đổi mật độ tổng thể. Khi nhiễu lớn hơn 0, thanh trượt `Kích thước` sẽ đặt kích thước của họa tiết.

### Hình dạng {#fog-shape}
Nơi sương mù phủ trong cảnh:

* `Đồng đều` - phủ toàn bộ cảnh.
* `Thẳng đứng` - giữ sương mù bên trong một dải theo chiều đứng với các mép mềm. Thanh trượt `Dưới` và `Trên` đặt độ cao của mép dưới và mép trên, và nút con mắt của chúng hiển thị dải này trong khung nhìn khi bạn điều chỉnh.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

Như tên gọi (MATerial CAPture, chụp vật liệu), một matcap đảm nhận cả thông tin chiếu sáng lẫn vật liệu trong một ảnh duy nhất.
Vì bản thân vật liệu đã có sẵn trong matcap, các kênh vẽ độ nhám và độ kim loại sẽ bị bỏ qua.
Màu vẽ sẽ được nhân với matcap, nghĩa là nếu bạn dùng một matcap đen/xám, vẽ màu trắng cũng sẽ không làm nó sáng hơn.

Các nghệ sĩ thường ưa chuộng chế độ này khi điêu khắc vì nó giúp họ tập trung vào hình dạng và hình học.

Chạm vào hình cầu sẽ mở trình duyệt ảnh. Bạn cũng có thể thêm matcap của riêng mình: nhìn chung, bất kỳ ảnh chụp, ảnh kết xuất, hay thậm chí một bức vẽ hình cầu nào được cắt sát thành hình vuông đều có thể dùng được. Có nhiều thư viện matcap trên mạng, một nguồn hữu ích là [thư viện matcap của nidorx](https://github.com/nidorx/matcaps).

### Sử dụng MatCap toàn cục {#matcap-global}

Thông thường các nghệ sĩ dùng một matcap duy nhất cho cả tác phẩm điêu khắc, nhưng nếu tắt tùy chọn này, đối tượng được chọn có thể có matcap riêng. Bạn có thể tận dụng điều này một cách nghệ thuật để có những kết quả ấn tượng.

::: tip
Hãy tắt tùy chọn này, và dùng ảnh một nhãn cầu cho mắt nhân vật của bạn!
:::

### Xoay {#matcap-rotation}
Matcap là một dạng đặc biệt của bản đồ môi trường, nên giống như bản đồ môi trường, nó có thể được xoay. Bạn cũng có thể làm điều này bất cứ lúc nào trong khung nhìn bằng cách kéo 3 ngón tay sang trái và phải.

Nút ổ khóa bên cạnh thanh trượt sẽ khóa góc xoay, để thao tác kéo 3 ngón tay không vô tình xoay matcap.



## ![](/icons/circle_fill.webp) Không sáng {#unlit}

Chế độ này chỉ hiển thị màu bề mặt. Nó hữu ích để kiểm tra màu bề mặt của các đối tượng có đúng như bạn mong muốn không, mà không bị phân tâm bởi đèn, bóng đổ, phản chiếu hay độ trong suốt. 

Chế độ này cũng có thể dùng cho các bản kết xuất phi hiện thực, tạo phong cách phẳng như hoạt hình.

## ![](/icons/cube.webp) ID vật thể {#object-id}

Mọi thông tin chiếu sáng và bề mặt đều bị bỏ qua, và mỗi đối tượng được tô một màu phẳng riêng biệt. Nếu bạn kết xuất chế độ này cùng với một bản kết xuất PBR, bạn có thể dùng nó trong một chương trình vẽ để chọn theo màu, từ đó chỉnh màu cho từng đối tượng cụ thể.

Lưu ý rằng các màu này cũng sẽ xuất hiện trong [chế độ xem dạng cây của menu Cảnh](scene#tree-view).

### Ngẫu nhiên hóa id {#object-random}

Tạo một bộ màu ngẫu nhiên mới. 

## ![](/icons/link.webp) ID thực thể {#instance-id}

Giống như ID vật thể, nhưng các thực thể sẽ có cùng màu. 

### Ngẫu nhiên hóa id {#instance-random}

Tạo một bộ màu ngẫu nhiên mới.
