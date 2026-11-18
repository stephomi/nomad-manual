# ![](/icons/toolbox.webp) Alat {#tools}

![](/images/tools_menu.webp)

::: tip
Langsung ke bagian [Alat](#tools-1) untuk penjelasan setiap alat.
:::

## Ikhtisar {#overview}

Alat dipilih dari `Kotak peralatan` di sebelah kanan, lalu dikendalikan dengan `Kontrol Alat` di sebelah kiri. Pengaturan tambahan ada di menu `Alat`, di menu kanan atas.

Alat kuas punya kontrol untuk ukuran dan intensitas. Alat seleksi punya kontrol untuk beberapa gaya seleksi. Bagian bawah kontrol alat berisi pintasan untuk operasi yang sering dipakai (Haluskan, Topeng, Sembunyi, Grup Face, Gizmo, Warna, Alpha).

Alat-alat Nomad diberi kode warna di kotak peralatan (matikan `Alat berwarna` di menu [Antarmuka](interface.md) untuk label polos):

* <span class=brush>**Alat kuas**</span> (Tanah Liat, Kuas, Haluskan, Lapisan, Kembung, HapusLapisan, Quad Remesher)
* <span class=move>**Alat pindah**</span> (Pindah, Tarik, Elastis, Dorongan)
* <span class=mask>**Alat topeng**</span> (Topeng)
* <span class=paint>**Alat lukis**</span> (Melukis, Smudge)
* <span class=flatten>**Alat perata**</span> (Datar, Planar, Poles)
* <span class=pinch>**Alat cubit**</span> (Alur tajam, Cubitan)
* <span class=stamp>**Alat cap**</span> (Cap, VDM)
* <span class=selection>**Alat berbasis seleksi**</span>, yang menggambar topeng 2d terlebih dahulu, lalu menjalankan sebuah operasi (Pangkas, Pisah, Proyeksi)
* <span class=creation>**Alat pembuat**</span> (Tabung, Bubut, Masukkan)
* <span class=transform>**Alat transformasi**</span> (Transformasi, Gizmo, Atur, Lattice)
* <span class=misc>**Alat lain-lain**</span> (Grup Face, Sembunyi)
* <span class=view>**Alat tampilan**</span> (Tampilan, Ukur, Pilih)



Banyak dari alat ini bisa disesuaikan dengan perilaku kuas, tekanan, tekstur, dan lainnya melalui menu [Goresan](stroke.md).


### Kontrol kuas {#brush-controls}

Bilah alat kiri berisi penggeser untuk jari-jari dan intensitas, lalu kontrol khusus sesuai kategori alat, yang dijelaskan di bawah.

![](/images/tool_left_panel.webp)

::: tip
Penggeser intensitas pada banyak alat bisa melewati 100%, layak untuk dicoba!
:::

### Mode sub {#sub-mode}
Tombol tepat di bawah penggeser intensitas adalah tombol `Kurang` (Sub). Label dan fungsinya berubah untuk setiap alat, dan saat ditekan akan menjalankan perilaku alternatif, biasanya kebalikannya. Misalnya, untuk [Melukis](#paint) tombol ini menjalankan mode hapus, untuk [Alur tajam](#crease) tombol ini membuat tepi yang menonjol, bukan alur, dan seterusnya.

Secara bawaan, tombol ini bekerja sebagai tombol lengket: Anda bisa menahannya untuk mengaktifkannya sementara, dan saat dilepas mode itu mati lagi. Jika Anda mengetuknya, mode sub akan aktif terus.

### Pintasan {#shortcuts}
Di bagian bawah bilah alat kiri terdapat pintasan untuk [Haluskan](#smooth), [Topeng](#mask), [Sembunyi](#hide), [Grup Face](#facegroup), [Gizmo](#gizmo), [Warna](painting.md#pbr-sliders), [Alpha](stroke.md#alpha).

Secara bawaan, semuanya bekerja sebagai tombol lengket: Anda bisa menahannya untuk mengaktifkannya sementara, dan saat dilepas mode itu mati lagi. Jika Anda mengetuknya, mode pintasan itu akan aktif terus.

### Kontrol seleksi {#selection-controls}

Alat [Topeng](#mask), [Melukis](#paint), [Pangkas](#trim), [Pisah](#split), [Proyeksi](#project), [Grup Face](#facegroup), [Sembunyi](#hide), dan [Pilih](#select) semuanya memakai kontrol serupa untuk menyeleksi area mesh.

![](/images/tools_shape_selector_panel.webp)

Ketuk tombol bentuk di bilah alat kiri (tombol ini menampilkan bentuk yang sedang aktif, `Tali` secara bawaan) untuk membuka popup berisi bentuk-bentuk. Untuk alat yang juga bisa bekerja dengan kuas (Topeng, Melukis, Grup Face, Sembunyi), popup yang sama juga memuat jenis goresan.

* `Tampilan` - Tanpa bentuk, alat tidak melakukan apa-apa, seperti mode kamera.
* `Tali` - Bentuk yang digambar bebas dengan tangan
* `Poligon` - Bentuk tertutup yang tersusun dari gabungan kurva dan/atau garis lurus. Lihat [Menyunting bentuk](#shape-editing) di bawah untuk info lebih lanjut.
* `Lengkung` - (Hanya Proyeksi) - Kurva bebas untuk proyeksi
* `Jalur` - (Hanya Proyeksi) - Kurva yang ditentukan oleh titik-titik. Lihat [Menyunting bentuk](#shape-editing) di bawah untuk info lebih lanjut.
* `Garis` - Seret sebuah garis untuk menentukan potongan bidang datar. Secara bawaan, operasi langsung dijalankan pada mesh; ubah opsi `Sunting` jika Anda tidak menginginkannya (tekan lama atau usap ikon garis).
* `Pita` - Jalur di antara dua pemandu sejajar, dengan gradien melintanginya. `Perpanjang` mempertahankan nilai penuh melewati pemandu terjauh alih-alih berhenti di batas pita, `Balik` menukar pemandu tempat gradien dimulai.
* `Rect` - Seret garis diagonal untuk menentukan sudut-sudut persegi panjang. Tekan lama atau usap untuk memunculkan opsi `Sunting`, `Persegi` untuk memaksa bentuk persegi, dan `Terpusat` agar klik pertama menjadi pusat persegi panjang.
* `Elips` - Seret garis diagonal untuk menentukan ukuran elips. Tekan lama atau usap untuk memunculkan opsi `Sunting`, `Lingkaran` untuk memaksa bentuk lingkaran, dan `Terpusat` agar klik pertama menjadi pusat elips.
* `Balik` - Membalik topeng bentuk, atau arah alat proyeksi.

Sebagian besar alat punya opsi `Sunting` yang menentukan apa yang terjadi setelah Anda selesai menggambar bentuk:
* `Edit: nonaktif` - Operasi langsung dijalankan begitu Anda melepas.
* `Edit: aktif` - Bentuk tetap bisa disunting. Sebuah tombol hijau muncul di samping bentuk untuk menjalankan operasi. Dengan begitu Anda bisa menyunting bentuk dan mengatur tampilan, lalu menekan tombol hijau saat sudah siap.
* `Edit: tahan` - Operasi dijalankan saat Anda melepas, kecuali Anda menahan di akhir goresan untuk terus menyunting bentuk.

### Menyunting bentuk {#shape-editing}
Penyuntingan poligon dan kurva bekerja dengan cara yang mirip:

* Untuk memulai, seret sebuah garis untuk menentukan 2 titik, lalu tarik dari tengah garis untuk membentuk poligon atau kurva.
* Klik titik-titik untuk beralih antara halus dan tajam.
* Klik dan seret bagian kurva atau garis untuk membuat titik baru.
* Untuk menghapus titik, seret titik ke titik tetangganya sampai berubah merah.
* Ikon tempat sampah di sudut ikon poligon atau jalur akan menghapus bentuk.

### Menu pengaturan {#settings-menu}

Banyak alat punya pengaturan tambahan yang ada di menu `Alat`, di menu kanan atas. Menu ini tampak abu-abu untuk alat yang tidak punya pengaturan tambahan.

![](/images/tools_settings_menu.webp)

## Alat {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)    <br> [Tanah Liat](#clay) | ![](/icons/tool_brush.webp)   <br> [Kuas](#brush)      | ![](/icons/tool_move.webp)       <br> [Pindah](#move)            | ![](/icons/tool_drag.webp)      <br> [Tarik](#drag)          | ![](/icons/tool_elastic.webp)   <br> [Elastis](#elastic)     | ![](/icons/tool_smooth.webp)  <br> [Haluskan](#smooth) |
| ![](/icons/tool_mask.webp)    <br> [Topeng](#mask)     | ![](/icons/tool_paint.webp)   <br> [Melukis](#paint)   | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp)   <br> [Datar](#flatten)       | ![](/icons/tool_planar.webp)    <br> [Planar](#planar)       | ![](/icons/tool_polish.webp)  <br> [Poles](#polish)    |
| ![](/icons/tool_crease.webp)  <br> [Alur tajam](#crease) | ![](/icons/tool_pinch.webp)   <br> [Cubitan](#pinch) | ![](/icons/tool_trim.webp)       <br> [Pangkas](#trim)           | ![](/icons/tool_split.webp)     <br> [Pisah](#split)         | ![](/icons/tool_project.webp)   <br> [Proyeksi](#project)    | ![](/icons/tool_layer.webp)   <br> [Lapisan](#layer)   |
| ![](/icons/tool_inflate.webp) <br> [Kembung](#inflate) | ![](/icons/tool_nudge.webp)   <br> [Dorongan](#nudge)  | ![](/icons/tool_stamp.webp)      <br> [Cap](#stamp)              | [VDM](#vdm)                                                  | ![](/icons/tool_clearLayer.webp) <br> [HapusLapisan](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tabung](#tube)     |
| ![](/icons/tool_lathe.webp)   <br> [Bubut](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Masukkan](#insert) | ![](/icons/tool_transform.webp)  <br> [Transformasi](#transform) | ![](/icons/tool_gizmo.webp)     <br> [Gizmo](#gizmo)         | ![](/icons/tool_faceGroup.webp) <br> [Grup Face](#facegroup) | ![](/icons/tool_hide.webp)    <br> [Sembunyi](#hide)   |
| ![](/icons/tool_measure.webp) <br> [Ukur](#measure)    | [Atur](#arrange)                                         | ![](/icons/tool_remesh.webp)     <br> [Quad Remesher](#quad-remesher) | ![](/icons/tool_select.webp)    <br> [Pilih](#select)        | ![](/icons/tool_lattice.webp)   <br> [Lattice](#lattice)     | ![](/icons/tool_view.webp)    <br> [Tampilan](#view)   |

------

### ![](/icons/tool_clay.webp) Tanah Liat {#clay}
Alat Tanah Liat berguna untuk membangun bentuk pahatan Anda. `Kurang` akan mengurangi material dari pahatan Anda.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Kuas {#brush}
Kuas standar. `Kurang` akan mengurangi material.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Pindah {#move}
Area di bawah kuas akan menempel pada kuas, sehingga menghasilkan deformasi elastis. Seleksi dipertahankan selama pemindahan, jadi jika Anda menggerakkan kuas menjauh lalu kembali ke titik awal, tidak akan ada deformasi.

Mode sub-nya adalah `Normal`, yang memindahkan area di bawah kuas mengikuti normal permukaan.

Kuas ini cocok untuk deformasi skala besar maupun deformasi kecil yang hati-hati.

#### Pengaturan Pindah {#move-settings}

* `Jari-jari (Latar belakang)` - Seberapa jauh dari tepi model Anda masih bisa memahat, berguna saat menggarap siluet objek. Hapus centangnya agar hanya mencengkeram jika Anda mulai di atas model.
* `Hanya verteks sisi yang sama` - Mengabaikan verteks yang menghadap ke arah berlawanan dengan deformasi.
* `Arah` - Dipakai oleh mode sub `Normal`, menentukan apakah seretan mendorong atau menarik permukaan:
    * `Otomatis` - Memilihkan salah satu dari dua metode di bawah untuk Anda, berdasarkan sudut normal permukaan.
    * `Normal 3D` - Membandingkan posisi penunjuk di layar dengan normal permukaan seperti terlihat dari kamera.
    * `XY` - Memakai posisi penunjuk di layar (atas/bawah, kiri/kanan) untuk menentukan dorong atau tarik.
    * `Ambang Batas` - Dengan `Otomatis`, batas sudut yang menentukan metode mana yang dipakai.
* `Kecepatan putar` - Anda bisa memuntir area yang dicengkeram sambil memindahkannya: putar dua jari, putar batang stylus Anda, atau tahan tombol pengubah (Alt, Ctrl, Shift, atau Cmd) sambil menyeret dengan mouse. Ada satu penggeser untuk masing-masing jari, stylus, dan mouse; hapus centang salah satunya untuk mematikan input itu.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Tarik {#drag}
Area di bawah kuas akan menempel pada kuas, sehingga menghasilkan deformasi elastis. Berbeda dengan kuas Pindah, seleksi terus diperbarui selama goresan, sehingga Anda bisa membuat objek yang panjang seperti ular, terutama saat Dynamic Topology diaktifkan.

Mode sub-nya adalah `Normal`, yang memindahkan area di bawah kuas mengikuti normal permukaan.

Kuas ini cocok untuk perubahan bentuk yang lebih longgar dan ekspresif.

#### Pengaturan Tarik {#drag-settings}

Tarik punya pengaturan yang sama dengan [Pindah](#move-settings): `Jari-jari (Latar belakang)`, `Hanya verteks sisi yang sama`, `Arah`, dan `Kecepatan putar`.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_elastic.webp) Elastis {#elastic}
Mencengkeram dan menarik permukaan seperti [Pindah](#move), tetapi dengan deformasi elastis: alih-alih berhenti di tepi kuas, tarikannya memudar perlahan seiring jarak di seluruh objek, mirip seperti meregangkan karet. Jari-jari kuas menentukan seberapa lebar tarikannya.

Mode sub-nya adalah `Normal`, yang memindahkan area di bawah kuas mengikuti normal permukaan.

Kuas ini cocok untuk perubahan proporsi yang besar dan lembut, dengan hasil yang tetap halus.

#### Pengaturan Elastis {#elastic-settings}

Elastis punya pengaturan yang sama dengan [Pindah](#move-settings), kecuali `Hanya verteks sisi yang sama`. `Jari-jari (Latar belakang)` nonaktif secara bawaan.

### ![](/icons/tool_smooth.webp) Haluskan {#smooth}
Menghaluskan area dengan merata-ratakan posisi titik. Alat ini sangat bergantung pada kepadatan poligon.
Jadi jika poligon Anda banyak, penghalusannya akan kurang efektif.

Mode sub-nya adalah `Santai`, yang hanya merapikan wireframe tetapi berusaha mempertahankan detail geometri.

#### Pengaturan Haluskan {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Grup Face {#smooth-facegroup}

* `Santai` - Menghaluskan batas grup face. Gunakan intensitas di atas 100% untuk menghaluskan batas dengan cepat. `Otomatis` hanya menghaluskan jika pratinjau grup face aktif, `Tidak` menonaktifkannya, `Ya` mengaktifkannya.

##### Verteks {#vertex}
* `Pertahankan volume` - Menghaluskan tanpa menyusutkan permukaan, sehingga penghalusan berulang tidak mengempiskan bentuk Anda. Tombol roda gigi di sebelahnya berisi nilai `Menyusut` dan `Kembung` yang dipakai untuk ini.
* `Pertahankan batas` - Pada mesh dengan tepi terbuka, misalnya bidang datar, sudut-sudutnya bisa ikut terhaluskan. Mengaktifkan opsi ini membuat verteks di batas mesh tetap diam.
* `Pelembutan stabil` - Berusaha membuat penghalusan tidak bergantung pada topologi. Paling baik bekerja pada kepadatan topologi yang bervariasi dan dengan nilai intensitas penghalusan yang tinggi.
* `Santai` - Sama dengan mode alternatif Santai di bilah alat kiri.

##### Pengecatan {#painting}
* `Melembutkan layar` - Gunakan opsi ini untuk mendapatkan penghalusan yang tidak bergantung pada topologi, bahkan pada jumlah poligon tinggi. `Otomatis`, `Tidak`, atau `Ya`.
* `Sampel layar` - Kualitas penghalusan; angka yang lebih tinggi lebih halus, tetapi lebih lambat.

::: tip
Kepadatan poligon yang lebih tinggi bisa membutuhkan intensitas di atas 100%. Nilai yang sangat tinggi (300%, 500%) juga bisa bekerja dengan baik sebagai alat pahat, memaksa area menjadi datar dan halus dengan cepat di bawah kuas, seperti memukul tanah liat dengan palu!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Topeng {#mask}
Alat ini memungkinkan Anda memberi topeng pada verteks. Verteks yang bertopeng terlindungi dari pemahatan maupun pengecatan.

Mode sub-nya adalah `Lepas Topeng`, yang menghapus topeng di tempat yang sudah dicat.

Mirip dengan seleksi di aplikasi lukis 2d, topeng bisa dicat dengan kuas atau dibuat dengan seleksi bentuk (`Tali`, `Rect`, `Pita`...), lalu dikaburkan atau dipertajam. Pilih kuas atau bentuknya di popup goresan pada bilah alat kiri, lihat [Kontrol seleksi](#selection-controls).

Berbeda dengan aplikasi lukis 2d, topeng juga bisa dibuat dari grup face, dan topeng bisa dipakai untuk membuat geometri baru melalui operasi bergaya ekstrusi/ekstraksi.

![](/videos/tool_mask1.mp4)

 Sebuah bilah alat akan muncul di bagian atas viewport dengan kontrol tambahan.

![](/images/tool_mask_toolbar.webp)

Judul bilah bisa diketuk untuk membuka/menutupnya, atau ketuk panah di kanan atas untuk memindahkannya ke bagian atas atau bawah antarmuka.

| Tindakan                                           | Deskripsi                                                                                  |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Hapus semua        | Menghapus topeng di semua objek. Jika objek lain juga bertopeng, tombol `Bersihkan` tambahan hanya menghapus topeng objek yang dipilih |
| ![](/icons/invert.webp)        Balik              | Membalik topeng                                                                            |
| ![](/icons/sharpen.webp)       Mempertajam        | Mempertajam tepi topeng                                                                    |
| ![](/icons/blur.webp)          Kabur              | Mengaburkan tepi topeng                                                                    |
| ![](/icons/outline.webp)       Batas              | Memberi topeng pada batas terbuka mesh, seperti tepi bidang datar atau bibir lubang       |
| ![](/icons/blur.webp)          Kabur ->           | Seret ke kanan untuk mengaburkan topeng, ke kiri untuk mempertajamnya                      |
| ![](/icons/circle_plus.webp)   Perbesar ->        | Seret ke kanan untuk memperluas area bertopeng, ke kiri untuk menyusutkannya              |
| ![](/icons/intensity.webp)     Tingkatkan ->      | Seret ke kanan untuk memperkuat topeng, ke kiri untuk melemahkannya, tanpa mengubah bentuknya |
| ![](/icons/dig.webp)           Rongga ->          | Membangun ulang topeng dari kelengkungan permukaan: seret ke kanan agar hanya bagian cekung yang bisa dicat, ke kiri agar hanya bagian menonjol |
| ![](/icons/culling.webp)       Depan              | Aktifkan agar hanya verteks yang menghadap depan yang diberi topeng                        |
| ![](/icons/eye_open.webp)      Terlihat           | Dengan bentuk, aktifkan untuk mengabaikan verteks yang tersembunyi di balik permukaan lain |
|                                 Konversi           | Mengonversi topeng menjadi grup face                                                       |
| ![](/icons/group_to_mask.webp) Saat diketuk (grup face) | Jika aktif, grup face akan ditampilkan, dan mengetuk sebuah grup face akan memberinya topeng |
|                                 Saat diketuk (topeng) | Jika aktif, mengetuk sebuah 'pulau' poligon bertopeng atau tidak bertopeng akan mengisi penuh pulau itu. |
| ![](/icons/connect.webp)       Terhubung          | Jika aktif, goresan topeng hanya memengaruhi topologi yang terhubung.                      |

##### Gestur cepat topeng {#mask-quick-gesture}
Anda bisa melakukan gestur bergaya ZBrush sambil menahan tombol topeng cepat di bilah alat kiri:
| Tindakan    | Gestur (tahan pintasan kiri bawah) |
| :---------: | :--------------------------------: |
| Balik       | Ketuk di latar belakang            |
| Bersihkan   | Seret di latar belakang            |
| Kabur       | Ketuk di area bertopeng            |
| Mempertajam | Ketuk di area tanpa topeng         |


#### Pengaturan Topeng {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

Pengaturan Topeng terutama dipakai untuk membuat geometri dari topeng. Tab di bagian atas memilih operasinya: [Ekstrak](#extract), [Pisah](#split-mask), atau [Ukir](#carve). Opsi di bawahnya berubah sesuai operasi.

* `Pratinjau` - Menampilkan seperti apa geometri baru nantinya selagi Anda mengatur pengaturannya.
* `X-Ray` - Objek mana yang digambar dalam mode x-ray selama pratinjau: `Tidak ada`, `Tidak terpilih`, `Dipilih`, atau `Semua`.

##### Ekstrak {#extract}
* `Ekstrak` - Membuat geometri hasil ekstraksi sebagai objek baru.
* `Aksi penutupan` - Cara bentuk hasil ekstraksi ditutup. `Tidak ada` menduplikasi poligon bertopeng menjadi bentuk baru dan membiarkannya terbuka. `Isi` melakukan hal yang sama, lalu mengisi dan menghaluskan lubang di bagian belakang (jangan gunakan pada permukaan datar). `Kulit` menutup bentuk dengan memakai nilai `Tinggi`, dan merupakan pilihan bawaan.

::: tip

Jika pratinjau aktif dengan x-ray, menekan tombol Ekstrak bisa membingungkan pada awalnya. Karena menu masih aktif, Nomad akan mencoba menampilkan pratinjau ekstraksi pada bentuk baru Anda, dan menampilkan permukaan asli dalam mode x-ray. Namun karena bentuk baru itu tidak punya topeng, pratinjau ekstraksi tidak bisa ditampilkan, dan Nomad akan memperingatkan 'Tidak ada yang bisa diekstrak!'.

Ini normal. Tutup menu pengaturan topeng untuk melihat bentuk baru dan bentuk aslinya, lalu pilih kembali permukaan asli jika Anda perlu menghapus topeng atau menggambar topeng baru.
:::

##### Pisah {#split-mask}
* `Pisah` - Mengekstrak area bertopeng DAN area tanpa topeng menjadi bentuk-bentuk baru.
* `Aksi penutupan` (bertopeng) - Cara bagian bertopeng ditutup, dengan pilihan `Tidak ada`, `Isi`, dan `Kulit` yang sama seperti pada Ekstrak.
* `Aksi penutupan` (tanpa topeng) - Cara bagian tanpa topeng ditutup, dengan pilihan yang sama.

##### Ukir {#carve}
* `Ukir` - Bekerja seolah-olah Anda memangkas ke dalam permukaan sedalam nilai `Tinggi`, seperti memotong sepotong kulit jeruk. `Tinggi` tidak boleh 0.

##### Tinggi {#thickness}
* `Tinggi` - Tinggi bentuk hasil ekstraksi. Tombol Plus/Minus memungkinkan Anda berganti antara ekstrusi ke luar, ke dalam, atau ke dua sisi.

##### Kehalusan {#smoothness}
Jika aktif, bentuk hasil ekstraksi akan dihaluskan; ini bekerja lebih baik dengan jumlah poligon yang lebih tinggi.
* `Semua` / `Hanya tepi` - Menghaluskan seluruh bentuk, atau hanya tepinya, tanpa mengubah bentuk permukaan atasnya.
* `Iterasi` - Dengan `Semua`, banyaknya penghalusan yang diterapkan. Nilai tinggi menghasilkan tepi lengkung yang sangat halus, tetapi bentuknya mulai menyimpang dari bentuk topeng.
* `Dinding` - Dengan `Hanya tepi`, banyaknya penghalusan pada dinding. Tombolnya berganti antara Santai, yang mempertahankan sudut-sudut tajam, dan Haluskan, yang juga membulatkannya.
* `Bagian dalam` - Dengan `Hanya tepi`, seberapa rata permukaan atas dibuat. Tombolnya berganti antara Santai, yang mempertahankan detail pahatan dan hanya meratakan arah ekstrusi (sehingga detail tidak lagi menimbulkan duri), dan Haluskan, yang menghaluskan permukaannya sendiri.

##### Sisi {#edge-loop-side}
* `Lurus` - Dinding polos di sisi-sisi bentuk hasil ekstraksi.
* `Bevel` - (Hanya Ekstrak dengan `Kulit`) Bibir miring di tepi depan. `Bevel` mengatur lebarnya, dalam % dari `Tinggi` atau dalam satuan dunia (tombol di sebelahnya untuk beralih), `Pembagian bevel` membaginya (`Otomatis` secara bawaan), dan sebuah kurva memungkinkan Anda membentuk profilnya.
* `Profil` - Membentuk dinding dengan kurva profil, dengan `Lebar` dalam % dari `Tinggi` atau dalam satuan dunia.
* `Topeng` - Tingginya mengikuti topeng: bagian topeng yang kabur mendapat tinggi lebih rendah, sehingga Anda bisa membuat bentuk dengan tinggi yang lembut dan bervariasi.
* `Pembagian dinding` - Jumlah loop tepi di sisi-sisinya. Dengan `Otomatis`, Nomad memilih jumlah pembagian yang menghasilkan poligon persegi, sesuai dengan poligon di area bertopeng.



### ![](/icons/tool_maskSelector.webp) Topeng Seleksi {#selection-mask}
Alat Topeng Seleksi (SelTopeng) kini menjadi bagian dari [alat Topeng](#mask). Untuk memberi topeng dengan bentuk alih-alih goresan kuas, pilih sebuah bentuk (`Tali`, `Poligon`, `Rect`...) di popup goresan alat Topeng, lihat [Kontrol seleksi](#selection-controls).

Mode sub `Lepas Topeng` juga bekerja dengan bentuk, dan akan menghapus topeng di dalam bentuk.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Melukis {#paint}
Menerapkan warna dan properti material. Untuk mempelajari lebih lanjut tentang material, Anda bisa mengunjungi bagian [Lukis](painting.md).

Mode sub-nya adalah `Hapus`, yang menghapus cat.

Selain goresan kuas, Melukis juga bisa mengisi bentuk (`Tali`, `Rect`, `Pita`...), lihat [Kontrol seleksi](#selection-controls).

#### Pengaturan Melukis {#paint-settings}
* `Penyaringan Layer` - Fungsinya seperti alpha lock lapisan di Photoshop atau Procreate. Jika Anda mengecat di sebuah lapisan dan opsi ini aktif, Anda hanya bisa mengubah bagian yang sudah ada catnya; area yang belum dicat akan terlindungi. Opsi ini hanya tersedia jika ada lapisan yang dipilih.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Smudge {#smudge}
Mengusapkan warna dan properti material. Menu pengaturan Smudge berisi penggeser `Kualitas`; nilai yang lebih rendah membuat goresan lebih cepat.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Datar {#flatten}
Meratakan area dengan memproyeksikan titik-titik ke bidang rata-rata.

Mode sub-nya adalah `Isi`, yang menentukan bidang berdasarkan titik tertinggi, dan cenderung menarik titik-titik ke atas.

#### Pengaturan Datar {#flatten-settings}

* `Kunci Arah Bidang` - Memakai arah bidang yang dihitung pada klik pertama. Secara bawaan opsi ini nonaktif.
* `Kunci Asal Bidang` - Memakai klik pertama sebagai pusat bidang. Secara bawaan opsi ini nonaktif, dan hanya bisa diaktifkan bersama `Kunci Arah Bidang`.

Jika salah satu atau keduanya nonaktif, perataan bisa diperdalam secara bertahap atau sudut bidangnya diubah dengan goresan panjang yang melewati kedalaman dan kelengkungan berbeda. Dipadukan dengan opsi pengambilan sampel area di menu kuas, ini memberi kendali yang sangat presisi.

::: tip
Saat bekerja di area dengan kelengkungan tinggi, misalnya saat mencoba meratakan pipi tetapi alat terus memengaruhi sisi hidung, coba buat topeng untuk melindungi area yang tidak boleh terkena kuas perata.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar {#planar}
Membuat titik-titik sebidang dengan memproyeksikannya ke bidang rata-rata, tetapi dengan penumpukan yang lebih sedikit dibanding kuas Datar. Hasilnya adalah permukaan bertepi keras yang lebih bersih. Goresan cepat akan lebih banyak mendorong dan menarik permukaan, sedangkan goresan lambat yang dimulai dari area yang sudah datar lalu bergerak ke luar akan lebih mempertahankan bidangnya.

Mode sub-nya adalah `Isi`, yang menentukan bidang berdasarkan titik tertinggi, dan cenderung menarik titik-titik ke atas.

Planar sebenarnya adalah alat yang sama dengan `Datar`, tetapi dengan `Kunci Arah Bidang` aktif, sehingga cenderung menghasilkan permukaan bertepi keras yang lebih stabil, sedangkan Datar bisa lebih bebas dipakai memahat dan membuat area setengah datar.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_polish.webp) Poles {#polish}
Anggota lain keluarga Datar, yang diatur untuk memoles permukaan menjadi bidang yang bersih. Ini adalah alat yang sama dengan `Datar`, dengan bawaan [Goresan](stroke.md) yang berbeda: `Jejak`, `Filter Normal Area`, dan `Filter kedalaman` diaktifkan.

Mode sub-nya adalah `Isi`, seperti Datar.

Poles punya pengaturan yang sama dengan [Datar](#flatten-settings): `Kunci Arah Bidang` dan `Kunci Asal Bidang`.

### ![](/icons/tool_crease.webp) Alur tajam {#crease}
Alat Alur tajam berguna untuk memahat potongan atau lekukan kecil.

Mode sub-nya adalah `Balik`, yang membuat alur yang menonjol.

#### Pengaturan Alur tajam {#crease-settings}

* `Faktor Cubitan` - Seberapa kuat verteks ditarik ke samping menuju kuas. Jika cubitan bernilai 1 dan ofset 0, kedalaman permukaan tidak berubah, hanya topologinya yang berubah, dengan tepi-tepi tertarik ke arah goresan.
* `Faktor Ofset` - Seberapa kuat verteks didorong/ditarik ke dalam. Jika cubitan bernilai 0 dan ofset 1, alur yang dalam atau lekukan yang menonjol akan terbentuk, tetapi tampak bergerigi karena geometri yang tertarik ke alur tidak cukup untuk membentuk sisi atau dasar alur dengan rapi.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Cubitan {#pinch}
Alat ini bisa dipakai untuk mempertajam tepi.

Mode sub-nya adalah `Balik`, yang merenggangkan verteks.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Pangkas {#trim}
Alat Pangkas bekerja dengan membuang sebagian mesh Anda, dan memberi pilihan cara mengolah celah yang tertinggal. Alat ini memakai [Kontrol seleksi](#selection-controls) untuk menentukan area pangkasan.

Mode sub-nya adalah `Balik`, yang membalik bentuk sehingga sisi lainnya yang dibuang.

::: tip
Karena alat ini memproyeksikan dari kamera, Anda akan mendapat peringatan jika kamera dalam mode perspektif.

Dalam mode ortografis, potongan yang menembus mesh sejajar dengan arah pandang, dan biasanya itulah yang diharapkan. Dengan kamera perspektif, potongan akan terlihat berbeda di sisi jauh objek dibanding di sisi dekatnya.
:::

#### Pengaturan Pangkas {#trim-settings}

Pengaturannya dikelompokkan di bawah `Pengisian lubang`:

* `Lukisan garis` - Jika cat diaktifkan di menu lukis, area tambalan akan diisi dengan warna yang sedang dipilih.
* `Boolean` - Mengisi lubang pangkasan dengan area poligon kuad. Area yang diisi akan datar.
* `Lama` - Mengisi lubang pangkasan dengan area segitiga. Area yang diisi akan datar.
* `Isi` - Mengisi lubang dengan area segitiga. Area yang diisi akan berupa permukaan lengkung, seperti lapisan gelembung sabun.
* `Tidak ada` - Tidak mengisi lubang.

Dengan `Boolean`, bagian `Rincian` berisi:

* `Bentuk` - Perkiraan ukuran kuad dan segitiga yang dipakai di sisi bentuk pangkasan.
* `Lubang` - Perkiraan ukuran segitiga atau poligon yang dipakai pada lubang yang diisi. Tombol tautan di sebelah `Rincian` menjaganya tetap sama dengan `Bentuk`; lepaskan tautannya untuk mengaturnya sendiri.
* `Pertahankan topologi` - Tidak menghaluskan dan menyederhanakan batas potongan, sehingga topologi mesh asli di dekat face bertopeng dan tersembunyi tetap terjaga.

Dengan `Lama`:

* `Rincian` - Perkiraan ukuran segitiga yang dipakai pada pangkasan.
* `Penghalusan lubang` - Seberapa banyak segitiga dirapikan pada area yang diisi.
* `Ambang batas epsilon` - Nilai yang bisa diatur untuk memperbaiki algoritma pengisian lubang lama.

Dengan `Isi`:

* `Rincian` - Perkiraan ukuran segitiga yang dipakai pada pangkasan.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Pisah {#split}
Mirip dengan alat [Pangkas](#trim), hanya saja Pangkas membuang seleksi, sedangkan Pisah menyimpan seleksi sebagai objek baru.

Mode sub-nya adalah `Bagi`: setiap potongan disimpan sebagai objek tersendiri, sehingga bentuk yang saling tumpang tindih (misalnya karena simetri) dipotong menjadi bagian-bagian terpisah, bukan digabung menjadi satu.

#### Pengaturan Pisah {#split-settings}

Pisah punya pengaturan `Pengisian lubang` yang sama dengan [Pangkas](#trim-settings): `Lukisan garis`, metode `Boolean`, `Lama`, `Isi`, dan `Tidak ada`, beserta opsi `Rincian`-nya.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Proyeksi {#project}
Alat Proyeksi mirip dengan alat [Pangkas](#trim), tetapi tidak menghapus atau membuat geometri apa pun; alat ini hanya memindahkan verteks agar mengikuti seleksi.

![](/videos/tool_project.mp4)

::: tip
Jika Anda memakai Proyeksi saat berada di sebuah lapisan, Anda bisa memadukan bentuk asli dan bentuk hasil proyeksi dengan penggeser lapisan.
:::

### ![](/icons/tool_layer.webp) Lapisan {#layer}
Menaikkan permukaan, tetapi dengan batas tinggi.

Jika Anda terus menahan pena dan menyapu suatu area berulang kali, Lapisan akan naik sampai ketinggian tertentu lalu berhenti, sedangkan alat lain akan terus menumpuk ketinggian.

Perlu diingat bahwa secara bawaan batas ini hanya berlaku per goresan! Jika Anda memulai goresan baru, alat akan membangun dari ketinggian permukaan yang baru.

Untuk mengatur tinggi maksimum yang tetap di banyak goresan, gunakan alat Lapisan bersama sistem [Lapisan](layers.md) Nomad.

Buat sebuah lapisan, lalu gunakan alat ini. Tinggi maksimumnya kini ditentukan dari lapisan, jadi Anda bisa membuat banyak goresan kuas dan tingginya akan selalu sama.

`Kurang` memakai kedalaman minimum, sehingga membuat cekungan.

#### Pengaturan Lapisan {#layer-settings}

* `Gunakan Data Lapisan` - Jika aktif, dan jika ada lapisan yang dipilih, data lapisan dipakai untuk menentukan tinggi maksimum. Sebuah peringatan mengingatkan Anda jika tidak ada lapisan yang dipilih.
* `Kembung` - Jika aktif, arah kerja lapisan disesuaikan untuk hasil yang lebih halus.
* `Santai (Normal)` - Dengan `Kembung` aktif, banyaknya penghalusan yang diterapkan pada normal.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_inflate.webp) Kembung {#inflate}
Memindahkan verteks searah normalnya masing-masing. `Kurang` memindahkan verteks searah kebalikan normalnya.

#### Pengaturan Kembung {#inflate-setings}
* `Santai (Normal)` - Banyaknya penghalusan yang diterapkan pada normal.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Dorongan {#nudge}
Memindahkan atau 'mengoleskan' titik-titik searah goresan.

Mode sub-nya adalah `Lipatan`, yang mendorong lipatan material sepanjang goresan: tonjolan di depan kuas, dan cekungan di belakangnya.

#### Pengaturan Dorongan {#nudge-settings}
* `Haluskan` - Seberapa banyak area di bawah kuas dihaluskan selagi Anda mendorongnya, agar permukaan yang dioles tetap rapi.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Cap {#stamp}

Klik dan seret untuk menaikkan area pahatan sesuai bentuk Alpha yang dipilih.

Ini sebenarnya adalah [alat Kuas](#brush) dengan jenis goresan `Kunci + jari-jari`.

`Kurang` akan menekan cap ke dalam alih-alih menariknya keluar dari permukaan.

::: tip
Cap biasanya bekerja paling baik pada geometri beresolusi tinggi. Jika Anda mencari 'wrinkles alpha', 'pores alpha', 'scales alpha', dan sejenisnya di internet, tekstur alpha tersebut bersama Cap bisa menjadi cara yang bagus untuk menambahkan detail organik pada pahatan karakter.

Kedua mode goresan berguna untuk hal yang berbeda.

* `Kunci + jari-jari` punya *tinggi* yang tetap; menyeret mengatur lebar dan rotasi cap. Cocok untuk tekstur kulit yang perlu kedalaman/tinggi yang sama, tetapi rotasi dan skala berbeda agar pola berulangnya tersamarkan.
* `Kunci + intensitas` punya *lebar* yang tetap; menyeret mengatur rotasi dan tinggi cap. Cocok untuk paku keling, yang semuanya harus berukuran sama, tetapi dengan rotasi dan tinggi berbeda.

:::

![](/videos/tool_stamp.mp4)

### ![](/icons/tool_vdm.webp) VDM {#vdm}

Mengecap peta pergeseran vektor (VDM). Berbeda dengan alpha, yang hanya bisa mendorong permukaan ke atas atau ke bawah, VDM menyimpan bentuk 3d lengkap, sehingga bisa mengecap bentuk menjorok seperti telinga, tanduk, atau daun yang melengkung. Cara kerjanya seperti [Cap](#stamp), dengan mode goresan `Kunci + jari-jari` dan `Kunci + intensitas` yang sama.

`Kurang` (`Balik`) membalik kedalaman cap, untuk menekannya ke dalam permukaan seperti cetakan.

VDM-nya sendiri dipilih di menu [Alpha](stroke.md#alpha), yang juga punya penggeser `Tinggi` untuk mengubah skala tinggi cap saja, tanpa mengubah pergeseran ke sampingnya.

Tombol `Buat` di bilah alat kiri memungkinkan Anda membuat cap sendiri:

* `VDM baru...` - Menambahkan bidang datar yang sudah disiapkan untuk memahat VDM. Pahat bentuk Anda di atasnya, lalu bake dengan `Topologi -> Bake -> VDM`: Nomad menambahkan cap baru ke pustaka VDM dan memilihnya.
* `Tangkap VDM` - (Eksperimental) Seret di permukaan model untuk mengambil area itu dan mengubahnya menjadi cap VDM. `Toleransi` meratakan tepi tangkapan secara halus.

::: tip
Hindari DynTopo saat memahat bidang VDM, karena merusak UV bidang dan membuat cap terdistorsi. Jauhkan juga pahatan dari tepi bidang, atau cap akan menampilkan tepi yang keras.
:::


### ![](/icons/tool_clearLayer.webp) Hapus Lapisan {#delete-layer}
Alat ini bisa mereset lapisan secara lokal; Anda memerlukan lapisan yang aktif, kalau tidak, tidak akan terjadi apa-apa. Alat ini menghapus data pahatan lapisan, dan juga catnya jika pengecatan diaktifkan.

Mode sub-nya adalah `Balik`, yang sedikit memperkuat lapisan alih-alih menghapusnya.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tabung {#tube}
Membuat tabung dengan menggambar kurva.
![](/images/tool_tube_new.webp)

Setelah tabung dibuat, jalurnya bisa disunting di ruang 3d dengan kontrol yang mirip dengan alat [Menyunting bentuk](#shape-editing) standar dan alat penyuntingan kurva.

![](/videos/tool_tube.mp4)

#### Bilah alat kiri Tabung {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Bilah alat kiri berisi opsi berikut:

* `Sinkron` - Jika tabung saat ini merupakan instans, dan ada node anak tabung yang berbeda di antara instans-instansnya, opsi ini akan menyinkronkannya kembali.
* `Snap` - Jika aktif, mode kurva dan jalur akan menempel ke objek lain saat Anda menggambar. Jika nonaktif, hanya titik pertama yang menempel, lalu sisa tabung digambar pada kedalaman itu.
* `Offset` - Mengatur kedalaman tempelan; 0% membuat bagian tengah penampang tabung menempel di permukaan, nilai positif mengangkatnya dari permukaan, nilai negatif menurunkannya. 100% sama dengan jari-jari tabung.
* `Tampilan` - Tanpa mode menggambar, sehingga Anda bisa menggerakkan kamera dengan bebas.
* `Lengkung` - Menggambar tabung secara bebas. Opsi ini punya menu kecil:
    * `Sunting` - Apa yang terjadi saat Anda menyelesaikan goresan, lihat [Kontrol seleksi](#selection-controls): langsung membuat tabung, mempertahankan kurva agar bisa disunting dengan lingkaran validasi hijau di sebelahnya, atau `Tahan` di akhir goresan untuk terus menyunting.
    * `Tutup` - Menjadikan tabung sebuah lingkaran tertutup.
    * `Terus menggambar` - Setelah memvalidasi sebuah tabung, tetap di alat ini untuk menggambar tabung berikutnya.
    * `Ketepatan` - Berapa banyak titik kurva yang dipakai untuk mengubah jalur yang digambar menjadi tabung. 0% memakai jumlah titik paling sedikit, tetapi melewatkan perubahan lengkung kecil pada jalur. 100% sangat akurat, dan memakai banyak titik.
* `Jalur` - Membuat tabung dengan mengklik untuk menentukan titik-titik kurva. Ketuk lingkaran hijau untuk memvalidasi jalur. Opsi ini punya menu kecil:
    * `B-spline` - Metode menggambar kurva alternatif, di mana titik-titik kurva biasanya tidak terletak tepat di kurva, tetapi bisa menghasilkan bentuk yang lebih halus dibanding metode bawaan.
    * `Tutup` - Menjadikan tabung sebuah lingkaran tertutup
    * `Layar` - Jika aktif, jalur 'disematkan' ke layar, sehingga Anda bisa menggerakkan tampilan dan objek sementara jalur tetap di tempatnya. Jika nonaktif, jalur menjadi bagian dari adegan 3d, dan akan bergerak bersama kamera dan objek.
* `Penampang` - Kurva menjadi cincin yang melingkari bentuk, memotong melalui kedua titiknya searah dengan arah pandang Anda.

##### Bilah alat atas Tabung {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Saat sebuah tabung dipilih, sebuah bilah alat akan muncul di bagian atas viewport dengan kontrol tambahan. Klik judul bilah alat untuk menutup/membukanya, dan klik panah di kanan atas untuk memindahkan bilah alat ke bagian atas atau bawah viewport.

* `Finalisasi` - Mengubah tabung menjadi poligon biasa agar bisa dipahat.
* `Sunting` - Menampilkan titik-titik kurva agar bisa dimanipulasi
* `Cermin` - Menambahkan pengulang cermin sebagai induk kurva ini
* `Snap` - Menempelkan titik-titik kurva ke permukaan terdekat
* `Tutup` - Menyambungkan awal dan akhir kurva menjadi lingkaran tertutup
* `B-spline` - Beralih antara interpolasi Catmull-rom dan B-spline.
* `Tutup` - Berganti antara tutup di kedua ujung tabung, hanya di awal atau akhir, atau tanpa tutup.
* `Lubang` - Menambahkan ketebalan pada tabung, mengubahnya menjadi pipa. Berganti antara lubang di kedua ujung, hanya di ujung akhir, atau tanpa lubang.
* `Radius` - Berganti antara radius seragam, radius di awal dan akhir, atau radius per titik kurva. Semuanya disunting dengan pegangan oranye pada kurva.
* `Lilitan` - Berganti antara tanpa lilitan, lilitan seragam, lilitan di awal dan akhir, atau lilitan per titik kurva. Semuanya disunting dengan pegangan merah muda pada kurva.
* `Profil` - Berganti antara tanpa profil (jadi profil lingkaran), profil seragam, profil di awal dan akhir, atau profil per titik.
* `Sunting profil` - Menampilkan editor profil. Fungsinya mirip dengan alat [Menyunting bentuk](#shape-editing), bisa menyimpan dan memuat prasetel profil, dan punya tombol untuk menyunting profil di ruang 3d.
* `Spiral` - Membuka menu untuk menambahkan lilitan spiral pada tabung. Menu ini punya opsi `Sudut lilitan`, `Offset`, `Skala`, dan `Offset sudut`.
* `Pembagian X` - Jumlah pembagian di sekeliling tabung; 4 pembagian akan membuat tabung persegi, misalnya.
* `Kepadatan konstan` - Jika aktif, poligon tetap berbentuk persegi. Jika nonaktif, Anda bisa mengatur `Pembagian Y` sepanjang tabung.
* `...` - Menu pengaturan tabung.

#### Tombol hapus titik kurva {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Di bawah bilah alat ada tombol hapus titik kurva. Saat Anda menyeret sebuah titik kurva mendekati titik lain, titik itu berubah merah, menandakan bahwa titik tersebut akan dihapus jika Anda melepasnya. Jika Anda sedang melakukan suntingan kecil dan tidak ingin menghapus titik, tombol ini menonaktifkan perilaku penghapusan titik.



#### Pengaturan Tabung {#tube-settings}
* `Primitif` - Tombol untuk mengaktifkan/menonaktifkan UV, atau untuk memvalidasi tabung.
* `Pembagian pasca` - Pintasan untuk mengatur level multiresolusi sebelum memvalidasi.
* `Subdivisi linear` - Pintasan untuk mengatur level subdivisi linear sebelum memvalidasi.
* `Pembagian X` - Sama dengan Pembagian X di bilah alat.
* `Pembagian Y` - Sama dengan Pembagian Y di bilah alat.
* `Kurva (Pengulang)` - Mengubah tabung menjadi [Pengulang Kurva](scene.md#curve)

::: tip
Pembagian 4 dan Pembagian pasca 3 akan menghasilkan tabung dengan ujung bulat yang halus, cocok untuk cacing, ular, dan bagian tubuh.
:::


### ![](/icons/tool_lathe.webp) Bubut {#lathe}
Membuat permukaan putar dengan menggambar kurva.

Alat ini sangat cocok untuk bentuk seperti vas dan gelas anggur.

![](/videos/tool_lathe.mp4)

#### Bilah alat kiri Bubut {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Bilah alat kiri berisi opsi berikut:

* `Sinkron` - Jika bubutan saat ini merupakan instans, dan ada node anak bubutan yang berbeda di antara instans-instansnya, opsi ini akan menyinkronkannya kembali.
* `Tetap` - Jika aktif, pusat bubutan tetap dan ditampilkan di layar. Garis pusat ini punya titik sunting yang bisa diatur. Jika nonaktif, pusat bubutan akan diperbarui secara dinamis mengikuti awal dan akhir kurva yang digambar.
* `Tampilan` - Tanpa mode menggambar, sehingga Anda bisa menggerakkan kamera dengan bebas.
* `Lengkung` - Menggambar profil bubutan dalam satu goresan. Opsi ini punya menu kecil:
    * `Sunting` - Apa yang terjadi saat Anda mengangkat pena, lihat [Kontrol seleksi](#selection-controls): langsung membuat bubutan, mempertahankan kurva agar bisa disunting dengan lingkaran hijau di sebelahnya untuk membuat bubutan, atau `Tahan` di akhir goresan untuk terus menyunting.
    * `Tutup` - Menyambungkan awal dan akhir kurva menjadi lingkaran tertutup
    * `Terus menggambar` - Setelah memvalidasi sebuah bubutan, tetap di alat ini untuk menggambar bubutan berikutnya.
    * `Ketepatan` - Berapa banyak titik kurva yang dipakai untuk mengubah jalur yang digambar menjadi tabung. 0% memakai jumlah titik paling sedikit, tetapi melewatkan perubahan lengkung kecil pada jalur. 100% sangat akurat, dan memakai banyak titik.
* `Jalur` - Membuat bubutan dengan mengklik untuk menentukan titik-titik kurva. Ketuk lingkaran hijau untuk memvalidasi jalur. Opsi ini punya menu kecil:
    * `B-spline` - Metode menggambar kurva alternatif, di mana titik-titik kurva biasanya tidak terletak tepat di kurva, tetapi bisa menghasilkan bentuk yang lebih halus dibanding metode bawaan.
    * `Tutup` - Menjadikan tabung sebuah lingkaran tertutup
    * `Layar` - Jika aktif, jalur 'disematkan' ke layar, sehingga Anda bisa menggerakkan tampilan dan objek sementara jalur tetap di tempatnya. Jika nonaktif, jalur menjadi bagian dari adegan 3d, dan akan bergerak bersama kamera dan objek.

#### Bilah alat atas Bubut {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Saat sebuah bubutan dipilih, sebuah bilah alat akan muncul di bagian atas viewport dengan kontrol tambahan. Klik judul bilah alat untuk menutup/membukanya, dan klik panah di kanan atas untuk memindahkan bilah alat ke bagian atas atau bawah viewport.

* `Finalisasi` - Mengubah bubutan menjadi poligon biasa agar bisa dipahat.
* `Sunting` - Menampilkan titik-titik kurva agar bisa dimanipulasi
* `Cermin` - Menambahkan pengulang cermin sebagai induk bubutan ini
* `Snap` - Menempelkan titik-titik kurva ke permukaan terdekat
* `Stabil` - Jika aktif, profil kurva menjadi anak dari garis pusat bubutan. Jika nonaktif, garis pusat bisa disunting tanpa menggerakkan kurva, sehingga bentuk yang lebih rumit bisa dibuat.
* `Fokus` - Memutar tampilan agar profil kurva terlihat lurus menghadap kamera.
* `Tutup` - Menyambungkan awal dan akhir kurva menjadi lingkaran tertutup
* `Tutup` - Jika Tutup (lingkaran) nonaktif, berganti antara tutup di kedua ujung, hanya di awal atau akhir, atau tanpa tutup.
* `Lubang` - Menambahkan ketebalan pada bubutan, mengubahnya menjadi pipa. Berganti antara lubang di kedua ujung, hanya di ujung akhir, atau tanpa lubang.
* `B-spline` - Beralih antara interpolasi Catmull-rom dan B-spline.
* `Pembagian X` - Jumlah pembagian di sekeliling bubutan; 4 pembagian akan membuat bubutan berprofil persegi, misalnya.
* `Kepadatan konstan` - Jika aktif, poligon tetap berbentuk persegi. Jika nonaktif, Anda bisa mengatur `Pembagian Y` sepanjang tabung.
* `...` - Menu pengaturan bubutan.

#### Pengaturan Bubut {#lathe-settings}
* `Primitif` - Tombol untuk mengaktifkan/menonaktifkan UV, atau untuk memvalidasi tabung.
* `Pembagian pasca` - Pintasan untuk mengatur level multiresolusi sebelum memvalidasi.
* `Subdivisi linear` - Pintasan untuk mengatur level subdivisi linear sebelum memvalidasi.
* `Pembagian X` - Sama dengan Pembagian X di bilah alat.
* `Pembagian Y` - Sama dengan Pembagian Y di bilah alat.
* `Kurva (Pengulang)` - Mengubah profil kurva menjadi [Pengulang Kurva](scene.md#curve)

### ![](/icons/tool_insert.webp) Masukkan {#insert}
Menempatkan sebuah objek di permukaan objek lain. Cara pakainya mirip alat Cap, tetapi untuk bentuk 3d utuh.

Jika Anda memilih sebuah primitif dari bilah alat kiri, klik-seret di permukaan mana pun akan menempatkan primitif di titik yang Anda klik, dan seretannya menentukan ukurannya. Setelah selesai menyeret, Masukkan akan beralih ke mode [Transformasi](#transform).

Dalam mode Instans, menyeret akan membuat instans baru dan menggesernya di atas permukaan. Ukurannya disalin dari bentuk pertama; dengan cara ini Anda bisa menempatkan banyak instans berukuran sama dari sebuah objek di atas permukaan lain.

Anda tidak harus memasukkan primitif saja! Pilih bentuk *apa pun* di outliner; jika Masukkan dalam mode Instans atau Kloning, Anda bisa menyeret salinan objek yang dipilih ke atas permukaan lain mana pun.

Jika sebuah objek punya poros khusus, poros itu akan dipakai sebagai titik jangkar. Lihat video di bawah.

Bilah alat kiri juga punya `Tampilan`, untuk menggerakkan kamera tanpa memasukkan apa pun, dan `Sinkron`: jika objek sasaran merupakan instans, objek baru juga ditambahkan ke semua instans lainnya.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transformasi {#transform}
Memindahkan/memutar/mengubah skala model secara langsung dengan 1 dan 2 jari, biasanya di atas permukaan objek lain.

Bilah alat kiri berisi tombol-tombol berikut:

* `Kloning` / `Instans` - Membuat salinan atau instans objek, lihat bilah alat [Gizmo](#left-menu-toolbar).
* `Pindah` - Seret dengan satu jari untuk memindahkan objek. Jika snap aktif, objek akan meluncur di atas permukaan di bawah jari Anda.
* `Putar` - Seret dengan satu jari untuk memutar objek. Jika snap aktif, objek berputar di sekitar normal permukaan di bawah jari Anda.
* `Skala` - Seret dengan satu jari untuk mengubah skala objek.

Sebuah bilah alat di bagian atas viewport berisi:

* `Sasaran` - Apakah alat memindahkan objek, grupnya, atau verteksnya, sama seperti pada [Gizmo](#left-menu-toolbar).
* `Snap` - Menempelkan model ke permukaan lain.
* `Permukaan` / `Verteks` - Dengan `Snap`, menempel ke permukaan, atau ke verteks terdekat.

Transformasi bisa menjalankan 2 mode ini dengan cepat menggunakan 2 jari:

* Seret objek untuk menempatkannya. Hentikan gerakan jari pertama, tetapi jangan angkat dari layar.
* Sentuhkan jari kedua ke layar sambil tetap menahan jari pertama. Saat jari kedua diseret, skala objek akan berubah.
* Angkat jari kedua, lalu lanjutkan menyeret jari pertama; objek akan kembali ke mode pindah.

Anda juga bisa mengganti mode kedua dengan gestur ketuk jari kedua:

* Seret objek untuk menempatkannya, hentikan gerakan, tetapi jangan angkat jari dari layar.
* Ketuk dengan jari kedua sambil menahan jari pertama
* Alat beralih ke mode rotasi. Seret jari pertama untuk mengatur rotasi.
* Ketuk jari kedua seperti tadi, alat kembali ke mode pindah.

Ini memberi alur kerja yang cepat untuk mengkloning objek di atas objek lain, misalnya batu di atas lanskap. Perhatikan bahwa tombol kloning juga ada di bilah alat kiri agar mudah dijangkau:

* Gunakan alat transformasi untuk memindahkan batu ke tempatnya.
* Lepaskan, tekan tombol kloning
* Pindahkan batu ini, putar/ubah skalanya sesuai kebutuhan
* Lepaskan, tekan tombol kloning
* Pindahkan batu ini, ulangi.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Alat ini memungkinkan Anda memindahkan, memutar, dan mengubah skala objek, serta mengubah poros objek.

Pegangan di viewport punya fitur-fitur berikut:

* `Pindah` - Seret garis+panah untuk memindahkan di sumbu X/Y/Z. Seret titik berwarna persik di tengah gizmo untuk memindahkan bebas di ruang layar. Klik kotak merah, hijau, biru untuk memindahkan di bidang X/Y/Z.
* `Putar` - Seret lingkaran merah/hijau/biru untuk memutar di sumbu X/Y/Z. Seret bola di dalam lingkaran-lingkaran itu untuk memutar bebas.
* `Skala` - Seret titik merah/hijau/biru di bagian luar untuk mengubah skala di sumbu X/Y/Z. Seret kerucut merah/hijau/biru di bagian luar untuk mengubah skala di bidang X/Y/Z. Seret lingkaran persik di bagian luar untuk mengubah skala secara seragam.

![](/images/tool_gizmo.webp)

#### Node dan verteks {#nodes-and-vertices}

Setiap objek di Nomad terdiri dari sebuah node dan verteks:

* `Node` - 'Pegangan' objek, yang menyimpan translasi, rotasi, dan skalanya, disebut matriks transformasinya.
* `Verteks` - Titik-titik yang membentuk permukaan objek; menyimpan posisi dan informasi cat.

Jika Anda punya kotak sederhana yang terdiri dari 8 verteks, Anda bisa memindahkannya dengan mengubah matriks transformasinya, atau dengan mengubah posisi verteksnya. Saat memahat, biasanya Anda ingin mengubah verteks; saat memindahkan objek dengan gizmo, biasanya Anda ingin mengubah node. Nomad memungkinkan keduanya.

#### Bilah alat Gizmo {#left-menu-toolbar}

Bilah alat kiri berisi:

* `Kloning` - Membuat salinan mandiri dari objek saat ini, yang bisa diseret menjauh dengan gizmo.
* `Instans` - Membuat salinan instans dari objek saat ini. Objek-objeknya saling terhubung, jadi perubahan pahatan pada satu objek akan muncul di semua objek instansnya.
* `Poros` - (Ikon gembok, di tempat tombol `Kurang`) Jika aktif, gizmo bisa dipindahkan dan diputar tanpa menggerakkan objek. Seperti `Kurang`, tahan untuk perubahan sesaat, atau ketuk agar tetap aktif.

Sebuah bilah alat di bagian atas viewport berisi kontrol lainnya:

* `Sasaran` - Menentukan apakah gizmo memengaruhi node atau verteks sebuah objek:
    * `Otomatis` - Bawaan; bekerja seperti `Grup`, tetapi jika mesh punya topeng atau simetri aktif, bekerja seperti `Verteks`.
    * `Verteks` - Menerapkan transformasi pada verteks, dengan memperhitungkan topeng dan simetri. Tidak bekerja pada primitif yang belum difinalisasi, dan instans juga ikut terpengaruh.
    * `Objek` - Hanya memindahkan objek saat ini, mengabaikan simetri dan topeng. Objek anak tetap diam.
    * `Grup` - Memindahkan objek beserta seluruh hierarkinya, mengabaikan simetri dan topeng.
    * `Instans` - (Objek dan Grup) Sama, tetapi semua instans objek ikut bergerak.
* `Poros` - Popup untuk menempatkan poros dengan cepat, dijelaskan [di bawah](#pivot).
* `Semua` / `Pindah` / `Putar` / `Skala` - Menampilkan semua pegangan gizmo, atau hanya pegangan pindah, putar, atau skala.
* `Pin` - Secara bawaan, gizmo akan berpindah ke poros objek yang dipilih. Jika pin aktif, gizmo tetap di posisinya saat ini.
* `Sejajarkan` - Beralih antara poros yang sejajar dengan objek saat ini, atau sejajar dengan dunia.
* `Snap` (rotasi) - Mengaktifkan nilai rotasi yang melompat per kelipatan; nilai snap ditampilkan dan bisa disunting saat snap aktif. Opsi `Magnet`-nya membuat rotasi menempel pada sebuah kelipatan saat melewatinya, lalu bergerak bebas lagi; matikan untuk melompat dari kelipatan ke kelipatan.
* `Snap` (translasi) - Mengaktifkan nilai translasi yang melompat per kelipatan; nilai snap ditampilkan dan bisa disunting saat snap aktif.

#### ![](/icons/reset.webp) Poros {#pivot}
Popup `Poros` di bilah alat atas memungkinkan perubahan poros dengan cepat. Posisi dan orientasi poros menentukan gizmo.

**Atur ulang**
* `Otomatis` - Pusat objek, sejajar dengan transformasinya.
* `Tengah` - Memindahkan poros ke pusat objek, dengan orientasi tetap.
* `Bawah` - Memindahkan poros ke tengah bawah objek. Ketuk lagi untuk memakai kotak pembatas dunia.
* `Atas` - Memindahkan poros ke tengah atas objek. Ketuk lagi untuk memakai kotak pembatas dunia.
* `Objek` - Memindahkan poros ke titik asal objek, sejajar dengan transformasinya.
* `Topeng` - Memindahkan poros ke pusat area tanpa topeng. Ketuk lagi untuk beralih ke area bertopeng.
* `Sejajarkan` - Mereset rotasi agar sejajar dengan dunia, dengan posisi tetap.
* `Tampilan` - Menyejajarkan poros dengan tampilan saat ini, dengan posisi tetap. Poros tidak mengikuti kamera setelahnya.

**Sekali ketuk (mode Poros)**

Hanya aktif saat `Poros` menyala; menentukan apa yang terjadi saat Anda mengetuk sekali di permukaan mesh:
* `Tidak ada` - Tidak melakukan apa-apa saat objek diketuk
* `Normal` - Memindahkan dan memutar poros agar sejajar dengan titik permukaan yang diketuk
* `Pertama` - Memindahkan (tanpa memutar) poros ke titik permukaan yang diketuk
* `Medial` - Memindahkan poros ke bagian tengah objek, di bawah titik permukaan yang diketuk.

#### Pengaturan Gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

* `Kompak` - Mengubah tata letak gizmo untuk meletakkan pegangan tambahan di luar atau di dalam bola rotasi
* `Ukuran Gizmo` - Ukuran gizmo
* `Ketebalan` - Ukuran garis-garis pada gizmo
* `Opasitas` - Opasitas gizmo
* `Sembunyikan saat berinteraksi` - Mengatur apakah gizmo disembunyikan sementara saat sedang diseret

-----

* `Ambang gulir tangensial` - Mengatur perilaku rotasi saat menyeret pegangan lingkaran untuk memutar di sumbu X/Y/Z. Jika nilainya 0, rotasi bekerja seperti tombol putar: seret gizmo dengan gerakan melingkar. Jika nilainya 90, rotasi bekerja seperti menarik tali yo-yo: seret dalam garis lurus mendekati atau menjauhi titik klik pertama. Nilai di antara 0 dan 90 memadukan keduanya; di bawah nilai tersebut gerakannya linear, di atasnya gerakannya melingkar.
* `Masukan numerik` - Jika aktif, satu ketukan pada gizmo akan memunculkan jendela untuk memasukkan nilai yang tepat bagi sumbu widget yang diketuk.

::: warning
Alat [Gizmo](#gizmo) dan [Transformasi](#transform) memakai kotak centang simetrinya sendiri, terpisah dari simetri pahatan!

Secara bawaan, simetri ini nonaktif.
:::

##### Matriks {#matrix}
Nilai transformasi yang tepat dari objek tidak lagi ada di pengaturan Gizmo: semuanya pindah ke menu `Transformasi`, di menu kanan atas. Bagian `Matriks`-nya berisi:

* ![](/icons/target.webp) `Pindahkan ke asal` - Memindahkan objek agar porosnya berada di pusat adegan, yang disebut titik asal.
* ![](/icons/bake.webp)  `Bake` - Membekukan objek di posisinya saat ini, dan mengatur nilai translasi/rotasi ke 0, skala ke 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Poros` - Bake poros: membuat nilai matriks sesuai dengan posisi pegangan gizmo di dunia.
* ![](/icons/reset.webp) `Atur Ulang` - Pintasan yang mengatur nilai translasi ke 0, nilai rotasi ke 0, skala ke 1, sehingga objek ikut berpindah dan berputar.

::: tip Bake vs bake ke poros
Buat sebuah kotak, pilih alat Gizmo, buka dan sematkan menu `Transformasi`. Secara bawaan, translasi dan rotasinya 0, skalanya 1.

Aktifkan mode poros, pindahkan pegangannya ke satu sisi, lalu matikan mode poros. Porosnya sudah berubah, tetapi perhatikan bahwa nilai translasinya masih 0.

Jika Anda ingin melihat di mana poros itu *sebenarnya* berada, klik tombol bake `Poros`. Sekarang nilai translasinya berubah. Perhatikan bahwa kotaknya tidak bergerak selama operasi ini, maupun saat mode poros.

Pindahkan dan putar kotak ke suatu tempat, lalu ketuk `Pindahkan ke asal`. Objek dipindahkan sehingga porosnya berada di pusat dunia, tetapi rotasinya tidak berubah.

Klik `Atur Ulang`, dan rotasinya juga akan diatur ke 0.

Pindahkan dan putar kotak lagi, kali ini klik `Bake`. Poros tetap di tempatnya, kotak tetap di tempatnya, tetapi nilai translasi dan rotasinya diatur ke 0.

Latih ini beberapa kali! Pahami bahwa nilai poros itu tersembunyi dan Nomad mengurusnya untuk Anda, tetapi jika Anda perlu menempatkan poros di lokasi nyata dalam ruang, Bake poros akan melakukannya untuk Anda.

:::

* `Translasi` - Nilai translasi X, Y, Z
* `Rotasi` - Nilai rotasi X, Y, Z
* `Skala` - Skala seragam jika opsi itu aktif, atau skala X, Y, Z jika nonaktif.
* `Miring` - Nilai kemiringan (shear) X, Y, Z, hanya ditampilkan jika objek sudah dimiringkan
* `Skala Uniform` - Beralih antara mengubah skala secara seragam atau terpisah di setiap sumbu

Di sebelah kiri, Anda bisa memindahkan poros gizmo; lihat cara kerjanya di video di bawah.
Ini terutama berguna untuk rotasi, karena tidak mengubah apa pun pada translasi.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Grup Face {#facegroup}

Grup face memungkinkan Anda menata objek menjadi kumpulan face dengan warna berbeda. Anda bisa memakai grup ini dengan banyak cara di Nomad:

* Cara cepat menyeleksi untuk topeng
* Menyembunyikan/menampilkan bagian objek
* Menata objek tanpa harus memecahnya menjadi bagian-bagian terpisah
* Menentukan area UV
* Memandu quad remesher
* Kendali tambahan untuk alat seperti Haluskan.

#### Bilah alat kiri Grup Face {#facegroup-left-toolbar}

* `Grup` - Tombol ini menampilkan grup face saat ini. Ketuk untuk menampilkan grup face yang tersedia sebagai petak-petak warna dan memilih salah satunya. Ketuk sebuah petak untuk mengganti nama atau warnanya, atau menghapusnya. `Hapus yang tidak digunakan` menghapus petak yang tidak terpakai, `Setel ulang` menghapus semuanya. Ikon plus memungkinkan Anda membuat petak baru.
* `Titik` - Cat di atas objek untuk menentukan grup face. Jika '+ Grup Face' aktif, setiap goresan baru otomatis membuat grup face baru, berguna untuk menentukan area dengan cepat. Satu ketukan akan mengisi penuh area yang dipilih. Penggesernya mengatur jari-jari titik.
* `Santai` - Menghaluskan batas grup face. Sangat berguna untuk membuat tepi yang rapi sebelum quad remeshing, atau untuk menentukan panel pada pemodelan hard surface. Penggesernya mengatur jari-jari dan intensitas operasi santai.
* Bentuk - Membuat grup face dengan bentuk alih-alih kuas, melalui `Kunci + jari-jari`, `Tali`, `Poligon`, `Garis`, `Rect`, dan `Elips`. Lihat [Kontrol seleksi](#selection-controls) untuk info lebih lanjut.
* `Pilih` - Mode sub. Jika aktif, petak tempat goresan dimulai akan dipilih, lalu dipakai untuk sisa goresan. Sangat berguna untuk merapikan area grup face; jika sebuah grup face meluas terlalu jauh, aktifkan `Pilih`, mulai goresan dari tempat petak grup face sudah benar, lalu seret sampai ke batasnya untuk menetapkan ulang petak yang benar.

#### Bilah alat atas Grup Face {#facegroup-top-toolbar}

Sebuah bilah alat di bagian atas viewport berisi kontrol tambahan:

* `Santai (Semua)` - Seret untuk merapikan batas semua grup face sekaligus.
* `Depan` / `Terlihat` / `Terhubung` - Filter goresan yang sama seperti pada bilah alat [Topeng](#mask).
* `Dari normal` - Membuat grup face berdasarkan sudut antar-face. Popup-nya berisi `Sudut`, dan memungkinkan Anda melewati grup kecil berdasarkan `Jumlah face` atau `Luas permukaan`, dengan `Pratinjau` sebelum Anda memvalidasi.
* `Dari bagian` - Membuat satu grup face untuk setiap bagian yang terpisah.
* `Dari UV` - Membuat satu grup face untuk setiap pulau UV.
* `Dari topeng` - Membuat grup face dari area bertopeng.
* `Saat diketuk` - Pilih apa yang terjadi saat sebuah grup face diketuk: mengisinya dengan grup face saat ini, menyembunyikannya, memberinya topeng, atau `Pose` (grup yang diketuk dan semua yang ada di baliknya dilepas topengnya, dan gizmo diletakkan di sambungannya, dengan penggeser `Kabur` untuk topeng). Tombol `Saat diketuk` kedua, yang tersedia jika mesh punya topeng, membatasi ketukan hanya pada face di sisi topeng yang sama.
* Tombol `Bersihkan` untuk alat [Sembunyi](#hide) dan [Topeng](#mask), untuk menampilkan kembali semuanya atau menghapus topeng tanpa meninggalkan alat.

#### Pengaturan Grup Face {#facegroup-settings}

Menu `Alat` mengekstrak grup face menjadi objek baru, dengan opsi yang sama seperti `Ekstrak` di [Pengaturan Topeng](#mask-settings). Tombol `Grup Face` di bagian atas memilih grup mana yang diekstrak, dan ada penggeser `Celah` tambahan: penggeser ini menggeser setiap batas ke dalam di sepanjang permukaan, sedangkan nilai negatif menggesernya ke luar sehingga tumpang tindih. Untuk panel yang bersebelahan, gunakan setengah dari celah yang diinginkan.

### ![](/icons/tool_hide.webp) Sembunyi {#hide}
Menyembunyikan atau mengisolasi bagian-bagian objek.

Mode utamanya diatur dari menu sebelah kiri:

* `Titik` - Sapukan kuas di atas objek untuk menyembunyikan bagian-bagiannya.
* Bentuk - Menyembunyikan dengan bentuk alih-alih kuas, melalui `Tali`, `Poligon`, `Garis`, `Rect`, dan `Elips`. Lihat [Kontrol seleksi](#selection-controls) untuk info lebih lanjut.
* `Tampilkan` - Mode sub, membalik operasi sehingga mode yang dipilih akan menampilkan bagian objek alih-alih menyembunyikannya.

Sebuah bilah alat akan muncul di bagian atas viewport dengan kontrol tambahan:

* `Hapus semua` - Memulihkan objek; semua bagian yang tersembunyi akan ditampilkan kembali. Jika objek lain juga punya bagian tersembunyi, tombol `Bersihkan` tambahan hanya memulihkan objek yang dipilih.
* `Balik` - Menukar bagian yang tersembunyi dan yang terlihat.
* `Hapus` - Menghapus bagian objek yang tersembunyi
* `Pisah` - Memisahkan bagian objek yang tersembunyi menjadi bentuk baru.
* `Depan` / `Terlihat` / `Terhubung` - Filter goresan yang sama seperti pada bilah alat [Topeng](#mask).
* `Saat diketuk` (grup face) - Memakai grup face untuk menyembunyikan bagian dengan cepat; mengetuk sebuah grup face akan menyembunyikan seluruh grup face itu.
* `Saat diketuk` (topeng) - Jika ada topeng yang aktif, ketukan akan menyembunyikan bagian yang bertopeng.

### ![](/icons/tool_measure.webp) Ukur {#measure}
Seret untuk mengukur jarak antara 2 titik. Setelah ditempatkan, Anda bisa menyeret titik-titik ujungnya untuk menyesuaikan ukuran.

Bilah alat kiri memilih cara jarak diukur:

* `Garis` - Garis lurus di antara kedua titik.
* `Permukaan` - Jarak di sepanjang permukaan, mengikuti potongan melalui kedua titik seperti terlihat dari kamera.
* `Penampang` - Keliling penampang melalui kedua titik, seperti meteran jahit yang dilingkarkan di lengan.
* `Verteks` - Menempelkan titik-titik ujung ke verteks terdekat.
* `Rasio emas` - Menampilkan titik kuning pada titik rasio emas dari ukuran.
* Tombol `?` menampilkan volume, luas permukaan, dan ukuran objek yang dipilih.

### ![](/icons/tool_arrange.webp) Atur {#arrange}
Menyusun dan menata beberapa objek sekaligus, seperti alat perataan di aplikasi desain 2d. Pilih objek-objeknya terlebih dahulu; dengan satu objek saja, Atur bekerja pada bagian-bagiannya yang terpisah. Sebuah kotak digambar di sekeliling seleksi; seret pegangannya untuk mengubah skalanya.

Sebuah bilah alat di bagian atas viewport berisi kontrolnya:

* `Dunia` / `Layar` - Menata mengikuti sumbu dunia, atau mengikuti layar (kiri, kanan, atas, bawah).
* `Sejajarkan` - Menyejajarkan objek pada sisi minimum, tengah, atau maksimumnya, di setiap sumbu.
* `Distribusikan` - Memberi jarak yang rata pada objek di antara dua objek terluar, berdasarkan sisi minimum, tengah, atau maksimumnya. Membutuhkan minimal 3 objek.
* `Garis` - Menyusun objek dalam satu baris di sepanjang sebuah sumbu.
* `Kisi` - Menyusun objek dalam kisi, dengan sejumlah objek di `X`, `Y`, dan `Z`.
* `Lingkaran` - (Hanya Dunia) Menyusun objek dalam lingkaran di sekitar sumbu `X`, `Y`, atau `Z`.
* `Bola` - (Hanya Dunia) Menyusun objek di atas permukaan bola.

`Garis`, `Kisi`, `Lingkaran`, dan `Bola` semuanya punya penggeser `Jarak` untuk celah di antara objek.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Alat ini mengubah objek yang dipilih menjadi tata letak topologi kuad yang rapi, dengan kontrol untuk kepadatan, aliran tepi, dan simetri.

::: tip
Quad Remesher dikembangkan oleh [Exoside](https://exoside.com/) untuk iOS dan desktop.

Di iOS, Quad Remesher adalah pembelian dalam aplikasi di Nomad, dengan pembayaran sekali sebesar $16USD.

Untuk desktop, beli lisensi dari [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Anda bisa membelinya khusus untuk Nomad desktop, atau lisensi silang untuk semua aplikasi desktop yang didukung.

Jika Anda sudah memiliki Quad Remesher untuk aplikasi desktop lain, Anda bisa [membeli upgrade ke semua platform dengan biaya lebih murah.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher tidak tersedia untuk Android. Di Android, Anda bisa memakai remesher open source gratis di tab topologi [Remesh Kuad](topology.md#quad-remesh) (AutoRemesher, Instant Mesh, QuadriFlow), tetapi perlu diingat bahwa fiturnya lebih terbatas.
:::

Selama Quad Remesher belum dibuka, bilah alat atas diawali dengan tombol keranjang belanja alih-alih tombol remesh. Di iOS, tombol ini membuka pembelian dalam aplikasi. Di desktop, tombol ini menampilkan `Buka kunci (beli, pulihkan, coba)`, yang memeriksa lisensi Exoside Anda (atau memulai masa uji coba). Setelah aktif, bilah alat kiri dan atas akan diaktifkan.

* `Titik` - Kuas ini mengatur kepadatan target. Intensitas 100% akan mengecat merah, yang memakai dua kali kepadatan kuad target di area tersebut. Intensitas 0% akan mengecat sian, yang memakai setengah kepadatan kuad target di area tersebut. Intensitas 50% akan mengecat abu-abu, yang memakai kepadatan kuad target bawaan.
* `Haluskan` - Menghaluskan peralihan kepadatan merah/abu-abu/sian.
* `Smudge` - Mengusap cat kepadatan.
* `Lengkung` - Gambar kurva di permukaan pahatan; quad remesher akan memakainya sebagai pemandu aliran tepi. Ketuk sebuah kurva untuk menghapusnya.
* `Jalur` - Gambar jalur di permukaan pahatan; quad remesher akan memakainya sebagai pemandu aliran tepi. Ketuk sebuah jalur untuk menghapusnya.
* `Rect` - Gambar persegi panjang di permukaan pahatan; quad remesher akan memakainya sebagai pemandu aliran tepi. Ketuk sebuah jalur untuk menghapusnya.
* `Elips` - Gambar elips di permukaan pahatan; quad remesher akan memakainya sebagai pemandu aliran tepi. Ketuk sebuah jalur untuk menghapusnya.

#### Bilah alat atas Quad Remesher {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

Sebuah bilah alat akan muncul di bagian atas viewport dengan kontrol tambahan:


* `<Jumlah>` - Klik ini untuk memulai proses quad remesher; angka ini menunjukkan jumlah kuad target hasil remesh.
* `Empat Sisi` - Atur jumlah kuad target dengan menggeser ke kiri dan kanan, atau ketuk untuk memasukkan angka yang tepat. Perlu diingat bahwa angka ini lebih merupakan panduan daripada angka pasti; berbagai kontrol quad remesher sering membuat hasilnya tidak persis sama dengan target ini.
* `Setengah` - Pintasan untuk mengatur jumlah target menjadi setengah dari jumlah poligon saat ini.
* `Sama` - Pintasan untuk mengatur jumlah target sama dengan jumlah poligon saat ini.
* `Panduan` - Beralih untuk memakai atau mengabaikan pemandu. Jika ada pemandu, tombol `Panduan` kedua menampilkan jumlahnya; ketuk untuk menghapus semuanya.
* `Kepadatan` - Beralih untuk memakai atau mengabaikan cat kepadatan. Jika ada cat kepadatan, tombol `Kepadatan` kedua akan menghapusnya.
* `Grup Face` - Beralih untuk memakai atau mengabaikan grup face untuk mengarahkan quad remesher.
* `Santai` - Beralih untuk merapikan batas grup face secara otomatis selama quad remeshing. Jika Anda sudah merapikan/menghaluskan batas grup face, nonaktifkan opsi ini.
* `Penggeser Santai` - Penggeser pintasan untuk merapikan batas grup face.
* `Tepi Keras` - Beralih untuk mencoba mempertahankan tepi keras.
* `Proyeksikan Ulang Vertex` - Beralih untuk memproyeksikan ulang tata letak baru ke mesh masukan.
* `Sim` - Beralih untuk mengaktifkan hasil yang simetris. Perlu diingat bahwa simetri selalu dihitung terhadap sumbu x dunia, jadi pastikan model Anda berada di titik asal jika Anda mengharapkan hasil yang simetris.
* `...` - Popup pengaturan Quad Remesher.

#### Menu pengaturan Quad Remesher {#quad-remesher-settings-menu}

Tombol `...` di ujung bilah alat atas membuka popup berisi pengaturan lainnya:

* `Jumlah Kuad Adaptif` - Beralih untuk memakai kuad yang lebih kecil di area dengan kelengkungan tinggi, dan kuad yang lebih besar di area dengan kelengkungan rendah.
* `Ukuran Adaptif` - Mengatur tingkat adaptivitas. 100% memungkinkan ukuran adaptif maksimum, pada 0% kuad akan seragam.

::: tip

Resep untuk mendapatkan quad remesh yang bagus dengan artefak minimal:

* Beri grup face pada mesh untuk menentukan aliran kuad ideal Anda.
* Rapikan grup face dengan Santai agar batas grup face halus.
* Desimasi. Ini memastikan tidak ada face yang tipis atau terdistorsi di tepi grup face. Di pengaturan desimasi, pastikan grup face diaktifkan. Dengan begitu, tepi segitiga akan mengikuti tepi grup face Anda dengan tepat.

Di opsi quad remesh, pastikan Santai dinonaktifkan (karena Anda sudah merapikan mesh), dan Anda seharusnya mendapat hasil yang bagus.

:::

### ![](/icons/tool_select.webp) Pilih {#select}
Gunakan mode bentuk (`Tali`, `Rect`, `Elips`) untuk memilih objek di adegan. `Batalkan Pilih` akan mengeluarkan objek dari seleksi.

### ![](/icons/tool_lattice.webp) Lattice {#lattice}
Mendeformasi objek dengan sangkar titik kontrol di sekelilingnya, alih-alih memahat permukaannya. Menggerakkan beberapa titik sangkar akan membengkokkan, memuntir, atau meregangkan seluruh objek dengan halus, sangat cocok untuk mengatur proporsi atau membuat pose tanpa menyentuh topologinya. Deformasinya tetap bisa diubah sampai Anda memvalidasinya.

Bilah alat kiri memilih cara Anda menyunting sangkar:

* `Titik` - Seret langsung titik dan tepi sangkar. Ketuk sebuah titik untuk memilihnya.
* `Tampilan` - Menggerakkan kamera tanpa menyunting sangkar.
* `Santai` - Kuas yang merapikan titik-titik sangkar di bawahnya.
* `Elastis` - Kuas yang menarik titik-titik sangkar dengan penurunan elastis, seperti alat [Elastis](#elastic).
* `Gizmo` - Memindahkan, memutar, dan mengubah skala titik-titik yang dipilih dengan gizmo. Mode sub-nya adalah `Poros`.
* `Tali` - Memilih titik sangkar dengan laso; `Batalkan Pilih` mengeluarkannya dari seleksi.

Popup bentuk juga berisi `Jari-jari lembut`, yang membuat seretan titik ikut menggerakkan titik-titik tetangganya (dalam satuan sel kisi; 0 hanya menggerakkan seleksi), dan `Balikkan pilihan`.

Sebuah bilah alat di bagian atas viewport berisi:

* `Finalisasi` - Menerapkan deformasi pada objek dan menghapus sangkarnya.
* `Atur ulang` - Menghapus sangkar beserta deformasinya.
* `Opasitas` - Opasitas tampilan sangkar.
* `Sisi cermin` - Dengan simetri, berganti sisi cermin sangkar mana yang ditampilkan dan bisa dipilih, dengan `Opasitas` tersendiri untuk sisi yang tersembunyi.
* `Titik grid` - Titik sangkar mana yang bisa dipindahkan: seluruh kisi, permukaan dan titik pusat, atau hanya permukaan.
* `Kekakuan` - Seberapa kaku deformasinya, dari halus (0%) sampai kaku dan linear (100%).
* `Falloff` - Seberapa jauh deformasi memudar di luar sangkar.
* `Sejajarkan` - Menyejajarkan sangkar dengan objek, atau dengan dunia.
* `X`, `Y`, `Z` `Pembagian` - Jumlah sel sangkar di setiap sumbu. Tombol mode di sebelahnya mengatur hubungan ketiganya: `x = y = z` memakai jumlah yang sama di 3 sumbu, `Seragam` menjaga jarak antar-titik tetap sama di setiap sumbu, dan `Kustom` memungkinkan Anda mengatur setiap sumbu dengan bebas.

#### Pengaturan Lattice {#lattice-settings}
* `Kecepatan putar` - Opsi putar yang sama seperti pada alat [Pindah](#move-settings), dipakai saat menyeret titik-titik sangkar.

### ![](/icons/tool_view.webp) Tampilan {#view}
"Alat" ini tidak melakukan apa-apa; ini hanyalah cara untuk melihat model tanpa mengubah adegan Anda.

#### Pengaturan Tampilan {#view-settings}
Selama alat Tampilan aktif, pengaturan ini menggantikan beberapa opsi tampilan, agar Anda mendapat tampilan bersih untuk presentasi atau memeriksa model:

* `Primitif (Sunting)`, `Pengulang (Sunting)`, `Cahaya (Sunting)`, `Kamera (Sunting)` - Mengizinkan penyuntingan primitif, pengulang, cahaya, dan kamera di viewport saat berada di alat Tampilan. Nonaktifkan agar pegangannya tidak tergeser secara tidak sengaja.
* `Pintasan kamera (selalu)` - Selalu menampilkan tombol pintasan kamera di viewport.
* `Tampilkan topeng`, `Garis tepi`, `Gelapkan objek yang tidak dipilih` - Menampilkan topeng, garis tepi objek yang dipilih, atau menggelapkan objek yang tidak dipilih. `Otomatis` mengikuti pengaturan Anda yang biasa, `Tidak` dan `Ya` memaksakannya.
* `Tampilkan garis (Simetri)`, `Tampilkan bidang (Simetri)` - Menampilkan garis atau bidang simetri, dengan pilihan `Otomatis`, `Tidak`, dan `Ya` yang sama.
* `Ikon` - Menampilkan ikon grup, pengulang, cahaya, kamera, dan hierarki di viewport, dengan pilihan yang sama.


## Menu konteks kotak peralatan {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Klik kanan atau tekan lama sebuah alat di kotak peralatan untuk memunculkan menu konteks. Menu ini berisi opsi berikut:

* `Simpan` - Menyimpan perubahan apa pun yang Anda buat pada alat
* `Kloning` - Menduplikasi alat menjadi pintasan alat baru
* `Simpanan terakhir` - Kembali ke versi alat yang terakhir disimpan
* `Ikon` - Mengganti ikon alat. Jika alat punya ikon khusus, tombol ini akan menghapusnya.
* `→ ...` - Memindahkan alat ke folder lain di kotak peralatan, atau ke folder baru
* `Setel ulang` - Mereset alat ke pengaturan bawaannya

Alat hasil kloning juga punya `Ganti nama` dan `Hapus`.
