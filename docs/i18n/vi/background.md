# ![](/icons/image.webp) Hình nền {#background}

Menu này điều khiển màu nền của Nomad, cũng như mọi ảnh tham chiếu được sử dụng.

![](/images/background_overview.webp)

## Hình nền {#type}
![](/images/background_selector.webp)

Có ba tùy chọn cho nền của khung nhìn (viewport).

* `Environment` - Hiển thị bản đồ môi trường được chọn trong [Shading](shading). Có thể điều chỉnh thêm bằng các điều khiển Blur và Exposure (độ sáng). 
* `Color` - Một màu phẳng mà bạn có thể chọn
* `Gradient` - Dải chuyển màu từ trên xuống dưới. Thanh trượt Factor cho phép bạn xác định điểm giữa của gradient.  

## Ảnh tham chiếu {#reference}

![](/images/background_reference.webp)

Bạn có thể thêm một ảnh tùy chọn vào nền để dùng làm tham chiếu.
Bạn có thể thay đổi vị trí và tỉ lệ, ví dụ nếu bạn muốn di chuyển nó vào góc màn hình.

### ![](/icons/tool_transform.webp) Biến đổi {#transform}

Nút này cho phép bạn đặt ảnh tham chiếu một cách tương tác. Dùng 2 ngón tay để pan, phóng to/thu nhỏ, xoay ảnh tham chiếu vào vị trí mong muốn. Vị trí cuối cùng sẽ được phản ánh trong các thanh trượt bên dưới:

* `Overlay` - ở 0% ảnh tham chiếu sẽ luôn nằm sau các đối tượng của bạn, ở 100% nó nằm phía trước. 
* `Opacity` - Độ trong suốt của ảnh.
* `Position` - Vị trí X và Y của ảnh.
* `Rotation` - Góc xoay của ảnh.
* `Scale` - Tỉ lệ của ảnh.


::: tip

Camera và ảnh tham chiếu được liên kết với nhau. 

Điều này có nghĩa là nếu bạn thiết lập ảnh tham chiếu trùng khớp với bản điêu khắc của mình, khi bạn tạo một camera từ [Camera menu](camera), vị trí, góc xoay, tỉ lệ của ảnh tham chiếu cũng sẽ được lưu cùng với camera. Bạn có thể tắt ảnh tham chiếu, xoay sang khung nhìn khác. Nếu bạn nhìn lại qua camera đó, ảnh tham chiếu sẽ được kích hoạt với các thiết lập bạn đã dùng.

Điều này thậm chí còn cho phép chọn các ảnh khác nhau cho từng camera!

 ![](/videos/reference_camera.mp4)

:::