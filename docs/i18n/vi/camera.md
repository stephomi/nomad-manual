# ![](/icons/camera.webp) Máy ảnh {#camera}

Menu này cho phép bạn tạo và chỉnh sửa camera, cũng như điều khiển cách bạn tương tác với camera.

![](/images/camera_overview2.webp)

Camera trong Nomad có nhiều mục đích sử dụng:

* Thiết lập góc nhìn để điêu khắc từ các góc chính xác
* Dùng như một máy ảnh để canh khung đối tượng
* Dùng như camera góc nhìn thứ nhất để di chuyển trong cảnh
* Dùng như camera trực giao (orthographic) cho game isometric hoặc render kiểu công nghiệp.

## Điều khiển máy ảnh {#control}

### Xoay {#rotation}
Bạn xoay camera bằng cách kéo *một* ngón tay trên nền (background).  
Nếu bạn kéo ngón tay trên mô hình, thao tác điêu khắc sẽ được bắt đầu thay vì xoay camera.

::: tip Tôi có thể xoay camera nếu không chạm được vào nền không?
Có, bạn có thể đặt *hai* ngón tay lên màn hình - giống như khi bắt đầu thao tác pan/zoom - rồi nhả *một* ngón tay ra.
:::

### Lấy nét / Đặt lại {#focus}
*Chạm đúp* lên mô hình để focus vào điểm được chọn.  
Nếu bạn *chạm đúp* vào nền, camera sẽ focus vào mesh đang được chọn.

### Tịnh tiến {#translation}
Bằng cách di chuyển *hai* ngón tay, bạn có thể pan (tịnh tiến) camera.

### Thu phóng {#zooming}
Bằng cách dùng thao tác chụm/banh (pinch), bạn có thể zoom vào/ra.

### Lăn {#rolling}
Bạn có thể *lăn* (roll) góc nhìn bằng cách xoay *hai* ngón tay.  
::: warning
Thao tác này chỉ khả dụng cho chế độ xoay `trackball`.
:::

### Điều khiển trên máy tính để bàn {#desktop}

Trên desktop, phím alt/opt được dùng để điều khiển camera:

* tip kéo trong vùng trống = xoay camera
* alt+tip kéo = pan
* alt+tip kéo, sau đó thả alt = zoom (giống như trong ZBrush)

Với bảng vẽ Wacom có 2 nút trở lên trên bút, hãy dùng phần cài đặt Wacom để cấu hình đầu bút và các nút như sau:

* tip = click trái
* rocker dưới = click giữa
* rocker trên = click phải

Với các cài đặt đó, bạn có thể điều khiển camera chỉ bằng bút:

* rocker trên và di chuyển khi hover = xoay camera
* rocker dưới và di chuyển khi hover = pan

## Điều khiển máy ảnh {#camera-controls}

![](/images/camera_list.webp)

### Góc nhìn {#views}
Bạn có thể lưu các góc nhìn camera bằng cách dùng `Add View`.  
Nếu bạn bấm vào tên view, camera sẽ khôi phục lại góc nhìn đó.

