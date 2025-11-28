# ![](/icons/cog.webp) Pengaturan {#reset-to-default}

Menu pengaturan berisi banyak opsi untuk mengontrol tampilan dan perilaku Nomad.

![](/images/settings_overview.webp)

## Pengaturan tampilan {#display-settings}
Bagian ini berisi pintasan peluncuran cepat untuk sebagian besar pengaturan di bawah menu ini.

![](/images/settings_display_settings.webp)

### Perhalus bayangan {#smooth-shading}
Alihkan shading halus dan bersegi. Saat bersegi, poligon diarsir secara independen, sehingga Anda dapat melihat topologi dasarnya.
Ini bisa berguna untuk melihat shading bersegi selama tahap pemahatan, lalu mengubah ke shading halus untuk rendering.

Menonaktifkan Smooth Shading sedikit meningkatkan performa.

### Garis luar {#outline-quick}
Alihkan garis luar pada seleksi Anda saat ini.

Ini berguna untuk mendapatkan umpan balik visual pada mesh yang saat ini dipilih jika [Darken Unselected](#darken-unselected-objects) dinonaktifkan.

Dari sudut pandang performa, menggunakan [Darken Unselected](#darken-unselected-objects) jauh lebih baik daripada menggunakan solusi outline.

### Kisi {#grid-quick}
Alihkan grid latar belakang, berguna untuk memahami penempatan dan skala objek.

### Dua sisi {#two-sided-quick}
Alihkan tampilan poligon dua sisi. Semua face mengarah ke arah tertentu.
Face yang dianggap *backface* adalah yang mengarah "menjauh" dari sudut pandang kamera.

Sebagai contoh, sphere sederhana saat startup akan memiliki face yang mengarah ke luar.
Jika Anda memindahkan kamera ke dalam sphere, Anda akan melihat backface dari face tersebut.

Sebagian besar waktu Anda seharusnya tidak melihat bagian backface dari face, jadi mewarnainya dapat membantu Anda mendeteksi potensi masalah atau topologi yang salah.

Menonaktifkan rendering `two sided` dapat sedikit meningkatkan performa rendering.


### Kerangka kawat {#wireframe-quick}
Alihkan overlay wireframe. 

Perlu dicatat bahwa mengaktifkan wireframe akan menurunkan performa.

### Kubus snap {#snap-cube-quick}
Alihkan ikon pembantu di sudut scene, berguna untuk mengorientasikan diri Anda di ruang dan dengan cepat beralih antara tampilan depan/belakang/kiri/kanan/atas/bawah.

### Tampilkan pengecatan {#show-painting}
Alihkan tampilan cat. Cat bawaan yang digunakan adalah material putih non-logam, dengan kekasaran 25%.

### Gunakan sembunyi {#use-hide}
Alihkan mode sembunyi. Saat dimatikan, mode ini masih ada, hanya dinonaktifkan. Tombol ini dinonaktifkan jika Anda sedang menggunakan tool hide.

### Tampilkan masker {#show-mask}
Alihkan mode mask. Saat dimatikan, mode ini masih ada, hanya dinonaktifkan. Tekan tombol ini lagi untuk mengaktifkannya kembali.

Jika Anda perlu menyembunyikan mask DAN tetap membuatnya aktif, gunakan warna mask di bawah dan atur ke putih. Ingat untuk mengubahnya kembali ke abu-abu saat Anda selesai!

Perlu dicatat bahwa tombol ini dinonaktifkan jika Anda sedang menggunakan tool mask. 

### Masker -> Buram {#mask-opaque}
Mask -> opaque akan mengabaikan vertex transparan untuk mask yang dimasker. Ini hanya relevan untuk opasitas vertex dan tekstur, face yang disembunyikan oleh “hide” akan tetap tersembunyi.

### Sorotan {#highlight-quick}
Alihkan kilatan highlight seleksi. Saat memilih objek, objek yang dipilih akan berkedip sementara dengan warna pink terang selama 500 milidetik. Warna dan lamanya kilatan dapat disesuaikan di bawah.

### Statistik {#stats-quick}
Alihkan teks tampilan status di viewport 3D. Ini menampilkan informasi tentang memori sistem Anda, jumlah vertex total scene, dan jumlah vertex seleksi saat ini.

----- 

### Gelapkan objek yang tidak dipilih {#darken-unselected-objects}
Objek yang tidak dipilih akan digelapkan sehingga seleksi saat ini dapat lebih menonjol.

### Masker {#mask}
Warna yang digunakan untuk masking, secara bawaan abu-abu sedang, dikalikan dengan warna objek Anda. Atur ini ke putih untuk membuat mask tidak terlihat, tetapi ingat untuk mengubahnya kembali ke abu-abu saat selesai!

## ![](/icons/cursor.webp) Kursor {#cursor}

### Tampilkan lingkaran saat memahat {#show-circle-while-sculpting}
Terus menampilkan radius brush saat memahat.

### Tampilkan titik kecil {#show-small-dot}
Menampilkan titik di tengah sapuan brush saat memahat, atau ketika pivot kamera diubah.

### Tampilkan penstabil tali {#show-rope-stabilizer}
Menggambar garis untuk menunjukkan panjang tali saat lazy rope stabilizer aktif di pengaturan stroke.

## ![](/icons/cursor.webp) Indikator {#indicator}
![](/images/settings_indicator.webp)

Menampilkan indikator visual untuk tutorial dan perekaman layar.

Tombol `Finger`, `Stylus` dan `Mouse` akan mengaktifkan penampilan ikon ketika jenis input tersebut terdeteksi.

### Warna {#indicator-color}
Warna indikator.

### Ukuran/Ikon/Lingkaran {#indicator-shape}
Kontrol untuk menyesuaikan ukuran indikator dan bentuk di dalam indikator.

## ![](/icons/wireframe.webp) Kerangka kawat {#wireframe}
![](/images/settings_wireframe.webp)
Mengaktifkan overlay wireframe.

### Target {#target}
Mengatur apakah objek yang tidak dipilih akan menampilkan wireframe, atau hanya objek yang dipilih, atau semua objek.

### Sembunyikan {#hide}
Mengatur apakah wireframe masih akan ditampilkan untuk poligon yang disembunyikan.

### Multiresolusi: Hanya level 0 {#multiresolution-level-0-only}
Multiresolution akan menampilkan wireframe untuk level 0 lebih gelap, dan level yang lebih tinggi semakin terang. Saat diaktifkan, opsi ini hanya akan menampilkan wireframe level 0.

### Warna {#wireframe-color}
Mengatur warna dan opasitas untuk wireframe.

## ![](/icons/grid.webp) Kisi {#grid}
![](/images/settings_grid.webp)
Mengaktifkan grid.

### Warna {#grid-color}
Mengatur warna dan opasitas grid.

### Snap {#snap}
Mengaktifkan snapping untuk tool berbasis kurva ke grid.

## ![](/icons/culling.webp)Dua sisi {#two-sided}
Mengaktifkan tampilan face poligon dari kedua sisi.

### Warna sisi belakang, Warna sisi belakang {#backface-color}
Mengaktifkan pewarnaan backface, dan warna tint-nya.

## ![](/icons/outline.webp)Garis luar {#outline}
Mengaktifkan garis luar di sekitar objek aktif.

### Warna garis luar, Ketebalan {#outline-color-thickness}
Mengatur warna dan ketebalan garis luar.


## ![](/icons/bang.webp) Sorotan {#highlight}
Mengaktifkan kilatan singkat ketika objek aktif berubah.
### Warna, Durasi {#color-duration}
Mengatur warna dan lamanya kilatan dalam milidetik.

## ![](/icons/snap_cube.webp) Kubus snap {#snap-cube}
![](/images/settings_snapcube.webp)

Menampilkan ikon pembantu di sudut scene, berguna untuk dengan cepat beralih antara tampilan depan/belakang/kiri/kanan/atas/bawah. Ketuk sisi-sisi kubus untuk berpindah antara tampilan ortografis.

### Bentuk {#shape}
Memilih antara bentuk kubus, sphere, atau gnomon untuk snap cube.

### Batasi perataan {#restrict-alignment}
Mengaktifkan penguncian rotasi kamera saat menyeret pada snap cube. Saat aktif, gerakan seret pada snap cube hanya akan ke kiri/kanan atau atas/bawah.

### Ukuran {#size}
Mengatur ukuran snap cube.

### Balik 180 {#flip-180}
Mengaktifkan perilaku ketukan sehingga jika tampilan sedang tersnap, mengetuk bagian tengah kubus akan memutar tampilan 180 derajat. Misalnya jika tampilan tersnap ke depan, mengetuk view cube akan memutar ke tampilan belakang.

### Posisi {#snap-position}
Mengatur di sudut mana snap cube akan berada.


## ![](/icons/edit_radius_n.webp) Statistik {#stats}
![](/images/settings_stats.webp)

Menampilkan informasi tentang memori sistem Anda, jumlah vertex total scene, dan jumlah vertex seleksi saat ini.

### Posisi {#stats-position}
Mengatur di sudut mana stats akan berada.

## Primtif/Pengulang {#primitive-repeaters}
## Masukan numerik {#gizmo-input}
Mengizinkan input numerik saat mengetuk widget gizmo.

## Multiresolusi {#multires}
### Jumlah simpul maksimum {#multires-lowres-count}
Mengatur ambang batas agar operasi subdivide multires tidak diizinkan melebihi jumlah poligon ini, yang kemungkinan akan membuat Nomad crash. Bawaannya adalah 10 juta.
### Ambang resolusi rendah {#multires-lowres-threshold}
Resolusi mesh yang lebih rendah dapat ditampilkan ketika Anda menggerakkan kamera. Anda dapat meningkatkan nilai ini jika ingin menampilkan resolusi mesh yang lebih tinggi.

## Pengaturan {#advanced}
### Atur ulang ke bawaan {#reset}
Mengatur ulang semua pengaturan ke nilai bawaan.