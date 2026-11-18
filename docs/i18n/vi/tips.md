# ![](/icons/manual.webp) Mẹo {#tips}

[[toc]]

## Cách bắt đầu một mô hình {#how-to-start-a-model}

Người mới làm quen với điêu khắc 3d thường hỏi đâu là cách tốt nhất để bắt đầu một mô hình. Không có cách nào là tốt nhất cả, mỗi người có sở thích riêng. Dưới đây là một số cách tiếp cận phổ biến.

### Điêu khắc trên hình cầu, đa phân giải {#sculpt-on-sphere-multires}

Mô hình mặc định khi Nomad khởi động là cách phổ biến nhất. Dùng các công cụ di chuyển, đất sét, rãnh sắc để đẩy và kéo hình cầu thành hình, dùng các cấp chia nhỏ thấp khi bạn muốn thay đổi lớn một cách nhanh chóng, và các cấp chia nhỏ cao hơn khi làm chi tiết.

Một vấn đề thường gặp là bạn sẽ hay thiếu đa giác ở chỗ cần, trong khi lại thừa đa giác ở chỗ khác. Ví dụ, nếu bạn đẩy hình cầu mặc định thành cả một cơ thể, nhiều khả năng bạn sẽ không đủ chi tiết để làm các ngón tay, trong khi lại có rất nhiều đa giác lãng phí ở phía sau đầu. Tuy nhiên, với những hình dạng gần như hình cầu như một cái đầu, cách này hoàn toàn ổn.

### DynTopo {#dyntopo}

Bật DynTopo sẽ tự động thêm và bớt đa giác theo nhu cầu khi bạn điêu khắc. Các đa giác này là tam giác, và người mới thường không thích cách bố trí lộn xộn của chúng so với vẻ gọn gàng của đa phân giải. Nhưng rất đáng để kiên trì! Nếu bạn bật tô bóng mượt, tắt khung lưới và thôi bận tâm về cách bố trí, chế độ này có thể mang lại cảm giác rất giống nặn đất sét. Đừng quên rằng nếu bạn dùng cọ lớn hoặc cọ làm mịn, chế độ này cũng có thể bớt đa giác đi, nên công cụ luôn nhanh và phản hồi tốt. Khi đã xong lượt điêu khắc đầu tiên, bạn có thể nhân bản nó và cho chạy qua quad remesher để có cách bố trí đẹp, rồi chiếu lại các chi tiết gốc lên một cấp chia nhỏ cao.

### Lưới lại voxel {#voxel-remesh}

Lưới lại voxel sẽ áp một cấu trúc chủ yếu là tứ giác lên tác phẩm điêu khắc của bạn. Thao tác này nhanh ở độ phân giải thấp, và có thể dùng để nhanh chóng thay thế những đa giác bị kéo giãn hoặc quá dày đặc bằng một cách bố trí cách đều. Đây có thể là một cách tuyệt vời để bắt đầu cả một cơ thể từ một hình cầu; giả sử bạn bắt đầu với cái đầu, bạn có thể kéo dài ra một cái cổ, lưới lại voxel. Kéo ra phần thân, lưới lại voxel, rồi tay, lưới lại voxel, và cứ thế, cho đến khi bạn có các hình khối cơ bản.

### Dùng nhiều đối tượng {#use-multiple-objects}

Nhiều tài liệu giải phẫu thể hiện cơ thể bằng những hình cầu, hình trụ, hình hộp đơn giản. Bạn cũng có thể điêu khắc theo cách này trong Nomad. Ưu điểm là bạn có thể gắn các đối tượng làm cha con với nhau trong cây phân cấp của cảnh, chẳng hạn khi xoay cổ thì đầu sẽ xoay theo. Việc dùng được công cụ gizmo để di chuyển/xoay/co giãn chính xác cũng rất hữu ích, và bạn còn có thể đặt trục xoay cho từng hình để chúng chuyển động đúng như bạn mong muốn. Khi các khối cơ bản đã ở đúng chỗ, bạn có thể chọn tất cả rồi lưới lại voxel hoặc boolean chúng thành một bề mặt duy nhất để điêu khắc chi tiết hơn.

Một mẹo tiện lợi cho cách làm này là bắt đầu với một hình cầu, co giãn nó thành hình như khúc xúc xích, nhấn trục xoay, nhấn 'đáy', rồi nhấn trục xoay lần nữa. Giờ bạn đã có một bộ phận cơ thể có thể nhân bản, di chuyển dọc theo chiều dài của hình cầu đầu tiên, nhân bản, xoay, nhân bản, trượt, nhân bản, v.v... để dựng bố cục cơ thể thật nhanh.

