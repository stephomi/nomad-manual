# ![](/icons/faq.webp) SSS {#faq}

[[toc]]

## Platform {#platform}
### Projelerim cihazımda nerede bulunuyor? {#locate}
Projeler, ana Nomad klasörünün içindeki `projects` klasöründe bulunur.

iOS'ta Nomad klasörüne iOS Dosyalar uygulamasıyla erişebilirsiniz.

Android'de Nomad klasörü `Android/data/com.stephaneginier.nomad/files/` konumundadır.  
Yeni Android sürümlerinde (10/11) artık `Android/data` klasörüne doğrudan erişiminiz yoktur.
Bu klasöre ayrı bir uygulama üzerinden erişebilirsiniz, örneğin [bu uygulama](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Beta testine katılmanın bir yolu var mı? {#beta}
Windows ve MacOS için [Ana sayfada](https://nomadsculpt.com) bir beta sürümü bulunabilir.
<br>
iOS için özel bir TestFlight var; [Discord](https://discord.com/invite/8h7BwpRz29) sunucusundaki #beta-ios kanalını ziyaret edin.
<br>
[Web Demo](https://nomadsculpt.com/demo) genellikle en son özelliklerle güncellenir.

### Neden Android'de ücretsiz deneme var da iOS'ta yok? {#android-trial}
Çünkü eski Android cihazlar berbat (bazı yenileri de öyle...) ve insanların uygulamayı satın alıp siyah bir ekranla karşılaşmasını istemedim.
Ama asıl neden, Android'de ücretli uygulamaların pek yaygın olmadığını düşünmemdi.

### Nomad'ı çalıştırmak için en iyi tablet hangisi? {#best-tablet}

Kısacası: Bir iPad.

Biraz daha uzun cevap şu: 

> "Gücünüzün _yettiği_ en yeni iPad; Apple'dan gerçekten nefret ediyorsanız, gücünüzün yettiği en yeni Samsung tablet. Bunların dışındaki her şeyi önce test edin." 

İnsanlar hep daha fazla bilgi istiyor, işte bir özet.

Nomad en iyi yeni iPad'lerde çalışır:

* iPad'ler ve iPhone'lar [Quad Remesher](tools#quad-remesher) eklentisini kullanabilir (geliştiricisi: [Exoside](https://exoside.com/))
* en son kalemi destekleyen yeni iPad'ler [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0) özelliğine sahiptir; Nomad'daki bazı araçlarda kalemi kendi ekseninde çevirebilirsiniz. 
* en yeni M serisi çiplerin performansı çok yüksektir. 

Piyasadaki en yeni ve en pahalı iPad, son görüntüleri çok hızlı işleyebilir ve çok fazla ayrıntıyla heykel yapmanıza olanak tanır.

Ancak daha ucuz ve daha eski iPad'lerdeki performans düşüşü, insanların sandığı kadar kötü değildir. Apple Pencil'ı destekleyen her iPad, Nomad'ı oldukça iyi çalıştırır. Örneğin:

* 2023 model bir iPad Pro 5 milyon poligonluk heykelleri akıcı biçimde kaldırabilir ve son kalitede bir görüntüyü 5 saniyede işleyebilir.
* 2015 model bir iPad Pro 1,2 milyon poligonluk bir nesneyi biraz takılarak kaldırabilir ve son kalitede bir görüntüyü 20 saniyede işleyebilir.

Bu büyük bir performans farkı, ama fiyatı da hesaba katmanız gerekir:

* 2025 model iPad Pro, tüm seçenekleriyle sıfır olarak *2500 USD*'dir. 
* 2023 model iPad Pro şu anda eBay'de *400 USD* civarındadır.
* 2015 model iPad Pro eBay'de *250 USD* civarındadır.

Fazladan 4 milyon poligon ve 15 saniye kazanmak 2100 dolara değer mi? Bu size kalmış.

Pro olmayan modeller daha da ucuz olabilir ve çok çeşitli boyut ve performans seçenekleri sunar. Güncel iPad Air, barrel roll özellikli 2. nesil kalemi destekler ve Pro'dan çok daha ucuzdur. İkinci el ve yenilenmiş ürün pazarında daha da fazla seçenek vardır. 

Yani bütçeniz ne olursa olsun, size uygun bir iPad bulabilirsiniz. Ve unutmayın, çoğu heykel milyonlarca poligondan oluşmaz! 500.000 poligonun altında kalabilirseniz eski iPad'ler bile hızlıca heykel yapmanızı sağlar.

`Peki ya Android?`

Android'in grafik performansı iPad'lerin gerisindedir. Nomad'ın geliştiricisine göre, "Bir Samsung Galaxy Tab S9, Nomad'ı bir iPad Air'den kat kat daha yavaş çalıştırır". Bununla birlikte birçok kullanıcı Samsung tabletlerinden çok memnun; Nomad çoğu heykel işi için sorunsuz çalışıyor. 

Diğer Android tabletlerde dikkatli olun. Android donanımlarının performansı çok değişebilir ve Nomad'ın nasıl çalışacağını tahmin etmek kolay değildir.

Lütfen önce Nomad'ın kaydetme özelliği kapalı ücretsiz sürümüyle test edin. 

`Peki ya bellek ve depolama alanı?`

Çoğu Nomad dosyası 100 MB ya da daha küçüktür. Yani bugünlerde alacağınız hemen her tablette, iPad ya da Android,  Nomad projeleriniz için bolca yer olacaktır.


### Nomad'ı bir cihaz için satın aldım, başka bir cihazda kullanabilir miyim? {#multi-devices}
Aynı uygulama mağazasını ve aynı hesabı kullandığı sürece evet.

Örneğin iOS App Store'dan satın aldıysanız, diğer iOS cihazlarınızda da kullanabilirsiniz.

Android tabletiniz için Google Play'den satın aldıysanız, diğer Android cihazlarınızda da kullanabilirsiniz.

Ancak Nomad'ı Android'de satın aldıktan sonra bir iPad alırsanız, yeniden satın almanız gerekir.

Bunun nedeni, Nomad'ın kendi lisans sunucusunun ya da abonelik modelinin olmamasıdır. Apple/Google/AppGallery arasında lisans paylaşımını sağlayan bir anlaşma yoktur. 


### Satın alımımı nasıl geri yüklerim? {#restore}
Google Play ve AppGallery eşitlemeyi otomatik olarak yapar.

- Hakkında menüsüne gidin (sol üstteki Nomad simgesi) ve `Satın almayı geri yükle` düğmesine basın
- Nomad'ı satın alırken kullandığınız hesapla oturum açtığınızdan emin olun (Google Play'de).
- Cihazı yeniden başlatın
- Bazen birkaç saat beklemeniz gerekir
- Google Play uygulamasının güncel olduğundan emin olun
- Nomad'ı yeniden yükleyin (hiçbir şey kaybetmek istemiyorsanız [dosyalarınızı yedeklemeyi](#locate) unutmayın)
- Ne olacağını görmek için yeniden satın almayı deneyebilirsiniz (not: aynı hesapta aynı ürünü iki kez satın alamazsınız)

:::tip
Bana <support@nomadsculpt.com> adresinden ulaşabilirsiniz, ama yapabileceğim *tek* şey bir e-posta adresiyle ilişkili bir satın alım olup olmadığını doğrulamak olacaktır.

Yeni bir cihaz edindikten sonra lisansların doğru güncellenmediğine dair düzenli olarak bildirim aldığımı belirtmeliyim.
Ödeme ve hesap eşitlemesi üzerinde hiçbir kontrolüm yok, hepsi Google/AppGallery tarafından yönetiliyor!

Satın alım eninde sonunda her zaman geri yükleniyor, ama süreci hızlandırmak için gereken adımlar belirsiz.
:::

::: warning
Yeni Huawei cihazların Google hizmetlerine erişimi yoktur.
Bu durumda uygulamayı AppGallery'de (Huawei uygulama mağazası) yeniden satın almanız gerekir.
:::

### [Dilim] çevirisini yapabilir ya da düzeltebilir misiniz? {#locale}
Yeni bir dil eklemek benim için görece kolay, ama düzenli güncellemelerle başa çıkmak çok daha kolay olduğu için yapay zekâ çevirisine güveniyorum.
Çeviri dosyalarını [burada](https://github.com/stephomi/nomad-translation) bulabilirsiniz.

## Özellikler {#features}

### Gizmo neden hareket etmiyor? {#gizmo-not-moving}
[Sol menü araç çubuğunda tutturma etkin](tools#left-menu-toolbar) olabilir. 

### Nomad'da animasyon yapabilir miyiz? {#animate}
Şimdilik hayır. Katmanları canlandırabilen bir zaman çizelgesi özelliği ilginç olabilir, ama şu an pek planlanmıyor.  

İleride rigging/skinning desteklemek isterim, ama bunun bazı zorlukları var (özellikle heykel araçlarıyla etkileşimi...), bu yüzden şimdilik kesin bir şey yok.


### Düzgün low-poly modelleme yapabilir miyiz? {#lowpoly}
Şimdilik hayır.
Bu aslında Nomad *Sculpt*'un kapsamında değil, ama belki ileride birkaç araç sunarım.


### UV ve doku çalışması yapabilir miyiz? {#texturing}
Kısa cevap: Evet. Uzun cevap: Doğrudan değil, ama Nomad'ın mükemmel verteks boyama araçlarını UV'ler ve dokularla birleştirmenin birkaç yolu var.

* Nomad renk, pürüzlülük ve malzeme özelliklerini doğrudan heykelinizin verteksleri içine boyamanıza olanak tanır.
* Nomad çok yüksek verteks sayılarına izin verir, böylece UV'leri dert etmeden boyayabilirsiniz.
* Nomad fırçalarda kullanmak için doku yükleyebilir; bu da dokularla damgalama ve boyama yapmanızı sağlar.
* Nomad, işleme amacıyla önceden doku atanmış nesneleri yükleyebilir.
* Nomad düşük poligonlu nesnelerin [UV açılımını](topology.md#uv-unwrap-uvatlas) yapabilir.
* Renk/pürüzlülük/metaliklik, [yansıtma seçenekleriyle](topology.md#reproject-to-vertex) dokulardan vertekslere aktarılabilir.
* Renk/pürüzlülük/metaliklik/normaller, [pişirme seçenekleriyle](topology.md#bake-texture) vertekslerden dokulara pişirilebilir
* Pişirme ve yansıtma tek nesneler ya da birçok nesne arasında veya tek bir nesnenin en yüksek ve en düşük alt bölüm seviyeleri arasında yapılabilir; bu da çeşitli pişirme ve yansıtma iş akışlarına olanak tanır.
* Pişirmeden sonra bir OBJ dışa aktarmak dokuları da dışa aktarır; bunları doğrudan dokular üzerinde boyamak için Procreate gibi bir uygulamaya götürebilirsiniz.

### Döner platform videosu kaydedebilir miyim? {#video}
Şimdilik planlanmıyor; iOS'ta kullanımı çok kolay bir [ekran kaydı özelliği](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) var.

iOS'ta bunu sol üstten aşağı kaydırıp kayıt düğmesine dokunarak yaparsınız. 3 saniyelik bir geri sayım başlar; menüyü kaydırarak Nomad'ı ortaya çıkarın ve döner platform özelliğini kullanın. Bittiğinde sağ üstten yeniden aşağı kaydırın ve kayıt düğmesine tekrar dokunun. Videonun başındaki ve sonundaki fazla kısımları çıkarmak için videoyu fotoğraf arşivinden düzenleyin.

### [favori-özellik] için üst düzey bir düğme ekleyebilir misiniz? {#interface}
Evet, alt araç çubuğu artık [arayüz](interface.md#shortcuts) menüsünden özelleştirilebiliyor ve artık kayan araç çubukları da oluşturulabiliyor.

### Sıradaki özellikler neler? {#next-features}
Orta/uzun vadeli yol haritası için birçok fikrim var ama henüz bilmiyorum.  

Hata düzeltmeleri ve mevcut özelliklerin geliştirilmesi, yeni özellik eklemekten her zaman daha önceliklidir.


### Nomad'da rig yapabilir miyiz? {#rigging}
Hayır, ama planlanıyor. Şimdilik şekilleri birbirine bağlayabilir ve eksen noktalarını değiştirerek basit poz verilebilir heykeller yapabilirsiniz.

### 4'ten fazla ışık kullanabilir miyiz? {#lights}
Mobilde en fazla 4, masaüstünde en fazla 6 ışık kullanabilirsiniz. Bu, Nomad'daki gerçek zamanlı işleme motorunun bir sınırlamasıdır. [Bu eğitimde](https://www.youtube.com/watch?v=QhrUGH7CuUA) gösterildiği gibi, yayıcı nesneler ve süreç sonrası işlemlerdeki küresel aydınlanma ile daha fazla ışık varmış gibi gösterebilirsiniz

### Zbrush araçlarını içe aktarabilir miyiz? {#zbrush-import}
Hayır, Zbrush kendine özel bir format kullanıyor. Alfa haritalarını çıkarıp Nomad'da kullanabilmeniz gerekir. 

### Renkler neden boyadığımla eşleşmiyor? İşlemede neden beyaz elde edemiyorum? {#paint-pbr}
Bir kâğıt parçasının, bir masa lambasının ve güneşin fotoğrafını çektiğinizi düşünün. Eski kameralar ve ekranlar hepsini 'beyaz' yapar. Daha modern sistemler ise kâğıdın yansıttığı beyaz, lambanın yaydığı ışık ve güneşin aşırı parlaklığı arasındaki farkı gösterebilir.

Modern bilgisayar grafikleri, ışığın ve yüzeylerin fiziğini taklit ederek benzer şekilde çalışmaya çalışır. Buna `Fiziksel Tabanlı İşleme` ya da PBR denir ve Nomad'ın PBR işleyicisi buna dayanır. Bu gerçekçi ve dengeli görünür, ancak parlak boyanmış renkler çoğu zaman daha koyu görünür.

İşlemenin boyanmış renklere daha yakın olması gerekiyorsa, bunu hem fiziksel tabanlı olmayan hem de fiziksel tabanlı yollarla düzeltebilirsiniz:

PBR olmadan:
* `Gölgelendirme menüsünde 'Aydınlatmasız' kipini kullanın`. Renkler tam boyandığı gibi görünür, ama tüm gölgelendirmeyi de kaybedersiniz. Hızlı kontroller ve daha grafik bir çıktı için kullanışlıdır.
* `Gölgelendirme menüsünde 'MatCap' kipini kullanın`. Renk tonu olmayan, çoğunlukla beyaz, daha parlak bir matcap seçin.

PBR ile:
* `Nötr bir ortam kullanın`. [Ortamı](shading.md#environment) daha nötr bir ortamla değiştirebilirsiniz. Daha renkli olma eğiliminde oldukları için iç mekân ortamlarından kaçının. Bunun yerine gün ışığında bir dış mekân ya da stüdyo ortamını tercih edin.
* `Aydınlatmayı güçlendirin`. Karanlık bir odada beyaz bir kâğıdın fotoğrafını çekiyor olsaydınız, sadece daha fazla ışık eklerdiniz. Ortam ışığında, renkler size doğru gelmeye başlayana kadar pozlandırma kaydırıcısını artırın ya da daha yoğun ayrı ışıklar ekleyin.
* `Kamera pozlandırmasını artırın`. Karanlık odada fazladan ışık yoksa, kameranın deklanşörünü daha uzun açık tutabilir ya da daha hassas bir ISO kullanabilirdiniz. Nomad'da benzer bir sonucu süreç sonrası işlemlerle elde edebilirsiniz. Süreç sonrası işlemlere gidin, etkinleştirin, ton eşleştirmeye inin, etkinleştirin ve renkler doğru gelene kadar pozlandırma kaydırıcısını artırın.
* `Yayıcı renk kullanın`. Malzeme menüsünde, dokular altındaki 'Yayıcı' seçeneğini etkinleştirebilirsiniz; bu, bir nesnenin ışık kaynağı gibi görünmesini sağlar. Süreç sonrası işlemler ayarlarında küresel aydınlanmayı açarsanız, sahnedeki diğer nesnelere de ışık yayar. O malzeme için 'Her zaman aydınlatmasız' seçeneğini de etkinleştirebilirsiniz; bu, doku olmadan benzer bir görünüm sağlar.

## Çökmeler {#crashes}

### Modelimi kaydederken ya da yeniden ağ örgülendirirken çöküyor! {#crash-remesh}
Cihazınızın belleği (RAM) yetmiyor.  
Sahnenizdeki bellek kullanımını azaltmak için poligon sayısını düşüren [Topoloji](topology.md) seçeneklerinden bazılarını kullanabilirsiniz.

::: tip RAM/Depolama
Önemli olan RAM miktarıdır, depolama alanı değil (depolama genellikle çok daha büyüktür).
:::


### Projemi yüklerken çöküyor! {#crash-load}
Dosya küçükse bana gönderebilirsiniz, bir göz atarım (e-posta: <support@nomadsculpt.com>).

Aksi halde cihazın RAM belleği muhtemelen yetmiyordur.

- Cihazınızda açık olan diğer tüm uygulamaları kapattığınızdan emin olun.
- Açık bir proje varken değil, Nomad'da yeni bir proje başlatmışken yükleyin.
- Hâlâ çöküyorsa tek çözüm, [proje dosyanızı](#locate) daha fazla belleği olan bir cihazda yüklemektir.

::: tip
Mobil cihazınız projeyi yükleyemiyorsa [masaüstü sürümünü](https://nomadsculpt.com) deneyin. Projeleri içe ve dışa aktarmak için Demo kipinde ücretsiz kullanabilirsiniz, ancak yalnızca birkaç düzenleme aracı kullanılabilir.

Projeniz [Katmanlar](layers.md) kullanıyorsa, bellek kullanımını azaltmak için onları birleştirmek isteyebilirsiniz.
:::

### Nomad'ı başlatırken çöküyor! {#crash-start}
Yükleme sırasında çöküyorsa, Nomad'ın Nomad klasöründeki belirli bir dosyada sorun yaşadığı anlamına gelir.

Çoğu zaman bunun nedeni projenin ağır olması ve ne yazık ki RAM sınırını aşmasıdır.

[Nomad klasörünü](#locate) bulun, ardından suçluyu bulmak için bazı dosyaları yeniden adlandırın ya da taşıyın.

Önce `settings.json` dosyasını yeniden adlandırmayı deneyin. Böylece son projeyi yüklemeyi bırakır.

İşe yaramazsa, son dosyalardan bazılarını kendi kaynak klasörlerinin (`projects`, `matcaps`, `environments` vb.) dışına taşımayı deneyin.

Klasörlerin kendisini de yeniden adlandırabilirsiniz, böylece Nomad onları tamamen yok sayar.
Nomad klasöründeki tüm dosyaları yeniden adlandırır ya da taşırsanız, temiz bir kurulumla aynı sonucu elde edersiniz.

::: tip
Nomad başlangıçta bir dosya yüklediğinde, dosyayı her zaman `can_be_deleted/` klasörüne taşır.
İşlem başarılı olursa dosya özgün klasörüne geri taşınır.

Yükleme bitmeden çökerse, Nomad bir sonraki açılışta `can_be_deleted/` klasörünü yok saydığı için sorunsuz başlar.

Başarılı olabileceğini düşünüyorsanız bu dosyayı yeniden yüklemeyi deneyebilirsiniz.
:::
