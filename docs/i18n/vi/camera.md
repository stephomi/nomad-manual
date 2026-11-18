# ![](/icons/camera.webp) Máy ảnh {#camera}

Menu này cho phép bạn tạo và chỉnh sửa camera, cũng như điều khiển cách bạn tương tác với camera.

![](/images/camera_overview2.webp)

Camera trong Nomad có nhiều công dụng:

* Thiết lập các góc nhìn để điêu khắc từ những góc chính xác
* Dùng như máy ảnh chụp hình để căn khung các đối tượng
* Làm camera góc nhìn thứ nhất để di chuyển trong cảnh
* Làm camera trực giao cho game isometric hoặc kiểu render công nghiệp.

## Điều khiển camera {#control}

### Xoay {#rotation}
Bạn xoay camera bằng cách kéo *một* ngón tay trên nền.
Nếu bạn kéo ngón tay trên mô hình, thao tác điêu khắc sẽ bắt đầu thay vào đó.

::: tip Tôi có thể xoay camera nếu không chạm được vào nền không?
Có, bạn có thể đặt *hai* ngón tay lên màn hình (như thể muốn bắt đầu thao tác di chuyển/thu phóng), rồi nhấc *một* ngón tay ra.
:::

### Lấy nét / Đặt lại {#focus}
*Chạm hai lần* lên mô hình để lấy nét vào điểm được chạm.
Nếu bạn *chạm hai lần* vào nền, camera sẽ lấy nét vào lưới được chọn hoặc toàn bộ cảnh, xem [Chạm hai lần vào nền](#dtap-tap-background).


### Di chuyển ngang {#translation}
Di chuyển *hai* ngón tay để dịch chuyển camera.


### Thu phóng {#zooming}
Dùng thao tác chụm/mở ngón tay để phóng to/thu nhỏ.


### Nghiêng {#rolling}
Bạn có thể *nghiêng* góc nhìn bằng cách xoay *hai* ngón tay.
::: warning
Thao tác này chỉ khả dụng với các chế độ xoay `Bi lăn`.
:::

### Điều khiển trên máy tính {#desktop}

Trên máy tính, phím alt/opt được dùng để điều khiển camera:

* kéo đầu bút ở vùng trống = xoay camera
* alt + kéo đầu bút = di chuyển ngang
* alt + kéo đầu bút, rồi thả alt = thu phóng (giống ZBrush)

Với bảng vẽ Wacom có bút từ 2 nút trở lên, hãy dùng phần cài đặt của Wacom để cấu hình đầu bút và các nút như sau:

* đầu bút = nhấp chuột trái
* nút bấm dưới = nhấp chuột giữa
* nút bấm trên = nhấp chuột phải

Với các cài đặt này, bạn có thể điều khiển camera hoàn toàn bằng bút:

* giữ nút bấm trên và di bút lơ lửng = xoay camera
* giữ nút bấm dưới và di bút lơ lửng = di chuyển ngang

## Điều khiển máy ảnh {#camera-controls}

![](/images/camera_list.webp)

### Góc nhìn {#views}
Bạn có thể lưu các điểm nhìn của camera bằng `Thêm góc nhìn`.
Nhấn vào tên góc nhìn để camera quay lại góc nhìn đó.


::: tip
Một góc nhìn đã lưu sẽ lưu cả cài đặt [Kiểu chiếu](#projection) lẫn [Ảnh tham chiếu](background.md).  
Điều này hữu ích khi bạn muốn chuyển qua lại giữa các góc nhìn tham chiếu trước/trái/sau với những ảnh nền khác nhau.
:::

| Thao tác    | Biểu tượng                    | Mô tả                                                                       |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Hiển thị    | ![](/icons/eye_open.webp)    | Bật/tắt camera. Các camera bị ẩn sẽ bị bỏ qua khi dùng nút trước/sau        |
| Tên         |                               | Chọn camera                                                                 |
| Hình ảnh    | ![](/icons/image.webp)       | Ảnh thu nhỏ của ảnh tham chiếu nếu nó được liên kết với camera              |
| Chiếu       | ![](/icons/perspective.webp) | Kiểu chiếu của camera, kèm trường nhìn khi ở chế độ phối cảnh               |
| Cập nhật góc nhìn | ![](/icons/update_view.webp) | Cập nhật góc nhìn đã lưu theo điểm nhìn hiện tại                      |
| Đổi tên     | ![](/icons/pencil.webp)      | Sửa tên camera                                                              |
| Xóa         | ![](/icons/trash.webp)       | Xóa camera                                                                  |

### ![](/icons/camera_add.webp) Thêm góc nhìn {#add}
Tạo một camera mới dựa trên góc nhìn hiện tại.

### ![](/icons/camera.webp) Biểu tượng {#icons-test}

Bật/tắt hiển thị biểu tượng camera trong khung nhìn. Nút này xuất hiện cạnh `Thêm góc nhìn` khi bạn đã có một camera. Nếu một camera đang được chọn, biểu tượng của nó luôn hiển thị.

### Kiểu chiếu {#projection}
Chọn giữa `Phối cảnh` và `Trực giao`.

Ở chế độ phối cảnh, bạn có thể đổi `Trường nhìn thẳng đứng` (FoV) của camera. Tiêu cự tương ứng của máy ảnh 35mm được hiển thị phía trên thanh trượt, rất tiện nếu bạn quen chụp ảnh.
Thường thì nên dùng FOV thấp khi điêu khắc, vì nó giúp giữ đúng tỷ lệ.  
Chế độ `Trực giao` gần giống như FOV bằng 0.

### Góc nhìn thứ nhất {#fps}
Chỉ với phối cảnh. Đặt tâm xoay ngay tại camera, thay vì trên tác phẩm điêu khắc. Kéo ngón tay trên nền sẽ giữ nguyên vị trí camera mà chỉ thay đổi hướng xoay, giống cách các game góc nhìn thứ nhất hoạt động. Hữu ích khi điêu khắc môi trường thay vì từng đối tượng riêng lẻ.

![](/images/camera_rotation_ortho_view.webp)

### Kiểu xoay {#rotation-type}
Theo mặc định, camera dùng chế độ xoay `Bàn xoay`.
Nghĩa là bạn chỉ có hai bậc tự do: trực quan hơn, nhưng đôi khi bạn sẽ cần linh hoạt hơn.  
Bạn có thể chuyển sang `Bi lăn`, khi đó bạn có thể *nghiêng* góc nhìn bằng cách xoay *hai* ngón tay trên khung nhìn. Có hai chế độ `Bi lăn`: chế độ đầu tiên nghiêng góc nhìn như một quả bóng lăn dưới ngón tay, còn chế độ thứ hai (có biểu tượng mũi tên) xoay góc nhìn theo chuyển động ngang và dọc khi bạn kéo, có thể quen thuộc hơn với một số người dùng.

### Bắt dính trực giao {#orthographic}

Khi bật, nếu bạn có bàn phím, giữ phím shift trong lúc xoay góc nhìn sẽ bắt dính camera vào góc nhìn trước/sau/trên/dưới/trái/phải gần nhất và chuyển camera sang trực giao. Camera cũng được chuyển sang trực giao khi bạn nhấn vào bộ điều hướng để bắt dính vào góc nhìn trước/sau/trái/phải/trên/dưới.

### Đặt lại chế độ xem {#reset}

Đưa camera về phía trước và căn toàn bộ cảnh vừa khung nhìn

### Bắt dính góc nhìn {#snap}
Bắt dính vào góc nhìn trước/sau/trái/phải/trên/dưới gần nhất. Nếu bạn đã ở một trong các góc nhìn đó, nhấn lần nữa sẽ xoay 180 độ sang phía đối diện.

### Tốc độ {#speed}

Nếu bạn thấy camera di chuyển quá chậm hoặc quá nhanh, bạn có thể đặt hệ số tốc độ cho `Xoay`, `Phóng to thu nhỏ` và `Dịch`. Hữu ích khi tác phẩm của bạn rất lớn hoặc rất nhỏ.

### Tổng quan về tâm xoay {#pivot}

Khi xoay camera, bạn sẽ thấy một chấm hồng nhỏ: đó là tâm xoay của camera.  
Hiểu rõ tâm xoay nằm ở đâu là rất quan trọng, để bạn không bị lạc hay bực mình với camera.

Theo mặc định, tâm xoay được cập nhật qua các thao tác sau:
- chạm hai lần lên mô hình
- chạm hai lần vào nền (tâm xoay mới sẽ nằm ở tâm lưới của bạn)
- đặt *hai* ngón tay lên màn hình (di chuyển/thu phóng/nghiêng) sẽ cập nhật tâm xoay vào giữa *hai* ngón tay

### Cập nhật tâm xoay... {#update-pivot}

Bạn có thể tùy chỉnh thêm cách cập nhật tâm xoay với các tùy chọn sau:

* `Khi camera bắt đầu chuyển động` - Cập nhật tâm xoay khi bạn bắt đầu tương tác với camera.
* `Tâm xoay ngoài bề mặt` - Cho phép đặt tâm xoay mới ngay cả khi bạn thu phóng ở ngoài bề mặt đối tượng. Cần bật `Khi camera bắt đầu chuyển động`.
* `Khi chạm hai lần` - Cập nhật tâm xoay khi bạn chạm hai lần lên bề mặt đối tượng.
* `Điêu khắc (Nét vẽ)` - Cập nhật tâm xoay khi bạn điêu khắc.

::: tip
Khi đã quen, bạn có thể ẩn chấm hồng (gợi ý) trong menu [Cài đặt](settings.md).
:::

### Chỉnh tâm khi thu nhỏ {#center-view-when-zooming-out}
Khi thu nhỏ, camera không dịch sang ngang mà chỉ lùi ra sau, nên góc nhìn vẫn được giữ ở giữa.

### Chạm hai lần vào đối tượng {#dtap-object}
Khi bật, chạm hai lần lên một đối tượng sẽ lấy nét camera vào điểm được chạm.

### Chạm hai lần vào nền {#dtap-tap-background}
Khi bật, chạm hai lần vào nền sẽ lấy nét camera vào:
* `Lựa chọn` - Các đối tượng được chọn.
* `Cảnh` - Toàn bộ cảnh.
* `Chuyển đổi` - Luân phiên giữa hai lựa chọn trên mỗi lần chạm hai lần. Có hai tùy chọn `Chuyển đổi`, chúng khác nhau ở chỗ cái nào đến trước, như biểu tượng của chúng cho thấy.
