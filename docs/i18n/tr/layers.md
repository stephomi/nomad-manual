# ![](/icons/layer.webp) Katmanlar {#layers}

Bu menü katman yığınını içerir: nesnenizdeki düzenlemeleri tahribatsız bir şekilde saklamanın bir yolu ve katmanları birleştirip yeniden kullanmanın birçok yolu.

![](/images/layers_overview.webp) 

## Genel bakış {#overview}

Nomad'da katmanların birden fazla amacı vardır.

Boya bilgileri (Renk, Pürüzlük, Metaliklik, Opaklık), 2d boyama uygulamalarındakine benzer şekilde katmanlarla çalışır. Bir katman oluşturulabilir ve modele boya uygulanabilir. Katman açılıp kapatılabilir, opaklığı ayarlanabilir, çoğaltılabilir, katman yığınındaki sırası değiştirilebilir ve karışım modu ayarlanabilir.

Nomad katmanları şekillendirme için de kullanır. Bir katman kırışıklıklar gibi ince ayrıntıları saklayabilir ya da büyük değişiklikleri saklayarak diğer 3d uygulamalarındaki blendshape/shape key/morph target gibi çalışabilir. Örneğin farklı yüz ifadelerini farklı katmanlarda şekillendirip, katman kaydırıcılarını ayarlayarak bunları yeni ifadelerde birleştirebilirsiniz.

Bu durumda bir katmanda saklanan değişiklikler tamamen toplanır; katman sırası, boyadaki gibi önem taşımaz.

