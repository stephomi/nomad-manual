# ![](/icons/scene.webp) Scene {#scene}

Menu ini memungkinkan Anda mengelola objek, lampu, kamera, dan repeater di Nomad. Menu ini menampilkan hierarki scene sebagai tampilan pohon (tree-view), sehingga Anda dapat mengubah banyak aspek dari objek Anda. Menu ini juga memungkinkan Anda membuat objek baru, serta menggabungkan dan memisahkan objek dengan berbagai cara.


![](/images/scene_menu_summary.webp)


## Bilah pintasan {#shortcut-bar}
| Action                 | Icon                              | Description                                                                                                         |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Add...](#add-menu)    | ![](/icons/plus.webp)            | Menampilkan [Add Menu](#add-menu) untuk menambahkan objek ke scene                                                 |
| Delete                 | ![](/icons/trash.webp)           | Menghapus objek                                                                                                    |
| Lock                   | ![](/icons/lock.webp)            | Membuat objek tidak dapat dipilih di viewport. Objek masih bisa dipilih dari tree view.                           |
| Join                   | ![](/icons/merge.webp)           | Menggabungkan objek yang dipilih menjadi satu objek tanpa mengubah geometri                                       |
| Separate               | ![](/icons/diagonal.webp)        | Jika sebuah objek terdiri dari beberapa shell poligon unik, pecah menjadi objek terpisah. Kebalikan dari join     |
| [Boolean...](#boolean) | ![](/icons/subtract_circle.webp) | Menampilkan menu [Boolean](#boolean)                                                                               |
| Clone                  | ![](/icons/clone.webp)           | Menggandakan objek menjadi objek baru                                                                              |
| Instance               | ![](/icons/link.webp)            | Menggandakan objek sebagai instance, sehingga perubahan modelling pada satu instance diterapkan ke semua instance  |
| Un-instance            | ![](/icons/unlink.webp)          | Mengubah instance menjadi bentuk unik, sehingga perubahan modelling tidak lagi disalin ke instance lain            |
| Sync                   | ![](/icons/link.webp)            | Jika instance memiliki anak, memastikan semua instance berbagi hierarki anak yang sama                             |


## Tampilan pohon {#tree-view}
![](/images/scene_treeview.webp) 

| Action       | Icon                       | Description              |
| :----------: | :------------------------: | :----------------------: |
| Select       | ![](/icons/checked.webp)  | Toggle pilih/tidak pilih |
| Visible      | ![](/icons/eye_open.webp) | Toggle visibilitas       |
| Menu         | ![](/icons/more.webp)     | Menampilkan menu objek   |

::: tip TIP: Cepat memilih atau menyembunyikan banyak objek

Ketuk ikon select untuk mengubah satu objek, atau seret secara vertikal pada kolom select untuk memilih banyak objek. Hal yang sama dapat dilakukan pada kolom visible.

:::

### Manipulasi tampilan pohon {#tree-view-manipulation}

Tekan lama pada sebuah item di tree view sampai berubah menjadi kuning. Anda kemudian dapat memindahkannya ke atas atau ke bawah di tree view, serta menyeretnya ke atas item lain untuk menjadikannya anak dari item tersebut.

Saat banyak item dipilih, sebagian besar akan berwarna kuning gelap, satu akan berwarna kuning lebih terang. Tekan lama dan seret item yang lebih terang untuk memindahkan semua objek sekaligus.

Saat Anda memilih item parent, secara default semua item child juga akan dipilih. Mengetuk ikon parent akan mengubah antara hanya memilih parent, atau parent beserta child-nya.

### Menu objek {#object-menu}

Mengklik tombol elipsis (...) untuk sebuah objek di tree view akan menampilkan object menu. 
Banyak opsi di sini mirip dengan shortcut bar di atas, diulang untuk kenyamanan.

|       Action        |                        Icon                        | Description                                                                                                                                                             |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      Instance       |               ![](/icons/link.webp)            | Menggandakan objek sebagai instance, sehingga perubahan modelling pada satu instance diterapkan ke semua instance.                                                     |
|        Clone        |              ![](/icons/clone.webp)            | Menggandakan objek menjadi objek baru                                                                                                                                  |
|        Name         |              ![](/icons/pencil.webp)           | Mengubah nama objek                                                                                                                                                    |
|       Delete        |              ![](/icons/trash.webp)            | Menghapus objek                                                                                                                                                         |
|       Delete+       |            ![](/icons/removeNode.webp)         | Menghapus objek beserta anak-anaknya                                                                                                                                   |
|     Un-instance     |              ![](/icons/unlink.webp)           | Mengubah instance menjadi bentuk unik, sehingga perubahan modelling tidak lagi disalin ke instance lain.                                                               |
|  Separate Topology  |             ![](/icons/separate.webp)          | Jika sebuah objek terdiri dari beberapa shell poligon unik, pecah menjadi objek terpisah. Kebalikan dari operasi join.                                                |
| Separate Face Group |            ![](/icons/faceGroup.webp)          | Jika sebuah objek memiliki beberapa face group, pecah mesh menjadi objek terpisah.                                                                                     |
|   Separate Layers   |              ![](/icons/layer.webp)            | Jika sebuah objek memiliki layer, pisahkan setiap layer menjadi objek terpisah. Berguna untuk mengirim blendshape ke aplikasi lain.                                   |
|   Join -> Layers    | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Jika beberapa objek dipilih dan memiliki topologi yang cocok, gabungkan objek-objek tersebut menjadi layer untuk objek utama (objek lain akan dihapus). Sekali lagi, berguna untuk blendshape yang datang DARI aplikasi lain.<br><br> Perhatikan bahwa layer akan dinonaktifkan secara default. Aktifkan jika Anda perlu menyesuaikan slider-nya. |




### Multiseleksi {#multiselection}
Anda dapat memilih beberapa objek untuk membantu dua hal:
- menggunakan gizmo tool untuk memindahkan beberapa objek sekaligus
- menggabungkan objek menggunakan operasi join dan boolean.

Anda dapat melakukannya dengan menggunakan checkbox `Multiselection`, lalu mengklik objek di daftar.

::: tip Quick multiselection
Anda juga dapat melakukan multiselect di viewport dengan menahan shortcut `Smooth` dan mengetuk mesh lain.

Anda dapat membatalkan pilihan sebuah objek dengan mengetuknya lagi (hanya jika pilihan Anda berisi lebih dari satu objek).
:::

::: warning Fitur gizmo terbatas
Saat menggunakan multiselection, gizmo tool akan selalu mengabaikan masking.
Selain itu, skala X/Y/Z dihilangkan.

Alasannya adalah multiselection hanya mengizinkan transformasi seluruh mesh, bukan transformasi per vertex.
Ini mungkin akan ditingkatkan di masa depan.
:::


## Gabung {#join}
Opsi ini akan membuat satu entri objek tunggal dari beberapa objek yang dipilih.

Anda dapat melihat contoh dalam video di bagian [Separate](#separate).

## Boolean {#boolean}
![](/images/scene_boolean_menu.webp) 
Menggabungkan objek menjadi satu permukaan.

`Voxel merge` akan mempertahankan volume objek, dan menghitung poligon baru yang terdistribusi merata pada permukaan. Karena ada langkah perhitungan, voxel merge dapat menangani geometri kompleks, tetapi dapat kehilangan detail halus jika resolusi target tidak cukup tinggi.

`Boolean` akan berusaha mempertahankan tata letak poligon asli, dan menjahit poligon di area tumpang tindih objek. Ini dapat menghasilkan hasil yang jauh lebih bersih dan tajam dibanding voxel merge, namun membutuhkan mesh yang 'watertight'; tidak boleh ada lubang atau bentuk rusak pada objek. Jika ini gagal, biasanya voxel merge akan berhasil.

### Operasi Boolean {#boolean-operations}
Baik Voxel Merge maupun Boolean akan menggunakan visibilitas objek untuk mengontrol operasi:

#### Gabung {#union}
Kedua objek terlihat akan membuat boolean **union**, kulit luar objek digabungkan, tanpa permukaan interior. ![](/images/boolean_union.webp)

#### Kurangi {#subtract}
Satu objek tidak terlihat = boolean **subtract**, objek yang tidak terlihat akan dikurangkan dari objek yang terlihat. ![](/images/boolean_subtract.webp)

#### Irisan {#intersect}
Kedua objek tidak terlihat = boolean **intersection**, membuat bentuk baru hanya di area di mana kedua objek saling tumpang tindih. ![](/images/boolean_intersect.webp)


### Tombol Voxel Merge {#voxel-merge-button}
Menekan tombol ini akan melakukan operasi voxel merge pada objek yang dipilih. Jika dilakukan pada satu objek, ini akan melakukan retopologi menjadi poligon yang terdistribusi merata, berguna ketika sebuah objek memiliki poligon yang teregang.

### Resolusi {#resolution}
Resolusi grid voxel 3D yang digunakan untuk perhitungan. Saat nilai ini diubah, pola papan catur akan ditampilkan di atas objek untuk mempratinjau ukuran poligon.

### Bangun multiresolusi {#build-multiresolution}
Membuat level multiresolution di bawah resolusi target Anda. Jadi jika resolusi Anda 400 dan build multiresolution bernilai 3, Anda akan mendapatkan mesh baru dengan sekitar 296.000 poligon, tetapi akan ada 3 level subdiv lebih rendah di 74.000, 18.000, 4.000k.

### Pertahankan tepi tajam {#keep-sharp-edges}
Mengaktifkan snapping mesh voxel ke tepi. Ini bekerja paling baik pada bentuk sederhana.

### Tombol Boolean {#boolean-button}
Menekan tombol ini akan melakukan operasi boolean poligon menggunakan pustaka Manifold oleh Emmett Lalish. 


## Pisah {#separate}
Jika Anda memiliki satu objek yang terdiri dari beberapa bagian yang tidak saling terhubung, Anda dapat membagi objek ini menjadi beberapa objek. 
Ini dapat dianggap sebagai kebalikan dari [Simple Merging](#simple-merge).

![](/videos/merge_separate.mp4)


## Menu tambah {#add-menu}

![](/images/scene_addmenu_overview.webp)

Menu ini akan membuat primitive, group, kamera, repeater, dan lampu.

Primitive adalah tipe bentuk dasar yang dapat disesuaikan menggunakan parameter. Setelah primitive disesuaikan dengan kebutuhan Anda, Anda kemudian melakukan 'validate', yang mengubah parameter tersebut menjadi mesh poligon yang dapat di-sculpt dan diwarnai. Primitive tidak dapat lagi diubah parameternya setelah divalidasi.


![](/images/scene_addmenu_top.webp)

### Pada gizmo {#on-gizmo}
Mengaktifkan penempatan primitive baru di posisi shape atau gizmo yang saat ini dipilih. Jika dinonaktifkan, primitive akan ditempatkan di pusat scene.

### Pilih gizmo {#select-gizmo}
Mengaktifkan perpindahan otomatis ke gizmo tool saat primitive baru dibuat. 

### Lanjutan {#add-advanced}

Menu ini memungkinkan Anda mengatur preferensi lokasi pembuatan primitive, group, repeater baru. Mereka dapat dibuat pada objek yang dipilih, di world origin, atau di lokasi gizmo.


### UV {#uvs}
Mengaktifkan UV pada primitive. UV (sering disebut koordinat tekstur) adalah data tambahan yang digunakan di 3D untuk memungkinkan tekstur diterapkan ke permukaan. UV memakan lebih banyak memori, tetapi untuk sebagian besar perangkat hal ini tidak menjadi masalah kecuali Anda menggunakan jumlah poligon yang sangat tinggi (misalnya 10 juta poligon atau lebih). 

### Primtif {#primitives}

| Primitive      | Icon                                      | Description                                                                                                     |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Box            | ![](/icons/cube.webp)                    | Kubus sederhana, Anda dapat mengontrol pembagian di X, Y dan Z                                                 |
| Sphere         | ![](/icons/circle.webp)                  | Demi kenyamanan dinamai Sphere tetapi sebenarnya adalah box yang disubdivide, dengan `Project on sphere` dipaksa |
| Cylinder       | ![](/icons/cylinder.webp)                | Anda dapat menambahkan lubang tengah pada primitive cylinder, misalnya untuk membuat pipa berongga             |
| Torus          | ![](/icons/torus.webp)                   | Torus dapat menjadi titik awal yang baik untuk cincin                                                           |
| Cone           | ![](/icons/cone.webp)                    | -                                                                                                               |
| Icosahedron    | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| UV-sphere      | ![](/icons/circle.webp)                  | Sphere dengan tata letak poly tidak merata, lihat [Peringatan di bawah](#uv-sphere)                            |
| Plane          | ![](/icons/rectangle.webp)               | Plane sederhana, perhatikan bahwa ini adalah satu-satunya primitive yang tidak tertutup                        |
| Tube           | ![](/icons/tool_tube.webp)               | lihat [Tube](tools#tube)                                                                                        |
| Lathe          | ![](/icons/tool_lathe.webp)              | lihat [Lathe](tools#lathe)                                                                                      |
| Triplanar      | ![](/icons/triplanar.webp)               | lihat [Triplanar](#triplanar)                                                                                   |
| Shadow Catcher | ![](/icons/material_shadow_catcher.webp) | lihat [Shadow Catcher](#shadow-catcher)                                                                         |
| Head           | ![](/icons/face.webp)                    | Kepala sederhana dengan layer untuk blending antara laki-laki/perempuan                                         |

::: tip
Jika Anda penasaran apa base mesh saat meluncurkan Nomad: itu juga adalah box yang disubdivide.
Namun base mesh di Nomad tidak menggunakan `Project on sphere`, artinya tidak benar-benar bulat.
:::

### Bilah alat primitif {#primitive-toolbar}

![](/images/scene_primitive_toolbar.gif)

Setelah primitive dibuat, toolbar akan muncul untuk mengontrol parameternya.

* `Validate` Mengubah primitive menjadi objek standar sehingga dapat di-sculpt dan diwarnai.
* `Edit` Mengaktifkan/menonaktifkan tampilan primitive gizmo. Ini ditampilkan langsung pada primitive untuk mengontrol parameternya, misalnya lebar cube, atau radius lubang cylinder.
* `Mirror` Mengaktifkan penempatan mirror repeater di atas primitive.
* `...` Menampilkan primitive menu.

Primitive yang berbeda akan memiliki opsi tambahan pada toolbar:

* `Project` Sphere dibangun sebagai cube yang disubdivide, karena ini lebih baik untuk sculpting, tetapi artinya tidak benar-benar bulat. Opsi ini akan memaksa bentuk lebih mendekati sphere sempurna. Icosahedron juga memiliki opsi ini.
* `Cap` Mengaktifkan/menonaktifkan end cap pada bentuk, misalnya cylinder dapat memiliki cap di atas, bawah, keduanya, atau tidak sama sekali.
* `Hole` Mengaktifkan/menonaktifkan lubang yang dibuat melalui pusat bentuk. Ini akan berputar antara tanpa lubang, lubang dengan satu radius, atau lubang dengan radius berbeda di atas dan bawah.
* `Radius` Mengaktifkan apakah cylinder memiliki satu radius, atau radius berbeda di atas dan bawah.
* `Disk` Mengaktifkan apakah plane berupa bentuk 4 sisi, atau bentuk lingkaran.

Toolbar kecil di bawah toolbar utama memungkinkan Anda beralih antara primitive gizmo dan transform gizmo.

::: tip

Mengklik judul toolbar akan memindahkannya ke bagian atas atau bawah tampilan. Mengklik panah di sudut akan melipatnya.

:::


### Menu primitif {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Menu ini berisi semua parameter untuk primitive yang dipilih. Parameter adalah deskripsi dasar untuk sebuah bentuk. Untuk mendeskripsikan cincin, misalnya, Anda akan mendeskripsikan radius luar, radius dalam, dan jumlah poligon.

Sebagian besar parameter primitive cukup jelas, dan ada beberapa parameter umum yang dibagi di semua primitive:

* `UVs` Tombol UVs kecil di bagian atas menu akan mengaktifkan/menonaktifkan pembuatan koordinat UV
* `Validate` Tombol validate kecil akan mengubah primitive menjadi objek standar sehingga dapat di-sculpt dan diwarnai.
* `Max faces` Menetapkan batas atas jumlah poligon dalam objek untuk menghindari crash pada perangkat Anda.
* `Post subdivision` Mengaktifkan jumlah subdivision yang dipilih dari bagian multiresolution di menu topology. Ini dapat digunakan untuk membuat primitive dengan sudut halus dan membulat dikombinasikan dengan pembagian topologi rendah. Misalnya, mengatur pembagian topologi box ke 2, dan post subdivision ke 4, akan membuat box dengan sudut halus.
* `Linear subdivision` Menetapkan berapa banyak level linear subdivision yang digunakan sebelum menggunakan smooth subdivision biasa. Ini dapat digunakan untuk mengontrol seberapa tajam atau lembut sudut pada permukaan yang disubdivide. Misalnya, atur pembagian topologi box ke 2, post subdivision ke 4, lalu coba ubah linear subdivision antara 0 dan 4. Sudut box akan berubah dari lembut menjadi tajam.

### Topologi {#topology}

Ini mengontrol jumlah poligon dalam primitive. Biasanya kontrol saling terhubung, sehingga mengubah satu slider aktif akan menyesuaikan semua poligon secara merata. Anda dapat mengetuk tombol unlink, dan mengontrol pembagian X/Y/Z pada bentuk secara terpisah.

### Geometri {#geometry}

Ini mengontrol ukuran keseluruhan primitive, dalam satuan X/Y/Z untuk bentuk bersudut, dan radius untuk bentuk bulat.


### UV Sphere {#uv-sphere}
::: warning
UV Sphere tidak cocok untuk sculpting, terutama di area kutub.

Sebaiknya gunakan primitive [Sphere](#sphere), [Box](#box) atau [Icosahedron](#icosahedron), bersama dengan opsi `Project on sphere`.

Perhatikan bahwa topologi masih dapat diterima untuk sculpting jika Anda menggunakan nilai yang sangat rendah untuk slider `Division`.
Anda kemudian dapat menggunakan slider `Overall Subdivision` untuk menaikkan jumlah poligon.

Meskipun tidak cocok untuk sculpting umum, UV Sphere berguna untuk mata; jika Anda memutar sphere sehingga kutub berada di pupil, tata letak poligon akan secara alami cocok untuk melukis dan memahat iris dan pupil.
:::


### Triplanar {#triplanar}
Primitive ini spesial karena Anda sebaiknya menggunakan [Masking tool](tools.md#mask) untuk membentuk geometrinya.

![](/videos/triplanar.mp4)


::: tip
Ketuk dua kali pada sebuah plane dan kamera akan fokus pada plane tersebut.
Ini tidak akan berfungsi jika Anda memutar primitive dengan gizmo.
:::

Triplanar menggunakan informasi mask dari 3 plane untuk mengisi grid voxel yang kemudian dipoligonisasi (berkat [Voxel Remesher](topology.md#voxel-remeshere)).

Setiap plane memiliki bidang simetrinya sendiri.

::: warning
Setiap kali Anda memperbarui ukuran primitive Triplanar, kualitas painting mask akan menurun.

Untuk saat ini belum ada opsi untuk 'mengunci' painting pada satu plane, tetapi mungkin akan hadir di masa depan.
Anda dapat menggunakan [Connected Topology](stroke.md#connected-topology) untuk sedikit membantu, karena jika kursor Anda berada tepat di satu plane, itu tidak akan memengaruhi plane lain.
:::

### Shadow Catcher {#shadow-catcher}
Menambahkan plane dengan material shadow catcher. Lihat [Shadow Catcher material](material.md#shadow-catcher) untuk detail lebih lanjut. 


## Grup/Kamera {#groupcamera}
### Grup {#group}
Membuat objek 'kosong', yang dapat Anda jadikan parent bagi objek lain di bawahnya. Ini dapat digunakan untuk sekadar mengatur hierarki dengan menempatkan banyak objek di bawah sebuah group, lalu menutupnya. Group juga dapat digunakan sebagai helper untuk memindahkan objek; banyak objek dapat ditempatkan di bawah group, lalu group tersebut dipindahkan, diputar, diskalakan dengan gizmo tool.

### Tambah sudut pandang {#add-view}
Membuat kamera.

## Pengulang {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Repeater adalah node yang membuat instance dari objek di bawahnya. 

### Array {#array}
![](/images/scene_primitive_array.webp)

Saat objek dijadikan child dari node ini, objek tersebut dapat di-instance ke dalam tata letak grid. Saat dipilih, node ini memiliki kontrol:
* Fit inside - toggle antara mengontrol ukuran grid/box array, atau mengontrol jarak antar instance array
* CountX/Y/Z - jumlah instance pada tiap sumbu
* OffsetX/Y/Z - jarak antar instance saat fit inside diaktifkan
* SizeX/Y/Z - lebar/tinggi/kedalaman total grid array saat fit inside diaktifkan.

### Kurva {#curve}
![](/images/scene_primitive_curve.webp)
Ini akan membuat sebuah curve, objek child dari node ini akan diulang sepanjang curve. Saat dipilih, node ini memiliki kontrol:
* Edit - memungkinkan penambahan titik pada curve, dan memindahkan titik pada curve.
* Snap - akan membuat titik curve menempel pada geometri lain
* Align - akan memutar bentuk child agar sejajar dengan arah curve
* Count - jumlah instance
* Closed - toggle curve untuk menyambung titik awal dan akhir, atau menjadi curve terbuka
* Radius - toggle kontrol pada setiap titik curve untuk mengontrol skala instance
* Twist - toggle kontrol pada setiap titik curve untuk mengontrol rotasi twist instance 
* B-spline - toggle instance untuk mengikuti curve secara tepat, atau menggunakan interpolasi b-spline yang hasilnya lebih halus. 

### Radial {#radial}
![](/images/scene_primitive_radial.webp)

Child dari node ini akan di-instance menjadi lingkaran. Pindahkan objek child untuk mengubah radius repeater ini. Saat dipilih, node ini memiliki kontrol:
* RadialX/Y/Z - memilih tombol ini akan mengatur sumbu radial, dan mengatur jumlah instance.



### Cermin {#mirror}
![](/images/scene_primitive_mirror.webp)

Child dari node ini akan dicerminkan melintasi sebuah sumbu. Saat dipilih, node ini memiliki kontrol:
* Gizmo - mengaktifkan transform gizmo untuk mengatur pusat mirror. Gizmo ini juga dapat diputar dan diskalakan. Jika sudah selesai, ketuk gizmo lagi untuk menampilkan kontrol standar.
* X/Y/Z - mengatur bidang mirror

Semua repeater memiliki kontrol `Validate`, yang akan mengubah hasil repeater menjadi objek tetap, dan akan menanyakan bagaimana cara melakukan bake:
* Join children - instance digabung menjadi satu objek
* Keep instances - instance tetap menjadi instance, tetapi tidak lagi memiliki parent repeater
* Un-instances - instance diubah menjadi objek unik

::: tip Tip: Menggabungkan repeater
Repeater dapat dijadikan parent satu sama lain, dan beberapa objek dapat dijadikan child repeater, menghasilkan efek kompleks.

![](/images/scene_repeater_combine.webp)
:::

::: tip Tip: Pivot repeater

Beberapa repeater akan mencoba mengatur pivot child secara otomatis, sehingga meskipun Anda memindahkan atau memutarnya dengan gizmo tool, mereka tidak akan bergerak. Jika Anda perlu menimpa perilaku ini, sisipkan sebuah group di antara repeater dan child. Sekarang Anda dapat memindahkan bentuk child secara independen dari repeater.
:::

## Cahaya {#light}

![](/images/scene_primitive_light.webp)

### Directional {#directional}
Membuat directional light, sumber cahaya yang sangat jauh seperti matahari.

### Spot {#spot}
Membuat spot light, dengan kontrol lebar dan kelembutan cone

### Titik {#point}
Membuat point light

## Lanjutan {#advanced}
### Fokus pada item {#focus-on-item}
Klik dua kali sebuah item di daftar Scene akan memusatkan kamera pada item tersebut di tampilan 3D.

### Sinkronkan visibilitas {#sync-visibility}
Menggunakan ikon mata akan memengaruhi semua item yang dipilih. 

### Instansi: Tampilkan {#instance-show}
Menampilkan kapsul warna di kiri daftar scene untuk menunjukkan instance.


### Ikon {#icons}
Mengatur ukuran dan opasitas ikon group, light, camera, mirror di viewport

### Garis hierarki {#hierarchy-lines}
Menampilkan garis antara parent dan child-nya di viewport

## Bilah alat bawah {#bottom-toolbar}
Ikon-ikon ini akan mengaktifkan/menonaktifkan visibilitas Group, Light, Camera, Repeater, dan Hierarchy lines di viewport.