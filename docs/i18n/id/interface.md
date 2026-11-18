# ![](/icons/sliders.webp) Menu Antarmuka {#interface-menu}

Menu ini berisi banyak opsi untuk menyesuaikan antarmuka Nomad.

![](/images/interface_overview2.webp)

Nomad bisa disesuaikan sampai ke tingkat yang cukup dalam; menu ini terbagi menjadi 5 tab: Antarmuka, Jalan pintas, Gestur, Pengikatan, Debug.

![](/images/interface_menu.webp)


::: tip
Halaman ini membahas menu antarmuka, bukan antarmukanya sendiri! Antarmuka secara keseluruhan dijelaskan di [Memulai](gettingstarted.md).
:::

## ![](/icons/sliders.webp) Antarmuka {#interface}

Tab antarmuka mengatur warna, ukuran, dan tata letak antarmuka pengguna Nomad. Tab ini punya dua sub-tab, `Tampilan` dan `Tata letak`.

![](/images/interface_overview3.webp)

### ![](/icons/palette.webp) Warna {#presets}

![](/images/interface_presets.webp)

Sub-tab `Tampilan` dimulai dengan kumpulan preset warna untuk antarmuka. Ketuk salah satunya untuk menerapkannya, lalu sempurnakan dengan opsi-opsi di bawah.

#### Aksen dan Dasar {#color-widgetcolor-base}
Warna utama yang dipakai di antarmuka: `Aksen` untuk tombol yang dipilih dan batang penggeser, `Dasar` untuk panel.

#### Opasitas teks {#text-opacity}
Membuat teks dan ikon tampak lebih lembut di atas panel.

#### Sakelar, Kotak centang, Tab {#high-contrast-button}
Gaya tombol sakelar (`Lembut` atau `Penuh`), kotak centang (`Garis tepi`, `Aksen`, atau `Isian`), dan tab (`Garis bawah`, `Lembut`, atau `Penuh`).

#### Alat berwarna {#colored}
Memberi kode warna pada ikon sesuai kategorinya, misalnya semua alat mask berwarna cokelat, alat pemisah merah, alat perata hijau, dan seterusnya.

#### Bayangan panel {#material-color-preview}
Panel menjatuhkan bayangan agar menonjol dari adegan.

#### Panel transparan {#transparent-panel-color-panel-blur-strength}
![](/images/interface_transparent.webp)
Jika diaktifkan, opsi tambahan akan muncul untuk mengatur tampilan menu dan panel di Nomad: `Warna panel` mengatur warnanya, `Kekuatan kabur` seberapa kabur adegan di belakangnya, dan `Kaca` menambahkan refraksi di tepi serta kilauan, paling terlihat dengan kabur yang rendah.

::: tip
Di perangkat kecil, ada gunanya membuat warna panel hampir putih, transparan, dengan kekuatan kabur rendah, agar menu tidak menutupi adegan.
:::

#### ![](/icons/reset.webp) Atur ulang tampilan {#reset-style}
Mengembalikan semua opsi tampilan ke nilai bawaannya.

### ![](/icons/panel_detach.webp) Tata letak {#layout}

Sub-tab `Tata letak` mengatur posisi dan ukuran berbagai elemen.

#### Kotak peralatan {#toolbox}

Opsi untuk menu alat di sebelah kanan antarmuka Nomad.

![](/images/interface_toolbox.webp)

##### ![](/icons/resize_bottom_right.webp) Ubah ukuran {#ui-resize-corner}

Menampilkan atau menyembunyikan pegangan pengubah ukuran di sudut bawah kotak peralatan.

##### Tersembunyi {#hidden}
Biasanya ikon kotak peralatan di bilah atas berganti antara satu kolom panjang atau daftar alat dengan beberapa kolom. Opsi ini membuatnya berganti antara daftar beberapa kolom atau disembunyikan.

##### Atur ulang urutan {#reset-order}
Mengembalikan alat bawaan di kotak peralatan ke urutan bawaannya. Ikon khusus tetap ada di kotak peralatan, di akhir daftar.