### Ống {#tubes}

Công cụ ống là một cách tuyệt vời để bắt đầu một tác phẩm điêu khắc. Đuôi bò sát, tay, chân, ngón tay, lông mày, tất cả đều có thể được phác thảo nhanh bằng công cụ ống, rồi dễ dàng chỉnh sửa sau đó. Nó còn cho phép bạn thay đổi mặt cắt, giúp đổi hình dạng thật nhanh. Bạn có thể xác nhận hình dạng để bắt đầu điêu khắc trên đó, và lưới lại voxel nó cùng các đối tượng khác để có lưới của cả cơ thể.

### Dùng các ứng dụng khác {#use-other-apps}

Một số người thích bắt đầu mô hình trong các ứng dụng khác, điều đó cũng hoàn toàn ổn. Những công cụ như Blender hay Valence cho phép bắt đầu mô hình bằng các kỹ thuật low poly, sau đó có thể nhập vào Nomad để điêu khắc.

### Dùng các thiết lập sẵn có {#use-the-built-in-presets}

Từ menu [Tệp tin](files.md), nhấn `Thiết lập sẵn…` ở bên trái phần dự án. Tại đây bạn sẽ thấy một số mẫu đầu và cơ thể có sẵn từ Blender Foundation. Chọn một mẫu bạn thích, chạm vào nó lần nữa, rồi thêm vào cảnh. 

### Dùng mô hình trên mạng {#use-online-models}

Có rất nhiều mô hình miễn phí trên mạng, ví dụ polyhaven, sketchfab, turbosquid. Thường thì các mô hình này có thể được nhập vào Nomad, rồi điêu khắc trực tiếp hoặc dùng làm tham khảo.

### Không có quy tắc nào cả! {#no-rules}

Rốt cuộc, bạn có thể kết hợp bất kỳ kỹ thuật nào trong số này, hoặc chẳng dùng cái nào cả! Nomad rất linh hoạt về mặt này: người dùng nâng cao có thể bắt đầu bằng ống, rồi DynTopo, rồi ghép với một bàn chân tải về, rồi quad remesh tất cả, rồi dùng đa phân giải cho chi tiết cuối cùng. Cách nào hợp với bạn là được.

## Nhóm mặt {#facegroups}

Công cụ nhóm mặt có thể dùng cho rất nhiều việc, như được giải thích trong video youtube này: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Đây là bản tóm tắt bằng chữ các tính năng được trình bày trong video đó.

### Tại sao dùng nhóm mặt? {#why-facegroups}

Nhóm mặt cho phép bạn sắp xếp và chọn các mặt ('mặt' và 'đa giác' được dùng thay thế cho nhau trong hướng dẫn này). Để dễ giải thích, hãy so sánh với các công cụ chọn và sắp xếp khác của Nomad. Nomad cho phép bạn tạo đối tượng, đặt tên, gắn cha con cho chúng, nên rất dễ tạo một cấu trúc đối tượng để mô tả một căn phòng gồm sàn, tường, ghế, bàn, v.v.

Với một nhân vật, bạn có thể dựng khối ban đầu bằng các đối tượng riêng cho đầu, tay, chân, nhưng một khi đã gộp tất cả thành một lưới duy nhất, cấu trúc này sẽ mất đi. Bạn có thể làm việc trên từng phần của nhân vật bằng mặt nạ, nhưng cứ phải tô mặt nạ cho bàn tay, rồi cái mũi, rồi lại bàn tay thì khá mệt.

Đây là lúc nhóm mặt phát huy tác dụng. Nó cho phép bạn gắn màu cho các mặt đa giác, rồi chọn và thao tác với những đa giác có cùng màu. Lưu ý rằng màu nhóm mặt và màu đỉnh là hai thứ khác nhau.

Cách so sánh gần nhất là tô màu lên một tấm bản đồ, rồi sau đó có thể chọn các quốc gia hay khu vực dựa trên màu.

Với đầu nhân vật, bạn có thể tô các vùng để đánh dấu hốc mắt, mũi, môi, cằm, tai, rồi sau đó dễ dàng chọn lại các vùng đó. Với điêu khắc bề mặt cứng và cơ khí, nó hữu ích để xác định các tấm và các phần.

### Tạo và chỉnh sửa nhóm mặt {#creating-and-editing-facegroups}

