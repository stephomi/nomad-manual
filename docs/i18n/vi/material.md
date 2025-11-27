# ![](/icons/material.webp) Vật liệu

Menu này cho phép bạn thay đổi vật liệu của đối tượng hiện tại, các thuộc tính kết xuất của đối tượng/vật liệu, và gán texture cho vật liệu.

![](/images/material_overview.webp)

Vật liệu xác định cách một đối tượng trông như thế nào, bằng cách điều khiển cách nó phản ứng với ánh sáng và với các đối tượng khác. Diện mạo của một đối tượng được điều khiển bởi các thuộc tính sau:

* `Material type`
* `Color`
* `Roughness`
* `Metalness`
* `Opacity`
* `Reflectance`
* `Emissive/unlit`

Kết hợp các thuộc tính này có thể đạt được rất nhiều kiểu kết quả, từ siêu thực cho đến hoạt hình hoặc thử nghiệm.

Color, roughness, metalness và opacity có thể được vẽ, xem [Tùy chọn Vertex Paint](painting.md) để biết thêm thông tin.

Material type, reflectance, emssive/unlit là các thuộc tính vật liệu được giải thích bên dưới.

Các nút copy/paste ở đầu menu này cho phép bạn sao chép vật liệu từ đối tượng này sang đối tượng khác.

Lưu ý rằng bộ kết xuất của Nomad là bộ kết xuất thời gian thực; dù mạnh mẽ, nó ưu tiên tốc độ hơn độ chính xác đối với một số hiệu ứng nhất định. 

## Material types

![](/images/material_types.webp)

Các loại vật liệu trong Nomad là Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Opaque
Chế độ mặc định, xử lý bề mặt như một vật liệu đơn giản hỗ trợ vẽ color, roughness, metalness, opacity.

### ![](/icons/material_subsurface.webp) Subsurface
Chế độ này có thể mô phỏng vật liệu cho phép ánh sáng mờ đi và tán xạ bên trong như da, sáp, ngọc.

Để có kết quả tốt nhất, hãy chuyển sang chế độ PBR shading và dùng ít nhất một đèn directional hoặc spot, lý tưởng là với môi trường mờ.

`Depth` điều khiển khoảng cách ánh sáng tán xạ từ mặt trước, xuyên xuống dưới bề mặt, rồi ra lại mặt trước. Điều này làm mềm bóng đổ gắt và làm mờ chi tiết bề mặt.

`Translucency` điều khiển cách ánh sáng tán xạ từ mặt trước ra mặt sau của một hình dạng, giống như ánh sáng tán xạ qua mặt dưới của chiếc lá, hoặc khi tai được chiếu sáng mạnh từ phía sau. 

### ![](/icons/material_blending.webp) Blending

Tương tự Opaque, nhưng hỗ trợ thanh trượt opacity để cho phép vật liệu trộn giữa đặc và trong suốt. Đây là một thanh trượt opacity đơn giản, so với opacity có thể vẽ được mà vật liệu opaque hỗ trợ. 

::: warning
Chế độ Blending có thể gây nhấp nháy và bật tắt trên các hình dạng phức tạp hoặc giao nhau.
:::

### ![](/icons/material_additive.webp) Additive
Bạn có thể làm cho mesh của mình bán trong suốt với vật liệu này. Nó tương tự vật liệu blending, nhưng trong khi blending sẽ trộn với môi trường xung quanh, additive sẽ luôn sáng hơn các đối tượng phía sau nó, phù hợp cho các hiệu ứng sáng như tia sáng, lửa, vụ nổ.

