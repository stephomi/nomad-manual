# ![](/icons/scene.webp) Sahne 

Bu menü, Nomad'da nesneleri, ışıkları, kameraları ve tekrarlayıcıları (repeater) yönetmenizi sağlar. Sahne hiyerarşisini ağaç görünümü olarak gösterir ve nesnelerinizin birçok yönünü değiştirmenize imkân tanır. Ayrıca yeni nesneler oluşturmanıza, nesneleri çeşitli şekillerde birleştirip ayırmanıza da olanak verir.


![](/images/scene_menu_summary.webp)


## Kısayol çubuğu
| Eylem                 | Simge                              | Açıklama                                                                                                           |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Ekle...](#add-menu)    | ![](/icons/plus.webp)            | Sahneye bir nesne eklemek için [Ekle Menüsü](#add-menu)'nü gösterir                                                 |
| Sil                 | ![](/icons/trash.webp)           | Nesneyi siler                                                                                                      |
| Kilitle                   | ![](/icons/lock.webp)            | Nesneyi görünüm penceresinde seçilemez yapar. Ağaç görünümünden hâlâ seçilebilir.                          |
| Birleştir                   | ![](/icons/merge.webp)           | Seçili nesneleri, geometrilerinde değişiklik yapmadan tek bir nesnede birleştirir                                             |
| Ayır               | ![](/icons/diagonal.webp)        | Bir nesne benzersiz çokgen kabuklardan oluşuyorsa, onu ayrı nesnelere böler. Birleştirme işleminin tersidir |
| [Boolean...](#boolean) | ![](/icons/subtract_circle.webp) | [Boolean](#boolean) menüsünü gösterir                                                                                |
| Kopya oluştur                  | ![](/icons/clone.webp)           | Nesnenin yeni bir kopyasını oluşturur                                                                              |
| Örnek (Instance)               | ![](/icons/link.webp)            | Nesneyi bir instance olarak çoğaltır; böylece birinde yapılan modelleme değişiklikleri tüm instance'lara uygulanır.                         |
| Instance kaldır            | ![](/icons/unlink.webp)          | Bir instance'ı benzersiz bir şekle dönüştürür; böylece modelleme değişiklikleri artık diğer instance'lara kopyalanmaz                 |
| Eşitle (Sync)                   | ![](/icons/link.webp)            | Instance'ların çocukları varsa, tüm instance'ların aynı çocuk hiyerarşisini paylaşmasını sağlar                                     |


## Ağaç görünümü
![](/images/scene_treeview.webp) 

| Eylem       | Simge                       | Açıklama              |
| :----------: | :------------------------: | :----------------------: |
| Seç       | ![](/icons/checked.webp)  | Seçili/seçili değil durumunu değiştir |
| Görünürlük      | ![](/icons/eye_open.webp) | Görünürlüğü değiştir        |
| Menü         | ![](/icons/more.webp)     | Nesne menüsünü göster      |

::: tip İPUCU: Birçok nesneyi hızlıca seçin veya gizleyin

Tek bir nesneyi değiştirmek için seçim simgesine dokunun veya seçim sütununda dikey sürükleyerek birçok nesneyi seçin. Aynısı görünürlük sütunu için de yapılabilir.

:::

### Ağaç görünümünü düzenleme

Ağaç görünümündeki bir öğeye uzun basın, sarıya dönene kadar bekleyin. Sonra onu ağaç görünümünde yukarı veya aşağı taşıyabilir, ayrıca başka bir öğenin üzerine sürükleyerek o öğenin çocuğu yapabilirsiniz.

Birçok öğe seçiliyken, çoğu koyu sarı, biri daha açık sarı olur. Tüm nesneleri bir kerede taşımak için açık sarı olana uzun basıp sürükleyin.

Bir üst (parent) öğeyi seçtiğinizde, varsayılan olarak tüm çocuk öğeler de seçilir. Üst simgesine dokunmak, yalnızca üstü veya üst ve çocukları seçme arasında geçiş yapar.

### Nesne menüsü

Ağaç görünümünde bir nesne için üç nokta (...) düğmesine tıklamak nesne menüsünü gösterir. 
Bu seçeneklerin çoğu, kolaylık olması için üstteki kısayol çubuğundakilere benzer.

|       Eylem        |                        Simge                        | Açıklama                                                                                                                                                             |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      Instance       |               ![](/icons/link.webp)            | Nesneyi bir instance olarak çoğaltır; böylece birinde yapılan modelleme değişiklikleri tüm instance'lara uygulanır.                                                                             |
|        Kopya        |              ![](/icons/clone.webp)            | Nesnenin yeni bir kopyasını oluşturur                                                                                                                                  |
|        İsim         |              ![](/icons/pencil.webp)           | Nesnenin adını değiştirir                                                                                                                                           |
|       Sil        |              ![](/icons/trash.webp)            | Nesneyi siler                                                                                                                                                       |
|       Sil+       |            ![](/icons/removeNode.webp)         | Nesneyi ve çocuklarını siler                                                                                                                                      |
|     Instance kaldır     |              ![](/icons/unlink.webp)           | Bir instance'ı benzersiz bir şekle dönüştürür; böylece modelleme değişiklikleri artık diğer instance'lara kopyalanmaz.                                                                    |
|  Topolojiyi ayır  |             ![](/icons/separate.webp)          | Bir nesne benzersiz çokgen kabuklardan oluşuyorsa, onu ayrı nesnelere böler. Birleştirme işleminin tersidir.                                                    |
| Yüz Grubunu Ayır |            ![](/icons/faceGroup.webp)          | Bir nesnede birden fazla yüz grubu varsa, ağı (mesh) ayrı nesnelere böler.                                                                                            |
|   Katmanları Ayır   |              ![](/icons/layer.webp)            | Bir nesnede katmanlar varsa, her katmanı ayrı bir nesneye böler. Blendshape'leri diğer uygulamalara gönderirken kullanışlıdır.                                                 |
|   Birleştir -> Katmanlar    | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Birden fazla nesne seçiliyse ve topolojileri eşleşiyorsa, bu nesneleri birincil nesne için katmanlar hâlinde birleştirir (diğer nesneler silinir). Yine, diğer uygulamalardan GELEN blendshape'ler için kullanışlıdır.<br><br> Katmanların varsayılan olarak devre dışı olacağını unutmayın. Kaydırıcılarını ayarlamanız gerekirse onları etkinleştirin. |




### Çoklu seçim
Birden fazla nesne seçerek iki şeyi daha kolay yapabilirsiniz:
- birden fazla nesneyi aynı anda taşımak için gizmo aracını kullanmak
- nesneleri birleştirme ve boolean işlemleriyle birleştirmek.

Bunu `Multiselection` (Çoklu seçim) onay kutusunu kullanarak ve ardından listede nesneye tıklayarak yapabilirsiniz.

::: tip Hızlı çoklu seçim
Görünüm penceresinde de `Smooth` kısayolunu basılı tutup başka bir ağa dokunarak çoklu seçim yapabilirsiniz.

Seçiminizde birden fazla nesne varsa, bir nesneye tekrar dokunarak onu seçimden çıkarabilirsiniz.
:::

::: warning Sınırlı gizmo özelliği
Çoklu seçim kullanırken, gizmo aracı her zaman maskelemeyi yok sayar.
Ayrıca X/Y/Z ölçekleme kaldırılır.

Bunun nedeni, çoklu seçimin yalnızca tüm ağı (mesh) dönüştürmeye izin vermesi, tepe noktası (vertex) bazlı dönüşüme izin vermemesidir.
Bu gelecekte geliştirilebilir.
:::


## Birleştir
Bu seçenek, birden fazla seçili nesneden tek bir nesne girdisi oluşturur.

[Ayır](#separate) bölümünde videolu bir örnek görebilirsiniz.

## Boolean
![](/images/scene_boolean_menu.webp) 
Nesneleri tek bir yüzeye birleştirir.

`Voxel merge` nesnelerin hacmini korur ve yüzeyde eşit aralıklı yeni çokgenler hesaplar. Hesaplama adımı nedeniyle voxel birleştirme karmaşık geometrileri kaldırabilir, ancak hedef çözünürlük yeterince yüksek değilse ince detaylar kaybolabilir.

`Boolean`, çokgenleri özgün yerleşimlerinde bırakmaya ve nesnelerin çakıştığı yerlerde çokgenleri birleştirmeye çalışır. Bu, voxel birleştirmeye göre çok daha temiz ve keskin sonuçlar verebilir; ancak bunun için "su geçirmez" ağlar gerekir; nesnelerde delikler veya bozuk şekiller olmamalıdır. Bu başarısız olursa, genellikle voxel birleştirme işe yarar.

### Boolean işlemleri
Hem Voxel Merge hem de Boolean, işlemi kontrol etmek için nesne görünürlüğünü kullanır:

#### Birleşim (Union)
Her iki nesne de görünürken boolean **union** oluşturulur; nesnelerin dış kabukları birleştirilir, iç yüzeyler olmaz. ![](/images/boolean_union.webp)

#### Çıkarma (Subtract)
Bir nesne görünmez = boolean **subtract**, görünmez nesne görünür nesneden çıkarılır. ![](/images/boolean_subtract.webp)

#### Kesişim (Intersect)
Her iki nesne de görünmez = boolean **intersection**, yalnızca iki nesnenin çakıştığı yerde yeni bir şekil oluşturulur. ![](/images/boolean_intersect.webp)


### Voxel Merge Düğmesi
Bu düğmeye basmak, seçili nesneler üzerinde voxel birleştirme işlemi yapar. Tek bir nesnede yapıldığında, gerilmiş çokgenleri olan bir nesne için faydalı olan, eşit aralıklı çokgenlere sahip olacak şekilde yeniden topoloji oluşturur.

### Çözünürlük
Hesaplama için kullanılan voxel 3B ızgarasının çözünürlüğü. Bu değer değiştirildiğinde, çokgen boyutunu önizlemek için nesnenin üzerine dama tahtası deseni bindirilir.

### Çoklu çözünürlük oluştur
Hedef çözünürlüğünüzün altında çoklu çözünürlük seviyeleri oluşturur. Örneğin çözünürlüğünüz 400 ve çoklu çözünürlük 3 ise, yaklaşık 296.000 çokgenli yeni bir ağ elde edersiniz, ancak bunun altında 74.000, 18.000, 4.000k gibi 3 alt bölme seviyesi olur.

### Keskin kenarları koru
Voxel ağını kenarlara oturtmayı etkinleştirir. Basit şekillerde en iyi sonucu verir.

### Boolean düğmesi
Bu düğmeye basmak, Emmett Lalish'in Manifold kütüphanesini kullanarak çokgen boolean işlemi yapar. 


## Ayır
Birden fazla bağlantısız parçaya dayanan tek bir nesneniz varsa, bu nesneyi birden fazla nesneye bölebilirsiniz. 
Bu, [Basit Birleştirme](#simple-merge)'nin tersi olarak görülebilir.

![](/videos/merge_separate.mp4)


## Ekle menüsü

![](/images/scene_addmenu_overview.webp)

Bu menü, primitifler, gruplar, kameralar, tekrarlayıcılar ve ışıklar oluşturur.

Primitifler, parametrelerle ayarlanabilen temel şekil türleridir. Primitifi ihtiyaçlarınıza göre ayarladıktan sonra onu "doğrularsınız" (validate); bu işlem parametreleri, yontulup boyanabilen bir çokgen ağa dönüştürür. Bir primitif doğrulandıktan sonra parametreleri artık değiştirilemez.


![](/images/scene_addmenu_top.webp)

### Gizmo üzerinde
Yeni primitifin, seçili şeklin veya gizmonun bulunduğu yere yerleştirilmesini etkinleştirir. Devre dışı bırakıldığında, primitif sahnenin merkezine yerleştirilir.

### Gizmo seç
Yeni bir primitif oluşturulduğunda otomatik olarak gizmo aracına geçmeyi etkinleştirir. 

### Gelişmiş

Bu menü, yeni primitiflerin, grupların, tekrarlayıcıların nerede oluşturulacağına dair tercihlerinizi ayarlamanıza olanak tanır. Seçili nesnenin üzerinde, dünya orijininde veya gizmonun konumunda olabilirler.


### UV'ler
Primitiflerde UV'leri etkinleştirir. UV'ler (genellikle doku koordinatları olarak adlandırılır), dokuların yüzeylere uygulanmasına izin vermek için 3B'de kullanılan ek verilerdir. Daha fazla bellek kullanırlar, ancak çoğu cihaz için 10 milyon poligon veya daha fazlası gibi çok yüksek poligon sayılarına çıkmadığınız sürece bu bir sorun olmamalıdır. 

### Primitifler

| Primitif      | Simge                                      | Açıklama                                                                                                     |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Kutu (Box)            | ![](/icons/cube.webp)                    | Basit bir küptür, X, Y ve Z bölünmelerini kontrol edebilirsiniz                                                  |
| Küre (Sphere)         | ![](/icons/circle.webp)                  | Kolaylık olması için Küre olarak adlandırılmıştır ancak aslında `Project on sphere` zorlanmış bölünmüş bir kutudur |
| Silindir       | ![](/icons/cylinder.webp)                | Silindir primitifine, örneğin içi boş bir boru yapmak için orta kısımda delik ekleyebilirsiniz                        |
| Torus          | ![](/icons/torus.webp)                   | Torus, yüzükler için iyi bir başlangıç noktası olabilir                                                                |
| Konik (Cone)           | ![](/icons/cone.webp)                    | -                                                                                                               |
| İkosahedron    | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| UV-küre      | ![](/icons/circle.webp)                  | Düzgün olmayan çokgen yerleşimine sahip bir küre, bkz. [Aşağıdaki uyarı](#uv-sphere)                                               |
| Düzlem (Plane)          | ![](/icons/rectangle.webp)               | Basit bir düzlemdir, bunun kapalı olmayan tek primitif olduğunu unutmayın                                    |
| Tüp (Tube)           | ![](/icons/tool_tube.webp)               | bkz. [Tube](tools#tube)                                                                                          |
| Torna (Lathe)          | ![](/icons/tool_lathe.webp)              | bkz. [Lathe](tools#lathe)                                                                                        |
| Triplanar      | ![](/icons/triplanar.webp)               | bkz. [Triplanar](#triplanar)                                                                                     |
| Gölge Yakalayıcı | ![](/icons/material_shadow_catcher.webp) | bkz. [Shadow Catcher](#shadow-catcher)                                                                           |
| Baş (Head)           | ![](/icons/face.webp)                    | Erkek/kadın arasında geçiş yapmaya yarayan bir katmana sahip basit bir kafa                                                         |

::: tip
Nomad'i başlattığınızda temel ağın ne olduğunu merak ediyorsanız: bu da bölünmüş bir kutudur.
Ancak Nomad'deki temel ağ `Project on sphere` kullanmaz, yani mükemmel yuvarlak değildir.
:::

### Primitif Araç Çubuğu

![](/images/scene_primitive_toolbar.gif)

Bir primitif oluşturulduğunda, parametrelerini kontrol etmek için bir araç çubuğu görünür.

* `Validate` Primitifi, yontulup boyanabilen standart bir nesneye dönüştürür.
* `Edit` Primitif gizmosunu gösterip gizlemeyi açıp kapatır. Bu, küp genişliği veya silindir delik yarıçapı gibi parametreleri kontrol etmek için doğrudan primitif üzerinde gösterilir.
* `Mirror` Primitifin üzerine bir ayna tekrarlayıcı yerleştirmeyi açıp kapatır.
* `...` Primitif menüsünü gösterir.

Farklı primitiflerin araç çubuğunda ek seçenekleri olabilir:

* `Project` Küre, yontma için daha iyi olduğu için bölünmüş bir küp olarak oluşturulur, ancak bu mükemmel yuvarlak olmadığı anlamına gelir. Bu seçenek, şekli mükemmel bir küreye daha yakın olmaya zorlar. İkosahedron da bu seçeneği paylaşır.
* `Cap` Bir şeklin uç kapaklarını açıp kapatır; örneğin bir silindirin üstte, altta, her ikisinde veya hiçbirinde kapak olabilir.
* `Hole` Şeklin ortasından geçen bir deliğin oluşturulup oluşturulmayacağını açıp kapatır. Bu, deliksiz, tek yarıçaplı delik veya üst ve altta farklı yarıçaplı delik arasında döngü yapar.
* `Radius` Bir silindirin tek bir yarıçap mı yoksa üst ve alt kısmında farklı yarıçap mı kullanacağını açıp kapatır.
* `Disk` Bir düzlemin 4 kenarlı bir şekil mi yoksa dairesel bir şekil mi olacağını açıp kapatır.

Ana araç çubuğunun altındaki küçük araç çubuğu, primitif gizmosu ile dönüşüm gizmosu arasında geçiş yapmanızı sağlar.

::: tip

Araç çubuğunun başlığına tıklamak, onu ekranın üstüne veya altına taşır. Köşedeki oka tıklamak ise araç çubuğunu daraltır.

:::


### Primitif menüsü

![](/images/scene_primitive_menu.webp)

Bu menü, seçili primitif için tüm parametreleri içerir. Parametreler, bir şeklin temel tanımlarıdır. Örneğin bir yüzüğü tanımlamak için dış yarıçapını, iç yarıçapını ve çokgen sayısını tanımlarsınız.

Çoğu primitif parametresi kendini açıklayıcıdır ve tüm primitifler arasında paylaşılan bazı ortak parametreler vardır:

* `UVs` Menünün üst kısmındaki küçük UVs düğmesi, UV koordinatlarının oluşturulmasını açıp kapatır
* `Validate` Küçük validate düğmesi, primitifin yontulup boyanabilen standart bir nesneye dönüştürülmesini sağlar.
* `Max faces` Cihazınızın çökmesini önlemek için nesnedeki çokgen sayısına üst sınır koyar.
* `Post subdivision` Topoloji menüsünün çoklu çözünürlük bölümünden seçilen alt bölme sayısını etkinleştirir. Bu, düşük topoloji bölünmeleriyle birlikte kullanıldığında yumuşatılmış, yumuşak köşeli primitifler yapmak için kullanılabilir. Örneğin, bir kutunun topoloji bölünmelerini 2'ye, post subdivision'ı 4'e ayarlamak, yumuşak köşeli bir kutu oluşturur.
* `Linear subdivision` Normal yumuşak alt bölmeden önce kaç seviye lineer alt bölme kullanılacağını ayarlar. Bu, alt bölünmüş yüzeylerde köşelerin ne kadar keskin veya yumuşak olacağını kontrol etmek için kullanılabilir. Örneğin, bir kutunun topoloji bölünmelerini 2'ye, post subdivision'ı 4'e ayarlayın, ardından lineer subdivision'ı 0 ile 4 arasında değiştirin. Kutunun köşeleri yumuşaktan keskin hale geçecektir.

### Topoloji

Bu, bir primitifteki çokgen sayısını kontrol eder. Genellikle kontroller bağlantılıdır; etkin kaydırıcıyı değiştirmek tüm çokgenleri eşit şekilde ayarlar. Bağlantıyı kesme düğmesine dokunarak bir şeklin X/Y/Z bölünmelerini ayrı ayrı kontrol edebilirsiniz.

### Geometri

Bu, kare şekiller için X/Y/Z birimlerinde, yuvarlak şekiller için yarıçap cinsinden bir primitifin genel boyutunu kontrol eder.


### UV Küre
::: warning
UV Küre, özellikle kutuplarda yontma için pek uygun değildir.

Lütfen `Project on sphere` seçeneğiyle birlikte [Sphere](#sphere), [Box](#box) veya [Icosahedron](#icosahedron) primitiflerini tercih edin.

`Division` kaydırıcıları için çok düşük bir değer kullanırsanız topoloji yontma için kabul edilebilir olabilir.
Daha sonra çokgen sayısını artırmak için `Overall Subdivision` kaydırıcısını kullanabilirsiniz.

Genel yontma için uygun olmasa da gözler için kullanışlıdır; küreyi kutuplar göz bebeğine gelecek şekilde döndürürseniz, çokgen yerleşimi doğal olarak iris ve göz bebeğini boyayıp yontmak için uygun olur.
:::


### Triplanar
Bu primitif özeldir; geometrisini şekillendirmek için üzerinde [Maskeleme aracı](tools.md#mask)'nı kullanmanız gerekir.

![](/videos/triplanar.mp4)


::: tip
Bir düzleme çift dokunun, kamera o düzleme odaklanır.
Ancak primitifin kendisini gizmo ile döndürürseniz bu çalışmaz.
:::

Triplanar, 3 düzlemden gelen maske bilgisini kullanarak bir voxel ızgarasını doldurur ve bu ızgara daha sonra çokgenleştirilir (bkz. [Voxel Remesher](topology.md#voxel-remeshere)).

Her düzlemin kendi simetri düzlemi vardır.

::: warning
Triplanar primitifinin boyutunu her güncellediğinizde, maske boyamanın kalitesi bozulur.

Şimdilik boyamayı tek bir düzlemde "kilitlemek" için bir seçenek yok, ancak gelecekte gelebilir.
[Connected Topology](stroke.md#connected-topology)'yi biraz yardımcı olması için kullanabilirsiniz; imleciniz tam olarak bir düzlemin üzerindeyse diğer düzlemleri etkilemez.
:::

### Gölge Yakalayıcı
Gölge yakalayıcı malzemesine sahip bir düzlem ekler. Daha fazla ayrıntı için bkz. [Shadow Catcher material](material.md#shadow-catcher). 


## Grup/Kamera
### Grup
Altına diğer nesneleri bağlayabileceğiniz "boş" bir nesne oluşturur. Bu, birçok nesneyi bir grup altına koyup sonra grubu kapatarak hiyerarşiyi basitçe düzenlemek için kullanılabilir. Bir grup ayrıca nesneleri taşımak için yardımcı olarak da kullanılabilir; birçok nesne bir grubun altına yerleştirilebilir ve ardından grup, gizmo aracıyla taşınabilir, döndürülebilir, ölçeklenebilir.

### Görünüm ekle
Bir kamera oluşturur.

## Tekrarlayıcılar (Repeaters)
![](/images/scene_primitive_repeaters.webp)

Tekrarlayıcılar, altındaki nesnelerin instance'larını oluşturan düğümlerdir. 

### Dizi (Array)
![](/images/scene_primitive_array.webp)

Nesneler bu düğümün çocukları yapıldığında, bir ızgara düzeninde instance'lanabilirler. Seçildiğinde şu kontrolleri vardır:
* Fit inside - Dizi örnekleri arasındaki boşluğu kontrol etmek ile dizinin ızgara/kutu boyutunu kontrol etmek arasında geçiş yapar
* CountX/Y/Z - Her eksendeki instance sayısı
* OffsetX/Y/Z - Fit inside kapalıyken instance'lar arasındaki mesafe
* SizeX/Y/Z - Fit inside açıkken toplam dizi ızgarasının genişlik/yükseklik/derinliği.

### Eğri (Curve)
![](/images/scene_primitive_curve.webp)
Bu, bir eğri oluşturur; bu düğümün çocukları eğri boyunca tekrarlanır. Seçildiğinde şu kontrolleri vardır:
* Edit - Eğriye nokta eklemeye ve eğri üzerindeki noktaları taşımaya izin verir.
* Snap - Eğri noktalarını diğer geometrilere yapıştırır
* Align - Çocuk şekilleri eğrinin yönüne hizalayacak şekilde döndürür
* Count - Instance sayısı
* Closed - Eğrinin başlangıç ve bitişini birleştirip kapalı bir eğri yapmayı veya açık eğri olmasını açıp kapatır
* Radius - Instance'ların ölçeğini kontrol etmek için her eğri noktasında kontrolleri açıp kapatır
* Twist - Instance'ların burulma dönüşünü kontrol etmek için her eğri noktasında kontrolleri açıp kapatır 
* B-spline - Instance'ların eğriyi tam olarak takip etmesini veya daha yumuşak sonuçlar veren b-spline enterpolasyonunu kullanmasını açıp kapatır. 

### Radyal
![](/images/scene_primitive_radial.webp)

Bu düğümün çocukları bir daire içinde instance'lanır. Bu tekrarlayıcının yarıçapını değiştirmek için çocuk nesneyi hareket ettirin. Seçildiğinde şu kontrolleri vardır:
* RadialX/Y/Z - Bu düğmelerden birini seçmek radyal ekseni ayarlar ve instance sayısını belirler.



### Ayna (Mirror)
![](/images/scene_primitive_mirror.webp)

Bu düğümün çocukları bir eksen boyunca aynalanır. Seçildiğinde şu kontrolleri vardır:
* Gizmo - Aynanın merkezini ayarlamak için dönüşüm gizmosunu etkinleştirir. Bu merkez ayrıca döndürülebilir ve ölçeklenebilir. İşiniz bittiğinde, standart kontrolleri göstermek için tekrar gizmo'ya dokunun.
* X/Y/Z - Ayna düzlemini ayarlar

Tüm tekrarlayıcıların bir `Validate` kontrolü vardır; bu, tekrarlayıcının sonuçlarını "pişirir" ve pişirmenin nasıl yapılacağını sorar:
* Join children - Instance'lar tek bir nesnede birleştirilir
* Keep instances - Instance'lar instance olarak kalır, ancak artık tekrarlayıcı "ebeveyn" olmaz
* Un-instances - Instance'lar benzersiz nesnelere dönüştürülür

::: tip İpucu: Tekrarlayıcıları birleştirin
Tekrarlayıcılar birbirlerinin altına bağlanabilir ve birkaç nesne tekrarlayıcıların çocukları yapılabilir; bu da karmaşık etkilere yol açar.

![](/images/scene_repeater_combine.webp)
:::

::: tip İpucu: Tekrarlayıcı pivotları

Bazı tekrarlayıcılar, çocuk nesnelerin pivotunu otomatik ayarlamaya çalışır; bu nedenle onları gizmo aracıyla hareket ettirseniz veya döndürseniz bile hareket etmezler. Bu davranışı geçersiz kılmanız gerekirse, tekrarlayıcı ile çocuk arasına bir grup ekleyin. Artık çocuk şekli tekrarlayıcıdan bağımsız olarak hareket ettirebilirsiniz.
:::

## Işık

![](/images/scene_primitive_light.webp)

### Yönlü (Directional)
Güneş gibi sonsuz uzaklıkta bir ışık kaynağı olan yönlü ışık oluşturur.

### Spot
Konik genişliği ve yumuşaklığı üzerinde kontrolleri olan bir spot ışık oluşturur

### Nokta (Point)
Noktasal ışık oluşturur

## Gelişmiş
### Öğeye odaklan
Sahne listesindeki bir öğeye çift tıklamak, kamerayı 3B görünümde o öğeye ortalar.

### Görünürlüğü eşitle
Göz simgesini kullanmak, tüm seçili öğeleri etkiler. 

### Instance: Göster
Sahne listesinin solunda instance'ları göstermek için renkli bir kapsül görüntüler.


### Simgeler
Görünüm penceresindeki grup, ışık, kamera, ayna simgelerinin boyutunu ve opaklığını ayarlar

### Hiyerarşi çizgileri
Görünüm penceresinde ebeveyn ile çocukları arasında bir çizgi gösterir

## Alt araç çubuğu
Bu simgeler, görünüm penceresinde Grup, Işık, Kamera, Tekrarlayıcı ve Hiyerarşi çizgilerinin görünürlüğünü açıp kapatır.
