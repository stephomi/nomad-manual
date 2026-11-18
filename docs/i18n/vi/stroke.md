# ![](/icons/brush.webp) Nét vẽ {#stroke}

---
![](/images/stroke_overview.webp) 

## Tổng quan {#overview}

Bạn có thể tùy chỉnh cách nét vẽ hoạt động cho hầu hết các cọ của công cụ.
Các thiết lập này khá giống với những gì bạn thấy trong các ứng dụng vẽ 2d, tuy nhiên có một số tùy chọn chỉ dành riêng cho điêu khắc và 3d.

Các tùy chọn được chia thành 5 menu con:

| Tên      | Biểu tượng                   | Mô tả                                                              |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Nét vẽ   | ![](/icons/brush.webp)      | Điều khiển cách nét vẽ được áp lên mô hình                         |
| Alpha    | ![](/icons/alpha.webp)      | Cách một kết cấu thang xám được dùng làm dấu cọ                    |
| Giảm dần | ![](/icons/falloff.webp)    | Điều khiển cách độ mạnh của cọ thay đổi từ tâm ra mép              |
| Bộ lọc   | ![](/icons/filter.webp)     | Cách cọ chịu ảnh hưởng từ hình học của mô hình                     |
| Áp lực   | ![](/icons/pressure.webp)   | Điều khiển cách phản hồi với áp lực bút                            |

::: tip
Không phải tùy chọn nét vẽ nào cũng áp dụng cho mọi công cụ. Những tùy chọn mà công cụ hiện tại không dùng đến sẽ bị vô hiệu hóa hoặc ẩn đi. 
:::


## ![](/icons/brush.webp) Nét vẽ {#stroke-1}

### ![](/icons/radius.webp) Bán kính {#radius}

![](/images/stroke_radius.webp)

Các tùy chọn bán kính là thiết lập chung: chúng áp dụng cho mọi công cụ.

#### Không gian {#size}

* `Màn hình` - bán kính được tính theo đơn vị màn hình. Nếu bạn đặt bán kính rộng 100 pixel, nó sẽ luôn rộng 100 pixel dù bạn phóng to hay thu nhỏ.
* `World (3D)` - bán kính được tính theo đơn vị 3d. Ví dụ, nếu bạn tạo một hình cầu và đặt bán kính bằng đúng kích thước hình cầu, bán kính sẽ luôn bằng kích thước hình cầu đó khi bạn phóng to hay thu nhỏ.

#### ![](/icons/link.webp) Đồng bộ phím tắt {#sync-shortcut}

Khi bật, các thiết lập bán kính và hình bóng sẽ được giữ đồng bộ khi bạn chuyển sang các cọ phím tắt (`Làm mịn`, `Mặt nạ` hoặc `Ẩn`). Nhờ vậy, một lượt làm mịn hay tô mặt nạ nhanh sẽ dùng đúng kích thước cọ của công cụ bạn đang dùng.

#### ![](/icons/link.webp) Chia sẻ bán kính {#share-radius}

Khi bật, tất cả công cụ sẽ dùng chung một bán kính. Mặc định, mỗi công cụ có bán kính riêng của nó.


### Kiểu nét vẽ {#stroke-type}

![](/images/stroke_strokemode.webp)

Nét vẽ có thể hoạt động theo nhiều chế độ:

### ![](/icons/stroke_dot.webp) Điểm {#dot}
Kéo như một nét vẽ thông thường. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Lăn alpha {#roll}
Alpha của cọ sẽ được xoay theo hướng của nét vẽ, rất hữu ích để tạo các đường khâu trên vải. 
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Khóa + bán kính {#lock-radius}
Đóng dấu một nét cọ với **_độ cao_** cố định. Thao tác kéo sẽ đặt tỷ lệ và góc xoay.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Khóa + cường độ {#lock-intensity}
Đóng dấu một nét cọ với **_bán kính_** cố định. Thao tác kéo sẽ đặt độ cao và góc xoay.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
Hai chế độ `Khóa + bán kính` và `Khóa + cường độ` bỏ qua các thiết lập [Áp lực](#pressure), vì thao tác kéo đã đặt sẵn kích thước và độ mạnh.
:::

![](/images/stroke_strokemodemove.webp)

Hai công cụ `Di chuyển` và `Kéo` có 3 tùy chọn riêng:

### ![](/icons/snake.webp) Kéo {#drag}

Liên tục cập nhật những gì nằm trong bán kính cọ trong suốt nét vẽ. Một nét vẽ nhanh sẽ bỏ lại bề mặt phía sau, còn một nét vẽ chậm sẽ giữ lấy vật liệu, tạo ra những hình dạng dài hơn. Đây là chế độ mặc định của công cụ `Kéo`. Khi dùng với `Tô pô động`, bạn có thể tạo những phần đùn ra uốn lượn như con rắn. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Chụp nắm {#grab}
Chọn những gì nằm trong bán kính cọ ngay khi bắt đầu nét vẽ, và giữ nguyên vùng chọn đó. Chế độ này hữu ích cho những thao tác di chuyển cần chính xác hơn, vì bạn có thể cẩn thận điều chỉnh khoảng cách di chuyển mà không vô tình kéo theo nhiều hơn phần đã chọn ban đầu. Đây là chế độ mặc định của công cụ `Di chuyển`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Khóa + bán kính (kéo) {#lock-radius-drag}
Bán kính bạn đặt sẽ bị bỏ qua, thay vào đó nó được tính động dựa trên khoảng cách bạn kéo nét vẽ ra xa điểm bắt đầu. Khoảng cách nhỏ = bán kính nhỏ, khoảng cách lớn = bán kính lớn. Dùng thanh trượt cường độ để điều khiển hình dạng của độ giảm dần. Rất hữu ích để dựng khối những hình dạng hữu cơ mềm dẻo như cao su.
![](/videos/stroke_lockradius_drag.mp4) 

Một số công cụ khác cũng liệt kê các kiểu nét vẽ riêng ở đây, ví dụ `Thư giãn`, `Làm mịn` và `Bôi nhòe` cho các công cụ làm mịn, hoặc các hình dạng như `Dây thòng lọng` và `Đường Cong` cho các công cụ dựa trên vùng chọn. Chúng được mô tả cùng với từng [công cụ](tools.md).


### Điều chỉnh cường độ khoảng cách {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Những nét vẽ có khoảng cách thấp (dưới 50%) có thể chồng lên nhau rất nhanh, khiến nét vẽ đậm hơn so với khi khoảng cách cao hơn. Tùy chọn này sẽ bù trừ cho điều đó, để nét vẽ có cường độ gần như nhau bất kể khoảng cách là bao nhiêu.

### Khoảng cách giữa nét vẽ {#stroke-spacing}
Khoảng cách giữa mỗi lần áp dấu cọ trong khi kéo. Giá trị dưới 100% sẽ chồng lên nhau, tạo cảm giác một nét vẽ liền mạch. Giá trị trên 100% sẽ bắt đầu để lại khoảng trống, hữu ích để điêu khắc các chi tiết như đường khâu hay khóa kéo.

### Định ổn dây lười {#lazy-rope-stabilizer}
Nét vẽ sẽ đi trễ sau vị trí con trỏ một khoảng nhất định. Bạn có thể dùng nó để vẽ những đường mượt mà.
![](/videos/stroke_lazy_rope.mp4) 

### Làm mượt nét vẽ {#stroke-smoothing}
Lấy trung bình nhiều vị trí của con trỏ để có nét vẽ mượt hơn.
Với giá trị cao, nét vẽ sẽ đi trễ sau con trỏ nhưng cuối cùng sẽ bắt kịp.
Tùy chọn này hữu ích để vẽ những đường mượt mà.

### Bán kính bắt dính {#snap-radius}
Nối nét vẽ vào nét trước đó khi con trỏ bắt đầu gần chỗ nét vẽ trước kết thúc. Bán kính quyết định phạm vi tìm điểm cuối của nét vẽ trước. Tùy chọn này hữu ích khi vẽ những đường dài liên tục mà bạn hay phải dừng lại giữa chừng.

### ![](/icons/trail.webp) Vệt kéo bút {#trail}

Khi bật, mỗi dấu cọ mới cũng áp lại những điểm gần nhất của nét vẽ phía sau nó. `Số lượng vệt kéo bút` đặt số điểm được áp lại, `Cường độ vệt kéo bút` đặt độ mạnh của chúng, và `Bán kính vệt kéo bút` đặt mức chúng to ra thêm bao nhiêu.

Vệt kéo bút chỉ hoạt động với kiểu nét vẽ `Điểm`, và không hoạt động với [ảnh hưởng của độ giảm dần](#influence) kiểu `Gờ`.

### ![](/icons/silhouette.webp) Hình bóng {#silhouette}
![](/images/stroke_silhouette.webp)
Mặc định, nét vẽ chỉ tác động lên bề mặt mô hình nằm trong bán kính cọ. Khi bật hình bóng, nét vẽ sẽ được chiếu xuyên qua toàn bộ mô hình. Điều này rất hữu ích khi dựng khối ban đầu cho mô hình, hoặc với những hình dạng cần giữ các mặt bên vuông góc.

Bạn có thể đặt rõ hướng chiếu:

* `X`, `Y`, `Z` - chiếu theo một trục cố định.
* `Xem` - chiếu theo hướng của camera.
* `Khi snap` - chiếu theo hướng của camera, nhưng chỉ khi camera đang được snap vào một góc nhìn. Nếu không, nét vẽ vẫn là nét vẽ thông thường.
* `Gần nhất` - chiếu theo trục gần nhất với hướng của camera. Đây là thiết lập mặc định.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Ngẫu nhiên {#randomize}

![](/images/stroke_randomize.webp)

`Cường độ`, `Độ lệch`, `Xoay` và `Tỷ lệ` của nét vẽ đều có thể được làm ngẫu nhiên. Dùng ô đánh dấu của mỗi hàng để bật hoặc tắt nó. Bạn có thể dùng tính năng này để tạo nhiều hiệu ứng khác nhau, ví dụ làm ngẫu nhiên với công cụ vẽ màu để tạo màu loang lổ, hoặc với công cụ tạo rãnh sắc để tạo chi tiết da.

`Chu kỳ (chậm hơn)` đặt độ dài của chu kỳ ngẫu nhiên: tăng lên để có những biến đổi chậm, nhấp nhô, giảm xuống để có nhiễu dày đặc. Nút nhỏ bên cạnh mỗi hàng điều chỉnh chu kỳ chỉ cho riêng hàng đó.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Ngẫu nhiên - HSV {#randomize-hsv}

Với các công cụ vẽ màu, `Sắc độ`, `Độ bão hòa` và `Giá trị` của màu vẽ cũng có thể được làm ngẫu nhiên, với chu kỳ riêng của chúng. Rất tuyệt để thêm những biến đổi màu tinh tế cho da hoặc đá.

### Độ lệch nét vẽ {#stroke-offset}

Áp một độ lệch cố định lên nét vẽ, để ngón tay của bạn không che mất nó. Tùy chọn này hữu ích trên màn hình nhỏ. Đây là thiết lập chung: bật nó bằng ô đánh dấu, và nó sẽ áp dụng cho mọi công cụ.

## ![](/icons/alpha.webp) Alpha {#alpha}
![](/images/stroke_alpha.webp) 

`Alpha` là một kết cấu dùng để điều biến cách cọ của bạn hoạt động.
Đó là một ảnh thang xám, trong đó điểm ảnh đen nghĩa là không biến dạng, còn điểm ảnh trắng nghĩa là biến dạng tối đa.

Nhấn vào ảnh alpha để thay đổi nó. Ngoài các alpha có sẵn và những alpha bạn tự nhập, danh sách alpha còn có thể tải về các bản đồ dịch chuyển (displacement map) từ Poly Haven.

Nhấn vào ô xem trước vật liệu để tải alpha từ một vật liệu thiết lập sẵn. Bạn cũng có thể lưu vật liệu thiết lập sẵn tại đây, và chọn nhúng kết cấu cùng với công cụ.

::: tip
Kết cấu không bao giờ bị thay đổi kích thước, vì vậy kết cấu lớn có thể làm chậm hiệu năng.
:::

### ![](/icons/blend_contrast.webp) Sửa alpha {#invert-pixels}
Nút `Sửa...` trên một alpha đã nhập sẽ mở một cửa sổ để chỉnh sửa chính ảnh đó: giá trị trung bình, đảo ngược điểm ảnh (đen thành trắng và trắng thành đen), xoay 90°, và lật ngang hoặc lật dọc. Tệp ảnh sẽ được ghi đè, nên các ứng dụng khác cũng thấy ảnh đã được sửa.

::: tip

Các alpha có sẵn đi kèm Nomad không thể sửa được.

:::

### Phép chiếu {#projection}

Cách alpha được chiếu lên mô hình:

* `Bề mặt` - alpha nằm trên bề mặt dưới cọ, theo hướng của bề mặt đó.
* `Màn hình` - alpha được chiếu thẳng từ góc nhìn.
* `Gạch lát` - alpha được chiếu từ góc nhìn và đứng yên tại chỗ khi bạn vẽ lên nó, giống như một tấm khuôn tô (stencil), nhờ vậy một họa tiết lặp lại sẽ nối liền với nhau không lộ đường nối. Góc xoay bị khóa, và áp lực bút không làm thay đổi kích thước họa tiết.
* `Ba Mặt Phẳng` - alpha được chiếu theo 3 trục. Các tùy chọn tỷ lệ, xoay và lát gạch bên dưới sẽ được thay bằng các thiết lập kết cấu ba mặt phẳng.

### ![](/icons/diagonal.webp) Tỷ lệ {#scaling}

Kích thước cọ trong Nomad là một hình tròn với bán kính do bạn đặt. Kết cấu thường có dạng vuông hoặc chữ nhật, và các tham số `Tỷ lệ` cho phép bạn quyết định kết cấu sẽ nằm vừa trong hình tròn như thế nào. Với một kết cấu vuông, giá trị 0.7 sẽ giúp nó nằm gọn trong hình tròn. Giá trị 1 sẽ phóng kết cấu lớn hơn để hình tròn nằm gọn bên trong nó, cắt bớt phần mép.

![](/images/alpha_scaling.webp) 

Bật `Tỷ lệ Y` cho phép bạn kéo giãn alpha theo chiều dọc. Khi đó thanh trượt đầu tiên trở thành `Tỷ lệ X`.

![](/images/alpha_scaling_y.webp) 

`Lật ngang` lật đối xứng alpha từ trái sang phải.

### Xoay {#rotation}

Kết cấu alpha sẽ được xoay theo hướng của nét vẽ. Bạn có thể thêm một độ lệch góc xoay, và nếu biểu tượng ổ khóa được bật, kết cấu sẽ bị khóa ở góc xoay này so với màn hình.

Nút hình bút bên cạnh sẽ xoay alpha khi bạn xoay thân bút cảm ứng (barrel roll), với các kiểu nét vẽ `Khóa + bán kính` và `Khóa + cường độ` khi góc xoay không bị khóa. Nó chỉ hoạt động với những bút cảm ứng có hỗ trợ tính năng này.

### Lát gạch {#tiling}
![](/images/stroke_tiling.webp) 

Tần suất kết cấu lặp lại bên trong dấu cọ. Các chế độ `Lát gạch - X` và `Lát gạch - Y` cho phép bạn giới hạn chỉ một kết cấu duy nhất trong nét vẽ (`Không có`), hoặc lặp lại kết cấu (`Lặp lại`), hoặc lặp lại kiểu soi gương, trong đó cứ mỗi kết cấu thứ hai sẽ bị lật lại để tạo họa tiết hoặc giúp tạo kết cấu liền mạch (`Gương`). Chúng có sẵn với nét vẽ `Lăn alpha`, phép chiếu `Gạch lát`, hoặc khi `Lát gạch` lớn hơn 1.

`Ôm khít (ảnh không vuông)` chỉ có tác dụng với các kết cấu alpha và kết cấu cọ không vuông. Khi bật, mỗi ảnh tự lát gạch riêng mà không có khoảng trống. Tắt nó đi để giữ alpha và các ảnh khác đồng bộ với nhau khi tỷ lệ khung hình của chúng khác nhau.

![](/videos/alpha_tiling.mp4) 



### Giá trị trung bình {#mid-value}

Mặc định, điểm ảnh đen nghĩa là không biến dạng, còn điểm ảnh trắng nghĩa là biến dạng dương tối đa. Ví dụ, một cọ đất sét với kết cấu alpha hình đá sẽ chỉ kéo bề mặt nhô ra ở những chỗ alpha không phải màu đen.

Nếu bạn muốn cọ ấn bề mặt lõm vào, hoặc vừa ấn vào VỪA kéo ra, bạn có thể chỉnh giá trị trung bình. Chẳng hạn nếu bạn đặt giá trị là 0.5, màu xám trung tính trong alpha sẽ không làm gì cả, màu đen sẽ ấn vào, còn màu trắng sẽ kéo ra.

Có hai nút giúp bạn tìm giá trị phù hợp: nút hình vuông đọc giá trị trung bình từ đường viền của ảnh, còn công cụ chọn màu cho phép bạn chọn trực tiếp trên alpha.




## ![](/icons/falloff.webp) Giảm dần {#falloff}

![](/images/falloff_menu.webp) 

Phần này tương tự [Alpha](#alpha), chỉ khác là bạn điều khiển cường độ bằng một đường cong duy nhất. Nó được kết hợp với alpha, để bạn có thể dùng kết cấu cho chi tiết, và dùng độ giảm dần để điều khiển độ mờ dần ở mép và cường độ ở tâm của công cụ.

Khi đường cong nằm ở trên cùng, đó là biến dạng tối đa; khi nó nằm ở dưới cùng, cọ không có tác dụng gì.

Bạn có thể hình dung đường cong như một mặt cắt ngang qua đầu cọ. Phần bên dưới cho bạn xem trước một 'dấu' cọ đơn lẻ trông như thế nào trên bề mặt mô hình, và nếu cọ có kết cấu alpha, nó cũng sẽ được hiển thị để bạn xem trước độ giảm dần và alpha tương tác với nhau ra sao.

### ![](/icons/fx.webp) Thiết lập sẵn {#preset}
Khi chọn `Thiết lập sẵn...`, nhấn vào đồ thị đường cong sẽ mở ra một menu các thiết lập sẵn. Đường cong tròn sẽ cho kết quả mềm hơn, đường cong góc cạnh sẽ cho kết quả sắc nét hơn. Nút `Trừ` ở thanh công cụ bên trái sẽ đảo ngược độ giảm dần, để đỉnh của đường cong ấn lõm vào bề mặt thay vì kéo ra, hoặc ngược lại.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
Khi chọn chế độ này, bạn có thể tự vẽ đường cong giảm dần của mình. Trình sửa đường cong hoạt động giống như các đường cong ở những nơi khác trong Nomad:

* Nhấn vào đường cong để tạo một điểm mới
* Kéo một điểm để thay đổi vị trí của nó
* Nhấn vào một điểm để chuyển đổi giữa sắc nét và mượt
* Kéo một điểm vào điểm bên cạnh để xóa nó

### ![](/icons/curve_bspline.webp) B-spline {#b-spline}
Khi chọn chế độ này, bạn có thể tự vẽ đường cong giảm dần của mình. Trình sửa hoạt động giống như Catmull-Rom, nhưng các điểm chỉ kéo ảnh hưởng lên đường cong thay vì nằm ngay trên nó, giúp tạo ra những hình dạng đường cong mượt hơn.

### ![](/icons/curve_bevel.webp) Vát {#bevel}
Các điểm được nối bằng những đoạn thẳng, với các góc bo tròn có kích thước tùy theo độ nét của từng điểm. Rất tiện cho những cọ đầu phẳng có cạnh vát gọn gàng ở mép.

Trình sửa đường cong có 3 nút:

| Mục       | Biểu tượng                  | Mô tả                                                |
| :-------: | :-------------------------: | :--------------------------------------------------: |
| Phóng to  | ![](/icons/maximize.webp)  | Mở rộng trình sửa đường cong                         |
| Đặt lại   | ![](/icons/reset.webp)     | Đưa đường cong về trạng thái mặc định                |
| Đối xứng  | ![](/icons/symmetric.webp) | Hiển thị đường cong như một 'đầu cọ' đối xứng        |


### Ảnh hưởng {#influence}

* `Hình cầu` (3d) - Ảnh hưởng được tính bằng khoảng cách từ đỉnh đến tâm cọ.
* `Hình tròn` (2d) - Đỉnh trước tiên được chiếu lên mặt phẳng vùng tác động, rồi mới tính khoảng cách đến tâm cọ. Cách này tương tự cách alpha được lấy mẫu. 
* `Hình trụ` - Ảnh hưởng được chiếu xuyên qua vùng tác động theo dạng hình trụ. Điều này giống như bật [Hình bóng](#silhouette-1) bên dưới.
* `Gờ` - Độ giảm dần được đo theo chiều ngang của nét vẽ, nên đường cong trở thành mặt cắt ngang của toàn bộ nét vẽ. Khi đó nút `Đối Xứng` sẽ lật đối xứng mặt cắt qua nét vẽ: bạn chỉnh một bên và bên kia sẽ tự thay đổi theo. Khi tắt nút này, đường cong đi từ mép trái sang mép phải của nét vẽ. Không có sẵn cho các công cụ dựa trên làm phẳng.

### ![](/icons/silhouette.webp) Hình bóng {#silhouette-1}
Mặc định, nét vẽ chỉ tác động lên bề mặt mô hình nằm trong bán kính cọ. Khi bật hình bóng, nét vẽ sẽ được chiếu xuyên qua toàn bộ mô hình. Điều này rất hữu ích khi dựng khối ban đầu cho mô hình, hoặc với những hình dạng cần giữ các mặt bên vuông góc. Nó có các tùy chọn hướng chiếu giống như [Hình bóng](#silhouette) của tab Nét vẽ.



## ![](/icons/filter.webp) Bộ lọc {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Tích lũy nét vẽ {#accumulate-stroke}
Không giới hạn lượng vật liệu có thể đắp thêm/bớt đi trong mỗi nét vẽ. Ví dụ, công cụ `Đất sét` bật tùy chọn này, nên vật liệu có thể tiếp tục bồi đắp lên, trong khi công cụ `Cọ` tắt nó, nên nét vẽ sẽ ngừng đắp thêm vật liệu nếu bạn cứ di cùng một nét qua cùng một vùng của lưới. 

### ![](/icons/culling.webp) Chỉ đỉnh trước hướng camera {#front-facing-vertex-only}
Tùy chọn này sẽ bỏ qua các đỉnh quay mặt về phía sau.
Nó hữu ích khi bạn muốn vẽ màu lên một phần của hình học mỏng mà không ảnh hưởng đến mặt bên kia.
Nó cũng hoạt động khi điêu khắc, nhưng bạn có thể gặp một số lỗi hiển thị.

### ![](/icons/eye_open.webp) Chỉ đỉnh nhìn thấy {#visible-vertex-only}
Bỏ qua những đỉnh bị che khuất sau các bề mặt khác, khi nhìn từ camera. Tùy chọn này xuất hiện với các nét vẽ hình dạng (dây thòng lọng, hình chữ nhật...) của các công cụ mặt nạ, vẽ màu, `Nhóm mặt` và `Ẩn`.

### ![](/icons/dynamic.webp) Cho phép tô pô động {#allow-dynamic-topology}
Tùy chọn này chỉ có sẵn khi lưới của bạn ở chế độ [Tô pô động](topology.md#dynamic-topology). Bạn có thể tắt hoặc bật tô pô động cho từng công cụ.

### ![](/icons/connect.webp) Kết nối hình học {#connected-topology}
Chỉ điêu khắc những đỉnh được nối liền với bề mặt mà bạn chạm vào bằng công cụ. Ví dụ, khi dùng với công cụ `Di chuyển`, tùy chọn này cho phép bạn di chuyển một phần ngay cả khi nó giao cắt với một phần khác.
![](/videos/connected_topology.mp4)

### Bảo vệ khu vực {#protect-area}
![](/images/filter_protect_area.webp) 

Các tùy chọn này sẽ ngăn công cụ tác động lên một số phần của lưới trong những điều kiện khác nhau. Mỗi tùy chọn có thể đặt là `Tự động`, `Không` hoặc `Có`, và mũi tên nhỏ cho biết `Tự động` hiện đang tương ứng với giá trị nào.

* `Ẩn` - Nếu một số phần của lưới bị ẩn bằng công cụ ẩn, đặt xem chúng có được bảo vệ hay không. Ở chế độ `Tự động`, các mặt bị ẩn sẽ được bảo vệ, trừ khi khung lưới của chúng đang hiển thị (xem thiết lập [Khung lưới](settings.md#wireframe)).
* `Mặt nạ` - Nếu một số phần của lưới được phủ mặt nạ, đặt xem chúng có được bảo vệ hay không. Ở chế độ `Tự động`, các phần có mặt nạ sẽ được bảo vệ khi mặt nạ đang hiển thị trong menu [Tô bóng](shading).
* `Nhóm mặt` - Đặt xem bạn có chỉ được dùng công cụ bên trong nhóm mặt đầu tiên mà bạn chạm vào hay không. Ở chế độ `Tự động`, tùy chọn này theo việc nhóm mặt có đang hiển thị trong menu [Tô bóng](shading) hay không.

Nút `(Tất cả)` đặt xem các chế độ bảo vệ này là chung, dùng cho mọi công cụ, hay được đặt riêng cho từng công cụ.


### Lấy mẫu khu vực {#area-sampling}
Một số cọ hoặc tùy chọn nét vẽ cần một pháp tuyến mặt phẳng và một vị trí mặt phẳng trên bề mặt để hoạt động.

Bạn có thể điều khiển cách tính mặt phẳng trung bình này bằng cách đặt vùng lấy mẫu theo tỷ lệ so với bán kính công cụ.

Ở 100%, mọi điểm bên trong vòng tròn chọn đều được tính đến.

Ở 0%, chỉ đỉnh hoặc tam giác gần nhất được tính đến. Các giá trị này có thể được liên kết cho cả `Bán kính pháp tuyến` và `Bán kính vị trí`, hoặc mở khóa để đặt riêng từng cái.

### Bộ lọc pháp tuyến theo vùng {#keep-sharp-edges}
Loại trừ những điểm có pháp tuyến lệch quá nhiều so với pháp tuyến của bề mặt.

Nó sẽ thay đổi cách tính vùng mặt phẳng (Lấy mẫu khu vực), nên chủ yếu hữu ích cho các công cụ đất sét hoặc dựa trên làm phẳng, hoặc khi bạn muốn tô màu một bề mặt gần như phẳng mà không bị lem ra ngoài.

Hai góc `Tối thiểu` và `Tối đa` điều khiển độ chuyển tiếp giữa các điểm bị loại trừ và các điểm bị tác động hoàn toàn, như được thể hiện qua đĩa màu nhỏ bên cạnh chúng.

![](/videos/filter_keep_sharp_edges.mp4)

### Bộ lọc pháp tuyến cho độ rơi {#falloff-normal-filter}
Giống như [Bộ lọc pháp tuyến theo vùng](#keep-sharp-edges), nó loại trừ những điểm có pháp tuyến lệch quá nhiều so với pháp tuyến của bề mặt, nhưng nó tác động lên độ giảm dần của cọ thay vì lên phép tính mặt phẳng. Nó hữu ích khi vẽ màu cho các nếp gấp hoặc chỗ gồ lên.


### Bộ lọc độ sâu {#depth-masking}
![](/images/stroke_depthmask.webp)

Loại trừ những điểm nằm trên hoặc dưới một khoảng cách nhất định so với mặt phẳng đã tính (Lấy mẫu khu vực).

Bạn có thể dùng nó để chỉ vẽ màu lên những vùng gồ ghề, hoặc chỉ lên những vùng hốc lõm.

Đồ thị thể hiện một mặt cắt ngang của bề mặt; đường nằm ngang là vị trí của bề mặt, vòng tròn thể hiện bán kính giảm dần của nét vẽ màu ở trên và dưới bề mặt. `Độ lệch chiều cao` là tỷ lệ phần trăm phía trên hoặc phía dưới bề mặt để bắt đầu tính toán vùng loại trừ. Khi bật `Giảm độ sâu`, `Khu vực trên` và `Khu vực dưới` cho phép bạn co giãn độ giảm dần ở phía trên và phía dưới điểm lệch.

#### Ví dụ: Vẽ màu trong các hốc lõm {#example-paint-in-cavities}
Để chỉ vẽ màu ở những vùng hốc lõm, đặt độ lệch chiều cao là -100%, và chỉnh thanh trượt khu vực trên sao cho nó tách khỏi đường nằm ngang. Như vậy lần nhấn đầu tiên sẽ đặt độ sâu 'bằng không', và sau đó chỉ những vùng thấp hơn độ sâu này mới bị tác động.

![](/videos/stroke_depth_cavity.mp4)

#### Ví dụ: Vẽ màu lên chỗ gồ lên {#example-paint-on-bumps}
Để chỉ vẽ màu ở những vùng cao, đặt độ lệch chiều cao là +90%, để đáy của vòng tròn cắt đường nằm ngang một chút.  Khi bạn nhấn lên đỉnh của một vùng 'cao', độ sâu sẽ được đặt tại đó, để mọi thứ ở độ sâu đó, thấp hơn nó một chút, và mọi thứ cao hơn nó đều được vẽ màu. Những hốc lõm sâu sẽ bị bỏ qua.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Áp lực {#pressure}
![](/images/pressure_menu.webp) 

Điều khiển cách áp lực của bút cảm ứng tác động lên cọ.

### Sử dụng cài đặt toàn cầu {#use-global-settings}

Mặc định, `Sử dụng cài đặt toàn cầu` được bật, nghĩa là tất cả các cọ sẽ dùng chung các giá trị áp lực. Bỏ chọn nó để công cụ hiện tại có thiết lập áp lực riêng.

### ![](/icons/radius.webp) Bán kính {#pressure-radius}

Đường cong này điều khiển cách bán kính cọ thay đổi theo áp lực. Mặc định là quan hệ tuyến tính, nên nếu bút cảm ứng của bạn phản hồi mượt mà, sự thay đổi bán kính cũng sẽ có cảm giác mượt mà. Tuy vậy, nhiều bút cảm ứng có phản hồi phi tuyến, và bạn có thể bù trừ điều đó bằng đường cong này. Ví dụ, nếu bạn cảm thấy bán kính không đạt tới giá trị tối đa khi ấn mạnh, hãy dùng một đường cong thiết lập sẵn như 'out-pow3', với độ cong hướng lên trên, để bán kính tăng sớm hơn.

Hộp thoại này tương tự như phần hiển thị đường cong giảm dần: bạn có thể dùng thiết lập sẵn bằng cách chạm vào khung đường cong, hoặc tự vẽ đường cong với các chế độ `Catmull-Rom`, `B-spline` và `Vát`.

Nếu bạn muốn bán kính không đổi, hãy tắt phần này.

### ![](/icons/intensity.webp) Cường độ {#pressure-intensity}

Tương tự đường cong bán kính, nhưng dùng để điều khiển cường độ. Nếu bạn muốn cường độ không đổi, hãy tắt phần này.

### Giới hạn áp lực ở mức 100% {#limit-pressure}

Đảm bảo áp lực bút cảm ứng không bao giờ vượt quá 100%. Đây là thiết lập chung.

### Làm mượt áp lực {#pressure-smoothing}

Lấy trung bình các tín hiệu áp lực của bút cảm ứng để có kết quả mượt hơn.
