# ![](/icons/material.webp) Vật liệu {#material}

Menu này giúp bạn đổi vật liệu của đối tượng hiện tại, chỉnh các thuộc tính hiển thị của đối tượng/vật liệu, và gán kết cấu (texture) cho vật liệu.

![](/images/material_overview.webp)

Vật liệu quyết định vẻ ngoài của một đối tượng, bằng cách điều khiển cách nó phản ứng với ánh sáng và với các đối tượng khác. Vẻ ngoài ấy được điều khiển bởi các thuộc tính sau:

* `Loại vật liệu`
* `Màu sắc`
* `Độ nhám`
* `Độ kim loại`
* `Độ mờ`
* `Phản xạ`
* `Phát sáng/không nhận sáng`

Kết hợp các thuộc tính này, bạn có thể đạt được rất nhiều kiểu kết quả, từ chân thực như ảnh chụp, đến phong cách hoạt hình, cho tới những thử nghiệm lạ mắt.

Màu sắc, độ nhám, độ kim loại và độ mờ đục có thể được vẽ trực tiếp, xem [các tùy chọn vẽ đỉnh](painting.md) để biết thêm.

Loại vật liệu, phản xạ và phát sáng/không nhận sáng là các thuộc tính của vật liệu, được giải thích bên dưới.

Hai nút `Sao chép` và `Dán` ở đầu menu cho phép bạn chép vật liệu từ đối tượng này sang đối tượng khác.

Lưu ý rằng trình kết xuất của Nomad là trình kết xuất thời gian thực: tuy mạnh mẽ, nó ưu tiên tốc độ hơn độ chính xác với một số hiệu ứng.

## Loại vật liệu {#material-types}

![](/images/material_types.webp)

Các loại vật liệu của Nomad gồm: Không trong suốt, Dưới bề mặt, Pha trộn, Thêm, Khúc xạ, Hiệu ứng mờ nhòe và Bộ bắt bóng.

### ![](/icons/material_opaque.webp) Không trong suốt {#opaque}
Chế độ mặc định, coi bề mặt là một vật liệu đơn giản hỗ trợ màu, độ nhám, độ kim loại và độ mờ đục được vẽ. Độ mờ đục được vẽ, kết cấu độ mờ hoặc kênh alpha của kết cấu màu vẫn làm đối tượng trở nên trong suốt, bằng kỹ thuật dithering. Chỉ có thanh trượt độ mờ chính là bị bỏ qua.

### ![](/icons/material_subsurface.webp) Dưới bề mặt {#subsurface}
Chế độ này mô phỏng những vật liệu mà ánh sáng bị khuếch tán và tán xạ bên trong, như da, sáp hay ngọc bích.

Nó cần chế độ tô bóng PBR. Để có kết quả đẹp nhất, hãy dùng ít nhất một đèn định hướng hoặc đèn rọi, lý tưởng là trong một môi trường hơi tối.

Ô màu đặt màu của ánh sáng bị tán xạ.

`Độ sâu` điều khiển khoảng cách ánh sáng tán xạ từ mặt trước, đi xuống dưới bề mặt, rồi thoát ra lại ở mặt trước. Hiệu ứng này làm mềm các bóng đổ gắt và làm nhòe chi tiết bề mặt.

`Độ xuyên sáng` điều khiển cách ánh sáng tán xạ từ mặt trước ra mặt sau của một hình khối, giống như ánh sáng xuyên qua mặt dưới của chiếc lá, hay đôi tai khi bị chiếu ngược sáng mạnh. Bạn cần một đèn có đổ bóng để thấy được hiệu ứng này.

### ![](/icons/material_blending.webp) Pha trộn {#blending}

Giống chế độ Không trong suốt, nhưng hỗ trợ thanh trượt độ mờ để vật liệu chuyển dần giữa đặc và trong suốt. Đây chỉ là một thanh trượt độ mờ duy nhất, khác với độ mờ đục vẽ được của vật liệu Không trong suốt.

::: warning
Chế độ Pha trộn có thể gây nhấp nháy và các lỗi hiển thị chập chờn trên những hình khối phức tạp hoặc cắt nhau.
:::

