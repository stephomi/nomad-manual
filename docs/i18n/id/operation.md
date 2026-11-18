# ![](/icons/operation.webp) Operasi {#operation}

Menu ini menerapkan sebuah operasi ke seluruh permukaan objek yang dipilih sekaligus: menghaluskan, merilekskan, memoles, menggembungkan, menyesuaikan warna, serta mengaburkan atau mempertajam cat dan topeng.

![](/images/operation_overview.webp)

## Ikhtisar {#overview}

Kalau kuas bekerja di tempat Anda menggoreskannya, operasi bekerja pada setiap verteks objek yang dipilih dalam satu kali jalan. Judulnya menampilkan nama objek, atau jumlah objek jika beberapa objek dipilih.

Setiap operasi berupa penggeser: seret ke kanan untuk menerapkan lebih banyak, ke kiri untuk menerapkan lebih sedikit (atau operasi kebalikannya, untuk penggeser yang memiliki panah di kedua sisinya). Penggeser kembali ke nol begitu Anda melepasnya, dan setiap seretan dihitung sebagai satu langkah di [Riwayat](history.md), jadi Anda bisa menerapkan operasi beberapa kali dalam dosis kecil.

::: tip
Operasi adalah cara cepat untuk merapikan seluruh mesh setelah remesh voxel atau boolean: sedikit `Santai` meratakan segitiga-segitiganya, sedikit `Haluskan` menghilangkan noise, tanpa perlu memburu setiap titik dengan kuas.
:::

## Filter {#filters}

Tombol-tombol di bagian atas membatasi di mana operasi diterapkan:

* `Topeng` - Area yang ditopeng tidak tersentuh.
* `Sembunyi` - Area yang disembunyikan tidak tersentuh.
* `Ofset` - (Saat sebuah [lapisan](layers.md) dipilih) Hanya area tempat lapisan aktif menyimpan pahatan yang terpengaruh, jadi Anda bisa menghaluskan atau menggembungkan isi sebuah lapisan tanpa menyentuh bagian lainnya.

## Penghalusan {#smoothing}

* `Pertahankan volume` - Menghaluskan tanpa menyusutkan permukaan. Tombol roda gigi menyimpan nilai `Menyusut` dan `Kembung` yang dipakai untuk itu.
* `Pertahankan batas` - Verteks di batas mesh (tepi sebuah lubang) tetap diam.
* `Pelembutan stabil` - Berusaha membuat penghalusan tidak bergantung pada topologi. Paling efektif ketika kepadatan poligon sangat bervariasi.
* `Haluskan` - Menghaluskan permukaan. Seret ke kiri untuk `Mempertajam` permukaan.
* ![](/icons/group.webp) `Haluskan` - Menghaluskan batas antar [grup face](tools.md#facegroup), meluruskan garis tepi grup yang bergerigi. Seret ke kiri untuk mempertajamnya.
* `Santai` - Meratakan poligon sambil mempertahankan bentuknya.
* ![](/icons/group.webp) `Santai` - Merilekskan poligon di sepanjang batas grup face.
* `Pertahankan pojok` - Dengan `Haluskan` dan `Santai` grup face, batas tetap diam di tempat yang berbelok lebih dari sudut ini, sehingga pojoknya tetap tajam sementara sisi-sisinya dihaluskan. Aktifkan dengan kotak centangnya.

## Poles {#polish}

Meratakan permukaan menjadi bidang-bidang (facet) yang bersih, seperti alat [Poles](tools.md#polish). `Sudut` menentukan face mana yang diratakan bersama: face yang menekuk kurang dari sudut ini menjadi satu bidang. Sudut yang lebih kecil mempertahankan lebih banyak lipatan dan bidang yang lebih kecil.

## Kembung {#inflate}

Mendorong permukaan ke luar mengikuti normalnya, atau ke dalam jika Anda menyeret ke kiri. `Normal (Santai)` sekaligus merilekskan poligon agar tidak meregang; matikan dengan kotak centangnya.

## Penyesuaian warna {#color-adjustments}

Pilih kanal yang ingin disesuaikan, `Warna`, `Kekasaran`, `Kemetalan`, `Opasitas`, `Kepadatan` (pengecatan kepadatan [Quad Remesher](tools.md#quad-remesher), jika objek memilikinya) atau `Topeng`, lalu:

* `Eksposur` - Mencerahkan atau menggelapkan nilai.
* `Kejenuhan` - (Hanya `Warna`) Warna lebih atau kurang hidup.
* `Kontras` - Merenggangkan nilai-nilai, atau mendekatkannya satu sama lain.
* `Hue` - Menggeser warna di sepanjang roda warna.

## Buram {#blur}

Mengaburkan kanal yang dipilih di seluruh permukaan: aktifkan `Warna`, `Kekasaran`, `Kemetalan`, `Opasitas`, `Kepadatan` atau `Topeng`, lalu seret `Buram`. Seret ke kiri untuk `Mempertajam`.

Untuk topeng, ini sama dengan penggeser `Kabur` pada alat [Topeng](tools.md#mask). Di sini Anda juga bisa mengaburkan kanal cat.
