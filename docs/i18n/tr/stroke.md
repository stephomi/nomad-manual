# ![](/icons/brush.webp) Darbe {#stroke}

---
![](/images/stroke_overview.webp) 

## Genel bakış {#overview}

Çoğu aracın fırçasında darbe davranışını özelleştirebilirsiniz.
Ayarlar 2d boyama uygulamalarındakilere benzer, ancak bazı seçenekler heykel yapmaya ve 3d'ye özgüdür.

Seçenekler 5 alt menüye ayrılmıştır:

| Ad     | Simge                         | Açıklama                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Darbe   | ![](/icons/brush.webp)      | Darbenin modele nasıl uygulandığını kontrol eder                   |
| Alfa    | ![](/icons/alpha.webp)      | Fırça damgası için gri tonlamalı bir dokunun nasıl kullanıldığı               |
| Düşüş  | ![](/icons/falloff.webp)    | Fırça gücünün merkezden kenara doğru nasıl değiştiğini kontrol eder |
| Filtre   | ![](/icons/filter.webp)     | Fırçanın modelin geometrisinden nasıl etkilendiği                    |
| Basım Şiddeti | ![](/icons/pressure.webp)   | Kalem basıncına verilen tepkiyi kontrol eder                                   |

::: tip
Darbe seçeneklerinin hepsi her araç için geçerli değildir. Geçerli aracın kullanmadığı darbe seçenekleri devre dışı bırakılır ya da gizlenir. 
:::


## ![](/icons/brush.webp) Darbe {#stroke-1}

### ![](/icons/radius.webp) Yarıçap {#radius}

![](/images/stroke_radius.webp)

Yarıçap seçenekleri global ayarlardır: her araç için geçerlidir.

#### Uzay {#size}

* `Ekran` - yarıçap ekran birimleriyle belirlenir. Yarıçapı 100 piksel genişliğinde yaparsanız, yakınlaştırsanız da uzaklaştırsanız da 100 piksel genişliğinde kalır.
* `Dünya (3D)` - yarıçap 3d birimleriyle belirlenir. Örneğin bir küre oluşturup yarıçapı kürenin boyutuna eşitlerseniz, yakınlaştırıp uzaklaştırdıkça yarıçap kürenin boyutunda kalır.

#### ![](/icons/link.webp) Kısayolu eşitle {#sync-shortcut}

Etkinleştirildiğinde, kısayol fırçalarına (`Pürüzsüzleştir`, `Maske` veya `Gizle`) geçtiğinizde yarıçap ve siluet ayarları eşit tutulur. Böylece hızlı bir pürüzsüzleştirme ya da maskeleme, kullandığınız araçla aynı fırça boyutunu kullanır.

#### ![](/icons/link.webp) Yarıçapı paylaş {#share-radius}

Etkinleştirildiğinde tüm araçlar aynı yarıçapı kullanır; varsayılan olarak her aracın kendi yarıçapı vardır.


### Darbe türü {#stroke-type}

![](/images/stroke_strokemode.webp)

Darbeler birkaç kipte çalışabilir:

