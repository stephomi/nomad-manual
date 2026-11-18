# ![](/icons/material.webp) Material {#material}

Menu ini memungkinkan Anda mengubah material objek saat ini, properti render objek/material, dan menetapkan tekstur ke material.

![](/images/material_overview.webp)

Material menentukan bagaimana tampilan sebuah objek, dengan mengatur bagaimana objek bereaksi terhadap cahaya dan objek lain. Tampilan objek diatur oleh properti-properti berikut:

* `Jenis material`
* `Warna`
* `Kekasaran`
* `Kemetalan`
* `Opasitas`
* `Reflektansi`
* `Emisif/tanpa pencahayaan`

Kombinasi properti ini bisa menghasilkan beragam hasil, mulai dari yang fotorealistis, bergaya kartun, hingga eksperimental.

Warna, kekasaran, kemetalan, dan opasitas bisa dicat, lihat [opsi Lukis Verteks](painting.md) untuk informasi lebih lanjut.

Jenis material, reflektansi, dan emisif/tanpa pencahayaan adalah properti material yang dijelaskan di bawah.

Tombol `Salin` dan `Tempel` di bagian atas menu ini memungkinkan Anda menyalin material dari satu objek ke objek lain.

Perhatikan bahwa renderer Nomad adalah renderer realtime; meskipun andal, renderer ini lebih mengutamakan kecepatan daripada akurasi untuk efek-efek tertentu. 

## Jenis material {#material-types}

![](/images/material_types.webp)

Jenis material di Nomad adalah Opak, Subpermukaan, Pencampuran, Tambah, Pembiasan, Dithering, dan Penangkap bayangan.

### ![](/icons/material_opaque.webp) Opak {#opaque}
Mode bawaan yang memperlakukan permukaan sebagai material sederhana yang mendukung warna, kekasaran, kemetalan, dan opasitas yang dicat. Opasitas yang dicat, tekstur opasitas, atau kanal alpha dari tekstur warna tetap membuat objek tembus pandang, dengan memakai dithering. Hanya penggeser opasitas utama yang diabaikan.

### ![](/icons/material_subsurface.webp) Subpermukaan {#subsurface}
Mode ini bisa menyimulasikan material yang membuat cahaya terbaur dan tersebar di dalamnya, seperti kulit, lilin, atau giok.

Mode ini memerlukan mode shading PBR. Untuk hasil terbaik, gunakan setidaknya satu lampu directional atau spot, idealnya dengan lingkungan yang redup.

Kotak warna menentukan warna cahaya yang tersebar.

`Kedalaman` mengatur seberapa jauh cahaya tersebar dari depan, ke bawah permukaan, lalu keluar lagi dari permukaan depan. Efeknya melembutkan bayangan yang keras dan mengaburkan detail permukaan.

`Translusensi` mengatur bagaimana cahaya tersebar dari depan ke belakang sebuah bentuk, seperti cahaya yang menembus bagian bawah daun, atau telinga yang disinari kuat dari belakang. Anda memerlukan lampu yang menghasilkan bayangan untuk melihatnya.

### ![](/icons/material_blending.webp) Pencampuran {#blending}

Mirip dengan Opak, tetapi mendukung penggeser opasitas sehingga material bisa bercampur antara padat dan transparan. Ini hanya satu penggeser opasitas sederhana, berbeda dengan opasitas yang bisa dicat pada material opak. 

::: warning
Mode pencampuran bisa menyebabkan kedipan dan bagian yang tiba-tiba muncul-hilang pada bentuk yang kompleks atau saling berpotongan.
:::

### ![](/icons/material_additive.webp) Tambah {#additive}
Dengan material ini Anda bisa membuat mesh semi-transparan. Mirip dengan material pencampuran, tetapi jika pencampuran akan berbaur dengan sekitarnya, material tambah akan selalu lebih terang daripada objek di belakangnya, cocok untuk efek terang seperti berkas cahaya, api, atau ledakan.

