# ![](/icons/manual.webp) Mẹo

[[toc]]

## Cách bắt đầu một mẫu

Người mới bắt đầu điêu khắc 3D thường hỏi cách tốt nhất để bắt đầu một mẫu là gì. Không có cách tốt nhất, mỗi người có sở thích khác nhau. Dưới đây là một số cách tiếp cận phổ biến hơn.

### Điêu khắc trên hình cầu, multires

Mẫu mặc định khi Nomad khởi động là cách phổ biến nhất. Dùng các công cụ move, clay, crease để đẩy và kéo hình cầu thành hình dạng mong muốn, dùng các mức subdivision thấp khi bạn muốn thay đổi lớn nhanh chóng, dùng các mức subdivision cao hơn cho phần chi tiết.

Một vấn đề thường gặp là bạn sẽ thường thiếu polygon ở nơi cần, trong khi lại có quá nhiều polygon ở chỗ khác. Ví dụ nếu bạn đẩy hình cầu mặc định thành một cơ thể hoàn chỉnh, rất có thể bạn sẽ không có đủ chi tiết để làm ngón tay, trong khi lại có rất nhiều polygon lãng phí ở phía sau đầu. Tuy nhiên, với các hình dạng gần cầu như cái đầu thì điều này có thể chấp nhận được.

### Dyntopo

Bật Dyntopo sẽ tự động thêm và bớt polygon khi bạn điêu khắc. Các polygon này sẽ là tam giác, và người mới thường không thích bố cục lộn xộn so với vẻ gọn gàng của multires. Rất đáng để kiên trì! Nếu bạn bật smooth shading, tắt wireframe và ngừng lo lắng về bố cục, chế độ này có thể mang lại cảm giác rất giống đất sét. Đừng quên rằng nếu bạn dùng cọ lớn, hoặc cọ smooth, chế độ này cũng có thể loại bỏ polygon, nên công cụ luôn cảm giác nhanh và phản hồi tốt. Khi bạn đã hoàn thành bản dựng đầu tiên của khối điêu khắc, bạn có thể clone nó và chạy qua quad remesher để có bố cục đẹp, rồi reproject chi tiết gốc lên một mức subdivision cao.

### Voxel remesh

Voxel remesh sẽ áp dụng topology chủ yếu là quad lên khối điêu khắc của bạn. Thao tác này nhanh ở độ phân giải thấp, và có thể dùng để nhanh chóng thay thế các polygon bị kéo giãn hoặc quá dày bằng một bố cục phân bố đều. Đây có thể là cách tuyệt vời để bắt đầu một cơ thể hoàn chỉnh từ một hình cầu; giả sử bạn bắt đầu với cái đầu, bạn có thể kéo dài ra cổ, voxel remesh. Kéo dài ra thân, voxel remesh, tay, voxel remesh, v.v., cho đến khi bạn có các khối cơ bản.

### Dùng nhiều đối tượng

Nhiều tài liệu giải phẫu sẽ biểu diễn cơ thể bằng các khối cầu, trụ, lập phương đơn giản. Bạn cũng có thể điêu khắc theo cách này trong Nomad. Cách này có ưu điểm là cho phép bạn parent các đối tượng với nhau trong cây phân cấp cảnh, ví dụ bạn có thể xoay cổ và đầu sẽ đi theo. Khả năng dùng công cụ gizmo để tịnh tiến/xoay/tỷ lệ chính xác cũng rất hữu ích, và bạn cũng có thể đặt pivot cho từng khối để chúng di chuyển đúng như mong đợi. Khi các khối cơ bản đã ở đúng vị trí, bạn có thể chọn tất cả và voxel remesh hoặc boolean chúng thành một bề mặt duy nhất để điêu khắc chi tiết hơn.

