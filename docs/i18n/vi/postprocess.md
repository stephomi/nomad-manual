# ![](/icons/postprocess.webp) Hậu kỳ {#post-process}

Menu này điều khiển nhiều khía cạnh của Nomad để thay đổi vẻ ngoài của ảnh render.

![](/images/postprocess_overview_drac.webp)

Dùng hậu kỳ có thể thay đổi đáng kể vẻ ngoài cuối cùng của cảnh.

![](/images/postprocess_overview.webp)
*Cùng một cảnh trước và sau khi áp hậu kỳ, không thêm đèn hay thay đổi vật liệu nào.*

Tùy thiết bị, hậu kỳ có thể ảnh hưởng rất nhiều đến hiệu năng.
Có một ô `Hậu kỳ` chung để tắt toàn bộ hậu kỳ, giúp bạn nhanh chóng quay lại điêu khắc/dựng hình mà không mất các thiết lập sẵn.
Với kết xuất PBR, bạn nên bật [Tắc sáng môi trường](#ambient-occlusion-ssao), [Phản chiếu](#reflection-ssr) và [Ánh xạ sắc độ](#tone-mapping).

Tuy vậy, phần lớn thời gian bạn sẽ muốn tắt hậu kỳ khi đang điêu khắc, để tập trung vào chính hình khối thay vì phần hiển thị.


## Chất lượng {#quality}

![](/images/postprocess_quality.webp)

Các tùy chọn này cải thiện chất lượng ảnh render, đổi lại là hiệu năng.

### Lấy mẫu khung tối đa {#max-frame-sampling}
Với mỗi khung hình, Nomad chỉ tính một phần hậu kỳ, nên ảnh có thể trông bị nhiễu. Tùy chọn này quyết định số khung hình được render rồi trộn lại với nhau để loại bỏ phần lớn nhiễu. Một số hiệu ứng không cần thêm mẫu nào (ví dụ chỉnh màu), trong khi những hiệu ứng khác như bóng mềm và chiếu sáng toàn cục có thể cần hàng trăm mẫu mới hết nhiễu.

Trong khung nhìn, bạn sẽ thấy điều này mỗi khi để yên Nomad: chất lượng ảnh dần được tinh chỉnh cho đến khi đạt số mẫu tối đa, rồi dừng lại. Khi đã dừng, Nomad không làm gì nữa, giúp tiết kiệm pin. Số lần tính toán này cũng được dùng trong phần kết xuất của [menu Tệp tin](files) khi bạn nhấn 'export png'.

Ô đánh dấu cạnh thanh trượt bật hoặc tắt việc lấy mẫu khung hình.

### Độ phân giải render {#resolution-multiplier}
Thanh trượt này điều khiển độ phân giải của ảnh render. Giá trị x1.0 nghĩa là render ở đúng độ phân giải điểm ảnh của thiết bị. Giá trị x0.5 sẽ render ở một nửa độ phân giải, nhanh nhưng chất lượng thấp. Giá trị lớn hơn 1 sẽ render ở kích thước lớn hơn rồi thu nhỏ lại, cho chất lượng cao hơn, ít nhiễu hơn, nhưng thời gian render lâu hơn.

Nó ảnh hưởng rất lớn đến hiệu năng, vì vậy hãy cố giữ ở mức x1.25 trở xuống. Giá trị này không được lưu trong cài đặt, và hiệu ứng [Nghệ thuật pixel](#pixel-art) sẽ ghi đè lên nó.

### ![](/icons/intensity.webp) Mẫu tối đa {#max-samples}

Cải thiện chất lượng các hiệu ứng hậu kỳ, đổi lại là hiệu năng.

### ![](/icons/material_dithering.webp) Dithering {#dithering}

Rải nhiễu điểm ảnh để giảm hiện tượng phân dải màu (trong các dải chuyển màu hay hiệu ứng tối góc chẳng hạn). Thường thì nên bật, nhưng có thể tắt cho những thao tác đặc thù (ví dụ xuất bản đồ độ sâu hay các thao tác xử lý dữ liệu khác).

### ![](/icons/denoise.webp) Bộ lọc khử nhiễu (oidn) {#oidn}

Áp bộ khử nhiễu lên ảnh khi đã tích lũy đủ mọi khung hình. Nhờ vậy bạn có thể dùng số mẫu thấp hơn nhiều. Khử nhiễu tốn nhiều sức xử lý, nên chỉ bật khi ảnh của bạn bị nhiễu. Tính năng này không có trên mọi thiết bị.

## Trình duyệt thiết lập sẵn {#preset-browser}
![](/images/postprocess_presets.webp)
Nhấn vào hình ảnh bên dưới tiêu đề `Hậu kỳ` sẽ hiện một bộ sưu tập các thiết lập sẵn cho hậu kỳ. Dùng `Mới` để tạo một thiết lập sẵn từ cài đặt hiện tại. Các thiết lập sẵn có sẵn chỉ có thể nhân bản: để tạo thiết lập của riêng bạn, hãy chọn một mẫu, nhấn `Nhân bản` rồi chỉnh sửa. Khi một thiết lập sẵn có thay đổi chưa được lưu, nó hiện `Thay đổi chưa lưu!`; để lưu, nhấn vào hình ảnh thiết lập sẵn, nhấn thêm lần nữa bên trong trình duyệt thiết lập sẵn, rồi chọn `Lưu`.

## Thanh lối tắt {#shortcut-bar}
Khi hậu kỳ được bật, một thanh ở cuối menu liệt kê mọi hiệu ứng (`SSR`, `SSGI`, `SSAO`, `DoF`, `Hiệu ứng Bloom`...). Chạm vào một hiệu ứng để nhảy đến phần của nó. Các hiệu ứng đang tắt sẽ bị làm mờ, nên thanh này cũng là bản tóm tắt nhanh những gì thiết lập sẵn hiện tại đang làm.

## ![](/icons/postprocess_ssr.webp) Phản chiếu (SSR) {#reflection-ssr}
Với tùy chọn này, các đối tượng có thể phản chiếu những đối tượng khác trong cảnh, miễn là chúng đang hiển thị trên màn hình.
Nếu cảnh của bạn có các vật thể kim loại và bóng loáng, có lẽ bạn nên dùng tùy chọn này.
Tùy chọn này cần chế độ tô bóng [Chiếu sáng (PBR)](shading.md#pbr).


| Tắt SSR                    | Bật SSR                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Chiếu sáng toàn cầu (SSGI) {#global-illumination-ssgi}

Chiếu sáng toàn cục mô phỏng cách ánh sáng nảy qua lại giữa các bề mặt, chẳng hạn một bức tường đỏ sẽ hắt sắc đỏ lên vật thể màu trắng ở gần. Khi dùng cùng tắc sáng môi trường và phản chiếu, nó có thể tăng đáng kể độ chân thực của ảnh render. Giống như phản chiếu, nó cần chế độ tô bóng [Chiếu sáng (PBR)](shading.md#pbr).

`Độ mạnh` - Cường độ của chiếu sáng toàn cục.



| Tắt SSGI                   | Bật SSGI                  |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Một đèn rọi đặt sau quả cầu, chiếu lên trần nhà. Khi tắt SSGI, chỉ trần nhà được chiếu sáng. Khi bật SSGI, ánh sáng nảy từ trần xuống các bức tường rồi đến quả cầu._

## ![](/icons/postprocess_ssao.webp) Tắc sáng môi trường (SSAO) {#ambient-occlusion-ssao}
Tắc sáng môi trường làm tối những vùng mà ánh sáng khó chạm tới (các góc khuất, v.v.).
Hiệu ứng chỉ phụ thuộc vào hình học của mô hình.

* `Độ mạnh` - Cường độ của hiệu ứng.
* `Kích thước` - Phạm vi lan rộng của hiệu ứng.
* `Độ dày` - Độ dày theo chiều sâu được giả định cho các vật che khuất, tính theo phần trăm của `Kích thước`.
* `Màu phủ` - Một màu được nhân vào vùng tắc sáng, dùng cho các hiệu ứng sáng tạo.


| Tắt SSAO                    | Bật SSAO                   |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO thấy rõ nhất ở những vùng được chiếu chủ yếu bằng ánh sáng môi trường. Những vùng chịu ánh sáng trực tiếp mạnh sẽ nhận hiệu ứng AO yếu hơn nhiều.

:::

## ![](/icons/postprocess_dof.webp) Chiều sâu trường ảnh {#depth-of-field-dof}
Thêm hiệu ứng nhòe cho vùng nằm ngoài tiêu điểm.

Chỉ cần chạm vào mô hình để đổi điểm lấy nét.

* `Chế độ khẩu độ` - Điều khiển độ nhòe bằng một khẩu độ camera duy nhất, thay vì hai thanh trượt độ nhòe bên dưới.
* `Khẩu độ` (_chỉ ở chế độ khẩu độ_) - Số f của ống kính, như trên một chiếc máy ảnh thật. Giá trị thấp hơn sẽ mở ống kính rộng hơn và nhòe nhiều hơn.
* `Mờ xa` - Mức độ nhòe áp cho phía xa của điểm lấy nét.
* `Mờ gần` - Mức độ nhòe áp cho khoảng giữa điểm lấy nét và camera.


| Tắt DOF                   | DOF lấy nét vòng xa         | DOF lấy nét vòng gần       |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Hiệu ứng Bloom {#bloom}
Bloom làm các vùng sáng trong cảnh tỏa sáng rực rỡ.

* `Cường độ` - độ mạnh của hiệu ứng.
* `Bán kính` - độ lan tỏa của hiệu ứng.
* `Ngưỡng` - Điểm ảnh trong cảnh phải sáng đến mức nào thì mới bắt đầu tỏa sáng. Ở mức 0 mọi thứ đều tỏa sáng, đặt cao thì chỉ những điểm ảnh sáng nhất mới tỏa sáng.
* `Màu phủ` - một màu có thể thêm vào bloom cho các hiệu ứng sáng tạo.

| Tắt Bloom                    | Bloom bán kính 0            | Bloom bán kính 1            |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Ánh xạ sắc độ {#tone-mapping}
Ánh xạ sắc độ là phép biến đổi đưa các giá trị HDR về khoảng `[0, 1]`.
Nếu bạn không dùng nó (hoặc chọn `Không có`), mọi thành phần màu lớn hơn 1 sẽ bị cắt bỏ.
Mọi biến đổi màu vượt quá khoảng này sẽ bị mất.

* `Không có/Trung tính/Agx/ACES` - bộ ánh xạ sắc độ được dùng. `Không có` không ánh xạ lại gì (nhưng các điều khiển khác vẫn hoạt động). Các lựa chọn còn lại giống như chọn những loại phim khác nhau, chúng xử lý các giá trị và màu sắc bị cháy sáng theo những cách khác nhau. Đây là một chủ đề rất sâu, hãy tìm hiểu thêm về tone mapping, Agx, ACES nếu bạn muốn biết nhiều hơn!
* `Phơi sáng` - độ sáng tổng thể của ảnh, giống như chỉnh khẩu độ trên máy ảnh. Đây là cách nhanh để làm sáng hoặc tối toàn bộ ảnh.
* `Bão hòa` - độ đậm của màu. 1 là trung tính, 0 là đơn sắc, giá trị trên 1 cho màu ngày càng rực.
* `Tương phản` - Làm vùng tối tối hơn và vùng sáng sáng hơn. Hãy dùng cẩn thận, giá trị cao có thể gây lỗi hiển thị.

Hãy để ý rằng khi tắt `Ánh xạ sắc độ`, một số chi tiết biến mất vì các điểm ảnh quá sáng.

| Tắt ánh xạ sắc độ           | Bật ánh xạ sắc độ          |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Ánh xạ sắc độ có thể làm nổi bật hiệu ứng chiếu sáng toàn cục. Nếu bạn giảm cường độ của bản đồ môi trường, tăng nguồn sáng chính, bạn có thể tăng `Phơi sáng` của ánh xạ sắc độ để thấy rõ hơn hiệu ứng ánh sáng nảy.
:::

## ![](/icons/postprocess_tone_curve.webp) Chỉnh màu {#color-grading}
Tương tự công cụ Curves trong Photoshop, tính năng này cho phép bạn điều khiển sự cân bằng và phân bố màu trong ảnh. Điều khiển `Chính` tác động lên toàn bộ cân bằng màu, còn các điều khiển `Đỏ`/`Xanh lá`/`Xanh dương` cho phép tinh chỉnh chi tiết.

| Tắt chỉnh màu                 | Bật chỉnh màu                |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Độ cong {#curvature}
Phát hiện những nơi độ cong thay đổi đột ngột, và tô một màu lên các vùng đó.

* `Yếu tố` - cường độ tổng thể của hiệu ứng
* `Lồi` - mức độ phát hiện các thay đổi lồi sắc nét, và tô màu đã chọn lên đó (mặc định là trắng)
* `Khoang` - mức độ phát hiện các thay đổi lõm, và tô màu đã chọn lên đó (mặc định là đen)
* `Độ dày` - độ rộng của các cạnh được phát hiện.

Cạnh `Lồi` và `Khoang`, một ô màu dùng để chọn màu, và một nút nhỏ chọn cách màu đó hòa trộn với ảnh.


| Tắt độ cong                      | Bật độ cong                    |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Sai sắc {#chromatic-aberration}
Mô phỏng lỗi ống kính khi ánh sáng bị tách màu ở các mép màn hình.

* `Độ mạnh` - mức độ các thành phần đỏ/xanh lá/xanh dương của ảnh bị tách ra về phía mép màn hình

| Tắt sai sắc                   | Bật sai sắc                  |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Tối góc {#vignette}
Mô phỏng lỗi ống kính bằng cách làm tối các mép màn hình.

* `Kích thước` - Kích thước của một hình elip đảo ngược phủ lên ảnh
* `Độ cứng` - Hình elip hòa lên ảnh nhòe hay sắc nét đến mức nào.
* `Màu phủ` - Màu của hiệu ứng tối góc, mặc định là đen.


| Tắt tối góc                     | Bật tối góc                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Nhiễu {#grain}
Thêm hiệu ứng hạt nhiễu, giúp ảnh trông bớt giả tạo một chút.

* `Cường độ` - lượng hạt/nhiễu thêm vào ảnh.


| Tắt nhiễu                    | Bật nhiễu                  |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Độ nét {#sharpness}
Hiệu ứng làm sắc nét giống như trong Photoshop hay các ứng dụng xử lý ảnh.

* `Độ mạnh` - mức làm sắc nét áp cho ảnh.


| Tắt độ nét                     | Bật độ nét                   |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Nghệ thuật pixel {#pixel-art}
Mô phỏng phong cách pixel art của game cổ điển. Hiệu ứng này ghi đè lên [Độ phân giải render](#resolution-multiplier).

* `Thanh trượt` - kích thước của điểm ảnh
* `Cho phép lấy mẫu khung hình` - nếu bạn thấy nhiều điểm ảnh đen, hãy thử bật tùy chọn này. Khi tắt, hiệu ứng pixel art sẽ tắt [lấy mẫu khung hình](#max-frame-sampling).

| Tắt pixel                   | Bật pixel                  |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Đường quét {#scanline}
Mô phỏng vẻ ngoài của màn hình CRT đời cũ.

* `Yếu tố` - độ đậm của các đường
* `Khoảng cách` - kích thước của các đường

| Tắt đường quét                 | Bật đường quét                |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |
