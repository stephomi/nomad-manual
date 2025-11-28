# ![](/icons/pencil.webp) Fırça Darbesi {#stroke}

---
![](/images/stroke_overview.webp) 

## Genel Bakış {#overview}

Çoğu araç fırçasının darbe davranışını özelleştirebilirsiniz.
Ayarlar 2B boyama uygulamalarında bulunanlara benzer olmalıdır, ancak bazı seçenekler yontma ve 3B’ye özeldir.

Seçenekler 5 alt menüye ayrılmıştır:

| Name     | Icon                         | Description                                                        |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Stroke   | ![](/icons/stroke_dot.webp) | Darbenin modele nasıl uygulandığını kontrol eder                   |
| Alpha    | ![](/icons/alpha.webp)      | Gri tonlamalı bir dokunun fırça damgası için nasıl kullanıldığını belirtir |
| Falloff  | ![](/icons/falloff.webp)    | Fırça gücünün merkezden kenara doğru nasıl değiştiğini kontrol eder |
| Filter   | ![](/icons/filter.webp)     | Fırçanın model geometrisinden nasıl etkilendiğini belirtir         |
| Pressure | ![](/icons/pressure.webp)   | Kalem basıncı tepkisini kontrol eder                               |

::: tip
Tüm darbe seçenekleri tüm araçlar için geçerli değildir. Mevcut araç tarafından kullanılmayan darbe seçenekleri devre dışı bırakılır veya gizlenir. 
:::


## Fırça darbesi {#stroke-1}

### Yarıçap {#radius}

![](/images/stroke_radius.webp)

#### Yarıçapı paylaş {#share-radius}

Etkinleştirildiğinde, tüm araçlar aynı yarıçapı kullanır; varsayılan olarak her aracın kendi yarıçapı vardır.

#### Boyut {#size}

* Screen - yarıçap ekran birimleriyle ayarlanır. Yarıçapı 100 piksel genişliğinde yaparsanız, yakınlaştırıp uzaklaştırsanız bile 100 piksel genişliğinde kalır.
* Constant (3d) - yarıçap 3B birimlerle ayarlanır. Örneğin bir küre oluşturup yarıçapı küreyle aynı boyuta getirirseniz, yakınlaştırıp uzaklaştırsanız bile yarıçap küreyle aynı boyutta kalır.


### Fırça darbesi {#stroke-type}

![](/images/stroke_strokemode.webp)

Darbeler birden fazla kipte davranabilir:

