# ![](/icons/layer.webp) Katmanlar 

Bu menü, nesnenize yaptığınız düzenlemeleri yıkıcı olmayan bir şekilde saklamanızı sağlayan katman yığını ile katmanları birleştirmenin ve yeniden amaçlandırmanın birçok yolunu içerir.

![](/images/layers_overview.webp) 

## Genel Bakış

Nomad katmanları birden fazla amaca hizmet eder.

Boya bilgisi (Renk, Pürüzlülük, Metalik, Opaklık) katmanlarla, 2B boyama uygulamalarına benzer şekilde çalışır. Bir katman oluşturulabilir ve modele boya uygulanabilir. Katman açılıp kapatılabilir, opaklığı ayarlanabilir, katman çoğaltılabilir, katman yığını içindeki sırası değiştirilebilir, karışım modu ayarlanabilir.

Nomad ayrıca yontma (sculpt) için de katmanlar kullanır. Bir katman kırışıklık gibi ince detayları saklayabilir veya büyük değişiklikleri saklayabilir; bu sayede diğer 3B uygulamalardaki blendshape/shape key/morph target’lar gibi çalışabilir. Örneğin farklı yüz ifadelerini farklı katmanlara yontabilir ve katman kaydırıcılarını ayarlayarak bunları yeni ifadelere dönüştürebilirsiniz.

Bu durumda, bir katmanda saklanan değişiklikler tamamen toplayıcıdır; boya için olduğu gibi katman sırası önemli değildir.

