# ![](/icons/sliders.webp) Arayüz Menüsü {#interface-menu}

Bu menü, Nomad'ın arayüzünü özelleştirmek için birçok seçenek içerir. 

![](/images/interface_overview2.webp)

Nomad oldukça derinlemesine özelleştirilebilir; bu menü 5 sekmeye ayrılmıştır: Arayüz, Kısayollar, Hareket, Atamalar, Ayıkla.

![](/images/interface_menu.webp)


::: tip
Bu sayfa arayüzün kendisini değil, arayüz menüsünü anlatıyor! Arayüzün geneli [Başlarken](gettingstarted.md) sayfasında anlatılıyor.
:::

## ![](/icons/sliders.webp) Arayüz {#interface}

Arayüz sekmesi, Nomad kullanıcı arayüzünün rengini, boyutunu ve düzenini kontrol eder. İki alt sekmesi vardır: `Görünüm` ve `Düzen`.

![](/images/interface_overview3.webp)

### ![](/icons/palette.webp) Renkler {#presets}

![](/images/interface_presets.webp)

`Görünüm` alt sekmesi, arayüz için hazır renk ayarlarından oluşan bir koleksiyonla başlar. Birini uygulamak için ona dokunun, sonra aşağıdaki seçeneklerle ince ayar yapın.

#### Vurgu ve Taban {#color-widgetcolor-base}
Arayüzde kullanılan ana renkler: seçili düğmeler ve kaydırıcı çubukları için `Vurgu`, paneller için `Taban`.

#### Metin opaklığı {#text-opacity}
Metinleri ve simgeleri panellerin üzerinde daha yumuşak gösterir.

#### Açma/kapama düğmeleri, Onay kutusu, Sekmeler {#high-contrast-button}
Açma/kapama düğmelerinin (`Yumuşak` veya `Dolu`), onay kutularının (`Dış Hatlar`, `Vurgu` veya `Dolgu`) ve sekmelerin (`Alt çizgi`, `Yumuşak` veya `Dolu`) stili.

#### Renkli araçlar {#colored}
Simgeleri kategoriye göre renklendirir; örneğin tüm maske araçları kahverengi, ayırma araçları kırmızı, düzleştirme araçları yeşil vb.

#### Panel gölgesi {#material-color-preview}
Paneller sahneden ayrışmak için gölge düşürür.

#### Şeffaf panel {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Açıkken, Nomad'daki menülerin ve panellerin görünümünü kontrol eden ek seçenekler belirir: `Panel tonu` rengini, `Bulanıklık seviyesi` arkadaki sahnenin ne kadar bulanıklaşacağını belirler, `Cam` ise kenarlara kırılma ve parlama efektleri ekler; bu efektler düşük bulanıklıkta daha belirgindir.

::: tip
Küçük cihazlarda panel tonunu neredeyse beyaz ve şeffaf yapıp bulanıklık seviyesini düşük tutmak işe yarayabilir; böylece menüler sahneyi kapatmaz.
:::

#### ![](/icons/reset.webp) Görünümü sıfırla {#reset-style}
Tüm görünüm seçeneklerini varsayılan değerlerine döndürür.

### ![](/icons/panel_detach.webp) Düzen {#layout}

`Düzen` alt sekmesi, öğelerin nerede duracağını ve ne kadar büyük olacağını kontrol eder.

#### Araç kutusu {#toolbox}

Nomad arayüzünün sağındaki araç menüsü için seçenekler.

![](/images/interface_toolbox.webp)

##### ![](/icons/resize_bottom_right.webp) Yeniden Boyutlandır {#ui-resize-corner}

Araç kutusunun alt köşesindeki yeniden boyutlandırma tutamacını açıp kapatır.

##### Gizle {#hidden}
Normalde üst çubuktaki araç kutusu simgesi, uzun tek sütunlu bir araç listesi ile çok sütunlu bir liste arasında geçiş yapar. Bu seçenekle simge, çok sütunlu liste ile tamamen gizli olma arasında geçiş yapar.

##### Sıralamasını sıfırla {#reset-order}
Araç kutusundaki varsayılan araçları varsayılan sıralarına döndürür. Özel simgeler listenin sonunda, araç kutusunda kalır.

