# ![](/icons/scene.webp) Adegan {#scene}

Menu ini membolehkan anda mengurus objek, cahaya, kamera dan pengulang (repeater) dalam Nomad. Ia memaparkan hierarki adegan sebagai paparan pokok (tree-view), membolehkan anda mengubah banyak aspek objek anda. Ia juga membolehkan anda mencipta objek baharu, serta menggabung dan memisahkan objek dengan pelbagai cara.


![](/images/scene_menu_summary.webp)


## Bar pintasan {#shortcut-bar}
| Tindakan              | Ikon                              | Penerangan                                                                                                         |
| :--------------------: | :-------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| [Tambah...](#add-menu) | ![](/icons/plus.webp)            | Paparkan [Menu Tambah](#add-menu) untuk menambah objek ke dalam adegan                                             |
| Padam                  | ![](/icons/trash.webp)           | Padam objek                                                                                                        |
| Kunci                  | ![](/icons/lock.webp)            | Jadikan objek tidak boleh dipilih dalam viewport. Ia masih boleh dipilih dari paparan pokok.                      |
| Gabung                 | ![](/icons/merge.webp)           | Gabungkan objek terpilih menjadi satu objek tanpa perubahan geometri                                               |
| Pisah                  | ![](/icons/diagonal.webp)        | Jika objek terdiri daripada kulit poligon unik, pecahkan ia kepada objek berasingan. Songsang kepada operasi gabung |
| [Boolean...](#boolean) | ![](/icons/bool_subtract_circle.webp) | Paparkan menu [Boolean](#boolean)                                                                                  |
| Klon                   | ![](/icons/clone.webp)           | Gandakan objek menjadi objek baharu                                                                                |
| Instans                | ![](/icons/link.webp)            | Gandakan objek sebagai instans, supaya perubahan pemodelan pada satu akan digunakan pada semua instans            |
| Nyah-instans           | ![](/icons/unlink.webp)          | Tukar instans kepada bentuk unik, supaya perubahan pemodelan tidak lagi disalin ke instans lain                   |
| Segerak                | ![](/icons/link.webp)            | Jika instans mempunyai anak, pastikan semua instans berkongsi hierarki anak yang sama                             |


## Paparan pepohon {#tree-view}
![](/images/scene_treeview.webp) 

| Tindakan    | Ikon                       | Penerangan                |
| :----------: | :------------------------: | :------------------------: |
| Pilih        | ![](/icons/checked.webp)  | Togol pilih/tidak dipilih |
| Kelihatan    | ![](/icons/eye_open.webp) | Togol keterlihatan        |
| Menu         | ![](/icons/more.webp)     | Paparkan menu objek       |

::: tip TIP: Pilih atau sembunyi banyak objek dengan pantas

Ketuk ikon pilih untuk togol satu objek, atau seret secara menegak pada lajur pilih untuk memilih banyak objek. Perkara yang sama boleh dilakukan dengan lajur kelihatan.

:::

### Manipulasi paparan pepohon {#tree-view-manipulation}

Tekan lama pada item dalam paparan pokok sehingga ia bertukar kuning. Anda kemudian boleh menggerakkannya ke atas atau ke bawah dalam paparan pokok, serta menyeretnya ke atas item lain untuk menjadikannya anak kepada item tersebut.

Apabila banyak item dipilih, kebanyakannya akan berwarna kuning gelap, satu akan berwarna kuning lebih cerah. Tekan lama dan seret pada item yang lebih cerah untuk menggerakkan semua objek sekali gus.

Apabila anda memilih item induk, secara lalai semua item anak juga akan dipilih. Mengetuk ikon induk akan menogol antara memilih hanya induk, atau induk dan anak-anaknya.

### Menu objek {#object-menu}

Mengklik butang elipsis (...) untuk objek dalam paparan pokok akan memaparkan menu objek. 
Banyak pilihan di sini serupa dengan bar pintasan di bahagian atas, diulang untuk kemudahan.

|       Tindakan       |                        Ikon                        | Penerangan                                                                                                                                                             |
| :-------------------: | :------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       Instans         |               ![](/icons/link.webp)            | Gandakan objek sebagai instans, supaya perubahan pemodelan pada satu akan digunakan pada semua instans                                                                 |
|         Klon          |              ![](/icons/clone.webp)            | Gandakan objek menjadi objek baharu                                                                                                                                     |
|         Nama          |              ![](/icons/pencil.webp)           | Tukar nama objek                                                                                                                                                        |
|         Padam         |              ![](/icons/trash.webp)            | Padam objek                                                                                                                                                             |
|        Padam+         |            ![](/icons/removeNode.webp)         | Padam objek dan anak-anaknya                                                                                                                                            |
|     Nyah-instans      |              ![](/icons/unlink.webp)           | Tukar instans kepada bentuk unik, supaya perubahan pemodelan tidak lagi disalin ke instans lain                                                                         |
|  Pisah Topologi       |             ![](/icons/separate.webp)          | Jika objek terdiri daripada kulit poligon unik, pecahkan ia kepada objek berasingan. Songsang kepada operasi gabung.                                                   |
| Pisah Kumpulan Muka   |            ![](/icons/faceGroup.webp)          | Jika objek mempunyai beberapa kumpulan muka, pecahkan mesh kepada objek berasingan.                                                                                    |
|   Pisah Lapisan       |              ![](/icons/layer.webp)            | Jika objek mempunyai lapisan, pisahkan setiap lapisan menjadi objek berasingan. Berguna untuk menghantar blendshape ke aplikasi lain.                                 |
|   Gabung -> Lapisan   | ![](/icons/merge.webp) -> ![](/icons/layer.webp) <span style="visibility:hidden">_________</span> | Jika beberapa objek dipilih dan mempunyai topologi sepadan, gabungkan objek tersebut menjadi lapisan untuk objek utama (objek lain akan dipadam). Sekali lagi, berguna untuk blendshape yang datang DARI aplikasi lain.<br><br> Perhatikan bahawa lapisan akan dinyahaktifkan secara lalai. Aktifkan ia jika anda perlu melaras peluncurnya. |




### Pemilihan berbilang {#multiselection}
Anda boleh memilih beberapa objek untuk membantu mencapai dua perkara:
- menggunakan alat gizmo untuk menggerakkan beberapa objek sekali gus
- menggabung objek menggunakan operasi gabung dan boolean.

Anda boleh melakukannya dengan menggunakan kotak semak `Multiselection`, dan kemudian mengklik pada objek dalam senarai.

::: tip Pemilihan berbilang pantas
Anda juga boleh memilih berbilang dalam viewport dengan menahan pintasan `Smooth` dan mengetuk pada mesh lain.

Anda boleh nyahpilih objek dengan mengetuknya sekali lagi (hanya jika pilihan anda mempunyai lebih daripada satu objek).
:::

::: warning Ciri gizmo terhad
Apabila menggunakan pemilihan berbilang, alat gizmo akan sentiasa mengabaikan masking.
Selain itu, penskalaan X/Y/Z dibuang.

Sebabnya ialah pemilihan berbilang hanya membenarkan transformasi keseluruhan mesh, bukan transformasi per verteks.
Ini mungkin akan diperbaiki pada masa hadapan.
:::


## Cantum {#join}
Pilihan ini hanya akan menghasilkan satu entri objek tunggal daripada beberapa objek terpilih.

Anda boleh melihat contoh dalam video di bahagian [Pisah](#separate).

## Boolean {#boolean}
![](/images/scene_boolean_menu.webp) 
Gabungkan objek menjadi satu permukaan.

`Voxel merge` akan mengekalkan isipadu objek, dan mengira poligon baharu yang jaraknya sekata pada permukaan. Disebabkan langkah pengiraan, voxel merge boleh mengendalikan geometri kompleks, tetapi boleh kehilangan perincian halus jika resolusi sasaran tidak cukup tinggi.

`Boolean` akan cuba mengekalkan susun atur asal poligon, dan menjahit poligon di mana objek bertindih. Ini boleh menghasilkan keputusan yang jauh lebih bersih dan tajam berbanding voxel merge, namun ia memerlukan mesh 'kedap air'; tidak boleh ada lubang atau bentuk rosak dalam objek. Jika ini gagal, biasanya voxel merge akan berjaya.

### Operasi Boolean {#boolean-operations}
Voxel Merge dan Boolean kedua-duanya akan menggunakan keterlihatan objek untuk mengawal operasi:

#### Cantuman {#union}
Kedua-dua objek kelihatan akan menghasilkan boolean **union**, kulit luar objek digabungkan, tanpa permukaan dalaman. ![](/images/boolean_union.webp)

#### Tolak {#subtract}
Satu objek tidak kelihatan = boolean **subtract**, objek yang tidak kelihatan akan ditolak daripada objek yang kelihatan. ![](/images/boolean_subtract.webp)

#### Silang {#intersect}
Kedua-dua objek tidak kelihatan = boolean **intersection**, cipta bentuk baharu hanya di tempat dua objek bertindih. ![](/images/boolean_intersect.webp)


### Butang Cantum Voxel {#voxel-merge-button}
Menekan butang ini akan melakukan operasi voxel merge pada objek terpilih. Apabila dilakukan pada satu objek, ia akan melakukan retopologi kepada poligon yang jaraknya sekata, berguna apabila objek mempunyai poligon yang diregangkan.

### Resolusi {#resolution}
Resolusi grid 3D voxel yang digunakan untuk pengiraan. Apabila nilai ini diubah, corak papan dam akan ditindih pada objek untuk pratonton saiz poligon.

### Bina multiresolusi {#build-multiresolution}
Cipta aras multiresolution di bawah resolusi sasaran anda. Jadi jika resolusi anda 400 dan bina multiresolution ialah 3, anda akan mendapat mesh baharu dengan kira-kira 296,000 poligon, tetapi akan ada 3 aras subdiv lebih rendah pada 74,000, 18,000, 4,000k.

### Kekalkan tepi tajam {#keep-sharp-edges}
Aktifkan snapping mesh voxel kepada tepi. Ini berfungsi paling baik pada bentuk ringkas.

### Butang Boolean {#boolean-button}
Menekan butang ini akan melakukan operasi boolean poligon menggunakan pustaka Manifold oleh Emmett Lalish. 


## Asingkan {#separate}
Jika anda mempunyai satu objek yang berdasarkan beberapa bahagian yang tidak bersambung, anda boleh membahagikan objek ini kepada beberapa objek. 
Ini boleh dianggap sebagai lawan kepada [Simple Merging](#simple-merge).

![](/videos/merge_separate.mp4)


## Menu Tambah {#add-menu}

![](/images/scene_addmenu_overview.webp)

Menu ini akan mencipta primitif, kumpulan, kamera, pengulang dan cahaya.

Primitif ialah jenis bentuk asas yang boleh dilaras menggunakan parameter. Setelah anda melaras primitif mengikut keperluan, anda kemudian 'sahkan' ia, yang akan menukarkan parameter tersebut kepada mesh poligon yang boleh diukir dan dicat. Primitif tidak boleh dilaras parameternya selepas ia disahkan.


![](/images/scene_addmenu_top.webp)

### Pada gizmo {#on-gizmo}
Aktifkan meletakkan primitif baharu di tempat bentuk atau gizmo terpilih semasa. Apabila dinyahaktifkan, primitif akan diletakkan di tengah adegan.

### Pilih gizmo {#select-gizmo}
Aktifkan penukaran automatik kepada alat gizmo apabila primitif baharu dicipta. 

### Lanjutan {#add-advanced}

Menu ini membolehkan anda menetapkan keutamaan untuk lokasi primitif, kumpulan, pengulang baharu dicipta. Ia boleh berada pada objek terpilih, di asal dunia (world origin), atau pada lokasi gizmo.


### UV {#uvs}
Aktifkan UV pada primitif. UV (sering dipanggil koordinat tekstur), ialah data tambahan yang digunakan dalam 3D untuk membolehkan tekstur digunakan pada permukaan. Ia menggunakan lebih banyak memori, tetapi bagi kebanyakan peranti ini tidak sepatutnya menjadi isu kecuali anda mencapai kiraan poligon yang sangat tinggi (cth 10 juta poligon atau lebih). 

### Primitif {#primitives}

| Primitif      | Ikon                                      | Penerangan                                                                                                     |
| :------------: | :---------------------------------------: | :-------------------------------------------------------------------------------------------------------------: |
| Kotak          | ![](/icons/cube.webp)                    | Ia adalah kiub ringkas, anda boleh mengawal pembahagian dalam X, Y dan Z                                       |
| Sfera          | ![](/icons/circle.webp)                  | Untuk kemudahan ini dinamakan Sfera tetapi sebenarnya ialah kotak yang disubdiv, dengan `Project on sphere` dipaksa |
| Silinder       | ![](/icons/cylinder.webp)                | Anda boleh menambah lubang tengah untuk primitif silinder, contohnya untuk membuat paip berongga               |
| Torus          | ![](/icons/torus.webp)                   | Torus boleh menjadi titik mula yang baik untuk cincin                                                           |
| Kon            | ![](/icons/cone.webp)                    | -                                                                                                               |
| Ikosahedron    | ![](/icons/icosahedron.webp)             | -                                                                                                               |
| UV-sfera       | ![](/icons/circle.webp)                  | Sfera dengan susun atur poli tidak sekata, lihat [Amaran di bawah](#uv-sphere)                                 |
| Satah          | ![](/icons/rectangle.webp)               | Ia adalah satah ringkas, perhatikan bahawa ini satu-satunya primitif yang tidak tertutup                       |
| Tiub           | ![](/icons/tool_tube.webp)               | lihat [Tube](tools#tube)                                                                                        |
| Larik          | ![](/icons/tool_lathe.webp)              | lihat [Lathe](tools#lathe)                                                                                      |
| Triplanar      | ![](/icons/triplanar.webp)               | lihat [Triplanar](#triplanar)                                                                                   |
| Penangkap Bayang | ![](/icons/material_shadow_catcher.webp) | lihat [Shadow Catcher](#shadow-catcher)                                                                        |
| Kepala         | ![](/icons/face.webp)                    | Kepala ringkas dengan lapisan untuk mengadun antara lelaki/perempuan                                            |

::: tip
Jika anda tertanya-tanya apakah mesh asas apabila anda melancarkan Nomad: ini juga ialah kotak yang disubdiv.
Namun mesh asas dalam Nomad tidak menggunakan `Project on sphere`, bermakna ia tidak bulat sempurna.
:::

### Bar Alat Primitif {#primitive-toolbar}

![](/images/scene_primitive_toolbar.gif)

Sebaik sahaja primitif dicipta, bar alat akan muncul untuk mengawal parameternya.

* `Validate` Tukar primitif kepada objek piawai supaya ia boleh diukir dan dicat.
* `Edit` Togol paparan gizmo primitif. Ini ditunjukkan terus pada primitif untuk mengawal parameternya, cth lebar kiub, atau jejari lubang silinder.
* `Mirror` Togol meletakkan pengulang cermin di atas primitif.
* `...` Paparkan menu primitif.

Primitif berbeza akan mempunyai pilihan tambahan pada bar alat:

* `Project` Sfera dibina sebagai kiub yang disubdiv, kerana ini lebih baik untuk mengukir, tetapi ini bermakna ia tidak bulat sempurna. Pilihan ini akan memaksa bentuk lebih hampir kepada sfera sempurna. Ikosahedron berkongsi pilihan ini.
* `Cap` Togol penutup hujung pada bentuk, cth silinder boleh mempunyai penutup di atas, atau bawah, atau kedua-duanya, atau tiada.
* `Hole` Togol lubang yang dicipta melalui tengah bentuk. Ini akan berputar antara tiada lubang, lubang dengan satu jejari, atau lubang dengan jejari berbeza di atas dan bawah.
* `Radius` Togol sama ada silinder patut mempunyai satu jejari, atau jejari berbeza di atas dan bawah.
* `Disk` Togol sama ada satah patut menjadi bentuk 4 sisi, atau bentuk bulatan.

Bar alat kecil di bawah bar alat utama akan membolehkan anda menogol antara gizmo primitif dan gizmo transform.

::: tip

Mengklik pada tajuk bar alat akan menogolnya ke bahagian atas atau bawah paparan. Mengklik pada anak panah di penjuru akan meruntunkannya.

:::


### Menu primitif {#primitive-menu}

![](/images/scene_primitive_menu.webp)

Ini mengandungi semua parameter untuk primitif terpilih. Parameter ialah penerangan asas untuk bentuk. Untuk menerangkan cincin, sebagai contoh, anda akan menerangkan jejari luar, jejari dalam, dan bilangan poligon.

Kebanyakan parameter primitif sepatutnya jelas, dan terdapat beberapa parameter umum yang dikongsi merentasi semua primitif:

* `UVs` Butang UV kecil di bahagian atas menu akan menogol penciptaan koordinat UV
* `Validate` Butang validate kecil akan menukar primitif kepada objek piawai supaya ia boleh diukir dan dicat.
* `Max faces` Tetapkan had atas jumlah poligon dalam objek untuk mengelakkan peranti anda terhenti.
* `Post subdivision` Aktifkan bilangan subdiv yang dipilih daripada bahagian multiresolution dalam menu topologi. Ini boleh digunakan untuk membuat primitif sudut lembut dan licin bersama pembahagian topologi rendah. Sebagai contoh, tetapkan pembahagian topologi kotak kepada 2, dan post subdivision kepada 4, akan menghasilkan kotak dengan sudut licin.
* `Linear subdivision` Tetapkan berapa banyak aras subdiv linear yang digunakan sebelum menggunakan subdiv licin biasa. Ini boleh digunakan untuk mengawal betapa tajam atau lembut sudut pada permukaan yang disubdiv. Cth, tetapkan pembahagian topologi kotak kepada 2, post subdivision kepada 4, kemudian cuba ubah subdiv linear antara 0 dan 4. Sudut kotak akan berubah daripada lembut kepada tajam.

### Topologi {#topology}

Ini mengawal bilangan poligon dalam primitif. Biasanya kawalan dipautkan, jadi mengubah satu peluncur aktif akan melaras semua poligon secara sekata. Anda boleh mengetuk butang nyahpaut, dan mengawal pembahagian X/Y/Z pada bentuk secara berasingan.

### Geometri {#geometry}

Ini mengawal saiz keseluruhan primitif, dalam unit X/Y/Z untuk bentuk segi empat, dan dalam jejari untuk bentuk bulat.


### Sfera UV {#uv-sphere}
::: warning
UV Sphere tidak begitu sesuai untuk mengukir, terutamanya pada kutub.

Sila utamakan primitif [Sphere](#sphere), [Box](#box) atau [Icosahedron](#icosahedron), bersama pilihan `Project on sphere`.

Perhatikan bahawa topologi boleh diterima untuk mengukir jika anda menggunakan nilai yang sangat rendah untuk peluncur `Division`.
Anda kemudian boleh menggunakan peluncur `Overall Subdivision` untuk menaikkan bilangan poligon.

Walaupun tidak sesuai untuk pengukiran umum, ia berguna untuk mata; jika anda memutar sfera supaya kutub berada di anak mata, susun atur poligon akan secara semula jadi sesuai untuk melukis dan mengukir iris dan anak mata.
:::


### Triplanar {#triplanar}
Primitif ini istimewa kerana anda sepatutnya menggunakan [alat Masking](tools.md#mask) padanya untuk membentuk geometri.

![](/videos/triplanar.mp4)


::: tip
Dwi-ketuk pada satah dan kamera akan memfokus pada satah tertentu itu.
Ini tidak akan berfungsi jika anda memutar primitif dengan gizmo.
:::

Triplanar menggunakan maklumat mask daripada 3 satah untuk mengisi grid voxel yang kemudian dipoligonkan (terima kasih kepada [Voxel Remesher](topology.md#voxel-remeshere)).

Setiap satah mempunyai satah simetrinya sendiri.

::: warning
Setiap kali anda mengemas kini saiz primitif Triplanar, kualiti lukisan mask akan merosot.

Buat masa ini tiada pilihan untuk 'mengunci' lukisan pada satu satah, tetapi mungkin akan datang pada masa hadapan.
Anda boleh menggunakan [Connected Topology](stroke.md#connected-topology) untuk membantu sedikit, di mana jika kursor anda berada tepat pada satu satah ia tidak akan menjejaskan satah lain.
:::

### Penangkap Bayang {#shadow-catcher}
Tambah satah dengan material shadow catcher. Lihat [material Shadow Catcher](material.md#shadow-catcher) untuk maklumat lanjut. 


## Kumpulan/Kamera {#groupcamera}
### Kumpulan {#group}
Cipta objek 'kosong', yang boleh anda jadikan induk kepada objek lain di bawahnya. Ini boleh digunakan untuk sekadar mengatur hierarki dengan meletakkan banyak objek di bawah kumpulan, kemudian menutupnya. Kumpulan juga boleh digunakan sebagai pembantu untuk menggerakkan objek; banyak objek boleh diletakkan di bawah kumpulan, dan kemudian kumpulan digerak, diputar, diskala dengan alat gizmo.

### Tambah pandangan {#add-view}
Cipta kamera.

## Pengulang {#repeaters}
![](/images/scene_primitive_repeaters.webp)

Pengulang ialah nod yang menghasilkan instans objek di bawahnya. 

### Tatasusunan {#array}
![](/images/scene_primitive_array.webp)

Apabila objek dijadikan anak kepada nod ini, ia boleh diinstans dalam susun atur grid. Apabila dipilih, ia mempunyai kawalan untuk:
* Fit inside - togol antara mengawal saiz grid/kotak array, atau mengawal jarak antara instans array
* CountX/Y/Z - bilangan instans pada setiap paksi
* OffsetX/Y/Z - jarak antara instans apabila fit inside ditogol
* SizeX/Y/Z - lebar/tinggi/dalam grid array keseluruhan apabila fit inside ditogol.

### Lengkung {#curve}
![](/images/scene_primitive_curve.webp)
Ini akan mencipta lengkung, anak kepada nod ini akan diulang sepanjang lengkung. Apabila dipilih, ia mempunyai kawalan untuk:
* Edit - benarkan penambahan titik pada lengkung, dan menggerakkan titik pada lengkung.
* Snap - akan snap titik lengkung kepada geometri lain
* Align - akan memutar bentuk anak untuk sejajar dengan arah lengkung
* Count - bilangan instans
* Closed - Togol lengkung untuk menyambung permulaan dan penghujung, atau menjadi lengkung terbuka
* Radius - Togol kawalan pada setiap titik lengkung untuk mengawal skala instans
* Twist - Togol kawalan pada setiap titik lengkung untuk mengawal putaran twist instans 
* B-spline - Togol instans untuk mengikut lengkung tepat, atau menggunakan interpolasi b-spline yang menghasilkan keputusan lebih licin. 

### Jejari {#radial}
![](/images/scene_primitive_radial.webp)

Anak kepada nod ini akan diinstans menjadi bulatan. Gerakkan objek anak untuk mengubah jejari pengulang ini. Apabila dipilih, ia mempunyai kawalan untuk:
* RadialX/Y/Z - memilih butang ini akan menetapkan paksi radial, dan menetapkan bilangan instans.



### Cermin {#mirror}
![](/images/scene_primitive_mirror.webp)

Anak kepada nod ini akan dicerminkan merentasi paksi. Apabila dipilih ia mempunyai kawalan untuk:
* Gizmo - aktifkan gizmo transform untuk menetapkan pusat cermin. Ini juga boleh diputar dan diskala. Apabila selesai, ketuk gizmo sekali lagi untuk memaparkan kawalan piawai.
* X/Y/Z - tetapkan satah cermin

Semua pengulang mempunyai kawalan `Validate`, yang akan menukar hasil pengulang, dan akan bertanya bagaimana untuk melakukan penukaran:
* Join children - instans digabungkan menjadi satu objek
* Keep instances - instans kekal sebagai instans, tetapi tidak lagi mempunyai 'induk' pengulang
* Un-instances - instans ditukar menjadi objek unik

::: tip Tip: Gabung pengulang
Pengulang boleh dijadikan anak antara satu sama lain, dan beberapa objek boleh dijadikan anak kepada pengulang, menghasilkan kesan kompleks.

![](/images/scene_repeater_combine.webp)
:::

::: tip Tip: Pivot pengulang

Sesetengah pengulang akan cuba auto-pivot objek anak, jadi walaupun anda menggerak atau memutarnya dengan alat gizmo, ia tidak akan bergerak. Jika anda perlu mengatasi tingkah laku ini, selitkan kumpulan di antara pengulang dan anak. Kini anda boleh menggerakkan bentuk anak secara bebas daripada pengulang.
:::

## Cahaya {#light}

![](/images/scene_primitive_light.webp)

### Berarah {#directional}
Cipta cahaya arah, sumber cahaya yang sangat jauh seperti matahari.

### Sorot {#spot}
Cipta cahaya spot, dengan kawalan ke atas lebar kon, kelembutan

### Titik {#point}
Cipta cahaya titik

## Lanjutan {#advanced}
### Fokus pada item {#focus-on-item}
Dwi-klik item dalam senarai Adegan akan memusatkan kamera pada item tersebut dalam paparan 3D.

### Segerak keterlihatan {#sync-visibility}
Menggunakan ikon mata akan memberi kesan kepada semua item terpilih. 

### Instans: Tunjuk {#instance-show}
Paparkan kapsul warna di sebelah kiri senarai adegan untuk menunjukkan instans.


### Ikon {#icons}
Tetapkan saiz dan kelegapan ikon kumpulan, cahaya, kamera, cermin dalam viewport

### Garis hierarki {#hierarchy-lines}
Paparkan garis antara induk dan anak-anaknya dalam viewport

## Bar alat bawah {#bottom-toolbar}
Ikon ini akan menogol keterlihatan Kumpulan, Cahaya, Kamera, Pengulang dan garis Hierarki dalam viewport.