### ![](/icons/material_additive.webp) Thêm {#additive}
Vật liệu này giúp lưới của bạn bán trong suốt. Nó gần giống vật liệu Pha trộn, nhưng trong khi Pha trộn hòa lẫn với xung quanh, thì Thêm luôn sáng hơn các vật thể phía sau nó. Rất hợp cho các hiệu ứng sáng như tia sáng, lửa, vụ nổ.

Bạn có thể đặt độ mờ lớn hơn 1, nghĩa là đối tượng sẽ sáng hơn nữa.  
Điều này hữu ích khi bạn dùng [Bloom](postprocess.md#bloom) cùng tham số `Ngưỡng` để chỉ riêng đối tượng này phát sáng như một vật thể tự phát sáng.

Chế độ này thường ít lỗi hiển thị hơn [Pha trộn](#blending) (độ trong suốt không phụ thuộc thứ tự vẽ).

### ![](/icons/material_refraction.webp) Khúc xạ {#refraction}
Chế độ này dùng để mô phỏng vật liệu thủy tinh. Nó cần chế độ tô bóng PBR. Do giới hạn của kết xuất thời gian thực, khả năng tự khúc xạ và khúc xạ nhiều lớp còn khá hạn chế.

Độ nhám được vẽ trên mô hình ảnh hưởng đến độ nhòe của khúc xạ.
Theo mặc định, mọi đối tượng tạo trong Nomad có độ nhám khoảng 25%, nên khúc xạ sẽ không hoàn hảo mà hơi nhòe.
Bạn có thể dùng nút `Sơn bóng` để vẽ lại mô hình với độ nhám và độ kim loại bằng 0 (màu sắc không bị ảnh hưởng).

Có 2 loại độ nhám khác nhau cùng tác động: một loại quyết định độ nhòe của phản chiếu trên bề mặt, loại kia quyết định phần bên trong (khúc xạ).  
Tuy nhiên, vì Nomad chỉ có một kênh vẽ độ nhám, cả độ nhám bên trong lẫn bên ngoài sẽ dùng chung một giá trị.  
Để có hai giá trị khác nhau (ví dụ một cây kẹo mút có bề mặt sắc nét nhưng bên trong nhòe), bạn dùng các thanh trượt `Bề mặt` và `Nội thất` trong `Ghi đè độ gồ ghề` để ghi đè độ nhám đã vẽ.

![](/videos/refraction.mp4)

#### Chỉ số khúc xạ {#index-of-refraction}
Mức độ ánh sáng bị bẻ cong khi đi vào đối tượng. Giá trị càng cao thì ánh sáng càng bị bẻ cong nhiều, như một thấu kính dày.

#### Hấp thụ {#absorption}
Mô phỏng ánh sáng bị hấp thụ khi đi xuyên qua khối vật thể, nhuốm màu theo ô màu, với `Hệ số` đặt độ mạnh. Những phần mỏng sáng hơn vì cho nhiều ánh sáng đi qua, còn những vùng dày thì tối hơn. Nomad chỉ dùng độ dày gần đúng của đối tượng, nên hiệu ứng phụ thuộc nhiều vào hình dạng.


### ![](/icons/material_dithering.webp) Hiệu ứng mờ nhòe {#dithering}
Làm đối tượng bán trong suốt bằng cách bỏ đi một số điểm ảnh một cách ngẫu nhiên.

### ![](/icons/material_shadow_catcher.webp) Bộ bắt bóng {#shadow-catcher}

Làm đối tượng trở nên vô hình, chỉ nhận bóng đổ từ các đèn. Hữu ích khi ghép ảnh render từ Nomad với các hình ảnh khác, thường dùng trên một mặt phẳng. Ô màu đặt màu của bóng.

Trong cảnh phải có một đèn đổ bóng, nếu không Bộ bắt bóng sẽ không làm gì cả. Các nút `Độ kim loại → 0%` và `Độ kim loại → 100%` vẽ lại đối tượng: khi hoàn toàn bằng kim loại, Bộ bắt bóng còn có thể phản chiếu cảnh nếu hiệu ứng hậu kỳ [Phản chiếu (SSR)](postprocess.md#reflection-ssr) được bật.

::: tip

Bạn có thể tìm thêm thông tin về độ trong suốt và các chế độ pha trộn tại https://support.fab.com/s/article/Transparency-Opacity

:::

## Điều khiển {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Luôn không nhận sáng {#always-unlit}
Khi bật, đối tượng sẽ bỏ qua PBR và MatCap, chỉ hiển thị màu đã vẽ mà không có tô bóng.
Lưu ý rằng nếu bạn dùng [Thêm](#additive), bạn có thể vẽ độ trong suốt trực tiếp bằng màu đen.

### Độ mờ {#opacity}
Mức độ đặc hay mờ đục của đối tượng: 100% là đặc hoàn toàn, 0% là trong suốt. Thanh trượt này hiện với các loại Pha trộn, Thêm, Hiệu ứng mờ nhòe và Bộ bắt bóng. Bạn cũng có thể vẽ độ mờ đục để điều khiển chi tiết hơn.

### Bước tiền khúc xạ {#pre-refract-pass}
Chỉ dành cho Pha trộn và Thêm. Vẽ đối tượng trong suốt này trước bước khúc xạ. Hữu ích khi một vật thể khúc xạ nằm phía trước các bề mặt trong suốt khác.

### Phản xạ {#reflectance}
Điều khiển lượng phản xạ mà vật liệu nhận được, với các vật liệu không phải kim loại. Phần lớn thời gian bạn nên giữ giá trị mặc định (tương ứng với mức chuẩn 4% ánh sáng phản xạ ở góc vuông), nhưng có thể tăng lên để làm nổi phản chiếu và điểm sáng, chẳng hạn trong mắt nhân vật. Nó cần chế độ tô bóng PBR.

### ![](/icons/culling.webp) Nghịch đảo {#inverse-culling}
Đảo ngược pháp tuyến của bề mặt. Thường thì không cần, nhưng có thể dùng khi mô hình bị lộn trong ra ngoài, hoặc kết hợp với việc tắt `Hai mặt` để làm nội thất, nơi bức tường gần camera nhất luôn bị ẩn đi.

Các tùy chọn sau có thể đặt là `Tự động`, `Không` hoặc `Có`. Với `Tự động`, mũi tên cho biết giá trị thực sự đang được dùng.

### ![](/icons/sphere_smooth.webp) Tô bóng mượt {#smooth-shading}
Xem [tùy chọn chung](settings.md#smooth-shading).  
Giá trị `Tự động` sẽ dùng tùy chọn chung.

### ![](/icons/culling.webp) Hai mặt {#two-sided}
Các mặt sẽ nhìn thấy được từ cả hai phía. Xem [tùy chọn chung](settings.md#two-sided-quick).  
Giá trị `Tự động` sẽ dùng tùy chọn chung.

### ![](/icons/culling.webp) Mặt sau có màu {#coloured-backface}
Xem [tùy chọn chung](settings.md#two-sided-quick).
Giá trị `Tự động` sẽ dùng tùy chọn chung.

### ![](/icons/shadow_cast.webp) Đổ bóng {#casts-shadows}
Các đối tượng trong suốt cũng đổ bóng (theo dạng dithering để giả lập bóng pha trộn).  
Hãy nhớ tắt đổ bóng nếu cảnh của bạn có một đối tượng lớn không cần đổ bóng (ví dụ một mặt sàn lớn).

### ![](/icons/shadow_receive.webp) Nhận bóng {#recieve-shadows}
Có vẽ bóng của các đối tượng khác lên đối tượng này hay không.

### ![](/icons/wireframe.webp) Khung lưới {#wireframe}
Xem [tùy chọn chung](settings.md#wireframe).  
Giá trị `Tự động` sẽ dùng tùy chọn chung.

### ![](/icons/trash.webp) Đặt lại pháp tuyến {#reset-normals}
Chỉ hiện khi một đối tượng được nhập vào mang sẵn pháp tuyến riêng (ví dụ khi dùng `Giữ topologi`). Nút này xóa chúng đi, để tô bóng dùng pháp tuyến được tính từ bề mặt.


## Kết cấu {#textures}

![](/images/material_textures.webp)

Nếu đối tượng có UV, bạn có thể áp kết cấu cho vật liệu, ngoài màu/độ nhám/độ kim loại/độ mờ đục được vẽ trên đỉnh. Thường thì đó là kết quả của một lần bake kết cấu, nhưng bạn cũng có thể dùng ảnh tạo bên ngoài Nomad. `UV:✓` hoặc `UV:✗` cạnh tiêu đề cho bạn biết đối tượng có UV hay không.

Kết cấu có thể áp cho

* Màu sắc
* Pháp tuyến
* Độ nhám
* Độ kim loại
* Độ mờ đục
* Dịch chuyển
* Phát sáng

Một hàng `Tắc nghẽn` cũng xuất hiện khi đối tượng được nhập vào có kết cấu che khuất (occlusion), nhưng Nomad không dùng đến nó.

Thanh trượt của mỗi hàng đặt mức áp kết cấu, từ hoàn toàn không đến đầy đủ. `Màu sắc` và `Phát sáng` còn có ô màu để nhuộm kết cấu, và `Phát sáng` đặt cường độ phát sáng.

`Dịch chuyển` đặt khoảng cách mà bản đồ dịch chuyển đẩy bề mặt đi. Nút `Áp dụng` của nó di chuyển các đỉnh theo độ dịch chuyển, rồi gỡ bản đồ đi. Kết quả được ghi vào lớp đang hoạt động.

Nút bảng màu cạnh tiêu đề mở các vật liệu thiết lập sẵn của menu [Sơn](painting.md): chạm vào một mẫu để chép kết cấu của nó lên đối tượng. Trên máy tính, các ảnh đã nhập sẽ đồng bộ với tệp gốc khi bạn quay lại Nomad, và một nút đồng bộ cạnh tiêu đề sẽ tải lại chúng.

Nhấn vào một ô kết cấu sẽ mở bộ chọn. Sau khi đã gán kết cấu cho một ô vật liệu, nhấn lần nữa sẽ mở bảng kết cấu:

### Tùy chọn của bảng kết cấu {#texture-panel-options}

![](/images/material_texture_panel.webp)

Bảng hiển thị kích thước ảnh và bản xem trước của kết cấu.

### ![](/icons/open.webp) Mở {#open}
Chọn một kết cấu khác. Trên máy tính, `Khám phá` hiển thị tệp ảnh trong trình duyệt tệp của bạn.

### ![](/icons/circle_cross.webp) Không có {#none}
Gỡ bỏ kết cấu

### Độ mờ {#texture-opacity}

Chỉ với kết cấu màu. Nếu ảnh có kênh alpha, tùy chọn này cho phép bạn dùng nó làm độ mờ đục, hoặc bỏ qua nó.

### Định dạng {#normal-format}
Chỉ với kết cấu pháp tuyến. Bản đồ pháp tuyến có hai kiểu, `OpenGL (+Y)` và `DirectX (-Y)`. Nếu chi tiết trông bị đảo ngược, hãy thử kiểu còn lại.

### Chiều cao {#displacement-height}
Chỉ với kết cấu dịch chuyển.
* `Cục bộ` - Chiều cao to lên và nhỏ lại theo tỷ lệ của đối tượng.
* `Thế giới` - Chiều cao giữ nguyên dù đối tượng có tỷ lệ thế nào.

### Nhân {#multiply}
Chỉ với kết cấu độ nhám, độ kim loại và độ mờ đục. Nhân các giá trị của kết cấu. Khi khác 100%, giá trị này được hiển thị trên ô kết cấu.

### ![](/icons/link.webp) Biểu tượng xích/liên kết {#chainlink-icon}

Khi biểu tượng liên kết trong các phần dưới đây được bật, mọi tùy chọn bạn dùng sẽ được chia sẻ với các kết cấu khác (màu, pháp tuyến, độ nhám, độ kim loại, độ mờ đục, phát sáng) cũng đang bật biểu tượng liên kết.

Nhờ vậy, nếu các kết cấu của bạn đã khớp nhau, chúng sẽ vẫn khớp kể cả khi bạn thay đổi tham số hay kiểu chiếu.


### Phép Chiếu {#projection}
![](/images/material_projection.webp)

Đặt cách áp kết cấu lên đối tượng.

* `Tự động` - Dùng UV nếu đối tượng có UV, nếu không thì dùng Triplanar
* `UV` - Dùng tọa độ UV của lưới để áp kết cấu. Nếu lưới và kết cấu đến từ bên ngoài Nomad, hoặc sẽ được xuất từ Nomad để dùng ở nơi khác, thì UV là lựa chọn đúng.
* `Triplanar` - Chiếu kết cấu dọc theo các trục X, Y, Z và hòa trộn các đường nối.

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Phép chiếu Triplanar là một cách đơn giản mà mạnh mẽ để áp kết cấu lên đối tượng.

Hãy hình dung có 6 máy chiếu cùng chiếu một hình ảnh, rọi vào mặt trước, mặt sau, bên trái, bên phải, phía trên và phía dưới đối tượng của bạn.

Khi cần, kết quả có thể được bake vào UV hoặc màu đỉnh.


![](/images/material_triplanar_example.webp)

#### Phương pháp {#method}

* `Cục bộ` - Phép chiếu di chuyển theo phép biến đổi của đối tượng
* `Thế giới` - Phép chiếu đứng yên, di chuyển đối tượng sẽ khiến nó trượt qua phép chiếu.

#### Độ cứng {#hardness}

Cách các phép chiếu hòa vào nhau. 100% là không hòa trộn, các cạnh của phép chiếu sẽ sắc nét. 0% hòa trộn các cạnh trên một góc rộng. Mặc định là 90%, đủ để giấu các cạnh mà phần còn lại của phép chiếu vẫn sắc nét.

### Đồng nhất {#uniform}

Khi được chọn, cùng một độ cứng được dùng cho mọi phép chiếu. Khi bỏ chọn, sẽ có thêm các điều khiển độ cứng riêng cho phép chiếu X, Y, Z.


### Tham số {#parameter}
![](/images/material_parameter.webp)

#### Lọc {#filtering}
Phương pháp lọc kết cấu: mặc định là `Tự động`, các phương pháp gồm `Gần nhất`, `Tuyến tính` và `Mipmap`. Gần nhất không lọc gì, nên khi nhìn gần kết cấu có thể bị răng cưa. Tuyến tính và Mipmap lọc tốt hơn, nên khi nhìn gần kết cấu trông nhòe thay vì răng cưa.

#### Lát gạch - X {#tiling-x}
Khi tham số Tỷ lệ lớn hơn 1, khiến kết cấu nhỏ hơn UV của đối tượng, tùy chọn này quyết định cách kết cấu được lát dọc theo trục X. `Không có` nghĩa là không lặp lại. `Lặp lại` tạo các bản sao của kết cấu. `Gương` tạo các bản sao của kết cấu, cứ mỗi bản sao thứ hai lại bị lật ngược, giúp che bớt dấu vết lặp lại.

#### Lát gạch - Y {#tiling-y}
Giống Lát gạch - X, nhưng cho trục Y.

### Biến đổi {#transform}
![](/images/material_transform.webp)

Các phép biến đổi 2d bổ sung áp cho kết cấu trong không gian UV. Nút đặt lại đưa về giá trị mặc định, còn biểu tượng xích (khi chọn kết cấu khác ngoài màu) sẽ liên kết hoặc bỏ liên kết phép biến đổi để giống với kết cấu màu.

#### Dịch chuyển {#translation}
Độ dời của kết cấu theo X và Y

#### Xoay {#rotation}
Góc xoay của kết cấu

#### Tỷ lệ {#scale}
Tỷ lệ của kết cấu: số càng lớn thì kết cấu trên đối tượng càng nhỏ. Dùng các tùy chọn Lát gạch - X và Lát gạch - Y để quyết định điều gì xảy ra khi đó.

### Tỷ lệ đồng nhất {#uniform-scale}
Khi tắt, Nomad sẽ hiển thị các điều khiển riêng cho Tỷ lệ X và Tỷ lệ Y.