Katmanlar [Delete Layer](tools.md#delete-layer) aracıyla kısmen silinebilir ve katmanlarda saklanan farklı bilgilere göre maskeler oluşturmak için de kullanılabilir.

![](/videos/layer.mp4)

::: tip
Çoğu yontma yazılımının aksine, bir ağın topolojisini değiştirmek katmanları silmez. [Voxel Remesher](topology.md#voxel-remesher), [Multiresolution](topology.md#multiresolution) veya [Trim](tools.md#trim)/[Split](tools.md#split) araçlarını kullanabilirsiniz, ancak [Voxel Remesher](topology.md#voxel-remesher) kullanırken katman kalitesinin etkileneceğini unutmayın.
:::

::: tip
Katmanları blendshape/morph target olarak kullanıyorsanız, [sahne menüsünde](scene.md#object-menu) ek katman işlevleri vardır. Katmanları nesnelere ayırabilir ve eşleşen nesneleri katmanlara birleştirebilirsiniz.
:::
----

## Katman menüsü 

![](/images/layers_menu.webp)

Yeni bir katman oluşturmak için `Add layer` düğmesine basın.

Her katmanın bir adı, gücünü/faktörünü kontrol eden bir kaydırıcısı ve seçenek düğmeleri vardır.

### Seçenekler

| Eylem        | Simge                        | Açıklama                                            |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Görünür      | ![](/icons/eye_open.webp)   | Katmanı göster/gizle                                |
| Karışım Modu | ![](/icons/opacity.webp)    | Photoshop tarzı karışım modu. 4 simge, Renk, Pürüzlülük, Metalik, Opaklık için modları gösterir. |
| Adı Düzenle  | ![](/icons/pencil.webp)     | Katman adını düzenle                                |
| Sil          | ![](/icons/trash.webp)      | Katmanı sil                                         |
| Çoğalt       | ![](/icons/clone.webp)      | Katmanı çoğalt                                      |
| Aşağı Birleştir | ![](/icons/merge_down.webp) | Katmanı alttaki katmanla (veya temel ağla) birleştir |
| Daha Fazla   | ![](/icons/more.webp)       | [Daha fazla...](#more) seçenekleri                 |

Bir katmanı katman yığınının başka bir bölümüne taşımak için, adına basılı tutun ve sürükleyin.

### Daha fazla...

‘Daha fazla...’ düğmesi, geçerli katman için ek seçenekler gösterir:

![](/images/layers_more.webp) 

#### Kanal faktörleri

Bu kontroller, katman için yontma/renk/pürüzlülük/metalik/opaklık miktarını ölçeklendirmenizi sağlar. Bu değerler, katman faktörü kaydırıcısıyla çarpılır; örneğin katman gücü 1 ise, ancak renk kanal faktörü 0,5 ise, görüntülenen renk 0,5 güçte olur.

`Offset` katman yontma gücünü kontrol eder. Renk/pürüzlülük/metalik 0 ile 1 arasında sınırlandırılırken, offset hem pozitif hem negatif olmak üzere herhangi bir değer olabilir. 

::: tip
Offset, bir kabartma katmanını oyuk katmanına veya bir gülümsemeyi somurtmaya dönüştürmek için kullanılabilir:
![](/videos/layer_happysad.mp4)


Simetrik bir katman klonlanabilir ve ardından del layer ile sol/sağ şekillere bölünebilir:
![](/videos/layer_leftright.mp4)

Negatif offset faktörlü katmanlar, yeni pozitif şekiller oluşturmak için boş katmanlara pişirilebilir.

1’in üzerindeki pozitif offset faktörlü katmanlar, daha uç blendshape’lerle denemeler yapmak için kullanılabilir.
:::

::: warning
Şu anda katmanlar, 3 kanalın (renk/metalik/pürüzlülük) tamamı için yalnızca tek bir opaklık kanalı paylaşmaktadır.
Kanal başına yoğunluğu tam olmayan birden fazla katmanı birleştirirseniz, nihai sonucun farklı görünmesi mümkündür.

Belki gelecekte, bu sınırlamayı kaldırmak için her kanalın kendi alfa kanalı olacaktır.
:::


#### ![](/icons/tool_mask.webp) Maske
Her kaydırıcının yanındaki maske düğmesi, o kanaldan bir maske oluşturur. Boyama uygulamalarında seçim yapmak için katman kullanmaya benzer şekilde, bu, bir katmanda yaptığınız çalışmayı diğer işlemler için yeniden kullanmanıza olanak tanır.

#### ![](/icons/preview.webp) Önizleme
![](/images/layers_preview.webp) 

Etkinleştirildiğinde, bu katman için çıkarma ayarlarını önizler (bir sonraki bölüme bakın).

X-ray etkinleştirildiğinde, yalnızca çıkarılan şekil katı olur, şeklin geri kalanı saydam yapılır; bu, negatif çıkarma yükseklikleri kullanıyorsanız kullanışlıdır.

#### Çıkar
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

`Extract` düğmesi, katmanın içeriğini genellikle bir sonraki bölümde ayarlanan, kullanıcı tanımlı bir kalınlıkla yeni bir nesneye kopyalar.

`Closing action`, kopyalamanın nasıl yapılacağını belirler:

* None - Sadece kısmı çıkar, yan yüzeyler oluşturmaya veya delikleri doldurmaya çalışma.
* Fill - Delik üçgenlerle doldurulur ve yumuşatılır. Düz yüzeyler için bu seçeneği kullanmayın.
* Shell - Çıkarılan şekli kalınlık değeri ve yön seçenekleriyle kapat.
* Layer - Katman farkını çıkar.

#### ![](/icons/height.webp) Kalınlık
![](/images/layers_thickness.webp) 

Kabuk ekstrüzyonunun derinliği. Pozitif değerler yüzeyden dışarı doğru, negatif değerler yüzeyin içine doğru büyür.

Bu değerin yanındaki artı/eksi, ekstrüzyonun yönünü ayarlar:
* Eksi ( - ) mevcut yüzeyden başlayıp aşağı doğru ekstrüde eder. 
* Artı ( + ) mevcut yüzeyden başlayıp yukarı doğru ekstrüde eder.
* ArtıEksi ( ± ) ekstrüzyonun üst ve altını eşit miktarda dışarı iter, böylece orijinal yüzeye yarı gömülü olur.

#### Pürüzsüzlük
![](/images/layers_smoothness.webp) 

Çıkarılacak bölgenin kenarları tırtıklıysa, bu kaydırıcı kenarı daha pürüzsüz bir şekle bulanıklaştırmaya çalışır. 

#### ![](/icons/height.webp) Kenar döngüsü (yan)
![](/images/layers_edgeloop.webp) 

Bu bölüm, kapatma eylemi ‘Shell’ olduğunda görünür. 

`Auto Edge-loop (side)` kabuk yanları boyunca kare poligonlar oluşturmak için kenar döngüsü sayısını hesaplar. 

Devre dışı bırakılırsa, `Division` kaydırıcısı yanlardaki bölme sayısını ayarlar.

_Bu, ‘Daha fazla...’ alt menüsünün sonudur._

### Gelişmiş
![](/images/layers_advanced.webp)

#### Üst katman detaylarını koru

Alt katmanlarda büyük değişiklikler yapıldığında, üst katmanlardaki küçük detayların görünür kalmasını sağlar.

Varsayılan olarak, bir katmanda küçük kırışıklıklar yontarsanız ve ardından temel katmanda büyük değişiklikler yaparsanız, kırışıklıklar kaybolur. Bu anahtarı etkinleştirmek, bu küçük detayların her zaman alttaki büyük değişikliklerin üzerinde yüzmesini sağlar. Aşağıdaki videoda, kırışıklık detayının varsayılan olarak nasıl kaldırıldığını, ancak ‘keep top layers details’ etkinleştirildiğinde görünür kaldığını görebilirsiniz:

![](/videos/layers_details.mp4)


#### Arayüz: Listeyi genişlet

Varsayılan katman menüsü, katman görünürlüğünü ve katman opaklığını değiştirmenize olanak tanır. Bu seçeneği etkinleştirmek, her katman için tam kontrolleri genişletir.

![](/images/layers_expand.webp)

#### Dönüşümü senkronize et

Etkinleştirilirse, seçili olmayan tüm katmanlar dönüşümün dönüş, ölçek, eğrilik (skew) değerlerine bağlı olarak ayarlanır. 

Uyguladığınız yeni dönüşüm diğer katmanlarla kullanılmayacaksa bu seçeneği devre dışı bırakın.

`Auto` olarak ayarlandığında, yalnızca görünür katmanlar ayarlanır.
