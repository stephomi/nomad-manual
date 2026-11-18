# ![](/icons/operation.webp) İşlem {#operation}

Bu menü, seçili nesnelerin tüm yüzeyine tek seferde bir işlem uygular: pürüzsüzleştirme, rahatlatma, parlatma, şişirme, renkleri ayarlama, boyayı ve maskeyi bulanıklaştırma veya keskinleştirme.

![](/images/operation_overview.webp)

## Genel bakış {#overview}

Bir fırça yalnızca darbe attığınız yerde çalışırken, bir işlem seçili nesnelerin bütün verteksleri üzerinde tek seferde çalışır. Başlıkta nesnenin adı, birden fazla nesne seçiliyse de nesne sayısı görünür.

Her işlem bir kaydırıcıdır: daha fazla uygulamak için sağa, daha az uygulamak için sola sürükleyin (iki yanında ok olan kaydırıcılarda sola sürüklemek ters işlemi uygular). Kaydırıcıyı bıraktığınızda sıfıra döner ve her sürükleme [Geçmiş](history.md) içinde tek bir adım olur; böylece bir işlemi küçük dozlarla birkaç kez uygulayabilirsiniz.

::: tip
İşlemler, bir voksel yeniden örgülemeden veya bir boolean işleminden sonra bütün ağ örgüsünü hızlıca toparlamanın pratik bir yoludur: biraz `Rahatlat` üçgenleri eşitler, biraz `Pürüzsüzleştir` de gürültüyü giderir; her noktayı tek tek fırçayla aramanıza gerek kalmaz.
:::

## Filtreler {#filters}

Üstteki düğmeler, işlemlerin nereye uygulanacağını sınırlar:

* `Maske` - Maskelenmiş alanlara dokunulmaz.
* `Gizle` - Gizlenmiş alanlara dokunulmaz.
* `Kaydırma` - (Bir [katman](layers.md) seçiliyken) Yalnızca etkin katmanın şekillendirme içerdiği alanlar etkilenir; böylece bir katmanın içeriğini, geri kalanına dokunmadan pürüzsüzleştirebilir veya şişirebilirsiniz.

## Pürüzsüzleştirme {#smoothing}

* `Hacmi koru` - Yüzeyi küçültmeden pürüzsüzleştirir. Dişli düğmesi, bunun için kullanılan `Küçült` ve `Şişir` miktarlarını içerir.
* `Sınırı koru` - Ağ örgüsünün sınırındaki (bir deliğin kenarındaki) verteksler yerinde kalır.
* `Stabil düzleştirme` - Pürüzsüzleştirmeyi topolojiden bağımsız hale getirmeye çalışır. Poligon yoğunluğu çok değişkense en iyi sonucu verir.
* `Pürüzsüzleştir` - Yüzeyi pürüzsüzleştirir. Bunun yerine `Keskinleştir` için sola sürükleyin.
* ![](/icons/group.webp) `Pürüzsüzleştir` - [Yüz grupları](tools.md#facegroup) arasındaki sınırları pürüzsüzleştirir ve tırtıklı grup hatlarını düzeltir. Keskinleştirmek için sola sürükleyin.
* `Rahatlat` - Şekli koruyarak poligonları eşitler.
* ![](/icons/group.webp) `Rahatlat` - Yüz grubu sınırları boyunca poligonları rahatlatır.
* `Köşeleri koru` - Yüz grubu `Pürüzsüzleştir` ve `Rahatlat` işlemlerinde, sınırlar bu açıdan daha fazla döndüğü yerlerde sabit kalır; böylece kenarlar pürüzsüzleşirken köşeler keskin kalır. Açmak için onay kutusunu kullanın.

## Parlat {#polish}

[Parlat](tools.md#polish) aracı gibi, yüzeyi temiz yüzeylere (fasetlere) düzleştirir. `Açı`, hangi yüzlerin birlikte düzleşeceğini belirler: bu açıdan daha az bükülen yüzler tek bir faset olur. Daha düşük bir açı daha fazla kırışığı ve daha küçük fasetleri korur.

## Şişir {#inflate}

Yüzeyi normalleri boyunca dışarı, sola sürüklediğinizde ise içeri iter. `Normal (Rahatlat)` aynı anda poligonları da rahatlatır, böylece gerilmezler; kapatmak için onay kutusunu kullanın.

## Renk ayarları {#color-adjustments}

Ayarlanacak kanalı seçin: `Renk`, `Pürüzlük`, `Metaliklik seviyesi`, `Opaklık`, `Yoğunluk` (nesnede varsa [Quad Remesher](tools.md#quad-remesher) yoğunluk boyaması) veya `Maske`; ardından:

* `Pozlandırma` - Değerleri aydınlatır veya karartır.
* `Doygunluk` - (Yalnızca `Renk`) Daha canlı veya daha soluk renkler.
* `Kontrast` - Değerleri birbirinden uzaklaştırır veya birbirine yaklaştırır.
* `Renk Tonu` - Renkleri renk çemberi üzerinde kaydırır.

## Bulanıklık {#blur}

Seçili kanalları yüzey boyunca bulanıklaştırır: `Renk`, `Pürüzlük`, `Metaliklik seviyesi`, `Opaklık`, `Yoğunluk` veya `Maske` kanallarını açıp kapatın, ardından `Bulanıklık` kaydırıcısını sürükleyin. Bunun yerine `Keskinleştir` için sola sürükleyin.

Maske için bu, [Maske](tools.md#mask) aracındaki `Bulanıklık` kaydırıcısıyla aynıdır. Burada boya kanallarını da bulanıklaştırabilirsiniz.
