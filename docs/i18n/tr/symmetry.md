# ![](/icons/symmetry.webp) Simetri

Bu menü, fırça darbelerinin bir ayna düzlemi boyunca veya radyal olarak nasıl tekrar edileceğini ve simetrik olmayan nesnelerde simetrinin nasıl geri getirileceğini kontrol eder.

![](/images/symmetry_overview.webp) 

## Genel Bakış 
Simetriyi birkaç şekilde kullanabilirsiniz:

* Ayna olarak, çalışmayı X (sol/sağ), Y (üst/alt), Z (arka/ön) veya bunların kombinasyonları boyunca çevirmek için. 
* Radyal simetri X Y Z eksenlerinde, tekrar sayısı belirlenerek ayarlanabilir; örneğin bir denizyıldızı yontmak gibi. 
* Aynalar, orijin etrafında (dünya modu olarak adlandırılır) veya bir nesnenin merkezi etrafında (yerel mod olarak adlandırılır) çalışabilir.
* Başlangıçta simetrik olmayan yontular zorla simetrik hale getirilebilir.

Simetriyi açıp kapatmak için sol hızlı panelde (*"Sym"*) bir kısayol da bulunur. Küçük 'L/W', Nomad'ın Yerel (Local) mi yoksa Dünya (World) simetri modunda mı olduğunu gösterir. Ayrıca uzun basarak veya ekranın ortasına doğru kaydırarak bir menü açabilirsiniz.

![](/images/symmetry_button.webp) 

Bu küresel (global) bir seçenektir, bu nedenle durumu farklı araçlar arasında korunur.
Tek istisnalar, kendi simetri durumuna sahip olan dönüştürme araçlarıdır ([Taşı](#translate), [Döndür](#rotate), [Ölçekle](#scale) ve [Gizmo](#gizmo)).

::: tip
Simetri menüsü esas olarak darbe (stroke) simetrisini kontrol etmek içindir. Nesneleri ayrıca [sahne menüsünde bulunan tekrarlayıcılar](scene#repeaters) aracılığıyla da aynalayabilir ve çoğaltabilirsiniz. 
:::

## Etkin
Ayna modunu açıp kapatır, bu sol hızlı paneldeki `Sym` düğmesiyle aynıdır. 

## Düzlemler

Simetri düzlemlerini ve radyal simetri için tekrar sayısını etkinleştirin. Yalnızca tek bir düzlem seçmek zorunda olmadığınızı, karmaşık simetri için 1, 2 veya 3 düzlemin tamamını etkinleştirebileceğinizi unutmayın.

Radyal simetri için eksen ve tekrar sayısı. Bunların da tek bir eksenle sınırlı olmadığını ve ayrıntılı sonuçları çok hızlı üretmek için düzlem simetrisiyle bile birlikte çalışabileceğini unutmayın. (Toplam tekrar sayısı 150 ile sınırlıdır)

![](/videos/symmetry_demo.mp4) 

## Yöntem
Ayna, nesneyle birlikte hareket eden 'Yerel' olabilir veya hareket etmeyen 'Dünya' olabilir. Hangi moda ihtiyacınız olduğundan emin değilseniz, nesnenin üzerine bindirilen ayna düzlemini ve radyal göstergeleri gözlemleyin. Yerel moddayken, dönüştürme gizmosunu kullanıp modeli hareket ettirirseniz, ayna göstergeleri de hareket eder. Dünya modunda ise ayna göstergeleri sabit kalır ve nesne onların içinden kayar.

## Aynalama
![](/images/symmetry_mirroring.webp)

Simetri düzlemlerinin yakınında yontu yaparken, bazı fırçalar mükemmel olmayan simetri davranışına sahip olabilir. Bu bölüm, yontunuzun bir tarafını diğerine kopyalayarak simetriyi geri yüklemenizi sağlar. 


`Direction` - `<<` ve `>>` düğmeleri, hangi tarafın diğerine kopyalanacağını belirler. Nomad bunu mevcut görünümünüzden hesaplar, bu nedenle örneğin `<<` olarak ayarlamak, her zaman ekranda sağdan sola kopyalama yapar.

![](/icons/shield.webp) `Mask` - Maske düğmesi, neyin aynalanacağını yalıtmanıza olanak tanır; hedef tarafı maskelemek o bölgeyi korur, kaynak tarafı maskelemek ise o alanın hedefe aynalanmasını engeller. 

![](/icons/tool_hide.webp) `Hide` - Etkin olduğunda, kaynak tarafta gizlenmiş alanlar hedefe aynalanmaz. 

`Mirror`, topolojinin ayna düzleminin her iki tarafında da aynı olup olmadığını anlamaya çalışır ve eğer öyleyse yalnızca tepe noktalarını (vertex) taşır. Bu daha yaygın senaryodur.

`Split & Mirror`, temelde nesneyi ayna boyunca keser, bir tarafı kopyalar, diğer tarafa aynalar ve ayna boyunca tepe noktalarını birleştirir (weld). Daha yıkıcı bir seçenektir ve çok çözünürlüklü (multiresolution) veriyi siler, ancak model ayna boyunca çok farklıysa bazen bu yöntem gereklidir.

### Nesneyi çevir
![](/images/symmetry_flip.webp)
Sol tarafı sağ tarafa ve tam tersini yapar. Görünüş olarak, gizmo araç menüsünü kullanıp X ölçeğini -1 olarak ayarlamaya benzer.

## Sıfırla ve Düzenle

![](/images/symmetry_edit.webp)

Simetri konumunu ve yönelimini düzenlemek mümkündür (ancak önerilmez!). Gerekirse, `World center` ve `Orientation` simetri konumunu ve yönelimini varsayılan değerlerine sıfırlar.

Nomad genellikle simetri düzlemini nereye koyacağını bilir. Bunu elle ayarlamak önerilmez, ancak `Gizmo (Edit)` düğmesi gelişmiş kullanıcılar için buna izin verir. Bu düğmeye tıklandığında, simetri düzlemini taşımak ve döndürmek için bir gizmo gösterilir. Varsayılan merkezi ve yönelimi geri yüklemek isterseniz, `object center` ve `orientation` düğmeleri bunu yapar.

Bu seçeneklerin davranışı, içinde bulunduğunuz uzaya (*Local/World*) bağlı olarak değişecektir.
Bu nedenle beklediğiniz gibi çalışmıyorsa, doğru uzayda olup olmadığınızı kontrol ettiğinizden emin olun.

::: tip
`Gizmo (Edit)` düğmesi, muhtemelen bunu kullanmamanız gerektiğini hatırlatmak için özellikle gri renktedir!
:::

## Gösterme seçenekleri
![](/images/symmetry_show.webp)


`Show line` ve `Show plane`, simetri konumlarının görünüm (viewport) bindirmesini açıp kapatır. Bu seçenekleri kapatmanın yalnızca simetri menüsü kapatıldığında etkili olacağını unutmayın.
