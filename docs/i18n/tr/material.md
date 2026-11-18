# ![](/icons/material.webp) Malzeme {#material}

Bu menü, geçerli nesnenin malzemesini ve nesnenin/malzemenin işleme özelliklerini değiştirmenize, ayrıca malzemeye doku atamanıza olanak tanır.

![](/images/material_overview.webp)

Malzemeler, bir nesnenin ışığa ve diğer nesnelere nasıl tepki verdiğini kontrol ederek nasıl göründüğünü belirler. Bir nesnenin görünümü şu özelliklerle kontrol edilir:

* `Malzeme türü`
* `Renk`
* `Pürüzlük`
* `Metaliklik seviyesi`
* `Opaklık`
* `Yansıtıcılık`
* `Yayıcı/aydınlatmasız`

Bu özelliklerin birleşimleriyle, foto-gerçekçiden çizgi film tarzına ve deneysele kadar çok çeşitli sonuçlar elde edilebilir.

Renk, pürüzlük, metaliklik ve opaklık boyanabilir; daha fazla bilgi için [Verteks boyama seçeneklerine](painting.md) bakın.

Malzeme türü, yansıtıcılık ve yayıcı/aydınlatmasız, aşağıda açıklanan malzeme özellikleridir.

Bu menünün üstündeki `Kopyala` ve `Yapıştır` düğmeleri, malzemeleri bir nesneden diğerine kopyalamanızı sağlar.

Nomad'ın işleyicisinin gerçek zamanlı bir işleyici olduğunu unutmayın; güçlü olsa da bazı efektlerde doğruluk yerine hızı ön planda tutar.

## Malzeme türleri {#material-types}

![](/images/material_types.webp)

Nomad'ın malzeme türleri şunlardır: Opak, Yüzey altı, Karışım, Eklenti, Kırılma, Renk Taklidi, Gölge yakalayıcı.

### ![](/icons/material_opaque.webp) Opak {#opaque}
Yüzeyleri; boyanmış renk, pürüzlük, metaliklik ve opaklığı destekleyen basit bir malzeme olarak ele alan varsayılan mod. Boyanmış opaklık, bir opaklık dokusu veya renk dokusunun alfa kanalı, renk taklidi (dithering) kullanarak nesneyi yine de saydam gösterir. Yalnızca ana opaklık kaydırıcısı yok sayılır.

### ![](/icons/material_subsurface.webp) Yüzey altı {#subsurface}
Bu mod; deri, mum, yeşim gibi, ışığın içinde bulanıklaşıp saçıldığı malzemeleri simüle edebilir.

Aydınlatılmış (PBR) gölgelendirme modunu gerektirir. En iyi sonuç için, tercihen loş bir ortamla birlikte en az bir yönlü ışık veya spot ışık kullanın.

Renk örneği, saçılan ışığın rengini belirler.

`Derinlik`, ışığın ön yüzeyden yüzeyin altına, sonra yeniden ön yüzeyden dışarı ne kadar uzağa saçılacağını kontrol eder. Bu, sert gölgeleri yumuşatır ve yüzey ayrıntılarını bulanıklaştırır.

`Yarı saydamlık`, ışığın bir şeklin önünden arkasına nasıl saçıldığını kontrol eder; bir yaprağın alt yüzünden geçen ışık ya da arkadan güçlü bir şekilde aydınlatılan kulaklar gibi. Bunu görmek için gölge oluşturan bir ışığa ihtiyacınız vardır.

### ![](/icons/material_blending.webp) Karışım {#blending}

Opak'a benzer, ama malzemenin katı ile saydam arasında karışabilmesi için opaklık kaydırıcısını destekler. Bu, opak malzemenin desteklediği boyanabilir opaklığa karşılık, opaklık için basit tek bir kaydırıcıdır.

::: warning
Karışım modu, karmaşık veya iç içe geçen şekillerde titreme ve aniden belirip kaybolma sorunlarına yol açabilir.
:::

