# ![](/icons/toolbox.webp) Alat {#tools}

![](/images/tools_menu.webp)

::: tip
Lompat ke bahagian [Alat](#tools-1) untuk penerangan setiap alat.
:::

## Gambaran Keseluruhan {#overview}

Alat dipilih daripada `Kotak alat` di sebelah kanan, dan dikawal dengan `Kawalan Alat` di sebelah kiri. Tetapan tambahan terdapat dalam menu `Alat`, di menu atas sebelah kanan.

Alat berus mempunyai kawalan untuk saiz dan intensiti. Alat pemilihan mempunyai kawalan untuk beberapa gaya pemilihan. Bahagian bawah kawalan alat mempunyai pintasan untuk operasi yang kerap digunakan (Lancar, Topeng, Sembunyi, Kumpulan muka, Gizmo, Warna, Alpha).

Alat Nomad diberi kod warna dalam kotak alat (matikan `Alat berwarna` dalam menu [Antara Muka](interface.md) untuk label biasa):

* <span class=brush>**Alat berus**</span> (Tanah liat, Berus, Lancar, Lapisan, Kembang, PadamLapisan, Quad Remesher)
* <span class=move>**Alat gerak**</span> (Alih, Seret, Elastik, Geser)
* <span class=mask>**Alat topeng**</span> (Topeng)
* <span class=paint>**Alat lukisan**</span> (Lukis, Smudge)
* <span class=flatten>**Alat perata**</span> (Leperkan, Planar, Gilap)
* <span class=pinch>**Alat cipit**</span> (Alur tajam, Cipit)
* <span class=stamp>**Alat cap**</span> (Cap, VDM)
* <span class=selection>**Alat berasaskan pemilihan**</span>, di mana topeng 2d dilukis dahulu, kemudian satu operasi berlaku (Potong, Pisahkan, Unjur)
* <span class=creation>**Alat penciptaan**</span> (Tiub, Larik, Masukkan)
* <span class=transform>**Alat transformasi**</span> (Transformasi, Gizmo, Susun, Lattice)
* <span class=misc>**Alat pelbagai**</span> (Kumpulan muka, Sembunyi)
* <span class=view>**Alat paparan**</span> (Lihat, Ukur, Pilih)



Kebanyakan alat ini boleh disesuaikan dengan tingkah laku berus, tekanan, tekstur dan lain-lain yang berbeza melalui menu [Sapuan](stroke.md). 


### Kawalan berus {#brush-controls}

Bar alat kiri mempunyai gelangsar untuk jejari dan intensiti, diikuti kawalan khusus mengikut kategori alat, yang diterangkan di bawah.

![](/images/tool_left_panel.webp)

::: tip
Gelangsar intensiti bagi banyak alat boleh melebihi 100%, berbaloi untuk dicuba!
:::

### Mod sub {#sub-mode}
Butang betul-betul di bawah gelangsar intensiti ialah butang `Tolak`. Label dan fungsinya berubah mengikut setiap alat, dan apabila ditekan ia menggunakan tingkah laku alternatif, biasanya yang bertentangan. Contohnya bagi [Lukis](#paint) ia menggunakan mod Padam, bagi [Alur tajam](#crease) ia mencipta tepi yang menonjol dan bukannya alur, dan sebagainya.

Secara lalai ia berfungsi sebagai butang melekit: anda boleh menahannya untuk menggunakannya buat sementara, dan apabila dilepaskan ia akan dimatikan. Jika anda mengetiknya, mod sub akan diaktifkan secara kekal.

### Pintasan {#shortcuts}
Di bahagian bawah bar alat kiri terdapat pintasan untuk [Lancar](#smooth), [Topeng](#mask), [Sembunyi](#hide), [Kumpulan muka](#facegroup), [Gizmo](#gizmo), [Warna](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Secara lalai semuanya berfungsi sebagai butang melekit: anda boleh menahannya untuk menggunakannya buat sementara, dan apabila dilepaskan ia akan dimatikan. Jika anda mengetiknya, mod pintasan itu akan diaktifkan secara kekal.

### Kawalan pemilihan {#selection-controls}

Alat [Topeng](#mask), [Lukis](#paint), [Potong](#trim), [Pisahkan](#split), [Unjur](#project), [Kumpulan muka](#facegroup), [Sembunyi](#hide) dan [Pilih](#select) semuanya menggunakan kawalan yang serupa untuk memilih kawasan mesh.

![](/images/tools_shape_selector_panel.webp)

Ketik butang bentuk dalam bar alat kiri (ia memaparkan bentuk semasa, `Laso` secara lalai) untuk membuka tetingkap timbul yang mengandungi bentuk-bentuk. Bagi alat yang juga berfungsi dengan berus (Topeng, Lukis, Kumpulan muka, Sembunyi), tetingkap timbul yang sama turut memuatkan jenis sapuan.

* `Lihat` - Tiada bentuk, alat tidak melakukan apa-apa yang khusus, seperti mod kamera.
* `Laso` - Bentuk yang dilukis bebas
* `Poligon` - Bentuk tertutup yang ditentukan oleh gabungan lengkung dan/atau garis lurus. Lihat [Penyuntingan bentuk](#shape-editing) di bawah untuk maklumat lanjut.
* `Lengkung` - (Unjur sahaja) - Lengkung bebas untuk unjuran
* `Laluan` - (Unjur sahaja) - Lengkung yang ditentukan oleh titik-titik. Lihat [Penyuntingan bentuk](#shape-editing) di bawah untuk maklumat lanjut.
* `Garis` - Seret satu garis untuk menentukan segmen satah. Secara lalai ia terus bertindak pada mesh; tukar pilihan `Sunting` jika anda tidak mahu begitu (tekan lama atau leret pada ikon garis)
* `Jalur` - Jalur di antara dua panduan selari, dengan kecerunan merentasinya. `Lanjutkan` mengekalkan nilai penuh melepasi panduan yang jauh dan bukannya berhenti pada jalur, `Balikkan` menukar panduan tempat kecerunan bermula.
* `Rekt` - Seret satu garis pepenjuru untuk menentukan penjuru bentuk segi empat. Tekan lama atau leret untuk memaparkan pilihan `Sunting`, `Segi empat sama` untuk memaksa bentuk segi empat sama, dan `Berpusat` supaya klik pertama menjadi tengah segi empat.
* `Elips` - Seret satu garis pepenjuru untuk menentukan saiz elips. Tekan lama atau leret untuk memaparkan pilihan `Sunting`, `Bulat` untuk memaksa bentuk bulatan, dan `Berpusat` supaya klik pertama menjadi tengah elips.
* `Balik` - songsangkan topeng bentuk, atau arah alat unjur.

Kebanyakan alat mempunyai pilihan `Sunting` yang menentukan apa yang berlaku apabila anda selesai melukis bentuk:
* `Sunting: mati` - operasi berlaku sebaik sahaja anda melepaskan.
* `Sunting: hidup` - bentuk kekal boleh disunting. Satu butang hijau dilukis di sebelah bentuk itu untuk melaksanakan operasi. Ini membolehkan anda menyunting bentuk dan melaraskan pandangan; apabila anda bersedia untuk menggunakan bentuk itu, tekan butang hijau.
* `Sunting: tahan` - operasi berlaku apabila dilepaskan, melainkan anda menahan di hujung sapuan untuk terus menyunting bentuk.

### Penyuntingan bentuk {#shape-editing}
Penyuntingan poligon dan penyuntingan lengkung berfungsi dengan cara yang serupa:

* Untuk bermula, seret satu garis untuk menentukan 2 titik, kemudian seret keluar dari tengah garis untuk menentukan poligon atau lengkung.
* Klik pada titik untuk menukar antara licin dan tajam. 
* Klik dan seret pada bahagian lengkung atau garis untuk mencipta titik baharu.
* Untuk memadam satu titik, seret titik itu ke titik jirannya sehingga ia bertukar merah.
* Ikon tong sampah di penjuru ikon poligon atau laluan akan memadam bentuk itu.

### Menu tetapan {#settings-menu}

Banyak alat mempunyai tetapan tambahan dalam menu `Alat`, di menu atas sebelah kanan. Menu ini menjadi kelabu bagi alat yang tiada tetapan tambahan.

![](/images/tools_settings_menu.webp)

## Alat {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)    <br> [Tanah liat](#clay)       | ![](/icons/tool_brush.webp)   <br> [Berus](#brush)     | ![](/icons/tool_move.webp)       <br> [Alih](#move)              | ![](/icons/tool_drag.webp)      <br> [Seret](#drag)           | ![](/icons/tool_elastic.webp)   <br> [Elastik](#elastic)     | ![](/icons/tool_smooth.webp)  <br> [Lancar](#smooth)   |
| ![](/icons/tool_mask.webp)    <br> [Topeng](#mask)       | ![](/icons/tool_paint.webp)   <br> [Lukis](#paint)     | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp)   <br> [Leperkan](#flatten)     | ![](/icons/tool_planar.webp)    <br> [Planar](#planar)       | ![](/icons/tool_polish.webp)  <br> [Gilap](#polish)   |
| ![](/icons/tool_crease.webp)  <br> [Alur tajam](#crease)   | ![](/icons/tool_pinch.webp)   <br> [Cipit](#pinch)     | ![](/icons/tool_trim.webp)       <br> [Potong](#trim)              | ![](/icons/tool_split.webp)     <br> [Pisahkan](#split)         | ![](/icons/tool_project.webp)   <br> [Unjur](#project)     | ![](/icons/tool_layer.webp)   <br> [Lapisan](#layer)     |
| ![](/icons/tool_inflate.webp) <br> [Kembang](#inflate) | ![](/icons/tool_nudge.webp)   <br> [Geser](#nudge)     | ![](/icons/tool_stamp.webp)      <br> [Cap](#stamp)            | [VDM](#vdm)                                                  | ![](/icons/tool_clearLayer.webp) <br> [PadamLapisan](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tiub](#tube)       |
| ![](/icons/tool_lathe.webp)   <br> [Larik](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Masukkan](#insert)   | ![](/icons/tool_transform.webp)  <br> [Transformasi](#transform)    | ![](/icons/tool_gizmo.webp)     <br> [Gizmo](#gizmo)         | ![](/icons/tool_faceGroup.webp) <br> [Kumpulan muka](#facegroup) | ![](/icons/tool_hide.webp)    <br> [Sembunyi](#hide)       |
| ![](/icons/tool_measure.webp) <br> [Ukur](#measure) | [Susun](#arrange)                                      | ![](/icons/tool_remesh.webp)     <br> [Quad Remesher](#quad-remesher) | ![](/icons/tool_select.webp)    <br> [Pilih](#select)       | ![](/icons/tool_lattice.webp)   <br> [Lattice](#lattice)     | ![](/icons/tool_view.webp)    <br> [Lihat](#view)       |

------

### ![](/icons/tool_clay.webp) Tanah liat {#clay}
Alat Tanah liat berguna untuk membina arca anda. `Tolak` akan membuang bahan daripada arca anda.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Berus {#brush}
Berus standard. `Tolak` akan membuang bahan.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Alih {#move}
Kawasan di bawah berus akan melekat pada berus, membolehkan ubah bentuk yang elastik. Pemilihan dikekalkan sepanjang pergerakan, jadi jika anda menggerakkan berus menjauh, kemudian membawanya kembali ke tempat permulaan, anda tidak akan nampak sebarang ubah bentuk.

Mod sub ialah `Normal`, dan ia menggerakkan kawasan di bawah berus mengikut normal permukaan.

Berus ini sesuai untuk ubah bentuk berskala besar dan juga ubah bentuk kecil yang teliti.

#### Tetapan Alih {#move-settings}

* `Jejari (Latar belakang)` - Sejauh mana anda boleh berada dari tepi model dan masih boleh mengukir, berguna apabila mengusahakan siluet objek. Nyahtandakannya supaya hanya mencengkam apabila anda bermula pada model.
* `Hanya verteks sebelah sama` - Abaikan verteks yang menghala ke arah bertentangan dengan ubah bentuk.
* `Arah` - Digunakan oleh mod sub `Normal`, ia menentukan sama ada seretan menolak atau menarik permukaan:
    * `Auto` - Memilih salah satu daripada dua kaedah di bawah untuk anda, berdasarkan sudut normal permukaan.
    * `Normal 3D` - Membandingkan kedudukan penuding pada skrin dengan normal permukaan seperti yang dilihat dari kamera.
    * `XY` - Menggunakan kedudukan penuding pada skrin (atas/bawah, kiri/kanan) untuk menentukan tolak atau tarik.
    * `Ambang` - Dengan `Auto`, had sudut yang menentukan kaedah mana yang digunakan.
* `Kelajuan putaran` - Anda boleh memulas kawasan yang dicengkam sambil menggerakkannya: putar dua jari, putar batang stilus anda, atau tahan kekunci pengubah suai (Alt, Ctrl, Shift atau Cmd) sambil menyeret dengan tetikus. Terdapat satu gelangsar masing-masing untuk jari, stilus dan tetikus; nyahtandakan salah satu untuk mematikan input itu.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Seret {#drag}
Kawasan di bawah berus akan melekat pada berus, membolehkan ubah bentuk yang elastik. Tidak seperti berus Alih, pemilihan sentiasa dikemas kini sepanjang sapuan, jadi anda boleh membuat objek yang lebih panjang seperti ular, terutamanya apabila Topologi dinamik diaktifkan.

Mod sub ialah `Normal`, dan ia menggerakkan kawasan di bawah berus mengikut normal permukaan.

Berus ini sesuai untuk perubahan bentuk yang lebih bebas dan ekspresif.

#### Tetapan Seret {#drag-settings}

Seret mempunyai tetapan yang sama seperti [Alih](#move-settings): `Jejari (Latar belakang)`, `Hanya verteks sebelah sama`, `Arah` dan `Kelajuan putaran`.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_elastic.webp) Elastik {#elastic}
Cengkam dan tarik permukaan seperti [Alih](#move), tetapi dengan ubah bentuk elastik: daripada berhenti di tepi berus, tarikan itu pudar secara lancar mengikut jarak merentasi objek, sedikit seperti meregangkan getah. Jejari berus menetapkan keluasan tarikan.

Mod sub ialah `Normal`, dan ia menggerakkan kawasan di bawah berus mengikut normal permukaan.

Berus ini sesuai untuk perubahan perkadaran yang besar dan lembut, yang kekal licin.

#### Tetapan Elastik {#elastic-settings}

Elastik mempunyai tetapan yang sama seperti [Alih](#move-settings), kecuali `Hanya verteks sebelah sama`. `Jejari (Latar belakang)` dimatikan secara lalai.

### ![](/icons/tool_smooth.webp) Lancar {#smooth}
Melicinkan kawasan dengan mempuratakan kedudukan titik. Alat ini sangat bergantung pada ketumpatan poligon.
Jadi jika anda mempunyai banyak poligon, pelicinan akan kurang berkesan.

Mod sub ialah `Santai`, yang hanya melicinkan rangka dawai tetapi cuba mengekalkan perincian geometri.

#### Tetapan Lancar {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Kumpulan muka {#smooth-facegroup}

* `Santai` - Melicinkan sempadan kumpulan muka. Gunakan intensiti melebihi 100% untuk melicinkan sempadan dengan cepat. `Auto` hanya melicinkan jika pratonton kumpulan muka diaktifkan, `Tidak` mematikannya, `Ya` mengaktifkannya. 

##### Verteks {#vertex}
* `Kekalkan isipadu` - Melicinkan tanpa mengecutkan permukaan, jadi pelicinan berulang tidak mengempiskan bentuk anda. Butang gear di sebelahnya memuatkan nilai `Mengecilkan` dan `Kembang` yang digunakan untuk ini.
* `Kekalkan sempadan` - Bagi mesh dengan tepi terbuka, contohnya satah, penjurunya boleh terlicin. Mengaktifkan pilihan ini akan memastikan verteks pada sempadan mesh tidak bergerak.
* `Melicinkan stabil` - Cuba menjadikan pelicinan tidak bergantung pada topologi. Ini berfungsi paling baik dengan ketumpatan topologi yang berbeza-beza dan nilai intensiti pelicinan yang tinggi.
* `Santai` - sama seperti mod alternatif santai dalam bar alat sebelah kiri.

##### Pewarnaan {#painting}
* `Pelarasan layar` - Gunakan pilihan ini untuk mendapatkan pelicinan yang tidak bergantung pada topologi, walaupun pada bilangan poligon yang tinggi. `Auto`, `Tidak` atau `Ya`.
* `Sampel layar` - Kualiti pelicinan; nombor yang lebih tinggi lebih licin, tetapi lebih perlahan.

::: tip
Ketumpatan poligon yang lebih tinggi mungkin memerlukan intensiti melebihi 100%. Nilai yang sangat tinggi (300%, 500%) juga boleh berfungsi dengan baik sebagai alat mengukir, memaksa kawasan di bawah berus menjadi rata dan licin dengan cepat, seperti mengetuk tanah liat dengan tukul kayu!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Topeng {#mask}
Alat ini membolehkan anda menopeng verteks. Verteks yang ditopeng dilindungi daripada diukir atau diwarnakan. 

Mod sub ialah `Buka Masker`, dan ia memadam kawasan yang telah ditopeng.

Seperti pemilihan dalam aplikasi lukisan 2d, topeng boleh dilukis dengan berus, atau dibuat dengan pemilihan bentuk (`Laso`, `Rekt`, `Jalur`...), dikaburkan atau ditajamkan. Pilih berus atau bentuk dalam tetingkap timbul sapuan pada bar alat kiri, lihat [Kawalan pemilihan](#selection-controls).

Tidak seperti aplikasi lukisan 2d, topeng juga boleh dibuat melalui kumpulan muka, dan topeng boleh digunakan untuk mencipta geometri baharu melalui operasi gaya penyemperitan/pengekstrakan. 

![](/videos/tool_mask1.mp4)

 Satu bar alat akan muncul di bahagian atas port pandangan dengan kawalan tambahan. 

![](/images/tool_mask_toolbar.webp)

Tajuk bar boleh diketik untuk mengembangkan/meruntuhkannya, atau anak panah di bahagian atas kanan boleh diketik untuk memindahkannya ke bahagian atas atau bawah antara muka.

| Tindakan                                             | Penerangan                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Kosongkan semua          | Kosongkan topeng pada setiap objek. Apabila objek lain turut ditopeng, butang `Bersihkan` tambahan hanya mengosongkan objek yang dipilih |
| ![](/icons/invert.webp)        Tukar             | Songsangkan topeng                                                                            |
| ![](/icons/sharpen.webp)       Tajamkan            | Tajamkan tepi topeng                                                                      |
| ![](/icons/blur.webp)          Kabur               | Kaburkan tepi topeng                                                                         |
| ![](/icons/outline.webp)       Sempadan             | Topeng sempadan terbuka mesh, seperti tepi satah atau bibir lubang          |
| ![](/icons/blur.webp)          Kabur ->            | Seret ke kanan untuk mengaburkan topeng, ke kiri untuk menajamkannya                                            |
| ![](/icons/circle_plus.webp)   Besarkan ->            | Seret ke kanan untuk membesarkan kawasan bertopeng, ke kiri untuk mengecilkannya                                      |
| ![](/icons/intensity.webp)     Kuatkan ->           | Seret ke kanan untuk menguatkan topeng, ke kiri untuk mencairkannya, tanpa mengubah bentuknya           |
| ![](/icons/dig.webp)           Rongga ->          | Bina semula topeng daripada kelengkungan permukaan: seret ke kanan supaya hanya rongga yang kekal boleh diwarnakan, ke kiri supaya hanya bonjolan |
| ![](/icons/culling.webp)       Depan              | Togol untuk hanya menopeng verteks yang menghadap ke depan                                                  |
| ![](/icons/eye_open.webp)      Kelihatan            | Dengan bentuk, togol untuk mengabaikan verteks yang tersembunyi di belakang permukaan lain                        |
|                                 Tukarkan            | Tukarkan topeng kepada kumpulan muka                                                            |
| ![](/icons/group_to_mask.webp) Ketuk (kumpulan muka) | Apabila diaktifkan, kumpulan muka akan dipaparkan, dan mengetik satu kumpulan muka akan menopengnya                    |
|                                 Ketuk (topeng)      | Apabila diaktifkan, mengetik satu 'pulau' poligon bertopeng atau tidak bertopeng akan mengisi penuh pulau itu. |
| ![](/icons/connect.webp)       Bersambung          | Apabila diaktifkan, sapuan topeng hanya menjejaskan topologi yang bersambung.                         |

##### Gerak isyarat pantas Topeng {#mask-quick-gesture}
Anda boleh melakukan gerak isyarat gaya ZBrush sambil menahan butang topeng pantas dalam bar alat kiri:
| Tindakan  | Gerak isyarat (tahan pintasan kiri bawah) |
| :-----: | :--------------------------------: |
| Tukar  | Ketik pada latar belakang              |
| Bersihkan   | Seret pada latar belakang             |
| Kabur    | Ketik pada kawasan bertopeng                 |
| Tajamkan | Ketik pada kawasan tidak bertopeng               |


#### Tetapan Topeng {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

Tetapan Topeng terutamanya digunakan untuk mencipta geometri daripada topeng. Tab di bahagian atas memilih operasi: [Ekstrak](#extract), [Pisah](#split-mask) atau [Ukir](#carve). Pilihan di bawahnya berubah mengikut operasi.

* `Pratonton` - Paparkan rupa geometri baharu semasa anda melaraskan tetapan.
* `X-Ray` - Objek mana yang dilukis dalam x-ray semasa pratonton: `Tiada`, `Tidak terpilih`, `Terpilih` atau `Semua`.

##### Ekstrak {#extract}
* `Ekstrak` - Cipta geometri yang diekstrak sebagai objek baharu.
* `Tindakan Penutupan` - Cara bentuk yang diekstrak ditutup. `Tiada` akan menduplikasi poligon bertopeng menjadi bentuk baharu dan membiarkannya terbuka. `Isi` melakukan perkara yang sama, serta mengisi dan melicinkan lubang di belakang (jangan gunakannya pada permukaan rata). `Cangkerang` menutup bentuk menggunakan nilai `Ketinggian`, dan merupakan pilihan lalai.

::: tip

Jika pratonton diaktifkan bersama x-ray, mengklik butang Ekstrak boleh mengelirukan pada mulanya. Oleh kerana menu masih aktif, ia akan cuba mempratonton pengekstrakan pada bentuk baharu anda, dan memaparkan permukaan asal dalam x-ray. Namun kerana tiada topeng pada permukaan baharu, ia tidak dapat mempratonton pengekstrakan, dan Nomad akan memberi amaran 'Tiada apa untuk diekstrak!'. 

Ini perkara biasa. Tutup menu tetapan topeng untuk melihat bentuk baharu dan yang asal, dan pilih semula permukaan asal jika anda perlu mengosongkan topeng atau melukis topeng baharu.
:::

##### Pisah {#split-mask}
* `Pisah` - Mengekstrak kedua-dua kawasan bertopeng DAN tidak bertopeng menjadi bentuk baharu. 
* `Tindakan Penutupan` (bertopeng) - Cara bahagian bertopeng ditutup, dengan pilihan `Tiada`, `Isi` dan `Cangkerang` yang sama seperti Ekstrak.
* `Tindakan Penutupan` (tidak bertopeng) - Cara bahagian tidak bertopeng ditutup, dengan pilihan yang sama.

##### Ukir {#carve}
* `Ukir` - Berkelakuan seolah-olah anda telah memotong ke dalam permukaan sebanyak nilai `Ketinggian`, seperti mengupas sebahagian kulit oren. `Ketinggian` tidak boleh 0.

##### Ketinggian {#thickness}
* `Ketinggian` - Ketinggian bentuk yang diekstrak. Butang Tambah/Tolak membolehkan anda bertukar antara penyemperitan ke luar, ke dalam, atau kedua-dua belah. 

##### Kehalusan {#smoothness}
Apabila aktif, bentuk yang diekstrak akan dilicinkan; ia berfungsi lebih baik dengan bilangan poligon yang lebih tinggi. 
* `Semua` / `Hanya Tepi` - Licinkan keseluruhan bentuk, atau hanya sempadannya, tanpa mengusik bentuk permukaan atas.
* `Ulangan` - Dengan `Semua`, jumlah pelicinan yang dikenakan. Nilai tinggi menghasilkan tepi melengkung yang sangat licin, tetapi mula menyimpang daripada bentuk topeng.
* `Dinding` - Dengan `Hanya Tepi`, jumlah pelicinan pada dinding. Butangnya bertukar antara Santai, yang mengekalkan penjuru tajam, dan Lancar, yang turut membulatkannya.
* `Bahagian dalam` - Dengan `Hanya Tepi`, sejauh mana permukaan atas diratakan. Butangnya bertukar antara Santai, yang mengekalkan perincian yang diukir dan hanya meratakan arah penyemperitan (supaya perincian tidak lagi menghasilkan pancang), dan Lancar, yang melicinkan permukaan itu sendiri.

##### Sisi {#edge-loop-side}
* `Lurus` - Dinding biasa pada sisi bentuk yang diekstrak.
* `Serong` - (Ekstrak dengan `Cangkerang` sahaja) Bibir condong pada tepi hadapan. `Serong` menetapkan lebarnya, dalam % `Ketinggian` atau dalam unit dunia (butang di sebelahnya menukarnya), `Bahagian serong` membahagikannya (`Auto` secara lalai), dan satu lengkung membolehkan anda membentuk profilnya.
* `Profil` - Bentuk dinding dengan lengkung profil, dengan `Lebar` dalam % `Ketinggian` atau dalam unit dunia.
* `Topeng` - Ketinggian mengikut topeng: bahagian topeng yang kabur mendapat ketinggian yang lebih rendah, membolehkan bentuk dengan ketinggian yang lembut dan berbeza-beza.
* `Bahagian dinding` - Bilangan gelung tepi pada sisi. Dengan `Auto`, Nomad memilih bilangan pembahagian yang menghasilkan poligon segi empat sama sepadan dengan poligon kawasan bertopeng.



### ![](/icons/tool_maskSelector.webp) Topeng Pemilihan {#selection-mask}
Alat Topeng Pemilihan (SelMask) kini menjadi sebahagian daripada [alat Topeng](#mask). Untuk menopeng dengan bentuk dan bukannya sapuan berus, pilih satu bentuk (`Laso`, `Poligon`, `Rekt`...) dalam tetingkap timbul sapuan alat Topeng, lihat [Kawalan pemilihan](#selection-controls).

Mod sub `Buka Masker` juga berfungsi dengan bentuk, dan akan memadam topeng di dalam bentuk itu.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Lukis {#paint}
Kenakan warna dan sifat bahan. Untuk mengetahui lebih lanjut tentang bahan, anda boleh melawat bahagian [Pewarnaan](painting.md).

Mod sub ialah `Padam` dan ia membuang cat.

Selain sapuan berus, Lukis juga boleh mengisi bentuk (`Laso`, `Rekt`, `Jalur`...), lihat [Kawalan pemilihan](#selection-controls).

#### Tetapan Lukis {#paint-settings}
* `Penapisan lapisan` - Ini berfungsi seperti kunci alpha lapisan dalam Photoshop atau Procreate. Jika anda melukis pada satu lapisan dan pilihan ini diaktifkan, anda hanya boleh mengubah kawasan yang sudah ada cat; kawasan yang belum dicat akan dilindungi. Ia hanya tersedia apabila satu lapisan dipilih.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Smudge {#smudge}
Comotkan warna dan sifat bahan. Menu tetapan smudge mengandungi gelangsar `Kualiti`; nilai yang lebih rendah bermakna sapuan yang lebih pantas.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Leperkan {#flatten}
Ratakan kawasan dengan mengunjurkan titik-titik ke atas satah purata.

Mod sub ialah `Isi` dan ia menentukan satah berdasarkan titik tertinggi, dan cenderung menarik titik ke atas.

#### Tetapan Leperkan {#flatten-settings}

* `Kunci arah satah` - Gunakan arah satah yang dikira pada klik pertama. Secara lalai ini dimatikan.
* `Kunci asal satah` - Gunakan klik pertama sebagai tengah satah. Secara lalai ini dimatikan, dan ia hanya boleh diaktifkan bersama `Kunci arah satah`.

Apabila salah satu atau kedua-duanya dimatikan, perataan boleh didalamkan secara beransur-ansur atau sudut satah diubah dengan menggunakan sapuan panjang yang melalui kedalaman dan kelengkungan yang berbeza. Digabungkan dengan pilihan pensampelan kawasan dalam menu berus, ini boleh memberikan kawalan yang sangat tepat.

::: tip
Apabila bekerja di kawasan berkelengkungan tinggi, contohnya cuba meratakan pipi tetapi alat ini asyik menjejaskan sisi hidung, cuba cipta topeng untuk melindungi kawasan yang tidak sepatutnya disentuh oleh berus perata.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar {#planar}
Jadikan titik-titik sesatah dengan mengunjurkannya ke atas satah purata, tetapi dengan kurang penumpukan berbanding berus Leperkan. Ini menghasilkan permukaan bertepi keras yang lebih kemas. Sapuan pantas akan lebih menolak dan menarik permukaan, manakala sapuan perlahan yang bermula dari kawasan yang sudah rata dan bergerak keluar akan lebih mengekalkan satah.

Mod sub ialah `Isi` dan ia menentukan satah berdasarkan titik tertinggi, dan cenderung menarik titik ke atas.

Planar sebenarnya alat yang sama seperti `Leperkan`, tetapi dengan `Kunci arah satah` diaktifkan, bermakna ia cenderung menghasilkan permukaan bertepi keras yang lebih stabil, manakala Leperkan lebih bersifat mengukir dan boleh digunakan untuk mencipta kawasan separa rata.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_polish.webp) Gilap {#polish}
Satu lagi ahli keluarga Leperkan, disediakan untuk menggilap permukaan menjadi satah yang kemas. Ia alat yang sama seperti `Leperkan`, dengan nilai lalai [Sapuan](stroke.md) yang berbeza: `Jejak`, `Penapis Normal Kawasan` dan `Penapis kedalaman` diaktifkan.

Mod sub ialah `Isi`, seperti Leperkan.

Gilap mempunyai tetapan yang sama seperti [Leperkan](#flatten-settings): `Kunci arah satah` dan `Kunci asal satah`.

### ![](/icons/tool_crease.webp) Alur tajam {#crease}
Alat alur tajam berguna untuk mengukir torehan atau lekuk kecil.

Mod sub ialah `Tukar`, dan ia mencipta alur yang menonjol.

#### Tetapan Alur tajam {#crease-settings}

* `Faktor Cipit` - Sejauh mana verteks ditarik ke sisi ke arah berus. Jika cipit pada 1 dan ofset pada 0, permukaan tidak akan berubah kedalaman, hanya topologinya, dengan tepi ditarik ke arah sapuan.
* `Faktor Offset` - Sejauh mana verteks ditolak/ditarik dari segi kedalaman. Jika cipit pada 0 dan ofset pada 1, alur dalam atau lekuk menonjol akan terhasil, tetapi akan kelihatan bergerigi kerana tidak cukup geometri ditarik ke arah alur untuk membentuk sisi atau dasar alur dengan tepat.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Cipit {#pinch}
Alat ini boleh digunakan untuk menajamkan tepi.

Mod sub ialah `Tukar` dan ia menjarakkan verteks.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Potong {#trim}
Alat Potong berfungsi dengan membuang sebahagian mesh anda, dan memberikan pilihan tentang cara memproses jurang yang ditinggalkan. Ia menggunakan [Kawalan pemilihan](#selection-controls) untuk menentukan potongan.

Mod sub ialah `Balik`, dan ia menyongsangkan bentuk, supaya bahagian sebelah lagi yang dibuang.

::: tip
Oleh kerana alat ini mengunjur dari kamera, anda akan menerima amaran jika kamera berada dalam mod perspektif.

Dalam mod ortografik, potongan melalui mesh adalah selari dengan pandangan, iaitu apa yang biasanya dijangka. Dengan kamera perspektif, potongan akan kelihatan berbeza di sebelah jauh objek berbanding sebelah dekat.
:::

#### Tetapan Potong {#trim-settings}

Tetapan dikumpulkan di bawah `Pengisian lubang`:

* `Pewarnaan Goresan` - Jika cat diaktifkan dalam menu lukisan, kawasan yang ditampal akan diisi dengan warna yang sedang dipilih.
* `Boolean` - isi lubang potongan menggunakan kawasan poligon segi empat. Kawasan yang diisi akan rata.
* `Lama` - isi lubang potongan dengan kawasan bersegi tiga. Kawasan yang diisi akan rata.
* `Isi` - isi lubang dengan kawasan bersegi tiga. Kawasan yang diisi akan menjadi permukaan melengkung, seperti selaput buih sabun.
* `Tiada` - jangan isi lubang.

Dengan `Boolean`, bahagian `Perincian` mempunyai:

* `Bentuk` - Anggaran saiz segi empat dan segi tiga yang digunakan pada sebelah bentuk potongan.
* `Lubang` - Anggaran saiz segi tiga atau poligon yang digunakan pada lubang potongan yang diisi. Butang pautan di sebelah `Perincian` memastikannya segerak dengan `Bentuk`; nyahpautkannya untuk menetapkannya secara berasingan.
* `Kekalkan topologi` - Jangan licinkan dan ringkaskan sempadan potongan, supaya topologi asal mesh dikekalkan berhampiran muka yang bertopeng dan tersembunyi.

Dengan `Lama`:

* `Perincian` - Anggaran saiz segi tiga yang digunakan pada potongan.
* `Pelicinan lubang` - Sejauh mana segi tiga dilonggarkan pada kawasan yang diisi.
* `Ambang epsilon` - Nilai yang boleh dilaraskan untuk menambah baik algoritma pengisian lubang lama.

Dengan `Isi`:

* `Perincian` - Anggaran saiz segi tiga yang digunakan pada potongan.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Pisahkan {#split}
Serupa dengan alat [Potong](#trim), kecuali Potong membuang pemilihan manakala Pisahkan menyimpan pemilihan sebagai objek baharu.

Mod sub ialah `Bahagi`: setiap kepingan disimpan sebagai objeknya sendiri, jadi bentuk yang bertindih (contohnya dengan simetri) dipotong menjadi bahagian berasingan dan bukannya dicantumkan menjadi satu.

#### Tetapan Pisahkan {#split-settings}

Pisahkan mempunyai tetapan `Pengisian lubang` yang sama seperti [Potong](#trim-settings): `Pewarnaan Goresan`, kaedah `Boolean`, `Lama`, `Isi` dan `Tiada`, serta pilihan `Perincian` masing-masing.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Unjur {#project}
Alat Unjur kelihatan seperti alat [Potong](#trim), tetapi ia tidak memadam atau mencipta sebarang geometri; ia hanya menggerakkan verteks supaya mengikut pemilihan.

![](/videos/tool_project.mp4)

::: tip
Jika anda menggunakan Unjur semasa berada dalam satu lapisan, anda boleh mengadun antara bentuk asal dan bentuk yang diunjurkan dengan gelangsar lapisan.
:::

### ![](/icons/tool_layer.webp) Lapisan {#layer}
Naikkan permukaan, tetapi hadkan ketinggiannya.

Jika anda terus menekan pensel dan menyapu berulang kali di atas satu kawasan, Lapisan akan naik ke ketinggian tertentu dan berhenti di situ, berbeza dengan alat lain yang terus menumpukkan ketinggian.

Ambil perhatian bahawa secara lalai had ini hanya ditetapkan bagi setiap sapuan! Jika anda memulakan sapuan baharu, ia akan membina daripada ketinggian permukaan yang baharu.

Untuk menetapkan ketinggian maksimum yang tetap merentasi banyak sapuan, gunakan alat Lapisan bersama sistem [Lapisan](layers.md) Nomad.

Cipta satu lapisan, dan gunakan alat ini. Ketinggian maksimum kini ditetapkan daripada lapisan, jadi anda boleh membuat banyak sapuan berus dan ketinggiannya akan sentiasa sama.

`Tolak` menggunakan kedalaman minimum, menghasilkan alur.

#### Tetapan Lapisan {#layer-settings}

* `Gunakan data lapisan` - Apabila aktif, dan apabila satu lapisan dipilih, gunakan data lapisan untuk menetapkan ketinggian maksimum. Satu amaran mengingatkan anda apabila tiada lapisan dipilih.
* `Kembang` - Apabila aktif, laraskan arah kerja lapisan untuk mendapatkan hasil yang lebih licin.
* `Santai (Normal)` - Dengan `Kembang` diaktifkan, jumlah pelicinan yang dikenakan pada normal.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_inflate.webp) Kembang {#inflate}
Gerakkan verteks mengikut normal masing-masing. `Tolak` menggerakkan verteks mengikut normal yang disongsangkan.

#### Tetapan Kembang {#inflate-setings}
* `Santai (Normal)` - Jumlah pelicinan yang dikenakan pada normal.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Geser {#nudge}
Gerakkan atau 'sapukan' titik-titik ke arah sapuan.

Mod sub ialah `Lipatan`, dan ia menolak satu lipatan bahan sepanjang sapuan: bonjolan di hadapan berus, lekukan di belakangnya.

#### Tetapan Geser {#nudge-settings}
* `Licin` - Sejauh mana kawasan di bawah berus dilicinkan semasa anda menggesernya, supaya permukaan yang disapu kekal kemas.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Cap {#stamp}

Klik dan seret untuk menaikkan satu kawasan arca mengikut bentuk Alpha yang dipilih.

Ini sebenarnya hanyalah [alat Berus](#brush) dengan jenis sapuan ditetapkan kepada `Kunci + jejari`. 

`Tolak` akan menekan cap ke dalam dan bukannya menariknya keluar dari permukaan.

::: tip
Cap biasanya berfungsi paling baik dengan geometri beresolusi tinggi. Jika anda mencari dalam talian 'wrinkles alpha', 'pores alpha', 'scales alpha' dan sebagainya, tekstur alpha ini bersama Cap boleh menjadi cara yang hebat untuk menambah perincian organik pada arca watak.

Kedua-dua mod sapuan berguna untuk perkara yang berbeza. 

* `Kunci + jejari` mempunyai *ketinggian* yang tetap; menyeret melaraskan lebar dan putaran cap. Sesuai untuk tekstur kulit yang perlu mempunyai kedalaman/ketinggian yang sama, tetapi putaran dan skala yang berbeza untuk menyembunyikan corak berulang.
* `Kunci + intensiti` mempunyai *lebar* yang tetap; menyeret melaraskan putaran dan ketinggian cap. Sesuai untuk rivet, yang semuanya mesti sama saiz, tetapi dengan putaran dan ketinggian yang berbeza. 

:::

![](/videos/tool_stamp.mp4)

### ![](/icons/tool_vdm.webp) VDM {#vdm}

Cap peta anjakan vektor (VDM). Tidak seperti alpha, yang hanya boleh menolak permukaan ke atas atau ke bawah, VDM menyimpan bentuk 3d yang lengkap, jadi ia boleh mengecap bahagian yang terjulur seperti telinga, tanduk atau daun yang bergulung. Ia berfungsi seperti [Cap](#stamp), dengan mod sapuan `Kunci + jejari` dan `Kunci + intensiti` yang sama.

`Tolak` (`Tukar`) membalikkan kedalaman cap, untuk menekannya ke dalam permukaan seperti acuan.

VDM itu sendiri dipilih dalam menu [Alpha](stroke.md#alpha), yang juga mempunyai gelangsar `Ketinggian` untuk menskalakan ketinggian cap sahaja, tanpa mengubah anjakan ke sisinya.

Butang `Buat` dalam bar alat kiri membolehkan anda membuat cap anda sendiri:

* `VDM baharu...` - Menambah satah yang disediakan untuk mengukir VDM. Ukir bentuk anda di atasnya, kemudian bake dengan `Topologi -> Bake -> VDM`: Nomad menambah cap baharu itu ke pustaka VDM dan memilihnya.
* `Tangkap VDM` - (Percubaan) Seret pada permukaan model untuk mengambil kawasan itu dan menjadikannya cap VDM. `Toleransi` meratakan sempadan tangkapan dengan lancar.

::: tip
Elakkan DynTopo semasa mengukir satah VDM, kerana ia merosakkan UV satah dan mengherotkan cap. Jauhkan juga ukiran daripada sempadan satah, jika tidak cap itu akan menunjukkan tepi yang keras.
:::


### ![](/icons/tool_clearLayer.webp) PadamLapisan {#delete-layer}
Alat ini boleh menetapkan semula lapisan secara setempat; anda memerlukan lapisan aktif, jika tidak tiada apa yang akan berlaku. Ia memadam data ukiran lapisan, dan juga catnya apabila pewarnaan diaktifkan.

Mod sub ialah `Tukar`, dan ia sedikit menguatkan lapisan dan bukannya memadamnya.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tiub {#tube}
Cipta tiub dengan melukis lengkung. 
![](/images/tool_tube_new.webp)

Setelah tiub dicipta, laluannya boleh disunting dalam ruang 3d menggunakan kawalan yang serupa dengan alat [Penyuntingan bentuk](#shape-editing) dan penyuntingan lengkung standard. 

![](/videos/tool_tube.mp4)

#### Bar alat kiri Tiub {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Bar alat kiri mempunyai pilihan berikut:

* `Segerak` - Jika tiub semasa ialah instans, dan terdapat nod anak tiub yang berbeza antara instans, ini akan menyegerakkannya semula.
* `Snap` - Apabila aktif, mod lengkung dan laluan akan melekap pada objek lain semasa anda melukis. Apabila tidak aktif, titik pertama akan melekap, kemudian selebihnya tiub dilukis pada kedalaman itu.
* `Ofset` - Tetapkan kedalaman lekapan; 0% meletakkan tengah keratan rentas tiub pada permukaan, nilai positif mengangkatnya dari permukaan, nilai negatif merendahkannya. 100% bersamaan dengan jejari tiub.
* `Lihat` - Tiada mod lukisan, jadi anda boleh menggerakkan kamera dengan bebas.
* `Lengkung` - Lakar tiub secara bebas. Ia mempunyai menu kecil:
    * `Sunting` - Apa yang berlaku apabila anda selesai menyapu, lihat [Kawalan pemilihan](#selection-controls): cipta tiub serta-merta, kekalkan lengkung boleh disunting dengan bulatan pengesahan hijau di sebelahnya, atau `Tahan` di hujung sapuan untuk terus menyunting.
    * `Tertutup` - jadikan tiub satu gelung.
    * `Terus melukis` - Selepas mengesahkan satu tiub, kekal dalam alat untuk melukis tiub seterusnya.
    * `Ketepatan` - Berapa banyak titik lengkung yang digunakan untuk menukar laluan yang dilukis menjadi tiub. 0% menggunakan bilangan titik paling sedikit, tetapi akan terlepas perubahan kelengkungan kecil. 100% sangat tepat, dan menggunakan banyak titik.
* `Laluan` - Cipta tiub dengan mengklik untuk menentukan titik lengkung. Ketik bulatan hijau untuk mengesahkan laluan. Ia mempunyai menu kecil:
    * `B-spline` - Kaedah melukis lengkung alternatif di mana titik lengkung biasanya tidak terletak betul-betul pada lengkung, tetapi boleh menghasilkan keputusan yang lebih licin daripada kaedah lalai.
    * `Tertutup` - jadikan tiub satu gelung
    * `Skrin` - Apabila aktif, laluan 'disematkan' pada skrin, membolehkan anda menggerakkan pandangan dan objek sementara laluan kekal di tempatnya. Apabila tidak aktif, laluan menjadi sebahagian daripada adegan 3d, dan ia akan bergerak bersama kamera dan objek.
* `Keratan` - Lengkung menjadi gelang mengelilingi bentuk, dipotong melalui dua titiknya mengikut arah pandangan anda.

##### Bar alat atas Tiub {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Apabila satu tiub dipilih, satu bar alat akan muncul di bahagian atas port pandangan dengan kawalan tambahan. Klik tajuk bar alat untuk meruntuhkan/mengembangkannya, dan klik anak panah di bahagian atas kanan untuk memindahkan bar alat ke bahagian atas atau bawah port pandangan.

* `Muktamadkan` - bake tiub menjadi poligon biasa supaya ia boleh diukir.
* `Sunting` - paparkan titik lengkung supaya ia boleh dimanipulasi
* `Cermin` - tambah pengulang cermin sebagai induk lengkung ini
* `Snap` - lekapkan titik lengkung pada permukaan berdekatan
* `Tertutup` - Sambungkan permulaan dan penghujung lengkung untuk membentuk gelung
* `B-spline` - Togol antara interpolasi Catmull-rom dan B-spline.
* `Tutup` - Bertukar antara penutup di kedua-dua hujung tiub, atau di permulaan atau penghujung sahaja, atau tiada penutup.
* `Lubang` - Tambah ketebalan pada tiub, menukarkannya menjadi paip. Bertukar antara lubang di kedua-dua hujung, di penghujung sahaja, atau tiada lubang. 
* `Jejari` - Bertukar antara jejari seragam, jejari di permulaan dan penghujung, atau jejari bagi setiap titik lengkung. Ini disunting dengan pemegang jingga pada lengkung.
* `Lilitan` - Bertukar antara tiada lilitan, lilitan seragam, lilitan di permulaan dan penghujung, atau lilitan bagi setiap titik lengkung. Ini disunting dengan pemegang merah jambu pada lengkung.
* `Profil` - Bertukar antara tiada profil (iaitu profil bulat), profil seragam, profil di permulaan dan penghujung, atau profil bagi setiap titik.
* `Sunting profil` - Paparkan penyunting profil. Ia berfungsi seperti alat [Penyuntingan bentuk](#shape-editing), boleh menyimpan dan memuatkan pratetap profil, dan mempunyai togol untuk membolehkan anda menyunting profil dalam ruang 3d.
* `Lingkaran` - Togol menu untuk menambah pulasan lingkaran pada tiub. Menu ini mempunyai pilihan `Sudut lilitan`, `Ofset`, `Skala` dan `Anjak sudut`.
* `Pembahagian X` - bilangan pembahagian di sekeliling tiub; contohnya 4 pembahagian akan menghasilkan tiub segi empat. 
* `Ketumpatan tetap` - apabila aktif, poligon dikekalkan segi empat sama. Apabila dimatikan, anda boleh menetapkan `Pembahagian Y` sepanjang tiub.
* `...` - Menu tetapan tiub.

#### Togol padam titik lengkung {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Di bawah bar alat terdapat togol padam titik lengkung. Apabila anda menyeret satu titik lengkung berhampiran titik lain, ia akan bertukar merah, menandakan bahawa jika anda melepaskannya, titik itu akan dipadam. Jika anda membuat suntingan kecil dan tidak mahu memadam titik, butang ini akan mematikan tingkah laku padam titik.



#### Tetapan Tiub {#tube-settings}
* `Primitif` - butang untuk mengaktifkan/mematikan UV, atau untuk mengesahkan tiub.
* `Pembahagian selepas` - pintasan untuk menetapkan tahap multiresolusi sebelum pengesahan.
* `Pembahagian linear` - pintasan untuk menetapkan tahap pembahagian linear sebelum pengesahan. 
* `Pembahagian X` - sama seperti Pembahagian X dalam bar alat.
* `Pembahagian Y` - sama seperti Pembahagian Y dalam bar alat.
* `Lengkung (Pengulang)` - tukar tiub menjadi [Pengulang Lengkung](scene.md#curve)

::: tip
Pembahagian pada 4 dan Pembahagian selepas pada 3 akan menghasilkan tiub licin berhujung bulat, sesuai untuk cacing, ular dan bahagian badan.
:::


### ![](/icons/tool_lathe.webp) Larik {#lathe}
Cipta permukaan putaran dengan melukis lengkung.

Alat ini sangat sesuai untuk bentuk seperti pasu dan gelas wain.

![](/videos/tool_lathe.mp4)

#### Bar alat kiri Larik {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Bar alat kiri mempunyai pilihan berikut:

* `Segerak` - Jika larik semasa ialah instans, dan terdapat nod anak larik yang berbeza antara instans, ini akan menyegerakkannya semula.
* `Tetap` - Apabila diaktifkan, tengah larik ditetapkan dan dipaparkan pada skrin. Garis tengah ini mempunyai titik suntingan yang boleh dilaraskan. Apabila dimatikan, tengah larik dikemas kini secara dinamik supaya sepadan dengan permulaan dan penghujung lengkung yang dilukis.
* `Lihat` - Tiada mod lukisan, jadi anda boleh menggerakkan kamera dengan bebas.
* `Lengkung` - Lukis profil larik dalam satu sapuan. Ia mempunyai menu kecil:
    * `Sunting` - Apa yang berlaku apabila anda mengangkat pensel, lihat [Kawalan pemilihan](#selection-controls): cipta larik serta-merta, kekalkan lengkung boleh disunting dengan bulatan hijau di sebelahnya untuk mencipta larik, atau `Tahan` di hujung sapuan untuk terus menyunting.
    * `Tertutup` - Sambungkan permulaan dan penghujung lengkung untuk membentuk gelung
    * `Terus melukis` - Selepas mengesahkan satu larik, kekal dalam alat untuk melukis larik seterusnya.
    * `Ketepatan` - Berapa banyak titik lengkung yang digunakan untuk menukar laluan yang dilukis menjadi tiub. 0% menggunakan bilangan titik paling sedikit, tetapi akan terlepas perubahan kelengkungan kecil. 100% sangat tepat, dan menggunakan banyak titik.
* `Laluan` - Cipta larik dengan mengklik untuk menentukan titik lengkung. Ketik bulatan hijau untuk mengesahkan laluan. Ia mempunyai menu kecil:
    * `B-spline` - Kaedah melukis lengkung alternatif di mana titik lengkung biasanya tidak terletak betul-betul pada lengkung, tetapi boleh menghasilkan keputusan yang lebih licin daripada kaedah lalai.
    * `Tertutup` - jadikan tiub satu gelung
    * `Skrin` - Apabila aktif, laluan 'disematkan' pada skrin, membolehkan anda menggerakkan pandangan dan objek sementara laluan kekal di tempatnya. Apabila tidak aktif, laluan menjadi sebahagian daripada adegan 3d, dan ia akan bergerak bersama kamera dan objek.

#### Bar alat atas Larik {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Apabila satu larik dipilih, satu bar alat akan muncul di bahagian atas port pandangan dengan kawalan tambahan. Klik tajuk bar alat untuk meruntuhkan/mengembangkannya, dan klik anak panah di bahagian atas kanan untuk memindahkan bar alat ke bahagian atas atau bawah port pandangan.

* `Muktamadkan` - bake larik menjadi poligon biasa supaya ia boleh diukir.
* `Sunting` - paparkan titik lengkung supaya ia boleh dimanipulasi
* `Cermin` - tambah pengulang cermin sebagai induk larik ini
* `Snap` - lekapkan titik lengkung pada permukaan berdekatan
* `Stabil` - Apabila diaktifkan, profil lengkung menjadi anak kepada garis tengah larik. Apabila dimatikan, garis tengah boleh disunting tanpa menggerakkan lengkung, membolehkan bentuk yang lebih kompleks.
* `Fokus` - Memutar pandangan supaya profil lengkung kelihatan rata sepenuhnya menghadap kamera.
* `Tertutup` - Sambungkan permulaan dan penghujung lengkung untuk membentuk gelung
* `Tutup` - Jika Tertutup dimatikan, bertukar antara penutup di kedua-dua hujung tiub, atau di permulaan atau penghujung sahaja, atau tiada penutup.
* `Lubang` - Tambah ketebalan pada larik, menukarkannya menjadi paip. Bertukar antara lubang di kedua-dua hujung, di penghujung sahaja, atau tiada lubang. 
* `B-spline` - Togol antara interpolasi Catmull-rom dan B-spline.
* `Pembahagian X` - bilangan pembahagian di sekeliling larik; contohnya 4 pembahagian akan menghasilkan larik berprofil segi empat. 
* `Ketumpatan tetap` - apabila aktif, poligon dikekalkan segi empat sama. Apabila dimatikan, anda boleh menetapkan `Pembahagian Y` sepanjang tiub.
* `...` - Menu tetapan larik.

#### Tetapan Larik {#lathe-settings}
* `Primitif` - butang untuk mengaktifkan/mematikan UV, atau untuk mengesahkan tiub.
* `Pembahagian selepas` - pintasan untuk menetapkan tahap multiresolusi sebelum pengesahan.
* `Pembahagian linear` - pintasan untuk menetapkan tahap pembahagian linear sebelum pengesahan. 
* `Pembahagian X` - sama seperti Pembahagian X dalam bar alat.
* `Pembahagian Y` - sama seperti Pembahagian Y dalam bar alat.
* `Lengkung (Pengulang)` - tukar profil lengkung menjadi [Pengulang Lengkung](scene.md#curve)

### ![](/icons/tool_insert.webp) Masukkan {#insert}
Letakkan satu objek pada permukaan objek lain. Cara penggunaannya serupa dengan alat cap, tetapi untuk bentuk 3d yang lengkap.

Jika anda memilih satu primitif daripada bar alat kiri, klik-seret pada mana-mana permukaan akan meletakkan primitif di tempat anda klik, dan seretan menetapkan saiznya. Sebaik sahaja anda selesai menyeret, Masukkan akan bertukar ke mod [Transformasi](#transform).

Dalam mod Instans, menyeret akan mencipta dan menggelongsorkan instans baharu di atas permukaan. Saiznya disalin daripada bentuk pertama; dengan cara ini anda boleh meletakkan banyak instans sesuatu objek yang sama saiz di atas permukaan lain.

Anda bukan hanya boleh memasukkan primitif! Pilih *mana-mana* bentuk dalam outliner; jika Masukkan berada dalam mod Instans atau Klona, anda boleh menyeret salinan objek yang dipilih ke atas mana-mana permukaan lain.

Jika satu objek mempunyai paksi tersuai, ia akan digunakan sebagai titik sauh. Lihat video di bawah.

Bar alat kiri juga mempunyai `Lihat`, untuk menggerakkan kamera tanpa memasukkan apa-apa, dan `Segerak`: apabila objek sasaran ialah instans, objek baharu turut ditambah pada semua instans lain.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transformasi {#transform}
Gerak/Putar/Skala model secara terus dengan 1 dan 2 jari, biasanya di atas permukaan objek lain.

Bar alat kiri mempunyai butang-butang ini:

* `Klona` / `Instans` - Buat salinan atau instans objek, lihat bar alat [Gizmo](#left-menu-toolbar).
* `Gerak` - Seretan satu jari akan menggerakkan objek. Apabila snap aktif, ini akan menggelongsorkan objek di sepanjang permukaan di bawah jari anda.
* `Putar` - Seretan satu jari akan memutar objek. Apabila snap aktif, ia berputar mengelilingi normal permukaan di bawah jari anda.
* `Skala` - Seretan satu jari akan menskalakan objek.

Satu bar alat di bahagian atas port pandangan mempunyai:

* `Sasaran` - Sama ada alat menggerakkan objek, kumpulannya, atau verteksnya, sama seperti bagi [Gizmo](#left-menu-toolbar).
* `Snap` - lekapkan model pada permukaan lain.
* `Permukaan` / `Verteks` - Dengan `Snap`, lekap pada permukaan, atau pada verteks terdekat.

Transformasi boleh mengendalikan 2 daripada mod ini dengan pantas menggunakan 2 jari:

* Seret objek untuk meletakkannya. Berhenti menggerakkan jari pertama anda, tetapi jangan angkat dari skrin.
* Sentuh skrin dengan jari kedua sambil jari pertama masih menekan. Apabila jari kedua diseret, objek akan diskalakan.
* Angkat jari kedua, dan teruskan menyeret jari pertama; objek akan kembali ke mod gerak.

Anda juga boleh menukar mod kedua dengan gerak isyarat ketik jari kedua:

* Seret objek untuk meletakkannya, berhenti bergerak, tetapi jangan angkat jari anda dari skrin.
* Ketik dengan jari kedua sambil jari pertama masih menekan
* Alat bertukar ke mod putaran. Seret jari pertama anda untuk menetapkan putaran.
* Ketik jari kedua seperti tadi, dan alat kembali ke mod gerak.

Ini memberikan aliran kerja yang pantas untuk mengklon objek di atas objek lain, contohnya batu di atas landskap. Perhatikan bahawa butang klona juga terdapat dalam bar alat kiri untuk akses mudah:

* Gunakan alat transformasi untuk menggerakkan batu ke tempatnya.
* Lepaskan, tekan butang klona
* Gerakkan batu ini, putar/skala mengikut keperluan
* Lepaskan, tekan butang klona
* Gerakkan batu ini, ulang.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Alat ini membolehkan anda menggerak, memutar dan menskala objek, serta mengubah paksi objek.

Pemegang dalam port pandangan mempunyai ciri-ciri berikut:

* `Gerak` - Seret pada garis+anak panah untuk bergerak pada X/Y/Z. Seret pada titik berwarna pic di tengah gizmo untuk menganjak secara bebas dalam ruang skrin. Klik pada segi empat merah, hijau, biru untuk menganjak pada satah X/Y/Z.
* `Putar` - Seret pada bulatan merah/hijau/biru untuk berputar pada X/Y/Z. Seret sfera di dalam bulatan untuk berputar secara bebas.
* `Skala` - Seret pada titik luar merah/hijau/biru untuk menskala pada X/Y/Z. Seret pada kon luar merah/hijau/biru untuk menskala pada satah X/Y/Z. Seret pada bulatan luar berwarna pic untuk menskala secara seragam.

![](/images/tool_gizmo.webp)

#### Nod dan verteks {#nodes-and-vertices}

Setiap objek dalam Nomad terdiri daripada nod dan verteks:

* `Nod` - 'Pemegang' objek, yang menyimpan anjakan, putaran dan skalanya, dipanggil matriks transformasinya.
* `Verteks` - Titik-titik yang membentuk permukaan objek; ia menyimpan maklumat kedudukan dan cat.

Jika anda mempunyai kotak ringkas yang terdiri daripada 8 verteks, anda boleh menganjaknya dengan mengubah matriks transformasinya, atau dengan mengubah kedudukan verteks. Semasa mengukir anda biasanya mahu mengubah verteks; semasa menggerakkan objek dengan gizmo, anda biasanya mahu mengubah nod. Nomad membolehkan anda melakukan kedua-duanya. 

#### Bar alat Gizmo {#left-menu-toolbar}

Bar alat sebelah kiri mempunyai:

* `Klona` - Buat salinan berdiri sendiri bagi objek semasa, yang boleh diseret keluar dengan gizmo.
* `Instans` - Buat salinan instans bagi objek semasa. Objek-objek itu dipautkan, jadi perubahan ukiran pada satu objek akan muncul pada semua objek instans.
* `Paksi` - (Ikon kunci, menggantikan butang `Tolak`) Apabila diaktifkan, gizmo boleh digerakkan dan diputar tanpa menggerakkan objek. Seperti `Tolak`, tahannya untuk perubahan pantas, atau ketik untuk memastikannya hidup.

Satu bar alat di bahagian atas port pandangan mempunyai kawalan lain:

* `Sasaran` - Menetapkan sama ada gizmo menjejaskan nod atau verteks objek:
    * `Auto` - Lalai; ia berfungsi seperti `Kumpulan`, tetapi jika mesh mempunyai topeng atau simetri diaktifkan, ia berfungsi seperti `Verteks`.
    * `Verteks` - Kenakan transformasi pada verteks, dengan mengambil kira topeng dan simetri. Ia tidak berfungsi pada primitif yang belum dimuktamadkan, dan instans turut terjejas.
    * `Objek` - Gerakkan objek semasa sahaja, mengabaikan simetri dan topeng. Objek anak kekal di tempatnya.
    * `Kumpulan` - Gerakkan objek dan seluruh hierarkinya, mengabaikan simetri dan topeng.
    * `Instans` - (Objek dan Kumpulan) Sama, tetapi setiap instans objek turut bergerak.
* `Paksi` - Tetingkap timbul untuk meletakkan paksi dengan pantas, diterangkan [di bawah](#pivot).
* `Semua` / `Gerak` / `Putar` / `Skala` - Paparkan semua pemegang gizmo, atau hanya pemegang gerak, putar atau skala.
* `Pinkan` - Secara lalai gizmo akan berpindah ke paksi objek yang dipilih. Apabila pin diaktifkan, gizmo kekal di tempatnya sekarang.
* `Selaras` - Togol sama ada paksi diselaraskan dengan objek semasa, atau dengan dunia.
* `Snap` (putaran) - Aktifkan nilai putaran dilekapkan mengikut kenaikan; nilai snap dipaparkan dan boleh disunting apabila snap aktif. Pilihan `Magnet` membuat putaran melekat pada satu langkah apabila melintasinya, kemudian bergerak bebas semula; matikannya untuk melompat dari langkah ke langkah.
* `Snap` (anjakan) - Aktifkan nilai anjakan dilekapkan mengikut kenaikan; nilai snap dipaparkan dan boleh disunting apabila snap aktif.

#### ![](/icons/reset.webp) Paksi {#pivot}
Tetingkap timbul `Paksi` dalam bar alat atas membolehkan perubahan paksi yang pantas. Kedudukan dan orientasi paksi memacu gizmo.

**Tetapkan semula** 
* `Auto` - Tengah objek, diselaraskan dengan transformasinya.
* `Tengah` - Pindahkan paksi ke tengah objek, mengekalkan orientasinya.
* `Bawah` - Pindahkan paksi ke tengah bahagian bawah objek. Ketik sekali lagi untuk menggunakan kotak sempadan dunia.
* `Atas` - Pindahkan paksi ke tengah bahagian atas objek. Ketik sekali lagi untuk menggunakan kotak sempadan dunia.
* `Objek` - Pindahkan paksi ke asalan objek, diselaraskan dengan transformasinya.
* `Topeng` - Pindahkan paksi ke tengah kawasan tidak bertopeng. Ketik sekali lagi untuk bertukar ke kawasan bertopeng.
* `Jajarkan` - Tetapkan semula putaran supaya sejajar dengan dunia, mengekalkan kedudukan.
* `Pandangan` - Jajarkan paksi dengan pandangan semasa, mengekalkan kedudukan. Ia tidak mengikut kamera selepas itu.

**Apabila diketuk (mod Paksi)**

Hanya aktif semasa `Paksi` dihidupkan; ia menetapkan apa yang berlaku apabila anda mengetik sekali pada permukaan mesh:
* `Tiada` - tidak melakukan apa-apa apabila objek diketik
* `Normal` - Gerak dan putar paksi supaya sejajar dengan tempat permukaan diketik
* `Pertama` - Gerakkan (tetapi jangan putar) paksi ke tempat permukaan diketik
* `Tengah` - Pindahkan paksi ke tengah objek, di bawah tempat permukaan diketik.

#### Tetapan Gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

* `Padat` - togol susun atur gizmo untuk meletakkan pemegang tambahan di luar atau di dalam sfera putaran
* `Saiz Gizmo` - saiz gizmo
* `Ketebalan` - saiz garisan pada gizmo
* `Kelegapan` - kelegapan gizmo
* `Sembunyi semasa interaksi` - togol sama ada gizmo disembunyikan buat sementara semasa diseret

-----

* `Ambang gulung tangent` - Kawal bagaimana antara muka putaran berkelakuan apabila menyeret pada pemegang bulatan untuk berputar pada X/Y/Z. Jika nilai ini 0, putaran berfungsi seperti dail: seret gizmo dalam bulatan. Jika nilai ini 90, putaran berfungsi seperti menarik tali yo-yo: seret dalam garis lurus ke arah atau menjauhi tempat anda mula-mula klik. Nilai antara 0 dan 90 menggabungkan kedua-duanya; di bawah nilai itu ialah gerakan linear, di atasnya gerakan bulat.
* `Input berangka` - apabila diaktifkan, satu ketikan pada gizmo akan membuka tetingkap untuk memasukkan nilai tepat bagi paksi widget yang diketik.

::: warning
Alat [Gizmo](#gizmo) dan [Transformasi](#transform) menggunakan kotak semak simetri mereka sendiri, berasingan daripada simetri ukiran!

Secara lalai simetri ini dimatikan.
:::

##### Matriks {#matrix}
Nilai transformasi tepat objek tidak lagi berada dalam tetapan Gizmo: ia telah dipindahkan ke menu `Transformasi`, di menu atas sebelah kanan. Bahagian `Matriks` di dalamnya mempunyai:

* ![](/icons/target.webp) `Pindah ke asalan` - Gerakkan objek supaya paksinya berada di tengah adegan, dipanggil asalan.
* ![](/icons/bake.webp)  `Bake` - Bekukan objek di tempatnya sekarang, dan tetapkan nilai anjakan/putaran kepada 0, skala kepada 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Paksi` - Bake paksi: jadikan nilai matriks sepadan dengan kedudukan pemegang gizmo di dunia.
* ![](/icons/reset.webp) `Tetapkan semula` - Pintasan yang menetapkan nilai anjakan kepada 0, nilai putaran kepada 0, skala kepada 1, sekali gus menggerakkan dan memutar objek.

::: tip Bake berbanding bake ke paksi
Cipta sebuah kotak, pilih alat Gizmo, buka dan pinkan menu `Transformasi`. Secara lalai anjakan dan putaran ialah 0, skala ialah 1.

Aktifkan mod paksi, gerakkan pemegang ke satu sisi, kemudian matikan mod paksi. Paksi telah berubah, tetapi perhatikan bahawa nilai anjakan masih 0. 

Jika anda mahu melihat di mana paksi itu *sebenarnya* berada, klik butang bake `Paksi`. Kini nilai anjakan dikemas kini. Perhatikan bahawa kotak tidak bergerak semasa operasi ini, mahupun dalam mod paksi.

Gerak dan putar kotak ke suatu tempat, kemudian ketik `Pindah ke asalan`. Ia menggerakkan objek supaya paksinya berada di tengah dunia, tetapi tidak mengubah putaran.

Klik `Tetapkan semula`, dan putaran turut ditetapkan kepada 0.

Gerak dan putar kotak sekali lagi, kali ini klik `Bake`. Paksi kekal di tempatnya, kotak kekal di tempatnya, tetapi nilai anjakan dan putaran ditetapkan kepada 0.

Cuba ini beberapa kali! Fahami bahawa nilai paksi tersembunyi dan Nomad menguruskannya untuk anda, tetapi jika anda perlu menetapkan paksi ke lokasi sebenar dalam ruang, bake paksi akan melakukannya untuk anda.

:::

* `Anjakan` - nilai anjakan X, Y, Z
* `Putaran` - nilai putaran X, Y, Z
* `Skala` - Skala seragam jika ia diaktifkan, atau skala X, Y, Z jika dimatikan.
* `Serong` - nilai serong (ricih) X, Y, Z, hanya dipaparkan apabila objek sudah diserongkan
* `Skala seragam` - Togol keupayaan untuk menskala secara seragam atau secara berasingan pada setiap paksi

Di sebelah kiri anda boleh menggerakkan paksi gizmo; anda boleh melihatnya beraksi dalam video di bawah.
Ini sangat berguna untuk putaran, kerana ia tidak mengubah apa-apa bagi anjakan.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Kumpulan muka {#facegroup}

Kumpulan muka membolehkan anda menyusun objek anda kepada muka-muka yang berlainan warna. Anda boleh menggunakan kumpulan ini dalam banyak cara dalam Nomad:

* Kaedah pemilihan pantas untuk topeng
* Sembunyikan/paparkan bahagian objek anda
* Susun objek anda tanpa perlu memisahkannya kepada bahagian berasingan
* Tentukan kawasan UV
* Membimbing quad remesher
* Kawalan tambahan untuk alat seperti Lancar.

#### Bar alat kiri Kumpulan muka {#facegroup-left-toolbar}

* `Kumpulan` - Butang ini memaparkan kumpulan muka semasa. Ketik untuk memaparkan kumpulan muka yang tersedia sebagai tampalan dan pilih satu. Ketik pada satu tampalan untuk menamakan semula, menukar warnanya, atau memadamnya. `Buang yang tidak dipakai` memadam tampalan yang tidak digunakan, `Tetapkan semula` membuang semuanya. Ikon tambah membolehkan anda mencipta tampalan baharu.
* `Titik` - Lukis pada objek untuk menentukan kumpulan muka. Apabila '+ Kumpulan muka' diaktifkan, setiap sapuan baharu akan mencipta kumpulan muka baharu secara automatik, berguna untuk menentukan kawasan dengan pantas. Satu ketikan akan mengisi penuh kawasan yang dipilih. Gelangsar menetapkan jejari titik.
* `Santai` - Licinkan sempadan kumpulan muka. Sangat berguna untuk menentukan tepi yang kemas untuk quad remesh, atau untuk menentukan panel bagi pemodelan permukaan keras. Gelangsar mengawal jejari dan intensiti operasi santai.
* Bentuk - Cipta kumpulan muka dengan bentuk dan bukannya berus, melalui `Kunci + jejari`, `Laso`, `Poligon`, `Garis`, `Rekt` dan `Elips`. Lihat [Kawalan pemilihan](#selection-controls) untuk maklumat lanjut.
* `Pilih` - Mod sub. Apabila diaktifkan, ia memilih tampalan tempat sapuan bermula, dan menggunakan tampalan itu untuk sepanjang sapuan. Sangat berguna untuk mengemaskan kawasan kumpulan muka; jika satu kumpulan muka telah melimpah terlalu jauh, aktifkan `Pilih`, mulakan sapuan dari tempat tampalan kumpulan muka itu betul, dan seret hingga ke sempadan untuk menetapkan semula tampalan yang betul.

#### Bar alat atas Kumpulan muka {#facegroup-top-toolbar}

Satu bar alat di bahagian atas port pandangan mempunyai kawalan tambahan:

* `Santai (Semua)` - Seret untuk melonggarkan sempadan semua kumpulan muka sekali gus.
* `Depan` / `Kelihatan` / `Bersambung` - Penapis sapuan yang sama seperti bar alat [Topeng](#mask).
* `Daripada normal` - Cipta kumpulan muka berdasarkan sudut antara muka. Tetingkap timbul mempunyai `Sudut`, dan membolehkan anda melangkau kumpulan kecil berdasarkan `Bilangan muka` atau `Kawasan permukaan`, dengan `Pratonton` sebelum anda mengesahkan.
* `Daripada bahagian` - Cipta satu kumpulan muka bagi setiap bahagian yang tidak bersambung.
* `Daripada UV` - Cipta satu kumpulan muka bagi setiap pulau UV.
* `Daripada topeng` - Cipta satu kumpulan muka daripada kawasan bertopeng.
* `Ketuk` - Pilih apa yang dilakukan oleh ketikan pada satu kumpulan muka: isikannya dengan kumpulan muka semasa, sembunyikannya, topengkannya, atau `Pose` (kumpulan yang diketik dan apa yang terletak di luarnya dinyahtopeng, dan gizmo diletakkan pada sendi, dengan gelangsar `Kabur` untuk topeng). Togol `Ketuk` kedua, tersedia apabila mesh mempunyai topeng, mengehadkan ketikan kepada muka di sebelah topeng yang sama.
* Butang `Bersihkan` untuk alat [Sembunyi](#hide) dan [Topeng](#mask), untuk memaparkan semula semuanya atau mengosongkan topeng tanpa meninggalkan alat.

#### Tetapan Kumpulan muka {#facegroup-settings}

Menu `Alat` mengekstrak kumpulan muka menjadi objek baharu, dengan pilihan yang sama seperti `Ekstrak` dalam [Tetapan Topeng](#mask-settings). Butang `Kumpulan muka` di bahagian atas memilih kumpulan mana yang diekstrak, dan terdapat gelangsar `Jurang` tambahan: ia menggerakkan setiap sempadan ke dalam di sepanjang permukaan; nilai negatif menggerakkannya ke luar supaya bertindih. Bagi panel yang bersebelahan, gunakan separuh daripada jurang yang dikehendaki.

### ![](/icons/tool_hide.webp) Sembunyi {#hide}
Sembunyikan atau asingkan bahagian objek. 

Mod utama dikawal dari menu sebelah kiri:

* `Titik` - Sapu pada objek untuk menyembunyikan bahagian objek.
* Bentuk - Sembunyikan dengan bentuk dan bukannya berus, melalui `Laso`, `Poligon`, `Garis`, `Rekt` dan `Elips`. Lihat [Kawalan pemilihan](#selection-controls) untuk maklumat lanjut.
* `Tunjuk` - Mod sub, menyongsangkan operasi, supaya mod yang dipilih memaparkan dan bukannya menyembunyikan bahagian objek.

Satu bar alat akan muncul di bahagian atas port pandangan dengan kawalan tambahan:

* `Kosongkan semua` - Pulihkan objek; semua bahagian tersembunyi akan dipaparkan semula. Apabila objek lain turut mempunyai bahagian tersembunyi, butang `Bersihkan` tambahan hanya memulihkan objek yang dipilih.
* `Tukar` - Tukar antara bahagian yang tersembunyi dan yang kelihatan.
* `Padam` - Padam bahagian tersembunyi objek
* `Pisah` - Pisahkan bahagian tersembunyi objek menjadi bentuk baharu.
* `Depan` / `Kelihatan` / `Bersambung` - Penapis sapuan yang sama seperti bar alat [Topeng](#mask).
* `Ketuk` (kumpulan muka) - Gunakan kumpulan muka untuk menyembunyikan bahagian dengan pantas; mengetik satu kumpulan muka akan menyembunyikan keseluruhan kumpulan muka itu.
* `Ketuk` (topeng) - Jika topeng aktif, mengetik akan menyembunyikan bahagian bertopeng.

### ![](/icons/tool_measure.webp) Ukur {#measure}
Seret untuk mengukur jarak antara 2 titik. Setelah diletakkan, anda boleh menyeret titik hujung untuk melaraskan ukuran.

Bar alat kiri memilih cara jarak diukur:

* `Garis` - Garis lurus antara dua titik.
* `Permukaan` - Jarak di sepanjang permukaan, mengikut potongan melalui dua titik seperti yang dilihat dari kamera.
* `Keratan` - Perimeter keratan rentas melalui dua titik, seperti pita ukur yang dililit pada lengan.
* `Verteks` - Lekapkan titik hujung pada verteks terdekat.
* `Nisbah emas` - Paparkan titik kuning pada titik nisbah emas ukuran.
* Butang `?` memaparkan isipadu, luas permukaan dan saiz objek yang dipilih.

### ![](/icons/tool_arrange.webp) Susun {#arrange}
Jajarkan dan atur beberapa objek sekali gus, seperti alat penjajaran dalam aplikasi reka bentuk 2d. Pilih objek-objek itu dahulu; dengan satu objek sahaja, Susun bertindak pada bahagian-bahagiannya yang berasingan. Satu kotak dilukis mengelilingi pemilihan; seret pemegangnya untuk menskalakannya.

Satu bar alat di bahagian atas port pandangan mempunyai kawalan:

* `Dunia` / `Skrin` - Susun mengikut paksi dunia, atau mengikut skrin (kiri, kanan, atas, bawah).
* `Selaras` - Jajarkan objek pada nilai minimum, tengah atau maksimumnya, pada setiap paksi.
* `Agihkan` - Jarakkan objek secara sekata di antara dua objek paling luar, mengikut minimum, tengah atau maksimumnya. Ia memerlukan sekurang-kurangnya 3 objek.
* `Garis` - Susun objek dalam satu baris di sepanjang satu paksi.
* `Grid` - Susun objek dalam grid, dengan bilangan objek pada `X`, `Y` dan `Z`.
* `Bulatan` - (Dunia sahaja) Susun objek dalam bulatan mengelilingi paksi `X`, `Y` atau `Z`.
* `Sfera` - (Dunia sahaja) Susun objek di atas sfera.

`Garis`, `Grid`, `Bulatan` dan `Sfera` semuanya mempunyai gelangsar `Jarak` untuk ruang antara objek.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Alat ini akan menukar objek yang dipilih kepada susun atur topologi segi empat yang kemas, dengan kawalan untuk ketumpatan, aliran tepi dan simetri. 

::: tip
Quad Remesher dibangunkan oleh [Exoside](https://exoside.com/) untuk iOS dan desktop. 

Untuk iOS, ia ialah pembelian dalam aplikasi di dalam Nomad, bayaran sekali sahaja sebanyak $16USD.

Untuk desktop, beli lesen daripada [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Anda boleh membelinya untuk Nomad desktop sahaja, atau lesen silang untuk semua aplikasi desktop yang disokong.

Jika anda sudah memiliki Quad Remesher untuk aplikasi desktop lain, anda boleh [membeli naik taraf ke semua platform dengan kos yang lebih rendah.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher tidak tersedia untuk Android. Android boleh menggunakan remesher sumber terbuka percuma dalam tab topologi [Remesh kuad](topology.md#quad-remesh) (AutoRemesher, Instant Mesh, QuadriFlow), tetapi fahami bahawa set cirinya lebih terhad.
:::

Selagi Quad Remesher belum dibuka kunci, bar alat atas bermula dengan butang troli dan bukannya butang remesh. Pada iOS ia membuka pembelian dalam aplikasi. Pada desktop ia memaparkan `Buka kunci (pembelian, pemulihan, percubaan)`, yang menyemak lesen Exoside anda (atau memulakan percubaan). Setelah aktif, bar alat kiri dan atas akan diaktifkan.

* `Titik` - Berus ini menetapkan ketumpatan sasaran. Intensiti pada 100% melukis warna merah, yang menggunakan dua kali ganda ketumpatan segi empat sasaran di kawasan tersebut. Intensiti pada 0% melukis warna sian, yang menggunakan separuh ketumpatan segi empat sasaran di kawasan tersebut. Intensiti pada 50% melukis warna kelabu, yang menggunakan ketumpatan segi empat sasaran lalai.
* `Lancar` - Licinkan peralihan ketumpatan merah/kelabu/sian.
* `Smudge` - Comotkan lukisan ketumpatan.
* `Lengkung` - Lakar lengkung pada permukaan arca; quad remesher akan menggunakannya sebagai panduan untuk aliran tepi. Ketik pada lengkung untuk memadamnya.
* `Laluan` - Lukis laluan pada permukaan arca; quad remesher akan menggunakannya sebagai panduan untuk aliran tepi. Ketik pada laluan untuk memadamnya. 
* `Rekt` - Lukis segi empat pada permukaan arca; quad remesher akan menggunakannya sebagai panduan untuk aliran tepi. Ketik pada laluan untuk memadamnya.
* `Elips` - Lukis elips pada permukaan arca; quad remesher akan menggunakannya sebagai panduan untuk aliran tepi. Ketik pada laluan untuk memadamnya.

#### Bar alat atas Quad Remesher {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

Satu bar alat akan muncul di bahagian atas port pandangan dengan kawalan tambahan:


* `<Count>` - Klik ini untuk memulakan proses quad remesher; nombor ini memberitahu anda bilangan segi empat sasaran.
* `Segi empat` - Tetapkan bilangan segi empat sasaran dengan menggelongsor ke kiri dan kanan, atau ketik untuk menetapkan nombor tepat. Ambil perhatian bahawa ini lebih kepada panduan daripada nombor tetap; pelbagai kawalan pada quad remesher selalunya bermakna hasilnya tidak akan tepat sepadan dengan sasaran ini.
* `Separuh` - Pintasan untuk menetapkan bilangan sasaran kepada separuh bilangan poligon semasa.
* `Sama` - Pintasan untuk menetapkan bilangan sasaran kepada bilangan poligon semasa.
* `Panduan` - togol untuk menggunakan atau mengabaikan panduan. Apabila terdapat panduan, butang `Panduan` kedua memaparkan bilangannya; ketik untuk memadam semuanya.
* `Kepadatan` - togol untuk menggunakan atau mengabaikan lukisan ketumpatan. Apabila terdapat lukisan ketumpatan, butang `Kepadatan` kedua membuangnya.
* `Kumpulan muka` - togol untuk menggunakan atau mengabaikan kumpulan muka untuk memandu quad remesher.
* `Santai` - togol untuk melonggarkan sempadan kumpulan muka secara automatik semasa quad remesh. Jika anda sudah melonggarkan/melicinkan sempadan kumpulan muka anda, matikan pilihan ini.
* `Gelangsar Santai` - Gelangsar pintasan untuk melonggarkan sempadan kumpulan muka.
* `Tepi keras` - togol untuk cuba mengekalkan tepi keras.
* `Reprojek Vertex` - togol untuk mengunjurkan semula susun atur baharu ke mesh input.
* `Sim` - Togol untuk mengaktifkan hasil yang simetri. Ambil perhatian bahawa simetri sentiasa dikira mengelilingi paksi-x dunia, jadi pastikan model anda berada di asalan jika anda mengharapkan hasil yang simetri.
* `...` - Tetingkap timbul tetapan Quad Remesher. 

#### Menu tetapan Quad Remesher {#quad-remesher-settings-menu}

Butang `...` di hujung bar alat atas membuka tetingkap timbul dengan tetapan selebihnya:

* `Kiraan Kuad Adaptif` - togol untuk menggunakan segi empat yang lebih kecil di kawasan berkelengkungan tinggi, dan segi empat yang lebih besar di kawasan berkelengkungan rendah.
* `Saiz Adaptif` - Tetapkan tahap penyesuaian. 100% membenarkan saiz adaptif maksimum; pada 0% segi empat akan seragam.

::: tip

Resipi untuk mendapatkan quad remesh yang baik dengan artifak yang minimum:

* Bahagikan mesh kepada kumpulan muka untuk menentukan aliran segi empat yang ideal.
* Santaikan kumpulan muka untuk mendapatkan sempadan kumpulan muka yang licin.
* Kurangkan. Ini memastikan tiada muka yang nipis atau herot pada tepi kumpulan muka. Dalam tetapan Kurangkan, pastikan kumpulan muka diaktifkan. Ini akan membuat tepi segi tiga mengikut tepi kumpulan muka anda dengan tepat. 

Dalam pilihan quad remesh, pastikan santai dimatikan (kerana anda sudah melonggarkan mesh) dan anda sepatutnya mendapat hasil yang baik.

:::

### ![](/icons/tool_select.webp) Pilih {#select}
Gunakan mod bentuk (`Laso`, `Rekt`, `Elips`) untuk memilih objek dalam adegan. `Nyahpilih` akan membuang objek daripada pemilihan.

### ![](/icons/tool_lattice.webp) Lattice {#lattice}
Ubah bentuk objek dengan sangkar titik kawalan di sekelilingnya, dan bukannya mengukir permukaannya. Menggerakkan beberapa titik sangkar akan membengkok, memulas atau meregangkan keseluruhan objek dengan lancar, sangat sesuai untuk melaraskan perkadaran atau memberi pose tanpa menyentuh topologi. Ubah bentuk kekal hidup sehingga anda memuktamadkannya.

Bar alat kiri memilih cara anda menyunting sangkar:

* `Titik` - Seret titik dan tepi sangkar secara terus. Ketik satu titik untuk memilihnya.
* `Lihat` - Gerakkan kamera tanpa menyunting sangkar.
* `Santai` - Berus yang melonggarkan titik sangkar di bawahnya.
* `Elastik` - Berus yang menarik titik sangkar dengan pengurangan elastik, seperti alat [Elastik](#elastic).
* `Gizmo` - Gerak, putar dan skala titik yang dipilih dengan gizmo. Mod subnya ialah `Paksi`.
* `Laso` - Pilih titik sangkar dengan laso; `Nyahpilih` membuangnya daripada pemilihan.

Tetingkap timbul bentuk juga mempunyai `Jejari lembut`, yang membolehkan seretan titik turut menggerakkan titik jiran (dalam sel grid; 0 hanya menggerakkan pemilihan), dan `Terbalikkan pemilihan`.

Satu bar alat di bahagian atas port pandangan mempunyai:

* `Muktamadkan` - Kenakan ubah bentuk pada objek dan buang sangkar.
* `Tetapkan semula` - Buang sangkar dan ubah bentuknya.
* `Kelegapan` - Kelegapan paparan sangkar.
* `Bahagian cermin` - Dengan simetri, bertukar antara bahagian cermin sangkar yang dipaparkan dan boleh dipilih, dengan `Kelegapan` tersendiri untuk bahagian yang tersembunyi.
* `Titik grid` - Titik sangkar mana yang boleh digerakkan: grid penuh, permukaan dan titik tengah, atau permukaan sahaja.
* `Kekakuan` - Sejauh mana ubah bentuk itu kaku, daripada licin (0%) hingga tegar dan linear (100%).
* `Falloff` - Sejauh mana ubah bentuk pudar di luar sangkar.
* `Selaras` - Jajarkan sangkar dengan objek, atau dengan dunia.
* `X`, `Y`, `Z` `Pembahagian` - Bilangan sel sangkar pada setiap paksi. Butang mod di sebelahnya menetapkan hubungan antara mereka: `x = y = z` menggunakan bilangan yang sama pada 3 paksi, `Seragam` mengekalkan jarak yang sama antara titik pada setiap paksi, dan `Tersuai` membolehkan anda menetapkan setiap paksi dengan bebas.

#### Tetapan Lattice {#lattice-settings}
* `Kelajuan putaran` - Pilihan putaran yang sama seperti alat [Alih](#move-settings), digunakan semasa menyeret titik sangkar.

### ![](/icons/tool_view.webp) Lihat {#view}
"Alat" ini tidak melakukan apa-apa yang khusus; ia hanyalah cara untuk melihat model tanpa mengubah adegan anda.

#### Tetapan Lihat {#view-settings}
Semasa alat Lihat aktif, tetapan ini mengatasi beberapa pilihan paparan, supaya anda mendapat pandangan yang bersih untuk membentang atau memeriksa model anda:

* `Primitif (Sunting)`, `Pengulang (Sunting)`, `Cahaya (Sunting)`, `Kamera (Sunting)` - Benarkan penyuntingan primitif, pengulang, lampu dan kamera dalam port pandangan semasa dalam alat Lihat. Matikannya untuk mengelakkan pemegangnya tergerak secara tidak sengaja.
* `Jalan pintas Kamera (sentiasa)` - Sentiasa paparkan butang pintasan kamera pada port pandangan.
* `Tunjukkan topeng`, `Garis luar`, `Gelapkan objek yang tidak dipilih` - Paparkan topeng, garis luar objek yang dipilih, atau gelapkan objek yang tidak dipilih. `Auto` mengikut tetapan biasa anda, `Tidak` dan `Ya` memaksanya.
* `Tunjukkan garis (Simetri)`, `Tunjukkan satah (Simetri)` - Paparkan garis atau satah simetri, dengan pilihan `Auto`, `Tidak` dan `Ya` yang sama.
* `Ikon` - Paparkan ikon kumpulan, pengulang, lampu, kamera dan hierarki dalam port pandangan, dengan pilihan yang sama.


## Menu konteks kotak alat {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Klik kanan atau tekan lama pada satu alat dalam kotak alat akan membuka menu konteks. Menu ini mempunyai pilihan berikut:

* `Simpan` - simpan sebarang perubahan yang anda buat pada alat
* `Klona` - duplikasikan alat menjadi pintasan alat baharu
* `Simpanan terakhir` - kembali ke versi alat yang disimpan sebelum ini
* `Ikon` - tukar ikon alat. Apabila alat mempunyai ikon tersuai, butang ini membuangnya.
* `→ ...` - pindahkan alat ke folder lain dalam kotak alat, atau ke folder baharu
* `Tetapkan semula` - tetapkan semula alat kepada nilai lalainya

Alat yang diklon juga mempunyai `Namakan semula` dan `Padam`.
