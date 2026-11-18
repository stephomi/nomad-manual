# ![](/icons/symmetry.webp) Simetri {#symmetry}

Bu menü, fırça darbelerinin bir ayna düzlemi boyunca, radyal olarak veya döşeme şeklinde nasıl tekrarlanacağını kontrol eder; simetrik olmayan nesnelerde simetriyi geri getirmenin yollarını da sunar.

![](/images/symmetry_overview.webp) 

## Genel bakış {#overview}
Simetriyi birkaç şekilde kullanabilirsiniz:

* Ayna olarak: çalışmanızı X (sol/sağ), Y (üst/alt), Z (arka/ön) boyunca veya bunların bir birleşimi boyunca yansıtır.
* Radyal simetri X, Y, Z üzerinde bir tekrar sayısıyla ayarlanabilir; örneğin bir deniz yıldızı şekillendirmek için.
* Döşeme, darbelerinizi nesne boyunca tekrarlar; böylece heykel kesintisiz bir şekilde döşenir.
* Aynalar orijin etrafında (dünya modu) veya bir nesnenin merkezi etrafında (yerel mod) çalışabilir.
* Simetrik olmayan şekilde başlamış heykeller simetrik olmaya zorlanabilir.

Simetriyi açıp kapatmak için sol hızlı paneldeki (*"Sim"*) kısayolu da kullanabilirsiniz. Üzerindeki küçük 'L/W' yazısı, Nomad'ın Yerel mi yoksa Dünya simetri modunda mı olduğunu gösterir. Bir menü açmak için düğmeye uzun basabilir veya ekranın ortasına doğru kaydırabilirsiniz.

![](/images/symmetry_button.webp) 

