# ![](/icons/layer.webp) Lapisan {#layers}

Menu ini berisi tumpukan lapisan, cara untuk menyimpan perubahan pada objek Anda secara non-destruktif, serta banyak cara untuk menggabungkan dan memanfaatkan ulang lapisan.

![](/images/layers_overview.webp) 

## Ikhtisar {#overview}

Lapisan di Nomad punya beberapa kegunaan.

Informasi cat (Warna, Kekasaran, Kemetalan, Opasitas) bekerja dengan lapisan seperti di aplikasi lukis 2d. Anda bisa membuat lapisan lalu mengecat model di atasnya. Lapisan itu bisa diaktifkan atau dinonaktifkan, diatur opasitasnya, diduplikasi, diubah urutannya di tumpukan lapisan, dan diatur mode blend-nya.

Nomad juga memakai lapisan untuk memahat. Sebuah lapisan bisa menyimpan detail halus seperti kerutan, atau perubahan besar, sehingga bisa berfungsi seperti blendshape/shape key/morph target di aplikasi 3d lainnya. Misalnya, Anda bisa memahat ekspresi wajah yang berbeda di lapisan yang berbeda, lalu mengatur penggeser lapisan untuk menggabungkannya menjadi ekspresi baru.

Dalam hal ini, perubahan yang tersimpan di lapisan bersifat murni aditif: urutan lapisan tidak berpengaruh seperti pada cat.

