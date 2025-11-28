# ![](/icons/sun.webp) Đổ bóng {#shading}

Menu này điều khiển các chế độ đổ bóng Nomad sử dụng, thuộc tính ánh sáng, và thuộc tính ánh sáng môi trường/matcap.

![](/images/shading_overview.webp)



Bạn có thể chọn giữa nhiều chế độ kết xuất:

| Mode                        | Meaning                          | Description                                                     |
| :-------------------------: | :------------------------------: | :-------------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Kết xuất dựa trên vật lý (PBR)   | Tô vẽ với metalness/roughness                                  |
| [Matcap](#matcap)           | Material Capture                 | Dùng khi điêu khắc, tốn ít gpu/cpu hơn PBR                      |
| [Unlit](#unlit)             | Màu bề mặt                       | Chỉ màu bề mặt, không có đổ bóng hay chiếu sáng                |
| [Object Id](#object-id)      | Object ID                        | Màu ngẫu nhiên cho mỗi đối tượng, hữu ích cho phần mềm tô vẽ   |
| [Instance Id](#instance-id)  | Instance ID                      | Màu ngẫu nhiên cho mỗi instance, hữu ích để nhận diện mesh dùng chung |

Nếu bạn muốn tìm hiểu thêm về metalness và roughness, xem phần [Vertex Paint](painting.md).

---

![](/images/shading_second.webp)

### Nhóm mặt {#face-group}
Hiển thị chồng màu facegroup. Facegroup là các vùng đa giác được tô màu, có thể được tạo bằng công cụ [Face group](tools#facegroup), và được tạo tự động với hầu hết các primitive.

Một số công cụ sẽ tự động lọc theo facegroup khi facegroup đang được hiển thị.

### Hiện sơn {#show-paint}
Nomad có thể lưu màu, roughness, metalness trong các vertex của bản điêu khắc. Bạn có thể bật/tắt hiển thị các thuộc tính này trên toàn cảnh bằng checkbox này.

Lưu ý nếu bạn có cả thuộc tính vertex và texture, và cả hai đều được bật, các giá trị sẽ được nhân với nhau.

### Hiện mặt nạ {#show-mask}
Bật/tắt lớp phủ mask thang xám của [các công cụ mask](tools#mask). Khi tắt tùy chọn này, mask cũng bị vô hiệu hóa, hữu ích khi cần chỉnh nhanh mà không dùng mask, sau đó có thể bật lại mà không mất mask.

### Dùng ẩn {#use-hide}

Bật/tắt các mặt bị ẩn. Lưu ý điều này chỉ hoạt động nếu bạn KHÔNG ở trong công cụ hide!

### Dùng kết cấu {#use-textures}

Nomad cho phép gán texture cho đối tượng từ menu [material](material). Nếu texture đã được gán, chúng có thể được bật/tắt toàn cục bằng checkbox này.







### Tổng quan PBR và ánh sáng {#pbr}
Tài liệu này sẽ không đi sâu vào chi tiết về Kết xuất Dựa trên Vật lý (PBR).

Một điều quan trọng cần nhớ là ánh sáng và vật liệu được tách biệt hoàn toàn.
Điều đó có nghĩa là bạn có thể tô màu, roughness và metalness cho đối tượng trong khi ánh sáng được xử lý độc lập.
Điều này cho phép bạn tô vẽ đối tượng rồi tinh chỉnh ánh sáng sau, mà không phá vỡ tổng thể diện mạo của mẫu.

Đèn chỉ khả dụng với [chế độ PBR](#pbr).
Vì lý do hiệu năng, bạn bị giới hạn tối đa 4 đèn.

::: tip
Bạn có thể tải một file glTF có hơn 4 đèn và Nomad sẽ giữ lại tất cả.
Tuy nhiên hiệu năng có thể không tốt.
:::

::: tip
Bạn có thể “giả” nhiều đèn bằng cách đặt đối tượng ở chế độ unlit/emissive, rồi bật global illumination trong menu [post process](postprocess).
:::

### Tổng quan loại ánh sáng {#light-types-overview}

Các loại đèn hiện được hỗ trợ:

| Mode                        | Description                                             | Can cast shadows                                       |
| :-------------------------: | :-----------------------------------------------------: | :----------------------------------------------------: |
| [Directional](#directional) | Ánh sáng mặt trời ở vô cực                              | yes                                                    |
| [Environment](#environment) | Ánh sáng xa được khớp với môi trường HDR               | yes                                                    |
| [Spot](#spot)               | Đèn hình nón				                            | Yes                                                    |
| [Point](#point)             | Điểm sáng phát mọi hướng                                | Yes, but only through less robust screen-space shadows |

#### Hướng {#directional}
Phát sáng từ khoảng cách vô hạn, với cường độ đồng đều.
Vị trí 3D của nó trong cảnh không quan trọng, chỉ có hướng là quan trọng.

Bạn có thể gắn đèn này vào camera, như vậy ánh sáng sẽ luôn nhất quán.  
Ví dụ bạn có thể dùng nó làm rim light (nguồn sáng mạnh từ phía sau mẫu, chiếu về phía camera) luôn chiếu sáng phía sau mẫu.

#### Ánh sáng môi trường {#env-light}
Dùng [environment hdr](#environment) rất tốt cho ánh sáng mềm tổng thể, nhưng nếu có nguồn sáng mạnh, sắc nét trong HDR, bóng đổ tạo ra sẽ rất mềm, thường gần như không thấy. Dùng đèn directional kết hợp với environment HDR có thể giúp, nhưng khó để căn thẳng hàng.

Loại đèn này làm việc đó giúp bạn. Đèn sẽ tự động xoay để thẳng hàng với vùng sáng nhất trong HDR, sau đó bạn có thể điều khiển cường độ và góc (độ mềm của bóng) riêng biệt. 

#### Đèn chiếu (Spot) {#spot}
Đèn spot phát sáng theo một hướng, bị giới hạn bởi hình nón.

#### Điểm {#point}
Đèn point phát sáng theo mọi hướng.  
Hiện tại, đèn point không hỗ trợ bóng đổ.

#### Bóng đổ {#shadows}
Tùy chọn `normal bias` có thể dùng để giảm các lỗi bóng thường gặp (acne/peter-panning).

Chất lượng bóng phụ thuộc vào kích thước đối tượng so với toàn cảnh.  
Nếu bạn có một đối tượng lớn trong cảnh không cần đổ bóng (ví dụ một mặt phẳng lớn), hãy tắt đổ bóng trong [thiết lập vật liệu](material.md#cast-shadows) của nó.

## Đèn {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Bật/tắt đèn {#lights-checkbox}

Bật/tắt toàn bộ các đèn trực tiếp trong cảnh.



### Thêm đèn {#add-light}

Thêm một đèn vào cảnh, tối đa 4 đèn. Khi một đèn được thêm, danh sách đèn sẽ hiển thị với các nút, và một thanh công cụ đèn được thêm vào phía trên khung nhìn.

![](/images/shading_lights_icons.webp)

* Dòng chữ hiển thị tên đèn và độ sáng.
* Biểu tượng con mắt bật/tắt khả năng hiển thị.
* Biểu tượng cây bút cho phép đổi tên đèn.
* Biểu tượng thùng rác sẽ xóa đèn.
* Biểu tượng copy sẽ nhân bản đèn. 
* Biểu tượng 3 chấm sẽ mở trình chỉnh sửa đèn đầy đủ. Hầu hết chức năng này cũng có trong thanh công cụ xuất hiện trong khung nhìn. 

### ![](/icons/spotlight.webp)  Biểu tượng {#icons}

Bật/tắt hiển thị biểu tượng đèn trong khung nhìn.

### Thanh công cụ đèn {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Thanh công cụ này sẽ xuất hiện ở phía trên khung nhìn khi một đèn được chọn.

* Show bật/tắt hiển thị đèn.
* Directional/Environment/Spot/Point sẽ đổi loại đèn. Chạm để chuyển vòng, hoặc nhấn giữ để hiện menu.
* Intensity điều khiển độ mạnh của đèn, giá trị có thể lớn hơn 1.0 cho đèn rất mạnh, hữu ích khi dùng với Global Illumination trong Post Process.
* Ô màu khi bấm sẽ mở bộ chọn màu. Nomad cung cấp nhiều cách chọn màu. Điều khiển Kelvin cho phép chọn ánh sáng ấm/lạnh một cách tự nhiên.
* Shadow bật/tắt bóng đổ.
* Size đặt bề rộng của đèn. Đèn rộng hơn sẽ tạo bóng mềm, ánh sáng mềm, và highlight mềm hơn trên đối tượng.
* ... sẽ mở các điều khiển bổ sung.

### Điều khiển bổ sung cho đèn {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Lưu ý một số tùy chọn chỉ áp dụng cho một số loại đèn nhất định.

* `Clone` sẽ nhân bản đèn.
* `Recenter` sẽ đưa đèn về lại gốc tọa độ.
* `Delete` sẽ xóa đèn.
* `Directional/Environment/Spot/Point` cho phép đổi loại đèn.
* `colour swatch` khi bấm sẽ mở bộ chọn màu. 
* `Intensity` điều khiển độ mạnh của đèn.
* `Attachment` (_chỉ directional_) đặt đèn gắn với thế giới, hoặc gắn với camera. Ví dụ nếu bạn dùng directional light phía sau nhân vật làm rim light, khi chọn attachment là camera, xoay camera sẽ luôn giữ đèn phía sau nhân vật.
* `Angle` (_chỉ directional và environment_) là kích thước biểu kiến của đèn, hãy nghĩ như kích thước mặt trời trên bầu trời. Góc lớn hơn sẽ tạo bóng mềm hơn và highlight rộng hơn.
* `Softness` (_chỉ spotlight_) điều khiển độ sắc của viền hình nón spotlight. 0 là viền rất sắc. 1 là rất mềm, với gradient vào tâm hình nón. Trong khung nhìn, chấm xanh nhỏ trên hình nón spotlight có thể dùng để chỉnh softness trực tiếp.
* `Cone angle` (_chỉ spotlight_) điều khiển góc tỏa của spotlight. Góc nhỏ là tia sáng rất hẹp, 170 là vùng sáng rất rộng. Trong khung nhìn, chấm cam có thể dùng để chỉnh cone angle trực tiếp.
* `Shadow` bật/tắt bóng đổ cho đèn hiện tại.
* `Shadow map` và `screenspace` là các cách khác nhau để tính bóng, thường shadow map đáng tin cậy hơn.
* `Contact` điều chỉnh cách tính bóng tiếp xúc. Bóng là một bài toán khó trong đồ họa máy tính, và có thể gây lỗi hiển thị. Có thể chọn bóng chính xác hơn cho đèn quan trọng nhất trong cảnh; điều khiển này quyết định đèn quan trọng được Nomad chọn tự động hay do người dùng chọn.
* `Tolerance` nếu thấy lỗi bóng (bóng không chạm bề mặt, hoặc có nhiễu/hoa văn trong bóng), chỉnh tolerance có thể giúp khắc phục.

## Môi trường {#environment}

![](/images/shading_environment.webp)

Ánh sáng trong thế giới thực đến từ mọi hướng; xanh của bầu trời, xanh lá của cỏ, đỏ của tòa nhà, tất cả ánh sáng từ “môi trường” này có thể được mô phỏng bằng bản đồ môi trường (environment map). 

Nomad đi kèm một số bản đồ môi trường mẫu cho không gian trong nhà và ngoài trời, với các sắc độ và độ sáng khác nhau. Hãy thử các bản đồ khác nhau để xem bản đồ nào làm nổi bật chi tiết bản điêu khắc của bạn nhất.

Chạm vào hình để xem các bản đồ môi trường có sẵn. Từ hộp thoại đó chọn 'Import...' để tải bản đồ của riêng bạn. Tốt nhất nên dùng ảnh High Dynamic Range (HDR), ở định dạng latlong hoặc equirectangular, dạng file .hdr hoặc .exr. [www.polyhaven.com](https://polyhaven.com/hdris) có bộ sưu tập bản đồ môi trường miễn phí rất tốt; thường các bản đồ hdr 1k là kích thước và chất lượng phù hợp.

### Phơi sáng {#env-exposure}
Điều chỉnh độ sáng của bản đồ môi trường. Thường các bản đồ có thể quá sáng khi dùng cùng đèn thông thường, giảm exposure có thể giúp cân bằng, đặc biệt khi dùng với Global Illumination trong thiết lập [Post Process](postprocess).

### Xoay {#env-rotation}

Vì bản đồ môi trường ghi lại ánh sáng từ mọi hướng, bạn có thể xoay chúng để phản xạ và ánh sáng tổng thể kết hợp tốt với bản điêu khắc.

### Gắn với camera {#env-attached}
Gắn môi trường với camera.

Nó sẽ buộc ánh sáng luôn nhất quán, hữu ích trong quá trình điêu khắc.


## ![](/icons/sphere_smooth.webp) Matcap {#matcap}

![](/images/shading_matcap.webp)

Đúng như tên gọi (MATerial CAPture), matcap chứa cả thông tin ánh sáng và vật liệu trong một hình ảnh duy nhất.
Vì vật liệu đã có sẵn trong matcap, các kênh tô vẽ roughness và metalness sẽ bị bỏ qua.
Màu tô sẽ được nhân với matcap, nghĩa là nếu bạn dùng matcap đen/xám, dùng sơn trắng cũng sẽ không làm nó sáng hơn.

Các họa sĩ thường ưa chuộng chế độ này cho mục đích điêu khắc vì nó cho phép tập trung vào hình khối và hình học.

Chạm vào hình cầu sẽ mở trình duyệt ảnh. Bạn cũng có thể thêm matcap của riêng mình, nói chung bất kỳ bức ảnh, bản render, thậm chí tranh vẽ một quả cầu được cắt gọn thành hình vuông đều có thể dùng. Có nhiều thư viện matcap trực tuyến, một nguồn hữu ích là [nidorx matcap library](https://github.com/nidorx/matcaps).

### Dùng Matcap toàn cục {#matcap-global}

Thông thường nghệ sĩ sẽ dùng một matcap cho toàn bộ bản điêu khắc, nhưng nếu tắt tùy chọn này, mỗi đối tượng có thể có matcap riêng. Điều này có thể dùng mang tính nghệ thuật để tạo hiệu ứng ấn tượng.

::: tip
Tắt tùy chọn này, và dùng một hình ảnh nhãn cầu cho đôi mắt nhân vật của bạn!
:::

### Xoay {#matcap-rotation}
Matcap là một dạng chuyên biệt của bản đồ môi trường, nên giống bản đồ môi trường, nó có thể xoay được. Bạn cũng có thể làm điều này bất cứ lúc nào trong khung nhìn bằng cách kéo 3 ngón tay sang trái/phải.



## ![](/icons/circle_fill.webp) Không đổ sáng (Unlit) {#unlit}

Chế độ này chỉ hiển thị màu bề mặt. Nó hữu ích để kiểm tra màu bề mặt của đối tượng có đúng như mong đợi hay không, mà không bị phân tán bởi đèn, bóng, phản xạ, trong suốt. 

Chế độ này cũng có thể dùng cho các bản render phi hiện thực, tạo phong cách phẳng, hoạt hình.

## ![](/icons/cube.webp) ID đối tượng {#object-id}

Mọi thông tin ánh sáng và bề mặt bị bỏ qua, và mỗi đối tượng được tô bằng một màu phẳng duy nhất. Nếu render song song với một bản render PBR, nó có thể được dùng trong phần mềm tô vẽ để chọn theo màu, từ đó chỉnh màu cho từng đối tượng cụ thể.

Lưu ý các màu này cũng xuất hiện trong [chế độ cây của menu Scene](scene#tree-view).

### Ngẫu nhiên hóa ID {#object-random}

Tạo một bộ màu ngẫu nhiên mới. 

## ![](/icons/link.webp) ID instance {#instance-id}

Giống Object ID, nhưng các instance sẽ có cùng màu. 

### Ngẫu nhiên hóa ID {#instance-random}

Tạo một bộ màu ngẫu nhiên mới.