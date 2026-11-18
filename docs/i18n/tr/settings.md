# ![](/icons/cog.webp) Ayarlar {#reset-to-default}

Ayarlar menüsü, Nomad'ın görünümünü ve davranışını kontrol eden birçok seçenek içerir.

![](/images/settings_overview.webp)

Menünün üstündeki düğme sırası doğrudan bir bölüme atlar: `İmleç`, `Gösterge`, `Taslak`, `Izgara`, `İki taraflı`, `Dış Hatlar`, `Vurgula`, `Gezgin`, `İstatistik`, `Tutamaklar`, `Biçim`, `Tekrarlayıcılar` ve `Çoklu Çözünürlük`.

## Ekran ayarları {#display-settings}
Bu bölüm, menünün aşağısındaki ayarların çoğu için hızlı erişim kısayolları içerir.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Yumuşak gölgelendirme {#smooth-shading}
Yumuşak ve fasetli gölgelendirme arasında geçiş yapar. Fasetli modda poligonlar birbirinden bağımsız gölgelendirilir; böylece alttaki topolojiyi görebilirsiniz.
Şekillendirme aşamasında fasetli gölgelendirmeyi görmek, işleme için ise yumuşak gölgelendirmeye geçmek faydalı olabilir.

Yumuşak gölgelendirmeyi kapatmak performansı biraz artırır.

### ![](/icons/outline.webp) Dış Hatlar {#outline-quick}
Geçerli seçiminizin etrafında bir dış hat gösterir veya gizler.

[Seçilmemiş nesneleri karart](#darken-unselected-objects) devre dışıysa, seçili ağ örgünüz (veya örgüleriniz) hakkında görsel geri bildirim almak için kullanışlıdır.

Performans açısından, [Seçilmemiş nesneleri karart](#darken-unselected-objects) kullanmak dış hat çözümünden çok daha iyidir.

### ![](/icons/grid.webp) Izgara {#grid-quick}
Arka planda bir ızgara gösterir veya gizler; nesnelerin yerleşimini ve ölçeğini anlamak için kullanışlıdır.

### ![](/icons/culling.webp) İki taraflı {#two-sided-quick}
Poligonların iki taraflı gösterimini açıp kapatır. Tüm yüzler belirli bir yöne bakar.
*Arka yüz* sayılan yüzler, kameranın bakış noktasından "uzağa" bakan yüzlerdir.

Örneğin açılıştaki basit kürenin yüzleri dışarıya bakar.
Kamerayı kürenin içine taşırsanız bu yüzlerin arka tarafını görürsünüz.

Çoğu zaman yüzlerin arka tarafını görmemeniz gerekir; bu yüzden onları renklendirmek olası sorunları veya hatalı topolojiyi fark etmenize yardımcı olabilir.

`İki taraflı` gösterimi kapatmak işleme performansını biraz artırabilir.


### ![](/icons/wireframe.webp) Genel taslak {#wireframe-quick}
Bir tel kafes katmanını açıp kapatır.

Tel kafesi etkinleştirmenin performansı düşüreceğini unutmayın.

### ![](/icons/navigator.webp) Gezgin {#snap-cube-quick}
Sahnenin köşesinde bir yardımcı simge gösterir veya gizler; uzayda yönünüzü bulmak ve ön/arka/sol/sağ/üst/alt görünümler arasında hızlıca geçiş yapmak için kullanışlıdır.

### ![](/icons/palette.webp) Boyamayı göster {#show-painting}
Boya gösterimini açıp kapatır. Kapalıyken nesneler, boyamaları yerine %25 pürüzlükte, beyaz, metalik olmayan bir malzemeyle gösterilir.

### ![](/icons/tool_hide.webp) Gizlemeyi Kullan {#use-hide}
Gizleme modunu açıp kapatır. Kapatıldığında gizleme hâlâ oradadır, yalnızca devre dışıdır. Şu anda gizleme aracını kullanıyorsanız bu düğme devre dışıdır.

### ![](/icons/shield.webp) Maskeyi göster {#show-mask}
Maske modunu açıp kapatır. Kapatıldığında maske hâlâ oradadır, yalnızca devre dışıdır. Yeniden etkinleştirmek için bu düğmeye tekrar basın.

Maskeyi gizleyip YİNE DE etkin tutmanız gerekiyorsa, aşağıdaki maske rengini kullanıp beyaza ayarlayın. İşiniz bitince griye geri almayı unutmayın!

Şu anda bir maske aracı kullanıyorsanız bu düğmenin devre dışı olduğunu unutmayın.

### ![](/icons/shield.webp) Maske → Opak {#mask-opaque}
`Maske → Opak`, maskelenmiş maske için saydam verteksleri yok sayar. Bu yalnızca verteks ve doku opaklığı için geçerlidir; “gizle” ile gizlenen yüzler yine gizli kalır. Yalnızca `Maskeyi göster` açıkken kullanılabilir.

### ![](/icons/bang.webp) Vurgula {#highlight-quick}
Seçim vurgusu parlamasını açıp kapatır. Nesneleri seçerken, seçili nesne 500 milisaniye boyunca kısa bir süreliğine parlar. Parlamanın rengi ve süresi aşağıda özelleştirilebilir.

### ![](/icons/list.webp) İstatistik {#stats-quick}
3d görüntü alanındaki durum bilgisi metnini açıp kapatır. Bu metin sistem belleğiniz, sahnedeki toplam verteks sayısı ve geçerli seçimin verteks sayısı hakkında bilgi gösterir.

----- 

### ![](/icons/cube.webp) Seçilmemiş nesneleri karart {#darken-unselected-objects}
Seçili olmayan nesneler karartılır; böylece geçerli seçim öne çıkar.

### ![](/icons/shield.webp) Maske {#mask}
Maskeleme için kullanılan, nesnenizin rengiyle çarpılan renk; varsayılan olarak orta gridir. Maskeyi görünmez yapmak için beyaza ayarlayın, ama işiniz bitince griye geri almayı unutmayın!

## ![](/icons/cursor.webp) İmleç {#cursor}

### Daire {#show-circle-while-sculpting}
Fırça yarıçapı dairesinin ne zaman gösterileceği:

* `Otomatik` - daireyi gösterir, ama şekillendirirken gizler.
* `Hayır` - daireyi hiçbir zaman göstermez.
* `Evet` - daireyi her zaman, şekillendirirken bile gösterir.

### Küçük noktayı göster {#show-small-dot}
Şekillendirirken veya kameranın pivot noktası değiştiğinde fırça darbesinin ortasında bir nokta gösterir.

### Dengeleyici ipi göster {#show-rope-stabilizer}
Darbe ayarlarında [Yavaş dengeleyici ip](stroke.md#lazy-rope-stabilizer) etkinken ipin uzunluğunu gösteren bir çizgi çizer.

### Kamera yatışı ipucunu göster {#show-roll-hint}
Bir yuvarlama tuş ataması kullanırken yuvarlama yönü kılavuzunu gösterir.

### ![](/icons/radius.webp) Büyüklük {#dot-size}
Küçük noktanın büyüklüğü.

### Renkler {#cursor-colors}
İmleç, ne yaptığınıza göre renk değiştirir: `Şekillendir`, `Arka Plan` (arka planın üzerinde gezinirken), `Maske`, `Pürüzsüzleştir`, `Kamera` ve `Yarıçap`. Her renk burada özelleştirilebilir.

## ![](/icons/cursor.webp) Gösterge {#indicator}
![](/images/settings_indicator.webp)

Eğitimler ve ekran kayıtları için görsel gösterge(ler) görüntüler. Açmak için `Evet` olarak ayarlayın (iOS'ta ayrıca bir `Otomatik` seçeneği de vardır).

`Parmak`, `Stylus` ve `Fare` düğmeleri, o türde bir giriş algılandığında bir simge gösterilmesini sağlar.

### Renk {#indicator-color}
Göstergenin rengi.

### Büyüklük/Simge/Daire {#indicator-shape}
Göstergenin büyüklüğünü ve içindeki simge ile dairenin opaklığını ayarlayan kontroller.

## ![](/icons/wireframe.webp) Genel taslak {#wireframe}
![](/images/settings_wireframe.webp)
Tel kafes katmanını etkinleştirir.

### Hedef {#target}
Tel kafesin seçilmemiş nesnelerde mi, yalnızca seçili nesnelerde mi, yoksa tüm nesnelerde mi gösterileceğini belirler.

### Gizle {#hide}
Gizlenmiş poligonlar için tel kafesin yine de gösterilip gösterilmeyeceğini belirler.

### Çoklu Çözünürlük: Yalnızca seviye 0 {#multiresolution-level-0-only}
Çoklu çözünürlük, seviye 0'ın tel kafesini daha koyu, daha yüksek seviyeleri ise giderek daha açık gösterir. Etkinleştirildiğinde bu seçenek yalnızca seviye 0'ın tel kafesini gösterir.

### Renk {#wireframe-color}
Tel kafesin rengini ve opaklığını ayarlar.

## ![](/icons/grid.webp) Izgara {#grid}
![](/images/settings_grid.webp)
Izgarayı etkinleştirir.

### Tuttur {#snap}
Bu seçenekler, eğri ve şekil tabanlı araçların (`Torna`, `Tüp`, çokgen ve yol şekilleri...) noktalarının siz çizerken bir yere tutturulmasını sağlar:

* `Izgaraya tuttur` - ızgaraya tutturur.
* `Noktalara tuttur (hizalanmış görünüm)` - kamera bir eksene hizalıyken yakındaki mevcut noktalara tutturur.
* `Noktalara tuttur (serbest görünüm)` - kamera hizalı değilken yakındaki mevcut noktalara tutturur.

### Renk {#grid-color}
Izgaranın rengini ve opaklığını ayarlar. Bu seçenekler ızgara görünürken belirir.

`Vinyet`, ızgarayı kenarlarına doğru soldurur. `Bölümün eşiğini yakala`, ızgara başka bir alt bölüm seviyesine geçmeden önce ızgara çizgilerinin ekranda ne kadar sıklaşabileceğini piksel cinsinden belirler.

## ![](/icons/culling.webp)İki taraflı {#two-sided}
Poligon yüzlerinin iki taraftan da görünmesini sağlar.

### Arka yüzün rengi {#backface-color}
`Renklendirilmiş arka yüz` arka yüzlerin renklendirilmesini etkinleştirir, `Arka yüzün rengi` de bu rengi belirler.

## ![](/icons/outline.webp)Dış Hatlar {#outline}
Seçili nesnelerin etrafında bir dış hat gösterir.

### Dış hat rengi, Kalınlık {#outline-color-thickness}
Dış hattın rengini ve `Kalınlık` değerini ayarlar.


## ![](/icons/bang.webp) Vurgula {#highlight}
Seçim değiştiğinde kısa bir parlama gösterir.
### Renk, Süre {#color-duration}
Parlamanın rengini ve milisaniye cinsinden süresini ayarlar.

## ![](/icons/navigator.webp) Gezgin {#snap-cube}
![](/images/settings_snapcube.webp)

Sahnenin köşesinde bir yardımcı simge gösterir; ön/arka/sol/sağ/üst/alt görünümler arasında hızlıca geçiş yapmak için kullanışlıdır. Ortografik görünümler arasında geçiş yapmak için yüzlerine dokunun.

### Biçim {#shape}
Gezgin için küre, küp veya gnomon (eksen göstergesi) biçimi arasında seçim yapın.

### Hizalamayı Sınırla {#restrict-alignment}
Yaslama görünümlerini dünya eksenlerine hizalar. Etkinleştirildiğinde yalnızca 6 ana görünüm mümkündür. `Otomatik` ayarında bu kısıtlama yalnızca kamera `Döner platform` modundayken uygulanır.

### Büyüklük {#size}
Gezgin'in büyüklüğünü ayarlar.

### 180° Çevir {#flip-180}
Görünüm yaslanmışken Gezgin'in ortasına dokunmanın görünümü 180 derece döndürmesini sağlar. Örneğin görünüm öne yaslanmışsa, Gezgin'e dokunmak arka görünüme döner.

### Kenarlar ve köşeler {#edges-corners}
Kenarlara ve köşelere (amber renkli bölgeler) yaslama görünümleri ekler. Gnomon biçiminde kullanılamaz.

### Döner platform sürüklemesi {#turntable-drag}
Gezgin'i sürüklemek, kamerayı yuvarlamadan döndürür ve her yaslama görünümünde bir an durur. Gezgin'i bunun yerine `İztopu` döndürmesiyle sürüklemek için devre dışı bırakın. Her iki durumda da sürükleme yatay veya dikey kalır. `Döner platform` kamerasında Gezgin her zaman bu şekilde sürüklenir.

### Konum {#snap-position}
Gezgin'in hangi köşede olacağını belirler.


## ![](/icons/list.webp) İstatistik {#stats}
![](/images/settings_stats.webp)

Sistem belleğiniz, sahnedeki toplam verteks sayısı ve geçerli seçimin verteks sayısı hakkında bilgi gösterir.

### Konum {#stats-position}
İstatistiklerin hangi köşede olacağını belirler.

## ![](/icons/edit_radius.webp) Tutamak {#handle}
Gizmo gibi, görüntü alanında sürüklediğiniz tutamakların ayarları.

### Sayısal girdi {#gizmo-input}
Gizmo kontrollerinden birine dokunulduğunda sayısal değer girmeye izin verir.

### Etkileşimde gizle {#hide-on-interaction}
Gizmo ile etkileşim halindeyken onu soldurur, böylece yolunuza çıkmaz.

### ![](/icons/opacity.webp) Opaklık {#handle-opacity}
Tutamakların opaklığı.

## ![](/icons/shape_lasso.webp) Biçim {#shape-settings}
Şekil darbeleriyle (kement, dikdörtgen, eğri...) çizdiğiniz şekillerin ekranda nasıl görüneceği.

### ![](/icons/opacity.webp) Dolgu, Dış çizgi {#shape-fill-outline}
Şeklin içinin ve etrafındaki çizginin opaklığı.

### Renkler {#shape-colors}
Her araç türü için şeklin rengi: `Maske`, `Gizle`, `Yüz Grubu` ve `Kes`.

## ![](/icons/array.webp) Tekrarlayıcılar {#primitive-repeaters}
[Tekrarlayıcıların](scene#repeaters) (dizi, radyal, eğri, yüzey) oluşturduğu kopyalar için sınırlar. Bir tekrarlayıcı kontrolden çıktığında Nomad'ın akıcı kalmasını sağlarlar.

### ![](/icons/cube.webp) En fazla kopya {#repeater-max-copies}
Tek bir tekrarlayıcının oluşturabileceği en fazla kopya sayısı. Nomad, boyutları ne olursa olsun çok sayıda nesneyle zorlanır.

### ![](/icons/cube.webp) Sahnedeki kopyalar {#repeater-scene-copies}
Tüm sahne için kopya bütçesi. Düşük poligonlu bir kopya az geometri tüketir ama yine de tam bir nesnedir; bu yüzden küçük kopyaların ilk ulaştığı sınır budur.

### ![](/icons/triangle.webp) Maks yüz {#repeater-max-faces}
Sahnedeki tüm kopyalar için yüz bütçesi. Bu aşıldığında, en ağır nesneler kopyalarını ilk kaybeder.

## ![](/icons/multires.webp) Çoklu Çözünürlük {#multires}
### Maks. verteks sayısı {#multires-lowres-count}
Bu verteks sayısının üzerine çıkan bir çoklu çözünürlük alt bölme işlemine izin vermemek için bir eşik belirler; böyle bir işlem büyük olasılıkla Nomad'ı çökertir: Nomad, alt bölmeden önce kullanılabilir belleği kontrol etmez. Varsayılan değer 10 milyondur.
### Düşük çözünürlük eşiği {#multires-lowres-threshold}
Kamerayı hareket ettirdiğinizde ağ örgüsünün daha düşük çözünürlüklü bir hali gösterilebilir. Ağ örgüsünün daha yüksek bir çözünürlüğünü göstermek istiyorsanız bu değeri artırabilirsiniz.

## Ayarlar {#advanced}
### ![](/icons/reset.webp) Varsayılan ayara sıfırla {#reset}
Uygulamanın tüm tercih ayarlarını varsayılan değerlerine sıfırlar.

Bazı kaynaklar ayrı kaydedilir ve sıfırlanMAZ: projeler, tuş atamaları, araç önayarları, HDR ortamları, MatCap'ler, alfalar, fırça dokuları ve referans görselleri. Aydınlatma, süreç sonrası işlemler veya kamera görünümleri gibi projeyle birlikte kaydedilen her şey de olduğu gibi korunur.
