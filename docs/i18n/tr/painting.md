# ![](/icons/paint.webp) Boyama  

Boya darbelerinin renk, pürüzlülük, metalliğini kontrol edin; boya özniteliklerini taşma (flood fill) ile doldurun ve boya araçlarının katmanlar, maskeler, gizli seçimlerle nasıl etkileşime girdiğini ayarlayın.

![](/images/paint_overview.webp)  

## Genel Bakış

Nomad, PBR vertex boyama kullanır. Bu ne anlama geliyor?

### PBR
PBR, yani Fiziksel Tabanlı Görselleştirme, film, televizyon, oyunlar ve mobil için popüler bir bilgisayar grafiği tekniğidir. Işıkları fiziksel özelliklere dayandırarak ve yüzeyleri renk, pürüzlülük, metanlık ile tanımlayarak çok çeşitli fotogerçekçi görünümler elde edilebilir.

### Vertex boyama

Vertex boyama, boya bilgisinin dokularda değil, modelin vertekslerinde saklandığı anlamına gelir. Nomad yüz binlerce, çoğu zaman milyonlarca verteksi olan modelleri işleyebildiği için, modellerinizin son derece detaylı yüzey boyamasına sahip olması gerekir; eğer detayı yontabiliyorsanız, o detayı boyayabilirsiniz de.

Bu aynı zamanda Nomad'de boyamanın, diğer 3B uygulamalarda genellikle yavaş ve teknik bir süreç olan UV eşleme gerektirmediği anlamına gelir. Birçok diğer 3B uygulama, Nomad'in desteklediği yüksek vertex sayılarını desteklemez, ancak Nomad'in ayrıca iyi doku pişirme (baking) ve küçültme (decimation) araçları da vardır.

### Dokulandırma

Nomad dokuları destekler, ancak bunların içe aktarılan bir modelde mevcut olması ya da vertex boyamayı dokulara pişirerek elde edilmesi gerekir. 

Bir doku basitçe bir görüntüdür, ancak 3B bağlamda genellikle bir nesneye atanmış bir görüntü anlamına gelir.
Bir görüntüyü bir modelin etrafına sarmak için modelin doku koordinatlarına (UV) ihtiyacı vardır.

