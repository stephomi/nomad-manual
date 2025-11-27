# ![](/icons/symmetry.webp) Đối xứng

Menu này điều khiển cách các nét vẽ được lặp lại qua một mặt phẳng gương hoặc theo hướng xuyên tâm, và các cách để khôi phục đối xứng trên các đối tượng không đối xứng.

![](/images/symmetry_overview.webp) 

## Tổng quan 
Bạn có thể dùng đối xứng theo nhiều cách:

* Như một gương, lật công việc qua trục X (trái/phải), Y (trên/dưới), Z (sau/trước), hoặc kết hợp. 
* Đối xứng xuyên tâm có thể được đặt trên X Y Z với số lần lặp, ví dụ điêu khắc một con sao biển. 
* Gương có thể hoạt động quanh gốc tọa độ (gọi là chế độ thế giới – world mode) hoặc quanh tâm của một đối tượng (gọi là chế độ cục bộ – local mode).
* Các bản điêu khắc bắt đầu không đối xứng có thể bị buộc trở nên đối xứng.

Một phím tắt để bật/tắt đối xứng cũng có thể được tìm thấy ở bảng nhanh bên trái (*"Sym"*). Chữ nhỏ 'L/W' cho biết Nomad đang ở chế độ đối xứng Local hay World. Bạn cũng có thể nhấn giữ lâu hoặc vuốt vào giữa màn hình để mở một menu.

![](/images/symmetry_button.webp) 

Đây là một tùy chọn toàn cục, vì vậy trạng thái của nó sẽ được giữ khi chuyển giữa các công cụ khác nhau.
Ngoại lệ duy nhất là các công cụ biến đổi ([Move](#translate), [Rotate](#rotate), [Scale](#scale) và [Gizmo](#gizmo)) có trạng thái đối xứng riêng.

::: tip
Menu đối xứng chủ yếu dùng để điều khiển đối xứng của nét vẽ. Bạn cũng có thể phản chiếu và lặp lại đối tượng thông qua [repeaters trong menu scene](scene#repeaters). 
:::

## Enabled
Bật/tắt chế độ gương, giống với nút `Sym` trong bảng nhanh bên trái. 

## Planes

Bật các mặt phẳng đối xứng và số lần lặp cho đối xứng xuyên tâm. Lưu ý rằng bạn không cần chỉ chọn một mặt phẳng; bạn có thể bật 1, 2 hoặc cả 3 mặt phẳng cho đối xứng phức tạp.

Trục và số lần lặp cho đối xứng xuyên tâm. Lưu ý rằng chúng cũng không bị giới hạn ở một trục duy nhất, và thậm chí có thể hoạt động kết hợp với đối xứng mặt phẳng để tạo ra kết quả chi tiết rất nhanh. (Tổng số lần lặp bị giới hạn ở 150)

![](/videos/symmetry_demo.mp4) 

## Method
Gương có thể là 'Local', di chuyển cùng đối tượng, hoặc 'World', không di chuyển. Nếu bạn không chắc cần chế độ nào, hãy quan sát mặt phẳng gương và các chỉ báo xuyên tâm được phủ lên đối tượng. Khi ở chế độ local, nếu bạn dùng gizmo biến đổi và di chuyển mô hình, các chỉ báo gương cũng sẽ di chuyển theo. Khi ở chế độ world, các chỉ báo gương sẽ đứng yên, và đối tượng sẽ trượt qua chúng.

## Mirroring
![](/images/symmetry_mirroring.webp)

Khi điêu khắc gần các mặt phẳng đối xứng, một số cọ sẽ có hành vi đối xứng không hoàn hảo. Phần này cho phép bạn khôi phục đối xứng bằng cách sao chép một bên của bản điêu khắc sang bên kia. 

`Direction` - Các nút `<<` và `>>` quyết định bên nào sẽ được sao chép sang bên còn lại. Nomad tính toán điều này từ góc nhìn hiện tại của bạn, vì vậy đặt `<<` chẳng hạn sẽ luôn sao chép từ bên phải màn hình sang bên trái màn hình.

![](/icons/shield.webp) `Mask` - Nút mask cho phép bạn cô lập phần sẽ được phản chiếu; mask phía đích sẽ bảo vệ vùng đó, mask phía nguồn sẽ ngăn vùng đó được phản chiếu sang phía đích. 

![](/icons/tool_hide.webp) `Hide` - Khi bật, các vùng bị ẩn ở phía nguồn sẽ không được phản chiếu sang phía đích. 

`Mirror` sẽ cố gắng xác định xem topology có giống nhau ở hai bên gương hay không, và nếu có, chỉ di chuyển các vertex. Đây là trường hợp phổ biến hơn.

`Split & Mirror` về cơ bản sẽ cắt đối tượng dọc theo gương, sao chép một bên, phản chiếu nó sang bên kia, và hàn các vertex dọc theo gương. Đây là tùy chọn phá hủy hơn, và sẽ xóa multiresolution, nhưng đôi khi phương pháp này là cần thiết nếu mô hình rất khác nhau giữa hai bên gương.

### Flip object
![](/images/symmetry_flip.webp)
Đổi bên trái thành bên phải và ngược lại. Trông tương tự như khi bạn dùng menu công cụ gizmo và đặt scale thành -1 trên trục X.

## Reset and Edit

![](/images/symmetry_edit.webp)

Có thể chỉnh sửa vị trí và hướng của đối xứng (nhưng không được khuyến nghị!). Nếu cần, `World center` và `Orientation` sẽ đặt lại vị trí và hướng đối xứng về giá trị mặc định.

Nomad thường biết nên đặt mặt phẳng đối xứng ở đâu. Không khuyến nghị chỉnh tay phần này, nhưng nút `Gizmo (Edit)` cho phép điều đó cho người dùng nâng cao. Khi nút này được bấm, một gizmo sẽ xuất hiện để bạn tịnh tiến và xoay mặt phẳng đối xứng. Nếu bạn muốn khôi phục tâm và hướng mặc định, các nút `object center` và `orientation` sẽ làm điều đó.

Hành vi của các tùy chọn này sẽ thay đổi tùy thuộc vào không gian (*Local/World*) mà bạn đang ở.
Vì vậy nếu nó không hoạt động như bạn mong đợi, hãy kiểm tra xem bạn đang ở đúng không gian hay không.

::: tip
Nút `Gizmo (Edit)` được cố ý làm mờ như một lời nhắc rằng có lẽ bạn không nên dùng nó!
:::

## Show options
![](/images/symmetry_show.webp)


`Show line` và `Show plane` sẽ bật/tắt lớp phủ trong viewport hiển thị vị trí đối xứng. Lưu ý rằng việc tắt các tùy chọn này chỉ có hiệu lực khi menu đối xứng được đóng.
