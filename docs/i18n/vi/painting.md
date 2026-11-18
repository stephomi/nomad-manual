# ![](/icons/paint.webp) Sơn {#painting}

Điều khiển màu, độ nhám, độ kim loại của nét vẽ, cho phép tô tràn các thuộc tính vẽ, và quyết định cách công cụ vẽ tương tác với lớp, mặt nạ và vùng bị ẩn.

![](/images/paint_overview.webp)  

## Tổng quan {#overview}

Nomad dùng phương pháp vẽ đỉnh PBR. Điều đó có nghĩa là gì?

### PBR {#pbr}
PBR, hay Physically Based Rendering (kết xuất dựa trên vật lý), là một kỹ thuật đồ họa máy tính phổ biến trong điện ảnh, truyền hình, game và thiết bị di động. Bằng cách dựa ánh sáng trên các thuộc tính vật lý, và mô tả bề mặt qua màu sắc, độ nhám và độ kim loại, bạn có thể đạt được rất nhiều vẻ ngoài chân thực như ảnh chụp.

### Vẽ đỉnh {#vertex-painting}

Vẽ đỉnh nghĩa là thông tin vẽ được lưu trong các đỉnh của mô hình, thay vì trong kết cấu. Vì Nomad xử lý được những mô hình có hàng trăm nghìn, thường là hàng triệu đỉnh, mô hình của bạn có thể mang lớp vẽ bề mặt rất chi tiết: nếu bạn điêu khắc được chi tiết nào, bạn cũng vẽ được chi tiết đó.

Điều này cũng có nghĩa là vẽ trong Nomad không cần UV, một quy trình thường chậm và nặng về kỹ thuật trong các ứng dụng 3d khác. Nhiều ứng dụng 3d khác không xử lý được số đỉnh lớn như Nomad, nhưng Nomad cũng có các công cụ bake kết cấu và tinh giảm tốt để hỗ trợ.

### Kết cấu {#texturing}

Nomad hỗ trợ kết cấu (texture), nhưng chúng phải có sẵn trong một mô hình được nhập vào, hoặc được tạo bằng cách bake phần vẽ đỉnh thành kết cấu.

Kết cấu đơn giản là một hình ảnh, nhưng trong bối cảnh 3d, nó thường chỉ một hình ảnh được gán cho một đối tượng.
Để bọc một hình ảnh quanh mô hình, mô hình cần có tọa độ kết cấu (UV).

