# ![](/icons/history.webp) Lịch sử {#history}
![](/images/history_overview.webp)

Như hầu hết các công cụ sáng tạo nội dung, bạn có thể hoàn tác/làm lại mọi chỉnh sửa trong Nomad.
Lịch sử có thể trở nên rất lớn, vì vậy bạn tự quyết định bao nhiêu phần được giữ trong bộ nhớ, bao nhiêu phần được giữ trên bộ nhớ lưu trữ, và có lưu nó cùng dự án hay không.

::: tip
Bạn có thể dùng các cử chỉ nhanh để hoàn tác/làm lại:
- Chạm 2 ngón tay để hoàn tác
- Chạm 3 ngón tay để làm lại
:::

## ![](/icons/history.webp) Lịch sử {#history-panel}
![](/images/history_history.webp)

Bảng này hiển thị ngăn xếp lịch sử, gồm số bước, tên thao tác, đối tượng mà thao tác áp dụng lên và dung lượng bộ nhớ mà bước đó đang dùng.

Chạm vào một mục để quay lại (hoặc tiến tới) trạng thái đó. Nhấn giữ một mục để xóa vĩnh viễn mục đó cùng toàn bộ lịch sử cũ hơn, một cách nhanh để giải phóng bộ nhớ khi bạn đã hài lòng với bản điêu khắc.

### ![](/icons/speed.webp) Phát lại {#replay}
Nút phát ở góc dưới bên trái sẽ tua về gốc, rồi làm lại từng thao tác một, một cách thú vị để xem bản điêu khắc của bạn được hình thành. Thanh trượt đặt tốc độ theo số thao tác mỗi giây. Chạm vào nút lần nữa để dừng; hoàn tác/làm lại hoặc chạm vào một mục cũng sẽ dừng nó.

Trước khi bắt đầu, một cửa sổ bật lên cho bạn chọn:
* `Đảo ngược` - Hoàn tác từ trạng thái hiện tại về gốc, thay vì phát lại từ gốc.
* `Khôi phục camera` - Máy ảnh đi theo các thao tác được phát lại, kể cả khi [Khôi phục camera](#restore-camera) đang tắt.
* `Làm mượt camera` - Máy ảnh lướt nhẹ nhàng giữa các góc nhìn thay vì nhảy đến từng góc. Giá trị càng cao thì máy ảnh chuyển động càng êm.

::: warning
Phát lại vẫn đang là tính năng thử nghiệm.
:::

## Bao gồm các thao tác {#include-actions}

Các biểu tượng ở cuối bảng Lịch sử cho bạn chọn loại chỉnh sửa nào được ghi vào lịch sử:

| Thao tác    | Biểu tượng                    | Mô tả                                                                               |
| :---------- | :---------------------------: | :---------------------------------------------------------------------------------- |
| Ánh sáng    | ![](/icons/light.webp)        | Chỉnh sửa đèn. Việc di chuyển đèn bằng Gizmo luôn được ghi lại, vì nó có thể ảnh hưởng đến các đối tượng khác trong cây phân cấp của cảnh |
| Tô bóng     | ![](/icons/sun.webp)          | Chế độ PBR, MatCap và Unlit, các MatCap và HDRI                                     |
| Xử lý hậu kỳ | ![](/icons/postprocess.webp) | Chỉnh sửa hậu kỳ                                                                    |
| Lựa chọn    | ![](/icons/tool_lattice.webp) | Chỉnh sửa vùng chọn của Lattice, như các lần nhấp, chọn bằng dây thòng lọng và bỏ chọn |

## Cài đặt {#settings}
![](/images/history_settings.webp)

### ![](/icons/camera.webp) Khôi phục camera {#restore-camera}
Với mỗi thao tác, góc nhìn của máy ảnh đều được lưu lại.
Nếu bật tùy chọn này, khi hoàn tác hoặc làm lại một thao tác, máy ảnh sẽ trở về góc nhìn đã lưu.

### ![](/icons/history.webp) Lưu lịch sử {#save-history}
Giữ lại lịch sử hoàn tác khi lưu dự án, để nó vẫn còn khi bạn mở lại dự án. Tắt đi để tệp dự án nhỏ gọn hơn.

### ![](/icons/ram.webp) Giới hạn RAM {#history-limit-mb}
Dung lượng lịch sử tối đa được giữ trong RAM. Các trạng thái cũ hơn được chuyển sang bộ nhớ lưu trữ và tải lại khi cần, chúng không bị xóa.

### ![](/icons/save.webp) Giới hạn lưu trữ {#storage-limit}
Dung lượng lưu trữ tối đa mà lịch sử của dự án này được dùng. Khi đạt đến giới hạn, các thao tác cũ nhất sẽ bị xóa vĩnh viễn.

::: tip
Giới hạn mới có hiệu lực sau lần chỉnh sửa, hoàn tác hoặc làm lại tiếp theo.
:::

### ![](/icons/undo.webp) Cảnh báo hoàn tác {#maximum-undoable}
Khi quay lại nhiều hơn số thao tác này trong một lần, Nomad sẽ hỏi xác nhận trước. Nếu sau đó bạn thực hiện một chỉnh sửa, mọi thao tác sau thời điểm đó sẽ bị mất, nên tùy chọn này bảo vệ bạn khỏi một cú chạm nhầm ở tận cuối danh sách.

## Thống kê bộ nhớ {#memory-stats}

Phần này cho biết chi tiết bộ nhớ mà Nomad đang sử dụng.
