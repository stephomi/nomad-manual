# ![](/icons/cog.webp) Pengaturan {#reset-to-default}

Menu pengaturan berisi banyak opsi untuk mengatur tampilan dan perilaku Nomad.

![](/images/settings_overview.webp)

Deretan tombol di bagian atas menu langsung membawa Anda ke sebuah bagian: `Kursor`, `Indikator`, `Kawat`, `Kisi`, `Dua sisi`, `Garis tepi`, `Sorot`, `Navigator`, `Statistik`, `Gagang-gagang`, `Bentuk`, `Pengulang` dan `Multires`.

## Pengaturan tampilan {#display-settings}
Bagian ini berisi pintasan cepat untuk sebagian besar pengaturan yang ada lebih jauh di menu ini.

![](/images/settings_display_settings.webp)

### ![](/icons/sphere_smooth.webp) Shading halus {#smooth-shading}
Beralih antara shading halus dan bersegi. Dalam mode bersegi, setiap poligon diberi shading secara terpisah, sehingga Anda bisa melihat topologi di baliknya.
Shading bersegi bisa berguna selama tahap memahat, lalu beralih ke shading halus untuk render.

Menonaktifkan Shading halus sedikit meningkatkan performa.

### ![](/icons/outline.webp) Garis tepi {#outline-quick}
Menampilkan atau menyembunyikan garis tepi pada seleksi Anda saat ini.

