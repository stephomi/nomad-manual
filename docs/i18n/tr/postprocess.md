# ![](/icons/postprocess.webp) Süreç sonrası işlemler {#post-process}

Bu menü, işlemenin görünümünü etkilemek için Nomad'ın birçok yönünü kontrol eder.

![](/images/postprocess_overview_drac.webp)

Süreç sonrası işlemleri kullanmak sahnenizin nihai görünümünü önemli ölçüde değiştirebilir.

![](/images/postprocess_overview.webp)
*Süreç sonrası işlemlerden önce ve sonra aynı sahne; ek ışık veya malzeme değişikliği yok.*

Süreç sonrası işlemler, cihazınıza bağlı olarak performansı çok etkileyebilir.
Tüm süreç sonrası işlemleri devre dışı bırakan genel bir `Süreç sonrası işlemler` onay kutusu vardır; böylece önayarlarınızı kaybetmeden hızlıca şekillendirmeye/modellemeye dönebilirsiniz.
PBR işleme için [Ortam Oklüzyonu](#ambient-occlusion-ssao), [Yansıma](#reflection-ssr) ve [Ton Eşleştirme](#tone-mapping) etkin olmalıdır.

Yine de şekillendirirken, işlemenin kendisine değil şekle odaklanmak için çoğu zaman süreç sonrası işlemleri kapalı tutmak istersiniz.


## Kalite {#quality}

![](/images/postprocess_quality.webp)

Bu seçenekler, performans pahasına işlemenin kalitesini artırır.

### Maks. kare örnekleme {#max-frame-sampling}
Nomad tek bir kare işlemesi için belirli miktarda süreç sonrası işlem hesaplar ve bu gürültülü görünebilir. Bu kontrol, gürültü kaynaklı kusurların çoğunu gidermek için kaç karenin işlenip birbiriyle harmanlanacağını belirler. Bazı efektler ek örnek gerektirmez (örneğin renk düzenleme), yumuşak gölgeler ve küresel aydınlanma gibi diğerleri ise gürültüsüz olmak için yüzlerce örnek gerektirebilir.

Görüntü alanında bunu Nomad'ı kendi haline bıraktığınızda görebilirsiniz: görüntü kalitesi maksimum örnek sayısına kadar yavaş yavaş iyileşir, sonra durur. Durduktan sonra Nomad hiçbir şey yapmaz, bu da pil tasarrufu sağlar. Bu hesaplama sayısı, [Dosyalar menüsündeki](files) işleme bölümünde 'export png' tıklandığında da kullanılır.

Kaydırıcının yanındaki onay kutusu kare örneklemeyi açıp kapatır.

### İşleme Çözünürlüğü {#resolution-multiplier}
Bu kaydırıcı işlemenin çözünürlüğünü kontrol eder. x1.0 değeri, işlemelerin cihazın piksel çözünürlüğünde yapılacağı anlamına gelir. x0.5 değeri yarı çözünürlükte işler; hızlıdır ama kalitesi düşüktür. 1'den büyük bir değer daha büyük bir boyutta işler, sonra küçültür. Bu daha yüksek kalite ve daha az gürültü sağlar, ama işleme süresi uzar.

Performans üzerinde büyük etkisi vardır, bu yüzden x1.25 veya altında tutmaya çalışın. Bu değer ayarlara kaydedilmez ve [Pixel Art](#pixel-art) efekti onu geçersiz kılar.

### ![](/icons/intensity.webp) Maks. örnek {#max-samples}

Performans pahasına süreç sonrası efektlerin kalitesini artırır.

### ![](/icons/material_dithering.webp) Renk Taklidi {#dithering}

Bantlaşma kusurlarını azaltmak için piksellere renk taklidi (dithering) uygular (örneğin gradyanlarda veya vinyette). Genellikle etkin olmalıdır, ama belirli işlemler için kapatılabilir (örneğin derinlik haritaları dışa aktarmak veya veriye özel diğer işlemler).

### ![](/icons/denoise.webp) Gürültü Giderici (oidn) {#oidn}

Tüm kareler biriktirildikten sonra görüntüye bir gürültü giderici uygular. Bu, çok daha düşük örnek sayıları kullanmanıza olanak tanıyabilir. Gürültü giderme işlemciyi yoğun kullanır, bu yüzden yalnızca görüntünüz gürültülüyse etkinleştirin. Her cihazda kullanılamaz.

## Önayar tarayıcısı {#preset-browser}
![](/images/postprocess_presets.webp)
`Süreç sonrası işlemler` başlığının altındaki görsele tıklamak bir süreç sonrası işlem önayarları koleksiyonu gösterir. Mevcut ayarlarınızdan bir önayar oluşturmak için `Yeni` seçeneğini kullanın. Yerleşik önayarlar yalnızca klonlanabilir: kendi önayarınızı tanımlamak için birini seçin, `Klonlama` düğmesine tıklayın ve değişikliklerinizi yapın. Bir önayarda henüz kaydedilmemiş değişiklikler varsa `Kaydedilmemiş değişiklikler!` gösterilir; kaydetmek için önayar görseline tıklayın, önayar tarayıcısının içine tekrar tıklayın ve `Kaydet` seçeneğini seçin.

## Kısayol çubuğu {#shortcut-bar}
Süreç sonrası işlemler etkinken, menünün altındaki bir çubuk tüm efektleri listeler (`SSR`, `SSGI`, `SSAO`, `DoF`, `Parlama`...). Bölümüne atlamak için birine dokunun. Kapalı efektler gri görünür; böylece çubuk, geçerli önayarın ne yaptığının hızlı bir özeti işlevini de görür.

## ![](/icons/postprocess_ssr.webp) Yansıma (SSR) {#reflection-ssr}
Bu seçenekle nesneler, ekranda göründükleri sürece sahnedeki diğer nesneleri yansıtabilir.
Sahnenizde metalik ve parlak nesneler varsa muhtemelen bu seçeneği kullanmalısınız.
Bu seçenek [Aydınlatılmış (PBR)](shading.md#pbr) gölgelendirme modunu gerektirir.


| SSR kapalı                    | SSR açık                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## ![](/icons/postprocess_ssgi.webp) Küresel Aydınlanma (SSGI) {#global-illumination-ssgi}

Küresel aydınlanma, ışığın yüzeyler arasında nasıl sektiğini simüle eder; örneğin kırmızı bir duvar yakındaki beyaz bir nesneye kırmızı yansıtır. Ortam oklüzyonu ve yansımalarla birlikte kullanıldığında bir işlemenin gerçekçiliğini büyük ölçüde artırabilir. Yansımalar gibi, [Aydınlatılmış (PBR)](shading.md#pbr) gölgelendirme modunu gerektirir.

`Şiddet` - Küresel aydınlanmanın yoğunluğu.



| SSGI kapalı                   | SSGI açık                   |
| :------------------------: | :-----------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Kürenin arkasında, tavana yönelmiş bir spot ışık var. SSGI kapalıyken yalnızca tavan aydınlanır. SSGI açıkken ışık tavandan duvarlara, oradan da küreye seker._

## ![](/icons/postprocess_ssao.webp) Ortam Oklüzyonu (SSAO) {#ambient-occlusion-ssao}
Ortam oklüzyonu, ışığın ulaşma ihtimalinin daha düşük olduğu alanları (köşeler vb.) karartır.
Efekt yalnızca modelin geometrisine bağlıdır.

* `Şiddet`- Efektin yoğunluğu.
* `Büyüklük`- Efektin ne kadar geniş bir alana yayıldığı.
* `Kalınlık` - Engelleyen nesneler için varsayılan derinlik kalınlığı, `Büyüklük` değerinin yüzdesi olarak.
* `Ton` - Oklüzyonla çarpılan bir renk; yaratıcı efektler için kullanılır.


| SSAO kapalı                    | SSAO açık                    |
| :-------------------------: | :------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO en çok, ağırlıklı olarak ortam ışığıyla aydınlanan alanlarda görünür. Güçlü doğrudan ışık alan alanlarda AO efekti çok daha zayıf olur.

:::

## ![](/icons/postprocess_dof.webp) Alan Derinliği {#depth-of-field-dof}
Odak dışındaki bölgeye bir bulanıklık efekti ekler.

Odak noktasını değiştirmek için modelinize dokunmanız yeterli.

* `Diyafram modu` - Bulanıklığı, aşağıdaki iki bulanıklık kaydırıcısı yerine tek bir kamera diyaframıyla yönetir.
* `Diyafram` (_yalnızca diyafram modunda_) - Gerçek bir fotoğraf makinesindeki gibi objektifin f-sayısı. Daha düşük bir değer diyaframı açar ve daha fazla bulanıklaştırır.
* `Uzaklık bulanıklığı` - Odak noktasının uzak tarafına uygulanacak bulanıklık miktarı.
* `Yakınlık bulanıklığı` - Odak noktası ile kamera arasına uygulanacak bulanıklık miktarı.


| DOF kapalı                   | DOF uzaktaki halkaya odaklı       | DOF yakındaki halkaya odaklı    |
| :-----------------------: | :-------------------------: | :------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp) |


## ![](/icons/sun.webp) Parlama {#bloom}
Parlama, sahnenizin parlak bölgelerinin ışıldamasını sağlar.

* `Yoğunluk` - efektin gücü.
* `Yarıçap` - Efektin yayılımı.
* `Eşik` - Piksellerin parlamaya başlaması için sahnede ne kadar parlak olmaları gerektiği. 0'da her şey parlar; yüksek bir değer yalnızca en parlak piksellerin parlamasına izin verir.
* `Ton` - yaratıcı efektler için parlamaya eklenebilecek bir renk.

| Parlama kapalı                    | Yarıçap 0 ile parlama         | Yarıçap 1 ile parlama         |
| :--------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## ![](/icons/postprocess_tone.webp) Ton Eşleştirme {#tone-mapping}
Ton eşleştirme, HDR değerlerini `[0, 1]` aralığına yeniden eşleyen bir işlemdir.
Bunu kullanmazsanız (veya `Yok` seçerseniz), 1'den büyük her renk bileşeni kırpılır.
Bu aralığın üzerindeki tüm renk farklılıkları da kaybolur.

* `Yok/Nötr/Agx/ACES` - hangi ton eşleyicinin kullanılacağı. `Yok` hiçbir yeniden eşleme yapmaz (ama diğer kontroller yine çalışır). Diğer seçenekler farklı film türleri seçmeye benzer; aşırı pozlanmış değerleri ve renkleri farklı şekillerde ele alırlar. Bu çok derin bir konu; daha fazla bilgi için ton eşleştirme, Agx ve ACES hakkında araştırma yapın!
* `Pozlandırma` - görüntülerin genel parlaklığı; bir fotoğraf makinesinde diyaframı ayarlamaya benzer. Bir görüntüyü topluca aydınlatmanın veya karartmanın hızlı bir yolu olabilir.
* `Doygunluk` - renk gücü. 1 nötrdür, 0 tek renklidir (monokrom), 1'in üzerindeki değerler giderek daha doygun olur.
* `Kontrast` - Koyuları daha koyu, açıkları daha açık yapar. Dikkatli kullanın, yüksek değerlerde kusurlara yol açabilir.

`Ton Eşleştirme` devre dışıyken bazı ayrıntıların, pikseller fazla parlak olduğu için kaybolduğuna dikkat edin.

| Ton Eşleştirme kapalı            | Ton Eşleştirme açık            |
| :-------------------------: | :------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Ton eşleştirme, küresel aydınlanmanın etkisini güçlendirebilir. Ortam haritasının yoğunluğunu düşürüp ana ışık kaynağını artırırsanız, sekme ışığı efektlerini daha çok görmek için ton eşleştirmenin `Pozlandırma` değerini yükseltebilirsiniz.
:::

## ![](/icons/postprocess_tone_curve.webp) Renk Düzenleme {#color-grading}
Photoshop'taki eğriler aracına benzer şekilde, görüntüdeki rengin dengesini ve dağılımını kontrol etmenizi sağlar. `Ana` kontrolü tüm renk dengesini etkiler, `Kırmızı`/`Yeşil`/`Mavi` kontrolleri ise ince ayar yapmanızı sağlar.

| Renk Düzenleme kapalı             | Renk Düzenleme açık             |
| :---------------------------: | :--------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## ![](/icons/postprocess_cavity.webp) Eğrilik {#curvature}
Eğriliğin hızlı değiştiği yerleri algılar ve bu bölgelere bir renk uygular.

* `Faktör` - efektin genel yoğunluğu
* `Yumru` - keskin dışbükey değişiklikleri ne kadar bulacağı ve seçilen rengi oraya ne kadar uygulayacağı (varsayılan olarak beyaz)
* `Boşluk` - içbükey değişiklikleri ne kadar algılayacağı ve seçilen rengi oraya ne kadar uygulayacağı (varsayılan olarak siyah)
* `Kalınlık` - algılanan kenarların ne kadar geniş olduğu.

`Yumru` ve `Boşluk` seçeneklerinin yanında, bir renk örneği rengi seçer, küçük bir düğme de bu rengin görüntüyle nasıl karışacağını seçer.


| Eğrilik kapalı                    | Eğrilik açık                   |
| :------------------------------: | :----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## ![](/icons/postprocess_chromatic.webp) Kromatik aberasyon {#chromatic-aberration}
Işığın ekran kenarlarında renklerine ayrışmasıyla oluşan objektif kusurlarını simüle eder.

* `Şiddet` - görüntünün kırmızı/yeşil/mavi bileşenlerinin ekran kenarlarına doğru ne kadar ayrışacağı

| Kromatik kapalı                 | Kromatik açık                 |
| :---------------------------: | :--------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## ![](/icons/postprocess_vignette.webp) Vinyet {#vignette}
Ekran kenarlarını karartarak objektif kusurlarını simüle eder.

* `Büyüklük` - Görüntünün üzerine yerleştirilen ters bir elipsin büyüklüğü
* `Sertlik` - Elipsin görüntünün üzerine ne kadar yumuşak veya keskin karıştığı.
* `Ton` - Vinyetin rengi, varsayılan olarak siyah.


| Vinyet kapalı                    | Vinyet açık                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## ![](/icons/postprocess_grain.webp) Tanecik {#grain}
Bir tanecik (gren) efekti ekler; görüntünün biraz daha az yapay görünmesine yardımcı olabilir.

* `Şiddet` - görüntüye eklenen tanecik/gürültü miktarı.


| Tanecik kapalı                    | Tanecik açık                   |
| :--------------------------: | :------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## ![](/icons/sharpen.webp) Keskinlik {#sharpness}
Photoshop'takine veya fotoğraf düzenleme uygulamalarındakine benzer bir keskinleştirme efekti.

* `Şiddet` - görüntüye uygulanan keskinleştirme miktarı.


| Keskinlik kapalı                  | Keskinlik açık                 |
| :----------------------------: | :--------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## ![](/icons/postprocess_pixel_art.webp) Pixel Art {#pixel-art}
Retro oyunların piksel sanatını simüle eder. Bu efekt [İşleme Çözünürlüğü](#resolution-multiplier) ayarını geçersiz kılar.

* `Kaydırıcı` - piksellerin büyüklüğü
* `Kare örneklemeye izin ver` - çok sayıda siyah piksel görüyorsanız bunu açmayı deneyin. Bu seçenek kapalıyken pixel art efekti [kare örneklemeyi](#max-frame-sampling) kapatır.

| Piksel kapalı                   | Piksel açık                   |
| :-------------------------: | :------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## ![](/icons/postprocess_scanline.webp) Tarama çizgisi {#scanline}
Eski CRT monitörlerin görünümünü simüle eder.

* `Faktör` - çizgilerin gücü
* `Aralık` - çizgilerin büyüklüğü

| Tarama çizgisi kapalı                   | Tarama çizgisi açık                   |
| :----------------------------: | :---------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |
