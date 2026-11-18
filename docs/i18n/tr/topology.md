# ![](/icons/multires.webp) Topoloji {#topology}

Bu menü, Nomad'daki nesnelerin topolojisini yönetir; ayrıca nesneler arasında ve dokular arasında detay pişirmek ve aktarmak için araçlar içerir.

![](/images/topology_overview.webp)

Nomad poligon tabanlıdır, geometriyi üçgenler ve dörtgenlerle işler.
Topoloji derken hem yüz sayısını hem de noktaların (verteksler) birbirine nasıl bağlandığını kastediyoruz.

Özellikle ince detaylar şekillendirmek veya boyamak istiyorsanız topolojiyi göz önünde tutmanız önemlidir.

::: tip Topolojinizi nasıl takip edersiniz?
[Genel taslak](settings.md#wireframe) görünümünü açabilir ya da kısaca [Yumuşak gölgelendirme](settings.md#smooth-shading) seçeneğini kapatabilirsiniz.
:::

![](/images/topology_top.webp)

Nomad'ın topoloji menüsünde iki sıraya dizilmiş birkaç sekme bulunur:

| Yöntem                                 | Simge                        | Açıklama                                                              |
| :------------------------------------: | :--------------------------: | :-------------------------------------------------------------------: |
| [Çoklu Çözünürlük](#multiresolution)   | ![](/icons/multires.webp)   | Alt bölümleme ile birden fazla detay seviyesinde çalışın               |
| [Voksel](#voxel-remesher)              | ![](/icons/voxel.webp)      | Yoğunluğu her yerde eşit olan yeni bir topoloji hesaplayın            |
| [Dinamik topoloji](#dynamic-topology)  | ![](/icons/dynamic.webp)    | Şekillendirirken veya boyarken yüzleri yerel olarak, anında ekleyin/silin |
| [Çeşitli](#misc)                       | ![](/icons/topo_extra.webp) | Delikleri kapatın, manifold yapıyı zorlayın ve üç düzlemliye dönüştürün |
| [Primitif](#primitive)                 | ![](/icons/dot.webp)        | Primitif seçenekleri                                                  |
| [Azalt](#decimation)                   | ![](/icons/decimate.webp)      | Şekli koruyarak yüz sayısını azaltın                               |
| [Dörtgen Yeniden Örgüleme](#quad-remesh) | ![](/icons/quad.webp)     | Nesneyi temiz bir dörtgen düzeniyle yeniden oluşturun                 |
| [UV Açma](#uv-unwrap)                  | ![](/icons/uv.webp)         | Doku kaplamak için UV oluşturun                                       |
| [Pişir](#bake)                         | ![](/icons/bake.webp)       | Detayları ve boyamayı dokulara, vertekslere veya VDM damgalarına pişirin |


## Poligon istatistikleri {#polygon-stats}

![](/images/topology_stats.webp)

Her sekmenin üst kısmı, seçili nesnenin poligon sayılarını, sahnede birden fazla nesne varsa tüm sahnenin sayılarını da gösterir. Sütunlar sırasıyla verteks, üçgen, dörtgen (4 kenarlı poligon) ve UV koordinatı sayısıdır (nesnenin UV'si yoksa 0).

Sahnedeki her nesneyi kesin sayılarıyla, yüz grubu sayısı da dahil olmak üzere listelemek için bu bölüme dokunun.

## ![](/icons/cog.webp) Dişli menüsü {#gear-menu}
[Dörtgen Yeniden Örgüleme](#quad-remesh) ve [Pişir](#bake) sekmelerindekiler gibi bazı bölümlerin ek seçenekleri vardır. Bunları bölüm başlığının yanındaki dişli simgesiyle açabilirsiniz.

## ![](/icons/multires.webp) Çoklu Çözünürlük {#multiresolution}

![](/images/topology_multires_menu.webp)

### Çoklu çözünürlük nedir? {#what-is-multiresolution}
Çoklu çözünürlük özelliği iki ana durumda işe yarar:
- Nesnenizin poligon sayısını artırmak için yumuşak alt bölümleme algoritması
- Küçük ve büyük ölçekli düzenlemeler arasında gidip gelebilmeniz için birden fazla çözünürlük seviyesini yönetmek

![](/videos/multiresolution.mp4)

#### Çoklu çözünürlükle çalışma {#multiresolution-workflow}
Çoklu çözünürlüğün önemli bir yanı şudur: daha düşük bir çözünürlüğe dönüp nesnenizde değişiklik yapabilir, sonra yüksek çözünürlükteki detayları kaybetmeden en yüksek çözünürlüğe geri dönebilirsiniz. Yüksek çözünürlükteki tüm detaylar otomatik olarak yeniden yansıtılır.

[Katmanlar](layers.md#layers) her çözünürlükte kullanılabilir.

::: warning
Nesnenizin topolojisini değiştiren bir araç kullanırsanız, nesnenin diğer tüm çözünürlüklerini kaybedersiniz!
Böyle bir durumda her zaman bir uyarı almanız gerekir, örneğin şunları kullanırken:
- [Voksel yeniden örgüleme](#voxel-remesher)
- [Dinamik topoloji](#dynamic-topology)
- [Kes aracı](tools.md#trim)
- [Ayır aracı](tools.md#split)
:::


### Çoklu çözünürlük kaydırıcısı {#multiresolution-slider}
Bu kaydırıcı, mevcut nesnedeki alt bölümleme seviyesi sayısını gösterir. 6 dikey çubuk varsa 6 alt bölümleme seviyesi vardır. Daire, o anda görüntülenen alt bölümleme seviyesini gösterir.

Kaydırıcının üstündeki küçük simgeler, her seviye için hangi seçeneklerin (`Seviye 0'ı kilitle`, `Lineer`, `Keskin sınır`, `Üçgenleri koru`) kullanıldığını gösterir.

### Tersine çevir {#reverse}
En düşük alt bölümleme seviyesindeyken bu düğme, mevcut seviyenin altında yeni bir seviye oluşturmaya çalışır. Bu genellikle yalnızca nesne baştan alt bölümleme ile oluşturulmuşsa mümkündür; örneğin Nomad'da ya da çoklu çözünürlüklü alt bölümleme yüzeyleri kullanan başka 3d uygulamalarda.

### Alt bölümlere ayır {#subdivide}
*Alt bölümlere ayır* düğmesi poligon sayısını 4 katına çıkarır; bu sayı çok hızlı artabileceği için gözünüz poligon sayısında olsun! Sonuç çok ağır olacaksa Nomad sizden onay ister.
*Alt bölümleme yüzeylerinin* önemli bir özelliği, *yumuşak bir yüzeye* doğru yakınsamalarıdır.
Nasıl çalıştığını anlamak için *Alt bölümlere ayır* düğmesini yalnızca birkaç poligonu olan bir nesnede deneyebilirsiniz.

Bu *yumuşatma* davranışını `Lineer` seçeneğiyle kapatabilirsiniz.

### Daha düşük olanı sil {#delete-lower}
Görüntülenen seviyenin altında alt bölümleme seviyeleri varsa onları siler. Bunu yanlışlıkla yaparsanız Tersine çevir düğmesiyle yeniden oluşturabilirsiniz.

### Daha yüksek olanı sil {#delete-higher}
Görüntülenen seviyenin üstünde alt bölümleme seviyeleri varsa onları siler.

### ![](/icons/lock.webp) Seviye 0'ı kilitle {#lock-lv0}
Daha yüksek seviyelerde şekillendirirken en düşük alt bölümleme seviyesinin şeklini korur. Boyama yine de seviye 0'a kadar iner. Nesneniz başka bir uygulamada oluşturulduysa ve temel nesnenin değişmeden kalması gerekiyorsa bu önemli olabilir.

Bu seçenek yalnızca ilk alt bölümlemeden önce kullanılabilir. Kapalıyken, yüksek alt bölümleme seviyelerinde yapılan büyük değişiklikler seviye 0'ı da hareket ettirir.

### ![](/icons/linear.webp) Lineer {#linear-subdivision}
Ağı hiç yumuşatma uygulamadan alt bölümlere ayırır.

### ![](/icons/group.webp) Keskin sınır {#sharp-border}
Nesnenizde yüz grupları varsa, bu seçeneği açmak yüz grubu sınırlarını keskin tutar. Her alt bölümleme seviyesi için ayrı ayrı ayarlanabilir (alt bölümleme kaydırıcısında, ilgili seviyenin üstünde bunu belirten küçük bir simge görünür).

### ![](/icons/triangle.webp) Üçgenleri koru {#keep-triangles}
Standart alt bölümleme yüzeyi sistemlerinin çoğu, alt bölümleme sırasında tüm poligonları dörtgene dönüştürmeye çalışır. Bu seçenek, alt bölümlemenin bunun yerine üçgen kullanmasını sağlar.

::: tip

Alt bölümleme varsayılan olarak tüm keskin kenarları yumuşatır. Kenarları biraz keskin tutmak için ilk 2 alt bölümleme seviyesinde `Lineer` veya `Keskin sınır` kullanmayı deneyin, sonra daha yüksek seviyeler için kapatın. Böylece yarı keskin, alt bölümlenmiş bir ağ elde edersiniz.

:::

### En yüksek seviyeyi göster {#show-highest-level}
Daha düşük bir seviyede şekillendirirken en yüksek seviyeyi tüm detaylarıyla gösterir. Büyük değişiklikler yaparken nihai sonucu görmek için kullanışlıdır.

### Genel taslak: Yalnızca seviye 0 {#wireframe-level-0-only}
[Genel taslak](settings.md#wireframe) açıkken yalnızca en düşük seviyenin tel kafesini gösterir. Yüksek seviyelerin yoğun tel kafesi şekli görmeyi zorlaştırabilir.


## ![](/icons/voxel.webp) Voksel {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
`Voksel` yeniden örgüleme kullanıldığında ağın tamamı tek tip bir çözünürlüğe zorlanır, yani tüm poligonlar aşağı yukarı aynı boyutta olur. Topolojiyi düşünmek istemediğinizde ve yalnızca serbestçe şekillendirmek istediğinizde çok kullanışlıdır.

Tipik bir şekillendirme süreci, kaba bir şekli düşük çözünürlükte oluşturmak için `Voksel` yeniden örgüleme ile başlayabilir.
Ağı çok fazla gerdiğinizde, aşırı bozulmayı önlemek için arada bir *Yeniden ağ örgülendirme* düğmesine basmanız yeterli.

![](/videos/voxel_remesher.mp4)


::: tip Voksel mi?
Yukarıda belirtildiği gibi Nomad poligon tabanlı bir yazılımdır, ancak `Voksel` yeniden örgüleme, yeniden örgüleme için (geçici olarak) başka bir yaklaşımın kullanıldığı bir istisnadır.

Önemli bir fark, voksel yaklaşımının kendi kendisiyle kesişmeleri kabul etmemesidir; bunlar çözümlenir.
Ayrıca delikli ağları desteklemez.

Delik derken `genus hole` (simidin ortasındaki `delik`) değil, `su geçirmez`/`kapalı` olmayan ağları kastediyoruz.
Pratikte bu, yeniden örgüleme uygulanmadan önce tüm deliklerin [Kes aracında](tools.md#trim) veya [Delik doldurma özelliğinde](#holes) olduğu gibi doldurulacağı anlamına gelir. Aşağıdaki [Delikler](#voxel-holes) seçeneği bunun nasıl yapılacağını belirler.
:::

### ![](/icons/voxel.webp) Yeniden ağ örgülendirme {#voxel-remesh}
Voksel yeniden örgülemeyi çalıştırır. Düğmenin üzerindeki küçük simgeler, aşağıdaki seçeneklerden hangilerinin açık olduğunu hatırlatır.

### Çözünürlük {#voxel-resolution}
Hesaplama sırasında kullanılan voksellerin boyutu; yüksek değerler daha fazla detay verir. Bu parametreyi değiştirirken, sonucun önizlemesi olarak ağın üzerinde bir dama tahtası deseni belirir.

Damlalık, çözünürlüğü dokunduğunuz yerdeki ağ yoğunluğundan alır. Yanındaki küp düğmesi değeri dünya birimiyle bir `Kenar uzunluğu` değerine çevirir: böylece aynı değer her nesnede aynı detayı verir.

### Çoklu çözünürlük oluştur {#build-multiresolution}
Voksel yeniden örgüleme için daha düşük çoklu çözünürlük seviyeleri oluşturur. Çözünürlüğü dama tahtası desenine bakarak ayarlar ve çoklu çözünürlük oluşturmayı 2'ye getirirseniz, sonuçtaki detay çözünürlük kaydırıcısıyla eşleşir; Çoklu Çözünürlük sekmesine gittiğinizde seviye 2'de olursunuz, yani seviye 1 ve seviye 0'da daha düşük çözünürlüklü ağlarınız olur. Bu, hem eşit poligonlu temiz bir ağ elde etmenin hem de düşük çözünürlüklü bir kontrol ağına sahip olmanın iyi bir yoludur.

Ayrıca yüksek çözünürlüklerde daha hızlı çalışır ve daha az bellek kullanır. Ancak düşük çözünürlük ve çok sayıda seviyeyle detay kaybedersiniz.

::: tip İpucu: Çoklu çözünürlük oluşturma ve stabil düzleştirme

Bu seçenek bazen geometride yumuşatılması zor 'döngüler' oluşturup küçük sivilceler gibi kabarıklıklara yol açabilir. Böyle olursa, Pürüzsüzleştir aracının seçeneklerinde 'Stabil düzleştirme' seçeneğini açın. 

:::

### İnce kısımları kalınlaştır {#thicken-thin-parts}
Vokselden daha ince kısımlar yeniden örgüleme sırasında kopabilir veya yok olabilir. Bu seçenek onları kalınlaştırarak korunmalarını sağlar; yüksek değerler daha fazla kalınlaştırır. `Keskin kenarlar` veya `Keskin sınır` ile birlikte kullanılamaz.

### Delikler {#voxel-holes}
Yeniden örgülemeden önce deliklerin nasıl kapatılacağı:

* `Doldur` - Her delik kendi sınırından başlanarak ayrı ayrı kapatılır.
* `Şekil` - Delikler çevredeki yüzeyi takip ederek kapatılır ve üst üste binen açık parçalar birleştirilir.

### ![](/icons/angle.webp) Keskin kenarlar {#keep-sharp-edges}
Yeni noktaları orijinal ağın keskin kenarlarına yaslar. Çoğunlukla basit primitif boolean işlemleri için kullanışlıdır ve bozulmalara yol açabilir.

### ![](/icons/group.webp) Keskin sınır {#voxel-sharp-border}
Yeni yüzler yüz grubu sınırlarını takip eder ve yüzeyin sınır boyunca kıvrıldığı yerlerde sınır keskin kalır.

### ![](/icons/group_separate.webp) Grupları ayrı tut {#keep-groups-separate}
Her yüz grubu kendi başına yeniden örgülenir: gruplar asla birleşmez ve her biri kendi grubunda kapalı bir parça olarak kalır. Bu modda çoklu çözünürlük oluşturulmaz. Nesnede birden fazla yüz grubu olduğunda kullanılabilir.

## ![](/icons/dynamic.webp) Dinamik topoloji {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Çoklu çözünürlük ve voksel yeniden örgüleme, topolojiyi kontrol etmek için sektörde yaygın yöntemlerdir; ancak ikisinde de poligonları fazla germediğinize veya fazla sıkıştırmadığınıza dikkat etmeniz gerekir. 

Dinamik topoloji alternatif bir yöntemdir. Siz şekillendirdikçe Nomad, fırça darbesi sırasında poligonları uyarlamalı olarak ekler ve siler; böylece küçük detaylar oyarken ihtiyaç duyduğunuz yere çok sayıda küçük poligon eklenir, başka yerlerde yumuşattığınızda ise poligonlar azalır.

Dinamik topolojinin dörtgen yerine üçgen poligonlar kullandığını unutmayın. Bu biraz dağınık görünebilir, ama tel kafese hiç bakmamak neredeyse daha iyidir: topolojiyi dert etmeden güzel bir heykel yapmaya odaklanın, sonra temiz bir dörtgen ağ elde etmek için Nomad'ın diğer yeniden örgüleme araçlarından birini kullanabilirsiniz.

Aşağıdaki videoda nasıl çalıştığını görebilirsiniz.

![](/videos/dynamic.mp4)

### Etkin {#enabled}
Dinamik topolojiyi açar. Fırça yarıçapı ve yoğunluk kaydırıcılarının altına bir DinTopo simgesi yerleşir; böylece DinTopo'yu her araç için ayrı ayrı açıp kapatabilirsiniz. Performansı belirgin şekilde etkileyebilir; katmanlar doğru şekilde güncellenir.

### Detay {#dyn-detail}
Detay miktarını kontrol eder; davranışı aşağıda anlatılan 'Detay neye göre...' seçimine bağlıdır. `Ekran` modunda etiket, hedef üçgen boyutunu piksel olarak gösterir. `Sabit` modunda bir damlalık, detayı dokunduğunuz yerdeki ağ yoğunluğundan almanızı sağlar.

### Detay neye göre... {#detail-based-on}
| Yöntem   | Açıklama                                                        |
| :------: | :-------------------------------------------------------------: |
| Ekran    | Detay seviyesi, nesnenin ekranda ne kadar büyük göründüğüne bağlıdır. Detay kaydırıcısı ince detay için %100 veya üstündedir ve küçük üçgenler oluşturur; düşük detay için %1'dir ve büyük üçgenler oluşturur.  |
| Yarıçap  | Detay miktarını araç yarıçapı belirler. İnce detay için küçük, düşük detay için büyük bir araç yarıçapı kullanın. Detay kaydırıcısı bu oranın çarpanıdır.                     |
| Sabit    | Detay miktarını detay kaydırıcısı belirler; ekran boyutundan veya araç boyutundan etkilenmez. `Yeniden ağ örgülendirme` bölümündeki [Detay](#all-detail) kaydırıcısıyla aynı değerdir.             |

::: tip İPUCU: Yarıçap modu

Yarıçap modunun nasıl çalıştığını daha iyi kavramak için detay kaydırıcısını bir parmağınızla hareket ettirmeye başlayın, aynı anda başka bir parmağınızla araç yarıçapını değiştirin. İkisinin nasıl bağlı olduğunu göreceksiniz.

:::

### Tercih... {#prefer}
| Yöntem  | Açıklama                 |
| :-----: | :----------------------: |
| Hız     | Performansa öncelik verir |
| Kalite  | Kaliteye öncelik verir   |

`Kalite` seçeneğini tercih ettiğinizde 2 temel fark vardır:
- iyileştirme şekillendirmeden önce uygulanır, böylece çok küçük detayları boyarken veya şekillendirirken daha az enterpolasyon kusuru oluşur
- iyileştirme adım adım ilerlemek yerine doğru detay seviyesine ulaşana kadar çalışır.
 
Böylece çok küçük detaylar şekillendirdiğinizde veya hızlı darbeler yaptığınızda topoloji her zaman beklendiği gibi iyileştirilir


### ![](/icons/pressure.webp) Yarıçapta basınç kullan {#use-pressure-on-radius}
Yalnızca `Yarıçap` etkinse geçerlidir. Açıkken detay seviyesi, fırça boyutu kalem basıncından etkilendiğinde bile her zaman fırça boyutunu yansıtır.

### Darbe düşüşünü kullan {#use-stroke-falloff}

Fırçanın düşüş eğrisini ve alfasını da DinTopo hesaplamalarına katar.

### Yöntem {#method}
Dinamik topolojinin ağı nasıl değiştireceğini seçer; hem siz şekillendirirken hem de [Yeniden ağ örgülendirme](#dyn-remesh) kullandığınızda geçerlidir:

| Yöntem           | Açıklama                                                              |
| :--------------: | :-------------------------------------------------------------------: |
| Tek tipleştirme  | Yüz ekleyebilir ve silebilir; yukarıdaki videoda kullanılan mod budur |
| Alt bölümleme    | Yalnızca yeni yüz ekler, yüz silemez                                  |
| Azaltım          | Yalnızca yüz siler, yeni yüz ekleyemez                                |

### ![](/icons/shield.webp) Maskelenmiş alanı koru {#protect-masked-area}
Maskelenmiş alanların topolojisinin değişmesini engeller.

### ![](/icons/normal.webp) Verteks ekstrapolasyonu {#vertex-extrapolation}
Noktaları mevcut yüzlerin üzerine düz bir şekilde yerleştirmek yerine, çevrelerindeki eğriliği takip eden yumuşak bir yüzeye yerleştirir.

### Detay {#all-detail}
Yeniden örgüleme işleminde kullanılan çözünürlük. DinTopo 'Sabit' modundaysa, bu menünün üstündeki Detay kaydırıcısıyla aynı değerdir. Damlalık, detayı dokunduğunuz yerdeki ağ yoğunluğundan alır.

### Yeniden ağ örgülendirme {#dyn-remesh}
DinTopo algoritmasıyla ağın tamamını yeniden örgüler. Tam bir yeniden örgüleme için genellikle [Voksel](#voxel-remesher) sekmesini kullanmanız gerekir.

Yine de vokselle karşılaştırıldığında bir avantajı vardır: ağın kapalı olması gerekmez ve maskelenmiş alan korunur; böylece yoğunluğun nerede fazla, nerede az olacağını daha iyi kontrol edebilirsiniz.



## ![](/icons/topo_extra.webp) Çeşitli {#misc}

![](/images/topology_misc_menu.webp)

Bu sekme ağı temizlemek veya dönüştürmek için araçları bir araya getirir: deliklerini kapatmak, manifold olmaya zorlamak ya da üç düzlemliye dönüştürmek.

### ![](/icons/hole.webp) Delikler {#holes}
![](/images/topology_holes_menu.webp)
Çoğu zaman nesneniz büyük olasılıkla su geçirmezdir, yani ağ 'kapalıdır'.

Nesnenizde delikler varsa bunları doldurabilirsiniz.

![](/videos/hole_filling.mp4)

::: tip
Voksel yeniden örgülemeyi çalıştırdığınızda, ister 1 ister birden fazla ağ üzerinde kullanın, tüm delikler otomatik olarak kapatılır.
:::

#### Delikleri kapat {#close-holes}
Delik kapatma işlemini çalıştırır.

#### Seçenekler {#holes-gear-menu}
Bu seçenekler deliklerin nasıl doldurulacağını değiştirir:

##### Yüz Grubu {#fill-face-group}
Yeni yüzlerin yüz grubunu seçer:

* `Karışık` - Tek bir yüz grubuyla çevrili bir delik o grubu kullanır, birden fazla gruba değen bir delik yeni bir grup alır.
* `Yeni` - Doldurulan delikler yeni bir yüz grubu alır.
* `Yeniden kullan` - Her delik, kendisini en çok çevreleyen yüz grubunu alır.

##### Detay {#fill-detail}
Deliği doldurmak için kullanılan poligon yoğunluğu. Bu kaydırıcıyı sürüklerken modelin üzerinde bir dama tahtası deseni görünür; bu, kullanılacak üçgen boyutu hakkında fikir verir. Onay kutusu bunu kapatır ve yalnızca mevcut noktaları kullanır; bu genellikle deliğin üzerinde uzun, ince üçgenler oluşturur ve bunları şekillendirmek zor olabilir.

##### Köprü {#fill-non-manifold}
Her sınırı ayrı ayrı doldurmak yerine, bir deliği ve içindeki adacıkları tek bir yüzey olarak doldurur. Daha yüksek bir açı, daha kavisli deliklerin de köprülenmesini sağlar. Onay kutusu bunu kapatır.

### ![](/icons/cog.webp) Manifold Zorla {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Manifold olmayan kenarları temizlemeye çalışır. İkiden fazla yüzün paylaştığı kenarları desteklemeyen harici yazılımlar için kullanışlı olabilir.

#### Temizle {#clean}
Temizleme işlemini çalıştırır.

#### Seçenekler {#force-manifold-gear-menu}
Bu seçenek ağın nasıl temizleneceğini değiştirir:

##### Küçük yüzeyleri sil {#delete-small-faces}
Küçük poligonları silmek ve birleştirmek için kullanılan bir eşik. Onay kutusuyla etkinleştirin.


### ![](/icons/triplanar.webp) Üç düzlemli {#triplanar}
![](/images/topology_triplanar_menu.webp)
Ağı bir [üç düzlemli](scene.md#triplanar) primitife dönüştürür.
Bu süreçte büyük olasılıkla çok fazla detay kaybedersiniz: katmanlar, boyama ve çoklu çözünürlük de kaybolur.

#### Küpe zorla {#force-cubic}
Üç düzlemlinin bir küp olmasını sağlar. Aksi halde üç düzlemli, nesnenizin etrafındaki en yakın sınırlayıcı kutuya uyar.

#### Dönüştür {#convert}
Üç düzlemli dönüşümünü çalıştırır.

#### Çözünürlük {#triplanar-resolution}
Üç düzlemli ızgaranın çözünürlüğü; yüksek değerler daha fazla detay korur.

## ![](/icons/decimate.webp) Azalt {#decimation}

![](/images/topology_decimation.webp)

Üçgen poligonlar kullanarak, olabildiğince fazla detayı korumaya çalışırken poligon sayısını azaltır.

Bu özellik, 3d baskı için dışa aktarmak istediğinizde işe yarayabilir.
Ancak üzerinde şekillendirmeye devam etmek istiyorsanız muhtemelen kullanmamalısınız, çünkü düzensiz üçgenler oluşturabilir.

Maskelenmiş alanların azaltılmayacağını unutmayın.

![](/videos/decimate.mp4)

::: tip

[Quad Remesher aracını](tools.md#quad-remesher) yüksek poligonlu nesnelerde kullanmak uzun sürebilir ve kontrolü zor sonuçlar verebilir. Ağı önceden [yüz grupları](tools.md#facegroup) ve azaltma ile hazırlamak, Quad Remesher'ın çok daha hızlı çalışmasını ve topoloji üzerinde çok daha fazla kontrol sahibi olmanızı sağlar.

* İdeal dörtgen akışınızı belirlemek için ağı yüz gruplarına ayırın.
* Yüz grubu sınırlarını yumuşatmak için yüz gruplarını rahatlatın.
* Azaltın. Bu, yüz grubu kenarında ince veya bozuk yüz kalmamasını sağlar. `Sınırı koru` altında `Yüz Grubu` seçeneğinin açık olduğundan emin olun. Böylece üçgen kenarları yüz grubu kenarlarınızı tam olarak takip eder.
* Quad Remesher seçeneklerinde rahatlatmanın kapalı olduğundan emin olun (ağı zaten rahatlattınız), böylece iyi sonuçlar almanız gerekir.

:::

### Azalt {#decimate}
Azaltma işlemini başlatır.

Azalt düğmesinin yanındaki simgeler aşağıdaki seçenekleri gösterir ve bunları açıp kapatmanızı sağlar. Yüzde, o seçeneğin ne kadar güçlü olduğunu gösterir.

* ![](/icons/palette.webp)  `Boyamayı koru` - Boyama detayı olan yerlere daha fazla üçgen yerleştirir.
* ![](/icons/triforce.webp) `Tek tip yüzler` - Eşit boyutlu üçgenler oluşturmayı tercih eder.
* ![](/icons/hole.webp)  `Delik` - Azaltma, açık geometrinin ve deliklerin yakınındaki sınırları değiştirmeden korumaya çalışır.
* ![](/icons/group.webp) `Yüz Grubu` - Azaltma, yüz grubu sınırlarını değiştirmeden korumaya çalışır.
* ![](/icons/uv.webp) `UV` - Azaltma, UV sınırlarını değiştirmeden korumaya çalışır.

### Hedef üçgenler {#target-triangles}
Hedef üçgen sayısını ayarlar. Varsayılan değer %50'dir; yüzde/hedef düğmesi yüzde ile kesin bir hedef poligon sayısı arasında geçiş yapar.

### Seçenekler {#decimate-gear-menu}
Her seçeneğin onu açıp kapatan bir onay kutusu ve gücünü belirleyen bir değeri vardır:

#### ![](/icons/palette.webp) Boyamayı koru {#preserve-painting}
Değer, boyama detayının ne kadar doğru korunacağını belirler. Yüksek değerler boyamayı daha fazla korur. Boyamayı önemsemiyorsanız 0'a ayarlayın.

#### ![](/icons/triforce.webp) Tek tip yüzler {#uniform-faces}
Yüksek değerler birbirine yakın boyutta üçgenler üretir.

#### Sınırı koru {#preserve-borders}
Sınırların azaltılmasını engeller. Sınır ağırlıkları `Delik`, `Yüz Grubu` veya `UV` sınırları için ayarlanabilir (`UV` için nesnenin UV'si olması gerekir).

## ![](/icons/quad.webp) Dörtgen Yeniden Örgüleme {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Nesneyi temiz bir dörtgen düzeniyle yeniden oluşturur. Bu sekmede birkaç yeniden örgüleyici bulunur; her birinin kendi `Yeniden ağ örgülendirme` düğmesi, `Hedef dörtgenler` kaydırıcısı ve dişli menüsü vardır. Hepsini nesnenizde deneyin, oldukça farklı sonuçlar verirler!

### Quad Remesher {#quad-remesher}
[Quad Remesher](tools.md#quad-remesher) aracıyla aynı yeniden örgüleyici; [Exoside](https://exoside.com/) tarafından geliştirilmiştir. Yalnızca bazı platformlarda kullanılabilir ve satın alma gerektirir: o zamana kadar `Yeniden ağ örgülendirme` düğmesinde bir alışveriş sepeti görünür.

`Araç seç`, kılavuz çizgileri çizmek ve yoğunluğu boyamak için Quad Remesher aracına geçer. Dişli menüsünde `Adaptif Kare Sayısı`, `Adaptif Boyut` (%100'de dörtgen boyutu eğriliği takip eder, %0'da dörtgenler eşit boyuttadır), `Sert Kenarları Otomatik Algıla` ve `Verteksi yeniden yansıt` bulunur.

::: tip
Kullanılabildiği yerlerde Quad Remesher genellikle en iyi sonuçları ve en fazla kontrolü sunar.
:::

### AutoRemesher {#autoremesher}
Dörtgen boyutunu ve şeklini yüzeye uyarlayan seçenekleri olan alternatif bir dörtgen yeniden örgüleyici.

#### ![](/icons/cog.webp) AutoRemesher dişli menüsü {#autoremesher-gear-menu}
Dişli menüsünde şu gelişmiş seçenekler bulunur:

##### Kenar ölçekleme {#edge-scaling}
Dörtgen boyutunu ölçekler; yüksek değerler daha büyük dörtgenler üretir.

##### Uyarlanabilirlik {#adaptivity}
Dörtgen yoğunluğunu eğriliğe uyarlar. 0 eşit boyutlu dörtgenler, 1 kavisli bölgelerde daha küçük dörtgenler üretir.

##### Anizotropi {#anisotropy}
Dörtgenleri yüzeyin en düz olduğu yön boyunca uzatır. 0 kare dörtgenler, 1 tüplerde ve sırtlarda uzun dörtgenler üretir.

##### Keskin kenar {#sharp-edge}
Bu açıdan daha fazla bükülen kenarlar keskin detay olarak korunur.

##### Normalleri yumuşat {#smooth-normal}
0, yeniden örgüleme sırasında yüzeyi köşeli (fasetli) tutar. Yüksek değerler verteks normallerini hesaba katarak yüzeyi yumuşatır.

##### Maksimum delik doldurma {#autoremesher-max-fill-hole}
Algoritma bazen istenmeyen delikler üretebilir. Bir deliğin verteks sayısı bu değerden azsa delik doldurulur.

### Instant Mesh {#quad-remesh-instant}
[Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung tarafından geliştirilen Instant Meshes algoritmasıyla](https://igl.ethz.ch/projects/instant-meshes/) yeniden örgüler. Ağın akışını analiz eder ve temiz bir dörtgen topoloji oluşturur.

#### Yeniden ağ örgülendirme {#instant-remesh}
Yeniden örgüleme işlemini başlatır.

#### Hedef dörtgenler {#target-quads}
Yeniden örgüleyicinin oluşturmaya çalışacağı dörtgen poligon sayısı.

#### ![](/icons/cog.webp) Instant Mesh dişli menüsü {#quad-remesh-instant-gear-menu}
Dişli menüsünde şu gelişmiş seçenekler bulunur:

##### Kırışık açısı {#crease-angle}
Yeniden örgüleme işlemine yön vermeye yardımcı olan keskin köşe eşiği. Onay kutusuyla etkinleştirin.

##### Maksimum delik doldurma {#max-fill-hole}
Algoritma bazen istenmeyen delikler üretebilir. Bir deliğin verteks sayısı bu değerden azsa delik doldurulur.

### QuadriFlow {#quadriflow}
Temiz bir dörtgen düzeni elde etmenin başka bir yolu olan QuadriFlow algoritmasıyla yeniden örgüler.

#### ![](/icons/cog.webp) QuadriFlow dişli menüsü {#quadriflow-gear-menu}
Dişli menüsünde şu gelişmiş seçenekler bulunur:

##### Sınırı koru {#quadriflow-preserve-boundary}
Delik sınırlarını korur.

##### Keskinliği koru {#keep-sharp}
Dörtgenleri yüzeyin keskin kenarlarıyla hizalar.

##### Minimum maliyetli akış {#min-cost-flow}
Dörtgen düzeni için minimum maliyetli akış çözücüsü kullanır. Daha yavaştır ama daha düzenli bir topoloji üretebilir.

## ![](/icons/uv.webp) UV Açma {#uv-unwrap}
Seçili nesne için doku koordinatlarını (UV) hesaplar. Nomad'da her biri kendi `Aç` düğmesine sahip iki yöntem vardır: `UVAtlas` ve `BFF`.

![](/videos/unwrap.mp4)

::: tip UV mi?
UV'ler için yaygın bir benzetme hediye paketlemektir: bir nesneyi hiç üst üste bindirmeden tamamen kaplamak için ambalaj kâğıdını en iyi nasıl kesersiniz? 

UV'ler de buna benzer, ama kâğıdı kesmek yerine nesneyi kesersiniz. Modelinizin ince plastikten yapıldığını düşünün: onu düz yatacak şekilde açmak, bu düz hâlde üzerine boyamak ve sonra yeniden birleştirmek için nereden keserdiniz?

Şimdi de modelinizin yüzeyinin esnek likradan yapıldığını düşünün. Modeli gererek düzleştirebilir, kesebilir ya da ikisini birlikte yapabilirsiniz. Ama düzleştirilmiş nesneye bir dama tahtası çizerseniz, yeniden birleştirdiğinizde dama tahtası bozulur. Hangisi daha iyi: daha çok kesik ve daha az bozulma mı, yoksa daha az kesik ve daha çok bozulma mı?

UV'ler, doku uygulanırken nesnenin nasıl 'kesilip gerileceğini' 3d yazılıma anlatan talimatlardır. UV Atlas aracı genellikle 'daha çok kesik, daha az bozulma' yaklaşımını benimser.


:::

::: tip UV'ler, Nomad ve diğer uygulamalar

İnternette bulduğunuz dokulu modellerin çoğu UV'lerle dokulanmıştır. Nomad bunları içe aktarıp [malzeme](material.md#textures) panelinde gösterebilir.

Modeller Nomad'da yapıldığında, UV olmadan doğrudan nesnelerin üzerine boyama yapabilirsiniz. Bunları başka uygulamalara, örneğin [Procreate](https://procreate.art/)'e aktarmanız gerekirse, Nomad'ın renk bilgisini UV'ler aracılığıyla dokulara 'pişirebilirsiniz'. 

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
UVAtlas, bozulmayı en aza indirmek için genellikle kesiklerle daha fazla ada oluşturmayı tercih eder.

#### Aç {#unwrap}
Seçili nesne için UV'leri hesaplar.

#### Seçenekler {#uvatlas-gear-menu}
`Aç` düğmesinin yanındaki düğmeler:

##### Yüz Grubu {#atlas-face-group}
`Evet` gösterdiğinde, UV kesiklerini yüz grupları belirler. Bu ayar BFF ile ortaktır.

##### UV'leri sil {#delete-uvs}
Çöp kutusu düğmesi nesnenin UV'lerini siler.

##### Denetle {#uv-inspect}
Nesnenin UV'lerini arka planda gösterir.

#### Maks. Esneme {#max-stretch}
Düşük değerler daha az bozulma ve daha çok ada, yüksek değerler daha çok bozulma ve daha az ada oluşturur. 

#### Ada Aralığı {#island-spacing}
Adalar arasındaki boşluk miktarı. Düşük değerler daha az alan harcar, ama dokuların adalar arasında taşma riskini artırır. 

::: warning
UV hesaplamak biraz zaman alabilir; ağın 100k'den az verteksi olması en iyisidir.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

BFF UV'leri 'daha az kesik, daha çok bozulma' yaklaşımını tercih eder. 

#### Seçenekler {#uv-bff-gear-menu}
`Aç` düğmesinin yanında [UVAtlas](#uvatlas-gear-menu) ile aynı `Yüz Grubu`, silme ve `Denetle` düğmeleri bulunur.

##### Yüz Grubu {#bff-face-group}

UV kesiklerini belirlemek için yüz gruplarını kullanır.

#### Koni sayısı {#cone-count}
Kullanılan ana izdüşüm sayısını belirler. Düşük değerler daha az ada ama daha çok bozulma üretir. Yüksek değerlerin hesaplanması daha uzun sürer.

#### Dikişsiz yamalar {#seamless-patches}
UV yamalarının yerleşimini etkiler; ciddi bozulmalara yol açabilir. Özenle oluşturulmuş yüz gruplarıyla en iyi sonucu verir.

::: warning
Ağda kulplar varsa (simidin deliği gibi) BFF üst üste binen UV'ler oluşturabilir.
:::

### ![](/icons/preview.webp) Açma işleminden sonra UV’yi göster {#show-uv-after-unwrap}
Açma işleminden sonra UV denetleyici görünümünü açar, böylece sonucu hemen kontrol edebilirsiniz.

### ![](/icons/bake.webp) Pişir: Doku → Doku {#unwrap-bake-texture}
Yalnızca nesnenin malzemesinde doku varsa kullanılabilir. Nesneyi yeniden açtığınızda dokular yeni UV'lere aktarılır, böylece yine doğru oturur. Çözünürlüğü varsayılan olarak en büyük dokuya uyan `Otomatik` değeridir, isterseniz kendiniz de ayarlayabilirsiniz.

## ![](/icons/bake.webp) Pişir {#bake}
Bu sekme detayları ve boyamayı nesneler arasında, ayrıca verteksler ile dokular arasında aktarır.

`Yüksek çözünürlüklüden` kaynak olarak diğer nesneleri kullanır; parantez içindeki sayı kaç nesne olduğunu gösterir. Nomad bunları şöyle seçer:

- seçili tüm nesneler kullanılır ve ana seçili nesne hedeftir ([Sahne](scene.md) menüsünde en belirgin şekilde vurgulanan)
- yalnızca bir nesne seçiliyse, Nomad bunun yerine görünür tüm nesneleri kullanır
- diğer tüm nesneler gizliyse (örneğin Solo ile), sahnenin tamamı kullanılır

### ![](/icons/bake.webp) Pişir → Doku {#bake-texture}
![](/images/topology_bake_menu.webp)

Doku pişirme, sahnedeki diğer görünür nesneleri seçili nesnenin UV'lerine yansıtarak dokular oluşturur. Nesnenin UV'si olması gerekir.

Tipik bir pişirme süreci şöyledir:
- İnce detaylı ve boyanmış bir ağınız var
- Klonlayın
- Azaltın (`Boyamayı koru` değerini 0'a ayarlayın)
- UV'lerini açın
- Pişirin!

Artık önceki nesnenizin boyamasının ve detaylarının çoğunu koruyan düşük çözünürlüklü bir ağınız olmalı.

İşlemden sonra verteks renkleri, dokularla karışmamaları için devre dışı bırakılmış yeni bir katmana taşınır.

#### Kendisinden {#tex-from-itself}
Nesneyi kendi UV'lerine pişirir: boyaması dokulara dönüşür ve çoklu çözünürlük seviyeleri varsa en yüksek seviyenin detayları mevcut seviyeye pişirilir (bu durumda düğmede bir çoklu çözünürlük simgesi görünür). Kurulumu basittir, ama çoğu zaman daha fazla kontrole ihtiyaç duyarsınız; o durumda bir sonraki seçenek daha kullanışlıdır.

#### Yüksek çözünürlüklüden {#tex-from-high-res}
Diğer nesnelerden seçili nesneye pişirir. Parantez içindeki sayı, yüksek çözünürlüklü kaynak olarak kullanılacak ve mevcut düşük çözünürlüklü, UV'li nesneye pişirilecek diğer nesnelerin sayısını gösterir. Diğer nesnelerin, pişirilen nesneyle benzer bir yerleşime veya topolojiye sahip olması gerekmez; bu da çok yönlü pişirme süreçlerine olanak tanır.

#### Çözünürlük {#tex-bake-resolution}
Pişirilen dokunun çözünürlüğü. Pişirilen dokular her zaman karedir, yani 1024 değeri 1024x1024 bir görüntü oluşturur. 

Alttaki düğmeler sık kullanılan çözünürlükler için kısayollardır. Fikir vermesi açısından 512x512 oldukça küçüktür, örneğin web grafikleri ve basit geometri için. 4096x4096 (kısaca 4k) yüksek kaliteli render'lar içindir.

#### Renk, Pürüzlük, Metaliklik seviyesi, Normal, Yer Değiştirme, Yayıcı, Opaklık {#tex-normal-roughness-metalness-color-emissive-opacity}
Bu düğmeler hangi özelliklerin pişirileceğini belirler; her biri ayrı bir haritaya pişirilir. Pişirme bittiğinde bunlar mevcut nesnenin malzemesine doku olarak eklenir. `Yer Değiştirme`, detayların yüksekliğini bir yer değiştirme haritası olarak pişirir.

#### ![](/icons/cog.webp) Pişir dişli menüsü {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Dişli menüsünde şu gelişmiş seçenekler bulunur:

##### Yedekle {#tex-backup}
Pişirilen dokuları önizlemek için nesnenin boyama bilgisinin devre dışı bırakılması gerekir. `Yedekle (Boyama → Katman)`, tüm boyama bilgisini yedek olarak yeni bir katmana aktarır; böylece kolayca açılıp kapatılabilir.

##### Çoklu çözünürlük kullan {#tex-use-multires}
Çoklu çözünürlük seviyeleri olan bir nesnede `Kendisinden` için. Nomad yüksek çözünürlüğü ışın göndermek yerine alt bölümleme seviyeleri üzerinden okur: daha hızlıdır ve izdüşüm hatası içermez. Aşağıdaki seçeneklerle pişirmek için kapatın.

##### Yumuşak taban {#tex-smooth-base}
Çoklu çözünürlük seviyeleri olan bir nesnede `Yer Değiştirme` için. Yer değiştirmeyi düz yüzlerden değil, alt bölümlenmiş tabandan ölçer. Yer değiştirme haritası Blender'ın uyarlamalı alt bölümlemesi gibi alt bölümlenmiş bir ağda kullanılacaksa açık tutun.

##### Arama mesafesi {#tex-cage-radius}
Kaynak yüzeyi bulmak için kullanılan en büyük mesafe. Kusurları önlemek için bu mesafe varsayılan olarak düşük tutulur, ancak hedef nesneler pişirilen nesneden uzaktaysa artırılabilir.

##### Projeksiyon {#tex-projection}
Kaynak yüzeyin nasıl bulunacağı:

* `Işın` - Yüzey normali boyunca yansıtır.
* `Işın + en yakın` - Normal ışınını kullanır, ışın ıskalarsa en yakın yüzeyi kullanır.
* `En Yakın` - Kaynak yüzeydeki en yakın noktaya yansıtır.

##### Işın ofseti {#tex-ray-offset}
Pişirme hesaplamalarının pişirilen nesne üzerinde nereden başlayacağını ayarlar. Yüzeyden küçük bir ofset en yaygın kusurları önler. Hedef nesneler pişirilen nesneden çok uzaktaysa bu ofsetin artırılması gerekebilir. `En Yakın` tarafından kullanılmaz.


### ![](/icons/bake.webp) Tekrar Projelendir → Verteks {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Şekillendirilmiş detayları, boyamayı, katmanları ve dokuları verteks değerlerine yansıtır.

Pişirmenin tersi olarak düşünülebilir: pişirme verteks özelliklerini dokulara aktarıyorsa, tekrar projelendirme de dokuları (ve diğer özellikleri)
 vertekslere geri aktarır.

::: tip
`Pişir → Doku` veya `Tekrar Projelendir → Verteks` kullanırken hem verteks renkleri hem de malzeme dokuları hesaba katılır.
:::

#### Kendisinden {#vertex-from-itself}
Malzemedeki dokuları verteks değerlerine dönüştürür. Bu düğme yalnızca nesnenin UV'si varsa ve malzemede dokular etkinse aktiftir.

::: tip İPUCU: Doku boyama
Nomad dokuları doğrudan boyamayı ve düzenlemeyi desteklemez, ancak dokuları verteks değerlerine yansıtıp vertekslerin üzerine boyayarak ve ardından verteksleri dokulara pişirerek çok benzer sonuçlar elde edebilirsiniz:

1. UV'leri olan düşük poligonlu bir nesne hazırlayın
1. Malzemesine dokuları yükleyin
1. Üzerine boyama yapabilecek kadar alt bölümlere ayırın
1. `Kendisinden` modunda `Tekrar Projelendir → Verteks` yapın; doku artık verteks değerlerine dönüştürülmüştür
1. Boyayın, yumuşatın, sürükleyin, damgalayın, ne düzenleme gerekiyorsa yapın
1. `Kendisinden` modunda `Pişir → Doku` yapın. Bu düzenlemeler yeniden dokulara dönüştürülür.
:::

#### Yüksek çözünürlüklüden {#vertex-from-high-res}
Diğer nesneleri seçili nesnenin verteks değerlerine dönüştürür. Bu düğmedeki sayı kaynak nesne sayısını gösterir. Bu çoğunlukla, yine yüksek çözünürlüklü ve genellikle temiz topolojiye sahip bir ağ üzerinde kullanılmak içindir.

::: tip
Diğer nesneleri tekrar projelendirme yalnızca renk bilgisini aktarmak için değil, verteksleri diğer nesnelerin üzerine yansıtmak için de kullanılabilir; örneğin bandajlar bir karakterin üzerine yansıtılabilir.
:::

#### Verteksler, Renk, Pürüzlük, Metaliklik seviyesi, Opaklık, Maske, Katmanlar, Yüz Grubu {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Bu düğmeler hangi özelliklerin seçili nesneye yansıtılacağını belirler. `Katmanlar`, diğer katmanları seçili ağa aktarır.

#### ![](/icons/cog.webp) Tekrar Projelendir dişli menüsü {#vertex-reproject-gear-menu}
Dişli menüsünde şu gelişmiş seçenekler bulunur:

##### Opaklık → Maske {#vertex-opacity-to-mask}
Kaynağın opaklığını seçili nesnede maskeye dönüştürür.

##### İterasyonlar {#vertex-iterations}
Tekrar projelendirme sırasında rahatlatma işleminin kaç kez uygulanacağı. Yalnızca `Verteksler` açıkken kullanılır.

##### Rahatlat {#vertex-relax}
Seçili ağın yerleşimi, yansıtma hedeflerine daha iyi uyması için belirli bir miktar yumuşatılabilir veya rahatlatılabilir. `Yumuşak` yüksek poligonlu ağlar için, `Rahatlat` düşük poligonlu ağlar için daha iyidir. `Otomatik` en iyi yöntemi Nomad'ın belirlemesine izin verir.

##### Arama mesafesi {#vertex-cage-radius}
Kaynak yüzeyi bulmak için kullanılan en büyük mesafe. Kusurları önlemek için bu mesafe varsayılan olarak düşük tutulur, ancak hedef nesneler seçili nesneden uzaktaysa artırılabilir.

##### Projeksiyon {#vertex-projection}
Kaynak yüzeyin nasıl bulunacağı:

* `Işın` - Yüzey normali boyunca yansıtır.
* `Uyarlanabilir karışım` - Normal ışınını ve en yakın yüzeyi mesafeye ve `Işın tercihi` değerine göre karıştırır. Biri ıskalarsa diğerini kullanır.
* `En Yakın` - Kaynak yüzeydeki en yakın noktaya yansıtır.

##### Işın tercihi {#vertex-ray-bias}
Yalnızca `Uyarlanabilir karışım` için. Yüksek değerler karışımı normal ışınının sonucuna, düşük değerler en yakın noktaya doğru dengeler.

##### Işın ofseti {#ray-vertex-offset}
Pişirme hesaplamalarının seçili nesne üzerinde nereden başlayacağını ayarlar. Yüzeyden küçük bir ofset bazı kusurları önler. Hedef nesneler pişirilen nesneden çok uzaktaysa bu ofsetin artırılması gerekebilir. `En Yakın` tarafından kullanılmaz.

### ![](/icons/bake.webp) Pişir → VDM {#bake-vdm}
Seçili nesneden bir VDM (vektör yer değiştirme) damgası oluşturur ve VDM kitaplığına ekler. Sizden bir isim istenir.

Tipik süreç şöyledir:
- Bir düzlem ekleyin ya da hazır ayarlanmış bir düzlem eklemek için VDM seçicide `Yeni VDM` seçeneğini seçin ([VDM](scene.md#add-menu) primitifi)
- Kenarını düz tutarak şeklinizi üzerine şekillendirin
- Pişirin!

Pişirilen kareyi düzlemin UV'leri belirler, bu yüzden nesnenin UV'si olması gerekir. Damga boyutunu `Çözünürlük` ile seçin; damganın yer değiştirmenin yanında neleri taşıyacağını da `Renk`, `Pürüzlük`, `Metaliklik seviyesi` ve `Opaklık` ile belirleyin.

::: tip
Düzlemde DinTopo kullanmaktan kaçının; UV'lerini bozar ve damga çarpık çıkar. Bir katmanda şekillendirmek en doğru sonucu verir, çünkü düz düzlem altta olduğu gibi durur. Boyama için de bir katman gerekir, aksi halde malzeme yalnızca boyadığınız yere değil, karenin tamamına damgalanır.
:::

## ![](/icons/dot.webp) Primitif {#primitive}
Seçili primitifin parametreleri. Bunların çoğuna primitif görünüm araç çubuğundaki `…` düğmesinden de ulaşılabilir.

![](/images/topology_primitive_screenshot.webp)
