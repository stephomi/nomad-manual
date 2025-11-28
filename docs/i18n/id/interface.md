# ![](/icons/interface.webp) Menu Antarmuka {#interface-menu}

Menu ini mengontrol banyak opsi untuk menyesuaikan antarmuka Nomad. 

![](/images/interface_overview2.webp)

Nomad dapat dikustomisasi hingga tingkat yang cukup dalam, menu ini dibagi menjadi 4 bagian; Interface, Gesture, Bindings, Debug.

![](/images/interface_menu.webp)


::: tip
Halaman ini untuk menu antarmuka, bukan antarmukanya sendiri! Antarmuka secara keseluruhan dijelaskan di [Getting Started](gettingstarted.md).
:::

## Antarmuka {#interface}

Bagian interface memungkinkan Anda menambahkan pintasan, membuat toolbar mengambang, dan mengontrol warna, ukuran, tampilan antarmuka pengguna Nomad.

![](/images/interface_overview3.webp)

### Tambahkan pintasan (bawah)... {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Toolbar bawah memiliki pintasan berikut yang diaktifkan secara bawaan:
* `Undo` - membatalkan operasi sebelumnya
* `Redo` - mengembalikan operasi yang sebelumnya dibatalkan
* `Solo` - Sembunyikan sementara semua objek lain, hanya menyisakan objek yang dipilih tetap terlihat. Tekan lagi untuk mengembalikan semua objek.
* `X-ray` - Sementara membuat semua objek lain menjadi semi-transparan, hanya menyisakan objek yang dipilih tetap solid. Tekan lagi untuk mengembalikan material bawaan.
* `Voxel remesh` - Remesh objek saat ini menggunakan resolusi voxel terakhir yang digunakan. Tekan lama atau geser ke atas akan menampilkan slider resolusi dan toggle tepi tajam.
* `Grid` - Mengaktifkan/mematikan grid tampilan. Tekan lama atau geser ke atas akan memungkinkan Anda mengubah warna dan opasitas grid.
* `Wireframe` - Mengaktifkan/mematikan overlay wireframe. Tekan lama atau geser ke atas akan memungkinkan Anda mengubah warna dan opasitas wireframe.
* `Inspector` - memungkinkan Anda melihat properti mesh seperti uv, tekstur baked, dan properti lain, ditampilkan di latar belakang Nomad.
* `Face Group` - Mengaktifkan/mematikan overlay facegroup, info lebih lanjut di [Tools->FaceGroup](tools.md#facegroup) 

Pintasan umum lain tersedia dari menu ini, lebih banyak lagi dapat ditemukan di dalam tombol bindings.

#### ![](/icons/more.webp) Pengikatan {#bindings-list}

Hampir setiap fungsi Nomad dapat ditambahkan ke toolbar pintasan melalui tombol bindings. Menu bindings akan ditampilkan ketika tombol diklik:

![](/images/interface_bindings_search.webp)

Anda dapat mencari berdasarkan kategori melalui ikon di bagian atas, atau gunakan kolom pencarian untuk menemukan fungsi berdasarkan nama. Klik pada sebuah fungsi untuk menambahkannya ke toolbar. Klik lagi untuk menghapusnya.

#### ![](/icons/list.webp) Urutan {#order}

Ini akan menampilkan daftar pintasan. Tekan lama lalu seret untuk mengubah urutan pintasan.

#### ![](/icons/reset.webp) Atur ulang {#reset}

Reset akan mengembalikan toolbar bawah ke pengaturan bawaan.

### Tambahkan pintasan (jendela)... + {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Mengklik tanda + akan menambahkan toolbar mengambang. Toolbar tidak akan terlihat sampai Anda mengklik tombol bindings dan menambahkan beberapa pintasan ke dalamnya, lalu Anda dapat membuatnya terlihat. 

Anda dapat membuat banyak toolbar, setiap toolbar memiliki opsi berikut di menu ini:

* ![](/icons/checked.webp) `Visible` - Mengaktifkan/mematikan visibilitas toolbar
* ![](/icons/more.webp)`Bindings` - Menampilkan jendela binding untuk memilih fungsi yang akan ditambahkan atau dihapus dari toolbar.
* ![](/icons/list.webp)`Order` - Menampilkan menu untuk mengubah urutan toolbar.
* ![](/icons/reset.webp) `Reset` - Mengatur ulang toolbar ke keadaan bawaan.
* ![](/icons/resize_bottom_right.webp) `Resize corner` - Mengaktifkan/mematikan handle pengubah ukuran di sudut kanan bawah toolbar.
* ![](/icons/sort_down.webp) `Collapsable` - Mengaktifkan/mematikan handle collapse di sudut kanan atas.
* ![](/icons/trash.webp) `Delete` - Menghapus toolbar.

### Kotak alat {#toolbox}

Opsi untuk menu tool di sisi kanan antarmuka Nomad.

![](/images/interface_toolbox.webp)

#### ![](/icons/resize_bottom_right.webp) Sudut Ubah Ukuran UI {#ui-resize-corner}

Mengaktifkan/mematikan handle pengubah ukuran di sudut bawah toolbar.

#### Tersembunyi {#hidden}
Biasanya ikon toolbox di bar atas akan berganti antara satu kolom panjang, atau daftar tool multi-kolom. Opsi ini akan berganti antara daftar multi-kolom, atau disembunyikan.

#### Berwarna {#colored}
Memberi kode warna pada ikon berdasarkan kategori, misalnya semua tool mask berwarna coklat, tool split merah, tool flatten hijau, dll.

#### Baris: Otomatis (>1) {#rows-auto-1}

#### Atur ulang urutan {#reset-order}
Mengatur ulang tool bawaan di toolbox ke urutan bawaan. Ikon kustom akan tetap berada di toolbox di akhir daftar.


### Preset {#presets}

![](/images/interface_presets.webp)

Kumpulan preset warna untuk antarmuka.

#### Tombol kontras tinggi {#high-contrast-button}
Gaya alternatif untuk tombol yang membuatnya lebih terlihat ketika diaktifkan. Jika disetel ke Auto, Nomad akan menggunakan mode ini ketika kontras warna UI antara aktif/nonaktif rendah.

#### Widget warna/Warna dasar {#color-widgetcolor-base}
Warna utama yang digunakan di antarmuka.

#### Panel transparan, Panel warna, Kekuatan blur {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Ketika diaktifkan, opsi tambahan akan muncul untuk mengontrol tampilan menu dan panel di Nomad. Warna, transparansi, dan jumlah blur dapat disesuaikan.

::: tip
Pada perangkat kecil, akan berguna membuat panel warna hampir putih, transparan, dan blur rendah, sehingga menu tidak menutupi scene.
:::

----

### Cermin bar atas {#mirror-top-bar}
Membalik urutan menu di bar atas.

### Cermin bar samping {#mirror-side-bars}
Menukar side bar sehingga toolbox berada di kiri, opsi tool di kanan.

### Cermin bar bawah {#mirror-bottom-bar}
Memindahkan bar bawah ke sudut kanan bawah, dan membalik urutan tombol.

### Pratinjau warna material {#material-color-preview}
Saat Anda memilih warna untuk material, pratinjau material ini ditampilkan pada objek yang sedang dipilih.

----
### Popup bantuan saat hover {#help-popup-on-hover}

Untuk perangkat yang mendukung hover, atur apakah bantuan konteks di Nomad yang diwakili ikon ![](/icons/help.webp) akan muncul saat hover, atau hanya ketika diklik.

----

### Skala keseluruhan {#overall-scale}
Pengali ukuran untuk semua elemen UI.
### Lebar panel {#panel-width}
Lebar menu dan panel.
### Skala font {#font-scale}
Skala font.
### Jarak vertikal {#vertical-spacing}
Jarak antar elemen di menu dan panel.
### Jarak vertikal (kiri) {#vertical-spacing-left}
Jarak antar elemen di toolbar kiri.

----

### Offset tepi {#edge-offset}
Anda hanya perlu mengubah nilai ini jika mengalami masalah berinteraksi dengan tombol di tepi layar. Jika slider ini dinonaktifkan, Nomad akan menggunakan nilai safe area yang dikembalikan oleh perangkat itu sendiri.

::: tip
Saat memindahkan Nomad ke perangkat baru (misalnya mengganti iPhone 12 dengan iPhone 15), pastikan untuk mereset opsi edge ke bawaan!
:::

### Atur ulang gaya {#reset-style}
Mengatur ulang semua elemen UI ke nilai bawaan.


## Gestur {#gesture}
Menu gesture mengontrol bagaimana tekanan stylus dan jari mengontrol Nomad.

![](/images/interface_gesture.webp)

### Opsi gestur {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad dapat membatasi operasi berdasarkan perangkat input. Misalnya drag dengan jari hanya dapat menggerakkan kamera, sementara drag dengan stylus hanya dapat melakukan sculpt. Jika Anda memiliki mouse atau trackpad, itu juga dapat ditetapkan untuk mengontrol operasi tertentu.

Saat ini Nomad memungkinkan Anda mengatur mode berikut agar dikontrol oleh kombinasi gesture jari, stylus, atau mouse mana pun:

* Camera
* Sculpt
* Gizmo
* Material picking (melalui tekan lama)
* Select object


`Finger always smooths` - Smooth dapat diatur hanya bekerja dengan drag jari.

### ![](/icons/tool_mask.webp) Masker {#mask}

![](/images/interface_gesture_mask.webp)

`One tap shortcuts` - Mengaktifkan pintasan satu ketukan berikut tanpa harus menahan tombol mask. Ini akan memungkinkan gesture berikut:
* ketuk pada background untuk membalik mask
* ketuk pada area yang termask untuk mengaburkan mask
* ketuk pada area yang tidak termask untuk menajamkan mask

### Alihkan Masker <-> SelMask {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)
* `Stroke` - Tekan lama akan berganti antara Mask dan SelMask dan memulai stroke baru. Di akhir stroke, tool sebelumnya dipilih kembali. 
* `Tool` - Tekan lama dan lepas tanpa menggerakkan untuk beralih antara Mask dan SelMask. 

### ![](/icons/tool_hide.webp) Sembunyikan {#hide}
![](/images/interface_gesture_hide.webp)

`One tap shortcuts` akan mengaktifkan pintasan berikut dengan tool hide:
* Ketuk pada face group untuk menyembunyikannya
* Ketuk di ruang kosong untuk membalik poligon yang disembunyikan

### ![](/icons/finger3.webp) Tiga jari {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Jika perangkat Anda mendukung gesture 3 jari, konfigurasikan pintasan untuk gesture tersebut. 

Matriks opsi memungkinkan Anda mendefinisikan drag vertikal dan horizontal sebagai pintasan terpisah. Perhatikan bahwa jika gesture yang sama dipilih untuk 2 opsi, salah satunya akan dinonaktifkan.

* `Rotate lighting` - Memutar environment, lampu, dan Matcap.
* `Tool Radius` - Mengubah radius tool.
* `Tool Intensity` - Mengubah intensitas tool. 

### ![](/icons/fingerprint.webp) Riwayat 2/3 {#history-23}
`History shortcuts` - ketika diaktifkan, gesture berikut aktif:
* Undo - ketuk dengan 2 jari
* Redo - ketuk dengan 3 jari

`Long press` - ketika diaktifkan, menahan 2/3 jari akan melakukan undo/redo dengan cepat.

### Aksesibilitas {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Assistive window` akan menampilkan toolbar mengambang untuk mengontrol drag, pinch, roll, dan operasi kamera.

### Kamera {#camera}
Pintasan untuk pergi ke menu `Camera` (opsi kamera sebelumnya berada di sini, tetapi dipindahkan ke menu kamera).

### Ketukan ganda Pensil -> Pengikatan {#pencil-tap} {#pencil-tap}

Pintasan untuk pergi ke menu `Bindings` (opsi tap dan double tap Pencil sebelumnya berada di sini, tetapi telah dipindahkan ke menu bindings).


## Pengikatan {#bindings}
Pintasan keyboard dan tombol dapat didefinisikan dari menu bindings:

![](/images/interface_bindings.webp)
Hampir semua fungsi di Nomad dapat diikat ke pintasan keyboard jika perangkat Anda memiliki keyboard, atau ke tombol tambahan pada stylus, atau bahkan kontroler gamepad.

Untuk membuat binding, klik persegi panjang di sebelah fungsi, lalu tekan tombol/tombol perangkat.

Temukan fungsi melalui ikon kategori di bagian atas, atau melalui kolom pencarian untuk mencari berdasarkan nama. 

Binding individual dapat dinonaktifkan melalui checkbox di sebelah nama binding.

### ![](/icons/more.webp) Menu konteks {#context-menu}
Ikon ![](/icons/more.webp) setelah setiap binding akan menampilkan context menu:

![](/images/interface_bindings_context.webp)

* `Clone` - Menggandakan binding
* `Reset` - Mengatur ulang binding
* `Delete` - Menghapus binding
* `Toggle shortcut on key tap` - Mengonfigurasi apakah tap vs tekan lama diperlakukan berbeda. Ketika diaktifkan, tap akan mengaktifkan tool. Tekan lama akan mengaktifkan tool hanya selama tombol ditekan, ketika dilepas akan kembali ke tool sebelumnya. Kadang disebut 'sticky keys' di aplikasi 3D lain.

### Lanjutan {#advanced}
Di bagian bawah menu bindings terdapat menu gear untuk opsi lanjutan:

![](/images/interface_bindings_advanced.webp)

* `Toggle shortcut on key tap` - Tap pada pintasan standar untuk mask, smooth, gizmo, hide, sub akan beralih ke mode tersebut, tetapi menahan tombol akan beralih ke mode itu, lalu ketika tombol dilepas, mode akan kembali ke mode sebelumnya. Kadang disebut 'sticky keys' di aplikasi 3D lain.
* `Toggle tool shortcuts` - Saat menggunakan salah satu pintasan tool, jika pintasan yang sama ditekan dua kali, itu akan beralih ke tool sebelumnya. Dengan cara ini Anda dapat terus bertukar antara dua tool dengan hotkey yang sama.
* `Invert Y (Zooming)` - Membalik arah zoom
* `Reset bindings` - mengatur ulang semua binding ke bawaan.


## Pintasan keyboard iOS ⌘ ditampilkan {#ios-keyboard-shortcuts-display}

Pada perangkat iOS dengan keyboard, tahan tombol ⌘ (cmd) untuk menampilkan daftar pintasan.

Dukungan keyboard Android masih agak eksperimental.

![](/images/shortcuts.webp)


## Debug {#debug}
Beberapa opsi eksperimental dan debug disimpan di menu ini. Banyak dari opsi ini sebaiknya dibiarkan pada nilai bawaan, dan hanya diubah setelah menghubungi dukungan Nomad.

![](/images/interface_debug.webp)
### UV {#uv}
* `Normalize Uvs` - Nomad akan menormalkan UV di dalam tile [0-1].

### Quad Remesh {#quad-remesh}
* `Instant Mesh` - Mengaktifkan algoritma instant remesh
* `Quadriflow` - Metode quad remesh alternatif.

### Render {#render}
* `Heightmap` - Mengubah viewport untuk merender kedalaman scene. Ini dapat digunakan untuk membuat alpha map untuk digunakan pada brush.
* `Refraction write depth (back)` - Backface dari mesh refraksi akan ditulis ke depth buffer.
* `Flip Y (normal map)` - Membalik channel y saat baking normal map, diperlukan untuk engine game dan render tertentu.
* `Angle weighted smooth normals` - Penyesuaian cara kerja smooth shading yang dapat menghindari lipatan pada kasus tertentu.

### FPS Target {#target-fps}
Ketika dinonaktifkan, Nomad akan menyinkronkan frame-per-second dengan refresh rate layar Anda.

Ketika diaktifkan, Anda dapat mengatur frame per second yang akan dirender Nomad.

### Antarmuka {#debug-interface}
* `Top: layout` 
  * Collapse: Pada perangkat kecil bar atas akan dilipat menjadi lebih banyak submenu. 
  * Scroll: Jika Anda terbiasa dengan Nomad di layar besar dan lebih menyukai layout normal, mengaktifkan ini akan menggunakan bar atas lebar standar, dan dapat digulir.
  * Multiline: Menampilkan seluruh menu atas dalam beberapa baris.
* `Bottom: draggable popup` - Toolbar bawah memiliki beberapa tombol yang memunculkan dialog. Jika opsi ini diaktifkan, dialog tersebut dapat dipindahkan ke tempat lain di layar.  
* `Toolbox: show all` - Nomad akan menyembunyikan tool yang tidak relevan untuk seleksi saat ini, misalnya semua brush sculpt disembunyikan pada primitive yang belum divalidasi. Opsi ini akan meredupkan tool yang dinonaktifkan alih-alih menyembunyikannya.
* `Toolbox: colored` - Memberi kode warna pada ikon toolbox berdasarkan tipenya.
* `Panel: Drop shadows` - Menggambar bayangan di sekitar menu dan panel. Pada beberapa perangkat lama ini dapat memengaruhi performa.
* `Panel: Blending` - Opsi debug
* `Pointer: hovering dot` - Untuk perangkat yang mendukung hover stylus, menampilkan titik ketika stylus melayang di atas menu dan panel.

### Gif turntable {#gif-turntable}
Nomad dapat mengekspor gif animasi turntable. Perhatikan bahwa karena keterbatasan format gif, kualitasnya rendah. Perekaman layar biasanya merupakan metode yang lebih baik.

* `Duration` - berapa lama dalam detik durasi turntable
* `Rotation center` - di mana pivot kamera berada, sehingga bagian mana dari scene yang akan diputar kamera
* `Transparent background` - Menggunakan opsi transparan untuk gif. Perhatikan bahwa gif hanya mendukung transparansi 1 bit, sehingga tepi dapat terlihat sangat bergerigi.
* `Max frame sampling` - Banyak efek rendering berkualitas tinggi Nomad berasal dari penggabungan beberapa frame. Slider ini mengatur berapa banyak frame yang digabungkan.
* `Export (GIF)` - memulai proses ekspor gif.

### Pasca Proses {#post-process}
* `Filtering` - Opsi debug
* `Format` - Opsi debug
* `Buffer reuse` - Opsi debug

### Performa {#performance}
* `Multicore general` - Opsi debug
* `Multicore sculpting` - Opsi debug
* `Partial Drawing` - Fitur eksperimental! Gunakan jika Anda sedang melakukan sculpt pada bagian yang relatif kecil dari mesh high poly. Ini seharusnya membuat sculpt lebih mulus, tetapi Anda tidak boleh mengaktifkan wireframe! Juga dapat menambah artefak visual selama sapuan brush.

### Fitur {#feature}
* `Flip quad split (on tap)` -  Opsi debug
* `Join: merge radius` - Vertex akan otomatis dilas jika cukup berdekatan ketika mesh digabungkan. Anda dapat menyesuaikan radius dengan slider ini.

### Debug {#dev}
* `Logs` - Menampilkan jendela log
* `App review popup` - Opsi debug
* `FPS` - menambahkan penghitung frame-per-second ke statistik viewport.