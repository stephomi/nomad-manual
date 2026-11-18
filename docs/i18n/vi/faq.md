# ![](/icons/faq.webp) Câu hỏi thường gặp {#faq}

[[toc]]

## Nền tảng {#platform}
### Các dự án của tôi nằm ở đâu trên thiết bị? {#locate}
Các dự án nằm trong thư mục `projects` bên trong thư mục chính của Nomad.

Trên iOS, bạn có thể truy cập thư mục Nomad bằng ứng dụng Tệp (Files) của iOS.

Trên Android, thư mục Nomad nằm ở `Android/data/com.stephaneginier.nomad/files/`.  
Trên các phiên bản Android gần đây (10/11), bạn không còn truy cập được thư mục `Android/data`nữa.
Bạn có thể truy cập nó qua một ứng dụng riêng, ví dụ [ứng dụng này](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Có cách nào để dùng thử bản beta không? {#beta}
Với Windows và MacOS, bản beta có thể có sẵn trên [Trang chủ](https://nomadsculpt.com).
<br>
Với iOS, có một nhóm TestFlight riêng, hãy vào kênh #beta-ios trên [Discord](https://discord.com/invite/8h7BwpRz29).
<br>
[Bản demo trên web](https://nomadsculpt.com/demo) thường được cập nhật các tính năng mới nhất.

### Tại sao có bản dùng thử miễn phí trên Android? Mà không có trên iOS? {#android-trial}
Vì các thiết bị Android cũ chạy rất tệ (và cả một số thiết bị mới nữa...), và tôi không muốn mọi người mua ứng dụng rồi chỉ nhận được một màn hình đen.
Nhưng lý do chính là tôi cảm thấy ứng dụng trả phí trên Android không thực sự phổ biến.

### Máy tính bảng nào tốt nhất để chạy Nomad? {#best-tablet}

Nói ngắn gọn: Một chiếc iPad.

Câu trả lời dài hơn một chút là 

> "Chiếc iPad mới nhất _mà bạn đủ tiền mua_, trừ khi bạn thực sự ghét Apple, khi đó là chiếc máy tính bảng Samsung mới nhất mà bạn đủ tiền mua. Còn lại thì hãy thử trước." 

Mọi người luôn muốn biết thêm thông tin, nên đây là phần tóm tắt.

Nomad chạy tốt nhất trên các iPad đời mới:

* iPad và iPhone có thể dùng plugin [Quad Remesher](tools#quad-remesher) của [Exoside](https://exoside.com/)
* các iPad gần đây với bút Pencil mới nhất hỗ trợ [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), cho phép bạn xoay thân bút trong một số công cụ của Nomad. 
* hiệu năng của các chip dòng M mới nhất rất nhanh. 

Chiếc iPad mới nhất và đắt nhất hiện có sẽ kết xuất ảnh cuối cùng rất nhanh, và cho phép bạn điêu khắc rất nhiều chi tiết.

Tuy nhiên, mức giảm hiệu năng trên các iPad rẻ hơn và cũ hơn không tệ như mọi người nghĩ. Bất kỳ iPad nào hỗ trợ Apple Pencil đều chạy Nomad khá tốt. Ví dụ:

* Một chiếc iPad Pro đời 2023 có thể xử lý tác phẩm điêu khắc 5 triệu đa giác mà vẫn mượt, và kết xuất một ảnh chất lượng cuối cùng trong 5 giây.
* Một chiếc iPad Pro đời 2015 có thể xử lý một đối tượng 1,2 triệu đa giác với chút giật lag, và kết xuất một ảnh chất lượng cuối cùng trong 20 giây.

Đó là một khác biệt hiệu năng lớn, nhưng bạn cũng phải tính đến giá cả:

* iPad Pro 2025 mới tinh với đầy đủ tùy chọn có giá *2500 USD*. 
* iPad Pro 2023 hiện có giá *400 USD* trên eBay.
* iPad Pro 2015 có giá *250 USD* trên eBay.

Có thêm 4 triệu đa giác và tiết kiệm 15 giây có đáng 2100 USD không? Điều đó tùy bạn quyết định.

Các mẫu không phải Pro còn rẻ hơn nữa, và cho bạn nhiều lựa chọn về kích thước và hiệu năng. iPad Air hiện tại hỗ trợ bút Pencil thế hệ 2 với barrel roll, và rẻ hơn đáng kể so với bản Pro. Thị trường máy cũ và máy tân trang còn có nhiều lựa chọn hơn nữa. 

Điều này có nghĩa là dù ngân sách của bạn thế nào, bạn cũng sẽ tìm được một chiếc iPad phù hợp. Và hãy nhớ rằng hầu hết các tác phẩm điêu khắc không cần đến hàng triệu đa giác! Nếu bạn giữ được dưới 500.000 đa giác, ngay cả những chiếc iPad cũ cũng cho phép bạn điêu khắc nhanh chóng.

`Còn Android thì sao?`

Hiệu năng đồ họa của Android kém hơn iPad. Theo nhà phát triển Nomad, "Một chiếc Samsung Galaxy Tab S9 sẽ chạy Nomad chậm hơn cả chục lần so với một chiếc iPad Air". Dù vậy, rất nhiều người dùng vẫn rất hài lòng với máy tính bảng Samsung của họ, Nomad chạy tốt cho hầu hết các tác vụ điêu khắc. 

Với các máy tính bảng Android khác, hãy cẩn thận. Hiệu năng phần cứng Android có thể chênh lệch rất nhiều, khó mà đoán trước Nomad sẽ chạy thế nào.

Hãy dùng phiên bản miễn phí bị tắt chức năng lưu của Nomad để thử trước. 

`Còn bộ nhớ và dung lượng lưu trữ thì sao?`

Hầu hết các tệp Nomad thường có dung lượng 100mb hoặc ít hơn. Điều này có nghĩa là gần như bất kỳ máy tính bảng nào bạn mua ngày nay, dù là iPad hay Android, đều có thừa chỗ cho các dự án Nomad của bạn.


### Tôi đã mua Nomad cho một thiết bị, tôi có thể dùng nó trên thiết bị khác không? {#multi-devices}
Có, miễn là dùng cùng một cửa hàng ứng dụng và cùng một tài khoản.

Ví dụ, nếu bạn đã mua trên App Store của iOS, bạn có thể dùng nó trên các thiết bị iOS khác của mình.

Nếu bạn đã mua cho máy tính bảng Android trên Google Play, bạn có thể dùng nó trên các thiết bị Android khác của mình.

Tuy nhiên, nếu bạn đã mua Nomad trên Android, rồi sau đó bạn có một chiếc iPad, bạn sẽ cần mua lại.

Đó là vì Nomad không có máy chủ giấy phép hay mô hình thuê bao riêng. Không có thỏa thuận nào giữa Apple/Google/AppGallery để xử lý việc chia sẻ giấy phép. 


### Làm thế nào để khôi phục giao dịch mua? {#restore}
Google Play và AppGallery đều tự động xử lý việc đồng bộ.

- Vào menu Giới thiệu (biểu tượng nomad ở góc trên bên trái), và nhấn `Khôi phục mua hàng`
- Kiểm tra kỹ xem bạn đã đăng nhập đúng tài khoản dùng để mua Nomad chưa (trên Google Play).
- Khởi động lại thiết bị
- Đôi khi bạn cần đợi vài giờ
- Đảm bảo ứng dụng Google Play đã được cập nhật
- Cài đặt lại Nomad (nhớ [sao lưu các tệp của bạn](#locate) nếu bạn không muốn mất gì)
- Bạn có thể thử mua lại để xem điều gì xảy ra (lưu ý: bạn không thể mua cùng một mặt hàng hai lần trên cùng một tài khoản)

:::tip
Bạn có thể liên hệ với tôi qua <support@nomadsculpt.com>, nhưng điều *duy nhất* tôi có thể làm là xác nhận một địa chỉ email có giao dịch mua nào gắn với nó hay không.

Lưu ý rằng tôi thường xuyên nhận được báo cáo về việc giấy phép không được cập nhật đúng sau khi đổi sang thiết bị mới.
Tôi không có quyền kiểm soát nào đối với việc thanh toán và đồng bộ tài khoản, tất cả đều do Google/AppGallery xử lý!

Cuối cùng thì giao dịch mua luôn được khôi phục, nhưng không rõ cần làm những bước nào để quá trình này nhanh hơn.
:::

::: warning
Các thiết bị Huawei gần đây không truy cập được các dịch vụ của Google.
Trong trường hợp đó, bạn sẽ cần mua lại ứng dụng trên AppGallery (cửa hàng ứng dụng của Huawei).
:::

### Bạn có thể dịch hoặc sửa bản dịch [ngôn-ngữ-của-tôi] không? {#locale}
Tôi có thể thêm một ngôn ngữ khác khá dễ dàng, nhưng tôi dựa vào bản dịch bằng AI vì nó dễ xử lý hơn nhiều với các bản cập nhật thường xuyên.
Các tệp bản dịch có thể được tìm thấy [tại đây](https://github.com/stephomi/nomad-translation).

## Tính năng {#features}

### Tại sao gizmo không di chuyển? {#gizmo-not-moving}
Có thể bạn đã [bật ghim trên thanh công cụ menu bên trái](tools#left-menu-toolbar). 

### Có thể làm hoạt hình trong Nomad không? {#animate}
Hiện tại thì chưa. Một tính năng dòng thời gian có thể tạo hoạt hình cho các lớp sẽ rất thú vị, nhưng hiện tại chưa thực sự có kế hoạch.  

Tôi muốn hỗ trợ rigging/skinning trong tương lai, nhưng việc này đặt ra một vài thách thức (đặc biệt là cách tương tác với các công cụ điêu khắc...) nên hiện tại chưa có gì chắc chắn.


### Có thể dựng hình low-poly đúng nghĩa không? {#lowpoly}
Hiện tại thì chưa.
Đây thực sự không nằm trong phạm vi của Nomad *Sculpt*, nhưng có thể tôi sẽ cung cấp một vài công cụ trong tương lai.


### Có thể làm uv và kết cấu không? {#texturing}
Câu trả lời ngắn: Có. Câu trả lời dài: Không trực tiếp, nhưng có nhiều cách để kết hợp các công cụ vẽ đỉnh tuyệt vời của Nomad với uv và kết cấu.

* Nomad cho phép bạn vẽ màu, độ nhám, các thuộc tính vật liệu trực tiếp vào các đỉnh của tác phẩm điêu khắc.
* Nomad cho phép số lượng đỉnh rất cao để bạn có thể vẽ mà không cần bận tâm đến uv.
* Nomad có thể tải kết cấu để dùng trong cọ, cho phép đóng dấu và vẽ bằng kết cấu.
* Nomad có thể mở các đối tượng đã được gán sẵn kết cấu, để phục vụ kết xuất.
* Nomad có thể [trải UV](topology.md#uv-unwrap-uvatlas) cho các đối tượng ít đa giác.
* Màu/độ nhám/độ kim loại có thể được chuyển từ kết cấu sang đỉnh qua [các tùy chọn chiếu](topology.md#reproject-to-vertex).
* Màu/độ nhám/độ kim loại/pháp tuyến có thể được bake từ đỉnh sang kết cấu qua [các tùy chọn bake](topology.md#bake-texture)
* Việc bake và chiếu có thể thực hiện giữa từng đối tượng hoặc nhiều đối tượng, hoặc giữa cấp chia nhỏ cao nhất và thấp nhất của cùng một đối tượng, cho phép nhiều quy trình bake và chiếu khác nhau.
* Sau khi bake, xuất tệp obj cũng sẽ xuất kèm kết cấu, mà bạn có thể đưa sang một ứng dụng như Procreate để vẽ trực tiếp lên kết cấu.

### Tôi có thể quay video bàn xoay không? {#video}
Hiện tại chưa có kế hoạch, iOS có sẵn [tính năng quay màn hình](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) rất dễ dùng.

Trên iOS, bạn vuốt xuống từ góc trên bên trái, rồi chạm vào nút ghi. Bạn sẽ có 3 giây đếm ngược, hãy vuốt menu đi để hiện Nomad, và dùng tính năng bàn xoay. Khi xong, vuốt xuống lần nữa từ góc trên bên phải, rồi chạm lại vào nút ghi. Chỉnh sửa video trong thư viện ảnh để cắt bỏ phần thừa ở đầu và cuối video.

### Bạn có thể thêm [tính-năng-yêu-thích] thành một nút ở cấp trên cùng không? {#interface}
Có, giờ đây thanh công cụ phía dưới có thể được tùy chỉnh từ menu [giao diện](interface.md#shortcuts), và bạn cũng có thể tạo các thanh công cụ nổi.

### Những tính năng tiếp theo là gì? {#next-features}
Với lộ trình trung/dài hạn, tôi có rất nhiều ý tưởng nhưng chưa biết chắc.  

Sửa lỗi và cải thiện các tính năng hiện có sẽ luôn được ưu tiên hơn việc thêm tính năng mới.


### Có thể rig trong nomad không? {#rigging}
Không, nhưng đã có kế hoạch. Hiện tại, bạn có thể gắn các hình làm cha con với nhau và thay đổi trục xoay, cho phép tạo những tác phẩm điêu khắc đơn giản có thể tạo dáng.

### Có thể dùng nhiều hơn 4 đèn không? {#lights}
Bạn có thể dùng tối đa 4 đèn trên thiết bị di động, và tối đa 6 đèn trên máy tính. Đây là giới hạn của bộ máy kết xuất thời gian thực trong Nomad. Bạn có thể giả lập nhiều đèn hơn bằng các đối tượng phát sáng và chiếu sáng toàn cầu trong hậu kỳ, như trong [video hướng dẫn này](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Có thể nhập công cụ của Zbrush không? {#zbrush-import}
Không, Zbrush dùng định dạng độc quyền. Bạn có thể trích xuất các alpha map và dùng chúng trong Nomad. 

### Tại sao màu không giống với màu tôi đã vẽ? Tại sao tôi không có được màu trắng trong ảnh kết xuất? {#paint-pbr}
Hãy tưởng tượng chụp ảnh một tờ giấy, so với chụp ảnh một chiếc đèn bàn, so với chụp ảnh mặt trời. Máy ảnh và màn hình đời cũ sẽ đơn giản là cho tất cả thành ‘trắng’. Các hệ thống hiện đại hơn có thể thể hiện sự khác biệt giữa màu trắng phản chiếu của tờ giấy, ánh sáng phát ra từ chiếc đèn, và độ sáng chói của mặt trời.

Đồ họa máy tính hiện đại cố gắng hoạt động theo cách tương tự, mô phỏng vật lý của ánh sáng và bề mặt. Điều này được gọi là `Kết xuất dựa trên vật lý` (Physically Based Rendering), hay PBR, và bộ kết xuất PBR của Nomad dựa trên nguyên lý này. Cách này trông chân thực và cân bằng, nhưng các màu được vẽ sáng thường sẽ trông tối hơn.

Nếu bạn cần ảnh kết xuất khớp hơn với màu đã vẽ, bạn có thể khắc phục theo cả cách không dựa trên vật lý lẫn cách dựa trên vật lý:

Không dùng PBR:
* `Dùng chế độ 'Không sáng' trong menu Tô bóng`. Màu sẽ hiển thị chính xác như khi vẽ, nhưng bạn cũng mất toàn bộ tô bóng. Tiện cho việc kiểm tra nhanh, và cho kết quả mang tính đồ họa hơn.
* `Dùng chế độ 'MatCap' trong menu Tô bóng`. Chọn một matcap sáng hơn, chủ yếu là màu trắng, không bị ám màu.

Dùng PBR:
* `Dùng một môi trường trung tính`. Bạn có thể [đổi môi trường](shading.md#environment) sang một môi trường trung tính hơn. Tránh các môi trường trong nhà vì chúng thường bị ám màu nhiều hơn. Hãy ưu tiên môi trường ngoài trời ban ngày hoặc môi trường studio.
* `Tăng ánh sáng`. Nếu bạn chụp ảnh tờ giấy trắng trong một căn phòng tối, bạn chỉ cần thêm ánh sáng. Với đèn môi trường, hãy tăng thanh trượt độ phơi sáng cho đến khi màu sắc bắt đầu trông đúng với bạn, hoặc thêm nhiều đèn riêng lẻ với cường độ cao hơn.
* `Tăng độ phơi sáng của camera`. Nếu căn phòng tối không có thêm đèn nào, bạn có thể để màn trập máy ảnh mở lâu hơn, hoặc dùng ISO nhạy hơn. Trong Nomad, bạn có thể đạt kết quả tương tự bằng hậu kỳ. Vào hậu kỳ, bật lên, kéo xuống phần tone mapping, bật lên, và tăng thanh trượt độ phơi sáng cho đến khi màu sắc trông đúng.
* `Dùng màu phát sáng`. Trong menu vật liệu, bạn có thể bật 'Phát sáng' trong phần kết cấu, giúp đối tượng trông như một nguồn sáng. Nếu bạn bật chiếu sáng toàn cầu trong thiết lập hậu kỳ, nó sẽ chiếu sáng lên các đối tượng khác trong cảnh. Bạn cũng có thể bật 'Luôn không nhận sáng' cho vật liệu đó, giúp đạt được vẻ ngoài tương tự mà không cần kết cấu.

## Sự cố ứng dụng bị thoát {#crashes}

### Ứng dụng bị thoát khi tôi lưu hoặc tái tạo lưới mô hình! {#crash-remesh}
Thiết bị của bạn đang hết bộ nhớ (RAM).  
Để giảm mức dùng bộ nhớ trong cảnh, bạn có thể dùng một số tùy chọn trong [Tô pô](topology.md) để giảm số lượng đa giác.

::: tip RAM/Bộ nhớ lưu trữ
Điều quan trọng là dung lượng RAM, chứ không phải bộ nhớ lưu trữ (thường lớn hơn nhiều).
:::


### Ứng dụng bị thoát khi tôi mở dự án! {#crash-load}
Nếu tệp nhỏ, bạn có thể gửi cho tôi và tôi sẽ xem thử (qua email <support@nomadsculpt.com>).

Nếu không, có lẽ thiết bị đang hết bộ nhớ RAM.

- Đảm bảo bạn đã đóng mọi ứng dụng khác đang mở trên thiết bị.
- Bắt đầu một dự án mới trong Nomad thay vì đang mở sẵn một dự án.
- Nếu vẫn bị thoát, giải pháp duy nhất là mở [tệp dự án của bạn](#locate) trên một thiết bị có nhiều bộ nhớ hơn.

::: tip
Nếu thiết bị di động của bạn không mở được dự án, hãy thử [phiên bản máy tính](https://nomadsculpt.com). Bạn có thể dùng miễn phí ở chế độ Demo để nhập và xuất dự án, dù chỉ có một vài công cụ chỉnh sửa.

Nếu dự án của bạn dùng [Lớp](layers.md), bạn có thể muốn gộp chúng lại để giảm mức dùng bộ nhớ.
:::

### Ứng dụng bị thoát khi tôi khởi động Nomad! {#crash-start}
Nếu ứng dụng bị thoát khi đang tải, điều đó có nghĩa là Nomad gặp khó khăn với một tệp nào đó trong thư mục Nomad.

Phần lớn trường hợp, điều này xảy ra vì dự án quá nặng và không may vượt quá giới hạn RAM.

Tìm đến [thư mục Nomad](#locate), rồi đổi tên hoặc di chuyển một số tệp để tìm ra thủ phạm.

Trước tiên, hãy thử đổi tên `settings.json`. Như vậy Nomad sẽ không mở dự án gần nhất nữa.

Nếu không được, hãy thử di chuyển một số tệp gần đây ra khỏi các thư mục tài nguyên tương ứng của chúng (`projects`, `matcaps`, `environments`, v.v.).

Bạn cũng có thể đổi tên chính các thư mục đó để Nomad hoàn toàn bỏ qua chúng.
Nếu bạn đổi tên hoặc di chuyển tất cả các tệp trong thư mục Nomad, kết quả sẽ giống như cài đặt mới hoàn toàn.

::: tip
Khi Nomad mở một tệp lúc khởi động, nó luôn chuyển tệp đó vào thư mục `can_be_deleted/`.
Nếu thao tác thành công, tệp sẽ được chuyển trở lại thư mục ban đầu.

Nếu ứng dụng bị thoát trước khi tải xong, Nomad sẽ khởi động thành công ở lần mở tiếp theo, vì nó bỏ qua thư mục `can_be_deleted/`.

Bạn chỉ cần thử mở lại tệp này nếu bạn nghĩ nó có thể thành công.
:::
