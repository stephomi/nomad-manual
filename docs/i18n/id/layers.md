# ![](/icons/layer.webp) Lapisan {#layers}

Menu ini berisi tumpukan lapisan (layer stack), cara untuk menyimpan edit pada objek Anda secara non-destruktif, dan banyak cara untuk menggabungkan serta memanfaatkan ulang lapisan.

![](/images/layers_overview.webp) 

## Ikhtisar {#overview}

Lapisan di Nomad memiliki beberapa fungsi.

Informasi cat (Color, Roughness, Metalness, Opacity) bekerja dengan lapisan mirip dengan aplikasi lukis 2D. Sebuah lapisan dapat dibuat dan cat dapat diaplikasikan ke model. Lapisan dapat diaktifkan/nonaktifkan, opasitasnya dapat diatur, lapisan dapat diduplikasi, urutannya dapat diubah dalam tumpukan lapisan, mode blending-nya dapat diatur.

Nomad juga menggunakan lapisan untuk pemahatan (sculpting). Sebuah lapisan dapat menyimpan detail halus seperti kerutan, atau dapat menyimpan perubahan besar, sehingga dapat berfungsi seperti blendshape/shape key/morph target di aplikasi 3D lainnya. Misalnya Anda dapat memahat ekspresi wajah yang berbeda pada lapisan yang berbeda, lalu mengatur slider lapisan untuk menggabungkannya menjadi ekspresi baru.

Dalam kasus ini perubahan yang disimpan di sebuah lapisan bersifat murni aditif, urutan lapisan tidak penting seperti halnya untuk cat.

