# ![](/icons/multires.webp) Topoloji 

Bu menü, Nomad'daki nesnelerin topolojisini, ayrıca nesneler ve dokular arasında detayları pişirmek ve aktarmak için kullanılan araçları kontrol eder.

![](/images/topology_overview.webp)

Nomad çokgen tabanlıdır, geometrinin işlenmesi için üçgenler ve dörtgenler kullanır.
Topoloji derken, hem yüz sayısını hem de noktaların (vertexlerin) birbirine bağlanma şeklini kastediyoruz.

Özellikle ince detayları yontmak veya boyamak istiyorsanız, topolojiyi takip etmek önemlidir.

::: tip Topolojinizi nasıl takip edersiniz?
[Wireframe](settings.md#wireframe) görüntüleyebilir veya [Smooth Shading](settings.md#smooth-shading) özelliğini devre dışı bırakabilirsiniz.
:::

![](/images/topology_top.webp)

Nomad'ın topoloji menüsü birkaç bölümden oluşur:

| Yöntem                                 | Simge                        | Açıklama                                                         |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Alt bölümlendirme kullanarak birden fazla detay seviyesini düzenleme |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | Üniform yoğunlukta yeni bir topoloji yeniden hesaplama           |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | Yontma veya boyama sırasında gerçek zamanlı olarak yerel yüz ekleme/çıkarma |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | Azaltma, UV'ler, pişirme, yeniden ağ oluşturma, yeniden projeksiyon |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | Primitif seçenekleri                                             |


## Polygon istatistikleri

![](/images/topology_stats.webp)

Topoloji menüsünün üst kısmı, seçili nesne ve tüm sahne için çokgen bilgilerini gösterir. Sayılar, toplam vertex sayısını, toplam üçgen sayısını ve toplam dörtgen (4 kenarlı çokgen) sayısını gösterir.

Bu bölüme dokunmak, sahnedeki tüm çokgen nesneler için çokgen istatistiklerinin bir listesini açar.

## ![](/icons/multires.webp) Multiresolution

![](/images/topology_multires_menu.webp)

### Multiresolution nedir?
Multiresolution özelliği iki ana senaryo için kullanışlıdır:
- Nesnenizin poligon sayısını artırmak için smooth subdivision algoritması
- Küçük ve büyük ölçekli düzenlemeler arasında geçiş yapabilmeniz için birden fazla çözünürlük seviyesiyle çalışmak

![](/videos/multiresolution.mp4)

#### Multiresolution iş akışı
Multiresolution'un önemli bir yönü, daha düşük bir çözünürlüğe geri dönebilmeniz, nesnenizde değişiklik yapabilmeniz ve ardından yüksek çözünürlüklü detayları kaybetmeden tekrar en yüksek çözünürlüğe çıkabilmenizdir. Tüm yüksek çözünürlüklü detaylar otomatik olarak projekte edilir.

::: warning
Nesnenizin topolojisini değiştiren bir araç kullanıyorsanız, nesnenizin diğer tüm çözünürlük seviyelerini kaybedersiniz!
Bu durum gerçekleştiğinde her zaman bir uyarı almalısınız, örneğin şunları kullanırken:
- [Voxel Remesher](#voxel-remesher)
- [Dynamic Topology](#dynamic-topology)
- [Trim aracı](tools.md#trim)
- [Split aracı](tools.md#split)
:::


### Multiresolution kaydırıcısı
Bu kaydırıcı, mevcut nesnedeki alt bölümlendirme seviyelerinin sayısını gösterir. 6 dikey çubuk varsa, 6 alt bölümlendirme seviyesi vardır. Daire, şu anda görüntülenen alt bölümlendirme seviyesini gösterir. 

### Reverse
En düşük alt bölümlendirme seviyesindeyken, reverse düğmesi mevcut seviyenin altında yeni bir seviye oluşturmaya çalışır. Bunun genellikle yalnızca nesne baştan itibaren, örneğin Nomad'de veya diğer multiresolution subdivision surface kullanan 3D uygulamalarda alt bölümlendirme ile oluşturulmuşsa mümkün olduğunu unutmayın.

### Subdivide
*Subdivide* düğmesi, poligon sayısını 4 kat artırır, bu nedenle poligon sayısını gözünüz üzerinde tutun, çok hızlı artabilir!
*Subdivision Surface*'ın önemli bir yönü, *Smooth Surface*'a yakınsamalarıdır.
Nasıl çalıştığını anlamak için, yalnızca birkaç poligona sahip bir nesnede *Subdivide* düğmesini deneyebilirsiniz.

Bu *Smooth* davranışını `Linear subdivision` seçeneğini işaretleyerek devre dışı bırakabilirsiniz.

### Delete lower
Şu anda görüntülenen seviyenin altında alt bölümlendirmeler varsa, bunları siler. Bunu yanlışlıkla yaparsanız, Reverse düğmesiyle yeniden oluşturabilirsiniz.

### Delete higher
Şu anda görüntülenen seviyenin üzerinde alt bölümlendirmeler varsa, bunları siler.

### Linear subdivision
Ağ yapısını yumuşatma uygulamadan alt bölümlendirir.

### Sharp border
Nesnenizde facegroup'lar varsa, bu seçeneği etkinleştirmek facegroup sınırlarını keskin tutar. Bu, her alt bölümlendirme seviyesinde ayarlanabilir (alt bölümlendirme kaydırıcısında, bu durumu göstermek için seviye üzerinde küçük bir simge görünür).

### Keep triangles
Çoğu standart subdivision surface sistemi, alt bölümlendirme işlemi sırasında tüm çokgenleri dörtgene dönüştürmeye çalışır. Bu anahtar, alt bölümlendirmenin bunun yerine üçgenler kullanmaya zorlanmasını sağlar.

### Lock (LV0)

En düşük alt bölümlendirme seviyesinin değiştirilmesini engeller. Nesneniz başka bir uygulamada üretilmişse ve temel nesnenin değişmeden kalması gerekiyorsa bu önemli olabilir. Bu seçenek devre dışı bırakıldığında, daha yüksek alt bölümlendirme seviyelerinde yapılan büyük değişiklikler seviye 0'ı da hareket ettirir.

::: tip 

Alt bölümlendirme varsayılan olarak tüm keskin kenarları yumuşatır. Kenarları hafifçe keskin tutmak için, ilk 2 alt bölümlendirme seviyesinde linear subdivision veya Sharp border kullanmayı deneyin, ardından daha yüksek seviyelerde kapatın. Bu, yarı keskin alt bölümlendirilmiş bir ağ oluşturur.

:::


## ![](/icons/voxel.webp) Voxel Remesher
![](/images/topology_voxel_menu.webp)
`Voxel Remesher` kullanıldığında, tüm ağ, topolojiyi üniform bir çözünürlüğe zorlar; yani tüm poligonlar aşağı yukarı aynı boyuttadır. Bu, topoloji hakkında düşünmek istemediğiniz ve sadece serbest biçimli yontma yapmak istediğiniz durumlarda çok kullanışlıdır.

Tipik bir yontma iş akışı, düşük çözünürlüklü kaba bir şekli bloklamak için `Voxel Remesher` kullanarak başlayabilir.
Ağı çok fazla esnettiğinizde, aşırı bozulmayı önlemek için ara sıra *Remesh* düğmesine basmanız yeterlidir.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Yukarıda belirtildiği gibi, Nomad çokgen tabanlı bir yazılımdır, ancak `Voxel Remesher`, yeniden ağ oluşturma işlemini gerçekleştirmek için (geçici olarak) farklı bir yaklaşımın kullanıldığı bir istisnadır.

Büyük farklardan biri, voxel yaklaşımının kendi kendine kesişmeyi kabul etmemesidir, bu nedenle bunlar çözümlenir.
Ayrıca delikli ağları desteklemez.

Burada delik derken `genus hole`'u (simitin `deliği`) değil, `watertight`/`closed` olmayan ağları kastediyoruz.
Tipik olarak, bu, yeniden ağ oluşturmadan önce tüm deliklerin doldurulacağı anlamına gelir; bu, [Trim aracı](tools.md#trim) veya [Hole filling özelliği](scene.md#hole-filling) ile benzerdir.
:::

### Remesh
Voxel remesh işlemini yürüt.

### Resolution
Hesaplama sırasında kullanılan voxel boyutu. Bu parametreyi değiştirirken, sonuç önizlemesi vermek için ağ üzerinde dama tahtası deseni bindirilir.

### Build multiresolution
Voxel remesh için daha düşük multiresolution seviyeleri oluşturur. Dama tahtası desenini kullanarak bir çözünürlük ayarlarsanız ve build multiresolution'ı 2'ye ayarlarsanız, nihai sonuç çözünürlük kaydırıcısıyla eşleşen detaya sahip olur ve multires sekmesine gittiğinizde seviye 2'de olur; yani seviye 1 ve seviye 0'da daha düşük çözünürlüklü multires ağlara sahip olursunuz. Bu, hem düzgün, eşit poligonlu bir ağ üretmek hem de daha düşük çözünürlüklü bir kontrol ağına sahip olmak için iyi bir yol olabilir.

::: tip İpucu: Build multiresolution ve stable smoothing

Bu seçenek bazen yumuşatılması zor, küçük sivilceler oluşturan 'döngüler' yaratabilir. Bu olursa, smooth aracı seçeneklerinde 'Stable smoothing'i etkinleştirin. 

:::

### Keep sharp edges
Yeni noktaların, orijinal ağdaki keskin kenarlara yapışmasını etkinleştirir. Bozulma yaratabilir.

## ![](/icons/dynamic.webp) Dynamic Topology

![](/images/topology_dyntopo_menu.webp)
Multiresolution ve voxel remeshing, topolojiyi kontrol etmek için yaygın endüstri yöntemleridir, ancak her ikisi de poligonları çok fazla germediğinizden veya çok fazla sıkıştırmadığınızdan emin olmanızı gerektirir. 

Dynamic Topology alternatif bir yöntemdir. Yontarken, Nomad fırça darbesi sırasında uyarlanabilir olarak poligon ekler ve çıkarır; böylece küçük detaylar oyarak çalıştığınız yerlerde birçok küçük poligon eklenir, başka yerlerde yumuşatma ise poligonları kaldırır.

Dynamic topology'nin üçgen poligonlar kullanacağını, dörtgen kullanmayacağını unutmayın. Bu biraz dağınık görünebilir, ancak tel kafese bakmamak, sadece güzel görünen bir heykel yapmaya odaklanmak ve topoloji hakkında endişelenmemek genellikle daha iyidir; daha sonra temiz bir dörtgen ağ üretmek için Nomad'ın diğer yeniden ağ oluşturma araçlarından birini kullanabilirsiniz.

Aşağıdaki videoda uygulamasını görebilirsiniz.

![](/videos/dynamic.mp4)

### Enabled
Dynamic topology'yi açar. Her araç için Dyntopo'yu açıp kapatmanıza izin vermek için, fırça yarıçapı ve yoğunluk kaydırıcılarının altına bir DynTopo simgesi yerleştirilir.

### Detail
Detay miktarını kontrol eder, davranışı aşağıdaki 'Detail based on...' seçimine göre değişir.

### Detail based on...
| Yöntem  | Açıklama                                                     |
| :-----: | :----------------------------------------------------------: |
| Screen  | Detay seviyesi, nesnenin ekrandaki büyüklüğüne bağlıdır. Detay kaydırıcısı, küçük üçgenler oluşturan ince detay için %100 veya daha yüksek, büyük üçgenler oluşturan düşük detay için %1'dir.  |
| Radius  | Araç yarıçapı, detay miktarını tanımlar. İnce detay için küçük, düşük detay için büyük araç yarıçapı kullanın. Detay kaydırıcısı, bu oranın çarpanıdır.                     |
| Constant | Detay kaydırıcısı, detay miktarını tanımlar ve ekran boyutundan veya araç boyutundan etkilenmez.             |

::: tip İPUCU: Radius modu

Radius modunun nasıl çalıştığını daha iyi anlamak için, bir parmağınızla detay kaydırıcısını hareket ettirmeye başlayın, ardından aynı anda başka bir parmağınızla araç yarıçapını değiştirin. Nasıl bağlantılı olduklarını göreceksiniz.

:::

### Prefer...
| Yöntem | Açıklama          |
| :----: | :---------------: |
| Speed  | Performansı tercih et |
| Quality | Kaliteyi tercih et  |

`Quality` tercih edildiğinde, 2 ana fark şunlardır:
- inceltme, yontmadan önce uygulanır, böylece çok küçük detayları boyarken veya yontarken daha az enterpolasyon artifaktı elde edersiniz
- inceltme, artımlı bir davranışın aksine, doğru detay seviyesine yakınsayana kadar çalışır.
 
Böylece, çok küçük detaylar yontarsanız veya hızlı darbeler yaparsanız, topoloji her zaman beklendiği gibi inceltilir.


### Use pressure on radius
Yalnızca `Radius` etkinse geçerlidir. Etkinleştirildiğinde, detay seviyesi, fırça boyutu kalem basıncından etkilendiğinde bile her zaman fırça boyutunu yansıtır.

### Use stroke falloff

Dyntopo hesaplamalarına fırça düşüş eğrisini ve alphasını da dahil eder.

### Method
`Dynamic Topology`'yi [Brush](#brush) üzerinde veya [Global](#global) olarak kullanıyor olun, hangi modda çalışacağını seçebilirsiniz:

| Yöntem          | Açıklama                                                            |
| :-------------: | :-----------------------------------------------------------------: |
| Uniformisation  | Yüz ekleyip çıkarabilir, yukarıdaki videoda kullanılan mod budur    |
| Subdivision     | Yalnızca yeni yüzler ekler, yüz çıkaramaz                           |
| Decimation      | Yalnızca yüz çıkarır, yüz ekleyemez                                 |

### Protect masked area
Maskelenmiş alanların topolojisinin değişmesini engellemeyi etkinleştirir.

### Vertex extrapolation


### Detail
Yeniden ağ oluşturma işlemi için kullanılan çözünürlük. Dyntopo 'Constant' modundaysa, bu değer, bu menünün üst kısmındaki Detail kaydırıcısıyla aynı olacaktır.

### Remesh
Dyntopo algoritmasını kullanarak global bir remesh yürütür. Genellikle tam yeniden ağ oluşturma için [Voxel Remesher](#voxel-remesher) kullanmalısınız.

Ancak voxel'lere göre bir avantajı, maskelenmiş alanın korunmasıdır; böylece nerede daha fazla veya daha az yoğunluk istediğiniz üzerinde daha iyi kontrol sahibi olabilirsiniz.



## ![](/icons/topo_extra.webp) Misc

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) Dişli menü
Bu menüdeki araçların çoğunun ek seçenekleri vardır. Bunlara bölüm başlığının yanındaki dişli simgesinden erişilebilir.

### Decimation

![](/images/topology_decimation.webp)

Üçgen çokgenler kullanarak mümkün olduğunca fazla detayı korumaya çalışırken poligon sayısını azaltır.

Bu özellik, 3D baskı için dışa aktarmak istiyorsanız kullanışlı olabilir.
Ancak, düzensiz üçgenler üretebileceği için üzerinde yontmaya devam etmek istiyorsanız muhtemelen kullanmamalısınız.

Maskelenmiş alanların azaltılmayacağını unutmayın.

![](/videos/decimate.mp4)

::: tip

Yüksek poligonlu nesnelerde [Quadremesh aracı](tools.md#quad-remesher) kullanmak, hesaplama için uzun zaman alabilir ve kontrol edilmesi zor sonuçlar verebilir. Ağı önceden [facegroup](tools.md#facegroup-1) ve decimate ile işlemek, Quadremesh'in çok daha hızlı çalışmasını sağlar ve topoloji üzerinde çok daha fazla kontrol sunar.

* İdeal dörtgen akışınızı tanımlamak için ağı facegroup'layın.
* Facegroup sınırlarını yumuşatmak için facegroup relax uygulayın.
* Decimate. Bu, facegroup kenarında ince veya bozulmuş yüzlerinizin olmamasını sağlar. Decimate ayarlarında facegroup'un etkin olduğundan emin olun. Bu, üçgen kenarlarının facegroup kenarlarınıza tam olarak uymasını sağlar.
* Quadremesh seçeneklerinde relax'in devre dışı olduğundan emin olun (ağı zaten gevşetmiş olduğunuz için) ve iyi sonuçlar almalısınız.

:::

#### Decimate
Azaltma işlemini başlatır.

Decimate düğmesinin yanındaki simgeler, azaltmayı etkileyen seçenekleri açıp kapatmanıza izin verir. Yüzde, bu seçeneğin ne kadar güçlü olduğunu gösterir ve gelişmiş dişli menüsünde ayarlanabilir.

* ![](/icons/palette.webp)  `Preserve Painting` - Boyama detayının olduğu yerlere daha fazla üçgen yerleştirir.
* ![](/icons/triforce.webp) `Uniform Faces` - Eşit boyutlu üçgenler oluşturmayı tercih eder.
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - Azaltma, açık geometri ve deliklerin yakınındaki sınırları mümkün olduğunca değiştirmemeye çalışır.
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - Azaltma, facegroup sınırlarını mümkün olduğunca değiştirmemeye çalışır.
* ![](/icons/checkerboard.webp) `Preserve UV Borders` - Azaltma, UV sınırlarını mümkün olduğunca değiştirmemeye çalışır.

#### ![](/icons/cog.webp) Decimate dişli menüsü
Dişli menüsü şu gelişmiş seçeneklere sahiptir:
##### Preserve painting
Onay kutusu bu modu açıp kapatır, değer ise boyama detayının ne kadar doğru korunacağını belirler. Daha yüksek değerler daha fazla boyamayı korur. Boyamayı umursamıyorsanız 0'a ayarlayın.


##### Uniform faces
Onay kutusu bu modu açıp kapatır. Daha yüksek değerler, benzer boyutta üçgenler üretir.

##### Preserve borders
Sınırların azaltılmasını durdurmak için etkinleştirin. Sınır ağırlıkları `Geometry`, `Face Group` veya `UV` sınırları için seçilebilir.

#### Target triangles
Hedef üçgen sayısını ayarlar. Varsayılan değer %50'dir, yüzde/hedef düğmesi, yüzde ile tam hedef poligon sayısı arasında geçiş yapar.



### UV Unwrap - UVAtlas

![](/images/topology_uvatlas_menu.webp)
Mevcut ağ için doku koordinatlarını (UV'ler) hesaplar; genellikle bozulmayı en aza indirmek için daha fazla ada ve kesim oluşturmayı tercih eder.

Menü başlığı ile dişli menü arasındaki küçük göz simgesi, nesne üzerindeki UV önizlemesini açıp kapatır.

![](/videos/unwrap.mp4)

#### Unwrap
Seçili nesne için UV'leri hesaplar, bunlar arka planda görüntülenir.

#### Delete UVs
Nesnedeki UV'leri siler.

#### ![](/icons/cog.webp) UVAtlas dişli menüsü
Dişli menüsü şu gelişmiş seçeneklere sahiptir:

#### Face Group

UV kesimlerini tanımlamak için facegroup'ları kullanın.

##### Max Stretch
Düşük değerler daha az bozulma ve daha fazla ada, yüksek değerler daha fazla bozulma ve daha az ada oluşturur. 

##### Island spacing
Adalar arasındaki boşluk miktarı. Düşük değerler daha az alan israf eder, ancak adalar arasında doku taşması riskini artırır. 

::: warning
UV hesaplamak biraz zaman alabilir, 100k'den az vertex'e sahip bir ağa sahip olmak en iyisidir.
:::

::: tip UV'ler?
UV'ler için yaygın bir benzetme, hediye paketi sarmaktır; bir nesneyi, üst üste binme olmadan tamamen kaplamak için hediye kağıdını kesmenin en iyi yolu nedir? 

UV'ler benzerdir, ancak kağıdı kesmek yerine nesneyi kesersiniz. Modelinizin ince plastikten yapıldığını hayal edin; modelinizi düz yatırmak için nasıl keserdiniz, o düz haldeyken üzerine nasıl boyar, sonra tekrar nasıl birleştirirdiniz?

Şimdi modelinizin yüzeyinin esnek likradan yapıldığını hayal edin. Modeli düzleştirmek için esnetebilir, kesebilir veya her ikisinin bir kombinasyonunu kullanabilirsiniz. Ancak nesne düzleştirilmiş haldeyken üzerine bir dama tahtası boyarsanız, yeniden birleştirdiğinizde dama tahtası bozulur. Hangisi daha iyi bir yöntemdir, daha az bozulma ile daha fazla kesim mi, yoksa daha fazla bozulma ile daha az kesim mi?

UV'ler, dokular uygulanırken nesnenin nasıl 'kesilip esnetileceğini' 3D yazılıma söyleyen talimatlardır. UV Atlas aracı genellikle 'daha fazla kesim, daha az bozulma' yaklaşımını kullanır.


:::

::: tip UV'ler, Nomad ve diğer uygulamalar

Çevrimiçi bulduğunuz çoğu dokulu model, UV'lerle dokulanmıştır. Nomad bunu [material](material#textures) paneli aracılığıyla içe aktarabilir ve görüntüleyebilir.

Modeller Nomad'de yapıldığında, UV'ler olmadan doğrudan nesneler üzerine boyayabilirsiniz. Bunları diğer uygulamalara, örneğin [Procreate](https://procreate.art/)'e aktarmanız gerekirse, Nomad renk bilgisini UV'ler aracılığıyla dokulara 'bake' edebilirsiniz. 

:::

### UV Unwrap - BFF
![](/images/topology_uvbff_menu.webp)

BFF UV'ler, 'daha az kesim, daha fazla bozulma' yaklaşımını tercih eder. 

#### ![](/icons/cog.webp) UV BFF dişli menüsü

#### Face Group

UV kesimlerini tanımlamak için facegroup'ları kullanın.

##### Cone count
Kullanılan ana projeksiyon sayısını tanımlar. Daha düşük değerler daha az ada, ancak daha fazla bozulma üretir.

##### Seamless patches
UV yamalarının yerleşimini etkiler, dikkatle oluşturulmuş facegroup'larla en iyi sonucu verir.

### Bake -> texture 
![](/images/topology_bake_menu.webp)

Doku pişirme, sahnedeki diğer görünür nesneleri, seçili nesnenin UV'lerine projekte ederek dokular oluşturur.

Pişirme için tipik iş akışı şöyledir:
- İnce detaylara ve boyamaya sahip bir ağınız var
- Bunu klonlayın
- Decimate edin (`Preserve painting` değerini 0'a ayarlayın)
- UV unwrap yapın
- Bake edin!

Nomad varsayılan olarak sahnedeki tüm görünür ağları hesaba katar.
Diğer ağların çoğunu hızlıca gizlemek için Solo modunu da kullanabilirsiniz.
Başka görünür nesne yoksa, tüm sahneyi hesaba katar.

Artık, önceki nesnenizin boyasının ve detaylarının çoğunu koruyan düşük çözünürlüklü bir ağınız olmalıdır.

İşlemden sonra, vertex renkleri, dokularla çakışmamaları için devre dışı bırakılmış yeni bir katmana taşınır.

#### From itself
Mevcut nesnede en yüksek multiresolution seviyesini en düşük seviyeye bake eder. Kurulumu basittir, ancak genellikle daha fazla kontrole ihtiyaç duyarsınız; bu durumda bir sonraki seçenek daha kullanışlıdır.

#### From high-res ()
Sahnedeki diğer görünür nesnelerden, seçili nesneye bake eder. Parantez içindeki sayı, yüksek çözünürlüklü hedefler olarak kullanılacak diğer görünür nesnelerin sayısını gösterir; bunlar, UV'li mevcut düşük çözünürlüklü nesneye bake edilir. Diğer nesnelerin, bake edilen nesneyle benzer yerleşim veya topolojiye sahip olması gerekmez; bu da esnek bake iş akışlarına olanak tanır.

#### Resolution
Bake edilen dokunun çözünürlüğü. Bake dokuları her zaman karedir, bu nedenle 1024, 1024x1024'lük bir görüntü oluşturur. 

Aşağıdaki düğmeler, yaygın olarak kullanılan çözünürlükler için kısayollardır. Referans olarak, 512x512, web grafikleri ve basit geometri için nispeten küçüktür. 4096x4096 (kısaca 4k), yüksek kaliteli renderlar içindir.

#### ![](/icons/cog.webp) Bake dişli menüsü
![](/images/topology_bake_gear_menu.webp)
Dişli menüsü şu gelişmiş seçeneklere sahiptir:

##### Normal, Roughness, Metalness, Color, Emissive, Opacity
Bu onay kutuları, hangi özelliklerin bake edileceğini belirler; her biri ayrı haritalara bake edilir. Bake tamamlandıktan sonra, bunlar mevcut nesnenin malzemesine doku olarak eklenir.

##### Backup
Bake edilmiş dokuları önizlemek için, nesnenin boya bilgisinin devre dışı bırakılması gerekir. Bu seçenek, boya bilgisini yedek olarak yeni bir katmana aktarır, böylece kolayca etkinleştirilebilir/devre dışı bırakılabilir.

#### Cage radius
Bake nesnesinden hedef nesneleri aramak için gönderilen ışınların ne kadar uzağa gideceğini ayarlar. Varsayılan olarak bu mesafe, artifaktlardan kaçınmak için düşük tutulur, ancak hedef nesneler bake nesnesinden uzaktaysa artırılabilir.

##### Ray offset
Bake hesaplamalarının, bake nesnesi üzerinde nereden başlayacağını ayarlar. Varsayılan olarak yüzeyden %5 uzakta başlarlar; bu, çoğu yaygın artifaktı önler. Hedef nesneler bake nesnesinden çok uzaktaysa, bu ofsetin artırılması gerekebilir.


### Reproject to vertex

![](/images/topology_reproject_menu.webp)

Yontulmuş detayları, boyamayı, katmanları, dokuları vertex değerlerine projekte eder.

Bake işleminin tersi olarak düşünülebilir; bake, vertex özelliklerini dokulara aktarırken, reproject dokuları (ve diğer özellikleri) tekrar vertexlere aktarır.

::: tip
`Bake to texture` veya `Reproject to vertex` kullanırken, hem vertex renkleri hem de malzeme dokuları hesaba katılır.
:::

#### From itself
Malzemedeki dokuları vertex değerlerine dönüştürür. Bu düğme yalnızca nesnenin UV'leri varsa ve malzemede dokular etkinse aktif olur.

::: tip İPUCU: Doku boyama
Nomad doğrudan doku boyamayı ve düzenlemeyi desteklemez, ancak dokuları -> vertex değerlerine projekte edip, vertexler üzerinde boyayıp, ardından vertex -> dokulara bake ederek çok benzer sonuçlar elde edilebilir:

1. UV'li düşük poligonlu bir nesne hazırlayın
1. Malzemesine dokular yükleyin
1. Üzerinde boyama yapabilecek kadar alt bölümlendirin
1. `Reproject to vertex`i `From itself` modunda çalıştırın; artık doku vertex değerlerine dönüştürülmüştür
1. Boyayın, yumuşatın, lekeleyin, damgalayın, ihtiyacınız olan tüm düzenlemeleri yapın
1. `Bake to texture`i `From itself` modunda çalıştırın. Bu düzenlemeler tekrar dokulara dönüştürülür.
:::

#### From high-res ()
Görünür nesneleri, seçili nesne üzerinde vertex değerlerine dönüştürür. Bu düğmedeki sayı, görünür nesnelerin sayısını gösterir.

::: tip
Diğer nesneleri yeniden projekte etmek, yalnızca diğer nesnelerden renk bilgisini aktarmak için değil, vertexleri diğer nesnelere projekte etmek için de kullanılabilir; örneğin bandajlar bir karakterin üzerine projekte edilebilir.
:::

#### ![](/icons/cog.webp) Reproject dişli menüsü
Dişli menüsü şu gelişmiş seçeneklere sahiptir:

#### Vertices, Roughness, Metalness, Color, Opacity, Opacity->Mask, Mask, Layers, Face Group
Bu onay kutuları, hangi özelliklerin seçili nesneye projekte edileceğini belirler. 

#### Relax
Seçili ağın yerleşimi, yeniden projeksiyon hedeflerine daha iyi uyması için belirli bir miktarda yumuşatılabilir veya gevşetilebilir. Smooth, yüksek poligonlu ağlar için daha iyidir. Relax, düşük poligonlu ağlar için daha iyidir. Auto, en iyi yöntemi Nomad'ın belirlemesine izin verir.

#### Iterations
Yeniden projeksiyon sırasında relax işleminin kaç kez uygulanacağını belirler.

#### Cage radius
Seçili nesneden hedef nesneleri aramak için gönderilen ışınların ne kadar uzağa gideceğini ayarlar. Varsayılan olarak bu mesafe, artifaktlardan kaçınmak için düşük tutulur, ancak hedef nesneler bake nesnesinden uzaktaysa artırılabilir.

#### Ray bias
Düşük değerler, hedef yüzeydeki en yakın noktaya projeksiyonu tercih eder. Yüksek değerler, yüzey normali kullanılarak bir kesişim noktasını tercih eder. 

#### Ray offset
Bake hesaplamalarının, seçili nesne üzerinde nereden başlayacağını ayarlar. Varsayılan olarak yüzeyden %5 uzakta başlarlar; bu, belirli artifaktları önler. Hedef nesneler seçili nesneden çok uzaktaysa, bu ofsetin artırılması gerekebilir.


### Quad Remesh - Instant
![](/images/topology_quadremesh_menu.webp)
[Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung tarafından geliştirilen Instant Meshes algoritmasını](https://igl.ethz.ch/projects/instant-meshes/) kullanarak yeniden ağ oluşturur. Bir ağın akışını analiz eder ve temiz dörtgen topoloji oluşturur.

::: tip
iOS ve masaüstünde, [Quad remesher](tools#quad-remesher) aracı daha iyi sonuçlar ve daha fazla kontrol sağlar.
:::

#### Remesh
Instant meshes işlemini başlatır.

#### Target quads
Quad remesh'in oluşturmaya çalışacağı dörtgen çokgen sayısı.

#### ![](/icons/cog.webp) Quad Remesh Instant dişli menüsü
Dişli menüsü şu gelişmiş seçeneklere sahiptir:

##### Crease angle
Yeniden ağ oluşturma işlemini yönlendirmeye yardımcı olmaya çalışacak keskin köşeler için bir eşik.

#### Max fill hole
Algoritma bazen istenmeyen delikler üretebilir. Bir deliğin bu değerden daha az vertex'i varsa, doldurulur.

### Holes
![](/images/topology_holes_menu.webp)
Çoğu zaman nesneniz muhtemelen watertight olacaktır; yani ağ 'kapalı'dır.

Nesnenizde delikler varsa, bunları doldurabilirsiniz. Bunun yalnızca 'naif' deliklerde çalıştığını, yani iki ayrı sınırı 'kaynaştıramayacağını' unutmayın.

![](/videos/hole_filling.mp4)

::: tip
Voxel remesher'i çalıştırdığınızda, 1 veya birden fazla ağ üzerinde kullanıyor olun, tüm delikler otomatik olarak kapatılır.
:::

#### Close holes
Delik kapatma işlemini yürütür.

#### ![](/icons/cog.webp) Holes dişli menüsü
Dişli menüsü şu gelişmiş seçeneklere sahiptir:

##### Detail
Deliği doldurmak için kullanılan poligon yoğunluğu. Bu kaydırıcıyı sürüklerken model üzerinde bir dama tahtası deseni gösterilir; bu, kullanılacak üçgen boyutuna dair bir gösterge verir. Onay kutusu bunu devre dışı bırakır ve yalnızca mevcut noktaları kullanır; bu genellikle deliğin üzerinde yontulması zor, uzun ince üçgenler oluşturur.

##### Fill non-manifold
Non manifold deliği doldurmaya çalışır.

##### Face Group

Delikler doldurulurken, her deliğin kendi facegroup'unu (Auto) mu alması, yoksa hepsinin bir facegroup'u paylaşması (Off) mı, yoksa hiç facegroup oluşturulmaması (On) mı gerektiğini belirler.

### Force Manifold
![](/images/topology_forcemanifold_menu.webp)
Non manifold kenarları temizlemeye çalışır. İkiden fazla yüzün ortak olduğu kenarları desteklemeyen harici yazılımlar için kullanışlı olabilir.

#### Clean
Temizleme işlemini yürütür.
#### ![](/icons/cog.webp) Force manifold dişli menüsü
Dişli menüsü şu gelişmiş seçeneklere sahiptir:

#### Delete small faces
Küçük çokgenleri kaldırmak ve birleştirmek için kullanılan bir eşik.


### Triplanar
![](/images/topology_triplanar_menu.webp)
Ağı bir [triplanar](scene.md#triplanar) primitife dönüştürür.
Bu süreçte muhtemelen birçok detayı kaybedersiniz.

#### Force cubic
Triplanar'ın bir küp olmasını sağlar. Aksi takdirde triplanar, nesnenizin en yakın bounding box'ına uyacak şekilde ayarlanır.

#### Convert
Triplanar işlemini yürütür.

#### Resolution
Triplanar işleminde kullanılan voxel boyutu.

## ![](/icons/dot.webp) Primitive
Seçili primitif için parametreler. Bunlar ayrıca primitif viewport araç çubuğunda da mevcuttur.

![](/images/topology_primitive_screenshot.webp)
