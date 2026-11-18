# ![](/icons/paint.webp) Boya {#painting}

Boya darbelerinin rengini, pürüzlüğünü ve metalikliğini kontrol eder; boya özelliklerini tüm yüzeye doldurmanıza olanak tanır ve boya araçlarının katmanlar, maskeler ve gizlenmiş seçimlerle nasıl etkileşime gireceğini belirler.

![](/images/paint_overview.webp)  

## Genel bakış {#overview}

Nomad, PBR verteks boyama kullanır. Bu ne anlama geliyor?

### PBR {#pbr}
PBR (Physically Based Rendering, yani fiziksel tabanlı işleme), film, televizyon, oyun ve mobil alanlarında yaygın bir bilgisayar grafiği tekniğidir. Işıklandırmayı fiziksel özelliklere dayandırıp yüzeyleri renk, pürüzlük ve metaliklik ile tanımlayarak, çok çeşitli foto-gerçekçi görünümler elde edilebilir.

### Verteks boyama {#vertex-painting}

Verteks boyama, boya bilgisinin dokularda değil, modelin vertekslerinde saklandığı anlamına gelir. Nomad yüz binlerce, çoğu zaman milyonlarca verteksli modelleri işleyebildiği için modelleriniz son derece ayrıntılı yüzey boyamalarına sahip olabilir: bir ayrıntıyı şekillendirebiliyorsanız, onu boyayabilirsiniz de.

Bu aynı zamanda Nomad'da boyama yapmak için UV haritalama gerekmediği anlamına gelir; UV haritalama diğer 3d uygulamalarında çoğu zaman yavaş ve teknik bir süreçtir. Diğer pek çok 3d uygulaması Nomad'ın işleyebildiği yüksek verteks sayılarını desteklemez; ama Nomad'da bu konuda yardımcı olacak iyi doku pişirme ve azaltma araçları da vardır.

### Dokular {#texturing}

Nomad dokuları destekler, ancak dokuların içe aktarılan bir modelde bulunması ya da verteks boyamasının dokulara pişirilmesiyle elde edilmesi gerekir.

Doku basitçe bir görseldir, ama 3d bağlamında genellikle bir nesneye atanmış bir görseli ifade eder.
Bir görseli bir modelin etrafına sarmak için modelin doku koordinatlarına (UV) ihtiyacı vardır.

