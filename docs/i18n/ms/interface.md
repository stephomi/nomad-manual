# ![](/icons/interface.webp) Menu Antara Muka 

Menu ini mengawal banyak pilihan untuk menyesuaikan antara muka Nomad. 

![](/images/interface_overview2.webp)

Nomad boleh disesuaikan pada tahap yang agak mendalam, menu ini dibahagikan kepada 4 bahagian; Interface, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
Halaman ini adalah untuk menu antara muka, bukan antara muka itu sendiri! Antara muka keseluruhan diterangkan dalam [Getting Started](gettingstarted.md).
:::

## Interface 

Bahagian interface membolehkan anda menambah pintasan, mencipta bar alat terapung, dan mengawal warna, saiz, rupa antara muka pengguna Nomad.

![](/images/interface_overview3.webp)

### Add shortcuts (bottom)...
![](/images/interface_shortcuts.webp)

Bar alat bawah mempunyai pintasan berikut didayakan secara lalai:
* `Undo` - batalkan operasi sebelumnya
* `Redo` - pulihkan operasi yang dibatalkan sebelum ini
* `Solo` - Sembunyikan sementara semua objek lain, hanya meninggalkan objek yang dipilih kelihatan. Tekan sekali lagi untuk memulihkan semua objek.
* `X-ray` - Jadikan sementara semua objek lain separa telus, hanya meninggalkan objek yang dipilih kelihatan pejal. Tekan sekali lagi untuk memulihkan bahan lalai.
* `Voxel remesh` - Remesh objek semasa menggunakan resolusi voxel yang terakhir digunakan. Tekan lama atau leret ke atas akan memaparkan peluncur resolusi dan togol tepi tajam.
* `Grid` - Togol grid paparan. Tekan lama atau leret ke atas akan membolehkan anda menukar warna dan kelegapan grid.
* `Wireframe` - Togol lapisan wireframe. Tekan lama atau leret ke atas akan membolehkan anda menukar warna dan kelegapan wireframe.
* `Inspector` - membolehkan anda melihat sifat mesh anda seperti uv, tekstur bakar, sifat lain, yang ditindih pada latar belakang Nomad.
* `Face Group` - Togol lapisan facegroup, maklumat lanjut di [Tools->FaceGroup](tools.md#facegroup) 

Pintasan biasa lain tersedia daripada menu ini, banyak lagi boleh ditemui dalam butang bindings.

#### ![](/icons/more.webp) Bindings

Hampir setiap fungsi Nomad boleh ditambah ke bar alat pintasan melalui butang bindings. Menu bindings akan dipaparkan apabila butang diklik:

![](/images/interface_bindings_search.webp)

Anda boleh mencari mengikut kategori melalui ikon di bahagian atas, atau gunakan medan carian untuk mencari fungsi mengikut nama. Klik pada fungsi untuk menambahkannya ke bar alat. Klik sekali lagi untuk mengeluarkannya.

#### ![](/icons/list.webp) Order

Ini akan memaparkan senarai pintasan. Tekan lama kemudian seret untuk menyusun semula pintasan.

#### ![](/icons/reset.webp) Reset

Reset akan memulihkan bar alat bawah kepada tetapan lalai.

### Add shortcuts (window)... +
![](/images/interface_add_shortcuts_window.webp)

Mengklik + akan menambah bar alat terapung. Ia tidak akan kelihatan sehingga anda mengklik butang bindings dan menambah beberapa pintasan padanya, kemudian anda boleh menjadikannya kelihatan. 

Anda boleh membuat banyak bar alat, setiap bar alat mempunyai pilihan berikut dalam menu ini:

* ![](/icons/checked.webp) `Visible` - Togol keterlihatan untuk bar alat
* ![](/icons/more.webp)`Bindings` - Paparkan tetingkap binding untuk memilih fungsi untuk ditambah atau dikeluarkan daripada bar alat.
* ![](/icons/list.webp)`Order` - Paparkan menu untuk menyusun semula bar alat.
* ![](/icons/reset.webp) `Reset` - Tetapkan semula bar alat kepada keadaan lalai.
* ![](/icons/resize_bottom_right.webp) `Resize corner` - Togol pemegang saiz semula di sudut kanan bawah bar alat.
* ![](/icons/sort_down.webp) `Collapsable` - Togol pemegang runtuh di sudut kanan atas.
* ![](/icons/trash.webp) `Delete` - Padam bar alat.

### Toolbox

Pilihan untuk menu alat di sebelah kanan antara muka Nomad.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Ui Resize Corner

Togol pemegang saiz semula di sudut bawah bar alat.

#### Hidden
Biasanya ikon toolbox di bar atas akan bertogol antara satu lajur panjang tunggal, atau senarai berbilang lajur alat. Pilihan ini akan bertogol antara senarai berbilang lajur, atau disembunyikan.

#### Colored
Kod warna ikon mengikut kategori, contohnya semua alat mask berwarna coklat, alat split merah, alat flatten hijau dan sebagainya.

#### Rows: Auto (>1)

#### Rows: Auto (>1)

#### Reset order
Tetapkan semula alat lalai dalam toolbox kepada susunan lalai. Ikon tersuai akan kekal dalam toolbox di hujung senarai.


### Presets

![](/images/interface_presets.webp)

Koleksi praset warna untuk antara muka.

#### High-contrast button
Gaya alternatif untuk butang yang menjadikannya lebih kelihatan apabila didayakan. Jika ditetapkan pada Auto, Nomad akan menggunakan mod ini apabila kontras warna UI antara dihidupkan/dimatikan adalah rendah.

#### Color widget/Color base
Warna utama yang digunakan dalam antara muka.

#### Transparent panel, Color panel, Blur strength
![](/images/interface_transparent.webp)
Apabila didayakan, pilihan tambahan akan muncul untuk mengawal rupa menu dan panel dalam Nomad. Warna, ketelusan dan jumlah kabur boleh dilaraskan.

::: tip
Pada peranti kecil adalah berguna untuk menjadikan panel warna hampir putih, telus, dan kekuatan kabur rendah, supaya menu tidak mengaburi paparan adegan.
:::

----

### Mirror top bar
Songsangkan susunan menu di bar atas.

### Mirror side bars
Tukar bar sisi supaya toolbox berada di kiri, pilihan alat di kanan.

### Mirror bottom bar
Alihkan bar bawah ke sudut kanan bawah, dan songsangkan susunan butang

### Material color preview
Apabila anda memilih warna untuk bahan, pratonton bahan ini dipaparkan pada objek yang sedang dipilih.

----
### Help popup on hover

Untuk peranti yang menyokong hover, tetapkan sama ada bantuan konteks dalam Nomad yang diwakili dengan ikon ![](/icons/help.webp) akan muncul apabila hover, atau hanya apabila diklik.

----

### Overall scale
Pengganda saiz pada semua elemen UI.
### Panel width
Lebar menu dan panel.
### Font scale
Skala fon.
### Vertical spacing
Jarak antara elemen dalam menu dan panel.
### Vertical spacing (left)
Jarak antara elemen dalam bar alat kiri.

----

### Edge offset
Anda hanya perlu menukar nilai ini jika anda menghadapi masalah berinteraksi dengan butang di tepi skrin. Jika peluncur ini dilumpuhkan, Nomad akan menggunakan nilai kawasan selamat yang dikembalikan oleh peranti itu sendiri.

::: tip
Apabila memindahkan Nomad ke peranti baharu (contohnya menggantikan iPhone 12 dengan iPhone 15), pastikan untuk menetapkan semula pilihan edge kepada lalai!
:::

### Reset style
Tetapkan semula semua elemen UI kepada nilai lalai.


## Gesture
Menu gesture mengawal bagaimana tekanan stylus dan jari mengawal Nomad.

![](/images/interface_gesture.webp)

### Gesture options
![](/images/interface_gesture_matrix.webp)

Nomad boleh mengehadkan operasi berdasarkan peranti input. Contohnya seretan jari hanya boleh menggerakkan kamera, manakala seretan stylus hanya boleh mengukir. Jika anda mempunyai tetikus atau pad jejak, ia juga boleh ditetapkan untuk mengawal operasi tertentu.

Nomad pada masa ini membenarkan anda menetapkan mod ini untuk dikawal pada sebarang kombinasi gesture jari, stylus atau tetikus:

* Camera
* Sculpt
* Gizmo
* Material picking (melalui tekan lama)
* Select object


`Finger always smooths` - Smooth boleh ditetapkan untuk hanya berfungsi dengan seretan jari.

### ![](/icons/tool_mask.webp) Mask

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Dayakan pintasan satu ketikan berikut tanpa perlu menahan butang mask. Ia akan membenarkan gesture berikut:
* ketik pada latar belakang untuk songsangkan mask
* ketik pada kawasan yang dimask untuk kaburkan mask
* ketik pada kawasan yang tidak dimask untuk menajamkan mask

### Toggle Mask <-> SelMask
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - Tekan lama akan bertogol antara Mask dan SelMask dan memulakan stroke baharu. Pada akhir stroke, alat sebelumnya dipilih semula. 
* `Tool` - Tekan lama dan lepaskan tanpa menggerakkan untuk bertukar antara Mask dan SelMask. 

### ![](/icons/tool_hide.webp) Hide
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` akan mendayakan pintasan berikut dengan alat hide:
* Ketik pada face group untuk menyembunyikannya
* Ketik pada ruang kosong untuk songsangkan poligon tersembunyi

### ![](/icons/finger3.webp) Three fingers
![](/images/interface_gesture_threefingers.webp)

Jika peranti anda menyokong gesture 3 jari, konfigurasikan pintasan untuk gesture tersebut. 

Matriks pilihan membolehkan anda mentakrifkan seretan menegak dan mendatar sebagai pintasan berasingan. Ambil perhatian bahawa jika gesture yang sama dipilih untuk 2 pilihan, salah satu akan dilumpuhkan.

* `Rotate lighting` - Putarkan environment, lampu dan Matcap.
* `Tool Radius` - Ubah jejari alat.
* `Tool Intensity` - Ubah intensiti alat. 

### ![](/icons/fingerprint.webp) History 2/3
`History shortcuts` - apabila didayakan, gesture berikut aktif:
* Undo - ketik dengan 2 jari
* Redo - ketik dengan 3 jari

`Long press` - apabila didayakan, menahan 2/3 jari akan membatalkan/mengulang dengan pantas.

### Accessibility 

![](/images/interface_gesture_accessibility.webp)

`Assistive window` akan memaparkan bar alat terapung untuk mengawal drag, pinch, roll dan operasi kamera.

### Camera
Pintasan untuk pergi ke menu `Camera` (pilihan kamera dahulunya berada di sini, tetapi telah dipindahkan ke menu kamera).

### Pencil double tap -> Bindings 

Pintasan untuk pergi ke menu `Bindings` (pilihan tap dan double tap Pencil dahulunya berada di sini, tetapi telah dipindahkan ke menu bindings).


## Bindings
Pintasan papan kekunci dan butang boleh ditakrifkan dari menu bindings:

![](/images/interface_bindings.webp)
Hampir semua fungsi dalam Nomad boleh diikat kepada pintasan papan kekunci jika peranti anda mempunyai papan kekunci, atau kepada butang tambahan pada stylus anda, atau juga pengawal gamepad.

Untuk mencipta binding, klik segi empat di sebelah fungsi, dan tekan kekunci/butang. 

Cari fungsi melalui ikon kategori di bahagian atas, atau melalui bar carian untuk mencari mengikut nama. 

Binding individu boleh dilumpuhkan melalui kotak semak di sebelah nama binding.

### ![](/icons/more.webp) Context menu
Ikon ![](/icons/more.webp) selepas setiap binding memaparkan menu konteks:

![](/images/interface_bindings_context.webp)

* `Clone` - Gandakan binding
* `Reset` - Tetapkan semula binding
* `Delete` - Padam binding
* `Toggle shortcut on key tap` - Konfigurasikan sama ada ketikan vs tekan lama dilayan berbeza. Apabila didayakan, ketikan akan mengaktifkan alat. Tekan lama akan mengaktifkan alat hanya semasa kekunci ditekan, apabila dilepaskan ia akan kembali ke alat sebelumnya. Kadangkala dipanggil 'sticky keys' dalam aplikasi 3D lain.

### Advanced
Di bahagian bawah menu bindings terdapat menu gear untuk pilihan lanjutan:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - Ketikan pintasan standard untuk mask, smooth, gizmo, hide, sub akan bertogol ke mod tersebut, tetapi menahan kekunci akan menukar ke mod itu, kemudian apabila kekunci dilepaskan, mod akan kembali ke mod sebelumnya. Kadangkala dipanggil 'sticky keys' dalam aplikasi 3D lain.
* `Toggle tool shortcuts` - Apabila menggunakan salah satu pintasan alat, jika pintasan yang sama ditekan dua kali, ia akan bertogol ke alat sebelumnya. Dengan cara ini anda boleh terus bertukar antara dua alat dengan hotkey yang sama.
* `Invert Y (Zooming)` - Akan songsangkan zum
* `Reset bindings` - tetapkan semula semua bindings kepada lalai.


## iOS ⌘ Paparan pintasan papan kekunci

Pada peranti iOS dengan papan kekunci, tahan kekunci ⌘ (cmd) untuk memaparkan senarai pintasan.

Sokongan papan kekunci Android masih agak eksperimental.

![](/images/shortcuts.webp)


## Debug
Beberapa pilihan eksperimen dan debug disimpan dalam menu ini. Banyak pilihan ini harus dibiarkan pada lalai, dan hanya diubah selepas menghubungi sokongan Nomad.

![](/images/interface_debug.webp)
### UV
* `Normalize Uvs` - Nomad akan menormalkan UV di dalam tile [0-1].

### Quad Remesh
* `Instant Mesh` - Dayakan algoritma instant remesh
* `Quadriflow` - Kaedah quad remesh alternatif.

### Render
* `Heightmap` - Tukar viewport untuk merender kedalaman adegan. Ini boleh digunakan untuk mencipta alpha map untuk digunakan pada berus.
* `Refraction write depth (back)` - Bahagian belakang mesh refraksi akan ditulis ke dalam depth buffer.
* `Flip Y (normal map)` - Songsangkan saluran y apabila membakar normal map, diperlukan untuk enjin permainan dan render tertentu.
* `Angle weighted smooth normals` - Pelarasan kepada cara smooth shading berfungsi yang boleh mengelakkan lipatan dalam kes tertentu.

### Target FPS
Apabila dilumpuhkan, Nomad akan menyegerakkan frames-per-second dengan kadar segar semula paparan anda.

Apabila didayakan, anda boleh menetapkan frame per second yang akan dirender oleh Nomad.

### Interface
* `Top: layout` 
  * Collapse: Pada peranti kecil bar atas akan runtuh ke lebih banyak submenu. 
  * Scroll: Jika anda biasa dengan Nomad pada paparan besar dan lebih suka susun atur biasa, mendayakan ini akan menggunakan bar atas lebar standard, dan ia boleh ditatal.
  * Multiline: Paparkan keseluruhan menu atas dalam beberapa baris.
* `Bottom: draggable popup` - Bar alat bawah mempunyai beberapa butang yang memaparkan dialog. Jika pilihan ini didayakan, dialog tersebut boleh dialihkan ke tempat lain pada skrin.  
* `Toolbox: show all` - Nomad akan menyembunyikan alat yang tidak berkaitan dengan pilihan semasa, contohnya semua berus sculpt disembunyikan pada primitif yang belum divalidasi. Pilihan ini akan memudarkan alat yang dilumpuhkan dan bukannya menyembunyikannya.
* `Toolbox: colored` - Kod warna ikon toolbox berdasarkan jenisnya.
* `Panel: Drop shadows` - Lukis bayang jatuh di sekeliling menu dan panel. Pada sesetengah peranti lama ini boleh menjejaskan prestasi.
* `Panel: Blending` - Pilihan debug
* `Pointer: hovering dot` - Untuk peranti yang menyokong hover stylus, paparkan titik apabila stylus melayang di atas menu dan panel.

### Gif turntable
Nomad boleh mengeksport gif turntable beranimasi. Ambil perhatian bahawa disebabkan had format gif, kualiti adalah rendah. Rakaman skrin biasanya kaedah yang lebih baik.

* `Duration` - berapa lama dalam saat turntable akan berputar
* `Rotation center` - di mana pivot kamera berada, oleh itu bahagian adegan mana yang akan diputar oleh kamera
* `Transparent background` - Gunakan pilihan telus untuk gif. Ambil perhatian bahawa gif hanya menyokong ketelusan 1 bit, jadi tepi boleh menjadi sangat bergerigi.
* `Max frame sampling` - Banyak kesan rendering berkualiti tinggi Nomad datang daripada menggabungkan beberapa frame bersama. Peluncur ini menetapkan berapa banyak frame untuk digabungkan.
* `Export (GIF)` - mulakan proses eksport gif.

### Post Process
* `Filtering` - Pilihan debug
* `Format` - Pilihan debug
* `Buffer reuse` - Pilihan debug

### Performance
* `Multicore general` - Pilihan debug
* `Multicore sculpting` - Pilihan debug
* `Partial Drawing` - Ciri eksperimen! Gunakan jika anda sedang mengukir bahagian yang agak kecil daripada mesh poligon tinggi. Ia sepatutnya menjadikan sculpt lebih lancar, tetapi anda tidak sepatutnya mendayakan wireframe! Ia juga mungkin menambah artifak visual semasa stroke berus.

### Feature
* `Flip quad split (on tap)` -  Pilihan debug
* `Join: merge radius` - Verteks akan dikimpal secara automatik jika cukup rapat apabila mesh digabungkan. Anda boleh melaraskan radius dengan peluncur ini.

### Debug
* `Logs` - Paparkan tetingkap log
* `App review popup` - Pilihan debug
* `FPS` - tambah kaunter frames-per-second pada statistik viewport.