::: tip
Một view đã lưu sẽ lưu cả thiết lập [Projection Type](#projection-type) và cả [Reference image](background.md).  
Điều này hữu ích nếu bạn muốn luân phiên giữa các view tham chiếu trước/trái/sau với các hình nền khác nhau.
:::

| Action      | Icon                          | Description                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibility  | ![](/icons/eye_open.webp)    | Bật/tắt camera. Camera ẩn sẽ bị bỏ qua khi dùng nút previous/next          |
| Name        |                               | Chọn camera                                                                 |
| Image       | ![](/icons/image.webp)       | Thumbnail của ảnh tham chiếu nếu nó được liên kết với camera                |
| Update View | ![](/icons/update_view.webp) | Cập nhật view đã lưu bằng góc nhìn hiện tại                                 |
| Edit Name   | ![](/icons/pencil.webp)      | Sửa tên camera                                                              |
| Delete      | ![](/icons/trash.webp)       | Xóa camera                                                                  |

### ![](/icons/tool_view.webp) Thêm góc nhìn {#add}
Tạo một camera mới dựa trên góc nhìn hiện tại.

### ![](/icons/camera.webp) Biểu tượng {#icons-test}

Bật/tắt hiển thị icon camera trong viewport. Nếu một camera đang được chọn, icon của nó luôn hiển thị.

### Kiểu chiếu {#projection}
Bạn có thể thay đổi `Field of View` (FOV / tiêu cự) của camera.  
Thông thường nên dùng FOV thấp cho mục đích điêu khắc, vì nó giúp dễ giữ tỷ lệ hơn.  
Bạn cũng có thể dùng chế độ `Orthographic`, về cơ bản tương đương với FOV bằng 0.

### Góc nhìn thứ nhất {#fps}
Bật tùy chọn đặt pivot trực tiếp trên camera thay vì trên tác phẩm điêu khắc. Kéo một ngón tay trên nền sẽ giữ nguyên vị trí camera nhưng thay đổi góc xoay, tương tự như cách hoạt động của game góc nhìn thứ nhất. Hữu ích khi điêu khắc môi trường thay vì từng đối tượng đơn lẻ.

![](/images/camera_rotation_ortho_view.webp)

### Kiểu xoay {#rotation-type}
Mặc định camera dùng chế độ xoay `Turntable`.  
Điều này nghĩa là bạn chỉ có hai bậc tự do, trực quan hơn nhưng trong một số trường hợp bạn sẽ muốn linh hoạt hơn.  
Bạn có thể chuyển sang `Trackball`, khi đó bạn có thể *lăn* (roll) góc nhìn bằng cách xoay *hai* ngón tay trên viewport. Trên desktop có một chế độ trackball thay thế có thể quen thuộc hơn với một số người dùng.

### Ghim trực giao {#orthographic}

Khi bật, nếu bạn có bàn phím, giữ phím Shift trong khi xoay góc nhìn sẽ làm camera snap về góc nhìn gần nhất trong các hướng trước/sau/trên/dưới/trái/phải, và chuyển camera sang chế độ orthographic. Camera cũng sẽ được chuyển sang orthographic khi bạn bấm vào khối view cube để snap về các hướng front/back/left/right/top/bottom.

### Đặt lại góc nhìn {#reset}

Đưa camera về phía trước và fit toàn bộ cảnh vào trong khung nhìn.

### Ghim góc nhìn {#snap}
Snap về góc nhìn gần nhất trong các hướng trước/sau/trái/phải/trên/dưới. Nếu bạn đã ở một trong các góc nhìn đó, bấm lại lần nữa sẽ xoay 180 độ sang phía đối diện.

### Tốc độ {#speed}

Nếu bạn cảm thấy camera di chuyển quá chậm hoặc quá nhanh, bạn có thể đặt hệ số tốc độ cho `rotation`, `translation` và `zooming`. Hữu ích nếu tác phẩm điêu khắc của bạn rất lớn hoặc rất nhỏ.

### Tổng quan về trục xoay {#pivot}

Khi bạn xoay camera, bạn sẽ thấy một chấm hồng nhỏ, đó là điểm pivot của camera.  
Việc hiểu pivot đang ở đâu là rất quan trọng để bạn không bị lạc hoặc khó chịu với camera.

Mặc định pivot được cập nhật thông qua các thao tác sau:
- chạm đúp lên mô hình
- chạm đúp lên nền (pivot mới sẽ ở tâm mesh của bạn)
- đặt *hai* ngón tay lên màn hình (pan/zoom/roll) sẽ cập nhật pivot ở tâm của *hai* ngón tay

### Cập nhật trục xoay... {#update-pivot}

Bạn có thể tùy biến thêm cách pivot được cập nhật với các tùy chọn sau:

* When camera starts moving 
* Allow air pivot
* When double tapping
* Sculpt (stroke)

::: tip
Khi đã quen, bạn có thể ẩn chấm hồng (gợi ý pivot) trong menu [Settings](settings.md).
:::

### Nhấn đúp vào đối tượng {#dtap-object}
Khi `Focus` được bật, chạm đúp sẽ di chuyển pivot tới đối tượng được chạm.

### Nhấn đúp vào nền {#dtap-tap-background}
Khi bật, đặt pivot thành một trong các lựa chọn Selection, Scene, hoặc chuyển đổi qua lại giữa chúng.