### ![](/icons/stroke_dot.webp) Nokta {#dot}
Normal bir boya darbesi gibi sürükleyin. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Yuvarla {#roll}
Fırça alfası darbenin yönünü izleyecek şekilde döndürülür; kumaş dikişleri yapmak için kullanışlıdır. 
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Yakala • dinamik yarıçap {#lock-radius}
Sabit **_yükseklikte_** bir fırça darbesi damgalar. Sürükleme, ölçeği ve dönüşü belirler.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Yakala • dinamik yoğunluk {#lock-intensity}
Sabit **_yarıçapta_** bir fırça darbesi damgalar. Sürükleme, yüksekliği ve dönüşü belirler.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
`Yakala • dinamik yarıçap` ve `Yakala • dinamik yoğunluk` kipleri [Basım Şiddeti](#pressure) ayarlarını yok sayar, çünkü boyutu ve gücü zaten sürükleme belirler.
:::

![](/images/stroke_strokemodemove.webp)

`Taşı` ve `Sürükle` araçlarının kendilerine ait 3 seçeneği vardır:

### ![](/icons/snake.webp) Sürükle {#drag}

Darbe boyunca fırça yarıçapının içinde kalanı sürekli günceller. Hızlı bir darbe yüzeyi geride bırakır, yavaş bir darbe ise malzemeyi tutarak daha uzun şekiller oluşturur. `Sürükle` aracının varsayılan kipidir. `Dinamik topoloji` ile birlikte yılan gibi uzantılar yapmak için kullanılabilir. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Yakala {#grab}
Fırça başladığında yarıçapın içinde kalanı seçer ve bu seçimi korur. Daha hassas taşıma işlemleri için kullanışlıdır: taşımanın mesafesini dikkatle ayarlayabilir, başta seçtiğinizden fazlasını yanlışlıkla taşımazsınız. `Taşı` aracının varsayılan kipidir.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Yakala • dinamik yarıçap (sürükleme) {#lock-radius-drag}
Kullanıcının yarıçapı yok sayılır; yarıçap, darbenin başlangıç noktasından ne kadar uzağa sürüklendiğine göre dinamik olarak belirlenir. Kısa mesafe = küçük yarıçap, uzun mesafe = büyük yarıçap. Düşüşün şeklini kontrol etmek için yoğunluk kaydırıcısını kullanın. Organik, lastiğimsi şekilleri kabaca oluşturmak için kullanışlıdır.
![](/videos/stroke_lockradius_drag.mp4) 

Bazı başka araçlar da burada kendi darbe türlerini listeler; örneğin pürüzsüzleştirme araçları için `Rahatlat`, `Pürüzsüzleştir` ve `Leke`, seçime dayalı araçlar için `Lasso` ve `Eğri` gibi şekiller. Bunlar her [aracın](tools.md) kendi bölümünde anlatılır.


### Aralık yoğunluğunu ayarla {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Düşük aralıklı (%50'nin altında) darbeler hızla birikerek daha yüksek aralık değerlerine göre daha yoğun darbeler oluşturabilir. Bu seçenek bunu telafi eder; böylece darbeler, aralık ne olursa olsun aşağı yukarı aynı yoğunlukta olur.

### Darbe aralığı {#stroke-spacing}
Sürükleme sırasında her fırça damgasının birbirinden ne kadar uzağa uygulanacağı. %100'ün altındaki değerler üst üste biner ve kesintisiz bir darbe görünümü verir. %100'ün üzerindeki değerler boşluklar bırakmaya başlar; dikiş ya da fermuar gibi ayrıntıları şekillendirmek için kullanışlıdır.

### Yavaş dengeleyici ip {#lazy-rope-stabilizer}
Darbeler, işaretçinin konumunu belirli bir mesafeden geriden izler. Düzgün çizgiler çizmek için kullanılabilir.
![](/videos/stroke_lazy_rope.mp4) 

### Darbe düzleştirme {#stroke-smoothing}
Daha düzgün bir darbe elde etmek için işaretçinin birkaç konumunun ortalamasını alır.
Yüksek değerlerde darbe işaretçinin gerisinde kalır, ama sonunda ona yetişir.
Düzgün çizgiler çizmek için kullanışlıdır.

### Yaslama yarıçapı {#snap-radius}
İşaretçi son darbenin bittiği yere yakın bir noktadan başladığında, darbeyi bir öncekine yaslar. Yarıçap, önceki darbenin sonunun ne kadar uzakta aranacağını belirler. Sık sık ara vererek uzun, kesintisiz çizgiler çizerken işe yarayabilir.

### ![](/icons/trail.webp) İz {#trail}

Etkinleştirildiğinde her yeni damga, darbenin hemen arkasındaki son noktaları da yeniden uygular. `İz sayısı` kaç noktanın yeniden uygulanacağını, `İz yoğunluğu` ne kadar güçlü olacaklarını, `İz yarıçapı` ise ne kadar büyüyeceklerini belirler.

İz yalnızca `Nokta` darbe türüyle çalışır ve `Sırt` [düşüş etkisiyle](#influence) çalışmaz.

### ![](/icons/silhouette.webp) Siluet {#silhouette}
![](/images/stroke_silhouette.webp)
Varsayılan olarak darbeler yalnızca fırça yarıçapının içindeki model yüzeyini etkiler. Siluet etkinleştirildiğinde darbe modelin tamamı boyunca yansıtılır. Bir modelin ilk kaba şekillendirmesinde ya da yanlarının dik kalması gereken şekillerde çok işe yarayabilir.

Yansıtma yönü açıkça belirlenebilir:

* `X`, `Y`, `Z` - sabit bir eksen boyunca yansıtır.
* `Görüntüle` - kamera yönünde yansıtır.
* `Sabitlendiyse` - kamera yönünde yansıtır, ama yalnızca kamera bir görünüme sabitlenmişken. Aksi halde darbe normal bir darbe olarak kalır.
* `En Yakın` - kamera yönüne en yakın eksen boyunca yansıtır. Varsayılan budur.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Rastgeleleştir {#randomize}

![](/images/stroke_randomize.webp)

Darbenin `Yoğunluk`, `Kaydırma`, `Döndürme` ve `Ölçek` değerlerinin her biri rastgeleleştirilebilir. Bir satırı açıp kapatmak için onay kutusunu kullanın. Bununla çeşitli efektler elde edebilirsiniz; örneğin boyama aracıyla rastgeleleştirme alacalı bir renk verir, oluk aracıyla ise cilt ayrıntısı oluşturmak için kullanılabilir.

`Periyot (daha yavaş)` rastgele döngünün uzunluğunu belirler: yavaş, dalgalı değişimler için artırın, hızlı bir gürültü için azaltın. Her satırın yanındaki küçük düğme periyodu yalnızca o satır için ölçekler.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Rastgeleleştir - HSV {#randomize-hsv}

Boyama yapan araçlarda boya renginin `Renk Tonu`, `Doygunluk` ve `Değer` bileşenleri de kendi periyotlarıyla rastgeleleştirilebilir. Cilde ya da taşa hafif renk çeşitliliği katmak için harikadır.

### Darbe kaydırma {#stroke-offset}

Darbeye sabit bir kaydırma uygulayarak parmağınızın onu örtmesini önler. Küçük ekranlarda kullanışlıdır. Global bir ayardır: onay kutusuyla etkinleştirin, her araç için geçerli olur.


## ![](/icons/alpha.webp) Alfa {#alpha}
![](/images/stroke_alpha.webp) 

`Alfa`, fırçanızın davranışını değiştiren bir dokudur.
Gri tonlamalı bir görüntüdür: siyah pikseller deformasyon olmadığı, beyaz pikseller tam deformasyon anlamına gelir.

Değiştirmek için alfa görüntüsüne tıklayın. Yerleşik alfaların ve kendi içe aktardıklarınızın yanı sıra, alfa listesi Poly Haven'dan yer değiştirme (displacement) haritaları da indirebilir.

Bir malzeme önayarından alfa yüklemek için malzeme önizlemesine tıklayın. Malzeme önayarlarını buradan kaydedebilir ve dokuları araçla birlikte gömmeyi seçebilirsiniz.

::: tip
Doku hiçbir zaman yeniden boyutlandırılmaz, bu yüzden büyük dokular performansı yavaşlatabilir.
:::

### ![](/icons/blend_contrast.webp) Alfayı düzelt {#invert-pixels}
İçe aktarılmış bir alfadaki `Düzelt...` düğmesi, görüntünün kendisini düzelten bir pencere açar: orta değeri, piksellerin tersine çevrilmesi (siyah beyaz, beyaz siyah olur), 90° döndürme ve yatay ya da dikey çevirme. Görüntü dosyası yeniden yazılır, böylece diğer uygulamalar da düzeltilmiş görüntüyü görür.

::: tip

Nomad ile birlikte gelen yerleşik alfalar düzeltilemez.

:::

### Projeksiyon {#projection}

Alfanın modele nasıl yansıtıldığı:

* `Yüzey` - alfa, fırçanın altındaki yüzeyin üzerine, onun yönelimini izleyerek yerleşir.
* `Ekran` - alfa doğrudan görünümden yansıtılır.
* `Döşeme` - alfa görünümden yansıtılır ve üzerine boyarken bir şablon gibi yerinde kalır; böylece tekrar eden bir desen kusursuzca birleşir. Döndürme kilitlenir ve kalem basıncı desenin boyutunu değiştirmez.
* `Üç düzlemli` - alfa 3 eksen boyunca yansıtılır. Aşağıdaki ölçeklendirme, döndürme ve döşeme seçeneklerinin yerini üç düzlemli doku ayarları alır.

### ![](/icons/diagonal.webp) Ölçeklendirme {#scaling}

Nomad'da fırça, yarıçapını sizin belirlediğiniz bir dairedir. Dokular ise çoğunlukla kare ya da dikdörtgendir; `Ölçeklendirme` parametreleri dokunun daireye nasıl sığacağına karar vermenizi sağlar. Kare bir doku için 0,7 değeri dokuyu dairenin içine sığdırır. 1 değeri ise dokuyu daire içine sığacak şekilde büyütür ve kenarlarını kırpar.

![](/images/alpha_scaling.webp) 

`Ölçeklendirme Y` etkinleştirildiğinde alfayı dikey olarak esnetebilirsiniz. İlk kaydırıcı bu durumda `Ölçeklendirme X` olur.

![](/images/alpha_scaling_y.webp) 

`Yatay çevir` alfayı soldan sağa aynalar.

### Döndürme {#rotation}

Alfa dokusu, darbenin yönünü izleyecek şekilde döndürülür. Bir döndürme kaydırması ekleyebilirsiniz; kilit simgesi etkinse doku, ekrana göre bu açıda kilitli kalır.

Yanındaki kalem düğmesi, döndürme kilitli değilken `Yakala • dinamik yarıçap` ve `Yakala • dinamik yoğunluk` darbelerinde, kaleminizi kendi ekseni etrafında çevirdiğinizde (barrel roll) alfayı döndürür. Yalnızca bunu destekleyen kalem donanımlarında çalışır.

### Döşeme {#tiling}
![](/images/stroke_tiling.webp) 

Dokunun fırça profili içinde ne sıklıkla tekrarlandığı. `Döşeme - X` ve `Döşeme - Y` kipleri, darbe içinde tek bir dokuyla sınırlamanıza (`Yok`), dokuları tekrarlamanıza (`Tekrarla`) ya da desen oluşturmak veya dikişsiz dokular yapmaya yardımcı olmak için her ikinci dokunun çevrildiği aynalı tekrara (`Aynala`) olanak tanır. `Yuvarla` darbesiyle, `Döşeme` projeksiyonuyla ya da 1'den büyük bir `Döşeme` değeriyle kullanılabilir.

`İçine sığdır` yalnızca kare olmayan alfa ve fırça dokuları için önemlidir. Etkinleştirildiğinde her görüntü, aralık bırakmadan kendi başına döşenir. Alfa ile diğer görüntülerin en boy oranları farklı olduğunda onları uyumlu tutmak için devre dışı bırakın.

![](/videos/alpha_tiling.mp4) 



### Orta değer {#mid-value}

Varsayılan olarak siyah pikseller deformasyon olmadığı, beyaz pikseller ise tam pozitif deformasyon anlamına gelir; örneğin kaya desenli bir alfa dokusuna sahip bir kil fırçası, yüzeyi yalnızca alfanın siyah olmadığı yerlerde dışarı çeker.

Fırçanın yüzeyi içeri itmesini ya da hem içeri itip HEM DE dışarı çekmesini istiyorsanız orta değeri değiştirebilirsiniz. Değeri 0,5 yaparsanız alfadaki orta gri hiçbir şey yapmaz, siyah içeri iter, beyaz dışarı çeker.

Doğru değeri bulmanıza iki düğme yardım eder: kare düğme orta değeri görüntünün kenarından okur, seçici ise değeri doğrudan alfanın üzerinden seçmenizi sağlar.




## ![](/icons/falloff.webp) Düşüş {#falloff}

![](/images/falloff_menu.webp) 

[Alfa](#alpha) ile benzerdir, ancak yoğunluğu tek bir eğriyle yönlendirirsiniz. Alfa ile birleştirilir; böylece ayrıntı için bir doku, kenarlardaki solmayı ve aracın merkezindeki yoğunluğu kontrol etmek için de düşüşü kullanabilirsiniz.

Eğri en üstteyken tam deformasyon vardır, en alttayken fırçanın hiçbir etkisi olmaz.

Eğriyi fırça ucunun bir kesiti gibi düşünebilirsiniz. Alttaki bölüm, fırçanın tek bir 'damgasının' model yüzeyinde nasıl görüneceğinin önizlemesini gösterir; fırçanın bir alfa dokusu varsa, düşüş ile alfanın birbirini nasıl etkileyeceğini görmeniz için o da gösterilir.

### ![](/icons/fx.webp) Önayar {#preset}
`Önayar...` seçiliyken eğri grafiğine tıklamak bir önayar menüsü açar. Yuvarlak eğriler daha yumuşak, köşeli eğriler daha keskin sonuçlar verir. Sol araç çubuğundaki `Alt` düğmesi düşüşü fiilen tersine çevirir; böylece eğrinin tepesi yüzeyi dışarı çekmek yerine içeri iter, ya da tersi.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
Seçildiğinde kendi düşüş eğrilerinizi çizebilirsiniz. Eğri düzenleyici, Nomad'ın geri kalanındaki eğrilerle aynı şekilde çalışır:

* Yeni bir nokta oluşturmak için eğriye tıklayın
* Bir noktayı yeniden konumlandırmak için sürükleyin
* Keskin ile yumuşak arasında geçiş yapmak için bir noktaya tıklayın
* Bir noktayı silmek için komşu noktanın üzerine sürükleyin

### ![](/icons/curve_bspline.webp) B-spline {#b-spline}
Seçildiğinde kendi düşüş eğrilerinizi çizebilirsiniz. Düzenleyici Catmull-Rom ile aynı şekilde çalışır, ama eğri noktaları doğrudan eğrinin üzerinde durmak yerine eğriyi etkiler; bu da daha yumuşak eğri şekilleri oluşturmaya yardımcı olabilir.

### ![](/icons/curve_bevel.webp) Pah {#bevel}
Noktalar düz çizgilerle birleştirilir; köşeler yuvarlatılır ve yuvarlaklığın boyutu her noktanın keskinliğine bağlıdır. Kenarında temiz bir pah bulunan düz tepeli fırçalar için kullanışlıdır.

Eğri düzenleyicide 3 düğme vardır:

| Öğe     | Simge                        | Açıklama                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Büyüt | ![](/icons/maximize.webp)  | Eğri düzenleyiciyi genişletir                      |
| Sıfırla    | ![](/icons/reset.webp)     | Eğriyi varsayılan durumuna döndürür        |
| Simetri | ![](/icons/symmetric.webp) | Eğriyi simetrik bir 'fırça ucu' olarak gösterir |


### Etki {#influence}

* `Küre` (3d) - Etki, verteksin fırça merkezine olan uzaklığı alınarak hesaplanır.
* `Daire` (2d) - Verteks, fırça merkezine olan uzaklığı alınmadan önce alan düzlemine yansıtılır. Alfaların örneklenme şekline benzer. 
* `Silindir` - Etki, alan boyunca bir silindir olarak yansıtılır. Aşağıdaki [Siluet](#silhouette-1) seçeneğini etkinleştirmekle aynıdır.
* `Sırt` - Düşüş darbenin enine ölçülür, böylece eğri darbenin tamamının kesiti olur. `Sim` düğmesi bu durumda profili darbenin iki yanına aynalar: bir tarafı düzenlediğinizde diğeri de onu izler. Kapalıyken eğri, darbenin sol kenarından sağ kenarına uzanır. Düzleştirme tabanlı araçlarda kullanılamaz.

### ![](/icons/silhouette.webp) Siluet {#silhouette-1}
Varsayılan olarak darbeler yalnızca fırça yarıçapının içindeki model yüzeyini etkiler. Siluet etkinleştirildiğinde darbe modelin tamamı boyunca yansıtılır. Bir modelin ilk kaba şekillendirmesinde ya da yanlarının dik kalması gereken şekillerde çok işe yarayabilir. Darbe sekmesindeki [Siluet](#silhouette) ile aynı yansıtma seçeneklerine sahiptir.



## ![](/icons/filter.webp) Filtre {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Darbe biriktir {#accumulate-stroke}
Bir darbede eklenip çıkarılabilecek malzeme miktarındaki sınırı kaldırır. Örneğin `Kil` aracında bu seçenek açıktır, böylece malzeme birikmeye devam edebilir; `Fırça` aracında ise kapalıdır, bu yüzden aynı darbeyi ağ örgüsünün aynı bölgesinde gezdirmeye devam ederseniz darbe malzeme eklemeyi bırakır. 

### ![](/icons/culling.webp) Sadece öne bakan verteks {#front-facing-vertex-only}
Bu seçenek arkaya bakan verteksleri yok sayar.
İnce bir geometrinin bir kısmını diğer tarafını etkilemeden boyamak istediğinizde işe yarayabilir.
Heykel yaparken de çalışır, ancak bazı bozukluklarla karşılaşabilirsiniz.

### ![](/icons/eye_open.webp) Yalnızca görünür köşeler {#visible-vertex-only}
Kameradan bakıldığında başka yüzeylerin arkasında gizli kalan verteksleri yok sayar. Bu seçenek maskeleme, boyama, `Yüz Grubu` ve `Gizle` araçlarının şekil darbelerinde (lasso, dikdörtgen...) görünür.

### ![](/icons/dynamic.webp) Dinamik topolojiye izin ver {#allow-dynamic-topology}
Bu seçenek yalnızca ağ örgünüz [Dinamik topoloji](topology.md#dynamic-topology) kipindeyse kullanılabilir. Dinamik topolojiyi araç başına açıp kapatabilirsiniz.

### ![](/icons/connect.webp) Bağlı topoloji {#connected-topology}
Yalnızca araçla dokunduğunuz yüzeye bağlı verteksleri şekillendirir. Örneğin `Taşı` aracıyla kullanıldığında, bir parça başka bir parçayla kesişse bile onu taşıyabilmenizi sağlar.
![](/videos/connected_topology.mp4)

### Alanı koru {#protect-area}
![](/images/filter_protect_area.webp) 

Bu seçenekler, araçların ağ örgünüzün bazı kısımlarını çeşitli koşullarda etkilemesini engeller. Her biri `Otomatik`, `Hayır` veya `Evet` olarak ayarlanabilir; küçük ok, `Otomatik` değerinin o anda neye karşılık geldiğini gösterir.

* `Gizle` - Ağ örgüsünün bazı kısımları gizleme aracıyla gizlendiyse, korunup korunmayacaklarını belirler. `Otomatik` durumunda gizli yüzler korunur, ancak tel kafesleri görünürse korunmaz (bkz. [Genel taslak](settings.md#wireframe) ayarları).
* `Maske` - Ağ örgüsünün bazı kısımları maskelendiyse, korunup korunmayacaklarını belirler. `Otomatik` durumunda maskeli kısımlar, maske [Gölgelendirme](shading) menüsünde görünür olduğu sürece korunur.
* `Yüz Grubu` - Bir aracı yalnızca ilk dokunulan yüz grubunun içinde kullanıp kullanamayacağınızı belirler. `Otomatik` durumunda bu, yüz gruplarının [Gölgelendirme](shading) menüsünde görünür olup olmadığına bağlıdır.

`(Tümü)` düğmesi bu korumaların tüm araçlarda ortak, global ayarlar mı yoksa araç başına ayarlar mı olacağını belirler.


### Alan örnekleme {#area-sampling}
Bazı fırçaların ya da darbe seçeneklerinin çalışabilmesi için yüzeye ait bir düzlem normali ve düzlem konumu gerekir.

Bu ortalama düzlemin nasıl hesaplanacağını, örnekleme alanını araç yarıçapının bir oranı olarak ayarlayarak kontrol edebilirsiniz.

%100'de seçim dairesinin içindeki her nokta hesaba katılır.

%0'da yalnızca en yakın verteks ya da üçgen hesaba katılır. Bu değerler `Normal yarıçap` ve `Pozisyon yarıçapı` için birbirine bağlanabilir ya da kilidi açılarak ayrı ayrı ayarlanabilir.

### Alan Normal Filtresi {#keep-sharp-edges}
Normalleri yüzey normalinden çok fazla sapan noktaları dışarıda bırakır.

Düzlem alanının nasıl hesaplandığını (Alan örnekleme) değiştirir; bu yüzden en çok kil ya da düzleştirme tabanlı araçlarda veya çoğunlukla düz bir yüzeyi taşırmadan boyamak istediğinizde işe yarar.

`Min` ve `Maks` açıları, dışarıda bırakılan noktalarla tamamen etkilenen noktalar arasındaki geçişi kontrol eder; yanlarındaki küçük renkli disk bunu gösterir.

![](/videos/filter_keep_sharp_edges.mp4)

### Düşüş Normal Filtresi {#falloff-normal-filter}
[Alan Normal Filtresi](#keep-sharp-edges) gibi, normalleri yüzey normalinden çok fazla sapan noktaları dışarıda bırakır, ancak düzlem hesabı yerine fırça düşüşüne etki eder. Kırışıkları ya da tümsekleri boyamak için kullanışlıdır.


### Derinlik maskesi {#depth-masking}
![](/images/stroke_depthmask.webp)

Hesaplanan düzlemin (Alan örnekleme) belirli bir mesafe üstünde ya da altında kalan noktaları dışarıda bırakır.

Yalnızca tümsekli bölgeleri ya da yalnızca oyuk bölgeleri boyamak için kullanılabilir.

Grafik, yüzeyin bir kesitini temsil eder: yatay çizgi yüzeyin bulunduğu yerdir, daire ise boyanın düşüş yarıçapını yüzeyin üstüne ve altına göre gösterir. `Yükseklik ofseti`, maskeleme hesabına başlanacak noktanın yüzeyin yüzde kaç üstünde ya da altında olacağıdır. `Derinlik azaltma` etkinken `Üst alan` ve `Alt alan`, ofset noktasının üstündeki ve altındaki düşüşü ölçeklendirmenizi sağlar.

#### Örnek: Oyuklara boyama {#example-paint-in-cavities}
Yalnızca oyuk bölgeleri boyamak için yükseklik ofsetini -%100 yapın ve üst alan kaydırıcısını, daire yatay çizgiden uzaklaşacak şekilde ayarlayın. Böylece ilk tıklama 'sıfır' derinliği belirler ve yalnızca bu derinliğin altındaki alanlar etkilenir.

![](/videos/stroke_depth_cavity.mp4)

#### Örnek: Tümseklere boyama {#example-paint-on-bumps}
Yalnızca yüksek bölgeleri boyamak için yükseklik ofsetini +%90 yapın; böylece dairenin alt kısmı yatay çizgiyle biraz kesişir. 'Yüksek' bir bölgenin tepesine tıkladığınızda derinlik belirlenir; o derinlikteki her şey, biraz altı ve daha yüksekte kalan her şey boyanır. Derin oyuklar atlanır.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Basım Şiddeti {#pressure}
![](/images/pressure_menu.webp) 

Kalem basıncının fırçaları nasıl etkilediğini kontrol eder.

### Global ayarları kullan {#use-global-settings}

Varsayılan olarak `Global ayarları kullan` etkindir; yani tüm fırçalar aynı basınç değerlerini paylaşır. Geçerli araca kendi basınç ayarlarını vermek için işaretini kaldırın.

### ![](/icons/radius.webp) Yarıçap {#pressure-radius}

Bu eğri, fırça yarıçapının basınçtan nasıl etkilendiğini kontrol eder. Varsayılan ilişki doğrusaldır; kaleminizin tepkisi düzgünse yarıçaptaki değişim de düzgün hissettirmelidir. Bununla birlikte birçok kalemin tepkisi doğrusal değildir ve bunu bu eğriyle telafi edebilirsiniz. Örneğin yarıçap yüksek basınçta en büyük değerine ulaşmıyor gibi geliyorsa, yarıçapı daha erken artırmak için 'out-pow3' gibi, kavisi yukarı doğru olan bir eğri önayarı kullanın.

Bu pencere düşüş eğrisi ekranına benzer: eğri penceresine dokunarak bir önayar kullanabilir ya da `Catmull-Rom`, `B-spline` ve `Pah` kipleriyle kendi eğrilerinizi çizebilirsiniz.

Sabit bir yarıçap istiyorsanız bu bölümü devre dışı bırakın.

### ![](/icons/intensity.webp) Yoğunluk {#pressure-intensity}

Yarıçap eğrisine benzer, ama yoğunluğu kontrol eder. Sabit bir yoğunluk istiyorsanız bu bölümü devre dışı bırakın.

### Basıncı %100 ile sınırla {#limit-pressure}

Kalem basıncının hiçbir zaman %100'ü geçmemesini sağlar. Global bir ayardır.

### Basınç yumuşatma {#pressure-smoothing}

Daha yumuşak sonuçlar için kalem basıncı olaylarının ortalamasını alır.
