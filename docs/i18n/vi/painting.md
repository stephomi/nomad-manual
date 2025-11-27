# ![](/icons/paint.webp) Tô màu  

Điều khiển màu sắc, độ nhám (roughness), độ kim loại (metalness) của các nét sơn, cho phép tô tràn (flood fill) các thuộc tính sơn, và cách các công cụ sơn tương tác với layer, mask, vùng ẩn.

![](/images/paint_overview.webp)  

## Tổng quan

Nomad sử dụng kỹ thuật tô màu theo đỉnh (PBR vertex painting). Điều này có nghĩa là gì?

### PBR
PBR, hay Physically Based Rendering (kết xuất dựa trên vật lý), là một kỹ thuật đồ họa máy tính phổ biến trong phim ảnh, truyền hình, game và di động. Bằng cách dựa ánh sáng trên các thuộc tính vật lý, và định nghĩa bề mặt thông qua màu sắc, độ nhám, độ kim loại, có thể đạt được rất nhiều kiểu hiển thị chân thực.

### Tô màu theo đỉnh (Vertex painting)

Vertex painting có nghĩa là thông tin sơn được lưu trong các đỉnh (vertex) của mô hình, thay vì trong texture. Vì Nomad có thể xử lý các mô hình với hàng trăm nghìn, thậm chí hàng triệu đỉnh, mô hình của bạn có thể có lớp sơn bề mặt rất chi tiết; nếu bạn có thể điêu khắc chi tiết đó, bạn cũng có thể tô màu chi tiết đó.

Điều này cũng có nghĩa là tô màu trong Nomad không cần UV mapping, vốn thường là một quy trình chậm và kỹ thuật trong các ứng dụng 3D khác. Nhiều ứng dụng 3D khác không hỗ trợ số lượng đỉnh cao như Nomad, tuy nhiên Nomad cũng có các công cụ bake texture và giảm đa giác (decimation) rất tốt để hỗ trợ.

### Dán chất liệu (Texturing)

Nomad hỗ trợ texture, nhưng chúng phải có sẵn trong mô hình được import, hoặc thông qua việc bake tô màu theo đỉnh sang texture. 

Texture đơn giản là một hình ảnh, nhưng trong ngữ cảnh 3D nó thường chỉ một hình ảnh được gán cho một đối tượng.
Để quấn một hình ảnh quanh mô hình, mô hình cần có tọa độ texture (UV).

Nomad có thể [tự động tính UV](topology.md#uv-unwrap) nhưng bạn sẽ không có nhiều quyền kiểm soát chất lượng tổng thể.

::: tip
Một ví dụ về quy trình làm việc:
- Điêu khắc trong Nomad, sau đó [UV unwrap](topology.md#uv-unwrap)
- Nếu bạn đã bắt đầu tô màu trong Nomad, bạn có thể [chuyển tô màu theo đỉnh sang texture](topology.md#bake-vertex-colors-to-texture)
- Export sang Procreate
- Tô texture trong Procreate
- Export trở lại Nomad để render
:::

Đó là phần tổng quan, giờ hãy khám phá các mục trong menu tô màu:


## Tô theo nét (Stroke painting)
![](/images/paint_intensity.webp)  

Bật tô màu cho công cụ này, hữu ích nếu bạn cần điêu khắc và tô màu cùng lúc.

Với các công cụ mà tô màu là chức năng chính (ví dụ Paint, Smudge, Mask), checkbox này sẽ không xuất hiện.

### Cường độ tô màu (Paint intensity)

Thanh trượt cho phép bạn dùng cường độ tô màu khác với cường độ chính của công cụ.

Các checkbox `Alpha`, `Falloff` và `Randomize` quyết định liệu các tính năng đó có ảnh hưởng đến tô màu hay không. Ví dụ bạn có thể bật randomize cho công cụ clay, nhưng màu sắc sẽ không bị random.

## Chất liệu (Material)
![](/images/paint_material.webp) 

Biểu tượng đầu tiên là hình xem trước chất liệu. Kéo trên hình xem trước 3D sẽ xoay nó. 

Biểu tượng thứ hai là xem trước nét sơn với alpha và falloff đã chọn.

Nút xem trước cạnh tiêu đề Material cho phép bạn chuyển giữa none, Material hoặc Triplanar. Điều này quyết định điều gì sẽ xảy ra khi bạn thay đổi thuộc tính sơn một cách tương tác:

* `None` - Không hiển thị xem trước trên mô hình khi bạn chỉnh thuộc tính
* `Material` - Giá trị chất liệu sẽ được xem trước trên đối tượng khi bạn chỉnh. Nếu bạn dùng texture và mô hình có UV, UV sẽ được sử dụng.
* `Triplanar` - Chất liệu sẽ được xem trước dưới dạng chiếu Triplanar. 

Ống nhỏ giọt có thể dùng để lấy mẫu tất cả thuộc tính từ một đối tượng trong cảnh của bạn.

## Preset chất liệu (Material Presets)
Chạm vào hình xem trước 3D sẽ mở menu preset chất liệu, bạn có thể clone chúng để tạo preset riêng.

![](/images/paint_presets.webp) 

Khi bật, các công tắc `Embed Textures` và `Alpha` sẽ lưu mọi texture được chất liệu này sử dụng bên trong preset. Điều này được giải thích kỹ hơn bên dưới.

## Thanh trượt PBR
![](/images/paint_sliders.webp) 

Tô màu [PBR](shading.md#pbr) sử dụng 4 kênh:
- `Color` Màu sẽ được tô. Ống nhỏ giọt có thể dùng để chọn màu từ phần khác của mô hình, hoặc từ ảnh tham chiếu.
- `Roughness` Cho biết bề mặt "nhám" hay "mịn". Giá trị roughness thấp nghĩa là phản xạ sẽ sắc nét.
- `Metalness` Cho biết bề mặt có phải kim loại hay không. Giá trị hầu hết nên là 0% hoặc 100%, giá trị ở giữa chỉ nên dùng trong trường hợp đặc biệt.
- `Opacity` Mức độ có thể nhìn xuyên qua chất liệu. Về mặt lý thuyết nó không thuộc đặc tả PBR, nhưng rất hữu ích trong nhiều tình huống. 1 là hoàn toàn đục, 0 là trong suốt. Lưu ý độ mờ (opacity) và khúc xạ (refraction) là hai thứ khác nhau, khúc xạ trong Nomad được xử lý qua chất liệu refraction. 

Nếu bạn chọn một preset chất liệu, 3 kênh sẽ được tô đồng thời (opacity thường cố ý bị loại trừ). Điều này có nghĩa là thay vì chỉ tô "màu đỏ", bạn có thể đang tô "một kim loại đỏ nhám" hoặc "một nhựa trắng mịn".

Ô vuông là một ô texture, nhấn vào để dùng texture cho thuộc tính đó thay vì một giá trị đơn sắc.

Biểu tượng cây cọ cạnh các thanh trượt sẽ tô tràn (flood fill) thuộc tính đó lên toàn bộ đối tượng.

Checkbox sẽ bật/tắt thuộc tính cụ thể đó, vì vậy bạn có thể chỉ tô màu, hoặc chỉ tô roughness và opacity, chẳng hạn. 

Dưới đây là một số ví dụ về các thuộc tính roughness và metalness khác nhau:

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Chỉ màu sắc được hỗ trợ trong chế độ [Matcap rendering](shading.md#matcap), metalness và roughness sẽ bị bỏ qua.
:::

::: tip
Khi dùng texture cho tô màu PBR, thường hữu ích nếu chuyển sang công cụ như `Stamp`, hoặc dùng menu stroke để chọn chế độ khác dot, vì dot có thể làm nhòe texture.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Bạn có thể cân nhắc bật `Smooth Shading` [toàn cục](settings.md#smooth-shading) hoặc [theo từng đối tượng](material.md#smooth-shading) nếu bạn đang tô bề mặt kim loại trên một đối tượng có số lượng polygon thấp.
:::

## Tô toàn bộ (Paint all)

![](/images/paint_paint_all.webp)

Áp dụng chất liệu hiện tại lên đối tượng, hoặc ở chế độ tiêu chuẩn với 'Paint All', hoặc dưới dạng chiếu Triplanar.

Các checkbox cạnh thanh trượt color/metalness/roughness/opacity sẽ được tôn trọng, mọi thuộc tính bị tắt sẽ không được tô.

Các nút bổ sung điều khiển cách Paint All có thể bị ảnh hưởng thêm:

| Icon                        | Mô tả                                         |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/tool_mask.webp) | Vùng bị mask sẽ không bị ảnh hưởng.          |
| ![](/icons/tool_hide.webp) | Vùng bị ẩn sẽ không bị ảnh hưởng.            |
| ![](/icons/opacity.webp)   | Dùng hệ số tô màu của công cụ phía trên.     |
| ![](/icons/layer.webp)     | Vùng chưa tô của một layer sẽ không bị ảnh hưởng. |
| ![](/icons/triplanar.webp) | Chỉ báo thiết lập triplanar                   |
| ![](/icons/cog.webp)       | Mở thiết lập Triplanar                        |

### Thiết lập Triplanar
![](/images/paint_triplanar_settings.webp)

Tương tự [thiết lập triplanar trong menu material](material.md#triplanar), bạn có thể điều khiển độ hòa trộn giữa các phép chiếu, độ lặp (tiling) và độ lệch (offset). 

Dùng checkbox preview ở đầu menu này để bật xem trước liên tục trong khi chỉnh giá trị.

## Chất liệu toàn cục (Global material)
Nếu tùy chọn này được bật, chất liệu đã chọn sẽ giống nhau cho các công cụ khác. Lưu ý nó chỉ tính đến thiết lập roughness, metalness và color.
