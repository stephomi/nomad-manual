# ![](/icons/history.webp) Lịch sử
![](/images/history_overview.webp)

Giống như hầu hết các công cụ tạo nội dung khác, bạn có thể hoàn tác/làm lại mọi chỉnh sửa trong Nomad.
Có một giới hạn về số lượng thao tác có thể hoàn tác, nhưng bạn có thể kiểm soát hành vi này.

::: tip
Bạn có thể dùng cử chỉ nhanh để hoàn tác/làm lại:
- Chạm 2 ngón để hoàn tác
- Chạm 3 ngón để làm lại
:::

## Lịch sử
![](/images/history_history.webp)

Bảng này hiển thị ngăn xếp lịch sử, cho thấy số bước, tên thao tác và lượng bộ nhớ mà bước đó đang sử dụng.

## Cài đặt
![](/images/history_settings.webp)

### Giới hạn lịch sử (Mb)
Nếu ngăn xếp lịch sử vượt quá giá trị này, các thao tác cũ hơn sẽ bị xóa để mức sử dụng bộ nhớ phù hợp với giới hạn này.


### Số thao tác có thể hoàn tác tối đa
Bạn có thể kiểm soát số lượng thao tác tối đa.

## Khôi phục camera
Với mỗi thao tác, góc nhìn của camera sẽ được lưu lại.
Nếu bạn bật tùy chọn này, hoàn tác hoặc làm lại một thao tác sẽ đặt lại camera về góc nhìn đã lưu.

## Bao gồm hành động

* `Lights` - Khi tắt, các thao tác với đèn (ngoại trừ di chuyển bằng gizmo) sẽ bị bỏ qua trong ngăn xếp lịch sử
* `Matcaps & HDRIs` - Khi tắt, các thay đổi đối với matcap và hdri sẽ bị bỏ qua trong ngăn xếp lịch sử
* `PostProcess` - Khi tắt, các thay đổi đối với tùy chọn hậu xử lý sẽ bị bỏ qua trong ngăn xếp lịch sử

## Thống kê bộ nhớ

Phần này cung cấp bảng phân tích bộ nhớ được Nomad sử dụng.
