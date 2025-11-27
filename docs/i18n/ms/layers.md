# ![](/icons/layer.webp) Lapisan 

Menu ini mengandungi susunan lapisan (layer stack), satu cara untuk menyimpan suntingan pada objek anda secara tidak merosakkan (non‑destructive), dan pelbagai cara untuk menggabung serta menggunakan semula lapisan.

![](/images/layers_overview.webp) 

## Gambaran keseluruhan

Lapisan Nomad mempunyai pelbagai tujuan.

Maklumat cat (Warna, Kekasaran, Keberkilatan Logam, Kelegapan) berfungsi dengan lapisan sama seperti aplikasi cat 2D. Satu lapisan boleh dicipta dan cat boleh digunakan pada model. Lapisan boleh dihidupkan atau dimatikan, kelegapannya boleh dilaraskan, lapisan boleh diduplikasi, susunannya boleh diubah dalam susunan lapisan, mod pengadunannya boleh dilaraskan.

Nomad juga menggunakan lapisan untuk pengukiran (sculpting). Satu lapisan boleh menyimpan perincian halus seperti kedutan, atau ia boleh menyimpan perubahan besar, membolehkannya berfungsi seperti blendshape/shape key/morph target dalam aplikasi 3D lain. Sebagai contoh anda boleh mengukir ekspresi muka yang berbeza pada lapisan berasingan, dan melaras peluncur lapisan untuk menggabungkannya menjadi ekspresi baharu.

Dalam kes ini perubahan yang disimpan dalam lapisan adalah semata‑mata tambahan (additive), susunan lapisan tidak penting seperti untuk cat.

