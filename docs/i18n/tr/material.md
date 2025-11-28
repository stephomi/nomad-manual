# ![](/icons/material.webp) Malzeme {#material}

Bu menü, geçerli nesnenin malzemesini, nesne/malzeme için oluşturma (render) özelliklerini değiştirmenize ve malzemeye dokular atamanıza olanak tanır.

![](/images/material_overview.webp)

Malzemeler, bir nesnenin ışığa ve diğer nesnelere nasıl tepki verdiğini kontrol ederek nasıl göründüğünü tanımlar. Bir nesnenin görünümü şu özellikler tarafından kontrol edilir:

* `Material type`
* `Color`
* `Roughness`
* `Metalness`
* `Opacity`
* `Reflectance`
* `Emissive/unlit`

Bu özelliklerin kombinasyonları, fotogerçekçiden çizgi film tarzına ve deneysele kadar çok çeşitli sonuçlar elde edebilir.

Renk, pürüzlülük, metalik ve opaklık boyanabilir, daha fazla bilgi için [Vertex Paint options](painting.md) bölümüne bakın.

Malzeme türü, yansıtma, emissive/unlit aşağıda açıklanan malzeme özellikleridir.

Bu menünün üst kısmındaki kopyala/yapıştır düğmeleri, malzemeleri bir nesneden diğerine kopyalamanıza olanak tanır.

Nomad'in oluşturucusunun gerçek zamanlı bir oluşturucu olduğunu unutmayın; güçlü olsa da, belirli efektlerde doğruluk yerine hıza öncelik verir. 

## Malzeme türleri {#material-types}

![](/images/material_types.webp)