Nhóm mặt có thể được áp bằng cọ, trong đó mỗi nét vẽ mới tạo ra một nhóm mặt mới, hoặc có thể chọn nhóm mặt dưới con trỏ rồi mở rộng nó. Chúng cũng có thể được tạo bằng các hình dạng.

* Điểm, chế độ mặc định - một lần kéo sẽ xác định một màu nhóm mặt mới và gán nó cho các mặt mà bạn kéo qua. Mỗi lần kéo mới sẽ xác định một nhóm mặt mới. Một lần chạm sẽ tô loang một nhóm mặt mới.
* Điểm, chế độ `Chọn` - khi nút `Chọn` trên thanh công cụ bên trái được bật, nomad sẽ chọn nhóm mặt dưới con trỏ, và áp nó trong suốt phần còn lại của lần kéo. Điều này hữu ích để tinh chỉnh nhóm mặt mà không phải chọn chúng thủ công.

### Tô mặt nạ {#masking}

Khi công cụ mặt nạ đang hoạt động, và nút nhóm mặt trên thanh công cụ của nó được bật, chạm vào một nhóm mặt sẽ phủ mặt nạ lên nó.


### Ẩn {#hiding}

Khi công cụ ẩn đang hoạt động, và nút nhóm mặt trên thanh công cụ của nó được bật, chạm vào một nhóm mặt sẽ ẩn nó.

### Sắp xếp {#organizing}

Như đã nói ở trên, nhóm mặt có thể dùng để sắp xếp lưới của bạn mà không cần tách thành các đối tượng riêng. Có thể bạn không muốn tách đầu thành các đối tượng riêng cho mũi, cằm, tai, nhưng việc xác định chúng bằng nhóm mặt lại rất hữu ích.

### Vùng UV {#uv-regions}

Công cụ UV Atlas sẽ cố gắng tự động xác định các đường nối, nhưng đôi khi sẽ đặt đường nối ở chỗ bạn không muốn. Nếu đối tượng có nhóm mặt, và tùy chọn nhóm mặt được bật trong các tùy chọn UV Atlas, nó sẽ dùng đường viền của nhóm mặt làm đường nối UV thay thế.

### Quad remesher {#quad-remesher}

Plugin quad remesher thường tạo dòng chảy cạnh đẹp trên mô hình của bạn, nhưng bạn có thể dùng nhóm mặt để giúp định hướng nó khi bật tùy chọn nhóm mặt. Điều này giúp dễ dàng tạo dòng chảy cạnh gọn gàng quanh mắt, gờ lông mày, môi, hay nếp gấp má chẳng hạn.

### Lọc với các công cụ khác {#filter-with-other-tools}

Nhiều công cụ có tùy chọn nhận biết nhóm mặt, hoặc ngay trong menu công cụ chính của chúng, hoặc qua menu Nét vẽ -> Bộ lọc. Ví dụ, công cụ làm mịn ở độ mạnh trên 100% có thể làm mịn mạnh tay các chi tiết bên trong một nhóm mặt, nhưng vẫn giữ đường viền nhóm mặt tương đối nguyên vẹn.

### Thư giãn và làm mịn đường viền nhóm mặt {#relax-and-smooth-facegroup-borders}

Tùy chọn `Thư giãn` trong công cụ nhóm mặt làm rất tốt việc làm mịn đường viền nhóm mặt mà vẫn giữ nguyên các chi tiết khác. Đây có thể là một cách tuyệt vời để tạo những vùng đường viền nhóm mặt mượt mà trước khi quad remesh.

## Giới hạn trên máy tính bảng/điện thoại {#limitations-on-tabletmobile}

Máy tính bảng và điện thoại ngày nay rất mạnh, nhưng có những khác biệt quan trọng so với máy tính để bàn và máy tính xách tay:

### Không có tản nhiệt chủ động {#no-active-cooling}

Máy tính có quạt và/hoặc tản nhiệt lớn để giữ mát, và được thiết kế để chạy ở nhiệt độ cao. Phần cứng di động thường được thiết kế ưu tiên độ mỏng trước, chứ không phải để giữ mát cho linh kiện bên trong. Nếu Nomad bị đẩy lên các thiết lập chất lượng cao nhất (chế độ chiếu sáng PBR, vật liệu phức tạp, nhiều đối tượng, bật nhiều tùy chọn hậu kỳ), thiết bị có thể vừa quá nhiệt vừa hết pin rất nhanh. 

