# ![](/icons/postprocess.webp) Post process 

Bu menü, render görünümünü etkilemek için Nomad’in birçok yönünü kontrol eder.

![](/images/postprocess_overview_drac.webp)

Post process kullanmak, sahnenizin nihai görünümünü önemli ölçüde değiştirebilir.

![](/images/postprocess_overview.webp)
*Aynı sahne, post process öncesi ve sonrası, ek ışık veya malzeme değişikliği olmadan.*

Post process, cihazınıza bağlı olarak performansı ciddi şekilde etkileyebilir.
Ayarlarınızı kaybetmeden hızlıca heykel/modelleme moduna dönebilmeniz için tüm post process’i devre dışı bırakan genel bir onay kutusu vardır.
PBR render için, [Ambient Occlusion](#ambient-occlusion-ssao), [Reflection](#reflection-ssr) ve [Tone Mapping](#tone-mapping) etkin olmalıdır.

Bununla birlikte, çoğu zaman heykel yaparken post process’in kapalı olmasını istersiniz; böylece render’ın şekline odaklanabilirsiniz.


## Quality

![](/images/postprocess_quality.webp)
### Max frame sampling
Nomad, tek bir kare render için belirli miktarda post process hesaplar; bu da gürültülü görünebilir. Bu kontrol, kaç kare render edileceğini ve ardından gürültülü artefaktların çoğunu gidermek için birbirine karıştırılacağını belirler. Bazı efektler ek örnek gerektirmez (ör. color grading), buna karşın global illumination gibi diğerleri gürültüsüz olmak için yüzlerce örnek gerektirebilir. 

Viewport’ta bu, Nomad kendi haline bırakıldığında görülebilir; görüntü kalitesi maksimum örneğe kadar kademeli olarak iyileşir, sonra durur. Bu hesaplama sayısı, [Files menüsü](files) altındaki render bölümünde ‘export png’ tıklandığında da kullanılır.

### Resolution multiplier
Bu kaydırıcı, post process çözünürlüğünü kontrol eder. x1.0 değeri, render’ların cihazın piksel çözünürlüğünde yapıldığı anlamına gelir. x0.5 değeri, yarı çözünürlükte render eder; bu hızlıdır ama düşük kalitelidir. 1’den büyük bir değer, daha büyük boyutta render edip sonra küçültür. Bu, daha yüksek kalite, daha az gürültü ama daha uzun render süreleriyle sonuçlanır.

### Max samples

Bu, post process kalitesini artırır, ancak genellikle `Full resolution` daha fazla etkiye sahiptir. 

### Full resolution
Etkinleştirildiğinde, resolution multiplier’ı x1.0’a zorlar.

### Denoiser (oidn)

Görüntüye bir denoiser uygular. Bu, çok daha düşük örnek sayıları kullanmanıza izin verebilir. Yalnızca `Full Resolution` etkinse çalışır. Denoise işleminin tüm örnekler hesaplandıktan sonra gerçekleştiğini ve işlemci açısından yoğun olabileceğini unutmayın.

## Preset browser
![](/images/postprocess_presets.webp)
Görsele tıklamak, bir post process preset koleksiyonu gösterir. Kendi preset’lerinizi tanımlamak için birini seçin, ‘clone’a tıklayın, değişiklik yapın. Kaydetmek için preset görseline tıklayın, preset tarayıcısının içinde tekrar tıklayın ve ‘save’i seçin.


## Reflection (SSR)
Bu seçenekle, nesneler sahnedeki diğer nesneleri, bu nesneler ekranda görünür olduğu sürece, yansıtabilir.
Sahnenizde metalik ve parlak nesneler varsa, bu seçeneği muhtemelen kullanmalısınız.
Bu seçenek yalnızca PBR modunda etkilidir.


| SSR off                    | SSR on                    |
| :------------------------: | :-----------------------: |
| ![](/images/ssr_off.webp) | ![](/images/ssr_on.webp) |

## Global Illumination (SSGI)

Global illumination, ışığın yüzeyler arasında nasıl sektiğini simüle eder; örneğin kırmızı bir duvar, yakındaki beyaz bir nesneye kırmızı ışık yansıtacaktır. Ambient occlusion ve yansımalarla birlikte kullanıldığında, bir render’ın gerçekçiliğini büyük ölçüde artırabilir. 

`Strength` - Global illumination yoğunluğu. 



| SSGI off                     | SSGI on                    |
| :--------------------------: | :------------------------: |
| ![](/images/ssgi_off.webp) | ![](/images/ssgi_on.webp) |

_Bir spot ışık kürenin arkasında, tavana doğru yöneltilmiş. SSGI kapalıyken yalnızca tavan aydınlanıyor. SSGI açıkken ışık tavandan duvarlara, oradan da küreye sekerek yayılıyor._

## Ambient Occlusion (SSAO)
Ambient occlusion, ışığın ulaşma şansının daha az olduğu bölgeleri (köşeler vb.) karartır.
Etki yalnızca model geometrisine bağlıdır.

* `Strength`- Etkinin yoğunluğu.
* `Size`- Etkinin ne kadar yaygın olduğu.
* `Curvature bias` - Etkinin, yüzeydeki değişimlere göre ne kadar hassas olduğu.
* `Color` - Creative efektler için, occlusion’a çarpılan bir renk tonu.


| SSAO off                     | SSAO on                     |
| :--------------------------: | :-------------------------: |
| ![](/images/ssao_off.webp) | ![](/images/ssao_on.webp) |

::: tip
AO, çoğunlukla ortam ışığıyla aydınlatılan alanlarda en görünür olacaktır. Güçlü doğrudan ışık altındaki alanlar çok daha zayıf AO etkisi alır.

:::

## Depth of Field (DOF)
Odak dışındaki bölgelerde bulanıklık efekti ekler.

Odak noktasını değiştirmek için modelinize dokunmanız yeterlidir.

* `Far blur` - Odak noktasının arka tarafına uygulanacak bulanıklık miktarı.
* `Near blur` - Odak noktası ile kamera arasına uygulanacak bulanıklık miktarı.


| DOF off                    | DOF focus on far ring       | DOF focus on close ring     |
| :------------------------: | :-------------------------: | :-------------------------: |
| ![](/images/dof_off.webp) | ![](/images/dof_near.webp) | ![](/images/dof_far.webp)  |


## Bloom
Bloom, sahnenizdeki parlak alanların parlamasını sağlar.

* `Intensity` - etkinin gücü.
* `Radius` - Etkinin yayılımı.
* `Threshold` - Pikselin bloom yapmaya başlaması için sahnede ne kadar parlak olması gerektiği. Bu değeri düşük ayarlamak her şeyi bloom’latır; yüksek ayarlamak yalnızca en parlak piksellerin bloom yapmasına izin verir.
* `Color` - creative efektler için bloom’a eklenebilecek bir renk tonu.

| Bloom off                     | Bloom with radius 0          | Bloom with radius 1          |
| :---------------------------: | :--------------------------: | :--------------------------: |
| ![](/images/bloom_off.webp) | ![](/images/bloom_r0.webp) | ![](/images/bloom_r1.webp) |


## Tone Mapping
Tone Mapping, HDR değerleri `[0, 1]` aralığına yeniden eşleyen bir işlemdir.
Bunu kullanmazsanız (veya `none` seçerseniz), 1’den büyük herhangi bir renk bileşeni kırpılır.
Bu aralığın üzerindeki tüm renk varyasyonları kaybolur.

* `None/Neutral/Agx/ACES` - hangi tonemapper’ın kullanılacağı. `None` yeniden eşleme yapmaz (ancak diğer kontroller yine de çalışır). Diğer seçenekler, farklı film stokları seçmeye benzer; aşırı pozlanmış değerler ve renklerle farklı şekillerde başa çıkarlar. Bu çok derin bir konu; daha fazla bilgi için tone mapping, Agx, ACES üzerine araştırma yapın!
* `Exposure` - Görüntünün genel parlaklığı; bir kamerada diyafram ayarlamaya benzer. Bir görüntüyü küresel olarak hızlıca aydınlatmak veya karartmak için kullanılabilir.
* `Saturation` - Renk yoğunluğu. 1 nötrdür, 0 monokromdur, 1’in üzerindeki değerler giderek daha doygundur.
* `Contrast` - Karanlıkları daha karanlık, aydınlıkları daha aydınlık yapar. Dikkatli kullanın; yüksek değerlerde artefaktlara neden olabilir.

`Tone Mapping` devre dışıyken, pikseller çok parlak olduğu için bazı detayların kaybolduğuna dikkat edin.

| Tone Mapping off             | Tone Mapping on             |
| :--------------------------: | :-------------------------: |
| ![](/images/tone_off.webp) | ![](/images/tone_on.webp) |

::: tip
Tone mapping, global illumination etkisini güçlendirebilir. Ortam haritasının yoğunluğunu azaltıp birincil ışık kaynağını artırırsanız, tone mapping `exposure` değerini yükselterek daha fazla sekme ışığı etkisi görebilirsiniz.
:::

## Color Grading
Photoshop’taki curves aracına benzer şekilde, görüntüdeki renk dengesini ve dağılımını kontrol etmenizi sağlar. `main` kontrolü tüm renk dengesini etkiler; `red`/`green`/`blue` kontrolleri ince ayar yapmanıza izin verir. 

| Color Grading off              | Color Grading on              |
| :----------------------------: | :---------------------------: |
| ![](/images/grading_off.webp) | ![](/images/grading_on.webp) |

## Curvature
Eğrilikte hızlı değişimlerin olduğu yerleri tespit eder ve bu bölgelere bir renk uygular.

* `Factor` - etkinin genel yoğunluğu
* `Bump` - keskin dışbükey değişimleri ne kadar bulacağı ve seçilen rengi (varsayılan olarak beyaz) oraya yerleştireceği
* `Cavity` - içbükey değişimleri ne kadar tespit edeceği ve seçilen rengi (varsayılan olarak siyah) oraya yerleştireceği


| Curvature off                     | Curvature on                    |
| :-------------------------------: | :-----------------------------: |
| ![](/images/curvature_off.webp) | ![](/images/curvature_on.webp) |


## Chromatic Aberration
Ekran kenarlarında ışığın ayrışmasını simüle ederek lens artefaktlarını taklit eder.

* `Strength` - Görüntünün kırmızı/yeşil/mavi kısımlarının ekran kenarlarına doğru ne kadar ayrılacağı

| Chromatic off                  | Chromatic on                  |
| :----------------------------: | :---------------------------: |
| ![](/images/chroma_off.webp) | ![](/images/chroma_on.webp) |


## Vignette
Ekran kenarlarını karartarak lens artefaktlarını simüle eder.

* `Size` - Görüntünün üzerine yerleştirilen ters elipsin boyutu
* `Hardness` - Elipsin görüntünün üzerine ne kadar bulanık veya keskin karıştırıldığı.


| Vignette off                     | Vignette on                     |
| :------------------------------: | :-----------------------------: |
| ![](/images/vignette_off.webp) | ![](/images/vignette_on.webp) |

## Grain
Bir grain efekti ekler; görüntünün biraz daha az yapay görünmesine yardımcı olabilir.

* `Strength` - Görüntüye eklenen grain/gürültü miktarı.


| Grain off                     | Grain on                    |
| :---------------------------: | :-------------------------: |
| ![](/images/grain_off.webp) | ![](/images/grain_on.webp) |


## Sharpness
Photoshop veya fotoğraf işleme uygulamalarındakine benzer bir keskinleştirme efekti.

* `Strength` - Görüntüye uygulanan keskinleştirme miktarı.


| Sharpness off                   | Sharpness on                  |
| :-----------------------------: | :---------------------------: |
| ![](/images/sharpen_off.webp) | ![](/images/sharpen_on.webp) |

## Pixel Art
Retro oyun piksel sanatını simüle eder.

* `Slider` - Piksel boyutu
* `Allow frame sampling` - Çok fazla siyah piksel görürseniz, varsayılan örneklemeyi geçersiz kılacak bu seçeneği açmayı deneyin.

| Pixel off                    | Pixel on                    |
| :--------------------------: | :-------------------------: |
| ![](/images/pixel_off.webp) | ![](/images/pixel_on.webp) |

## Scanline
Eski CRT monitörlerin görünümünü simüle eder.

* `Factor` - Çizgilerin gücü
* `Spacing` - Çizgilerin boyutu

| Scanline off                    | Scanline on                    |
| :-----------------------------: | :----------------------------: |
| ![](/images/scanline_off.webp) | ![](/images/scanline_on.webp) |


## Dithering

Pikselleri dither ederek banding artefaktlarını azaltır. Genellikle etkin olmalıdır, ancak belirli işlemler için (ör. depth map dışa aktarma veya veri odaklı diğer işlemler) kapatılabilir.
