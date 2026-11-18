# ![](/icons/transform.webp) Transformasi {#transform}

Menu ini menampilkan transformasi objek yang dipilih dalam bentuk angka: di mana posisinya, bagaimana rotasi dan skalanya, serta seberapa besar ukurannya. Ketik nilai yang tepat, atur ulang, atau bake ke dalam mesh.

![](/images/transform_overview.webp)

## Ikhtisar {#overview}

Setiap objek memiliki sebuah node yang menyimpan translasi, rotasi, dan skalanya (matriksnya), terpisah dari verteks-verteksnya. Alat [Gizmo](tools.md#gizmo) dan [Transformasi](tools.md#transform) mengubah matriks itu saat Anda menyeret di viewport; menu ini memungkinkan Anda membacanya dan mengetikkan nilainya. Lihat [Node dan verteks](tools.md#nodes-and-vertices) untuk memahami perbedaan antara memindahkan node dan memindahkan verteks.

Seret sebuah nilai ke kiri atau ke kanan untuk mengubahnya, atau ketuk untuk mengetikkan angka. Nilai X, Y, dan Z diberi warna merah, hijau, dan biru, seperti sumbu gizmo.

::: tip
Mengetik nilai sangat praktis untuk menempatkan objek dengan presisi, misalnya untuk meletakkan beberapa bagian pada ketinggian yang persis sama, atau untuk mengembalikan rotasi ke angka bulat setelah memutarnya bebas dengan gizmo.
:::

## Matriks {#matrix}

Judulnya memberi tahu Anda dalam ruang apa nilai-nilai itu dinyatakan: `lokal` (relatif terhadap objek induk) atau `dunia`.

### Objek dan Poros {#object-pivot}

* `Objek` - Nilainya adalah transformasi objek itu sendiri.
* `Poros` - Nilainya menggerakkan seleksi dari [poros](tools.md#pivot)-nya, sama seperti pegangan gizmo: baris-barisnya menunjukkan nol, dan mengubahnya akan memindahkan, memutar, atau menskalakan seleksi di sekitar poros. Aktifkan `Sunting` (ikon gembok) untuk memindahkan porosnya saja, sementara objek tetap diam.

### Lokal dan Dunia {#local-world}

Jika objek memiliki induk atau anak, atau jika beberapa objek dipilih, Anda bisa memilih dalam ruang apa nilainya ditampilkan: `Lokal` (relatif terhadap induk) atau `Dunia`.

### Tindakan {#actions}

| Tindakan      | Ikon                          | Deskripsi |
| :-----------: | :---------------------------: | :---------- |
| Pindahkan ke asal | ![](/icons/target.webp)  | Memindahkan objek ke titik asal dunia. |
| Bake          | ![](/icons/bake.webp)        | Menerapkan matriks ke verteks lalu mengatur ulang matriksnya. Secara visual tidak ada yang berubah, tetapi titik asal objek kini adalah titik asal dunia. |
| Poros         | ![](/icons/gizmo.webp)       | Mem-bake poros ke dalam objek: titik asal dan orientasi objek menjadi milik poros. Secara visual tidak ada yang berubah. |
| Sunting       | ![](/icons/lock.webp)        | (Mode `Poros`) Memindahkan porosnya saja. |
| Atur Ulang    | ![](/icons/reset.webp)       | Mengatur ulang transformasi ke identitas. Dalam mode `Poros`, tombol ini justru mengembalikan poros ke tempatnya. |

Jika objek yang dipilih memiliki instans, bake akan meminta konfirmasi, dengan opsi `Batalkan instans`: bake mengubah verteks, dan verteks itu dipakai bersama oleh semua instans.

### Translasi, Rotasi, Skala {#translation-rotation-scale}

Posisi, rotasi (dalam derajat), dan skala objek, pada X, Y, dan Z. Dua tombol di ujung setiap baris hanya mem-bake bagian transformasi itu ke dalam verteks, atau mengatur ulangnya.

Baris `Miring` juga muncul jika objeknya miring, misalnya setelah skala yang tidak seragam pada induk yang diputar.

### Skala Uniform {#uniform-scale}

Jika diaktifkan, skalanya berupa satu nilai, sama untuk ketiga sumbu. Matikan untuk menskalakan X, Y, dan Z secara terpisah.

## Dimensi {#dimension}

Ukuran dan titik tengah kotak pembatas seleksi, dalam satuan dunia. Jika beberapa objek dipilih, kotak ini mencakup semuanya.

* `Ukuran` - Lebar, tinggi, dan kedalaman. Dengan tombol tautan aktif, mengubah satu ukuran akan menskalakan dua ukuran lainnya dengan besaran yang sama, sehingga proporsinya tetap.
* `Tengah` - Titik tengah kotak pembatas. Tombol target memindahkan seleksi sehingga titik tengahnya berada di titik asal dunia.

::: tip
`Ukuran` adalah cara tercepat untuk memberi objek ukuran dunia nyata, misalnya sebelum dicetak 3d: atur tinggi yang Anda inginkan dan tautannya akan menjaga proporsi.
:::
