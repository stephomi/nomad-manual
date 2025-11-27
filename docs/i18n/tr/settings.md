# ![](/icons/cog.webp) Ayarlar 

Ayarlar menüsü, Nomad’in görünümünü ve davranışını kontrol etmek için birçok seçenek içerir.

![](/images/settings_overview.webp)

## Görüntü ayarları
Bu bölüm, bu menünün ilerleyen kısımlarındaki çoğu ayar için hızlı başlatma kısayolları içerir.

![](/images/settings_display_settings.webp)

### Yumuşak Gölgelendirme 
Yumuşak ve köşeli (faceted) gölgelendirme arasında geçiş yapar. Köşeli modda, çokgenler birbirinden bağımsız gölgelendirilir, böylece alttaki topolojiyi görebilirsiniz.
Heykel aşamasında köşeli gölgelendirmeyi görmek, ardından render için yumuşak gölgelendirmeye geçmek faydalı olabilir.

Yumuşak Gölgelendirme’yi devre dışı bırakmak performansı biraz artırır.

### Dış Çizgi
Geçerli seçiminiz için bir dış çizgiyi açıp kapatır.

Bu, [Seçilmemişleri Karart](#darken-unselected-objects) devre dışıysa, seçili ağ(lar)ınızı görsel olarak takip etmek için kullanışlıdır.

Performans açısından bakıldığında, dış çizgi çözümünü kullanmaktansa [Seçilmemişleri Karart](#darken-unselected-objects) kullanmak çok daha iyidir.

### Izgara
Arka plan ızgarasını açıp kapatır; nesne yerleşimini ve ölçeğini anlamak için kullanışlıdır.

### Çift taraflı
Çift taraflı çokgen gösterimini açıp kapatır. Tüm yüzler belirli bir yöne bakar.
*Kamera arkasına bakan yüzler* (backface), kamera bakış açısından “uzaklaşan” yönde olanlardır.

Örneğin başlangıçtaki basit kürenin yüzleri dışarıya doğru bakar.
Kamerayı kürenin içine taşırsanız, bu yüzlerin arka tarafını görürsünüz.

Çoğu zaman yüzlerin arka tarafını görmemeniz gerekir, bu yüzden onları renklendirmek olası sorunları veya hatalı topolojiyi tespit etmenize yardımcı olabilir.

`Çift taraflı` render’ı devre dışı bırakmak, render performansını biraz artırabilir.


### Tel Kafes
Tel kafes bindirmesini açıp kapatır. 

Tel kafesi etkinleştirmenin performansı düşüreceğini unutmayın.

### Yakalama Küpü
Sahnenin köşesinde, uzayda yönünüzü bulmak ve ön/arka/sol/sağ/üst/alt görünümler arasında hızlıca geçiş yapmak için yardımcı bir simgeyi açıp kapatır.

### Boyamayı Göster
Boya gösterimini açıp kapatır. Varsayılan boya, %25 pürüzlülükte, beyaz, metalik olmayan bir malzemedir.

### Gizlemeyi Kullan
Gizleme modunu açıp kapatır. Kapalıyken hâlâ mevcuttur, sadece devre dışıdır. Bu düğme, şu anda gizleme aracını kullanıyorsanız devre dışı kalır.

### Maskeyi Göster
Maske modunu açıp kapatır. Kapalıyken hâlâ mevcuttur, sadece devre dışıdır. Yeniden etkinleştirmek için bu düğmeye tekrar basın.

Maskeyi gizlemeniz ve yine de etkin kalmasını istemeniz durumunda, aşağıdaki maske rengini kullanın ve beyaza ayarlayın. İşiniz bittiğinde tekrar griye çevirmeyi unutmayın!

Bu düğmenin, şu anda bir maske aracı kullanıyorsanız devre dışı olduğunu unutmayın. 

### Maske -> Opak
Maske -> opak, maskelenmiş maske için şeffaf verteksleri yok sayar. Bu yalnızca verteks ve doku opaklığı için geçerlidir, “gizle” ile gizlenen yüzler yine gizli kalacaktır.

### Vurgu
Seçim vurgu flaşını açıp kapatır. Nesneleri seçerken, seçilen nesneyi 500 milisaniyeliğine sıcak pembe renkte yanıp söner. Flaşın rengi ve süresi aşağıdan özelleştirilebilir.

### İstatistikler
3B görünümde durum metni gösterimini açıp kapatır. Bu, sistem belleğiniz, toplam sahne verteks sayısı ve geçerli seçimin verteks sayısı hakkında bilgi gösterir.

----- 

### Seçilmemiş nesneleri karart
Seçili olmayan nesneler karartılır, böylece geçerli seçim öne çıkar.

### Maske
Varsayılan olarak orta gri olan, nesne renginizle çarpılan maskeleme rengi. Maskeyi görünmez yapmak için bunu beyaza ayarlayın, ancak işiniz bittiğinde tekrar griye çevirmeyi unutmayın!

## ![](/icons/cursor.webp) İmleç

### Heykelleme sırasında çemberi göster
Heykelleme sırasında fırça yarıçapını göstermeye devam eder.

### Küçük noktayı göster
Heykelleme sırasında veya kamera pivotu değiştirildiğinde, fırça darbesinin merkezinde bir nokta gösterir.

### Halat sabitleyiciyi göster
Vuruş ayarlarında tembel halat sabitleyici etkin olduğunda, halat uzunluğunu göstermek için bir çizgi çizer.

## ![](/icons/cursor.webp) Gösterge
![](/images/settings_indicator.webp)

Öğreticiler ve ekran kayıtları için görsel gösterge(ler) görüntüler.

`Parmak`, `Kalem` ve `Fare` düğmeleri, bu tür bir girdi algılandığında bir simge görüntülenmesini etkinleştirir.

### Renk
Gösterge rengi.

### Boyut/Simgesi/Çember
Gösterge boyutunu ve gösterge içindeki şekilleri ayarlamak için denetimler.

## ![](/icons/wireframe.webp) Tel Kafes
![](/images/settings_wireframe.webp)
Tel kafes bindirmesini etkinleştirir.

### Hedef
Tel kafesin yalnızca seçili nesnelerde mi, seçili olmayan nesnelerde mi, yoksa tüm nesnelerde mi gösterileceğini ayarlar.

### Gizle
Gizli çokgenler için tel kafesin gösterilmeye devam edip etmeyeceğini ayarlar.

### Çoklu çözünürlük: Yalnızca seviye 0
Çoklu çözünürlük, seviye 0 için tel kafesi daha koyu, daha yüksek seviyeler için giderek daha açık gösterir. Etkinleştirildiğinde, bu seçenek yalnızca seviye 0 tel kafesini gösterir.

### Renk
Tel kafes için renk ve opaklığı ayarlar.

## ![](/icons/grid.webp) Izgara
![](/images/settings_grid.webp)
Izgarayı etkinleştirir.

### Renk
Izgara rengi ve opaklığını ayarlar.

### Yakalama
Eğri tabanlı araçlar için ızgaraya yakalamayı etkinleştirir.

## ![](/icons/culling.webp)Çift taraflı
Çokgen yüzlerini her iki taraftan da görmeyi etkinleştirir.

### Arka Yüzü Renklendir, Arka Yüz Rengi
Arka yüzlerin renklendirilmesini ve renklendirme rengini etkinleştirir.

## ![](/icons/outline.webp)Dış Çizgi
Etkin nesnenin etrafında bir dış çizgiyi etkinleştirir.

### Dış çizgi rengi, Kalınlık
Dış çizginin rengini ve kalınlığını ayarlar.


## ![](/icons/bang.webp) Vurgu
Etkin nesne değiştiğinde kısa bir flaşı etkinleştirir.
### Renk, Süre
Flaşın rengini ve süresini milisaniye cinsinden ayarlar.

## ![](/icons/snap_cube.webp) Yakalama küpü
![](/images/settings_snapcube.webp)

Sahnenin köşesinde, ön/arka/sol/sağ/üst/alt görünümler arasında hızlıca geçiş yapmak için yardımcı bir simge görüntüler. Ortografik görünümler arasında geçiş yapmak için küpün yüzlerine dokunun.

### Şekil
Yakalama küpü için küp, küre veya gnomon şekli arasında seçim yapın.

### Hizalamayı kısıtla
Yakalama küpü üzerinde sürüklerken kamera döndürme kilitlemesini etkinleştirir. Etkin olduğunda, yakalama küpü üzerindeki sürükleme hareketi yalnızca sola/sağa veya yukarı/aşağı gider.

### Boyut
Yakalama küpünün boyutunu ayarlar.

### 180° çevir
Görünüm sabitlenmişse, küpün ortasına dokunulduğunda görünümü 180 derece döndürecek bir dokunma davranışını etkinleştirir. Örneğin görünüm öne sabitlenmişse, görünüm küpüne dokunmak arkaya döndürür.

### Konum
Yakalama küpünün hangi köşede olacağını ayarlar.


## ![](/icons/edit_radius_n.webp) İstatistikler
![](/images/settings_stats.webp)

Sistem belleğiniz, toplam sahne verteks sayısı ve geçerli seçimin verteks sayısı hakkında bilgi görüntüler.

### Konum
İstatistiklerin hangi köşede olacağını ayarlar.

## Primitif/Yineleyiciler
## Sayısal giriş
Gizmo bileşenlerine dokunurken sayısal girişe izin verir.

## Çoklu çözünürlük
### Maksimum verteks sayısı
Nomad’in muhtemelen çökmesine neden olacak bu poligon sayısından daha yüksek bir çoklu çözünürlük bölme işleminin yapılmasına izin vermemek için bir eşik ayarlar. Varsayılan 10 milyondur.
### Düşük çözünürlük eşiği
Kamerayı hareket ettirdiğinizde, ağın daha düşük çözünürlüklü bir hali görüntülenebilir. Ağın daha yüksek çözünürlüklü halini görüntülemek istiyorsanız bu değeri artırabilirsiniz.

## Ayarlar
### Varsayılana sıfırla
Tüm ayarları varsayılan değerlerine sıfırlar.