#### Üst bar {#rows-auto-1}
`Duyarlı`, üst çubuk ekrana sığmadığında ne olacağını seçer; çoğunlukla küçük ekranlarda önemlidir: `Çok Satırlı` menüleri birkaç satıra yayar, `Kaydır` ise kaydırabileceğiniz tek bir satır tutar.

#### Üst çubuğu aynala {#mirror-top-bar}
Üst çubuktaki menülerin sırasını tersine çevirir.

#### Yan çubukları aynala {#mirror-side-bars}
Yan çubukların yerini değiştirir; böylece araç kutusu solda, araç seçenekleri sağda olur.

#### Alt çubuğu aynala {#mirror-bottom-bar}
Alt çubuğu sağ alt köşeye taşır ve düğmelerin sırasını tersine çevirir.

#### ![](/icons/move.webp) Paneli sürükle {#drag-panel}
Yüzen bir panel her zaman çubuğundan sürüklenerek taşınır; bu seçenek onu gövdesinden de sürüklemenizi sağlar. `Otomatik` durumunda parmak veya kalem paneli yalnızca sürükleme dikeyden çok yataysa taşır, böylece dikey sürükleme yine içeriği kaydırır. Fareyle de, her yönde sürükleyebilmek için `Evet` olarak ayarlayın.

#### ![](/icons/pencil.webp) Nomad İletişim Kutusunu Kullan {#use-nomad-dialog}
Bir ad veya değer yazarken sistemin kendi metin iletişim kutusu yerine Nomad'ınkini gösterir.

#### ![](/icons/stylus.webp) Kalem noktası {#hover-dot}
Ekranın üzerinde gezinen bir kalem algılandığında arayüzde küçük bir nokta gösterir.

#### ![](/icons/help.webp) Üzerine gelince yardım {#help-popup-on-hover}

Üzerine gelmeyi (hover) destekleyen cihazlarda, Nomad'daki ![](/icons/help.webp) simgesiyle gösterilen bağlam yardımının üzerine gelince mi yoksa yalnızca tıklandığında mı görüneceğini belirler.

#### Genel ölçek {#overall-scale}
Tüm arayüz öğelerine uygulanan bir boyut çarpanı.
#### Panel genişliği {#panel-width}
Menülerin ve panellerin genişliği.
#### Yazı tipi boyutu {#font-scale}
Yazı tiplerini ölçekler.
#### Dikey boşluk {#vertical-spacing}
Menülerdeki ve panellerdeki öğeler arasındaki boşluk.
#### Dikey boşluk (sol) {#vertical-spacing-left}
Sol araç çubuğundaki öğeler arasındaki boşluk.

#### Kenardan kaydırmalar {#edge-offset}
Bu değerleri yalnızca ekran kenarlarındaki düğmeleri kullanırken sorun yaşıyorsanız değiştirmelisiniz. Bu kaydırıcılar devre dışıysa Nomad, cihazın kendisinden gelen güvenli bölge değerlerini kullanır.

::: tip
Nomad'ı yeni bir cihaza taşırken (örneğin bir iPhone 12'den iPhone 15'e geçerken) kenar seçeneklerini varsayılanlara sıfırlamayı unutmayın!
:::

#### ![](/icons/reset.webp) Düzeni sıfırla {#reset-layout}
Tüm düzen seçeneklerini varsayılan değerlerine döndürür.

## ![](/icons/window.webp) Kısayollar {#shortcuts}

Kısayollar sekmesi, görünümün çevresinde hangi hızlı erişim düğmelerinin görüneceğini seçer ve kendi yüzen araç çubuklarınızı oluşturmanızı sağlar.

### Yan çubuk {#side-bar}
Sol yan çubuğun altındaki hızlı araç düğmeleri: `Pürüzsüzleştir`, `Maske`, `Gizle`, `Yüz Grubu` ve `Gizmo`. Sıralarını değiştirmek için onları sürükleyin.