Nomad malzeme türleri: Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Opak {#opaque}
Boyanmış renk, pürüzlülük, metalik, opaklık destekleyen basit bir malzeme olarak yüzeyleri ele alan varsayılan moddur.

### ![](/icons/material_subsurface.webp) Yarı saydam {#subsurface}
Bu mod, ışığın iç kısımda bulanıklaşıp saçılmasına izin veren, cilt, mum, yeşim gibi malzemeleri simüle edebilir.

En iyi sonucu almak için PBR gölgelendirme moduna geçin ve en az bir yönlü veya spot ışık kullanın, ideal olarak loş bir ortamla birlikte.

`Depth`, ışığın önden yüzey altına, ardından tekrar ön yüzeye çıkana kadar ne kadar uzağa saçıldığını kontrol eder. Bu, sert gölgeleri yumuşatma ve yüzey detayını bulanıklaştırma etkisine sahiptir.

`Translucency`, ışığın bir şeklin önünden arkasına nasıl saçıldığını kontrol eder; bir yaprağın alt yüzeyinden geçen saçılma veya kulakların güçlü şekilde arkadan aydınlatılması gibi durumlar buna örnektir. 

### ![](/icons/material_blending.webp) Harmanlama {#blending}

Opaque’a benzer, ancak malzemenin katı ile saydam arasında karışmasına izin vermek için opaklık kaydırıcısını destekler. Bu, opaque malzemenin desteklediği boyanabilir opaklığa karşılık, opaklık için basit tek bir kaydırıcıdır. 

::: warning
Blending modu, karmaşık veya kesişen şekillerde titreme ve zıplamalara neden olabilir.
:::

### ![](/icons/material_additive.webp) Toplamalı {#additive}
Bu malzeme ile örgünüzü yarı saydam yapabilirsiniz. Blending malzemeye benzer, ancak blending çevresiyle karışırken, additive her zaman arkasındaki nesnelerden daha parlak olur; ışık huzmeleri, ateş, patlamalar gibi parlak efektler için iyidir.

1’den büyük bir opaklık değeri ayarlayabilirsiniz, bu nesnenin daha parlak olacağı anlamına gelir.  
Yalnızca bu nesnenin emissive bir nesne gibi parlamasını sağlamak için [bloom](postprocess.md#bloom) ve `threshold parameter` kullanmak istiyorsanız faydalı olabilir.

Bu mod, [Blending](#blending) moduna göre daha az yapaylık (order independent transparency) üretme eğilimindedir.

### ![](/icons/material_refraction.webp) Kırılma {#refraction}
Bu mod cam malzemeyi simüle etmek için kullanılabilir. Gerçek zamanlı kısıtlamalar nedeniyle, kendi kendine kırılma ve çok katmanlı kırılma bir miktar sınırlıdır.

Modelin pürüzlülük boyaması, kırılmanın ne kadar bulanık olduğunu etkiler.
Varsayılan olarak, Nomad’de oluşturulan her nesnenin pürüzlülüğü yaklaşık %25 civarındadır; dolayısıyla kırılma mükemmel olmayacak, biraz bulanık olacaktır.
Modelinizi, renkler etkilenmeden, pürüzlülük ve metalik değeri 0 olacak şekilde yeniden boyamak için `paint glossy` düğmesini kullanabilirsiniz.

İki farklı pürüzlülük söz konusudur: biri yüzeydeki yansımaların ne kadar bulanık olduğunu, diğeri ise iç kısmı (kırılma) kontrol eder.  
Ancak Nomad’de yalnızca tek bir pürüzlülük boyama kanalı olduğundan, iç ve dış pürüzlülük aynı değeri paylaşacaktır.  
Farklı değerlere sahip olmak için (örneğin keskin yüzeye ama bulanık iç kısma sahip bir lolipop) `Surface glossiness` ve `Interior roughness` kaydırıcılarını kullanarak boyanmış pürüzlülüğü geçersiz kılabilirsiniz.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Bazı pikselleri rastgele bir şekilde atarak nesneyi yarı saydam yapar.

### ![](/icons/material_shadow_catcher.webp) Gölge Yakalayıcı {#shadow-catcher}

Nesneyi görünmez yapar ve yalnızca gölge almasını sağlar. Nomad render’larını diğer görüntülerle birleştirmek için kullanışlıdır. 

::: tip

Şeffaflık ve karıştırma (blending) modları hakkında daha fazla bilgi için: https://support.fab.com/s/article/Transparency-Opacity

:::

## Kontroller {#controls}

![](/images/material_controls.webp)

### Her zaman ışıksız {#always-unlit}
Etkinleştirilirse, nesne PBR ve Matcap’i yok sayar ve yalnızca gölgelendirme olmadan renk boyamasını gösterir.
[Additive](#additive) kullanıyorsanız, siyah renk kullanarak doğrudan saydamlık boyayabileceğinizi unutmayın.

### Opaklık {#opacity}
Bir nesnenin ne kadar katı veya opak görüneceği; %100 katı, %0 saydamdır. Daha ince kontrol için opaklığı da boyayabilirsiniz.

### Yansıtırlık {#reflectance}
Metalik olmayan malzemelerin alacağı yansıma miktarını kontrol eder. Çoğu zaman varsayılan değer kullanılmalıdır (normal açıda standart %4 yansıtılan ışığa karşılık gelir), ancak örneğin bir karakterin gözlerindeki yansımaları ve parlak noktaları güçlendirmek için artırılabilir.

### Ters yüzey eleme {#inverse-culling}
Bir yüzeyin normallerini tersine çevirir. Genellikle gerekmez, ancak bir model içten dışa dönük görünüyorsa veya `Two sided` devre dışı bırakılmışken birlikte kullanıldığında, kameraya en yakın duvarın her zaman gizli olduğu iç mekânlar yapmak için kullanılabilir.

### Yumuşak gölgeleme {#smooth-shading}
[Genel seçeneğe](settings.md#smooth-shading) bakın.  
`Auto` değeri genel seçeneği kullanır.

### Çift taraflı {#two-sided}
[Genel seçeneğe](settings.md#two-sided) bakın.  
`Auto` değeri genel seçeneği kullanır.

### Renkli arka yüz {#coloured-backface}
[Genel seçeneğe](settings#two-sided) bakın.
`Auto` değeri genel seçeneği kullanır.

### Gölge oluşturur {#casts-shadows}
Şimdilik `Auto`, `On` ile aynıdır.
Saydam nesneler de gölge oluşturur (karışık gölgeleri taklit etmek için dithering deseninde).  
Sahnenizde gölge oluşturmasına gerek olmayan büyük bir nesne varsa (örneğin büyük bir zemin), gölge oluşturmayı devre dışı bıraktığınızdan emin olun.

### Gölge alır {#recieve-shadows}
Şimdilik `Auto`, `On` ile aynıdır.

### Tel kafes {#wireframe}
[Genel seçeneğe](settings.md#wireframe) bakın.  
`Auto` değeri genel seçeneği kullanır.


## Dokular {#textures}

![](/images/material_textures.webp)

Bir nesnenin UV’leri varsa, doku bake işleminin sonucu olmaları yaygın olmakla birlikte, Nomad dışında oluşturulan görüntüler de kullanılabilse de, tepe (vertex) renk/pürüzlülük/metallic/opacity’ye ek olarak malzemeye dokular uygulanabilir.

Dokular şunlara uygulanabilir:

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Emissive

Bir doku yuvasına tıklamak bir seçici açar. Bir doku bir malzeme yuvasına atandıktan sonra tekrar tıklamak bir doku paneli açar:

### Doku paneli seçenekleri {#texture-panel-options}

![](/images/material_texture_panel.webp)

### Aç {#open}
Başka bir doku seç

### Yok {#none}
Dokuyu kaldır

### Opaklık {#texture-opacity}

Görüntünün bir alfa kanalı varsa, bunu Opacity için kullanmanıza veya yok saymanıza olanak tanır.

### ![](/icons/link.webp) Zincir/Bağlantı simgesi {#chainlink-icon}

Aşağıdaki bölümlerdeki bağlantı simgesi etkinleştirildiğinde, kullanılan seçenekler, bağlantı simgesi etkinleştirilmiş diğer dokular (color, normal, roughness, metalness, opacity, emissive) ile paylaşılır. 

Bu, hizalanmış dokularınız varsa, parametreleri veya projeksiyon türlerini değiştirseniz bile hizalı kalmalarını sağlar.


### İzdüşüm {#projection}
![](/images/material_projection.webp)

Dokunun nesneye nasıl uygulanacağını ayarlayın.

* `Auto` - Nesnenin UV’si varsa UV, yoksa Triplanar
* `UV` - Dokuyu uygulamak için örgünün UV koordinatlarını kullanır. Örgü ve doku Nomad dışından geliyorsa veya Nomad’den dışa aktarılıp başka yerde kullanılacaksa, doğru seçenek UV’dir.
* `Triplanar` - Dokuyu X, Y, Z eksenleri boyunca yansıtır ve dikişleri harmanlar. 

### Üç düzlemli {#triplanar}
![](/images/material_triplanar.webp)

Triplanar projeksiyonlar, dokuları nesnelere uygulamanın güçlü ama basit bir yoludur.

Triplanar, tamamı aynı görüntüye sahip 6 video projektörünün, nesnenizin ön, arka, sol, sağ, üst ve alt yüzeyine ışık tuttuğunu hayal etmeye benzer.

Gerektiğinde bu daha sonra UV’lere veya tepe renklerine bake edilebilir.


![](/images/material_triplanar_example.webp)

#### Yöntem {#method}

* `Local` - Projeksiyon, nesnenin dönüşümüyle birlikte hareket eder
* `World` - Projeksiyon sabit kalır, nesneyi hareket ettirmek onu projeksiyonun içinden kaydırır.

#### Sertlik {#hardness}

Projeksiyonların nasıl karıştığı. %100, hiçbir harmanlama yapmaz ve projeksiyonların kenarları keskin olur. %0, kenarları geniş bir açı boyunca harmanlar. Varsayılan %90’dır; kenarları gizlemek için yeterli karışım sağlar ve projeksiyonların geri kalanı keskin kalır.

### Üniform {#uniform}

İşaretlendiğinde, tüm projeksiyonlar için aynı hardness kullanılır. İşaret kaldırıldığında, X, Y, Z projeksiyonları için ek hardness kontrolleri görünür hale gelir.


### Parametre {#parameter}
![](/images/material_parameter.webp)

#### Filtreleme {#filtering}
Kullanılacak doku filtreleme yöntemi, varsayılan `Auto`dur; yöntemler `Nearest`, `Linear`, `Mipmap`’tir. Nearest hiçbir filtreleme yapmaz, bu nedenle dokular yakından bakıldığında tırtıklı yapaylıklar gösterebilir. Linear ve Mipmap daha iyi filtreleme yapar, böylece dokular yakından bakıldığında tırtıklı yerine bulanık görünür.

#### Döşeme-X {#tiling-x}
Scale parametresi 1’den büyükse ve dokuyu nesnenin UV’lerinden daha küçük yapıyorsa, doku X ekseni boyunca nasıl döşenecektir. `None` tekrar yok anlamına gelir. `Repeat` dokunun kopyalarını yapar. `Mirror`, her ikinci kopyası ters çevrilmiş olacak şekilde dokunun kopyalarını yapar; bu, döşeme yapaylıklarını gizlemeye yardımcı olabilir.

#### Döşeme-Y {#tiling-y}
Tiling-X ile aynıdır, ancak Y ekseni için.

### Dönüşüm {#transform}
![](/images/material_transform.webp)

Dokunun UV uzayında uygulanan ek 2B dönüşümler. Sıfırlama düğmesi varsayılanlara döndürür, zincir simgesi (renk dışındaki dokular seçiliyken) dönüşümü renk dokusuyla aynı olacak şekilde bağlar veya ayırır.

#### Öteleme {#translation}
Dokunun X ve Y ofseti

#### Döndürme {#rotation}
Dokunun dönüşü

#### Ölçek {#scale}
Dokunun ölçeği; daha büyük sayılar, dokuyu nesne üzerinde daha küçük yapar, ne olacağını kontrol etmek için Tiling-X ve Tiling-Y kaydırıcılarını kullanın.

### Üniform ölçek {#uniform-scale}
Kapalıyken Nomad, Scale-X ve Scale-Y için ayrı kontroller gösterir.