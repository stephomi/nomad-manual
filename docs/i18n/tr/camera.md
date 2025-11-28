# ![](/icons/camera.webp) Kamera {#camera}

Bu menü, kameralar oluşturmanıza ve değiştirmenize, ayrıca kameralara nasıl etkileşimde bulunduğunuzu kontrol etmenize olanak tanır.

![](/images/camera_overview2.webp)

Nomad'daki kameraların birkaç kullanım alanı vardır:

* Belirli açılardan yontma (sculpt) görünümü ayarlamak
* Nesnelerinizi kadrajlamak için fotoğraf makinesi gibi kullanmak
* Sahnede gezinmek için bir birinci şahıs bakış açısı kamerası olarak kullanmak
* İzometrik oyunlar veya endüstriyel tarz render için ortografik kamera olarak kullanmak.

## Kamerayı kontrol etme {#control}

### Döndürme {#rotation}
Arka planda *bir* parmağınızı sürükleyerek kamerayı döndürürsünüz.
Parmağınızı modeliniz üzerinde sürüklerseniz, bunun yerine yontma işlemi başlar.

::: tip Arka plana erişemiyorsam kamerayı döndürebilir miyim?
Evet, ekrana *iki* parmağınızı koyabilirsiniz – sanki kaydırma/zoom hareketi yapmak istiyormuşsunuz gibi – ve ardından *bir* parmağınızı kaldırabilirsiniz.
:::

### Odaklama / Sıfırlama {#focus}
Model üzerinde *çift dokunarak* seçilen noktaya odaklanın.
Arka plana *çift dokunursanız*, kamera bunun yerine seçili mesh'e odaklanır.


### Taşıma {#translation}
*İki* parmağınızı hareket ettirerek kamerayı kaydırabilirsiniz (pan).


### Yakınlaştırma {#zooming}
Çimdikleme (pinch) hareketini kullanarak yakınlaştırıp/uzaklaştırabilirsiniz.


### Döndürme (Roll) {#rolling}
*İki* parmağı döndürerek görünümü *yuvarlayabilirsiniz* (roll).
::: warning
Bu hareket yalnızca `trackball` döndürme modunda kullanılabilir.
:::

### Masaüstü kontrolleri {#desktop}

Masaüstünde, alt/opt tuşu kamerayı kontrol etmek için kullanılır:

* uç boş alanda sürükleme = kamerayı döndür
* alt+uç sürükleme = kaydır (pan)
* alt+uç sürükleme, ardından alt'ı bırakma = zoom (zbrush ile aynı)

Kalemde 2 veya daha fazla tuşu olan Wacom tabletlerde, uç ve tuşları şu şekilde yapılandırmak için Wacom ayarlarını kullanın:

* uç = sol tık
* alt sallama tuşu = orta tık
* üst sallama tuşu = sağ tık

Bu ayarlarla, kamerayı yalnızca kalemle kontrol edebilirsiniz:

* üst sallama tuşu ve havada hareket = kamerayı döndür
* alt sallama tuşu ve havada hareket = kaydır (pan)

## Kamera kontrolleri {#camera-controls}

![](/images/camera_list.webp)

### Görünümler {#views}
`Add View` kullanarak kamera bakış noktalarını kaydedebilirsiniz.
Görünüm adına tıklarsanız, kamera o görünümü geri yükler.


