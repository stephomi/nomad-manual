# ![](/icons/scene.webp) Sahne {#scene}

Bu menü, Nomad'daki nesneleri, ışıkları, kameraları ve tekrarlayıcıları yönetmenizi sağlar. Sahne hiyerarşisini bir ağaç görünümü olarak gösterir ve nesnelerinizin birçok özelliğini değiştirmenize olanak tanır. Ayrıca yeni nesneler oluşturmanızı, nesneleri çeşitli şekillerde birleştirip ayırmanızı da sağlar.


![](/images/scene_menu_summary.webp)


## Kısayol çubuğu {#shortcut-bar}
| İşlem                  | Simge                             | Açıklama                                                                                                            |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Ekle...](#add-menu)   | ![](/icons/plus.webp)            | Sahneye nesne eklemek için [Ekle menüsünü](#add-menu) gösterir                                                      |
| Sil                    | ![](/icons/trash.webp)           | Seçili nesneleri siler. Alt öğeleri korunur.                                                                        |
| Kilitle                | ![](/icons/lock.webp)            | Seçili nesneleri görünümde seçilemez hâle getirir. Ağaç görünümünden yine de seçilebilirler. Bir grubu kilitlemek altındaki her şeyi kilitler. Kilidi açmak için tekrar dokunun. |
| [Birleştir](#join)     | ![](/icons/merge.webp)           | Seçili nesneleri, geometrilerini değiştirmeden tek bir nesnede birleştirir                                          |
| [Ayır...](#separate)   | ![](/icons/separate.webp)        | Bir nesneyi birkaç nesneye bölmek için [Ayır](#separate) penceresini gösterir. Birleştirme işleminin tersidir       |
| [Boolean...](#boolean) | ![](/icons/bool_subtract_circle.webp) | [Boolean](#boolean) penceresini gösterir                                                                       |
| Klonlama               | ![](/icons/clone.webp)           | Seçili nesneleri yeni nesneler olarak çoğaltır                                                                      |
| Örnek                  | ![](/icons/link.webp)            | Seçili nesneleri örnek olarak çoğaltır; böylece birinde yapılan modelleme değişiklikleri tüm örneklere uygulanır.   |
| Örneklemeyi kaldır     | ![](/icons/unlink.webp)          | Bir örneği benzersiz bir şekle dönüştürür; böylece modelleme değişiklikleri artık diğer örneklere kopyalanmaz       |
| Senkronize             | ![](/icons/checked.webp)         | İşaretliyken işlemler yalnızca seçili nesnelere değil, seçili nesnelerin tüm örneklerine uygulanır. Yalnızca seçimde örnekler varken kullanılabilir. Hangi işlemlerin bu onay kutusunu izleyeceğini `Gelişmiş` penceresinin [Senkronize sekmesi](#sync) belirler. |

::: tip
Bir işlem diğer örnekleri de etkileyecekse düğmesinde küçük bir bağlantı simgesi görünür.
:::


## Ağaç görünümü {#tree-view}
![](/images/scene_treeview.webp) 

Ağaç görünümü sahnedeki nesneleri, grupları, tekrarlayıcıları, ışıkları ve kameraları listeler. Bir ağın adının yanında verteks sayısını, katmanları varsa renkli bir katman simgesini görürsünüz. Her satırda şu düğmeler bulunur:

| İşlem        | Simge                      | Açıklama                 |
| :----------: | :------------------------: | :----------------------: |
| İsim         | ![](/icons/pencil.webp)   | Nesneyi yeniden adlandırır. Nesne seçiliyse tüm seçili nesneler, sonlarına bir numara eklenerek tek seferde yeniden adlandırılır. Alt öğeleriyle birlikte yeniden adlandırmak için uzun basın. |
| Seç          | ![](/icons/checked.webp)  | Seçili/seçili değil arasında geçiş yapar |
| Görülebilir  | ![](/icons/eye_open.webp) | Görünürlüğü açıp kapatır |
| Menü         | ![](/icons/more.webp)     | [Nesne menüsünü](#object-menu) gösterir |

::: tip İPUCU: Çok sayıda nesneyi hızlıca seçin veya gizleyin

Tek bir nesneyi seçmek veya seçimini kaldırmak için seçim simgesine dokunun ya da birçok nesneyi seçmek için seçim sütununda dikey olarak sürükleyin. Aynısı görünürlük sütununda da yapılabilir.

Alt öğeleri de etkilemek için seçim veya görünürlük simgesine uzun basın.

:::

### Ağaç görünümü başlığı {#tree-view-header}

Listenin üstündeki satırda birkaç yardımcı düğme bulunur:

* ![](/icons/sort_down.webp) - tüm grupları tek seferde daraltır veya genişletir.
* ![](/icons/preview.webp) - listedeki her nesne için küçük bir render önizlemesi olan `Nesne önizlemeleri` seçeneğini açıp kapatır.
* ![](/icons/search.webp) - listeyi ada göre filtreler.

### Ağaç görünümünde düzenleme {#tree-view-manipulation}

Ağaç görünümündeki bir öğeye, vurgulanana kadar uzun basın. Ardından onu ağaç görünümünde yukarı veya aşağı taşıyabilir, ya da başka bir öğenin üzerine sürükleyerek o öğenin alt öğesi yapabilirsiniz.

Birden fazla öğe seçiliyken bunlardan biri ana seçimdir ve daha parlak görünür. Seçili nesnelerin hepsini birden taşımak için bunlardan birine uzun basıp sürükleyin.

Bir üst öğeyi seçtiğinizde, varsayılan olarak tüm alt öğeleri de seçilir. Üst öğeye tekrar dokunmak, yalnızca üst öğeyi seçmek ile üst öğeyi alt öğeleriyle birlikte seçmek arasında geçiş yapar.

Kamerayı bir öğeye odaklamak için ona çift dokunun (bkz. [Gelişmiş](#focus-on-item)).

### Nesne menüsü {#object-menu}

Ağaç görünümünde bir nesnenin üç nokta düğmesine (...) tıklamak nesne menüsünü gösterir. 
Bu seçeneklerin birçoğu, kolaylık olsun diye tekrarlanan, üstteki kısayol çubuğundakilere benzer.

|        İşlem              |                        Simge                       | Açıklama                                                                                                                                                                |
| :-----------------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        İsim               |              ![](/icons/pencil.webp)           | Nesnenin adını değiştirir                                                                                                                                               |
|   Örneklemeyi kaldır      |              ![](/icons/unlink.webp)           | Bir örneği benzersiz bir şekle dönüştürür; böylece modelleme değişiklikleri artık diğer örneklere kopyalanmaz.                                                          |
|        Örnek              |               ![](/icons/link.webp)            | Nesneyi örnek olarak çoğaltır; böylece birinde yapılan modelleme değişiklikleri tüm örneklere uygulanır.                                                                |
|        Klonlama           |              ![](/icons/clone.webp)            | Nesneyi yeni bir nesne olarak çoğaltır                                                                                                                                  |
|        Sil                |              ![](/icons/trash.webp)            | Nesneyi siler. `Alt öğeler` işaretli değilse alt öğeleri korunur.                                                                                                       |
|      Alt öğeler           |            ![](/icons/hierarchy.webp)          | İşaretliyken `Örnek`, `Klonlama` ve `Sil` nesnenin alt öğelerine de uygulanır.                                                                                         |
|  Parçalara göre Ayır      |             ![](/icons/separate.webp)          | Bir nesne birbirine bağlı olmayan parçalardan oluşuyorsa, her biri için ayrı bir nesne oluşturur. Birleştirme işleminin tersidir.                                       |
|  Gruplara göre Ayır       |            ![](/icons/group.webp)          | Bir nesnenin birden fazla yüz grubu varsa, her yüz grubu için ayrı bir nesne oluşturur.                                                                                    |
|  Katmanlara göre Ayır     |              ![](/icons/layer.webp)            | Bir nesnenin katmanları varsa, temel ağ ve her katman için ayrı nesneler oluşturur. Blendshape'leri başka uygulamalara göndermek için kullanışlıdır.                    |
|  Birleştir → Katmanlar    | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Birden fazla nesne seçiliyse ve topolojileri eşleşiyorsa, bu nesneleri ana nesnenin katmanları olarak birleştirir (diğer nesneler silinir). Bu da başka uygulamalardan GELEN blendshape'ler için kullanışlıdır.<br><br> Katmanların varsayılan olarak devre dışı olacağını unutmayın. Kaydırıcılarını ayarlamanız gerekirse onları etkinleştirin. |
|  Eğri (Tekrarlayıcı)      |              ![](/icons/curve.webp)            | Yalnızca tüp veya torna için: aynı eğriyi takip eden bir [Eğri](#curve) tekrarlayıcısını nesnenin alt öğesi olarak ekler.                                             |
|        Tüp                |             ![](/icons/tube.webp)              | Torna için, profilini takip eden bir [tüpü](tools.md#tube) alt öğe olarak ekler. Silindir, koni veya torus için ise onu aynı şekle sahip bir tüpe dönüştürür, böylece bir eğri boyunca bükebilirsiniz. |




### Çoklu seçim {#multiselection}
Birden fazla nesne seçmek iki şey için işinize yarar:
- gizmo aracıyla birkaç nesneyi aynı anda taşımak
- nesneleri birleştirme ve boolean işlemleriyle bir araya getirmek.

Ağaç görünümünde her nesnenin seçim simgesine dokunun ya da seçim sütunu boyunca sürükleyin. İsimlere dokunurken, tek bir nesne eklemek veya çıkarmak için `Maske` kısayolunu (klavyede `Ctrl`) basılı tutun; mevcut nesne ile dokunduğunuz nesne arasındaki tüm nesneleri seçmek için ise `Pürüzsüzleştir` kısayolunu (veya `Shift`) basılı tutun.

::: tip Hızlı çoklu seçim
Görünümde de `Pürüzsüzleştir` kısayolunu (veya `Shift`) basılı tutup başka bir ağa dokunarak çoklu seçim yapabilirsiniz.

Bir nesnenin seçimini, ona tekrar dokunarak kaldırabilirsiniz (yalnızca seçiminizde birden fazla nesne varsa).
:::

Gizmo tüm seçili nesneleri birlikte taşır, bkz. [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Birleştir {#join}
Bu seçenek, seçili birden fazla nesneden tek bir nesne kaydı oluşturur.
[Kaynaştırma yarıçapından](#weld-radius) daha yakın olan noktalar ve UV'ler birleştirilir.

Videolu bir örneği [Ayır](#separate) bölümünde görebilirsiniz.

## ![](/icons/bool_subtract_circle.webp) Boolean {#boolean}
![](/images/scene_boolean_menu.webp) 
Nesneleri tek bir yüzeyde birleştirir.

`Voksel birleşimi` nesnelerin hacmini korur ve yüzeyde eşit aralıklı yeni poligonlar hesaplar. Bu hesaplama adımı sayesinde voksel birleşimi karmaşık geometriyle başa çıkabilir, ancak hedef çözünürlük yeterince yüksek değilse ince detaylar kaybolabilir.

`Boolean` poligonları orijinal yerleşimlerinde bırakmaya çalışır ve nesnelerin kesiştiği yerlerde poligonları birbirine diker. Bu, voksel birleşiminden çok daha temiz ve keskin sonuçlar verebilir, ancak 'su geçirmez' ağlar gerektirir: nesnelerde delik veya bozuk şekiller olmamalıdır. Başarısız olursa genellikle voksel birleşimi işe yarar.

### Boolean işlemleri {#boolean-operations}
Hem Voksel birleşimi hem de Boolean, pencerenin altındaki hatırlatmaların da belirttiği gibi, işlemi kontrol etmek için nesnelerin görünürlüğünü kullanır:

#### Birleşim {#union}
İki nesne de görünürse boolean **birleşim** oluşur: nesnelerin dış yüzeyleri iç yüzey kalmadan birleştirilir. ![](/images/boolean_union.webp)

#### Çıkarma {#subtract}
Bir nesne görünmezse = boolean **çıkarma**: görünmez nesne görünür nesneden çıkarılır. ![](/images/boolean_subtract.webp)

#### Kesişme {#intersect}
İki nesne de görünmezse = boolean **kesişim**: yalnızca iki nesnenin üst üste bindiği yerde yeni bir şekil oluşturulur. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Voksel birleşimi {#voxel-merge-button}
Bu düğmeye basmak, seçili nesneler üzerinde bir voksel birleşimi işlemi yapar. Tek bir nesnede yapıldığında, nesneyi eşit aralıklı poligonlarla yeniden topolojilendirir; gerilmiş poligonları olan bir nesne için kullanışlıdır. Aşağıdaki seçenekler [Voksel](topology.md#voxel-remesher) sekmesindekiler gibi çalışır.

### Çözünürlük {#resolution}
Hesaplama için kullanılan 3d voksel ızgarasının çözünürlüğü. Bu değer değiştirildiğinde, poligonların boyutunu önizlemek için nesnenin üzerinde bir dama tahtası deseni belirir.

Kaydırıcının yanındaki seçici, detayı parmağınızın altındaki ağ yoğunluğundan alır. Onun yanındaki düğme kaydırıcıyı dünya birimiyle bir boyut olan `Kenar uzunluğu` değerine çevirir: aynı değer her nesnede aynı detayı verir.

### Çoklu çözünürlük oluştur {#build-multiresolution}
Hedef çözünürlüğünüzün altında çoklu çözünürlük seviyeleri oluşturur. Örneğin çözünürlüğünüz 400 ve çoklu çözünürlük oluşturma değeri 3 ise, diyelim 296.000 poligonlu yeni bir ağ elde edersiniz, ama bunun altında yaklaşık 74.000, 18.500 ve 4.600 poligonlu 3 alt bölümleme seviyesi daha olur.

### İnce kısımları kalınlaştır {#thicken-thin-parts}
Voksel ızgarası için fazla ince olan kısımları kalınlaştırır, böylece kopmazlar. `Keskin kenarlar` veya `Keskin sınır` ile birlikte kullanılamaz.

### Delikler {#holes}
Açık nesnelerdeki deliklerin birleştirmeden önce nasıl kapatılacağı:
* `Doldur` - her delik kendi sınırından başlanarak ayrı ayrı kapatılır.
* `Şekil` - delikler çevredeki yüzeyi takip ederek kapatılır ve üst üste binen açık parçalar birleştirilir.

### ![](/icons/angle.webp) Keskin kenarları koru {#keep-sharp-edges}
`Keskin kenarlar` düğmesi voksel ağını nesnelerin keskin kenarlarına yaslar. Basit şekillerde en iyi sonucu verir ve bazı bölgelerde bozulmalara yol açabilir.

### ![](/icons/group.webp) Keskin sınır {#sharp-border}
Yeni yüzler yüz grubu sınırlarını takip eder ve yüzeyin sınır boyunca kıvrıldığı yerlerde sınır keskin kalır.

### ![](/icons/group_separate.webp) Grupları ayrı tut {#keep-groups-separate}
Her yüz grubu kendi başına yeniden örgülenir: gruplar asla birleşmez ve her biri kendi grubunda kapalı bir parça olarak kalır. Bu modda çoklu çözünürlük oluşturulmaz.

### ![](/icons/bool_subtract_circle.webp) Boolean düğmesi {#boolean-button}
Bu düğmeye basmak, Emmett Lalish'in Manifold kitaplığını kullanarak poligon tabanlı bir boolean işlemi yapar. 

### ![](/icons/bool_unite_circle.webp) Çakışmaları Temizle {#clean-overlaps}
Yalnızca bir nesne seçiliyken `Boolean` düğmesi `Çakışmaları Temizle` olur: nesnenin birbirini kesen kısımlarını temiz bir yüzeyde birleştirir.

## ![](/icons/separate.webp) Ayır {#separate}
Birbirine bağlı olmayan birkaç parçadan oluşan tek bir nesneniz varsa, bu nesneyi birkaç nesneye ayırabilirsiniz. 
Bu, [Birleştir](#join) işleminin tersi olarak görülebilir.

`Ayır...` penceresi, seçili nesneleri ayırmanın üç yolunu sunar:
* `Parçalara göre Ayır` - bağlı olmayan her parça için ayrı bir nesne oluşturur.
* `Gruplara göre Ayır` - her yüz grubu için ayrı bir nesne oluşturur.
* `Katmanlara göre Ayır` - temel ağ ve her katman için ayrı nesneler oluşturur.

![](/videos/merge_separate.mp4)


## ![](/icons/plus.webp) Ekle menüsü {#add-menu}

![](/images/scene_addmenu_overview.webp)

Bu menü primitifler, gruplar, kameralar, tekrarlayıcılar ve ışıklar oluşturur.

Primitifler, parametrelerle ayarlanabilen temel şekil türleridir. Primitifi ihtiyaçlarınıza göre ayarladıktan sonra onu 'tamamlarsınız'; bu, parametreleri şekillendirilip boyanabilen bir poligon ağına dönüştürür. Bir primitif tamamlandıktan sonra parametreleri artık ayarlanamaz.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) Gizmo üzerinde {#on-gizmo}
Yeni primitifin, o anda seçili şeklin veya gizmonun bulunduğu yere yerleştirilmesini sağlar. Kapalıyken primitif sahnenin merkezine yerleştirilir.

### ![](/icons/gizmo.webp) Gizmo'yu seç {#select-gizmo}
Yeni bir primitif oluşturulduğunda otomatik olarak gizmo aracına geçilmesini sağlar. 

### ![](/icons/cog.webp) Gelişmiş {#add-advanced}

Bu menü, yeni primitiflerin, grupların ve tekrarlayıcıların nerede oluşturulacağını belirlemenizi sağlar. Seçili nesnenin üzerinde, dünyanın orijin noktasında veya gizmonun konumunda oluşturulabilirler.


### UV'ler {#uvs}
Primitif başlığının yanındaki `UV'ler` düğmesi primitiflerde UV'leri etkinleştirir. UV'ler (genellikle doku koordinatları olarak adlandırılır), 3d'de dokuların yüzeylere uygulanabilmesi için kullanılan ek verilerdir. Daha fazla bellek kaplarlar, ama çok yüksek poligon sayılarına (örneğin 10 milyon poligon veya daha fazlası) çıkmadığınız sürece çoğu cihazda bu sorun olmamalıdır. 

### Primitifler {#primitives}

| Primitif           | Simge                                     | Açıklama                                                                                                        |
| :----------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Küp                | ![](/icons/cube.webp)                    | Basit bir küp; X, Y ve Z yönündeki bölüm sayısını kontrol edebilirsiniz                                         |
| Dörtgen Küre       | ![](/icons/circle.webp)                  | `Küreye yansıt` seçeneği zorunlu olarak açık, alt bölümlenmiş bir küp; şekillendirmeye uygun, düzgün bir dörtgen yerleşimi vardır |
| Silindir           | ![](/icons/cylinder.webp)                | Silindir primitifine ortadan bir delik ekleyebilirsiniz, örneğin içi boş bir boru yapmak için                    |
| Torus              | ![](/icons/torus.webp)                   | Torus, yüzükler için iyi bir başlangıç noktası olabilir                                                          |
| Koni               | ![](/icons/cone.webp)                    | -                                                                                                               |
| İkosahedron        | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| UV Küre            | ![](/icons/circle.webp)                  | Düzensiz poligon yerleşimine sahip bir küre, bkz. [aşağıdaki uyarı](#uv-sphere)                                  |
| Düzlem             | ![](/icons/rectangle.webp)               | Basit bir düzlem; kapalı olmayan tek primitifin bu olduğunu unutmayın                                            |
| Metin              | ![](/icons/text.webp)                    | Yazı tipi, stil, hizalama, derinlik ve bükülme ayarlarıyla 3d metin. `Harfleri birleştir` birbirine değen harfleri kaynaştırır |
| Tüp                | ![](/icons/tube.webp)                    | bkz. [Tüp](tools#tube)                                                                                          |
| Torna              | ![](/icons/lathe.webp)                   | bkz. [Torna](tools#lathe)                                                                                       |
| Üç düzlemli        | ![](/icons/triplanar.webp)               | bkz. [Üç düzlemli](#triplanar)                                                                                  |
| VDM                | ![](/icons/vdm.webp)                     | Vektör yer değiştirme damgası şekillendirmek için hazırlanmış bir düzlem: UV'leri vardır ve kameraya bakar      |
| Gölge yakalayıcı   | ![](/icons/material_shadow_catcher.webp) | bkz. [Gölge yakalayıcı](#shadow-catcher)                                                                        |
| Kafa               | ![](/icons/face.webp)                    | Erkek/kadın arasında geçiş yapmak için bir katmanı olan basit bir kafa                                           |

::: tip
Nomad'ı açtığınızda gelen temel ağın ne olduğunu merak ediyorsanız: o da alt bölümlenmiş bir küptür.
Ancak Nomad'daki temel ağ `Küreye yansıt` seçeneğini kullanmaz, yani tam olarak yuvarlak değildir.
:::

### Primitif araç çubuğu {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

Bir primitif oluşturulduğunda, parametrelerini kontrol etmek için bir araç çubuğu belirir.

* `Tamamla` Primitifi şekillendirilip boyanabilen standart bir nesneye dönüştürür.
* `Aynala` Primitifin üstüne bir ayna tekrarlayıcısı yerleştirmeyi açıp kapatır.
* `Tümü` (göz simgesi) Parametreleri kontrol etmek için doğrudan primitifin üzerinde hangi tutamaçların gösterileceğini seçer (örneğin küpün genişliği veya silindirin delik yarıçapı): primitife göre `Yok`, `Tümü` ya da yalnızca bir tür (yarıçap, delik, profil...).
* `Bölüm` Primitifin bölüm sayısı, burada bir küp için X yönünde.
* `Sabit yoğunluk` Primitifi gizmo ile bir eksen boyunca gerdiğinizde poligonlar gerilmek yerine boyutu ve bölüm sayısı artar, böylece yüzler kare kalır. Küplerde, düzlemlerde ve silindirlerde kullanılabilir.
* `...` Primitif menüsünü gösterir.

Farklı primitiflerin araç çubuğunda ek seçenekler bulunur:

* `Küre` Küre, şekillendirmeye daha uygun olduğu için alt bölümlenmiş bir küp olarak oluşturulur, ancak bu tam olarak yuvarlak olmadığı anlamına gelir. Bu seçenek şekli kusursuz bir küreye yaklaştırır. İkosahedron da bu seçeneği paylaşır.
* `Kapak` Bir şeklin uç kapaklarını açıp kapatır; örneğin bir silindirin üstte, altta, her ikisinde de kapağı olabilir ya da hiç olmayabilir.
* `Delik` Bir şeklin ortasından geçen bir delik oluşturmayı açıp kapatır. Deliksiz, tek yarıçaplı delik ve üstte ve altta farklı yarıçaplı delik seçenekleri arasında geçiş yapar.
* `Yarıçap` Bir silindirin tek bir yarıçapa mı, yoksa üstte ve altta farklı yarıçaplara mı sahip olacağını belirler.
* `Disk` Bir düzlemin 4 kenarlı bir şekil mi, yoksa daire şeklinde mi olacağını belirler.

Ana araç çubuğunun altındaki küçük araç çubuğu, primitif gizmosu ile dönüştürme gizmosu arasında geçiş yapmanızı sağlar.

::: tip

Araç çubuğunun başlığına tıklamak onu ekranın üstüne veya altına taşır. Köşedeki oka tıklamak onu daraltır.

:::


### Primitif menüsü {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Bu menü seçili primitifin tüm parametrelerini içerir. Parametreler bir şeklin temel tanımlarıdır. Örneğin bir halkayı tanımlamak için dış yarıçapını, iç yarıçapını ve poligon sayısını belirtirsiniz.

Primitif parametrelerinin çoğu kendini açıklar niteliktedir; tüm primitiflerin paylaştığı bazı ortak parametreler de vardır:

* `UV'ler` Menünün üstündeki küçük UV'ler düğmesi UV koordinatlarının oluşturulmasını açıp kapatır
* `Tamamla` Küçük tamamla düğmesi primitifi şekillendirilip boyanabilen standart bir nesneye dönüştürür.
* `Maks yüz` Cihazınızın çökmesini önlemek için nesnedeki poligon sayısına bir üst sınır koyar.
* `İşlem sonrası altbölümleme` Topoloji menüsünün çoklu çözünürlük bölümünden seçilen sayıda alt bölümlemeyi uygular. Düşük topoloji bölümleriyle birlikte kullanıldığında yumuşatılmış, köşeleri yuvarlak primitifler yapmak için kullanılabilir. Örneğin bir küpün topoloji bölümlerini 2'ye, işlem sonrası alt bölümlemeyi 4'e ayarlamak köşeleri yumuşak bir küp oluşturur.
* `Lineer altbölümleme` Normal yumuşak alt bölümlemeye geçmeden önce kaç seviye lineer alt bölümleme kullanılacağını belirler. Alt bölümlenmiş yüzeylerde köşelerin ne kadar keskin veya yumuşak olacağını kontrol etmek için kullanılabilir. Örneğin bir küpün topoloji bölümlerini 2'ye, işlem sonrası alt bölümlemeyi 4'e ayarlayın, sonra lineer alt bölümlemeyi 0 ile 4 arasında değiştirmeyi deneyin. Küpün köşeleri yumuşaktan keskine doğru değişir.

### Topoloji {#topology}

Bir primitifteki poligon sayısını kontrol eder. Kontroller genellikle birbirine bağlıdır, yani etkin olan tek kaydırıcıyı değiştirmek tüm poligonları eşit şekilde ayarlar. Bağlantıyı kaldır düğmesine dokunarak bir şeklin X/Y/Z bölümlerini ayrı ayrı kontrol edebilirsiniz.

### Geometri {#geometry}

Bir primitifin genel boyutunu kontrol eder; köşeli şekiller için X/Y/Z birimleriyle, yuvarlak şekiller için yarıçapla.


### ![](/icons/circle.webp) UV Küre {#uv-sphere}
::: warning
UV Küre, özellikle kutuplarda şekillendirmeye pek uygun değildir.

Lütfen `Küreye yansıt` seçeneğiyle birlikte Dörtgen Küre, Küp veya İkosahedron [primitifini](#primitives) tercih edin.

`Bölüm` kaydırıcıları için çok düşük bir değer kullanırsanız topolojinin şekillendirme için kabul edilebilir olabileceğini unutmayın.
Ardından poligon sayısını artırmak için `Genel alt bölümleme` kaydırıcısını kullanabilirsiniz.

Genel şekillendirme için uygun olmasa da gözler için kullanışlıdır: küreyi kutuplar göz bebeğine denk gelecek şekilde döndürürseniz, poligon yerleşimi irisi ve göz bebeğini boyamaya ve şekillendirmeye doğal olarak uyar.
:::


### ![](/icons/triplanar.webp) Üç düzlemli {#triplanar}
Bu primitif özeldir: geometrisini şekillendirmek için üzerinde [Maske aracını](tools.md#mask) kullanmanız gerekir.

![](/videos/triplanar.mp4)


::: tip
Bir düzleme çift dokunduğunuzda kamera o düzleme odaklanır.
Ancak primitifi gizmo ile döndürdüyseniz bu çalışmaz.
:::

Üç düzlemli, 3 düzlemdeki maske bilgisini kullanarak bir voksel ızgarasını doldurur; bu ızgara daha sonra ([Voksel](topology.md#voxel-remesher) yeniden örgüleme sayesinde) poligonlara dönüştürülür.

Her düzlemin kendi simetri düzlemi vardır.

::: warning
Üç düzlemli primitifin boyutunu her güncellediğinizde maske boyamasının kalitesi düşer.

Şimdilik boyamayı tek bir düzlemde 'kilitlemek' için bir seçenek yok, ama belki ileride gelir.
Biraz yardımcı olması için [Bağlı topoloji](stroke.md#connected-topology) seçeneğini kullanabilirsiniz: imleciniz tam olarak bir düzlemin üzerindeyse diğer düzlemleri etkilemez.
:::

### ![](/icons/material_shadow_catcher.webp) Gölge yakalayıcı {#shadow-catcher}
Gölge yakalayıcı malzemesine sahip bir düzlem ekler. Daha fazla bilgi için [Gölge yakalayıcı malzemesi](material.md#shadow-catcher) bölümüne bakın. 


## Grup/Kamera {#groupcamera}
### ![](/icons/share.webp) Grup {#group}
Altına başka nesneler bağlayabileceğiniz 'boş' bir nesne oluşturur. Birçok nesneyi bir grubun altına koyup grubu kapatarak hiyerarşiyi düzenlemek için kullanılabilir. Grup, nesneleri taşımak için bir yardımcı olarak da kullanılabilir: birçok nesne bir grubun altına yerleştirilir, sonra grup gizmo aracıyla taşınır, döndürülür, ölçeklenir.

### ![](/icons/camera.webp) Kamera {#add-view}
Bir kamera oluşturur.

## Tekrarlayıcılar {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Tekrarlayıcılar, altlarındaki nesnelerin örneklerini oluşturan düğümlerdir. 

### ![](/icons/array.webp) Dizi {#array}
![](/images/scene_primitive_array.webp)

Bu düğümün alt öğesi yapılan nesneler bir ızgara düzeninde örneklenebilir. Seçiliyken şu kontrollere sahiptir:
* `İçine sığdır` - açıkken tüm kopyalar dizinin sınırları içine yerleştirilir; kapalıyken kaydırıcılar kopyalar arasındaki boşluğu belirler
* `Sayı X/Y/Z` - her eksendeki örnek sayısı
* `X/Y/Z Büyüklüğü` - ızgaranın her eksen boyunca boyutu, ya da `İçine sığdır` kapalıyken kopyalar arasındaki mesafe
* `Rastgeleleştir...` - kopyalara rastgele farklılıklar ekler, aşağıdaki [Rastgeleleştir](#curve) bölümüne bakın.

### ![](/icons/curve.webp) Eğri {#curve}
![](/images/scene_primitive_curve.webp)
Bir eğri oluşturur; bu düğümün alt öğeleri eğri boyunca tekrarlanır. Seçiliyken şu kontrollere sahiptir:
* `Eğri` - eğriyi düzenler: eğriye nokta ekleyin ve eğri üzerindeki noktaları taşıyın.
* `Göster` - eğriyi ve noktalarını gösterir veya gizler.
* `Yasla` - eğri noktalarını diğer geometriye yaslar.
* `Sim` - eğriyi simetrik olarak düzenler.
* `Kapalı` - eğrinin başlangıcını ve sonunu birleştirmek ile açık bir eğri olması arasında geçiş yapar.
* `B-spline` - örneklerin eğriyi tam olarak takip etmesi ile daha yumuşak sonuç veren b-spline enterpolasyonu kullanması arasında geçiş yapar.
* `Şekle uydur` - her kopyayı eğri boyunca büker, böylece kopyalar komşularıyla buluşur (`Yumuşak`, kenarlarını açı oluşturmadan buluşacak şekilde büker).
* `Hizala` - kopyaları eğrinin yönünü takip edecek şekilde döndürür.
* `Eksen` - kopyaların pivotu: eğrinin kendisi (`Eğrinin kendisi`) veya alt öğeleri.
* `Sayı` - örnek sayısı. Yanındaki mod düğmesi `Mesafe` moduna geçer: kopyalar arasında sabit bir aralık olur ve sayı eğrinin uzunluğuna göre belirlenir.
* `Yarıçap` - örneklerin ölçeğini ayarlamak için her eğri noktasındaki kontroller.
* `Kıvır` - örneklerin burulma dönüşünü ayarlamak için her eğri noktasındaki kontroller.
* `Dönüşümlü` - her iki kopyadan birini, seçtiğiniz `Eksen` etrafında eğrinin çevresinde döndürür: zincir halkaları için 90°, yapraklar veya fermuar dişleri için 180°.
* `Sarmal...` - kopyaları eğrinin etrafında birkaç tel hâlinde sarar (halat, örgü, şerit...).
* `Rastgeleleştir...` - kopyalara rastgele farklılıklar ekler; her satır bunun yerine her kopyaya aynı miktarı da ekleyebilir.

Araç çubuğunun altındaki `(Birleştir)` düğmesi, bir noktayı başka bir noktanın üzerine sürüklediğinizde ikisini birleştirir. `IK` (ters kinematik) eğriye poz vermenizi sağlar: bir noktayı sürükleyin, bağlı noktalar onu takip eder. Bir noktayı kilitlemek veya kilidini açmak için ona dokunun, hepsini kilitlemek veya kilidini açmak için uzun basın; kilitli noktalar yerinde kalır.

### ![](/icons/radial.webp) Radyal {#radial}
![](/images/scene_primitive_radial.webp)

Bu düğümün alt öğeleri bir daire üzerinde örneklenir. Bu tekrarlayıcının yarıçapını değiştirmek için alt nesneyi taşıyın. Seçiliyken şu kontrollere sahiptir:
* RadyalX/Y/Z - bu düğmeleri seçmek radyal ekseni belirler ve örnek sayısını ayarlar.



### ![](/icons/mirror.webp) Aynala {#mirror}
![](/images/scene_primitive_mirror.webp)

Bu düğümün alt öğeleri bir eksene göre aynalanır. Seçiliyken şu kontrollere sahiptir:
* Gizmo - aynanın merkezini ayarlamak için dönüştürme gizmosunu etkinleştirir. Gizmo döndürülebilir ve ölçeklenebilir de. İşiniz bitince standart kontrolleri yeniden görmek için tekrar gizmoya dokunun.
* X/Y/Z - ayna düzlemini belirler

### ![](/icons/surface.webp) Yüzey {#surface}

Bu düğümün alt öğeleri bir nesnenin yüzeyine kopyalanır: yüz başına, kenar başına veya verteks başına bir kopya ya da rastgele dağıtılmış olarak. Seçiliyken şu kontrollere sahiptir:
* Mod - kopyaları `Yüzler`, `Kenarlar` veya verteksler üzerine yerleştirir ya da `Dağıt` ile dağıtır.
* Her - her N yüz, kenar veya vertekste bir kopya. `Rastgele` bunun yerine rastgele seçer, `Karıştır` ise başka bir rastgele küme çeker.
* Aralık - dağıtırken iki kopya arasındaki en küçük mesafe.
* Hizala - kopyalar orijinalin yönünü korumak yerine yüzeyin normalini takip ederek yüzeyin üzerinde durur.
* Yakala - orijinali en yakın yüzey noktasına yansıtır, kopyalar da onu takip eder.
* Boyutu uydur, Yatır - kopyaları her yüzün şekline göre ölçekler ve gerer.
* Şekle uydur - her kopyayı yüzünün üzerine veya kenarı boyunca büker, böylece komşu kopyalar boşluk kalmadan buluşur.

Tüm tekrarlayıcıların bir `Tamamla` kontrolü vardır; bu, tekrarlayıcının sonucunu kalıcı hâle getirir ve bunun nasıl yapılacağını sorar:
* Alt öğeleri birleştir - örnekler tek bir nesnede birleştirilir
* Örnekleri Koru - örnekler örnek olarak kalır, ama artık tekrarlayıcı 'üst öğesi' yoktur
* Örneklemeyi kaldır - örnekler benzersiz nesnelere dönüştürülür

`Tümünü düzleştir` bunun içine yerleştirilmiş tekrarlayıcıları da kalıcı hâle getirir, böylece her kopya sıradan bir nesneye dönüşür.

::: tip İpucu: Tekrarlayıcıları birleştirin
Tekrarlayıcılar birbirinin altına bağlanabilir ve birkaç nesne tekrarlayıcıların alt öğesi yapılabilir; böylece karmaşık efektler elde edilir.

![](/images/scene_repeater_combine.webp)
:::

::: tip İpucu: Tekrarlayıcı pivotları

Bazı tekrarlayıcılar alt nesnelerin pivotunu otomatik ayarlamaya çalışır; bu yüzden onları gizmo aracıyla taşısanız veya döndürseniz bile hareket etmezler. Bu davranışı geçersiz kılmanız gerekirse, tekrarlayıcı ile alt öğe arasına bir grup ekleyin. Artık alt şekli tekrarlayıcıdan bağımsız olarak taşıyabilirsiniz.
:::

## Işık {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Yönsel {#directional}
Güneş gibi sonsuz uzaklıktaki bir ışık kaynağı olan yönsel bir ışık oluşturur.

### ![](/icons/panorama.webp) Ortam {#environment}
Sahneyi çevresini saran bir görüntüyle aydınlatan bir ortam ışığı oluşturur (HDRI gibi, görüntü tabanlı aydınlatma).

### ![](/icons/spotlight.webp) Spot {#spot}
Koni genişliği ve yumuşaklığı ayarlanabilen bir spot ışık oluşturur

### ![](/icons/light.webp) Nokta {#point}
Bir nokta ışık oluşturur

## ![](/icons/cog.webp) Gelişmiş {#advanced}
Panelin sol altındaki `Gelişmiş` düğmesi iki sekmeli bir pencere açar: `Genel` ve `Senkronize`.

### ![](/icons/focus.webp) UI: Çift dokunmada odaklan {#focus-on-item}
Sahne listesinde bir öğeye çift dokunmak, 3d görünümde kamerayı o öğeye ortalar.

### ![](/icons/eye_open.webp) Görünürlüğü Senkronize Et {#sync-visibility}
Açıkken, seçili bir öğenin göz simgesini kullanmak tüm seçili öğeleri etkiler. 

### ![](/icons/bang.webp) Vurgula {#highlight}
Seçim değiştiğinde seçili nesneleri görünümde vurgular.

### ![](/icons/link.webp) Göster (Örnek) {#instance-show}
Örnekleri belirtmek için sahne listesinin solunda renkli bir kapsül gösterir.

### ![](/icons/preview.webp) Nesne önizlemeleri {#object-previews}
Sahne listesindeki her nesne için bir render önizlemesi gösterir. Listenin üstündeki önizleme düğmesiyle aynıdır.

### Kaynaştırma yarıçapı {#weld-radius}
`Birleştir` başlığının altında `Pozisyon Kaynaştırma Yarıçapı` ve `UV Kaynaştırma Yarıçapı` bulunur: bu yarıçaplardan daha yakın olan noktalar ve UV'ler birleştirilir. Her biri kendi onay kutusuyla kapatılabilir. Bu; Birleştir, Boolean, Kes, Azalt, yeniden örgüleme ve dosya içe aktarma işlemleri için geçerlidir.

### Simgeler {#icons}
Görünümdeki grup, ışık, kamera ve tekrarlayıcı simgelerinin en küçük ve en büyük `Büyüklük` değerini ve `Opaklık` değerini ayarlar.

### ![](/icons/hierarchy.webp) Hiyerarşi çizgileri {#hierarchy-lines}
Görünümde bir üst öğe ile alt öğeleri arasında bir çizgi gösterir. Açıkken şunları da ayarlayabilirsiniz:
* `Nomad pivotunu kullan` - çizgiler Dönüştür ve Gizmo araçlarının kullandığı pivottan başlar. Kapalıyken nesnenin doğal temel pivotunu kullanırlar; bu pivot nesnenin merkezinden uzakta olabilir.
* `Kalınlık` - çizgilerin genişliği. Kaydırıcının yanındaki düğme çizgilere bir dış hat ekler.
* Çizgilerin rengi.

### ![](/icons/link.webp) Senkronize {#sync}
`Senkronize` sekmesi her işlem için (`Ekle`, `Sil`, `Kilitle`, `Klonlama`, `Örnek`, `Örneklemeyi kaldır`, `Birleştir`, `Ayır` ve `Boolean`) işlemin seçimin tüm örneklerine uygulanıp uygulanmayacağını belirler:
* `Otomatik` - sahne menüsünün üstündeki `Senkronize` onay kutusunu izler.
* `Hayır` - yalnızca seçili nesneler.
* `Evet` - her zaman tüm örnekler.

Varsayılan olarak `Birleştir`, `Ayır` ve `Boolean` `Evet`, diğerleri `Otomatik` durumundadır. `Sıfırla` bu varsayılanları geri getirir.

## Alt araç çubuğu {#bottom-toolbar}
Bu simgeler görünümde Grup, Işık, Kamera, Tekrarlayıcı ve Hiyerarşi çizgilerinin görünürlüğünü açıp kapatır. Tuvalde gösterilen simgelere dokunarak onları doğrudan seçip düzenleyebilirsiniz.
