# ![](/icons/postprocess.webp) Hậu kỳ (Post process) 

Menu này điều khiển nhiều khía cạnh của Nomad để ảnh hưởng đến diện mạo của bản render.

![](/images/postprocess_overview_drac.webp)

Việc dùng hậu kỳ có thể thay đổi đáng kể diện mạo cuối cùng của cảnh.

![](/images/postprocess_overview.webp)
*Cùng một cảnh trước và sau khi hậu kỳ, không thêm đèn hay thay đổi vật liệu.*

Hậu kỳ có thể ảnh hưởng rất nhiều đến hiệu năng tùy theo thiết bị của bạn.
Có một ô chọn (checkbox) toàn cục để tắt toàn bộ hậu kỳ, giúp bạn nhanh chóng quay lại điêu khắc/mô hình mà không mất các thiết lập sẵn.
Đối với render PBR, nên bật [Ambient Occlusion](#ambient-occlusion-ssao), [Reflection](#reflection-ssr) và [Tone Mapping](#tone-mapping).

Tuy nhiên, hầu hết thời gian bạn sẽ muốn tắt hậu kỳ khi đang điêu khắc, để tập trung vào hình khối của bản render.

## Chất lượng (Quality)

![](/images/postprocess_quality.webp)
### Lấy mẫu khung hình tối đa (Max frame sampling)
Nomad sẽ tính toán một lượng hiệu ứng hậu kỳ nhất định cho một khung hình đơn, điều này có thể trông nhiễu. Điều khiển này xác định có bao nhiêu khung hình sẽ được render rồi trộn lại với nhau để loại bỏ phần lớn nhiễu. Một số hiệu ứng không cần thêm mẫu (ví dụ color grading), trong khi các hiệu ứng khác như global illumination có thể cần hàng trăm mẫu để hết nhiễu. 

Trong viewport, điều này có thể thấy khi bạn để Nomad đứng yên, chất lượng hình ảnh sẽ dần được tinh chỉnh cho đến khi đạt số mẫu tối đa rồi dừng. Số lượng tính toán này cũng được dùng trong phần render của [menu Files](files) khi nhấn 'export png'.

### Hệ số độ phân giải (Resolution multiplier)
Thanh trượt này điều khiển độ phân giải của hậu kỳ. Giá trị x1.0 nghĩa là render được thực hiện ở độ phân giải điểm ảnh của thiết bị. Giá trị x0.5 sẽ render ở nửa độ phân giải, nhanh nhưng chất lượng thấp. Giá trị lớn hơn 1 sẽ render ở kích thước lớn hơn rồi thu nhỏ xuống. Điều này cho chất lượng cao hơn, ít nhiễu hơn nhưng thời gian render lâu hơn.

### Số mẫu tối đa (Max samples)

Tùy chọn này sẽ tăng chất lượng hậu kỳ, nhưng nhìn chung `Full resolution` sẽ có tác động nhiều hơn. 

### Full resolution
Khi bật sẽ buộc hệ số độ phân giải về x1.0

### Denoiser (oidn)

Áp dụng bộ khử nhiễu cho hình ảnh. Điều này cho phép bạn dùng số mẫu thấp hơn nhiều. Tùy chọn này chỉ hoạt động nếu `Full Resolution` được bật. Lưu ý việc khử nhiễu diễn ra sau khi tất cả mẫu đã được tính toán, và có thể tốn tài nguyên xử lý.

## Trình duyệt preset (Preset browser)
![](/images/postprocess_presets.webp)
Nhấn vào hình sẽ hiển thị một bộ sưu tập preset hậu kỳ. Để tạo preset riêng, chọn một preset, nhấn 'clone', rồi chỉnh sửa. Để lưu, nhấn vào hình preset, nhấn lần nữa trong trình duyệt preset và chọn 'save'.

## Reflection (SSR)
Với tùy chọn này, các đối tượng có thể phản chiếu những đối tượng khác trong cảnh, miễn là các đối tượng đó hiển thị trên màn hình.
Nếu bạn có các vật thể kim loại và bóng trong cảnh, thì nên dùng tùy chọn này.
Tùy chọn này chỉ hiệu quả với chế độ PBR.

| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## Global Illumination (SSGI)

Global illumination mô phỏng cách ánh sáng dội giữa các bề mặt, ví dụ một bức tường đỏ sẽ hắt đỏ lên một vật thể trắng gần đó. Điều này có thể tăng mạnh tính chân thực của bản render khi dùng cùng ambient occlusion và reflection. 

`Strength` - Cường độ của global illumination. 

| SSGI off                     | SSGI on                    |
| :--------------------------: | :------------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Một spotlight ở phía sau hình cầu, chiếu lên trần. Khi tắt SSGI, chỉ có trần được chiếu sáng. Khi bật SSGI, ánh sáng dội từ trần xuống tường rồi tới hình cầu._

## Ambient Occlusion (SSAO)
Ambient occlusion sẽ làm tối các vùng mà ánh sáng khó tiếp cận (góc cạnh, khe, v.v.).
Hiệu ứng này chỉ phụ thuộc vào hình học của mô hình.

* `Strength` - Cường độ hiệu ứng.
* `Size` - Độ lan rộng của hiệu ứng.
* `Curvature bias` - Độ nhạy của hiệu ứng so với biến thiên bề mặt.
* `Color` - Màu pha vào vùng tối, dùng cho các hiệu ứng sáng tạo.

| SSAO off                     | SSAO on                     |
| :--------------------------: | :-------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO sẽ thấy rõ nhất ở những vùng chủ yếu được chiếu sáng bởi ánh sáng môi trường. Những vùng dưới nguồn sáng trực tiếp mạnh sẽ nhận hiệu ứng AO yếu hơn nhiều.

:::

## Depth of Field (DOF)
Thêm hiệu ứng nhòe cho vùng nằm ngoài điểm lấy nét.

Chỉ cần chạm vào mô hình để thay đổi điểm lấy nét.

* `Far blur` - Lượng nhòe áp dụng cho vùng phía sau điểm lấy nét.
* `Near blur` - Lượng nhòe áp dụng cho vùng giữa điểm lấy nét và camera.

| DOF off                    | DOF focus on far ring       | DOF focus on close ring    |
| :------------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |

## Bloom
Bloom sẽ làm các vùng sáng trong cảnh phát sáng (glow).

* `Intensity` - Cường độ hiệu ứng.
* `Radius` - Độ lan của hiệu ứng.
* `Threshold` - Độ sáng tối thiểu của điểm ảnh trong cảnh trước khi bắt đầu bloom. Đặt thấp sẽ khiến mọi thứ đều bloom, đặt cao sẽ chỉ cho những điểm ảnh sáng nhất bloom.
* `Color` - Màu pha thêm vào bloom cho các hiệu ứng sáng tạo.

| Bloom off                     | Bloom với radius 0          | Bloom với radius 1          |
| :---------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |

## Tone Mapping
Tone Mapping là thao tác ánh xạ các giá trị HDR về khoảng `[0, 1]`.
Nếu bạn không dùng (hoặc chọn `none`), mọi thành phần màu lớn hơn 1 sẽ bị cắt ngưỡng (clipped).
Mọi biến thiên màu sắc trên khoảng này sẽ bị mất.

* `None/Neutral/Agx/ACES` - chọn bộ tone mapper. `None` không ánh xạ lại (nhưng các điều khiển khác vẫn hoạt động). Các tùy chọn còn lại giống như chọn loại phim khác nhau, chúng xử lý vùng cháy sáng và màu sắc theo những cách khác nhau. Đây là chủ đề rất sâu, hãy tìm thêm về tone mapping, Agx, ACES để biết thêm!
* `Exposure` - Độ sáng tổng thể của hình, tương tự chỉnh khẩu độ trên máy ảnh. Đây là cách nhanh để làm sáng hoặc tối toàn bộ hình.
* `Saturation` - Độ đậm màu. 1 là trung tính, 0 là đơn sắc, lớn hơn 1 là tăng bão hòa.
* `Contrast` - Làm vùng tối tối hơn và vùng sáng sáng hơn. Dùng cẩn thận, giá trị cao có thể gây lỗi hình (artifact).

Lưu ý khi tắt `Tone Mapping`, một số chi tiết biến mất vì điểm ảnh quá sáng.

| Tone Mapping off             | Tone Mapping on             |
| :--------------------------: | :-------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Tone mapping có thể tăng hiệu ứng của global illumination. Nếu bạn giảm cường độ bản đồ môi trường, tăng nguồn sáng chính, sau đó tăng `exposure` trong tone mapping để thấy rõ hơn hiệu ứng ánh sáng dội.
:::

## Color Grading
Tương tự công cụ Curves trong Photoshop, tính năng này cho phép bạn điều khiển cân bằng và phân bố màu trong hình. Điều khiển `main` ảnh hưởng đến cân bằng màu tổng thể, các điều khiển `red`/`green`/`blue` cho phép tinh chỉnh chi tiết. 

| Color Grading off              | Color Grading on              |
| :----------------------------: | :---------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## Curvature
Phát hiện nơi có thay đổi độ cong nhanh và áp màu lên những vùng đó.

* `Factor` - Cường độ tổng thể của hiệu ứng
* `Bump` - Mức độ phát hiện các thay đổi lồi sắc nét và đặt màu đã chọn ở đó (mặc định là trắng)
* `Cavity` - Mức độ phát hiện các thay đổi lõm và đặt màu đã chọn ở đó (mặc định là đen)

| Curvature off                     | Curvature on                    |
| :-------------------------------: | :-----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |

## Chromatic Aberration
Mô phỏng lỗi ống kính khi ánh sáng bị tách màu quanh rìa màn hình.

* `Strength` - Mức độ tách các phần đỏ/lục/lam của hình về phía rìa màn hình

| Chromatic off                  | Chromatic on                  |
| :----------------------------: | :---------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |

## Vignette
Mô phỏng lỗi ống kính bằng cách làm tối rìa màn hình.

* `Size` - Kích thước của ellipse đảo ngược đặt lên hình
* `Hardness` - Độ mờ hoặc sắc nét của ellipse khi trộn lên hình.

| Vignette off                     | Vignette on                     |
| :------------------------------: | :-----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## Grain
Thêm hiệu ứng hạt (grain), có thể giúp hình bớt cảm giác nhân tạo.

* `Strength` - Lượng hạt/nhiễu thêm vào hình.

| Grain off                     | Grain on                    |
| :---------------------------: | :-------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |

## Sharpness
Hiệu ứng làm nét tương tự trong Photoshop hoặc các ứng dụng xử lý ảnh.

* `Strength` - Lượng làm nét áp dụng lên hình.

| Sharpness off                   | Sharpness on                  |
| :-----------------------------: | :---------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## Pixel Art
Mô phỏng đồ họa pixel của game retro.

* `Slider` - Kích thước pixel
* `Allow frame sampling` - nếu bạn gặp nhiều điểm ảnh đen, hãy thử bật tùy chọn này, nó sẽ ghi đè thiết lập lấy mẫu mặc định.

| Pixel off                    | Pixel on                    |
| :--------------------------: | :-------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## Scanline
Mô phỏng diện mạo của màn hình CRT cũ.

* `Factor` - Cường độ của các đường
* `Spacing` - Kích thước các đường

| Scanline off                    | Scanline on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |

## Dithering

Rải nhiễu điểm ảnh (dither) để giảm hiện tượng banding. Thông thường nên bật, nhưng có thể tắt cho một số thao tác đặc biệt (ví dụ xuất depth map hoặc các thao tác đặc thù dữ liệu khác).