Nomad có thể [tự động tính toán chúng](topology.md#uv-unwrap) nhưng bạn không kiểm soát được nhiều về chất lượng tổng thể.

::: tip
Một ví dụ về quy trình làm việc:
- Điêu khắc trong Nomad, rồi [Unwrap UV](topology.md#uv-unwrap)
- Nếu bạn đã bắt đầu vẽ trong Nomad, bạn có thể [chuyển phần vẽ đỉnh sang kết cấu](topology.md#bake-texture)
- Xuất sang Procreate
- Vẽ kết cấu trong Procreate
- Xuất ngược về Nomad để render
:::

Đó là phần tổng quan, giờ hãy cùng khám phá các phần của menu Sơn:


## Vẽ nét {#stroke-painting}
![](/images/paint_intensity.webp)  

Bật tính năng vẽ cho công cụ này, hữu ích khi bạn cần vừa điêu khắc vừa vẽ cùng lúc. Khi một công cụ có thể vẽ nhưng ô này đang tắt, một biểu tượng cảnh báo cạnh tiêu đề sẽ nhắc bạn.

Với những công cụ mà vẽ là chức năng chính (ví dụ Vẽ, Bôi nhòe, Mặt nạ), ô này không tồn tại.

### ![](/icons/opacity.webp) Độ mạnh màu {#paint-intensity}

Một thanh trượt cho phép bạn dùng cường độ vẽ khác với cường độ chính của công cụ.

Nút thanh trượt bên cạnh thêm một thanh trượt độ mạnh màu nhanh vào thanh bên, dành cho những công cụ vừa điêu khắc vừa vẽ.

Các nút `Alpha`, `Giảm dần` và `Ngẫu nhiên hóa cường độ` quyết định các tính năng đó có ảnh hưởng đến việc vẽ hay không. Ví dụ, bạn có thể bật ngẫu nhiên cho công cụ Đất sét, nhưng màu thì không bị ngẫu nhiên hóa.

* `Alpha` - khi tắt, phần vẽ bỏ qua alpha và phủ toàn bộ vùng cọ. Với công cụ VDM, nút này được thay bằng `Vật liệu con dấu`, dùng để bật hoặc tắt vật liệu lưu trong con dấu.
* `Giảm dần` - khi tắt, phần vẽ giữ nguyên cường độ tối đa cho đến tận mép cọ.
* `Ngẫu nhiên hóa cường độ` - phần cường độ của bộ ngẫu nhiên hóa nét vẽ có ảnh hưởng đến việc vẽ hay không. Ngẫu nhiên hóa vị trí, góc xoay và tỷ lệ thì luôn di chuyển toàn bộ con dấu.

Các tùy chọn này bị [Vẽ tất cả](#paint-all) bỏ qua, nhưng biến thể triplanar của nó vẫn dùng alpha.

### ![](/icons/link.webp) Vật liệu toàn cầu {#global-material}
Nếu bật tùy chọn này, vật liệu được chọn sẽ giống với các công cụ khác. Lưu ý rằng nó chỉ tính đến các cài đặt độ nhám, độ kim loại và màu sắc. Tắt đi để công cụ này có vật liệu riêng.


## Vật liệu {#material}
![](/images/paint_material.webp) 

Biểu tượng đầu tiên là hình xem trước vật liệu. Kéo trên bản xem trước vật liệu 3d sẽ xoay nó.

Biểu tượng thứ hai là bản xem trước nét vẽ với các tùy chọn alpha và giảm dần đã chọn.

### ![](/icons/falloff.webp) Đường cong {#curves}

Mở trình chỉnh sửa đường cong cho các ô kết cấu của [các thanh trượt PBR](#pbr-sliders). Nó ánh xạ lại giá trị kết cấu trước khi được vẽ, mà không động đến tệp ảnh. Một biểu tượng đường cong nhỏ trên ô kết cấu cho biết đường cong của nó đã được chỉnh sửa.

### ![](/icons/cog.webp) Tùy chọn vật liệu {#material-options}

Nút `Vật liệu` cạnh tiêu đề chứa hai cài đặt.

`Xem trước hiển thị vật liệu` quyết định điều gì xảy ra trên đối tượng được chọn khi bạn thay đổi các thanh trượt màu, độ nhám, độ kim loại, độ mờ đục và cường độ:

* `Không có` - Không hiển thị bản xem trước nào trên mô hình khi bạn chỉnh thuộc tính
* `Vật liệu` - Các giá trị vật liệu được xem trước trên đối tượng khi bạn chỉnh thuộc tính.
* `Triplanar` - Vật liệu được xem trước dưới dạng phép chiếu Triplanar.

Các ô đánh dấu màu, độ nhám, độ kim loại và độ mờ đục bên dưới chọn những kênh mà [Bộ chọn vật liệu](#material-picker) sẽ thay thế.

### ![](/icons/dropper.webp) Bộ chọn vật liệu {#material-picker}

Ống hút màu lấy vật liệu dưới con trỏ, từ bất kỳ đối tượng nào trong cảnh. Chỉ những kênh được đánh dấu trong [Tùy chọn vật liệu](#material-options) mới bị thay thế.

## Vật liệu thiết lập sẵn {#material-presets}
Chạm vào hình xem trước 3d sẽ mở menu các vật liệu thiết lập sẵn; bạn có thể nhân bản chúng để tạo thiết lập sẵn của riêng mình.

![](/images/paint_presets.webp) 

Nút `Nhúng kết cấu` lưu một bản sao của các kết cấu mà vật liệu này dùng vào bên trong thiết lập sẵn. Nếu không bật, thiết lập sẵn chỉ tham chiếu đến các kết cấu trong thư mục textures/ của Nomad. Hãy bật khi bạn muốn chia sẻ một thiết lập sẵn có kết cấu mà không phải gửi riêng các kết cấu của nó.

`Bao gồm Alpha` cũng lưu alpha của cọ vào vật liệu thiết lập sẵn.

## Các thanh trượt PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

Vẽ [PBR](shading.md#pbr) dùng 4 kênh:
- `Màu sắc` Màu sẽ được vẽ. Bạn có thể dùng ống hút màu để lấy màu từ những phần khác của mô hình, hoặc từ ảnh tham chiếu.
- `Độ nhám` Cho biết bề mặt "nhám" hay "mịn" đến đâu. Độ nhám thấp nghĩa là phản chiếu sẽ sắc nét.
- `Độ kim loại` Đơn giản cho biết bề mặt có phải kim loại hay không. Phần lớn thời gian giá trị nên là 0% hoặc 100%, các giá trị ở giữa chỉ nên là ngoại lệ.
- `Độ mờ` Mức độ có thể nhìn xuyên qua vật liệu. Nói chính xác thì nó không thuộc chuẩn PBR, nhưng lại hữu ích trong nhiều tình huống. 1 là đặc hoàn toàn, 0 là trong suốt. Lưu ý rằng độ mờ đục và khúc xạ là hai thứ khác nhau: khúc xạ trong Nomad được xử lý bằng vật liệu Khúc xạ.

Nếu bạn chọn một vật liệu thiết lập sẵn, 3 kênh sẽ được vẽ cùng lúc (độ mờ đục thường được cố ý loại ra). Nghĩa là thay vì chỉ vẽ 'màu đỏ', bạn có thể vẽ 'một kim loại đỏ nhám' hay 'một chất nhựa trắng mịn'.

Ô vuông là ô kết cấu: nhấn vào để dùng một kết cấu cho thuộc tính đó thay vì một giá trị cố định. Kết cấu màu sẽ nhuộm màu, còn kết cấu độ nhám, độ kim loại hay độ mờ đục thì thay thế giá trị của thanh trượt (nhãn của nó bị gạch ngang để thể hiện điều đó). Với kết cấu độ mờ đục, `Dùng Alpha làm Giá trị` đọc kênh alpha của kết cấu thay vì giá trị thang xám.

Với công cụ VDM, khi con dấu mang vật liệu riêng, một ô bổ sung hiển thị nó cạnh ô kết cấu. Chạm vào để dùng hoặc bỏ qua kênh đó của con dấu.

Biểu tượng cọ cạnh các thanh trượt sẽ tô tràn thuộc tính đó lên toàn bộ đối tượng.

Ô đánh dấu bật hoặc tắt từng thuộc tính, ví dụ bạn có thể chỉ vẽ màu, hoặc chỉ vẽ độ nhám và độ mờ đục.

Dưới đây là vài ví dụ về các mức độ nhám và độ kim loại khác nhau:

|                | Độ kim loại 0%                    | Độ kim loại 100%             |
| :------------: | :-------------------------------: | :--------------------------: |
| Độ nhám 0%     | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Độ nhám 50%    | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Độ nhám 100%   | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Độ nhám và độ kim loại cần chế độ tô bóng [Chiếu sáng (PBR)](shading.md#pbr). Ở chế độ [MatCap](shading.md#matcap) hoặc [Không sáng](shading.md#unlit), chúng bị bỏ qua và menu sẽ hiện cảnh báo.
:::

::: tip
Khi dùng kết cấu để vẽ PBR, bạn thường nên chuyển sang công cụ như `Dấu Triện`, hoặc dùng menu Nét vẽ để chọn một chế độ khác ngoài chấm, vốn có thể làm nhòe kết cấu.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Bạn có thể cân nhắc bật `Tô bóng mượt` [cho toàn bộ](settings.md#smooth-shading) hoặc [cho từng đối tượng](material.md#smooth-shading) nếu bạn vẽ bề mặt kim loại trên một đối tượng có ít đa giác.
:::

## ![](/icons/paint.webp) Vẽ tất cả {#paint-all}

![](/images/paint_paint_all.webp)

Áp vật liệu hiện tại lên các đối tượng được chọn, theo chế độ thường với `Vẽ tất cả`, hoặc dưới dạng phép chiếu Triplanar với `Vẽ tất cả + Triplanar`. Biến thể triplanar không khả dụng với những hình cơ bản chưa được hoàn tất.

Các ô đánh dấu cạnh thanh trượt màu/độ kim loại/độ nhám/độ mờ đục được tôn trọng: những thuộc tính bị tắt sẽ không được tô.

Các nút bổ sung điều khiển những yếu tố khác tác động lên Vẽ tất cả. Hầu hết hiển thị một tỷ lệ phần trăm, và bị làm mờ khi chúng không có tác dụng gì:

| Biểu tượng                  | Mô tả                                         |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | Khu vực mặt nạ sẽ không bị ảnh hưởng.         |
| ![](/icons/tool_hide.webp) | Khu vực ẩn sẽ không bị ảnh hưởng.             |
| ![](/icons/opacity.webp)   | Sử dụng hệ số vẽ công cụ ở trên.              |
| ![](/icons/layer.webp)     | Khu vực chưa sơn của một lớp sẽ không bị ảnh hưởng. |
| ![](/icons/triplanar.webp) | `Đỉnh`: biến thể triplanar còn đẩy lệch bề mặt theo alpha, với cường độ công cụ hiển thị trên nút. |
| ![](/icons/cog.webp)       | Mở cài đặt Triplanar                          |

### ![](/icons/cog.webp) Cài đặt Triplanar {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Tương tự [cài đặt triplanar trong menu Vật liệu](material.md#triplanar), bạn có thể điều khiển cách hòa trộn các phép chiếu, cách lát gạch và độ dời.

Dùng ô xem trước ở đầu menu này để bật bản xem trước liên tục trong khi chỉnh giá trị.