Cách tốt hơn là dùng chế độ chiếu sáng matcap, và dùng `Độ phân giải render` thấp hơn (ở đầu menu hậu kỳ). Những lựa chọn này sẽ giữ thiết bị mát và cho phép bạn điêu khắc lâu hơn.

### Bộ nhớ có hạn {#limited-memory}

Nomad có thể đạt kết quả ngang với hầu hết các ứng dụng điêu khắc trên máy tính, nhưng nó không thể bẻ cong các định luật vật lý! Hầu hết máy tính để bàn có bộ nhớ gấp đôi thiết bị di động, còn các máy trạm dành cho làm hoạt hình 3d thường có bộ nhớ gấp 4 hoặc 8 lần. Vì vậy, bạn nên để ý số lượng đa giác mình đang dùng, và chạy thử vài bài kiểm tra trên thiết bị để xem khi nào nó bắt đầu giật. Gần như mọi thiết bị chạy được Nomad đều xử lý 1 triệu đa giác khá dễ dàng. Một chiếc iPad Pro M2 có thể xử lý thoải mái 8 triệu, và đã có người thử trên những chiếc iPad mới nhất với số lượng cao hơn thế nhiều.

Tuy vậy, chỉ những tác phẩm điêu khắc chi tiết nhất mới cần hơn 4 triệu đa giác; nếu bạn làm những đối tượng tương đối đơn giản mà thường xuyên vượt quá 500.000, 1 triệu, 4 triệu, thì bạn đang dùng quá nhiều đa giác! Hãy đảm bảo bạn đã bật `Tô bóng mượt` trong phần [Cài đặt](settings.md).

### Hệ điều hành khắt khe hơn với các ứng dụng nặng {#os-is-less-forgiving-with-intensive-apps}

Apple và Android mong đợi các ứng dụng lưu và mở những tệp nhỏ rất nhanh. Chúng cũng cho rằng các ứng dụng có thể chuyển đổi tác vụ rất nhanh. Một lần nữa, Nomad dùng một số thủ thuật khéo léo để giữ dung lượng tệp tương đối nhỏ và lưu chúng rất nhanh, nhưng nếu hệ điều hành di động cho rằng Nomad mất quá nhiều thời gian, nó sẽ đơn giản là tắt Nomad trước khi tác vụ hoàn tất. Đây là một lý do nữa để giữ tệp ở mức nhỏ; có thể làm việc với tác phẩm điêu khắc 37 triệu đa giác như một người dùng đã kể trên discord, nhưng điều đó không được khuyến khích!

## Làm việc trên màn hình nhỏ {#working-on-small-screens}

Nomad được thiết kế để dùng trên máy tính bảng, nhưng cũng hoạt động tốt trên điện thoại. Điêu khắc trên màn hình nhỏ như điện thoại có thể dễ dàng hơn với vài điều chỉnh về giao diện và quy trình làm việc:

