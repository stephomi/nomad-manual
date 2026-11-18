# ![](/icons/toolbox.webp) Araçlar {#tools}

![](/images/tools_menu.webp)

::: tip
Araçların tek tek açıklamaları için aşağıdaki [Araçlar](#tools-1) bölümüne geçin.
:::

## Genel Bakış {#overview}

Araçlar sağdaki `Araç kutusu`ndan seçilir ve soldaki `Araç Kontrolleri` ile yönetilir. Ek ayarlar, sağ üstteki menüde bulunan `Araç` menüsündedir.

Fırça araçlarında boyut ve yoğunluk kontrolleri bulunur. Seçim araçlarında ise çeşitli seçim biçimleri için kontroller vardır. Araç kontrollerinin alt kısmında sık kullanılan işlemler için kısayollar yer alır (Pürüzsüzleştir, Maske, Gizle, Yüz Grubu, Gizmo, Renk, Alfa).

Nomad'ın araçları araç kutusunda renklerle gruplanmıştır (düz etiketler için [Arayüz](interface.md) menüsünde `Renkli araçlar` seçeneğini kapatın):

* <span class=brush>**Fırça araçları**</span> (Kil, Fırça, Pürüzsüzleştir, Katman, Şişir, KatmanSil, Quad Remesher)
* <span class=move>**Taşıma araçları**</span> (Taşı, Sürükle, Elastik, Dürt)
* <span class=mask>**Maske aracı**</span> (Maske)
* <span class=paint>**Boyama araçları**</span> (Boya, Leke)
* <span class=flatten>**Düzleştirme araçları**</span> (Düzleştir, Düzlemsel, Parlat)
* <span class=pinch>**Kıstırma araçları**</span> (Oluk, Kıstır)
* <span class=stamp>**Damga araçları**</span> (Damga, VDM)
* <span class=selection>**Seçim tabanlı araçlar**</span>: önce 2d bir maske çizilir, ardından bir işlem uygulanır (Kes, Ayır, Yansıt)
* <span class=creation>**Oluşturma araçları**</span> (Tüp, Torna, Ekle)
* <span class=transform>**Dönüştürme araçları**</span> (Dönüştür, Gizmo, Düzenle, Kafes)
* <span class=misc>**Çeşitli araçlar**</span> (Yüz Grubu, Gizle)
* <span class=view>**Görünüm araçları**</span> (Görüntüle, Ölç, Seç)



Bu araçların birçoğu, [Darbe](stroke.md) menüsü aracılığıyla farklı fırça davranışları, basım şiddeti, dokular vb. ile özelleştirilebilir. 


### Fırça kontrolleri {#brush-controls}

Sol araç çubuğunda yarıçap ve yoğunluk kaydırıcıları, ardından aracın kategorisine özel kontroller bulunur; bunlar aşağıda açıklanmıştır.

![](/images/tool_left_panel.webp)

::: tip
Birçok aracın yoğunluk kaydırıcısı %100'ün üzerine çıkabilir, denemeye değer!
:::

### Alt mod {#sub-mode}
Yoğunluk kaydırıcısının hemen altındaki düğme `Alt` düğmesidir. Etiketi ve işlevi her araçla değişir; basıldığında genellikle tersi olan alternatif bir davranışı devreye sokar. Örneğin [Boya](#paint) için bir silme modunu çağırır, [Oluk](#crease) için ise oluk yerine kabarık kenarlar oluşturur.

Varsayılan olarak yapışkan bir düğme gibi çalışır: geçici olarak etkinleştirmek için basılı tutabilirsiniz, bıraktığınızda kapanır. Üzerine dokunursanız alt mod kalıcı olarak etkin kalır.

### Kısayollar {#shortcuts}
Sol araç çubuğunun altında [Pürüzsüzleştir](#smooth), [Maske](#mask), [Gizle](#hide), [Yüz Grubu](#facegroup), [Gizmo](#gizmo), [Renk](painting.md#pbr-sliders) ve [Alfa](stroke.md#alpha) kısayolları bulunur. 

Varsayılan olarak bunların hepsi yapışkan düğme gibi çalışır: geçici olarak etkinleştirmek için basılı tutabilirsiniz, bıraktığınızda kapanır. Üzerine dokunursanız o kısayol modu kalıcı olarak etkin kalır.

### Seçim kontrolleri {#selection-controls}

[Maske](#mask), [Boya](#paint), [Kes](#trim), [Ayır](#split), [Yansıt](#project), [Yüz Grubu](#facegroup), [Gizle](#hide) ve [Seç](#select) araçları, ağın bölgelerini seçmek için benzer kontroller kullanır.

![](/images/tools_shape_selector_panel.webp)

Şekilleri içeren bir açılır pencere açmak için sol araç çubuğundaki şekil düğmesine dokunun (geçerli şekli gösterir, varsayılan olarak `Lasso`). Fırçayla da çalışan araçlarda (Maske, Boya, Yüz Grubu, Gizle) aynı açılır pencerede darbe türleri de bulunur.

* `Görüntüle` - Şekil yok; araç, kamera modu gibi özel bir şey yapmaz.
* `Lasso` - Serbest elle çizilen bir şekil
* `Poligon` - Eğrilerin ve/veya düz çizgilerin birleşimiyle tanımlanan kapalı bir şekil. Daha fazla bilgi için aşağıdaki [Şekil düzenleme](#shape-editing) bölümüne bakın.
* `Eğri` - (Yalnızca Yansıt) - Yansıtma için serbest elle çizilen bir eğri
* `Yol` - (Yalnızca Yansıt) - Noktalarla tanımlanan bir eğri. Daha fazla bilgi için aşağıdaki [Şekil düzenleme](#shape-editing) bölümüne bakın.
* `Çizgi` - Düzlemsel bir kesit tanımlamak için bir çizgi sürükleyin. Varsayılan olarak işlem ağa hemen uygulanır; bunu istemiyorsanız `Düzenle` seçeneğini değiştirin (çizgi simgesine uzun basın veya kaydırın)
* `Şerit` - İki paralel kılavuz arasında, boyunca bir gradyan olan bir şerit. `Uzat`, şeritte durmak yerine uzaktaki kılavuzun ötesinde de tam değeri korur; `Ters çevir`, gradyanın hangi kılavuzdan başlayacağını değiştirir.
* `Dikdörtgen` - Çapraz bir çizgi sürükleyin, bu çizgi dikdörtgenin köşelerini belirler. `Düzenle` seçeneğini, şekli kareye zorlayan `Kare` seçeneğini ve ilk tıklamayı dikdörtgenin merkezi yapan `Ortalanmış` seçeneğini görmek için uzun basın veya kaydırın.
* `Elips` - Çapraz bir çizgi sürükleyin, bu çizgi elipsin boyutunu belirler. `Düzenle` seçeneğini, şekli daireye zorlayan `Daire` seçeneğini ve ilk tıklamayı elipsin merkezi yapan `Ortalanmış` seçeneğini görmek için uzun basın veya kaydırın.
* `Ters Çevir` - Şekil maskesini veya Yansıt aracının yönünü tersine çevirir.

Çoğu aracın, şekli çizmeyi bitirdiğinizde ne olacağını belirleyen bir `Düzenle` seçeneği vardır:
* `Düzenle: kapalı` - İşlem, parmağınızı kaldırır kaldırmaz uygulanır.
* `Düzenle: açık` - Şekil düzenlenebilir kalır. Şeklin yanında, işlemi uygulayan yeşil bir düğme çizilir. Böylece şekli düzenleyebilir, görünümü ayarlayabilir ve şekli kullanmaya hazır olduğunuzda yeşil düğmeye basabilirsiniz.
* `Düzenle: basılı tut` - İşlem bırakınca uygulanır; ancak şekli düzenlemeye devam etmek için darbenin sonunda basılı tutabilirsiniz.

### Şekil düzenleme {#shape-editing}
Poligon düzenleme ve eğri düzenleme benzer şekilde çalışır:

* Başlamak için 2 nokta tanımlayan bir çizgi sürükleyin, ardından bir poligon veya eğri oluşturmak için çizginin ortasından dışarı doğru sürükleyin.
* Yumuşak ve keskin arasında geçiş yapmak için noktalara tıklayın. 
* Yeni noktalar oluşturmak için eğri veya çizgi parçalarına tıklayıp sürükleyin.
* Bir noktayı silmek için onu kırmızıya dönene kadar komşusunun üzerine sürükleyin.
* Poligon veya yol simgesinin köşesindeki çöp kutusu simgesi şekli siler.

### Ayarlar menüsü {#settings-menu}

Birçok aracın, sağ üstteki menüde bulunan `Araç` menüsünde ek ayarları vardır. Ek ayarı olmayan araçlarda bu menü soluk görünür.

![](/images/tools_settings_menu.webp)

## Araçlar {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)    <br> [Kil](#clay)        | ![](/icons/tool_brush.webp)   <br> [Fırça](#brush)     | ![](/icons/tool_move.webp)       <br> [Taşı](#move)              | ![](/icons/tool_drag.webp)      <br> [Sürükle](#drag)        | ![](/icons/tool_elastic.webp)   <br> [Elastik](#elastic)     | ![](/icons/tool_smooth.webp)  <br> [Pürüzsüzleştir](#smooth) |
| ![](/icons/tool_mask.webp)    <br> [Maske](#mask)      | ![](/icons/tool_paint.webp)   <br> [Boya](#paint)      | ![](/icons/tool_smudge.webp)     <br> [Leke](#smudge)            | ![](/icons/tool_flatten.webp)   <br> [Düzleştir](#flatten)   | ![](/icons/tool_planar.webp)    <br> [Düzlemsel](#planar)    | ![](/icons/tool_polish.webp)  <br> [Parlat](#polish)   |
| ![](/icons/tool_crease.webp)  <br> [Oluk](#crease)     | ![](/icons/tool_pinch.webp)   <br> [Kıstır](#pinch)    | ![](/icons/tool_trim.webp)       <br> [Kes](#trim)               | ![](/icons/tool_split.webp)     <br> [Ayır](#split)          | ![](/icons/tool_project.webp)   <br> [Yansıt](#project)      | ![](/icons/tool_layer.webp)   <br> [Katman](#layer)    |
| ![](/icons/tool_inflate.webp) <br> [Şişir](#inflate)   | ![](/icons/tool_nudge.webp)   <br> [Dürt](#nudge)      | ![](/icons/tool_stamp.webp)      <br> [Damga](#stamp)            | [VDM](#vdm)                                                  | ![](/icons/tool_clearLayer.webp) <br> [KatmanSil](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tüp](#tube)        |
| ![](/icons/tool_lathe.webp)   <br> [Torna](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Ekle](#insert)     | ![](/icons/tool_transform.webp)  <br> [Dönüştür](#transform)     | ![](/icons/tool_gizmo.webp)     <br> [Gizmo](#gizmo)         | ![](/icons/tool_faceGroup.webp) <br> [Yüz Grubu](#facegroup) | ![](/icons/tool_hide.webp)    <br> [Gizle](#hide)      |
| ![](/icons/tool_measure.webp) <br> [Ölç](#measure)     | [Düzenle](#arrange)                                      | ![](/icons/tool_remesh.webp)     <br> [Quad Remesher](#quad-remesher) | ![](/icons/tool_select.webp)    <br> [Seç](#select)          | ![](/icons/tool_lattice.webp)   <br> [Kafes](#lattice)       | ![](/icons/tool_view.webp)    <br> [Görüntüle](#view)  |

------

### ![](/icons/tool_clay.webp) Kil {#clay}
Kil aracı, heykelinize hacim eklemek için idealdir. `Alt`, heykelinizden malzeme kaldırır.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Fırça {#brush}
Standart fırça. `Alt` malzeme kaldırır.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Taşı {#move}
Fırçanın altındaki bölge fırçaya yapışır ve elastik bir deformasyon sağlar. Seçim taşıma boyunca korunur; yani fırçayı uzaklaştırıp sonra başladığınız yere geri getirirseniz hiçbir deformasyon görmezsiniz.

Alt mod `Normal boyunca`'dır; fırçanın altındaki bölgeyi yüzey normali boyunca hareket ettirir.

Bu fırça hem büyük ölçekli deformasyonlar hem de dikkatli, küçük deformasyonlar için uygundur.

#### Taşı ayarları {#move-settings}

* `Yarıçap (Arka Plan)` - Modelin kenarından ne kadar uzakta olursanız olun hâlâ yontabileceğinizi belirler; bir nesnenin silueti üzerinde çalışırken kullanışlıdır. Yalnızca model üzerinde başladığınızda yakalamak için işareti kaldırın.
* `Sadece aynı taraftaki verteks` - Deformasyonun ters yönüne bakan verteksleri yok sayar.
* `Yön` - `Normal boyunca` alt modu tarafından kullanılır; bir sürüklemenin yüzeyi itip itmeyeceğine ya da çekip çekmeyeceğine karar verir:
    * `Otomatik` - Yüzey normalinin açısına göre aşağıdaki iki yöntemden birini sizin için seçer.
    * `Normal 3D` - İmlecin ekrandaki konumunu, kameradan görüldüğü hâliyle yüzey normaliyle karşılaştırır.
    * `XY` - İtme veya çekmeye karar vermek için imlecin ekrandaki konumunu (yukarı/aşağı, sol/sağ) kullanır.
    * `Eşik` - `Otomatik` ile, hangi yöntemin kullanılacağına karar veren açı sınırı.
* `Yuvarlanma hızı` - Yakaladığınız bölgeyi taşırken döndürebilirsiniz: iki parmağınızı döndürün, kaleminizin gövdesini çevirin veya fareyle sürüklerken bir değiştirici tuşu (Alt, Ctrl, Shift veya Cmd) basılı tutun. Parmak, kalem ve fare için ayrı birer kaydırıcı vardır; bir girişi kapatmak için işaretini kaldırın.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Sürükle {#drag}
Fırçanın altındaki bölge fırçaya yapışır ve elastik bir deformasyon sağlar. Taşı fırçasından farklı olarak seçim darbe boyunca sürekli güncellenir; bu sayede, özellikle Dinamik Topoloji etkinken, daha uzun, yılan benzeri nesneler oluşturmak mümkündür.

Alt mod `Normal boyunca`'dır; fırçanın altındaki bölgeyi yüzey normali boyunca hareket ettirir.

Bu fırça daha serbest, jest niteliğinde şekil değişiklikleri için uygundur.

#### Sürükle ayarları {#drag-settings}

Sürükle, [Taşı](#move-settings) ile aynı ayarlara sahiptir: `Yarıçap (Arka Plan)`, `Sadece aynı taraftaki verteks`, `Yön` ve `Yuvarlanma hızı`.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_elastic.webp) Elastik {#elastic}
Yüzeyi [Taşı](#move) gibi yakalayıp çekin, ancak elastik bir deformasyonla: çekme etkisi fırçanın kenarında durmak yerine nesne boyunca mesafeyle birlikte yumuşakça azalır, biraz kauçuğu germeye benzer. Fırça yarıçapı, çekmenin ne kadar geniş olacağını belirler.

Alt mod `Normal boyunca`'dır; fırçanın altındaki bölgeyi yüzey normali boyunca hareket ettirir.

Bu fırça, yumuşak kalan büyük ve hafif oran değişiklikleri için uygundur.

#### Elastik ayarları {#elastic-settings}

Elastik, `Sadece aynı taraftaki verteks` dışında [Taşı](#move-settings) ile aynı ayarlara sahiptir. `Yarıçap (Arka Plan)` varsayılan olarak kapalıdır.

### ![](/icons/tool_smooth.webp) Pürüzsüzleştir {#smooth}
Nokta konumlarının ortalamasını alarak bölgeyi pürüzsüzleştirir. Bu araç büyük ölçüde poligon yoğunluğuna bağlıdır.
Yani çok sayıda poligonunuz varsa pürüzsüzleştirme daha az etkili olur.

Alt mod `Rahatlat`'tır; yalnızca tel kafesi pürüzsüzleştirir ama geometrik detayları korumaya çalışır.

#### Pürüzsüzleştir ayarları {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Yüz Grubu {#smooth-facegroup}

* `Rahatlat` - Yüz gruplarının sınırlarını pürüzsüzleştirir. Sınırları hızlıca pürüzsüzleştirmek için %100'ün üzerinde yoğunluk kullanın. `Otomatik` yalnızca yüz grubu önizlemesi etkinse pürüzsüzleştirir, `Hayır` devre dışı bırakır, `Evet` etkinleştirir. 

##### Verteks {#vertex}
* `Hacmi koru` - Yüzeyi küçültmeden pürüzsüzleştirir; böylece tekrarlanan pürüzsüzleştirmeler şekillerinizi söndürmez. Yanındaki çark düğmesi, bunun için kullanılan `Küçült` ve `Şişir` miktarlarını içerir.
* `Sınırı koru` - Açık kenarları olan ağlarda, örneğin bir düzlemde, köşeler pürüzsüzleşip yuvarlanabilir. Bu seçeneği etkinleştirmek, ağın sınırındaki verteksleri yerinde tutar.
* `Stabil düzleştirme` - Pürüzsüzleştirmeyi topolojiden bağımsız hâle getirmeye çalışır. Değişken topoloji yoğunluğunda ve yüksek bir pürüzsüzleştirme yoğunluğu değeriyle en iyi sonucu verir.
* `Rahatlat` - Sol araç çubuğundaki Rahatlat alternatif moduyla aynıdır.

##### Boyama {#painting}
* `Ekran düzleştirme` - Yüksek poligon sayılarında bile topolojiden bağımsız pürüzsüzleştirme elde etmek için bu seçeneği kullanın. `Otomatik`, `Hayır` veya `Evet`.
* `Ekran örnekleri` - Pürüzsüzleştirmenin kalitesi; daha yüksek değerler daha pürüzsüz ama daha yavaştır.

::: tip
Daha yüksek poligon yoğunlukları, yoğunluğu %100'ün üzerine çıkarmayı gerektirebilir. Çok yüksek değerler (%300, %500) yontma aracı olarak da işe yarayabilir: fırçanın altındaki bölgeleri hızla düz ve pürüzsüz olmaya zorlar, tıpkı kile tokmakla vurmak gibi!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Maske {#mask}
Bu araç verteksleri maskelemenizi sağlar. Maskelenmiş verteksler yontmaya ve boyamaya karşı korunur. 

Alt mod `Maske Yok`'tur; maskenin boyandığı yerleri siler.

2d boyama programlarındaki seçimlere benzer şekilde, maskeler bir fırçayla boyanabilir veya şekil seçimleriyle (`Lasso`, `Dikdörtgen`, `Şerit`...) oluşturulabilir, bulanıklaştırılabilir veya keskinleştirilebilir. Fırçayı ya da şekli sol araç çubuğundaki darbe açılır penceresinden seçin, bkz. [Seçim kontrolleri](#selection-controls).

2d boyama programlarından farklı olarak maskeler yüz grupları üzerinden de oluşturulabilir ve maskeler, ekstrüzyon/çıkarma tarzı işlemlerle yeni geometri oluşturmak için kullanılabilir. 

![](/videos/tool_mask1.mp4)

 Görünümün üst kısmında ek kontroller içeren bir araç çubuğu belirir. 

![](/images/tool_mask_toolbar.webp)

Çubuğun başlığına dokunarak çubuğu genişletebilir/daraltabilir, sağ üstteki oka dokunarak da arayüzün üstüne veya altına taşıyabilirsiniz.

| Eylem                                              | Açıklama                                                                                   |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Tümünü temizle     | Tüm nesnelerdeki maskeyi temizler. Başka nesneler de maskeliyse, ek bir `Kaldır` düğmesi yalnızca seçili nesnelerin maskesini temizler |
| ![](/icons/invert.webp)        Ters Çevir         | Maskeyi tersine çevirir                                                                    |
| ![](/icons/sharpen.webp)       Keskinleştir       | Maske kenarını keskinleştirir                                                              |
| ![](/icons/blur.webp)          Bulanıklık         | Maske kenarını bulanıklaştırır                                                             |
| ![](/icons/outline.webp)       Kenar              | Ağın açık sınırını maskeler, örneğin bir düzlemin kenarını veya bir deliğin ağzını         |
| ![](/icons/blur.webp)          Bulanıklık ->      | Maskeyi bulanıklaştırmak için sağa, keskinleştirmek için sola sürükleyin                   |
| ![](/icons/circle_plus.webp)   Büyüt ->           | Maskelenen bölgeyi büyütmek için sağa, küçültmek için sola sürükleyin                      |
| ![](/icons/intensity.webp)     Güçlendir ->       | Maskenin şeklini değiştirmeden güçlendirmek için sağa, seyreltmek için sola sürükleyin     |
| ![](/icons/dig.webp)           Boşluk ->          | Maskeyi yüzey eğriliğinden yeniden oluşturur: yalnızca çukurların boyanabilir kalması için sağa, yalnızca kabartıların boyanabilir kalması için sola sürükleyin |
| ![](/icons/culling.webp)       Ön                 | Yalnızca öne bakan verteksleri maskelemek için açıp kapatın                                |
| ![](/icons/eye_open.webp)      Görülebilir        | Şekillerle kullanıldığında, başka yüzeylerin arkasında gizli kalan verteksleri yok saymak için açıp kapatın |
|                                 Dönüştür           | Maskeyi bir yüz grubuna dönüştürür                                                         |
| ![](/icons/group_to_mask.webp) Dokunuşta (yüz grubu) | Etkinken yüz grupları gösterilir; bir yüz grubuna dokunmak onu maskeler                 |
|                                 Dokunuşta (maske)  | Etkinken maskeli veya maskesiz poligonlardan oluşan bir 'adaya' dokunmak o adayı tamamen doldurur. |
| ![](/icons/connect.webp)       Bağlı              | Etkinken maske darbelerinin yalnızca bağlı topolojiyi etkilemesine izin verir.             |

##### Maske hızlı hareketleri {#mask-quick-gesture}
Sol araç çubuğundaki hızlı maskeleme düğmesini basılı tutarken ZBrush tarzı hareketler yapabilirsiniz:
| Eylem   | Hareket (sol alttaki kısayolu basılı tutun) |
| :-----: | :--------------------------------: |
| Ters Çevir | Arka plana dokunun              |
| Kaldır  | Arka planda sürükleyin             |
| Bulanıklık | Maskeli bölgeye dokunun         |
| Keskinleştir | Maskesiz bölgeye dokunun      |


#### Maske ayarları {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

Maske ayarları esas olarak maskeden geometri oluşturmak için kullanılır. Üstteki sekmeler işlemi seçer: [Çıkar](#extract), [Ayır](#split-mask) veya [Oyma](#carve). Altlarındaki seçenekler işleme göre değişir.

* `Önizleme` - Ayarları değiştirirken yeni geometrinin nasıl görüneceğini gösterir.
* `X-Ray` - Önizleme sırasında hangi nesnelerin x-ray ile çizileceği: `Yok`, `Seçilmemiş`, `Seçilen` veya `Tümü`.

##### Çıkar {#extract}
* `Çıkar` - Çıkarılan geometriyi yeni bir nesne olarak oluşturur.
* `Kapatma eylemi` - Çıkarılan şeklin nasıl kapatılacağı. `Yok`, maskelenen poligonları yeni bir şekle kopyalar ve açık bırakır. `Doldur` aynısını yapar, ayrıca arkadaki deliği doldurup pürüzsüzleştirir (düz yüzeylerde kullanmayın). `Kabuk`, şekli `Yükseklik` değerini kullanarak kapatır ve varsayılan seçenektir.

::: tip

Önizleme x-ray ile etkinse, Çıkar düğmesine tıklamak ilk başta kafa karıştırıcı olabilir. Menü açık olduğu için yeni şekliniz üzerinde bir çıkarma önizlemesi yapmaya çalışır ve orijinal yüzeyi x-ray ile gösterir. Ancak yeni yüzeyde maske olmadığından çıkarmayı önizleyemez ve Nomad sizi 'Çıkarılacak bir şey yok!' diye uyarır. 

Bu normaldir; yeni şekli ve orijinali görmek için maske ayarları menüsünü kapatın ve maskeyi temizlemeniz veya yeni maskeler çizmeniz gerekiyorsa orijinal yüzeyi yeniden seçin.
:::

##### Ayır {#split-mask}
* `Ayır` - Hem maskeli HEM DE maskesiz bölgeleri yeni şekillere çıkarır. 
* `Kapatma eylemi` (maskeli) - Maskeli parçanın nasıl kapatılacağı; Çıkar ile aynı `Yok`, `Doldur` ve `Kabuk` seçenekleri.
* `Kapatma eylemi` (maskesiz) - Maskesiz parçanın nasıl kapatılacağı; aynı seçenekler.

##### Oyma {#carve}
* `Oyma` - Yüzeyi `Yükseklik` kadar derinlemesine kesmişsiniz gibi davranır, portakal kabuğundan bir parça kesip çıkarmak gibi. `Yükseklik` 0 olamaz.

##### Yükseklik {#thickness}
* `Yükseklik` - Çıkarılan şeklin yüksekliği. Artı/Eksi düğmesi dışa doğru ekstrüzyon, içe doğru ekstrüzyon veya iki yöne birden arasında geçiş yapmanızı sağlar. 

##### Pürüzsüzlük {#smoothness}
Etkinken çıkarılan şekli pürüzsüzleştirir; daha yüksek poligon sayılarında daha iyi çalışır. 
* `Tümü` / `Yalnızca kenarlar` - Şeklin tamamını veya yalnızca kenarlarını pürüzsüzleştirir; ikincisinde üst yüzeyin şekline dokunulmaz.
* `İterasyonlar` - `Tümü` ile uygulanan pürüzsüzleştirme miktarı. Yüksek değerler çok pürüzsüz, kavisli kenarlar oluşturur ama maskenin şeklinden uzaklaşmaya başlar.
* `Duvar` - `Yalnızca kenarlar` ile duvarlardaki pürüzsüzleştirme miktarı. Düğmesi, keskin köşeleri koruyan Rahatlat ile onları da yuvarlayan Pürüzsüzleştir arasında geçiş yapar.
* `İç kısım` - `Yalnızca kenarlar` ile üst yüzeyin ne kadar düzleştirileceği. Düğmesi, yontulmuş detayları koruyup yalnızca ekstrüzyon yönünü düzelten (böylece detaylar sivri çıkıntılar oluşturmaz) Rahatlat ile yüzeyin kendisini pürüzsüzleştiren Pürüzsüzleştir arasında geçiş yapar.

##### Yanlar {#edge-loop-side}
* `Düz` - Çıkarılan şeklin yanlarında düz duvarlar.
* `Pah` - (Yalnızca `Kabuk` ile Çıkar) Ön kenarda eğimli bir kenar şeridi. `Pah` genişliğini `Yükseklik`'in yüzdesi veya dünya birimi olarak belirler (yanındaki düğme ikisi arasında geçiş yapar), `Pah bölümleri` onu alt bölümlere ayırır (varsayılan olarak `Otomatik`), bir eğri ise profilini şekillendirmenizi sağlar.
* `Profil` - Duvarları bir profil eğrisiyle şekillendirir; `Genişlik`, `Yükseklik`'in yüzdesi veya dünya birimi olarak verilir.
* `Maske` - Yükseklik maskeyi takip eder: maskenin bulanık kısımları daha düşük bir yükseklik alır; böylece yumuşak ve değişken yükseklikte şekiller elde edilir.
* `Duvar bölümleri` - Yanlardaki kenar döngüsü sayısı. `Otomatik` ile Nomad, maskelenen bölgenin poligonlarına uyan kare poligonlar oluşturacak bölüm sayısını kendisi seçer.



### ![](/icons/tool_maskSelector.webp) Seçim Maskesi {#selection-mask}
Seçim Maskesi (MaskeSeç) aracı artık [Maske aracının](#mask) bir parçasıdır. Fırça darbesi yerine şekillerle maskelemek için Maske aracının darbe açılır penceresinden bir şekil (`Lasso`, `Poligon`, `Dikdörtgen`...) seçin, bkz. [Seçim kontrolleri](#selection-controls).

`Maske Yok` alt modu şekillerle de çalışır ve şeklin içindeki maskeyi siler.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Boya {#paint}
Renk ve malzeme özelliklerini uygular. Malzeme hakkında daha fazla bilgi için [Boyama](painting.md) bölümüne göz atabilirsiniz.

Alt mod `Sil`'dir ve boyayı kaldırır.

Fırça darbelerinin yanı sıra Boya, şekilleri de (`Lasso`, `Dikdörtgen`, `Şerit`...) doldurabilir, bkz. [Seçim kontrolleri](#selection-controls).

#### Boya ayarları {#paint-settings}
* `Katman filtreleme` - Photoshop veya Procreate'teki katman alfa kilidi gibi çalışır. Bir katman üzerinde boyuyorsanız ve bu seçenek etkinse, yalnızca zaten boya olan yerleri değiştirebilirsiniz; boyanmamış bölgeler korunur. Yalnızca bir katman seçiliyken kullanılabilir.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Leke {#smudge}
Renk ve malzeme özelliklerini lekeler, yayar. Leke ayarları menüsünde bir `Kalite` kaydırıcısı bulunur; düşük değerler daha hızlı darbeler demektir.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Düzleştir {#flatten}
Noktaları ortalama düzleme yansıtarak bölgeyi düzleştirir.

Alt mod `Doldur`'dur; en yüksek noktaya göre bir düzlem belirler ve noktaları yukarı çekme eğilimindedir.

#### Düzleştir ayarları {#flatten-settings}

* `Düzlem yönünü kilitle` - İlk tıklamada hesaplanan düzlem yönünü kullanır. Varsayılan olarak devre dışıdır.
* `Düzlem kökenini kilitle`- İlk tıklamayı düzlemin merkezi olarak kullanır. Varsayılan olarak devre dışıdır ve yalnızca `Düzlem yönünü kilitle` ile birlikte etkinleştirilebilir.

Bunlardan biri veya ikisi de devre dışıyken, farklı derinlik ve eğriliklerin üzerinden geçen uzun darbelerle düzleştirmeyi kademeli olarak derinleştirebilir veya düzlemin açısını değiştirebilirsiniz. Bu, fırça menüsündeki alan örnekleme seçenekleriyle birlikte çok hassas bir kontrol sağlayabilir.

::: tip
Eğriliği yüksek bölgelerde çalışırken, örneğin yanakları düzleştirmeye çalışırken araç sürekli burnun yanlarını da etkiliyorsa, düzleştirme fırçasının etkilememesi gereken bölgeleri korumak için bir maske oluşturmayı deneyin.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Düzlemsel {#planar}
Noktaları ortalama düzleme yansıtarak düzlemsel hâle getirir, ancak düzleştirme fırçasına göre daha az birikim yapar. Böylece daha temiz, keskin kenarlı yüzeyler oluşur. Hızlı darbeler yüzeyi daha çok iter ve çeker; zaten düz olan bölgelerden başlayıp dışa doğru ilerleyen yavaş darbeler ise düzlemi daha iyi korur.

Alt mod `Doldur`'dur; en yüksek noktaya göre bir düzlem belirler ve noktaları yukarı çekme eğilimindedir.

Düzlemsel aslında `Düzleştir` ile aynı araçtır, ancak `Düzlem yönünü kilitle` etkindir; yani daha kararlı, keskin kenarlı yüzeyler oluşturma eğilimindedir. Düzleştir ise daha heykelsi olabilir ve yarı düz bölgeler oluşturmak için kullanılabilir.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_polish.webp) Parlat {#polish}
Düzleştir ailesinin bir başka üyesi; yüzeyleri temiz düzlemlere dönüştürecek şekilde ayarlanmıştır. `Düzleştir` ile aynı araçtır, ancak [Darbe](stroke.md) varsayılanları farklıdır: `İz`, `Alan Normal Filtresi` ve `Derinlik maskesi` etkindir.

Alt mod, Düzleştir'de olduğu gibi `Doldur`'dur.

Parlat, [Düzleştir](#flatten-settings) ile aynı ayarlara sahiptir: `Düzlem yönünü kilitle` ve `Düzlem kökenini kilitle`.

### ![](/icons/tool_crease.webp) Oluk {#crease}
Oluk araçları küçük kesikler veya çentikler yontmak için kullanışlıdır.

Alt mod `Ters Çevir`'dir ve kabarık bir oluk oluşturur.

#### Oluk ayarları {#crease-settings}

* `Kıstırma gücü` - Verteksleri yanlardan fırçaya doğru ne kadar çekeceği. Kıstırma 1'de ve ofset 0'da ise yüzeyin derinliği hiç değişmez, yalnızca topoloji değişir ve kenarlar darbeye doğru çekilir.
* `Ofset faktörü` - Verteksleri derinlemesine ne kadar itip çekeceği. Kıstırma 0'da ve ofset 1'de ise derin oluklar veya kabarık çentikler oluşur, ancak oluğun yanlarını veya tabanını doğru tanımlayacak kadar geometri oluğa doğru çekilmediği için tırtıklı görünür.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Kıstır {#pinch}
Bu araç kenarları keskinleştirmek için kullanılabilir.

Alt mod `Ters Çevir`'dir ve verteksleri birbirinden uzaklaştırır.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Kes {#trim}
Kes aracı ağınızdan bir parçayı kaldırarak çalışır ve geride kalan boşluğun nasıl işleneceğine dair seçenekler sunar. Kesimi tanımlamak için [Seçim kontrollerini](#selection-controls) kullanır.

Alt mod `Ters Çevir`'dir; şekli tersine çevirerek diğer tarafın kaldırılmasını sağlar.

::: tip
Bu araç kameradan yansıtma yaptığı için, kamera perspektif modundaysa bir uyarı alırsınız.

Ortografik modda ağ boyunca yapılan kesim görünüme paraleldir; genellikle beklenen de budur. Perspektif bir kamerayla yapıldığında ise kesim, nesnenin uzak tarafında yakın tarafına göre farklı görünür.
:::

#### Kes ayarları {#trim-settings}

Ayarlar `Delik doldurma` altında toplanmıştır:

* `Darbe boyama` - Boya menüsünde boyama etkinse, yamalanan bölge seçili renkle doldurulur.
* `Boolean` - Kesimin deliğini dörtgen poligonlu bir bölgeyle doldurur. Doldurulan bölge düz olur.
* `Eski` - Kesimin deliğini üçgenlerden oluşan bir bölgeyle doldurur. Doldurulan bölge düz olur.
* `Doldur` - Deliği üçgenlerden oluşan bir bölgeyle doldurur. Doldurulan bölge, sabun köpüğü zarı gibi kavisli bir yüzey olur.
* `Yok` - Deliği doldurmaz.

`Boolean` ile `Detay` bölümünde şunlar bulunur:

* `Biçim` - Kesimin şekil tarafında kullanılan dörtgen ve üçgenlerin yaklaşık boyutu.
* `Delikleri` - Kesimin doldurulan deliğinde kullanılan üçgen veya poligonların yaklaşık boyutu. `Detay`'ın yanındaki bağlantı düğmesi bunu `Biçim` ile eşit tutar; ayrı ayarlamak için bağlantıyı kaldırın.
* `Topolojiyi koru` - Kesim sınırını pürüzsüzleştirmez ve sadeleştirmez; maskeli ve gizli yüzlerin yakınındaki orijinal ağ topolojisini korur.

`Eski` ile:

* `Detay` - Kesimde kullanılan üçgenlerin yaklaşık boyutu.
* `Delik düzleştirme` - Doldurulan bölgedeki üçgenlerin ne kadar rahatlatılacağı.
* `Eşik epsilon` - Eski delik doldurma algoritmasını iyileştirmek için ayarlanabilen bir değer.

`Doldur` ile:

* `Detay` - Kesimde kullanılan üçgenlerin yaklaşık boyutu.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Ayır {#split}
[Kes](#trim) aracına benzer; farkı, Kes seçimi atarken Ayır'ın seçimi yeni bir nesne olarak tutmasıdır.

Alt mod `Böl`'dür: her parça kendi başına bir nesne olarak tutulur; böylece örtüşen şekiller (örneğin simetriyle) tek parçada birleştirilmek yerine ayrı parçalara kesilir.

#### Ayır ayarları {#split-settings}

Ayır, [Kes](#trim-settings) ile aynı `Delik doldurma` ayarlarına sahiptir: `Darbe boyama`, `Boolean`, `Eski`, `Doldur` ve `Yok` yöntemleri ve bunların `Detay` seçenekleri.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Yansıt {#project}
Yansıt aracı [Kes](#trim) aracına benzer, ancak hiçbir geometri silmez veya oluşturmaz; yalnızca verteksleri seçime uyacak şekilde hareket ettirir.

![](/videos/tool_project.mp4)

::: tip
Yansıt'ı bir katmandayken kullanırsanız, katman kaydırıcısıyla orijinal şekil ile yansıtılmış şekil arasında geçiş yapabilirsiniz.
:::

### ![](/icons/tool_layer.webp) Katman {#layer}
Yüzeyi yükseltir, ancak yüksekliği sınırlar.

Kalemi kaldırmadan bir bölgenin üzerinden fırçalamaya devam ederseniz, Katman belirli bir yüksekliğe kadar yükselir ve daha fazla çıkmaz; diğer araçlar ise yükseklik biriktirmeye devam eder.

Varsayılan olarak bu sınırın yalnızca darbe başına belirlendiğini unutmayın! Yeni bir darbeye başlarsanız, yeni yüzey yüksekliğinden itibaren yükselir.

Birçok darbe boyunca sabit bir en fazla yükseklik belirlemek için Katman aracını Nomad'ın [Katmanlar](layers.md) sistemiyle birlikte kullanın.

Bir katman oluşturun ve bu aracı kullanın. En fazla yükseklik artık katmandan belirlenir; böylece birçok fırça darbesi uygulasanız da yükseklik hep aynı kalır.

`Alt` en düşük bir derinlik kullanarak oluklar oluşturur.

#### Katman ayarları {#layer-settings}

* `Katman verilerini kullan` - Etkinken ve bir katman seçiliyken, en fazla yüksekliği belirlemek için katman verilerini kullanır. Hiçbir katman seçili değilse bir uyarı bunu hatırlatır.
* `Şişir`- Etkinken, daha pürüzsüz sonuçlar elde etmek için Katman'ın çalıştığı yönü ayarlar.
* `Rahatlat (Normal)` - `Şişir` etkinken normallere uygulanan pürüzsüzleştirme miktarı.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_inflate.webp) Şişir {#inflate}
Verteksleri kendi normalleri boyunca hareket ettirir. `Alt`, verteksleri ters normalleri boyunca hareket ettirir.

#### Şişir ayarları {#inflate-setings}
* `Rahatlat (Normal)` - Normallere uygulanan pürüzsüzleştirme miktarı.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Dürt {#nudge}
Noktaları darbe yönünde hareket ettirir veya 'sürer'.

Alt mod `Kıvrım`'dır ve darbe boyunca malzemeden bir kıvrım iter: fırçanın önünde bir kabarıklık, arkasında bir çukur.

#### Dürt ayarları {#nudge-settings}
* `Pürüzsüzleştir` - Dürterken fırçanın altındaki bölgenin ne kadar pürüzsüzleştirileceği; bu, sürülen yüzeyi temiz tutar.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Damga {#stamp}

Heykelin bir bölgesini seçili Alfa şeklinde yükseltmek için tıklayıp sürükleyin.

Bu, darbe türü `Yakala • dinamik yarıçap` olarak ayarlanmış [Fırça aracından](#brush) ibarettir. 

`Alt`, damgayı yüzeyden dışarı çekmek yerine içeri iter.

::: tip
Damga genellikle yüksek çözünürlüklü geometriyle en iyi sonucu verir. İnternette 'wrinkles alpha', 'pores alpha', 'scales alpha' gibi aramalar yaparsanız, bu alfa dokuları ve Damga, bir karakter heykeline organik detay eklemenin harika bir yolu olabilir.

İki darbe modu farklı işler için kullanışlıdır. 

* `Yakala • dinamik yarıçap` sabit bir *yüksekliğe* sahiptir; sürüklemek damganın genişliğini ve dönüşünü ayarlar. Tekrarlayan desenleri gizlemek için aynı derinlikte/yükseklikte ama farklı dönüş ve ölçeklerde olması gereken cilt dokuları için iyidir.
* `Yakala • dinamik yoğunluk` sabit bir *genişliğe* sahiptir; sürüklemek damganın dönüşünü ve yüksekliğini ayarlar. Hepsinin aynı boyutta ama farklı dönüş ve yükseklikte olması gereken perçinler için iyidir. 

:::

![](/videos/tool_stamp.mp4)

### ![](/icons/tool_vdm.webp) VDM {#vdm}

Bir vektör yer değiştirme haritası (VDM) damgalar. Yüzeyi yalnızca yukarı veya aşağı itebilen bir alfanın aksine, VDM tam bir 3d şekil saklar; bu sayede kulak, boynuz veya kıvrık yaprak gibi çıkıntılı (alttan boşluklu) şekilleri damgalayabilir. [Damga](#stamp) gibi çalışır ve aynı `Yakala • dinamik yarıçap` ve `Yakala • dinamik yoğunluk` darbe modlarına sahiptir.

`Alt` (`Ters Çevir`), damganın derinliğini tersine çevirerek onu bir kalıp gibi yüzeye bastırır.

VDM'nin kendisi [Alfa](stroke.md#alpha) menüsünden seçilir; bu menüde, damganın yalnızca yüksekliğini ölçekleyip yanlara doğru yer değiştirmesini değiştirmeyen bir `Yükseklik` kaydırıcısı da bulunur.

Sol araç çubuğundaki `Oluştur` düğmesi kendi damgalarınızı yapmanızı sağlar:

* `Yeni VDM...` - VDM yontmak için hazırlanmış bir düzlem ekler. Şeklinizi bunun üzerinde yontun, ardından `Topoloji -> Pişir -> VDM` ile pişirin: Nomad yeni damgayı VDM kitaplığına ekler ve seçer.
* `VDM yakala` - (Deneysel) Bir modelin yüzeyinde sürükleyerek o bölgeyi yakalayın ve bir VDM damgasına dönüştürün. `Tolerans`, yakalanan bölgenin kenarını yumuşakça düzleştirir.

::: tip
Bir VDM düzlemini yontarken DinTopo kullanmaktan kaçının; düzlemin UV'lerini bozar ve damgayı çarpıtır. Yontuyu düzlemin kenarından da uzak tutun, yoksa damga sert bir kenar gösterir.
:::


### ![](/icons/tool_clearLayer.webp) Katmanı Sil {#delete-layer}
Bu araç katmanları yerel olarak sıfırlayabilir; etkin bir katmanınız olmalıdır, aksi hâlde hiçbir şey olmaz. Katmanın yontu verilerini, boyama etkinse boyasını da siler.

Alt mod `Ters Çevir`'dir ve katmanı silmek yerine biraz güçlendirir.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tüp {#tube}
Bir eğri çizerek tüp oluşturur. 
![](/images/tool_tube_new.webp)

Tüp oluşturulduktan sonra yolu, standart [Şekil düzenleme](#shape-editing) ve eğri düzenleme araçlarına benzer kontrollerle 3d alanda düzenlenebilir. 

![](/videos/tool_tube.mp4)

#### Tüp sol araç çubuğu {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Sol araç çubuğunda şu seçenekler bulunur:

* `Senkronize` - Geçerli tüp örneklenmişse ve tüpün örnekler arasında farklılık gösteren alt düğümleri varsa, bu onları yeniden senkronize eder.
* `Yasla` - Etkinken eğri ve yol modları çizdikçe diğer nesnelere yaslanır. Devre dışıyken ilk nokta yaslanır, tüpün geri kalanı o derinlikte çizilir.
* `Kaydırma` - Yaslamanın derinliğini belirler; %0'da tüp kesitinin ortası yüzeye yaslanır, pozitif değerler onu yüzeyden kaldırır, negatif değerler alçaltır. %100, tüpün yarıçapına eşittir.
* `Görüntüle` - Çizim modu yok, böylece kamerayı serbestçe hareket ettirebilirsiniz.
* `Eğri` - Serbest elle bir tüp çizin. Küçük bir açılır menüsü vardır:
    * `Düzenle` - Darbeyi bitirdiğinizde ne olacağı, bkz. [Seçim kontrolleri](#selection-controls): tüpü hemen oluşturur, eğriyi yanında yeşil bir onay dairesiyle düzenlenebilir bırakır ya da düzenlemeye devam etmek için darbenin sonunda `Düzenle: basılı tut`.
    * `Kapalı` - Tüpü bir döngüye dönüştürür.
    * `Çizmeye devam et` - Bir tüpü onayladıktan sonra bir sonrakini çizmek için araçta kalır.
    * `Hassasiyet` - Çizilen yolu tüpe dönüştürmek için kaç eğri noktası kullanılacağı. %0 en az sayıda nokta kullanır ama yoldaki küçük eğrilik değişikliklerini kaçırır. %100 çok hassastır ve çok sayıda nokta kullanır.
* `Yol` - Eğri noktalarını tıklayarak tanımlayıp bir tüp oluşturun. Yolu onaylamak için yeşil daireye dokunun. Küçük bir açılır menüsü vardır:
    * `B-spline` - Eğri noktalarının genellikle doğrudan eğrinin üzerinde durmadığı, ancak varsayılan yöntemden daha pürüzsüz sonuçlar verebilen alternatif bir eğri çizim yöntemi.
    * `Kapalı` - Tüpü bir döngüye dönüştürür
    * `Ekran` - Etkinken yol ekrana 'sabitlenir'; görünümü ve nesneyi hareket ettirebilirsiniz, yol yerinde kalır. Devre dışıyken yol 3d sahnenin bir parçasıdır ve kamera ile nesnelerle birlikte hareket eder.
* `Kesit` - Eğri, iki noktasından geçecek şekilde, baktığınız yön boyunca kesilerek şeklin etrafında bir halkaya dönüşür.

##### Tüp üst araç çubuğu {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Bir tüp seçiliyken, görünümün üst kısmında ek kontroller içeren bir araç çubuğu belirir. Araç çubuğunu daraltmak/genişletmek için başlığına, araç çubuğunu görünümün üstüne veya altına taşımak için sağ üstteki oka tıklayın.

* `Tamamla` - Tüpü yontulabilmesi için normal poligonlara pişirir.
* `Düzenle` - Eğri noktalarını üzerinde oynanabilmeleri için gösterir
* `Aynala` - Bu eğrinin üst öğesi olarak bir ayna tekrarlayıcısı ekler
* `Yasla` - Eğri noktalarını yakındaki yüzeylere yaslar
* `Kapalı` - Bir döngü oluşturmak için eğrinin başını ve sonunu birleştirir
* `B-spline` - Catmull-rom ve B-spline enterpolasyonu arasında geçiş yapar.
* `Kapak` - Tüpün iki ucunda, yalnızca başında veya sonunda kapak ya da hiç kapak olmaması arasında geçiş yapar.
* `Delik` - Tüpe kalınlık ekleyerek onu bir boruya dönüştürür. İki uçta delik, yalnızca sonda delik veya hiç delik olmaması arasında geçiş yapar. 
* `Yarıçap` - Tekdüze bir yarıçap, başta ve sonda birer yarıçap veya her eğri noktası için ayrı bir yarıçap arasında geçiş yapar. Bunlar eğri üzerindeki turuncu tutamaçlarla düzenlenir.
* `Sarım` - Sarım yok, tekdüze bir sarım, başta ve sonda birer sarım veya her eğri noktası için ayrı bir sarım arasında geçiş yapar. Bunlar eğri üzerindeki pembe tutamaçlarla düzenlenir.
* `Profil` - Profil yok (yani daire profili), tekdüze bir profil, başta ve sonda birer profil veya her nokta için ayrı bir profil arasında geçiş yapar.
* `Profil düzenleme` - Bir profil düzenleyici gösterir. [Şekil düzenleme](#shape-editing) araçlarına benzer şekilde çalışır, profil önayarlarını kaydedip yükleyebilir ve profili 3d alanda düzenlemenizi sağlayan bir anahtarı vardır.
* `Sarmal` - Tüpe sarmal bir sarım eklemek için bir menüyü açıp kapatır. Bu menüde `Sarım açısı`, `Kaydırma`, `Ölçek` ve `Açı kaydırma` seçenekleri bulunur.
* `X bölümleri` - Tüpün çevresindeki bölüm sayısı; örneğin 4 bölüm kare bir tüp oluşturur. 
* `Sabit yoğunluk` - Etkinken poligonları kare tutar. Devre dışıyken tüpün uzunluğu boyunca `Y bölümleri` ayarlamanıza izin verir.
* `...` - Tüp ayarları menüsü.

#### Eğri noktası silme anahtarı {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Araç çubuğunun altında bir eğri noktası silme anahtarı bulunur. Bir eğri noktasını başka bir noktanın yakınına sürüklediğinizde kırmızıya döner; bu, bırakırsanız noktanın silineceğini gösterir. Küçük düzenlemeler yapıyorsanız ve nokta silmek istemiyorsanız, bu düğme nokta silme davranışını devre dışı bırakır.



#### Tüp ayarları {#tube-settings}
* `Primitif` - UV'leri etkinleştirmenizi/devre dışı bırakmanızı veya tüpü tamamlamanızı sağlayan düğmeler.
* `İşlem sonrası altbölümleme` - Tamamlamadan önce çoklu çözünürlük seviyesini ayarlamak için bir kısayol.
* `Lineer altbölümleme` - Tamamlamadan önce lineer altbölümleme seviyesini ayarlamak için kısayol. 
* `Bölüm X` - Araç çubuğundaki X bölümleri ile aynı.
* `Bölüm Y` - Araç çubuğundaki Y bölümleri ile aynı.
* `Eğri (Tekrarlayıcı)` - Tüpü bir [Eğri Tekrarlayıcısına](scene.md#curve) dönüştürür

::: tip
4 bölüm ve 3 işlem sonrası altbölümleme, ucu yuvarlak pürüzsüz tüpler oluşturur; solucanlar, yılanlar, vücut parçaları için idealdir.
:::


### ![](/icons/tool_lathe.webp) Torna {#lathe}
Bir eğri çizerek dönel bir yüzey oluşturur.

Bu araç vazo, şarap kadehi gibi şekiller için harikadır.

![](/videos/tool_lathe.mp4)

#### Torna sol araç çubuğu {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Sol araç çubuğunda şu seçenekler bulunur:

* `Senkronize` - Geçerli torna örneklenmişse ve tornanın örnekler arasında farklılık gösteren alt düğümleri varsa, bu onları yeniden senkronize eder.
* `Sabit` - Etkinken tornanın merkezi sabittir ve ekranda gösterilir. Bu merkez çizgisinin ayarlanabilen düzenleme noktaları vardır. Devre dışıyken tornanın merkezi, çizilen eğrinin başına ve sonuna uyacak şekilde dinamik olarak güncellenir.
* `Görüntüle` - Çizim modu yok, böylece kamerayı serbestçe hareket ettirebilirsiniz.
* `Eğri` - Torna profilini tek darbede çizin. Küçük bir açılır menüsü vardır:
    * `Düzenle` - Kalemi kaldırdığınızda ne olacağı, bkz. [Seçim kontrolleri](#selection-controls): tornayı hemen oluşturur, eğriyi yanında tornayı oluşturan yeşil bir daireyle düzenlenebilir bırakır ya da düzenlemeye devam etmek için darbenin sonunda `Düzenle: basılı tut`.
    * `Kapalı` - Bir döngü oluşturmak için eğrinin başını ve sonunu birleştirir
    * `Çizmeye devam et` - Bir tornayı onayladıktan sonra bir sonrakini çizmek için araçta kalır.
    * `Hassasiyet` - Çizilen yolu tüpe dönüştürmek için kaç eğri noktası kullanılacağı. %0 en az sayıda nokta kullanır ama yoldaki küçük eğrilik değişikliklerini kaçırır. %100 çok hassastır ve çok sayıda nokta kullanır.
* `Yol` - Eğri noktalarını tıklayarak tanımlayıp bir torna oluşturun. Yolu onaylamak için yeşil daireye dokunun. Küçük bir açılır menüsü vardır:
    * `B-spline` - Eğri noktalarının genellikle doğrudan eğrinin üzerinde durmadığı, ancak varsayılan yöntemden daha pürüzsüz sonuçlar verebilen alternatif bir eğri çizim yöntemi.
    * `Kapalı` - Tüpü bir döngüye dönüştürür
    * `Ekran` - Etkinken yol ekrana 'sabitlenir'; görünümü ve nesneyi hareket ettirebilirsiniz, yol yerinde kalır. Devre dışıyken yol 3d sahnenin bir parçasıdır ve kamera ile nesnelerle birlikte hareket eder.

#### Torna üst araç çubuğu {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Bir torna seçiliyken, görünümün üst kısmında ek kontroller içeren bir araç çubuğu belirir. Araç çubuğunu daraltmak/genişletmek için başlığına, araç çubuğunu görünümün üstüne veya altına taşımak için sağ üstteki oka tıklayın.

* `Tamamla` - Tornayı yontulabilmesi için normal poligonlara pişirir.
* `Düzenle` - Eğri noktalarını üzerinde oynanabilmeleri için gösterir
* `Aynala` - Bu tornanın üst öğesi olarak bir ayna tekrarlayıcısı ekler
* `Yasla` - Eğri noktalarını yakındaki yüzeylere yaslar
* `Kararlı` - Etkinken eğri profili tornanın merkez çizgisine bağlanır (onun alt öğesi olur). Devre dışıyken merkez çizgisi eğriyi hareket ettirmeden düzenlenebilir; bu da daha karmaşık şekillere olanak tanır.
* `Odak` - Görünümü, eğri profilini kameraya tamamen düz bakacak şekilde görecek biçimde döndürür.
* `Kapalı` - Bir döngü oluşturmak için eğrinin başını ve sonunu birleştirir
* `Kapak` - Kapalı devre dışıysa, iki uçta, yalnızca başta veya sonda kapak ya da hiç kapak olmaması arasında geçiş yapar.
* `Delik` - Tornaya kalınlık ekleyerek onu bir boruya dönüştürür. İki uçta delik, yalnızca sonda delik veya hiç delik olmaması arasında geçiş yapar. 
* `B-spline` - Catmull-rom ve B-spline enterpolasyonu arasında geçiş yapar.
* `X bölümleri` - Tornanın çevresindeki bölüm sayısı; örneğin 4 bölüm kare profilli bir torna oluşturur. 
* `Sabit yoğunluk` - Etkinken poligonları kare tutar. Devre dışıyken tüpün uzunluğu boyunca `Y bölümleri` ayarlamanıza izin verir.
* `...` - Torna ayarları menüsü.

#### Torna ayarları {#lathe-settings}
* `Primitif` - UV'leri etkinleştirmenizi/devre dışı bırakmanızı veya tüpü tamamlamanızı sağlayan düğmeler.
* `İşlem sonrası altbölümleme` - Tamamlamadan önce çoklu çözünürlük seviyesini ayarlamak için bir kısayol.
* `Lineer altbölümleme` - Tamamlamadan önce lineer altbölümleme seviyesini ayarlamak için kısayol. 
* `Bölüm X` - Araç çubuğundaki X bölümleri ile aynı.
* `Bölüm Y` - Araç çubuğundaki Y bölümleri ile aynı.
* `Eğri (Tekrarlayıcı)` - Eğri profilini bir [Eğri Tekrarlayıcısına](scene.md#curve) dönüştürür

### ![](/icons/tool_insert.webp) Ekle {#insert}
Bir nesneyi başka bir nesnenin yüzeyine yerleştirir. Kullanımı damga aracına benzer, ancak tam 3d şekiller içindir.

Sol araç çubuğundan bir primitif seçerseniz, herhangi bir yüzeyde tıklayıp sürüklemek, tıkladığınız yere bir primitif yerleştirir; sürükleme boyutunu belirler. Sürüklemeyi bitirdiğinizde Ekle, [Dönüştür](#transform) moduna geçer.

Örnek modunda sürüklemek yeni bir örnek oluşturur ve yüzey üzerinde kaydırır. Boyut ilk şekilden kopyalanır; bu sayede bir nesnenin aynı boyuttaki birçok örneğini başka yüzeylerin üzerine yerleştirebilirsiniz.

Yalnızca primitif eklemek zorunda değilsiniz! Anahat görünümünde *herhangi bir* şekli seçin; Ekle, Örnek veya Klonlama modundaysa seçili nesnenin kopyalarını başka herhangi bir yüzeyin üzerine sürükleyebilirsiniz.

Bir nesnenin özel bir ekseni varsa, bu eksen bir bağlantı noktası olarak kullanılır. Aşağıdaki videoya bakın.

Sol araç çubuğunda ayrıca hiçbir şey eklemeden kamerayı hareket ettirmek için `Görüntüle` ve `Senkronize` bulunur: hedef nesne örneklenmişse yeni nesne diğer tüm örneklere de eklenir.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Dönüştür {#transform}
Bir modeli 1 ve 2 parmakla doğrudan, genellikle başka bir nesnenin yüzeyi üzerinde Taşıyın/Döndürün/Ölçekleyin.

Sol araç çubuğunda şu düğmeler bulunur:

* `Klonlama` / `Örnek` - Nesnenin bir kopyasını veya örneğini oluşturur, bkz. [Gizmo](#left-menu-toolbar) araç çubuğu.
* `Taşı` - Tek parmakla sürüklemek nesneyi taşır. Yaslama etkinken nesneyi parmağınızın altındaki yüzey boyunca kaydırır.
* `Döndür` - Tek parmakla sürüklemek nesneyi döndürür. Yaslama etkinken parmağınızın altındaki yüzeyin normali etrafında döndürür.
* `Ölçek` - Tek parmakla sürüklemek nesneyi ölçekler.

Görünümün üst kısmındaki bir araç çubuğunda şunlar bulunur:

* `Hedef` - Aracın nesneyi mi, grubunu mu yoksa verteksleri mi hareket ettireceği; [Gizmo](#left-menu-toolbar) ile aynı.
* `Yasla` - Modeli diğer yüzeylere yaslar.
* `Yüzey` / `Verteks` - `Yasla` ile, yüzeye veya en yakın vertekse yaslar.

Dönüştür, 2 parmak kullanarak bu modlardan ikisini hızla kullanabilir:

* Bir nesneyi yerleştirmek için sürükleyin. İlk parmağınızı hareket ettirmeyi bırakın, ama ekrandan kaldırmayın.
* İlk parmağınız basılıyken ikinci parmağınızla ekrana dokunun. İkinci parmak sürüklendikçe nesne ölçeklenir.
* İkinci parmağı kaldırın ve ilk parmağı sürüklemeye devam edin; nesne yeniden taşıma modunda olur.

İkinci mod, ikinci parmakla dokunma hareketiyle de değiştirilebilir:

* Nesneyi yerleştirmek için sürükleyin, hareket etmeyi bırakın ama parmağınızı ekrandan kaldırmayın.
* İlk parmağınız basılıyken ikinci parmağınızla dokunun
* Araç döndürme moduna geçer. Dönüşü ayarlamak için ilk parmağınızı sürükleyin.
* İkinci parmakla önceki gibi dokunun; araç yeniden taşıma moduna geçer.

Bu, nesneleri başka bir nesnenin üzerine klonlamak için hızlı bir iş akışı sunar, örneğin bir arazinin üzerine kayalar. Klonlama düğmesinin de kolay erişim için sol araç çubuğunda olduğuna dikkat edin:

* Bir kayayı yerine taşımak için dönüştürme aracını kullanın.
* Bırakın, klonlama düğmesine basın
* Bu kayayı taşıyın, gerektiği gibi döndürün/ölçekleyin
* Bırakın, klonlama düğmesine basın
* Bu kayayı taşıyın, tekrarlayın.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Bu araç nesneleri taşımanızı, döndürmenizi ve ölçeklemenizi, ayrıca nesnelerin eksenlerini değiştirmenizi sağlar.

Görünümdeki tutamacın şu özellikleri vardır:

* `Taşı` - X/Y/Z üzerinde taşımak için çizgi+ok üzerinde sürükleyin. Ekran alanında serbestçe taşımak için gizmonun ortasındaki şeftali rengi noktayı sürükleyin. X/Y/Z düzlemlerinde taşımak için kırmızı, yeşil, mavi karelere tıklayın.
* `Döndür` - X/Y/Z üzerinde döndürmek için kırmızı/yeşil/mavi daireleri sürükleyin. Serbestçe döndürmek için dairelerin içindeki küreyi sürükleyin.
* `Ölçek`- X/Y/Z üzerinde ölçeklemek için dıştaki kırmızı/yeşil/mavi noktaları sürükleyin. X/Y/Z düzlemlerinde ölçeklemek için dıştaki kırmızı/yeşil/mavi konileri sürükleyin. Tekdüze ölçeklemek için dıştaki şeftali rengi daireyi sürükleyin.

![](/images/tool_gizmo.webp)

#### Düğümler ve verteksler {#nodes-and-vertices}

Nomad'daki her nesne bir düğüm ve vertekslerden oluşur:

* `Düğüm` - Nesnenin 'tutamacı'; nesnenin ötelemesini, dönüşünü ve ölçeğini, yani dönüşüm matrisini saklar.
* `Verteksler` - Bir nesnenin yüzeyini tanımlayan noktalar; konum ve boya bilgisini saklarlar.

8 verteksten oluşan basit bir kutunuz varsa, onu dönüşüm matrisini değiştirerek veya verteks konumlarını değiştirerek öteleyebilirsiniz. Yontarken genellikle verteksleri değiştirmek istersiniz; nesneleri gizmo ile taşırken ise genellikle düğümü değiştirmek istersiniz. Nomad ikisini de yapmanıza izin verir. 

#### Gizmo araç çubukları {#left-menu-toolbar}

Sol araç çubuğunda şunlar bulunur:

* `Klonlama` - Geçerli nesnenin, gizmo ile sürüklenip uzaklaştırılabilen bağımsız bir kopyasını oluşturur.
* `Örnek` - Geçerli nesnenin bir örnek kopyasını oluşturur. Nesneler birbirine bağlıdır; bu yüzden bir nesnedeki yontma değişiklikleri tüm örneklenmiş nesnelerde görünür.
* `Eksen` - (Kilit simgesi, `Alt` düğmesinin yerinde) Etkinken gizmo, nesne hareket etmeden taşınabilir ve döndürülebilir. `Alt` gibi, hızlı bir geçiş için basılı tutun veya açık bırakmak için dokunun.

Görünümün üst kısmındaki bir araç çubuğunda diğer kontroller bulunur:

* `Hedef` - Gizmonun bir nesnenin düğümünü mü yoksa vertekslerini mi etkileyeceğini belirler:
    * `Otomatik` - Varsayılan; `Grup` gibi çalışır, ancak ağda maske varsa veya simetri etkinse `Verteks` gibi çalışır.
    * `Verteks` - Dönüşümü maskeyi ve simetriyi hesaba katarak verteksler üzerinde uygular. Tamamlanmamış primitiflerde çalışmaz ve örnekler de etkilenir.
    * `Nesne` - Simetri ve maskeyi yok sayarak yalnızca geçerli nesneyi taşır. Alt nesneler yerinde kalır.
    * `Grup` - Simetri ve maskeyi yok sayarak nesneyi ve hiyerarşisinin geri kalanını taşır.
    * `Örnek` - (Nesne ve Grup) Aynısı, ancak nesnenin her örneği de birlikte hareket eder.
* `Eksen` - Ekseni hızla yerleştirmek için bir açılır pencere; [aşağıda](#pivot) açıklanmıştır.
* `Tümü` / `Taşı` / `Döndür` / `Ölçek` - Tüm gizmo tutamaçlarını veya yalnızca taşıma, döndürme ya da ölçekleme tutamaçlarını gösterir.
* `Tuttur` - Varsayılan olarak gizmo seçili nesnenin eksenine gider. Tuttur etkinken gizmo bulunduğu yerde kalır.
* `Hizala` - Eksenin geçerli nesneyle veya dünyayla hizalanması arasında geçiş yapar.
* `Yasla` (döndürme) - Döndürme değerlerinin belirli artışlara yaslanmasını etkinleştirir; yaslama etkinken yaslama değeri gösterilir ve düzenlenebilir. `Mıknatıs` seçeneği, döndürmenin bir adımı geçerken o adıma yapışmasını, sonra yeniden serbestçe hareket etmesini sağlar; adımdan adıma atlamak için kapatın.
* `Yasla` (öteleme) - Öteleme değerlerinin belirli artışlara yaslanmasını etkinleştirir; yaslama etkinken yaslama değeri gösterilir ve düzenlenebilir.

#### ![](/icons/reset.webp) Eksen {#pivot}
Üst araç çubuğundaki `Eksen` açılır penceresi, eksende hızlı değişiklikler yapmanızı sağlar. Eksenin konumu ve yönelimi gizmoyu belirler.

**Sıfırla** 
* `Otomatik` - Nesnenin merkezi, nesnenin dönüşümüyle hizalı.
* `Ortalanmış` - Yönelimini koruyarak ekseni nesnenin merkezine taşır.
* `Alt` - Ekseni nesnenin alt merkezine taşır. Bunun yerine dünya sınırlayıcı kutusunu kullanmak için tekrar dokunun.
* `Üst` - Ekseni nesnenin üst merkezine taşır. Bunun yerine dünya sınırlayıcı kutusunu kullanmak için tekrar dokunun.
* `Nesne` - Ekseni nesnenin orijinine, nesnenin dönüşümüyle hizalı olarak taşır.
* `Maske` - Ekseni maskesiz bölgenin merkezine taşır. Maskeli bölgeye geçmek için tekrar dokunun.
* `Hizala` - Konumu koruyarak dönüşleri dünyayla hizalı olacak şekilde sıfırlar.
* `Görünüm` - Konumu koruyarak ekseni geçerli görünümle hizalar. Sonrasında kamerayı takip etmez.

**Tek dokunuşta (Eksen modu)**

Yalnızca `Eksen` açıkken etkindir; ağ yüzeyine bir kez dokunduğunuzda ne olacağını belirler:
* `Yok` - Nesneye dokunulduğunda hiçbir şey yapmaz
* `Normal` - Ekseni, yüzeye dokunulan yere hizalanacak şekilde taşır ve döndürür
* `İlk` - Ekseni yüzeye dokunulan yere taşır (ama döndürmez)
* `Orta` - Ekseni, yüzeye dokunulan yerin altında, nesnenin ortasına taşır.

#### Gizmo ayarları {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

* `Kompakt` - Gizmo düzenini değiştirerek ek tutamaçları döndürme küresinin dışına veya içine yerleştirir
* `Araç boyutu` - Gizmonun boyutu
* `Kalınlık` - Gizmo üzerindeki çizgilerin kalınlığı
* `Opaklık` - Gizmonun opaklığı
* `Etkileşimde gizle` - Gizmonun sürüklenirken geçici olarak gizlenip gizlenmeyeceğini belirler

-----

* `Tanjant ilerleme açı eşiği` - X/Y/Z üzerinde döndürmek için daire tutamaçlarında sürüklerken döndürme arayüzünün nasıl davranacağını kontrol eder. Bu değer 0 ise döndürme bir kadran gibi çalışır, gizmoyu daireler çizerek sürüklersiniz. Bu değer 90 ise döndürme bir yoyonun ipini çekmek gibi çalışır; ilk tıkladığınız yere doğru veya ondan uzağa düz bir çizgide sürüklersiniz. 0 ile 90 arasındaki değerler ikisinin bir karışımını yapar; değerin altında doğrusal hareket, üstünde dairesel hareket olur.
* `Sayısal girdi` - Etkinken gizmoya tek dokunuş, dokunulan eksen için kesin bir değer girebileceğiniz bir pencere açar.

::: warning
[Gizmo](#gizmo) ve [Dönüştür](#transform) araçları, yontma simetrisinden ayrı, kendi simetri onay kutularını kullanır!

Bu simetri varsayılan olarak kapalıdır.
:::

##### Matris {#matrix}
Nesnenin kesin dönüşüm değerleri artık Gizmo ayarlarında değil: sağ üstteki menüde bulunan `Dönüştür` menüsüne taşındılar. Bu menünün `Matris` bölümünde şunlar bulunur:

* ![](/icons/target.webp) `Kökeni hareket ettir` - Nesneyi, ekseni sahnenin merkezinde, yani orijinde olacak şekilde taşır.
* ![](/icons/bake.webp)  `Pişir` - Nesneyi bulunduğu yerde dondurur; öteleme/döndürme değerlerini 0'a, ölçeği 1'e ayarlar.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Eksen` - Ekseni pişirir: matris değerlerinin, gizmo tutamacının dünyadaki konumuna karşılık gelmesini sağlar.
* ![](/icons/reset.webp) `Sıfırla` - Öteleme değerlerini 0'a, döndürme değerlerini 0'a, ölçeği 1'e ayarlayan bir kısayol; nesneyi taşır ve döndürür.

::: tip Pişir ile eksene pişir arasındaki fark
Bir kutu oluşturun, Gizmo aracını seçin, `Dönüştür` menüsünü açıp sabitleyin. Varsayılan olarak öteleme ve döndürme 0, ölçek 1'dir.

Eksen modunu etkinleştirin, tutamacı bir yana taşıyın, eksen modunu devre dışı bırakın. Eksen değişti, ancak öteleme değerlerinin hâlâ 0 olduğuna dikkat edin. 

Eksenin *gerçekte* nerede olduğunu görmek istiyorsanız, `Eksen` pişirme düğmesine tıklayın. Artık öteleme değerleri güncellenir. Bu işlem sırasında da, eksen modunda da kutunun hareket etmediğine dikkat edin.

Kutuyu bir yere taşıyıp döndürün, ardından `Kökeni hareket ettir` düğmesine dokunun. Nesneyi ekseni dünyanın merkezinde olacak şekilde taşır, ancak dönüşü değiştirmez.

`Sıfırla` düğmesine tıklayın; dönüş de 0'a ayarlanır.

Kutuyu yeniden taşıyıp döndürün, bu kez `Pişir` düğmesine tıklayın. Eksen olduğu yerde kalır, kutu olduğu yerde kalır, ancak öteleme ve döndürme değerleri 0'a ayarlanır.

Bunu birkaç kez deneyin! Eksen değerlerinin gizli olduğunu, Nomad'ın bunları sizin için yönettiğini, ancak ekseni uzayda gerçek konumlara ayarlamanız gerekirse eksen pişirmenin bunu sizin için yapacağını kavrayın.

:::

* `Öteleme` - X, Y, Z öteleme değerleri
* `Döndürme` - X, Y, Z döndürme değerleri
* `Ölçek` - Etkinse tekdüze ölçek, devre dışıysa X, Y, Z ölçeği.
* `Yatır` - X, Y, Z yatırma (kesme) değerleri; yalnızca nesne zaten yatırılmışsa gösterilir
* `Tek tip ölçeklendirme` - Tekdüze ölçekleme ile her eksende bağımsız ölçekleme arasında geçiş yapar

Solda gizmonun eksenini taşıyabilirsiniz; aşağıdaki videoda bunu iş başında görebilirsiniz.
Bu özellikle döndürme için kullanışlıdır, çünkü öteleme için hiçbir şeyi değiştirmez.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Yüz Grubu {#facegroup}

Yüz grupları, nesnenizi farklı renklerdeki yüzlere ayırarak düzenlemenizi sağlar. Bu grupları Nomad'da birçok şekilde kullanabilirsiniz:

* Maskeler için hızlı bir seçim yöntemi
* Nesnenizin bölümlerini gizlemek/göstermek
* Nesnenizi ayrı parçalara bölmek zorunda kalmadan düzenlemek
* UV bölgelerini tanımlamak
* Quad Remesher'a yol göstermek
* Pürüzsüzleştir gibi araçlar için ek kontrol.

#### Yüz Grubu sol araç çubuğu {#facegroup-left-toolbar}

* `Grup` - Düğme geçerli yüz grubunu gösterir. Mevcut yüz gruplarını renk lekeleri olarak görüntülemek ve birini seçmek için dokunun. Bir lekeye dokunarak adını veya rengini değiştirebilir ya da silebilirsiniz. `Kullanılmayanları kaldır` kullanılmayan lekeleri siler, `Sıfırla` hepsini kaldırır. Artı simgesi yeni lekeler oluşturmanızı sağlar.
* `Nokta` - Yüz gruplarını tanımlamak için nesnenin üzerine boyayın. '+ Yüz Grubu' etkinken her yeni darbe otomatik olarak yeni bir yüz grubu oluşturur; bölgeleri hızla tanımlamak için kullanışlıdır. Bir dokunuş seçili bölgeyi tamamen doldurur. Kaydırıcı noktanın yarıçapını belirler.
* `Rahatlat` - Yüz gruplarının sınırlarını pürüzsüzleştirir. Dörtgen yeniden örgüleme için temiz kenarlar tanımlamada veya sert yüzey modellemede paneller tanımlamada çok kullanışlıdır. Kaydırıcılar rahatlatma işleminin yarıçapını ve yoğunluğunu kontrol eder.
* Şekiller - Fırça yerine şekillerle yüz grupları oluşturun: `Yakala • dinamik yarıçap`, `Lasso`, `Poligon`, `Çizgi`, `Dikdörtgen` ve `Elips`. Daha fazla bilgi için bkz. [Seçim kontrolleri](#selection-controls).
* `Seç` - Alt mod. Etkinken darbenin başladığı lekeyi seçer ve darbenin geri kalanında o lekeyi uygular. Yüz grubu bölgelerini toparlamak için çok kullanışlıdır: bir yüz grubu fazla taşmışsa `Seç`'i etkinleştirin, yüz grubu lekesinin doğru olduğu yerden bir darbe başlatın ve doğru lekeyi yeniden atamak için sınıra kadar sürükleyin.

#### Yüz Grubu üst araç çubuğu {#facegroup-top-toolbar}

Görünümün üst kısmındaki bir araç çubuğunda ek kontroller bulunur:

* `Rahatlat (Tümü)` - Tüm yüz gruplarının sınırlarını bir kerede rahatlatmak için sürükleyin.
* `Ön` / `Görülebilir` / `Bağlı` - [Maske](#mask) araç çubuğundakiyle aynı darbe filtreleri.
* `Normallerden` - Yüzler arasındaki açıya göre yüz grupları oluşturur. Açılır pencerede `Açı` bulunur ve küçük grupları `Yüz sayısı` veya `Yüzey alanı` temelinde atlamanızı sağlar; onaylamadan önce bir `Önizleme` de sunar.
* `Parçalardan` - Her bağlantısız parça için bir yüz grubu oluşturur.
* `UV’lerden` - Her UV adası için bir yüz grubu oluşturur.
* `Maskeden` - Maskelenen bölgeden bir yüz grubu oluşturur.
* `Dokunuşta` - Bir yüz grubuna dokunmanın ne yapacağını seçin: onu geçerli yüz grubuyla doldurmak, gizlemek, maskelemek veya `Poz` vermek (dokunulan grup ve onun ötesinde kalanların maskesi kaldırılır ve gizmo eklem noktasına yerleşir; maske için bir `Bulanıklık` kaydırıcısı da vardır). Ağda bir maske varken kullanılabilen ikinci bir `Dokunuşta` anahtarı, dokunuşu maskenin aynı tarafındaki yüzlerle sınırlar.
* [Gizle](#hide) ve [Maske](#mask) araçları için `Kaldır` düğmeleri; araçtan çıkmadan her şeyi yeniden göstermek veya maskeyi temizlemek için.

#### Yüz Grubu ayarları {#facegroup-settings}

`Araç` menüsü yüz gruplarını yeni nesnelere çıkarır; seçenekleri [Maske ayarları](#mask-settings) bölümündeki `Çıkar` ile aynıdır. Üstteki `Yüz Grubu` düğmesi hangi grupların çıkarılacağını seçer ve ek bir `Boşluk` kaydırıcısı vardır: her sınırı yüzey boyunca içe doğru kaydırır, negatif bir değer ise üst üste binecek şekilde dışa doğru kaydırır. Komşu paneller için istediğiniz boşluğun yarısını kullanın.

### ![](/icons/tool_hide.webp) Gizle {#hide}
Nesnenin parçalarını gizler veya yalıtır. 

Ana modlar sol menüden kontrol edilir:

* `Nokta` - Nesnenin parçalarını gizlemek için nesnenin üzerine fırçayla boyayın.
* Şekiller - Fırça yerine şekillerle gizleyin: `Lasso`, `Poligon`, `Çizgi`, `Dikdörtgen` ve `Elips`. Daha fazla bilgi için bkz. [Seçim kontrolleri](#selection-controls).
* `Göster` - Alt mod; işlemi tersine çevirir, böylece seçili mod nesnenin parçalarını gizlemek yerine gösterir.

Görünümün üst kısmında ek kontroller içeren bir araç çubuğu belirir:

* `Tümünü temizle` - Nesneleri eski hâline getirir, tüm gizli parçalar yeniden görünür olur. Başka nesnelerde de gizli parçalar varsa, ek bir `Kaldır` düğmesi yalnızca seçili nesneleri eski hâline getirir.
* `Ters Çevir` - Gizli ve görünür parçaları yer değiştirir.
* `Sil` - Nesnenin gizli parçasını siler
* `Ayır` - Nesnenin gizli parçasını yeni bir şekle ayırır.
* `Ön` / `Görülebilir` / `Bağlı` - [Maske](#mask) araç çubuğundakiyle aynı darbe filtreleri.
* `Dokunuşta` (yüz grubu) - Bölümleri hızla gizlemek için yüz gruplarını kullanır; bir yüz grubuna dokunmak yüz grubunun tamamını gizler.
* `Dokunuşta` (maske) - Bir maske etkinse, dokunmak maskelenen bölümü gizler.

### ![](/icons/tool_measure.webp) Ölç {#measure}
2 nokta arasındaki mesafeyi ölçmek için sürükleyin. Yerleştirildikten sonra ölçümü ayarlamak için uç noktaları sürükleyebilirsiniz.

Sol araç çubuğu mesafenin nasıl ölçüleceğini seçer:

* `Çizgi` - İki nokta arasında düz bir çizgi.
* `Yüzey` - Kameradan görüldüğü hâliyle iki noktadan geçen kesiti izleyerek yüzey boyunca mesafe.
* `Kesit` - İki noktadan geçen kesitin çevresi; bir kolun etrafına sarılan mezura gibi.
* `Verteks` - Uç noktaları en yakın vertekse yaslar.
* `Altın oran` - Ölçümün altın oran noktasında sarı bir nokta gösterir.
* `?` düğmesi, seçili nesnelerin hacmini, yüzey alanını ve boyutunu gösterir.

### ![](/icons/tool_arrange.webp) Düzenle {#arrange}
2d tasarım uygulamalarındaki hizalama araçları gibi, birden fazla nesneyi aynı anda hizalayın ve yerleştirin. Önce nesneleri seçin; tek bir nesneyle Düzenle, onun ayrı parçaları üzerinde çalışır. Seçimin etrafına bir kutu çizilir; ölçeklemek için tutamaçlarını sürükleyin.

Görünümün üst kısmındaki bir araç çubuğunda kontroller bulunur:

* `Dünya` / `Ekran` - Dünya eksenleri veya ekran (sol, sağ, üst, alt) boyunca düzenler.
* `Hizala` - Nesneleri her eksende en küçük değerlerine, merkezlerine veya en büyük değerlerine göre hizalar.
* `Dağıt` - Nesneleri en dıştaki iki nesne arasında en küçük değerlerine, merkezlerine veya en büyük değerlerine göre eşit aralıklarla yerleştirir. En az 3 nesne gerekir.
* `Çizgi` - Nesneleri bir eksen boyunca sıraya dizer.
* `Izgara` - Nesneleri `X`, `Y` ve `Z` üzerinde belirli sayıda nesneyle bir ızgaraya dizer.
* `Daire` - (Yalnızca Dünya) Nesneleri `X`, `Y` veya `Z` ekseni etrafında bir daireye dizer.
* `Küre` - (Yalnızca Dünya) Nesneleri bir kürenin üzerine dizer.

`Çizgi`, `Izgara`, `Daire` ve `Küre`'nin hepsinde nesneler arasındaki boşluk için bir `Aralık` kaydırıcısı bulunur.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Bu araç seçili nesneyi temiz bir dörtgen topoloji düzenine dönüştürür; yoğunluk, kenar akışı ve simetri için kontroller sunar. 

::: tip
Quad Remesher, iOS ve masaüstü için [Exoside](https://exoside.com/) tarafından geliştirilmiştir. 

iOS'ta Nomad içinden bir uygulama içi satın alımdır; tek seferlik 16 USD ödemeyle alınır.

Masaüstü için [Exoside](https://exoside.com/quadremesher/quadremesher-buy/) üzerinden bir lisans satın alın. Yalnızca Nomad masaüstü için veya desteklenen tüm masaüstü uygulamaları için geçerli çapraz bir lisans satın alabilirsiniz.

Quad Remesher'a başka bir masaüstü uygulaması için zaten sahipseniz, [tüm platformlara daha düşük bir ücretle yükseltme satın alabilirsiniz.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher Android'de mevcut değildir. Android'de [Dörtgen Yeniden Örgüleme](topology.md#quad-remesh) topoloji sekmesindeki ücretsiz, açık kaynaklı yeniden örgüleyiciler (AutoRemesher, Instant Mesh, QuadriFlow) kullanılabilir, ancak özelliklerinin daha sınırlı olduğunu bilmelisiniz.
:::

Quad Remesher'ın kilidi açılana kadar üst araç çubuğu, yeniden örgüleme düğmeleri yerine bir alışveriş sepeti düğmesiyle başlar. iOS'ta bu düğme uygulama içi satın alımı açar. Masaüstünde `Kilit Aç (satın al, geri yükle, deneme)` seçeneğini gösterir; bu, Exoside lisansınızı denetler (veya deneme sürümünü başlatır). Etkinleştirildikten sonra sol ve üst araç çubukları kullanılabilir hâle gelir.

* `Nokta` - Bu fırça hedef yoğunluğu belirler. %100 yoğunluk kırmızı boyar; bu bölgelerde hedef dörtgen yoğunluğunun iki katı kullanılır. %0 yoğunluk camgöbeği boyar; bu bölgelerde hedef dörtgen yoğunluğunun yarısı kullanılır. %50 yoğunluk gri boyar; varsayılan hedef dörtgen yoğunluğu kullanılır.
* `Pürüzsüzleştir` - Kırmızı/gri/camgöbeği yoğunluk geçişlerini yumuşatır.
* `Leke` - Yoğunluk boyamasını lekeler, yayar.
* `Eğri` - Heykelin yüzeyine eğriler çizin; Quad Remesher bunları kenar akışı için kılavuz olarak kullanır. Silmek için bir eğriye dokunun.
* `Yol` - Heykelin yüzeyine yollar çizin; Quad Remesher bunları kenar akışı için kılavuz olarak kullanır. Silmek için bir yola dokunun. 
* `Dikdörtgen` - Heykelin yüzeyine dikdörtgenler çizin; Quad Remesher bunları kenar akışı için kılavuz olarak kullanır. Silmek için bir yola dokunun.
* `Elips` - Heykelin yüzeyine elipsler çizin; Quad Remesher bunları kenar akışı için kılavuz olarak kullanır. Silmek için bir yola dokunun.

#### Quad Remesher üst araç çubuğu {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

Görünümün üst kısmında ek kontroller içeren bir araç çubuğu belirir:


* `<Sayı>` - Yeniden örgüleme işlemini başlatmak için buna tıklayın; bu sayı hedef dörtgen sayısını gösterir.
* `Dörtgenler` - Sağa sola kaydırarak hedef dörtgen sayısını ayarlayın veya kesin bir sayı girmek için dokunun. Bunun sabit bir sayıdan çok bir kılavuz olduğunu unutmayın; Quad Remesher'daki çeşitli kontroller nedeniyle sonuç çoğu zaman bu hedefle tam olarak eşleşmez.
* `Yarı` - Hedef sayıyı geçerli poligon sayısının yarısına ayarlayan bir kısayol.
* `Aynı` - Hedef sayıyı geçerli poligon sayısına ayarlayan bir kısayol.
* `Rehberler` - Kılavuzları kullanmak veya yok saymak için açıp kapatın. Kılavuzlar varsa, ikinci bir `Rehberler` düğmesi sayılarını gösterir; hepsini silmek için ona dokunun.
* `Yoğunluk` - Yoğunluk boyamasını kullanmak veya yok saymak için açıp kapatın. Yoğunluk boyaması varsa, ikinci bir `Yoğunluk` düğmesi onu kaldırır.
* `Yüz Grubu` - Quad Remesher'ı yönlendirmek için yüz gruplarını kullanmak veya yok saymak üzere açıp kapatın.
* `Rahatlat` - Dörtgen yeniden örgüleme sırasında yüz grubu sınırlarını otomatik olarak rahatlatmak için açıp kapatın. Yüz grubu sınırlarınızı zaten rahatlattıysanız/pürüzsüzleştirdiyseniz bu seçeneği devre dışı bırakın.
* `Rahatlat kaydırıcısı` - Yüz grubu sınırlarını rahatlatmak için bir kısayol kaydırıcısı.
* `Sert Kenarlar` - Sert kenarları korumaya çalışmak için açıp kapatın.
* `Verteksi yeniden yansıt` - Yeni düzeni girdi ağına yeniden yansıtmak için açıp kapatın.
* `Sim` - Simetrik bir sonuç için açıp kapatın. Simetrinin her zaman dünya x ekseni etrafında hesaplandığını unutmayın; simetrik bir sonuç bekliyorsanız modelinizin orijinde olduğundan emin olun.
* `...` - Quad Remesher ayarları açılır penceresi. 

#### Quad Remesher ayarlar menüsü {#quad-remesher-settings-menu}

Üst araç çubuğunun sonundaki `...` düğmesi, kalan ayarları içeren bir açılır pencere açar:

* `Adaptif Kare Sayısı` - Yüksek eğriliğe sahip bölgelerde daha küçük, düşük eğrilikli bölgelerde daha büyük dörtgenler kullanılmasını etkinleştirir.
* `Adaptif Boyut` - Uyarlanabilirlik miktarını ayarlar. %100 en fazla uyarlanabilir boyuta izin verir, %0'da dörtgenler tekdüze olur.

::: tip

Az kusurla iyi bir dörtgen yeniden örgüleme elde etmek için bir tarif:

* İdeal dörtgen akışınızı tanımlamak için ağı yüz gruplarına ayırın.
* Pürüzsüz yüz grubu sınırları elde etmek için yüz gruplarını rahatlatın.
* Azaltın. Bu, yüz grubu kenarında ince veya bozuk yüzler kalmamasını sağlar. Azaltma ayarlarında yüz grubunun etkin olduğundan emin olun. Böylece üçgen kenarları yüz grubu kenarlarınızı tam olarak takip eder. 

Dörtgen yeniden örgüleme seçeneklerinde rahatlatmanın devre dışı olduğundan emin olun (ağı zaten rahatlattınız); iyi sonuçlar almanız gerekir.

:::

### ![](/icons/tool_select.webp) Seç {#select}
Sahnedeki nesneleri seçmek için şekil modlarını (`Lasso`, `Dikdörtgen`, `Elips`) kullanın. `Seçimi kaldır` nesneleri seçimden çıkarır.

### ![](/icons/tool_lattice.webp) Kafes {#lattice}
Bir nesneyi yüzeyini yontmak yerine, etrafındaki kontrol noktalarından oluşan bir kafesle deforme edin. Kafesin birkaç noktasını hareket ettirmek tüm nesneyi pürüzsüzce büker, burar veya esnetir; oranları ayarlamak veya topolojiye dokunmadan poz vermek için harikadır. Deformasyon siz onaylayana kadar canlı kalır.

Sol araç çubuğu kafesi nasıl düzenleyeceğinizi seçer:

* `Noktalar` - Kafesin noktalarını ve kenarlarını doğrudan sürükleyin. Bir noktayı seçmek için ona dokunun.
* `Görüntüle` - Kafesi düzenlemeden kamerayı hareket ettirin.
* `Rahatlat` - Altındaki kafes noktalarını rahatlatan bir fırça.
* `Elastik` - [Elastik](#elastic) aracı gibi, kafes noktalarını elastik bir düşüşle çeken bir fırça.
* `Gizmo` - Seçili noktaları gizmo ile taşıyın, döndürün ve ölçekleyin. Alt modu `Eksen`'dir.
* `Lasso` - Kafes noktalarını kementle seçin; `Seçimi kaldır` onları seçimden çıkarır.

Şekil açılır penceresinde ayrıca, nokta sürüklemelerinin komşu noktaları da hareket ettirmesini sağlayan `Yumuşak yarıçap` (ızgara hücresi cinsinden; 0 yalnızca seçimi hareket ettirir) ve `Seçimi tersine çevir` bulunur.

Görünümün üst kısmındaki bir araç çubuğunda şunlar bulunur:

* `Tamamla` - Deformasyonu nesneye uygular ve kafesi kaldırır.
* `Sıfırla` - Kafesi ve deformasyonunu kaldırır.
* `Opaklık` - Kafesin görüntülenme opaklığı.
* `Ayna tarafı` - Simetriyle, kafesin hangi ayna tarafının gösterileceği ve seçilebileceği arasında geçiş yapar; gizli taraf için ayrı bir `Opaklık` ayarı vardır.
* `Izgara noktaları` - Kafesin hangi noktalarının hareket ettirilebileceği: tam ızgara, yüzey ve merkez noktası veya yalnızca yüzey.
* `Rijitlik` - Deformasyonun ne kadar sert olduğu; pürüzsüzden (%0) rijit ve doğrusala (%100) kadar.
* `Düşüş` - Deformasyonun kafesin dışında ne kadar uzağa kadar azalarak süreceği.
* `Hizala` - Kafesi nesneyle veya dünyayla hizalar.
* `X`, `Y`, `Z` `Bölüm` - Kafesin her eksendeki hücre sayısı. Yanlarındaki mod düğmesi bunların birbiriyle ilişkisini belirler: `x = y = z` üç eksende aynı sayıyı kullanır, `Düzenli` her eksende noktalar arasında aynı aralığı korur, `Özel` ise her ekseni serbestçe ayarlamanızı sağlar.

#### Kafes ayarları {#lattice-settings}
* `Yuvarlanma hızı` - [Taşı](#move-settings) aracındakiyle aynı yuvarlama seçenekleri; kafes noktaları sürüklenirken kullanılır.

### ![](/icons/tool_view.webp) Görüntüle {#view}
Bu "araç" özel bir şey yapmaz; sahnenizi değiştirmeden modeli görüntülemenin basit bir yoludur.

#### Görüntüle ayarları {#view-settings}
Görüntüle aracı etkinken bu ayarlar bazı görüntüleme seçeneklerini geçersiz kılar; böylece modelinizi sunmak veya kontrol etmek için temiz bir görünüm elde edebilirsiniz:

* `Primitif (Düzenle)`, `Tekrarlayıcı (Düzenle)`, `Işık (Düzenle)`, `Kamera (Düzenle)` - Görüntüle aracındayken görünümde primitifleri, tekrarlayıcıları, ışıkları ve kameraları düzenlemeye izin verir. Tutamaçlarını yanlışlıkla hareket ettirmemek için devre dışı bırakın.
* `Kamera kısayolu (her zaman)` - Kamera kısayol düğmelerini her zaman görünümde gösterir.
* `Maskeyi göster`, `Dış Hatlar`, `Seçilmemiş nesneleri karart` - Maskeyi, seçili nesnelerin dış hatlarını gösterir veya seçilmemiş nesneleri karartır. `Otomatik` her zamanki ayarınızı izler, `Hayır` ve `Evet` bunu zorlar.
* `Çizgiyi göster (Simetri)`, `Düzlemi göster (Simetri)` - Simetri çizgisini veya düzlemini aynı `Otomatik`, `Hayır` ve `Evet` seçenekleriyle gösterir.
* `Simge` - Grupların, tekrarlayıcıların, ışıkların, kameraların ve hiyerarşinin simgelerini aynı seçeneklerle görünümde gösterir.


## Araç kutusu bağlam menüsü {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Araç kutusundaki bir araca sağ tıklamak veya uzun basmak bir bağlam menüsü açar. Bu menüde şu seçenekler bulunur:

* `Kaydet` - Araçta yaptığınız değişiklikleri kaydeder
* `Klonlama` - Aracı yeni bir araç kısayolu olarak çoğaltır
* `Son kaydetme` - Aracın daha önce kaydedilmiş sürümüne geri döner
* `Simge` - Aracın simgesini değiştirir. Aracın özel bir simgesi varsa bu düğme onu kaldırır.
* `→ ...` - Aracı araç kutusunun başka bir klasörüne veya yeni bir klasöre taşır
* `Sıfırla` - Aracı varsayılanlarına sıfırlar

Klonlanmış araçlarda ayrıca `Yeniden Adlandır` ve `Sil` bulunur.
