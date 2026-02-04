# ![](/icons/toolbox.webp) Alat {#tools}

![](/images/tools_menu.webp)

::: tip
Lompat ke bawah ke [Alat](#tools-1) untuk deskripsi tiap alat.
:::

## Ikhtisar {#overview}

Alat dipilih dari `Toolbox` di sebelah kanan, dan dikendalikan dengan `Tool Controls` di sebelah kiri. Pengaturan tambahan ada di menu `Settings`, ikon pertama di menu kanan atas.

Alat kuas memiliki kontrol untuk ukuran dan intensitas. Alat seleksi memiliki kontrol untuk beberapa gaya seleksi. Bagian bawah kontrol alat memiliki pintasan untuk operasi yang sering digunakan (Smooth, Mask, Hide, Gizmo, Color, Alpha).

Alat Nomad diberi kode warna di toolbox:

* <span class=brush>**Brush tools**</span> (Clay, Brush, Smooth, Layer, Inflate, Nudge, Stamp, DelLayer)
* <span class=move>**Move tools**</span> (Move, Drag)
* <span class=mask>**Mask tools**</span> (Mask, SelMask)
* <span class=paint>**Paint tools**</span> (Paint, Smudge)
* <span class=flatten>**Flatten tools**</span> (Flatten, Planar)
* <span class=pinch>**Pinch tools**</span> (Crease, Pinch)
* <span class=selection>**Selection based tools**</span> di mana sebuah mask 2D digambar terlebih dahulu, lalu sebuah operasi dijalankan (Trim, Split, Project)
* <span class=creation>**Creation tools**</span> (Tube, Lathe, Insert)
* <span class=transform>**Transform tools**</span> (Transform, Gizmo)
* <span class=misc>**Misc tools**</span> (Facegroup, Hide, Measure, Select)
* <span class=view>**View tool**</span>



Banyak dari alat ini dapat dikustomisasi dengan perilaku kuas, tekanan, tekstur, dll yang berbeda melalui menu [Stroke](stroke.md). 


### Kontrol kuas {#brush-controls}

Toolbar kiri memiliki slider untuk radius dan intensitas, lalu kontrol spesifik kategori alat, dijelaskan di bawah.

![](/images/tool_left_panel.webp)

::: tip
Slider intensitas untuk banyak alat bisa melampaui 100%, layak untuk dieksperimenkan!
:::

### Mode sub {#sub-mode}
Tombol tepat di bawah slider intensitas adalah tombol `Sub`. Label dan fungsinya akan berubah untuk setiap alat, dan ketika ditekan akan memanggil perilaku alternatif, biasanya kebalikan. Misalnya untuk [Paint](#paint) akan memanggil mode Erase, untuk [Crease](#crease) akan membuat tepi yang terangkat alih-alih cekungan, dll.

Secara bawaan tombol ini bersifat lengket; artinya Anda bisa menahannya untuk sementara memanggilnya, ketika Anda lepaskan ia akan mati. Jika Anda mengetuknya, sub mode akan diaktifkan secara permanen.

### Pintasan {#shortcuts}
Di bagian bawah toolbar kiri ada pintasan untuk [Smooth](#smooth), [Mask](#mask), [Hide](#hide), [Gizmo](#gizmo), [Color](painting.md#pbr-sliders), [Alpha](stroke.md#alpha). 

Secara bawaan semuanya berfungsi sebagai tombol lengket; artinya Anda bisa menahannya untuk sementara memanggilnya, ketika Anda lepaskan ia akan mati. Jika Anda mengetuknya, mode pintasan itu akan diaktifkan secara permanen.

### Kontrol seleksi {#selection-controls}

Alat [Selection Mask](#selection-mask), [Trim](#trim), [Split](#split), [Project](#project), [Facegroup](#facegroup) dan [Hide](#hide) semuanya menggunakan kontrol serupa untuk memilih area mesh.

![](/images/tools_shape_selector_panel.webp)


* `Lasso` - Bentuk gambar bebas
* `Polygon` - Bentuk tertutup yang didefinisikan oleh kombinasi kurva dan/atau garis lurus. Lihat [Shape editing](#shape-editing) di bawah untuk info lebih lanjut.
* `Curve` - (Project saja) - Kurva gambar bebas untuk proyeksi
* `Path` - (Project saja) - Kurva yang didefinisikan oleh titik-titik. Lihat [Shape editing](#shape-editing) di bawah untuk info lebih lanjut.
* `Line` - Seret garis untuk mendefinisikan segmen planar. Secara bawaan akan langsung beroperasi pada mesh, matikan auto validate jika Anda tidak menginginkannya (tekan lama atau geser pada ikon garis)
* `Rect` - Seret garis diagonal, ini akan mendefinisikan sudut-sudut bentuk persegi panjang. Tekan lama atau geser untuk menampilkan opsi auto validate, paksa ke bentuk persegi, dan agar klik pertama menjadi pusat persegi panjang.
* `Ellipse` - Seret garis diagonal, ini akan mendefinisikan ukuran elips. Tekan lama atau geser untuk menampilkan opsi auto validate, paksa ke bentuk lingkaran, dan agar klik pertama menjadi pusat elips.
* `Flip` - membalik mask bentuk, atau arah alat project.

Kebanyakan alat memiliki opsi auto validate, artinya operasi akan terjadi segera setelah Anda selesai menggambar bentuk. Ketika auto validate mati, sebuah tombol hijau akan digambar di sebelah bentuk yang akan mengeksekusi operasi. Ini memungkinkan Anda mengedit bentuk, menyesuaikan tampilan, ketika siap menggunakan bentuk, tekan tombol hijau.

### Pengeditan bentuk {#shape-editing}
Pengeditan poligon dan kurva berperilaku dengan cara yang mirip:

* Untuk memulai, seret garis untuk mendefinisikan 2 titik, lalu seret keluar dari tengah garis untuk mendefinisikan poligon atau kurva.
* Klik pada titik untuk beralih antara halus dan tajam. 
* Klik dan seret pada bagian kurva atau garis untuk membuat titik baru.
* Untuk menghapus titik, seret titik ke tetangganya sampai berubah merah.
* Ikon tempat sampah di sudut ikon poligon atau path akan menghapus bentuk.

### Menu pengaturan {#settings-menu}

Banyak alat memiliki pengaturan tambahan yang ditemukan di menu settings, ikon pertama di menu kanan atas:

![](/images/tools_settings_menu.webp)

## Alat {#tools-1}

|                                                                     |                                                   |                                                                   |                                                         |                                                         |                                                                     |
| :-----------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------: |
| ![](/icons/tool_clay.webp)         <br> [Clay](#clay)              | ![](/icons/tool_brush.webp) <br> [Brush](#brush) | ![](/icons/tool_move.webp)       <br> [Move](#move)              | ![](/icons/tool_drag.webp)    <br> [Drag](#drag)       | ![](/icons/tool_smooth.webp)  <br> [Smooth](#smooth)   | ![](/icons/tool_mask.webp)    <br> [Mask](#mask)                   |
| ![](/icons/tool_maskSelector.webp) <br> [Sel Mask](#selector-mask) | ![](/icons/tool_paint.webp) <br> [Paint](#paint) | ![](/icons/tool_smudge.webp)     <br> [Smudge](#smudge)          | ![](/icons/tool_flatten.webp) <br> [Flatten](#flatten) | ![](/icons/tool_planar.webp)  <br> [Planar](#planar)   | ![](/icons/tool_crease.webp)  <br> [Crease](#crease)               |
| ![](/icons/tool_pinch.webp)        <br> [Pinch](#pinch)            | ![](/icons/tool_trim.webp)  <br> [Trim](#trim)   | ![](/icons/tool_split.webp)      <br> [Split](#split)            | ![](/icons/tool_project.webp) <br> [Project](#project) | ![](/icons/tool_layer.webp)   <br> [Layer](#layer)     | ![](/icons/tool_inflate.webp) <br> [Inflate](#inflate)             |
| ![](/icons/tool_nudge.webp)        <br> [Nudge](#nudge)            | ![](/icons/tool_stamp.webp) <br> [Stamp](#stamp) | ![](/icons/tool_clearLayer.webp) <br> [Del Layer](#delete-layer) | ![](/icons/tool_tube.webp)    <br> [Tube](#tube)       | ![](/icons/tool_lathe.webp)   <br> [Lathe](#lathe)     | ![](/icons/tool_insert.webp)  <br> [Insert](#insert)               |
| ![](/icons/tool_transform.webp)    <br> [Transform](#transform)    | ![](/icons/tool_gizmo.webp) <br> [Gizmo](#gizmo) | ![](/icons/tool_faceGroup.webp)  <br> [FaceGroup](#facegroup)    | ![](/icons/tool_hide.webp)    <br> [Hide](#hide)       | ![](/icons/tool_measure.webp) <br> [Measure](#measure) | ![](/icons/tool_remesh.webp)  <br> [Quad Remesher](#quad-remesher) |
| ![](/icons/tool_select.webp)       <br> [Select](#select)          | ![](/icons/tool_view.webp)  <br> [View](#view)   |                                                                   |                                                         |                                                         |                                                                     |

------

### ![](/icons/tool_clay.webp) Tanah liat {#clay}
Alat Clay berguna untuk membangun bentuk patung Anda. `Sub` akan menghapus material dari patung Anda.

![](/videos/tool_clay.mp4)

### ![](/icons/tool_brush.webp) Kuas {#brush}
Brush standar. `Sub` akan menghapus material.

![](/videos/tool_brush.mp4)

### ![](/icons/tool_move.webp) Pindah {#move}
Area di bawah kuas akan menempel pada kuas, memungkinkan deformasi elastis. Seleksi dipertahankan selama pemindahan, jadi jika Anda menjauhkan kuas, lalu mengembalikannya ke tempat semula, Anda tidak akan melihat deformasi.

Sub mode adalah `Normal`, dan akan memindahkan area di bawah kuas sepanjang normal permukaan.

Brush ini bagus untuk deformasi skala besar maupun deformasi kecil yang hati-hati.

#### Pengaturan Pindah {#move-settings}

* `Radius (Background)` - Seberapa jauh dari tepi model Anda masih bisa memahat, berguna saat bekerja pada siluet objek. 
* `Same-side vertex only` - Abaikan verteks yang menghadap ke arah berlawanan dari deformasi.


![](/videos/tool_move.mp4)

### ![](/icons/tool_drag.webp) Seret {#drag}
Area di bawah kuas akan menempel pada kuas, memungkinkan deformasi elastis. Tidak seperti move brush, seleksi terus diperbarui selama sapuan, sehingga memungkinkan membuat objek panjang seperti ular, terutama ketika Dynamic Topology diaktifkan.

Sub mode adalah `Normal`, dan akan memindahkan area di bawah kuas sepanjang normal permukaan.

Brush ini bagus untuk perubahan bentuk yang lebih longgar dan gestural.

#### Pengaturan Seret {#drag-settings}

* `Radius (Background)` - Seberapa jauh dari tepi model Anda masih bisa memahat, berguna saat bekerja pada siluet objek. 
* `Same-side vertex only` - Abaikan verteks yang menghadap ke arah berlawanan dari deformasi.

![](/videos/tool_drag.mp4)

### ![](/icons/tool_smooth.webp) Haluskan {#smooth}
Menghaluskan area dengan merata-ratakan posisi titik. Alat ini sangat bergantung pada kepadatan poligon.
Jadi jika Anda memiliki banyak poligon, penghalusan akan kurang efektif.

Sub mode adalah `Relax`, yang hanya menghaluskan wireframe tetapi berusaha mempertahankan detail geometris.

#### Pengaturan haluskan {#smooth-settings}

![](/images/tool_smooth_settings.webp)

##### Facegroup {#smooth-facegroup}

* `Relax` - Akan menghaluskan batas facegroup. Gunakan intensitas lebih dari 100% untuk cepat menghaluskan batas. `Auto` akan menghaluskan hanya jika pratinjau facegroup diaktifkan, `Off` akan menonaktifkan, `On` akan mengaktifkan. 

##### Vertex {#vertex}
* `Sticky vertex on border` - Untuk mesh dengan tepi terbuka, misalnya bidang, memungkinkan untuk menghaluskan sudut. Mengaktifkan opsi ini akan mengunci tepi terbuka.
* `Relax` - sama dengan mode alternatif relax di toolbar kiri.
* `Stable smoothing` - Berusaha membuat penghalusan tidak bergantung pada topologi. Ini bekerja paling baik dengan kepadatan topologi yang bervariasi dan dengan nilai intensitas smoothing yang tinggi.

##### Pengecatan {#painting}
* `Screen Smoothing` - Gunakan opsi ini untuk mendapatkan smoothing yang tidak bergantung pada topologi, bahkan pada jumlah poligon tinggi.
* `Screen samples` - Kualitas smoothing, angka lebih tinggi akan lebih halus, tetapi lebih lambat.

::: tip
Kepadatan poligon yang lebih tinggi dapat memerlukan peningkatan intensitas di atas 100%. Nilai sangat tinggi (300%, 500%) juga dapat bekerja dengan baik sebagai alat pemahatan, memaksa area menjadi datar dan halus dengan cepat di bawah kuas, seperti memukul tanah liat dengan palu!
:::

![](/videos/tool_smooth.mp4)

### ![](/icons/tool_mask.webp) Masker {#mask}
Alat ini memungkinkan Anda mem-mask verteks. Verteks yang di-mask terlindungi dari sculpting atau painting. 

Sub mode adalah `Unmask`, dan akan menghapus area di mana mask telah dilukis.

Mirip dengan seleksi di program lukis 2D, mask dapat dilukis dengan kuas, atau dibuat dengan seleksi bentuk, diburamkan atau dipertajam. 

Berbeda dengan program lukis 2D, mask juga dapat dibuat melalui facegroup, dan mask dapat digunakan untuk membuat geometri baru melalui operasi ekstrusi/ekstraksi. 

![](/videos/tool_mask1.mp4)

 Sebuah toolbar akan muncul di bagian atas viewport dengan kontrol tambahan. 

![](/images/tool_mask_toolbar.webp)

Judul bar dapat diketuk untuk memperluas/meruntuhkan, atau panah di kanan atas dapat diketuk untuk memindahkannya ke bagian atas atau bawah UI.

| Action                                             | Description                                                                                |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| ![](/icons/circle_cross2.webp) Clear              | Menghapus mask                                                                             |
| ![](/icons/invert.webp)        Invert             | Membalik mask                                                                              |
| ![](/icons/sharpen.webp)       Sharpen            | Menajamkan tepi mask                                                                       |
| ![](/icons/blur.webp)          Blur               | Memburamkan tepi mask                                                                      |
|                                 Blur ->            | Seret kiri/kanan untuk memburamkan mask secara interaktif                                  |
| ![](/icons/culling.webp)       Front              | Beralih untuk hanya mem-mask verteks yang menghadap ke depan                              |
|                                 Convert            | Mengonversi mask menjadi facegroup                                                         |
| ![](/icons/group_to_mask.webp) On tap (facegroup) | Saat diaktifkan facegroup akan ditampilkan, mengetuk facegroup akan mem-mask-nya          |
|                                 On tap (mask)      | Saat diaktifkan, mengetuk 'pulau' mask atau poligon tak ter-mask akan flood fill pulau itu |
| ![](/icons/vertex.webp)        Connected          | Saat diaktifkan hanya mengizinkan sapuan mask memengaruhi topologi yang terhubung         |

##### Gerakan cepat masker {#mask-quick-gesture}
Anda dapat melakukan gesture gaya ZBrush sambil menahan tombol quick masking di toolbar kiri:
| Action  | Gesture (hold lower-left shortcut) |
| :-----: | :--------------------------------: |
| Invert  | Ketuk pada background              |
| Clear   | Seret pada background              |
| Blur    | Ketuk pada area yang di-mask       |
| Sharpen | Ketuk pada area yang tidak di-mask |


#### Pengaturan masker {#mask-settings}
![](/images/tool_mask_settings.webp)

![](/videos/tool_mask2.mp4)

* `Preview` - Menu Mask settings terutama digunakan untuk membuat geometri dari mask. Karena itu perilaku bawaan adalah mempratinjau seperti apa geometri baru. Anda dapat memilih tanpa pratinjau, pratinjau extract, pratinjau split, dan apakah geometri ini akan ditampilkan dalam mode x-ray.

##### Ketebalan {#thickness}
* `Height` - Tinggi bentuk yang diekstrak. Ikon Plus/Minus memungkinkan Anda berputar antara ekstrusi ke luar, ke dalam, atau terpusat. 
* `Height/Height+Mask` - Beralih antara tinggi yang konstan, atau apakah bagian mask yang diburamkan memengaruhi tinggi, memungkinkan bentuk lembut dengan tinggi bervariasi. 

##### Kelembutan {#smoothness}
Saat aktif, akan menghaluskan tepi bentuk yang diekstrak, bekerja lebih baik dengan jumlah poligon tinggi. 
* `Iterations` - Jumlah smoothing yang diterapkan. Nilai tinggi akan menghasilkan tepi melengkung yang sangat halus, tetapi akan mulai menyimpang dari bentuk mask.
* `All/Sharp border/Borders only` - Smoothing dapat bekerja ke segala arah, menghaluskan sisi dan atas bentuk yang diekstrak, atau menghaluskan atas dan sisi tetapi mempertahankan tepi tajam, atau hanya menghaluskan tepi, membiarkan permukaan atas tidak terpengaruh.

##### Loop tepi (samping) {#edge-loop-side}
* `Auto Edge-loop (side)` - Akan menghitung jumlah divisi di sisi bentuk yang diekstrak untuk membuat poligon persegi yang cocok dengan poligon area yang di-mask. Saat dinonaktifkan, Anda dapat mengatur jumlah edge loop sendiri dengan slider edge loop.

----

##### Ekstrak {#extract}
* `Extract` - Membuat geometri hasil ekstraksi.
* `Closing action` - Bagaimana extract harus berperilaku. 'None' akan menduplikasi poligon yang di-mask ke bentuk baru. 'Fill' akan melakukan hal yang sama, dan mencoba menambal permukaan belakang. 'Shell' akan mengekstrusi sesuai jumlah yang diatur di 'thickness', dan ini adalah bawaan.

::: tip

Jika preview dalam mode 'Extract' dengan 'X-ray' diaktifkan, mengklik tombol Extract bisa membingungkan pada awalnya. Karena menu aktif, ia akan mencoba mempratinjau ekstraksi pada bentuk baru Anda, dan men-xray permukaan asli. Namun karena Anda tidak memiliki mask pada permukaan baru, ia tidak dapat mempratinjau ekstraksi, dan Nomad akan memperingatkan Anda 'Nothing to Extract!'. 

Ini normal, tutup menu mask settings untuk melihat bentuk baru dan yang asli, dan pilih lagi permukaan asli jika Anda perlu menghapus mask atau menggambar mask baru.
:::

##### Pisah {#split-mask}
* `Split` - Akan mengekstrak area yang di-mask DAN yang tidak di-mask ke bentuk baru. 
* `Closing action (masked)` - Bagaimana ekstraksi mask harus berperilaku. 'None' akan menduplikasi poligon yang di-mask ke bentuk baru. 'Fill' akan melakukan hal yang sama, dan mencoba menambal permukaan belakang. 'Shell' akan mengekstrusi sesuai jumlah yang diatur di 'thickness', dan ini adalah bawaan.
* `Closing action (unmasked)` - Bagaimana ekstraksi area tak ter-mask harus berperilaku. 'None' akan menduplikasi poligon yang di-mask ke bentuk baru. 'Fill' akan melakukan hal yang sama, dan mencoba menambal permukaan belakang. 'Shell' akan mengekstrusi sesuai jumlah yang diatur di 'thickness', dan ini adalah bawaan.
* `Sync border` - Memastikan batas antara bentuk hasil ekstraksi area mask dan tak ter-mask tetap berdekatan. Saat dinonaktifkan, karena operasi shell akan mengekstrusi tiap face sepanjang normalnya, celah bisa terbentuk di antara bentuk.

##### Pahat {#carve}
* `Carve` - Dalam mode bawaan, berperilaku seolah Anda telah melakukan trim ke permukaan sejauh nilai 'thickness', seperti memotong sepotong kulit jeruk. 



### ![](/icons/tool_maskSelector.webp) Masker Seleksi {#selection-mask}
Alat ini sebagian besar mirip dengan [Masking tool](#mask), perbedaan utamanya adalah Anda tidak menggunakan stroke untuk melukis mask, tetapi menggunakan [Selection Controls](#selection-controls).

Sub mode adalah `Unmask`, dan akan menghapus mask menggunakan selection controls.

Selection mask berbagi pengaturan alat yang sama dengan alat `Mask`.

![](/videos/tool_selector_mask.mp4)

### ![](/icons/tool_paint.webp) Cat {#paint}
Menerapkan warna dan properti material. Untuk mempelajari lebih lanjut tentang material Anda dapat mengunjungi bagian [Painting](painting.md).

Sub mode adalah `Erase` dan akan menghapus cat.

#### Pengaturan cat {#paint-settings}
* `Layer fitering` - Ini berfungsi seperti layer alpha lock di Photoshop atau Procreate. Jika Anda melukis pada sebuah layer, ketika ini diaktifkan, Anda hanya dapat memodifikasi area yang sudah dicat; area yang belum dicat akan terlindungi.

![](/videos/tool_paint.mp4)

### ![](/icons/tool_smudge.webp) Oles {#smudge}
Menggosok warna dan properti material. Menu smudge settings berisi slider `Quality`, nilai lebih rendah berarti sapuan lebih cepat.

![](/videos/tool_smudge.mp4)


### ![](/icons/tool_flatten.webp) Ratakan {#flatten}
Meratakan area dengan memproyeksikan titik ke bidang rata-rata.

Sub mode adalah `Fill` dan akan mendefinisikan bidang yang diatur oleh titik tertinggi, dan cenderung menarik titik ke atas.

#### Pengaturan ratakan {#flatten-settings}

* `Lock plane direction` - Gunakan arah bidang yang dihitung pada klik pertama. Secara bawaan ini dinonaktifkan.
* `Lock plane origin`- Gunakan klik pertama sebagai pusat bidang. Secara bawaan ini dinonaktifkan.

Ketika salah satu atau keduanya dinonaktifkan, flatten dapat diperdalam secara bertahap atau sudut bidang diubah dengan menggunakan sapuan panjang yang bergerak di atas kedalaman dan kelengkungan berbeda. Ini bersama dengan opsi area sampling di menu brush dapat menawarkan kontrol yang sangat presisi.

::: tip
Saat bekerja di area dengan kelengkungan tinggi, misalnya mencoba meratakan pipi tetapi alat terus memengaruhi sisi hidung, cobalah membuat mask untuk melindungi area yang tidak boleh dipengaruhi kuas flatten.
:::

![](/videos/tool_flatten.mp4)


### ![](/icons/tool_planar.webp) Planar {#planar}
Membuat titik planar dengan memproyeksikan ke bidang rata-rata, tetapi dengan penumpukan yang lebih sedikit dibanding kuas flatten. Ini menciptakan permukaan hard-edge yang lebih bersih. Sapuan cepat akan lebih mendorong dan menarik permukaan, sapuan lambat yang dimulai dari area yang sudah planar dan bergerak keluar akan lebih mempertahankan bidang.

Sub mode adalah `Fill` dan akan mendefinisikan bidang yang diatur oleh titik tertinggi, dan cenderung menarik titik ke atas.

Planar sebenarnya adalah alat yang sama dengan `Flatten`, tetapi dengan `Lock plane direction` diaktifkan, artinya ia akan cenderung membuat permukaan hard edge yang lebih stabil, sementara flatten bisa lebih skulptural dan digunakan untuk membuat area semi-datar.

![](/videos/tool_planar.mp4)

### ![](/icons/tool_crease.webp) Lipatan {#crease}
Alat Crease berguna untuk memahat potongan kecil atau cekungan.

Sub mode adalah `Invert`, dan akan membuat crease yang terangkat.

#### Pengaturan lipatan {#crease-settings}

* `Pinch factor` - Seberapa banyak menarik verteks ke samping menuju kuas. Jika pinch di 1, dan offset di 0, permukaan tidak akan memiliki perubahan kedalaman, hanya perubahan topologi, menarik edge ke arah stroke.
* `Offset factor` - Seberapa banyak mendorong/menarik verteks dalam kedalaman. Jika pinch di 0, dan offset di 1, crease dalam atau tonjolan akan dibuat, tetapi akan terlihat bergerigi karena tidak cukup geo yang ditarik ke crease untuk mendefinisikan sisi atau dasar crease dengan akurat.

![](/videos/tool_crease.mp4)

### ![](/icons/tool_pinch.webp) Cubit {#pinch}
Alat ini dapat digunakan untuk menajamkan tepi.

Sub mode adalah `Invert` dan akan menyebarkan verteks.

![](/videos/tool_pinch.mp4)


### ![](/icons/tool_trim.webp) Pangkas {#trim}
Alat Trim bekerja dengan menghapus sebagian mesh Anda, dan memberikan opsi bagaimana memproses celah yang tersisa. Ia menggunakan [Selection controls](#selection-controls) untuk mendefinisikan trim.

::: tip
Karena alat ini memproyeksikan dari kamera, Anda akan mendapat peringatan jika kamera dalam mode perspektif.

Dalam mode ortografik potongan yang dibuat melalui mesh sejajar dengan tampilan, yang biasanya diharapkan orang. Ketika dilakukan dengan kamera perspektif, potongan akan terlihat berbeda di sisi jauh objek dibanding sisi dekat.
:::

#### Pengaturan pangkas {#trim-settings}

* `Stroke painting` - Jika paint diaktifkan di menu paint, area yang ditambal akan diisi dengan warna yang saat ini dipilih.
* `Boolean` - mengisi lubang trim menggunakan area quad poly. Area yang diisi akan datar.
* `Legacy` - mengisi lubang trim dengan area triangulasi. Area yang diisi akan datar.
* `Fill` - mengisi lubang dengan area triangulasi. Area yang diisi akan berupa permukaan melengkung, seperti film gelembung sabun.
* `None` - tidak mengisi lubang.
* `Boolean Detail Shape` - Perkiraan ukuran quad dan triangle yang digunakan di sisi bentuk trim.
* `Boolean Detail Hole` - Perkiraan ukuran triangle atau poly yang digunakan pada lubang trim yang diisi. 
* `Legacy Detail` - Perkiraan ukuran triangle yang digunakan pada trim.
* `Legacy Hole smoothing` - Seberapa banyak triangle dirilekskan pada area yang diisi.
* `Legacy Threshold espilon` - Nilai yang dapat disesuaikan untuk meningkatkan algoritma pengisian lubang legacy.
* `Fill Detail` - Perkiraan ukuran triangle yang digunakan pada trim.

![](/videos/tool_trim.mp4)

### ![](/icons/tool_split.webp) Belah {#split}
Mirip dengan alat [Trim](#trim), kecuali Trim membuang seleksi, Split akan menyimpan seleksi sebagai objek baru.

#### Pengaturan belah {#split-settings}

* `Stroke painting` - Jika paint diaktifkan di menu paint, area yang ditambal akan diisi dengan warna yang saat ini dipilih.
* `Boolean` - mengisi lubang split menggunakan area quad poly. Area yang diisi akan datar.
* `Legacy` - mengisi lubang split dengan area triangulasi. Area yang diisi akan datar.
* `Fill` - mengisi lubang dengan area triangulasi. Area yang diisi akan berupa permukaan melengkung, seperti film gelembung sabun.
* `None` - tidak mengisi lubang.
* `Boolean Detail Shape` - Perkiraan ukuran quad dan triangle yang digunakan di sisi bentuk split.
* `Boolean Detail Hole` - Perkiraan ukuran triangle atau poly yang digunakan pada lubang split yang diisi. 
* `Legacy Detail` - Perkiraan ukuran triangle yang digunakan pada split.
* `Legacy Hole smoothing` - Seberapa banyak triangle dirilekskan pada area yang diisi.
* `Legacy Threshold espilon` - Nilai yang dapat disesuaikan untuk meningkatkan algoritma pengisian lubang legacy.
* `Fill Detail` - Perkiraan ukuran triangle yang digunakan pada split.

![](/videos/tool_split.mp4)


### ![](/icons/tool_project.webp) Proyeksi {#project}
Alat Project terlihat seperti alat [Trim](#trim), tetapi tidak menghapus atau membuat geometri apa pun, hanya memindahkan verteks agar sesuai dengan seleksi.

![](/videos/tool_project.mp4)

::: tip
Jika Anda menggunakan Project saat berada di layer, Anda dapat melakukan blend antara bentuk asli dan bentuk hasil proyeksi dengan slider layer.
:::

### ![](/icons/tool_layer.webp) Lapisan {#layer}
Mengangkat permukaan, tetapi membatasi tinggi.

Jika Anda terus menekan pensil dan terus menyapu area, Layer akan naik ke ketinggian tertentu lalu tidak lebih jauh, berbeda dengan alat lain yang akan terus menumpuk tinggi.

Perhatikan bahwa secara bawaan batas hanya diatur per stroke! Jika Anda memulai stroke baru, ia akan membangun dari tinggi permukaan baru.

Untuk mengatur tinggi maksimum konstan di banyak stroke, gunakan alat Layer dengan sistem [Layers](layers.md) Nomad.

Buat layer, dan gunakan alat ini. Tinggi maksimum sekarang diatur dari layer, sehingga Anda dapat menerapkan banyak sapuan kuas dan tinggi akan selalu sama.

`Sub` akan menggunakan kedalaman minimum, menciptakan alur.

#### Pengaturan lapisan {#layer-settings}

* `Use layer data` - Saat aktif, dan ketika sebuah layer dipilih, gunakan data layer untuk mengatur tinggi maksimum.
* `Inflate`- Saat aktif menyesuaikan arah kerja layer untuk mendapatkan hasil yang lebih halus.
* `Relax (Normal)` - Jumlah smoothing yang diterapkan pada normal.

![](/videos/tool_layer.mp4)


### ![](/icons/tool_flatten.webp) Mengembung {#inflate}
Memindahkan verteks sepanjang normalnya sendiri. `Sub` akan memindahkan verteks sepanjang normal terbalik.

#### Pengaturan mengembung {#inflate-setings}
* `Relax (Normal)` - Jumlah smoothing yang diterapkan pada normal.

![](/videos/tool_inflate.mp4)




### ![](/icons/tool_nudge.webp) Dorong {#nudge}
Memindahkan atau 'mengoles' titik ke arah stroke.

![](/videos/tool_nudge.mp4)


### ![](/icons/tool_stamp.webp) Stempel {#stamp}

Klik dan seret untuk mengangkat area patung dalam bentuk Alpha yang dipilih.

Ini hanyalah [Brush tool](#brush) dengan tipe stroke diatur ke `Lock + radius`. 

`Sub` akan mendorong stamp ke dalam alih-alih menariknya keluar dari permukaan.

::: tip
Stamp biasanya bekerja paling baik dengan geometri resolusi tinggi. Jika Anda mencari secara online 'wrinkles alpha', 'pores alpha', 'scales alpha' dll, tekstur alpha ini dan Stamp bisa menjadi cara hebat untuk menambah detail organik pada sculpt karakter.

Dua mode stroke berguna untuk hal yang berbeda. 

* `Lock + radius` memiliki *tinggi* yang tetap, menyeret akan menyesuaikan lebar dan rotasi stamp. Bagus untuk tekstur kulit yang perlu memiliki kedalaman/tinggi sama, tetapi rotasi dan skala berbeda untuk menyamarkan pola berulang.
* `Lock + intensity` memiliki *lebar* yang tetap, menyeret menyesuaikan rotasi dan tinggi stamp. Bagus untuk rivet, yang semuanya harus berukuran sama, tetapi rotasi dan tinggi berbeda. 

:::

![](/videos/tool_stamp.mp4)


### ![](/icons/tool_clearLayer.webp) Hapus Lapisan {#delete-layer}
Alat ini dapat mereset layer secara lokal, Anda memerlukan layer aktif jika tidak tidak akan terjadi apa-apa.

![](/videos/tool_delete_layer.mp4)


### ![](/icons/tool_tube.webp) Tabung {#tube}
Membuat tube dengan menggambar kurva. 
![](/images/tool_tube_new.webp)

Setelah tube dibuat, path dapat diedit dalam ruang 3D menggunakan kontrol serupa dengan alat [Shape editing](#shape-editing) dan pengeditan kurva standar. 

![](/videos/tool_tube.mp4)

#### Bilah alat kiri tabung {#tube-left-toolbar}

![](/images/tool_tube_left_toolbar.webp)

Toolbar kiri memiliki opsi berikut:

* `Sync` - Jika tube saat ini di-instance, dan ada child node dari tube yang berbeda antar instance, ini akan menyinkronkannya kembali.
* `Snap` - Saat aktif, mode curve dan path akan snap ke objek lain saat Anda menggambar. Saat tidak aktif, titik pertama akan snap, lalu sisa tube akan digambar pada kedalaman itu. Ia memiliki menu kecil:
    * `Offset` - Mengatur kedalaman snap; 0% akan membuat tengah penampang tube snap ke permukaan, nilai positif akan mengangkatnya dari permukaan, nilai negatif akan menurunkannya.
* `Curve` - Menggambar bebas sebuah tube. Ia memiliki menu kecil:
    * `Auto-validate` - Akan membuat tube segera setelah stroke selesai. Saat dinonaktifkan, lingkaran validasi hijau akan terlihat di sebelah path kurva, tekan untuk memvalidasi, atau gunakan tautan `Reset` yang muncul di menu ini untuk menghapus path.
    * `Closed` - membuat tube menjadi loop.
    * `Screen` - Hanya tersedia ketika Auto-validate dinonaktifkan. Saat aktif, path 'dipin' ke layar, memungkinkan Anda menggerakkan tampilan dan objek, dan path tetap di tempat. Saat tidak aktif, path adalah bagian dari scene 3D, dan akan bergerak bersama kamera dan objek.
    * `Accuracy` - Berapa banyak titik kurva yang akan digunakan untuk mengonversi path yang digambar menjadi tube. 0% akan menggunakan jumlah titik terendah, tetapi akan melewatkan perubahan kelengkungan kecil. 100% akan sangat akurat, dan menggunakan banyak titik.
* `Path` - Membuat tube dengan mengklik untuk mendefinisikan titik kurva. Ketuk lingkaran hijau untuk memvalidasi path. Ia memiliki menu kecil:
    * `B-spline` - Metode gambar kurva alternatif di mana titik kurva biasanya tidak berada langsung di kurva, tetapi dapat menghasilkan hasil yang lebih halus daripada metode bawaan.
    * `Closed` - membuat tube menjadi loop
    * `Screen` - Saat aktif, path 'dipin' ke layar, memungkinkan Anda menggerakkan tampilan dan objek, dan path tetap di tempat. Saat tidak aktif, path adalah bagian dari scene 3D, dan akan bergerak bersama kamera dan objek.

##### Bilah alat atas tabung {#tube-top-toolbar}
![](/images/tool_tube_toolbar.webp)
Ketika sebuah tube dipilih, toolbar akan muncul di bagian atas viewport dengan kontrol tambahan. Klik judul toolbar untuk meruntuhkan/memperluas toolbar, dan klik panah di kanan atas untuk memindahkan toolbar ke bagian atas atau bawah viewport.

* `Validate` - memanggang tube menjadi poligon biasa sehingga dapat dipahat.
* `Edit` - menampilkan titik kurva sehingga dapat dimanipulasi
* `Mirror` - menambahkan mirror repeater sebagai parent dari kurva ini
* `Snap` - men-snap titik kurva ke permukaan terdekat
* `Closed` - Menggabungkan awal dan akhir kurva menjadi loop
* `B-spline` - Beralih antara interpolasi Catmull-rom dan B-spline.
* `Cap` - Berputar antara cap di kedua ujung tube, atau hanya awal atau akhir, atau tanpa cap.
* `Hole` - Menambahkan ketebalan ke tube, mengubahnya menjadi pipa. Berputar antara memiliki lubang di kedua ujung, hanya di ujung, atau tanpa lubang. 
* `Radius` - Berputar antara radius seragam, radius di awal dan akhir, atau radius per titik kurva. Ini diedit dengan handle oranye pada kurva.
* `Twist` - Berputar antara tanpa twist, twist seragam, twist di awal dan akhir, atau twist per titik kurva. Ini diedit dengan handle merah muda pada kurva.
* `Profile` - Berputar antara tanpa profil (jadi profil lingkaran), profil seragam, profil di awal dan akhir, atau profil per titik.
* `Profile edit` - Menampilkan editor profil. Ini berfungsi mirip dengan alat [Shape editing](#shape-editing), dapat menyimpan dan memuat preset profil, dan memiliki toggle untuk memungkinkan Anda mengedit profil dalam ruang 3D.
* `Spiral` - Mengaktifkan menu untuk menambahkan twist spiral ke tube. Menu ini memiliki opsi `Twist Angle`, `Offset`, `Scale`, dan `Angle offset`.
* `X Divisions` - jumlah divisi di sekitar tube, 4 divisi akan membuat tube persegi misalnya. 
* `Constant density` - saat aktif, akan menjaga poligon tetap persegi. saat dinonaktifkan, akan memungkinkan Anda mengatur `Y divisions` sepanjang panjang tube.
* `...` - Menu pengaturan Tube.

#### Toggle hapus titik kurva {#curve-point-delete-toggle}

![](/images/tool_tube_delete_toggle.webp)

Di bawah toolbar ada toggle hapus titik kurva. Ketika Anda menyeret titik kurva dekat dengan yang lain, ia akan berubah merah, menunjukkan bahwa jika Anda melepaskan, titik akan dihapus. Jika Anda melakukan edit kecil dan tidak ingin menghapus titik, tombol ini akan menonaktifkan perilaku hapus titik.



#### Pengaturan tabung {#tube-settings}
* `Primitive` - tombol untuk mengaktifkan/nonaktifkan UV, atau untuk memvalidasi tube.
* `Post subdivision` - pintasan untuk mengatur level multiresolution sebelum memvalidasi.
* `Linear subdivision` - pintasan untuk mengatur level linear subdivision sebelum memvalidasi. 
* `Division X` - sama dengan X Divisions di toolbar.
* `Division Y` - sama dengan Y Divisions di toolbar.
* `Curve (Repeater)` - mengonversi tube menjadi [Curve Repeater](scene.md#curve)

::: tip
Divisions di 4 dan Post subdivision di 3 akan membuat tube ujung bulat yang halus, bagus untuk cacing, ular, bagian tubuh.
:::


### ![](/icons/tool_lathe.webp) Bubut {#lathe}
Membuat permukaan revolusi dengan menggambar kurva.

Alat ini bagus untuk bentuk seperti vas, gelas anggur.

![](/videos/tool_lathe.mp4)

#### Bilah alat kiri bubut {#lathe-left-toolbar}

![](/images/tool_lathe_left_toolbar.webp)

Toolbar kiri memiliki opsi berikut:

* `Sync` - Jika lathe saat ini di-instance, dan ada child node dari lathe yang berbeda antar instance, ini akan menyinkronkannya kembali.
* `Fixed` - Saat diaktifkan, pusat lathe tetap dan ditampilkan di layar. Garis pusat ini memiliki titik edit yang dapat disesuaikan. Saat dinonaktifkan, pusat lathe akan diperbarui secara dinamis agar sesuai dengan awal dan akhir kurva yang digambar.
* `Curve` - Menggambar profil lathe dalam satu stroke. Ia memiliki menu kecil:
    * `Auto-validate` - Saat diaktifkan, lathe akan dibuat ketika pensil diangkat dari layar. Saat dinonaktifkan, lingkaran hijau di sebelah kurva dapat ditekan untuk membuat lathe. Kurva dapat dihapus dengan tombol `Reset`.
    * `Closed` - Menggabungkan awal dan akhir kurva menjadi loop
    * `Screen` - Hanya tersedia ketika Auto-validate dinonaktifkan. Saat aktif, path 'dipin' ke layar, memungkinkan Anda menggerakkan tampilan dan objek, dan path tetap di tempat. Saat tidak aktif, path adalah bagian dari scene 3D, dan akan bergerak bersama kamera dan objek.
    * `Accuracy` - Berapa banyak titik kurva yang akan digunakan untuk mengonversi path yang digambar menjadi tube. 0% akan menggunakan jumlah titik terendah, tetapi akan melewatkan perubahan kelengkungan kecil. 100% akan sangat akurat, dan menggunakan banyak titik.
* `Path` - Membuat lathe dengan mengklik untuk mendefinisikan titik kurva. Ketuk lingkaran hijau untuk memvalidasi path. Ia memiliki menu kecil:
    * `B-spline` - Metode gambar kurva alternatif di mana titik kurva biasanya tidak berada langsung di kurva, tetapi dapat menghasilkan hasil yang lebih halus daripada metode bawaan.
    * `Closed` - membuat tube menjadi loop
    * `Screen` - Saat aktif, path 'dipin' ke layar, memungkinkan Anda menggerakkan tampilan dan objek, dan path tetap di tempat. Saat tidak aktif, path adalah bagian dari scene 3D, dan akan bergerak bersama kamera dan objek.

#### Bilah alat atas bubut {#lathe-top-toolbar}
![](/images/tool_lathe_top_toolbar.webp)

Ketika sebuah lathe dipilih, toolbar akan muncul di bagian atas viewport dengan kontrol tambahan. Klik judul toolbar untuk meruntuhkan/memperluas toolbar, dan klik panah di kanan atas untuk memindahkan toolbar ke bagian atas atau bawah viewport.

* `Validate` - memanggang lathe menjadi poligon biasa sehingga dapat dipahat.
* `Edit` - menampilkan titik kurva sehingga dapat dimanipulasi
* `Mirror` - menambahkan mirror repeater sebagai parent dari lathe ini
* `Snap` - men-snap titik kurva ke permukaan terdekat
* `Stable` - Saat diaktifkan, profil kurva akan diparent ke garis pusat lathe. Saat dinonaktifkan, garis pusat dapat diedit dan tidak akan memindahkan kurva, memungkinkan bentuk yang lebih kompleks.
* `Focus` - Akan memutar tampilan untuk melihat profil kurva rata sempurna terhadap kamera.
* `Closed` - Menggabungkan awal dan akhir kurva menjadi loop
* `Cap` - Jika Closed dinonaktifkan, berputar antara cap di kedua ujung tube, atau hanya awal atau akhir, atau tanpa cap.
* `Hole` - Menambahkan ketebalan ke lathe, mengubahnya menjadi pipa. Berputar antara memiliki lubang di kedua ujung, hanya di ujung, atau tanpa lubang. 
* `B-spline` - Beralih antara interpolasi Catmull-rom dan B-spline.
* `X Divisions` - jumlah divisi di sekitar tulathebe, 4 divisi akan membuat profil lathe persegi misalnya. 
* `Constant density` - saat aktif, akan menjaga poligon tetap persegi. saat dinonaktifkan, akan memungkinkan Anda mengatur `Y divisions` sepanjang panjang tube.
* `...` - Menu pengaturan Lathe.

#### Pengaturan bubut {#lathe-settings}
* `Primitive` - tombol untuk mengaktifkan/nonaktifkan UV, atau untuk memvalidasi tube.
* `Post subdivision` - pintasan untuk mengatur level multiresolution sebelum memvalidasi.
* `Linear subdivision` - pintasan untuk mengatur level linear subdivision sebelum memvalidasi. 
* `Division X` - sama dengan X Divisions di toolbar.
* `Division Y` - sama dengan Y Divisions di toolbar.
* `Curve (Repeater)` - mengonversi profil kurva menjadi [Curve Repeater](scene.md#curve)

### ![](/icons/tool_insert.webp) Sisipkan {#insert}
Menempatkan objek di permukaan objek lain. Dalam penggunaan mirip dengan alat stamp, tetapi untuk bentuk 3D penuh.

Jika Anda memilih primitif dari toolbar kiri, klik-seret pada permukaan apa pun akan menempatkan primitif di tempat Anda mengklik, seret akan mengatur ukuran. Setelah Anda selesai menyeret, Insert akan beralih ke mode [Transform](#transform).

Dalam mode Instance, menyeret akan membuat dan menggeser instance baru di atas permukaan. Ukuran akan diduplikasi dari bentuk pertama, dengan cara ini Anda dapat menempatkan banyak instance berukuran sama dari sebuah objek di atas permukaan lain.

Anda tidak harus hanya menyisipkan primitif! Pilih *bentuk apa pun* di outliner, jika Insert dalam mode Instance atau Clone, Anda dapat menyeret salinan objek yang dipilih di atas permukaan lain.

Jika sebuah objek memiliki pivot kustom, maka itu akan digunakan sebagai titik jangkar. Lihat video di bawah.

![](/videos/tool_insert.mp4)

### ![](/icons/tool_transform.webp) Transformasi {#transform}
Memindahkan/Memutar/Menskala model secara langsung dengan 1 dan 2 jari, biasanya di atas permukaan objek lain.

Alat dikendalikan dengan toolbar kiri, dan memiliki 5 tombol:

* `Snap` - men-snap model ke permukaan lain
* `Group` - Jika objek yang dipilih memiliki kombinasi objek dan instance, ini memungkinkan Anda menentukan perilaku alat.
* `Move` - Seret satu jari akan memindahkan objek. Saat snap aktif, ini akan menggeser objek sepanjang permukaan di bawah jari Anda.
* `Rotate` - Seret satu jari akan memutar objek. Saat snap aktif, akan memutar di sekitar normal permukaan di bawah jari Anda.
* `Scale` - Seret satu jari akan menskala objek.

Transform dapat digunakan untuk mengoperasikan 2 mode ini dengan cepat menggunakan 2 jari:

* Seret objek untuk menempatkannya. Berhenti menggerakkan jari pertama Anda, tetapi jangan angkat dari layar.
* Sentuhkan jari kedua Anda di layar sambil tetap menahan jari pertama. Saat jari kedua diseret, objek akan diskalakan.
* Angkat jari kedua, dan lanjutkan menyeret jari pertama, objek akan kembali dalam mode move.

Anda juga dapat mengubah mode kedua dengan gesture ketukan jari kedua:

* Seret objek untuk menempatkannya, berhenti menggerakkan, tetapi jangan angkat jari Anda dari layar.
* Ketuk jari kedua Anda sambil menahan jari pertama
* Alat ditukar ke mode rotasi. Seret jari pertama Anda untuk mengatur rotasi.
* Ketuk jari kedua seperti sebelumnya, alat ditukar kembali ke mode move.

Ini menghadirkan alur kerja cepat untuk mengkloning objek di atas yang lain, misalnya batu di atas lanskap. Perhatikan bahwa tombol clone juga ada di toolbar kiri untuk akses mudah:

* Gunakan alat transform untuk memindahkan batu ke tempatnya.
* Lepaskan, tekan tombol clone
* Pindahkan batu ini, putar/skalakan sesuai kebutuhan
* Lepaskan, tekan tombol clone
* Pindahkan batu ini, ulangi.

![](/videos/tool_transform.mp4)

### ![](/icons/tool_gizmo.webp) Gizmo {#gizmo}
Alat ini memungkinkan Anda memindahkan, memutar dan menskala objek, serta mengubah pivot objek.

Handle viewport memiliki fitur berikut:

* `Move` - Seret pada garis+panah untuk memindahkan pada X/Y/Z. Seret pada titik persik di tengah gizmo untuk translasi bebas dalam ruang layar. Klik pada kotak merah, hijau, biru untuk translasi pada bidang X/Y/Z.
* `Rotate` - Seret pada lingkaran merah/hijau/biru untuk rotasi pada X/Y/Z. Seret bola di dalam lingkaran untuk rotasi bebas.
* `Scale`- Seret pada titik merah/hijau/biru luar untuk skala pada X/Y/Z. Seret pada kerucut merah/hijau/biru luar untuk skala pada bidang X/Y/Z. Seret pada lingkaran persik luar untuk skala seragam.

![](/images/tool_gizmo.webp)

#### Node dan verteks {#nodes-and-vertices}

Setiap objek di Nomad terdiri dari node dan verteks:

* `Node` - 'Handle' objek, yang menyimpan translasi, rotasi, skala, disebut matriks transformasinya.
* `Vertices` - Titik yang mendefinisikan permukaan objek, menyimpan informasi posisi dan cat.

Jika Anda memiliki kotak sederhana yang terdiri dari 8 verteks, Anda dapat mentranslasikannya dengan memodifikasi matriks transformasinya, atau dengan memodifikasi posisi verteks. Saat memahat Anda biasanya ingin memodifikasi verteks, saat memindahkan objek dengan gizmo, Anda biasanya ingin memodifikasi node. Nomad memungkinkan Anda melakukan keduanya. 

#### Bilah alat menu kiri {#left-menu-toolbar}

Toolbar kiri mengontrol apakah gizmo akan bekerja pada node atau verteks, serta fungsi lainnya:

* `Clone` - Membuat salinan mandiri dari objek saat ini, yang dapat diseret menjauh dengan gizmo.
* `Instance` - Membuat salinan instance dari objek saat ini. Objek saling tertaut, sehingga perubahan sculpting pada satu objek akan muncul di semua objek instance.
* `Group/Object/Vertex/Auto` - Akan mengatur apakah gizmo akan memengaruhi node atau verteks objek. Mode 'auto' bawaan akan mencoba tebakan terbaik. Jika ada beberapa objek yang diparent bersama dalam hierarki, 'Object' hanya akan memindahkan objek saat ini, objek anak akan tetap diam. Gizmo juga dapat mempertimbangkan masking dan simetri.
* `Pin` - Secara bawaan gizmo akan berpindah ke pivot objek yang dipilih. Saat pin diaktifkan, gizmo akan tetap di tempatnya saat ini.
* `Align` - Beralih antara pivot disejajarkan dengan objek saat ini, atau disejajarkan dengan dunia.
* `Snap rotation` - Mengaktifkan nilai rotasi yang di-snap ke kelipatan, nilai snap ditampilkan dan dapat diedit saat snap aktif.
* `Snap translation` - Mengaktifkan nilai translasi yang di-snap ke kelipatan, nilai snap ditampilkan dan dapat diedit saat snap aktif.
* `Pivot` - Saat diaktifkan, gizmo dapat dipindahkan dan diputar tanpa memindahkan objek. Ia memiliki menu tambahan yang dijelaskan di bawah.

#### Pivot {#pivot}
Saat mode pivot aktif, sebuah menu ditampilkan untuk memungkinkan perubahan pivot cepat:

**Reset** 
* `Center` - Memindahkan pivot ke pusat objek
* `Bottom` - Memindahkan pivot ke bagian bawah objek
* `Align` - Mereset rotasi agar sejajar dengan dunia.
* `Mask` - Memindahkan pivot ke pusat area tak ter-mask.

**On Tap**
* `None` - tidak melakukan apa-apa saat objek diketuk
* `Normal` - Memindahkan dan memutar pivot agar sejajar dengan tempat permukaan diketuk
* `First` - Memindahkan (tetapi tidak memutar) pivot ke tempat permukaan diketuk
* `Medial` - Memindahkan pivot ke tengah objek, di bawah tempat permukaan diketuk.

#### Pengaturan gizmo {#gizmo-settings}

![](/images/tool_gizmo_settings.webp)

##### Matriks {#matrix}
* ![](/icons/target.webp) `Move origin` - Memindahkan objek sehingga pivot-nya berada di pusat scene, disebut origin.
* ![](/icons/bake.webp)  `Bake` - Membekukan objek di tempat saat ini, dan mengatur nilai translate/rotate ke 0, scale ke 1.
* ![](/icons/bake.webp) -> ![](/icons/tool_gizmo.webp) `Bake Pivot` - Membuat nilai matriks sesuai dengan posisi handle gizmo di dunia.
* ![](/icons/reset.webp) `Reset` - Pintasan yang mengatur nilai translasi ke 0, rotasi ke 0, skala ke 1, memindahkan dan memutar objek.

::: tip Bake vs bake to pivot
Buat kotak, pilih alat Gizmo, buka dan pin menu settings. Secara bawaan translasi dan rotasi adalah 0, skala 1.

Aktifkan mode pivot, pindahkan handle ke satu sisi, nonaktifkan mode pivot. Pivot telah berubah, tetapi perhatikan bahwa nilai translasi masih 0. 

Jika Anda ingin melihat di mana pivot *sebenarnya* berada, klik `Bake Pivot`. Sekarang nilai translasi diperbarui. Perhatikan kotak tidak bergerak selama operasi ini, maupun dalam mode pivot.

Pindahkan dan putar kotak ke suatu tempat, lalu ketuk `Move Origin`. Ini memindahkan objek sehingga pivot-nya berada di pusat dunia, tetapi membiarkan rotasi tidak berubah.

Klik `Reset`, dan rotasi akan diatur ke 0 juga.

Pindahkan dan putar kotak lagi, kali ini klik `Bake`. Pivot tetap di tempatnya, kotak tetap di tempatnya, tetapi nilai translasi dan rotasi diatur ke 0.

Latih ini beberapa kali! Pahami bahwa nilai pivot tersembunyi, Nomad mengurusnya untuk Anda, tetapi jika Anda perlu mengatur pivot ke lokasi nyata di ruang, Bake pivot akan melakukannya untuk Anda.

:::

* `Translation` - nilai translate X, Y, Z
* `Rotation` - nilai rotate X, Y, Z
* `Scale` - Skala seragam jika diaktifkan, atau skala X, Y, Z jika dinonaktifkan.
* `Uniform scale` - Beralih kemampuan untuk skala seragam atau independen di tiap sumbu

-----

* `Compact` - beralih tata letak gizmo untuk menempatkan handle tambahan di luar atau di dalam bola rotasi
* `Widget size` - ukuran gizmo
* `Thickness` - ukuran garis pada gizmo
* `Opacity` - opasitas gizmo
* `Hide on interaction` - beralih apakah gizmo harus disembunyikan sementara saat diseret

-----

* `Tangent roll threshold` - Mengontrol bagaimana UI rotasi berperilaku saat menyeret pada handle lingkaran untuk rotasi pada X/Y/Z. Jika nilai ini 0, rotasi bekerja seperti dial, seret gizmo melingkar. Jika nilai ini 90, rotasi bekerja seperti menarik tali yo-yo; seret dalam garis lurus menuju atau menjauh dari tempat Anda pertama kali mengklik. Nilai antara 0 dan 90 akan melakukan kombinasi keduanya; di bawah nilai akan menjadi gerakan linear, di atas nilai akan menjadi gerakan melingkar.
* `Numerical input` - saat diaktifkan, satu ketukan pada gizmo akan memunculkan jendela untuk memasukkan nilai tepat untuk sumbu widget yang diketuk.

::: warning
[Gizmo](#gizmo), [Translate](#translate), [Rotate](#rotate) dan [Scale](#scale) menggunakan checkbox simetri mereka sendiri!

Secara bawaan simetri ini dimatikan.
:::

Di sebelah kiri Anda dapat memindahkan pivot gizmo, Anda dapat melihat video di bawah dalam aksi.
Ini sangat berguna untuk rotasi, karena tidak mengubah apa pun untuk translasi.

![](/videos/tool_gizmo.mp4)

### ![](/icons/tool_faceGroup.webp) Facegroup {#facegroup}

Facegroup memungkinkan Anda mengorganisir objek menjadi face dengan warna berbeda. Anda dapat menggunakan grup ini dengan banyak cara di Nomad:

* Metode seleksi cepat untuk mask
* Menyembunyikan/menampilkan bagian objek
* Mengorganisir objek tanpa harus memecahnya menjadi bagian terpisah
* Mendefinisikan region UV
* Membimbing quad remesher
* Kontrol tambahan untuk alat seperti smooth.

#### Bilah alat kiri Facegroup {#facegroup-left-toolbar}

* `Patch ` - Menampilkan facegroup yang tersedia sebagai patch. Patch yang tidak digunakan dapat dihapus. Ketuk patch untuk mengganti nama atau mengubah warnanya. Ikon plus memungkinkan Anda membuat patch baru.
* `Dot` - Melukis pada objek untuk mendefinisikan facegroup. Saat '+ Face Group' diaktifkan, setiap stroke baru akan otomatis membuat facegroup baru, berguna untuk cepat mendefinisikan region. Ketukan akan flood fill region yang dipilih. Slider mengatur radius dot.
* `Relax` - Menghaluskan batas facegroup. Sangat berguna untuk mendefinisikan tepi bersih untuk quad remeshing, atau untuk mendefinisikan panel untuk pemodelan hard surface. Slider mengontrol radius dan intensitas operasi relax.
* `Shape selector` - Membuat facegroup dengan bentuk alih-alih kuas, melalui `Lock+Radius`, `Lasso`, `Polygon`, `Rect` dan `Ellipse`. Lihat [Shape Selector](#shape-selector) untuk info lebih lanjut.
* `Auto-pick` - Saat diaktifkan, akan memilih patch tempat stroke dimulai, dan menerapkan patch itu untuk sisa stroke. Sangat berguna untuk merapikan region facegroup; jika facegroup telah meluas terlalu jauh, aktifkan auto-pick, mulai stroke dari tempat patch facegroup benar, dan seret ke batas untuk menetapkan ulang patch yang benar.

### ![](/icons/tool_hide.webp) Sembunyikan {#hide}
Menyembunyikan atau mengisolasi bagian objek. 

Mode utama dikendalikan dari menu kiri:

* `Dot` - Menggosok pada objek untuk menyembunyikan bagian objek.
* `Shape selector` -  Menyembunyikan dengan bentuk alih-alih kuas, melalui `Lasso`, `Polygon`, `Line`, `Rect` dan `Ellipse`. Lihat [Shape Selector](#shape-selector) untuk info lebih lanjut.
* `Show` - membalik operasi, sehingga mode yang dipilih akan menampilkan alih-alih menyembunyikan bagian objek.

Toolbar akan muncul di bagian atas viewport dengan kontrol tambahan:

* `Clear` - Mengembalikan objek, semua bagian tersembunyi akan ditampilkan.
* `Invert` - Menukar bagian tersembunyi dan terlihat.
* `Facegroup` - Menggunakan facegroup untuk cepat menyembunyikan bagian, mengetuk facegroup akan menyembunyikan seluruh facegroup.
* `Mask` - Jika mask aktif, mengetuk tombol ini akan menyembunyikan bagian yang di-mask.
* `Delete` - Menghapus bagian objek yang tersembunyi
* `Split` - Memisahkan bagian objek yang tersembunyi menjadi bentuk baru.

### ![](/icons/tool_measure.webp) Ukur {#measure}
Seret untuk mengukur jarak antara 2 titik.

### ![](/icons/tool_remesh.webp) Quad Remesher {#quad-remesher}

![](/images/tool_quadremesher.webp)

Alat ini akan mengonversi objek yang dipilih menjadi tata letak topologi quad yang bersih, dengan kontrol untuk kepadatan, aliran edge, simetri. 

::: tip
Quad Remesher dikembangkan oleh [Exoside](https://exoside.com/) untuk iOS dan desktop. 

Untuk iOS ini adalah pembelian dalam aplikasi di dalam Nomad, pembayaran satu kali sebesar $16USD.

Untuk desktop, beli lisensi dari [Exoside](https://exoside.com/quadremesher/quadremesher-buy/). Anda dapat membelinya hanya untuk Nomad desktop, atau lisensi lintas semua aplikasi desktop yang didukung.

Jika Anda sudah memiliki Quad Remesher untuk aplikasi desktop lain, Anda dapat [membeli upgrade ke semua platform dengan biaya lebih rendah.](https://exoside.com/quadremesher/quadremesher-upgrade/)

Quad Remesher tidak tersedia untuk Android. Android dapat menggunakan 'Quad Remesh - Instant' open source gratis yang tersedia di bawah menu Topology -> Misc, tetapi pahami bahwa set fiturnya sangat terbatas.
:::

When alat ini diaktifkan untuk pertama kali, alat ini akan menanyakan apakah Anda ingin mengaktifkannya sebagai pembelian dalam aplikasi. Setelah aktif, bilah alat kiri dan atas akan diaktifkan.

* `Dot` - Kuas ini akan mengatur kerapatan target. Intensitas 100% akan melukis dengan warna merah, yang akan menggunakan dua kali kerapatan quad target di area tersebut. Intensitas 0% akan melukis dengan warna sian, yang akan menggunakan setengah kerapatan quad target di area tersebut. Intensitas 50% akan melukis dengan warna abu-abu, yang akan menggunakan kerapatan quad target bawaan.
* `Smooth` - Menghaluskan transisi kerapatan merah/abu-abu/sian.
* `Curve` - Menggambar kurva di permukaan sculpt, quad remesher akan menggunakannya sebagai panduan aliran edge. Ketuk sebuah kurva untuk menghapusnya.
* `Path` - Menggambar path di permukaan sculpt, quad remesher akan menggunakannya sebagai panduan aliran edge. Ketuk sebuah path untuk menghapusnya. 
* `Rect` - Menggambar persegi panjang di permukaan sculpt, quad remesher akan menggunakannya sebagai panduan aliran edge. Ketuk sebuah path untuk menghapusnya.
* `Ellipse` - Menggambar elips di permukaan sculpt, quad remesher akan menggunakannya sebagai panduan aliran edge. Ketuk sebuah path untuk menghapusnya.

#### Bilah alat atas Quad remesher {#quad-remesher-top-toolbar}
![](/images/tool_quadremesher_toolbar.webp)

Sebuah bilah alat akan muncul di bagian atas viewport dengan kontrol tambahan:


* `<Count>` - Klik ini untuk memulai proses quad remesher, angka ini memberi tahu Anda berapa target jumlah quad remesh.
* `Quads` - Mengatur target jumlah quad dengan menggeser ke kiri dan kanan, atau ketuk untuk mengatur angka pasti. Perhatikan bahwa ini lebih merupakan panduan daripada angka tetap, berbagai kontrol pada quad remesher sering kali membuat hasilnya tidak persis sama dengan target ini.
* `Half` - Pintasan untuk mengatur target jumlah menjadi setengah jumlah poly saat ini.
* `Same` - Pintasan untuk mengatur target jumlah menjadi sama dengan jumlah poly saat ini.
* `Guides` - menunjukkan total jumlah guide, atau ketuk untuk menghapus semua guide.
* `Density X` - ketuk untuk menghapus semua pengecatan kerapatan.
* `Density (painting)` - toggle untuk menggunakan atau mengabaikan pengecatan kerapatan.
* `Face Group` - toggle untuk menggunakan atau mengabaikan facegroup untuk mengarahkan quad remesher.
* `Relax` - toggle untuk secara otomatis merelaksasi batas facegroup selama quad remeshing. Jika Anda sudah merelaksasi/menghaluskan batas facegroup, nonaktifkan opsi ini.
* `Relax Slider` - Slider pintasan untuk merelaksasi batas facegroup.
* `Hard Edges` - toggle untuk mencoba mempertahankan hard edge.
* `Reproject Vertex` - toggle untuk memproyeksikan ulang tata letak baru ke mesh input.
* `Symmetry` - Toggle untuk mengaktifkan hasil simetris. Perhatikan bahwa simetri selalu dihitung di sekitar sumbu x dunia, jadi pastikan model Anda berada di origin jika Anda mengharapkan hasil simetris.
* `...` - Menu pengaturan Quadremesher. 

#### Menu pengaturan Quad remesher {#quad-remesher-settings-menu}

Sebagian besar pengaturan ini tersedia di bilah alat atas.

* `<Count>, Half, Same` - Sama seperti tombol Remesh, Half, Same di bilah alat atas.
* `Target Quads` - Sama seperti tombol `Quads` di bilah alat atas
* `Adaptive quad count` - toggle untuk mengaktifkan penggunaan quad yang lebih kecil di area dengan kelengkungan tinggi, dan quad yang lebih besar di kelengkungan rendah.
* `Adaptive size` - Mengatur jumlah adaptivitas. 100% akan mengizinkan ukuran adaptif maksimum, pada 0% quad akan seragam.
* `Auto-Detect Hard Edges` - toggle untuk menyesuaikan tata letak quad remesh agar lebih mengikuti permukaan tajam.
* `Density (painting)` - Sama seperti tombol `Density (painting)` di bilah alat atas
* `Reproject Vertex` - toggle untuk memproyeksikan ulang tata letak baru ke mesh input.
* `Face Group` - Sama seperti tombol `Face Group` di bilah alat atas
* `Relax Slider` - Slider pintasan untuk merelaksasi batas facegroup.

::: tip

Resep untuk mendapatkan quad remesh yang baik dengan artefak minimal:

* Facegroup mesh untuk mendefinisikan aliran quad ideal Anda.
* Facegroup relax untuk mendapatkan batas facegroup yang halus.
* Decimate. Ini akan memastikan Anda tidak memiliki face tipis atau terdistorsi di tepi facegroup. Di pengaturan decimate pastikan facegroup diaktifkan. Ini akan membuat edge segitiga mengikuti edge facegroup Anda secara presisi. 

Di opsi quad remesh pastikan relax dinonaktifkan (karena Anda sudah merelaksasi mesh) dan Anda seharusnya mendapatkan hasil yang baik.

:::

### ![](/icons/tool_select.webp) Pilih {#select}
Gunakan mode bentuk untuk memilih objek di scene. `Unselect` akan menghapus objek dari seleksi.

### ![](/icons/tool_view.webp) Tampilan {#view}
"Alat" ini tidak melakukan apa pun secara khusus, ini hanyalah cara untuk melihat model tanpa memodifikasi scene Anda.


## Menu konteks kotak alat {#toolbox-context-menu}

![](/images/tools_context_menu.webp)

Klik kanan atau tekan lama pada sebuah alat di toolbox akan memunculkan menu konteks. Menu ini memiliki opsi berikut:

* `Save` - menyimpan perubahan apa pun yang Anda buat pada alat
* `Clone` - menduplikasi alat menjadi pintasan alat baru
* `Last save` - mengembalikan ke versi alat yang terakhir disimpan
* `Icon` - mengubah ikon untuk alat
* `Reset` - mengatur ulang alat ke setelan defaultnya