* Chạm bằng 4 ngón tay sẽ ẩn/hiện toàn bộ giao diện, cho bạn thêm không gian để điêu khắc.
* Kéo lên xuống bằng 3 ngón tay sẽ thay đổi bán kính cọ
* Bạn có thể thu nhỏ tỷ lệ giao diện để chứa thêm nút nếu mắt bạn tinh, hoặc phóng to nếu mắt bạn kém!
* Các menu rộng đôi khi có thể che mất tác phẩm điêu khắc; bạn có thể làm chúng trong suốt và không làm mờ để nhìn thấy tác phẩm bên dưới menu.
* Nếu điêu khắc bằng ngón tay, hãy dùng tùy chọn [`Độ lệch nét vẽ`](stroke.md#stroke-offset) để dời tâm cọ ra xa ngón tay một chút.
* Những tùy chọn này và nhiều tùy chọn khác có trong [menu Giao diện](./interface.md). 


## Bộ biến dạng bơm phồng hoặc đẩy đỉnh {#inflate-or-peak-deformer}

Nhiều ứng dụng 3d có bộ biến dạng bơm phồng, giúp đẩy tất cả các đỉnh theo pháp tuyến của chúng một lượng có thể điều chỉnh. Tuy Nomad hiện chưa có bộ biến dạng, bạn vẫn có thể mô phỏng hành vi này bằng cọ bơm phồng:

* Chọn cọ bơm phồng
* Từ [menu Nét vẽ](./stroke.md#stroke), đổi kiểu nét vẽ thành `Khóa + bán kính`
* Đặt bán kính cọ lớn hơn tác phẩm điêu khắc, kéo camera ra xa tác phẩm nếu cần.
* Nhấn rồi kéo một nét vẽ trên bề mặt đối tượng; khi bán kính lớn hơn đối tượng, toàn bộ hình dạng sẽ được bơm phồng đều một lượng cố định.
* Chỉnh cường độ cọ để điều khiển mức bơm phồng
* Dùng mặt nạ nếu cần để bảo vệ hoặc giảm hiệu ứng bơm phồng ở một số vùng.

## Xóa các cục u hoặc 'mụn' sau thao tác lưới lại voxel {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Lưới lại voxel rất tuyệt để tạo các đa giác cách đều, nhưng đôi khi tạo ra cấu trúc lưới gây nên những cục u hay mụn nhỏ khi làm mịn. Ví dụ:

* Dùng cọ rãnh sắc trên hình cầu mặc định và vẽ một đường xoắn
* Lưới lại voxel với `Tạo dựng đa độ phân giải` ở mức 3
* Làm mịn với cường độ cao
* các lỗi xuất hiện (dễ thấy hơn với một vật liệu matcap có độ tương phản cao):

![](/videos/tip_pimples_before.mp4)

Để sửa bằng cách điêu khắc, hãy thử tùy chọn `Làm mịn ổn định` trong thiết lập làm mịn. Nó có thể xử lý cách bố trí lưới không đều của lưới lại voxel, và cho kết quả sạch sẽ.

![](/videos/tip_pimples_stable_smooth.mp4)

Để sửa chính cấu trúc lưới, hãy dùng một khối cơ bản mới, hoặc các công cụ quad remesh, hoặc một phần mềm dựng hình 3d bên ngoài, rồi chiếu chi tiết từ lưới gốc sang lưới mới qua `Tô pô -> Bake -> Chiếu lại → Đỉnh`. 

![](/videos/tip_pimples_reproject.mp4)

## Chiếu sáng ban ngày {#daylight-lighting}

Bản kết xuất PBR mặc định, đúng như tên gọi, dựa trên vật lý, nên giống như một bức ảnh kỹ thuật số chưa qua xử lý, nó có thể trông hơi nhạt và phẳng. Đèn và hậu kỳ của Nomad có thể giúp bản kết xuất trông sống động hơn.

Đây là một bản kết xuất mặc định, hãy xem liệu chúng ta có thể làm nó đẹp hơn không:
![](/images/tips_lighting_default.webp)

Bật hậu kỳ và tone mapping có thể tăng độ sáng và độ tương phản:

![](/images/tips_lighting_tonemap.webp)

Nói về đèn, đèn môi trường mặc định rất tốt để điêu khắc, nhưng có thể cải thiện cho bản kết xuất cuối cùng. Một cách để suy nghĩ về điều này là tách ánh sáng trực tiếp (ví dụ mặt trời) với ánh sáng môi trường (ví dụ ánh sáng từ màu xanh của bầu trời, từ mặt đất). Bằng cách giảm ánh sáng môi trường và xoay nó, ta bắt đầu có được ánh sáng trông như khi chủ thể ở trong bóng râm:

![](/images/tips_lighting_env.webp)

Có thể thêm một đèn trực tiếp và tăng cường độ của nó để mô phỏng ánh nắng gắt. Cân bằng nó với ánh sáng môi trường sẽ cho kết quả dễ chịu:

![](/images/tips_lighting_sunlight.webp)

Nhân vật có thể đẹp hơn khi đổi vật liệu sang tán xạ dưới bề mặt (subsurface), và đặt một đèn rọi phía sau nhân vật chiếu vào tai để làm chúng ửng sáng:

![](/images/tips_lighting_sss.webp)

Sau đó hãy thử nghiệm với các thiết lập hậu kỳ còn lại! Chiếu sáng toàn cầu và Ambient Occlusion giúp ánh sáng chân thực hơn. Độ cong và Làm sắc nét giúp làm nổi bật thêm chi tiết của tác phẩm điêu khắc. Quang sai màu, Độ sâu trường ảnh, Hạt nhiễu, Bloom, Vignette giúp mô phỏng các hiệu ứng máy ảnh. Lưu ý rằng khi bật thêm tính năng, bạn cần điều chỉnh ánh sáng và các giá trị hậu kỳ khác để bù lại.

Đây là bản kết xuất với đầy đủ các tinh chỉnh hậu kỳ:
![](/images/tips_lighting_final.webp)
