# ![](/icons/transform.webp) Transformasi {#transform}

Menu ini menunjukkan transformasi objek yang dipilih dalam bentuk nombor: di mana ia berada, bagaimana ia diputar dan diskalakan, dan berapa besar ia. Taip nilai yang tepat, tetapkan semula, atau bake nilai itu ke dalam mesh.

![](/images/transform_overview.webp)

## Gambaran keseluruhan {#overview}

Setiap objek mempunyai nod yang menyimpan anjakan, putaran dan skalanya (matriksnya), selain verteksnya. Alat [Gizmo](tools.md#gizmo) dan [Transformasi](tools.md#transform) mengubah matriks itu apabila anda menyeret dalam paparan; menu ini membolehkan anda membacanya dan menaip nilainya. Lihat [Nod dan verteks](tools.md#nodes-and-vertices) untuk perbezaan antara menggerakkan nod dan menggerakkan verteks.

Seret sesuatu nilai ke kiri atau ke kanan untuk mengubahnya, atau ketuk untuk menaip nombor. Nilai X, Y dan Z diwarnakan merah, hijau dan biru, sama seperti paksi gizmo.

::: tip
Menaip nilai memudahkan anda meletakkan objek dengan tepat, contohnya untuk meletakkan beberapa bahagian pada ketinggian yang betul-betul sama, atau untuk mengembalikan putaran kepada nombor bulat selepas memutar bebas dengan gizmo.
:::

## Matriks {#matrix}

Tajuk memberitahu anda dalam ruang mana nilai dinyatakan: `Tempatan` (relatif kepada objek induk) atau `Dunia`.

### Objek dan Paksi {#object-pivot}

* `Objek` - Nilai ialah transformasi objek itu sendiri.
* `Paksi` - Nilai menggerakkan pilihan dari [paksinya](tools.md#pivot), sama seperti pemegang gizmo: baris menunjukkan sifar, dan mengubahnya akan menggerakkan, memutar atau menskalakan pilihan di sekeliling paksi. Hidupkan `Sunting` (ikon kunci) untuk menggerakkan paksi sahaja, manakala objek kekal di tempatnya.

### Tempatan dan Dunia {#local-world}

Apabila objek mempunyai induk atau anak, atau beberapa objek dipilih, anda boleh memilih ruang untuk memaparkan nilai: `Tempatan` (relatif kepada induk) atau `Dunia`.

### Tindakan {#actions}

| Tindakan          | Ikon                          | Penerangan |
| :---------------: | :---------------------------: | :--------- |
| Pindah ke asalan  | ![](/icons/target.webp)      | Memindahkan objek ke asalan dunia. |
| Bake              | ![](/icons/bake.webp)        | Menggunakan matriks pada verteks dan menetapkan semula matriks. Dari segi visual, tiada apa yang berubah, tetapi asalan objek kini ialah asalan dunia. |
| Paksi             | ![](/icons/gizmo.webp)       | Bake paksi ke dalam objek: asalan dan orientasi objek menjadi sama seperti paksi. Dari segi visual, tiada apa yang berubah. |
| Sunting           | ![](/icons/lock.webp)        | (Mod `Paksi`) Menggerakkan paksi sahaja. |
| Tetapkan semula   | ![](/icons/reset.webp)       | Menetapkan semula transformasi kepada identiti. Dalam mod `Paksi`, ia mengembalikan paksi ke tempatnya. |

Apabila objek yang dipilih mempunyai instans, bake akan meminta pengesahan, dengan pilihan `Batalkan instans`: bake mengubah verteks, yang dikongsi oleh instans.

### Anjakan, Putaran, Skala {#translation-rotation-scale}

Kedudukan, putaran (dalam darjah) dan skala objek, pada X, Y dan Z. Dua butang di hujung setiap baris hanya bake bahagian transformasi itu ke dalam verteks, atau menetapkannya semula.

Baris `Serong` juga muncul apabila objek diserongkan, contohnya selepas skala tidak seragam pada induk yang diputar.

### Skala seragam {#uniform-scale}

Apabila didayakan, skala ialah satu nilai sahaja, sama pada ketiga-tiga paksi. Nyahdayakannya untuk menskalakan X, Y dan Z secara berasingan.

## Dimensi {#dimension}

Saiz dan pusat kotak sempadan pilihan, dalam unit dunia. Apabila beberapa objek dipilih, ia merangkumi kesemuanya.

* `Saiz` - Lebar, tinggi dan kedalaman. Apabila butang pautan dihidupkan, mengubah satu saiz akan menskalakan dua yang lain dengan kadar yang sama, mengekalkan perkadaran.
* `Tengah` - Pusat kotak sempadan. Butang sasaran menggerakkan pilihan supaya pusatnya berada di asalan dunia.

::: tip
`Saiz` ialah cara paling pantas untuk memberikan saiz dunia sebenar kepada objek, contohnya sebelum cetakan 3d: tetapkan ketinggian yang anda mahu dan pautan akan mengekalkan perkadaran.
:::
