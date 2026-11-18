# ![](/icons/paint.webp) Lukis {#painting}

Mengatur warna, kekasaran, dan kemetalan goresan cat, mengisi seluruh objek dengan atribut cat, serta bagaimana alat cat berinteraksi dengan lapisan, topeng, dan area yang disembunyikan.

![](/images/paint_overview.webp)  

## Ikhtisar {#overview}

Nomad memakai pengecatan verteks PBR. Apa artinya?

### PBR {#pbr}
PBR, atau Physically Based Rendering, adalah teknik grafis komputer yang populer untuk film, televisi, game, dan perangkat seluler. Dengan mendasarkan pencahayaan pada sifat-sifat fisik, dan mendefinisikan permukaan melalui warna, kekasaran, dan kemetalan, beragam tampilan fotorealistis bisa dicapai.

### Pengecatan verteks {#vertex-painting}

Pengecatan verteks berarti informasi cat disimpan di verteks model, bukan di tekstur. Karena Nomad mampu menangani model dengan ratusan ribu, bahkan sering jutaan verteks, model Anda bisa memiliki cat permukaan yang sangat detail; jika Anda bisa memahat detailnya, Anda juga bisa mengecat detail itu.

Ini juga berarti mengecat di Nomad tidak memerlukan pemetaan UV, yang di aplikasi 3d lain sering kali merupakan proses yang lambat dan teknis. Banyak aplikasi 3d lain tidak mendukung jumlah verteks setinggi yang bisa ditangani Nomad, tetapi Nomad juga punya alat bake tekstur dan desimasi yang bagus untuk membantu.

### Tekstur {#texturing}

Nomad mendukung tekstur, tetapi tekstur itu harus sudah ada di model yang diimpor, atau didapat dengan mem-bake pengecatan verteks ke tekstur. 

Tekstur hanyalah sebuah gambar, tetapi dalam konteks 3d biasanya yang dimaksud adalah gambar yang ditetapkan ke sebuah objek.
Agar gambar bisa membungkus model, model memerlukan koordinat tekstur (UV).