Ini berguna untuk mendapatkan umpan balik visual tentang mesh yang sedang dipilih jika [Gelapkan objek yang tidak dipilih](#darken-unselected-objects) dinonaktifkan.

Dari sisi performa, memakai [Gelapkan objek yang tidak dipilih](#darken-unselected-objects) jauh lebih baik daripada memakai garis tepi.

### ![](/icons/grid.webp) Kisi {#grid-quick}
Menampilkan atau menyembunyikan kisi latar belakang, berguna untuk memahami posisi dan skala objek.

### ![](/icons/culling.webp) Dua sisi {#two-sided-quick}
Mengaktifkan atau menonaktifkan tampilan poligon dua sisi. Setiap face menghadap ke arah tertentu.
Face yang dianggap sebagai *bagian belakang* (backface) adalah face yang menghadap "menjauh" dari sudut pandang kamera.

Misalnya, bola sederhana saat aplikasi dibuka memiliki face yang menghadap ke luar.
Jika Anda memindahkan kamera ke dalam bola, Anda akan melihat bagian belakang face-face tersebut.

Hampir selalu, Anda seharusnya tidak melihat bagian belakang face, jadi memberinya warna bisa membantu Anda mendeteksi kemungkinan masalah atau topologi yang salah.

Menonaktifkan render `Dua sisi` bisa sedikit meningkatkan performa render.


### ![](/icons/wireframe.webp) Kerangka kawat {#wireframe-quick}
Menampilkan atau menyembunyikan overlay kerangka kawat. 

Perhatikan bahwa mengaktifkan kerangka kawat akan menurunkan performa.

### ![](/icons/navigator.webp) Navigator {#snap-cube-quick}
Menampilkan atau menyembunyikan ikon bantu di pojok adegan, berguna untuk mengetahui orientasi Anda di ruang 3d dan beralih cepat antara tampilan depan/belakang/kiri/kanan/atas/bawah.

### ![](/icons/palette.webp) Tampilkan lukisan {#show-painting}
Menampilkan atau menyembunyikan cat. Jika dimatikan, objek ditampilkan dengan material putih non-metalik dengan kekasaran 25%, alih-alih dengan catnya.

### ![](/icons/tool_hide.webp) Gunakan Sembunyikan {#use-hide}
Mengaktifkan atau menonaktifkan mode sembunyi. Jika dimatikan, area tersembunyi tetap ada, hanya dinonaktifkan. Tombol ini dinonaktifkan jika Anda sedang memakai alat sembunyi.

### ![](/icons/shield.webp) Tampilkan topeng {#show-mask}
Mengaktifkan atau menonaktifkan mode topeng. Jika dimatikan, topeng tetap ada, hanya dinonaktifkan. Tekan tombol ini lagi untuk mengaktifkannya kembali.

Jika Anda perlu menyembunyikan topeng TETAPI tetap membuatnya aktif, gunakan warna topeng di bawah dan atur ke putih. Jangan lupa mengembalikannya ke abu-abu setelah selesai!

Perhatikan bahwa tombol ini dinonaktifkan jika Anda sedang memakai alat topeng. 

### ![](/icons/shield.webp) Topeng → Opak {#mask-opaque}
`Topeng → Opak` akan mengabaikan verteks transparan pada topeng. Ini hanya berlaku untuk opasitas verteks dan tekstur; face yang disembunyikan dengan "sembunyi" akan tetap tersembunyi. Opsi ini hanya tersedia saat `Tampilkan topeng` aktif.

### ![](/icons/bang.webp) Sorot {#highlight-quick}
Mengaktifkan atau menonaktifkan kilatan sorotan seleksi. Saat memilih objek, objek yang dipilih akan berkilat sebentar selama 500 milidetik. Warna dan durasi kilatan bisa diatur di bawah.

### ![](/icons/list.webp) Statistik {#stats-quick}
Menampilkan atau menyembunyikan teks status di viewport 3d. Teks ini menampilkan informasi tentang memori sistem, jumlah total verteks di adegan, dan jumlah verteks seleksi saat ini.

----- 

### ![](/icons/cube.webp) Gelapkan objek yang tidak dipilih {#darken-unselected-objects}
Objek yang tidak dipilih akan digelapkan agar seleksi saat ini lebih menonjol.

### ![](/icons/shield.webp) Topeng {#mask}
Warna yang dipakai untuk topeng, secara bawaan abu-abu sedang, yang dikalikan dengan warna objek Anda. Atur ke putih untuk membuat topeng tidak terlihat, tetapi jangan lupa mengembalikannya ke abu-abu setelah selesai!

## ![](/icons/cursor.webp) Kursor {#cursor}

### Lingkaran {#show-circle-while-sculpting}
Kapan lingkaran jari-jari kuas ditampilkan:

* `Otomatis` - menampilkan lingkaran, tetapi menyembunyikannya saat Anda memahat.
* `Tidak` - tidak pernah menampilkan lingkaran.
* `Ya` - selalu menampilkan lingkaran, bahkan saat memahat.

### Tampilkan titik kecil {#show-small-dot}
Menampilkan titik di tengah goresan kuas saat memahat, atau saat poros kamera berubah.

### Tampilkan penstabil tali {#show-rope-stabilizer}
Menggambar garis yang menunjukkan panjang tali saat [Stabilisator tali malas](stroke.md#lazy-rope-stabilizer) aktif di pengaturan goresan.

### Tampilkan petunjuk gulir {#show-roll-hint}
Menampilkan panduan arah putaran saat Anda memakai pintasan tombol untuk memiringkan kamera.

### ![](/icons/radius.webp) Ukuran {#dot-size}
Ukuran titik kecil.

### Warna {#cursor-colors}
Kursor berganti warna tergantung apa yang sedang Anda lakukan: `Memahat`, `Latar belakang` (saat kursor berada di atas latar belakang), `Topeng`, `Haluskan`, `Kamera` dan `Jari-jari`. Setiap warna bisa diatur di sini.

## ![](/icons/cursor.webp) Indikator {#indicator}
![](/images/settings_indicator.webp)

Menampilkan indikator visual untuk tutorial dan rekaman layar. Atur ke `Ya` untuk mengaktifkannya (di iOS juga ada opsi `Otomatis`).

Tombol `Jari`, `Stylus` dan `Mouse` akan menampilkan ikon saat jenis input tersebut terdeteksi.

### Warna {#indicator-color}
Warna indikator.

### Ukuran/Ikon/Lingkaran {#indicator-shape}
Kontrol untuk mengatur ukuran indikator, serta opasitas ikon dan lingkaran di dalam indikator.

## ![](/icons/wireframe.webp) Kerangka kawat {#wireframe}
![](/images/settings_wireframe.webp)
Mengaktifkan overlay kerangka kawat.

### Sasaran {#target}
Menentukan apakah kerangka kawat ditampilkan pada objek yang tidak dipilih, hanya pada objek yang dipilih, atau pada semua objek.

### Sembunyi {#hide}
Menentukan apakah kerangka kawat tetap ditampilkan untuk poligon yang disembunyikan.

### Multiresolution: Hanya level 0 {#multiresolution-level-0-only}
Multiresolution menampilkan kerangka kawat level 0 lebih gelap, dan level yang lebih tinggi semakin terang. Jika diaktifkan, opsi ini hanya menampilkan kerangka kawat level 0.

### Warna {#wireframe-color}
Mengatur warna dan opasitas kerangka kawat.

## ![](/icons/grid.webp) Kisi {#grid}
![](/images/settings_grid.webp)
Mengaktifkan kisi.

### Snap {#snap}
Opsi-opsi ini membuat titik-titik pada alat berbasis kurva dan bentuk (`Bubut`, `Tabung`, bentuk poligon dan jalur...) menempel (snap) saat Anda menggambarnya:

* `Snap ke grid` - menempel ke kisi.
* `Snap ke titik (tampilan sejajar)` - menempel ke titik yang sudah ada di dekatnya saat kamera sejajar dengan sebuah sumbu.
* `Snap ke titik (tampilan bebas)` - menempel ke titik yang sudah ada di dekatnya saat kamera tidak sejajar.

### Warna {#grid-color}
Mengatur warna dan opasitas kisi. Opsi-opsi ini muncul saat kisi terlihat.

`Vinyet` memudarkan kisi ke arah tepinya. `Ambang pembagian snap` menentukan, dalam piksel, seberapa rapat garis kisi boleh tampil di layar sebelum kisi beralih ke tingkat subdivisi lain.

## ![](/icons/culling.webp)Dua sisi {#two-sided}
Memungkinkan face poligon terlihat dari kedua sisinya.

### Warna bagian belakang {#backface-color}
`Bagian belakang berwarna` mengaktifkan pewarnaan bagian belakang face, dan `Warna bagian belakang` menentukan warnanya.

## ![](/icons/outline.webp)Garis tepi {#outline}
Mengaktifkan garis tepi di sekitar objek yang dipilih.

### Warna garis tepi, Ketebalan {#outline-color-thickness}
Mengatur warna dan `Ketebalan` garis tepi.


## ![](/icons/bang.webp) Sorot {#highlight}
Mengaktifkan kilatan singkat saat seleksi berubah.
### Warna, Durasi {#color-duration}
Mengatur warna dan lama kilatan dalam milidetik.

## ![](/icons/navigator.webp) Navigator {#snap-cube}
![](/images/settings_snapcube.webp)

Menampilkan ikon bantu di pojok adegan, berguna untuk beralih cepat antara tampilan depan/belakang/kiri/kanan/atas/bawah. Ketuk sisi-sisinya untuk berpindah antar tampilan ortografis.

### Bentuk {#shape}
Pilih antara bentuk bola, kubus, atau gnomon untuk navigator.

### Batasi penyelarasan {#restrict-alignment}
Menyelaraskan tampilan snap dengan sumbu dunia. Jika diaktifkan, hanya 6 tampilan utama yang bisa dipakai. Pada `Otomatis`, batasan ini hanya berlaku saat kamera dalam mode `Meja putar`.

### Ukuran {#size}
Mengatur ukuran navigator.

### Balik 180° {#flip-180}
Mengaktifkan perilaku ketukan sehingga jika tampilan sedang menempel, mengetuk bagian tengah navigator akan memutar tampilan 180 derajat. Misalnya, jika tampilan menempel ke depan, mengetuk navigator akan memutar ke tampilan belakang.

### Tepi & sudut {#edges-corners}
Menambahkan tampilan snap di tepi dan sudut (zona berwarna kuning tua). Tidak tersedia untuk bentuk gnomon.

### Seret meja putar {#turntable-drag}
Menyeret navigator akan memutar tampilan tanpa memiringkan kamera, dan berhenti sejenak di setiap tampilan snap. Nonaktifkan untuk menyeret navigator dengan rotasi `Bola jejak`. Apa pun pilihannya, seretan tetap horizontal atau vertikal. Dengan kamera `Meja putar`, navigator selalu diseret dengan cara ini.

### Posisi {#snap-position}
Menentukan di pojok mana navigator berada.


## ![](/icons/list.webp) Statistik {#stats}
![](/images/settings_stats.webp)

Menampilkan informasi tentang memori sistem, jumlah total verteks di adegan, dan jumlah verteks seleksi saat ini.

### Posisi {#stats-position}
Menentukan di pojok mana statistik berada.

## ![](/icons/edit_radius.webp) Gagang {#handle}
Pengaturan untuk gagang yang Anda seret di viewport, seperti gizmo.

### Masukan numerik {#gizmo-input}
Memungkinkan masukan angka saat mengetuk salah satu kontrol gizmo.

### Sembunyikan saat berinteraksi {#hide-on-interaction}
Memudarkan gizmo saat Anda berinteraksi dengannya, agar tidak menghalangi.

### ![](/icons/opacity.webp) Opasitas {#handle-opacity}
Opasitas gagang.

## ![](/icons/shape_lasso.webp) Bentuk {#shape-settings}
Bagaimana bentuk yang Anda gambar dengan goresan bentuk (laso, persegi panjang, kurva...) tampil di layar.

### ![](/icons/opacity.webp) Isian, Garis tepi {#shape-fill-outline}
Opasitas bagian dalam bentuk dan garis di sekelilingnya.

### Warna {#shape-colors}
Warna bentuk untuk setiap jenis alat: `Topeng`, `Sembunyi`, `Grup Face` dan `Pangkas`.

## ![](/icons/array.webp) Pengulang {#primitive-repeaters}
Batas untuk salinan yang dibuat oleh [pengulang](scene#repeaters) (array, radial, kurva, permukaan). Batas ini menjaga Nomad tetap responsif saat sebuah pengulang lepas kendali.

### ![](/icons/cube.webp) Maks. salinan {#repeater-max-copies}
Jumlah salinan terbanyak yang dibuat oleh satu pengulang. Nomad kesulitan menangani banyak objek, berapa pun ukurannya.

### ![](/icons/cube.webp) Salinan dalam adegan {#repeater-scene-copies}
Anggaran salinan untuk seluruh adegan. Salinan low poly hanya memakan sedikit geometri tetapi tetap merupakan objek utuh, jadi batas inilah yang paling dulu tercapai oleh salinan-salinan kecil.

### ![](/icons/triangle.webp) Face maksimum {#repeater-max-faces}
Anggaran face untuk semua salinan di adegan. Jika terlampaui, objek yang paling berat kehilangan salinannya lebih dulu.

## ![](/icons/multires.webp) Multiresolution {#multires}
### Jumlah verteks maksimum {#multires-lowres-count}
Menetapkan ambang agar operasi subdivisi multiresolution tidak melebihi jumlah verteks ini, yang kemungkinan besar akan membuat Nomad crash: Nomad tidak memeriksa memori yang tersedia sebelum melakukan subdivisi. Nilai bawaannya 10 juta.
### Ambang resolusi rendah {#multires-lowres-threshold}
Versi mesh dengan resolusi lebih rendah bisa ditampilkan saat Anda menggerakkan kamera. Anda bisa menaikkan nilai ini jika ingin menampilkan mesh dengan resolusi yang lebih tinggi.

## Pengaturan {#advanced}
### ![](/icons/reset.webp) Reset ke default {#reset}
Mengatur ulang semua pengaturan preferensi aplikasi ke nilai bawaannya.

Beberapa sumber daya disimpan secara terpisah dan TIDAK diatur ulang: proyek, pintasan tombol, preset alat, lingkungan HDR, MatCap, alpha, tekstur kuas, dan gambar referensi. Semua yang disimpan bersama proyek, seperti pencahayaan, pemrosesan pasca, atau tampilan kamera, juga tetap utuh.
