# ![](/icons/operation.webp) Hoạt động {#operation}

Menu này áp một thao tác lên toàn bộ bề mặt của các đối tượng được chọn cùng lúc: làm mịn, thư giãn, đánh bóng, bơm phồng, chỉnh màu, làm mờ hoặc làm sắc phần vẽ và mặt nạ.

![](/images/operation_overview.webp)

## Tổng quan {#overview}

Cọ chỉ tác động ở nơi bạn vẽ nét, còn một thao tác ở đây tác động lên mọi đỉnh của các đối tượng được chọn trong một lần. Tiêu đề hiển thị tên của đối tượng, hoặc số lượng đối tượng khi bạn chọn nhiều cái.

Mỗi thao tác là một thanh trượt: kéo sang phải để áp nhiều hơn, sang trái để áp ít hơn (hoặc áp thao tác ngược lại, với những thanh trượt có mũi tên ở cả hai bên). Thanh trượt trở về 0 khi bạn thả tay, và mỗi lần kéo là một bước trong [Lịch sử](history.md), nên bạn có thể áp một thao tác nhiều lần với liều lượng nhỏ.

::: tip
Các thao tác này là cách nhanh để dọn dẹp toàn bộ lưới sau khi remesh voxel hay boolean: một chút `Thư giãn` giúp các tam giác đều đặn hơn, một chút `Làm mịn` xóa đi nhiễu, mà không phải dò từng chỗ bằng cọ.
:::

## Bộ lọc {#filters}

Các nút ở trên cùng giới hạn nơi các thao tác được áp dụng:

* `Mặt nạ` - Các vùng bị che mặt nạ được giữ nguyên.
* `Ẩn` - Các vùng bị ẩn được giữ nguyên.
* `Độ lệch` - (Khi đang chọn một [lớp](layers.md)) Chỉ những vùng mà lớp đang hoạt động có chứa phần điêu khắc mới bị ảnh hưởng, nhờ vậy bạn có thể làm mịn hay bơm phồng nội dung của một lớp mà không động đến phần còn lại.

## Làm mịn {#smoothing}

* `Bảo toàn thể tích` - Làm mịn mà không làm bề mặt co lại. Nút bánh răng chứa các lượng `Thu nhỏ` và `Bơm phồng` được dùng cho nó.
* `Bảo vệ đường viền` - Các đỉnh nằm trên biên của lưới (mép của một lỗ) được giữ yên.
* `Làm mịn ổn định` - Cố gắng làm cho việc làm mịn không phụ thuộc vào tô pô. Nó hoạt động tốt nhất khi mật độ đa giác thay đổi nhiều.
* `Làm mịn` - Làm mịn bề mặt. Kéo sang trái để `Làm sắc` thay vào đó.
* ![](/icons/group.webp) `Làm mịn` - Làm mịn đường biên giữa các [nhóm mặt](tools.md#facegroup), làm thẳng những đường viền nhóm bị răng cưa. Kéo sang trái để làm sắc chúng.
* `Thư giãn` - Làm các đa giác đều đặn hơn, giữ nguyên hình dạng.
* ![](/icons/group.webp) `Thư giãn` - Thư giãn các đa giác dọc theo đường biên của nhóm mặt.
* `Giữ góc` - Với `Làm mịn` và `Thư giãn` theo nhóm mặt, các đường biên được giữ cố định ở những chỗ chúng gấp khúc lớn hơn góc này, nhờ vậy các góc vẫn sắc nét trong khi các cạnh được làm mịn. Dùng ô đánh dấu của nó để bật.

## Đánh bóng {#polish}

Làm phẳng bề mặt thành các mặt vát gọn gàng, giống công cụ [Đánh bóng](tools.md#polish). `Góc` quyết định những mặt nào được làm phẳng cùng nhau: các mặt gấp ít hơn góc này sẽ trở thành một mặt vát. Góc thấp hơn giữ được nhiều nếp gấp và các mặt vát nhỏ hơn.

## Bơm phồng {#inflate}

Đẩy bề mặt ra ngoài theo pháp tuyến, hoặc vào trong khi bạn kéo sang trái. `Pháp tuyến (Thư giãn)` đồng thời thư giãn các đa giác để chúng không bị kéo giãn; dùng ô đánh dấu của nó để tắt.

## Chỉnh màu {#color-adjustments}

Chọn kênh cần chỉnh: `Màu sắc`, `Độ nhám`, `Độ kim loại`, `Độ mờ`, `Mật Độ` (phần vẽ mật độ của [Quad Remesher](tools.md#quad-remesher), khi đối tượng có) hoặc `Mặt nạ`, rồi:

* `Phơi sáng` - Làm sáng hoặc tối các giá trị.
* `Bão hòa` - (chỉ với `Màu sắc`) Màu rực hơn hoặc nhạt hơn.
* `Tương phản` - Kéo các giá trị ra xa nhau, hoặc dồn chúng lại gần nhau.
* `Sắc độ` - Dịch chuyển màu quanh bánh xe màu.

## Làm mờ {#blur}

Làm nhòe các kênh được chọn trên khắp bề mặt: bật `Màu sắc`, `Độ nhám`, `Độ kim loại`, `Độ mờ`, `Mật Độ` hoặc `Mặt nạ`, rồi kéo `Làm mờ`. Kéo sang trái để `Làm sắc` thay vào đó.

Với mặt nạ, đây cũng chính là thanh trượt `Làm mờ` của công cụ [Mặt nạ](tools.md#mask). Ở đây bạn có thể làm nhòe cả các kênh vẽ.
