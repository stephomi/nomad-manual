# ![](/icons/toolbox.webp) Alat

![](/images/tools_menu.webp)

::: tip
Lompat ke bawah ke [Alat](#tools-1) untuk penerangan setiap alat.
:::

## Gambaran keseluruhan

Alat dipilih daripada `Toolbox` di sebelah kanan, dan dikawal dengan `Tool Controls` di sebelah kiri. Tetapan tambahan boleh ditemui dalam menu `Settings`, ikon pertama di menu kanan-atas.

Alat berus mempunyai kawalan untuk saiz dan intensiti. Alat pemilihan mempunyai kawalan untuk beberapa gaya pemilihan. Bahagian bawah kawalan alat mempunyai pintasan untuk operasi yang kerap digunakan (Smooth, Mask, Hide, Gizmo, Color, Alpha).

Alat Nomad dikodkan warna dalam toolbox:

* <span class=brush>**Alat berus**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**Alat gerak**</span> (Move, Drag)
* <span class=mask>**Alat mask**</span> (Mask, SelMask)
* <span class=paint>**Alat lukis**</span> (Paint, Smudge)
* <span class=flatten>**Alat ratakan**</span> (Flatten, Planar)
* <span class=pinch>**Alat pinch**</span> (Crease, Pinch)
* <span class=selection>**Alat berasaskan pemilihan**</span> di mana topeng 2D dilukis dahulu, kemudian operasi dijalankan (Trim, Split, Project)
* <span class=creation>**Alat ciptaan**</span> (Tube, Lathe, Insert)
* <span class=transform>**Alat transformasi**</span> (Transform, Gizmo)
* <span class=misc>**Alat pelbagai**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**Alat pandangan**</span>



Banyak alat ini boleh disesuaikan dengan kelakuan berus, tekanan, tekstur dan lain-lain melalui menu [Stroke](stroke.md). 


### Kawalan berus

Toolbar kiri mempunyai peluncur untuk radius dan intensiti, dan kemudian kawalan khusus kategori alat, diterangkan di bawah.

![](/images/tool_left_panel.webp)

::: tip
Peluncur intensiti untuk banyak alat boleh melebihi 100%, berbaloi untuk dicuba!
:::

### Sub mode
Butang betul-betul di bawah peluncur intensiti ialah butang `Sub`. Label dan fungsinya akan berubah mengikut alat, dan apabila ditekan akan memanggil kelakuan alternatif, biasanya bertentangan. Contohnya untuk [Paint](#paint) ia akan memanggil mod Padam, untuk [Crease](#crease) ia akan mencipta tepi timbul dan bukannya lekuk dan sebagainya.

Secara lalai ia berfungsi sebagai butang “sticky”; iaitu anda boleh menekannya dan menahan untuk mengaktifkannya sementara, apabila anda lepaskan ia akan dimatikan. Jika anda mengetik, sub mode akan diaktifkan secara kekal.

### Pintasan
Di bahagian bawah toolbar kiri terdapat pintasan untuk [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Secara lalai semuanya berfungsi sebagai butang “sticky”; iaitu anda boleh menekannya dan menahan untuk mengaktifkannya sementara, apabila anda lepaskan ia akan dimatikan. Jika anda mengetik, mod pintasan itu akan diaktifkan secara kekal.

### Kawalan pemilihan

Alat [Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup) dan [Hide](#hide) semuanya menggunakan kawalan yang serupa untuk memilih kawasan pada mesh.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - Bentuk lukisan bebas
* `Polygon` - Bentuk tertutup yang ditakrifkan oleh gabungan lengkung dan/atau garisan lurus. Lihat [Shape editing](#shape-editing) di bawah untuk maklumat lanjut.
* `Curve` - (Project sahaja) - Lengkung lukisan bebas untuk projek
* `Path` - (Project sahaja) - Lengkung yang ditakrifkan oleh titik. Lihat [Shape editing](#shape-editing) di bawah untuk maklumat lanjut.
* `Line` - Seret satu garisan untuk mentakrifkan segmen satah. Secara lalai ia akan beroperasi pada mesh serta-merta, matikan auto validate jika anda tidak mahu ini (tekan lama atau leret pada ikon garisan)
* `Rect` - Seret satu garisan pepenjuru, ini akan mentakrifkan bucu bentuk segi empat tepat. Tekan lama atau leret untuk mendedahkan pilihan untuk auto validate, paksa kepada bentuk segi empat sama, dan supaya klik pertama menjadi pusat segi empat tepat.
* `Ellipse` - Seret satu garisan pepenjuru, ini akan mentakrifkan saiz elips. Tekan lama atau leret untuk mendedahkan pilihan untuk auto validate, paksa kepada bentuk bulatan, dan supaya klik pertama menjadi pusat elips.
* `Flip` - songsangkan topeng bentuk, atau arah alat project.

Kebanyakan alat mempunyai pilihan auto validate, bermaksud operasi akan berlaku sebaik sahaja anda selesai melukis bentuk. Apabila auto validate dimatikan, satu butang hijau akan dilukis di sebelah bentuk yang akan melaksanakan operasi. Ini membolehkan anda mengedit bentuk, melaras pandangan, dan apabila anda bersedia untuk menggunakan bentuk itu, tekan butang hijau.

### Penyuntingan bentuk
Penyuntingan poligon dan penyuntingan lengkung berkelakuan dengan cara yang serupa:

* Untuk bermula, seret satu garisan untuk mentakrifkan 2 titik, kemudian seret keluar dari tengah garisan untuk mentakrifkan poligon atau lengkung.
* Klik pada titik untuk tukar antara licin dan tajam. 
* Klik dan seret pada bahagian lengkung atau garisan untuk mencipta titik baharu.
* Untuk memadam titik, seret satu titik ke jirannya sehingga ia bertukar merah.
* Ikon tong sampah di penjuru ikon poligon atau path akan memadam bentuk.

### Menu Settings

Banyak alat mempunyai tetapan tambahan yang ditemui dalam menu settings, ikon pertama di menu kanan-atas:

![](/images/tools_settings_menu.webp)

## Alat

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Clay
Alat Clay berguna untuk membina arca anda. `Sub` akan membuang material daripada arca anda.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Brush
Berus piawai. `Sub` akan membuang material.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Move
Kawasan di bawah berus akan melekat pada berus, membenarkan deformasi elastik. Pemilihan dikekalkan semasa gerakan, jadi jika anda mengalihkan berus jauh, kemudian mengembalikannya ke tempat asal, anda tidak akan melihat sebarang deformasi.

Sub mode ialah `Normal`, dan akan menggerakkan kawasan di bawah berus sepanjang normal permukaan.

Berus ini bagus untuk deformasi skala besar dan juga deformasi kecil yang teliti.

#### Tetapan Move

* `Radius (Background)` - Sejauh mana dari tepi model anda boleh berada dan masih boleh mengukir, berguna apabila bekerja pada siluet objek. 
* `Same-side vertex only` - Abaikan verteks yang menghala ke arah bertentangan dengan deformasi.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Drag
Kawasan di bawah berus akan melekat pada berus, membenarkan deformasi elastik. Tidak seperti berus move, pemilihan dikemas kini secara berterusan semasa stroke, jadi adalah mungkin untuk membuat objek panjang seperti ular, terutamanya apabila Dynamic Topology diaktifkan.

Sub mode ialah `Normal`, dan akan menggerakkan kawasan di bawah berus sepanjang normal permukaan.

Berus ini bagus untuk perubahan bentuk yang lebih longgar dan gestural.

#### Tetapan Drag

* `Radius (Background)` - Sejauh mana dari tepi model anda boleh berada dan masih boleh mengukir, berguna apabila bekerja pada siluet objek. 
* `Same-side vertex only` - Abaikan verteks yang menghala ke arah bertentangan dengan deformasi.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Smooth
Lembutkan kawasan dengan mempuratakan kedudukan titik. Alat ini sangat bergantung pada ketumpatan poligon.
Jadi jika anda mempunyai banyak poligon, pelicinan akan kurang berkesan.

Sub mode ialah `Relax`, yang hanya melicinkan wireframe tetapi cuba mengekalkan butiran geometri.

#### Tetapan Smooth

![](/images/tool_smooth_settings.webp)

##### Facegroup

* `Relax` - Akan melicinkan sempadan facegroup. Gunakan intensiti lebih besar daripada 100% untuk melicinkan sempadan dengan cepat. `Auto` akan melicinkan hanya jika pratonton facegroup diaktifkan, `Off` akan mematikan, `On` akan menghidupkan. 

##### Vertex
* `Sticky vertex on border` - Untuk mesh dengan tepi terbuka, contohnya satah, adalah mungkin untuk melicinkan bucu. Mengaktifkan pilihan ini akan mengunci tepi terbuka.
* `Relax` - sama seperti mod alternatif relax di toolbar kiri.
* `Stable smoothing` - Cuba menjadikan pelicinan bebas topologi. Ini berfungsi paling baik dengan ketumpatan topologi yang berubah-ubah dan dengan nilai intensiti pelicinan yang tinggi.

##### Painting
* `Screen Smoothing` - Gunakan pilihan ini untuk mendapatkan pelicinan bebas topologi, walaupun pada kiraan poligon tinggi.
* `Screen samples` - Kualiti pelicinan, nombor lebih tinggi akan lebih licin, tetapi lebih perlahan.

::: tip
Ketumpatan poligon yang lebih tinggi mungkin memerlukan peningkatan intensiti melebihi 100%. Nilai yang sangat tinggi (300%, 500%) juga boleh berfungsi dengan baik sebagai alat mengukir, memaksa kawasan menjadi rata dan licin dengan cepat di bawah berus, seperti memukul tanah liat dengan pengetuk!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Mask
Alat ini membolehkan anda memask verteks. Verteks yang dimask dilindungi daripada sculpting atau painting. 

Sub mode ialah `Unmask`, dan akan memadam di mana mask telah dilukis.

Serupa dengan pemilihan dalam program lukisan 2D, mask boleh dilukis dengan berus, atau dibuat dengan pemilihan bentuk, dikaburkan atau ditajamkan. 

Tidak seperti program lukisan 2D, ia juga boleh dibuat melalui facegroup, dan mask boleh digunakan untuk mencipta geometri baharu melalui operasi gaya extrusion/extraction. 

![](/videos/tool_mask1.mp4)

 Satu toolbar akan muncul di bahagian atas viewport dengan kawalan tambahan. 

![](/images/tool_mask_toolbar.webp)

Tajuk bar boleh diketuk untuk kembang/kuncup, atau anak panah di kanan-atas boleh diketuk untuk memindahkannya ke bahagian atas atau bawah UI.

| Action                                             | Description                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/cross_circle2.webp) Clear              | Kosongkan mask                                                                             |
| ![](/icons/invert.webp)        Invert             | Songsangkan mask                                                                           |
| ![](/icons/sharpen.webp)       Sharpen            | Tajamkan tepi mask                                                                         |
| ![](/icons/blur.webp)          Blur               | Kaburkan tepi mask                                                                         |
|                                 Blur ->            | Seret kiri/kanan untuk mengaburkan mask secara interaktif                                  |
| ![](/icons/culling.webp)       Front              | Togol untuk hanya memask verteks yang menghadap ke hadapan                                |
|                                 Convert            | Tukar mask kepada facegroup                                                               |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | Apabila diaktifkan facegroup akan dipaparkan, mengetik facegroup akan memaskkannya        |
|                                 On tap (mask)      | Apabila diaktifkan, mengetik 'pulau' mask atau poligon tidak dimask akan flood fill pulau itu. |
| ![](/icons/vertex.webp)        Connected          | Apabila diaktifkan hanya benarkan stroke mask menjejaskan topologi yang bersambung.       |

##### Gerak isyarat pantas Mask
Anda boleh melakukan gerak isyarat gaya ZBrush sambil menahan butang quick masking di toolbar kiri:
| Action  | Gesture (hold lower-left shortcut) |
| :-----: | :--------------------------------: |
| Invert  | Ketik pada latar belakang          |
| Clear   | Seret pada latar belakang          |
| Blur    | Ketik pada kawasan dimask          |
| Sharpen | Ketik pada kawasan tidak dimask    |


#### Tetapan Mask
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - Menu tetapan Mask terutamanya digunakan untuk mencipta geometri daripada mask. Oleh itu kelakuan lalai ialah mempratonton rupa geometri baharu. Anda boleh memilih untuk tiada pratonton, pratonton extract, pratonton split, dan sama ada geometri ini akan dipaparkan dalam mod x-ray.

##### Thickness
* `Height` - Ketinggian bentuk yang diekstrak. Ikon Plus/Minus membolehkan anda mengitar antara extrusion ke luar, ke dalam, atau berpusat. 
* `Height/Height+Mask` - Togol antara ketinggian kekal malar, atau jika bahagian mask yang dikaburkan patut menjejaskan ketinggian, membolehkan bentuk lembut dan ketinggian berubah-ubah. 

##### Smoothness
Apabila aktif, akan melicinkan sempadan bentuk yang diekstrak, ia berfungsi lebih baik dengan kiraan poligon yang lebih tinggi. 
* `Iterations` - Jumlah pelicinan yang digunakan. Nilai tinggi akan menghasilkan tepi melengkung yang sangat licin, tetapi akan mula menyimpang daripada bentuk mask.
* `All/Sharp border/Borders only` - Pelicinan boleh berfungsi dalam semua arah, melicinkan sisi dan bahagian atas bentuk yang diekstrak, atau melicinkan bahagian atas dan sisi tetapi mengekalkan tepi tajam, atau hanya melicinkan sempadan, meninggalkan permukaan atas tidak terjejas.

##### Edge loop (side)
* `Auto Edge-loop (side)` - Akan mengira jumlah pembahagian pada sisi bentuk yang diekstrak untuk menghasilkan poligon segi empat sama yang sepadan dengan poligon kawasan dimask. Apabila dimatikan, anda boleh menetapkan bilangan edge loop sendiri dengan peluncur edge loop.

----

##### Extract
* `Extract` - Cipta geometri yang diekstrak.
* `Closing action` - Cara extract patut berkelakuan. 'None' akan menduplikasi poligon dimask ke bentuk baharu. 'Fill' akan melakukan perkara yang sama, dan cuba menampal permukaan belakang. 'Shell' akan mengekstrak ke jumlah yang ditetapkan dalam 'thickness', dan ini ialah lalai.

::: tip

Jika preview berada dalam mod 'Extract' dengan 'X-ray' diaktifkan, mengklik butang Extract boleh mengelirukan pada mulanya. Oleh kerana menu aktif, ia akan cuba mempratonton extraction pada bentuk baharu anda, dan xray permukaan asal. Namun kerana tiada mask pada permukaan baharu, ia tidak boleh mempratonton extraction, dan Nomad akan memberi amaran 'Nothing to Extract!'. 

Ini adalah normal, tutup menu tetapan mask untuk melihat bentuk baharu dan yang asal, dan pilih semula permukaan asal jika anda perlu mengosongkan mask atau melukis mask baharu.
:::

##### Split
* `Split` - Akan mengekstrak kedua-dua kawasan dimask DAN tidak dimask ke bentuk baharu. 
* `Closing action (masked)` - Cara extract mask patut berkelakuan. 'None' akan menduplikasi poligon dimask ke bentuk baharu. 'Fill' akan melakukan perkara yang sama, dan cuba menampal permukaan belakang. 'Shell' akan mengekstrak ke jumlah yang ditetapkan dalam 'thickness', dan ini ialah lalai.
* `Closing action (unmasked)` - Cara extract tidak dimask patut berkelakuan. 'None' akan menduplikasi poligon dimask ke bentuk baharu. 'Fill' akan melakukan perkara yang sama, dan cuba menampal permukaan belakang. 'Shell' akan mengekstrak ke jumlah yang ditetapkan dalam 'thickness', dan ini ialah lalai.
* `Sync border` - Pastikan sempadan antara bentuk dimask dan tidak dimask yang diekstrak kekal rapat. Apabila dimatikan, kerana operasi shell akan mengekstrak setiap muka sepanjang normalnya, jurang boleh terbentuk antara bentuk.

##### Carve
* `Carve` - Dalam mod lalai, berkelakuan seolah-olah anda telah men-trim ke dalam permukaan mengikut jumlah 'thickness', seperti memotong sepotong kulit oren. 



### ![](/icons/tool_maskSelector.webp) Selection Mask
Alat ini kebanyakannya serupa dengan [alat Masking](#mask), perbezaan utama ialah anda tidak menggunakan stroke untuk melukis mask, tetapi sebaliknya menggunakan [Selection Controls](#selection-controls).

Sub mode ialah `Unmask`, dan akan memadam mask menggunakan kawalan pemilihan.

Selection mask berkongsi tetapan alat yang sama seperti alat `Mask`.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Paint
Sapukan warna dan sifat material. Untuk mengetahui lebih lanjut tentang material anda boleh lawati bahagian [Painting](painting.md).

Sub mode ialah `Erase` dan akan membuang cat.

#### Tetapan Paint
* `Layer fitering` - Ini berfungsi seperti layer alpha lock dalam Photoshop atau Procreate. Jika anda melukis pada layer, apabila ini diaktifkan, anda hanya boleh mengubah di mana cat sudah wujud; kawasan tidak dicat akan dilindungi.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Smudge
Smudge warna dan sifat material. Menu tetapan smudge mengandungi peluncur `Quality`, nilai lebih rendah bermakna stroke lebih pantas.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Flatten
Ratakan kawasan dengan memproyeksikan titik ke satah purata.

Sub mode ialah `Fill` dan akan mentakrifkan satah yang ditetapkan oleh titik tertinggi, dan cenderung menarik titik ke atas.

#### Tetapan Flatten

* `Lock plane direction` - Gunakan arah satah yang dikira pada klik pertama. Secara lalai ini dimatikan.
* `Lock plane origin`- Gunakan klik pertama sebagai pusat satah. Secara lalai ini dimatikan.

Apabila salah satu atau kedua-duanya dimatikan, flatten boleh diperdalam secara beransur-ansur atau sudut satah diubah dengan menggunakan stroke panjang yang bergerak merentasi kedalaman dan kelengkungan berbeza. Ini bersama-sama dengan pilihan pensampelan kawasan dalam menu berus boleh menawarkan kawalan yang sangat tepat.

::: tip
Apabila bekerja di kawasan kelengkungan tinggi, contohnya cuba meratakan pipi tetapi alat sentiasa menjejaskan sisi hidung, cuba cipta mask untuk melindungi kawasan yang tidak patut disentuh berus flatten.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar
Menjadikan titik planar dengan memproyeksikan ke satah purata, tetapi dengan penimbunan kurang daripada berus flatten. Ini menghasilkan permukaan tepi keras yang lebih bersih. Stroke pantas akan menolak dan menarik permukaan lebih banyak, stroke perlahan yang bermula dari kawasan yang sudah planar dan bergerak keluar akan mengekalkan satah dengan lebih baik.

Sub mode ialah `Fill` dan akan mentakrifkan satah yang ditetapkan oleh titik tertinggi, dan cenderung menarik titik ke atas.

Planar sebenarnya alat yang sama seperti `Flatten`, tetapi dengan `Lock plane direction` diaktifkan, bermakna ia akan cenderung menghasilkan permukaan tepi keras yang lebih stabil, manakala flatten boleh lebih bersifat sculptural dan digunakan untuk mencipta kawasan separa rata.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Crease
Alat Crease berguna untuk mengukir potongan kecil atau lekuk.

Sub mode ialah `Invert`, dan akan mencipta crease timbul.

#### Tetapan Crease

* `Pinch factor` - Berapa banyak untuk menarik verteks ke sisi ke arah stroke berus. Jika pinch pada 1, dan offset pada 0, permukaan tidak akan mempunyai sebarang perubahan kedalaman, hanya perubahan topologi, menarik tepi ke arah stroke.
* `Offset factor` - Berapa banyak untuk menolak/tarik verteks dalam kedalaman. Jika pinch pada 0, dan offset pada 1, crease dalam atau lekuk timbul akan dibuat, tetapi akan kelihatan bergerigi kerana tidak cukup geo ditarik ke arah crease untuk mentakrifkan sisi atau dasar crease dengan tepat.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Pinch
Alat ini boleh digunakan untuk menajamkan tepi.

Sub mode ialah `Invert` dan akan menjarakkan verteks.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Trim
Alat Trim berfungsi dengan membuang sebahagian mesh anda, dan memberikan pilihan cara memproses jurang yang ditinggalkan. Ia menggunakan [Selection controls](#selection-controls) untuk mentakrifkan trim.

::: tip
Oleh kerana alat ini memproyeksikan dari kamera, anda akan mendapat amaran jika kamera berada dalam mod perspektif.

Dalam mod ortografik potongan yang dibuat melalui mesh adalah selari dengan pandangan, yang biasanya dijangka. Apabila dilakukan dengan kamera perspektif, potongan akan kelihatan berbeza di bahagian jauh objek berbanding bahagian dekat.
:::

#### Tetapan Trim

* `Stroke painting` - Jika painting diaktifkan dalam menu paint, kawasan yang ditampal akan diisi dengan warna semasa.
* `Boolean` - isi lubang trim menggunakan kawasan poligon quad. Kawasan yang diisi akan rata.
* `Legacy` - isi lubang trim dengan kawasan bertiga. Kawasan yang diisi akan rata.
* `Fill` - isi lubang dengan kawasan bertiga. Kawasan yang diisi akan menjadi permukaan melengkung, seperti filem buih sabun.
* `None` - jangan isi lubang.
* `Boolean Detail Shape` - Saiz anggaran quad dan segi tiga yang digunakan pada bahagian bentuk trim.
* `Boolean Detail Hole` - Saiz anggaran segi tiga atau poligon yang digunakan pada lubang trim yang diisi. 
* `Legacy Detail` - Saiz anggaran segi tiga yang digunakan pada trim.
* `Legacy Hole smoothing` - Berapa banyak segi tiga dilonggarkan pada kawasan yang diisi.
* `Legacy Threshold espilon` - Nilai yang boleh dilaras untuk menambah baik algoritma pengisian lubang legacy.
* `Fill Detail` - Saiz anggaran segi tiga yang digunakan pada trim.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Split
Serupa dengan alat [Trim](#trim), kecuali Trim membuang pemilihan, Split akan mengekalkan pemilihan sebagai objek baharu.

#### Tetapan Split

* `Stroke painting` - Jika painting diaktifkan dalam menu paint, kawasan yang ditampal akan diisi dengan warna semasa.
* `Boolean` - isi lubang split menggunakan kawasan poligon quad. Kawasan yang diisi akan rata.
* `Legacy` - isi lubang split dengan kawasan bertiga. Kawasan yang diisi akan rata.
* `Fill` - isi lubang dengan kawasan bertiga. Kawasan yang diisi akan menjadi permukaan melengkung, seperti filem buih sabun.
* `None` - jangan isi lubang.
* `Boolean Detail Shape` - Saiz anggaran quad dan segi tiga yang digunakan pada bahagian bentuk split.
* `Boolean Detail Hole` - Saiz anggaran segi tiga atau poligon yang digunakan pada lubang split yang diisi. 
* `Legacy Detail` - Saiz anggaran segi tiga yang digunakan pada split.
* `Legacy Hole smoothing` - Berapa banyak segi tiga dilonggarkan pada kawasan yang diisi.
* `Legacy Threshold espilon` - Nilai yang boleh dilaras untuk menambah baik algoritma pengisian lubang legacy.
* `Fill Detail` - Saiz anggaran segi tiga yang digunakan pada split.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Project
Alat Project kelihatan seperti alat [Trim](#trim), tetapi ia tidak memadam atau mencipta sebarang geometri, ia hanya menggerakkan verteks supaya mengikut pemilihan.

![](/videos/tool_project.mp4)

::: tip
Jika anda menggunakan Project semasa berada dalam layer, anda boleh mengadun antara bentuk asal dan bentuk yang diprojek dengan peluncur layer.
:::

### ![](/icons/tool_layer.webp) Layer
Naikkan permukaan, tetapi hadkan ketinggian.

Jika anda terus menekan pensel dan terus berus di atas kawasan, Layer akan naik ke ketinggian tertentu kemudian tidak akan naik lagi, berbanding alat lain yang akan terus mengumpul ketinggian.

Perhatikan bahawa secara lalai had hanya ditetapkan setiap stroke! Jika anda memulakan stroke baharu, ia akan membina dari ketinggian permukaan baharu.

Untuk menetapkan ketinggian maksimum malar merentasi banyak stroke, gunakan alat Layer dengan sistem [Layers](layers.md) Nomad.

Cipta satu layer, dan gunakan alat ini. Ketinggian maksimum kini ditetapkan daripada layer, jadi anda boleh menggunakan banyak stroke berus dan ketinggian akan sentiasa sama.

`Sub` akan menggunakan kedalaman minimum, mencipta alur.

#### Tetapan Layer

* `Use layer data` - Apabila aktif, dan apabila layer dipilih, gunakan data layer untuk menetapkan ketinggian maksimum.
* `Inflate`- Apabila aktif laraskan arah kerja layer untuk mendapatkan hasil yang lebih licin.
* `Relax (Normal)` - Jumlah pelicinan yang digunakan pada normal.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Inflate
Gerakkan verteks sepanjang normal masing-masing. `Sub` akan menggerakkan verteks sepanjang normal songsang.

#### Tetapan Inflate
* `Relax (Normal)` - Jumlah pelicinan yang digunakan pada normal.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Nudge
Gerakkan atau 'smear' titik mengikut arah stroke.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stamp

Klik dan seret untuk menaikkan kawasan arca mengikut bentuk Alpha terpilih.

Ini hanyalah [alat Brush](#brush) dengan jenis stroke ditetapkan kepada `Lock + radius`. 

`Sub` akan menolak stamp ke dalam dan bukannya menariknya keluar dari permukaan.

::: tip
Stamp biasanya berfungsi paling baik dengan geometri resolusi tinggi. Jika anda mencari dalam talian 'wrinkles alpha', 'pores alpha', 'scales alpha' dan sebagainya, tekstur alpha ini dan Stamp boleh menjadi cara yang hebat untuk menambah butiran organik pada arca watak.

Dua mod stroke berguna untuk perkara berbeza. 

* `Lock + radius` mempunyai *ketinggian* tetap, seretan melaras lebar dan putaran stamp. Bagus untuk tekstur kulit di mana ia perlu mempunyai kedalaman/ketinggian sama, tetapi putaran dan skala berbeza untuk menyembunyikan corak berulang.
* `Lock + intensity` mempunyai *lebar* tetap, seretan melaras putaran dan ketinggian stamp. Bagus untuk rivet, di mana semuanya perlu sama saiz, tetapi putaran dan ketinggian berbeza. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Delete Layer
Alat ini boleh menetapkan semula layer secara setempat, anda memerlukan layer aktif jika tidak tiada apa akan berlaku.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tube
Cipta tube dengan melukis satu lengkung. 
![](/images/tool_tube_new.webp)

Sebaik sahaja tube dicipta, path boleh diedit dalam ruang 3D menggunakan kawalan serupa dengan alat [Shape editing](#shape-editing) dan penyuntingan lengkung standard. 

![](/videos/tool_tube.mp4)

#### Toolbar kiri Tube

![](/images/tool_tube_left_toolbar.webp)

Toolbar kiri mempunyai pilihan berikut:

* `Sync` - Jika tube semasa di-instance, dan terdapat nod anak tube yang berbeza antara instance, ini akan menyelaraskannya semula.
* `Snap` - Apabila aktif, mod curve dan path akan snap ke objek lain semasa anda melukis. Apabila tidak aktif, titik pertama akan snap, kemudian selebihnya tube akan dilukis pada kedalaman itu. Ia mempunyai menu kecil:
    * `Offset` - Tetapkan kedalaman snap; 0% akan menyebabkan tengah keratan rentas tube snap ke permukaan, nilai positif akan mengangkatnya dari permukaan, nilai negatif akan menurunkannya.
* `Curve` - Lakarkan tube secara bebas. Ia mempunyai menu kecil:
    * `Auto-validate` - Akan mencipta tube sebaik sahaja stroke selesai. Apabila dimatikan, bulatan hijau validate akan kelihatan di sebelah path lengkung, tekan untuk validate, atau gunakan pautan `Reset` yang muncul dalam menu ini untuk membuang path.
    * `Closed` - jadikan tube satu gelung.
    * `Screen` - Hanya tersedia apabila Auto-validate dimatikan. Apabila aktif, path 'dipin' ke skrin, membolehkan anda menggerakkan pandangan dan objek, dan path kekal di tempat. Apabila tidak aktif, path adalah sebahagian daripada adegan 3D, dan ia akan bergerak dengan kamera dan objek.
    * `Accuracy` - Berapa banyak titik lengkung akan digunakan untuk menukar path yang dilukis menjadi tube. 0% akan menggunakan bilangan titik paling rendah, tetapi akan terlepas perubahan kelengkungan kecil. 100% akan sangat tepat, dan menggunakan banyak titik.
* `Path` - Cipta tube dengan mengklik untuk mentakrifkan titik lengkung. Ketik bulatan hijau untuk validate path. Ia mempunyai menu kecil:
    * `B-spline` - Kaedah lukisan lengkung alternatif di mana titik lengkung biasanya tidak terletak terus pada lengkung, tetapi boleh menghasilkan keputusan lebih licin daripada kaedah lalai.
    * `Closed` - jadikan tube satu gelung
    * `Screen` - Apabila aktif, path 'dipin' ke skrin, membolehkan anda menggerakkan pandangan dan objek, dan path kekal di tempat. Apabila tidak aktif, path adalah sebahagian daripada adegan 3D, dan ia akan bergerak dengan kamera dan objek.

##### Toolbar atas Tube
![](/images/tool_tube_toolbar.webp)
Apabila tube dipilih, toolbar akan muncul di bahagian atas viewport dengan kawalan tambahan. Klik tajuk toolbar untuk kuncup/kembang toolbar, dan klik anak panah di kanan-atas untuk memindahkan toolbar ke bahagian atas atau bawah viewport.

* `Validate` - bakar tube menjadi poligon biasa supaya ia boleh diukir.
* `Edit` - paparkan titik lengkung supaya ia boleh dimanipulasi
* `Mirror` - tambah mirror repeater sebagai parent kepada lengkung ini
* `Snap` - snap titik lengkung ke permukaan berdekatan
* `Closed` - Sambungkan permulaan dan penghujung lengkung untuk membentuk gelung
* `B-spline` - Togol antara interpolasi Catmull-rom dan B-spline.
* `Cap` - Kitar antara cap pada kedua-dua hujung tube, atau permulaan atau penghujung, atau tiada cap.
* `Hole` - Tambah ketebalan pada tube, menukarnya menjadi paip. Kitar antara mempunyai lubang di kedua-dua hujung, hanya di hujung, atau tiada lubang. 
* `Radius` - Kitar antara radius seragam, radius di permulaan dan penghujung, atau radius setiap titik lengkung. Ini diedit dengan pemegang oren pada lengkung.
* `Twist` - Kitar antara tiada twist, twist seragam, twist di permulaan dan penghujung, atau twist setiap titik lengkung. Ini diedit dengan pemegang merah jambu pada lengkung.
* `Profile` - Kitar antara tiada profil (jadi profil bulatan), profil seragam, profil di permulaan dan penghujung, atau profil setiap titik.
* `Profile edit` - Paparkan penyunting profil. Ini berfungsi serupa dengan alat [Shape editing](#shape-editing), boleh menyimpan dan memuat preset profil, dan mempunyai togol untuk membolehkan anda mengedit profil dalam ruang 3D.
* `Spiral` - Togol menu untuk menambah twist spiral pada tube. Menu ini mempunyai pilihan untuk `Twist Angle`, `Offset`, `Scale`, dan `Angle offset`.
* `X Divisions` - bilangan pembahagian di sekeliling tube, 4 pembahagian akan menghasilkan tube segi empat sama sebagai contoh. 
* `Constant density` - apabila aktif, akan mengekalkan poligon segi empat sama. apabila dimatikan, akan membenarkan anda menetapkan `Y divisions` sepanjang panjang tube.
* `...` - Menu tetapan Tube.

#### Togol padam titik lengkung

![](/images/tool_tube_delete_toggle.webp)

Di bawah toolbar terdapat togol padam titik lengkung. Apabila anda menyeret satu titik lengkung berhampiran titik lain, ia akan bertukar merah, menunjukkan bahawa jika anda lepaskan, titik itu akan dipadam. Jika anda melakukan suntingan kecil dan tidak mahu memadam titik, butang ini akan mematikan kelakuan padam titik.



#### Tetapan Tube
* `Primitive` - butang untuk membolehkan/nyahdayakan UV, atau untuk validate tube.
* `Post subdivision` - pintasan untuk menetapkan tahap multiresolution sebelum validate.
* `Linear subdivision` - pintasan untuk menetapkan tahap linear subdivision sebelum validate. 
* `Division X` - sama seperti X Divisions dalam toolbar.
* `Division Y` - sama seperti Y Divisions dalam toolbar.
* `Curve (Repeater)` - tukar tube menjadi [Curve Repeater](scene.md#curve)

::: tip
Divisions pada 4 dan Post subdivision pada 3 akan menghasilkan tube hujung bulat licin, bagus untuk cacing, ular, anggota badan.
:::


### ![](/icons/tool_lathe.webp) Lathe
Cipta permukaan putaran dengan melukis satu lengkung.

Alat ini bagus untuk bentuk seperti pasu, gelas wain.

![](/videos/tool_lathe.mp4)

#### Toolbar kiri Lathe

![](/images/tool_lathe_left_toolbar.webp)

Toolbar kiri mempunyai pilihan berikut:

* `Sync` - Jika lathe semasa di-instance, dan terdapat nod anak lathe yang berbeza antara instance, ini akan menyelaraskannya semula.
* `Fixed` - Apabila diaktifkan, pusat lathe adalah tetap dan dipaparkan pada skrin. Garisan pusat ini mempunyai titik edit yang boleh dilaraskan. Apabila dimatikan, pusat lathe akan dikemas kini secara dinamik untuk sepadan dengan permulaan dan penghujung lengkung yang dilukis.
* `Curve` - Lukis profil lathe dalam satu stroke. Ia mempunyai menu kecil:
    * `Auto-validate` - Apabila diaktifkan, lathe akan dicipta apabila pensel diangkat dari skrin. Apabila dimatikan, bulatan hijau di sebelah lengkung boleh ditekan untuk mencipta lathe. Lengkung boleh dipadam dengan butang `Reset`.
    * `Closed` - Sambungkan permulaan dan penghujung lengkung untuk membentuk gelung
    * `Screen` - Hanya tersedia apabila Auto-validate dimatikan. Apabila aktif, path 'dipin' ke skrin, membolehkan anda menggerakkan pandangan dan objek, dan path kekal di tempat. Apabila tidak aktif, path adalah sebahagian daripada adegan 3D, dan ia akan bergerak dengan kamera dan objek.
    * `Accuracy` - Berapa banyak titik lengkung akan digunakan untuk menukar path yang dilukis menjadi tube. 0% akan menggunakan bilangan titik paling rendah, tetapi akan terlepas perubahan kelengkungan kecil. 100% akan sangat tepat, dan menggunakan banyak titik.
* `Path` - Cipta lathe dengan mengklik untuk mentakrifkan titik lengkung. Ketik bulatan hijau untuk validate path. Ia mempunyai menu kecil:
    * `B-spline` - Kaedah lukisan lengkung alternatif di mana titik lengkung biasanya tidak terletak terus pada lengkung, tetapi boleh menghasilkan keputusan lebih licin daripada kaedah lalai.
    * `Closed` - jadikan tube satu gelung
    * `Screen` - Apabila aktif, path 'dipin' ke skrin, membolehkan anda menggerakkan pandangan dan objek, dan path kekal di tempat. Apabila tidak aktif, path adalah sebahagian daripada adegan 3D, dan ia akan bergerak dengan kamera dan objek.

#### Toolbar atas Lathe
![](/images/tool_lathe_top_toolbar.webp)

Apabila lathe dipilih, toolbar akan muncul di bahagian atas viewport dengan kawalan tambahan. Klik tajuk toolbar untuk kuncup/kembang toolbar, dan klik anak panah di kanan-atas untuk memindahkan toolbar ke bahagian atas atau bawah viewport.

* `Validate` - bakar lathe menjadi poligon biasa supaya ia boleh diukir.
* `Edit` - paparkan titik lengkung supaya ia boleh dimanipulasi
* `Mirror` - tambah mirror repeater sebagai parent kepada lathe ini
* `Snap` - snap titik lengkung ke permukaan berdekatan
* `Stable` - Apabila diaktifkan, profil lengkung akan diparentkan kepada garisan pusat lathe. Apabila dimatikan, garisan pusat boleh diedit dan tidak akan menggerakkan lengkung, membolehkan bentuk lebih kompleks.
* `Focus` - Akan memutar pandangan untuk melihat profil lengkung rata sempurna ke kamera.
* `Closed` - Sambungkan permulaan dan penghujung lengkung untuk membentuk gelung
* `Cap` - Jika Closed dimatikan, kitar antara cap pada kedua-dua hujung tube, atau permulaan atau penghujung, atau tiada cap.
* `Hole` - Tambah ketebalan pada lathe, menukarnya menjadi paip. Kitar antara mempunyai lubang di kedua-dua hujung, hanya di hujung, atau tiada lubang. 
* `B-spline` - Togol antara interpolasi Catmull-rom dan B-spline.
* `X Divisions` - bilangan pembahagian di sekeliling lathe, 4 pembahagian akan menghasilkan profil lathe segi empat sama sebagai contoh. 
* `Constant density` - apabila aktif, akan mengekalkan poligon segi empat sama. apabila dimatikan, akan membenarkan anda menetapkan `Y divisions` sepanjang panjang tube.
* `...` - Menu tetapan Lathe.

#### Tetapan Lathe
* `Primitive` - butang untuk membolehkan/nyahdayakan UV, atau untuk validate tube.
* `Post subdivision` - pintasan untuk menetapkan tahap multiresolution sebelum validate.
* `Linear subdivision` - pintasan untuk menetapkan tahap linear subdivision sebelum validate. 
* `Division X` - sama seperti X Divisions dalam toolbar.
* `Division Y` - sama seperti Y Divisions dalam toolbar.
* `Curve (Repeater)` - tukar profil lengkung menjadi [Curve Repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) Insert
Letakkan objek pada permukaan objek lain. Dari segi penggunaan ia serupa dengan alat stamp, tetapi untuk bentuk 3D penuh.

Jika anda memilih primitif dari toolbar kiri, klik-seret pada mana-mana permukaan akan meletakkan primitif di tempat anda klik, seretan akan menetapkan saiz. Sebaik sahaja anda selesai menyeret, Insert akan bertukar ke mod [Transform](#transform).

Dalam mod Instance, seretan akan mencipta dan meluncurkan instance baharu di atas permukaan. Saiz akan diduplikasi daripada bentuk pertama, dengan cara ini anda boleh meletakkan banyak instance objek bersaiz sama di atas permukaan lain.

Anda tidak perlu hanya insert primitif! Pilih *mana-mana* bentuk dalam outliner, jika Insert berada dalam mod Instance atau Clone, anda boleh menyeret salinan objek terpilih di atas mana-mana permukaan lain.

Jika objek mempunyai pivot tersuai, maka ia akan digunakan sebagai titik sauh. Lihat video di bawah.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transform
Alih/Putar/Skalakan model secara terus dengan 1 dan 2 jari, biasanya di atas permukaan objek lain.

Alat dikawal dengan toolbar kiri, dan mempunyai 5 butang:

* `Snap` - snap model ke permukaan lain
* `Group` - Jika objek terpilih mempunyai gabungan objek dan instance, ini membolehkan anda menentukan kelakuan alat.
* `Move` - Seretan satu jari akan menggerakkan objek. Apabila snap aktif, ini akan meluncurkan objek sepanjang permukaan di bawah jari anda.
* `Rotate` - Seretan satu jari akan memutar objek. Apabila snap aktif, akan memutar mengelilingi normal permukaan di bawah jari anda.
* `Scale` - Seretan satu jari akan menskalakan objek.

Transform boleh digunakan untuk mengendalikan 2 mod ini dengan cepat menggunakan 2 jari:

* Seret objek untuk meletakkannya. Hentikan pergerakan jari pertama anda, tetapi jangan angkat dari skrin.
* Sentuh jari kedua anda pada skrin sambil mengekalkan jari pertama. Apabila jari kedua diseret, objek akan diskalakan.
* Angkat jari kedua, dan terus seret jari pertama, objek akan berada dalam mod move semula.

Anda juga boleh menukar mod kedua dengan gerak isyarat ketikan jari kedua:

* Seret objek untuk meletakkannya, hentikan pergerakan, tetapi jangan angkat jari anda dari skrin.
* Ketik jari kedua anda sambil menahan jari pertama
* Alat ditukar ke mod rotation. Seret jari pertama anda untuk menetapkan putaran.
* Ketik jari kedua seperti sebelum ini, alat ditukar kembali ke mod move.

Ini memberikan aliran kerja pantas untuk mengklon objek di atas objek lain, contohnya batu di atas landskap. Perhatikan bahawa butang clone juga berada di toolbar kiri untuk akses mudah:

* Gunakan alat transform untuk menggerakkan batu ke tempatnya.
* Lepaskan, tekan butang clone
* Gerakkan batu ini, putar/skalakan seperti diperlukan
* Lepaskan, tekan butang clone
* Gerakkan batu ini, ulang.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo
Alat ini membolehkan anda menggerak, memutar dan menskalakan objek, dan mengubah pivot objek.

Pemegang viewport mempunyai ciri berikut:

* `Move` - Seret pada garisan+anak panah untuk menggerak pada X/Y/Z. Seret pada titik pic oren di tengah gizmo untuk terjemah bebas dalam ruang skrin. Klik pada petak merah, hijau, biru untuk terjemah pada satah X/Y/Z.
* `Rotate` - Seret pada bulatan merah/hijau/biru untuk memutar pada X/Y/Z. Seret sfera dalam bulatan untuk putaran bebas.
* `Scale`- Seret pada titik merah/hijau/biru luar untuk skalakan pada X/Y/Z. Seret pada kon merah/hijau/biru luar untuk skalakan pada satah X/Y/Z. Seret pada bulatan pic luar untuk skalakan seragam.

![](/images/tool_gizmo.webp)

#### Node dan verteks 

Setiap objek dalam Nomad terdiri daripada node dan verteks:

* `Node` - 'Pemegang' objek, yang menyimpan terjemahan, putaran, skala, dipanggil matriks transformasi.
* `Vertices` - Titik yang mentakrifkan permukaan objek, ia menyimpan maklumat kedudukan dan cat.

Jika anda mempunyai kotak ringkas yang terdiri daripada 8 verteks, anda boleh menterjemahkannya dengan mengubah matriks transformasinya, atau dengan mengubah kedudukan verteks. Semasa sculpting anda biasanya mahu mengubah verteks, semasa menggerakkan objek dengan gizmo, anda biasanya mahu mengubah node. Nomad membenarkan anda melakukan kedua-duanya. 

#### Toolbar menu kiri

Toolbar kiri mengawal sama ada gizmo akan berfungsi pada node atau verteks, serta fungsi lain:

* `Clone` - Buat salinan berdiri sendiri objek semasa, yang boleh diseret dengan gizmo.
* `Instance` - Buat salinan instance objek semasa. Objek dipautkan, jadi perubahan sculpting pada satu objek akan muncul pada semua objek instance.
* `Group/Object/Vertex/Auto` - Akan menetapkan sama ada gizmo akan menjejaskan node atau verteks objek. Mod 'auto' lalai akan cuba membuat tekaan terbaik. Jika terdapat beberapa objek diparentkan bersama dalam hierarki, 'Object' hanya akan menggerakkan objek semasa, objek anak akan kekal pegun. Gizmo juga boleh mengambil kira masking dan simetri.
* `Pin` - Secara lalai gizmo akan bergerak ke pivot objek terpilih. Apabila pin diaktifkan, gizmo akan kekal di tempat ia berada.
* `Align` - Togol pivot sejajar dengan objek semasa, atau sejajar dengan dunia.
* `Snap rotation` - Aktifkan nilai putaran disnap kepada kenaikan, nilai snap dipaparkan dan boleh diedit apabila snap aktif.
* `Snap translation` - Aktifkan nilai terjemahan disnap kepada kenaikan, nilai snap dipaparkan dan boleh diedit apabila snap aktif.
* `Pivot` - Apabila diaktifkan, gizmo boleh digerak dan diputar tanpa menggerakkan objek. Ia mempunyai menu tambahan yang diterangkan di bawah.

#### Pivot
Apabila mod pivot aktif, menu dipaparkan untuk membolehkan perubahan pivot pantas:

**Reset** 
* `Center` - Pindahkan pivot ke tengah objek
* `Bottom` - Pindahkan pivot ke bahagian bawah objek
* `Align` - Tetapkan semula putaran supaya sejajar dengan dunia.
* `Mask` - Pindahkan pivot ke tengah kawasan tidak dimask.

**On Tap**
* `None` - jangan buat apa-apa apabila objek diketuk
* `Normal` - Pindah dan putar pivot supaya sejajar dengan tempat permukaan diketuk
* `First` - Pindah (tetapi jangan putar) pivot ke tempat permukaan diketuk
* `Medial` - Pindahkan pivot ke tengah objek, di bawah tempat permukaan diketuk.

#### Tetapan Gizmo

![](/images/tool_gizmo_settings.webp)

##### Matrix 
* ![](/icons/target.webp) `Move origin` - Pindahkan objek supaya pivotnya berada di tengah adegan, dipanggil origin.
* ![](/icons/bake.webp)  `Bake` - Bekukan objek di tempat ia berada, dan tetapkan nilai translate/rotate kepada 0, scale kepada 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - Jadikan nilai matriks sepadan dengan tempat pemegang gizmo berada dalam dunia.
* ![](/icons/reset.webp) `Reset` - Pintasan yang menetapkan nilai terjemahan kepada 0, nilai putaran kepada 0, skala kepada 1, menggerak dan memutar objek.

::: tip Bake vs bake to pivot
Cipta kotak, pilih alat Gizmo, buka dan pin menu tetapan. Secara lalai nilai terjemahan dan putaran ialah 0, skala ialah 1.

Aktifkan mod pivot, gerakkan pemegang ke satu sisi, matikan mod pivot. Pivot telah berubah, tetapi perhatikan bahawa nilai terjemahan masih 0. 

Jika anda mahu melihat di mana pivot *sebenarnya* berada, klik `Bake Pivot`. Kini nilai terjemahan dikemas kini. Perhatikan kotak tidak bergerak semasa operasi ini, begitu juga dalam mod pivot.

Gerak dan putar kotak ke suatu tempat, kemudian ketik `Move Origin`. Ia menggerakkan objek supaya pivotnya berada di tengah dunia, tetapi meninggalkan putaran tidak berubah.

Klik `Reset`, dan putaran akan ditetapkan kepada 0 juga.

Gerak dan putar kotak sekali lagi, kali ini klik `Bake`. Pivot kekal di tempatnya, kotak kekal di tempatnya, tetapi nilai terjemahan dan putaran ditetapkan kepada 0.

Latih ini beberapa kali! Fahami bahawa nilai pivot tersembunyi, Nomad menguruskannya untuk anda, tetapi jika anda perlu menetapkan pivot ke lokasi sebenar dalam ruang, Bake pivot akan melakukannya untuk anda.

:::

* `Translation` - nilai translate X, Y, Z
* `Rotation` - nilai rotate X, Y, Z
* `Scale` - Skala seragam jika itu diaktifkan, atau skala X, Y, Z jika dimatikan.
* `Uniform scale` - Togol keupayaan untuk skalakan secara seragam atau bebas pada setiap paksi

-----

* `Compact` - togol susun atur gizmo untuk meletakkan pemegang tambahan di luar atau di dalam sfera putaran
* `Widget size` - saiz gizmo
* `Thickness` - saiz garisan pada gizmo
* `Opacity` - kelegapan gizmo
* `Hide on interaction` - togol sama ada gizmo patut disembunyikan sementara apabila diseret

-----

* `Tangent roll threshold` - Kawal cara UI putaran berkelakuan apabila menyeret pada pemegang bulatan untuk memutar pada X/Y/Z. Jika nilai ini 0, putaran berfungsi seperti dail, seret gizmo dalam bulatan. Jika nilai ini 90, putaran berfungsi seperti menarik tali yo-yo; seret dalam garisan lurus ke arah atau menjauhi tempat anda mula-mula klik. Nilai antara 0 dan 90 akan melakukan gabungan kedua-duanya; di bawah nilai akan menjadi gerakan linear, di atas nilai akan menjadi gerakan bulatan.
* `Numerical input` - apabila diaktifkan, ketikan tunggal pada gizmo akan memaparkan tetingkap untuk memasukkan nilai tepat bagi paksi widget yang diketuk.

::: warning
[Gizmo](#gizmo), [Translate](#translate), [Rotate](#rotate) dan [Scale](#scale) menggunakan kotak semak simetri mereka sendiri!

Secara lalai simetri ini dimatikan.
:::

Di sebelah kiri anda boleh menggerakkan pivot gizmo, anda boleh lihat video di bawah dalam tindakan.
Ini amat berguna untuk putaran, kerana ia tidak mengubah apa-apa untuk terjemahan.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Facegroup

Facegroup membolehkan anda mengatur objek kepada muka berwarna berbeza. Anda boleh menggunakan kumpulan ini dalam banyak cara dalam Nomad:

* Kaedah pemilihan pantas untuk mask
* Sembunyi/papar bahagian objek anda
* Mengatur objek tanpa perlu memecahkannya kepada bahagian berasingan
* Mentakrifkan kawasan UV
* Membimbing quad remesher
* Kawalan tambahan untuk alat seperti smooth.

#### Toolbar kiri Facegroup

* `Patch ` - Paparkan facegroup tersedia sebagai patch. Patch tidak digunakan boleh dipadam. Ketik pada patch untuk menamakan semula atau menukar warnanya. Ikon tambah membolehkan anda mencipta patch baharu.
* `Dot` - Lukis pada objek untuk mentakrifkan facegroup. Apabila '+ Face Group' diaktifkan, setiap stroke baharu akan secara automatik mencipta facegroup baharu, berguna untuk mentakrifkan kawasan dengan cepat. Ketikan akan flood fill kawasan terpilih. Peluncur menetapkan radius dot.
* `Relax` - Lembutkan sempadan facegroup. Sangat berguna untuk mentakrifkan tepi bersih untuk quad remeshing, atau untuk mentakrifkan panel untuk pemodelan hard surface. Peluncur mengawal radius dan intensiti operasi relax.
* `Shape selector` - Cipta facegroup dengan bentuk dan bukannya berus, melalui `Lock+Radius`, `Lasso`, `Polygon`, `Rect` dan `Ellipse`. Lihat [Shape Selector](#shape-selector) untuk maklumat lanjut.
* `Auto-pick` - Apabila diaktifkan, akan memilih patch di mana stroke bermula, dan menggunakan patch itu untuk sepanjang stroke. Sangat berguna untuk mengemas kawasan facegroup; jika facegroup telah meluas terlalu jauh, aktifkan auto-pick, mulakan stroke dari tempat patch facegroup betul, dan seret ke sempadan untuk menetapkan semula patch yang betul.

### ![](/icons/tool_hide.webp) Hide
Sembunyikan atau asingkan bahagian objek. 

Mod utama dikawal dari menu kiri:

* `Dot` - Berus pada objek untuk menyembunyikan bahagian objek.
* `Shape selector` -  Sembunyikan dengan bentuk dan bukannya berus, melalui `Lasso`, `Polygon`, `Line`, `Rect` dan `Ellipse`. Lihat [Shape Selector](#shape-selector) untuk maklumat lanjut.
* `Show` - songsangkan operasi, jadi mod terpilih akan memaparkan dan bukannya menyembunyikan bahagian objek.

Toolbar akan muncul di bahagian atas viewport dengan kawalan tambahan:

* `Clear` - Pulihkan objek, semua bahagian tersembunyi akan dipaparkan semula.
* `Invert` - Tukar bahagian tersembunyi dan tidak tersembunyi.
* `Facegroup` - Gunakan facegroup untuk menyembunyikan bahagian dengan cepat, mengetik facegroup akan menyembunyikan keseluruhan facegroup.
* `Mask` - Jika mask aktif, mengetik butang ini akan menyembunyikan bahagian dimask.
* `Delete` - Padam bahagian objek yang tersembunyi
* `Split` - Pisahkan bahagian objek yang tersembunyi menjadi bentuk baharu.

### ![](/icons/tool_measure.webp) Measure
Seret untuk mengukur jarak antara 2 titik.

### ![](/icons/tool_remesh.webp) Quad Remesher

![](/images/tool_quadremesher.webp)

Alat ini akan menukar objek terpilih kepada susun atur topologi quad yang bersih, dengan kawalan untuk ketumpatan, aliran tepi, simetri. 

::: tip
Quad Remesher dibangunkan oleh [Exoside](https://exoside.com/) untuk iOS dan desktop. 

Untuk iOS ia adalah pembelian dalam aplikasi dalam Nomad, bayaran sekali sebanyak $16USD.

Untuk desktop, beli lesen daripada [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Anda boleh membelinya hanya untuk Nomad desktop, atau lesen silang untuk semua aplikasi desktop yang disokong.

Jika anda sudah memiliki Quad Remesher untuk aplikasi desktop lain, anda boleh [membeli naik taraf ke semua platform dengan kos lebih rendah.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher tidak tersedia untuk Android. Android boleh menggunakan 'Quad Remesh - Instant' sumber terbuka percuma yang tersedia di bawah menu Topology -> Misc, tetapi fahami set cirinya sangat terhad.
:::

Apabila alat ini diaktifkan buat kali pertama, ia akan bertanya sama ada anda mahu mengaktifkannya sebagai pembelian dalam apl. Setelah aktif, bar alat kiri dan atas akan diaktifkan.

* `Dot` - Berus ini akan menetapkan ketumpatan sasaran. Keamatan pada 100% akan melukis dalam merah, yang akan menggunakan dua kali ganda ketumpatan quad sasaran pada kawasan tersebut. Keamatan pada 0% akan melukis dalam sian, yang akan menggunakan separuh ketumpatan quad sasaran pada kawasan tersebut. Keamatan pada 50% akan melukis dalam kelabu, yang akan menggunakan ketumpatan quad sasaran lalai.
* `Smooth` - Melicinkan peralihan ketumpatan merah/kelabu/sian.
* `Curve` - Lakarkan lengkung pada permukaan arca, quad remesher akan menggunakannya sebagai panduan untuk aliran tepi. Ketik pada satu lengkung untuk memadamkannya.
* `Path` - Lukis laluan pada permukaan arca, quad remesher akan menggunakannya sebagai panduan untuk aliran tepi. Ketik pada satu laluan untuk memadamkannya. 
* `Rect` - Lukis segi empat tepat pada permukaan arca, quad remesher akan menggunakannya sebagai panduan untuk aliran tepi. Ketik pada satu laluan untuk memadamkannya.
* `Ellipse` - Lukis elips pada permukaan arca, quad remesher akan menggunakannya sebagai panduan untuk aliran tepi. Ketik pada satu laluan untuk memadamkannya.

#### Quad remesher top toolbar
![](/images/tool_quadremesher_toolbar.webp)

Satu bar alat akan muncul di bahagian atas viewport dengan kawalan tambahan:


* `<Count>` - Klik ini untuk memulakan proses quad remesher, nombor ini memberitahu anda apakah kiraan quad remesh sasaran.
* `Quads` - Tetapkan kiraan quad sasaran dengan meleret ke kiri dan kanan, atau ketik untuk menetapkan nombor yang tepat. Ambil perhatian bahawa ini lebih kepada panduan berbanding nombor tetap, pelbagai kawalan pada quad remesher selalunya akan menyebabkan hasil tidak sepadan tepat dengan sasaran ini.
* `Half` - Pintasan untuk menetapkan kiraan sasaran kepada separuh kiraan poli semasa.
* `Same` - Pintasan untuk menetapkan kiraan sasaran kepada kiraan poli semasa.
* `Guides` - menunjukkan jumlah keseluruhan panduan, atau ketik untuk memadam semua panduan.
* `Density X` - ketik untuk membuang semua lukisan ketumpatan.
* `Density (painting)` - togol untuk menggunakan atau mengabaikan lukisan ketumpatan.
* `Face Group` - togol untuk menggunakan atau mengabaikan facegroup bagi mengemudi quad remesher.
* `Relax` - togol untuk melonggarkan sempadan facegroup secara automatik semasa quad remeshing. Jika anda telah pun melonggarkan/melicinkan sempadan facegroup anda, lumpuhkan pilihan ini.
* `Relax Slider` - Peluncur pintasan untuk melonggarkan sempadan facegroup.
* `Hard Edges` - togol untuk cuba mengekalkan tepi keras.
* `Reproject Vertex` - togol untuk memprojek semula susun atur baharu ke mesh input.
* `Symmetry` - Togol untuk mengaktifkan hasil simetri. Ambil perhatian bahawa simetri sentiasa dikira di sekeliling paksi-x dunia, jadi pastikan model anda berada di origin jika anda menjangkakan hasil simetri.
* `...` - Menu tetapan Quadremesher. 

#### Quad remesher settings menu

Kebanyakan tetapan ini tersedia dalam bar alat atas.

* `<Count>, Half, Same` - Sama seperti butang Remesh, Half, Same dalam bar alat atas.
* `Target Quads` - Sama seperti butang `Quads` dalam bar alat atas
* `Adaptive quad count` - togol untuk membolehkan penggunaan quad yang lebih kecil di kawasan berkeliukan tinggi, dan quad yang lebih besar di kawasan berkeliukan rendah.
* `Adaptive size` - Tetapkan jumlah adaptiviti. 100% akan membenarkan saiz adaptif maksimum, pada 0% quad akan seragam.
* `Auto-Detect Hard Edges` - togol untuk menyesuaikan susun atur quad remesh supaya lebih baik mengikut permukaan tajam.
* `Density (painting)` - Sama seperti butang `Density (painting)` dalam bar alat atas
* `Reproject Vertex` - togol untuk memprojek semula susun atur baharu ke mesh input.
* `Face Group` - Sama seperti butang `Face Group` dalam bar alat atas
* `Relax Slider` - Peluncur pintasan untuk melonggarkan sempadan facegroup.

::: tip

Resipi untuk mendapatkan quad remesh yang baik dengan artifak minimum:

* Facegroup mesh untuk menentukan aliran quad ideal anda.
* Facegroup relax untuk mendapatkan sempadan facegroup yang licin.
* Decimate. Ini akan memastikan anda tidak mempunyai muka yang nipis atau terherot pada tepi facegroup. Dalam tetapan decimate pastikan facegroup diaktifkan. Ini akan membuat tepi segi tiga mengikut tepi facegroup anda dengan tepat. 

Dalam pilihan quad remesh pastikan relax dilumpuhkan (kerana anda telah pun melonggarkan mesh) dan anda sepatutnya mendapat hasil yang baik.

:::

### ![](/icons/tool_select.webp) Select
Gunakan mod bentuk untuk memilih objek dalam adegan. `Unselect` akan mengeluarkan objek daripada pemilihan.

### ![](/icons/tool_view.webp) View
"Alat" ini tidak melakukan apa-apa secara khusus, ini hanyalah cara untuk melihat model tanpa mengubah suai adegan anda.


## Toolbox context menu

![](/images/tools_context_menu.webp)

Klik kanan atau tekan lama pada alat dalam toolbox akan memaparkan menu konteks. Menu ini mempunyai pilihan berikut:

* `Save` - simpan sebarang perubahan yang anda buat pada alat
* `Clone` - gandakan alat ke dalam pintasan alat baharu
* `Last save` - kembali kepada versi alat yang disimpan sebelum ini
* `Icon` - tukar ikon untuk alat
* `Reset` - tetapkan semula alat kepada lalainya