Bạn có thể đặt giá trị opacity cao hơn 1, nghĩa là đối tượng sẽ sáng hơn.  
Điều này hữu ích nếu bạn muốn dùng [bloom](postprocess.md#bloom) và `threshold parameter` để chỉ làm đối tượng này phát sáng như một đối tượng emissive.

Chế độ này thường có ít lỗi hơn [Blending](#blending) (order independent transparency).

### ![](/icons/material_refraction.webp) Refraction
Chế độ này có thể dùng để mô phỏng vật liệu kính. Do giới hạn thời gian thực, tự khúc xạ và khúc xạ nhiều lớp bị giới hạn phần nào.

Roughness được vẽ trên model ảnh hưởng đến độ mờ của khúc xạ.
Mặc định, mọi đối tượng được tạo trong Nomad có roughness khoảng 25%, do đó khúc xạ sẽ không hoàn hảo mà hơi mờ.
Bạn có thể dùng nút `paint glossy` để vẽ lại model với roughness và metalness bằng 0 (màu sắc sẽ không bị ảnh hưởng).

Có 2 loại roughness khác nhau: một loại điều khiển độ mờ của phản xạ trên bề mặt, và loại kia điều khiển phần bên trong (khúc xạ).  
Tuy nhiên, vì trong Nomad chỉ có một kênh roughness để vẽ, nên roughness bên trong và bên ngoài sẽ dùng chung một giá trị.  
Để có các giá trị khác nhau (ví dụ một cây kẹo mút có bề mặt sắc nét nhưng bên trong mờ), bạn dùng các thanh trượt `Surface glossiness` và `Interior roughness` để ghi đè roughness đã vẽ.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering
Làm cho đối tượng bán trong suốt bằng cách loại bỏ một số pixel một cách ngẫu nhiên.

### ![](/icons/material_shadow_catcher.webp) Shadow Catcher

Làm cho đối tượng vô hình và chỉ nhận bóng. Hữu ích để kết hợp kết xuất từ Nomad với các hình ảnh khác. 

::: tip

Thông tin thêm về transparency và các chế độ blending có thể được tìm thấy tại https://support.fab.com/s/article/Transparency-Opacity

:::

## Controls

![](/images/material_controls.webp)

### Always unlit
Nếu bật, đối tượng sẽ bỏ qua PBR và Matcap và chỉ hiển thị màu đã vẽ mà không có shading.
Lưu ý rằng nếu bạn dùng [Additive](#additive), bạn có thể vẽ độ trong suốt trực tiếp bằng cách dùng màu đen.

### Opacity
Mức độ đặc hay trong suốt của đối tượng; 100% là đặc, 0% là trong suốt. Bạn cũng có thể vẽ opacity để điều khiển chi tiết hơn.

### Reflectance
Điều khiển lượng phản xạ mà vật liệu nhận được đối với vật liệu không kim loại. Hầu hết thời gian nên dùng giá trị mặc định (tương ứng với 4% ánh sáng phản xạ ở góc vuông), nhưng có thể tăng lên để làm nổi bật phản xạ và highlight, ví dụ trong mắt nhân vật.

### Inverse culling
Đảo ngược normal của bề mặt. Thường không cần, nhưng có thể dùng nếu model trông như bị lộn trong ra ngoài, hoặc kết hợp với `Two sided` tắt, có thể dùng để tạo nội thất nơi bức tường gần camera luôn bị ẩn.

### Smooth Shading
Xem [tùy chọn toàn cục](settings.md#smooth-shading).  
Giá trị `Auto` sẽ dùng tùy chọn toàn cục.

### Two sided
Xem [tùy chọn toàn cục](settings.md#two-sided).  
Giá trị `Auto` sẽ dùng tùy chọn toàn cục.

### Coloured backface
Xem [tùy chọn toàn cục](settings#two-sided).
Giá trị `Auto` sẽ dùng tùy chọn toàn cục.

### Casts shadows
Hiện tại `Auto` giống với `On`.
Các đối tượng trong suốt cũng đổ bóng (theo mẫu dithering để mô phỏng bóng trộn).  
Hãy tắt đổ bóng nếu bạn có một đối tượng lớn trong cảnh không cần đổ bóng (ví dụ một mặt sàn lớn).

### Recieve shadows
Hiện tại `Auto` giống với `On`.

### Wireframe
Xem [tùy chọn toàn cục](settings.md#wireframe).  
Giá trị `Auto` sẽ dùng tùy chọn toàn cục.


## Textures

![](/images/material_textures.webp)

Nếu một đối tượng có UV, thì texture có thể được áp dụng cho vật liệu bên cạnh color/roughness/metalness/opacity theo vertex. Thông thường đây là kết quả của việc bake texture, nhưng hình ảnh tạo bên ngoài Nomad cũng có thể được dùng.

Texture có thể được áp dụng cho

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Emissive

Nhấp vào một ô texture sẽ mở bộ chọn. Sau khi một texture đã được gán cho một ô vật liệu, nhấp lại sẽ mở bảng texture:

### Texture panel options

![](/images/material_texture_panel.webp)

### Open
Chọn texture khác

### None
Gỡ bỏ texture

### Opacity

Nếu hình ảnh có kênh alpha, tùy chọn này cho phép bạn dùng nó cho Opacity, hoặc bỏ qua nó.

### ![](/icons/link.webp) Biểu tượng Chain/Link 

Biểu tượng link trong các phần sau, khi bật, có nghĩa là bất kỳ tùy chọn nào được dùng sẽ được chia sẻ với các texture khác (color, normal, roughness, metalness, opacity, emissive) cũng đang bật biểu tượng link. 

Điều này cho phép bạn đảm bảo nếu bạn có các texture đã được canh thẳng hàng, chúng sẽ vẫn thẳng hàng ngay cả khi bạn thay đổi tham số hoặc kiểu projection.


### Projection
![](/images/material_projection.webp)

Thiết lập cách texture được áp dụng lên đối tượng.

* `Auto` - Nếu đối tượng có uv, dùng UV, nếu không thì dùng Triplanar
* `UV` - Dùng tọa độ uv của mesh để áp dụng texture. Nếu mesh và texture đến từ bên ngoài Nomad, hoặc sẽ được xuất từ Nomad để dùng ở nơi khác, UV là lựa chọn đúng.
* `Triplanar` - Chiếu texture dọc theo các trục X,Y,Z và trộn các đường nối. 

### Triplanar
![](/images/material_triplanar.webp)

Projection Triplanar là một cách mạnh mẽ nhưng đơn giản để áp dụng texture lên đối tượng.

Triplanar giống như có 6 máy chiếu video cùng chiếu một hình ảnh, chiếu lên mặt trước, sau, trái, phải, trên và dưới của đối tượng.

Sau đó có thể bake thành UV hoặc vertex color nếu cần.


![](/images/material_triplanar_example.webp)

#### Method

* `Local` - Projection sẽ di chuyển theo transform của đối tượng
* `World` - Projection giữ cố định, di chuyển đối tượng sẽ làm nó trượt qua projection.

#### Hardness

Cách các projection trộn với nhau. 100% sẽ không trộn, và cạnh của các projection sẽ sắc nét. 0% sẽ trộn cạnh trên một góc rộng. Mặc định là 90%, đủ trộn để che giấu cạnh, và để phần còn lại của projection vẫn sắc nét.

### Uniform

Khi được bật, cùng một hardness được dùng cho tất cả projection. Khi tắt, các điều khiển hardness riêng cho các projection X, Y, Z sẽ được hiển thị.


### Parameter
![](/images/material_parameter.webp)

#### Filtering
Phương pháp lọc texture để dùng, `Auto` là mặc định, các phương pháp gồm `Nearest`, `Linear`, `Mipmap`. Nearest không lọc, nên texture có thể bị răng cưa khi nhìn gần. Linear và Mipmap lọc tốt hơn, nên texture trông mờ thay vì răng cưa khi nhìn gần.

#### Tiling-X
Nếu tham số Scale lớn hơn 1, làm texture nhỏ hơn UV của đối tượng, texture sẽ được lặp lại thế nào dọc theo trục X. `None` nghĩa là không lặp. `Repeat` sẽ sao chép texture. `Mirror` sẽ sao chép texture, với mỗi bản sao thứ hai bị đảo ngược, có thể giúp che giấu lỗi lặp.

#### Tiling-Y
Giống Tiling-X, nhưng cho trục Y.

### Transform
![](/images/material_transform.webp)

Các phép biến đổi 2D bổ sung được áp dụng cho texture trong không gian UV. Nút reset đưa về mặc định, biểu tượng chain (khi chọn các texture khác color) sẽ liên kết hoặc bỏ liên kết transform để giống với texture color.

#### Translation
Độ lệch X và Y của texture

#### Rotation
Góc xoay của texture

#### Scale
Tỷ lệ của texture, số lớn hơn sẽ làm texture nhỏ hơn trên đối tượng, dùng các thanh trượt Tiling-X và Tiling-Y để điều khiển những gì xảy ra.

### Uniform scale
Khi tắt, Nomad sẽ hiển thị các điều khiển riêng cho Scale-X và Scale-Y.
