# ![](/icons/sun.webp) Shading {#shading}

Menu ini mengontrol mode shading yang digunakan oleh Nomad, properti pencahayaan, dan properti cahaya lingkungan/matcap.

![](/images/shading_overview.webp)



Anda dapat memilih antara beberapa mode rendering:

| Mode                        | Arti                        | Deskripsi                                                      |
| :-------------------------: | :-------------------------: | :------------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Physically Based Rendering  | Melukis dengan metalness/roughness                            |
| [Matcap](#matcap)           | Material Capture            | Digunakan saat memahat dengan penggunaan gpu/cpu lebih rendah dibanding PBR |
| [Unlit](#unlit)             | Surface Color               | Hanya warna permukaan tanpa shading atau pencahayaan          |
| [Object Id](#object-id)      | Object ID                   | Warna acak per objek, berguna untuk aplikasi pengecatan       |
| [Instance Id](#instance-id)  | Instance ID                 | Warna acak per instance, berguna untuk mengidentifikasi mesh yang dibagi |

Jika Anda ingin mempelajari lebih lanjut tentang metalness dan roughness, lihat bagian [Vertex Paint](painting.md).

---

![](/images/shading_second.webp)

### Grup Muka {#face-group}
Overlay warna facegroup. Facegroup adalah seleksi poligon berwarna yang dapat dibuat dengan tool [Face group](tools#facegroup), dan dibuat secara otomatis pada sebagian besar primitif.

Beberapa tool akan otomatis memfilter berdasarkan facegroup ketika facegroup terlihat.

### Tampilkan cat {#show-paint}
Nomad dapat menyimpan color, roughness, metalness di vertex sculpt Anda. Anda dapat mengaktif/nonaktifkan tampilan properti ini secara global dengan checkbox ini.

Perhatikan bahwa jika Anda memiliki properti vertex dan tekstur sekaligus, dan keduanya diaktifkan, nilainya akan dikalikan satu sama lain.

### Tampilkan mask {#show-mask}
Mengaktif/nonaktifkan overlay mask grayscale dari [mask tools](tools#mask). Saat ini dinonaktifkan, mask juga dinonaktifkan, berguna untuk membuat perubahan cepat tanpa mask, lalu Anda dapat mengaktifkannya lagi tanpa kehilangan mask.

### Gunakan Sembunyi {#use-hide}

Mengaktif/nonaktifkan wajah yang disembunyikan. Perhatikan ini hanya berfungsi jika Anda TIDAK berada di tool hide!

### Gunakan tekstur {#use-textures}

Nomad memungkinkan tekstur ditetapkan ke objek dari menu [material](material). Jika tekstur ditetapkan, tekstur dapat diaktif/nonaktifkan secara global dengan checkbox ini.







### Ikhtisar PBR dan lampu {#pbr}
Manual ini tidak akan membahas detail tentang Physically Based Rendering.

Satu hal penting yang perlu diingat adalah bahwa pencahayaan dan material sepenuhnya terpisah.
Artinya Anda dapat melukis color, roughness, dan metalness objek Anda sementara pencahayaan ditangani secara independen.
Ini memungkinkan Anda melukis objek lalu menyetel pencahayaan nanti tanpa merusak tampilan keseluruhan model Anda.

Lampu hanya tersedia dengan [mode PBR](#pbr).
Untuk alasan performa, Anda dibatasi hanya 4 lampu.

::: tip
Anda dapat memuat file glTF dengan lebih dari 4 lampu di dalamnya dan Nomad akan mempertahankan semuanya.
Namun performanya belum tentu baik.
:::

::: tip
Anda dapat memalsukan banyak lampu dengan membuat objek unlit/emissive, lalu mengaktifkan global illumination di menu [post process](postprocess).
:::

### Ikhtisar jenis lampu {#light-types-overview}

Berikut jenis lampu yang saat ini didukung:

| Mode                        | Deskripsi                                              | Dapat membuat bayangan                                   |
| :-------------------------: | :----------------------------------------------------: | :------------------------------------------------------: |
| [Directional](#directional) | Cahaya matahari yang sangat jauh                      | ya                                                       |
| [Environment](#environment) | Cahaya jauh yang disesuaikan dengan environment HDR   | ya                                                       |
| [Spot](#spot)               | Cahaya berbentuk kerucut                              | Ya                                                       |
| [Point](#point)             | Titik cahaya omni-directional                         | Ya, tetapi hanya melalui screen-space shadow yang kurang andal |

#### Directional {#directional}
Memancarkan cahaya dari jarak tak terhingga, dengan intensitas seragam.
Posisi 3D-nya di dalam scene tidak penting, hanya orientasinya yang berpengaruh.

Anda dapat melampirkan lampu ini ke kamera, sehingga pencahayaan menjadi konsisten.  
Sebagai contoh Anda dapat menggunakannya untuk membuat rim light (cahaya kuat yang memancar dari belakang model Anda, mengarah ke kamera) yang selalu menerangi bagian belakang model Anda.

#### Cahaya lingkungan {#env-light}
Menggunakan [environment hdr](#environment) bekerja dengan baik untuk pencahayaan lembut secara keseluruhan, tetapi jika ada cahaya tajam yang kuat terlihat di HDR, bayangan yang dibuat akan sangat lembut, sering kali tidak terlihat sama sekali. Menggunakan directional light bersamaan dengan environment HDR dapat membantu, tetapi bisa sulit untuk menyelaraskannya.

Lampu ini melakukan pekerjaan itu untuk Anda. Lampu akan otomatis diputar agar sejajar dengan bagian paling terang dari HDR, lalu Anda dapat mengontrol intensitas dan sudutnya (kelembutan bayangan) secara terpisah. 

#### Spot {#spot}
Spot light memancarkan cahaya ke satu arah, dibatasi oleh bentuk kerucut.

#### Titik {#point}
Point light akan memancarkan cahaya ke segala arah.  
Saat ini, point light tidak mendukung bayangan.

#### Bayangan {#shadows}
Opsi `normal bias` dapat digunakan untuk mengurangi artefak bayangan umum (acne/peter-panning).

Kualitas bayangan bergantung pada ukuran objek relatif terhadap keseluruhan scene.  
Jika Anda memiliki objek besar di scene yang tidak perlu membuat bayangan (misalnya bidang datar besar), pastikan untuk menonaktifkan pembuatan bayangan di [pengaturan material](material.md#cast-shadows)-nya.

## Lampu {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Kotak centang Lampu {#lights-checkbox}

Mengaktif/nonaktifkan semua direct light di scene.



### Tambah lampu {#add-light}

Menambahkan lampu ke scene, hingga maksimum 4. Saat lampu ditambahkan, daftar lampu akan ditampilkan dengan tombol, dan toolbar lampu ditambahkan ke bagian atas viewport.

![](/images/shading_lights_icons.webp)

* Teks menampilkan nama lampu dan kecerahan.
* Ikon mata mengaktif/nonaktifkan visibilitas.
* Ikon pensil memungkinkan Anda mengganti nama lampu.
* Ikon tempat sampah akan menghapus lampu.
* Ikon salin akan menduplikasi lampu. 
* Ikon 3 titik akan menampilkan editor lampu lengkap. Sebagian besar fungsinya juga tersedia dari toolbar yang muncul di viewport. 

### ![](/icons/spotlight.webp)  Ikon {#icons}

Mengaktif/nonaktifkan tampilan ikon lampu di viewport

### Toolbar lampu {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Toolbar ini akan muncul di bagian atas viewport saat sebuah lampu dipilih.

* Show akan mengaktif/nonaktifkan visibilitas lampu.
* Directional/Environment/Spot/Point akan mengubah jenis lampu. Ketuk untuk berputar, atau tekan lama untuk melihat menu.
* Intensity mengontrol kekuatan lampu, nilainya dapat lebih dari 1.0 untuk lampu yang sangat kuat, berguna saat digunakan dengan Global Illumination di Post Process.
* Swatch warna ketika diklik akan menampilkan pemilih warna. Nomad menawarkan beberapa cara untuk memilih warna. Kontrol Kelvin menawarkan cara alami untuk memilih pencahayaan hangat/dingin.
* Shadow akan mengaktif/nonaktifkan bayangan.
* Size mengatur lebar lampu. Lampu yang lebih lebar akan menghasilkan bayangan lembut, pencahayaan lembut, dan highlight yang lebih lembut pada objek.
* ... akan menampilkan kontrol tambahan.

### Kontrol ekstra lampu {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Perhatikan bahwa beberapa opsi spesifik untuk jenis lampu tertentu.

* `Clone` akan menduplikasi lampu.
* `Recenter` akan memindahkan lampu kembali ke origin.
* `Delete` akan menghapus lampu.
* `Directional/Environment/Spot/Point` memungkinkan Anda mengubah jenis lampu.
* `colour swatch` ketika diklik akan menampilkan pemilih warna. 
* `Intensity` mengontrol kekuatan lampu.
* `Attachment` (_hanya directional_) akan mengatur lampu agar diparent ke world, atau diparent ke kamera. Misalnya jika Anda menggunakan directional light di belakang karakter sebagai rim light, ketika attachment sebagai camera dipilih, memutar kamera akan selalu membuat lampu berada di belakang karakter.
* `Angle` (_hanya directional dan environment_) adalah ukuran tampak lampu, anggap saja seberapa besar matahari tampak di langit. Sudut yang lebih besar akan menghasilkan bayangan lebih lembut dan highlight lebih lebar.
* `Softness` (_hanya spotlight_) mengontrol ketajaman tepi kerucut spotlight. 0 adalah tepi yang sangat tajam. 1 sangat lembut, dengan gradasi ke tengah kerucut cahaya. Di viewport, titik biru kecil pada kerucut spotlight dapat digunakan untuk mengatur softness secara interaktif.
* `Cone angle` (_hanya spotlight_) mengontrol sudut sebaran spotlight. Sudut kecil adalah berkas cahaya yang sangat tipis, 170 adalah sebaran cahaya yang sangat lebar. Di viewport, titik oranye dapat digunakan untuk mengatur cone angle secara interaktif.
* `Shadow` akan mengaktif/nonaktifkan bayangan untuk lampu saat ini.
* `Shadow map` dan `screenspace` adalah cara berbeda untuk menghitung bayangan, umumnya shadow map lebih andal.
* `Contact` menyesuaikan bagaimana bayangan dihitung. Bayangan adalah masalah sulit dalam grafik komputer, dan dapat menyebabkan artefak dalam rendering. Bayangan yang lebih akurat dapat dipilih untuk lampu terpenting di scene, kontrol ini menentukan apakah lampu terpenting dipilih secara otomatis oleh Nomad, atau oleh pengguna.
* `Tolerance` jika artefak bayangan terlihat (baik bayangan tampak tidak menyentuh permukaan, atau ada noise dan pola di dalam bayangan), menyetel tolerance dapat membantu memperbaiki masalah tersebut.


## Lingkungan {#environment}

![](/images/shading_environment.webp)

Cahaya di dunia nyata datang dari segala arah; birunya langit, hijaunya rumput, merahnya bangunan, semua cahaya dari 'environment' ini dapat disimulasikan dengan environment map. 

Nomad menyertakan beberapa contoh environment map untuk area indoor dan outdoor, dengan tint dan tingkat kecerahan berbeda. Cobalah berbagai map untuk melihat mana yang paling menonjolkan detail sculpt Anda.

Ketuk gambar untuk melihat environment map yang tersedia. Dari dialog tersebut pilih 'Import...' untuk memuat milik Anda sendiri. Sebaiknya gunakan gambar High Dynamic Range (HDR), dalam format latlong atau equirectangular, sebagai file .hdr atau .exr. [www.polyhaven.com](https://polyhaven.com/hdris) memiliki koleksi environment map gratis yang bagus untuk digunakan, umumnya map hdr 1k adalah ukuran dan kualitas yang baik.

### Eksposur {#env-exposure}
Mengatur kecerahan environment map. Sering kali map bisa terlalu terang saat digunakan dengan lampu biasa, menurunkan exposure dapat membantu menyeimbangkan, terutama saat digunakan dengan Global Illumination di pengaturan [Post Process](postprocess).

### Rotasi {#env-rotation}

Karena environment map menangkap cahaya dari segala arah, Anda dapat memutarnya untuk mendapatkan pantulan dan pencahayaan keseluruhan yang berpadu baik dengan sculpt Anda.

### Terpasang ke kamera {#env-attached}
Melampirkan environment ke kamera.

Ini akan memaksa pencahayaan menjadi konsisten, yang bisa berguna saat memahat.


## ![](/icons/sphere_smooth.webp) Matcap {#matcap}

![](/images/shading_matcap.webp)

Seperti namanya (MATerial CAPture), matcap menangani informasi pencahayaan dan material dalam satu gambar.
Karena material itu sendiri sudah ada di matcap, channel pengecatan roughness dan metalness akan diabaikan.
Warna pengecatan akan dikalikan dengan matcap, artinya jika Anda memiliki matcap hitam/abu-abu, menggunakan cat putih tidak akan membuatnya lebih terang.

Seniman cenderung menyukai mode ini untuk keperluan sculpting karena memungkinkan mereka fokus pada bentuk dan geometri itu sendiri.

Mengetuk sphere akan menampilkan image browser. Anda juga dapat menambahkan matcap Anda sendiri, umumnya foto apa pun, render, bahkan lukisan sebuah sphere yang dipotong rapat menjadi persegi dapat digunakan. Banyak pustaka matcap tersedia online, salah satu sumber yang berguna adalah [nidorx matcap library](https://github.com/nidorx/matcaps).

### Gunakan Matcap global {#matcap-global}

Biasanya seniman akan menggunakan satu matcap untuk seluruh sculpt, tetapi jika toggle ini dinonaktifkan, setiap objek dapat memiliki matcap sendiri. Ini dapat digunakan secara artistik untuk mendapatkan hasil yang mencolok.

::: tip
Nonaktifkan opsi ini, dan gunakan gambar bola mata untuk mata karakter Anda!
:::

### Rotasi {#matcap-rotation}
Matcap adalah bentuk khusus dari environment map, jadi seperti environment map, matcap dapat diputar. Anda juga dapat melakukannya kapan saja di viewport dengan menyeret menggunakan 3 jari ke kiri dan kanan.



## ![](/icons/circle_fill.webp) Tanpa cahaya {#unlit}

Mode ini hanya akan menampilkan warna permukaan. Ini dapat berguna untuk memeriksa apakah warna permukaan objek Anda sesuai harapan, tanpa terganggu oleh lampu, bayangan, refleksi, transparansi. 

Mode ini juga dapat digunakan untuk render non-fotorealistik, menghasilkan tampilan datar dan kartun.

## ![](/icons/cube.webp) ID Objek {#object-id}

Semua informasi pencahayaan dan permukaan diabaikan, dan setiap objek diarsir dengan warna flat unik. Jika ini dirender bersamaan dengan render PBR, ini dapat digunakan di program pengecatan untuk memilih berdasarkan warna, dan dengan demikian dapat melakukan koreksi warna pada objek tertentu.

Perhatikan bahwa warna-warna ini juga akan muncul di [tree view menu Scene](scene#tree-view).

### Acak id {#object-random}

Menghasilkan set warna acak baru. 

## ![](/icons/link.webp) ID Instance {#instance-id}

Sama seperti Object ID, tetapi instance akan memiliki warna yang sama. 

### Acak id {#instance-random}

Menghasilkan set warna acak baru.