# Memulai

## Selamat datang di Nomad!

Nomad adalah aplikasi pemodelan 3D (3D sculpting) yang bekerja di banyak perangkat, dan paling optimal digunakan pada tablet dengan stylus yang sensitif terhadap tekanan, misalnya Apple iPad dengan Apple Pencil, atau Samsung Galaxy Tab dengan stylus.

Aplikasi ini terinspirasi dari aplikasi sculpting desktop seperti ZBrush dan Blender, dengan fokus pada antarmuka yang mudah dipahami tanpa mengorbankan fitur. Jika Anda sudah pernah menggunakan aplikasi sculpting 3D sebelumnya, Nomad akan terasa sangat familiar.

Jika ini adalah pertama kalinya Anda melakukan sculpting 3D, ada baiknya mengetahui beberapa dasar terlebih dahulu.

::: tip Lebih suka video?
Youtube sekarang memiliki BANYAK video tutorial untuk pemula, berikut beberapa tautan yang bagus:

* [Nomad Sculpt Crash Course oleh Dave Reed](https://www.youtube.com/watch?v=69m86ICy2Q4)
* [Tutorial pemula Nomad Sculpt oleh Small Robot Studio](https://www.youtube.com/watch?v=J644wXoTiww)
* [Seri NOMAD FOR BEGINNERS oleh SouthernGFX](https://www.youtube.com/watch?v=bEh0WxRoOmg)

Ada baiknya memeriksa kanal utama para kreator tersebut, mereka sering mengunggah tutorial baru.
:::

## Sculpt pertama Anda

Saat pertama kali menjalankan Nomad, Anda akan melihat sebuah bola di layar. Cukup seret stylus Anda di atas bola tersebut untuk mulai melakukan sculpting. Simetri diaktifkan secara bawaan untuk memudahkan proses sculpting.

![](/videos/gettingstarted_01.mp4)

Untuk memperbesar atau memperkecil kuas, gunakan penggeser radius di sebelah kiri.

![](/videos/gettingstarted_02.mp4)

Untuk memperkuat atau memperlemah kuas, gunakan penggeser intensitas di sebelah kiri.

![](/videos/gettingstarted_03.mp4)

Alat bawaan adalah `Clay tool`, dan alat ini menambahkan volume ke permukaan. Untuk mengurangi volume dari permukaan, ketuk tombol `Sub` di sebelah kiri. Untuk kembali menambahkan volume ke permukaan, ketuk tombol Sub lagi.

![](/videos/gettingstarted_04.mp4)

Untuk menghaluskan permukaan, ketuk tombol `Smooth`. Untuk kembali ke sculpting biasa, ketuk tombol Smooth lagi.

![](/videos/gettingstarted_05.mp4)

Untuk memutar kamera mengelilingi model, seret di area kosong di luar model.

![](/videos/gettingstarted_06.mp4)

Untuk melakukan zoom, gunakan gestur cubit/zoom dengan dua jari.

![](/videos/gettingstarted_07.mp4)

Untuk menggeser (pan) kamera, tekan 2 jari di layar lalu seret.

![](/videos/gettingstarted_08.mp4)

Jika Anda melakukan kesalahan, ketukan dua jari akan melakukan undo, atau gunakan tombol undo di kiri bawah. 

![](/videos/gettingstarted_09.mp4)

::: tip Rilis desktop
Di desktop, tombol alt/opt digunakan untuk mengontrol kamera:

* tip seret di area kosong = memutar kamera
* alt+tip seret = pan
* alt+tip seret, lalu lepaskan alt = zoom (sama seperti zbrush)

Dengan tablet Wacom yang memiliki 2 tombol atau lebih pada pena, gunakan pengaturan Wacom untuk mengonfigurasi ujung pena dan tombol seperti ini:

* tip = klik kiri
* rocker bawah = klik tengah
* rocker atas = klik kanan

Dengan pengaturan tersebut, Anda dapat memanipulasi kamera hanya dengan pena:

* rocker atas dan gerakan hover = memutar kamera
* rocker bawah dan gerakan hover = pan
:::

## Menambahkan warna

Nomad memungkinkan Anda mengecat permukaan sculpt Anda. Dari menu alat di sebelah kanan, cari alat `Paint`, lalu klik. Di toolbar kiri akan muncul sebuah bola berwarna. Klik bola tersebut, ini akan menampilkan pemilih warna. Pilih warna, lalu lukis di model Anda.

![](/videos/gettingstarted_10.mp4)

Untuk menghapus, ketuk tombol `Erase` di toolbar kiri, lalu hapus di permukaan. Ketuk tombol erase lagi untuk kembali ke mode paint.

![](/videos/gettingstarted_11.mp4)

Dengan menggunakan kuas clay dalam mode add/sub, smooth, dan paint, coba lihat apakah Anda bisa membuat kepala kartun sederhana:

![](/images/gettingstarted_head1.webp)

## Alat lainnya

Palet alat memiliki banyak tool untuk membantu proses sculpting. Sejauh ini Anda telah menggunakan kuas clay (alat awal bawaan), smooth, dan paint. Karena smooth sering digunakan, alat ini memiliki pintasan tambahan di toolbar kiri.

Alat-alat di Nomad dapat melakukan berbagai hal, mulai dari alat yang berhubungan langsung dengan sculpting seperti move, crease, inflate, hingga alat seperti split dan trim yang lebih mirip alat pertukangan kayu atau logam. Halaman [Tools](tools.md) memiliki informasi lebih lanjut.

Coba gunakan alat move, crease, inflate, dan smooth untuk menambahkan lebih banyak detail pada kepala Anda, mengubah bentuknya:

![](/images/gettingstarted_head2.webp)

Sekarang setelah Anda mengetahui dasar-dasar Nomad, mari kita lihat bagian lain dari antarmuka.

## Antarmuka

![](/images/interface_overview1.webp)

* `Top menus` - Menu untuk mengakses sebagian besar fitur Nomad. Menu kiri atas terutama mencakup fitur scene dan objek, menu kanan atas terkait dengan alat. Pada layar yang lebih kecil, menu-menu ini akan digabung untuk menghemat ruang.
* `Stats` - Informasi tentang scene, objek saat ini, status mask, penggunaan memori.
* `Nav Cube` - Bantuan visual untuk menunjukkan sisi mana dari sculpt yang sedang Anda lihat, sekaligus pintasan untuk melompat ke berbagai sudut pandang. Mengetuk kubus akan mengubah tampilan ke sisi yang diketuk. Menyeret kubus akan memutarnya. Ketuk ikon kecil di samping kubus untuk memusatkan tampilan pada objek saat ini, atau mengatur ulang ke tampilan awal bawaan.
* `Toolbox` - Alat-alat Nomad tersedia di area yang dapat digulir ini.
* `Left toolbar` - Penggeser untuk radius dan intensitas untuk sebagian besar alat, tombol kontekstual untuk alat lain, dan pintasan untuk simetri, mode alt/sub alat, masking, smoothing, gizmo, dan opsi paint.
* `Bottom toolbar` - Pintasan untuk fitur yang sering digunakan, dijelaskan di bawah.

::: tip Kidal?
Anda dapat mencerminkan posisi dan urutan semua toolbar, lihat [Mirror top bar](interface.md#mirror-top-bar) dan opsi terkait lainnya.
:::

## Bottom toolbar

![](/images/interface_bottom_toolbar.webp)

* `Undo` - mengembalikan operasi terakhir
* `Redo` - mengulang kembali operasi yang di-undo terakhir
* `History` - mengakses opsi riwayat, dijelaskan di menu [History](history.md).
* `Solo` - Mengaktifkan tampilan hanya objek saat ini, atau semua objek
* `X-Ray` - Membuat semua objek lain dirender dalam mode x-ray, dan objek saat ini tetap solid. Tekan lama atau geser ke atas untuk mengatur warna dan opasitas mode x-ray.
* `Voxel` - Pintasan untuk tombol [Voxel Remesher](topology.md#voxel-remesher). Tekan lama atau geser ke atas untuk menampilkan pintasan pengaturan kualitas voxel remesh.
* `Grid` - Mengaktifkan/menonaktifkan tampilan grid. Tekan lama atau geser ke atas untuk menampilkan opsi grid.
* `Wire` - Mengaktifkan/menonaktifkan overlay wireframe. Tekan lama atau geser ke atas untuk menampilkan opsi wireframe.
* `Inspect` - Mengaktifkan tampilan data tambahan tentang mesh saat ini. Secara bawaan akan menampilkan UV, tetapi tekan lama atau geser ke atas untuk memeriksa properti lain jika ada, dan apakah ini ditampilkan di latar belakang atau langsung pada mesh.

## Langkah berikutnya

Apa yang sebaiknya Anda pelajari selanjutnya terserah Anda, dan apa yang Anda anggap menarik! Berikut beberapa saran:

Ingin belajar lebih banyak tentang alat-alat sculpting? Buka bagian [Tools](tools.md).

Ingin mengekspor model Anda? Atau mengimpor model untuk di-sculpt? Atau membuat gambar dari sculpt Anda? Buka bagian [Files](files.md).

Ingin belajar lebih banyak tentang cara mengontrol detail pada sculpt Anda? Buka bagian [Topology](topology.md) dan pelajari tentang multires dan decimation.

Ingin bekerja dengan lebih banyak objek? Menggabungkan objek sederhana dan primitif menjadi scene yang lebih besar? Buka bagian [Scene](scene.md).

Ingin mempelajari *semua hal* tentang Nomad? Pilihan yang bagus! Manual ini mencakup seluruh Nomad, berisi banyak tips dan trik, dan memiliki fungsi pencarian yang sangat baik di bagian atas. Gunakan navigasi di sebelah kiri untuk mempelajari lebih lanjut.

Jika Anda lebih suka video, Holger Schönischka telah membuat koleksi besar tips dan trik untuk Nomad di Youtube: https://www.youtube.com/@ProcreateFX/videos


## Mendapatkan bantuan

Jika Anda masih memiliki pertanyaan setelah membaca manual dan menonton video tutorial, ada tiga cara utama untuk berbicara dengan pengguna Nomad lainnya atau pengembang Nomad:

* Kunjungi forum: [forum.nomadsculpt.com](http://forum.nomadsculpt.com)
* Bergabung dengan obrolan Discord Nomad: [https://discord.com/invite/8h7BwpRz29](https://discord.com/invite/8h7BwpRz29)
* Hubungi pengembang secara langsung di support@nomadsculpt.com