Một mẹo hữu ích cho cách làm này là bắt đầu với một hình cầu, scale nó thành một “xúc xích” kéo dài, nhấn pivot, bấm 'bottom', nhấn pivot lần nữa. Giờ bạn có một bộ phận cơ thể có thể được clone, tịnh tiến dọc theo chiều dài của hình cầu đầu tiên, clone, xoay, clone, trượt, clone v.v... để bố trí cơ thể nhanh chóng.

### Tubes

Công cụ tube là một cách tuyệt vời để bắt đầu một khối điêu khắc. Đuôi bò sát, tay, chân, ngón tay, lông mày, tất cả đều có thể được phác nhanh bằng công cụ tube, rồi dễ dàng chỉnh sửa sau đó. Nó cũng cho phép bạn chỉnh tiết diện mặt cắt, giúp thay đổi hình dạng nhanh. Bạn có thể validate hình dạng để bắt đầu điêu khắc trên đó, và voxel remesh nó cùng với các đối tượng khác để có một mesh cơ thể hoàn chỉnh.

### Dùng ứng dụng khác

Một số người thích bắt đầu mẫu trong các ứng dụng khác, điều đó cũng ổn. Các công cụ như Blender hoặc Valence cho phép bắt đầu mẫu bằng kỹ thuật low poly, sau đó có thể import vào Nomad để điêu khắc.

### Dùng preset tích hợp sẵn

Từ menu project bấm `Preset...` ở góc trên bên phải. Ở đây bạn sẽ thấy một số preset hình đầu và cơ thể từ Blender Foundation. Chọn một cái bạn thích, chạm lại lần nữa, thêm vào cảnh của bạn. 

### Dùng mẫu online

Có rất nhiều mẫu miễn phí trên mạng, ví dụ polyhaven, sketchfab, turbosquid. Thông thường các mẫu này có thể import vào Nomad, và hoặc là điêu khắc trực tiếp trên đó, hoặc dùng làm tham chiếu.

### Không có luật lệ!

Cuối cùng thì bạn có thể dùng bất kỳ kết hợp nào của các kỹ thuật này, hoặc không dùng cái nào cả! Nomad rất linh hoạt ở điểm này, người dùng nâng cao có thể dùng tubes để bắt đầu, rồi dyntopo, rồi kết hợp với một bàn chân tải về, rồi quad remesh tất cả, rồi multires cho chi tiết cuối cùng. Cái gì phù hợp với bạn thì dùng.

## Facegroups

Công cụ facegroup có thể dùng cho nhiều việc, như được giải thích trong video youtube này: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Đây là tóm tắt bằng chữ các tính năng được đề cập trong video đó.

### Tại sao dùng facegroups?

Facegroups cho phép bạn tổ chức và chọn các mặt ('faces' và 'polygons' được dùng thay thế cho nhau trong tài liệu này). Điều này dễ giải thích hơn so với các công cụ chọn và tổ chức khác của Nomad. Nomad cho phép bạn tạo đối tượng, đặt tên, parent chúng, rất dễ để tạo cấu trúc đối tượng để định nghĩa một căn phòng gồm sàn, tường, ghế, bàn, v.v.

Với nhân vật bạn có thể dựng khối ban đầu bằng các đối tượng riêng cho đầu, tay, chân, nhưng khi bạn merge tất cả thành một mesh duy nhất, cấu trúc này bị mất. Bạn có thể làm việc trên các phần con của nhân vật bằng mask, nhưng sẽ mệt mỏi khi phải liên tục vẽ mask cho tay, rồi mũi, rồi lại tay.

Đây là lúc facegroups hữu ích. Nó cho phép bạn gắn nhãn các mặt polygon bằng một màu, rồi sau đó có thể chọn và thao tác các poly có cùng màu. Lưu ý màu facegroup và màu vertex là hai thứ khác nhau.

Ví dụ gần nhất là tô màu trên bản đồ, rồi sau đó có thể chọn quốc gia hoặc vùng dựa trên màu.

Với đầu nhân vật bạn có thể tô vùng để đánh dấu hốc mắt, mũi, môi, cằm, tai, rồi dễ dàng chọn các vùng đó sau này. Với điêu khắc hard surface và cơ khí, nó hữu ích để định nghĩa các panel và phần.

