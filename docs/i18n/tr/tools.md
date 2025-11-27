# ![](/icons/toolbox.webp) Araçlar

![](/images/tools_menu.webp)

::: tip
Tek tek araçların açıklamaları için aşağıda [Araçlar](#tools-1) bölümüne atlayın.
:::

## Genel Bakış

Araçlar sağdaki `Toolbox` içinden seçilir ve soldaki `Tool Controls` ile kontrol edilir. Ek ayarlar, sağ üst menüdeki ilk simge olan `Settings` menüsünde bulunur.

Fırça araçlarının boyut ve yoğunluk kontrolleri vardır. Seçim araçlarının çeşitli seçim stilleri için kontrolleri vardır. Araç kontrollerinin en altında sık kullanılan işlemler için kısayollar bulunur (Smooth, Mask, Hide, Gizmo, Color, Alpha).

Nomad'ın araçları araç kutusunda renk kodludur:

* <span class=brush>**Fırça araçları**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**Taşıma araçları**</span> (Move, Drag)
* <span class=mask>**Maske araçları**</span> (Mask, SelMask)
* <span class=paint>**Boya araçları**</span> (Paint, Smudge)
* <span class=flatten>**Düzleştirme araçları**</span> (Flatten, Planar)
* <span class=pinch>**Sıkıştırma araçları**</span> (Crease, Pinch)
* <span class=selection>**Seçim tabanlı araçlar**</span> önce 2d bir maske çizilir, ardından bir işlem gerçekleşir (Trim, Split, Project)
* <span class=creation>**Yaratma araçları**</span> (Tube, Lathe, Insert)
* <span class=transform>**Dönüştürme araçları**</span> (Transform, Gizmo)
* <span class=misc>**Çeşitli araçlar**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**Görünüm aracı**</span>



Bu araçların çoğu, [Stroke](stroke.md) menüsü aracılığıyla farklı fırça davranışı, basınç, dokular vb. ile özelleştirilebilir. 


### Fırça kontrolleri

Sol araç çubuğunda yarıçap ve yoğunluk için kaydırıcılar ve ardından aşağıda açıklanan araç kategorisine özel kontroller bulunur.

![](/images/tool_left_panel.webp)

::: tip
Birçok araç için yoğunluk kaydırıcısı %100'ün üzerine çıkabilir, denemeye değer!
:::

### Alt mod
Yoğunluk kaydırıcısının hemen altındaki düğme `Sub` düğmesidir. Etiketi ve işlevi her araçla değişir ve basıldığında genellikle zıt olan alternatif bir davranışı çağırır. Örneğin [Paint](#paint) için Silme modunu çağırır, [Crease](#crease) için ise yarıklar yerine yükseltilmiş kenarlar oluşturur vb.

Varsayılan olarak yapışkan düğme gibi çalışır; yani basılı tutarsanız geçici olarak devreye girer, bıraktığınızda kapanır. Dokunursanız alt mod kalıcı olarak etkinleştirilir.

### Kısayollar
Sol araç çubuğunun altında [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha) için kısayollar bulunur. 

Varsayılan olarak bunların hepsi yapışkan düğme gibi çalışır; yani basılı tutarsanız geçici olarak devreye girer, bıraktığınızda kapanır. Dokunursanız, o kısayol modu kalıcı olarak etkinleştirilir.

### Seçim kontrolleri

[Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup) ve [Hide](#hide) araçlarının tümü, ağın alanlarını seçmek için benzer kontroller kullanır.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - Serbest el çizilmiş bir şekil
* `Polygon` - Eğriler ve/veya düz çizgilerin birleşimiyle tanımlanan kapalı bir şekil. Daha fazla bilgi için aşağıdaki [Shape editing](#shape-editing) bölümüne bakın.
* `Curve` - (Sadece Project) - Projeksiyon için serbest el eğrisi
* `Path` - (Sadece Project) - Noktalarla tanımlanan bir eğri. Daha fazla bilgi için aşağıdaki [Shape editing](#shape-editing) bölümüne bakın.
* `Line` - Düzlemsel bir kesit tanımlamak için bir çizgi sürükleyin. Varsayılan olarak ağ üzerinde hemen çalışır, bunu istemiyorsanız otomatik onaylamayı kapatın (çizgi simgesine uzun basın veya kaydırın)
* `Rect` - Köşeleri bir dikdörtgen şeklinin köşelerini tanımlayacak şekilde çapraz bir çizgi sürükleyin. Otomatik onaylama, kare şekle zorlama ve ilk tıklamanın dikdörtgenin merkezi olması seçeneklerini görmek için uzun basın veya kaydırın.
* `Ellipse` - Bir elipsin boyutunu tanımlayacak şekilde çapraz bir çizgi sürükleyin. Otomatik onaylama, daire şekline zorlama ve ilk tıklamanın elipsin merkezi olması seçeneklerini görmek için uzun basın veya kaydırın.
* `Flip` - şekil maskesini veya project aracının yönünü tersine çevirir.

Çoğu aracın otomatik onaylama seçeneği vardır, bu da işlemin şekli çizer çizmez gerçekleşeceği anlamına gelir. Otomatik onaylama kapalıyken, işlemi gerçekleştirecek olan şeklin yanında yeşil bir düğme çizilir. Bu, şekli düzenlemenize, görünümü ayarlamanıza olanak tanır; şekli kullanmaya hazır olduğunuzda yeşil düğmeye basın.

### Şekil düzenleme
Poligon düzenleme ve eğri düzenleme benzer şekilde davranır:

* Başlamak için, 2 noktayı tanımlamak üzere bir çizgi sürükleyin, ardından bir poligon veya eğri tanımlamak için çizginin ortasından dışarı doğru sürükleyin.
* Noktalara tıklayarak yumuşak ve keskin arasında geçiş yapın. 
* Yeni noktalar oluşturmak için eğri veya çizgi bölümlerine tıklayıp sürükleyin.
* Bir noktayı silmek için, bir noktayı komşusuna doğru sürükleyin, kırmızıya dönene kadar.
* Poligon veya path simgesinin köşesindeki çöp kutusu simgesi şekli siler.

### Ayarlar menüsü

Birçok aracın, sağ üst menüdeki ilk simge olan ayarlar menüsünde bulunan ek ayarları vardır:

![](/images/tools_settings_menu.webp)

## Araçlar

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Clay
Clay aracı, heykelinizi inşa etmek için kullanışlıdır. `Sub` heykelinizden malzeme kaldırır.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Brush
Standart fırça. `Sub` malzeme kaldırır.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Move
Fırçanın altındaki alan fırçaya yapışır, bu da esnek deformasyona izin verir. Seçim, hareket sırasında korunur, bu nedenle fırçayı uzaklaştırıp sonra başladığınız yere geri getirirseniz, hiçbir deformasyon görmezsiniz.

Alt mod `Normal`dir ve fırçanın altındaki alanı yüzey normali boyunca hareket ettirir.

Bu fırça hem büyük ölçekli deformasyon hem de dikkatli küçük deformasyon için iyidir.

#### Move Ayarları

* `Radius (Background)` - Bir modelin kenarından ne kadar uzakta olup hâlâ yontu yapabileceğinizi belirler, bir nesnenin siluetinde çalışırken kullanışlıdır. 
* `Same-side vertex only` - Deformasyonun ters yönüne bakan köşeleri yok say.

![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Drag
Fırçanın altındaki alan fırçaya yapışır, bu da esnek deformasyona izin verir. Move fırçasından farklı olarak, seçim vuruş boyunca sürekli güncellenir, bu nedenle özellikle Dinamik Topoloji etkinleştirildiğinde daha uzun, yılan benzeri nesneler yapmak mümkündür.

Alt mod `Normal`dir ve fırçanın altındaki alanı yüzey normali boyunca hareket ettirir.

Bu fırça daha gevşek, jestsel şekil değişiklikleri için iyidir.

#### Drag Ayarları

* `Radius (Background)` - Bir modelin kenarından ne kadar uzakta olup hâlâ yontu yapabileceğinizi belirler, bir nesnenin siluetinde çalışırken kullanışlıdır. 
* `Same-side vertex only` - Deformasyonun ters yönüne bakan köşeleri yok say.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Smooth
Noktaların konumlarını ortalayarak alanı yumuşatır. Bu araç, poligon yoğunluğuna oldukça bağlıdır.
Yani çok fazla poligon varsa, yumuşatma daha az etkili olacaktır.

Alt mod `Relax`tir, yalnızca tel kafesi yumuşatır ancak geometrik detayları korumaya çalışır.

#### Smooth ayarları

![](/images/tool_smooth_settings.webp)

##### Facegroup

* `Relax` - Facegroup sınırlarını yumuşatır. Sınırları hızlıca yumuşatmak için yoğunluğu %100'ün üzerine çıkarın. `Auto` yalnızca facegroup önizlemesi etkinse yumuşatır, `Off` devre dışı bırakır, `On` etkinleştirir. 

##### Vertex
* `Sticky vertex on border` - Açık kenarlı ağlar için, örneğin bir düzlem, köşeleri düzleştirmek mümkündür. Bu seçeneği etkinleştirmek açık kenarları kilitler.
* `Relax` - sol araç çubuğundaki relax alternatif modu ile aynıdır.
* `Stable smoothing` - Yumuşatmayı topolojiden bağımsız hale getirmeye çalışır. Bu, değişken topoloji yoğunluğu ve yüksek yumuşatma yoğunluğu değeriyle en iyi sonucu verir.

##### Painting
* `Screen Smoothing` - Bu seçeneği, yüksek poligon sayılarında bile topolojiden bağımsız yumuşatma elde etmek için kullanın.
* `Screen samples` - Yumuşatma kalitesi, daha yüksek değerler daha pürüzsüz ama daha yavaştır.

::: tip
Daha yüksek poligon yoğunlukları, yoğunluğun %100'ün üzerine çıkarılmasını gerektirebilir. Çok yüksek değerler (%300, %500) aynı zamanda bir yontu aracı olarak da iyi çalışabilir, alanları fırçanın altında hızla düz ve pürüzsüz hale zorlayarak, kilin tokmakla dövülmesi gibi!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Mask
Bu araç, köşeleri maskelemenizi sağlar. Maskelenmiş köşeler yontma veya boyamadan korunur. 

Alt mod `Unmask`tir ve maskenin boyandığı yerleri siler.

2d boyama programlarındaki seçimlere benzer şekilde, maskeler bir fırça ile boyanabilir veya şekil seçimleriyle yapılabilir, bulanıklaştırılabilir veya keskinleştirilebilir. 

2d boyama programlarından farklı olarak, facegroup'lar aracılığıyla da yapılabilirler ve maskeler ekstrüzyon/ekstraksiyon tarzı işlemlerle yeni geometri oluşturmak için kullanılabilir. 

![](/videos/tool_mask1.mp4)

 Görüntü alanının üst kısmında ek kontroller içeren bir araç çubuğu görünür. 

![](/images/tool_mask_toolbar.webp)

Çubuğun başlığına dokunarak genişletip/daraltabilir veya sağ üstteki oka dokunarak UI'nin üstüne veya altına taşıyabilirsiniz.

| Action                                             | Description                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/cross_circle2.webp) Clear              | Maskeyi temizle                                                                            |
| ![](/icons/invert.webp)        Invert             | Maskeyi tersine çevir                                                                      |
| ![](/icons/sharpen.webp)       Sharpen            | Maske kenarını keskinleştir                                                                |
| ![](/icons/blur.webp)          Blur               | Maske kenarını bulanıklaştır                                                              |
|                                 Blur ->            | Maskeyi etkileşimli olarak bulanıklaştırmak için sola/sağa sürükleyin                     |
| ![](/icons/culling.webp)       Front              | Yalnızca öne bakan köşeleri maskelemeyi aç/kapat                                          |
|                                 Convert            | Maskeyi bir facegroup'a dönüştür                                                           |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | Etkinleştirildiğinde facegroup'lar gösterilir, bir facegroup'a dokunmak onu maskeleyecektir |
|                                 On tap (mask)      | Etkinleştirildiğinde, maskeli veya maskesiz poligonlardan oluşan bir 'ada'ya dokunmak o adayı doldurur. |
| ![](/icons/vertex.webp)        Connected          | Etkinleştirildiğinde, yalnızca bağlı topolojiyi etkileyen maske vuruşlarına izin verilir. |

##### Mask Hızlı jesti
Sol alt kısayol düğmesini basılı tutarken zbrush tarzı jestler yapabilirsiniz:
| Action  | Gesture (hold lower-left shortcut) |
| :-----: | :--------------------------------: |
| Invert  | Arka plana dokun                   |
| Clear   | Arka plan üzerinde sürükle         |
| Blur    | Maskeli alana dokun                |
| Sharpen | Maskesiz alana dokun               |


#### Mask ayarları
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - Mask ayarları menüsü esas olarak maskeden geometri oluşturmak için kullanılır. Bu nedenle varsayılan davranış, yeni geometrinin nasıl görüneceğini önizlemektir. Hiç önizleme olmamasını, bir extract önizlemesini, bir split önizlemesini ve bu geometrinin x-ray modunda gösterilip gösterilmeyeceğini seçebilirsiniz.

##### Thickness
* `Height` - Çıkarılan şeklin yüksekliği. Artı/Eksi simgesi, dışa doğru ekstrüzyon, içe doğru veya ortalanmış arasında geçiş yapmanızı sağlar. 
* `Height/Height+Mask` - Yüksekliğin sabit olup olmayacağını veya maskenin bulanık kısımlarının yüksekliği etkileyip etkilemeyeceğini değiştirir, bu da yumuşak ve değişken yükseklikte şekiller oluşturmanıza olanak tanır. 

##### Smoothness
Etkin olduğunda, çıkarılan şeklin sınırını yumuşatır, daha yüksek poligon sayılarıyla daha iyi çalışır. 
* `Iterations` - Uygulanan yumuşatma miktarı. Yüksek değerler çok pürüzsüz kavisli kenarlar üretir, ancak maskenin şeklinden uzaklaşmaya başlar.
* `All/Sharp border/Borders only` - Yumuşatma tüm yönlerde çalışabilir, hem kenarları hem de çıkarılan şeklin üstünü yumuşatır veya üst ve kenarları yumuşatır ancak keskin bir kenarı korur ya da yalnızca sınırı yumuşatır, üst yüzeyi etkilemeden bırakır.

##### Edge loop (side)
* `Auto Edge-loop (side)` - Çıkarılan şeklin kenarlarında, maskelenmiş alanın poligonlarıyla eşleşen kare poligonlar oluşturmak için bölümlerin sayısını hesaplar. Devre dışı bırakıldığında, kenar döngüsü kaydırıcısıyla kenar döngülerinin sayısını kendiniz ayarlayabilirsiniz.

----

##### Extract
* `Extract` - Çıkarılmış geometriyi oluştur.
* `Closing action` - Extract'in nasıl davranması gerektiği. 'None' maskelenmiş poligonları yeni bir şekle kopyalar. 'Fill' aynı şeyi yapar ve arka yüzeyi yamalamaya çalışır. 'Shell' 'thickness'ta ayarlanan miktarda ekstrüde eder ve varsayılandır.

::: tip

Önizleme 'Extract' modunda ve 'X-ray' etkin durumdayken Extract düğmesine tıklamak ilk başta kafa karıştırıcı olabilir. Menü etkin olduğundan, yeni şeklinizde bir extract önizlemeye çalışır ve orijinal yüzeyi x-ray yapar. Ancak yeni yüzeyde maskeniz olmadığı için extract'i önizleyemez ve Nomad size 'Nothing to Extract!' uyarısı verir. 

Bu normaldir, yeni şekli ve orijinali görmek için mask ayarları menüsünü kapatın ve maskeyi temizlemeniz veya yeni maskeler çizmeniz gerekiyorsa orijinal yüzeyi tekrar seçin.
:::

##### Split
* `Split` - Hem maskelenmiş HEM de maskesiz bölgeleri yeni şekillere çıkarır. 
* `Closing action (masked)` - Mask extract'in nasıl davranması gerektiği. 'None' maskelenmiş poligonları yeni bir şekle kopyalar. 'Fill' aynı şeyi yapar ve arka yüzeyi yamalamaya çalışır. 'Shell' 'thickness'ta ayarlanan miktarda ekstrüde eder ve varsayılandır.
* `Closing action (unmasked)` - Maskesiz extract'in nasıl davranması gerektiği. 'None' maskelenmiş poligonları yeni bir şekle kopyalar. 'Fill' aynı şeyi yapar ve arka yüzeyi yamalamaya çalışır. 'Shell' 'thickness'ta ayarlanan miktarda ekstrüde eder ve varsayılandır.
* `Sync border` - Maskelenmiş ve maskesiz çıkarılmış şekiller arasındaki sınırın birbirine yakın kalmasını sağlar. Devre dışı bırakıldığında, shell işlemi her yüzü normaline göre ekstrüde edeceğinden, şekiller arasında bir boşluk oluşabilir.

##### Carve
* `Carve` - Varsayılan modda, yüzeye 'thickness' miktarı kadar trim yapılmış gibi davranır, bir portakal kabuğu parçasını kesmek gibi. 



### ![](/icons/tool_maskSelector.webp) Selection Mask
Bu araç çoğunlukla [Masking tool](#mask) ile benzerdir, temel fark, maskeyi boyamak için stroke kullanmamanız, bunun yerine [Selection Controls](#selection-controls) kullanmanızdır.

Alt mod `Unmask`tir ve seçim kontrollerini kullanarak maskeyi siler.

Selection mask, `Mask` aracıyla aynı araç ayarlarını paylaşır.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Paint
Renk ve malzeme özellikleri uygular. Malzeme hakkında daha fazla bilgi edinmek için [Painting](painting.md) bölümünü ziyaret edebilirsiniz.

Alt mod `Erase`tir ve boyayı kaldırır.

#### Paint ayarları
* `Layer fitering` - Photoshop veya Procreate'teki layer alpha lock gibi çalışır. Bir katmanda boyuyorsanız, bu etkinleştirildiğinde yalnızca boyanın zaten bulunduğu yerleri değiştirebilirsiniz; boyanmamış alanlar korunur.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Smudge
Renk ve malzeme özelliklerini dağıtır. Smudge ayarları menüsünde bir `Quality` kaydırıcısı bulunur, daha düşük değerler daha hızlı vuruşlar anlamına gelir.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Flatten
Noktaları ortalama düzleme projekte ederek alanı düzleştirir.

Alt mod `Fill`dir ve en yüksek nokta tarafından belirlenen bir düzlem tanımlar ve noktaları yukarı çekme eğilimindedir.

#### Flatten ayarları

* `Lock plane direction` - İlk tıklamada hesaplanan düzlem yönünü kullan. Varsayılan olarak devre dışıdır.
* `Lock plane origin`- İlk tıklamayı düzlemin merkezi olarak kullan. Varsayılan olarak devre dışıdır.

Bunlardan biri veya her ikisi devre dışı bırakıldığında, flatten, farklı derinlikler ve eğrilikler üzerinde hareket eden uzun vuruşlar kullanılarak kademeli olarak derinleştirilebilir veya düzlem açısı değiştirilebilir. Bu, fırça menüsünün alan örnekleme seçenekleriyle birlikte çok hassas kontrol sunabilir.

::: tip
Yüksek eğrilikli alanlarda çalışırken, örneğin yanakları düzleştirmeye çalışırken aracın sürekli burnun yanlarını etkilemesi durumunda, flatten fırçasının etkilememesi gereken alanları korumak için bir maske oluşturmayı deneyin.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar
Noktaları ortalama düzleme projekte ederek düzlemsel hale getirir, ancak flatten fırçasına göre daha az birikimle. Bu, daha temiz sert kenarlı yüzeyler oluşturur. Hızlı vuruşlar yüzeyde daha fazla iter ve çeker, daha yavaş vuruşlar ise zaten düzlemsel alanlardan başlayıp dışa doğru çalışarak düzlemi daha fazla korur.

Alt mod `Fill`dir ve en yüksek nokta tarafından belirlenen bir düzlem tanımlar ve noktaları yukarı çekme eğilimindedir.

Planar aslında `Flatten` ile aynı araçtır, ancak `Lock plane direction` etkinleştirilmiştir, bu da daha kararlı, sert kenarlı yüzeyler oluşturma eğilimindeyken flatten'ın daha heykelsi olmasına ve yarı düz alanlar oluşturmak için kullanılmasına olanak tanır.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Crease
Crease araçları küçük kesikler veya çukurlar yontmak için kullanışlı olabilir.

Alt mod `Invert`tir ve yükseltilmiş bir yarık oluşturur.

#### Crease Ayarları

* `Pinch factor` - Köşeleri fırçaya doğru yanlara ne kadar çekeceğini belirler. Pinch 1'de ve offset 0'da ise, yüzeyde derinlik değişikliği olmaz, sadece topoloji değişiklikleri olur, kenarlar vuruşa doğru çekilir.
* `Offset factor` - Köşeleri derinlikte ne kadar itip çekeceğini belirler. Pinch 0'da ve offset 1'de ise, derin yarıklar veya yükseltilmiş çukurlar oluşturulur, ancak yarığın yanlarını veya tabanını doğru tanımlamak için yeterli geometri çekilmediğinden tırtıklı görünürler.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Pinch
Bu araç kenarları keskinleştirmek için kullanılabilir.

Alt mod `Invert`tir ve köşeleri birbirinden uzaklaştırır.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Trim
Trim aracı, ağınızdan bir parçayı kaldırarak çalışır ve geride kalan boşluğun nasıl işleneceğine dair seçenekler sunar. Trim'i tanımlamak için [Selection controls](#selection-controls) kullanılır.

::: tip
Bu araç kameradan projeksiyon yaptığı için, kamera perspektif modundaysa bir uyarı alırsınız.

Ortografik modda, ağ boyunca yapılan kesim görünüme paraleldir, bu da insanların genellikle beklediği şeydir. Perspektif kamerayla yapıldığında, nesnenin uzak tarafındaki kesim, yakın tarafındakinden farklı görünecektir.
:::

#### Trim ayarları

* `Stroke painting` - Paint menüsünde boya etkinse, yamalanan bölge mevcut seçili renkle doldurulur.
* `Boolean` - Trim'in deliğini dörtgen poligon bölgesi kullanarak doldurur. Doldurulan bölge düz olur.
* `Legacy` - Trim'in deliğini üçgenleştirilmiş bir bölgeyle doldurur. Doldurulan bölge düz olur.
* `Fill` - Deliği üçgenleştirilmiş bir bölgeyle doldurur. Doldurulan bölge, sabun köpüğü filmi gibi kavisli bir yüzey olur.
* `None` - Deliği doldurma.
* `Boolean Detail Shape` - Trim'in şekil tarafında kullanılan dörtgen ve üçgenlerin yaklaşık boyutu.
* `Boolean Detail Hole` - Trim'in doldurulan deliğinde kullanılan üçgen veya poligonların yaklaşık boyutu. 
* `Legacy Detail` - Trim'de kullanılan üçgenlerin yaklaşık boyutu.
* `Legacy Hole smoothing` - Doldurulan alandaki üçgenlerin ne kadar gevşetildiği.
* `Legacy Threshold espilon` - Eski delik doldurma algoritmasını iyileştirmek için ayarlanabilen bir değer.
* `Fill Detail` - Trim'de kullanılan üçgenlerin yaklaşık boyutu.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Split
[Trim](#trim) aracına benzer, ancak Trim seçimi atarken, Split seçimi yeni bir nesne olarak saklar.

#### Split ayarları

* `Stroke painting` - Paint menüsünde boya etkinse, yamalanan bölge mevcut seçili renkle doldurulur.
* `Boolean` - Split'in deliğini dörtgen poligon bölgesi kullanarak doldurur. Doldurulan bölgeler düz olur.
* `Legacy` - Split'in deliğini üçgenleştirilmiş bir bölgeyle doldurur. Doldurulan bölgeler düz olur.
* `Fill` - Delikleri üçgenleştirilmiş bir bölgeyle doldurur. Doldurulan bölgeler, sabun köpüğü filmi gibi kavisli yüzeyler olur.
* `None` - Delikleri doldurma.
* `Boolean Detail Shape` - Split'in şekil tarafında kullanılan dörtgen ve üçgenlerin yaklaşık boyutu.
* `Boolean Detail Hole` - Split'in doldurulan deliğinde kullanılan üçgen veya poligonların yaklaşık boyutu. 
* `Legacy Detail` - Split'te kullanılan üçgenlerin yaklaşık boyutu.
* `Legacy Hole smoothing` - Doldurulan alandaki üçgenlerin ne kadar gevşetildiği.
* `Legacy Threshold espilon` - Eski delik doldurma algoritmasını iyileştirmek için ayarlanabilen bir değer.
* `Fill Detail` - Split'te kullanılan üçgenlerin yaklaşık boyutu.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Project
Project aracı [Trim](#trim) aracına benzer görünür, ancak hiçbir geometriyi silmez veya oluşturmaz, yalnızca köşeleri seçime uydurmak için hareket ettirir.

![](/videos/tool_project.mp4)

::: tip
Bir layer içindeyken Project kullanırsanız, layer kaydırıcısıyla orijinal ve projeksiyonlu şekil arasında geçiş yapabilirsiniz.
:::

### ![](/icons/tool_layer.webp) Layer
Yüzeyi yükseltir, ancak yüksekliği sınırlar.

Kalemi basılı tutup bir alan üzerinde fırçalamaya devam ederseniz, Layer belirli bir yüksekliğe kadar yükselir ve daha fazla gitmez, diğer araçlar ise yüksekliği biriktirmeye devam eder.

Varsayılan olarak sınır yalnızca vuruş başına ayarlanır! Yeni bir vuruş başlatırsanız, yeni yüzey yüksekliğinden itibaren inşa eder.

Birçok vuruş boyunca sabit bir maksimum yükseklik ayarlamak için, Layer aracını Nomad'ın [Layers](layers.md) sistemiyle birlikte kullanın.

Bir layer oluşturun ve bu aracı kullanın. Maksimum yükseklik artık layer'dan ayarlanır, böylece birçok fırça darbesi uygulayabilir ve yükseklik her zaman aynı kalır.

`Sub` minimum derinlik kullanır, oluklar oluşturur.

#### Layer Ayarları

* `Use layer data` - Etkin olduğunda ve bir layer seçiliyken, maksimum yüksekliği ayarlamak için layer verilerini kullanır.
* `Inflate`- Etkin olduğunda, daha yumuşak sonuçlar elde etmek için layer'ın çalıştığı yönü ayarlar.
* `Relax (Normal)` - Normallere uygulanan yumuşatma miktarı.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Inflate
Köşeleri kendi normalleri boyunca hareket ettirir. `Sub` köşeleri ters normal boyunca hareket ettirir.

#### Inflate Ayarları
* `Relax (Normal)` - Normallere uygulanan yumuşatma miktarı.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Nudge
Noktaları vuruş yönünde hareket ettirir veya 'sürükler'.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stamp

Seçili Alpha'nın şekliyle heykelin bir alanını yükseltmek için tıklayıp sürükleyin.

Bu, stroke türü `Lock + radius` olarak ayarlanmış [Brush tool](#brush)'dur. 

`Sub` damgayı yüzeyden dışarı çekmek yerine içeri iter.

::: tip
Stamp genellikle yüksek çözünürlüklü geometriyle en iyi sonucu verir. İnternette 'wrinkles alpha', 'pores alpha', 'scales alpha' vb. ararsanız, bu alpha dokuları ve Stamp, bir karakter heykeline organik detay eklemek için harika bir yol olabilir.

İki stroke modu farklı şeyler için kullanışlıdır. 

* `Lock + radius` sabit bir *yüksekliğe* sahiptir, sürükleme damganın genişliğini ve dönüşünü ayarlar. Aynı derinlik/yükseklikte, ancak tekrarlayan desenleri gizlemek için farklı dönüş ve ölçeklere sahip olması gereken cilt dokuları için iyidir.
* `Lock + intensity` sabit bir *genişliğe* sahiptir, sürükleme damganın dönüşünü ve yüksekliğini ayarlar. Hepsi aynı boyutta, ancak farklı dönüş ve yüksekliklere sahip olması gereken perçinler için iyidir. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Delete Layer
Bu araç, layer'ları yerel olarak sıfırlayabilir, etkin bir layer'a ihtiyacınız vardır, aksi takdirde hiçbir şey olmaz.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tube
Bir eğri çizerek bir tüp oluşturun. 
![](/images/tool_tube_new.webp)

Tüp oluşturulduktan sonra, yol standart [Shape editing](#shape-editing) ve eğri düzenleme araçlarına benzer kontroller kullanılarak 3d alanda düzenlenebilir. 

![](/videos/tool_tube.mp4)

#### Tube sol araç çubuğu

![](/images/tool_tube_left_toolbar.webp)

Sol araç çubuğunda aşağıdaki seçenekler bulunur:

* `Sync` - Mevcut tüp örneklenmişse ve örnekler arasında farklı olan tüpün alt düğümleri varsa, bunları yeniden senkronize eder.
* `Snap` - Etkin olduğunda, curve ve path modları çizerken diğer nesnelere yapışır. Devre dışı olduğunda, ilk nokta yapışır, ardından tüpün geri kalanı o derinlikte çizilir. Küçük bir açılır menüsü vardır:
    * `Offset` - Yapışmanın derinliğini ayarlar; %0, tüp kesitinin ortasının yüzeye yapışmasına neden olur, pozitif değerler yüzeyden kaldırır, negatif değerler aşağı indirir.
* `Curve` - Serbest biçimli bir tüp çizin. Küçük bir açılır menüsü vardır:
    * `Auto-validate` - Vuruş tamamlanır tamamlanmaz tüpü oluşturur. Devre dışı olduğunda, eğri yolunun yanında görünen yeşil onay dairesine basarak onaylayabilirsiniz veya bu menüde görünen `Reset` bağlantısını kullanarak yolu kaldırabilirsiniz.
    * `Closed` - Tüpü bir döngü haline getirin.
    * `Screen` - Yalnızca Auto-validate devre dışı olduğunda kullanılabilir. Etkin olduğunda, yol ekrana 'sabitleme' yapılır, böylece görünümü ve nesneyi hareket ettirebilir, yol yerinde kalır. Devre dışı olduğunda, yol 3d sahnenin bir parçasıdır ve kamera ve nesnelerle birlikte hareket eder.
    * `Accuracy` - Çizilen yolu tüpe dönüştürmek için kaç eğri noktası kullanılacağını belirler. %0 en az sayıda noktayı kullanır, ancak küçük eğrilik yolu değişikliklerini kaçırır. %100 çok hassas olur ve birçok nokta kullanır.
* `Path` - Eğri noktalarını tanımlamak için tıklayarak bir tüp oluşturun. Yolu onaylamak için yeşil daireye dokunun. Küçük bir açılır menüsü vardır:
    * `B-spline` - Eğri noktalarının genellikle doğrudan eğri üzerinde oturmadığı, ancak varsayılan yönteme göre daha pürüzsüz sonuçlar verebilen alternatif bir eğri çizim yöntemi.
    * `Closed` - Tüpü bir döngü haline getirin
    * `Screen` - Etkin olduğunda, yol ekrana 'sabitleme' yapılır, böylece görünümü ve nesneyi hareket ettirebilir, yol yerinde kalır. Devre dışı olduğunda, yol 3d sahnenin bir parçasıdır ve kamera ve nesnelerle birlikte hareket eder.

##### Tube üst araç çubuğu
![](/images/tool_tube_toolbar.webp)
Bir tüp seçildiğinde, görüntü alanının üst kısmında ek kontroller içeren bir araç çubuğu görünür. Araç çubuğunu daraltmak/genişletmek için başlığına tıklayın ve görüntü alanının üstüne veya altına taşımak için sağ üstteki oka tıklayın.

* `Validate` - Tüpü, yontulabilmesi için normal poligonlara dönüştürür.
* `Edit` - Eğri noktalarını gösterir, böylece bunlar üzerinde işlem yapılabilir
* `Mirror` - Bu eğrinin ebeveyni olarak bir mirror repeater ekler
* `Snap` - Eğri noktalarını yakın yüzeylere yapıştırır
* `Closed` - Eğrinin başlangıcını ve sonunu birleştirerek bir döngü oluşturur
* `B-spline` - Catmull-rom ve B-spline enterpolasyonu arasında geçiş yapar.
* `Cap` - Tüpün her iki ucunda kapak, yalnızca başlangıç veya bitişte kapak veya hiç kapak olmaması arasında geçiş yapar.
* `Hole` - Tüpü kalınlaştırarak bir boruya dönüştürür. Her iki uçta, yalnızca uçta veya hiç delik olmaması arasında geçiş yapar. 
* `Radius` - Tekdüze yarıçap, başlangıç ve bitişte yarıçap veya eğri noktası başına yarıçap arasında geçiş yapar. Bunlar eğri üzerindeki turuncu tutamaçlarla düzenlenir.
* `Twist` - Hiç bükülme, tekdüze bükülme, başlangıç ve bitişte bükülme veya eğri noktası başına bükülme arasında geçiş yapar. Bunlar eğri üzerindeki pembe tutamaçlarla düzenlenir.
* `Profile` - Profil olmaması (yani daire profili), tekdüze profil, başlangıç ve bitişte profil veya nokta başına profil arasında geçiş yapar.
* `Profile edit` - Bir profil düzenleyici gösterir. Bu, [Shape editing](#shape-editing) araçlarına benzer şekilde çalışır, profil ön ayarlarını kaydedip yükleyebilir ve profili 3d alanda düzenlemenize izin veren bir geçişe sahiptir.
* `Spiral` - Tüpe spiral bükülme eklemek için bir menüyü açıp kapatır. Bu menüde `Twist Angle`, `Offset`, `Scale` ve `Angle offset` seçenekleri bulunur.
* `X Divisions` - Tüp etrafındaki bölümlerin sayısı, örneğin 4 bölüm kare bir tüp oluşturur. 
* `Constant density` - Etkin olduğunda, poligonları kare tutar. Devre dışı olduğunda, tüp boyunca `Y divisions` ayarlamanıza izin verir.
* `...` - Tube ayarları menüsü.

#### Eğri noktası silme geçişi

![](/images/tool_tube_delete_toggle.webp)

Araç çubuğunun altında bir eğri noktası silme geçişi bulunur. Bir eğri noktasını diğerine yaklaştırdığınızda kırmızıya döner, bu da bırakırsanız noktanın silineceğini gösterir. Küçük düzenlemeler yapıyorsanız ve noktaları silmek istemiyorsanız, bu düğme nokta silme davranışını devre dışı bırakır.



#### Tube ayarları
* `Primitive` - UV'leri etkinleştirmek/devre dışı bırakmak veya tüpü onaylamak için düğmeler.
* `Post subdivision` - Onaylamadan önce çoklu çözünürlük seviyesini ayarlamak için bir kısayol.
* `Linear subdivision` - Onaylamadan önce lineer subdivision seviyesini ayarlamak için kısayol. 
* `Division X` - Araç çubuğundaki X Divisions ile aynıdır.
* `Division Y` - Araç çubuğundaki Y Divisions ile aynıdır.
* `Curve (Repeater)` - Tüpü bir [Curve Repeater](scene.md#curve)'a dönüştürür.

::: tip
Divisions 4 ve Post subdivision 3 iken, solucanlar, yılanlar, vücut parçaları için iyi olan, uçları yuvarlak pürüzsüz tüpler oluşturur.
:::


### ![](/icons/tool_lathe.webp) Lathe
Bir eğri çizerek bir dönel yüzey oluşturun.

Bu araç, vazo, şarap kadehi gibi şekiller için harikadır.

![](/videos/tool_lathe.mp4)

#### Lathe sol araç çubuğu

![](/images/tool_lathe_left_toolbar.webp)

Sol araç çubuğunda aşağıdaki seçenekler bulunur:

* `Sync` - Mevcut lathe örneklenmişse ve örnekler arasında farklı olan lathe'in alt düğümleri varsa, bunları yeniden senkronize eder.
* `Fixed` - Etkinleştirildiğinde, lathe'in merkezi sabitlenir ve ekranda gösterilir. Bu merkez çizgisinin ayarlanabilen düzenleme noktaları vardır. Devre dışı bırakıldığında, lathe'in merkezi, çizilen eğrinin başlangıcına ve sonuna dinamik olarak uyacak şekilde güncellenir.
* `Curve` - Lathe profilini tek vuruşta çizin. Küçük bir açılır menüsü vardır:
    * `Auto-validate` - Etkinleştirildiğinde, kalem ekrandan kaldırıldığında lathe oluşturulur. Devre dışı olduğunda, eğrinin yanındaki yeşil daireye basarak lathe oluşturulabilir. Eğri `Reset` düğmesiyle silinebilir.
    * `Closed` - Eğrinin başlangıcını ve sonunu birleştirerek bir döngü oluşturur
    * `Screen` - Yalnızca Auto-validate devre dışı olduğunda kullanılabilir. Etkin olduğunda, yol ekrana 'sabitleme' yapılır, böylece görünümü ve nesneyi hareket ettirebilir, yol yerinde kalır. Devre dışı olduğunda, yol 3d sahnenin bir parçasıdır ve kamera ve nesnelerle birlikte hareket eder.
    * `Accuracy` - Çizilen yolu tüpe dönüştürmek için kaç eğri noktası kullanılacağını belirler. %0 en az sayıda noktayı kullanır, ancak küçük eğrilik yolu değişikliklerini kaçırır. %100 çok hassas olur ve birçok nokta kullanır.
* `Path` - Eğri noktalarını tanımlamak için tıklayarak bir lathe oluşturun. Yolu onaylamak için yeşil daireye dokunun. Küçük bir açılır menüsü vardır:
    * `B-spline` - Eğri noktalarının genellikle doğrudan eğri üzerinde oturmadığı, ancak varsayılan yönteme göre daha pürüzsüz sonuçlar verebilen alternatif bir eğri çizim yöntemi.
    * `Closed` - Tüpü bir döngü haline getirin
    * `Screen` - Etkin olduğunda, yol ekrana 'sabitleme' yapılır, böylece görünümü ve nesneyi hareket ettirebilir, yol yerinde kalır. Devre dışı olduğunda, yol 3d sahnenin bir parçasıdır ve kamera ve nesnelerle birlikte hareket eder.

#### Lathe üst araç çubuğu
![](/images/tool_lathe_top_toolbar.webp)

Bir lathe seçildiğinde, görüntü alanının üst kısmında ek kontroller içeren bir araç çubuğu görünür. Araç çubuğunu daraltmak/genişletmek için başlığına tıklayın ve görüntü alanının üstüne veya altına taşımak için sağ üstteki oka tıklayın.

* `Validate` - Lathe'i, yontulabilmesi için normal poligonlara dönüştürür.
* `Edit` - Eğri noktalarını gösterir, böylece bunlar üzerinde işlem yapılabilir
* `Mirror` - Bu lathe'in ebeveyni olarak bir mirror repeater ekler
* `Snap` - Eğri noktalarını yakın yüzeylere yapıştırır
* `Stable` - Etkinleştirildiğinde, eğri profili lathe'in merkez çizgisine bağlanır. Devre dışı bırakıldığında, merkez çizgi düzenlenebilir ve eğriyi hareket ettirmez, bu da daha karmaşık şekillere izin verir.
* `Focus` - Görünümü, eğri profilini kameraya mükemmel düz görünecek şekilde döndürür.
* `Closed` - Eğrinin başlangıcını ve sonunu birleştirerek bir döngü oluşturur
* `Cap` - Closed devre dışıysa, tüpün her iki ucunda kapak, yalnızca başlangıç veya bitişte kapak veya hiç kapak olmaması arasında geçiş yapar.
* `Hole` - Lathe'i kalınlaştırarak bir boruya dönüştürür. Her iki uçta, yalnızca uçta veya hiç delik olmaması arasında geçiş yapar. 
* `B-spline` - Catmull-rom ve B-spline enterpolasyonu arasında geçiş yapar.
* `X Divisions` - Lathe etrafındaki bölümlerin sayısı, örneğin 4 bölüm kare profilli bir lathe oluşturur. 
* `Constant density` - Etkin olduğunda, poligonları kare tutar. Devre dışı olduğunda, tüp boyunca `Y divisions` ayarlamanıza izin verir.
* `...` - Lathe ayarları menüsü.

#### Lathe ayarları
* `Primitive` - UV'leri etkinleştirmek/devre dışı bırakmak veya tüpü onaylamak için düğmeler.
* `Post subdivision` - Onaylamadan önce çoklu çözünürlük seviyesini ayarlamak için bir kısayol.
* `Linear subdivision` - Onaylamadan önce lineer subdivision seviyesini ayarlamak için kısayol. 
* `Division X` - Araç çubuğundaki X Divisions ile aynıdır.
* `Division Y` - Araç çubuğundaki Y Divisions ile aynıdır.
* `Curve (Repeater)` - Eğri profilini bir [Curve Repeater](scene.md#curve)'a dönüştürür.

### ![](/icons/tool_insert.webp) Insert
Bir nesneyi başka bir nesnenin yüzeyine yerleştirin. Kullanımda Stamp aracına benzer, ancak tam 3d şekiller içindir.

Sol araç çubuğundan bir primitive seçerseniz, herhangi bir yüzeye tıklayıp sürüklemek, tıkladığınız yere bir primitive yerleştirir, sürükleme boyutu ayarlar. Sürüklemeyi bitirdiğinizde, Insert [Transform](#transform) moduna geçer.

Instance modunda, sürükleme, yüzey üzerinde kayan yeni bir instance oluşturur. Boyut, ilk şekilden kopyalanır, bu şekilde başka yüzeyler üzerinde aynı boyutta birçok instance yerleştirebilirsiniz.

Sadece primitive eklemek zorunda değilsiniz! Outliner'dan *herhangi* bir şekil seçin, Insert Instance veya Clone modundaysa, seçili nesnenin kopyalarını diğer yüzeyler üzerinde sürükleyebilirsiniz.

Bir nesnenin özel bir pivotu varsa, bu bir çapa noktası olarak kullanılır. Aşağıdaki videoya bakın.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transform
Bir modeli genellikle başka bir nesnenin yüzeyi üzerinde doğrudan 1 ve 2 parmakla Taşı/Döndür/Ölçekle.

Araç sol araç çubuğuyla kontrol edilir ve 5 düğmesi vardır:

* `Snap` - Modeli diğer yüzeylere yapıştır
* `Group` - Seçili nesne, nesneler ve instance'ların bir kombinasyonuna sahipse, bu, aracın davranışını belirlemenize olanak tanır.
* `Move` - Tek parmak sürükleme nesneyi hareket ettirir. Snap etkin olduğunda, bu, nesneyi parmağınızın altındaki yüzey boyunca kaydırır.
* `Rotate` - Tek parmak sürükleme nesneyi döndürür. Snap etkin olduğunda, parmağınızın altındaki yüzeyin normali etrafında döndürür.
* `Scale` - Tek parmak sürükleme nesneyi ölçeklendirir.

Transform, 2 parmak kullanarak bu modlardan 2'sini hızlıca çalıştırmak için kullanılabilir:

* Bir nesneyi yerleştirmek için sürükleyin. İlk parmağınızı hareket ettirmeyi bırakın, ancak ekrandan kaldırmayın.
* İlk parmağınızı basılı tutarken ikinci parmağınızla ekrana dokunun. İkinci parmak sürüklendikçe nesne ölçeklenir.
* İkinci parmağı kaldırın ve ilk parmağı sürüklemeye devam edin, nesne tekrar move modunda olur.

İkinci mod, ikinci parmakla dokunma jestiyle de değiştirilebilir:

* Nesneyi yerleştirmek için sürükleyin, hareket etmeyi bırakın, ancak parmağınızı ekrandan kaldırmayın.
* İlk parmağınızı basılı tutarken ikinci parmağınızla dokunun
* Araç rotation moduna geçer. Döndürmeyi ayarlamak için ilk parmağınızı sürükleyin.
* Önceki gibi ikinci parmağınızla dokunun, araç tekrar move moduna geçer.

Bu, başka bir nesne üzerinde nesneleri çoğaltmak için hızlı bir iş akışı sunar, örneğin bir manzara üzerinde kayalar. Klon düğmesinin de sol araç çubuğunda kolay erişim için bulunduğuna dikkat edin:

* Transform aracını kullanarak bir kayayı yerine taşıyın.
* Bırakın, clone düğmesine basın
* Bu kayayı hareket ettirin, gerektiği gibi döndürün/ölçeklendirin
* Bırakın, clone düğmesine basın
* Bu kayayı hareket ettirin, tekrarlayın.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo
Bu araç, nesneleri hareket ettirmenize, döndürmenize ve ölçeklendirmenize ve nesnelerin pivotlarını değiştirmenize olanak tanır.

Görüntü alanı tutamacının aşağıdaki özellikleri vardır:

* `Move` - X/Y/Z üzerinde hareket etmek için çizgi+ok üzerinde sürükleyin. Gizmo'nun ortasındaki şeftali rengi noktayı sürükleyerek ekran uzayında serbestçe çevirin. X/Y/Z düzlemlerinde çevirmek için kırmızı, yeşil, mavi karelere tıklayın.
* `Rotate` - X/Y/Z üzerinde döndürmek için kırmızı/yeşil/mavi daireler üzerinde sürükleyin. Serbest döndürmek için dairelerin içindeki küreyi sürükleyin.
* `Scale`- X/Y/Z üzerinde ölçeklendirmek için dış kırmızı/yeşil/mavi noktalar üzerinde sürükleyin. X/Y/Z düzlemlerinde ölçeklendirmek için dış kırmızı/yeşil/mavi koniler üzerinde sürükleyin. Tekdüze ölçeklendirmek için dış şeftali rengi daireyi sürükleyin.

![](/images/tool_gizmo.webp)

#### Düğümler ve köşeler 

Nomad'daki her nesne bir düğüm ve köşelerden oluşur:

* `Node` - Nesnenin, çeviri, döndürme, ölçek (transformasyon matrisi olarak adlandırılır) bilgilerini saklayan 'tutamacı'.
* `Vertices` - Bir nesnenin yüzeyini tanımlayan noktalar, konum ve boya bilgilerini saklarlar.

8 köşeden oluşan basit bir kutunuz varsa, onu transformasyon matrisini değiştirerek veya köşe konumlarını değiştirerek çevirebilirsiniz. Yontma yaparken genellikle köşeleri değiştirmek istersiniz, gizmo ile nesneleri hareket ettirirken genellikle düğümü değiştirmek istersiniz. Nomad her ikisini de yapmanıza izin verir. 

#### Sol menü araç çubuğu

Sol araç çubuğu, gizmo'nun düğüm veya köşeler üzerinde çalışıp çalışmayacağını ve diğer işlevleri kontrol eder:

* `Clone` - Mevcut nesnenin bağımsız bir kopyasını oluşturur, bu kopya gizmo ile uzaklaştırılabilir.
* `Instance` - Mevcut nesnenin bir instance kopyasını oluşturur. Nesneler bağlantılıdır, bu nedenle bir nesnedeki yontma değişiklikleri tüm instance nesnelerde görünür.
* `Group/Object/Vertex/Auto` - Gizmo'nun bir nesnenin düğümünü mü yoksa köşelerini mi etkileyeceğini ayarlar. Varsayılan 'auto' modu en iyi tahmini yapmaya çalışır. Bir hiyerarşide birlikte ebeveynlenmiş birkaç nesne varsa, 'Object' yalnızca mevcut nesneyi hareket ettirir, alt nesneler sabit kalır. Gizmo ayrıca maskeyi ve simetriyi de dikkate alabilir.
* `Pin` - Varsayılan olarak gizmo, seçili nesnenin pivotuna taşınır. Pin etkinleştirildiğinde, gizmo mevcut konumunda kalır.
* `Align` - Pivotun mevcut nesneyle hizalanmasını veya dünya ile hizalanmasını aç/kapat.
* `Snap rotation` - Döndürme değerlerinin artışlara sabitlenmesini etkinleştirir, snap değeri snap etkin olduğunda görüntülenir ve düzenlenebilir.
* `Snap translation` - Çeviri değerlerinin artışlara sabitlenmesini etkinleştirir, snap değeri snap etkin olduğunda görüntülenir ve düzenlenebilir.
* `Pivot` - Etkinleştirildiğinde, gizmo nesneyi hareket ettirmeden hareket ettirilebilir ve döndürülebilir. Aşağıda açıklanan ek bir menüsü vardır.

#### Pivot
Pivot modu etkin olduğunda, hızlı pivot değişikliklerine izin veren bir menü görüntülenir:

**Reset** 
* `Center` - Pivotu nesnenin merkezine taşı
* `Bottom` - Pivotu nesnenin altına taşı
* `Align` - Döndürmeleri dünyaya hizalanacak şekilde sıfırla.
* `Mask` - Pivotu maskesiz bölgenin merkezine taşı.

**On Tap**
* `None` - Nesneye dokunulduğunda hiçbir şey yapma
* `Normal` - Pivotu, yüzeye dokunulan yere taşır ve döndürür
* `First` - Pivotu, yüzeye dokunulan yere taşır (ancak döndürmez)
* `Medial` - Pivotu, yüzeye dokunulan yerin altındaki nesnenin ortasına taşır.

#### Gizmo ayarları

![](/images/tool_gizmo_settings.webp)

##### Matrix 
* ![](/icons/target.webp) `Move origin` - Nesneyi, pivotu sahnenin merkezi olan orijine gelecek şekilde taşır.
* ![](/icons/bake.webp)  `Bake` - Nesneyi mevcut konumunda dondurur ve translate/rotate değerlerini 0'a, scale'i 1'e ayarlar.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - Matris değerlerini, gizmo tutamacının dünyadaki konumuna karşılık gelecek şekilde ayarlar.
* ![](/icons/reset.webp) `Reset` - Çeviri değerlerini 0'a, döndürme değerlerini 0'a, scale'i 1'e ayarlayan ve nesneyi hareket ettirip döndüren bir kısayol.

::: tip Bake vs bake to pivot
Bir kutu oluşturun, Gizmo aracını seçin, ayarlar menüsünü açın ve sabitleyin. Varsayılan olarak çeviri ve döndürme 0, scale 1'dir.

Pivot modunu etkinleştirin, tutamacı bir tarafa taşıyın, pivot modunu devre dışı bırakın. Pivot değişti, ancak çeviri değerlerinin hâlâ 0 olduğuna dikkat edin. 

Pivotun *gerçekte* nerede olduğunu görmek istiyorsanız, `Bake Pivot`a tıklayın. Şimdi çeviri değerleri güncellenir. Kutunun bu işlem sırasında hareket etmediğine ve pivot modunda da hareket etmediğine dikkat edin.

Kutuyu bir yere taşıyıp döndürün, ardından `Move Origin`e tıklayın. Nesneyi pivotu dünyanın merkezinde olacak şekilde taşır, ancak döndürmeyi değiştirmez.

`Reset`e tıklayın, döndürme de 0'a ayarlanır.

Kutuyu tekrar taşıyıp döndürün, bu sefer `Bake`e tıklayın. Pivot olduğu yerde kalır, kutu olduğu yerde kalır, ancak çeviri ve döndürme değerleri 0'a ayarlanır.

Bunu birkaç kez pratik yapın! Pivot değerlerinin gizli olduğunu, Nomad'ın bunu sizin için hallettiğini, ancak pivotu uzaydaki gerçek konumlara ayarlamanız gerektiğinde Bake pivot'un bunu sizin için yapacağını anlayın.

:::

* `Translation` - translate X, Y, Z değerleri
* `Rotation` - rotate X, Y, Z değerleri
* `Scale` - Tekdüze scale etkinse tekdüze scale, devre dışıysa scale X, Y, Z.
* `Uniform scale` - Tekdüze ölçeklendirme veya her eksende bağımsız ölçeklendirme yeteneğini aç/kapat

-----

* `Compact` - Ek tutamaçları döndürme küresinin dışına veya içine yerleştirmek için gizmo düzenini değiştirir
* `Widget size` - Gizmo boyutu
* `Thickness` - Gizmodaki çizgilerin kalınlığı
* `Opacity` - Gizmo opaklığı
* `Hide on interaction` - Sürüklenirken gizmonun geçici olarak gizlenip gizlenmeyeceğini aç/kapat

-----

* `Tangent roll threshold` - X/Y/Z üzerinde döndürmek için daire tutamaçları üzerinde sürüklerken döndürme UI'sinin nasıl davranacağını kontrol eder. Bu değer 0 ise, döndürme bir kadran gibi çalışır, gizmo'yu daireler çizerek sürükleyin. Bu değer 90 ise, döndürme bir yo-yo ipini çekmek gibi çalışır; ilk tıkladığınız yere doğru veya oradan uzağa düz bir çizgide sürükleyin. 0 ile 90 arasındaki değerler her ikisinin bir kombinasyonunu yapar; değerin altındaki hareket doğrusal, üzerindeki hareket dairesel olur.
* `Numerical input` - Etkinleştirildiğinde, gizmo üzerinde tek bir dokunuş, tıklanan widget ekseni için tam bir değer girmek üzere bir pencere açar.

::: warning
[Gizmo](#gizmo), [Translate](#translate), [Rotate](#rotate) ve [Scale](#scale) kendi simetri onay kutularını kullanır!

Varsayılan olarak bu simetri kapalıdır.
:::

Solda, gizmo pivotunu hareket ettirebilirsiniz, aşağıdaki videoda bunu görebilirsiniz.
Bu, özellikle çeviriyi değiştirmediği için döndürme için kullanışlıdır.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Facegroup

Facegroup'lar, nesnenizi farklı renkte yüzeylere ayırmanıza olanak tanır. Bu grupları Nomad'da birçok şekilde kullanabilirsiniz:

* Maskeler için hızlı bir seçim yöntemi
* Nesnenizin bölümlerini gizleme/gösterme
* Nesnenizi ayrı parçalara bölmek zorunda kalmadan düzenleme
* UV bölgeleri tanımlama
* Quad remesher'ı yönlendirme
* Smooth gibi araçlar için ek kontrol.

#### Facegroup sol araç çubuğu

* `Patch ` - Kullanılabilir facegroup'ları patch olarak gösterir. Kullanılmayan patch'ler silinebilir. Bir patch'e dokunarak adını veya rengini değiştirebilirsiniz. Artı simgesi yeni patch'ler oluşturmanıza olanak tanır.
* `Dot` - Nesne üzerinde boyayarak facegroup'ları tanımlayın. '+ Face Group' etkinleştirildiğinde, her yeni vuruş otomatik olarak yeni bir facegroup oluşturur, bu da bölgeleri hızlıca tanımlamak için kullanışlıdır. Bir dokunuş seçili bölgeyi doldurur. Kaydırıcı, noktanın yarıçapını ayarlar.
* `Relax` - Facegroup sınırlarını yumuşatır. Quad remeshing için temiz kenarlar tanımlamak veya sert yüzey modelleme için paneller tanımlamak için çok kullanışlıdır. Kaydırıcılar, relax işleminin yarıçapını ve yoğunluğunu kontrol eder.
* `Shape selector` - Fırça yerine `Lock+Radius`, `Lasso`, `Polygon`, `Rect` ve `Ellipse` aracılığıyla şekillerle facegroup oluşturun. Daha fazla bilgi için [Shape Selector](#shape-selector) bölümüne bakın.
* `Auto-pick` - Etkinleştirildiğinde, vuruşun başladığı yerdeki patch'i seçer ve vuruşun geri kalanı için o patch'i uygular. Facegroup bölgelerini düzenlemek için çok kullanışlıdır; bir facegroup çok uzağa taşmışsa, auto-pick'i etkinleştirin, vuruşa facegroup patch'inin doğru olduğu yerden başlayın ve doğru patch'i yeniden atamak için sınıra kadar sürükleyin.

### ![](/icons/tool_hide.webp) Hide
Nesnenin bölümlerini gizleyin veya izole edin. 

Birincil modlar sol menüden kontrol edilir:

* `Dot` - Nesne üzerinde fırçalayarak nesnenin bölümlerini gizleyin.
* `Shape selector` - Fırça yerine `Lasso`, `Polygon`, `Line`, `Rect` ve `Ellipse` aracılığıyla şekillerle gizleyin. Daha fazla bilgi için [Shape Selector](#shape-selector) bölümüne bakın.
* `Show` - İşlemi tersine çevirir, böylece seçili mod nesnenin bölümlerini gizlemek yerine gösterir.

Görüntü alanının üst kısmında ek kontroller içeren bir araç çubuğu görünür:

* `Clear` - Nesneyi geri yükler, gizli tüm bölümler görünür hale gelir.
* `Invert` - Gizli ve görünür bölümleri değiştirir.
* `Facegroup` - Facegroup'ları kullanarak bölümleri hızlıca gizleyin, bir facegroup'a dokunmak tüm facegroup'u gizler.
* `Mask` - Bir maske etkinse, bu düğmeye dokunmak maskelenmiş bölümü gizler.
* `Delete` - Nesnenin gizli bölümünü siler
* `Split` - Nesnenin gizli bölümünü yeni bir şekle böler.

### ![](/icons/tool_measure.webp) Measure
İki nokta arasındaki mesafeyi ölçmek için sürükleyin.

### ![](/icons/tool_remesh.webp) Quad Remesher

![](/images/tool_quadremesher.webp)

Bu araç, seçili nesneyi yoğunluk, edge flow, simetri kontrolleriyle temiz bir quad topoloji düzenine dönüştürür. 

::: tip
Quad Remesher, iOS ve masaüstü için [Exoside](https://exoside.com/) tarafından geliştirilmiştir. 

iOS için Nomad içinde bir uygulama içi satın almadır, tek seferlik 16 USD ödemedir.

Masaüstü için, [Exoside](https://exoside.com/quadremesher/quadremesher-buy/) üzerinden bir lisans satın alın. Yalnızca Nomad masaüstü için veya desteklenen tüm masaüstü uygulamaları için çapraz lisans satın alabilirsiniz.

Quad Remesher'a zaten başka bir masaüstü uygulaması için sahipseniz, [tüm platformlara daha düşük maliyetle yükseltme satın alabilirsiniz.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher Android için mevcut değildir. Android, Topology -> Misc menüsü altında bulunan ücretsiz açık kaynaklı 'Quad Remesh - Instant'ı kullanabilir, ancak özellik setinin çok sınırlı olduğunu unutmayın.
:::

Bu araç ilk kez etkinleştirildiğinde, uygulama içi satın alma olarak etkinleştirmek isteyip istemediğinizi soracaktır. Etkinleştirildiğinde, sol ve üst araç çubukları etkin hale gelir.

* `Dot` - Bu fırça hedef yoğunluğu ayarlar. Yoğunluk %100 iken kırmızı boyar, bu da o bölgelerde hedef quad yoğunluğunun iki katını kullanır. Yoğunluk %0 iken camgöbeği (cyan) boyar, bu da o bölgelerde hedef quad yoğunluğunun yarısını kullanır. Yoğunluk %50 iken gri boyar, bu da varsayılan hedef quad yoğunluğunu kullanır.
* `Smooth` - Kırmızı/gri/camgöbeği yoğunluk geçişlerini yumuşatır.
* `Curve` - Heykelin yüzeyi üzerinde eğriler çizin, quad remesher bunları kenar akışı için kılavuz olarak kullanacaktır. Bir eğriye dokunarak onu silebilirsiniz.
* `Path` - Heykelin yüzeyi üzerinde yollar çizin, quad remesher bunları kenar akışı için kılavuz olarak kullanacaktır. Bir yola dokunarak onu silebilirsiniz. 
* `Rect` - Heykelin yüzeyi üzerinde dikdörtgenler çizin, quad remesher bunları kenar akışı için kılavuz olarak kullanacaktır. Bir yola dokunarak onu silebilirsiniz.
* `Ellipse` - Heykelin yüzeyi üzerinde elipsler çizin, quad remesher bunları kenar akışı için kılavuz olarak kullanacaktır. Bir yola dokunarak onu silebilirsiniz.

#### Quad remesher üst araç çubuğu
![](/images/tool_quadremesher_toolbar.webp)

Görünüm penceresinin üst kısmında ek kontroller içeren bir araç çubuğu görünecektir:


* `<Count>` - Quad remesher sürecini başlatmak için buna tıklayın, bu sayı hedef quad remesh sayısının ne olacağını gösterir.
* `Quads` - Hedef quad sayısını sola ve sağa kaydırarak ayarlayın veya tam bir sayı girmek için dokunun. Bunun sabit bir sayıdan çok bir kılavuz olduğunu unutmayın; quad remesher üzerindeki çeşitli kontroller, sonucun çoğu zaman bu hedefle tam olarak eşleşmemesi anlamına gelir.
* `Half` - Hedef sayıyı mevcut poligon sayısının yarısına ayarlamak için bir kısayol.
* `Same` - Hedef sayıyı mevcut poligon sayısına ayarlamak için bir kısayol.
* `Guides` - Toplam kılavuz sayısını gösterir veya tüm kılavuzları silmek için dokunun.
* `Density X` - Tüm yoğunluk boyamasını kaldırmak için dokunun.
* `Density (painting)` - Yoğunluk boyamasını kullanmak veya yok saymak için aç/kapat.
* `Face Group` - Quad remesher’i yönlendirmek için yüz gruplarını kullanmak veya yok saymak için aç/kapat.
* `Relax` - Quad remeshing sırasında yüz grup sınırlarını otomatik olarak gevşetmek için aç/kapat. Yüz grup sınırlarınızı zaten gevşetmiş/yumuşatmışsanız bu seçeneği devre dışı bırakın.
* `Relax Slider` - Yüz grup sınırlarını gevşetmek için bir kısayol kaydırıcısı.
* `Hard Edges` - Sert kenarları korumaya çalışmak için aç/kapat.
* `Reproject Vertex` - Yeni yerleşimi giriş mesh’ine yeniden yansıtmak için aç/kapat.
* `Symmetry` - Simetrik bir sonuç elde etmek için aç/kapat. Simetrinin her zaman dünya x ekseni etrafında hesaplandığını unutmayın, bu nedenle simetrik bir sonuç bekliyorsanız modelinizin orijinde olduğundan emin olun.
* `...` - Quadremesher ayarları menüsü. 

#### Quad remesher ayarları menüsü

Bu ayarların çoğu üst araç çubuğunda mevcuttur.

* `<Count>, Half, Same` - Üst araç çubuğundaki Remesh, Half, Same düğmeleriyle aynıdır.
* `Target Quads` - Üst araç çubuğundaki `Quads` düğmesiyle aynıdır.
* `Adaptive quad count` - Yüksek eğrilik alanlarında daha küçük, düşük eğrilik alanlarında daha büyük quad’lar kullanmayı etkinleştirmek için aç/kapat.
* `Adaptive size` - Uyarlanabilirlik miktarını ayarlayın. %100 maksimum uyarlanabilir boyuta izin verir, %0’da quad’lar tekdüze olur.
* `Auto-Detect Hard Edges` - Quad remesh yerleşimini keskin yüzeyleri daha iyi takip edecek şekilde uyarlamak için aç/kapat.
* `Density (painting)` - Üst araç çubuğundaki `Density (painting)` düğmesiyle aynıdır.
* `Reproject Vertex` - Yeni yerleşimi giriş mesh’ine yeniden yansıtmak için aç/kapat.
* `Face Group` - Üst araç çubuğundaki `Face Group` düğmesiyle aynıdır.
* `Relax Slider` - Yüz grup sınırlarını gevşetmek için bir kısayol kaydırıcısı.

::: tip

En az yapaylıkla iyi bir quad remesh elde etmek için bir tarif:

* İdeal quad akışınızı tanımlamak için mesh’i yüz gruplarına ayırın (facegroup).
* Yüz grup sınırlarını yumuşatmak için facegroup relax uygulayın.
* Decimate uygulayın. Bu, yüz grup kenarında ince veya bozulmuş yüzlerinizin olmamasını sağlayacaktır. Decimate ayarlarında facegroup’un etkin olduğundan emin olun. Bu, üçgen kenarlarının yüz grup kenarlarını tam olarak takip etmesini sağlayacaktır. 

Quad remesh seçeneklerinde relax’in devre dışı olduğundan emin olun (mesh’i zaten gevşetmiş olduğunuz için) ve iyi sonuçlar elde etmelisiniz.

:::

### ![](/icons/tool_select.webp) Select
Sahnedeki nesneleri seçmek için şekil modlarını kullanın. `Unselect` seçimi nesnelerden kaldırır.

### ![](/icons/tool_view.webp) View
Bu "araç" özel olarak hiçbir şey yapmaz, bu yalnızca sahnenizi değiştirmeden modeli görüntülemenin bir yoludur.


## Araç kutusu bağlam menüsü

![](/images/tools_context_menu.webp)

Araç kutusundaki bir araca sağ tıklamak veya uzun basmak bir bağlam menüsü açar. Bu menüde şu seçenekler bulunur:

* `Save` - araçta yaptığınız değişiklikleri kaydedin
* `Clone` - aracı yeni bir araç kısayoluna kopyalayın
* `Last save` - aracı en son kaydedilen sürümüne geri döndürün
* `Icon` - araç için simgeyi değiştirin
* `Reset` - aracı varsayılanlarına sıfırlayın
