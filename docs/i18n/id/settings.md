# ![](/icons/cog.webp) Pengaturan 

Menu pengaturan berisi banyak opsi untuk mengontrol tampilan dan perilaku Nomad.

![](/images/settings_overview.webp)

## Pengaturan tampilan
Bagian ini berisi pintasan peluncuran cepat untuk sebagian besar pengaturan di bawah menu ini.

![](/images/settings_display_settings.webp)

### Smooth Shading 
Alihkan shading halus dan bersegi. Saat bersegi, poligon diarsir secara independen, sehingga Anda dapat melihat topologi dasarnya.
Ini bisa berguna untuk melihat shading bersegi selama tahap pemahatan, lalu mengubah ke shading halus untuk rendering.

Menonaktifkan Smooth Shading sedikit meningkatkan performa.

### Outline
Alihkan garis luar pada seleksi Anda saat ini.

Ini berguna untuk mendapatkan umpan balik visual pada mesh yang saat ini dipilih jika [Darken Unselected](#darken-unselected-objects) dinonaktifkan.

Dari sudut pandang performa, menggunakan [Darken Unselected](#darken-unselected-objects) jauh lebih baik daripada menggunakan solusi outline.

### Grid
Alihkan grid latar belakang, berguna untuk memahami penempatan dan skala objek.

### Two sided
Alihkan tampilan poligon dua sisi. Semua face mengarah ke arah tertentu.
Face yang dianggap *backface* adalah yang mengarah "menjauh" dari sudut pandang kamera.

Sebagai contoh, sphere sederhana saat startup akan memiliki face yang mengarah ke luar.
Jika Anda memindahkan kamera ke dalam sphere, Anda akan melihat backface dari face tersebut.

Sebagian besar waktu Anda seharusnya tidak melihat bagian backface dari face, jadi mewarnainya dapat membantu Anda mendeteksi potensi masalah atau topologi yang salah.

Menonaktifkan rendering `two sided` dapat sedikit meningkatkan performa rendering.


### Wireframe
Alihkan overlay wireframe. 

Perlu dicatat bahwa mengaktifkan wireframe akan menurunkan performa.

### Snap cube
Alihkan ikon pembantu di sudut scene, berguna untuk mengorientasikan diri Anda di ruang dan dengan cepat beralih antara tampilan depan/belakang/kiri/kanan/atas/bawah.

### Show Painting
Alihkan tampilan cat. Cat bawaan yang digunakan adalah material putih non-logam, dengan kekasaran 25%.

### Use Hide
Alihkan mode sembunyi. Saat dimatikan, mode ini masih ada, hanya dinonaktifkan. Tombol ini dinonaktifkan jika Anda sedang menggunakan tool hide.

### Show Mask
Alihkan mode mask. Saat dimatikan, mode ini masih ada, hanya dinonaktifkan. Tekan tombol ini lagi untuk mengaktifkannya kembali.

Jika Anda perlu menyembunyikan mask DAN tetap membuatnya aktif, gunakan warna mask di bawah dan atur ke putih. Ingat untuk mengubahnya kembali ke abu-abu saat Anda selesai!

Perlu dicatat bahwa tombol ini dinonaktifkan jika Anda sedang menggunakan tool mask. 

### Mask -> Opaque
Mask -> opaque akan mengabaikan vertex transparan untuk mask yang dimasker. Ini hanya relevan untuk opasitas vertex dan tekstur, face yang disembunyikan oleh “hide” akan tetap tersembunyi.

### Highlight
Alihkan kilatan highlight seleksi. Saat memilih objek, objek yang dipilih akan berkedip sementara dengan warna pink terang selama 500 milidetik. Warna dan lamanya kilatan dapat disesuaikan di bawah.

### Stats
Alihkan teks tampilan status di viewport 3D. Ini menampilkan informasi tentang memori sistem Anda, jumlah vertex total scene, dan jumlah vertex seleksi saat ini.

----- 

### Darken Unselected objects
Objek yang tidak dipilih akan digelapkan sehingga seleksi saat ini dapat lebih menonjol.

### Mask
Warna yang digunakan untuk masking, secara bawaan abu-abu sedang, dikalikan dengan warna objek Anda. Atur ini ke putih untuk membuat mask tidak terlihat, tetapi ingat untuk mengubahnya kembali ke abu-abu saat selesai!

## ![](/icons/cursor.webp) Cursor

### Show circle while sculpting
Terus menampilkan radius brush saat memahat.

### Show small dot
Menampilkan titik di tengah sapuan brush saat memahat, atau ketika pivot kamera diubah.

### Show rope stabilizer
Menggambar garis untuk menunjukkan panjang tali saat lazy rope stabilizer aktif di pengaturan stroke.

## ![](/icons/cursor.webp) Indicator
![](/images/settings_indicator.webp)

Menampilkan indikator visual untuk tutorial dan perekaman layar.

Tombol `Finger`, `Stylus` dan `Mouse` akan mengaktifkan penampilan ikon ketika jenis input tersebut terdeteksi.

### Color
Warna indikator.

### Size/Icon/Circle
Kontrol untuk menyesuaikan ukuran indikator dan bentuk di dalam indikator.

## ![](/icons/wireframe.webp) Wireframe
![](/images/settings_wireframe.webp)
Mengaktifkan overlay wireframe.

### Target
Mengatur apakah objek yang tidak dipilih akan menampilkan wireframe, atau hanya objek yang dipilih, atau semua objek.

### Hide
Mengatur apakah wireframe masih akan ditampilkan untuk poligon yang disembunyikan.

### Multiresolution: Level 0 only
Multiresolution akan menampilkan wireframe untuk level 0 lebih gelap, dan level yang lebih tinggi semakin terang. Saat diaktifkan, opsi ini hanya akan menampilkan wireframe level 0.

### Color
Mengatur warna dan opasitas untuk wireframe.

## ![](/icons/grid.webp) Grid
![](/images/settings_grid.webp)
Mengaktifkan grid.

### Color
Mengatur warna dan opasitas grid.

### Snap
Mengaktifkan snapping untuk tool berbasis kurva ke grid.

## ![](/icons/culling.webp)Two sided
Mengaktifkan tampilan face poligon dari kedua sisi.

### Color Backface, Backface Color
Mengaktifkan pewarnaan backface, dan warna tint-nya.

## ![](/icons/outline.webp)Outline
Mengaktifkan garis luar di sekitar objek aktif.

### Outline color, Thickness
Mengatur warna dan ketebalan garis luar.


## ![](/icons/bang.webp) Highlight
Mengaktifkan kilatan singkat ketika objek aktif berubah.
### Color, Duration
Mengatur warna dan lamanya kilatan dalam milidetik.

## ![](/icons/snap_cube.webp) Snap cube
![](/images/settings_snapcube.webp)

Menampilkan ikon pembantu di sudut scene, berguna untuk dengan cepat beralih antara tampilan depan/belakang/kiri/kanan/atas/bawah. Ketuk sisi-sisi kubus untuk berpindah antara tampilan ortografis.

### Shape
Memilih antara bentuk kubus, sphere, atau gnomon untuk snap cube.

### Restrict alignment
Mengaktifkan penguncian rotasi kamera saat menyeret pada snap cube. Saat aktif, gerakan seret pada snap cube hanya akan ke kiri/kanan atau atas/bawah.

### Size
Mengatur ukuran snap cube.

### Flip 180
Mengaktifkan perilaku ketukan sehingga jika tampilan sedang tersnap, mengetuk bagian tengah kubus akan memutar tampilan 180 derajat. Misalnya jika tampilan tersnap ke depan, mengetuk view cube akan memutar ke tampilan belakang.

### Position
Mengatur di sudut mana snap cube akan berada.


## ![](/icons/edit_radius_n.webp) Stats
![](/images/settings_stats.webp)

Menampilkan informasi tentang memori sistem Anda, jumlah vertex total scene, dan jumlah vertex seleksi saat ini.

### Position
Mengatur di sudut mana stats akan berada.

## Primtive/Repeaters
## Numerical input
Mengizinkan input numerik saat mengetuk widget gizmo.

## Multiresolution
### Max vertices count
Mengatur ambang batas agar operasi subdivide multires tidak diizinkan melebihi jumlah poligon ini, yang kemungkinan akan membuat Nomad crash. Bawaannya adalah 10 juta.
### Low resolution threshold
Resolusi mesh yang lebih rendah dapat ditampilkan ketika Anda menggerakkan kamera. Anda dapat meningkatkan nilai ini jika ingin menampilkan resolusi mesh yang lebih tinggi.

## Settings
### Reset to default
Mengatur ulang semua pengaturan ke nilai bawaan.