Lapisan dapat dihapus sebagian melalui tool [Delete Layer](tools.md#delete-layer), dan lapisan juga dapat digunakan untuk membuat mask berdasarkan berbagai informasi yang disimpan di lapisan.

![](/videos/layer.mp4)

::: tip
Tidak seperti kebanyakan perangkat lunak sculpting, mengubah topologi mesh tidak akan menghapus lapisan. Anda dapat menggunakan [Voxel Remesher](topology.md#voxel-remesher), [Multiresolution](topology.md#multires) atau tool [Trim](tools.md#trim)/[Split](tools.md#split), tetapi perlu dicatat bahwa saat menggunakan [Voxel Remesher](topology.md#voxel-remesher), kualitas lapisan akan terpengaruh.
:::

::: tip
Jika menggunakan lapisan untuk blendshape/morph target, ada fungsi lapisan tambahan di [menu scene](scene.md#object-menu). Anda dapat memisahkan lapisan menjadi objek, dan menggabungkan objek yang cocok menjadi lapisan.
:::
----

## Menu lapisan {#layer-menu}

![](/images/layers_menu.webp)

Tekan `Add layer` untuk membuat lapisan baru.

Setiap lapisan memiliki nama, slider untuk mengontrol kekuatan/faktornya, dan tombol opsi.

### Opsi {#options}

| Action       | Icon                         | Description                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Visible      | ![](/icons/eye_open.webp)   | Tampilkan/sembunyikan lapisan                      |
| Blend Mode   | ![](/icons/opacity.webp)    | Mode blending ala Photoshop. Ke-4 ikon menampilkan mode untuk Color, Roughness, Metalness, Opacity. |
| Edit Name    | ![](/icons/pencil.webp)     | Edit nama lapisan                                   |
| Delete       | ![](/icons/trash.webp)      | Hapus lapisan                                       |
| Duplicate    | ![](/icons/clone.webp)      | Duplikasi lapisan                                   |
| Merge Down   | ![](/icons/merge_down.webp) | Gabungkan lapisan dengan lapisan di bawahnya (atau mesh dasar) |
| More         | ![](/icons/more.webp)       | Opsi [More...](#more)                               |

Untuk memindahkan lapisan ke bagian lain dari tumpukan lapisan, tekan dan tahan pada namanya, lalu seret.

### Lainnya... {#more}

Tombol 'More...' akan menampilkan opsi tambahan untuk lapisan saat ini:

![](/images/layers_more.webp) 

#### Faktor kanal {#channel-factors}

Kontrol ini memungkinkan Anda menskalakan jumlah sculpt/color/roughness/metalness/opacity untuk lapisan tersebut. Nilai-nilai ini dikalikan dengan slider faktor lapisan, jadi misalnya jika kekuatan lapisan adalah 1, tetapi faktor channel warna adalah 0.5, maka warna yang ditampilkan akan berada pada kekuatan 0.5.

`Offset` mengontrol kekuatan sculpt lapisan. Sementara color/roughness/metalness dijepit antara 0 dan 1, offset dapat berupa nilai apa pun, baik positif maupun negatif. 

::: tip
Offset dapat digunakan untuk mengubah lapisan tonjolan (bumps) menjadi lapisan cekungan (cavities), atau senyuman menjadi cemberut:
![](/videos/layer_happysad.mp4)


Lapisan simetris dapat diklon lalu dipecah menjadi bentuk kiri/kanan dengan del layer:
![](/videos/layer_leftright.mp4)

Lapisan dengan faktor offset negatif dapat di-bake menjadi lapisan kosong untuk membuat bentuk positif baru.

Lapisan dengan faktor offset positif di atas 1 dapat digunakan untuk bereksperimen dengan blendshape yang lebih ekstrem.
:::

::: warning
Saat ini lapisan hanya berbagi satu channel opacity untuk semua 3 channel (color/metalness/roughness).
Jika Anda menggabungkan beberapa lapisan dengan intensitas per-channel yang tidak pada intensitas penuh, ada kemungkinan hasil akhirnya akan terlihat berbeda.

Mungkin di masa depan, setiap channel akan memiliki channel alpha sendiri untuk menghilangkan keterbatasan ini.
:::


#### ![](/icons/tool_mask.webp) Masker {#mask}
Tombol mask di sebelah setiap slider akan membuat mask dari channel tersebut. Mirip dengan penggunaan lapisan untuk membuat seleksi di aplikasi lukis, ini memungkinkan Anda menggunakan kembali pekerjaan yang telah Anda lakukan di sebuah lapisan untuk operasi lainnya.

#### ![](/icons/preview.webp) Pratinjau {#preview}
![](/images/layers_preview.webp) 

Saat diaktifkan, akan menampilkan pratinjau pengaturan extract untuk lapisan ini (lihat bagian berikutnya).

Saat xray diaktifkan, hanya bentuk yang diekstrak yang akan tampak solid, bagian bentuk lainnya akan dibuat transparan, berguna jika Anda menggunakan tinggi ekstraksi negatif.

#### Ekstrak {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Tombol `Extract` akan menduplikasi isi lapisan ke dalam objek baru, biasanya dengan ketebalan yang ditentukan pengguna yang diatur di bagian berikutnya.

`Closing action` menentukan bagaimana duplikasi dilakukan:

* None - Hanya mengekstrak bagian tersebut, tidak mencoba membuat sisi atau mengisi lubang apa pun.
* Fill - Lubang diisi dan dihaluskan dengan segitiga. Jangan gunakan opsi ini untuk permukaan datar.
* Shell - Menutup bentuk yang diekstrak dengan nilai ketebalan dan opsi arah.
* Layer - Mengekstrak perbedaan lapisan.

#### ![](/icons/height.webp) Ketebalan {#thickness}
![](/images/layers_thickness.webp) 

Kedalaman ekstrusi shell. Nilai positif tumbuh keluar dari permukaan, nilai negatif tumbuh ke dalam permukaan.

Tombol plus/minus di sebelah nilai ini akan mengatur arah ekstrusi:
* Minus ( - ) akan mulai dari permukaan saat ini dan mengekstrusi ke bawah. 
* Plus ( + ) akan mulai dari permukaan saat ini dan mengekstrusi ke atas.
* PlusMinus ( ± ) akan mendorong bagian atas dan bawah ekstrusi menjauh dengan jumlah yang sama, sehingga akan setengah tertanam di permukaan asli.

#### Kehalusan {#smoothness}
![](/images/layers_smoothness.webp) 

Jika tepi area yang akan diekstrak bergerigi, slider ini akan mencoba mengaburkan tepi menjadi bentuk yang lebih halus. 

#### ![](/icons/height.webp) Loop tepi (sisi) {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Bagian ini terlihat ketika closing action adalah 'Shell'. 

`Auto Edge-loop (side)` akan menghitung jumlah edge loop di sepanjang sisi shell untuk membuat poligon persegi. 

Jika dinonaktifkan, slider `Division` akan mengatur jumlah divisi di sisi.

_Ini adalah akhir dari submenu 'More...'._

### Tingkat lanjut {#advanced}
![](/images/layers_advanced.webp)

#### Pertahankan detail lapisan atas {#keep-top-layers-details}

Memastikan detail kecil pada lapisan yang lebih tinggi tetap terlihat ketika perubahan besar dibuat pada lapisan yang lebih rendah.

Secara bawaan jika Anda memahat kerutan kecil pada sebuah lapisan, lalu membuat perubahan besar pada lapisan dasar, kerutan tersebut akan hilang. Mengaktifkan toggle ini akan memungkinkan detail kecil tersebut selalu mengambang di atas perubahan besar di bawahnya. Pada video berikut, lihat bagaimana detail kerutan dihapus secara default, tetapi tetap terlihat ketika 'keep top layers details' diaktifkan:

![](/videos/layers_details.mp4)


#### UI: Perluas daftar {#ui-expand-list}

Menu lapisan bawaan memungkinkan Anda mengaktifkan/nonaktifkan visibilitas lapisan dan opasitas lapisan. Mengaktifkan opsi ini akan memperluas kontrol penuh untuk setiap lapisan.

![](/images/layers_expand.webp)

#### Sinkronkan transformasi {#sync-transform}

Jika diaktifkan, semua lapisan yang tidak dipilih akan disesuaikan tergantung pada transformasi rotasi, skala, dan skew. 

Nonaktifkan opsi ini jika lapisan lain dimaksudkan untuk digunakan tanpa transformasi baru yang sedang Anda terapkan.

Jika diatur ke `Auto`, hanya lapisan yang terlihat yang akan disesuaikan.