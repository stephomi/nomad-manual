# ![](/icons/camera.webp) Kamera {#camera}

Bu menü kameralar oluşturmanızı ve düzenlemenizi, ayrıca kamerayla nasıl etkileşime girdiğinizi kontrol etmenizi sağlar.

![](/images/camera_overview2.webp)

Nomad'da kameraların birkaç kullanımı vardır:

* Hassas açılardan şekillendirmek için görünümler hazırlamak
* Nesnelerinizi kadraja almak için bir fotoğraf makinesi gibi kullanmak
* Sahnenizde gezinmek için birinci şahıs perspektifli bir kamera olarak kullanmak
* İzometrik oyunlar veya endüstriyel tarzda işlemeler için ortografik bir kamera olarak kullanmak

## Kamerayı kontrol etmek {#control}

### Döndürme {#rotation}
Kamerayı, arka plan üzerinde *tek* parmağınızı sürükleyerek döndürürsünüz.
Parmağınızı modelinizin üzerinde sürüklerseniz, bunun yerine şekillendirme işlemi başlar.

::: tip Arka plana erişemiyorsam kamerayı döndürebilir miyim?
Evet: kaydırma/yakınlaştırma hareketi başlatacakmış gibi ekrana *iki* parmağınızı koyun, sonra *bir* parmağınızı kaldırın.
:::

