# ![](/icons/scene.webp) Adegan {#scene}

Menu ini memungkinkan Anda mengelola objek, lampu, kamera, dan pengulang di Nomad. Hierarki adegan ditampilkan sebagai tampilan pohon, sehingga Anda bisa mengubah banyak aspek objek Anda. Di sini Anda juga bisa membuat objek baru, serta menggabungkan dan memisahkan objek dengan berbagai cara.


![](/images/scene_menu_summary.webp)


## Bilah pintasan {#shortcut-bar}
| Aksi                   | Ikon                              | Deskripsi                                                                                                           |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Tambahkan...](#add-menu) | ![](/icons/plus.webp)         | Menampilkan [menu Tambahkan](#add-menu) untuk menambahkan objek ke adegan                                           |
| Hapus                  | ![](/icons/trash.webp)           | Menghapus objek yang dipilih. Anak-anaknya tetap dipertahankan.                                                     |
| Kunci                  | ![](/icons/lock.webp)            | Membuat objek yang dipilih tidak bisa dipilih di viewport. Objek tersebut masih bisa dipilih dari tampilan pohon. Mengunci sebuah grup akan mengunci semua yang ada di bawahnya. Ketuk lagi untuk membuka kunci. |
| [Gabung](#join)        | ![](/icons/merge.webp)           | Menggabungkan objek yang dipilih menjadi satu objek tanpa mengubah geometrinya                                      |
| [Pisah...](#separate)  | ![](/icons/separate.webp)        | Menampilkan popup [Pisah](#separate), untuk memecah satu objek menjadi beberapa objek. Kebalikan dari operasi gabung |
| [Boolean...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Menampilkan popup [Boolean](#boolean)                                                                          |
| Kloning                | ![](/icons/clone.webp)           | Menduplikasi objek yang dipilih menjadi objek baru                                                                  |
| Instans                | ![](/icons/link.webp)            | Menduplikasi objek yang dipilih sebagai instans, sehingga perubahan bentuk pada satu objek diterapkan ke semua instansnya. |
| Batalkan instans       | ![](/icons/unlink.webp)          | Mengubah instans menjadi bentuk yang berdiri sendiri, sehingga perubahan bentuk tidak lagi disalin ke instans lain  |
| Sinkronkan             | ![](/icons/checked.webp)         | Jika dicentang, operasi diterapkan ke setiap instans dari objek yang dipilih, bukan hanya ke objek yang dipilih. Hanya tersedia jika pilihan berisi instans. [Tab Sinkronkan](#sync) di popup `Lanjutan` menentukan operasi mana yang mengikuti kotak centang ini. |

::: tip
Jika sebuah operasi juga akan memengaruhi instans lain, ikon tautan kecil muncul di tombolnya.
:::


## Tampilan pohon {#tree-view}
![](/images/scene_treeview.webp) 

Tampilan pohon menampilkan daftar objek, grup, pengulang, lampu, dan kamera di adegan. Di samping nama mesh, Anda akan melihat jumlah verteksnya, dengan ikon lapisan berwarna jika mesh tersebut punya lapisan. Setiap baris punya tombol-tombol berikut:

| Aksi         | Ikon                       | Deskripsi                |
| :----------: | :------------------------: | :----------------------: |
| Nama         | ![](/icons/pencil.webp)   | Mengganti nama objek. Jika objek sedang dipilih, semua objek yang dipilih diganti namanya sekaligus, dengan tambahan angka. Tekan lama untuk mengganti namanya beserta anak-anaknya. |
| Pilih        | ![](/icons/checked.webp)  | Memilih/membatalkan pilihan |
| Tampak       | ![](/icons/eye_open.webp) | Menampilkan/menyembunyikan |
| Menu         | ![](/icons/more.webp)     | Menampilkan [menu objek](#object-menu) |

::: tip TIPS: Memilih atau menyembunyikan banyak objek dengan cepat

Ketuk ikon pilih untuk memilih satu objek, atau seret secara vertikal di kolom pilih untuk memilih banyak objek. Hal yang sama bisa dilakukan di kolom tampak.

Tekan lama ikon pilih atau tampak untuk ikut memengaruhi anak-anaknya.

:::

### Kepala tampilan pohon {#tree-view-header}

Baris di atas daftar punya beberapa alat bantu:

* ![](/icons/sort_down.webp) - menciutkan atau membentangkan semua grup sekaligus.
* ![](/icons/preview.webp) - menyalakan/mematikan `Pratinjau objek`, gambar mini hasil render untuk setiap objek di daftar.
* ![](/icons/search.webp) - menyaring daftar berdasarkan nama.

### Mengatur tampilan pohon {#tree-view-manipulation}

Tekan lama sebuah item di tampilan pohon sampai item itu tersorot. Setelah itu Anda bisa memindahkannya ke atas atau ke bawah di tampilan pohon, atau menyeretnya ke atas item lain untuk menjadikannya anak dari item tersebut.

Jika banyak item dipilih, salah satunya menjadi pilihan utama dan digambar lebih terang. Tekan lama lalu seret salah satunya untuk memindahkan semua objek yang dipilih sekaligus.

Saat Anda memilih item induk, secara bawaan semua item anaknya juga ikut terpilih. Mengetuk induk lagi akan berganti antara memilih induknya saja, atau induk beserta anak-anaknya.

Ketuk dua kali sebuah item untuk memfokuskan kamera ke item tersebut (lihat [Lanjutan](#focus-on-item)).

### Menu objek {#object-menu}

Mengklik tombol elipsis (...) sebuah objek di tampilan pohon akan menampilkan menu objek.
Banyak opsi di sini mirip dengan bilah pintasan di bagian atas, diulang agar lebih praktis.

|       Aksi          |                        Ikon                        | Deskripsi                                                                                                                                                               |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Nama         |              ![](/icons/pencil.webp)           | Mengganti nama objek                                                                                                                                                    |
|  Batalkan instans   |              ![](/icons/unlink.webp)           | Mengubah instans menjadi bentuk yang berdiri sendiri, sehingga perubahan bentuk tidak lagi disalin ke instans lain.                                                    |
|      Instans        |               ![](/icons/link.webp)            | Menduplikasi objek sebagai instans, sehingga perubahan bentuk pada satu objek diterapkan ke semua instansnya.                                                          |
|      Kloning        |              ![](/icons/clone.webp)            | Menduplikasi objek menjadi objek baru                                                                                                                                   |
|       Hapus         |              ![](/icons/trash.webp)            | Menghapus objek. Anak-anaknya tetap dipertahankan, kecuali `Anak` dicentang.                                                                                           |
|        Anak         |            ![](/icons/hierarchy.webp)          | Jika dicentang, `Instans`, `Kloning`, dan `Hapus` juga berlaku pada anak-anak objek.                                                                                   |
| Pisah menurut Bagian |             ![](/icons/separate.webp)         | Jika objek terdiri dari beberapa bagian yang tidak terhubung, buat objek terpisah untuk masing-masing bagian. Kebalikan dari operasi gabung.                            |
| Pisah menurut Grup  |            ![](/icons/group.webp)          | Jika objek punya beberapa grup face, buat objek terpisah untuk setiap grup face.                                                                                           |
| Pisah menurut Lapisan |            ![](/icons/layer.webp)          | Jika objek punya lapisan, buat objek terpisah untuk mesh dasar dan setiap lapisan. Berguna untuk mengirim blendshape ke aplikasi lain.                                  |
|  Gabung → Lapisan   | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Jika beberapa objek dipilih dan topologinya sama persis, gabungkan objek-objek itu menjadi lapisan pada objek utama (objek lainnya akan dihapus). Ini juga berguna untuk blendshape yang datang DARI aplikasi lain.<br><br> Perlu diingat bahwa lapisan-lapisan tersebut nonaktif secara bawaan. Aktifkan jika Anda perlu mengatur penggesernya. |
|  Kurva (Pengulang)  |              ![](/icons/curve.webp)            | Hanya untuk tabung atau bubut: menambahkan pengulang [Kurva](#curve) yang mengikuti kurva yang sama, sebagai anak dari objek.                                          |
|       Tabung        |             ![](/icons/tube.webp)              | Untuk bubut, menambahkan [tabung](tools.md#tube) yang mengikuti profilnya, sebagai anak. Untuk silinder, kerucut, atau donat, mengubahnya menjadi tabung dengan bentuk yang sama, sehingga Anda bisa membengkokkannya mengikuti kurva. |




### Pilihan ganda {#multiselection}
Anda bisa memilih beberapa objek sekaligus untuk dua hal:
- memakai alat gizmo untuk memindahkan beberapa objek sekaligus
- menggabungkan objek dengan operasi gabung dan boolean.

Di tampilan pohon, ketuk ikon pilih setiap objek, atau seret di sepanjang kolom pilih. Saat mengetuk nama, tahan pintasan `Mask` (atau `Ctrl` pada keyboard) untuk menambah atau mengurangi satu objek, atau tahan pintasan `Haluskan` (atau `Shift`) untuk memilih semua objek di antara objek saat ini dan objek yang Anda ketuk.

::: tip Pilihan ganda cepat
Anda juga bisa memilih beberapa objek di viewport dengan menahan pintasan `Haluskan` (atau `Shift`) sambil mengetuk mesh lain.

Anda bisa membatalkan pilihan sebuah objek dengan mengetuknya lagi (hanya jika pilihan Anda berisi lebih dari satu objek).
:::

Gizmo memindahkan semua objek yang dipilih bersama-sama, lihat [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Gabung {#join}
Opsi ini cukup menjadikan beberapa objek yang dipilih sebagai satu entri objek.
Titik dan UV yang jaraknya lebih dekat dari [radius las](#weld-radius) akan disatukan.

Anda bisa melihat contohnya dalam video di bagian [Pisah](#separate).

## ![](/icons/bool_subtract_circle.webp) Boolean {#boolean}
![](/images/scene_boolean_menu.webp) 
Menggabungkan beberapa objek menjadi satu permukaan.

`Gabung voxel` mempertahankan volume objek, lalu menghitung poligon baru yang merata di permukaannya. Karena adanya tahap perhitungan ini, gabung voxel bisa menangani geometri yang rumit, tetapi bisa kehilangan detail halus jika resolusi targetnya tidak cukup tinggi.

`Boolean` berusaha mempertahankan susunan poligon aslinya, dan menjahit poligon di tempat objek-objek saling tumpang tindih. Hasilnya bisa jauh lebih rapi dan tajam dibanding gabung voxel, tetapi memerlukan mesh yang 'kedap air': tidak boleh ada lubang atau bentuk yang cacat pada objek. Jika gagal, biasanya gabung voxel akan berhasil.

### Operasi boolean {#boolean-operations}
Gabung voxel dan Boolean sama-sama memakai visibilitas objek untuk mengatur operasinya, seperti yang diingatkan di bagian bawah popup:

#### Gabungan {#union}
Kedua objek terlihat akan menghasilkan boolean **gabungan** (union): kulit luar objek-objek digabungkan, tanpa permukaan di bagian dalam. ![](/images/boolean_union.webp)

#### Pengurangan {#subtract}
Satu objek tersembunyi = boolean **pengurangan** (subtract): objek yang tersembunyi akan dikurangkan dari objek yang terlihat. ![](/images/boolean_subtract.webp)

#### Intersect {#intersect}
Kedua objek tersembunyi = boolean **irisan** (intersection): membuat bentuk baru hanya di bagian tempat kedua objek saling tumpang tindih. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Gabung voxel {#voxel-merge-button}
Menekan tombol ini akan menjalankan operasi gabung voxel pada objek yang dipilih. Jika dilakukan pada satu objek saja, objek itu akan diretopologi menjadi poligon yang merata, berguna saat objek punya poligon yang meregang. Opsi-opsi di bawah bekerja seperti opsi [Remesh voxel](topology.md#voxel-remesher).

### Resolusi {#resolution}
Resolusi grid 3d voxel yang dipakai untuk perhitungan. Saat nilai ini diubah, pola papan catur ditampilkan di atas objek sebagai pratinjau ukuran poligonnya.

Pipet di samping penggeser mengambil detail dari kepadatan mesh di bawah jari Anda. Tombol di sebelahnya mengubah penggeser menjadi `Panjang tepi`, ukuran dalam satuan dunia: nilai yang sama memberi detail yang sama pada objek apa pun.

### Bangun multiresolusi {#build-multiresolution}
Membuat level multiresolusi di bawah resolusi target Anda. Jadi jika resolusinya 400 dan bangun multiresolusi 3, Anda akan mendapat mesh baru dengan, katakanlah, 296.000 poligon, tetapi akan ada 3 level subdivisi lebih rendah dengan sekitar 74.000, 18.500, dan 4.600 poligon.

### Pertebal bagian tipis {#thicken-thin-parts}
Mempertebal bagian yang terlalu tipis untuk grid voxel, agar tidak terpecah. Opsi ini tidak tersedia bersama `Tepi tajam` atau `Batas tajam`.

### Lubang {#holes}
Cara lubang pada objek terbuka ditutup sebelum penggabungan:
* `Isi` - setiap lubang ditutup sendiri-sendiri, dari tepinya.
* `Bentuk` - lubang ditutup dengan mengikuti permukaan di sekitarnya, dan bagian terbuka yang saling tumpang tindih digabungkan.

### ![](/icons/angle.webp) Pertahankan tepi tajam {#keep-sharp-edges}
Tombol `Tepi tajam` menempelkan mesh voxel ke tepi tajam objek. Ini paling baik untuk bentuk sederhana, dan bisa menimbulkan distorsi di beberapa area.

### ![](/icons/group.webp) Batas tajam {#sharp-border}
Face baru mengikuti batas grup face, dan batas tetap tajam di tempat permukaan membentuk lipatan di sepanjangnya.

### ![](/icons/group_separate.webp) Pisahkan grup {#keep-groups-separate}
Setiap grup face di-remesh sendiri-sendiri: grup tidak pernah bergabung, dan masing-masing tetap menjadi bagian tertutup dalam grupnya sendiri. Multiresolusi tidak dibangun dalam mode ini.

### ![](/icons/bool_subtract_circle.webp) Tombol Boolean {#boolean-button}
Menekan tombol ini akan menjalankan operasi boolean poligon dengan pustaka Manifold karya Emmett Lalish.

### ![](/icons/bool_unite_circle.webp) Bersihkan Tumpang Tindih {#clean-overlaps}
Jika hanya satu objek yang dipilih, tombol `Boolean` berubah menjadi `Bersihkan Tumpang Tindih`: tombol ini menggabungkan bagian-bagian objek yang saling bersilangan menjadi satu permukaan yang rapi.


## ![](/icons/separate.webp) Pisah {#separate}
Jika Anda punya satu objek yang terdiri dari beberapa bagian yang tidak terhubung, Anda bisa memisahkannya menjadi beberapa objek.
Ini bisa dianggap kebalikan dari [Gabung](#join).

Popup `Pisah...` punya tiga cara untuk memisahkan objek yang dipilih:
* `Pisah menurut Bagian` - membuat objek terpisah untuk setiap bagian yang tidak terhubung.
* `Pisah menurut Grup` - membuat objek terpisah untuk setiap grup face.
* `Pisah menurut Lapisan` - membuat objek terpisah untuk mesh dasar dan setiap lapisan.

![](/videos/merge_separate.mp4)


## ![](/icons/plus.webp) Menu Tambahkan {#add-menu}

![](/images/scene_addmenu_overview.webp)

Menu ini membuat primitif, grup, kamera, pengulang, dan lampu.

Primitif adalah bentuk dasar yang bisa diatur dengan parameter. Setelah primitif diatur sesuai kebutuhan, Anda lalu 'memfinalisasinya', yang akan mengubah parameter tersebut menjadi mesh poligon yang bisa dipahat dan diwarnai. Parameter primitif tidak bisa diubah lagi setelah difinalisasi.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) Di atas gizmo {#on-gizmo}
Menempatkan primitif baru di posisi bentuk yang sedang dipilih atau di posisi gizmo. Jika dinonaktifkan, primitif akan ditempatkan di tengah adegan.

### ![](/icons/gizmo.webp) Pilih gizmo {#select-gizmo}
Otomatis beralih ke alat gizmo saat primitif baru dibuat.

### ![](/icons/cog.webp) Lanjutan {#add-advanced}

Menu ini memungkinkan Anda mengatur di mana primitif, grup, dan pengulang baru akan dibuat. Bisa di objek yang dipilih, di titik asal dunia, atau di lokasi gizmo.


### UV {#uvs}
Tombol `UVs` di samping judul Primitif mengaktifkan UV pada primitif. UV (sering disebut koordinat tekstur) adalah data tambahan yang dipakai dalam 3d agar tekstur bisa diterapkan ke permukaan. UV memakan lebih banyak memori, tetapi di sebagian besar perangkat hal ini tidak perlu dikhawatirkan kecuali jumlah poligon Anda sudah sangat tinggi (misalnya 10 juta poligon atau lebih).

### Primitif {#primitives}

| Primitif       | Ikon                                      | Deskripsi                                                                                                       |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Kotak          | ![](/icons/cube.webp)                    | Kubus sederhana; Anda bisa mengatur pembagiannya di X, Y, dan Z                                                 |
| Bola Kubus     | ![](/icons/circle.webp)                  | Kotak yang disubdivisi, dengan opsi `Bola` (proyeksi ke bola) dipaksa aktif, sehingga tata letak kuadnya merata dan bagus untuk memahat |
| Silinder       | ![](/icons/cylinder.webp)                | Anda bisa menambahkan lubang di tengah primitif silinder, misalnya untuk membuat pipa berongga                  |
| Donat          | ![](/icons/torus.webp)                   | Donat bisa menjadi titik awal yang bagus untuk membuat cincin                                                   |
| Kerucut        | ![](/icons/cone.webp)                    | -                                                                                                               |
| Ikosahedron    | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| Bola UV        | ![](/icons/circle.webp)                  | Bola dengan tata letak poligon yang tidak merata, lihat [Peringatan di bawah](#uv-sphere)                       |
| Bidang         | ![](/icons/rectangle.webp)               | Bidang sederhana; perlu diingat bahwa ini satu-satunya primitif yang tidak tertutup                             |
| Teks           | ![](/icons/text.webp)                    | Teks 3d, dengan font, gaya, perataan, kedalaman, dan tekukan. `Gabungkan huruf` menyatukan huruf-huruf yang bersentuhan |
| Tabung         | ![](/icons/tube.webp)                    | lihat [Tabung](tools#tube)                                                                                      |
| Bubut          | ![](/icons/lathe.webp)                   | lihat [Bubut](tools#lathe)                                                                                      |
| Triplanar      | ![](/icons/triplanar.webp)               | lihat [Triplanar](#triplanar)                                                                                   |
| VDM            | ![](/icons/vdm.webp)                     | Bidang yang disiapkan untuk memahat stempel vector displacement: sudah dilengkapi UV dan menghadap kamera       |
| Penangkap bayangan | ![](/icons/material_shadow_catcher.webp) | lihat [Penangkap bayangan](#shadow-catcher)                                                                 |
| Kepala         | ![](/icons/face.webp)                    | Kepala sederhana dengan lapisan untuk berpindah antara bentuk pria/wanita                                       |

::: tip
Jika Anda penasaran apa mesh dasar yang muncul saat Nomad dijalankan: itu juga kotak yang disubdivisi.
Namun mesh dasar di Nomad tidak memakai opsi `Bola` (proyeksi ke bola), artinya bentuknya tidak bulat sempurna.
:::

### Toolbar primitif {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

Setelah primitif dibuat, sebuah toolbar akan muncul untuk mengatur parameternya.

* `Finalisasi` Mengubah primitif menjadi objek biasa agar bisa dipahat dan diwarnai.
* `Cermin` Menempatkan atau menghapus pengulang cermin di atas primitif.
* `Semua` (ikon mata) Memilih pegangan mana yang ditampilkan langsung pada primitif untuk mengatur parameternya, misalnya lebar kubus atau radius lubang silinder: `Tidak ada`, `Semua`, atau hanya satu jenis (radius, lubang, profil...) tergantung primitifnya.
* `Pembagian` Jumlah pembagian primitif, di sini sepanjang X untuk kotak.
* `Kepadatan konstan` Saat Anda meregangkan primitif sepanjang satu sumbu dengan gizmo, ukuran dan jumlah pembagiannya ikut bertambah alih-alih poligonnya meregang, sehingga face tetap persegi. Tersedia untuk kotak, bidang, dan silinder.
* `...` Menampilkan menu primitif.

Primitif yang berbeda punya opsi tambahan di toolbar:

* `Bola` Bola dibangun dari kubus yang disubdivisi, karena lebih cocok untuk memahat, tetapi artinya bentuknya tidak bulat sempurna. Opsi ini memaksa bentuknya mendekati bola sempurna. Ikosahedron juga punya opsi ini.
* `Tutup` Menyalakan/mematikan tutup ujung pada sebuah bentuk, misalnya silinder bisa punya tutup di atas, di bawah, keduanya, atau tidak sama sekali.
* `Lubang` Membuat lubang yang menembus bagian tengah bentuk. Opsi ini berganti antara tanpa lubang, lubang dengan satu radius, atau lubang dengan radius berbeda di atas dan bawah.
* `Radius` Menentukan apakah silinder punya satu radius, atau radius berbeda di bagian atas dan bawahnya.
* `Cakram` Menentukan apakah bidang berbentuk segi empat atau lingkaran.

Toolbar kecil di bawah toolbar utama memungkinkan Anda berganti antara gizmo primitif dan gizmo transformasi.

::: tip

Mengklik judul toolbar akan memindahkannya ke bagian atas atau bawah layar. Mengklik panah di sudutnya akan menciutkannya.

:::


### Menu primitif {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Menu ini berisi semua parameter untuk primitif yang dipilih. Parameter adalah deskripsi dasar sebuah bentuk. Misalnya, untuk mendeskripsikan sebuah cincin, Anda akan menyebutkan radius luarnya, radius dalamnya, dan jumlah poligonnya.

Sebagian besar parameter primitif seharusnya sudah jelas dengan sendirinya, dan ada beberapa parameter umum yang dimiliki semua primitif:

* `UVs` Tombol kecil UVs di bagian atas menu akan menyalakan/mematikan pembuatan koordinat UV
* `Finalisasi` Tombol kecil finalisasi akan mengubah primitif menjadi objek biasa agar bisa dipahat dan diwarnai.
* `Face maksimum` Menetapkan batas atas jumlah poligon pada objek agar perangkat Anda tidak crash.
* `Pembagian pasca` Mengaktifkan sejumlah subdivisi yang dipilih dari bagian multiresolusi di menu topologi. Ini bisa dipakai untuk membuat primitif yang halus dengan sudut-sudut lembut, dikombinasikan dengan pembagian topologi yang rendah. Misalnya, mengatur pembagian topologi kotak ke 2, dan pembagian pasca ke 4, akan menghasilkan kotak dengan sudut-sudut halus.
* `Subdivisi linear` Menentukan berapa level subdivisi linear yang dipakai sebelum subdivisi halus biasa. Ini bisa dipakai untuk mengatur seberapa tajam atau lembut sudut-sudut permukaan yang disubdivisi. Misalnya, atur pembagian topologi kotak ke 2, pembagian pasca ke 4, lalu coba ubah subdivisi linear antara 0 dan 4. Sudut-sudut kotak akan berubah dari lembut menjadi tajam.

### Topologi {#topology}

Bagian ini mengatur jumlah poligon pada primitif. Biasanya kontrolnya saling terhubung, jadi mengubah satu penggeser yang aktif akan menyesuaikan semua poligon secara merata. Anda bisa mengetuk tombol putus tautan untuk mengatur pembagian X/Y/Z sebuah bentuk secara terpisah.

### Geometri {#geometry}

Bagian ini mengatur ukuran keseluruhan primitif, dalam satuan X/Y/Z untuk bentuk bersudut, dan dalam radius untuk bentuk bulat.


### ![](/icons/circle.webp) Bola UV {#uv-sphere}
::: warning
Bola UV kurang cocok untuk memahat, terutama di bagian kutubnya.

Sebaiknya gunakan [primitif](#primitives) Bola Kubus, Kotak, atau Ikosahedron, bersama opsi `Bola` (proyeksi ke bola).

Perlu diingat bahwa topologinya masih bisa diterima untuk memahat jika Anda memakai nilai yang sangat rendah pada penggeser `Pembagian`.
Setelah itu Anda bisa memakai penggeser `Subdivisi keseluruhan` untuk menambah jumlah poligon.

Meskipun tidak cocok untuk memahat secara umum, bola ini berguna untuk mata: jika Anda memutar bola sehingga kutubnya berada di pupil, tata letak poligonnya akan pas secara alami untuk mewarnai dan memahat iris dan pupil.
:::


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
Primitif ini istimewa karena Anda sebaiknya memakai [alat Topeng](tools.md#mask) padanya untuk membentuk geometrinya.

![](/videos/triplanar.mp4)


::: tip
Ketuk dua kali sebuah bidang, dan kamera akan fokus ke bidang tersebut.
Namun ini tidak akan berfungsi jika Anda memutar primitif dengan gizmo.
:::

Triplanar memakai informasi mask dari 3 bidang untuk mengisi grid voxel yang kemudian diubah menjadi poligon (berkat [Remesh voxel](topology.md#voxel-remesher)).

Setiap bidang punya bidang simetrinya sendiri.

::: warning
Setiap kali Anda mengubah ukuran primitif Triplanar, kualitas pewarnaan mask akan menurun.

Untuk saat ini belum ada opsi untuk 'mengunci' pewarnaan pada satu bidang saja, tetapi mungkin akan ada di masa mendatang.
Anda bisa memakai [Topologi terhubung](stroke.md#connected-topology) untuk sedikit membantu: jika kursor Anda tepat berada di satu bidang, bidang lain tidak akan terpengaruh.
:::

### ![](/icons/material_shadow_catcher.webp) Penangkap bayangan {#shadow-catcher}
Menambahkan bidang dengan material penangkap bayangan. Lihat [material Penangkap bayangan](material.md#shadow-catcher) untuk detail lebih lanjut.


## Grup/Kamera {#groupcamera}
### ![](/icons/share.webp) Grup {#group}
Membuat objek 'kosong' yang bisa menjadi induk bagi objek lain. Ini bisa dipakai untuk merapikan hierarki dengan menaruh banyak objek di bawah sebuah grup, lalu menciutkannya. Grup juga bisa dipakai sebagai alat bantu untuk memindahkan objek: banyak objek bisa ditaruh di bawah satu grup, lalu grupnya dipindahkan, diputar, atau diskalakan dengan alat gizmo.

### ![](/icons/camera.webp) Kamera {#add-view}
Membuat kamera.

## Pengulang {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Pengulang adalah node yang membuat instans dari objek-objek di bawahnya.

### ![](/icons/array.webp) Array {#array}
![](/images/scene_primitive_array.webp)

Jika objek dijadikan anak dari node ini, objek tersebut bisa diinstans dalam susunan grid. Saat dipilih, node ini punya kontrol untuk:
* `Pas di dalam` - jika aktif, semua salinan ditempatkan di dalam batas array; jika nonaktif, penggeser mengatur jarak antar salinan
* `Jumlah X/Y/Z` - jumlah instans di setiap sumbu
* `Ukuran X/Y/Z` - ukuran grid di setiap sumbu, atau jarak antar salinan jika `Pas di dalam` nonaktif
* `Acak...` - menambahkan variasi acak pada salinan, lihat [Acak](#curve) di bawah.

### ![](/icons/curve.webp) Kurva {#curve}
![](/images/scene_primitive_curve.webp)
Membuat sebuah kurva; anak-anak dari node ini akan diulang di sepanjang kurva. Saat dipilih, node ini punya kontrol untuk:
* `Kurva` - mengedit kurva: menambahkan titik pada kurva, dan memindahkan titik-titik kurva.
* `Tampilkan` - menampilkan atau menyembunyikan kurva beserta titik-titiknya.
* `Snap` - menempelkan titik kurva ke geometri lain.
* `Sim` - mengedit kurva secara simetris.
* `Tutup` - menyambungkan awal dan akhir kurva, atau membiarkannya sebagai kurva terbuka.
* `B-spline` - membuat instans mengikuti kurva dengan tepat, atau memakai interpolasi b-spline yang hasilnya lebih halus.
* `Lengkungkan` - membengkokkan setiap salinan mengikuti kurva, sehingga salinan bertemu dengan tetangganya (`Halus` membengkokkan sisi-sisinya agar bertemu tanpa sudut).
* `Sejajarkan` - memutar salinan agar mengikuti arah kurva.
* `Poros` - poros salinan: kurva itu sendiri (`Kurva`) atau anak-anaknya.
* `Jumlah` - jumlah instans. Tombol mode di sebelahnya beralih ke `Jarak`: jarak tetap antar salinan, dan jumlahnya mengikuti panjang kurva.
* `Radius` - kontrol di setiap titik kurva untuk mengatur skala instans.
* `Putar` - kontrol di setiap titik kurva untuk mengatur rotasi puntiran instans.
* `Bergantian` - memutar setiap salinan kedua di sekitar kurva: 90° untuk mata rantai, 180° untuk daun atau gigi ritsleting, di sekitar `Sumbu` yang Anda pilih.
* `Spiral...` - melilitkan salinan di sekitar kurva, dalam beberapa untaian (tali, kepang, pita...).
* `Acak...` - menambahkan variasi acak pada salinan; setiap baris juga bisa menambahkan nilai yang sama di setiap salinan.

Di bawah toolbar, tombol `(Gabungkan)` menyatukan sebuah titik ke titik lain saat Anda menyeretnya ke atasnya. `IK` (inverse kinematics) memungkinkan Anda mengatur pose kurva: seret sebuah titik dan titik-titik yang terhubung akan ikut bergerak. Ketuk sebuah titik untuk mengunci atau membuka kuncinya, tekan lama untuk mengunci atau membuka kunci semuanya; titik yang terkunci tetap di tempatnya.

### ![](/icons/radial.webp) Radial {#radial}
![](/images/scene_primitive_radial.webp)

Anak-anak dari node ini akan diinstans dalam bentuk lingkaran. Pindahkan objek anak untuk mengubah radius pengulang ini. Saat dipilih, node ini punya kontrol untuk:
* RadialX/Y/Z - memilih tombol ini akan menentukan sumbu radial, dan mengatur jumlah instans.



### ![](/icons/mirror.webp) Cermin {#mirror}
![](/images/scene_primitive_mirror.webp)

Anak-anak dari node ini akan dicerminkan terhadap sebuah sumbu. Saat dipilih, node ini punya kontrol untuk:
* Gizmo - mengaktifkan gizmo transformasi untuk mengatur pusat cermin. Gizmo ini juga bisa diputar dan diskalakan. Setelah selesai, ketuk gizmo lagi untuk menampilkan kontrol standar.
* X/Y/Z - menentukan bidang cermin

### ![](/icons/surface.webp) Permukaan {#surface}

Anak-anak dari node ini disalin ke permukaan sebuah objek: satu salinan per face, per edge, atau per verteks, atau disebar secara acak. Saat dipilih, node ini punya kontrol untuk:
* Mode - menempatkan salinan di `Face`, di `Edge`, atau di verteks, atau `Sebar` secara acak.
* Setiap - satu salinan setiap N face, edge, atau verteks. `Acak` memilihnya secara acak, dan `Acak ulang` membuat kumpulan acak yang lain.
* Jarak - saat menyebar, jarak minimum antara dua salinan.
* Sejajarkan - salinan berdiri di atas permukaan, mengikuti normalnya, alih-alih mempertahankan orientasi objek aslinya.
* Tempel - memproyeksikan objek asli ke titik permukaan terdekat, dan salinannya ikut.
* Sesuaikan ukuran, Miring - menskalakan dan meregangkan salinan sesuai bentuk setiap face.
* Lengkungkan - membengkokkan setiap salinan ke face-nya, atau di sepanjang edge-nya, sehingga salinan yang bersebelahan bertemu tanpa celah.

Semua pengulang punya kontrol `Finalisasi`, yang akan mengubah hasil pengulang menjadi objek permanen, dan akan menanyakan caranya:
* Gabungkan anak-anak - instans digabungkan menjadi satu objek
* Pertahankan instans - instans tetap menjadi instans, tetapi tidak lagi punya 'induk' pengulang
* Batalkan instans - instans diubah menjadi objek yang berdiri sendiri

`Ratakan semua` juga memfinalisasi pengulang yang bersarang di dalam pengulang ini, sehingga setiap salinan menjadi objek biasa.

::: tip Tips: Menggabungkan pengulang
Pengulang bisa dijadikan anak dari pengulang lain, dan beberapa objek bisa dijadikan anak dari pengulang, sehingga menghasilkan efek yang rumit.

![](/images/scene_repeater_combine.webp)
:::

::: tip Tips: Poros pengulang

Beberapa pengulang akan mencoba mengatur poros objek anak secara otomatis, sehingga meskipun Anda memindahkan atau memutarnya dengan alat gizmo, objek tersebut tidak akan bergerak. Jika Anda perlu mengabaikan perilaku ini, sisipkan sebuah grup di antara pengulang dan anaknya. Sekarang Anda bisa memindahkan bentuk anak secara terpisah dari pengulangnya.
:::

## Cahaya {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Arah {#directional}
Membuat lampu terarah (directional), sumber cahaya yang sangat jauh tak terhingga seperti matahari.

### ![](/icons/panorama.webp) Lingkungan {#environment}
Membuat lampu lingkungan, yang menerangi adegan dari sebuah gambar yang mengelilinginya (pencahayaan berbasis gambar, seperti HDRI).

### ![](/icons/spotlight.webp) Titik (spot) {#spot}
Membuat lampu sorot (spot), dengan kontrol untuk lebar kerucut dan kelembutannya

### ![](/icons/light.webp) Titik (point) {#point}
Membuat lampu titik (point)

## ![](/icons/cog.webp) Lanjutan {#advanced}
Tombol `Lanjutan` di kiri bawah panel membuka popup dengan dua tab: `Umum` dan `Sinkronkan`.

### ![](/icons/focus.webp) Antarmuka: Fokus pada item saat ketuk dua kali {#focus-on-item}
Mengetuk dua kali sebuah item di daftar Adegan akan memusatkan kamera ke item tersebut di tampilan 3d.

### ![](/icons/eye_open.webp) Sinkronisasi visibilitas {#sync-visibility}
Jika diaktifkan, memakai ikon mata pada item yang dipilih akan memengaruhi semua item yang dipilih.

### ![](/icons/bang.webp) Sorot {#highlight}
Menyorot objek yang dipilih di viewport saat pilihan berubah.

### ![](/icons/link.webp) Tampilkan (Instans) {#instance-show}
Menampilkan kapsul berwarna di sebelah kiri daftar adegan untuk menandai instans.

### ![](/icons/preview.webp) Pratinjau objek {#object-previews}
Menampilkan gambar mini hasil render untuk setiap objek di daftar adegan. Sama dengan tombol pratinjau di atas daftar.

### Radius las {#weld-radius}
Di bawah judul `Gabung`, ada `Radius Las Posisi` dan `Radius Las UV`: titik dan UV yang jaraknya lebih dekat dari radius ini akan disatukan. Masing-masing bisa dimatikan dengan kotak centangnya. Ini berlaku untuk Gabung, Boolean, Pangkas, Desimasi, remesh, dan impor file.

### Ikon {#icons}
Mengatur `Ukuran` minimum dan maksimum serta `Opasitas` ikon grup, lampu, kamera, dan pengulang di viewport.

### ![](/icons/hierarchy.webp) Garis Hirarki {#hierarchy-lines}
Menampilkan garis antara induk dan anak-anaknya di viewport. Jika diaktifkan, Anda juga bisa mengatur:
* `Gunakan pivot Nomad` - garis dimulai dari pivot yang dipakai oleh alat Transformasi dan Gizmo. Jika dinonaktifkan, garis memakai pivot dasar alami, yang bisa jauh dari pusat objek.
* `Ketebalan` - lebar garis. Tombol di samping penggeser menambahkan kontur pada garis.
* Warna garis.

### ![](/icons/link.webp) Sinkronkan {#sync}
Tab `Sinkronkan` menentukan, untuk setiap operasi (`Tambahkan`, `Hapus`, `Kunci`, `Kloning`, `Instans`, `Batalkan instans`, `Gabung`, `Pisah`, dan `Boolean`), apakah operasi itu diterapkan ke setiap instans dari pilihan:
* `Otomatis` - mengikuti kotak centang `Sinkronkan` di bagian atas menu adegan.
* `Tidak` - hanya objek yang dipilih.
* `Ya` - selalu setiap instans.

Secara bawaan `Gabung`, `Pisah`, dan `Boolean` diatur ke `Ya` dan sisanya ke `Otomatis`. `Setel ulang` mengembalikan pengaturan bawaan ini.

## Bilah alat bawah {#bottom-toolbar}
Ikon-ikon ini menyalakan/mematikan tampilan Grup, Cahaya, Kamera, Pengulang, dan Garis Hirarki di viewport. Ikon yang ditampilkan di kanvas bisa diketuk untuk memilih dan mengeditnya secara langsung.