Nomad bunları [otomatik olarak hesaplayabilir](topology.md#uv-unwrap), ancak genel kalite üzerinde pek kontrolünüz olmaz.

::: tip
Örnek bir iş akışı:
- Nomad'da şekillendirin, ardından [UV açma](topology.md#uv-unwrap) yapın
- Nomad'da boyamaya zaten başladıysanız [verteks boyamasını dokulara aktarabilirsiniz](topology.md#bake-texture)
- Procreate'e dışa aktarın
- Procreate'te dokulandırın
- İşleme için Nomad'a geri aktarın
:::

Genel bakış bu kadar; şimdi boya menüsünün bölümlerini inceleyelim:


## Darbe boyama {#stroke-painting}
![](/images/paint_intensity.webp)  

Bu araç için boyamayı etkinleştirir; aynı anda hem şekillendirip hem boyamanız gerektiğinde kullanışlıdır. Bir araç boyama yapabildiği halde bu onay kutusu kapalıysa, başlığın yanındaki bir uyarı simgesi bunu size hatırlatır.

Boyamanın asıl işlev olduğu araçlarda (örneğin Boya, Leke, Maske) bu onay kutusu bulunmaz.

### ![](/icons/opacity.webp) Boyama yoğunluğu {#paint-intensity}

Aracın asıl yoğunluğundan farklı bir yoğunluk kullanmanızı sağlayan bir kaydırıcı.

Yanındaki kaydırıcılar düğmesi, aynı anda hem şekillendiren hem boyayan araçlar için yan çubuğa hızlı bir boyama yoğunluğu kaydırıcısı ekler.

`Alfa`, `Düşüş` ve `Yoğunluğu rastgeleleştir` düğmeleri, bu özelliklerin boyamayı etkileyip etkilemeyeceğini belirler. Örneğin kil aracı için rastgeleleştirmeyi açabilirsiniz, ama renk rastgeleleştirilmez.

* `Alfa` - devre dışıyken boyama alfayı yok sayar ve fırça alanının tamamını kaplar. VDM aracında bu düğmenin yerini, damgada saklanan malzemeyi açıp kapatan `Damga malzemesi` alır.
* `Düşüş` - devre dışıyken boyama, fırçanın kenarına kadar tam yoğunlukta kalır.
* `Yoğunluğu rastgeleleştir` - darbe rastgeleleştiricisinin yoğunluk kısmının boyamayı etkileyip etkilemeyeceği. Konum, dönüş ve ölçek rastgeleleştirmesi her zaman damganın tamamını hareket ettirir.

Bu seçenekler [Tümünü boya](#paint-all) tarafından yok sayılır, ama onun üç düzlemli varyantı alfayı kullanır.

### ![](/icons/link.webp) Global malzeme {#global-material}
Bu seçenek etkinse, seçili malzeme diğer araçlarınkiyle aynı olur. Yalnızca pürüzlük, metaliklik ve renk ayarlarının dikkate alındığını unutmayın. Bu araca kendi malzemesini vermek için devre dışı bırakın.


## Malzeme {#material}
![](/images/paint_material.webp) 

İlk simge, bir malzeme önizleme şeklidir. 3d malzeme önizlemesi üzerinde sürüklemek onu döndürür.

İkinci simge, seçili alfa ve düşüş seçenekleriyle boya darbesinin bir önizlemesidir.

### ![](/icons/falloff.webp) Eğriler {#curves}

[PBR kaydırıcılarının](#pbr-sliders) doku yuvaları için bir eğri düzenleyici açar. Doku değerlerini, görsel dosyasına dokunmadan, boyanmadan önce yeniden eşler. Bir doku yuvasındaki küçük eğri simgesi, eğrisinin düzenlendiğini gösterir.

### ![](/icons/cog.webp) Malzeme seçenekleri {#material-options}

Başlığın yanındaki `Malzeme` düğmesi iki ayar içerir.

`Malzeme önizlemesi`, renk, pürüzlük, metaliklik, opaklık ve yoğunluk kaydırıcılarını değiştirirken seçili nesnede ne olacağını belirler:

* `Yok` - Özellikleri ayarlarken model üzerinde hiçbir önizleme gösterilmez
* `Malzeme` - Özellikleri ayarlarken malzeme değerleri nesne üzerinde önizlenir.
* `Üç düzlemli` - Malzeme, üç düzlemli bir projeksiyon olarak önizlenir.

Aşağıdaki renk, pürüzlük, metaliklik ve opaklık onay kutuları, [Malzeme damlalığı](#material-picker) ile hangi kanalların değiştirileceğini seçer.

### ![](/icons/dropper.webp) Malzeme damlalığı {#material-picker}

Damlalık, sahnenizdeki herhangi bir nesneden, imlecin altındaki malzemeyi alır. Yalnızca [Malzeme seçenekleri](#material-options) içinde işaretlenen kanallar değiştirilir.

## Malzeme önayarları {#material-presets}
3d önizleme şekline dokunmak bir malzeme önayarları menüsü açar; bunlar klonlanarak kendi önayarlarınızı tanımlayabilirsiniz.

![](/images/paint_presets.webp) 

`Dokuları göm` seçeneği, bu malzemenin kullandığı dokuların bir kopyasını önayarın içinde saklar. Bu seçenek kapalıyken önayar yalnızca Nomad'ın textures/ klasöründeki dokulara başvurur. Dokulu bir önayarı, dokularını ayrıca göndermeden paylaşmak istediğinizde açın.

`Alfa Kanalını Dahil Et`, fırça alfasını da malzeme önayarına kaydeder.

## PBR kaydırıcıları {#pbr-sliders}
![](/images/paint_sliders.webp) 

[PBR](shading.md#pbr) boyama 4 kanal kullanır:
- `Renk` Boyanacak renk. Damlalık, modelin diğer bölümlerinden veya referans görsellerden renk seçmek için kullanılabilir.
- `Pürüzlük` Bir yüzeyin ne kadar "pürüzlü" veya "pürüzsüz" olduğunu belirtir. Düşük bir pürüzlük değeri, yansımaların keskin olacağı anlamına gelir.
- `Metaliklik seviyesi` Yüzeyin metalik olup olmadığını belirtir. Değer çoğu zaman ya %0 ya da %100 olmalıdır; aradaki değerler istisnai olmalıdır.
- `Opaklık` Malzemenin ne kadar saydam olduğu. Kesin konuşmak gerekirse PBR tanımının bir parçası değildir, ama birçok durumda işe yarar. 1 tamamen opak, 0 saydamdır. Opaklık ile kırılmanın farklı şeyler olduğunu unutmayın; Nomad'da kırılma, kırılma malzemesiyle sağlanır.

Bir malzeme önayarı seçerseniz 3 kanal aynı anda boyanır (opaklık çoğu zaman bilerek hariç tutulur). Yani yalnızca 'kırmızı' boyamak yerine 'kırmızı, pürüzlü bir metal' ya da 'beyaz, pürüzsüz bir plastik' boyayabilirsiniz.

Kare, bir doku yuvasıdır; o özellik için sabit bir değer yerine doku kullanmak üzere ona tıklayın. Bir renk dokusu rengi tonlar; pürüzlük, metaliklik veya opaklık dokusu ise kaydırıcının değerinin yerini alır (bunu göstermek için etiketinin üstü çizilir). Opaklık dokusu için `Alfayı Değer Olarak Kullan`, dokunun gri tonlama değeri yerine alfa kanalını okur.

VDM aracında, damga kendi malzemesini taşıyorsa, doku yuvasının yanında onu gösteren ek bir yuva belirir. Damganın o kanalını kullanmak veya yok saymak için ona dokunun.

Kaydırıcıların yanındaki fırça simgesi, o özelliği nesnenizin tamamına doldurur.

Onay kutusu o özelliği etkinleştirir veya devre dışı bırakır; böylece örneğin yalnızca renk, ya da yalnızca pürüzlük ve opaklık boyayabilirsiniz.

Farklı pürüzlük ve metaliklik değerlerine bazı örnekler:

|                | Metaliklik %0                      | Metaliklik %100               |
| :------------: | :-------------------------------: | :--------------------------: |
| Pürüzlük %0   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Pürüzlük %50  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Pürüzlük %100 | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Pürüzlük ve metaliklik için [Aydınlatılmış (PBR)](shading.md#pbr) gölgelendirme modu gerekir. [MatCap](shading.md#matcap) veya [Aydınlatmasız](shading.md#unlit) modunda yok sayılırlar ve menü bir uyarı gösterir.
:::

::: tip
PBR boyama için doku kullanırken, `Damga` aracı gibi bir araca geçmek ya da darbe menüsünden nokta dışında bir mod seçmek çoğu zaman işe yarar; nokta modu dokuyu bulaştırabilir.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Düşük poligonlu bir nesneye metalik bir yüzey boyuyorsanız, `Yumuşak gölgelendirme` seçeneğini [genel olarak](settings.md#smooth-shading) veya [nesne başına](material.md#smooth-shading) açmayı düşünebilirsiniz.
:::

## ![](/icons/paint.webp) Tümünü boya {#paint-all}

![](/images/paint_paint_all.webp)

Geçerli malzemeyi seçili nesnelere uygular: ya standart modda `Tümünü boya` ile, ya da üç düzlemli bir projeksiyon olarak `Tümünü boya + Üç düzlemli` ile. Üç düzlemli varyant, tamamlanmamış primitiflerde kullanılamaz.

Renk/metaliklik/pürüzlük/opaklık kaydırıcılarının yanındaki onay kutuları dikkate alınır; devre dışı bırakılan özellikler doldurulmaz.

Ek düğmeler, tümünü boya işleminin ayrıca nasıl etkileneceğini kontrol eder. Çoğu bir yüzde gösterir ve hiçbir etkisi olmayacaklarında gri görünürler:

| Simge                        | Açıklama                                   |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | Maskelenmiş alanlar etkilenmez.               |
| ![](/icons/tool_hide.webp) | Gizlenmiş alanlar etkilenmez.               |
| ![](/icons/opacity.webp)   | Yukarıdaki araç boyama faktörünü kullanır.           |
| ![](/icons/layer.webp)     | Bir katmanın boyanmamış alanları etkilenmez. |
| ![](/icons/triplanar.webp) | `Verteks`: üç düzlemli varyant, gösterilen araç yoğunluğuyla yüzeyi alfa ile de kaydırır. |
| ![](/icons/cog.webp)       | Üç düzlemli ayarlarını açar                   |

### ![](/icons/cog.webp) Üç düzlemli ayarları {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

[Malzeme menüsündeki üç düzlemli ayarlarına](material.md#triplanar) benzer şekilde, projeksiyonların karışımını, döşemeyi ve kaydırmaları kontrol edebilirsiniz.

Değerleri ayarlarken kalıcı bir önizleme açmak için bu menünün üstündeki önizleme onay kutusunu kullanın.