Katmanlar [KatmanSil](tools.md#delete-layer) aracıyla kısmen silinebilir; ayrıca katmanlar, içlerinde saklanan farklı bilgilere dayanarak maske oluşturmak için de kullanılabilir.

![](/videos/layer.mp4)

::: tip
Çoğu şekillendirme yazılımının aksine, bir ağ örgüsünün topolojisini değiştirmek katmanları silmez. [Voksel yeniden ağ örgülendirme](topology.md#voxel-remesher), [Çoklu Çözünürlük](topology.md#multiresolution) veya [Kes](tools.md#trim)/[Ayır](tools.md#split) araçlarını kullanabilirsiniz; ancak [Voksel yeniden ağ örgülendirme](topology.md#voxel-remesher) kullanırken katmanın kalitesinin etkileneceğini unutmayın.
:::

::: tip
Katmanları blendshape/morph target olarak kullanıyorsanız, [sahne menüsünde](scene.md#object-menu) ek katman işlevleri bulunur: katmanları nesnelere ayırabilir ve eşleşen nesneleri katmanlarda birleştirebilirsiniz.
:::
----

## Katman menüsü {#layer-menu}

![](/images/layers_menu.webp)

Başlık seçili nesnenin adını gösterir. Katmanlar primitiflerde kullanılamaz, bu yüzden önce primitifi tamamlayın.

Yeni bir katman oluşturmak için `Katman ekle` düğmesine basın. `Katmanları Birleştir`, tüm katmanları taban ağ örgüsüne birleştirir; simgesinin yanındaki sayı kaç katman olduğunu gösterir.

Her katmanın bir adı, gücünü/faktörünü kontrol eden bir kaydırıcısı ve seçenek düğmeleri vardır. Bir katmana dokunarak onu etkin katman yapın: şekillendirme ve boyama o katmana gider. Yeniden taban ağ örgüsü üzerinde çalışmak için `Taban` satırına dokunun.

### ![](/icons/sort_right.webp) Listeyi genişlet {#ui-expand-list}

Varsayılan olarak katman listesi her katmanın yalnızca görünürlüğünü, karışım modunu ve gücünü gösterir; etkin katman ise tüm kontrolleriyle genişletilmiş olarak görünür. Başlığın solundaki ok, her katmanın tüm kontrollerini genişletir.

![](/images/layers_expand.webp)

### Seçenekler {#options}

| Eylem       | Simge                         | Açıklama                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Görülebilir      | ![](/icons/eye_open.webp)   | Katmanı gösterir/gizler                                 |
| Karışım   | ![](/icons/opacity.webp)    | Photoshop tarzı karışım modu. 4 simge, Renk, Pürüzlük, Metaliklik ve Opaklık için modları gösterir.                                 |
| Yeniden Adlandır    | ![](/icons/pencil.webp)     | Katmanın adını düzenler                                 |
| Sil       | ![](/icons/trash.webp)      | Katmanı siler                                    |
| Çoğalt    | ![](/icons/clone.webp)      | Katmanı çoğaltır                                 |
| Aşağı birleştir   | ![](/icons/merge_down.webp) | Katmanı alttaki katmanla (veya taban ağ örgüsüyle) birleştirir |
| Daha fazla         | ![](/icons/more.webp)       | [Daha fazla...](#more) seçenek                            |

Bir katman genişletilmemişse, `Yeniden Adlandır`, `Sil`, `Çoğalt` ve `Aşağı birleştir` onun [Daha fazla...](#more) menüsünde bulunur.

Bir katmanı katman yığınının başka bir yerine taşımak için adına basılı tutun, ardından sürükleyin.

### Taban {#base}

`Taban` satırındaki 3 nokta düğmesi, `Taban → Katman` düğmesiyle taban ağ örgüsünün boyasını yeni bir katmana taşır. Taban daha sonra arka plan malzemesine sıfırlanır. Herhangi bir katman oluşturmadan önce çok fazla boyama yaptıysanız bu çok kullanışlıdır.

* Yanındaki maske ve gizleme düğmeleri, maskelenmiş ve gizlenmiş alanlara dokunmaz.
* `Çıkar` - taşınacak kanallar: `Renk`, `Opaklık`, `Pürüzlük` ve `Metaliklik seviyesi`.
* `Arka plan malzemesi` - etkinse, yalnızca bu malzemeden farklı olan değerler taşınır. Kaydırıcılarla ayarlayın ya da damlalıkla modelden alın.

### ![](/icons/more.webp) Daha fazla... {#more}

'Daha fazla...' düğmesi, geçerli katman için iki sekmede ek seçenekler gösterir: ayarlar (dişli simgesi) ve çıkarma (küp simgesi).

![](/images/layers_more.webp) 

#### Kanal faktörleri {#channel-factors}

Bu kontroller, katman için şekillendirme/renk/pürüzlük/metaliklik/opaklık miktarını ölçeklendirmenizi sağlar. Bu değerler katmanın faktör kaydırıcısıyla çarpılır; örneğin katman gücü 1 ama renk kanalı faktörü 0,5 ise, görüntülenen renk 0,5 güçte olur.

`Kaydırma`, katmanın şekillendirme gücünü kontrol eder. Renk/pürüzlük/metaliklik 0 ile 1 arasında sınırlıyken, kaydırma pozitif ya da negatif herhangi bir değer olabilir.

::: tip
Kaydırma, bir tümsek katmanını bir çukur katmanına ya da bir gülümsemeyi kaş çatmaya dönüştürmek için kullanılabilir:
![](/videos/layer_happysad.mp4)


Simetrik bir katman klonlanabilir, ardından KatmanSil ile sol/sağ şekillere ayrılabilir:
![](/videos/layer_leftright.mp4)

Negatif kaydırma faktörlü katmanlar, yeni pozitif şekiller elde etmek için boş katmanlara pişirilebilir.

1'in üzerinde pozitif kaydırma faktörlü katmanlar, daha uç blendshape'ler denemek için kullanılabilir.
:::

::: warning
Şu an için katmanlar, 3 kanal (renk/metaliklik/pürüzlük) için tek bir opaklık kanalını paylaşır.
Tam yoğunlukta olmayan kanal başına yoğunluklara sahip birden fazla katmanı birleştirirseniz, nihai sonuç farklı görünebilir.

Belki ileride, bu sınırlamayı kaldırmak için her kanalın kendi alfa kanalı olur.
:::


#### ![](/icons/shield.webp) Maske {#mask}
Her kaydırıcının yanındaki maske düğmesi, o kanaldan bir maske oluşturur. Boyama uygulamalarında seçim yapmak için katmanları kullanmaya benzer şekilde, bir katmanda yaptığınız çalışmayı başka işlemler için yeniden kullanmanızı sağlar.

#### ![](/icons/preview.webp) Önizleme {#preview}
![](/images/layers_preview.webp) 

Aşağıdaki seçenekler 'Daha fazla...' menüsünün çıkarma sekmesindedir.

Etkinleştirildiğinde, bu katmanın çıkarma ayarlarını önizler (bir sonraki bölüme bakın).

`X-Ray`, önizleme sırasında hangi nesnelerin saydam yapılacağını seçer (`Yok`, `Seçilmemiş`, `Seçilen` veya `Tümü`); böylece çıkarılan şekil katı kalır. Negatif çıkarma yükseklikleri kullanıyorsanız kullanışlıdır.

#### ![](/icons/mask_extract.webp) Çıkar {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

`Çıkar` düğmesi, katmanın içeriğini yeni bir nesneye çoğaltır; genellikle bir sonraki bölümde kullanıcının belirlediği bir kalınlıkla.

`Kapatma eylemi:` çoğaltmanın nasıl yapılacağını belirler:

* `Yok` - Parçayı yalnızca çıkarır; yan yüzeyler oluşturmaya veya delikleri doldurmaya çalışmaz.
* `Doldur` - Delik üçgenlerle doldurulur ve pürüzsüzleştirilir. Bu seçeneği düz yüzeyler için kullanmayın.
* `Kabuk` - Çıkarılan şekli, kalınlık değeri ve yön seçenekleriyle kapatır.
* `Katman` - Katman farkını çıkarır.

#### ![](/icons/height.webp) Yükseklik {#thickness}
![](/images/layers_thickness.webp) 

Kabuk ekstrüzyonunun derinliği. Pozitif değerler yüzeyden dışarı, negatif değerler yüzeyin içine doğru büyür. Kapatma eylemi `Katman` olduğunda gizlenir.

Bu değerin yanındaki artı/eksi, ekstrüzyonun yönünü belirler:
* Eksi ( - ) mevcut yüzeyden başlar ve aşağı doğru ekstrüde eder.
* Artı ( + ) mevcut yüzeyden başlar ve yukarı doğru ekstrüde eder.
* ArtıEksi ( ± ) ekstrüzyonun üstünü ve altını eşit miktarda uzaklaştırır; böylece ekstrüzyon orijinal yüzeye yarı yarıya gömülü olur.

#### Yanlar {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Bu bölüm, kapatma eylemi `Kabuk` olduğunda görünür.

`Duvar bölümleri`, kabuğun yanları boyunca bölüm sayısını belirler. `Otomatik` anahtarı açıkken Nomad, kare poligonlar oluşturmak için gereken kenar döngüsü sayısını hesaplar.

#### Düzleştirme seviyesi {#smoothness}
![](/images/layers_smoothness.webp) 

Çıkarılacak bölgenin kenarları tırtıklıysa, onları daha güzel bir şekle pürüzsüzleştirmek için bu seçeneği etkinleştirin. `Tümü` çıkarılan yüzeyin tamamını, `Yalnızca kenarlar` ise yalnızca kenarlarını pürüzsüzleştirir. `İterasyonlar` pürüzsüzleştirmenin ne kadar güçlü olacağını belirler.

_'Daha fazla...' alt menüsü burada sona eriyor._

### ![](/icons/cog.webp) Gelişmiş {#advanced}
![](/images/layers_advanced.webp)

Menünün altındaki `Gelişmiş` düğmesi, nesnenin katmanları olduğunda görünür.

#### Üst katmanların detaylarını koru {#keep-top-layers-details}

Alt katmanlarda büyük değişiklikler yapıldığında üst katmanlardaki küçük ayrıntıların görünür kalmasını sağlar. Siz şekillendirirken üst katmanlardan gelen deformasyon yok sayılır, ama ayrıntıları görünür kalır. Yalnızca bu üst katmanlar görece küçük ayrıntılar içeriyorsa iyi çalışır.

Varsayılan olarak, bir katmanda küçük kırışıklıklar şekillendirip ardından taban katmanda büyük değişiklikler yaparsanız kırışıklıklar kaybolur. Bu seçeneği etkinleştirmek, bu küçük ayrıntıların alttaki büyük değişikliklerin üzerinde her zaman yüzmesini sağlar. Aşağıdaki videoda, kırışıklık ayrıntısının varsayılan olarak nasıl silindiğini, ama 'Üst katmanların detaylarını koru' etkinken nasıl görünür kaldığını izleyin:

![](/videos/layers_details.mp4)


#### Dönüşümü Senkronize Et {#sync-transform}

Açıkken, Gizmo veya Dönüştür araçlarını kullandığınızda seçili olmayan tüm katmanlar dönüşümün döndürme, ölçek ve yatırma değerlerine göre ayarlanır. `Otomatik`, `Hayır` veya `Evet` olabilir.

Diğer katmanlar, uyguladığınız yeni dönüşüm olmadan kullanılmak üzere tasarlanmışsa bu seçeneği devre dışı bırakın.

`Otomatik` olarak ayarlandığında yalnızca görünür katmanlar ayarlanır.