### Tạo và chỉnh sửa facegroups

Facegroups có thể được áp dụng bằng cọ, trong đó mỗi stroke mới tạo một facegroup mới, hoặc chúng có thể chọn facegroup dưới con trỏ và mở rộng nó. Chúng cũng có thể được tạo bằng các hình dạng.

* Dot, auto-pick bật - một lần kéo sẽ định nghĩa một màu facegroup mới và gán nó cho các mặt bạn kéo qua. Mỗi lần kéo mới sẽ định nghĩa một facegroup mới. Một lần chạm sẽ flood fill một facegroup mới.
* Dot, auto-pick tắt - khi nút auto-pick ở chế độ 'sub', nomad sẽ chọn facegroup dưới con trỏ, và áp dụng nó trong phần còn lại của lần kéo. Điều này hữu ích để tinh chỉnh facegroups mà không phải chọn thủ công.

### Masking

Khi công cụ mask đang hoạt động, và nút facegroup đang bật trên thanh công cụ của nó, chạm vào một facegroup sẽ mask nó.


### Ẩn

Khi công cụ hide đang hoạt động, và nút facegroup đang bật trên thanh công cụ của nó, chạm vào một facegroup sẽ ẩn nó.

### Tổ chức

Như đã đề cập, facegroups có thể dùng để tổ chức mesh của bạn mà không cần phải tạo các đối tượng riêng. Bạn có thể không muốn tách đầu thành các đối tượng riêng cho mũi, cằm, tai, nhưng việc có chúng được định nghĩa qua facegroups thì rất hữu ích.

### Vùng UV

Công cụ UV Atlas sẽ cố gắng tự động định nghĩa seam, nhưng đôi khi sẽ đặt seam ở nơi bạn không muốn. Nếu tồn tại facegroups trên một đối tượng, và tùy chọn facegroup đang bật trong tùy chọn UV Atlas, nó sẽ dùng biên facegroup làm UV seam thay thế.

### Quad remesher

Plugin quad remesher thường sẽ cho dòng cạnh chảy đẹp trên mẫu của bạn, nhưng bạn có thể dùng facegroups để giúp điều hướng nó khi tùy chọn facegroup được bật. Điều này có thể giúp dễ dàng định nghĩa dòng cạnh sạch quanh mắt, sống lông mày, môi, nếp gấp má chẳng hạn.

### Lọc với các công cụ khác

Nhiều công cụ sẽ có tùy chọn nhận biết facegroup, hoặc từ menu công cụ chính, hoặc qua menu stroke -> filtering. Ví dụ công cụ smooth ở cường độ trên 100% có thể làm mịn mạnh mẽ chi tiết bên trong một facegroup, nhưng giữ biên facegroup tương đối nguyên vẹn.

### Làm mượt và thư giãn biên facegroup

Tùy chọn relax trong công cụ facegroup làm rất tốt việc làm mượt biên facegroup trong khi giữ các đặc điểm khác nguyên vẹn. Đây có thể là cách tuyệt vời để định nghĩa vùng biên facegroup mượt trước khi quad remeshing.

## Hạn chế trên tablet/di động

Các tablet và điện thoại hiện nay rất mạnh, nhưng có những khác biệt quan trọng so với máy tính để bàn và laptop:

### Không có tản nhiệt chủ động

Máy tính có quạt và/hoặc tản nhiệt lớn để giữ mát, và được thiết kế để chạy ở nhiệt độ cao. Phần cứng di động thường được thiết kế ưu tiên độ mỏng, không phải để giúp làm mát linh kiện bên trong. Nếu Nomad bị đẩy lên thiết lập chất lượng cao nhất (chế độ chiếu sáng PBR, vật liệu phức tạp, nhiều đối tượng, nhiều tùy chọn hậu kỳ bật), điều này vừa có thể làm thiết bị quá nóng vừa làm pin tụt rất nhanh. 