#### Bar atas {#rows-auto-1}
`Responsif` menentukan apa yang dilakukan bilah atas jika tidak muat di layar, terutama relevan untuk layar kecil: `Multiline` membungkus menu ke beberapa baris, `Gulir` mempertahankan satu baris yang bisa Anda gulir.

#### Cermin bilah atas {#mirror-top-bar}
Membalik urutan menu di bilah atas.

#### Cermin bilah samping {#mirror-side-bars}
Menukar bilah samping sehingga kotak peralatan ada di kiri, dan opsi alat di kanan.

#### Cermin bilah bawah {#mirror-bottom-bar}
Memindahkan bilah bawah ke sudut kanan bawah, dan membalik urutan tombolnya.

#### ![](/icons/move.webp) Seret panel {#drag-panel}
Panel mengambang selalu bisa dipindahkan dengan menyeret bilahnya; opsi ini memungkinkan Anda menyeret badannya juga. Pada `Otomatis`, jari atau stylus hanya memindahkan panel jika seretannya lebih horizontal daripada vertikal, sehingga seretan vertikal tetap menggulir isinya. Atur ke `Ya` agar juga bisa diseret dengan mouse, ke arah mana pun.

#### ![](/icons/pencil.webp) Gunakan Dialog Nomad {#use-nomad-dialog}
Menampilkan dialog teks milik Nomad sendiri, bukan dialog bawaan sistem, saat Anda mengetik nama atau nilai.

#### ![](/icons/stylus.webp) Titik hover {#hover-dot}
Menampilkan titik kecil di antarmuka saat stylus yang melayang terdeteksi.

#### ![](/icons/help.webp) Popup bantuan saat melayang {#help-popup-on-hover}

Untuk perangkat yang mendukung hover, aktifkan agar bantuan konteks di Nomad yang ditandai dengan ikon ![](/icons/help.webp) muncul saat melayang, bukan hanya saat diklik.

#### Skala keseluruhan {#overall-scale}
Pengali ukuran untuk semua elemen antarmuka.
#### Lebar panel {#panel-width}
Lebar menu dan panel.
#### Skala huruf {#font-scale}
Mengubah skala huruf.
#### Jarak vertikal {#vertical-spacing}
Jarak antar elemen di menu dan panel.
#### Jarak vertikal (kiri) {#vertical-spacing-left}
Jarak antar elemen di toolbar kiri.

#### Offset tepi {#edge-offset}
Anda sebaiknya hanya mengubah nilai-nilai ini jika mengalami masalah saat berinteraksi dengan tombol di tepi layar. Jika penggeser ini dinonaktifkan, Nomad akan memakai nilai area aman yang diberikan oleh perangkat itu sendiri.

::: tip
Saat memindahkan Nomad ke perangkat baru (misalnya mengganti iPhone 12 dengan iPhone 15), pastikan untuk mengembalikan opsi tepi ke nilai bawaannya!
:::

#### ![](/icons/reset.webp) Atur ulang tata letak {#reset-layout}
Mengembalikan semua opsi tata letak ke nilai bawaannya.

## ![](/icons/window.webp) Jalan pintas {#shortcuts}

Tab jalan pintas menentukan tombol cepat mana yang muncul di sekitar viewport, dan memungkinkan Anda membuat toolbar mengambang sendiri.

### Bilah samping {#side-bar}
Tombol alat cepat di bagian bawah bilah samping kiri: `Haluskan`, `Topeng`, `Sembunyi`, `Grup Face`, dan `Gizmo`. Seret untuk mengubah urutannya.

### Tambahkan pintasan (bawah)... {#add-shortcuts-bottom}
![](/images/interface_shortcuts.webp)