Lapisan bisa dihapus sebagian dengan alat [HapusLapisan](tools.md#delete-layer), dan lapisan juga bisa dipakai untuk membuat topeng berdasarkan berbagai informasi yang tersimpan di dalamnya.

![](/videos/layer.mp4)

::: tip
Tidak seperti kebanyakan perangkat lunak pahat, mengubah topologi mesh tidak akan membuang lapisan. Anda bisa memakai [Remesh voxel](topology.md#voxel-remesher), [Multiresolution](topology.md#multiresolution), atau alat [Pangkas](tools.md#trim)/[Pisah](tools.md#split), tetapi perlu diingat bahwa saat memakai [Remesh voxel](topology.md#voxel-remesher), kualitas lapisan akan terpengaruh.
:::

::: tip
Jika Anda memakai lapisan untuk blendshape/morph target, ada fungsi lapisan tambahan di [menu adegan](scene.md#object-menu): Anda bisa memisahkan lapisan menjadi objek, dan menggabungkan objek yang cocok menjadi lapisan.
:::
----

## Menu lapisan {#layer-menu}

![](/images/layers_menu.webp)

Judulnya menampilkan nama objek yang dipilih. Lapisan tidak tersedia untuk primitif, jadi validasi primitifnya terlebih dahulu.

Tekan `Tambah lapisan` untuk membuat lapisan baru. `Gabungkan Lapisan` menggabungkan semua lapisan ke dalam mesh dasar; angka di sebelah ikonnya menunjukkan jumlah lapisan yang ada.

Setiap lapisan memiliki nama, penggeser untuk mengatur kekuatan/faktornya, dan tombol-tombol opsi. Ketuk sebuah lapisan untuk menjadikannya lapisan aktif: pahatan dan cat akan masuk ke lapisan itu. Ketuk `Dasar` untuk kembali bekerja pada mesh dasar.

### ![](/icons/sort_right.webp) Bentangkan daftar {#ui-expand-list}

Secara bawaan, daftar lapisan hanya menampilkan visibilitas, mode blend, dan kekuatan setiap lapisan, sedangkan lapisan aktif dibentangkan dengan semua kontrolnya. Panah di sebelah kiri judul akan membentangkan semua kontrol untuk setiap lapisan.

![](/images/layers_expand.webp)

### Opsi {#options}

| Tindakan     | Ikon                         | Deskripsi                                           |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Tampak       | ![](/icons/eye_open.webp)   | Menampilkan/menyembunyikan lapisan                  |
| Mode blend   | ![](/icons/opacity.webp)    | Mode blend ala Photoshop. Keempat ikon menunjukkan mode untuk Warna, Kekasaran, Kemetalan, Opasitas. |
| Ganti nama   | ![](/icons/pencil.webp)     | Mengubah nama lapisan                               |
| Hapus        | ![](/icons/trash.webp)      | Menghapus lapisan                                   |
| Kloning      | ![](/icons/clone.webp)      | Menduplikasi lapisan                                |
| Gabungkan ke bawah | ![](/icons/merge_down.webp) | Menggabungkan lapisan dengan lapisan di bawahnya (atau mesh dasar) |
| Lainnya      | ![](/icons/more.webp)       | Opsi [Lainnya...](#more)                            |

Jika sebuah lapisan tidak dibentangkan, `Ganti nama`, `Hapus`, `Kloning` dan `Gabungkan ke bawah` ada di menu [Lainnya...](#more)-nya.

Untuk memindahkan lapisan ke posisi lain di tumpukan lapisan, tekan dan tahan namanya, lalu seret.

### Dasar {#base}

Tombol titik tiga di baris `Dasar` memindahkan cat mesh dasar ke lapisan baru, dengan tombol `Dasar → Lapisan`. Dasarnya kemudian diatur ulang ke material latar belakang. Ini praktis jika Anda sudah banyak mengecat sebelum membuat lapisan apa pun.

* Tombol topeng dan sembunyi di sebelahnya membiarkan area yang ditopeng dan disembunyikan tidak tersentuh.
* `Ekstrak` - kanal yang akan dipindahkan: `Warna`, `Opasitas`, `Kekasaran` dan `Kemetalan`.
* `Material latar belakang` - jika diaktifkan, hanya nilai yang berbeda dari material ini yang dipindahkan. Atur dengan penggeser, atau ambil dari model dengan pipet.

### ![](/icons/more.webp) Lainnya... {#more}

Tombol 'Lainnya...' menampilkan opsi tambahan untuk lapisan saat ini, dalam dua tab: pengaturan (ikon roda gigi), dan ekstraksi (ikon kubus).

![](/images/layers_more.webp) 

#### Faktor saluran {#channel-factors}

Kontrol ini memungkinkan Anda menskalakan jumlah pahatan/warna/kekasaran/kemetalan/opasitas untuk lapisan tersebut. Nilai-nilai ini dikalikan dengan penggeser faktor lapisan, jadi misalnya jika kekuatan lapisan bernilai 1 tetapi faktor kanal warna bernilai 0.5, warna yang ditampilkan akan berkekuatan 0.5.

`Ofset` mengatur kekuatan pahatan lapisan. Sementara warna/kekasaran/kemetalan dibatasi antara 0 dan 1, ofset bisa bernilai berapa saja, baik positif maupun negatif. 

::: tip
Ofset bisa dipakai untuk mengubah lapisan tonjolan menjadi lapisan cekungan, atau senyuman menjadi cemberut:
![](/videos/layer_happysad.mp4)


Lapisan yang simetris bisa dikloning lalu dipisah menjadi bentuk kiri/kanan dengan HapusLapisan:
![](/videos/layer_leftright.mp4)

Lapisan dengan faktor ofset negatif bisa di-bake ke lapisan kosong untuk membuat bentuk positif baru.

Lapisan dengan faktor ofset positif di atas 1 bisa dipakai untuk bereksperimen dengan blendshape yang lebih ekstrem.
:::

::: warning
Saat ini, lapisan hanya memiliki satu kanal opasitas yang dipakai bersama oleh ketiga kanal (warna/kemetalan/kekasaran).
Jika Anda menggabungkan beberapa lapisan dengan intensitas per kanal yang tidak penuh, hasil akhirnya mungkin akan terlihat berbeda.

Mungkin di masa mendatang, setiap kanal akan memiliki kanal alpha sendiri untuk menghilangkan batasan ini.
:::


#### ![](/icons/shield.webp) Topeng {#mask}
Tombol topeng di sebelah setiap penggeser akan membuat topeng dari kanal tersebut. Mirip dengan memakai lapisan untuk membuat seleksi di aplikasi lukis, fitur ini memungkinkan Anda memanfaatkan ulang hasil kerja di sebuah lapisan untuk operasi lain.

#### ![](/icons/preview.webp) Pratinjau {#preview}
![](/images/layers_preview.webp) 

Opsi-opsi berikut ada di tab ekstraksi pada menu 'Lainnya...'.

Jika diaktifkan, opsi ini menampilkan pratinjau pengaturan ekstraksi untuk lapisan ini (lihat bagian berikutnya).

`X-Ray` memilih objek mana yang dibuat transparan selama pratinjau (`Tidak ada`, `Tidak terpilih`, `Dipilih` atau `Semua`), sehingga bentuk yang diekstrak tetap terlihat padat. Ini berguna jika Anda memakai tinggi ekstraksi negatif.

#### ![](/icons/mask_extract.webp) Ekstrak {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Tombol `Ekstrak` akan menduplikasi isi lapisan menjadi objek baru, biasanya dengan ketebalan yang Anda tentukan di bagian berikutnya.

`Aksi penutupan` menentukan bagaimana duplikasi dilakukan:

* `Tidak ada` - Hanya mengekstrak bagiannya, tanpa mencoba membuat sisi atau mengisi lubang.
* `Isi` - Lubang diisi dan dihaluskan dengan segitiga. Jangan pakai opsi ini untuk permukaan datar.
* `Kulit` - Menutup bentuk yang diekstrak dengan nilai ketebalan dan opsi arah.
* `Lapisan` - Mengekstrak selisih lapisan.

#### ![](/icons/height.webp) Tinggi {#thickness}
![](/images/layers_thickness.webp) 

Kedalaman ekstrusi kulit. Nilai positif tumbuh keluar dari permukaan, nilai negatif tumbuh ke dalam permukaan. Opsi ini disembunyikan jika aksi penutupannya adalah `Lapisan`.

Tanda plus/minus di sebelah nilai ini menentukan arah ekstrusi:
* Minus ( - ) dimulai dari permukaan saat ini dan mengekstrusi ke bawah. 
* Plus ( + ) dimulai dari permukaan saat ini dan mengekstrusi ke atas.
* PlusMinus ( ± ) mendorong bagian atas dan bawah ekstrusi menjauh dengan besaran yang sama, sehingga setengahnya tertanam di permukaan asli.

#### Sisi {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Bagian ini terlihat jika aksi penutupannya adalah `Kulit`. 

`Pembagian dinding` mengatur jumlah pembagian di sepanjang sisi kulit. Dengan sakelar `Otomatis` aktif, Nomad menghitung jumlah edge loop agar menghasilkan poligon berbentuk persegi.

#### Kelembutan {#smoothness}
![](/images/layers_smoothness.webp) 

Jika tepi area yang akan diekstrak bergerigi, aktifkan opsi ini untuk menghaluskannya menjadi bentuk yang lebih rapi. `Semua` menghaluskan seluruh permukaan yang diekstrak, `Hanya tepi` menghaluskan tepinya saja. `Iterasi` mengatur seberapa kuat penghalusannya.

_Ini adalah akhir dari submenu 'Lainnya...'._

### ![](/icons/cog.webp) Lanjutan {#advanced}
![](/images/layers_advanced.webp)

Tombol `Lanjutan` di bagian bawah menu muncul setelah objek memiliki lapisan.

#### Tetap detail lapisan atas {#keep-top-layers-details}

Memastikan detail kecil di lapisan yang lebih atas tetap terlihat saat Anda membuat perubahan besar di lapisan yang lebih bawah. Selama Anda memahat, deformasi dari lapisan atas diabaikan, tetapi detailnya tetap terlihat. Ini hanya bekerja dengan baik jika lapisan atas tersebut berisi detail yang relatif kecil.

Secara bawaan, jika Anda memahat kerutan kecil di sebuah lapisan, lalu membuat perubahan besar di lapisan dasar, kerutan itu akan hilang. Mengaktifkan sakelar ini membuat detail kecil tersebut selalu mengambang di atas perubahan besar di bawahnya. Pada video berikut, perhatikan bagaimana detail kerutan hilang secara bawaan, tetapi tetap terlihat saat 'tetap detail lapisan atas' diaktifkan:

![](/videos/layers_details.mp4)


#### Sinkronisasi transformasi {#sync-transform}

Jika aktif, semua lapisan yang tidak dipilih akan disesuaikan mengikuti rotasi, skala, dan kemiringan transformasi saat Anda memakai alat Gizmo atau Transformasi. Nilainya bisa `Otomatis`, `Tidak` atau `Ya`.

Nonaktifkan opsi ini jika lapisan lain memang dimaksudkan untuk dipakai tanpa transformasi baru yang sedang Anda terapkan.

Jika diatur ke `Otomatis`, hanya lapisan yang terlihat yang akan disesuaikan.