Nomad bunları [otomatik olarak hesaplayabilir](topology.md#uv-unwrap), ancak genel kalite üzerinde fazla kontrolünüz olmaz.

::: tip
Örnek bir iş akışı:
- Nomad'de yontun, ardından [UV açma işlemi yapın](topology.md#uv-unwrap)
- Eğer Nomad'de boyamaya zaten başladıysanız, [vertex boyamayı dokulara aktarabilirsiniz](topology.md#bake-vertex-colors-to-texture)
- Procreate'e dışa aktarın
- Procreate'te dokulandırın
- Render amacıyla tekrar Nomad'e aktarın
:::

Genel bakış bu kadar, şimdi boyama menüsünün bölümlerini inceleyelim:


## Darbe boyama
![](/images/paint_intensity.webp)  

Bu araç için boyamayı etkinleştirin; aynı anda hem yontmanız hem de boyamanız gerektiğinde kullanışlıdır.

Boyamanın birincil işlev olduğu araçlarda (örn. Paint, Smudge, Mask) bu onay kutusu yoktur.

### Boya yoğunluğu

Birincil araç yoğunluğundan farklı bir yoğunluk kullanmanıza izin veren bir kaydırıcı.

`Alpha`, `Falloff` ve `Randomize` onay kutuları, bu özelliklerin boyamayı etkileyip etkilemeyeceğini belirler. Örneğin, kil aracı için rastgeleleştirmeyi etkinleştirmiş olabilirsiniz, ancak renk rastgeleleştirilmeyebilir.


## Malzeme
![](/images/paint_material.webp) 

İlk simge bir malzeme önizleme şeklidir. 3B malzeme önizlemesi üzerinde sürüklemek onu döndürür. 

İkinci simge, seçili alfa ve düşüş (falloff) seçenekleriyle boya darbesinin bir önizlemesidir.

Malzeme başlığının yanındaki önizleme düğmesi, None, Material veya Triplanar arasında geçiş yapmanızı sağlar. Bu, boya özelliklerini etkileşimli olarak değiştirdiğinizde ne olacağını belirler:

* `None` - Özellikleri ayarlarken model üzerinde hiçbir önizleme gösterilmez
* `Material` - Özellikleri ayarlarken malzeme değerleri nesne üzerinde önizlenir. Dokular kullanıyorsanız ve modelin UV'leri varsa, UV'ler kullanılır.
* `Triplanar` - Malzeme, Triplanar projeksiyon olarak önizlenir. 

Damlalık, sahnenizdeki bir nesneden tüm özellikleri örneklemek için kullanılabilir.

## Malzeme Ön Ayarları
3B önizleme şekline dokunmak, malzemelerin bir ön ayar menüsünü açar; bunlar kendi ön ayarlarınızı tanımlamak için klonlanabilir.

![](/images/paint_presets.webp) 

`Embed Textures` ve `Alpha` anahtarları etkinleştirildiğinde, bu malzeme tarafından kullanılan tüm dokular ön ayar içinde saklanır. Bu aşağıda daha ayrıntılı açıklanmıştır.

## PBR kaydırıcıları
![](/images/paint_sliders.webp) 

[PBR](shading.md#pbr) boyama 4 kanal kullanır:
- `Color` Boyanacak renk. Damlalık, modelin diğer kısımlarından veya referans görüntülerden renk seçmek için kullanılabilir.
- `Roughness` Bir yüzeyin ne kadar "pürüzlü" veya "düzgün" olduğunu belirtir. Düşük pürüzlülük değeri, yansımaların keskin olacağı anlamına gelir.
- `Metalness` Yüzeyin metalik olup olmadığını belirtir. Değer çoğu zaman ya %0 ya da %100 olmalıdır, aradaki değerler istisnai olmalıdır.
- `Opacity` Malzemenin ne kadar görülebilir olduğunu belirtir. Teknik olarak PBR spesifikasyonunun bir parçası değildir, ancak birçok durumda kullanışlıdır. 1 tamamen opak, 0 şeffaftır. Opaklık ve kırılmanın farklı şeyler olduğuna dikkat edin; Nomad'de kırılma, kırılma (refraction) malzemesiyle ele alınır. 

Bir malzeme ön ayarı seçerseniz, 3 kanal aynı anda boyanır (opaklık genellikle kasıtlı olarak hariç tutulur). Bu, yalnızca 'kırmızı' boyamak yerine, 'kırmızı pürüzlü metal' veya 'beyaz düzgün plastik' boyayabileceğiniz anlamına gelir.

Kare, bir doku yuvasıdır; bu özelliğe katı bir değer yerine bir doku kullanmak için üzerine tıklayın.

Kaydırıcıların yanındaki fırça simgesi, bu özelliği nesneniz üzerinde taşma (flood fill) ile doldurur.

Onay kutusu, belirli bir özelliği etkinleştirir veya devre dışı bırakır; böylece yalnızca rengi boyayabilir veya örneğin yalnızca pürüzlülük ve opaklığı boyayabilirsiniz. 

İşte farklı pürüzlülük ve metanlık özelliklerine bazı örnekler:

|                | Metalness 0%                      | Metalness 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Roughness 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Roughness 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Roughness 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
[Matcap render](shading.md#matcap) modunda yalnızca renk desteklenir, metanlık ve pürüzlülük yok sayılır.
:::

::: tip
PBR boyama için dokular kullanırken, genellikle `Stamp` gibi bir araca geçmek veya dokuyu bulaştırabilen nokta (dot) dışındaki bir modu kullanmak için darbe menüsünü kullanmak faydalıdır.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Daha düşük poligon sayısına sahip bir nesne üzerinde metalik bir yüzey boyuyorsanız, `Smooth Shading` özelliğini [genel](settings.md#smooth-shading) veya [nesne bazında](material.md#smooth-shading) açmayı düşünebilirsiniz.
:::

## Tümünü boya

![](/images/paint_paint_all.webp)

Geçerli malzemeyi nesneye, standart modda 'Paint All' ile veya Triplanar projeksiyon olarak uygulayın.

Renk/metanlık/pürüzlülük/opaklık kaydırıcılarının yanındaki onay kutuları dikkate alınır; devre dışı bırakılan özellikler doldurulmaz.

Ek düğmeler, tümünü boya işleminin nasıl daha fazla etkilenebileceğini kontrol eder:

| Icon                        | Açıklama                                      |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/tool_mask.webp) | Maskelenmiş alanlar etkilenmez.               |
| ![](/icons/tool_hide.webp) | Gizli alanlar etkilenmez.                     |
| ![](/icons/opacity.webp)   | Yukarıdaki araç boyama faktörünü kullan.      |
| ![](/icons/layer.webp)     | Bir katmanın boyanmamış alanları etkilenmez.  |
| ![](/icons/triplanar.webp) | Triplanar ayarlarının göstergesi              |
| ![](/icons/cog.webp)       | Triplanar ayarlarını aç                       |

### Triplanar ayarları
![](/images/paint_triplanar_settings.webp)

[Malzeme menüsündeki triplanar ayarlarına](material.md#triplanar) benzer şekilde, projeksiyonların karışımını, döşemeyi (tiling) ve ofsetleri kontrol edebilirsiniz. 

Değerleri ayarlarken kalıcı bir önizleme etkinleştirmek için bu menünün üst kısmındaki önizleme onay kutusunu kullanın.

## Global malzeme
Bu seçenek etkinleştirilirse, seçili malzeme diğer araçlarla aynı olur. Yalnızca pürüzlülük, metanlık ve renk ayarlarının dikkate alındığını unutmayın.