Simetri ayarları her nesneyle birlikte kaydedilir ve menü başlığı düzenlediğiniz nesnenin adını gösterir.
Şekillendirme araçları aynı açık/kapalı durumunu paylaşırken, dönüştürme araçlarının ([Dönüştür](tools.md#transform) ve [Gizmo](tools.md#gizmo)) kendi durumları vardır.

::: tip
Simetri menüsü esas olarak darbe simetrisini kontrol etmek içindir. Nesneleri, [sahne menüsündeki tekrarlayıcılar](scene#repeaters) ile de aynalayabilir ve tekrarlayabilirsiniz.
:::

## ![](/icons/symmetry.webp) Etkin {#enabled}
Ayna modunu açar veya kapatır; sol hızlı paneldeki `Sim` düğmesiyle aynıdır. Kapalıyken bir uyarı simgesi bunu size hatırlatır, menü ayrıca geçerli araç simetriyi göz ardı ettiğinde de sizi uyarır.

## Düzlemler {#planes}

Simetri düzlemlerini ve radyal simetri için tekrar sayısını etkinleştirin. Tek bir düzlem seçmek zorunda olmadığınızı unutmayın; karmaşık simetriler için 1, 2 veya 3 düzlemin hepsini etkinleştirebilirsiniz.

`Radyal` satırı, her eksen etrafındaki radyal simetrinin tekrar sayısını ayarlar. Bunlar da tek bir eksenle sınırlı değildir; hatta düzlem simetrisiyle birlikte kullanılarak çok hızlı bir şekilde ayrıntılı sonuçlar üretebilirler. (Toplam tekrar sayısı 200 ile sınırlıdır.)

![](/videos/symmetry_demo.mp4) 

## Döşeme {#tile}

Darbelerinizi bir eksen boyunca, düzenli aralıklarla tekrarlayın; böylece heykel kesintisiz bir şekilde döşenir. Desenler, tuğlalar veya tekrarlamayı planladığınız bir doku için kullanışlıdır.

Her eksen için döşemeyi `Döşeme` düğmeleriyle açın, ardından bir `Sayı` (nesne boyunca kaç tekrar olacağı) veya bir `Mesafe` (iki tekrar arasındaki boşluk) belirleyin. İkisi arasında geçiş yapmak için soldaki anahtara dokunun.

## Yöntem {#method}
Ayna ya `Yerel` olabilir ve nesneyle birlikte hareket eder ya da `Dünya` olabilir ve yerinde kalır. Hangi moda ihtiyacınız olduğundan emin değilseniz, nesnenin üzerinde gösterilen ayna düzlemi ve radyal göstergelere bakın. Yerel modda, dönüştürme araçlarını (`Gizmo` veya `Dönüştür`) kullanıp modeli taşırsanız ayna göstergeleri de onunla birlikte hareket eder. Dünya modunda ise ayna göstergeleri sabit kalır ve nesne onların içinden kayarak geçer.

## Ayna {#mirroring}
![](/images/symmetry_mirroring.webp)

Simetri düzlemlerinin yakınında şekillendirirken bazı fırçalar kusurlu bir simetri davranışı gösterebilir. Bu bölüm, heykelinizin bir tarafını diğerine kopyalayarak simetriyi geri getirmenizi sağlar.

`Yön` - `Ayna` başlığının yanındaki iki ok düğmesi, hangi tarafın diğerine kopyalanacağını belirler. Nomad bunu mevcut görüş açınıza göre hesaplar; böylece modele hangi yönden bakarsanız bakın, taraf ekranda aynı kalır.

![](/icons/shield.webp) `Maske` - Maske düğmesi, neyin aynalanacağını ayırmanızı sağlar; hedef taraftaki maske o bölgeyi korur, kaynak taraftaki maske ise o alanın hedefe aynalanmasını engeller.

![](/icons/tool_hide.webp) `Gizle` - Etkin olduğunda, kaynak tarafta gizlenmiş alanlar hedefe aynalanmaz.

`Ayna` (Topolojiyi koru), aynanın iki tarafında topolojinin aynı olup olmadığını anlamaya çalışır; aynıysa yalnızca verteksleri taşır. En yaygın durum budur. Radyal simetri göz ardı edilir. Topoloji simetrik değilse, Nomad aynalamayı bunun yerine `Kes • Ayna` ile zorlamayı önerir.

`Kes` düğmeleri nesneyi simetri düzlemi (veya düzlemleri) boyunca keser. Topolojiyi değiştirdikleri için `Ayna` seçeneğinden daha yıkıcıdırlar. Her düğmenin üzerindeki sayı, kaç nesne elde edeceğinizi gösterir:

* `Kes` - nesnenin bir tarafını kaldırır.
* `Kes • Ayna` - nesneyi keser, bir tarafı kopyalar, diğer tarafa aynalar ve ayna boyunca verteksleri birbirine kaynatır. Model aynanın iki tarafında çok farklıysa bazen bu yöntem gerekir.
* `Kes • Ayır` - nesneyi keser ve her tarafı ayrı bir nesne olarak tutar.
* `Kes • Ayna • Ayır` - `Kes • Ayna` gibidir, ama her taraf ayrı bir nesne olur.

Birden fazla nesne seçiliyse, `Ayna` ve [Nesneyi ters çevir](#flip-object) hepsine uygulanır.

### Nesneyi ters çevir {#flip-object}
![](/images/symmetry_flip.webp)
Sol tarafı sağ tarafa, sağ tarafı da sol tarafa çevirir; `X`, `Y` veya `Z` boyunca. Görünüş olarak, gizmo aracının menüsünde X ölçeğini -1 yapmaya benzer.

## Sıfırla ve Düzenle {#reset-and-edit}

![](/images/symmetry_edit.webp)

Simetrinin konumunu ve yönelimini düzenlemek mümkündür (ama önerilmez!). Gerekirse `Dünya merkezi` (yerel modda `Nesne merkezi`) ve `Yönelim`, simetrinin konumunu ve yönelimini varsayılan değerlerine sıfırlar.

Nomad simetri düzlemini nereye koyacağını genellikle bilir. Bunu elle ayarlamanız önerilmez, ama `Gizmo düzenleme` düğmesi ileri düzey kullanıcılara bu imkânı verir. Bu düğmeye tıklandığında, simetri düzlemini taşımanızı ve döndürmenizi sağlayan bir gizmo görünür. Varsayılan merkezi ve yönelimi geri getirmek isterseniz yukarıdaki sıfırlama düğmelerini kullanın.

`Pivottan`, simetri düzlemini [Gizmo](tools.md#gizmo) aracının pivot noktasına yerleştirir. Yalnızca `Gizmo` aracı etkinken kullanılabilir.

Bu seçeneklerin davranışı, içinde bulunduğunuz uzaya (*Yerel/Dünya*) göre değişir.
Yani beklediğiniz gibi çalışmıyorsa, doğru uzayda olup olmadığınızı mutlaka kontrol edin.

::: tip
Simetri düzlemini gizmo ile düzenlemek biraz deneyseldir, muhtemelen buna hiç ihtiyacınız olmaz!
:::

## Gösterim seçenekleri {#show-options}
![](/images/symmetry_show.webp)


`Çizgiyi göster` ve `Düzlemi göster`, simetri konumlarını gösteren bir görüntü alanı katmanını açıp kapatır. Bu seçenekleri kapatmanın ancak simetri menüsü kapandığında etkili olacağını unutmayın.
