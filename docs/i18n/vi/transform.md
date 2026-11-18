# ![](/icons/transform.webp) Biến Đổi {#transform}

Menu này hiển thị phép biến đổi của đối tượng được chọn dưới dạng số: nó nằm ở đâu, được xoay và co giãn thế nào, và lớn cỡ nào. Bạn có thể nhập giá trị chính xác, đặt lại chúng, hoặc bake chúng vào lưới.

![](/images/transform_overview.webp)

## Tổng quan {#overview}

Mỗi đối tượng có một nút (node) lưu vị trí, góc xoay và tỷ lệ của nó (ma trận của nó), bên cạnh các đỉnh. Các công cụ [Gizmo](tools.md#gizmo) và [Biến Đổi](tools.md#transform) thay đổi ma trận đó khi bạn kéo trong khung nhìn; menu này cho phép bạn đọc ma trận và nhập giá trị thay vì kéo. Xem [Nút và đỉnh](tools.md#nodes-and-vertices) để hiểu sự khác nhau giữa di chuyển nút và di chuyển các đỉnh.

Kéo một giá trị sang trái hoặc phải để thay đổi nó, hoặc chạm vào để nhập số. Các giá trị X, Y và Z được tô màu đỏ, xanh lá và xanh dương, giống các trục của gizmo.

::: tip
Nhập giá trị rất tiện để đặt đối tượng chính xác, ví dụ đặt nhiều bộ phận ở cùng một độ cao, hoặc đưa góc xoay về một số tròn sau khi xoay tự do bằng gizmo.
:::

## Ma trận {#matrix}

Tiêu đề cho bạn biết các giá trị đang được biểu diễn trong không gian nào: `cục bộ` (tương đối so với đối tượng cha) hay `thế giới`.

### Đối tượng và Trục {#object-pivot}

* `Đối tượng` - Các giá trị là phép biến đổi riêng của đối tượng.
* `Trục` - Các giá trị điều khiển vùng chọn từ [trục xoay](tools.md#pivot) của nó, giống như các tay cầm của gizmo: các hàng hiển thị số 0, và thay đổi chúng sẽ di chuyển, xoay hoặc co giãn vùng chọn quanh trục xoay. Bật `Chỉnh sửa` (biểu tượng ổ khóa) để chỉ di chuyển trục xoay, còn các đối tượng đứng yên.

### Cục bộ và Thế giới {#local-world}

Khi đối tượng có đối tượng cha hoặc con, hoặc khi chọn nhiều đối tượng, bạn có thể chọn không gian để hiển thị giá trị: `Cục bộ` (tương đối so với đối tượng cha) hoặc `Thế giới`.

### Thao tác {#actions}

| Thao tác      | Biểu tượng                    | Mô tả |
| :-----------: | :---------------------------: | :---------- |
| Di chuyển về gốc | ![](/icons/target.webp)    | Di chuyển đối tượng về gốc tọa độ thế giới. |
| Bake          | ![](/icons/bake.webp)        | Áp ma trận vào các đỉnh rồi đặt lại ma trận. Về mặt hình ảnh không có gì thay đổi, nhưng gốc của đối tượng giờ là gốc tọa độ thế giới. |
| Trục          | ![](/icons/gizmo.webp)       | Bake trục xoay vào đối tượng: gốc và hướng của đối tượng trở thành gốc và hướng của trục xoay. Về mặt hình ảnh không có gì thay đổi. |
| Chỉnh sửa     | ![](/icons/lock.webp)        | (Chế độ `Trục`) Chỉ di chuyển trục xoay. |
| Thiết lập lại | ![](/icons/reset.webp)       | Đặt phép biến đổi về đơn vị (không dịch, không xoay, tỷ lệ 1). Ở chế độ `Trục`, nó đưa trục xoay về lại vị trí cũ. |

Khi đối tượng được chọn có các thực thể (instance), việc bake sẽ hỏi xác nhận, kèm tùy chọn `Bỏ thực thể`: bake thay đổi các đỉnh, mà các thực thể lại dùng chung các đỉnh đó.

### Dịch chuyển, Xoay, Tỷ lệ {#translation-rotation-scale}

Vị trí, góc xoay (tính bằng độ) và tỷ lệ của đối tượng, trên X, Y và Z. Hai nút ở cuối mỗi hàng chỉ bake riêng phần đó của phép biến đổi vào các đỉnh, hoặc đặt lại nó.

Một hàng `Xiên` cũng xuất hiện khi đối tượng bị xiên, ví dụ sau khi co giãn không đều một đối tượng cha đã bị xoay.

### Tỷ lệ đồng nhất {#uniform-scale}

Khi bật, tỷ lệ là một giá trị duy nhất, giống nhau trên cả ba trục. Tắt đi để co giãn X, Y và Z riêng biệt.

## Kích thước {#dimension}

Kích thước và tâm của hộp bao quanh vùng chọn, tính theo đơn vị thế giới. Khi chọn nhiều đối tượng, hộp bao quanh tất cả chúng.

* `Kích thước` - Chiều rộng, chiều cao và chiều sâu. Khi bật nút liên kết, thay đổi một kích thước sẽ co giãn hai kích thước còn lại theo cùng tỷ lệ, giữ nguyên tỷ lệ hình.
* `Giữa` - Tâm của hộp bao. Nút mục tiêu di chuyển vùng chọn để tâm của nó nằm ở gốc tọa độ thế giới.

::: tip
`Kích thước` là cách nhanh nhất để đặt cho đối tượng một kích thước thực tế, ví dụ trước khi in 3d: đặt chiều cao bạn muốn và nút liên kết sẽ giữ nguyên tỷ lệ.
:::
