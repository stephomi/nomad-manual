# ![](/icons/layer.webp) Lapisan {#layers}

Menu ini mengandungi tindanan lapisan, satu cara untuk menyimpan suntingan pada objek anda tanpa merosakkannya, serta banyak cara untuk menggabungkan dan menggunakan semula lapisan.

![](/images/layers_overview.webp) 

## Gambaran keseluruhan {#overview}

Lapisan dalam Nomad mempunyai pelbagai kegunaan.

Maklumat cat (Warna, Kekasaran, Kemetalan, Kelegapan) berfungsi dengan lapisan sama seperti dalam aplikasi lukisan 2d. Anda boleh mencipta lapisan dan mengecat model padanya. Lapisan boleh dihidupkan atau dimatikan, kelegapannya dilaraskan, ia boleh diklon, susunannya dalam tindanan lapisan boleh diubah, dan mod campurannya dilaraskan.

Nomad juga menggunakan lapisan untuk memahat. Lapisan boleh menyimpan butiran halus seperti kedutan, atau perubahan besar, membolehkannya berfungsi seperti blendshape/shape key/morph target dalam aplikasi 3d lain. Contohnya, anda boleh memahat ekspresi wajah yang berbeza pada lapisan yang berbeza, dan melaraskan peluncur lapisan untuk menggabungkannya menjadi ekspresi baharu.

Dalam kes ini, perubahan yang disimpan dalam lapisan bersifat tambahan semata-mata; susunan lapisan tidak penting seperti untuk cat.

