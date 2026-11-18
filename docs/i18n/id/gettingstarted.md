# ![](/icons/play.webp) Memulai {#getting-started}

## Selamat datang di Nomad! {#welcome-to-nomad}

Nomad adalah aplikasi pahat 3d yang berjalan di banyak perangkat, dan paling nyaman dipakai di tablet dengan stylus yang peka tekanan, misalnya Apple iPad dengan Pencil, atau Samsung Galaxy Tab dengan stylus.

Nomad terinspirasi dari aplikasi pahat desktop seperti ZBrush dan Blender, dengan fokus pada antarmuka yang mudah dipahami tanpa mengorbankan fitur. Jika Anda pernah memakai aplikasi pahat 3d sebelumnya, Nomad akan terasa sangat familier.

Jika ini pertama kalinya Anda memahat 3d, ada baiknya Anda mengenal beberapa dasarnya.

::: tip Lebih suka video?
Di YouTube sekarang ada BANYAK sekali video tutorial untuk pemula, berikut beberapa tautan yang bagus:

* [Nomad Sculpt Crash Course oleh Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Tutorial pemula Nomad Sculpt oleh Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [Seri NOMAD FOR BEGINNERS oleh SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

Saluran utama para kreator ini layak Anda kunjungi, mereka sering mengunggah tutorial baru.
:::

## Pahatan pertama Anda {#your-first-sculpt}

Saat pertama kali membuka Nomad, Anda akan melihat sebuah bola di layar. Cukup seret stylus Anda di atas bola untuk mulai memahat. Simetri aktif secara bawaan agar memahat lebih mudah.

![](/videos/gettingstarted_01.mp4)

Untuk memperbesar atau memperkecil kuas, gunakan penggeser radius di sebelah kiri.

![](/videos/gettingstarted_02.mp4)

Untuk membuat kuas lebih kuat atau lebih lemah, gunakan penggeser intensitas di sebelah kiri.

![](/videos/gettingstarted_03.mp4)

Alat bawaannya adalah alat `Tanah Liat`, yang menambahkan material ke permukaan. Untuk mengurangi permukaan, ketuk tombol `Kurang` di sebelah kiri. Untuk kembali menambah, ketuk tombol Kurang sekali lagi.

![](/videos/gettingstarted_04.mp4)

Untuk menghaluskan permukaan, ketuk tombol `Haluskan`. Untuk kembali memahat seperti biasa, ketuk tombol Haluskan sekali lagi.

![](/videos/gettingstarted_05.mp4)

Untuk berputar mengelilingi model, seret di ruang kosong di luar model.

![](/videos/gettingstarted_06.mp4)

Untuk zoom, gunakan gerakan mencubit dengan dua jari.

![](/videos/gettingstarted_07.mp4)

Untuk menggeser kamera, tekan 2 jari di layar lalu seret.

![](/videos/gettingstarted_08.mp4)

Jika Anda membuat kesalahan, ketukan 2 jari akan membatalkannya, atau gunakan tombol urungkan di kiri bawah. 

![](/videos/gettingstarted_09.mp4)

::: tip Versi desktop
Di desktop, tombol alt/opt dipakai untuk mengendalikan kamera:

* seret ujung pena di ruang kosong = putar kamera
* alt+seret ujung pena = geser
* alt+seret ujung pena, lalu lepaskan alt = zoom (sama seperti ZBrush)

Dengan tablet Wacom yang penanya memiliki 2 tombol atau lebih, gunakan pengaturan Wacom untuk mengonfigurasi ujung pena dan tombol-tombolnya seperti ini:

* ujung pena = klik kiri
* tombol rocker bawah = klik tengah
* tombol rocker atas = klik kanan

Dengan pengaturan tersebut, Anda bisa mengendalikan kamera sepenuhnya dengan pena:

* tombol rocker atas dan gerakkan pena di atas layar tanpa menyentuh = putar kamera
* tombol rocker bawah dan gerakkan pena di atas layar tanpa menyentuh = geser
:::

## Menambahkan warna {#add-color}

Nomad memungkinkan Anda mewarnai permukaan pahatan. Dari menu alat di sebelah kanan, cari alat `Melukis`, lalu klik. Di bilah alat kiri akan muncul sebuah bola berwarna. Klik bola itu untuk membuka pemilih warna. Pilih sebuah warna, lalu lukis di atas model Anda.

![](/videos/gettingstarted_10.mp4)

Untuk menghapus, ketuk tombol `Hapus` di bilah alat kiri, lalu hapus di permukaan. Ketuk tombol hapus sekali lagi untuk kembali ke mode melukis.

![](/videos/gettingstarted_11.mp4)

Dengan memakai kuas tanah liat dalam mode tambah/kurang, haluskan, dan lukis, cobalah membuat kepala kartun sederhana:

![](/images/gettingstarted_head1.webp)

## Alat lainnya {#other-tools}

Palet alat berisi banyak alat untuk membantu Anda memahat. Sejauh ini Anda sudah memakai kuas tanah liat (alat awal bawaan), haluskan, dan lukis. Karena haluskan sangat sering dipakai, alat ini punya pintasan tambahan di bilah alat sebelah kiri.

Alat-alat di Nomad bisa melakukan banyak hal, mulai dari alat yang berkaitan dengan pahat seperti pindah, lipatan, dan kembung, hingga alat seperti pisah dan pangkas yang lebih mirip perkakas tukang kayu atau pandai logam. Halaman [Alat](tools.md) berisi informasi lebih lanjut.

Cobalah memakai alat pindah, lipatan, kembung, dan haluskan untuk menambahkan detail pada kepala Anda dan mengubah bentuknya:

![](/images/gettingstarted_head2.webp)

Sekarang setelah Anda mengenal dasar-dasar Nomad, mari kita lihat bagian antarmuka lainnya.

## Antarmuka {#interface}

![](/images/interface_overview1.webp)

* `Menu atas` - Menu untuk mengakses sebagian besar fitur Nomad. Menu di kiri atas terutama berisi fitur adegan dan objek, sedangkan menu di kanan atas berkaitan dengan alat. Di layar yang lebih kecil, menu-menu ini akan digabung untuk menghemat ruang.
* `Statistik` - Informasi tentang adegan, objek saat ini, status topeng, dan penggunaan memori.
* `Navigator` - Alat bantu yang menunjukkan sisi pahatan mana yang sedang Anda lihat, sekaligus pintasan untuk melompat ke tampilan yang berbeda. Mengetuk salah satu sisi akan memindahkan tampilan ke sisi tersebut. Menyeret navigator akan memutar tampilan. Ketuk ikon kecil di sampingnya untuk membingkai objek saat ini, kembali ke tampilan awal bawaan, mengunci kamera, atau menampilkan/menyembunyikan kisi. Tampilannya (kubus, bola, atau gnomon) serta posisinya bisa diubah di [Pengaturan](settings.md#snap-cube).
* `Kotak peralatan` - Alat-alat Nomad tersedia di area yang bisa digulir ini.
* `Bilah alat kiri` - Penggeser radius dan intensitas untuk sebagian besar alat, tombol khusus untuk alat lainnya, serta pintasan untuk simetri, mode alt/kurang alat, penghalusan, topeng, menyembunyikan, grup face, gizmo, dan opsi melukis. Anda bisa mengatur ulang urutan pintasan di menu [Antarmuka](interface.md#side-bar).
* `Bilah alat bawah` - Pintasan untuk fitur yang sering dipakai, dijelaskan di bawah.

::: tip Kidal?
Anda bisa mencerminkan posisi dan urutan semua bilah alat, lihat [Cermin bilah atas](interface.md#mirror-top-bar) dan opsi terkait lainnya.
:::

## Bilah alat bawah {#bottom-toolbar}

![](/images/interface_bottom_toolbar.webp)

* `Urungkan` - membatalkan operasi terakhir
* `Ulangi` - mengembalikan operasi yang terakhir dibatalkan
* `Riwayat` - mengakses opsi riwayat, dijelaskan di menu [Riwayat](history.md).
* `Solo` - Beralih antara hanya menampilkan objek saat ini, atau semua objek
* `X-Ray` - Menampilkan semua objek lain dalam mode x-ray, sementara objek saat ini tetap padat. Tekan lama atau geser ke atas untuk memilih matcap dan warna x-ray, serta objek mana yang terkena.
* `Voxel` - Pintasan untuk tombol remesh voxel di [Remesh voxel](topology.md#voxel-remesher). Tekan lama atau geser ke atas untuk memunculkan opsi remesh voxel, seperti resolusinya.
* `Grid` - Menampilkan atau menyembunyikan kisi. Tekan lama atau geser ke atas untuk memunculkan opsi kisi, seperti warnanya dan snapping.
* `Kerangka kawat` - Menampilkan atau menyembunyikan overlay kerangka kawat. Tekan lama atau geser ke atas untuk memunculkan opsi kerangka kawat.
* `Inspektur` - Menampilkan data tambahan tentang mesh saat ini. Secara bawaan yang ditampilkan adalah UV, tetapi dengan menekan lama atau menggeser ke atas Anda bisa memeriksa properti lain jika ada, dan memilih apakah ditampilkan di latar belakang atau di atas mesh.
* `Log` - Menampilkan atau menyembunyikan jendela berisi log debug Nomad.
* `Grup Face` - Menampilkan atau menyembunyikan overlay grup face, lihat alat [Grup Face](tools.md#facegroup).

Anda bisa menambah, menghapus, dan mengatur ulang urutan pintasan ini di menu [Antarmuka](interface.md#add-shortcuts-bottom).

## Langkah berikutnya {#next-steps}

Apa yang ingin Anda pelajari selanjutnya terserah Anda, tergantung apa yang menurut Anda menarik! Berikut beberapa saran:

Ingin mempelajari alat-alat pahat lebih dalam? Kunjungi bagian [Alat](tools.md).

Ingin mengekspor model Anda? Atau mengimpor model untuk dipahat? Atau membuat gambar dari pahatan Anda? Kunjungi bagian [File](files.md).

Ingin belajar lebih banyak tentang mengatur tingkat detail pahatan Anda? Kunjungi bagian [Topologi](topology.md) dan pelajari tentang multiresolution dan desimasi.

Ingin bekerja dengan lebih banyak objek? Menggabungkan objek sederhana dan primitif menjadi adegan yang lebih besar? Kunjungi bagian [Adegan](scene.md).

Ingin mempelajari *segala hal* tentang Nomad? Pilihan yang bagus! Manual ini mencakup seluruh fitur Nomad, berisi banyak tips dan trik, dan punya fungsi pencarian yang bagus di bagian atas. Gunakan navigasi di sebelah kiri untuk mempelajari lebih lanjut.

Jika Anda lebih suka video, Holger Schönischka telah membuat koleksi besar tips dan trik Nomad di YouTube: https://www.youtube.com/@ProcreateFX/videos


## Mendapatkan bantuan {#getting-help}

Jika Anda masih punya pertanyaan setelah membaca manual dan menonton video tutorial, ada tiga cara utama untuk berbicara dengan pengguna Nomad lainnya atau dengan pengembang Nomad:

* Kunjungi forum: [forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* Bergabunglah di obrolan Discord Nomad: [https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* Hubungi pengembang langsung di support@nomadsculpt.com