Nomad bisa menghitung [koordinat itu secara otomatis](topology.md#uv-unwrap), tetapi Anda tidak punya banyak kendali atas kualitas keseluruhannya.

::: tip
Salah satu contoh alur kerja:
- Pahat di Nomad, lalu lakukan [UV unwrap](topology.md#uv-unwrap)
- Jika Anda sudah mulai mengecat di Nomad, Anda bisa [memindahkan pengecatan verteks ke tekstur](topology.md#bake-texture)
- Ekspor ke Procreate
- Buat tekstur di Procreate
- Ekspor kembali ke Nomad untuk keperluan render
:::

Itulah gambaran umumnya, sekarang mari kita jelajahi bagian-bagian menu lukis:


## Lukisan garis {#stroke-painting}
![](/images/paint_intensity.webp)  

Mengaktifkan pengecatan untuk alat ini, berguna jika Anda perlu memahat dan mengecat sekaligus. Jika sebuah alat bisa mengecat tetapi kotak centang ini mati, ikon peringatan di sebelah judul akan mengingatkan Anda.

Untuk alat yang fungsi utamanya mengecat (misalnya Melukis, Smudge, Topeng), kotak centang ini tidak ada.

### ![](/icons/opacity.webp) Intensitas lukisan {#paint-intensity}

Penggeser yang memungkinkan Anda memakai intensitas yang berbeda dari intensitas utama alat.

Tombol penggeser di sebelahnya menambahkan penggeser intensitas cat cepat ke bilah samping, untuk alat yang memahat dan mengecat sekaligus.

Tombol `Alpha`, `Penurunan` dan `Acak intensitas` menentukan apakah fitur-fitur tersebut memengaruhi pengecatan. Misalnya, Anda bisa mengaktifkan pengacakan untuk alat tanah liat, tetapi warnanya tidak ikut diacak.

* `Alpha` - jika dinonaktifkan, pengecatan mengabaikan alpha dan menutupi seluruh area kuas. Pada alat VDM, tombol ini diganti dengan `Material stempel`, yang mengaktifkan atau menonaktifkan material yang tersimpan di stempel.
* `Penurunan` - jika dinonaktifkan, pengecatan tetap berintensitas penuh hingga ke tepi kuas.
* `Acak intensitas` - apakah bagian intensitas dari pengacak goresan memengaruhi pengecatan. Pengacakan posisi, rotasi, dan skala selalu memindahkan seluruh stempel.

Opsi-opsi ini diabaikan oleh [Lukis semua](#paint-all), tetapi alpha tetap dipakai oleh varian triplanarnya.

### ![](/icons/link.webp) Material global {#global-material}
Jika opsi ini diaktifkan, material yang dipilih akan sama dengan alat lainnya. Perhatikan bahwa ini hanya memperhitungkan pengaturan kekasaran, kemetalan, dan warna. Nonaktifkan untuk memberi alat ini materialnya sendiri.


## Material {#material}
![](/images/paint_material.webp) 

Ikon pertama adalah bentuk pratinjau material. Menyeret pada pratinjau material 3d akan memutarnya. 

Ikon kedua adalah pratinjau goresan cat dengan opsi alpha dan penurunan yang dipilih.

### ![](/icons/falloff.webp) Kurva {#curves}

Membuka editor kurva untuk slot tekstur pada [penggeser PBR](#pbr-sliders). Editor ini memetakan ulang nilai tekstur sebelum dicatkan, tanpa menyentuh file gambarnya. Ikon kurva kecil pada slot tekstur memberi tahu Anda bahwa kurvanya telah diubah.

### ![](/icons/cog.webp) Opsi material {#material-options}

Tombol `Material` di sebelah judul menyimpan dua pengaturan.

`Pratinjau tampilan material` menentukan apa yang terjadi pada objek yang dipilih saat Anda mengubah penggeser warna, kekasaran, kemetalan, opasitas, dan intensitas:

* `Tidak ada` - Tidak ada pratinjau yang ditampilkan pada model saat Anda mengatur properti
* `Material` - Nilai material ditampilkan sebagai pratinjau pada objek saat Anda mengatur properti.
* `Triplanar` - Material ditampilkan sebagai pratinjau dengan proyeksi Triplanar. 

Kotak centang warna, kekasaran, kemetalan, dan opasitas di bawahnya menentukan kanal mana yang diganti oleh [Pemilih material](#material-picker).

### ![](/icons/dropper.webp) Pemilih material {#material-picker}

Pipet mengambil material di bawah kursor, dari objek mana pun di adegan Anda. Hanya kanal yang dicentang di [Opsi material](#material-options) yang diganti.

## Preset material {#material-presets}
Mengetuk bentuk pratinjau 3d akan memunculkan menu preset material; preset ini bisa dikloning untuk membuat preset Anda sendiri.

![](/images/paint_presets.webp) 

Sakelar `Sematkan tekstur` menyimpan salinan tekstur yang dipakai material ini di dalam preset. Tanpa opsi ini, preset hanya merujuk ke tekstur di folder textures/ Nomad. Aktifkan jika Anda ingin membagikan preset bertekstur tanpa harus mengirim teksturnya secara terpisah.

`Sertakan Alpha` juga menyimpan alpha kuas di dalam preset material.

## Penggeser PBR {#pbr-sliders}
![](/images/paint_sliders.webp) 

Pengecatan [PBR](shading.md#pbr) memakai 4 kanal:
- `Warna` Warna yang akan dicatkan. Pipet bisa dipakai untuk mengambil warna dari bagian lain model, atau dari gambar referensi.
- `Kekasaran` Menunjukkan seberapa "kasar" atau "halus" sebuah permukaan. Nilai kekasaran yang rendah berarti pantulannya tajam.
- `Kemetalan` Sekadar menunjukkan apakah permukaan itu logam atau bukan. Nilainya sebaiknya 0% atau 100% hampir di setiap kasus; nilai di antaranya seharusnya merupakan pengecualian.
- `Opasitas` Seberapa tembus pandang material tersebut. Secara ketat, ini bukan bagian dari spesifikasi PBR, tetapi berguna dalam banyak situasi. 1 berarti sepenuhnya buram, 0 berarti transparan. Perhatikan bahwa opasitas dan refraksi adalah dua hal yang berbeda; refraksi di Nomad ditangani oleh material refraksi. 

Jika Anda memilih preset material, 3 kanal dicatkan sekaligus (opasitas sering kali sengaja dikecualikan). Artinya, alih-alih hanya mengecat 'merah', Anda bisa mengecat 'logam merah yang kasar' atau 'plastik putih yang halus'.

Kotak persegi adalah slot tekstur; klik untuk memakai tekstur bagi properti itu, bukan nilai tunggal. Tekstur warna akan mewarnai warnanya, sedangkan tekstur kekasaran, kemetalan, atau opasitas menggantikan nilai penggeser (labelnya dicoret untuk menunjukkan hal ini). Untuk tekstur opasitas, `Gunakan Alpha sebagai Nilai` membaca kanal alpha tekstur, bukan nilai skala abu-abunya.

Pada alat VDM, jika stempel membawa materialnya sendiri, sebuah slot tambahan menampilkannya di sebelah slot tekstur. Ketuk untuk memakai atau mengabaikan kanal stempel tersebut.

Ikon kuas di sebelah penggeser akan mengisi seluruh objek Anda dengan properti tersebut.

Kotak centang akan mengaktifkan atau menonaktifkan properti tertentu, jadi Anda bisa, misalnya, hanya mengecat warna, atau hanya mengecat kekasaran dan opasitas. 

Berikut beberapa contoh properti kekasaran dan kemetalan yang berbeda:

|                | Kemetalan 0%                      | Kemetalan 100%               |
| :------------: | :-------------------------------: | :--------------------------: |
| Kekasaran 0%   | ![](/images/dielectric_r0.webp)   | ![](/images/metal_r0.webp)   |
| Kekasaran 50%  | ![](/images/dielectric_r50.webp)  | ![](/images/metal_r50.webp)  |
| Kekasaran 100% | ![](/images/dielectric_r100.webp) | ![](/images/metal_r100.webp) |

::: warning
Kekasaran dan kemetalan memerlukan mode shading [Terang (PBR)](shading.md#pbr). Dalam mode [MatCap](shading.md#matcap) atau [Tanpa pencahayaan](shading.md#unlit), keduanya diabaikan, dan menu menampilkan peringatan.
:::

::: tip
Saat memakai tekstur untuk pengecatan PBR, sering kali berguna untuk beralih ke alat seperti `Cap`, atau memakai menu goresan dengan mode selain titik, yang bisa membuat tekstur tercoreng.

![](/videos/paint_color_texture.mp4)  
:::

::: tip
Anda mungkin perlu mengaktifkan `Shading halus` [secara global](settings.md#smooth-shading) atau [per objek](material.md#smooth-shading) jika Anda mengecat permukaan logam pada objek dengan jumlah poligon yang rendah.
:::

## ![](/icons/paint.webp) Lukis semua {#paint-all}

![](/images/paint_paint_all.webp)

Menerapkan material saat ini ke objek yang dipilih, baik dalam mode standar dengan `Lukis semua`, maupun sebagai proyeksi Triplanar dengan `Lukis semua + Triplanar`. Varian triplanar tidak tersedia untuk primitif yang belum divalidasi.

Kotak centang di sebelah penggeser warna/kemetalan/kekasaran/opasitas tetap dipatuhi: properti yang dinonaktifkan tidak akan diisi.

Tombol-tombol tambahan mengatur bagaimana lukis semua bisa dipengaruhi lebih lanjut. Sebagian besar menampilkan persentase, dan menjadi abu-abu jika tidak akan berpengaruh:

| Ikon                        | Deskripsi                                     |
| :-------------------------: | :-------------------------------------------: |
| ![](/icons/shield.webp)    | Area yang ditopeng tidak akan terpengaruh.    |
| ![](/icons/tool_hide.webp) | Area yang disembunyikan tidak akan terpengaruh. |
| ![](/icons/opacity.webp)   | Memakai faktor pengecatan alat di atas.       |
| ![](/icons/layer.webp)     | Area lapisan yang belum dicat tidak akan terpengaruh. |
| ![](/icons/triplanar.webp) | `Verteks`: varian triplanar juga menggeser permukaan dengan alpha, sebesar intensitas alat yang ditampilkan. |
| ![](/icons/cog.webp)       | Membuka pengaturan Triplanar                  |

### ![](/icons/cog.webp) Pengaturan triplanar {#triplanar-settings}
![](/images/paint_triplanar_settings.webp)

Serupa dengan [pengaturan triplanar di menu material](material.md#triplanar), Anda bisa mengatur pembauran proyeksi, pengubinan, dan ofset. 

Gunakan kotak centang pratinjau di bagian atas menu ini untuk mengaktifkan pratinjau yang terus tampil selama Anda mengatur nilai.
