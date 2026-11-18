# ![](/icons/image.webp) Arka Plan {#background}

Bu menü, Nomad'ın arka plan rengini ve kullanmak istediğiniz referans görüntülerini yönetir.

![](/images/background_overview.webp)

## Tür {#type}
![](/images/background_selector.webp)

Görünümün arka planı için üç seçenek vardır.

* `Ortam` - [Gölgelendirme](shading.md) menüsünde seçilen ortam haritasını gösterir. `Bulanıklık` ve `Pozlandırma` (parlaklık) kaydırıcılarıyla daha da ayarlanabilir. 
* `Renk` - İstediğiniz düz bir renk
* `Gradyanı` - İki renk arasında bir geçiş. `Faktör` kaydırıcısı, gradyanın orta noktasını kaydırmanızı sağlar.  

### Gradyan türü {#gradient-type}
`Gradyanı` seçiliyken şeklini belirleyin:
* `Doğrusal` - Düz bir gradyan, yönünü `Açı` kaydırıcısı belirler.
* `Radyal` - Ekranın ortasından başlayan dairesel bir gradyan.
* `Gökyüzü` - Dünya ufkuna sabitlenmiş bir gradyan; yukarı ve aşağı baktıkça kamerayı takip eder.

Her rengin bir sıfırlama düğmesi ve ekrandan renk almak için bir renk seçicisi vardır.

## ![](/icons/lock.webp) Kamera kilidi ile senkronize et {#sync-on-camera-lock}
Kamera [Gezgin](settings.md#snap-cube) ile kilitlendiğinde, referans görüntüsü kameranın hareketini takip eder ve böylece heykelinizle hizalı kalır.

* `Yatışa izin ver (İztopu)` - Kamera kilidinden çıktığınızda kameranın yatmasına izin verir.
* `Kilidi açınca görünümü sıfırla` - Kamera kilidinden çıktığınızda görünümü sıfırlar.

## Referans Görüntüsü {#reference}

![](/images/background_reference.webp)

Arka plana, referans olarak kullanmak üzere istediğiniz bir görüntüyü ekleyebilirsiniz. Eklemek için `İçe aktar...` düğmesine dokunun, ardından göstermek için `Referans görüntüsü` kutusunu işaretleyin.
Konumunu ve ölçeğini değiştirebilirsiniz, örneğin görüntüyü ekranın bir köşesine taşımak isterseniz.

### ![](/icons/tool_transform.webp) Dönüştür {#transform}

Bu düğme, referans görüntüsünü etkileşimli olarak yerleştirmenizi sağlar. Görüntüyü kaydırmak, ölçeklemek ve döndürmek için 2 parmağınızı kullanın. `Ayarları sıfırla`, görüntüyü varsayılan yerine geri koyar. Son yerleşim aşağıdaki kaydırıcılara yansır:

* `Kaplama` - %0'da referans görüntüsü her zaman nesnelerinizin arkasında kalır, %100'de önlerindedir. 
* `Opaklık` - Görüntünün ne kadar saydam olduğu.
* `Süreç sonrası işlemler` - Süreç sonrası efektlerini referans görüntüsüne de uygular. Orijinal renkleri korumak için kapatın.
* `X Konumu` / `Y Konumu` - Görüntünün X ve Y konumu.
* `Ölçek` - Görüntünün ölçeği.
* `Döndürme` - Görüntünün dönüşü.


::: tip

Kameralar ve referans görüntüleri birbirine bağlıdır. 

Yani referans görüntünüzü heykelinizle hizalayıp ardından [Kamera menüsünden](camera.md) bir kamera oluşturursanız, referans görüntüsünün konumu, dönüşü ve ölçeği de kamerayla birlikte saklanır. Referans görüntüsünü kapatıp görünümü başka bir açıya çevirebilirsiniz. Kameradan tekrar baktığınızda, referans görüntüsü kullandığınız ayarlarla yeniden etkinleşir.

Hatta farklı kameralar için farklı görüntüler bile seçebilirsiniz!

 ![](/videos/reference_camera.mp4)

:::
