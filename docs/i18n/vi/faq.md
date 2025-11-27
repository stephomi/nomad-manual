# ![](/icons/faq.webp) Câu hỏi thường gặp (FAQ)

[[toc]]

## Nền tảng 
### Dự án của tôi nằm ở đâu trên thiết bị?
Các dự án nằm trong thư mục `projects` bên trong thư mục chính của Nomad.

Trên iOS, bạn có thể truy cập thư mục Nomad bằng ứng dụng Files của iOS.

Trên Android, thư mục Nomad nằm ở `Android/data/com.stephaneginier.nomad/files/`.  
Trên các phiên bản Android gần đây (10/11), bạn không còn truy cập được thư mục `Android/data` nữa.
Bạn có thể truy cập nó thông qua một ứng dụng riêng, ví dụ [ứng dụng này](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Có cách nào để tham gia beta test không?
Đối với Windows & MacOS, bản beta có thể có sẵn trên [Trang chủ](https://nomadsculpt.com).
<br>
Đối với iOS có TestFlight riêng, hãy vào [Discord](https://discord.com/invite/8h7BwpRz29) trong kênh #beta-ios.
<br>
[Web Demo](https://nomadsculpt.com/demo) thường được cập nhật với các tính năng mới nhất.

### Tại sao Android có bản dùng thử miễn phí, còn iOS thì không?
Vì các thiết bị Android cũ khá tệ (và một số máy mới cũng vậy...), và tôi không muốn mọi người mua ứng dụng rồi chỉ thấy màn hình đen.
Nhưng lý do chính là tôi cảm thấy ứng dụng trả phí trên Android không thực sự phổ biến.

### Máy tính bảng nào chạy Nomad tốt nhất?

Tóm tắt: Một chiếc iPad.

Câu trả lời dài hơn một chút là 

> "Chiếc iPad mới nhất _mà bạn có thể mua được_, trừ khi bạn thực sự ghét Apple, khi đó hãy mua chiếc máy tính bảng Samsung mới nhất mà bạn có thể mua được. Bất cứ thứ gì khác, hãy thử trước." 

Mọi người luôn muốn thêm thông tin, nên đây là phần tóm lược.

Nomad chạy tốt nhất trên các iPad đời mới:

* iPad và iPhone có thể dùng plugin [Quad Remesher](tools#quad-remesher) từ [Exoside](https://exoside.com/)
* iPad đời mới với bút Pencil mới nhất hỗ trợ [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), bạn có thể xoay bút trong một số công cụ của Nomad. 
* hiệu năng của các chip dòng M mới nhất rất nhanh. 

Chiếc iPad mới nhất, đắt nhất sẽ có thể render ảnh cuối rất nhanh và cho phép bạn điêu khắc với rất nhiều chi tiết.

Tuy nhiên, mức giảm hiệu năng trên các iPad rẻ hơn và cũ hơn không tệ như mọi người nghĩ. Bất kỳ iPad nào hỗ trợ Apple Pencil đều chạy Nomad khá tốt. Ví dụ:

* iPad Pro 2023 có thể xử lý mô hình 5 triệu polygon và vẫn phản hồi tốt, ảnh chất lượng cuối có thể render trong 5 giây.
* iPad Pro 2015 có thể xử lý đối tượng 1,2 triệu polygon với chút độ trễ, ảnh chất lượng cuối có thể render trong 20 giây.

Đó là khác biệt hiệu năng khá lớn, nhưng bạn cũng phải tính đến giá:

* iPad Pro 2025 giá *2500 USD* mới tinh với đầy đủ tùy chọn. 
* iPad Pro 2023 hiện có giá khoảng *400 USD* trên eBay.
* iPad Pro 2015 giá khoảng *250 USD* trên eBay.

Thêm 4 triệu polygon và tiết kiệm 15 giây có đáng 2100 USD không? Tùy bạn quyết định.

Các mẫu không phải Pro còn rẻ hơn nữa và cho bạn nhiều lựa chọn về kích cỡ và hiệu năng. iPad Air hiện tại hỗ trợ bút Pencil gen 2 với barrel roll, và rẻ hơn đáng kể so với Pro. Thị trường máy cũ và tân trang còn nhiều lựa chọn hơn nữa. 

Điều này có nghĩa là với bất kỳ ngân sách nào, bạn cũng có thể tìm được một chiếc iPad phù hợp. Và hãy nhớ rằng hầu hết các bản điêu khắc không đến mức hàng triệu polygon! Nếu bạn giữ dưới 500.000 polygon, ngay cả iPad cũ cũng cho phép bạn điêu khắc nhanh.

`Thế còn Android thì sao?`

Hiệu năng đồ họa Android thấp hơn iPad. Theo nhà phát triển Nomad, "Samsung Galaxy Tab S9 sẽ chạy Nomad chậm hơn khoảng một bậc so với iPad Air". Dù vậy, rất nhiều người dùng vẫn rất hài lòng với tablet Samsung, Nomad chạy ổn cho hầu hết nhu cầu điêu khắc. 

Với các tablet Android khác, hãy cẩn thận. Phần cứng Android có thể chênh lệch hiệu năng rất nhiều, không dễ đoán Nomad sẽ chạy thế nào.

Hãy dùng bản Nomad miễn phí (không lưu được) để thử trước. 

`Thế còn bộ nhớ và lưu trữ?`

Hầu hết file Nomad thường dưới 100mb. Điều này có nghĩa là gần như bất kỳ tablet nào bạn mua hiện nay, iPad hay Android, đều sẽ có đủ chỗ cho các dự án Nomad của bạn.


### Tôi đã mua Nomad cho một thiết bị, có dùng được trên thiết bị khác không?
Miễn là dùng cùng kho ứng dụng và cùng tài khoản, thì được.

Ví dụ nếu bạn mua trên App Store iOS, bạn có thể dùng trên các thiết bị iOS khác của mình.

Nếu bạn mua cho tablet Android trên Google Play, bạn có thể dùng trên các thiết bị Android khác.

Tuy nhiên nếu bạn mua Nomad trên Android rồi sau đó mua iPad, bạn sẽ phải mua lại.

Vì Nomad không có máy chủ cấp phép riêng hay mô hình thuê bao. Không có thỏa thuận nào giữa Apple/Google/AppGallery để chia sẻ giấy phép. 


### Làm sao khôi phục mua hàng?
Google Play và AppGallery đều tự động đồng bộ.

- Vào menu About (biểu tượng nomad góc trên trái), và nhấn `restore purchase`
- Kiểm tra kỹ bạn đang đăng nhập đúng tài khoản đã dùng để mua Nomad (trên Google Play).
- Khởi động lại thiết bị
- Đôi khi bạn phải chờ vài tiếng
- Đảm bảo ứng dụng Google Play được cập nhật mới nhất
- Cài lại Nomad (nhớ [sao lưu file](#where-are-my-projects-located-on-my-device) nếu bạn không muốn mất dữ liệu)
- Bạn có thể thử mua lại để xem chuyện gì xảy ra (lưu ý: bạn không thể mua cùng một mục hai lần trên cùng một tài khoản)

:::tip
Bạn có thể liên hệ tôi tại <support@nomadsculpt.com> nhưng *việc duy nhất* tôi có thể làm là xác nhận xem một email có gắn với một lượt mua hay không.

Lưu ý là tôi thường xuyên nhận báo cáo về việc giấy phép không cập nhật đúng sau khi mua thiết bị mới.
Tôi không có bất kỳ quyền kiểm soát nào với việc thanh toán và đồng bộ tài khoản, tất cả do Google/AppGallery xử lý!

Cuối cùng thì mua hàng luôn được khôi phục, nhưng các bước cần thiết để đẩy nhanh quá trình thì không rõ ràng.
:::

::: warning
Các thiết bị Huawei gần đây không truy cập được dịch vụ Google.
Trong trường hợp đó bạn sẽ cần mua lại ứng dụng trên AppGallery (kho ứng dụng của Huawei).
:::

### Bạn có thể dịch hoặc sửa [ngôn-ngữ-của-tôi] không?
Tôi có thể tương đối dễ dàng thêm một ngôn ngữ khác, nhưng tôi đang dựa vào dịch máy AI vì nó dễ xử lý hơn cho các bản cập nhật thường xuyên.
File dịch có thể tìm thấy [tại đây](https://github.com/stephomi/nomad-translation).

## Tính năng

### Tại sao gizmo không di chuyển?
Có thể bạn đã [bật pin trong thanh công cụ menu bên trái](tools#left-menu-toolbar). 

### Có thể làm animation trong Nomad không?
Hiện tại thì chưa. Một tính năng timeline có thể animate các layer sẽ khá thú vị, nhưng hiện chưa thực sự được lên kế hoạch.  

Tôi muốn hỗ trợ rigging/skinning trong tương lai, nhưng nó đặt ra vài thách thức (đặc biệt là tương tác với các công cụ điêu khắc...) nên hiện chưa chắc chắn.

### Có thể làm modeling low-poly đúng nghĩa không?
Hiện tại thì chưa.
Đây không hẳn là phạm vi của Nomad *Sculpt*, nhưng có thể tôi sẽ cung cấp một vài công cụ trong tương lai.

### Có thể làm uv và texturing không?
Câu ngắn: Có. Câu dài: Không trực tiếp, nhưng có nhiều cách kết hợp công cụ tô màu theo vertex rất tốt của Nomad với uv và texture.

* Nomad cho phép bạn tô màu, độ nhám, thuộc tính vật liệu trực tiếp vào các vertex của mô hình.
* Nomad cho phép số lượng vertex rất cao để bạn có thể tô mà không cần lo về uv.
* Nomad có thể nạp texture để dùng trong brush, cho phép đóng dấu (stamping) và tô bằng texture.
* Nomad có thể nạp các đối tượng đã gán sẵn texture, phục vụ mục đích render.
* Nomad có thể [UV unwrap](topology.md#uv-unwrap) các đối tượng low-poly.
* Màu/độ nhám/độ kim loại có thể được chuyển từ texture sang vertex thông qua [tùy chọn project](topology.md#reproject-to-vertex).
* Màu/độ nhám/độ kim loại/normal có thể được bake từ vertex sang texture thông qua [tùy chọn baking](topology.md#bake-to-texture)
* Bake và project có thể thực hiện giữa các đối tượng đơn lẻ hoặc nhiều đối tượng, hoặc giữa mức subdivision cao nhất và thấp nhất của một đối tượng, cho phép nhiều quy trình bake và project khác nhau.
* Sau khi bake, xuất obj cũng sẽ xuất texture, có thể đưa sang ứng dụng như Procreate để vẽ trực tiếp lên texture.

### Tôi có thể ghi video turntable không?
Hiện chưa có kế hoạch, iOS có [tính năng ghi màn hình](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) rất dễ dùng.

Trên iOS, thao tác là vuốt xuống từ góc trên bên trái và nhấn nút ghi. Sẽ có đếm ngược 3 giây, vuốt ẩn menu để hiện Nomad, và dùng tính năng turntable. Khi xong, vuốt xuống lại từ góc trên bên phải và nhấn nút ghi lần nữa. Chỉnh sửa video trong thư viện ảnh để cắt bỏ phần thừa ở đầu và cuối.

### Bạn có thể thêm [tính-năng-ưa-thích] thành nút cấp cao (top-level) không?
Có, thanh công cụ phía dưới giờ có thể tùy biến từ menu [interface](interface.md), và bạn có thể tạo các thanh công cụ nổi.

### Các tính năng tiếp theo là gì?
Cho lộ trình trung/dài hạn tôi có rất nhiều ý tưởng nhưng chưa biết chắc.  

Sửa lỗi và cải thiện tính năng hiện có sẽ luôn được ưu tiên cao hơn việc thêm tính năng mới.

### Có thể rig trong Nomad không?
Không, nhưng đã được lên kế hoạch. Hiện tại bạn có thể gắn (parent) các khối với nhau và chỉnh điểm pivot, cho phép tạo các mô hình có thể tạo dáng đơn giản.

### Có thể dùng hơn 4 đèn không?
Không, đây là giới hạn của engine render thời gian thực trong Nomad. Có thể giả lập thêm bằng cách dùng các đối tượng phát sáng (emissive) và global illumination trong hậu kỳ, như trong [hướng dẫn này](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Có thể import Zbrush tools không?
Không, Zbrush dùng định dạng độc quyền. Bạn có thể trích xuất alpha map và dùng chúng trong Nomad. 

### Tại sao màu không khớp với những gì tôi đã tô? Tại sao tôi không thể có màu trắng trong render?
Hãy tưởng tượng chụp ảnh một tờ giấy, so với chụp ảnh một chiếc đèn bàn, so với chụp ảnh mặt trời. Máy ảnh và màn hình đời cũ sẽ chỉ hiển thị tất cả là “trắng”. Hệ thống hiện đại hơn có thể thể hiện sự khác biệt giữa màu trắng phản xạ của giấy, ánh sáng phát ra từ đèn, và độ sáng cực mạnh của mặt trời.

Đồ họa máy tính hiện đại cố gắng hoạt động tương tự, mô phỏng vật lý của ánh sáng và bề mặt. Điều này gọi là `Physically Based Rendering` (render dựa trên vật lý), hay PBR, và renderer PBR của Nomad dựa trên nguyên lý này. Nó trông thực tế và cân bằng, nhưng thường các màu tô sáng sẽ trông tối hơn.

Nếu bạn cần render khớp hơn với màu đã tô, bạn có thể chỉnh theo cả cách không dựa trên vật lý lẫn dựa trên vật lý:

Không PBR:
* `Dùng chế độ 'Unlit' trong menu lighting`. Màu sẽ hiển thị đúng như đã tô, nhưng bạn cũng mất toàn bộ shading. Hữu ích cho việc kiểm tra nhanh và output mang tính đồ họa.
* `Dùng chế độ 'Matcap' trong menu lighting`. Chọn matcap sáng hơn, chủ yếu là trắng, không có ám màu.

PBR:
* `Dùng môi trường trung tính`. Bạn có thể [đổi môi trường](shading.md#environment) sang môi trường trung tính hơn. Tránh môi trường trong nhà vì chúng thường có nhiều màu. Ưu tiên môi trường ngoài trời ban ngày hoặc studio.
* `Tăng độ sáng chiếu`. Nếu bạn chụp ảnh tờ giấy trắng trong phòng tối, bạn sẽ đơn giản là thêm đèn. Ở ánh sáng môi trường, tăng thanh trượt exposure cho đến khi màu trông ổn với bạn, hoặc thêm nhiều đèn riêng lẻ với cường độ cao hơn.
* `Tăng exposure của camera`. Nếu phòng tối không có thêm đèn, bạn có thể để máy ảnh mở màn trập lâu hơn, hoặc dùng ISO nhạy hơn. Trong Nomad bạn có thể đạt hiệu ứng tương tự bằng hậu kỳ. Vào post process, bật, kéo xuống tone mapping, bật, và tăng thanh trượt exposure cho đến khi màu trông ổn.
* `Dùng màu phát sáng (emissive)`. Trong menu material, bạn có thể bật 'emissive' trong phần textures, khiến đối tượng trông như nguồn sáng. Nếu bật global illumination trong cài đặt post process, nó sẽ chiếu sáng lên các đối tượng khác trong cảnh. Bạn cũng có thể bật 'unlit' cho material đó, đạt hiệu ứng tương tự mà không cần texture.

## Crash

### Ứng dụng bị crash khi tôi lưu hoặc remesh model!
Thiết bị của bạn đang hết bộ nhớ (RAM).  
Để giảm mức dùng bộ nhớ trong cảnh, bạn có thể dùng một số tùy chọn trong [Topology](topology.md) để giảm số lượng polygon.

::: tip RAM/Lưu trữ
Điều quan trọng là lượng RAM, không phải dung lượng lưu trữ (thường lớn hơn nhiều).
:::

### Ứng dụng bị crash khi tôi load project!
Nếu file nhỏ, bạn có thể gửi cho tôi và tôi sẽ xem thử (qua email <support@nomadsculpt.com>).

Nếu không thì có lẽ thiết bị đang hết RAM.

- Đảm bảo bạn đóng tất cả ứng dụng khác đang mở trên thiết bị.
- Bắt đầu một project mới trong Nomad thay vì đang mở sẵn một project.
- Nếu vẫn crash, giải pháp duy nhất là load [file project của bạn](#where-are-my-projects-located-on-my-device) trên một thiết bị có nhiều bộ nhớ hơn.

::: tip
Trên trình duyệt desktop, bạn có thể thử load file tại [url này](https://nomadsculpt.com/demo_save/) rồi export lại sau khi đơn giản hóa cảnh.

Một số trình duyệt giới hạn lượng RAM mà một tab có thể dùng, nên có thể kỹ thuật này sẽ không hoạt động.

Nếu project của bạn dùng [Layers](layers.md), bạn có thể squash chúng để giảm mức dùng bộ nhớ.
:::

<!-- ::: tip
Additionally, for legacy glb.lz4 file format, you can try the following:

1. If your project is using [Layers](layers.md), enable the `Merge layers` option before loading the project.
The option can be found in the `Files -> Settings` sub menu.
Layers can take a lot of memory, merging them at loading can help reduce the memory peak usage.

2. Decompress your [project](#where-are-my-projects-located-on-my-device) (`.glb.lz4` to `.glb`).
On windows, you need to download [LZ4](https://github.com/lz4/lz4/releases).
On MacOS, you can use the command line.
With homebrew, simply do `brew install lz4` and then `lz4 myproject.glb.lz4`.

3. Try to load the `.glb` file directly into Nomad again.

4. If it still crashes at loading, you can open the file on any 3d desktop software that supports `glTF`.
::: -->

### Ứng dụng bị crash khi tôi khởi động Nomad!
Nếu crash ngay khi load, nghĩa là Nomad gặp vấn đề với một file nào đó trong thư mục Nomad.

Phần lớn thời gian, điều này xảy ra vì project quá nặng và không may là vượt quá giới hạn RAM.

Xác định vị trí [thư mục Nomad](#where-are-my-projects-located-on-my-device), rồi đổi tên hoặc di chuyển một số file để tìm file gây lỗi.

Đầu tiên, thử đổi tên `settings.json`. Như vậy Nomad sẽ không load project cuối cùng nữa.

Nếu không hiệu quả, thử di chuyển một số file gần đây ra khỏi các thư mục tài nguyên tương ứng (`projects`, `matcaps`, `environments`, v.v.).

Bạn cũng có thể đổi tên chính các thư mục đó để Nomad hoàn toàn bỏ qua chúng.
Nếu bạn đổi tên hoặc di chuyển tất cả file trong thư mục Nomad, kết quả sẽ giống như cài mới hoàn toàn.

::: tip
Khi Nomad load một file lúc khởi động, nó luôn di chuyển file đó vào thư mục `can_be_deleted/`.
Nếu thao tác thành công, file sẽ được chuyển lại về thư mục gốc.

Nếu crash trước khi load xong, Nomad sẽ khởi động thành công ở lần mở tiếp theo, vì nó bỏ qua thư mục `can_be_deleted/`.

Bạn có thể thử load lại file này nếu nghĩ rằng lần sau có thể thành công.
:::
