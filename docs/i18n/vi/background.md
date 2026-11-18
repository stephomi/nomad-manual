# ![](/icons/image.webp) Nền {#background}

Menu này điều khiển màu nền của Nomad, cùng với các hình ảnh tham khảo mà bạn muốn dùng.

![](/images/background_overview.webp)

## Loại {#type}
![](/images/background_selector.webp)

Có ba lựa chọn cho nền của khung nhìn.

* `Môi trường` - Hiển thị bản đồ môi trường đã chọn trong [Tô bóng](shading.md). Bạn có thể tinh chỉnh thêm bằng các thanh trượt `Làm mờ` và `Phơi sáng` (độ sáng). 
* `Màu sắc` - Một màu phẳng do bạn chọn
* `Màu gradient` - Dải chuyển giữa hai màu. Thanh trượt `Yếu tố` cho phép bạn dời điểm giữa của dải màu.  

### Kiểu gradient {#gradient-type}
Với `Màu gradient`, hãy chọn hình dạng của nó:
* `Tuyến tính` - Dải màu thẳng, hướng của nó được đặt bằng thanh trượt `Góc`.
* `Xuyên tâm` - Dải màu tròn, lan ra từ giữa màn hình.
* `Bầu trời` - Dải màu gắn với đường chân trời của thế giới, nên nó đi theo máy ảnh khi bạn nhìn lên hay nhìn xuống.

Mỗi màu đều có một nút đặt lại và một công cụ chọn màu để lấy màu ngay trên màn hình.

## ![](/icons/lock.webp) Đồng bộ hóa với khóa máy ảnh {#sync-on-camera-lock}
Khi máy ảnh bị khóa bằng [Bộ điều hướng](settings.md#snap-cube), hình ảnh tham khảo sẽ đi theo chuyển động của máy ảnh, nhờ đó luôn khớp với bản điêu khắc của bạn.

* `Cho phép nghiêng camera (Bi lăn)` - Cho phép máy ảnh nghiêng khi bạn thoát khỏi chế độ khóa máy ảnh.
* `Đặt lại góc nhìn khi mở khóa` - Đặt lại góc nhìn khi bạn thoát khỏi chế độ khóa máy ảnh.

## Hình ảnh tham khảo {#reference}

![](/images/background_reference.webp)

Bạn có thể đặt một hình ảnh tùy ý lên nền để dùng làm tham khảo. Chạm vào `Nhập...` để thêm ảnh, rồi đánh dấu `Hình ảnh tham khảo` để hiển thị nó.
Bạn có thể đổi vị trí và tỷ lệ của ảnh, chẳng hạn khi muốn dời nó vào góc màn hình.

### ![](/icons/tool_transform.webp) Biến đổi {#transform}

Nút này cho phép bạn đặt hình ảnh tham khảo một cách trực quan. Dùng 2 ngón tay để kéo, phóng to thu nhỏ và xoay ảnh vào đúng chỗ. `Đặt lại cài đặt` đưa ảnh về vị trí mặc định. Vị trí cuối cùng sẽ được thể hiện qua các thanh trượt bên dưới:

* `Lớp phủ` - Ở 0%, hình ảnh tham khảo luôn nằm sau các đối tượng của bạn, ở 100% thì nó nằm phía trước. 
* `Độ mờ đục` - Mức độ trong suốt của ảnh.
* `Hậu kỳ` - Áp dụng các hiệu ứng hậu kỳ lên hình ảnh tham khảo. Tắt nó đi để giữ nguyên màu gốc.
* `Vị trí X` / `Vị trí Y` - Vị trí X và Y của ảnh.
* `Tỉ lệ` - Tỷ lệ của ảnh.
* `Xoay vòng` - Góc xoay của ảnh.


::: tip

Máy ảnh và hình ảnh tham khảo được liên kết với nhau. 

Nghĩa là nếu bạn đã căn hình ảnh tham khảo khớp với bản điêu khắc, rồi tạo một máy ảnh từ [menu Máy ảnh](camera.md), thì vị trí, góc xoay và tỷ lệ của hình ảnh tham khảo cũng được lưu cùng máy ảnh đó. Bạn có thể tắt hình ảnh tham khảo và xoay sang một góc nhìn khác. Khi nhìn lại qua máy ảnh đó, hình ảnh tham khảo sẽ được bật lại với đúng các cài đặt bạn đã dùng.

Bạn thậm chí có thể chọn những hình ảnh khác nhau cho từng máy ảnh!

 ![](/videos/reference_camera.mp4)

:::
