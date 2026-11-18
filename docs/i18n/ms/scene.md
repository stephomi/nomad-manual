# ![](/icons/scene.webp) Adegan {#scene}

Menu ini membolehkan anda mengurus objek, cahaya, kamera dan pengulang dalam Nomad. Ia memaparkan hierarki adegan sebagai paparan pepohon, yang membolehkan anda mengubah banyak aspek objek anda. Ia juga membolehkan anda mencipta objek baharu, serta menggabungkan dan memisahkan objek dengan pelbagai cara.


![](/images/scene_menu_summary.webp)


## Bar pintasan {#shortcut-bar}
| Tindakan               | Ikon                              | Penerangan                                                                                                          |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Tambah...](#add-menu) | ![](/icons/plus.webp)            | Paparkan [menu Tambah](#add-menu) untuk menambah objek ke adegan                                                    |
| Padam                  | ![](/icons/trash.webp)           | Padam objek yang dipilih. Anak-anaknya dikekalkan.                                                                  |
| Kunci                  | ![](/icons/lock.webp)            | Jadikan objek yang dipilih tidak boleh dipilih dalam ruang pandang. Objek ini masih boleh dipilih daripada paparan pepohon. Mengunci grup akan mengunci semua yang berada di bawahnya. Ketuk sekali lagi untuk membuka kunci. |
| [Gabung](#join)        | ![](/icons/merge.webp)           | Gabungkan objek yang dipilih menjadi satu objek tanpa mengubah geometri                                             |
| [Pisah...](#separate)  | ![](/icons/separate.webp)        | Paparkan popup [Pisah](#separate) untuk memecahkan objek kepada beberapa objek. Kebalikan operasi gabung            |
| [Boolean...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Paparkan popup [Boolean](#boolean)                                                                             |
| Klona                  | ![](/icons/clone.webp)           | Gandakan objek yang dipilih menjadi objek baharu                                                                    |
| Instans                | ![](/icons/link.webp)            | Gandakan objek yang dipilih sebagai instans, supaya perubahan pemodelan pada satu instans berlaku pada semua instans. |
| Batalkan instans       | ![](/icons/unlink.webp)          | Tukar instans kepada bentuk unik, supaya perubahan pemodelan tidak lagi disalin ke instans lain                     |
| Segerak                | ![](/icons/checked.webp)         | Apabila ditanda, operasi digunakan pada setiap instans objek yang dipilih, bukan hanya pada objek yang dipilih. Ia hanya tersedia apabila pilihan mengandungi instans. [Tab Segerak](#sync) dalam popup `Lanjutan` menetapkan operasi yang mengikut kotak semak ini. |

::: tip
Apabila sesuatu operasi turut mempengaruhi instans lain, ikon pautan kecil dipaparkan pada butangnya.
:::


## Paparan pepohon {#tree-view}
![](/images/scene_treeview.webp) 

Paparan pepohon menyenaraikan objek, grup, pengulang, cahaya dan kamera dalam adegan. Di sebelah nama mesh, anda akan melihat bilangan verteksnya, dengan ikon lapisan berwarna jika ia mempunyai lapisan. Setiap baris mempunyai butang berikut:

| Tindakan     | Ikon                       | Penerangan               |
| :----------: | :------------------------: | :----------------------: |
| Nama         | ![](/icons/pencil.webp)   | Namakan semula objek. Jika ia dipilih, semua objek yang dipilih dinamakan semula serentak, dengan nombor ditambah. Tekan lama untuk menamakannya semula bersama anak-anaknya. |
| Pilih        | ![](/icons/checked.webp)  | Pilih/nyahpilih          |
| Kelihatan    | ![](/icons/eye_open.webp) | Tunjuk/sembunyi          |
| Menu         | ![](/icons/more.webp)     | Paparkan [menu objek](#object-menu) |

::: tip PETUA: Pilih atau sembunyikan banyak objek dengan pantas

Ketuk ikon pilih untuk menukar satu objek, atau seret secara menegak pada lajur pilih untuk memilih banyak objek. Perkara yang sama boleh dilakukan dengan lajur kelihatan.

Tekan lama ikon pilih atau kelihatan untuk turut mempengaruhi anak-anaknya.

:::

### Pengepala paparan pepohon {#tree-view-header}

Baris di atas senarai mempunyai beberapa pembantu:

* ![](/icons/sort_down.webp) - kuncupkan atau kembangkan semua grup sekali gus.
* ![](/icons/preview.webp) - hidupkan atau matikan `Pratonton objek`, iaitu lakaran kenit kecil yang dirender bagi setiap objek dalam senarai.
* ![](/icons/search.webp) - tapis senarai mengikut nama.

### Manipulasi paparan pepohon {#tree-view-manipulation}

Tekan lama pada item dalam paparan pepohon sehingga ia diserlahkan. Kemudian anda boleh mengalihkannya ke atas atau ke bawah dalam paparan pepohon, atau menyeretnya ke atas item lain untuk menjadikannya anak kepada item tersebut.

Apabila banyak item dipilih, salah satunya ialah pilihan utama dan dilukis lebih terang. Tekan lama dan seret salah satu daripadanya untuk mengalihkan semua objek yang dipilih sekali gus.

Apabila anda memilih item induk, secara lalai semua item anak juga akan dipilih. Mengetuk induk sekali lagi akan bertukar antara memilih induk sahaja, atau induk bersama anak-anaknya.

Ketuk dua kali pada item untuk memfokuskan kamera padanya (lihat [Lanjutan](#focus-on-item)).

### Menu objek {#object-menu}

Mengklik butang elipsis (...) bagi objek dalam paparan pepohon akan memaparkan menu objek.
Kebanyakan pilihan ini serupa dengan bar pintasan di bahagian atas, diulang untuk kemudahan.

|       Tindakan      |                        Ikon                        | Penerangan                                                                                                                                                              |
| :-----------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Nama         |              ![](/icons/pencil.webp)           | Tukar nama objek                                                                                                                                                        |
|  Batalkan instans   |              ![](/icons/unlink.webp)           | Tukar instans kepada bentuk unik, supaya perubahan pemodelan tidak lagi disalin ke instans lain.                                                                        |
|      Instans        |               ![](/icons/link.webp)            | Gandakan objek sebagai instans, supaya perubahan pemodelan pada satu instans berlaku pada semua instans.                                                                |
|        Klona        |              ![](/icons/clone.webp)            | Gandakan objek menjadi objek baharu                                                                                                                                     |
|        Padam        |              ![](/icons/trash.webp)            | Padam objek. Anak-anaknya dikekalkan, kecuali jika `Anak-anak` ditanda.                                                                                                 |
|     Anak-anak       |            ![](/icons/hierarchy.webp)          | Apabila ditanda, `Instans`, `Klona` dan `Padam` turut bertindak pada anak-anak objek.                                                                                   |
| Pisah mengikut Bahagian |          ![](/icons/separate.webp)          | Jika objek terdiri daripada bahagian yang tidak bersambung, cipta objek berasingan bagi setiap bahagian. Kebalikan operasi gabung.                                     |
| Pisah mengikut Kumpulan |          ![](/icons/group.webp)          | Jika objek mempunyai beberapa kumpulan muka, cipta objek berasingan bagi setiap kumpulan muka.                                                                            |
| Pisah mengikut Lapisan  |            ![](/icons/layer.webp)            | Jika objek mempunyai lapisan, cipta objek berasingan bagi mesh asas dan setiap lapisan. Berguna untuk menghantar blendshape ke aplikasi lain.                          |
|  Gabung → Lapisan   | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Jika beberapa objek dipilih dan mempunyai topologi yang sepadan, gabungkan objek-objek tersebut menjadi lapisan bagi objek utama (objek lain akan dipadam). Sekali lagi, berguna untuk blendshape yang datang DARIPADA aplikasi lain.<br><br> Perhatikan bahawa lapisan tersebut dinyahaktifkan secara lalai. Dayakannya jika anda perlu melaraskan peluncurnya. |
|  Lengkung (Pengulang) |            ![](/icons/curve.webp)            | Hanya untuk tiub atau pelarik: tambah pengulang [Lengkung](#curve) yang mengikut lengkung yang sama, sebagai anak objek tersebut.                                     |
|        Tiub         |             ![](/icons/tube.webp)              | Untuk pelarik, tambah [tiub](tools.md#tube) yang mengikut profilnya, sebagai anak. Untuk silinder, kon atau torus, tukarkannya kepada tiub dengan bentuk yang sama, supaya anda boleh melenturkannya mengikut lengkung. |




### Pemilihan berganda {#multiselection}
Anda boleh memilih beberapa objek untuk mencapai dua perkara:
- menggunakan alat gizmo untuk menggerakkan beberapa objek sekali gus
- menggabungkan objek menggunakan operasi gabung dan boolean.

Dalam paparan pepohon, ketuk ikon pilih bagi setiap objek, atau seret sepanjang lajur pilih. Apabila mengetuk nama, tahan pintasan `Topeng` (atau `Ctrl` pada papan kekunci) untuk menambah atau membuang satu objek, atau tahan pintasan `Lancar` (atau `Shift`) untuk memilih setiap objek di antara objek semasa dan objek yang anda ketuk.

::: tip Pemilihan berganda pantas
Anda juga boleh membuat pemilihan berganda dalam ruang pandang dengan menahan pintasan `Lancar` (atau `Shift`) dan mengetuk mesh lain.

Anda boleh menyahpilih objek dengan mengetuknya sekali lagi (hanya jika pilihan anda mempunyai lebih daripada satu objek).
:::

Gizmo menggerakkan semua objek yang dipilih bersama-sama, lihat [Gizmo](tools.md#gizmo).


## ![](/icons/merge.webp) Gabung {#join}
Pilihan ini hanya menjadikan beberapa objek yang dipilih sebagai satu entri objek.
Titik dan UV yang lebih dekat daripada [jejari kimpalan](#weld-radius) akan digabungkan.

Anda boleh melihat contoh dalam video di bahagian [Pisah](#separate).

## ![](/icons/bool_subtract_circle.webp) Boolean {#boolean}
![](/images/scene_boolean_menu.webp) 
Gabungkan objek menjadi satu permukaan.

`Merge voxel` mengekalkan isi padu objek, dan mengira poligon baharu yang jaraknya sekata pada permukaan. Disebabkan langkah pengiraan ini, merge voxel boleh mengendalikan geometri yang kompleks, tetapi boleh kehilangan perincian halus jika resolusi sasaran tidak cukup tinggi.

`Boolean` cuba mengekalkan susun atur asal poligon, dan menjahit poligon di tempat objek bertindih. Ini boleh menghasilkan keputusan yang jauh lebih bersih dan tajam berbanding merge voxel, namun ia memerlukan mesh yang 'kedap air'; tidak boleh ada lubang atau bentuk yang cacat pada objek. Jika ia gagal, biasanya merge voxel akan berjaya.

### Operasi boolean {#boolean-operations}
Merge voxel dan Boolean kedua-duanya menggunakan keterlihatan objek untuk mengawal operasi, seperti yang diingatkan di bahagian bawah popup:

#### Kesatuan {#union}
Kedua-dua objek kelihatan akan menghasilkan **kesatuan** boolean: kulit luar objek digabungkan, tanpa permukaan dalaman. ![](/images/boolean_union.webp)

#### Tolakan {#subtract}
Satu objek tidak kelihatan = **tolakan** boolean: objek yang tidak kelihatan akan ditolak daripada objek yang kelihatan. ![](/images/boolean_subtract.webp)

#### Persimpangan {#intersect}
Kedua-dua objek tidak kelihatan = **persimpangan** boolean: cipta bentuk baharu hanya di tempat kedua-dua objek bertindih. ![](/images/boolean_intersect.webp)


### ![](/icons/voxel.webp) Merge voxel {#voxel-merge-button}
Menekan butang ini akan melakukan operasi merge voxel pada objek yang dipilih. Apabila dilakukan pada satu objek, ia akan membina semula topologi menjadi poligon yang jaraknya sekata, berguna apabila objek mempunyai poligon yang teregang. Pilihan di bawah berfungsi seperti pilihan [Remes voxel](topology.md#voxel-remesher).

### Resolusi {#resolution}
Resolusi grid voxel 3d yang digunakan untuk pengiraan. Apabila nilai ini diubah, corak papan dam ditindih pada objek untuk mempratonton saiz poligon.

Pemilih di sebelah peluncur mengambil perincian daripada ketumpatan mesh di bawah jari anda. Butang di sebelahnya menukar peluncur kepada `Panjang tepi`, iaitu saiz dalam dunia: nilai yang sama memberikan perincian yang sama pada mana-mana objek.

### Bina multiresolusi {#build-multiresolution}
Cipta tahap multiresolusi di bawah resolusi sasaran anda. Jadi jika resolusi anda 400 dan bina multiresolusi ialah 3, anda akan mendapat mesh baharu dengan, katakan, 296,000 poligon, tetapi akan ada 3 tahap pembahagian yang lebih rendah pada kira-kira 74,000, 18,500 dan 4,600.

### Tebalkan bahagian nipis {#thicken-thin-parts}
Tebalkan bahagian yang terlalu nipis untuk grid voxel, supaya ia tidak terpecah. Ia tidak tersedia dengan `Tepi tajam` atau `Sempadan tajam`.

### Lubang {#holes}
Cara lubang pada objek terbuka ditutup sebelum penggabungan:
* `Isi` - setiap lubang ditutup secara berasingan, daripada sempadannya.
* `Bentuk` - lubang ditutup dengan mengikut permukaan di sekelilingnya, dan kepingan terbuka yang bertindih akan dicantumkan.

### ![](/icons/angle.webp) Kekalkan tepi tajam {#keep-sharp-edges}
Butang `Tepi tajam` melekapkan mesh voxel pada tepi tajam objek. Ini paling sesuai untuk bentuk ringkas, dan ia boleh menyebabkan herotan di sesetengah kawasan.

### ![](/icons/group.webp) Sempadan tajam {#sharp-border}
Muka baharu mengikut sempadan kumpulan muka, dan sempadan kekal tajam di tempat permukaan berlipat di sepanjangnya.

### ![](/icons/group_separate.webp) Asingkan kumpulan {#keep-groups-separate}
Setiap kumpulan muka di-remesh secara berasingan: kumpulan tidak pernah bercantum, dan setiap satu kekal sebagai kepingan tertutup dalam kumpulannya sendiri. Multiresolusi tidak dibina dalam mod ini.

### ![](/icons/bool_subtract_circle.webp) Butang Boolean {#boolean-button}
Menekan butang ini akan melakukan operasi boolean poligon menggunakan pustaka Manifold oleh Emmett Lalish.

### ![](/icons/bool_unite_circle.webp) Bersihkan Pertindihan {#clean-overlaps}
Apabila hanya satu objek dipilih, butang `Boolean` menjadi `Bersihkan Pertindihan`: ia menggabungkan bahagian objek yang bersilang antara satu sama lain menjadi permukaan yang bersih.

## ![](/icons/separate.webp) Pisah {#separate}
Jika anda mempunyai satu objek yang terdiri daripada beberapa bahagian yang tidak bersambung, anda boleh memisahkan objek ini kepada beberapa objek.
Ini boleh dianggap sebagai kebalikan [Gabung](#join).

Popup `Pisah...` mempunyai tiga cara untuk memisahkan objek yang dipilih:
* `Pisah mengikut Bahagian` - cipta objek berasingan bagi setiap bahagian yang tidak bersambung.
* `Pisah mengikut Kumpulan` - cipta objek berasingan bagi setiap kumpulan muka.
* `Pisah mengikut Lapisan` - cipta objek berasingan bagi mesh asas dan setiap lapisan.

![](/videos/merge_separate.mp4)


## ![](/icons/plus.webp) Menu Tambah {#add-menu}

![](/images/scene_addmenu_overview.webp)

Menu ini mencipta primitif, grup, kamera, pengulang dan cahaya.

Primitif ialah jenis bentuk asas yang boleh dilaraskan menggunakan parameter. Setelah primitif dilaraskan mengikut keperluan anda, anda kemudian 'memuktamadkannya', yang menukar parameter tersebut menjadi mesh poligon yang boleh diukir dan dicat. Parameter primitif tidak boleh dilaraskan lagi selepas ia dimuktamadkan.


![](/images/scene_addmenu_top.webp)

### ![](/icons/gizmo.webp) Pada gizmo {#on-gizmo}
Dayakan untuk meletakkan primitif baharu di tempat bentuk yang sedang dipilih atau gizmo berada. Apabila dinyahaktifkan, primitif akan diletakkan di tengah adegan.

### ![](/icons/gizmo.webp) Pilih gizmo {#select-gizmo}
Dayakan untuk bertukar secara automatik kepada alat gizmo apabila primitif baharu dicipta.

### ![](/icons/cog.webp) Lanjutan {#add-advanced}

Menu ini membolehkan anda menetapkan tempat primitif, grup dan pengulang baharu akan dicipta. Ia boleh dicipta pada objek yang dipilih, di asalan dunia, atau di lokasi gizmo.


### UV {#uvs}
Suis `UVs` di sebelah tajuk Primitif mendayakan UV pada primitif. UV (sering dipanggil koordinat tekstur) ialah data tambahan yang digunakan dalam 3d untuk membolehkan tekstur dipasang pada permukaan. Ia menggunakan lebih banyak memori, tetapi bagi kebanyakan peranti ini tidak sepatutnya menjadi masalah melainkan anda mencapai bilangan poligon yang sangat tinggi (contohnya 10 juta poligon atau lebih).

### Primitif {#primitives}

| Primitif          | Ikon                                      | Penerangan                                                                                                      |
| :---------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Kotak             | ![](/icons/cube.webp)                    | Kiub ringkas, anda boleh mengawal pembahagian dalam X, Y dan Z                                                  |
| Sfera Kuad        | ![](/icons/circle.webp)                  | Kotak yang dibahagikan, dengan `Project on sphere` dipaksa, jadi ia mempunyai susun atur kuad yang sekata dan sesuai untuk mengukir |
| Silinder          | ![](/icons/cylinder.webp)                | Anda boleh menambah lubang tengah pada primitif silinder, contohnya untuk membuat paip berongga                   |
| Torus             | ![](/icons/torus.webp)                   | Torus boleh menjadi titik permulaan yang baik untuk cincin                                                       |
| Kon               | ![](/icons/cone.webp)                    | -                                                                                                               |
| Ikosahedron       | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| Sfera UV          | ![](/icons/circle.webp)                  | Sfera dengan susun atur poligon yang tidak sekata, lihat [Amaran di bawah](#uv-sphere)                          |
| Satah             | ![](/icons/rectangle.webp)               | Satah ringkas, perhatikan bahawa ini satu-satunya primitif yang tidak tertutup                                   |
| Teks              | ![](/icons/text.webp)                    | Teks 3d, dengan fon, gaya, penjajaran, kedalaman dan lenturan. `Gabungkan huruf` mencantumkan huruf yang bersentuhan |
| Tiub              | ![](/icons/tube.webp)                    | lihat [Tiub](tools#tube)                                                                                        |
| Pelarik           | ![](/icons/lathe.webp)                   | lihat [Larik](tools#lathe)                                                                                      |
| Triplanar         | ![](/icons/triplanar.webp)               | lihat [Triplanar](#triplanar)                                                                                   |
| VDM               | ![](/icons/vdm.webp)                     | Satah yang disediakan untuk mengukir cop anjakan vektor: ia termasuk UV dan menghadap kamera                    |
| Penangkap bayang  | ![](/icons/material_shadow_catcher.webp) | lihat [Penangkap bayang](#shadow-catcher)                                                                       |
| Kepala            | ![](/icons/face.webp)                    | Kepala ringkas dengan lapisan untuk mengadun antara lelaki/perempuan                                            |

::: tip
Jika anda tertanya-tanya apakah mesh asas semasa anda melancarkan Nomad: ia juga kotak yang dibahagikan.
Walau bagaimanapun, mesh asas dalam Nomad tidak menggunakan `Project on sphere`, bermakna ia tidak bulat dengan sempurna.
:::

### Bar alat primitif {#primitive-toolbar}

![](/images/scene_primitive_toolbar.webp)

Setelah primitif dicipta, bar alat akan muncul untuk mengawal parameternya.

* `Muktamadkan` Tukarkan primitif menjadi objek biasa supaya ia boleh diukir dan dicat.
* `Cermin` Hidupkan atau matikan pengulang cermin di atas primitif.
* `Semua` (ikon mata) Pilih pemegang yang dipaparkan terus pada primitif untuk mengawal parameternya, contohnya lebar kiub atau jejari lubang silinder: `Tiada`, `Semua`, atau hanya satu jenis (jejari, lubang, profil...) bergantung pada primitif.
* `Pembahagian` Bilangan pembahagian primitif, di sini sepanjang X bagi kotak.
* `Ketumpatan tetap` Apabila anda meregangkan primitif sepanjang satu paksi dengan gizmo, saiz dan pembahagiannya bertambah dan bukannya poligonnya teregang, jadi muka kekal segi empat sama. Tersedia pada kotak, satah dan silinder.
* `...` Paparkan menu primitif.

Primitif yang berbeza mempunyai pilihan tambahan pada bar alat:

* `Sfera` Sfera dibina sebagai kiub yang dibahagikan, kerana ini lebih baik untuk mengukir, tetapi ini bermakna ia tidak bulat dengan sempurna. Pilihan ini memaksa bentuk menjadi lebih hampir kepada sfera sempurna. Ikosahedron berkongsi pilihan ini.
* `Tutup` Hidupkan atau matikan penutup hujung pada bentuk, contohnya silinder boleh mempunyai penutup di atas, di bawah, kedua-duanya atau tiada.
* `Lubang` Hidupkan atau matikan lubang yang menembusi tengah bentuk. Ia bergilir antara tiada lubang, lubang dengan satu jejari, atau lubang dengan jejari berbeza di atas dan di bawah.
* `Jari-jari` Tentukan sama ada silinder mempunyai satu jejari, atau jejari yang berbeza di atas dan di bawahnya.
* `Cakera` Tentukan sama ada satah berbentuk empat sisi atau bulat.

Bar alat kecil di bawah bar alat utama membolehkan anda bertukar antara gizmo primitif dan gizmo transformasi.

::: tip

Mengklik tajuk bar alat akan mengalihkannya ke bahagian atas atau bawah paparan. Mengklik anak panah di sudut akan menguncupkannya.

:::


### Menu primitif {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Menu ini mengandungi semua parameter bagi primitif yang dipilih. Parameter ialah penerangan asas sesuatu bentuk. Untuk menerangkan cincin, contohnya, anda menerangkan jejari luarnya, jejari dalamnya dan bilangan poligonnya.

Kebanyakan parameter primitif sepatutnya mudah difahami, dan terdapat beberapa parameter biasa yang dikongsi oleh semua primitif:

* `UVs` Butang UVs kecil di bahagian atas menu menghidupkan atau mematikan penciptaan koordinat UV
* `Muktamadkan` Butang muktamadkan kecil akan menukar primitif menjadi objek biasa supaya ia boleh diukir dan dicat.
* `Muka maksimum` Tetapkan had atas bilangan poligon dalam objek untuk mengelakkan peranti anda ranap.
* `Pembahagian selepas` Dayakan bilangan pembahagian yang dipilih daripada bahagian multiresolusi dalam menu topologi. Ini boleh digunakan untuk membuat primitif yang licin dengan bucu lembut, digabungkan dengan pembahagian topologi yang rendah. Contohnya, menetapkan pembahagian topologi kotak kepada 2, dan pembahagian selepas kepada 4, akan menghasilkan kotak dengan bucu yang licin.
* `Pembahagian linear` Tetapkan berapa tahap pembahagian linear yang digunakan sebelum menggunakan pembahagian licin biasa. Ini boleh digunakan untuk mengawal sejauh mana tajam atau lembutnya bucu pada permukaan yang dibahagikan. Contohnya, tetapkan pembahagian topologi kotak kepada 2, pembahagian selepas kepada 4, kemudian cuba ubah pembahagian linear antara 0 dan 4. Bucu kotak akan berubah daripada lembut kepada tajam.

### Topologi {#topology}

Ini mengawal bilangan poligon dalam primitif. Biasanya kawalan-kawalan ini dipautkan, jadi mengubah satu peluncur aktif akan melaraskan semua poligon secara sekata. Anda boleh mengetuk butang nyahpaut untuk mengawal pembahagian X/Y/Z pada bentuk secara berasingan.

### Geometri {#geometry}

Ini mengawal saiz keseluruhan primitif, dalam unit X/Y/Z untuk bentuk bersegi, dan dalam jejari untuk bentuk bulat.


### ![](/icons/circle.webp) Sfera UV {#uv-sphere}
::: warning
Sfera UV tidak sesuai untuk mengukir, terutamanya di bahagian kutub.

Sebaiknya gunakan [primitif](#primitives) Sfera Kuad, Kotak atau Ikosahedron, bersama pilihan `Project on sphere`.

Perhatikan bahawa topologinya boleh diterima untuk mengukir jika anda menggunakan nilai yang sangat rendah untuk peluncur `Pembahagian`.
Kemudian anda boleh menggunakan peluncur `Overall Subdivision` untuk menaikkan bilangan poligon.

Walaupun tidak sesuai untuk mengukir secara umum, ia berguna untuk mata; jika anda memutar sfera supaya kutubnya berada di anak mata, susun atur poligon akan sesuai secara semula jadi untuk mengecat dan mengukir iris dan anak mata.
:::

### ![](/icons/triplanar.webp) Triplanar {#triplanar}
Primitif ini istimewa kerana anda perlu menggunakan [alat Topeng](tools.md#mask) padanya untuk membentuk geometri.

![](/videos/triplanar.mp4)


::: tip
Ketuk dua kali pada satah dan kamera akan memfokus pada satah tersebut.
Namun, ini tidak akan berfungsi jika anda memutar primitif dengan gizmo.
:::

Triplanar menggunakan maklumat topeng daripada 3 satah untuk mengisi grid voxel yang kemudiannya ditukar menjadi poligon (melalui [Remes voxel](topology.md#voxel-remesher)).

Setiap satah mempunyai satah simetrinya sendiri.

::: warning
Setiap kali anda mengubah saiz primitif Triplanar, kualiti lukisan topeng akan merosot.

Buat masa ini tiada pilihan untuk 'mengunci' lukisan pada satu satah, tetapi mungkin ia akan datang pada masa hadapan.
Anda boleh menggunakan [Topologi bersambung](stroke.md#connected-topology) untuk membantu sedikit: jika kursor anda berada tepat pada satu satah, ia tidak akan menjejaskan satah lain.
:::

### ![](/icons/material_shadow_catcher.webp) Penangkap bayang {#shadow-catcher}
Tambah satah dengan bahan penangkap bayang. Lihat [bahan Penangkap bayang](material.md#shadow-catcher) untuk butiran lanjut.


## Grup/Kamera {#groupcamera}
### ![](/icons/share.webp) Grup {#group}
Cipta objek 'kosong' yang boleh menjadi induk kepada objek lain. Ini boleh digunakan untuk menyusun hierarki dengan meletakkan banyak objek di bawah grup, kemudian menutupnya. Grup juga boleh digunakan sebagai pembantu untuk menggerakkan objek; banyak objek boleh diletakkan di bawah grup, dan kemudian grup itu digerakkan, diputar atau diskala dengan alat gizmo.

### ![](/icons/camera.webp) Kamera {#add-view}
Cipta kamera.

## Repeater {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Pengulang ialah nod yang membuat instans bagi objek di bawahnya.

### ![](/icons/array.webp) Tatasusunan {#array}
![](/images/scene_primitive_array.webp)

Apabila objek dijadikan anak kepada nod ini, ia boleh dijadikan instans dalam susun atur grid. Apabila dipilih, ia mempunyai kawalan untuk:
* `Sesuaikan dalam` - apabila hidup, semua salinan diletakkan di dalam sempadan tatasusunan; apabila mati, peluncur menetapkan jarak antara salinan
* `Kiraan X/Y/Z` - bilangan instans pada setiap paksi
* `Saiz X/Y/Z` - saiz grid sepanjang setiap paksi, atau jarak antara salinan apabila `Sesuaikan dalam` dimatikan
* `Rawakkan...` - menambah variasi rawak pada salinan, lihat [Rawakkan](#curve) di bawah.

### ![](/icons/curve.webp) Lengkung {#curve}
![](/images/scene_primitive_curve.webp)
Ini mencipta lengkung, dan anak-anak nod ini akan diulang sepanjang lengkung. Apabila dipilih, ia mempunyai kawalan untuk:
* `Lengkung` - sunting lengkung: tambah titik pada lengkung, dan gerakkan titik pada lengkung.
* `Tunjuk` - tunjukkan atau sembunyikan lengkung dan titik-titiknya.
* `Snap` - lekapkan titik lengkung pada geometri lain.
* `Sim` - sunting lengkung secara simetri.
* `Tertutup` - tentukan sama ada lengkung menyambungkan permulaan dan penghujungnya, atau kekal sebagai lengkung terbuka.
* `B-spline` - tentukan sama ada instans mengikut lengkung dengan tepat, atau menggunakan interpolasi b-spline yang memberikan hasil lebih licin.
* `Lenturkan` - lenturkan setiap salinan sepanjang lengkung, supaya salinan bertemu dengan jirannya (`Licin` melenturkan sisinya supaya ia bertemu tanpa sudut).
* `Selaras` - putar salinan untuk mengikut arah lengkung.
* `Poros` - poros salinan: lengkung itu sendiri (`Lengkung`) atau anak-anaknya.
* `Kiraan` - bilangan instans. Butang mod di sebelahnya menukar kepada `Jarak`: jarak tetap antara salinan, dan kiraan mengikut panjang lengkung.
* `Jejari` - kawalan pada setiap titik lengkung untuk menetapkan skala instans.
* `Pintalan` - kawalan pada setiap titik lengkung untuk menetapkan putaran pintalan instans.
* `Berselang-seli` - pusingkan setiap salinan yang berselang di sekitar lengkung: 90° untuk mata rantai, 180° untuk daun atau gigi zip, di sekitar `Paksi` yang anda pilih.
* `Lingkaran...` - lilitkan salinan di sekeliling lengkung, dalam beberapa lembar (tali, jalinan, reben...).
* `Rawakkan...` - tambah variasi rawak pada salinan; setiap baris boleh sebaliknya menambah jumlah yang sama pada setiap salinan.

Di bawah bar alat, suis `(gabungkan)` menggabungkan satu titik ke titik lain apabila anda menyeretnya ke atasnya. `IK` (kinematik songsang) membolehkan anda mengatur pose lengkung: seret satu titik dan titik-titik yang bersambung akan mengikut. Ketuk titik untuk mengunci atau membuka kuncinya, tekan lama untuk mengunci atau membuka kunci semuanya; titik yang dikunci kekal di tempatnya.

### ![](/icons/radial.webp) Radial {#radial}
![](/images/scene_primitive_radial.webp)

Anak-anak nod ini akan dijadikan instans dalam bentuk bulatan. Gerakkan objek anak untuk mengubah jejari pengulang ini. Apabila dipilih, ia mempunyai kawalan untuk:
* RadialX/Y/Z - memilih butang ini akan menetapkan paksi radial, dan menetapkan bilangan instans.



### ![](/icons/mirror.webp) Cermin {#mirror}
![](/images/scene_primitive_mirror.webp)

Anak-anak nod ini akan dicerminkan merentasi satu paksi. Apabila dipilih, ia mempunyai kawalan untuk:
* Gizmo - dayakan gizmo transformasi untuk menetapkan pusat cermin. Ia juga boleh diputar dan diskala. Apabila selesai, ketuk gizmo sekali lagi untuk memaparkan kawalan biasa.
* X/Y/Z - tetapkan satah cermin

### ![](/icons/surface.webp) Permukaan {#surface}

Anak-anak nod ini disalin pada permukaan sesuatu objek: satu salinan bagi setiap muka, setiap tepi atau setiap verteks, atau ditabur secara rawak. Apabila dipilih, ia mempunyai kawalan untuk:
* Mod - letakkan salinan pada `Muka`, `Tepi` atau verteks, atau `Tabur` salinan tersebut.
* Setiap - satu salinan bagi setiap N muka, tepi atau verteks. `Rawak` memilihnya secara rawak, dan `Kocok` mencabut set rawak yang lain.
* Jarak - semasa menabur, jarak minimum antara dua salinan.
* Selaras - salinan berdiri pada permukaan, mengikut normalnya, dan bukannya mengekalkan orientasi objek asal.
* Lekap - unjurkan objek asal ke titik permukaan terdekat, dan salinan akan mengikut.
* Sesuaikan saiz, Serong - skala dan regangkan salinan mengikut bentuk setiap muka.
* Lenturkan - lenturkan setiap salinan pada mukanya, atau sepanjang tepinya, supaya salinan yang berjiran bertemu tanpa celah.

Semua pengulang mempunyai kawalan `Muktamadkan`, yang akan menukar hasil pengulang menjadi objek tetap, dan akan bertanya cara melakukannya:
* Gabung anak-anak - instans digabungkan menjadi satu objek
* Kekalkan instans - instans kekal sebagai instans, tetapi tidak lagi mempunyai 'induk' pengulang
* Batalkan instans - instans ditukar menjadi objek unik

`Leperkan semua` turut memuktamadkan pengulang yang bersarang di dalam pengulang ini, jadi setiap salinan menjadi objek biasa.

::: tip Petua: Gabungkan pengulang
Pengulang boleh dijadikan induk antara satu sama lain, dan beberapa objek boleh dijadikan anak kepada pengulang, menghasilkan kesan yang kompleks.

![](/images/scene_repeater_combine.webp)
:::

::: tip Petua: Poros pengulang

Sesetengah pengulang akan cuba menetapkan poros objek anak secara automatik, jadi walaupun anda menggerakkan atau memutarnya dengan alat gizmo, ia tidak akan bergerak. Jika anda perlu mengatasi tingkah laku ini, sisipkan grup di antara pengulang dan objek anak. Kini anda boleh menggerakkan bentuk anak secara bebas daripada pengulang.
:::

## Cahaya {#light}

![](/images/scene_primitive_light.webp)

### ![](/icons/sun.webp) Bercahaya arah {#directional}
Cipta cahaya berarah, iaitu sumber cahaya yang jauhnya tidak terhingga seperti matahari.

### ![](/icons/panorama.webp) Persekitaran {#environment}
Cipta cahaya persekitaran, yang menerangi adegan daripada imej di sekelilingnya (pencahayaan berasaskan imej, seperti HDRI).

### ![](/icons/spotlight.webp) Spot {#spot}
Cipta lampu sorot, dengan kawalan ke atas lebar kon dan kelembutannya.

### ![](/icons/light.webp) Titik {#point}
Cipta cahaya titik.

## ![](/icons/cog.webp) Lanjutan {#advanced}
Butang `Lanjutan` di bahagian kiri bawah panel membuka popup dengan dua tab: `Umum` dan `Segerak`.

### ![](/icons/focus.webp) UI: Fokus pada item semasa ketukan dua kali {#focus-on-item}
Mengetuk dua kali pada item dalam senarai Adegan akan memusatkan kamera pada item tersebut dalam paparan 3d.

### ![](/icons/eye_open.webp) Sinkronkan Visibilitas {#sync-visibility}
Apabila didayakan, menggunakan ikon mata pada item yang dipilih akan mempengaruhi semua item yang dipilih.

### ![](/icons/bang.webp) Sorotan {#highlight}
Serlahkan objek yang dipilih dalam ruang pandang apabila pilihan berubah.

### ![](/icons/link.webp) Tunjuk (Instans) {#instance-show}
Paparkan kapsul berwarna di sebelah kiri senarai adegan untuk menunjukkan instans.

### ![](/icons/preview.webp) Pratonton objek {#object-previews}
Paparkan lakaran kenit yang dirender bagi setiap objek dalam senarai adegan. Ia sama seperti butang pratonton di atas senarai.

### Jejari kimpalan {#weld-radius}
Di bawah tajuk `Gabung`, `Jejari Kimpalan Kedudukan` dan `Jejari Kimpalan UV`: titik dan UV yang lebih dekat daripada jejari ini akan digabungkan. Setiap satu boleh dimatikan dengan kotak semaknya. Ini terpakai pada Gabung, Boolean, Potong (Trim), Kurangkan, remesh dan import fail.

### Ikon-ikon {#icons}
Tetapkan `Saiz` minimum dan maksimum serta `Kelegapan` ikon grup, cahaya, kamera dan pengulang dalam ruang pandang.

### ![](/icons/hierarchy.webp) Garis Hierarki {#hierarchy-lines}
Paparkan garis antara induk dan anak-anaknya dalam ruang pandang. Apabila didayakan, anda juga boleh menetapkan:
* `Gunakan pivot Nomad` - garis bermula dari pangsi yang digunakan oleh alat Transformasi dan Gizmo. Apabila dinyahaktifkan, garis menggunakan pangsi asas semula jadi, yang mungkin jauh dari pusat objek.
* `Ketebalan` - lebar garis. Butang di sebelah peluncur menambah garis luar padanya.
* Warna garis.

### ![](/icons/link.webp) Segerak {#sync}
Tab `Segerak` menetapkan, bagi setiap operasi (`Tambah`, `Padam`, `Kunci`, `Klona`, `Instans`, `Batalkan instans`, `Gabung`, `Pisah` dan `Boolean`), sama ada ia digunakan pada setiap instans dalam pilihan:
* `Auto` - ikut kotak semak `Segerak` di bahagian atas menu adegan.
* `Tidak` - hanya objek yang dipilih.
* `Ya` - sentiasa setiap instans.

Secara lalai, `Gabung`, `Pisah` dan `Boolean` ditetapkan pada `Ya` dan yang lain pada `Auto`. `Tetapkan semula` memulihkan nilai lalai ini.

## Bar alat bawah {#bottom-toolbar}
Ikon-ikon ini menunjukkan atau menyembunyikan Grup, Cahaya, Kamera, Pengulang dan Garis Hierarki dalam ruang pandang. Ikon yang dipaparkan pada kanvas boleh diketuk untuk memilih dan menyuntingnya secara terus.