::: tip
Kaydedilmiş bir görünüm, [Projection Type](#projection-type) ayarlarını ve ayrıca [Reference image](background.md)'i kaydeder.  
Farklı arka planlara sahip ön/sol/arka referans görünümleri arasında geçiş yapmak istiyorsanız kullanışlıdır.
:::

| Action      | Icon                          | Description                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Visibility  | ![](/icons/eye_open.webp)    | Toggle the camera. Hidden cameras will be skipped from previous/next button |
| Name        |                               | Select the camera                                                           |
| Image       | ![](/icons/image.webp)       | A thumbnail of a reference image if it is linked to the camera              |
| Update View | ![](/icons/update_view.webp) | Update the saved view with the current view point                           |
| Edit Name   | ![](/icons/pencil.webp)      | Edit the camera name                                                        |
| Delete      | ![](/icons/trash.webp)       | Delete the camera                                                           |

### ![](/icons/tool_view.webp) Görünüm Ekle {#add}
Geçerli görünüme dayalı yeni bir kamera oluşturun.

### ![](/icons/camera.webp) Simgeler {#icons-test}

Kamera simgelerinin görünüm alanında (viewport) görünüp görünmeyeceğini aç/kapat. Bir kamera seçiliyse, simgesi her zaman görünür.

### Projeksiyon Türü {#projection}
Kameranızın `Field of View` (FOV / odak uzaklığı) değerini değiştirebilirsiniz.
Oranlara yardımcı olabileceği için yontma amaçları için düşük bir FOV kullanmanız genellikle tavsiye edilir.  
Ayrıca, kabaca FOV'un 0'a eşit olmasına benzer olan `Orthographic` modunu da kullanabilirsiniz.

### Birinci Şahıs {#fps}
Döndürme eksenini (pivot) heykelin üzerinde değil doğrudan kamera üzerinde olacak şekilde ayarlamayı etkinleştirir. Arka planda bir parmağı sürüklemek, kamera konumunu kilitli tutar ancak döndürmeyi değiştirir; bu, birinci şahıs oyunların çalışma şekline benzer. Tekil nesneler yerine ortam (environment) yontarken kullanışlıdır.

![](/images/camera_rotation_ortho_view.webp)

### Döndürme Türü {#rotation-type}
Varsayılan olarak kamera `Turntable` döndürme modunu kullanır.
Bu, yalnızca iki serbestlik derecesine sahip olduğunuz anlamına gelir; daha sezgiseldir ancak bazı durumlarda daha fazla esneklik isteyebilirsiniz.  
`Trackball` moduna geçebilirsiniz; görünüm alanında *iki* parmağı döndürerek görünümü *yuvarlayabilirsiniz*. Masaüstünde, bazı kullanıcılara daha tanıdık gelebilecek alternatif bir trackball modu vardır.

### Ortografik yakalama {#orthographic}

Etkinleştirildiğinde, bir klavyeniz varsa görünümü döndürürken shift tuşunu basılı tutmak kamerayı en yakın ön/arka/üst/alt/sol/sağ görünüme sabitler ve kamerayı ortografik yapar. Görünüm küpüne tıklanarak ön/arka/sol/sağ/üst/alt görünüme sabitlendiğinde de kamera ortografik yapılır.

### Görünümü sıfırla {#reset}

Kamerayı öne taşır ve sahneyi görünüme sığdırır.

### Görünümü yakala {#snap}
En yakın ön/arka/sol/sağ/üst/alt görünüme sabitle. Zaten bu görünümlerden birindeyseniz, tekrar tıklamak 180 derece dönerek karşı tarafa sabitler.

### Hız {#speed}

Kameranın çok yavaş veya çok hızlı hareket ettiğini düşünüyorsanız, `rotation`, `translation` ve `zooming` için bir hız çarpanı ayarlayabilirsiniz. Heykeliniz çok büyük veya çok küçükse kullanışlıdır.

### Pivot genel bakış {#pivot}

Kamerayı döndürdüğünüzde küçük pembe bir nokta görürsünüz; bu, kamera pivot noktanızdır.  
Kameradan kaybolmamak veya sinirlenmemek için pivotunuzun nerede olduğunu anlamak çok önemlidir.

Varsayılan olarak pivot şu işlemlerle güncellenir:
- model üzerinde çift dokunma
- arka planda çift dokunma (yeni pivot, mesh'inizin merkezinde olur)
- ekrana *iki* parmak koymak (pan/zoom/roll) pivotu *iki* parmağın merkezine günceller

### Pivotu Güncelle... {#update-pivot}

Pivotun şu seçeneklerle güncellenmesini daha da özelleştirebilirsiniz:

* When camera starts moving 
* Allow air pivot
* When double tapping
* Sculpt (stroke)

::: tip
Alıştığınızda, [Settings](settings.md) menüsüne giderek (ipucu) pembe noktayı gizleyebilirsiniz.
:::

### Nesneye çift dokunma {#dtap-object}
`Focus` etkinleştirildiğinde, çift dokunma pivotu dokunulan nesneye taşır.

### Arka plana çift dokunma {#dtap-tap-background}
Etkinleştirildiğinde, pivotu Selection, Scene seçeneklerinden birine ayarlar veya bunlar arasında geçiş yapar.