Lapisan boleh dipadam sebahagiannya dengan alat [PadamLapisan](tools.md#delete-layer), dan lapisan juga boleh digunakan untuk mencipta topeng berdasarkan maklumat berbeza yang disimpan dalam lapisan.

![](/videos/layer.mp4)

::: tip
Tidak seperti kebanyakan perisian pemahatan, mengubah topologi mesh tidak akan membuang lapisan. Anda boleh menggunakan [Remesh voxel](topology.md#voxel-remesher), [Multiresolusi](topology.md#multiresolution) atau alat [Potong](tools.md#trim)/[Pisahkan](tools.md#split), tetapi perhatikan bahawa apabila menggunakan [Remesh voxel](topology.md#voxel-remesher), kualiti lapisan akan terjejas.
:::

::: tip
Jika anda menggunakan lapisan sebagai blendshape/morph target, terdapat fungsi lapisan tambahan dalam [menu adegan](scene.md#object-menu): anda boleh memisahkan lapisan menjadi objek, dan menggabungkan objek yang sepadan menjadi lapisan.
:::
----

## Menu lapisan {#layer-menu}

![](/images/layers_menu.webp)

Tajuk menunjukkan nama objek yang dipilih. Lapisan tidak tersedia untuk primitif, jadi sahkan primitif terlebih dahulu.

Tekan `Tambah lapisan` untuk mencipta lapisan baharu. `Gabungkan Lapisan` menggabungkan setiap lapisan ke dalam mesh asas; nombor di sebelah ikonnya ialah bilangan lapisan yang ada.

Setiap lapisan mempunyai nama, peluncur untuk mengawal kekuatan/faktornya, dan butang pilihan. Ketuk lapisan untuk menjadikannya lapisan aktif: pemahatan dan pengecatan akan masuk ke dalam lapisan itu. Ketuk `Asas` untuk kembali bekerja pada mesh asas.

### ![](/icons/sort_right.webp) Kembangkan senarai {#ui-expand-list}

Secara lalai, senarai lapisan hanya memaparkan keterlihatan, mod campuran dan kekuatan setiap lapisan, dan lapisan aktif dikembangkan dengan kawalan penuhnya. Anak panah di sebelah kiri tajuk mengembangkan kawalan penuh untuk setiap lapisan.

![](/images/layers_expand.webp)

### Pilihan {#options}

| Tindakan         | Ikon                         | Penerangan                                          |
| :--------------: | :--------------------------: | :-------------------------------------------------  |
| Kelihatan        | ![](/icons/eye_open.webp)   | Tunjuk/sembunyikan lapisan                          |
| Mod Campuran     | ![](/icons/opacity.webp)    | Mod campuran gaya Photoshop. 4 ikon memaparkan mod untuk Warna, Kekasaran, Kemetalan, Kelegapan. |
| Namakan semula   | ![](/icons/pencil.webp)     | Sunting nama lapisan                                |
| Padam            | ![](/icons/trash.webp)      | Padam lapisan                                       |
| Klona            | ![](/icons/clone.webp)      | Klon lapisan                                        |
| Gabung ke bawah  | ![](/icons/merge_down.webp) | Gabungkan lapisan dengan lapisan di bawahnya (atau mesh asas) |
| Lagi             | ![](/icons/more.webp)       | Pilihan [Lagi...](#more)                            |

Apabila sesuatu lapisan tidak dikembangkan, `Namakan semula`, `Padam`, `Klona` dan `Gabung ke bawah` terdapat dalam menu [Lagi...](#more) lapisan itu.

Untuk memindahkan lapisan ke bahagian lain dalam tindanan lapisan, tekan dan tahan pada namanya, kemudian seret.

### Asas {#base}

Butang 3 titik pada baris `Asas` memindahkan cat mesh asas ke dalam lapisan baharu, dengan butang `Asas → Lapisan`. Mesh asas kemudian ditetapkan semula kepada bahan latar belakang. Ini berguna apabila anda sudah banyak mengecat sebelum mencipta sebarang lapisan.

* Butang topeng dan sembunyi di sebelahnya membiarkan kawasan bertopeng dan tersembunyi tanpa diubah.
* `Ekstrak` - saluran yang hendak dipindahkan: `Warna`, `Kelegapan`, `Kekasaran` dan `Kemetalan`.
* `Bahan latar belakang` - jika didayakan, hanya nilai yang berbeza daripada bahan ini akan dipindahkan. Tetapkannya dengan peluncur, atau pilih daripada model dengan penitis mata.

### ![](/icons/more.webp) Lagi... {#more}

Butang 'Lagi...' memaparkan pilihan tambahan untuk lapisan semasa, dalam dua tab: tetapan (ikon gear), dan pengekstrakan (ikon kiub).

![](/images/layers_more.webp) 

#### Faktor saluran {#channel-factors}

Kawalan ini membolehkan anda menskalakan jumlah pahatan/warna/kekasaran/kemetalan/kelegapan bagi lapisan. Nilai ini didarabkan dengan peluncur faktor lapisan; contohnya, jika kekuatan lapisan ialah 1 tetapi faktor saluran warna ialah 0.5, warna yang dipaparkan akan berada pada kekuatan 0.5.

`Ofset` mengawal kekuatan pahatan lapisan. Walaupun warna/kekasaran/kemetalan dihadkan antara 0 dan 1, ofset boleh menjadi apa-apa nilai, sama ada positif atau negatif. 

::: tip
Ofset boleh digunakan untuk menukar lapisan bonjolan menjadi lapisan lekukan, atau senyuman menjadi muka masam:
![](/videos/layer_happysad.mp4)


Lapisan yang simetri boleh diklon dan kemudian dipisahkan kepada bentuk kiri/kanan dengan PadamLapisan:
![](/videos/layer_leftright.mp4)

Lapisan dengan faktor ofset negatif boleh di-bake ke dalam lapisan kosong untuk menghasilkan bentuk positif yang baharu.

Lapisan dengan faktor ofset positif melebihi 1 boleh digunakan untuk bereksperimen dengan blendshape yang lebih ekstrem.
:::

::: warning
Buat masa ini, lapisan hanya berkongsi satu saluran kelegapan untuk ketiga-tiga saluran (warna/kemetalan/kekasaran).
Jika anda menggabungkan beberapa lapisan dengan keamatan setiap saluran yang tidak penuh, hasil akhirnya mungkin kelihatan berbeza.

Mungkin pada masa hadapan, setiap saluran akan mempunyai saluran alpha sendiri untuk menghapuskan had ini.
:::


#### ![](/icons/shield.webp) Topeng {#mask}
Butang topeng di sebelah setiap peluncur akan mencipta topeng daripada saluran itu. Sama seperti menggunakan lapisan untuk membuat pilihan dalam aplikasi lukisan, ini membolehkan anda menggunakan semula kerja yang telah anda lakukan dalam sesuatu lapisan untuk operasi lain.

#### ![](/icons/preview.webp) Pratonton {#preview}
![](/images/layers_preview.webp) 

Pilihan berikut terdapat dalam tab pengekstrakan menu 'Lagi...'.

Apabila didayakan, tetapan ekstrak untuk lapisan ini akan dipratonton (lihat bahagian seterusnya).

`X-Ray` memilih objek yang dijadikan lut sinar semasa pratonton (`Tiada`, `Tidak terpilih`, `Terpilih` atau `Semua`), supaya bentuk yang diekstrak kekal padu. Ia berguna jika anda menggunakan ketinggian ekstrak negatif.

#### ![](/icons/mask_extract.webp) Ekstrak {#extract}
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Butang `Ekstrak` akan menduplikasi kandungan lapisan ke dalam objek baharu, biasanya dengan ketebalan yang ditentukan pengguna melalui bahagian seterusnya.

`Tindakan Penutupan` menentukan cara penduplikasian dilakukan:

* `Tiada` - Hanya ekstrak bahagian itu, tanpa cuba menjana sisi atau mengisi sebarang lubang.
* `Isi` - Lubang diisi dan dilicinkan dengan segi tiga. Jangan gunakan pilihan ini untuk permukaan rata.
* `Cangkerang` - Menutup bentuk yang diekstrak dengan nilai ketebalan dan pilihan arah.
* `Lapisan` - Mengekstrak perbezaan lapisan.

#### ![](/icons/height.webp) Ketinggian {#thickness}
![](/images/layers_thickness.webp) 

Kedalaman penyemperitan cangkerang. Nilai positif tumbuh keluar dari permukaan, nilai negatif tumbuh ke dalam permukaan. Ia disembunyikan apabila tindakan penutupan ialah `Lapisan`.

Tanda tambah/tolak di sebelah nilai ini menetapkan arah penyemperitan:
* Tolak ( - ) bermula dari permukaan semasa dan menyemperit ke bawah. 
* Tambah ( + ) bermula dari permukaan semasa dan menyemperit ke atas.
* TambahTolak ( ± ) menolak bahagian atas dan bawah penyemperitan sama jauh, jadi ia akan terbenam separuh dalam permukaan asal.

#### Sisi {#edge-loop-side}
![](/images/layers_edgeloop.webp) 

Bahagian ini kelihatan apabila tindakan penutupan ialah `Cangkerang`. 

`Bahagian dinding` menetapkan bilangan pembahagian di sepanjang sisi cangkerang. Apabila togol `Auto` dihidupkan, Nomad mengira bilangan gelung tepi untuk menghasilkan poligon segi empat sama.

#### Kehalusan {#smoothness}
![](/images/layers_smoothness.webp) 

Jika tepi kawasan yang hendak diekstrak bergerigi, dayakan pilihan ini untuk melicinkannya menjadi bentuk yang lebih kemas. `Semua` melicinkan keseluruhan permukaan yang diekstrak, `Hanya Tepi` melicinkan tepinya. `Ulangan` menetapkan kekuatan pelicinan.

_Ini ialah penghujung submenu 'Lagi...'._

### ![](/icons/cog.webp) Lanjutan {#advanced}
![](/images/layers_advanced.webp)

Butang `Lanjutan` di bahagian bawah menu muncul sebaik sahaja objek mempunyai lapisan.

#### Simpan butiran layer atas {#keep-top-layers-details}

Memastikan butiran kecil pada lapisan yang lebih tinggi kekal kelihatan apabila perubahan besar dibuat pada lapisan yang lebih rendah. Semasa anda memahat, ubah bentuk yang datang daripada lapisan atas diabaikan, tetapi butirannya kekal kelihatan. Ia hanya berfungsi dengan baik jika lapisan atas tersebut mengandungi butiran yang agak kecil.

Secara lalai, jika anda memahat kedutan kecil pada satu lapisan, kemudian membuat perubahan besar pada lapisan asas, kedutan itu akan hilang. Mendayakan togol ini membolehkan butiran kecil tersebut sentiasa terapung di atas perubahan besar di bawahnya. Dalam video berikut, lihat bagaimana butiran kedutan terhapus secara lalai, tetapi kekal kelihatan apabila 'simpan butiran layer atas' didayakan:

![](/videos/layers_details.mp4)


#### Segerak transformasi {#sync-transform}

Apabila dihidupkan, semua lapisan yang tidak dipilih akan dilaraskan mengikut putaran, skala dan serong transformasi, apabila anda menggunakan alat Gizmo atau Transformasi. Ia boleh ditetapkan kepada `Auto`, `Tidak` atau `Ya`.

Nyahdayakan pilihan ini jika lapisan lain sepatutnya digunakan tanpa transformasi baharu yang sedang anda gunakan.

Apabila ditetapkan kepada `Auto`, hanya lapisan yang kelihatan akan dilaraskan.