### ![](/icons/stroke_dot.webp) Nokta {#dot}
Normal bir boya darbesi gibi sürükleyin. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Döndür {#roll}
Fırça alfası, dikiş gibi kumaş efektleri yapmak için darbenin yönünü takip edecek şekilde döndürülür. 
![](/videos/stroke_roll.mp4) 

 ### ![](/icons/radius.webp) Lock + radius
Sabit **_yükseklik_** ile bir fırça darbesi damgalayın. Sürükleme ölçeği ve dönüşü ayarlar.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/falloff.webp) Kilit + yoğunluk {#lock-intensity}
Sabit **_yarıçap_** ile bir fırça darbesi damgalayın. Sürükleme yüksekliği ve dönüşü ayarlar.
![](/videos/stroke_lock_intensity.mp4) 

![](/images/stroke_strokemodemove.webp)

`Move` ve `Drag` araçlarının kendilerine ait 3 seçeneği vardır:

### ![](/icons/snake.webp) Sürükle {#drag}

Darbe sırasında fırça yarıçapının içindeki alanı güncellemeye devam eder. Hızlı bir darbe yüzeyi geride bırakırken, yavaş bir darbe malzemeyi tutar ve daha uzun şekiller oluşturur. Bu, `Drag` aracı için varsayılan kipdir. `Dynamic Topology` ile yılan benzeri çıkıntılar yapmak için kullanılabilir. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Yakala {#grab}
Fırça başlatıldığında fırça yarıçapının içindeki alanı seçer ve bu seçimi korur. Bu, daha hassas taşıma işlemleri için kullanışlıdır; hareket mesafesini dikkatlice ayarlayabilir ve başlangıçta seçtiğinizden fazlasını yanlışlıkla hareket ettirmezsiniz. Bu, `Move` aracı için varsayılan kipdir.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Kilit + yarıçap (sürükle) {#lock-radius-drag}
Kullanıcı yarıçapı yok sayılır ve başlangıç noktasından ne kadar uzağa sürüklendiğine bağlı olarak dinamik olarak ayarlanır. Küçük mesafe = küçük yarıçap, daha büyük mesafe = daha büyük yarıçap. Düşüş şeklini kontrol etmek için yoğunluk kaydırıcısını kullanın. Organik, lastiksi şekilleri bloklamak için kullanışlıdır.
![](/videos/stroke_lockradius_drag.mp4) 



### Aralık yoğunluğunu ayarla {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Düşük aralıklı darbeler (%50’nin altında) hızlıca birikebilir ve daha yüksek aralıklı değerlere göre daha yoğun darbeler oluşturabilir. Bu anahtar bunu telafi eder; böylece darbeler, aralıktan bağımsız olarak yaklaşık olarak aynı yoğunlukta olur.

### Fırça darbesi aralığı {#stroke-spacing}
Sürükleme işlemi sırasında her fırça darbesinin ne kadar aralıkla uygulanacağını belirler. %100’ün altındaki değerler üst üste biner ve kesintisiz bir darbe görünümü verir. %100’ün üzerindeki değerler boşluklar bırakmaya başlar; dikiş veya fermuar gibi detayları yontmak için kullanışlıdır.

### Tembel ip dengeleyici {#lazy-rope-stabilizer}
Darbeler, imleç konumunun belirli bir mesafe gerisinden gelir. Bu, düzgün çizgiler çizmek için kullanılabilir.
![](/videos/stroke_lazy_rope.mp4) 

### Fırça darbesi yumuşatma {#stroke-smoothing}
Daha düzgün bir darbe elde etmek için birden fazla imleç konumunu ortalamaya alır.
Yüksek değerlerde darbe imlecin gerisinde kalır ama sonunda yetişir.
Bu, düzgün çizgiler çizmek için kullanışlıdır.

### Yakalama yarıçapı {#snap-radius}
Darbe başlangıcını önceki darbenin sonuna yaklaştırır. Yarıçap, önceki darbenin sonunu aramak için ne kadar uzağa bakılacağını belirler. Sık sık duraklayarak uzun, kesintisiz çizgiler çizerken kullanışlı olabilir.

### ![](/icons/silhouette.webp) Silüet {#silhouette}
![](/images/stroke_silhouette.webp)
Varsayılan olarak darbeler yalnızca fırça yarıçapı içindeki model yüzeyini etkiler. Silhouette etkinleştirildiğinde darbe tüm model boyunca projeksiyon yapılır. Bu, bir modelin ilk bloklamasını yaparken veya yanların dik kalması gereken şekiller için çok kullanışlı olabilir.

Projeksiyon yönü açıkça ayarlanabilir; varsayılan 'Closest' yöntemi, görünüme göre en iyi açıyı algılar. 

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp) Rastgeleleştir {#randomize}

![](/images/stroke_randomize.webp)

Darbe yoğunluğu, ötelemesi, dönüşü ve ölçeği ayrı ayrı rastgeleleştirilebilir. Bu, çeşitli efektler oluşturmak için kullanılabilir; örneğin paint aracıyla rastgeleleştirme, benekli renkler oluşturabilir veya crease aracıyla rastgeleleştirme, cilt detayı oluşturmak için kullanılabilir.

![](/videos/stroke_randomize.mp4) 

### Fırça darbesi ofseti {#stroke-offset}

Darbeye sabit bir ofset uygular. Bu, parmağınızın darbeyi kapatacağı küçük ekranlar için kullanışlıdır. 


## ![](/icons/alpha.webp) Alfa {#alpha}
![](/images/stroke_alpha.webp) 

`Alpha`, fırça davranışınızı modüle eden bir dokudur.
Siyah piksellerin deformasyon yapmadığı, beyaz piksellerin tam deformasyon yaptığı gri tonlamalı bir görüntüdür.

Alfayı değiştirmek için alfa görseline tıklayın.

Bir materyal ön ayarından alfa yüklemek için materyal ön izlemesine tıklayın. Buradan materyal ön ayarlarını kaydedebilir ve dokuları araçla birlikte gömmeyi seçebilirsiniz.

::: tip
Doku asla yeniden boyutlandırılmaz, bu nedenle büyük dokular performansı yavaşlatabilir.
:::

### Pikselleri ters çevir {#invert-pixels}
Bu, görüntüdeki değerleri tersine çevirir; böylece siyah pikseller beyaz, beyaz pikseller siyah olur.

::: tip

Nomad ile gelen yerleşik alfalar ters çevrilemez.

:::

### Ölçekleme {#scaling}

Nomad’daki fırça boyutu, kullanıcı tanımlı yarıçapa sahip bir dairedir. Dokular genellikle kare veya dikdörtgendir; `Scaling` parametreleri, dokunun daire içine nasıl sığacağını belirlemenizi sağlar. Kare bir doku için 0.7 değeri, dokuyu dairenin içine sığdırır. 1 değeri, dairenin dokunun içinde kalacağı şekilde dokuyu büyütür ve kenarları kırpar.

![](/images/alpha_scaling.webp) 

`Scaling - Y` etkinleştirildiğinde alfayı dikey olarak esnetmenize olanak tanır.

![](/images/alpha_scaling_y.webp) 

### Döndürme {#rotation}

Alfa dokusu, darbenin yönünü takip edecek şekilde döndürülür. Bir dönüş ofseti ekleyebilirsiniz ve kilit simgesi etkinse, doku ekrana göre bu dönüşe kilitli kalır.

### Döşeme {#tiling}
![](/images/stroke_tiling.webp) 

Doku, fırça profilinin içinde ne sıklıkla tekrar eder. Döşeme kipleri, darbe içinde tek bir dokuya, tekrarlanan dokulara veya her ikinci dokunun çevrildiği, desenler oluşturmaya veya kusursuz dokular yapmaya yardımcı olan yansıtılmış dokulara izin verir.

![](/videos/alpha_tiling.mp4) 



### Orta değer {#mid-value}

Varsayılan olarak siyah pikseller deformasyon yapmaz, beyaz pikseller tam pozitif deformasyon yapar; örneğin, kaya alfalı bir kil fırçası, yalnızca alfa siyah olmadığında yüzeyi dışarı çeker.

Fırçanın yüzeyi içeri itmesini veya hem içeri hem dışarı itmesini istiyorsanız, orta değeri değiştirebilirsiniz. Değeri 0.5’e ayarlarsanız, alfadaki orta gri hiçbir şey yapmaz, siyah değer içeri iter, beyaz dışarı çeker.




## Düşüş {#falloff}

![](/images/falloff_menu.webp) 

Bu, [Alpha](#alpha)’ya benzer, ancak yoğunluğu tek bir eğriyle yönlendirirsiniz. Bu, ayrıntı için bir doku ve kenar solmasını ve aracın merkezindeki yoğunluğu kontrol etmek için falloff kullanabilmeniz için alfayla birleştirilir.

Eğri üstteyken bu tam deformasyondur, alttayken fırçanın etkisi yoktur.

Eğriyi, fırça ucunun enine kesiti olarak düşünebilirsiniz. Alt bölüm, fırçanın tek bir 'damgasının' model yüzeyinde nasıl görüneceğine dair bir ön izleme sunar ve fırça için bir alfa dokusu varsa, falloff ve alfanın nasıl etkileşeceğini ön izlemek için bu da gösterilir.

### Hazır ayar {#preset}
Bu seçiliyken, eğri grafiğine tıklamak bir ön ayar menüsü açar. Yuvarlak eğriler daha yumuşak sonuçlar verir, köşeli eğriler daha keskin sonuçlar verir. Sol araç çubuğundaki `Sub` düğmesi, falloff’u tersine çevirir; böylece eğrinin üst kısmı yüzeyi dışarı çekmek yerine içeri iter veya tam tersi.

### Catmull-Rom {#catmull-rom}
Seçildiğinde kullanıcı kendi falloff eğrilerini çizebilir. Eğri düzenleyici, Nomad’in geri kalanındaki eğrilerle aynı şekilde çalışır:

* Yeni bir nokta oluşturmak için eğriye tıklayın
* Bir noktayı yeniden konumlandırmak için sürükleyin
* Keskin ve yumuşak arasında geçiş yapmak için bir noktaya tıklayın
* Bir noktayı komşu noktaya sürükleyerek kaldırın

### B-spline {#b-spline}
Seçildiğinde kullanıcı kendi falloff eğrilerini çizebilir. Düzenleyici Catmull-Rom ile aynı şekilde çalışır, ancak eğri noktaları eğriyi doğrudan üzerinde olmak yerine etkiler; bu da daha yumuşak eğri şekilleri oluşturmaya yardımcı olabilir.

Eğri düzenleyicide 3 düğme vardır:

| Item     | Icon                        | Description                                  |
| :------: | :-------------------------: | :------------------------------------------: |
| Maximize | ![](/icons/maximize.webp)  | Eğri düzenleyiciyi genişletir                |
| Reset    | ![](/icons/reset.webp)     | Eğriyi varsayılan duruma döndürür            |
| Symmetry | ![](/icons/symmetric.webp) | Eğriyi simetrik bir 'fırça ucu' olarak gösterir |


### Etki {#influence}

* Sphere (3d) - Etki, verteksin fırça merkezine olan uzaklığı alınarak hesaplanır.
* Circle (2d) - Verteks, fırça merkezine olan uzaklığı alınmadan önce alan düzlemine yansıtılır. Bu, alfaların örneklenmesine benzer. 
* Cylinder - Etki, aşağıdaki Silhouette kipinde kullanılan, alan boyunca bir silindir olarak projeksiyon yapılır.

### Silüet {#silhouette-1}
Varsayılan olarak darbeler yalnızca fırça yarıçapı içindeki model yüzeyini etkiler. Silhouette etkinleştirildiğinde darbe tüm model boyunca projeksiyon yapılır. Bu, bir modelin ilk bloklamasını yaparken veya yanların dik kalması gereken şekiller için çok kullanışlı olabilir.



## Filtre {#filter}

![](/images/filter_menu.webp) 

### Fırça darbesini biriktir {#accumulate-stroke}
Darbe başına ne kadar madde eklenip/çıkarılabileceğine dair sınırı kaldırır. Örneğin `Clay` aracında bu etkindir, böylece malzeme birikmeye devam eder; `Brush` aracında ise bu devre dışıdır, böylece aynı darbeyi ağın aynı bölgesi üzerinde hareket ettirmeye devam ederseniz darbeler malzeme eklemeyi durdurur. 

### Yalnızca öne bakan verteks {#front-facing-vertex-only}
Bu seçenek, arkaya bakan verteksleri yok sayar.
İnce bir geometrinin bir kısmını, diğer tarafı etkilemeden boyamak istiyorsanız kullanışlı olabilir.
Yontma için de çalışır, ancak bazı yapaylıklar görebilirsiniz.

### Dinamik topolojiye izin ver {#allow-dynamic-topology}
Bu seçenek yalnızca ağınız [Dynamic Topology](topology.md#dynamic-topology) kipindeyse kullanılabilir. Dinamik topolojiyi araç başına devre dışı bırakabilir veya etkinleştirebilirsiniz.

### Bağlı topoloji {#connected-topology}
Yalnızca araçla dokunduğunuz yüzeye bağlı verteksleri yontmayı etkinleştirir. Örneğin `Move` aracıyla kullanıldığında, başka bir parçayla kesişse bile bir kısmı hareket ettirmenize olanak tanır.
![](/videos/connected_topology.mp4)

### Alanı koru {#protect-area}
![](/images/filter_protect_area.webp) 

Bu seçenekler, çeşitli koşullar altında araçların ağınızın bazı kısımlarını etkilemesini durdurur. 

'Auto' seçeneği, [Shading](shading) menüsünde gizleme, maskeleme veya yüz grubu görünürse bunların korunacağı, ancak bu menüde kapatılmışlarsa korumanın devre dışı bırakılacağı anlamına gelir.

* `All` - Koruma filtrelerinin küresel mi yoksa araç başına mı olduğunu ayarlamak için geçiş.
* `Hide` - Ağın bazı kısımları hide aracıyla gizlendiyse, korunup korunmayacağını ayarlayın.
* `Mask` - Ağın bazı kısımları maskeliyse, korunup korunmayacağını ayarlayın.
* `Facegroup` - Bir aracı yalnızca ilk dokunulan yüz grubunun içinde kullanıp kullanamayacağınızı ayarlayın.


### Keskin kenarları koru {#keep-sharp-edges}
Normalleri yüzey normalinden çok fazla farklı olan noktaları hariç tutar.

Düzlem alanının (Area sampling) nasıl hesaplandığını değiştirir.

Bu seçenek, düzleştirme tabanlı araçlar için veya çoğunlukla düz bir yüzeyi taşmadan renklendirmek istiyorsanız kullanışlı olabilir.

![](/videos/filter_keep_sharp_edges.mp4)

### Alan örnekleme {#area-sampling}
Bazı fırçalar veya darbe seçenekleri, çalışmak için yüzeye göre bir düzlem normali ve düzlem konumu gerektirir.

Bu ortalama düzlemin nasıl hesaplanacağını, örnekleme alanını araç yarıçapının bir oranı olarak ayarlayarak kontrol edebilirsiniz.

%100’de seçim dairesi içindeki her nokta hesaba katılır.

%0’da yalnızca en yakın verteks veya üçgen hesaba katılır. Bu değerler hem `Normal radius` hem de `Position radius` için bağlanabilir veya kilidi açılıp bağımsız olarak ayarlanabilir.


### Derinlik maskeleme {#depth-masking}
![](/images/stroke_depthmask.webp)

Hesaplanan düzleme (Area sampling) göre belirli bir mesafenin üstünde veya altında kalan noktaları hariç tutar.

Bu, yalnızca çıkıntılı bölgeleri veya yalnızca oyuk bölgeleri boyamak için kullanılabilir.

Grafik, yüzeyin enine kesitini temsil eder; yatay çizgi yüzeyin olduğu yerdir, daire yüzeyin üstünde ve altında boya düşüş yarıçapını temsil eder. `Height offset`, maskeleme hesaplamasına başlanacak yüzeyin üstünde veya altında bir yüzdeliktir. `Top area` ve `Bottom area`, ofset noktasının üstündeki ve altındaki düşüşü ölçeklendirmenize olanak tanır.

#### Örnek: Oyuklara boya {#example-paint-in-cavities}
Yalnızca oyuk bölgeleri boyamak için yükseklik ofsetini -%100’e ayarlayın ve üst alan kaydırıcısını yatay çizgiden uzak olacak şekilde ayarlayın. Bu, ilk tıklamanın 'sıfır' derinliğini belirleyeceği ve ardından yalnızca bu derinliğin altındaki alanların etkileneceği anlamına gelir.

![](/videos/stroke_depth_cavity.mp4)

#### Örnek: Tümseklere boya {#example-paint-on-bumps}
Yalnızca yüksek bölgeleri boyamak için yükseklik ofsetini +%90’a ayarlayın; böylece dairenin alt kısmı yatay çizgiyi az bir miktar keser. 'Yüksek' bir bölgenin tepesine tıkladığınızda bu derinliği ayarlar; böylece o derinlikteki, biraz altındaki ve üstündeki her şey boyanır. Derin oyuklar atlanır.
![](/videos/stroke_depth_bump.mp4)


## Basınç {#pressure}
![](/images/pressure_menu.webp) 

Kalem basıncının fırçaları nasıl etkilediğini kontrol eder.

Varsayılan olarak `Use global settings` etkindir; bu, tüm fırçaların aynı basınç değerlerini paylaşacağı anlamına gelir.

### Basınç - Yarıçap {#pressure-radius}

Bu eğri, fırça yarıçapının basınçtan nasıl etkilendiğini kontrol eder. Varsayılan, doğrusal bir ilişkidir; bu nedenle kaleminizin tepkisi yumuşaksa yarıçap değişimi de yumuşak hissettirmelidir. Bununla birlikte, birçok kalemin doğrusal olmayan bir tepkisi vardır; bunu bu eğriyle telafi edebilirsiniz. Örneğin, yarıçap yüksek basınçta maksimum değerine ulaşmıyormuş gibi geliyorsa, yukarı doğru kıvrılan 'out-pow3' gibi bir eğri ön ayarı kullanarak yarıçapı daha erken artırabilirsiniz.

Bu iletişim kutusu, falloff eğrisi görünümüne benzer; eğri penceresine dokunarak bir ön ayar kullanabilir veya Catmull-Rom ve B-Spline kipleriyle kendi eğrilerinizi çizebilirsiniz.

Sabit yarıçap istiyorsanız bu bölümü devre dışı bırakın.

### Basınç - Yoğunluk {#pressure-intensity}

Yarıçap kaydırıcısına benzer, ancak yoğunluğu kontrol etmek içindir. Sabit yoğunluk istiyorsanız bu bölümü devre dışı bırakın.

### Basınç yumuşatma {#pressure-smoothing}

Daha düzgün sonuçlar için kalem basınç olaylarını ortalamaya alır.