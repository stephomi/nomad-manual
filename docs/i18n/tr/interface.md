# ![](/icons/interface.webp) Arayüz Menüsü {#interface-menu}

Bu menü, Nomad'ın arayüzünü özelleştirmek için birçok seçeneği kontrol eder. 

![](/images/interface_overview2.webp)

Nomad oldukça derin bir seviyeye kadar özelleştirilebilir, bu menü 4 bölüme ayrılmıştır; Arayüz, Jest, Bağlantılar, Hata Ayıklama.

![](/images/interface_menu.webp)


::: tip
Bu sayfa arayüz menüsü içindir, arayüzün kendisi için değil! Genel arayüz [Başlarken](gettingstarted.md) bölümünde açıklanmıştır.
:::

## Arayüz {#interface}

Arayüz bölümü, kısayollar eklemenize, yüzen araç çubukları oluşturmanıza ve Nomad'ın kullanıcı arayüzünün renk, boyut ve görünümünü kontrol etmenize olanak tanır.

![](/images/interface_overview3.webp)

### Kısayollar ekle (alt)... {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Alt araç çubuğunda varsayılan olarak şu kısayollar etkindir:
* `Geri al` - önceki işlemi geri al
* `Yinele` - daha önce geri alınan işlemi geri yükle
* `Solo` - Sadece seçili nesne görünür kalacak şekilde diğer tüm nesneleri geçici olarak gizle. Tüm nesneleri geri getirmek için tekrar basın.
* `X-ray` - Sadece seçili nesne opak kalacak şekilde diğer tüm nesneleri geçici olarak yarı saydam yap. Varsayılan malzemeleri geri yüklemek için tekrar basın.
* `Voksel yeniden örgü` - Geçerli nesneyi son kullanılan voksel çözünürlüğüyle yeniden örgüle. Uzun basma veya yukarı kaydırma, çözünürlük kaydırıcısını ve keskin kenar geçişini açar.
* `Izgara` - Görünüm ızgarasını aç/kapat. Uzun basma veya yukarı kaydırma, ızgaranın rengini ve opaklığını değiştirmenizi sağlar.
* `Tel kafes` - Tel kafes bindirmesini aç/kapat. Uzun basma veya yukarı kaydırma, tel kafesin rengini ve opaklığını değiştirmenizi sağlar.
* `Denetçi` - Nomad arka planına bindirilmiş şekilde uv'ler, pişirilmiş dokular ve diğer özellikler gibi ağınızın özelliklerini görüntülemenizi sağlar.
* `Yüz Grubu` - yüz grubu bindirmesini aç/kapat, daha fazla bilgi için [Araçlar->FaceGroup](tools.md#facegroup) 

Bu menüden erişilebilen başka yaygın kısayollar da vardır, çok daha fazlası bağlantılar düğmesinin içinde bulunabilir.

#### ![](/icons/more.webp) Bağlantılar {#bindings-list}

Nomad'ın neredeyse her işlevi, bağlantılar düğmesi aracılığıyla kısayol araç çubuğuna eklenebilir. Düğmeye tıklandığında bir bağlantılar menüsü görüntülenir:

![](/images/interface_bindings_search.webp)

Üstteki simgelerle kategoriye göre arama yapabilir veya işlevleri ada göre bulmak için arama alanını kullanabilirsiniz. Bir işlevi araç çubuğuna eklemek için üzerine tıklayın. Kaldırmak için tekrar tıklayın.

#### ![](/icons/list.webp) Sıra {#order}

Bu, kısayolların bir listesini görüntüler. Kısayolları yeniden sıralamak için uzun basıp sürükleyin.

#### ![](/icons/reset.webp) Sıfırla {#reset}

Sıfırla, alt araç çubuğunu varsayılan ayarlarına geri döndürür.

### Kısayollar ekle (pencere)... + {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

+ işaretine tıklamak yüzen bir araç çubuğu ekler. Bağlantılar düğmesine tıklayıp ona bazı kısayollar ekleyene kadar görünür olmayacaktır, ardından görünür hale getirebilirsiniz. 

Birçok araç çubuğu oluşturabilirsiniz, her araç çubuğunun bu menüde aşağıdaki seçenekleri vardır:

* ![](/icons/checked.webp) `Görünür` - Araç çubuğunun görünürlüğünü aç/kapat
* ![](/icons/more.webp)`Bağlantılar` - Araç çubuğuna eklenecek veya kaldırılacak işlevleri seçmek için bağlantı penceresini görüntüle.
* ![](/icons/list.webp)`Sıra` - Araç çubuğunu yeniden sıralamak için bir menü görüntüle.
* ![](/icons/reset.webp) `Sıfırla` - Araç çubuğunu varsayılan durumuna sıfırla.
* ![](/icons/resize_bottom_right.webp) `Yeniden boyutlandırma köşesi` - Araç çubuğunun sağ alt köşesinde bir yeniden boyutlandırma tutamacını aç/kapat.
* ![](/icons/sort_down.webp) `Daraltılabilir` - Sağ üst köşede bir daraltma tutamacını aç/kapat.
* ![](/icons/trash.webp) `Sil` - Araç çubuğunu sil.

### Araç kutusu {#toolbox}

Nomad arayüzünün sağındaki araç menüsü için seçenekler.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Arayüz Yeniden Boyutlandırma Köşesi {#ui-resize-corner}

Araç çubuğunun alt köşesinde bir yeniden boyutlandırma tutamacını aç/kapat.

#### Gizli {#hidden}
Normalde üst çubuktaki araç kutusu simgesi, uzun tek sütun ile çok sütunlu araç listesi arasında geçiş yapar. Bu seçenek, çok sütunlu liste ile tamamen gizli olma arasında geçiş yapar.

#### Renkli {#colored}
Simgeleri kategoriye göre renklendir, örn. tüm maske araçları kahverengi, bölme araçları kırmızı, düzleştirme araçları yeşil vb.

#### Satırlar: Otomatik (>1) {#rows-auto-1}

#### Sıralamayı sıfırla {#reset-order}
Araç kutusundaki varsayılan araçları varsayılan sıraya sıfırla. Özel simgeler, listenin sonunda araç kutusunda kalacaktır.


### Ön ayarlar {#presets}

![](/images/interface_presets.webp)

Arayüz için bir renk ön ayarları koleksiyonu.

#### Yüksek kontrastlı düğme {#high-contrast-button}
Etkinleştirildiğinde, düğmeler etkin olduklarında daha görünür hale getiren alternatif bir stil. Otomatik olarak ayarlanırsa, Nomad etkin/pasif durumlar arasındaki UI renk kontrastı düşük olduğunda bu modu kullanır.

#### Renk aracı/Renk tabanı {#color-widgetcolor-base}
Arayüzde kullanılan birincil renkler.

#### Şeffaf panel, Renk paneli, Bulanıklık gücü {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Etkinleştirildiğinde, Nomad'daki menü ve panellerin nasıl görüneceğini kontrol etmek için ek seçenekler görünür. Renkleri, şeffaflıkları ve bulanıklık miktarları ayarlanabilir.

::: tip
Küçük cihazlarda, sahnenin menüler tarafından gizlenmemesi için renk panelini neredeyse beyaz, şeffaf ve düşük bulanıklık gücünde yapmak faydalı olabilir.
:::

----

### Üst çubuğu yansıt {#mirror-top-bar}
Üst çubuktaki menülerin sırasını tersine çevir.

### Yan çubukları yansıt {#mirror-side-bars}
Yan çubukları değiştirerek araç kutusunu sola, araç seçeneklerini sağa al.

### Alt çubuğu yansıt {#mirror-bottom-bar}
Alt çubuğu sağ alt köşeye taşı ve düğme sırasını tersine çevir

### Malzeme rengi önizlemesi {#material-color-preview}
Bir malzeme için renk seçtiğinizde, bu malzemenin bir önizlemesi seçili nesne üzerinde görüntülenir.

----
### Üzerine gelince yardım açılır penceresi {#help-popup-on-hover}

Üzerine gelmeyi destekleyen cihazlarda, Nomad'daki ![](/icons/help.webp) simgesiyle temsil edilen bağlamsal yardımın üzerine gelindiğinde mi yoksa yalnızca tıklandığında mı görüneceğini ayarlayın.

----

### Genel ölçek {#overall-scale}
Tüm UI öğeleri için bir boyut çarpanı.
### Panel genişliği {#panel-width}
Menü ve panellerin genişliği.
### Yazı tipi ölçeği {#font-scale}
Yazı tiplerini ölçeklendir.
### Dikey aralık {#vertical-spacing}
Menü ve panellerdeki öğeler arasındaki boşluk.
### Dikey aralık (sol) {#vertical-spacing-left}
Sol araç çubuğundaki öğeler arasındaki boşluk.

----

### Kenar uzaklığı {#edge-offset}
Bu değerleri yalnızca ekran kenarlarındaki düğmelerle etkileşimde sorun yaşıyorsanız değiştirmelisiniz. Bu kaydırıcılar devre dışıysa, Nomad cihazın kendisinin döndürdüğü güvenli alan değerlerini kullanır.

::: tip
Nomad'ı yeni bir cihaza taşırken (örn. bir iPhone 12'yi iPhone 15 ile değiştirirken), kenar seçeneklerini varsayılanlara sıfırladığınızdan emin olun!
:::

### Stili sıfırla {#reset-style}
Tüm UI öğelerini varsayılan değerlerine sıfırla.


## Hareket {#gesture}
Jest menüsü, kalem ve parmak dokunuşlarının Nomad'ı nasıl kontrol ettiğini belirler.

![](/images/interface_gesture.webp)

### Hareket seçenekleri {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad, işlemleri giriş cihazına göre sınırlayabilir. Örneğin bir parmak sürüklemesi yalnızca kamerayı hareket ettirebilirken, kalem sürüklemesi yalnızca yontma yapabilir. Fare veya trackpad'iniz varsa, bunlar da belirli işlemleri kontrol edecek şekilde atanabilir.

Nomad şu modların parmak, kalem veya fare jestlerinin herhangi bir kombinasyonuyla kontrol edilmesine izin verir:

* Kamera
* Yontma
* Gizmo
* Malzeme seçme (uzun basma ile)
* Nesne seçme


`Parmak her zaman yumuşatır` - Yumuşatma yalnızca parmak sürüklemesiyle çalışacak şekilde ayarlanabilir.

### ![](/icons/tool_mask.webp) Maske {#mask}

![](/images/interface_gesture_mask.webp)

`Tek dokunuş kısayolları` - Maske düğmesini basılı tutmak zorunda kalmadan aşağıdaki tek dokunuş kısayollarını etkinleştir. Şu jestlere izin verir:
* Arka plana dokunarak maskeyi ters çevir
* Maskeli bir alana dokunarak maskeyi bulanıklaştır
* Maskesiz bir alana dokunarak maskeyi keskinleştir

### Maskeyi Aç/Kapat <-> SelMask {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)
* `Darbe` - Uzun basma, Maske ve SelMask arasında geçiş yapar ve yeni bir darbe başlatır. Darbe sonunda, önceki araç yeniden seçilir. 
* `Araç` - Hareket ettirmeden uzun bas ve bırak, Maske ve SelMask arasında geçiş yap.

### ![](/icons/tool_hide.webp) Gizle {#hide}
![](/images/interface_gesture_hide.webp)

`Tek dokunuş kısayolları`, gizle aracıyla aşağıdaki kısayolları etkinleştirir:
* Bir yüz grubuna dokunarak onu gizle
* Boş bir alana dokunarak gizli çokgenleri ters çevir

### ![](/icons/finger3.webp) Üç parmak {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Cihazınız 3 parmak jestlerini destekliyorsa, bu jest için kısayolları yapılandırın. 

Seçenek matrisi, dikey ve yatay sürüklemeleri ayrı kısayollar olarak tanımlamanıza olanak tanır. Aynı jest 2 seçenek için seçilirse, bunlardan biri devre dışı bırakılır.

* `Aydınlatmayı döndür` - Ortamı, ışıkları ve Matcap'i döndür.
* `Araç yarıçapı` - Araç yarıçapını düzenle.
* `Araç yoğunluğu` - Araç yoğunluğunu düzenle. 

### ![](/icons/fingerprint.webp) Geçmiş 2/3 {#history-23}
`Geçmiş kısayolları` - etkinleştirildiğinde, aşağıdaki jestler aktiftir:
* Geri al - 2 parmakla dokun
* Yinele - 3 parmakla dokun

`Uzun basma` - etkinleştirildiğinde, 2/3 parmağı basılı tutmak hızlıca geri al/yinele işlemi yapar.

### Erişilebilirlik {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Yardımcı pencere`, sürükleme, sıkıştırma, döndürme ve kamera işlemlerini kontrol etmek için yüzen bir araç çubuğu açar.

### Kamera {#camera}
`Kamera` menüsüne gitmek için bir kısayol (kamera seçenekleri eskiden burada bulunuyordu, ancak kamera menüsüne taşındı).

### Kalem çift dokunuş -> Bağlantılar {#pencil-tap}

`Bağlantılar` menüsüne gitmek için bir kısayol (Pencil dokunma ve çift dokunma seçenekleri eskiden burada bulunuyordu, ancak bağlantılar menüsüne taşındı).


## Bağlantılar {#bindings}
Klavye ve düğme kısayolları bağlantılar menüsünden tanımlanabilir:

![](/images/interface_bindings.webp)
Nomad'daki neredeyse tüm işlevler, cihazınızda klavye varsa klavye kısayollarına, kaleminizdeki ek düğmelere veya hatta oyun kumandalarına bağlanabilir.

Bir bağlantı oluşturmak için, işlevin yanındaki dikdörtgene tıklayın ve tuşa/düğmeye basın. 

İşlevleri üstteki kategori simgeleriyle veya adlarına göre bulmak için arama çubuğuyla bulun. 

Tek tek bağlantılar, bağlantı adının yanındaki onay kutusuyla devre dışı bırakılabilir.

### ![](/icons/more.webp) Bağlam menüsü {#context-menu}
Her bağlantının yanındaki ![](/icons/more.webp) simgesi bir bağlam menüsü açar:

![](/images/interface_bindings_context.webp)

* `Klonla` - Bağlantıyı klonla
* `Sıfırla` - Bağlantıyı sıfırla
* `Sil` - Bağlantıyı sil
* `Tuş dokunuşunda kısayolu değiştir` - Dokunma ile uzun basmanın farklı şekilde ele alınıp alınmayacağını yapılandır. Etkinleştirildiğinde, dokunma aracı etkinleştirir. Uzun basma, araç yalnızca tuş basılıyken etkin olur, bırakıldığında önceki araca geri döner. Diğer 3B uygulamalarda bazen 'yapışkan tuşlar' olarak adlandırılır.

### Gelişmiş {#advanced}
Bağlantılar menüsünün altında, gelişmiş seçenekler için bir dişli menüsü bulunur:

![](/images/interface_bindings_advanced.webp)

* `Tuş dokunuşunda kısayolu değiştir` - Maske, yumuşatma, gizmo, gizle, çıkarma için standart kısayollara dokunmak o moda geçiş yapar, ancak tuşu basılı tutmak o moda geçici olarak geçer, tuş bırakıldığında mod önceki moda döner. Diğer 3B uygulamalarda bazen 'yapışkan tuşlar' olarak adlandırılır.
* `Araç kısayollarını değiştir` - Araç kısayollarından birini kullanırken, aynı kısayola iki kez basılırsa, önceki araca geçiş yapar. Bu şekilde aynı kısayolla iki araç arasında sürekli geçiş yapabilirsiniz.
* `Y'yi ters çevir (Yakınlaştırma)` - Yakınlaştırmayı ters çevirir
* `Bağlantıları sıfırla` - tüm bağlantıları varsayılanlarına sıfırlar.


## iOS ⌘ Klavye kısayolları gösterimi {#ios-keyboard-shortcuts-display}

Klavyesi olan iOS cihazlarında, kısayol listesini görüntülemek için ⌘ (cmd) tuşunu basılı tutun.

Android klavye desteği biraz deneyseldir.

![](/images/shortcuts.webp)


## Hata ayıklama {#debug}
Bazı deneysel ve hata ayıklama seçenekleri bu menüde saklanır. Bu seçeneklerin çoğu varsayılanlarında bırakılmalı ve yalnızca Nomad desteğiyle iletişime geçtikten sonra değiştirilmelidir.

![](/images/interface_debug.webp)
### UV {#uv}
* `UV'leri normalize et` - Nomad, UV'leri [0-1] döşemesi içine normalize eder.

### Quad Remesh {#quad-remesh}
* `Instant Mesh` - Instant remesh algoritmasını etkinleştir
* `Quadriflow` - Alternatif bir dörtlü yeniden örgü yöntemi.

### Render {#render}
* `Yükseklik haritası` - Görünüm alanını sahnenin derinliğini renderlayacak şekilde değiştir. Bu, fırçalar için alfa haritaları oluşturmak için kullanılabilir.
* `Kırılma derinliği yaz (arka)` - Kırılma ağlarının arka yüzü derinlik arabelleğine yazılır.
* `Y'yi ters çevir (normal harita)` - Normal haritaları pişirirken y kanalını ters çevir, bazı oyun ve render motorları için gereklidir.
* `Açı ağırlıklı yumuşak normaller` - Bazı durumlarda kırışıklıkları önleyebilen, yumuşak gölgelemenin çalışma biçimine yönelik bir ayarlama.

### Hedef FPS {#target-fps}
Devre dışı bırakıldığında, Nomad saniyedeki kare sayısını ekranınızın yenileme hızıyla senkronize eder.

Etkinleştirildiğinde, Nomad'ın renderlayacağı saniyedeki kare sayısını ayarlayabilirsiniz.

### Arayüz {#debug-interface}
* `Üst: yerleşim` 
  * Daralt: Küçük cihazlarda üst çubuk daha fazla alt menüye daraltılır. 
  * Kaydır: Nomad'a büyük ekranlarda alışkınsanız ve normal yerleşimi tercih ediyorsanız, bunu etkinleştirmek standart geniş üst çubuğu kullanır ve bu çubuk kaydırılabilir.
  * Çok satırlı: Tüm üst menüyü birkaç satır halinde görüntüle.
* `Alt: sürüklenebilir açılır pencere` - Alt araç çubuğunda, bir iletişim kutusu açan birkaç düğme vardır. Bu seçenek etkinleştirilirse, bu iletişim kutuları ekranda başka bir yere taşınabilir.  
* `Araç kutusu: tümünü göster` - Nomad, geçerli seçim için geçerli olmayan araçları gizler, örn. doğrulanmamış primitiflerde tüm yontma fırçaları gizlenir. Bu seçenek, araçları gizlemek yerine devre dışı olanları soluk gösterir.
* `Araç kutusu: renkli` - Araç kutusu simgelerini türlerine göre renklendir.
* `Panel: Gölge düşür` - Menü ve panellerin etrafına gölge çizer. Bazı eski cihazlarda bu performansı etkileyebilir.
* `Panel: Karıştırma` - Hata ayıklama seçeneği
* `İşaretçi: üzerine gelme noktası` - Kalemle üzerine gelmeyi destekleyen cihazlarda, kalem menü ve panellerin üzerinde gezinirken bir nokta görüntüle.

### Gif turntable {#gif-turntable}
Nomad, animasyonlu gif döner tabla dışa aktarabilir. Gif formatının sınırlamaları nedeniyle kalitenin düşük olduğunu unutmayın. Ekran kaydı genellikle daha iyi bir yöntemdir.

* `Süre` - döner tablanın saniye cinsinden ne kadar süreceği
* `Dönme merkezi` - kamera ekseninin nerede olduğu, dolayısıyla kameranın sahnenin hangi kısmı etrafında döneceği
* `Şeffaf arka plan` - Gif'ler için şeffaf seçeneğini kullan. Gif'lerin yalnızca 1 bit şeffaflığı desteklediğini, bu nedenle kenarların kötü piksellenebileceğini unutmayın.
* `Maksimum kare örnekleme` - Nomad'ın yüksek kaliteli render efektlerinin çoğu, birkaç karenin birleştirilmesinden gelir. Bu kaydırıcı, kaç karenin birleştirileceğini ayarlar.
* `Dışa aktar (GIF)` - gif dışa aktarma işlemini başlat.

### Son işleme {#post-process}
* `Filtreleme` - Hata ayıklama seçeneği
* `Biçim` - Hata ayıklama seçeneği
* `Arabellek yeniden kullanımı` - Hata ayıklama seçeneği

### Performans {#performance}
* `Çok çekirdekli genel` - Hata ayıklama seçeneği
* `Çok çekirdekli yontma` - Hata ayıklama seçeneği
* `Kısmi Çizim` - Deneysel özellik! Yüksek poligonlu bir ağın nispeten küçük bir bölümünü yontuyorsanız kullanın. Yontmayı daha akıcı hale getirmelidir, ancak tel kafesi etkinleştirmemelisiniz! Ayrıca fırça darbeleri sırasında görsel yapaylıklar ekleyebilir.

### Özellik {#feature}
* `Dörtlü bölmeyi ters çevir (dokunmada)` -  Hata ayıklama seçeneği
* `Birleştir: birleştirme yarıçapı` - Ağlar birleştirildiğinde, yeterince yakınlarsa köşeler otomatik olarak birleştirilir. Bu yarıçapı bu kaydırıcıyla ayarlayabilirsiniz.

### Hata ayıklama {#dev}
* `Günlükler` - Bir günlük görünümü aç
* `Uygulama inceleme açılır penceresi` - Hata ayıklama seçeneği
* `FPS` - görünüm alanı istatistiklerine saniyedeki kare sayacı ekle.