### Odaklama / Sıfırlama {#focus}
Dokunduğunuz noktaya odaklanmak için model üzerine *çift dokunun*.
Arka plana *çift dokunursanız*, kamera bunun yerine seçili ağ örgüsüne veya tüm sahneye odaklanır; bkz. [Arka plana çift dokun](#dtap-tap-background).


### Kaydırma {#translation}
*İki* parmağınızı hareket ettirerek kamerayı kaydırabilirsiniz.


### Yakınlaştırma {#zooming}
İki parmakla sıkıştırma hareketiyle yakınlaştırıp uzaklaştırabilirsiniz.


### Yuvarlama {#rolling}
*İki* parmağınızı döndürerek görünümü *yuvarlayabilirsiniz* (kendi ekseni etrafında çevirebilirsiniz).
::: warning
Bu hareket yalnızca `İztopu` döndürme modlarında kullanılabilir.
:::

### Masaüstü kontrolleri {#desktop}

Masaüstünde kamerayı kontrol etmek için alt/opt tuşu kullanılır:

* boş alanda kalem ucuyla sürükleme = kamerayı döndürür
* alt + kalem ucuyla sürükleme = kaydırır
* alt + kalem ucuyla sürükleme, ardından alt tuşunu bırakma = yakınlaştırır (ZBrush'taki gibi)

Kaleminde 2 veya daha fazla düğme bulunan Wacom tabletlerde, ucu ve düğmeleri Wacom ayarlarından şöyle yapılandırın:

* uç = sol tık
* alt düğme = orta tık
* üst düğme = sağ tık

Bu ayarlarla kamerayı yalnızca kalemle yönetebilirsiniz:

* üst düğme ve havada gezdirme = kamerayı döndürür
* alt düğme ve havada gezdirme = kaydırır

## Kamera kontrolleri {#camera-controls}

![](/images/camera_list.webp)

### Görünümler {#views}
`Görünüm ekle` ile kamera bakış noktalarını kaydedebilirsiniz.
Görünümün adına tıklarsanız kamera o görünüme geri döner.


::: tip
Kaydedilen bir görünüm, [Projeksiyon türü](#projection) ayarlarını ve [Referans görselini](background.md) de kaydeder.  
Farklı arka planlarla ön/sol/arka referans görünümleri arasında geçiş yapmak istediğinizde işe yarayabilir.
:::

| Eylem      | Simge                          | Açıklama                                                                 |
| :---------: | :---------------------------: | :-------------------------------------------------------------------------: |
| Görünürlük  | ![](/icons/eye_open.webp)    | Kamerayı açar/kapatır. Gizli kameralar önceki/sonraki düğmesiyle geçilirken atlanır |
| İsim        |                               | Kamerayı seçer                                                           |
| Resim       | ![](/icons/image.webp)       | Kameraya bağlıysa referans görselinin küçük resmi              |
| Projeksiyon  | ![](/icons/perspective.webp) | Kameranın projeksiyonu; perspektifteyken görüş alanıyla birlikte    |
| Görünümü güncelle | ![](/icons/update_view.webp) | Kaydedilen görünümü mevcut bakış noktasıyla günceller                           |
| Yeniden Adlandır   | ![](/icons/pencil.webp)      | Kameranın adını düzenler                                                        |
| Sil      | ![](/icons/trash.webp)       | Kamerayı siler                                                           |

### ![](/icons/camera_add.webp) Görünüm ekle {#add}
Mevcut görünüme dayanarak yeni bir kamera oluşturur.

### ![](/icons/camera.webp) Simgeler {#icons-test}

Kamera simgelerinin görüntü alanında görünüp görünmeyeceğini belirler. Düğme, bir kameranız olduğunda `Görünüm ekle` seçeneğinin yanında belirir. Bir kamera seçiliyse simgesi her zaman görünür.

### Projeksiyon türü {#projection}
`Perspektif` ve `Ortografik` arasında seçim yapın.

Perspektifte kameranızın `Dikey Görünüm Alanı` (FoV) değerini değiştirebilirsiniz. Kaydırıcının üstünde, 35 mm'lik bir fotoğraf makinesindeki karşılık gelen odak uzaklığı gösterilir; fotoğrafçılığa alışkınsanız kullanışlıdır.
Şekillendirme için genellikle düşük bir FoV kullanmanız önerilir, çünkü oranları doğru görmeye yardımcı olur.  
`Ortografik` mod, aşağı yukarı 0'a eşit bir FoV'ye benzer.

### Birinci Kişi {#fps}
Yalnızca perspektifte. Pivot noktasını heykel yerine doğrudan kameranın üzerine koyar. Arka planda parmağınızı sürüklediğinizde kameranın konumu sabit kalır, ama dönüşü değişir; birinci şahıs oyunlarındaki gibi. Tek nesneler yerine ortamlar şekillendirirken kullanışlıdır.

![](/images/camera_rotation_ortho_view.webp)

### Döndürme türü {#rotation-type}
Varsayılan olarak kamera `Döner platform` döndürme modunu kullanır.
Bu, yalnızca iki serbestlik derecesine sahip olduğunuz anlamına gelir; daha sezgiseldir, ama bazı durumlarda daha fazla esneklik isteyeceksiniz.  
`İztopu` moduna geçebilirsiniz; bu durumda görüntü alanında *iki* parmağınızı döndürerek görünümü *yuvarlayabilirsiniz*. İki `İztopu` modu vardır: ilki görünümü parmağınızın altındaki bir top gibi yuvarlar, ikincisi (oklu simge) ise görünümü sürüklemenizin yatay ve dikey hareketine göre çevirir; bu da bazı kullanıcılara daha tanıdık gelebilir.

### Ortografik yaslama {#orthographic}

Etkinleştirildiğinde, klavyeniz varsa görünümü döndürürken shift tuşunu basılı tutmak kamerayı en yakın ön/arka/üst/alt/sol/sağ görünüme yaslar ve kamerayı ortografik yapar. Görünüm küpüne tıklanarak ön/arka/sol/sağ/üst/alt görünüme yaslandığında da kamera ortografik olur.

### Görünümü sıfırla {#reset}

Kamerayı öne taşır ve sahneyi görünüme sığdırır.

### Görünümü yasla {#snap}
En yakın ön/arka/sol/sağ/üst/alt görünüme yaslar. Zaten bu görünümlerden birindeyseniz, tekrar tıklamak 180 derece dönerek karşı tarafa yaslar.

### Hız {#speed}

Kameranın çok yavaş veya çok hızlı hareket ettiğini düşünüyorsanız `Döndürme`, `Yakınlaştırma` ve `Yatay Kayma` için bir hız çarpanı ayarlayabilirsiniz. Heykeliniz çok büyük veya çok küçükse kullanışlıdır.

### Pivot noktasına genel bakış {#pivot}

Kamerayı döndürdüğünüzde küçük pembe bir nokta görürsünüz; bu, kameranızın pivot noktasıdır.  
Kamerayla kaybolmamak veya sinirlenmemek için pivot noktanızın nerede olduğunu anlamanız çok önemlidir.

Varsayılan olarak pivot noktası şu işlemlerle güncellenir:
- model üzerine çift dokunmak
- arka plana çift dokunmak (yeni pivot noktası ağ örgünüzün merkezinde olur)
- ekrana *iki* parmak koymak (kaydırma/yakınlaştırma/yuvarlama), pivot noktasını *iki* parmağın ortasına günceller

### Ekseni güncelle... {#update-pivot}

Pivot noktasının güncellenme şeklini şu seçeneklerle daha da özelleştirebilirsiniz:

* `Kamera hareketinde` - Kamerayla etkileşime başladığınızda pivot noktasını günceller.
* `Yüzey dışı eksen` - Nesne yüzeyinin dışına yakınlaştırdığınızda bile yeni bir pivot noktasına izin verir. `Kamera hareketinde` seçeneğini gerektirir.
* `Çift dokunmayla güncelle` - Nesne yüzeyine çift dokunduğunuzda dönüş pivot noktasını günceller.
* `Şekillendirme (Darbe)` - Şekillendirdiğinizde pivot noktasını günceller.

::: tip
Alıştığınızda, pembe (ipucu) noktayı [Ayarlar](settings.md) menüsünden gizleyebilirsiniz.
:::

### Uzaklaşırken ortala {#center-view-when-zooming-out}
Uzaklaştırırken kamera yana kaymaz: yalnızca geriye doğru hareket eder, böylece görünüm ortalanmış kalır.

### Nesneye çift dokun {#dtap-object}
Etkinleştirildiğinde, bir nesneye çift dokunmak kamerayı dokunulan noktaya odaklar.

### Arka plana çift dokun {#dtap-tap-background}
Etkinleştirildiğinde, arka plana çift dokunmak kamerayı şunlara odaklar:
* `Seçim` - Seçili nesneler.
* `Sahne` - Tüm sahne.
* `Değiştir` - Her çift dokunuşta ikisi arasında geçiş yapar. İki `Değiştir` seçeneği vardır; simgelerinin gösterdiği gibi, hangisinin önce geldiğine göre farklılaşırlar.
