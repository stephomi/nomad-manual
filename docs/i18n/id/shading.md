# ![](/icons/sun.webp) Shading {#shading}

Menu ini mengatur mode shading yang dipakai Nomad, properti pencahayaan, lingkungan dan matcap, serta kabut.

![](/images/shading_overview.webp)



Anda bisa memilih di antara beberapa mode rendering:

| Mode                        | Arti                       | Deskripsi                                                       |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Terang (PBR)](#pbr)        | Physically Based Rendering | Cahaya, bayangan, lingkungan, serta metalness/roughness yang dicat |
| [MatCap](#matcap)           | Material Capture           | Mode cepat untuk memahat, dengan penggunaan gpu/cpu lebih rendah dari PBR |
| [Tanpa pencahayaan](#unlit) | Warna permukaan            | Hanya warna permukaan, tanpa shading atau pencahayaan           |
| [ID Objek](#object-id)      | ID Objek                   | Warna acak per objek, berguna untuk aplikasi lukis.             |
| [ID Instansi](#instance-id) | ID Instansi                | Warna acak per instans, berguna untuk mengenali mesh yang dipakai bersama |

Jika Anda ingin mempelajari lebih lanjut tentang metalness dan roughness, lihat bagian [Lukis](painting.md).

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) Grup Face {#face-group}
Menampilkan warna grup face di atas model. Grup face adalah kumpulan poligon berwarna yang bisa dibuat dengan alat [Grup Face](tools#facegroup), dan dibuat secara otomatis pada sebagian besar primitif.

Beberapa alat akan otomatis menyaring berdasarkan grup face saat grup face terlihat.

### ![](/icons/palette.webp) Tampilkan lukisan {#show-paint}
Nomad bisa menyimpan warna, roughness, dan metalness di verteks pahatan Anda. Anda bisa menyalakan atau mematikan tampilan properti ini secara global dengan kotak centang ini.

Perlu diingat, jika Anda punya properti verteks sekaligus tekstur, dan keduanya diaktifkan, nilainya akan dikalikan.

### ![](/icons/shield.webp) Tampilkan topeng {#show-mask}
Menyalakan atau mematikan lapisan masker skala abu-abu dari [alat masker](tools#mask). Jika dinonaktifkan, masker juga ikut nonaktif. Ini berguna untuk membuat perubahan cepat tanpa masker, lalu Anda bisa mengaktifkannya lagi tanpa kehilangan masker Anda.

### ![](/icons/tool_hide.webp) Gunakan Sembunyikan {#use-hide}

Menyalakan atau mematikan face yang disembunyikan. Perlu diingat, ini hanya bekerja jika Anda TIDAK sedang memakai alat sembunyi!

### ![](/icons/image.webp) Gunakan tekstur {#use-textures}

Nomad memungkinkan tekstur dipasang ke objek dari menu [Material](material). Jika tekstur sudah dipasang, Anda bisa menyalakan atau mematikannya secara global dengan kotak centang ini.

Anda tidak bisa membuat atau menyunting tekstur di dalam Nomad, tetapi tekstur dari file yang diimpor bisa dipakai. Tekstur opasitas bekerja di Terang, MatCap dan Tanpa pencahayaan, normal map di Terang dan MatCap, warna di Terang dan Tanpa pencahayaan, sedangkan emisif, roughness dan metalness hanya di Terang. Tombolnya berwarna abu-abu jika adegan tidak punya tekstur.

### Ikhtisar PBR dan cahaya {#pbr}
Manual ini tidak akan membahas detail Physically Based Rendering.

Satu hal penting yang perlu diingat: pencahayaan dan material sepenuhnya terpisah.
Artinya, Anda bisa mengecat warna, roughness dan metalness objek sementara pencahayaannya diatur secara terpisah.
Dengan begitu, Anda bisa mengecat objek lalu menyesuaikan pencahayaan belakangan, tanpa merusak tampilan keseluruhan model Anda.

Cahaya, lingkungan dan kabut hanya tersedia dalam [mode PBR](#pbr).
Demi kinerja, Anda dibatasi 4 cahaya di perangkat seluler dan 6 di desktop.

::: tip
Anda bisa memuat file glTF yang berisi lebih banyak cahaya, dan Nomad akan mempertahankan semuanya.
Namun kinerjanya belum tentu bagus.
:::

::: tip
Anda bisa meniru banyak cahaya dengan membuat objek tanpa pencahayaan/emisif, lalu mengaktifkan pencahayaan global di menu [PascaProses](postprocess).
:::

### Ikhtisar jenis cahaya {#light-types-overview}

Berikut jenis cahaya yang saat ini didukung:

| Mode                        | Deskripsi                                               | Bisa membuat bayangan |
| :-------------------------: | :-----------------------------------------------------: | :--------------: |
| [Arah](#directional)        | Cahaya matahari yang sangat jauh tak terhingga          | Ya               |
| [Lingkungan](#env-light)    | Cahaya jauh yang diselaraskan dengan HDR lingkungan     | Ya               |
| [Lampu sorot](#spot)        | Cahaya berbentuk kerucut                                | Ya               |
| [Lampu titik](#point)       | Titik cahaya ke segala arah                             | Ya               |

#### ![](/icons/sun.webp) Arah {#directional}
Memancarkan cahaya dari jarak yang sangat jauh tak terhingga, dengan intensitas yang merata.
Posisi 3d-nya di adegan tidak berpengaruh, hanya orientasinya yang penting.

Anda bisa menautkan cahaya ini ke kamera, sehingga pencahayaannya selalu konsisten.  
Misalnya, Anda bisa memakainya untuk membuat rim light (cahaya kuat yang datang dari belakang model, mengarah ke kamera) yang selalu menerangi bagian belakang model Anda.

#### ![](/icons/panorama.webp) Cahaya lingkungan {#env-light}
Memakai [HDR lingkungan](#environment) cocok untuk pencahayaan lembut secara keseluruhan, tetapi jika ada cahaya kuat dan tajam di HDR, bayangan yang dihasilkannya akan sangat lembut, bahkan sering tidak terlihat sama sekali. Menggabungkan cahaya arah dengan HDR lingkungan bisa membantu, tetapi menyelaraskan keduanya bisa cukup sulit.

Cahaya ini melakukannya untuk Anda. Cahaya akan otomatis diputar agar sejajar dengan bagian paling terang dari HDR, lalu Anda bisa mengatur intensitas dan sudutnya (kelembutan bayangan) secara terpisah. 

#### ![](/icons/spotlight.webp) Lampu sorot {#spot}
Lampu sorot memancarkan cahaya ke satu arah, dibatasi oleh bentuk kerucut.

#### ![](/icons/light.webp) Lampu titik {#point}
Lampu titik memancarkan cahaya ke segala arah, dan juga bisa membuat bayangan.

#### Bayangan {#shadows}
Setiap cahaya bisa membuat bayangan, dan Anda bisa memilih cara bayangannya dihitung di [pengaturannya](#light-extra-controls). Jika Anda melihat artefak bayangan, penggeser `Toleransi` di sana bisa membantu.

Kualitas bayangan bergantung pada ukuran objek dibandingkan dengan seluruh adegan.  
Jika ada objek besar di adegan Anda yang tidak perlu membuat bayangan (misalnya bidang datar yang besar), pastikan untuk menonaktifkan pembuatan bayangan di [pengaturan materialnya](material.md#casts-shadows).

## ![](/icons/sun.webp) Cahaya {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Kotak centang Cahaya {#lights-checkbox}

Menyalakan atau mematikan semua cahaya langsung di adegan.



### Tambah cahaya {#add-light}

Menambahkan cahaya ke adegan, hingga 4 cahaya di perangkat seluler dan 6 di desktop. Saat cahaya ditambahkan, daftar cahaya ditampilkan beserta tombol-tombolnya, dan bilah alat cahaya muncul di bagian atas viewport.

![](/images/shading_lights_icons.webp)

* Teksnya menampilkan nama cahaya dan tingkat kecerahannya. Ketuk untuk memilih cahaya.
* Ikon mata menyalakan atau mematikan visibilitas.
* Ikon pensil memungkinkan Anda mengganti nama cahaya.
* Ikon tempat sampah menghapus cahaya.
* Ikon salin menduplikasi cahaya. 
* Ikon 3 titik membuka editor cahaya lengkap. Sebagian besar fungsinya juga tersedia di bilah alat yang muncul di viewport. 

Anda juga bisa menyeret cahaya di daftar untuk mengubah urutannya.

### ![](/icons/spotlight.webp)  Ikon {#icons}

Menyalakan atau mematikan tampilan ikon cahaya di viewport

### Bilah alat cahaya {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Bilah alat ini muncul di bagian atas viewport saat sebuah cahaya dipilih.

* `Tampak` menyalakan atau mematikan visibilitas cahaya.
* Arah/Lingkungan/Sorot/Titik mengubah jenis cahaya. Ketuk untuk berganti secara bergiliran, atau tekan lama untuk melihat menunya.
* Intensitas mengatur kekuatan cahaya; nilainya bisa melebihi 1,0 untuk cahaya yang sangat kuat, berguna saat dipakai bersama Pencahayaan Global di PascaProses
* Kotak warna, jika diklik, membuka pemilih warna. Nomad menyediakan beberapa cara untuk memilih warna. Kontrol Kelvin memberi cara alami untuk memilih pencahayaan hangat/dingin.
* Bayangan menyalakan atau mematikan bayangan.
* Sudut (_arah dan lingkungan_) atau Ukuran (_sorot dan titik_) mengatur lebar cahaya. Cahaya yang lebih lebar menghasilkan bayangan lembut, pencahayaan lembut, dan pantulan cahaya yang lebih lembut pada objek.
* Lampiran (_khusus arah_), Sudut kerucut dan Kelembutan (_khusus sorot_) dijelaskan di [editor cahaya](#light-extra-controls) di bawah.
* ... memunculkan `Kloning`, `Pusatkan ulang` dan `Hapus`, beserta pengaturan bayangan.

### Kontrol tambahan cahaya {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Ikon 3 titik pada cahaya di daftar membuka editor lengkapnya. Perlu diingat bahwa beberapa opsi khusus untuk jenis cahaya tertentu.

* `Arah/Lingkungan/Titik` memungkinkan Anda mengubah jenis cahaya (lampu sorot dan lampu titik sama-sama bernama `Titik`).
* `Kotak warna`, jika diklik, membuka pemilih warna. 
* `Intensitas` mengatur kekuatan cahaya.
* `Lampiran` (_khusus arah_) menautkan cahaya ke dunia (`Tetap`), atau ke kamera (`Kamera`). Misalnya, jika Anda memakai cahaya arah di belakang karakter sebagai rim light, dengan lampiran kamera dipilih, cahaya akan selalu berada di belakang karakter saat kamera diputar.
* `Kelembutan` (_khusus lampu sorot_) mengatur ketajaman tepi kerucut lampu sorot. 0 berarti tepi yang sangat tajam. 1 sangat lembut, dengan gradasi ke arah tengah kerucut cahaya. Di viewport, titik biru kecil pada kerucut lampu sorot bisa dipakai untuk mengatur kelembutan secara interaktif.
* `Sudut kerucut` (_khusus lampu sorot_) mengatur sudut sebaran lampu sorot. Sudut kecil berarti berkas cahaya yang sangat tipis, 170 berarti sebaran cahaya yang sangat lebar. Di viewport, titik oranye bisa dipakai untuk mengatur sudut kerucut secara interaktif.
* `Sudut` (_khusus arah dan lingkungan_) adalah ukuran semu cahaya; bayangkan seberapa besar matahari tampak di langit. Sudut yang lebih besar menghasilkan bayangan lebih lembut dan pantulan cahaya lebih lebar.
* `Ukuran` (_khusus sorot dan titik_) adalah lebar cahaya. Cahaya yang lebih besar menghasilkan bayangan lebih lembut.
* `Bayangan` menyalakan atau mematikan bayangan untuk cahaya ini.
* Jenis bayangan menentukan cara bayangan dihitung. `Peta bayangan` merender adegan dari sudut pandang cahaya, sehingga juga membayangi geometri yang tidak terlihat oleh kamera. `Ruang layar` hanya memakai apa yang sudah terlihat di layar: lebih ringan, tetapi masih eksperimental. Umumnya peta bayangan lebih andal.
* `Toleransi` (_khusus ruang layar_): jika terlihat artefak bayangan (bayangan tampak tidak menyentuh permukaan, atau ada noise dan pola di dalam bayangan), menyesuaikan toleransi bisa membantu mengatasinya.
* `Kontak` menambahkan bayangan yang lebih presisi pada jarak pendek, di tempat objek saling bersentuhan. Dengan `Otomatis`, hanya cahaya yang paling dominan di adegan yang mendapat bayangan kontak; `Tidak` dan `Ya` memaksa fitur ini mati atau menyala untuk cahaya ini. Penggeser `Toleransi`-nya bekerja seperti yang di atas.

Tombol `...` pada bilah alat viewport berisi pengaturan bayangan yang sama, ditambah:

* `Kloning` menduplikasi cahaya.
* `Pusatkan ulang` memindahkan cahaya ke depan kamera, dengan tetap mempertahankan orientasinya.
* `Hapus` menghapus cahaya.


## ![](/icons/panorama.webp) Lingkungan {#environment}

![](/images/shading_environment.webp)

Di dunia nyata, cahaya datang dari segala arah: birunya langit, hijaunya rumput, merahnya sebuah gedung. Semua cahaya dari 'lingkungan' ini bisa disimulasikan dengan peta lingkungan. 

Gunakan kotak centang di sebelah judul untuk menyalakan atau mematikan pencahayaan lingkungan.

Nomad menyertakan beberapa contoh peta lingkungan untuk ruang dalam dan luar, dengan warna dan tingkat kecerahan yang berbeda-beda. Cobalah berbagai peta untuk melihat mana yang paling menonjolkan detail pahatan Anda.

Ketuk gambarnya untuk melihat peta lingkungan yang tersedia. Dari dialog itu, pilih `Impor...` untuk memuat peta Anda sendiri. Sebaiknya gunakan gambar High Dynamic Range (HDR), dalam format latlong atau equirectangular, berupa file .hdr atau .exr. Penjelajahnya juga bisa mengunduh lingkungan langsung dari [Poly Haven](https://polyhaven.com/hdris), yang punya koleksi peta lingkungan gratis yang bagus.

### Eksposur {#env-exposure}
Mengatur kecerahan peta lingkungan. Peta sering kali terlalu terang jika dipakai bersama cahaya biasa; menurunkan eksposur bisa membantu menyeimbangkannya, terutama saat dipakai bersama Pencahayaan Global di pengaturan [PascaProses](postprocess).

### Rotasi {#env-rotation}

Karena peta lingkungan menangkap cahaya dari segala arah, Anda bisa memutarnya agar pantulan dan pencahayaan keseluruhan berpadu dengan baik dengan pahatan Anda. Anda juga bisa memutar lingkungan dengan menyeret 3 jari secara horizontal di viewport.

### Tautkan ke kamera {#env-attached}
Menautkan lingkungan ke kamera.

Ini membuat pencahayaan selalu konsisten, yang bisa berguna selama memahat.

### Blur (latar belakang) {#env-background-blur}
Penggeser ini hanya muncul jika [latar belakang](background.md) diatur ke lingkungan. Penggeser ini memburamkan gambar lingkungan di belakang model Anda, tanpa mengubah pencahayaannya.


## ![](/icons/fog.webp) Kabut {#fog}

Kabut menambahkan kedalaman atmosfer pada adegan Anda dan membuat berkas cahaya terlihat. Aktifkan dengan kotak centang di sebelah judul. Seperti cahaya dan lingkungan, kabut hanya tersedia dalam mode [Terang (PBR)](#pbr).

::: tip Berkas cahaya yang lebih kuat
Turunkan `Lingkungan` kabut, lalu gunakan lampu sorot atau lampu titik yang terang. Naikkan `Kepadatan` sampai kabut terlihat jelas. Untuk berkas cahaya yang terlihat di kabut yang lebih tipis, atur `Arah Hamburan` ke nilai positif yang tinggi dan arahkan kamera ke cahaya.
:::

### Warna {#fog-color}
Warna kabut dan warna cahaya yang dihamburkannya.

### Kepadatan {#fog-density}
Seberapa cepat kabut menebal seiring jarak.

### Opasitas Maksimum {#fog-opacity}
Membatasi seberapa banyak kabut bisa menutupi adegan, bahkan pada kepadatan tinggi.

### Arah Hamburan {#fog-scattering}
Arah kabut menghamburkan cahaya (disebut juga anisotropi). Nilai positif membuat kabut lebih terang saat Anda melihat ke arah cahaya, nilai negatif saat Anda melihat menjauhinya, dan nol menghamburkan cahaya secara merata ke segala arah.

### ![](/icons/panorama.webp) Lingkungan {#fog-environment}
Seberapa banyak [lingkungan](#environment) menerangi kabut. Opsi ini berwarna abu-abu jika lingkungan dimatikan.

### Derau {#fog-noise}
Mencampurkan derau ke dalam kabut untuk memecahnya menjadi gumpalan-gumpalan, tanpa mengubah kepadatan keseluruhannya. Jika derau di atas 0, penggeser `Ukuran` mengatur ukuran polanya.

### Bentuk {#fog-shape}
Bagian adegan yang diisi kabut:

* `Seragam` - mengisi seluruh adegan.
* `Vertikal` - menjaga kabut di dalam pita vertikal dengan tepi yang lembut. Penggeser `Bawah` dan `Atas` mengatur ketinggian tepi bawah dan atasnya, dan tombol mata di sebelahnya menampilkan pita itu di viewport selama Anda menyesuaikannya.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

Sesuai namanya (MATerial CAPture), matcap menangani informasi pencahayaan sekaligus material dalam satu gambar.
Karena materialnya sudah ada di dalam matcap, kanal cat roughness dan metalness akan diabaikan.
Warna cat akan dikalikan dengan matcap, artinya jika Anda memakai matcap hitam/abu-abu, cat putih tidak akan membuatnya lebih terang.

Para seniman cenderung memilih mode ini untuk memahat, karena mereka bisa fokus pada bentuk dan geometrinya saja.

Mengetuk bola akan membuka penjelajah gambar. Anda juga bisa menambahkan matcap sendiri; umumnya foto, render, bahkan lukisan sebuah bola apa pun yang dipotong rapat menjadi persegi bisa dipakai. Banyak pustaka matcap tersedia secara online, salah satu sumber yang berguna adalah [pustaka matcap nidorx](https://github.com/nidorx/matcaps).

### Gunakan MatCap global {#matcap-global}

Biasanya seniman memakai satu matcap untuk seluruh pahatan, tetapi jika opsi ini dinonaktifkan, objek yang dipilih bisa punya matcap sendiri. Ini bisa dimanfaatkan secara artistik untuk mendapatkan hasil yang mencolok.

::: tip
Nonaktifkan opsi ini, lalu gunakan gambar bola mata untuk mata karakter Anda!
:::

### Rotasi {#matcap-rotation}
Matcap adalah bentuk khusus dari peta lingkungan, jadi seperti peta lingkungan, matcap bisa diputar. Anda juga bisa melakukannya kapan saja di viewport dengan menyeret 3 jari ke kiri dan ke kanan.

Tombol gembok di sebelah penggeser mengunci rotasinya, sehingga seretan 3 jari tidak memutar matcap secara tidak sengaja.



## ![](/icons/circle_fill.webp) Tanpa pencahayaan {#unlit}

Mode ini hanya menampilkan warna permukaan. Berguna untuk memeriksa apakah warna permukaan objek Anda sudah sesuai harapan, tanpa terganggu oleh cahaya, bayangan, pantulan, atau transparansi. 

Mode ini juga bisa dipakai untuk render non-fotorealistis, untuk mendapatkan tampilan datar ala kartun.

## ![](/icons/cube.webp) ID Objek {#object-id}

Semua informasi pencahayaan dan permukaan diabaikan, dan setiap objek diberi satu warna datar yang unik. Jika ini dirender bersama render PBR, hasilnya bisa dipakai di program lukis untuk memilih berdasarkan warna, sehingga Anda bisa melakukan koreksi warna pada objek tertentu.

Perlu diingat bahwa warna-warna ini juga muncul di [tampilan pohon menu Adegan](scene#tree-view).

### Acak id {#object-random}

Membuat sekumpulan warna acak yang baru. 

## ![](/icons/link.webp) ID Instansi {#instance-id}

Sama seperti ID Objek, tetapi instans akan memiliki warna yang sama. 

### Acak id {#instance-random}

Membuat sekumpulan warna acak yang baru.
