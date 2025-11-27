# ![](/icons/sun.webp) Gölgelendirme

Bu menü, Nomad tarafından kullanılan gölgelendirme kiplerini, ışık özelliklerini ve ortam ışığı/matcap özelliklerini kontrol eder.

![](/images/shading_overview.webp)



Birden fazla işleme kipi arasından seçim yapabilirsiniz:

| Kip                         | Anlam                     | Açıklama                                                      |
| :-------------------------: | :-----------------------: | :-----------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Fiziksel Tabanlı İşleme   | Metalik/pürüzlülük ile boyama                                |
| [Matcap](#matcap)           | Malzeme Yakalama          | PBR’ye göre daha düşük gpu/cpu kullanımıyla yontma sırasında |
| [Unlit](#unlit)             | Yüzey Rengi               | Gölgelendirme ve aydınlatma olmadan yalnızca yüzey rengi     |
| [Object Id](#object-id)      | Nesne Kimliği             | Nesne başına rastgele renk, boyama uygulamaları için yararlı |
| [Instance Id](#instance-id)  | Örnek Kimliği             | Örnek başına rastgele renk, paylaşılan ağları ayırt etmek için yararlı |

Metaliklik ve pürüzlülük hakkında daha fazla bilgi edinmek istiyorsanız [Vertex Paint](painting.md) bölümüne bakın.

---

![](/images/shading_second.webp)

### Yüz Grubu
Yüz grubu renklerini bindirme olarak gösterir. Yüz grupları, [Face group](tools#facegroup) aracıyla oluşturulabilen ve çoğu primitif ile otomatik olarak yapılan, çokgenlerin renkli seçimleridir.

Bazı araçlar, yüz grupları görünürken otomatik olarak yüz gruplarına göre filtre uygular.

### Boyayı göster
Nomad, yontunuzun tepe noktalarında renk, pürüzlülük ve metalikliği saklayabilir. Bu özelliklerin görüntülenmesini bu onay kutusuyla küresel olarak açıp kapatabilirsiniz.

Hem tepe noktası özellikleriniz hem de dokularınız varsa ve ikisi de etkinse, değerlerin birbiriyle çarpılacağını unutmayın.

### Maskeyi göster
[Maske araçlarının](tools#mask) gri tonlu maske bindirmesini açıp kapatır. Bu devre dışı bırakıldığında maske de devre dışı kalır; bu, maskesiz hızlı değişiklikler yapmak, ardından maskenizi kaybetmeden tekrar etkinleştirmek için kullanışlıdır.

### Gizlemeyi kullan

Gizli yüzleri açıp kapatır. Bunun yalnızca gizleme aracında DEĞİLSENİZ çalıştığını unutmayın!

### Dokuları kullan

Nomad, [malzeme](material) menüsünden nesnelere dokular atanmasına izin verir. Dokular atanmışsa, bu onay kutusuyla küresel olarak açılıp kapatılabilirler.







### PBR ve ışıklar genel bakış
Bu kılavuz, Fiziksel Tabanlı İşleme ayrıntılarına girmeyecektir.

Aklınızda tutmanız gereken önemli bir nokta, aydınlatma ve malzemenin tamamen ayrılmış olmasıdır.
Bu, ışıklandırma bağımsız olarak ele alınırken nesnenizin rengini, pürüzlülüğünü ve metalikliğini boyayabileceğiniz anlamına gelir.
Bu sayede nesnenizi boyayıp, modelinizin genel görünümünü bozmadan ışığı daha sonra ayarlayabilirsiniz.

Işıklar yalnızca [PBR kipi](#pbr) ile kullanılabilir.
Performans nedenleriyle en fazla 4 ışıkla sınırlısınız.

::: tip
4’ten fazla ışık içeren bir glTF dosyası yükleyebilirsiniz ve Nomad bunların hepsini korur.
Ancak performans iyi olmayabilir.
:::

::: tip
Birçok ışığı, nesneleri aydınlatmasız/emissive yapıp ardından [post process](postprocess) menüsünde küresel aydınlatmayı etkinleştirerek taklit edebilirsiniz.
:::

### Işık türleri genel bakış

Şu anda desteklenen ışık türleri şunlardır:

| Kip                         | Açıklama                                              | Gölge oluşturabilir mi                                   |
| :-------------------------: | :---------------------------------------------------: | :------------------------------------------------------: |
| [Directional](#directional) | Sonsuz uzaktaki güneş ışığı                          | evet                                                     |
| [Environment](#environment) | Ortam HDR ile eşleşen uzak ışık                      | evet                                                     |
| [Spot](#spot)               | Konik şekilli ışıklar				                 | Evet                                                     |
| [Point](#point)             | Her yöne yayılan noktasal ışık                       | Evet, ancak yalnızca daha az sağlam ekran-uzayı gölgeleriyle |

#### Yönlü
Sonsuz uzaktan, tekdüze yoğunlukta ışık yayar.
Sahnedeki 3B konumu önemli değildir, yalnızca yönelimi önemlidir.

Bu ışığı kameraya bağlayabilirsiniz; böylece aydınlatma tutarlı olur.  
Örneğin, modelinizin arkasından, kameraya doğru ışık yayan güçlü bir ışık (rim light) kullanarak, modelinizin arkasını her zaman aydınlatan bir ışık elde edebilirsiniz.

#### Ortam ışığı
[Ortam hdr](#environment) kullanmak genel yumuşak aydınlatma için iyi çalışır, ancak HDR’de görünen güçlü, keskin bir ışık varsa, bunun oluşturduğu gölge çok yumuşak olur, çoğu zaman hiç görünmez. Ortam HDR ile birlikte yönlü ışık kullanmak yardımcı olabilir, ancak bunları hizalamak zor olabilir.

Bu ışık işi sizin yerinize yapar. Işık, HDR’nin en parlak kısmıyla hizalanacak şekilde otomatik olarak döndürülür, ardından yoğunluğunu ve açısını (gölge yumuşaklığı) ayrı ayrı kontrol edebilirsiniz. 

#### Spot
Spot ışık, tek bir yönde, koni şekliyle sınırlandırılmış ışık yayar.

#### Noktasal
Noktasal ışık her yöne ışık yayar.  
Şu anda noktasal ışık gölge desteklemez.

#### Gölgeler
`normal bias` seçeneği, yaygın gölge yapıtlarını (acne/peter-panning) azaltmak için kullanılabilir.

Gölge kalitesi, nesnelerin tüm sahneye göre boyutuna bağlıdır.  
Sahnenizde gölge oluşturmasına gerek olmayan büyük bir nesne varsa (örneğin büyük bir düzlem), [malzeme ayarlarında](material.md#cast-shadows) gölge oluşturmayı devre dışı bıraktığınızdan emin olun.

## Işıklar

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Işıklar onay kutusu

Sahnedeki tüm doğrudan ışıkları açıp kapatır.



### Işık ekle

Sahneye en fazla 4’e kadar ışık ekler. Bir ışık eklendiğinde, ışık listesi düğmelerle birlikte görüntülenir ve görünüm penceresinin üstüne bir ışık araç çubuğu eklenir.

![](/images/shading_lights_icons.webp)

* Metin, ışığın adını ve parlaklığını gösterir.
* Göz simgesi görünürlüğü açıp kapatır.
* Kalem simgesi, ışığı yeniden adlandırmanıza olanak tanır.
* Çöp kutusu simgesi bir ışığı siler.
* Kopya simgesi bir ışığı çoğaltır. 
* 3 nokta simgesi tam bir ışık düzenleyici açar. Bu işlevlerin çoğu, görünüm penceresinde beliren araç çubuğundan da kullanılabilir. 

### ![](/icons/spotlight.webp)  Simgeler

Görünüm penceresinde ışık simgelerinin görüntülenmesini açıp kapatır

### Işık araç çubuğu
![](/images/shading_lights_toolbar.webp) 

Bu araç çubuğu, bir ışık seçildiğinde görünüm penceresinin üst kısmında görünür.

* Show, ışık görünürlüğünü açıp kapatır.
* Directional/Environment/Spot/Point, ışık türünü değiştirir. Dokunarak döngü yapın veya menü görmek için uzun basın.
* Intensity, ışık gücünü kontrol eder; değer, çok yoğun ışıklar için 1.0’ın üzerine çıkabilir, Post Process’te Küresel Aydınlatma ile birlikte kullanıldığında yararlıdır.
* Renk örneğine tıklandığında bir renk seçici açılır. Nomad, renk seçmek için birkaç yol sunar. Kelvin kontrolü, sıcak/soğuk aydınlatmayı doğal bir şekilde seçmenizi sağlar.
* Shadow, gölgeleri açıp kapatır.
* Size, ışığın genişliğini ayarlar. Daha geniş ışıklar yumuşak gölgeler, yumuşak aydınlatma ve nesneler üzerinde daha yumuşak bir parlama oluşturur.
* ... ek denetimleri açar.

### Işık ek denetimleri

![](/images/shading_extra_controls.webp) 

Bazı seçeneklerin belirli ışık türlerine özgü olduğunu unutmayın.

* `Clone` ışığı çoğaltır.
* `Recenter` ışığı tekrar orijine taşır.
* `Delete` ışığı siler.
* `Directional/Environment/Spot/Point` ışık türünü değiştirmenize olanak tanır.
* `Renk örneği`ne tıklandığında bir renk seçici açılır. 
* `Intensity` ışık gücünü kontrol eder.
* `Attachment` (_yalnızca yönlü_) ışığın dünyaya mı yoksa kameraya mı bağlanacağını ayarlar. Örneğin karakterinizin arkasında bir rim light kullanıyorsanız, attachment olarak camera seçildiğinde, kamerayı döndürmek ışığın her zaman karakterin arkasında kalmasını sağlar.
* `Angle` (_yalnızca yönlü ve ortam_) ışığın görünen boyutudur; gökyüzünde güneşin ne kadar büyük göründüğünü düşünün. Daha büyük açılar daha yumuşak gölgeler ve daha geniş parlamalar oluşturur.
* `Softness` (_yalnızca spot_) spot ışık konisinin kenarının keskinliğini kontrol eder. 0 çok keskin bir kenardır. 1 çok yumuşaktır, ışık konisinin merkezine doğru bir gradyan vardır. Görünüm penceresinde, spot konisi üzerindeki küçük mavi nokta, yumuşaklığı etkileşimli olarak ayarlamak için kullanılabilir.
* `Cone angle` (_yalnızca spot_) spot ışığın yayılma açısını kontrol eder. Küçük bir açı çok ince bir ışık demetidir, 170 ise çok geniş bir ışık yayılımıdır. Görünüm penceresinde turuncu nokta, koni açısını etkileşimli olarak ayarlamak için kullanılabilir.
* `Shadow` geçerli ışık için gölgeleri açıp kapatır.
* `Shadow map` ve `screenspace`, gölgeleri hesaplamanın farklı yollarıdır; genellikle shadow map daha güvenilirdir.
* `Contact`, gölgelerin nasıl hesaplandığını ayarlar. Gölgeler, bilgisayar grafiklerinde zor bir problemdir ve görselleştirmede yapıtlar oluşturabilir. En önemli ışık için daha doğru gölgeler seçilebilir; bu denetim, en önemli ışığın Nomad tarafından otomatik mi yoksa kullanıcı tarafından mı seçileceğini belirler.
* `Tolerance` eğer gölge yapıtları görünürse (gölgeler yüzeylere temas etmiyor gibi görünüyorsa veya gölgelerin içinde gürültü ve desenler varsa), toleransı ayarlamak bu sorunları gidermeye yardımcı olabilir.


## Ortam

![](/images/shading_environment.webp)

Gerçek dünyada ışık her yönden gelir; gökyüzünün mavisi, çimin yeşili, bir binanın kırmızısı, ‘ortam’dan gelen tüm bu ışık bir ortam haritasıyla simüle edilebilir. 

Nomad, iç ve dış mekânlar için, farklı ton ve parlaklık seviyelerine sahip birkaç örnek ortam haritasıyla birlikte gelir. Yontularınızda en fazla ayrıntıyı ortaya çıkaranı görmek için farklı haritaları deneyin.

Görüntüye dokunarak mevcut ortam haritalarını görebilirsiniz. Bu iletişim kutusundan kendi haritanızı yüklemek için ‘Import...’ seçin. En iyisi, latlong veya equirectangular formatında, .hdr veya .exr dosyaları olarak Yüksek Dinamik Aralıklı (HDR) görüntüler kullanmaktır. [www.polyhaven.com](https://polyhaven.com/hdris), kullanılabilecek iyi bir ücretsiz ortam haritası koleksiyonuna sahiptir; genellikle 1k hdr haritalar iyi boyut ve iyi kalitededir.

### Pozlama
Ortam haritasının parlaklığını ayarlar. Haritalar, normal ışıklarla birlikte kullanıldığında çoğu zaman fazla parlak olabilir; özellikle [Post Process](postprocess) ayarlarında Küresel Aydınlatma ile birlikte kullanıldığında, pozlamayı kısmak denge kurmaya yardımcı olabilir.

### Döndürme

Ortam haritaları tüm yönlerden gelen ışığı yakaladığından, yansımaların ve genel aydınlatmanın yontunuzla iyi birleşmesi için bunları döndürebilirsiniz.

### Kameraya bağlı
Ortamı kameraya bağlar.

Bu, aydınlatmayı tutarlı olmaya zorlar; bu da yontma sırasında kullanışlı olabilir.


## ![](/icons/sphere_smooth.webp) Matcap

![](/images/shading_matcap.webp)

Adından da anlaşılacağı gibi (MATerial CAPture), bir matcap tek bir görüntüde hem aydınlatma hem de malzeme bilgisini üstlenir.
Malzemenin kendisi zaten matcap’te bulunduğundan, pürüzlülük ve metaliklik boyama kanalları yok sayılır.
Boyama rengi matcap ile çarpılır; yani siyah/gri bir matcap’iniz varsa, beyaz boya kullanmak onu daha parlak yapmaz.

Sanatçılar, şekle ve geometrinin kendisine odaklanmalarına izin verdiği için bu kipi yontma amaçları için tercih etme eğilimindedir.

Küreye dokunmak bir görüntü tarayıcısı açar. Kendi matcap’inizi de ekleyebilirsiniz; genel olarak, kareye sıkıca kırpılmış herhangi bir küre fotoğrafı, render’ı, hatta resmi kullanılabilir. Çevrimiçi birçok matcap kütüphanesi mevcuttur; yararlı bir kaynak [nidorx matcap kütüphanesidir](https://github.com/nidorx/matcaps).

### Küresel Matcap kullan

Genellikle sanatçılar tüm yontu için tek bir matcap kullanır, ancak bu anahtar devre dışı bırakılırsa, her nesnenin kendi matcap’i olabilir. Bu, çarpıcı sonuçlar elde etmek için sanatsal olarak kullanılabilir.

::: tip
Bu seçeneği devre dışı bırakın ve karakterlerinizin gözleri için bir göz küresi görüntüsü kullanın!
:::

### Döndürme
Matcap, ortam haritasının özel bir biçimidir; bu nedenle ortam haritası gibi döndürülebilir. Bunu, görünüm penceresinde üç parmakla sola ve sağa sürükleyerek istediğiniz zaman yapabilirsiniz.



## ![](/icons/circle_fill.webp) Aydınlatmasız

Bu kip yalnızca yüzey rengini gösterir. Işıklar, gölgeler, yansıma, saydamlık tarafından dikkatiniz dağılmadan nesnelerinizin yüzey renginin beklediğiniz gibi olup olmadığını kontrol etmek için yararlı olabilir. 

Bu kip, fotogerçekçi olmayan render’lar için de kullanılabilir ve düz, çizgi film tarzı bir görünüm elde edilebilir.

## ![](/icons/cube.webp) Nesne Kimliği

Tüm aydınlatma ve yüzey bilgisi yok sayılır ve her nesne benzersiz düz bir renkle gölgelenir. Bu, bir PBR render’ı ile birlikte oluşturulursa, bir boyama programında renge göre seçim yapmak ve böylece belirli nesneler üzerinde renk düzeltmeleri yapabilmek için kullanılabilir.

Bu renklerin [Sahne menüsü ağaç görünümünde](scene#tree-view) de görüneceğini unutmayın.

### Kimliği rastgeleleştir

Yeni bir rastgele renk kümesi oluşturur. 

## ![](/icons/link.webp) Örnek Kimliği

Nesne Kimliği ile aynıdır, ancak örnekler aynı renge sahip olur. 

### Kimliği rastgeleleştir

Yeni bir rastgele renk kümesi oluşturur.
