# ![](/icons/image.webp) Arka Plan {#background}

Bu menü, Nomad'ın arka plan rengini ve kullanılacak referans görsellerini kontrol eder.

![](/images/background_overview.webp)

## Arka Plan {#type}
![](/images/background_selector.webp)

Görünüm penceresi arka planı için üç seçenek vardır.

* `Environment` - [Shading](shading) bölümünde seçilen ortam haritasını gösterir. Bu, Blur ve Exposure (parlaklık) kontrolleriyle daha da ayarlanabilir.
* `Color` - Seçebileceğiniz düz bir renk
* `Gradient` - Yukarıdan aşağıya bir renk geçişi. Factor kaydırıcısı, gradyanın orta noktasını belirlemenizi sağlar.  

## Referans Görsel {#reference}

![](/images/background_reference.webp)

Arka plana referans olarak kullanılmak üzere seçtiğiniz bir görsel ekleyebilirsiniz.
Örneğin ekranın köşesine taşımak isterseniz, konumunu ve ölçeğini değiştirebilirsiniz.

### ![](/icons/tool_transform.webp) Dönüştür {#transform}

Bu düğme, referans görselini etkileşimli olarak yerleştirmenizi sağlar. Referans görselini yerine oturtmak için 2 parmağınızı kullanarak kaydırın, ölçekleyin, döndürün. Son yerleşim aşağıdaki kaydırıcılara yansıtılır:

* `Overlay` - %0'da referans görseli her zaman nesnelerinizin arkasında, %100'de ise önündedir.
* `Opacity` - Görselin ne kadar saydam olduğu.
* `Position` - Görselin X ve Y konumu.
* `Rotation` - Görselin dönüşü.
* `Scale` - Görselin ölçeği.


::: tip

Kameralar ve referans görselleri bağlantılıdır. 

Bu, referans görselinizi yontunuzla hizalayacak şekilde ayarlarsanız, [Camera menüsü](camera) üzerinden bir kamera oluşturduğunuzda, referans görselinin konum, dönüş ve ölçek bilgilerinin de kamera ile birlikte saklanacağı anlamına gelir. Referans görselini kapatabilir, başka bir görünüme dönebilirsiniz. Kameradan tekrar baktığınızda, referans görseli kullandığınız ayarlarla birlikte yeniden etkinleştirilir.

Bu, farklı kameralar için farklı görseller seçmeyi bile kapsar!

 ![](/videos/reference_camera.mp4)

:::