Ketuk sebuah pintasan untuk menambahkannya ke bilah bawah, atau untuk menghapusnya. Pintasan berikut aktif secara bawaan:
* `Urungkan` - mengurungkan operasi sebelumnya
* `Ulangi` - mengembalikan operasi yang baru saja diurungkan
* `Solo` - Menyembunyikan sementara semua objek lain, sehingga hanya objek yang dipilih yang terlihat. Tekan lagi untuk menampilkan kembali semua objek.
* `X-Ray` - Membuat semua objek lain semi-transparan untuk sementara, sehingga hanya objek yang dipilih yang tampak padat. Tekan lagi untuk mengembalikan material bawaan.
* `Voxel` - Melakukan remesh pada objek saat ini dengan resolusi voxel terakhir yang dipakai. Ketukan lama atau usapan ke atas akan memunculkan penggeser resolusi dan sakelar tepi tajam.
* `Grid` - Menampilkan/menyembunyikan grid tampilan. Ketukan lama atau usapan ke atas memungkinkan Anda mengubah warna dan opasitas grid.
* `Kerangka kawat` - Menampilkan/menyembunyikan lapisan kerangka kawat. Ketukan lama atau usapan ke atas memungkinkan Anda mengubah warna dan opasitas kerangka kawat.
* `Periksa` - memungkinkan Anda melihat properti mesh, seperti UV, tekstur hasil bake, dan properti lainnya, ditampilkan di latar belakang Nomad.
* `Grup Face` - Menampilkan/menyembunyikan tampilan grup face, info lebih lanjut di [Alat->Grup Face](tools.md#facegroup)

Pintasan lain yang sering dipakai juga tersedia: `Garis tepi`, `Proyeksi` (perspektif atau ortografis), `MatCap`, `DynTopo`, serta tombol `Subdivisi`, `Balikkan`, dan level dari [Multiresolusi](topology.md#multiresolution).

#### ![](/icons/more.webp) Pengikatan {#bindings-list}

Hampir setiap fungsi Nomad bisa ditambahkan ke bilah bawah melalui tombol pengikatan, yang menunjukkan berapa banyak pintasan di bilah tersebut. Menu pengikatan akan ditampilkan saat tombol ini diklik:

![](/images/interface_bindings_search.webp)

Anda bisa mencari berdasarkan kategori lewat ikon-ikon di bagian atas, atau memakai kolom pencarian untuk menemukan fungsi berdasarkan nama. Klik sebuah fungsi untuk menambahkannya ke toolbar. Klik lagi untuk menghapusnya.

#### ![](/icons/eye_open.webp) Tampak {#order}

Menampilkan atau menyembunyikan seluruh bilah bawah.

#### ![](/icons/reset.webp) Setel ulang {#reset}

Setel ulang akan mengembalikan bilah bawah ke pengaturan bawaannya.

### Tambahkan pintasan (jendela)... {#add-shortcuts-window}
![](/images/interface_add_shortcuts_window.webp)

Mengklik tombol + akan menambahkan toolbar mengambang. Toolbar ini tidak akan terlihat sampai Anda mengklik tombol pengikatan dan menambahkan beberapa pintasan ke dalamnya; setelah itu Anda bisa menampilkannya.

Anda bisa membuat banyak toolbar, dan masing-masing punya satu baris dengan opsi berikut:

* Seret pegangan di kiri baris untuk mengubah urutan toolbar.
* `Nama` - Nama toolbar.
* `Tampak` - Menampilkan/menyembunyikan toolbar.
* `Bilah` - Menampilkan bilah judul pada toolbar.
* `Mode ringkas` - Tetap menampilkan toolbar di layar saat antarmuka diringkas.
* `Pengikatan` - Menampilkan jendela pengikatan untuk memilih fungsi yang akan ditambahkan ke atau dihapus dari toolbar.
* `Hapus` - Menghapus toolbar.


## ![](/icons/gesture.webp) Gestur {#gesture}
Menu gestur mengatur bagaimana jari, stylus, mouse, dan trackpad Anda mengendalikan Nomad.

![](/images/interface_gesture.webp)

### Opsi gestur {#gesture-options}
![](/images/interface_gesture_matrix.webp)

Nomad bisa membatasi operasi berdasarkan perangkat input. Misalnya, seretan jari hanya bisa menggerakkan kamera, sementara seretan stylus hanya bisa memahat. Jika Anda punya mouse atau trackpad, perangkat itu juga bisa ditugaskan untuk mengendalikan operasi tertentu.

Setiap baris adalah satu operasi: nyalakan `Jari`, `Stylus`, dan `Mouse` untuk memilih input mana yang bisa melakukannya.

* `Kamera` - Menggerakkan kamera.
* `Pengeditan simpul` - Menyeret pegangan yang digambar di kanvas, misalnya untuk mengedit primitif, kurva, pengulang, atau lampu.
* `Memahat` - Memahat dengan kuas. Alat yang punya baris sendiri di bawah mengikuti baris tersebut.
* `Pilih objek` - Mengetuk objek untuk memilihnya.
* `Pemilihan material` - Menekan lama kanvas untuk mengambil warna atau material di bawah kursor. Hanya berfungsi jika kuas saat ini punya pewarnaan yang aktif.
* `Saat diketuk` - Pintasan ketuk dari alat seperti Topeng, Sembunyi, dan Grup Face (lihat di bawah).
* `Lukis` - Alat Lukis dan Smudge.
* `Mask` - Alat Topeng.
* `Sisi` - Alat Sembunyi dan Grup Face.
* `Buat` - Alat Tabung, Bubut, dan Masukkan.
* `Potong` - Alat Pangkas, Pisah, dan Proyeksi.
* `Pilih` - Alat Pilih dan Ukur.
* `Gizmo` - Alat Gizmo dan Lattice.
* `Transformasi` - Alat Transformasi dan Atur.

::: tip
Pengaturan yang umum di tablet adalah membiarkan hanya stylus yang memahat dan mewarnai, sementara jari dipakai untuk kamera. Dengan begitu, telapak tangan atau jari yang tidak sengaja menyentuh layar tidak akan meninggalkan goresan di model Anda.
:::

### ![](/icons/tool_smooth.webp) Jari selalu meratakan {#finger-always-smooths}
Jika diaktifkan, jari Anda selalu menghaluskan selama alat pahat aktif, apa pun kuasnya. Mengaktifkannya akan menghapus `Jari` dari baris `Memahat`, sehingga stylus memahat dan jari menghaluskan.

### Goresan di ruang kosong {#allow-air-stroke}
Memungkinkan goresan dimulai meskipun kursor pertama kali mendarat di luar mesh. Pilih alat yang terpengaruh: `Alat` (semua kuas lainnya), `Haluskan`, `Topeng`, dan `Sembunyi`. Ini hanya berfungsi untuk input yang bisa memahat tetapi tidak bisa menggerakkan kamera, jadi tombol-tombol ini nonaktif sampai salah satu input Anda diatur seperti itu.

### ![](/icons/stroke.webp) Snap stroke {#stroke-snap}
Tahan penunjuk tetap diam di akhir goresan untuk menjadikannya garis lurus atau kurva halus. Terus seret untuk memutar dan menskalakan goresan tersebut di sekitar titik awalnya.

`Jeda tahan` mengatur berapa lama Anda harus diam sebelum goresan berubah, atau sebelum sebuah bentuk beralih ke mode edit.

### ![](/icons/stylus.webp) Gunakan sampel masukan tambahan {#use-extra-input-samples}
Memakai sampel input tambahan yang dilaporkan perangkat. Nonaktifkan jika goresan Anda bergerigi atau tekanan berperilaku tidak semestinya. Opsi ini tidak ditampilkan di iOS.

### ![](/icons/tool_mask.webp) Topeng {#mask}

![](/images/interface_gesture_mask.webp)

`Jalan pintas satu ketuk` - Mengaktifkan pintasan satu ketuk berikut tanpa harus menahan tombol mask. Gestur yang tersedia:
* ketuk latar belakang untuk membalik mask
* ketuk area yang di-mask untuk mengaburkan mask
* ketuk area yang tidak di-mask untuk mempertajam mask

#### Tekan lama {#toggle-mask-selmask}
![](/images/interface_gesture_togglemask.webp)

Menekan lama dengan alat Topeng akan berganti antara kuas mask dan laso (SelMask):
* `Tekan lama - Memahat` - Tekan lama, lalu terus seret: goresan digambar dengan mode yang lain, dan mode sebelumnya kembali di akhir goresan.
* `Tekan lama - Alihkan` - Tekan lama lalu lepas tanpa bergerak untuk berganti di antara keduanya.

### ![](/icons/tool_smooth.webp) Haluskan {#smooth}
`Tekan lama - Tali` - Menekan lama dengan alat Haluskan akan beralih ke alat Pilih selama goresan pemilihan berlangsung.

### ![](/icons/tool_hide.webp) Sembunyi {#hide}
![](/images/interface_gesture_hide.webp)

`Jalan pintas satu ketuk` akan mengaktifkan pintasan berikut pada alat sembunyi:
* Ketuk sebuah grup face untuk menyembunyikannya
* Ketuk ruang kosong untuk membalik poligon yang tersembunyi

### ![](/icons/finger3.webp) Tiga jari {#three-fingers}
![](/images/interface_gesture_threefingers.webp)

Jika perangkat Anda mendukung gestur 3 jari, atur pintasan untuk gestur tersebut.

Matriks opsi memungkinkan Anda menetapkan seretan vertikal dan horizontal sebagai pintasan terpisah, atau `Tidak` untuk menonaktifkannya. Perlu diingat, jika gestur yang sama dipilih untuk 2 opsi, salah satunya akan dinonaktifkan dan namanya dicoret.

* `Putar pencahayaan` - Memutar lingkungan, lampu, dan MatCap.
* `Radius Alat` - Mengubah radius alat.
* `Intensitas Alat` - Mengubah intensitas alat.

### ![](/icons/fingerprint.webp) Riwayat 2/3 {#history-23}
`Jalan pintas riwayat` - jika diaktifkan, gestur berikut aktif:
* Urungkan - ketuk dengan 2 jari
* Ulangi - ketuk dengan 3 jari

`Tekan lama` - jika diaktifkan, menahan 2/3 jari akan mengurungkan/mengulangi dengan cepat.

### ![](/icons/mouse.webp) Roda mouse {#mouse-wheel}
`Kecepatan (perbesaran 3d)` mengatur seberapa cepat roda memperbesar tampilan, dan `Kecepatan (antarmuka 2d)` seberapa cepat roda menggulir menu dan panel. Tombol minus di samping setiap penggeser membalik arahnya.

### ![](/icons/fingerprint.webp) Trackpad {#trackpad}
Di Mac, `Dua jari` menentukan apa yang dilakukan dua jari di trackpad. Mencubit selalu memperbesar/memperkecil, dan memutar selalu memiringkan tampilan.
* `Nonaktif` - Menggulir dengan dua jari akan memperbesar/memperkecil, seperti roda mouse. Jari tidak dibaca satu per satu.
* `Geser` - Dua jari menggeser tampilan, dan mengangkat salah satunya akan mengorbit. Sama seperti di tablet.
* `Orbit` - Dua jari mengorbit tampilan, dan mengangkat salah satunya akan menggeser.

### Aksesibilitas {#accessibility}

![](/images/interface_gesture_accessibility.webp)

`Jendela Asistif` akan memunculkan toolbar mengambang untuk mengendalikan operasi seret, cubit, putar, dan kamera.

### Kamera {#camera}
Pintasan menuju menu `Kamera` (opsi kamera dulu ada di sini, tetapi sudah dipindahkan ke menu kamera).

### Ketuk ganda pensil -> Pengikatan {#pencil-tap}

Pintasan menuju menu `Pengikatan`, tempat Anda mengatur apa yang dilakukan ketuk ganda Pencil. Di luar iOS, tulisannya `Tombol pensil → Pengikatan`, untuk tombol stylus.

### Penolakan telapak {#palm-rejection}
Di ponsel dan tablet, abaikan sentuhan yang area kontaknya lebih besar dari `Ambang batas ukuran maksimal`, seperti telapak tangan yang bertumpu di layar. Fitur ini mungkin tidak berfungsi di semua perangkat, jadi matikan jika Anda kesulitan berinteraksi dengan kanvas.


## ![](/icons/keyboard.webp) Pengikatan {#bindings}
Pintasan keyboard dan tombol bisa diatur dari menu pengikatan:

![](/images/interface_bindings.webp)
Hampir semua fungsi di Nomad bisa diikat ke pintasan keyboard jika perangkat Anda punya keyboard, ke tombol tambahan pada stylus, atau bahkan ke kontroler gamepad.

Untuk membuat pengikatan, klik kotak di samping fungsi, lalu tekan tombol/kunci yang diinginkan.

Temukan fungsi lewat ikon kategori di bagian atas, atau lewat bilah pencarian untuk mencari berdasarkan nama.

Setiap pengikatan bisa dinonaktifkan lewat kotak centang di samping nama pengikatannya. Tekan lama kotak centang lalu seret untuk mengubah urutan daftar.

Jika dua pengikatan yang aktif memakai pintasan yang sama, ikon ![](/icons/help.webp) muncul di sampingnya, berisi daftar fungsi yang bentrok.

### ![](/icons/more.webp) Menu konteks {#context-menu}
Ikon ![](/icons/more.webp) setelah setiap pengikatan membuka menu konteks:

![](/images/interface_bindings_context.webp)

* `Kloning` - Mengkloning pengikatan, misalnya untuk memberi fungsi pintasan kedua.
* `Setel ulang` - Mengembalikan pengikatan ke bawaannya
* `Hapus` - Menghapus pengikatan. Hanya bisa dilakukan jika fungsi tersebut punya lebih dari satu pengikatan.

Di bawahnya, beberapa pengikatan punya opsi tambahan:

* `Tombol lekat` - Untuk pintasan alat dan pintasan cepat (Topeng, Haluskan, Gizmo, Sembunyi, Grup Face, Tambah/Kurang), memilih bagaimana menekan tombol akan berganti alat. `Otomatis` memakai pengaturan bawaan dari opsi [Lanjutan](#advanced).
  * `Tahan` - Tahan tombol untuk memakai alat, lepaskan untuk kembali ke alat sebelumnya.
  * `Alihkan` - Tekan sekali untuk berganti alat.
  * `Tekan Cepat` - Tahan untuk memakai alat sementara, atau tekan cepat untuk beralih ke alat tersebut.
* `Tahan Pemulihan` - Untuk pintasan cepat, memilih apakah melepas tombol yang ditahan selalu kembali ke alat sebelumnya, bahkan jika alat itu sudah aktif sebelumnya.
* `Alihkan Alat Sebelumnya` - Untuk pintasan alat, menekan pintasan alat yang sedang aktif akan kembali ke alat terakhir. Memerlukan `Tombol lekat` pada `Alihkan` atau `Tekan Cepat`.
* `Posisi` - Untuk pintasan jendela mengambang, membuka jendela di posisi terakhirnya (`Pertahankan sebelumnya`) atau di bawah kursor (`Pada kursor`).
* `Menggeser (saat dilepas)` / `Zoom (saat dilepas)` - Untuk pengikatan zoom dan geser kamera, beralih ke yang lainnya saat Anda melepas tombol.
* Arah seretan - Untuk `Putar pencahayaan`, `Radius Alat`, dan `Intensitas Alat`, memilih seretan horizontal atau vertikal.
* `Sinkron` - Untuk fungsi yang menambah, mengkloning, atau membuat instans objek, memilih apakah hasilnya disinkronkan. Secara bawaan, memakai nilai sinkron yang diatur di menu Adegan.
* `Pada Latar Belakang` - Untuk pintasan cepat Haluskan dan Topeng, seret di latar belakang sambil menahan tombol untuk menggambar laso: laso pemilihan untuk Haluskan, laso mask untuk Topeng.
* `Paksa Kamera` - Untuk pengikatan kamera, tetap gerakkan kamera meskipun pintasan yang sama juga dipakai oleh pengikatan lain, biasanya pintasan alat atau Tambah/Kurang.
* `Rotasi linear` - Untuk pengikatan putar (roll), memutar dengan seretan horizontal, vertikal, atau diagonal, bukan dengan bergerak di sekitar poros.

::: tip
Dengan `Tekan Cepat`, satu tombol bisa melakukan keduanya: tahan untuk menghaluskan atau memberi mask sebentar, dan Anda kembali ke kuas saat melepasnya, atau ketuk untuk tetap memakai alat tersebut.
:::

### ![](/icons/cog.webp) Lanjutan {#advanced}
Di bagian bawah menu pengikatan ada menu roda gigi untuk opsi lanjutan:

![](/images/interface_bindings_advanced.webp)

* `Jalan pintas cepat` - Pengaturan bawaan `Tombol lekat` dan `Tahan Pemulihan` untuk pintasan Topeng, Haluskan, Gizmo, Sembunyi, Grup Face, dan Tambah/Kurang.
* `Jalan pintas alat` - Pengaturan bawaan `Tombol lekat` dan `Alihkan Alat Sebelumnya` untuk pintasan alat. Dengan `Alihkan Alat Sebelumnya`, Anda bisa terus berganti antara dua alat dengan hotkey yang sama.
* `Jendela pintasan` - Mode `Tombol lekat` untuk pintasan yang menampilkan jendela mengambang.
* `Balikkan zoom Y` - Membalik arah seretan vertikal saat memperbesar/memperkecil dengan pengikatan.
* `Rotasi linear` - Memutar (roll) tampilan dengan seretan horizontal, vertikal, atau diagonal, bukan dengan bergerak di sekitar poros.
* `SpaceMouse` - Mengaktifkan dukungan 3Dconnexion SpaceMouse. Di beberapa sistem, opsi tambahan muncul: apa yang digerakkannya (`Objek`, `Kamera`, `Orang Pertama`, `Drone`), `Perbarui poros otomatis` untuk memindahkan poros ke permukaan di bawah kursor saat mulai bergerak, serta kecepatan `Translasi`, `Perbesaran`, dan `Rotasi`.
* `Zona mati (drift)` - Untuk kontroler `Gamepad`, `Joystick`, dan `Tombol`. Naikkan nilai ini jika kamera bergerak sendiri saat kontroler tidak disentuh.
* `Radius Alat` - Cara seretan dengan pengikatan radius mengubah ukuran kuas (`Lingkaran`, `Tengah`, atau `dx`), lalu seberapa banyak pengikatan radius menambah (dalam piksel) atau mengalikan di setiap tekanan.
* `Intensitas Alat` - Seberapa banyak pengikatan intensitas menambah atau mengalikan di setiap tekanan.
* `Kamera - Kecepatan` - Kecepatan `Translasi` dan `Rotasi` untuk pengikatan yang menggeser dan memutar tampilan.
* `Reset pengikatan` - mengembalikan semua pengikatan ke bawaannya.
* `Atur ulang urutan` - mengembalikan urutan bawaan daftar pengikatan.


## Tampilan pintasan keyboard iOS ⌘ {#ios-keyboard-shortcuts-display}

Di perangkat iOS dengan keyboard, tahan tombol ⌘ (cmd) untuk menampilkan daftar pintasan.

Dukungan keyboard di Android masih agak eksperimental.

![](/images/shortcuts.webp)


## ![](/icons/bug.webp) Debug {#debug}
Beberapa opsi eksperimental dan debug disimpan di menu ini. Banyak opsi di sini sebaiknya dibiarkan pada nilai bawaannya, dan hanya diubah setelah menghubungi dukungan Nomad. Ikon-ikon di bagian atas langsung membawa Anda ke setiap bagian.

![](/images/interface_debug.webp)
### ![](/icons/uv.webp) UV {#uv}
* `Normalisasi UVs` - Nomad akan menormalisasi UV mesh yang dipilih ke dalam tile [0-1].

### ![](/icons/sun.webp) Shading {#render}
* `Tulis kedalaman refraksi (belakang)` - Sisi belakang mesh refraksi akan ditulis ke depth buffer.
* `Normal halus berbobot sudut` - Penyesuaian cara kerja shading halus yang bisa menghindari lipatan dalam kasus tertentu.

### ![](/icons/speed.webp) Target FPS {#target-fps}
Jika dinonaktifkan, Nomad akan menyinkronkan frame per detiknya dengan refresh rate layar Anda.

Jika diaktifkan, Anda bisa mengatur berapa frame per detik yang akan dirender Nomad.

### ![](/icons/window.webp) Antarmuka {#debug-interface}
* `Kotak alat: tampilkan semua` - Nomad menyembunyikan alat yang tidak relevan untuk pilihan saat ini, misalnya semua kuas pahat disembunyikan pada primitif yang belum difinalisasi. Opsi ini akan meredupkan alat yang nonaktif alih-alih menyembunyikannya.

Opsi antarmuka lain yang dulu ada di sini sekarang berada di tab [Antarmuka](#interface).

### ![](/icons/turntable.webp) Piringan Putar {#gif-turntable}
Nomad bisa mengekspor turntable berupa gif animasi. Perlu diingat bahwa karena keterbatasan format gif, kualitasnya rendah. Merekam layar biasanya cara yang lebih baik.

* `Durasi` - berapa detik lamanya turntable
* `Sampel frame maksimum` - Banyak efek render berkualitas tinggi di Nomad berasal dari penggabungan beberapa frame. Penggeser ini mengatur berapa banyak frame yang digabungkan, dan kotak centangnya menyalakan atau mematikannya.
* `Pusat rotasi` - titik yang menjadi pusat putaran kamera: `Pertahankan saat ini` mempertahankan poros saat ini, `(0, 0, 0)` memakai pusat dunia, `Adegan` memakai pusat adegan.
* `Latar belakang transparan` - Memakai opsi transparan untuk gif. Perlu diingat bahwa gif hanya mendukung transparansi 1 bit, sehingga tepinya bisa tampak sangat bergerigi.
* `Ekspor (GIF)` - memulai proses ekspor gif.

### ![](/icons/postprocess.webp) Pemrosesan pasca {#post-process}
* `Penyaringan` - Opsi debug
* `Format` - Opsi debug
* `Gunakan ulang buffer` - Opsi debug

### ![](/icons/ram.webp) Performa {#performance}
* `Multithread: umum` - Opsi debug
* `Multithread: memahat` - Opsi debug
* `Gambar pengulangan dengan instans` - Menggambar semua salinan pengulang dalam satu draw call. Opsi debug.

### ![](/icons/star.webp) Fitur {#feature}
* `nom: kompres multires` - Mengurangi ukuran proyek dan ekspor Nomad yang memakai multiresolusi. File ini tidak bisa dibuka oleh versi Nomad yang lebih lama. Opsi ini mungkin akan dihapus dan diaktifkan secara bawaan di masa mendatang.
* `Balik diagonal quad (saat diketuk)` -  Opsi debug

### ![](/icons/bug.webp) Debug {#dev}
* `Log` - Memunculkan tampilan log
* `Catat event` - Menulis event penunjuk Anda (jari, stylus, mouse) ke tampilan log, untuk menyelidiki masalah input.
* `FPS` - menambahkan penghitung frame per detik ke statistik viewport.
* `Popup ulasan aplikasi` - Opsi debug, di iOS dan Android.

### ![](/icons/image.webp) Ikon khusus {#custom-icons}
Mengganti ikon Nomad dengan file png Anda sendiri.
* `Impor ikon` - Mengimpor file png ke `tmp_session/icons`. Setiap file menggantikan ikon dasar dengan nama yang sama. File-file ini dibuang saat Nomad dijalankan ulang.
* `Ekspor ikon alat` - Menyalin ikon dasar `tool_<tool>.png` ke `tmp_session/icons`, tanpa menimpa. Anda bisa mengeditnya di sana dan menerapkannya dengan `Muat ulang ikon`.
* `Muat ulang ikon` - Menerapkan ikon dari `tmp_session/icons`.

### Remesh Kuad {#quad-remesh}
Opsi remesh kuad sudah tidak ada di menu ini: lihat [Remesh Kuad](topology.md#quad-remesh-instant) di menu Topologi dan alat [Quad Remesher](tools.md#quad-remesher).

### Buat thumbnail toko {#make-store-thumbnails}
Merender tangkapan layar dengan ukuran yang sesuai untuk iOS App Store.