Anda bisa mengatur nilai opasitas lebih dari 1, yang berarti objek akan menjadi lebih terang.  
Ini berguna jika Anda ingin memakai [kembang](postprocess.md#bloom) dan `parameter ambang batas` agar hanya objek ini yang berpendar seperti objek emisif.

Mode ini cenderung menghasilkan lebih sedikit artefak daripada [Pencampuran](#blending) (transparansi yang tidak bergantung pada urutan).

### ![](/icons/material_refraction.webp) Pembiasan {#refraction}
Mode ini bisa dipakai untuk menyimulasikan material kaca. Mode ini memerlukan mode shading PBR. Karena keterbatasan realtime, pembiasan pada dirinya sendiri dan pembiasan berlapis agak terbatas.

Pengecatan kekasaran pada model memengaruhi seberapa buram pembiasannya.
Secara bawaan, setiap objek yang dibuat di Nomad memiliki kekasaran sekitar 25%, sehingga pembiasannya tidak sempurna melainkan agak buram.
Anda bisa memakai tombol `Mengecat berkilau` untuk mengecat ulang model dengan kekasaran dan kemetalan 0 (warnanya tidak akan terpengaruh).

Ada 2 kekasaran yang berperan: yang satu menentukan seberapa buram pantulan di permukaan, yang lain menentukan bagian dalam (pembiasan).  
Namun, karena Nomad hanya memiliki satu kanal kekasaran cat, kekasaran bagian dalam dan luar akan berbagi nilai yang sama.  
Agar nilainya bisa berbeda (misalnya permen lolipop dengan permukaan tajam tetapi bagian dalam buram), gunakan penggeser `Permukaan` dan `Bagian Dalam` di bawah `Timpa kekasaran` untuk menimpa kekasaran yang dicat.

![](/videos/refraction.mp4)

#### Indeks Pembiasan {#index-of-refraction}
Seberapa besar cahaya dibelokkan saat memasuki objek. Nilai yang lebih tinggi membelokkannya lebih kuat, seperti lensa yang tebal.

#### Penyerapan {#absorption}
Menyimulasikan cahaya yang diserap saat melewati volume, diwarnai oleh kotak warna, dengan `Faktor` yang mengatur kekuatannya. Bagian yang tipis lebih terang karena meneruskan lebih banyak cahaya, sedangkan area yang tebal lebih gelap. Yang dipakai hanyalah perkiraan ketebalan objek, jadi efeknya sangat bergantung pada bentuknya.


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Membuat objek semi-transparan dengan membuang sebagian piksel secara acak.

### ![](/icons/material_shadow_catcher.webp) Penangkap bayangan {#shadow-catcher}

Membuat objek tidak terlihat, dan hanya menerima bayangan dari lampu. Berguna untuk menggabungkan hasil render Nomad dengan gambar lain, biasanya pada sebuah bidang datar. Kotak warna menentukan warna bayangan.

Harus ada lampu yang menghasilkan bayangan di adegan; jika tidak, penangkap bayangan tidak melakukan apa-apa. Tombol `Kemetalan → 0%` dan `Kemetalan → 100%` mengecat ulang objek: jika sepenuhnya metalik, penangkap bayangan juga bisa memantulkan adegan saat pemrosesan pasca [Refleksi (SSR)](postprocess.md#reflection-ssr) diaktifkan.

::: tip

Informasi lebih lanjut tentang transparansi dan mode pencampuran bisa ditemukan di https://support.fab.com/s/article/Transparency-Opacity

:::

## Kontrol {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Selalu tidak berlampu {#always-unlit}
Jika diaktifkan, objek akan mengabaikan PBR dan MatCap, dan hanya menampilkan cat warnanya tanpa shading.
Perhatikan bahwa jika Anda memakai [Tambah](#additive), Anda bisa langsung mengecat transparansi dengan warna hitam.

### Opasitas {#opacity}
Seberapa padat atau buram sebuah objek terlihat; 100% berarti padat, 0% berarti transparan. Penggeser ini ditampilkan untuk jenis Pencampuran, Tambah, Dithering, dan Penangkap bayangan. Anda juga bisa mengecat opasitas untuk kendali yang lebih halus.

### Pass pra-refraksi {#pre-refract-pass}
Hanya untuk Pencampuran dan Tambah. Menggambar objek transparan ini sebelum pass pembiasan. Berguna jika objek pembias berada di depan permukaan transparan lainnya.

### Reflektansi {#reflectance}
Mengatur jumlah pantulan yang diterima material non-metalik. Hampir selalu nilai bawaannya yang sebaiknya dipakai (sesuai dengan standar 4% cahaya yang dipantulkan pada sudut tegak lurus), tetapi bisa dinaikkan untuk memperkuat pantulan dan kilauan di mata karakter, misalnya. Ini memerlukan mode shading PBR.

### ![](/icons/culling.webp) Pembalikan pemangkasan {#inverse-culling}
Membalik normal sebuah permukaan. Biasanya tidak diperlukan, tetapi bisa dipakai jika model tampak terbalik luar-dalam, atau jika dipadukan dengan `Dua sisi` yang dinonaktifkan, bisa dipakai untuk membuat interior yang dinding terdekatnya dengan kamera selalu tersembunyi.

Opsi-opsi berikut bisa diatur ke `Otomatis`, `Tidak` atau `Ya`. Dengan `Otomatis`, panah menunjukkan nilai yang benar-benar dipakai.

### ![](/icons/sphere_smooth.webp) Shading halus {#smooth-shading}
Lihat [opsi global](settings.md#smooth-shading).  
Nilai `Otomatis` akan memakai opsi global.

### ![](/icons/culling.webp) Dua sisi {#two-sided}
Face akan terlihat dari kedua sisi. Lihat [opsi global](settings.md#two-sided-quick).  
Nilai `Otomatis` akan memakai opsi global.

### ![](/icons/culling.webp) Bagian belakang berwarna {#coloured-backface}
Lihat [opsi global](settings.md#two-sided-quick).
Nilai `Otomatis` akan memakai opsi global.

### ![](/icons/shadow_cast.webp) Hasilkan bayangan {#casts-shadows}
Objek transparan juga menghasilkan bayangan (dengan pola dithering untuk meniru bayangan yang tercampur).  
Pastikan untuk menonaktifkan bayangan jika ada objek besar di adegan Anda yang tidak perlu menghasilkan bayangan (misalnya lantai yang besar).

### ![](/icons/shadow_receive.webp) Terima bayangan {#recieve-shadows}
Apakah bayangan dari objek lain digambar pada objek ini.

### ![](/icons/wireframe.webp) Kerangka kawat {#wireframe}
Lihat [opsi global](settings.md#wireframe).  
Nilai `Otomatis` akan memakai opsi global.

### ![](/icons/trash.webp) Setel ulang normal {#reset-normals}
Hanya ditampilkan jika objek yang diimpor membawa normalnya sendiri (misalnya dengan `Pertahankan topologi`). Tombol ini menghapusnya, sehingga shading memakai normal yang dihitung dari permukaan.


## Tekstur {#textures}

![](/images/material_textures.webp)

Jika sebuah objek memiliki UV, tekstur bisa diterapkan ke material, sebagai tambahan atas warna/kekasaran/kemetalan/opasitas verteks. Biasanya tekstur ini adalah hasil bake tekstur, tetapi gambar yang dibuat di luar Nomad juga bisa dipakai. `UV:✓` atau `UV:✗` di sebelah judul memberi tahu Anda apakah objek memiliki UV.

Tekstur bisa diterapkan ke

* Warna
* Normal
* Kekasaran
* Kemetalan
* Opasitas
* Perpindahan
* Emisif

Baris `Oklusi` juga muncul jika objek yang diimpor memiliki tekstur oklusi, tetapi Nomad tidak memakainya.

Penggeser di setiap baris mengatur seberapa kuat teksturnya diterapkan, dari tidak sama sekali hingga penuh. `Warna` dan `Emisif` juga memiliki kotak warna yang mewarnai tekstur, dan `Emisif` mengatur kekuatan pendarannya.

`Perpindahan` mengatur seberapa jauh peta perpindahan mendorong permukaan. Tombol `Terapkan`-nya memindahkan verteks sesuai perpindahan, lalu menghapus petanya. Hasilnya masuk ke lapisan aktif.

Tombol palet di sebelah judul membuka preset material dari menu [lukis](painting.md): ketuk salah satunya untuk menyalin teksturnya ke objek. Di desktop, gambar yang diimpor akan disinkronkan dengan file aslinya saat Anda kembali ke Nomad, dan tombol sinkronisasi di sebelah judul akan memuat ulang gambar-gambar tersebut.

Mengklik slot tekstur akan memunculkan pemilih. Setelah tekstur ditetapkan ke slot material, mengklik lagi akan memunculkan panel tekstur:

### Opsi panel tekstur {#texture-panel-options}

![](/images/material_texture_panel.webp)

Panel ini menampilkan ukuran gambar dan pratinjau teksturnya.

### ![](/icons/open.webp) Buka {#open}
Memilih tekstur lain. Di desktop, `Jelajahi` menampilkan file gambar di penjelajah file Anda.

### ![](/icons/circle_cross.webp) Tidak ada {#none}
Menghapus tekstur

### Opasitas {#texture-opacity}

Hanya untuk tekstur warna. Jika gambar memiliki kanal alpha, opsi ini memungkinkan Anda memakainya untuk Opasitas, atau mengabaikannya.

### Format {#normal-format}
Hanya untuk tekstur normal. Peta normal hadir dalam dua jenis, `OpenGL (+Y)` dan `DirectX (-Y)`. Jika detailnya tampak terbalik, coba jenis yang lain.

### Tinggi {#displacement-height}
Hanya untuk tekstur perpindahan.
* `Lokal` - Tingginya membesar dan mengecil mengikuti skala objek.
* `Dunia` - Tingginya tetap sama berapa pun skala objek.

### Multiply {#multiply}
Hanya untuk tekstur kekasaran, kemetalan, dan opasitas. Mengalikan nilai-nilai tekstur. Jika tidak bernilai 100%, nilainya ditampilkan pada slot tekstur.

### ![](/icons/link.webp) Ikon rantai/tautan {#chainlink-icon}

Ikon tautan di bagian-bagian berikut, jika diaktifkan, berarti opsi apa pun yang dipakai akan dibagikan dengan tekstur lain (warna, normal, kekasaran, kemetalan, opasitas, emisif) yang ikon tautannya juga aktif. 

Dengan begitu, tekstur-tekstur yang sudah sejajar akan tetap sejajar meskipun Anda mengubah parameter atau jenis proyeksi.


### Proyeksi {#projection}
![](/images/material_projection.webp)

Menentukan bagaimana tekstur diterapkan ke objek.

* `Otomatis` - UV jika objek memiliki UV, jika tidak, Triplanar
* `UV` - Memakai koordinat UV mesh untuk menerapkan tekstur. Jika mesh dan tekstur berasal dari luar Nomad, atau akan diekspor dari Nomad untuk dipakai di tempat lain, UV adalah opsi yang tepat.
* `Triplanar` - Memproyeksikan tekstur di sepanjang sumbu X, Y, Z, dan memadukan sambungannya. 

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Proyeksi triplanar adalah cara yang andal namun sederhana untuk menerapkan tekstur ke objek.

Triplanar seperti memiliki 6 proyektor video dengan gambar yang sama, yang menyorot ke bagian depan, belakang, kiri, kanan, atas, dan bawah objek Anda.

Hasilnya kemudian bisa di-bake ke UV atau warna verteks jika diperlukan.


![](/images/material_triplanar_example.webp)

#### Metode {#method}

* `Lokal` - Proyeksi akan bergerak mengikuti transformasi objek
* `Dunia` - Proyeksi tetap diam; memindahkan objek akan membuatnya bergeser melewati proyeksi.

#### Kekerasan {#hardness}

Bagaimana proyeksi-proyeksi bercampur. 100% berarti tidak ada pencampuran, dan tepi proyeksi akan tajam. 0% akan memadukan tepinya dalam sudut yang lebar. Nilai bawaannya 90%, cukup untuk menyamarkan tepi sambil membiarkan bagian proyeksi lainnya tetap tajam.

### Seragam {#uniform}

Jika dicentang, kekerasan yang sama dipakai untuk semua proyeksi. Jika tidak dicentang, kontrol kekerasan tambahan muncul untuk proyeksi X, Y, Z.


### Parameter {#parameter}
![](/images/material_parameter.webp)

#### Penyaringan {#filtering}
Metode penyaringan tekstur yang dipakai; `Otomatis` adalah bawaannya, metodenya adalah `Terdekat`, `Linear`, `Mipmap`. Terdekat tidak melakukan penyaringan, sehingga tekstur bisa tampak bergerigi jika dilihat dari dekat. Linear dan Mipmap menyaring dengan lebih baik, sehingga tekstur tampak buram alih-alih bergerigi jika dilihat dari dekat.

#### Ubin - X {#tiling-x}
Jika parameter Skala lebih dari 1, sehingga tekstur lebih kecil daripada UV objek, ini menentukan bagaimana tekstur diubinkan di sepanjang sumbu X. `Tidak ada` berarti tanpa pengulangan. `Ulangi` membuat salinan tekstur. `Cermin` membuat salinan tekstur dengan setiap salinan kedua dibalik, yang bisa membantu menyamarkan artefak pengubinan.

#### Ubin - Y {#tiling-y}
Sama seperti Ubin - X, tetapi untuk sumbu Y.

### Transformasi {#transform}
![](/images/material_transform.webp)

Transformasi 2d tambahan yang diterapkan ke tekstur di ruang UV. Tombol atur ulang mengembalikan nilai bawaan; ikon rantai (saat tekstur selain warna dipilih) akan menautkan atau melepas tautan transformasi agar sama dengan tekstur warna.

#### Translasi {#translation}
Ofset X dan Y tekstur

#### Rotasi {#rotation}
Rotasi tekstur

#### Skala {#scale}
Skala tekstur; angka yang lebih besar membuat tekstur lebih kecil pada objek. Gunakan opsi Ubin - X dan Ubin - Y untuk mengatur apa yang terjadi.

### Skala Uniform {#uniform-scale}
Jika dinonaktifkan, Nomad akan menampilkan kontrol terpisah untuk Skala-X dan Skala-Y.