### Alt çubuk {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Bir kısayolu alt çubuğa eklemek veya çıkarmak için ona dokunun. Şunlar varsayılan olarak açıktır:
* `Geri Al` - önceki işlemi geri alır
* `Yinele` - en son geri alınan işlemi geri getirir
* `Solo` - Diğer tüm nesneleri geçici olarak gizler, yalnızca seçili nesne görünür kalır. Tüm nesneleri geri getirmek için tekrar basın.
* `X-Ray` - Diğer tüm nesneleri geçici olarak yarı saydam yapar, yalnızca seçili nesne opak kalır. Varsayılan malzemeleri geri getirmek için tekrar basın.
* `Voksel` - Mevcut nesneyi en son kullanılan voksel çözünürlüğüyle yeniden örgüler. Uzun dokunma veya yukarı kaydırma, bir çözünürlük kaydırıcısı ve keskin kenarlar düğmesi açar.
* `Izgara` - Görünüm ızgarasını açıp kapatır. Uzun dokunma veya yukarı kaydırma, ızgaranın rengini ve opaklığını değiştirmenizi sağlar.
* `Genel taslak` - Tel kafes katmanını açıp kapatır. Uzun dokunma veya yukarı kaydırma, tel kafesin rengini ve opaklığını değiştirmenizi sağlar.
* `Denetle` - ağınızın UV'ler, pişirilmiş dokular ve diğer özelliklerini Nomad'ın arka planına bindirilmiş olarak görmenizi sağlar.
* `Yüz Grubu` - Yüz grubu katmanını açıp kapatır, daha fazla bilgi [Araçlar->Yüz Grubu](tools.md#facegroup) bölümünde

Sık kullanılan diğer kısayollar da mevcuttur: `Dış Hatlar`, `Projeksiyon` (perspektif veya ortografik), `MatCap`, `DinTopo` ve [Çoklu Çözünürlük](topology.md#multiresolution) için `Alt bölümlere ayır`, `Tersine çevir` ve seviye düğmeleri.

#### ![](/icons/more.webp) Atamalar {#bindings-list}

Nomad'ın neredeyse her işlevi, çubuğun kaç kısayol içerdiğini gösteren atamalar düğmesiyle alt çubuğa eklenebilir. Düğmeye tıklandığında bir atamalar menüsü görüntülenir:

![](/images/interface_bindings_search.webp)

Üstteki simgelerle kategoriye göre arama yapabilir ya da işlevleri adlarıyla bulmak için arama alanını kullanabilirsiniz. Bir işlevi araç çubuğuna eklemek için ona tıklayın. Kaldırmak için tekrar tıklayın.

#### ![](/icons/eye_open.webp) Görülebilir {#order}

Alt çubuğun tamamını gösterir veya gizler.

#### ![](/icons/reset.webp) Sıfırla {#reset}

Sıfırla, alt çubuğu varsayılan ayarlarına döndürür.

### Yüzen pencereler {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

+ düğmesine tıklamak yüzen bir araç çubuğu ekler. Atamalar düğmesine tıklayıp ona birkaç kısayol ekleyene kadar görünmez; sonra görünür yapabilirsiniz.

Birçok araç çubuğu oluşturabilirsiniz; her birinin şu seçeneklerin bulunduğu bir satırı vardır:

* Araç çubuklarını yeniden sıralamak için satırın solundaki tutamacı sürükleyin.
* `İsim` - Araç çubuğunun adı.
* `Görülebilir` - Araç çubuğunun görünürlüğünü açıp kapatır.
* `Çubuk` - Araç çubuğunda bir başlık çubuğu gösterir.
* `Küçültülmüş` - Arayüz küçültüldüğünde araç çubuğunu ekranda tutar.
* `Atamalar` - Araç çubuğuna işlev eklemek veya çıkarmak için atama penceresini gösterir.
* `Sil` - Araç çubuğunu siler.


## ![](/icons/gesture.webp) Hareket {#gesture}
Hareket menüsü, parmağınızın, kaleminizin, farenizin ve izleme dörtgeninizin Nomad'ı nasıl kontrol edeceğini belirler.

![](/images/interface_gesture.webp)

### Hareket seçenekleri {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad, işlemleri giriş cihazına göre sınırlayabilir. Örneğin parmakla sürükleme yalnızca kamerayı hareket ettirirken, kalemle sürükleme yalnızca şekillendirme yapabilir. Fareniz veya izleme dörtgeniniz varsa, onlar da belirli işlemlere atanabilir.

Her satır bir işlemdir: hangi girişlerin bu işlemi yapabileceğini seçmek için `Parmak`, `Stylus` ve `Fare` seçeneklerini açıp kapatın.

* `Kamera` - Kamerayı hareket ettirir.
* `Düğüm düzenleme` - Tuvalde çizilen tutamaçları sürükler; örneğin bir primitifi, eğriyi, tekrarlayıcıyı veya ışığı düzenlemek için.
* `Şekillendir` - Fırçalarla şekillendirir. Aşağıda kendi satırı olan araçlar bu satırı değil, kendi satırlarını izler.
* `Nesne seç` - Bir nesneyi seçmek için ona dokunun.
* `Malzeme seçimi` - İmlecin altındaki rengi veya malzemeyi almak için tuvale uzun basın. Yalnızca mevcut fırçada boyama açıksa çalışır.
* `Dokunuşta` - Maske, Gizle ve Yüz Grubu gibi araçların dokunma kısayolları (aşağıya bakın).
* `Boya` - Boya ve Leke araçları.
* `Maske` - Maske aracı.
* `Yüz` - Gizle ve Yüz Grubu araçları.
* `Oluştur` - Tüp, Torna ve Ekle araçları.
* `Kes` - Kes, Ayır ve Yansıt araçları.
* `Seç` - Seç ve Ölç araçları.
* `Gizmo` - Gizmo ve Kafes araçları.
* `Dönüştür` - Dönüştür ve Düzenle araçları.

::: tip
Tablette yaygın bir kurulum, şekillendirme ve boyamayı yalnızca kaleme bırakıp parmaklarınızı kamera için ayırmaktır. Böylece avucunuz veya yanlışlıkla değen bir parmak modelinizde asla iz bırakmaz.
:::

### ![](/icons/tool_smooth.webp) Parmak her zaman düzleştirir {#finger-always-smooths}
Açıkken, şekillendirme aracı etkin olduğu sürece hangi fırça seçili olursa olsun parmağınız her zaman düzleştirir. Açmak `Parmak` seçeneğini `Şekillendir` satırından kaldırır; böylece kalem şekillendirir, parmak düzleştirir.

### Yüzey dışı vuruş {#allow-air-stroke}
İmleç ilk olarak ağın dışına düşse bile darbenin başlamasına izin verir. Hangi araçlara uygulanacağını seçin: `Araç` (diğer tüm fırçalar), `Pürüzsüzleştir`, `Maske` ve `Gizle`. Yalnızca şekillendirebilen ama kamerayı hareket ettiremeyen girişlerde çalışır; bu yüzden girişlerinizden biri bu şekilde ayarlanana kadar bu düğmeler devre dışıdır.

### ![](/icons/stroke.webp) Kontur yakalama {#stroke-snap}
Bir darbenin sonunda imleci hareketsiz tutarak darbeyi düz bir çizgiye veya yumuşak bir eğriye dönüştürün. Yakalanan darbeyi başlangıç noktası etrafında döndürmek ve ölçeklemek için sürüklemeye devam edin.

`Basılı tutma süresi`, darbe yakalanmadan veya bir şekil düzenleme moduna geçmeden önce ne kadar süre hareketsiz kalmanız gerektiğini belirler.

### ![](/icons/stylus.webp) Ekstra giriş örnekleri kullanın {#use-extra-input-samples}
Cihazın bildirdiği ek giriş örneklerini kullanır. Darbeleriniz tırtıklı çıkıyorsa veya basınç hatalı davranıyorsa kapatın. Bu seçenek iOS'ta gösterilmez.

### ![](/icons/tool_mask.webp) Maske {#mask}

![](/images/interface_gesture_mask.webp)

`Tek dokunmalı` - Maske düğmesini basılı tutmanıza gerek kalmadan aşağıdaki tek dokunuşluk kısayolları etkinleştirir. Şu hareketleri kullanmanızı sağlar:
* maskeyi tersine çevirmek için arka plana dokunun
* maskeyi bulanıklaştırmak için maskelenmiş bir alana dokunun
* maskeyi keskinleştirmek için maskelenmemiş bir alana dokunun

#### Uzun basılı tut {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)

Maske aracıyla uzun basmak, maske fırçası ile kement (SelMask) arasında geçiş yapar:
* `Uzun basılı tut - Şekillendir` - Uzun basın, sonra sürüklemeye devam edin: darbe diğer modla çizilir ve darbe bitince önceki mod geri gelir.
* `Uzun basılı tut - Değiştir` - İkisi arasında geçiş yapmak için uzun basın ve hareket ettirmeden bırakın.

### ![](/icons/tool_smooth.webp) Pürüzsüzleştir {#smooth}
`Uzun basılı tut - Lasso` - Pürüzsüzleştir aracıyla uzun basmak, seçim darbesi boyunca Seç aracına geçer.

### ![](/icons/tool_hide.webp) Gizle {#hide}
![](/images/interface_gesture_hide.webp)

`Tek dokunmalı`, gizle aracıyla şu kısayolları etkinleştirir:
* Bir yüz grubunu gizlemek için ona dokunun
* Gizli poligonları tersine çevirmek için boş alana dokunun

### ![](/icons/finger3.webp) Üç parmak {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Cihazınız 3 parmak hareketlerini destekliyorsa, bu hareket için kısayollar ayarlayın. 

Seçenek tablosu, dikey ve yatay sürüklemeleri ayrı kısayollar olarak tanımlamanızı ya da kapalı bırakmak için `Hayır` seçmenizi sağlar. Aynı hareket 2 seçenek için seçilirse birinin devre dışı kalacağını ve adının üstünün çizileceğini unutmayın.

* `Işıklandırmayı döndür` - Ortamı, ışıkları ve Matcap'i döndürür.
* `Araç Yarıçapı` - Araç yarıçapını düzenler.
* `Araç yoğunluğu` - Araç yoğunluğunu düzenler. 

### ![](/icons/fingerprint.webp) Geçmiş 2/3 {#history-23}
`Geçmiş kısayolları` - açıkken şu hareketler etkin olur:
* Geri al - 2 parmakla dokunun
* Yinele - 3 parmakla dokunun

`Uzun basılı tut` - açıkken 2/3 parmağı basılı tutmak hızlıca geri alır/yineler.

### ![](/icons/mouse.webp) Fare tekerleği {#mouse-wheel}
`Hız (3d yakınlaştırma)` tekerleğin görünümü ne kadar hızlı yakınlaştıracağını, `Hız (2d arayüz)` ise menüleri ve panelleri ne kadar hızlı kaydıracağını belirler. Her kaydırıcının yanındaki eksi düğmesi yönü tersine çevirir.

### ![](/icons/fingerprint.webp) İzleme dörtgeni {#trackpad}
Mac'te `İki parmak`, izleme dörtgenindeki iki parmağın ne yapacağını seçer. Kıstırma her zaman yakınlaştırır, döndürme hareketi ise her zaman görünümü yuvarlar.
* `Kapalı` - İki parmakla kaydırma, fare tekerleği gibi yakınlaştırır. Parmaklar tek tek okunmaz.
* `Kaydır` - İki parmak görünümü kaydırır, birini kaldırmak yörüngede döndürür. Tablettekiyle aynıdır.
* `Yörünge` - İki parmak görünümü yörüngede döndürür, birini kaldırmak kaydırır.

### Erişilebilirlik {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Yardımcı pencere`, sürükleme, kıstırma, yuvarlama ve kamera işlemlerini kontrol etmek için yüzen bir araç çubuğu açar.

### Kamera {#camera}
`Kamera` menüsüne giden bir kısayol (kamera seçenekleri eskiden buradaydı, ancak kamera menüsüne taşındı).

### Kalem çift dokunma -> Atamalar {#pencil-tap}

Pencil'a çift dokunmanın ne yapacağını ayarladığınız `Atamalar` menüsüne giden bir kısayol. iOS dışında kalem düğmesi için `Kalem düğme → Atamalar` olarak görünür.

### Avuç içi reddi {#palm-rejection}
Telefonlarda ve tabletlerde, ekrana dayanan avuç içi gibi temas alanı `Maksimum boyut eşiği` değerinden büyük olan dokunuşları yok sayar. Her cihazda çalışmayabilir; tuvalle etkileşimde sorun yaşarsanız kapatın.


## ![](/icons/keyboard.webp) Atamalar {#bindings}
Klavye ve düğme kısayolları atamalar menüsünden tanımlanabilir:

![](/images/interface_bindings.webp)
Cihazınızda klavye varsa Nomad'daki işlevlerin neredeyse tamamı klavye kısayollarına, ayrıca kaleminizdeki ek düğmelere, hatta oyun kumandalarına atanabilir.

Bir atama oluşturmak için işlevin yanındaki dikdörtgene tıklayın ve tuşa/düğmeye basın. 

İşlevleri üstteki kategori simgeleriyle ya da adıyla bulmak için arama çubuğuyla bulun. 

Tek tek atamalar, atama adının yanındaki onay kutusuyla devre dışı bırakılabilir. Listeyi yeniden sıralamak için onay kutusuna uzun basıp sürükleyin.

Etkin iki atama aynı kısayolu kullandığında yanlarında, çakışan işlevleri listeleyen bir ![](/icons/help.webp) simgesi belirir.

### ![](/icons/more.webp) Bağlam menüsü {#context-menu}
Her atamanın sonundaki ![](/icons/more.webp) simgesi bir bağlam menüsü açar:

![](/images/interface_bindings_context.webp)

* `Klonlama` - Atamayı klonlar; örneğin bir işleve ikinci bir kısayol vermek için.
* `Sıfırla` - Atamayı sıfırlar
* `Sil` - Atamayı siler. Yalnızca işlevin birden fazla ataması varsa mümkündür.

Bunların altında, bazı atamaların ek seçenekleri vardır:

* `Yapışkan tuşlar` - Araç kısayolları ve hızlı kısayollar (Maske, Pürüzsüzleştir, Gizmo, Gizle, Yüz Grubu, Ekle/Çıkar) için, tuşa basmanın araçları nasıl değiştireceğini seçer. `Otomatik`, [Gelişmiş](#advanced) seçeneklerinde ayarlanan varsayılanı kullanır.
  * `Beklet` - Aracı kullanmak için tuşu basılı tutun, önceki araca dönmek için bırakın.
  * `Değiştir` - Araç değiştirmek için bir kez basın.
  * `Hızlı Bas` - Aracı geçici olarak kullanmak için basılı tutun ya da ona geçmek için kısa basın.
* `Geriye çek` - Hızlı kısayollar için, basılı tutulan tuşu bırakmanın, o araç zaten etkin olsa bile her zaman önceki araca dönüp dönmeyeceğini seçer.
* `Önceki Aracı Değiştir` - Araç kısayolları için, mevcut aracın kısayoluna basmak son kullanılan araca geri döner. `Yapışkan tuşlar` seçeneğinin `Değiştir` veya `Hızlı Bas` olması gerekir.
* `Konum` - Yüzen pencere kısayolları için, pencereyi bulunduğu yerde (`Öncekini tut`) veya imlecin altında (`İmleçte`) açar.
* `Kaydırma (bırakınca)` / `Yakınlaştırma (bırakınca)` - Kamera yakınlaştırma ve kaydırma atamaları için, tuşu bıraktığınızda diğerine geçer.
* Sürükleme yönü - `Işıklandırmayı döndür`, `Araç Yarıçapı` ve `Araç yoğunluğu` için yatay veya dikey sürüklemeyi seçer.
* `Senkronize` - Nesne ekleyen, klonlayan veya örnekleyen işlevler için, sonucun senkronize edilip edilmeyeceğini seçer. Varsayılan olarak Sahne menüsünde ayarlanan senkronizasyon değerini kullanır.
* `Arka Planda` - Pürüzsüzleştir ve Maske hızlı kısayolları için, tuşu basılı tutarken arka planda sürükleyerek bir kement çizin: Pürüzsüzleştir için seçim kementi, Maske için maske kementi.
* `Kamerayı zorla` - Kamera atamaları için, aynı kısayol başka bir atama tarafından da kullanılıyor olsa bile (genellikle bir araç kısayolu veya Ekle/Çıkar) kamerayı hareket ettirir.
* `Doğrusal yuvarlanma` - Yuvarlama ataması için, pivot etrafında hareket etmek yerine yatay, dikey veya çapraz bir sürüklemeyle yuvarlar.

::: tip
`Hızlı Bas` ile tek tuş iki işi birden görür: hızlıca düzleştirmek veya maskelemek için basılı tutun, bıraktığınızda fırçanıza geri dönersiniz; ya da o araçta kalmak için kısa basın.
:::

### ![](/icons/cog.webp) Gelişmiş {#advanced}
Atamalar menüsünün altında gelişmiş seçenekler için bir dişli menüsü bulunur:

![](/images/interface_bindings_advanced.webp)

* `Hızlı kısayollar` - Maske, Pürüzsüzleştir, Gizmo, Gizle, Yüz Grubu ve Ekle/Çıkar kısayolları için varsayılan `Yapışkan tuşlar` ve `Geriye çek` ayarları.
* `Araç kısayolları` - Araç kısayolları için varsayılan `Yapışkan tuşlar` ve `Önceki Aracı Değiştir` ayarları. `Önceki Aracı Değiştir` ile aynı kısayol tuşuyla iki araç arasında gidip gelebilirsiniz.
* `Kısayol penceresi` - Yüzen pencereleri gösteren kısayolların `Yapışkan tuşlar` modu.
* `Zoom Y’yi Ters Çevir` - Bir atamayla yakınlaştırırken dikey sürükleme yönünü tersine çevirir.
* `Doğrusal yuvarlanma` - Pivot etrafında hareket etmek yerine görünümü yatay, dikey veya çapraz bir sürüklemeyle yuvarlar.
* `SpaceMouse` - 3Dconnexion SpaceMouse desteğini etkinleştirir. Bazı sistemlerde ek seçenekler belirir: neyi hareket ettireceği (`Nesne`, `Kamera`, `Birinci Kişi`, `Drone`), hareket etmeye başladığında pivotu imlecin altındaki yüzeye taşımak için `Ekseni otomatik güncelle` ve `Yatay Kayma`, `Yakınlaştırma` ve `Döndürme` hızları.
* `Ölü bölgeler (drift)` - `Gamepad`, `Joystick` ve `Düğme` kumandaları için. Kumandaya dokunulmadığı hâlde kamera hareket ediyorsa bu değerleri artırın.
* `Araç Yarıçapı` - Yarıçap atamasıyla sürüklemenin fırçayı nasıl yeniden boyutlandıracağı (`Daire`, `Ortalanmış` veya `dx`), ardından yarıçap atamalarının her basışta ne kadar ekleyeceği (piksel olarak) veya çarpacağı.
* `Araç yoğunluğu` - Yoğunluk atamalarının her basışta ne kadar ekleyeceği veya çarpacağı.
* `Kamera - Hız` - Görünümü kaydıran ve döndüren atamaların `Yatay Kayma` ve `Döndürme` hızı.
* `Atamaları sıfırla` - tüm atamaları varsayılanlarına döndürür.
* `Sıralamasını sıfırla` - atamalar listesinin varsayılan sırasını geri getirir.


## iOS ⌘ Klavye kısayollarını görüntüleme {#ios-keyboard-shortcuts-display}

Klavyeli iOS cihazlarda kısayol listesini görmek için ⌘ (cmd) tuşunu basılı tutun.

Android'de klavye desteği biraz deneyseldir.

![](/images/shortcuts.webp)


## ![](/icons/bug.webp) Ayıkla {#debug}
Bu menüde bazı deneysel ve hata ayıklama seçenekleri bulunur. Bu seçeneklerin çoğu varsayılan değerlerinde bırakılmalı ve yalnızca Nomad desteğiyle iletişime geçtikten sonra değiştirilmelidir. Üstteki simgeler her bölüme atlamanızı sağlar.

![](/images/interface_debug.webp)
### ![](/icons/uv.webp) UV {#uv}
* `UV'leri normalleştir` - Nomad, seçili ağın UV'lerini [0-1] karesi içine normalleştirir.

### ![](/icons/sun.webp) Gölgelendirme {#render}
* `Kırılma derinliğini yaz (arka)` - Kırılma ağlarının arka yüzü derinlik tamponuna yazılır.
* `Açı ağırlıklı yumuşak normaller` - Yumuşak gölgelendirmenin çalışma biçiminde, bazı durumlarda kırışıkları önleyebilen bir ayar.

### ![](/icons/speed.webp) Hedef FPS {#target-fps}
Kapalıyken Nomad saniyedeki kare sayısını ekranınızın yenileme hızıyla senkronize eder.

Açıkken Nomad'ın saniyede kaç kare render edeceğini ayarlayabilirsiniz.

### ![](/icons/window.webp) Arayüz {#debug-interface}
* `Araç kutusu: tümünü göster` - Nomad, mevcut seçimle ilgisi olmayan araçları gizler; örneğin tamamlanmamış primitiflerde tüm şekillendirme fırçaları gizlenir. Bu seçenek devre dışı araçları gizlemek yerine soluk gösterir.

Eskiden burada olan diğer arayüz seçenekleri artık [Arayüz](#interface) sekmesinde.

### ![](/icons/turntable.webp) Döner platform {#gif-turntable}
Nomad animasyonlu bir gif döner platform videosu dışa aktarabilir. Gif biçiminin sınırlamaları nedeniyle kalitenin düşük olduğunu unutmayın. Ekran kaydı genellikle daha iyi bir yöntemdir.

* `Süre` - döner platform animasyonunun saniye cinsinden uzunluğu
* `Maks. kare örnekleme` - Nomad'ın yüksek kaliteli render efektlerinin çoğu, birkaç kareyi birleştirmekten gelir. Bu kaydırıcı kaç karenin birleştirileceğini belirler, onay kutusu ise bunu açıp kapatır.
* `Dönüş merkezi` - kameranın etrafında döneceği nokta: `Mevcut olanı koru` mevcut pivotu korur, `(0, 0, 0)` dünyanın merkezini, `Sahne` sahnenin merkezini kullanır.
* `Şeffaf arkaplan` - Gif'ler için şeffaflık seçeneğini kullanır. Gif'lerin yalnızca 1 bitlik şeffaflığı desteklediğini, bu yüzden kenarların çok tırtıklı olabileceğini unutmayın.
* `Dışa Aktar (GIF)` - gif dışa aktarma işlemini başlatır.

### ![](/icons/postprocess.webp) Süreç sonrası işlemler {#post-process}
* `Filtreleme` - Hata ayıklama seçeneği
* `Biçim` - Hata ayıklama seçeneği
* `Tamponları yeniden kullan` - Hata ayıklama seçeneği

### ![](/icons/ram.webp) Performans {#performance}
* `Çoklu iş parçacığı: genel` - Hata ayıklama seçeneği
* `Çoklu iş parçacığı: heykel` - Hata ayıklama seçeneği
* `Tekrarları örneklerle çiz` - Bir tekrarlayıcının tüm kopyalarını tek bir çizim çağrısında çizer. Hata ayıklama seçeneği.

### ![](/icons/star.webp) Özellik {#feature}
* `nom: çoklu çözünürlüğü sıkıştır` - Çoklu çözünürlük kullanan projelerin ve Nomad dışa aktarımlarının boyutunu küçültür. Bu dosyalar Nomad'ın eski sürümleriyle açılamaz. Bu seçenek ileride kaldırılıp varsayılan olarak etkinleştirilebilir.
* `Dörtgen köşegenini çevir (dokununca)` -  Hata ayıklama seçeneği

### ![](/icons/bug.webp) Ayıkla {#dev}
* `Kayıtları` - Bir kayıt penceresi açar
* `Olayları kaydet` - İşaretçi olaylarınızı (parmak, kalem, fare) kayıt penceresine yazar; giriş sorunlarını incelemek için.
* `FPS` - görünüm istatistiklerine saniyedeki kare sayacı ekler.
* `Uygulama değerlendirme penceresi` - Hata ayıklama seçeneği, iOS ve Android'de.

### ![](/icons/image.webp) Özel simgeler {#custom-icons}
Nomad'ın simgelerini kendi png dosyalarınızla değiştirin.
* `Simgeleri içe aktar` - Png dosyalarını `tmp_session/icons` klasörüne aktarır. Her biri aynı adı taşıyan temel simgenin yerini alır. Nomad yeniden başladığında kaldırılırlar.
* `Araç simgelerini dışa aktar` - Temel `tool_<tool>.png` simgelerini, var olanların üzerine yazmadan `tmp_session/icons` klasörüne kopyalar. Onları orada düzenleyip `Simgeleri yeniden yükle` ile uygulayabilirsiniz.
* `Simgeleri yeniden yükle` - `tmp_session/icons` içindeki simgeleri uygular.

### Dörtgen Yeniden Örgüleme {#quad-remesh}
Dörtgen yeniden örgüleme seçenekleri artık bu menüde değil: Topoloji menüsündeki [Dörtgen Yeniden Örgüleme](topology.md#quad-remesh-instant) bölümüne ve [Quad Remesher](tools.md#quad-remesher) aracına bakın.

### Mağaza küçük resimleri {#make-store-thumbnails}
iOS App Store'a uygun boyutlarda ekran görüntüleri render eder.
