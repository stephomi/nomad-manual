# ![](/icons/transform.webp) Dönüştür {#transform}

Bu menü, seçili nesnenin dönüşümünü sayılarla gösterir: nerede olduğunu, nasıl döndürülüp ölçeklendiğini ve ne kadar büyük olduğunu. Tam değerler yazabilir, onları sıfırlayabilir veya ağ örgüsüne pişirebilirsiniz.

![](/images/transform_overview.webp)

## Genel bakış {#overview}

Her nesnenin, verteks verilerinin yanında, ötelemesini, dönüşünü ve ölçeğini (matrisini) saklayan bir düğümü vardır. [Gizmo](tools.md#gizmo) ve [Dönüştür](tools.md#transform) araçları, görüntü alanında sürüklediğinizde bu matrisi değiştirir; bu menü ise onu okumanızı ve değerleri elle yazmanızı sağlar. Düğümü taşımakla verteksleri taşımak arasındaki fark için [Düğümler ve verteksler](tools.md#nodes-and-vertices) bölümüne bakın.

Bir değeri değiştirmek için sola veya sağa sürükleyin ya da bir sayı yazmak için üzerine dokunun. X, Y ve Z değerleri, gizmo eksenlerinde olduğu gibi kırmızı, yeşil ve maviye boyanmıştır.

::: tip
Değer yazmak, nesneleri hassas bir şekilde yerleştirmek için çok kullanışlıdır; örneğin birkaç parçayı tam olarak aynı yüksekliğe koymak ya da gizmo ile serbestçe döndürdükten sonra dönüşü yuvarlak bir sayıya geri getirmek için.
:::

## Matris {#matrix}

Başlık, değerlerin hangi uzayda ifade edildiğini söyler: `yerel` (üst nesneye göre) veya `dünya`.

### Nesne ve Eksen {#object-pivot}

* `Nesne` - Değerler, nesnenin kendi dönüşümüdür.
* `Eksen` - Değerler, seçimi gizmo tutamaklarıyla aynı şekilde [pivot noktasından](tools.md#pivot) yönetir: satırlar sıfır gösterir ve onları değiştirmek seçimi pivot noktası etrafında taşır, döndürür veya ölçeklendirir. Yalnızca pivot noktasını taşımak için `Düzenle` (kilit simgesi) seçeneğini açın; nesneler yerinde kalır.

### Yerel ve Dünya {#local-world}

Nesnenin bir üst nesnesi veya alt nesneleri varsa ya da birden fazla nesne seçiliyse, değerlerin hangi uzayda gösterileceğini seçebilirsiniz: `Yerel` (üst nesneye göre) veya `Dünya`.

### Eylemler {#actions}

| Eylem         | Simge                         | Açıklama |
| :-----------: | :---------------------------: | :---------- |
| Kökeni hareket ettir | ![](/icons/target.webp)      | Nesneyi dünya orijinine taşır. |
| Pişir          | ![](/icons/bake.webp)        | Matrisi verteksler üzerine uygular ve matrisi sıfırlar. Görsel olarak hiçbir şey değişmez, ama nesnenin orijini artık dünya orijinidir. |
| Eksen         | ![](/icons/gizmo.webp)       | Pivot noktasını nesneye pişirir: nesnenin orijini ve yönelimi, pivot noktasınınkiler olur. Görsel olarak hiçbir şey değişmez. |
| Düzenle          | ![](/icons/lock.webp)        | (`Eksen` modu) Yalnızca pivot noktasını taşır. |
| Sıfırla         | ![](/icons/reset.webp)       | Dönüşümü birim (identity) dönüşüme sıfırlar. `Eksen` modunda bunun yerine pivot noktasını eski yerine koyar. |

Seçili nesnenin örnekleri (instance) varsa, pişirme işlemi bir `Örneklemeyi kaldır` seçeneğiyle birlikte onay ister: pişirme, örneklerin paylaştığı verteksleri değiştirir.

### Öteleme, Döndürme, Ölçek {#translation-rotation-scale}

Nesnenin X, Y ve Z üzerindeki konumu, dönüşü (derece cinsinden) ve ölçeği. Her satırın sonundaki iki düğme, dönüşümün yalnızca o kısmını verteksler üzerine pişirir veya sıfırlar.

Nesne yatırılmışsa, örneğin döndürülmüş bir üst nesneye tek tip olmayan bir ölçek uygulandıktan sonra, bir `Yatır` satırı da görünür.

### Tek tip ölçeklendirme {#uniform-scale}

Etkinleştirildiğinde ölçek, üç eksende de aynı olan tek bir değerdir. X, Y ve Z'yi ayrı ayrı ölçeklendirmek için devre dışı bırakın.

## Boyut {#dimension}

Seçimin sınırlayıcı kutusunun dünya birimi cinsinden boyutu ve merkezi. Birden fazla nesne seçiliyse, kutu hepsini kapsar.

* `Büyüklük` - Genişlik, yükseklik ve derinlik. Bağlantı düğmesi açıkken bir boyutu değiştirmek diğer ikisini de aynı oranda ölçeklendirir ve oranlar korunur.
* `Ortalanmış` - Sınırlayıcı kutunun merkezi. Hedef düğmesi, seçimi merkezi dünya orijinine gelecek şekilde taşır.

::: tip
`Büyüklük`, bir nesneye gerçek dünyadaki boyutunu vermenin en hızlı yoludur; örneğin bir 3d baskı öncesinde: istediğiniz yüksekliği girin, bağlantı da oranları korusun.
:::
