# ![](/icons/symmetry.webp) Đối xứng {#symmetry}

Menu này điều khiển cách các nét vẽ được lặp lại qua một mặt phẳng gương, theo kiểu xuyên tâm hoặc theo dạng lát gạch, và các cách khôi phục đối xứng cho những đối tượng không đối xứng.

![](/images/symmetry_overview.webp) 

## Tổng quan {#overview}
Bạn có thể dùng đối xứng theo nhiều cách:

* Như một tấm gương, lật phần việc qua trục X (trái/phải), Y (trên/dưới), Z (sau/trước), hoặc kết hợp các trục.
* Đối xứng xuyên tâm có thể đặt trên X, Y, Z với số lần lặp lại tùy chọn, ví dụ khi điêu khắc một con sao biển.
* Lát gạch lặp lại các nét vẽ của bạn trên khắp đối tượng, để tác phẩm liền mạch khi lát.
* Gương có thể hoạt động quanh gốc tọa độ (gọi là chế độ thế giới) hoặc quanh tâm của đối tượng (gọi là chế độ cục bộ).
* Những tác phẩm ban đầu không đối xứng có thể được ép thành đối xứng.

Bạn cũng có thể tìm thấy lối tắt bật/tắt đối xứng trên bảng nhanh bên trái (*"Đối Xứng"*). Chữ nhỏ 'L/W' cho biết Nomad đang ở chế độ đối xứng Cục bộ (L) hay Thế giới (W). Bạn cũng có thể nhấn giữ hoặc vuốt về phía giữa màn hình để mở một menu.

![](/images/symmetry_button.webp) 

Cài đặt đối xứng được lưu theo từng đối tượng, và tiêu đề menu hiển thị tên của đối tượng bạn đang chỉnh sửa.
Các công cụ điêu khắc dùng chung một trạng thái bật/tắt, còn các công cụ biến đổi ([Biến Đổi](tools.md#transform) và [Gizmo](tools.md#gizmo)) có trạng thái riêng.

::: tip
Menu Đối xứng chủ yếu dùng để điều khiển đối xứng của nét vẽ. Bạn cũng có thể phản chiếu và lặp lại các đối tượng bằng [trình lặp lại trong menu Cảnh](scene#repeaters).
:::

## ![](/icons/symmetry.webp) Kích hoạt {#enabled}
Bật/tắt chế độ gương, giống như nút `Đối Xứng` trên bảng nhanh bên trái. Một biểu tượng cảnh báo nhắc bạn khi nó đang tắt, và menu cũng cho bạn biết khi công cụ hiện tại bỏ qua đối xứng.

## Mặt phẳng {#planes}

Bật (các) mặt phẳng đối xứng, và đặt số lần lặp lại cho đối xứng xuyên tâm. Lưu ý rằng bạn không nhất thiết chỉ chọn một mặt phẳng: bạn có thể bật 1, 2 hoặc cả 3 mặt phẳng cho những kiểu đối xứng phức tạp.

Hàng `Xuyên tâm` đặt số lần lặp lại cho đối xứng xuyên tâm quanh từng trục. Lưu ý rằng chúng cũng không bị giới hạn ở một trục, và thậm chí có thể kết hợp với đối xứng mặt phẳng để tạo ra kết quả chi tiết rất nhanh. (Tổng số lần lặp lại bị giới hạn ở 200)

![](/videos/symmetry_demo.mp4) 

## Gạch lát {#tile}

Lặp lại các nét vẽ dọc theo một trục, cách nhau một khoảng đều đặn, để tác phẩm liền mạch khi lát. Rất tiện cho hoa văn, gạch, hoặc một kết cấu bạn định lặp lại.

Bật lát gạch cho từng trục bằng các nút `Gạch lát`, rồi đặt `Số lượng` (bao nhiêu lần lặp trải trên đối tượng) hoặc `Khoảng cách` (khoảng trống giữa hai lần lặp). Chạm vào nút gạt bên trái để chuyển giữa hai cách này.

## Phương pháp {#method}
Gương có thể là `Cục bộ`, di chuyển theo đối tượng, hoặc `Thế giới`, đứng yên. Nếu không chắc mình cần chế độ nào, hãy quan sát các chỉ báo mặt phẳng gương và xuyên tâm hiển thị chồng lên đối tượng. Ở chế độ cục bộ, nếu bạn dùng các công cụ biến đổi (`Gizmo` hoặc `Biến Đổi`) để di chuyển mô hình, các chỉ báo gương cũng di chuyển theo. Ở chế độ thế giới, các chỉ báo gương đứng yên, và đối tượng sẽ trượt qua chúng.

## Phản chiếu {#mirroring}
![](/images/symmetry_mirroring.webp)

Khi điêu khắc gần các mặt phẳng đối xứng, một số cọ sẽ cho kết quả đối xứng không hoàn hảo. Phần này cho phép bạn khôi phục đối xứng bằng cách chép một bên của tác phẩm sang bên kia.

`Hướng` - Hai nút mũi tên cạnh tiêu đề `Phản chiếu` quyết định bên nào được chép sang bên kia. Nomad tính hướng này từ khung nhìn hiện tại, nên bên được chọn vẫn giữ nguyên trên màn hình dù bạn nhìn mô hình từ phía nào.

![](/icons/shield.webp) `Mặt nạ` - Nút mặt nạ cho phép bạn khoanh vùng phần sẽ được phản chiếu: che mặt nạ bên đích sẽ bảo vệ vùng đó, che mặt nạ bên nguồn sẽ ngăn vùng đó bị phản chiếu sang bên đích.

![](/icons/tool_hide.webp) `Ẩn` - Khi bật, những vùng bị ẩn ở bên nguồn sẽ không được phản chiếu sang bên đích.

`Phản chiếu` (giữ cấu trúc) sẽ cố xác định xem tô pô hai bên gương có giống nhau không, và nếu có, chỉ di chuyển các đỉnh. Đây là trường hợp phổ biến hơn. Đối xứng xuyên tâm bị bỏ qua. Nếu tô pô không đối xứng, Nomad sẽ đề nghị ép phản chiếu bằng `Cắt • Phản chiếu`.

Các nút `Cắt` cắt đối tượng dọc theo (các) mặt phẳng đối xứng. Chúng thay đổi tô pô, nên mang tính phá hủy hơn `Phản chiếu`. Con số trên mỗi nút là số đối tượng bạn nhận được:

* `Cắt` - bỏ đi một bên của đối tượng.
* `Cắt • Phản chiếu` - cắt đối tượng, chép một bên, phản chiếu sang bên kia, rồi hàn các đỉnh dọc theo mặt gương. Đôi khi bạn cần cách này nếu mô hình rất khác nhau giữa hai bên gương.
* `Cắt • Tách` - cắt đối tượng và giữ mỗi bên thành một đối tượng riêng.
* `Cắt • Phản chiếu • Tách` - giống `Cắt • Phản chiếu`, nhưng mỗi bên trở thành một đối tượng riêng.

Nếu chọn nhiều đối tượng, `Phản chiếu` và [Lật đối tượng](#flip-object) sẽ áp dụng cho tất cả.

### Lật đối tượng {#flip-object}
![](/images/symmetry_flip.webp)
Đổi bên trái thành bên phải và ngược lại, theo `X`, `Y` hoặc `Z`. Kết quả trông giống như khi bạn dùng menu công cụ gizmo và đặt tỷ lệ X thành -1.

## Đặt lại và Chỉnh sửa {#reset-and-edit}

![](/images/symmetry_edit.webp)

Bạn có thể chỉnh vị trí và hướng của đối xứng (nhưng không khuyến khích!). Khi cần, `Trung tâm thế giới` (`Trung tâm đối tượng` ở chế độ cục bộ) và `Hướng` sẽ đặt lại vị trí và hướng của đối xứng về giá trị mặc định.

Nomad thường biết nên đặt mặt phẳng đối xứng ở đâu. Không nên tự chỉnh, nhưng nút `Chỉnh sửa Gizmo` cho phép người dùng nâng cao làm điều đó. Khi nhấn nút này, một gizmo hiện ra để bạn di chuyển và xoay mặt phẳng đối xứng. Nếu muốn khôi phục tâm và hướng mặc định, hãy dùng các nút đặt lại ở trên.

`Từ trục xoay` đặt mặt phẳng đối xứng vào trục xoay của công cụ [Gizmo](tools.md#gizmo). Nó chỉ khả dụng khi công cụ `Gizmo` đang hoạt động.

Hành vi của các tùy chọn này thay đổi tùy theo không gian (*Cục bộ/Thế giới*) bạn đang dùng.
Vì vậy nếu nó không hoạt động như bạn mong đợi, hãy kiểm tra xem bạn có đang ở đúng không gian không.

::: tip
Chỉnh mặt phẳng đối xứng bằng gizmo còn khá thử nghiệm, có lẽ bạn sẽ không cần đến nó!
:::

## Tùy chọn hiển thị {#show-options}
![](/images/symmetry_show.webp)


`Hiển thị đường` và `Hiển thị mặt phẳng` bật/tắt lớp phủ trong khung nhìn thể hiện vị trí đối xứng. Lưu ý rằng việc tắt các tùy chọn này chỉ có hiệu lực khi menu Đối xứng được đóng lại.
