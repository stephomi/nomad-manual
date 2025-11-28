# ![](/icons/faq.webp) SSS {#faq}

[[toc]]

## Platform {#platform}
### Projelerim cihazımda nerede bulunur? {#locate}
Projeler, ana Nomad klasörünün içindeki `projects` klasöründe bulunur.

iOS’ta, iOS Dosyalar uygulamasıyla Nomad klasörüne erişebilirsiniz.

Android’de Nomad klasörü `Android/data/com.stephaneginier.nomad/files/` içindedir.  
Android’in son sürümlerinde (10/11) artık `Android/data` klasörüne erişiminiz yok.
Ayrı bir uygulama üzerinden erişebilirsiniz, örneğin [şu uygulama](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Beta testi yapmanın bir yolu var mı? {#beta}
Windows & MacOS için, [Ana Sayfa](https://nomadsculpt.com)’da bir beta mevcut olabilir.
<br>
iOS için özel bir TestFlight var, [Discord](https://discord.com/invite/8h7BwpRz29)’da #beta-ios kanalını ziyaret edin.
<br>
[Web Demo](https://nomadsculpt.com/demo) genellikle en son özelliklerle güncellenir.

### Neden Android'de ücretsiz deneme var da iOS'ta yok? {#android-trial}
Çünkü eski Android cihazlar berbat (ve bazı yenileri de öyle...), ve insanların uygulamayı satın alıp siyah bir ekranla karşılaşmasını istemedim.
Ama asıl sebep, ücretli Android uygulamalarının pek standart olmamasıydı.

### Nomad'i çalıştırmak için en iyi tablet hangisi? {#best-tablet}

Kısaca: Bir iPad.

Biraz daha uzun cevap ise:

> "Gerçekten Apple’dan nefret etmiyorsanız, _alabileceğiniz en yeni_ iPad. Apple’dan nefret ediyorsanız, alabileceğiniz en yeni Samsung tablet. Diğer her şey için, önce test edin." 

İnsanlar her zaman daha fazla bilgi istiyor, işte özet.

Nomad en iyi yeni iPad’lerde çalışır:

* iPad ve iPhone’lar [Exoside](https://exoside.com/) firmasının [Quad Remesher](tools#quad-remesher) eklentisine erişebilir
* son iPad’ler, en yeni kalem desteğiyle [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0) özelliğini destekler, Nomad’de bazı araçlarda kalemi bükerek kullanabilirsiniz. 
* en yeni M serisi çiplerin performansı çok hızlıdır. 

Mevcut en pahalı, en yeni iPad, son görüntüleri çok hızlı render edebilir ve çok detaylı heykeller yapmanıza izin verir.

Ancak, daha ucuz ve eski iPad’lerdeki performans düşüşü insanların beklediği kadar kötü değildir. Apple Pencil destekleyen herhangi bir iPad, Nomad’i oldukça iyi çalıştırır. Örneğin:

* 2023 iPad Pro, 5 milyon poligonluk heykelleri tepkisel şekilde işleyebilir, son kalite bir görüntü 5 saniyede render edilebilir.
* 2015 iPad Pro, 1,2 milyon poligonluk bir nesneyi biraz gecikmeyle işleyebilir, son kalite bir görüntü 20 saniyede render edilebilir.

Bu büyük bir performans farkı, ama fiyatı da hesaba katmanız gerekir:

* 2025 iPad Pro, tüm seçeneklerle birlikte sıfır olarak *2500 $ USD*’dir. 
* 2023 iPad Pro şu anda eBay’de *400 $ USD* civarındadır.
* 2015 iPad Pro eBay’de *250 $ USD* civarındadır.

Ek 4 milyon poligon ve 15 saniye tasarruf 2100 $ etmeye değer mi? Bu size kalmış.

Pro olmayan modeller daha da ucuz olabilir ve seçebileceğiniz geniş bir boyut ve performans yelpazesi sunar. Mevcut iPad Air, barrel roll destekli 2. nesil kalemi destekler ve Pro’dan oldukça ucuzdur. İkinci el ve yenilenmiş pazarında daha da fazla seçenek vardır. 

Bu, bütçeniz ne olursa olsun size uygun bir iPad bulabileceğiniz anlamına gelir. Ve unutmayın, çoğu heykel milyonlarca poligon içermez! 500.000 poligonun altında kalabilirseniz, eski iPad’ler bile hızlıca heykel yapmanıza izin verir.

`Peki ya Android?`

Android grafik performansı iPad’lerden düşüktür. Nomad’in geliştiricisine göre, “Bir Samsung Galaxy Tab S9, Nomad’i bir iPad Air’den bir büyüklük mertebesi daha yavaş çalıştırır.” Yine de birçok kullanıcı Samsung tabletlerinden çok memnun, Nomad çoğu heykel için gayet iyi çalışıyor. 

Diğer Android tabletler için dikkatli olun. Android donanımı performans açısından çok değişken olabilir, Nomad’in nasıl çalışacağını tahmin etmek kolay değildir.

Lütfen önce ücretsiz, kaydetme devre dışı bırakılmış Nomad sürümünü kullanarak test edin. 

`Peki ya bellek ve depolama?`

Çoğu Nomad dosyası 100 MB veya daha küçüktür. Bu da günümüzde alacağınız hemen her tablette, iPad veya Android fark etmeksizin, Nomad projeleriniz için fazlasıyla yer olacağı anlamına gelir.


### Nomad'i bir cihaz için satın aldım, başka bir cihazda kullanabilir miyim? {#multi-devices}
Aynı uygulama mağazasını ve aynı hesabı kullandığı sürece, evet.

Örneğin iOS uygulama mağazasından satın aldıysanız, diğer iOS cihazlarınızda kullanabilirsiniz.

Android tabletiniz için Google Play’den satın aldıysanız, diğer Android cihazlarınızda kullanabilirsiniz.

Ancak Nomad’i Android’de satın alıp sonra bir iPad alırsanız, yeniden satın almanız gerekir.

Bunun sebebi, Nomad’in kendi lisans sunucusu veya abonelik modelinin olmamasıdır. Apple/Google/AppGallery arasında lisans paylaşımını yönetecek bir anlaşma yoktur. 


### Satın almamı nasıl geri yüklerim? {#restore}
Google Play ve AppGallery senkronizasyonu otomatik olarak halleder.

- Hakkında menüsüne gidin (sol üstteki nomad simgesi) ve `restore purchase` düğmesine basın
- Nomad’i satın almak için kullandığınız hesapla (Google Play’de) oturum açtığınızdan emin olun.
- Cihazı yeniden başlatın
- Bazen birkaç saat beklemeniz gerekebilir
- Google Play uygulamasının güncel olduğundan emin olun
- Nomad’i yeniden yükleyin (hiçbir şeyi kaybetmek istemiyorsanız [dosyalarınızı yedeklediğinizden](#where-are-my-projects-located-on-my-device) emin olun)
- Ne olacağını görmek için tekrar satın almaya çalışabilirsiniz (not: aynı hesapta aynı ürünü iki kez satın alamazsınız)

:::tip
Bana <support@nomadsculpt.com> adresinden ulaşabilirsiniz, ancak yapabileceğim *tek* şey bir e-postanın ona bağlı bir satın alma olup olmadığını doğrulamaktır.

Yeni bir cihaz aldıktan sonra lisansların doğru şekilde güncellenmemesiyle ilgili düzenli olarak raporlar alıyorum.
Ödeme ve hesap senkronizasyonu üzerinde hiçbir kontrolüm yok, bunların hepsi Google/AppGallery tarafından yönetiliyor!

Sonunda satın alma her zaman geri yükleniyor, ancak süreci hızlandırmak için gerekli adımlar net değil.
:::

::: warning
Yeni Huawei cihazlarının Google hizmetlerine erişimi yoktur.
Bu durumda uygulamayı AppGallery’den (Huawei uygulama mağazası) tekrar satın almanız gerekir.
:::

### [Benim-dilim] için çeviri yapabilir veya düzeltme yapabilir misiniz? {#locale}
Görece kolayca başka bir dil ekleyebilirim, ancak düzenli güncellemeleri daha kolay yönetebilmek için yapay zekâ çevirisine güveniyorum.
Çeviri dosyalarını [burada](https://github.com/stephomi/nomad-translation) bulabilirsiniz.

## Özellikler {#features}

### Neden gizmo hareket etmiyor? {#gizmo-not-moving}
Muhtemelen [sol menü araç çubuğunda sabitleme (pin) etkin](tools#left-menu-toolbar). 

### Nomad içinde animasyon yapabilir miyiz? {#animate}
Şimdilik hayır. Katmanları animasyonlu hale getirebilecek bir zaman çizelgesi özelliği ilginç olabilir, ancak şu anda pek planlanmıyor.  

Gelecekte rigging/skin’leme desteği vermek isterim, ancak bazı zorluklar barındırıyor (özellikle heykel araçlarıyla etkileşim...) bu yüzden şimdilik kesin bir şey yok.


### Düzgün low-poly modelleme yapabilir miyiz? {#lowpoly}
Şimdilik hayır.
Bu aslında Nomad *Sculpt*’un kapsamına pek girmiyor, ama belki gelecekte birkaç araç sağlayabilirim.


### UV ve dokulama yapabilir miyiz? {#texturing}
Kısa cevap: Evet. Uzun cevap: Doğrudan değil, ama Nomad’in mükemmel vertex boyama araçlarını UV ve kaplamalarla birleştirmenin birkaç yolu var.

* Nomad, heykelinizin vertekslerine doğrudan renk, pürüzlülük ve malzeme özellikleri boyamanıza izin verir.
* Nomad, UV’lerle uğraşmadan boyama yapabilmeniz için çok yüksek vertex sayısına izin verir.
* Nomad, fırçalarda kullanmak üzere kaplamalar yükleyebilir, böylece damgalama ve kaplamayla boyama yapabilirsiniz.
* Nomad, önceden atanmış kaplamalara sahip nesneleri, render amaçlı yükleyebilir.
* Nomad, düşük poligonlu nesneleri [UV açabilir](topology.md#uv-unwrap).
* Renk/pürüzlülük/metaliklik, [proje seçenekleri](topology.md#reproject-to-vertex) aracılığıyla kaplamalardan vertekslere aktarılabilir.
* Renk/pürüzlülük/metaliklik/normaller, [pişirme seçenekleri](topology.md#bake-to-texture) aracılığıyla vertekslerden kaplamalara pişirilebilir.
* Pişirme ve projeksiyon, tek nesneler veya birçok nesne arasında, ya da tek bir nesnenin en yüksek ve en düşük alt bölüm seviyeleri arasında yapılabilir; bu da çeşitli pişirme ve projeksiyon iş akışlarına olanak tanır.
* Pişirmeden sonra bir obj dosyası dışa aktarmak, kaplamaları da dışa aktarır; bunlar Procreate gibi bir uygulamaya alınıp doğrudan kaplamalar üzerinde boyama yapmak için kullanılabilir.

### Bir turntable videosu kaydedebilir miyim? {#video}
Şimdilik planlanmıyor, iOS’ta kullanımı çok kolay bir [video kaydetme özelliği](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) var.

iOS’ta bu, sol üstten aşağı kaydırıp kayıt düğmesine dokunarak yapılır. Size 3 saniyelik bir geri sayım verir, menüyü kaydırarak Nomad’i görünür hale getirin ve turntable özelliğini kullanın. İşiniz bittiğinde, tekrar sağ üstten aşağı kaydırın ve kayıt düğmesine tekrar dokunun. Fotoğraf kitaplığından videonun başındaki ve sonundaki fazlalıkları keserek düzenleyin.

### [favori-özelliğimi] en üst seviye bir düğme olarak ekleyebilir misiniz? {#interface}
Evet, alt araç çubuğu artık [arayüz](interface.md) menüsünden özelleştirilebilir ve yüzen araç çubukları oluşturulabilir.

### Sıradaki özellikler neler? {#next-features}
Orta/uzun vadeli yol haritası için birçok fikrim var ama henüz bilmiyorum.  

Hata düzeltmeleri ve mevcut özellikleri iyileştirmek, her zaman yeni özellikler eklemenin önünde önceliğe sahip olacak.


### Nomad'de rig yapabilir miyiz? {#rigging}
Hayır, ama planlanıyor. Şimdilik şekilleri birbirine bağlayabilir ve pivot noktalarını değiştirebilirsiniz, bu da basit pozlanabilir heykellere izin verir.

### 4'ten fazla ışık kullanabilir miyiz? {#lights}
Hayır, bu Nomad’in gerçek zamanlı render motorunun bir sınırlamasıdır. Bunu, [bu eğitimde](https://www.youtube.com/watch?v=QhrUGH7CuUA) gösterildiği gibi, emisyonlu nesneler ve son işlemde global aydınlatma kullanarak taklit etmek mümkündür.

### Zbrush tool'larını içe aktarabilir miyiz? {#zbrush-import}
Hayır, Zbrush özel bir format kullanır. Alpha haritalarını çıkarıp Nomad’de kullanabilmeniz gerekir. 

### Neden renkler boyadığım gibi görünmüyor? Neden render'da beyaz elde edemiyorum? {#paint-pbr}
Bir kâğıt parçasının fotoğrafını çektiğinizi, bir masa lambasının fotoğrafını çektiğinizi ve güneşin fotoğrafını çektiğinizi düşünün. Eski kameralar ve ekranlar bunların hepsini sadece ‘beyaz’ yapar. Daha modern sistemler, kâğıdın yansıttığı beyaz ile lambanın yaydığı ışık ve güneşin süper parlaklığı arasında fark gösterebilir.

Modern bilgisayar grafikleri benzer bir şekilde çalışmaya çalışır, ışığın ve yüzeylerin fiziğini taklit eder. Buna `Fiziksel Tabanlı Render` veya PBR denir ve Nomad’in PBR render’ı buna dayanır. Bu gerçekçi ve dengeli görünür, ancak çoğu zaman parlak boyanmış renkler daha koyu görünür.

Render’ın boyadığınız renklere daha yakın olmasını istiyorsanız, bunu hem fiziksel tabanlı olmayan hem de fiziksel tabanlı yollarla düzeltebilirsiniz:

PBR olmayan:
* `Aydınlatma menüsünde 'Unlit' modunu kullanın`. Renkler tam olarak boyandığı gibi gösterilir, ancak tüm gölgelendirmeyi de kaybedersiniz. Hızlı kontroller ve daha grafiksel çıktı için kullanışlıdır.
* `Aydınlatma menüsünde 'Matcap' modunu kullanın`. Çoğunlukla beyaz, renk tonu olmayan daha parlak bir matcap seçin.

PBR:
* `Nötr bir ortam kullanın`. [Ortamı değiştirebilir](shading.md#environment) ve daha nötr bir ortam seçebilirsiniz. İç mekân ortamlarından kaçının, genellikle daha renklidirler. Bunun yerine gün ışığı dış mekân veya stüdyo ortamını tercih edin.
* `Aydınlatmayı artırın`. Karanlık bir odada beyaz kâğıdın fotoğrafını çekiyor olsaydınız, basitçe daha fazla ışık eklerdiniz. Ortam ışığında, renkler size doğru gelene kadar pozlama kaydırıcısını artırın veya daha yüksek yoğunluklu ek ışıklar ekleyin.
* `Kamera pozlamasını artırın`. Karanlık odada ekstra ışık yoksa, kamera deklanşörü daha uzun süre açık tutabilir veya daha hassas bir ISO kullanabilirdi. Nomad’de benzer bir sonucu son işlemle elde edebilirsiniz. Post process’e gidin, etkinleştirin, tone mapping bölümüne inin, etkinleştirin ve renkler doğru gelene kadar pozlama kaydırıcısını yükseltin.
* `Emissive renk kullanın`. Malzeme menüsünde, bir nesnenin ışık kaynağı gibi görünmesini sağlayan ‘emissive’i dokular altında etkinleştirebilirsiniz. Post process ayarlarında global aydınlatmayı açarsanız, sahnedeki diğer nesnelerin üzerine ışık düşürecektir. Ayrıca o malzeme için ‘unlit’i etkinleştirebilirsiniz, bu da benzer bir görünümü doku olmadan sağlar.

## Çökmeler {#crashes}

### Modelimi kaydederken veya yeniden mesh yaparken çöküyor! {#crash-remesh}
Cihazınızın belleği (RAM) tükeniyor.  
Sahnenizdeki bellek kullanımını azaltmak için, poligon sayısını azaltmak amacıyla bazı [Topoloji](topology.md) seçeneklerini kullanabilirsiniz.

::: tip RAM/Depolama
Önemli olan RAM miktarıdır, depolama alanı (genellikle çok daha büyüktür) değil.
:::


### Projemi yüklerken çöküyor! {#crash-load}
Dosya küçükse, bana gönderebilirsiniz, bir göz atarım (e-posta ile <support@nomadsculpt.com>).

Aksi halde cihaz muhtemelen RAM belleğinin sınırına ulaşıyordur.

- Cihazınızda açık olan diğer tüm uygulamaları kapattığınızdan emin olun.
- Halihazırda bir proje açık tutmak yerine Nomad’de yeni bir proje başlatın.
- Hâlâ çöküyorsa, [proje dosyanızı](#where-are-my-projects-located-on-my-device) daha fazla belleğe sahip bir cihaza yüklemek tek çözümdür.

::: tip
Masaüstü bir tarayıcıda, dosyanızı [bu adreste](https://nomadsculpt.com/demo_save/) yüklemeyi deneyebilir ve ardından sahnenizi basitleştirdikten sonra tekrar dışa aktarabilirsiniz.

Bazı tarayıcılar tek bir sekmenin kullanabileceği RAM miktarını sınırlar, bu nedenle bu tekniğin işe yaramaması mümkündür.

Projeniz [Katmanlar](layers.md) kullanıyorsa, bellek kullanımını azaltmak için onları birleştirmek isteyebilirsiniz.
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

### Nomad'i başlatırken çöküyor! {#crash-start}
Yükleme sırasında çöküyorsa, Nomad’in Nomad klasöründe bulunan belirli bir dosyayla sorun yaşadığı anlamına gelir.

Çoğu zaman, proje ağır olduğu için olur ve maalesef RAM sınırını aşar.

[Nomad klasörünü](#where-are-my-projects-located-on-my-device) bulun ve ardından sorunu bulmak için bazı dosyaları yeniden adlandırın veya taşıyın.

Önce `settings.json` dosyasını yeniden adlandırmayı deneyin. Böylece son projeyi yüklemeyi durdurur.

Bu işe yaramazsa, bazı son dosyaları kendi kaynak klasörlerinden (`projects`, `matcaps`, `environments`, vb.) dışarı taşımayı deneyin.

Nomad’in onları tamamen yok sayması için klasörlerin kendilerini de yeniden adlandırabilirsiniz.
Nomad klasöründeki tüm dosyaları yeniden adlandırır veya taşırsanız, bu temiz bir kurulumla aynı sonucu verir.

::: tip
Nomad başlangıçta bir dosya yüklediğinde, dosyayı her zaman `can_be_deleted/` klasörüne taşır.
İşlem başarılı olursa, dosya tekrar orijinal klasörüne taşınır.

Yükleme tamamlanmadan önce çökme olursa, Nomad bir sonraki başlatmada sorunsuz açılır, çünkü `can_be_deleted/` klasörünü yok sayar.

Başarılı olabileceğini düşünüyorsanız bu dosyayı tekrar yüklemeyi deneyebilirsiniz.
:::