Lapisan boleh dipadam sebahagiannya melalui alat [Delete Layer](tools.md#delete-layer), dan lapisan juga boleh digunakan untuk mencipta topeng (mask) berdasarkan maklumat berbeza yang disimpan dalam lapisan.

![](/videos/layer.mp4)

::: tip
Tidak seperti kebanyakan perisian sculpting, menukar topologi mesh tidak akan membuang lapisan. Anda boleh menggunakan [Voxel Remesher](topology.md#voxel-remesher), [Multiresolution](topology.md#multiresolution) atau alat [Trim](tools.md#trim)/[Split](tools.md#split), tetapi ambil perhatian bahawa apabila menggunakan [Voxel Remesher](topology.md#voxel-remesher), kualiti lapisan akan terjejas.
:::

::: tip
Jika menggunakan lapisan untuk blendshape/morph target, terdapat fungsi lapisan tambahan dalam [menu scene](scene.md#object-menu). Anda boleh memisahkan lapisan menjadi objek, dan menggabungkan objek yang sepadan menjadi lapisan.
:::
----

## Menu lapisan 

![](/images/layers_menu.webp)

Tekan `Add layer` untuk mencipta lapisan baharu.

Setiap lapisan mempunyai nama, peluncur untuk mengawal kekuatan/faktornya, dan butang pilihan.

### Pilihan

| Action       | Icon                         | Description                                         |
| :----------: | :--------------------------: | :-------------------------------------------------  |
| Visible      | ![](/icons/eye_open.webp)   | Tunjuk/sorok lapisan                                |
| Blend Mode   | ![](/icons/opacity.webp)    | Mod pengadunan gaya Photoshop. 4 ikon memaparkan mod untuk Warna, Kekasaran, Keberkilatan Logam, Kelegapan. |
| Edit Name    | ![](/icons/pencil.webp)     | Sunting nama lapisan                                |
| Delete       | ![](/icons/trash.webp)      | Padam lapisan                                       |
| Duplicate    | ![](/icons/clone.webp)      | Gandakan lapisan                                    |
| Merge Down   | ![](/icons/merge_down.webp) | Gabungkan lapisan dengan lapisan di bawah (atau mesh asas) |
| More         | ![](/icons/more.webp)       | Pilihan [More...](#more)                            |

Untuk mengalihkan lapisan ke bahagian lain dalam susunan lapisan, tekan dan tahan pada namanya, kemudian seret.

### More...

Butang 'More...' akan memaparkan pilihan tambahan untuk lapisan semasa:

![](/images/layers_more.webp) 

#### Faktor saluran (Channel factors)

Kawalan ini membolehkan anda menskalakan jumlah sculpt/color/roughness/metalness/opacity untuk lapisan. Nilai‑nilai ini didarab dengan peluncur faktor lapisan, jadi sebagai contoh jika kekuatan lapisan ialah 1, tetapi faktor saluran warna ialah 0.5, maka warna yang dipaparkan akan berada pada kekuatan 0.5.

`Offset` mengawal kekuatan sculpt lapisan. Walaupun color/roughness/metalness dihadkan antara 0 dan 1, offset boleh menjadi sebarang nilai, positif atau negatif. 

::: tip
Offset boleh digunakan untuk menukar lapisan bonjolan menjadi lapisan lekuk, atau senyuman menjadi masam:
![](/videos/layer_happysad.mp4)


Lapisan simetri boleh digandakan dan kemudian dipecahkan kepada bentuk kiri/kanan dengan del layer:
![](/videos/layer_leftright.mp4)

Lapisan dengan faktor offset negatif boleh dibakar (bake) ke lapisan kosong untuk membuat bentuk positif baharu.

Lapisan dengan faktor offset positif melebihi 1 boleh digunakan untuk mencuba blendshape yang lebih ekstrem.
:::

::: warning
Pada masa ini lapisan hanya berkongsi satu saluran kelegapan untuk semua 3 saluran (color/metalness/roughness).
Jika anda menggabungkan berbilang lapisan dengan keamatan per‑saluran yang tidak pada keamatan penuh, adalah mungkin hasil akhir kelihatan berbeza.

Mungkin pada masa hadapan, setiap saluran akan mempunyai saluran alfa sendiri untuk menghapuskan had ini.
:::


#### ![](/icons/tool_mask.webp) Mask
Butang mask di sebelah setiap peluncur akan mencipta mask daripada saluran tersebut. Sama seperti menggunakan lapisan untuk membuat pilihan dalam aplikasi melukis, ini membolehkan anda menggunakan semula kerja yang telah anda lakukan dalam satu lapisan untuk operasi lain.

#### ![](/icons/preview.webp) Preview
![](/images/layers_preview.webp) 

Apabila diaktifkan, akan mempratonton tetapan extract untuk lapisan ini (lihat seksyen seterusnya).

Apabila xray diaktifkan, hanya bentuk yang diekstrak akan menjadi legap, selebihnya bentuk akan menjadi lutsinar, berguna jika anda menggunakan ketinggian ekstraksi negatif.

#### Extract
![](/images/layers_extract.webp) 

![](/videos/layer_shell.mp4)

Butang `Extract` akan menduplikasi kandungan lapisan ke dalam objek baharu, biasanya dengan ketebalan yang ditentukan pengguna yang ditetapkan oleh seksyen seterusnya.

`Closing action` menentukan bagaimana penduplikasian dilakukan:

* None - Hanya ekstrak bahagian tersebut, jangan cuba menjana sisi atau mengisi sebarang lubang.
* Fill - Lubang diisi dan dilicinkan dengan segi tiga. Jangan gunakan pilihan ini untuk permukaan rata.
* Shell - Tutup bentuk yang diekstrak dengan nilai ketebalan dan pilihan arah.
* Layer - Ekstrak perbezaan lapisan.

#### ![](/icons/height.webp) Thickness
![](/images/layers_thickness.webp) 

Kedalaman ekstrusi shell. Nilai positif berkembang keluar dari permukaan, nilai negatif berkembang masuk ke dalam permukaan.

Tanda tambah/tolak di sebelah nilai ini akan menetapkan arah ekstrusi:
* Minus ( - ) akan bermula dari permukaan semasa dan mengekstrud ke bawah. 
* Plus ( + ) akan bermula dari permukaan semasa dan mengekstrud ke atas.
* PlusMinus ( ± ) akan menolak bahagian atas dan bawah ekstrusi menjauh dengan jumlah yang sama, jadi ia akan tertanam separuh dalam permukaan asal.

#### Smoothness
![](/images/layers_smoothness.webp) 

Jika tepi rantau yang akan diekstrak bergerigi, peluncur ini akan cuba mengaburkan tepi menjadi bentuk yang lebih licin. 

#### ![](/icons/height.webp) Edge loop (side)
![](/images/layers_edgeloop.webp) 

Seksysen ini kelihatan apabila closing action ialah 'Shell'. 

`Auto Edge-loop (side)` akan mengira bilangan edge loop sepanjang sisi shell untuk mencipta poligon segi empat sama. 

Jika dinyahaktifkan, peluncur `Division` akan menetapkan bilangan bahagian pada sisi.

_Ini adalah penghujung submenu 'More...'._

### Advanced
![](/images/layers_advanced.webp)

#### Keep top layers details

Memastikan perincian kecil pada lapisan lebih tinggi kekal kelihatan apabila perubahan besar dibuat pada lapisan lebih rendah.

Secara lalai jika anda mengukir kedutan kecil pada satu lapisan, kemudian pergi membuat perubahan besar pada lapisan asas, kedutan itu akan hilang. Mengaktifkan togol ini akan membenarkan perincian kecil tersebut sentiasa terapung di atas perubahan besar di bawah. Dalam video berikut, lihat bagaimana perincian kedutan dibuang secara lalai, tetapi kekal kelihatan apabila 'keep top layers details' diaktifkan:

![](/videos/layers_details.mp4)


#### UI: Expand list

Menu lapisan lalai membolehkan anda menogol keterlihatan lapisan dan kelegapan lapisan. Mengaktifkan pilihan ini mengembangkan kawalan penuh untuk setiap lapisan.

![](/images/layers_expand.webp)

#### Sync transform

Jika diaktifkan, semua lapisan yang tidak dipilih akan dilaraskan bergantung pada putaran, skala, herotan (skew) transform.

Nyahaktifkan pilihan ini jika lapisan lain dimaksudkan untuk digunakan tanpa transform baharu yang anda gunakan.

Apabila ditetapkan kepada `Auto`, hanya lapisan yang kelihatan akan dilaraskan.