### ![](/icons/material_additive.webp) Eklenti {#additive}
Bu malzemeyle ağ örgünüzü yarı saydam yapabilirsiniz. Karışım malzemesine benzer, ama karışım çevresiyle harmanlanırken eklenti her zaman arkasındaki nesnelerden daha parlak olur; ışık huzmeleri, ateş, patlamalar gibi parlak efektler için uygundur.

1'den yüksek bir opaklık değeri ayarlayabilirsiniz; bu, nesnenin daha parlak olacağı anlamına gelir.  
[Parlama](postprocess.md#bloom) ve `eşik parametresi` ile yalnızca bu nesnenin, yayıcı bir nesne gibi ışıldamasını istiyorsanız işe yarayabilir.

Bu mod, [Karışım](#blending) moduna göre daha az kusur üretme eğilimindedir (sıradan bağımsız saydamlık).

### ![](/icons/material_refraction.webp) Kırılma {#refraction}
Bu mod cam malzemeyi simüle etmek için kullanılabilir. Aydınlatılmış (PBR) gölgelendirme modunu gerektirir. Gerçek zamanlı işlemenin kısıtlamaları nedeniyle, nesnenin kendi içindeki kırılma ve çok katmanlı kırılma bir ölçüde sınırlıdır.

Modelin pürüzlük boyaması, kırılmanın ne kadar bulanık olacağını etkiler.
Varsayılan olarak Nomad'da oluşturulan her nesnenin pürüzlüğü yaklaşık %25'tir; dolayısıyla kırılma kusursuz olmaz, biraz bulanık görünür.
Modelinizi pürüzlüğü ve metalikliği 0 olacak şekilde yeniden boyamak için `Parlak boyama` düğmesini kullanabilirsiniz (renkler etkilenmez).

İşin içinde 2 farklı pürüzlük vardır: biri yüzeydeki yansımanın ne kadar bulanık olacağını, diğeri ise iç kısmın (kırılmanın) bulanıklığını belirler.  
Ancak Nomad'da yalnızca tek bir pürüzlük boyama kanalı olduğu için, iç ve dış pürüzlük aynı değeri paylaşır.  
Farklı değerler elde etmek için (örneğin yüzeyi keskin ama içi bulanık bir lolipop), boyanmış pürüzlüğü geçersiz kılmak üzere `Pürüzlülüğü geçersiz kıl` altındaki `Yüzey` ve `İç alan` kaydırıcılarını kullanırsınız.

![](/videos/refraction.mp4)

#### Kırılma Endeksi {#index-of-refraction}
Işığın nesneye girerken ne kadar büküldüğü. Daha yüksek değerler ışığı daha çok büker, kalın bir mercek gibi.

#### Emilim {#absorption}
Işığın hacmin içinden geçerken emilmesini simüle eder; renk örneğiyle tonlanır, gücü de `Faktör` ile ayarlanır. İnce kısımlar daha fazla ışık geçirdikleri için daha parlak, kalın alanlar ise daha koyu olur. Nesnenin kalınlığı yalnızca yaklaşık olarak hesaplandığı için efekt büyük ölçüde şekle bağlıdır.


### ![](/icons/material_dithering.webp) Renk Taklidi {#dithering}
Bazı pikselleri rastgele atarak nesneyi yarı saydam yapar.

### ![](/icons/material_shadow_catcher.webp) Gölge yakalayıcı {#shadow-catcher}

Nesneyi görünmez yapar ve yalnızca ışıklardan gelen gölgeleri almasını sağlar. Nomad işlemelerini, genellikle bir düzlem üzerinde, başka görsellerle birleştirmek için kullanışlıdır. Renk örneği gölgenin rengini belirler.

Sahnede gölge oluşturan bir ışık olmalıdır; aksi halde gölge yakalayıcı hiçbir şey yapmaz. `Metaliklik seviyesi → %0` ve `Metaliklik seviyesi → %100` düğmeleri nesneyi yeniden boyar: tamamen metalik olduğunda, [Yansıma (SSR)](postprocess.md#reflection-ssr) süreç sonrası işlemi etkinse gölge yakalayıcı sahneyi de yansıtabilir.

::: tip

Saydamlık ve karışım modları hakkında daha fazla bilgiyi https://support.fab.com/s/article/Transparency-Opacity adresinde bulabilirsiniz.

:::

## Kontroller {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Her zaman aydınlatmasız {#always-unlit}
Etkinleştirilirse nesne PBR ve MatCap'i yok sayar ve boyanmış rengini gölgelendirme olmadan gösterir.
[Eklenti](#additive) kullanıyorsanız, siyah renk kullanarak saydamlığı doğrudan boyayabileceğinizi unutmayın.

### Opaklık {#opacity}
Bir nesnenin ne kadar katı veya opak görüneceği; %100 katı, %0 saydamdır. Kaydırıcı Karışım, Eklenti, Renk Taklidi ve Gölge yakalayıcı türlerinde gösterilir. Daha ince kontrol için opaklığı boyayabilirsiniz de.

### Ön kırılma geçişi {#pre-refract-pass}
Yalnızca Karışım ve Eklenti. Bu saydam nesneyi kırılma geçişinden önce çizer. Kırılan bir nesne başka saydam yüzeylerin önündeyse kullanışlıdır.

### Yansıtıcılık {#reflectance}
Metalik olmayan malzemelerin alacağı yansıma miktarını kontrol eder. Çoğu zaman varsayılan değer kullanılmalıdır (dik açıda standart %4 yansıyan ışığa karşılık gelir), ama örneğin bir karakterin gözlerindeki yansımaları ve parlak noktaları güçlendirmek için artırılabilir. Aydınlatılmış (PBR) gölgelendirme modunu gerektirir.

### ![](/icons/culling.webp) Ters culling {#inverse-culling}
Bir yüzeyin normallerini ters çevirir. Genellikle gerekmez, ama bir model içi dışına çıkmış gibi görünüyorsa kullanılabilir; ya da `İki taraflı` devre dışıyken, kameraya en yakın duvarın her zaman gizlendiği iç mekânlar oluşturmak için kullanılabilir.

Aşağıdaki seçenekler `Otomatik`, `Hayır` veya `Evet` olarak ayarlanabilir. `Otomatik` ayarında ok, gerçekte kullanılan değeri gösterir.

### ![](/icons/sphere_smooth.webp) Yumuşak gölgelendirme {#smooth-shading}
Bkz. [genel seçenek](settings.md#smooth-shading).  
`Otomatik` değeri genel seçeneği kullanır.

### ![](/icons/culling.webp) İki taraflı {#two-sided}
Yüzler iki taraftan da görünür. Bkz. [genel seçenek](settings.md#two-sided-quick).  
`Otomatik` değeri genel seçeneği kullanır.

### ![](/icons/culling.webp) Renklendirilmiş arka yüz {#coloured-backface}
Bkz. [genel seçenek](settings.md#two-sided-quick).
`Otomatik` değeri genel seçeneği kullanır.

### ![](/icons/shadow_cast.webp) Gölge oluştur {#casts-shadows}
Saydam nesneler de gölge oluşturur (karışık gölgeleri taklit etmek için renk taklidi deseniyle).  
Sahnenizde gölge oluşturması gerekmeyen büyük bir nesne varsa (örneğin büyük bir zemin), gölge oluşturmayı devre dışı bıraktığınızdan emin olun.

### ![](/icons/shadow_receive.webp) Gölge al {#recieve-shadows}
Diğer nesnelerin gölgelerinin bu nesnenin üzerine çizilip çizilmeyeceği.

### ![](/icons/wireframe.webp) Genel taslak {#wireframe}
Bkz. [genel seçenek](settings.md#wireframe).  
`Otomatik` değeri genel seçeneği kullanır.

### ![](/icons/trash.webp) Normalleri sıfırla {#reset-normals}
Yalnızca içe aktarılan bir nesne kendi normallerini taşıdığında gösterilir (örneğin `Topolojiyi koru` ile). Bu normalleri kaldırır; böylece gölgelendirme, yüzeyden hesaplanan normalleri kullanır.

## Dokular {#textures}

![](/images/material_textures.webp)

Bir nesnenin UV'leri varsa, malzemeye verteks rengi/pürüzlüğü/metalikliği/opaklığına ek olarak dokular da uygulanabilir. Bunlar genellikle bir doku pişirme işleminin sonucudur, ama Nomad dışında oluşturulmuş görseller de kullanılabilir. Başlığın yanındaki `UV:✓` veya `UV:✗`, nesnenin UV'leri olup olmadığını gösterir.

Dokular şunlara uygulanabilir:

* Renk
* Normal
* Pürüzlük
* Metaliklik
* Opaklık
* Yer Değiştirme
* Yayıcı

İçe aktarılan bir nesnenin oklüzyon dokusu varsa bir `Oklüzyon` satırı da görünür, ama Nomad bunu kullanmaz.

Her satırın kaydırıcısı, dokusunun ne kadar güçlü uygulanacağını, hiç uygulanmamaktan tamamen uygulanmaya kadar belirler. `Renk` ve `Yayıcı` satırlarında ayrıca dokuyu tonlayan bir renk örneği bulunur; `Yayıcı` ayrıca ışıma gücünü belirler.

`Yer Değiştirme`, yer değiştirme haritasının yüzeyi ne kadar uzağa iteceğini belirler. `Uygula` düğmesi verteksleri yer değiştirme kadar taşır, ardından haritayı kaldırır. Sonuç etkin katmana gider.

Başlığın yanındaki palet düğmesi, [boya](painting.md) menüsünün malzeme önayarlarını açar: dokularını nesneye kopyalamak için birine dokunun. Masaüstünde, Nomad'a geri döndüğünüzde içe aktarılan görseller orijinal dosyalarıyla senkronize edilir; başlığın yanındaki bir senkronizasyon düğmesi de onları yeniden yükler.

Bir doku yuvasına tıklamak bir seçici açar. Bir malzeme yuvasına doku atandıktan sonra tekrar tıklamak bir doku paneli açar:

### Doku paneli seçenekleri {#texture-panel-options}

![](/images/material_texture_panel.webp)

Panel, görselin boyutunu ve dokunun bir önizlemesini gösterir.

### ![](/icons/open.webp) Aç {#open}
Başka bir doku seçer. Masaüstünde `Keşfet`, görsel dosyasını dosya tarayıcınızda gösterir.

### ![](/icons/circle_cross.webp) Yok {#none}
Dokuyu kaldırır.

### Opaklık {#texture-opacity}

Yalnızca renk dokusu. Görselin bir alfa kanalı varsa, bu seçenek onu opaklık için kullanmanızı ya da yok saymanızı sağlar.

### Biçim {#normal-format}
Yalnızca normal dokusu. Normal haritaları iki türde gelir: `OpenGL (+Y)` ve `DirectX (-Y)`. Ayrıntılar ters görünüyorsa diğerini deneyin.

### Yükseklik {#displacement-height}
Yalnızca yer değiştirme dokusu.
* `Yerel` - Yükseklik, nesnenin ölçeğiyle birlikte büyür ve küçülür.
* `Dünya` - Nesnenin ölçeği ne olursa olsun yükseklik aynı kalır.

### Çarp {#multiply}
Yalnızca pürüzlük, metaliklik ve opaklık dokuları. Dokunun değerlerini çarpar. %100 olmadığında değer doku yuvasının üzerinde gösterilir.

### ![](/icons/link.webp) Zincir/Bağlantı simgesi {#chainlink-icon}

Aşağıdaki bölümlerdeki bağlantı simgesi etkinken, hangi seçenekler kullanılırsa kullanılsın, bağlantı simgesi aynı şekilde etkin olan diğer dokularla (renk, normal, pürüzlük, metaliklik, opaklık, yayıcı) paylaşılır.

Böylece hizalanmış dokularınız varsa, parametreleri veya projeksiyon türlerini değiştirseniz bile hizalı kalmalarını sağlayabilirsiniz.


### Projeksiyon {#projection}
![](/images/material_projection.webp)

Dokunun nesneye nasıl uygulanacağını belirler.

* `Otomatik` - Nesnenin UV'leri varsa UV, yoksa Üç düzlemli
* `UV` - Dokuyu uygulamak için ağ örgüsünün UV koordinatlarını kullanır. Ağ örgüsü ve doku Nomad dışından geliyorsa ya da başka bir yerde kullanılmak üzere Nomad'dan dışa aktarılacaksa, doğru seçenek UV'dir.
* `Üç düzlemli` - Dokuyu X, Y, Z eksenleri boyunca yansıtır ve dikişleri harmanlar.

### Üç düzlemli {#triplanar}
![](/images/material_triplanar.webp)

Üç düzlemli projeksiyonlar, nesnelere doku uygulamanın güçlü ama basit bir yoludur.

Üç düzlemli projeksiyon, aynı görseli nesnenizin önüne, arkasına, soluna, sağına, üstüne ve altına yansıtan 6 projektöre sahip olmak gibidir.

Gerekirse bu daha sonra UV'lere veya verteks renklerine pişirilebilir.


![](/images/material_triplanar_example.webp)

#### Yöntem {#method}

* `Yerel` - Projeksiyon nesnenin dönüşümüyle birlikte hareket eder
* `Dünya` - Projeksiyonlar sabit kalır; nesneyi hareket ettirmek onu projeksiyonun içinden kaydırır.

#### Sertlik {#hardness}

Projeksiyonların nasıl karıştığı. %100 hiç harmanlama yapmaz ve projeksiyonların kenarları keskin olur. %0 kenarları geniş bir açı boyunca harmanlar. Varsayılan değer %90'dır: kenarları gizlemeye yetecek kadar karışım sağlar, projeksiyonların geri kalanı ise keskin kalır.

### Düzenli {#uniform}

İşaretliyken tüm projeksiyonlar için aynı sertlik kullanılır. İşaret kaldırıldığında X, Y, Z projeksiyonları için ek sertlik kontrolleri görünür.


### Parametre {#parameter}
![](/images/material_parameter.webp)

#### Filtreleme {#filtering}
Kullanılacak doku filtreleme yöntemi; varsayılan `Otomatik`'tir, yöntemler ise `En Yakın`, `Doğrusal`, `Mipmap`'tir. En Yakın hiç filtreleme yapmaz; bu yüzden dokular yakından bakıldığında tırtıklı kusurlar gösterebilir. Doğrusal ve Mipmap daha iyi filtreleme yapar; dokular yakından tırtıklı değil bulanık görünür.

#### Döşeme - X {#tiling-x}
Ölçek parametresi 1'den büyükse, yani doku nesnenin UV'lerinden daha küçükse, dokunun X ekseni boyunca nasıl döşeneceği. `Yok`, hiç tekrar olmadığı anlamına gelir. `Tekrarla` dokunun kopyalarını oluşturur. `Aynala` da dokunun kopyalarını oluşturur, ama her ikinci kopyayı ters çevirir; bu, döşeme kusurlarını gizlemeye yardımcı olabilir.

#### Döşeme - Y {#tiling-y}
Döşeme - X ile aynıdır, ama Y ekseni için.

### Dönüştür {#transform}
![](/images/material_transform.webp)

Dokuya UV uzayında uygulanan ek 2d dönüşümler. Sıfırlama düğmesi varsayılan değerlere döndürür; zincir simgesi (renk dışındaki dokular seçiliyken) dönüşümü renk dokusununkiyle aynı olacak şekilde bağlar veya bağlantıyı kaldırır.

#### Öteleme {#translation}
Dokunun X ve Y kaydırması.

#### Döndürme {#rotation}
Dokunun dönüşü.

#### Ölçek {#scale}
Dokunun ölçeği. Daha büyük sayılar dokuyu nesne üzerinde küçültür; ne olacağını kontrol etmek için Döşeme - X ve Döşeme - Y seçeneklerini kullanın.

### Tek tip ölçeklendirme {#uniform-scale}
Kapatıldığında Nomad, Ölçek-X ve Ölçek-Y için ayrı kontroller gösterir.
