# ![](/icons/sun.webp) Gölgelendirme {#shading}

Bu menü Nomad'ın kullandığı gölgelendirme kiplerini, aydınlatma özelliklerini, ortamı ve matcap'i ve sisi kontrol eder.

![](/images/shading_overview.webp)



Birkaç işleme kipi arasından seçim yapabilirsiniz:

| Kip                        | Anlamı                    | Açıklama                                                     |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Aydınlatılmış (PBR)](#pbr)           | Fiziksel Tabanlı İşleme (Physically Based Rendering) | Işıklar, gölgeler, ortam ve boyanmış metaliklik/pürüzlülük   |
| [MatCap](#matcap)           | Malzeme Yakalama (Material Capture)           | Heykel için hızlı kip; GPU/CPU kullanımı PBR'den düşüktür        |
| [Aydınlatmasız](#unlit)             | Yüzey Rengi                | Gölgelendirme ya da aydınlatma olmadan yalnızca yüzey rengi                  |
| [Nesne kimliği](#object-id)     | Nesne kimliği                  | Nesne başına rastgele bir renk; boyama uygulamaları için kullanışlıdır.    |
| [Örnek kimliği](#instance-id) | Örnek kimliği                | Örnek başına rastgele bir renk; paylaşılan ağ örgülerini ayırt etmek için kullanışlıdır   |

Metaliklik ve pürüzlülük hakkında daha fazla bilgi için [Verteks Boyama](painting.md) bölümüne bakın.

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) Yüz Grubu {#face-group}
Yüz grubu renklerini üste bindirir. Yüz grupları, [Yüz Grubu](tools#facegroup) aracıyla oluşturulabilen, renklendirilmiş poligon seçimleridir; primitiflerin çoğunda kendiliğinden oluşturulurlar.

Yüz grupları görünürken bazı araçlar otomatik olarak yüz gruplarına göre filtreleme yapar.

### ![](/icons/palette.webp) Boyamayı göster {#show-paint}
Nomad, heykelinizin verteksleri içinde renk, pürüzlülük ve metaliklik saklayabilir. Bu onay kutusuyla bu özelliklerin gösterimini global olarak açıp kapatabilirsiniz.

Hem verteks özellikleriniz hem de dokularınız varsa ve ikisi de etkinse, değerlerin birbiriyle çarpılacağını unutmayın.

### ![](/icons/shield.webp) Maskeyi göster {#show-mask}
[Maske araçlarının](tools#mask) gri tonlamalı maske katmanını açıp kapatır. Bu devre dışıyken maske de devre dışı kalır; maske olmadan hızlı değişiklikler yapmak için kullanışlıdır, sonra tekrar etkinleştirdiğinizde maskenizi kaybetmezsiniz.

### ![](/icons/tool_hide.webp) Gizlemeyi Kullan {#use-hide}

Gizli yüzleri açıp kapatır. Bunun yalnızca gizleme aracında DEĞİLKEN çalıştığını unutmayın!

### ![](/icons/image.webp) Dokular kullan {#use-textures}

Nomad, [malzeme](material) menüsünden nesnelere doku atanmasına olanak tanır. Doku atanmışsa, bu onay kutusuyla global olarak açılıp kapatılabilirler.

Nomad içinde doku oluşturamaz ya da düzenleyemezsiniz, ancak içe aktarılan dosyalardaki dokular çalışır. Opaklık dokuları Aydınlatılmış, MatCap ve Aydınlatmasız kiplerinde; normal haritaları Aydınlatılmış ve MatCap kiplerinde; renk Aydınlatılmış ve Aydınlatmasız kiplerinde; yayıcı, pürüzlülük ve metaliklik ise yalnızca Aydınlatılmış kipte çalışır. Sahnede doku yoksa düğme soluk görünür.

### PBR ve ışıklara genel bakış {#pbr}
Bu kılavuz Fiziksel Tabanlı İşleme'nin ayrıntılarına girmeyecek.

Akılda tutulması gereken önemli bir nokta, aydınlatma ile malzemenin tamamen ayrı olmasıdır.
Yani nesnenizin rengini, pürüzlülüğünü ve metalikliğini boyarken aydınlatma bağımsız olarak ele alınır.
Böylece nesnenizi boyayıp aydınlatmayı sonradan, modelinizin genel görünümünü bozmadan ayarlayabilirsiniz.

Işıklar, ortam ve sis yalnızca [PBR kipinde](#pbr) kullanılabilir.
Performans nedenleriyle mobilde en fazla 4, masaüstünde en fazla 6 ışık kullanabilirsiniz.

::: tip
İçinde daha fazla ışık bulunan bir glTF dosyası yükleyebilirsiniz; Nomad hepsini korur.
Ancak performans iyi olmayabilir.
:::

::: tip
Nesneleri aydınlatmasız/yayıcı yapıp [süreç sonrası işlemler](postprocess) menüsünde küresel aydınlanmayı etkinleştirerek birçok ışık varmış gibi gösterebilirsiniz.
:::

### Işık türlerine genel bakış {#light-types-overview}

Şu anda desteklenen ışık türleri şunlardır:

| Kip                        | Açıklama                                             | Gölge oluşturabilir |
| :-------------------------: | :-----------------------------------------------------: | :--------------: |
| [Yönsel](#directional) | Sonsuz uzaklıktaki güneş ışığı                           | Evet              |
| [Ortam](#env-light)   | Ortam HDR'siyle eşleştirilmiş uzak bir ışık  | Evet              |
| [Spot](#spot)               | Koni biçimli ışıklar                                      | Evet              |
| [Nokta](#point)             | Her yöne ışık yayan nokta ışık                         | Evet              |

#### ![](/icons/sun.webp) Yönsel {#directional}
Işığı sonsuz uzaklıktan, tekdüze bir yoğunlukla yayar.
Sahnedeki 3d konumu önemli değildir, yalnızca yönelimi önemlidir.

Bu ışığı kameraya iliştirebilirsiniz; böylece aydınlatma hep tutarlı kalır.  
Örneğin, modelinizin arkasını her zaman aydınlatan bir kenar ışığı (modelinizin arkasından kameraya doğru yönelen güçlü bir ışık) yapmak için kullanabilirsiniz.

#### ![](/icons/panorama.webp) Ortam ışığı {#env-light}
Bir [ortam HDR'si](#environment) kullanmak genel, yumuşak bir aydınlatma için iyi sonuç verir; ancak HDR'de güçlü ve keskin bir ışık görünüyorsa, oluşturduğu gölge çok yumuşak olur ve çoğu zaman hiç görünmez. Ortam HDR'siyle birlikte bir yönsel ışık kullanmak yardımcı olabilir, ama ikisini hizalamak zor olabilir.

Bu ışık işi sizin yerinize yapar. Işık, HDR'nin en parlak kısmıyla hizalanacak şekilde otomatik olarak döndürülür; ardından yoğunluğunu ve açısını (gölge yumuşaklığı) ayrı ayrı kontrol edebilirsiniz. 

#### ![](/icons/spotlight.webp) Spot {#spot}
Spot ışık, ışığı koni biçimiyle sınırlanmış tek bir yöne yayar.

#### ![](/icons/light.webp) Nokta {#point}
Nokta ışık, ışığı her yöne yayar ve gölge de oluşturabilir.

#### Gölgeler {#shadows}
Her ışık gölge oluşturabilir; gölgelerin nasıl hesaplanacağını ışığın [ayarlarından](#light-extra-controls) seçebilirsiniz. Gölgelerde bozukluklar görürseniz oradaki `Tolerans` kaydırıcıları yardımcı olabilir.

Gölgelerin kalitesi, nesnelerin tüm sahneye göre boyutuna bağlıdır.  
Sahnenizde gölge oluşturması gerekmeyen büyük bir nesne varsa (örneğin büyük bir düzlem), [malzeme ayarlarından](material.md#casts-shadows) gölge oluşturmasını kapattığınızdan emin olun.

## ![](/icons/sun.webp) Işıklar {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Işıklar onay kutusu {#lights-checkbox}

Sahnedeki tüm doğrudan ışıkları açıp kapatır.



### Işık ekle {#add-light}

Sahneye bir ışık ekler; mobilde en fazla 4, masaüstünde en fazla 6 ışık. Bir ışık eklendiğinde, ışık listesi düğmeleriyle birlikte görüntülenir ve görünüm alanının üstüne bir ışık araç çubuğu eklenir.

![](/images/shading_lights_icons.webp)

* Metin, ışığın adını ve parlaklığını gösterir. Işığı seçmek için ona dokunun.
* Göz simgesi görünürlüğü açıp kapatır.
* Kalem simgesi ışığı yeniden adlandırmanızı sağlar.
* Çöp kutusu simgesi ışığı siler.
* Kopyala simgesi ışığı çoğaltır. 
* 3 nokta simgesi tam bir ışık düzenleyicisi açar. Bu işlevlerin çoğu, görünüm alanında beliren araç çubuğundan da kullanılabilir. 

Listede bir ışığı sürükleyerek yeniden sıralayabilirsiniz.

### ![](/icons/spotlight.webp)  Simgeler {#icons}

Görünüm alanındaki ışık simgelerinin gösterimini açıp kapatır

### Işık araç çubuğu {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Bir ışık seçildiğinde bu araç çubuğu görünüm alanının üstünde belirir.

* `Görülebilir` ışığın görünürlüğünü açıp kapatır.
* Yönsel/Ortam/Spot/Nokta ışık türünü değiştirir. Sırayla geçmek için dokunun ya da bir menü görmek için uzun basın.
* Yoğunluk ışığın gücünü kontrol eder; çok yoğun ışıklar için değer 1,0'ın üzerine çıkabilir, bu da Süreç sonrası işlemlerdeki Küresel Aydınlanma ile birlikte kullanıldığında işe yarar
* Renk örneğine tıklamak bir renk seçici açar. Nomad renk seçmek için birkaç yol sunar. Kelvin denetimi sıcak/soğuk aydınlatmayı doğal bir şekilde seçmenizi sağlar.
* Gölge, gölgeleri açıp kapatır.
* Açı (_yönsel ve ortam_) ya da Büyüklük (_spot ve nokta_) ışığın genişliğini belirler. Daha geniş ışıklar yumuşak gölgeler, yumuşak aydınlatma ve nesnelerde daha yumuşak parlamalar oluşturur.
* İliştirme (_yalnızca yönsel_), Koni açısı ve Yumuşaklık (_yalnızca spot_) aşağıdaki [ışık düzenleyicisi](#light-extra-controls) bölümünde anlatılmıştır.
* ... düğmesi, gölge ayarlarıyla birlikte `Klonlama`, `Yeniden ortala` ve `Sil` seçeneklerini açar.

### Işık ek denetimleri {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Listedeki bir ışığın 3 nokta simgesi, onun tam düzenleyicisini açar. Bazı seçeneklerin belirli ışık türlerine özgü olduğunu unutmayın.

* `Yönsel/Ortam/Spot/Nokta` ışık türünü değiştirmenizi sağlar.
* `Renk örneği`ne tıklamak bir renk seçici açar. 
* `Yoğunluk` ışığın gücünü kontrol eder.
* `İliştirme` (_yalnızca yönsel_) ışığı dünyaya (`Sabit`) ya da kameraya (`Kamera`) bağlar. Örneğin karakterinizin arkasında kenar ışığı olarak bir yönsel ışık kullanıyorsanız, iliştirme olarak kamera seçiliyken kamerayı döndürdüğünüzde ışık hep karakterin arkasında kalır.
* `Yumuşaklık` (_yalnızca spot ışık_) spot ışık konisinin kenar keskinliğini kontrol eder. 0 çok keskin bir kenardır. 1 ise ışık konisinin merkezine doğru bir geçişle çok yumuşaktır. Görünüm alanında, spot ışık konisinin üzerindeki küçük mavi nokta ile yumuşaklığı etkileşimli olarak ayarlayabilirsiniz.
* `Koni açısı` (_yalnızca spot ışık_) spot ışığın yayılma açısını kontrol eder. Küçük bir açı çok ince bir ışık huzmesidir, 170 ise çok geniş bir yayılımdır. Görünüm alanında, turuncu nokta ile koni açısını etkileşimli olarak ayarlayabilirsiniz.
* `Açı` (_yalnızca yönsel ve ortam_) ışığın görünen boyutudur; güneşin gökyüzünde ne kadar büyük göründüğü gibi düşünün. Daha büyük açılar daha yumuşak gölgeler ve daha geniş parlamalar oluşturur.
* `Büyüklük` (_yalnızca spot ve nokta_) ışığın genişliğidir. Daha büyük ışıklar daha yumuşak gölgeler oluşturur.
* `Gölge` geçerli ışığın gölgelerini açıp kapatır.
* Gölge türü, gölgelerin nasıl hesaplanacağını seçer. `Gölge haritası` sahneyi ışığın bakış açısından işler, bu yüzden kameranın göremediği geometri için de gölge oluşturur. `Ekran uzayı` yalnızca ekranda zaten görünen şeyleri kullanır: daha ucuzdur, ama deneyseldir. Genelde gölge haritası daha güvenilirdir.
* `Tolerans` (_yalnızca ekran uzayı_): gölgelerde bozukluklar görünüyorsa (gölgeler yüzeylere değmiyor gibi görünüyorsa ya da gölgelerin içinde gürültü ve desenler varsa), toleransı ayarlamak bu sorunları gidermeye yardımcı olabilir.
* `Temaslı`, nesnelerin birbirine değdiği kısa mesafelerde daha hassas gölgeler ekler. `Otomatik` ile yalnızca sahnedeki en baskın ışık temas gölgeleri alır; `Hayır` ve `Evet` bu ışık için onları zorla kapatır ya da açar. `Tolerans` kaydırıcısı yukarıdakiyle aynı şekilde çalışır.

Görünüm alanı araç çubuğunun `...` düğmesi aynı gölge ayarlarını ve ek olarak şunları içerir:

* `Klonlama` ışığı çoğaltır.
* `Yeniden ortala` ışığı yönelimini koruyarak kameranın önüne taşır.
* `Sil` ışığı siler.


## ![](/icons/panorama.webp) Ortam {#environment}

![](/images/shading_environment.webp)

Gerçek dünyada ışık her yönden gelir: gökyüzünün mavisi, çimenin yeşili, bir binanın kırmızısı... 'Ortamdan' gelen tüm bu ışık bir ortam haritasıyla taklit edilebilir. 

Ortam aydınlatmasını açıp kapatmak için başlığın yanındaki onay kutusunu kullanın.

Nomad, iç ve dış mekanlar için farklı renk tonlarında ve parlaklık düzeylerinde birkaç örnek ortam haritasıyla birlikte gelir. Heykellerinizdeki ayrıntıları en iyi hangisinin ortaya çıkardığını görmek için farklı haritaları deneyin.

Kullanılabilir ortam haritalarını görmek için görüntüye dokunun. Kendi haritanızı yüklemek için bu pencereden `İçe aktar...` seçeneğini seçin. En iyisi, enlem-boylam (latlong) ya da eşdikdörtgen (equirectangular) formatında, .hdr ya da .exr dosyası olarak Yüksek Dinamik Aralıklı (HDR) görüntüler kullanmaktır. Tarayıcı, iyi bir ücretsiz ortam haritası koleksiyonuna sahip olan [Poly Haven](https://polyhaven.com/hdris)'den doğrudan ortam da indirebilir.

### Pozlandırma {#env-exposure}
Ortam haritasının parlaklığını ayarlar. Haritalar normal ışıklarla birlikte kullanıldığında çoğu zaman fazla parlak kalabilir; pozlandırmayı düşürmek dengeyi sağlamaya yardım eder, özellikle de [Süreç sonrası işlemler](postprocess) ayarlarındaki Küresel Aydınlanma ile kullanıldığında.

### Döndürme {#env-rotation}

Ortam haritaları ışığı her yönden yakaladığı için, yansımaların ve genel aydınlatmanın heykelinizle iyi uyum sağlaması amacıyla onları döndürebilirsiniz. Görünüm alanında 3 parmağınızı yatay olarak sürükleyerek de ortamı döndürebilirsiniz.

### Kameraya bağlı {#env-attached}
Ortamı kameraya bağlar.

Aydınlatmanın tutarlı kalmasını sağlar; bu da heykel yaparken işe yarayabilir.

### Bulanıklaştır (arka plan) {#env-background-blur}
Bu kaydırıcı yalnızca [arka plan](background.md) ortama ayarlandığında görünür. Aydınlatmayı değiştirmeden modelinizin arkasındaki ortam görüntüsünü bulanıklaştırır.


## ![](/icons/fog.webp) Sis {#fog}

Sis sahnenize atmosferik derinlik katar ve ışık huzmelerini görünür kılar. Başlığın yanındaki onay kutusuyla etkinleştirin. Işıklar ve ortam gibi yalnızca [Aydınlatılmış (PBR)](#pbr) kipinde kullanılabilir.

::: tip Daha güçlü ışık huzmeleri
Sisin `Ortam` değerini düşürün ve parlak bir spot ya da nokta ışık kullanın. Sis açıkça görünene kadar `Yoğunluk` değerini artırın. Daha ince bir siste görünür huzmeler için `Saçılma Yönü` değerini yüksek pozitif bir değere ayarlayın ve kamerayı ışığa doğru çevirin.
:::

### Renk {#fog-color}
Sisin ve onun saçtığı ışığın rengi.

### Yoğunluk {#fog-density}
Sisin mesafeyle ne kadar hızlı koyulaştığı.

### Maksimum Opaklık {#fog-opacity}
Yüksek yoğunlukta bile sisin sahneyi ne kadar örtebileceğini sınırlar.

### Saçılma Yönü {#fog-scattering}
Sisin ışığı saçtığı yön (anizotropi olarak da bilinir). Pozitif değerler bir ışığa doğru baktığınızda sisi parlatır, negatif değerler ise ışıktan uzağa baktığınızda; sıfır ışığı her yöne eşit olarak saçar.

### ![](/icons/panorama.webp) Ortam {#fog-environment}
[Ortamın](#environment) sisi ne kadar aydınlattığı. Ortam kapalıyken soluk görünür.

### Gürültü {#fog-noise}
Sisi, genel yoğunluğunu değiştirmeden öbeklere ayırmak için ona gürültü karıştırır. Gürültü 0'ın üzerindeyken bir `Boyut` kaydırıcısı desenin boyutunu belirler.

### Şekil {#fog-shape}
Sisin sahnede nereyi doldurduğu:

* `Homojen` - tüm sahneyi doldurur.
* `Dikey` - sisi yumuşak kenarlı dikey bir şeridin içinde tutar. `Alt` ve `Üst` kaydırıcıları alt ve üst kenarların yüksekliğini belirler; göz düğmeleri ise siz ayarlarken şeridi görünüm alanında gösterir.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

Adından da anlaşılacağı gibi (MATerial CAPture, malzeme yakalama), bir matcap hem aydınlatma hem de malzeme bilgisini tek bir görüntüde toplar.
Malzemenin kendisi zaten matcap'in içinde bulunduğundan, pürüzlülük ve metaliklik boyama kanalları yok sayılır.
Boyama rengi matcap ile çarpılır; yani siyah/gri bir matcap'iniz varsa beyaz boya kullanmak onu daha parlak yapmaz.

Sanatçılar heykel yaparken bu kipi tercih etme eğilimindedir, çünkü şeklin ve geometrinin kendisine odaklanmalarını sağlar.

Küreye dokunmak bir görüntü tarayıcısı açar. Kendi matcap'inizi de ekleyebilirsiniz; genel olarak bir kürenin kare olarak sıkıca kırpılmış herhangi bir fotoğrafı, işlemesi, hatta resmi bile kullanılabilir. İnternette birçok matcap kütüphanesi bulunur; faydalı bir kaynak [nidorx matcap kütüphanesidir](https://github.com/nidorx/matcaps).

### Global MatCap kullan {#matcap-global}

Sanatçılar genellikle tüm heykel için tek bir matcap kullanır; ama bu seçenek devre dışıysa seçili nesnenin kendi matcap'i olabilir. Bu, çarpıcı sonuçlar elde etmek için sanatsal olarak kullanılabilir.

::: tip
Bu seçeneği devre dışı bırakın ve karakterlerinizin gözleri için bir göz küresi görüntüsü kullanın!
:::

### Döndürme {#matcap-rotation}
Matcap, ortam haritasının özelleşmiş bir biçimidir, bu yüzden bir ortam haritası gibi döndürülebilir. Bunu görünüm alanında 3 parmakla sola ve sağa sürükleyerek istediğiniz zaman da yapabilirsiniz.

Kaydırıcının yanındaki kilit düğmesi döndürmeyi kilitler; böylece 3 parmakla sürükleme matcap'i yanlışlıkla döndürmez.



## ![](/icons/circle_fill.webp) Aydınlatmasız {#unlit}

Bu kip yalnızca yüzey rengini gösterir. Işıklar, gölgeler, yansımalar ve saydamlık dikkatinizi dağıtmadan, nesnelerinizin yüzey renginin beklediğiniz gibi olup olmadığını kontrol etmek için işe yarayabilir. 

Bu kip, düz ve çizgi film gibi bir görünüm elde etmek için fotogerçekçi olmayan işlemelerde de kullanılabilir.

## ![](/icons/cube.webp) Nesne kimliği {#object-id}

Tüm aydınlatma ve yüzey bilgileri yok sayılır ve her nesne kendine özgü düz bir renkle gölgelendirilir. Bu, bir PBR işlemesinin yanında işlenirse, bir boyama programında renge göre seçim yapmak ve böylece belirli nesnelerde renk düzeltmeleri yapabilmek için kullanılabilir.

Bu renklerin [Sahne menüsünün ağaç görünümünde](scene#tree-view) de görüneceğini unutmayın.

### Rasgele id atama {#object-random}

Yeni bir rastgele renk seti oluşturur. 

## ![](/icons/link.webp) Örnek kimliği {#instance-id}

Nesne kimliği ile aynıdır, ama örnekler aynı renge sahip olur. 

### Rasgele id atama {#instance-random}

Yeni bir rastgele renk seti oluşturur. 