Cách tốt hơn là dùng chế độ chiếu sáng matcap, và dùng hệ số render multiplier thấp hơn (trên cùng của menu post process). Những lựa chọn này sẽ giữ thiết bị mát và cho phép bạn điêu khắc lâu hơn.

### Bộ nhớ hạn chế

Nomad có thể đạt kết quả ngang với hầu hết ứng dụng điêu khắc trên desktop, nhưng nó không thể bẻ cong các định luật vật lý! Hầu hết máy tính để bàn có gấp đôi bộ nhớ so với thiết bị di động, workstation dựng cho hoạt hình 3D thường có gấp 4 hoặc 8 lần bộ nhớ. Vì vậy, tốt là bạn nên để ý mình đang dùng bao nhiêu polygon, chạy vài thử nghiệm trên thiết bị để xem khi nào nó bắt đầu lag. Gần như mọi thiết bị chạy được Nomad đều xử lý 1 triệu polygon khá dễ dàng. Một Ipad Pro M2 có thể xử lý 8 triệu thoải mái, mọi người đã thử trên các Ipad mới nhất và vượt xa con số đó.

Tuy vậy, chỉ những khối điêu khắc cực kỳ chi tiết mới cần hơn 4 triệu poly; nếu bạn làm các đối tượng tương đối đơn giản mà thường xuyên vượt 500.000, 1 triệu, 4 triệu, là bạn đang dùng quá nhiều polygon! Hãy chắc chắn bạn đã bật chế độ smooth shaded trong tùy chọn.

### Hệ điều hành kém “dễ tính” với ứng dụng nặng

Apple và Android kỳ vọng ứng dụng sẽ lưu và tải file nhỏ rất nhanh. Chúng cũng giả định ứng dụng có thể chuyển tác vụ rất nhanh. Một lần nữa, Nomad làm vài mẹo thông minh để giữ kích thước file tương đối nhỏ và lưu rất nhanh, nhưng nếu hệ điều hành di động quyết định Nomad mất quá nhiều thời gian, nó sẽ đơn giản kill ứng dụng trước khi hoàn thành tác vụ. Đây là một lý do khác để giữ file ở phía nhỏ; có thể làm việc với khối điêu khắc 37 triệu poly như một người dùng báo cáo trên discord, nhưng không được khuyến khích!

## Làm việc trên màn hình nhỏ

Nomad được thiết kế để hoạt động trên tablet, nhưng cũng hoạt động tốt trên điện thoại. Điêu khắc trên màn hình nhỏ như điện thoại có thể dễ hơn với vài tinh chỉnh UI và quy trình:

* Chạm 4 ngón sẽ bật/tắt toàn bộ UI, cho bạn nhiều không gian điêu khắc hơn.
* Kéo 3 ngón lên xuống sẽ thay đổi bán kính cọ
* Tỷ lệ UI có thể làm nhỏ để vừa nhiều nút hơn nếu bạn mắt tốt, hoặc to hơn nếu bạn mắt kém!
* Các menu rộng đôi khi che khuất khối điêu khắc, bạn có thể làm chúng trong suốt và không blur để nhìn thấy khối bên dưới menu.
* Nếu điêu khắc bằng ngón tay, dùng tùy chọn offset để di chuyển tâm cọ ra xa ngón tay một chút.
* Những tùy chọn này và nhiều hơn nữa có thể tìm thấy trong [Interface menu](./interface.md). 


## Inflate hoặc peak deformer

Nhiều ứng dụng 3D có deformer inflate, sẽ đẩy tất cả vertex theo normal của chúng một lượng có thể điều chỉnh. Trong khi Nomad hiện chưa có deformers, có thể mô phỏng hành vi này bằng cọ inflate:

* Chọn cọ inflate
* Từ [Stroke menu](./stroke.md#stroke) đổi phương thức stroke sang `Lock + Radius'
* Làm bán kính cọ lớn hơn khối điêu khắc của bạn, zoom camera lùi xa khối nếu cần.
* Click rồi kéo một stroke trên bề mặt đối tượng; khi bán kính lớn hơn đối tượng, toàn bộ hình dạng sẽ được inflate đều với một lượng cố định.
* Điều chỉnh cường độ cọ để kiểm soát lượng inflate
* Dùng masking nếu cần để bảo vệ hoặc giảm hiệu ứng inflate ở một số vùng.

## Loại bỏ cục u hoặc 'mụn' sau thao tác voxel remesh

Voxel remesh rất tốt để tạo polygon phân bố đều, nhưng đôi khi tạo topology gây ra các cục u nhỏ hoặc mụn khi làm mịn. Ví dụ:

* Dùng cọ crease trên hình cầu mặc định và vẽ một đường xoáy
* Voxel remesh với 'build multiresolution at 3'
* Smooth với cường độ cao
* xuất hiện artifacts (dễ thấy hơn với vật liệu matcap tương phản cao):

![](/videos/tip_pimples_before.mp4)

Để sửa bằng điêu khắc, thử tùy chọn `Stable smoothing` trong thiết lập smooth. Tùy chọn này có thể xử lý bố cục topology không đều của voxel remesh, và cho kết quả sạch.

![](/videos/tip_pimples_stable_smooth.mp4)

Để sửa chính topology, dùng một primitive mới, hoặc công cụ quad remesh, hoặc một phần mềm 3D bên ngoài, và project chi tiết từ mesh gốc sang mesh mới qua `Topology -> Misc -> Reproject`. 

![](/videos/tip_pimples_reproject.mp4)

## Chiếu sáng ban ngày

Render PBR mặc định, đúng như tên gọi, là dựa trên vật lý, giống như một bức ảnh số chưa xử lý có thể trông hơi nhạt và phẳng. Đèn và hậu kỳ của Nomad có thể dùng để làm render trông sống động hơn.

Đây là một render mặc định, hãy xem ta có thể làm nó trông đẹp hơn không:
![](/images/tips_lighting_default.webp)

Bật post processing và tonemapping có thể thêm độ sáng và tương phản:

![](/images/tips_lighting_tonemap.webp)

Để tập trung vào đèn, đèn môi trường mặc định tốt cho điêu khắc, nhưng có thể cải thiện cho render cuối. Một cách nghĩ về điều này là tách ánh sáng trực tiếp (ví dụ mặt trời) và ánh sáng môi trường (ví dụ ánh sáng từ màu xanh của bầu trời, mặt đất). Bằng cách giảm ánh sáng môi trường và xoay nó, điều này bắt đầu mô phỏng ánh sáng sẽ trông như thế nào nếu chủ thể ở vùng bóng râm:

![](/images/tips_lighting_env.webp)

Có thể thêm một direct light, và tăng cường độ của nó để mô phỏng ánh nắng gắt. Cân bằng nó với ánh sáng môi trường sẽ đạt kết quả dễ chịu:

![](/images/tips_lighting_sunlight.webp)

Nhân vật có thể hưởng lợi từ việc đổi vật liệu sang subsurface, và đặt một spotlight phía sau nhân vật chiếu vào tai để làm chúng phát sáng:

![](/images/tips_lighting_sss.webp)

Sau đó hãy thử nghiệm với phần còn lại của thiết lập post process! Global Illumination và Ambient Occlusion giúp chiếu sáng thực tế hơn. Curvature và Sharpen có thể giúp làm nổi chi tiết điêu khắc. Chromatic Aberration, Depth of Field, Grain, Bloom, Vignette giúp mô phỏng hiệu ứng máy ảnh. Lưu ý khi bật thêm tính năng, cần điều chỉnh lại ánh sáng và các giá trị hậu kỳ khác để bù trừ.

Đây là render với bộ tinh chỉnh hậu kỳ đầy đủ:
![](/images/tips_lighting_final.webp)
