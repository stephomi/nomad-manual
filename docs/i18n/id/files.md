# ![](/icons/open.webp) File {#files}

Menu File memungkinkan Anda menyimpan dan memuat proyek Nomad, mengimpor dan mengekspor model 3d, mengekspor gambar hasil render, dan menghubungkan Nomad dengan aplikasi lain. Menu ini punya tiga tab: `File`, `Render` dan `Tautan`.

![](/images/file_menu.webp)

## Proyek {#project}
![](/images/file_project.webp)

Gambar mini di bagian atas menampilkan proyek saat ini, dengan ukuran filenya, simpan otomatis dan riwayat tersimpan di sebelahnya. Ketuk gambar mini untuk membuka penjelajah mini berisi proyek-proyek Anda, lalu ketuk sebuah proyek untuk memunculkan menu untuk membuka, menambahkan, menimpa, mengklon, mengganti nama, atau menghapusnya.

Jika proyek punya perubahan yang belum disimpan, `Perubahan yang tidak disimpan!` ditampilkan di bawah gambar mini.

### Ruang Lingkup {#scope}
Di desktop, pilih tempat proyek Anda disimpan:
* `Internal` - Pilihan bawaan, sama seperti di perangkat seluler. Proyek hanya disimpan di dalam folder utama Nomad.
* `Di Tempat` - Saat Anda membuka proyek dari luar folder Nomad, menyimpan akan menimpa file aslinya. Simpan Otomatis tidak bekerja untuk proyek eksternal ini.

### ![](/icons/nomad.webp) Prasetel {#preset}
Akses kumpulan demo dan komponen karakter. Pilih salah satu, lalu pilih lagi untuk memilih `Buka` atau `Tambahkan ke adegan`. Anda juga bisa mengunduh model gratis dari Poly Haven melalui penjelajah ini.

![](/images/file_preset_preview.webp)

### ![](/icons/history.webp) Riwayat... {#history}
Akses cepat ke opsi riwayat proyek, seperti `Simpan riwayat`, yang mempertahankan riwayat urungkan saat proyek disimpan. Lencana hijau pada tombol menandakan bahwa riwayat disimpan bersama proyek. Lihat [Riwayat](history.md#save-history) untuk detailnya.

### ![](/icons/save.webp) Simpan {#save}
Menyimpan proyek Nomad. Jika proyek belum pernah disimpan, Anda akan diminta memberi nama.

### ![](/icons/save_as.webp) Simpan Sebagai... {#save-as}
Menyimpan proyek dengan nama baru, sebagai proyek baru.

### ![](/icons/save_as.webp) Timpa... {#overwrite}
Menampilkan penjelajah proyek untuk menyimpan adegan saat ini di atas proyek lain. Aktifkan `Hanya sertakan objek yang dipilih` untuk menyimpan objek yang dipilih saja, bukan seluruh adegan. Penjelajahnya juga punya tombol `Simpan Sebagai...` untuk menyimpannya sebagai proyek baru.

### ![](/icons/pencil.webp) Ganti nama {#rename}
Menampilkan kotak teks untuk mengganti nama proyek saat ini.

### ![](/icons/open.webp) Buka... {#open}
Menampilkan penjelajah proyek untuk membuka sebuah proyek.

### ![](/icons/add_file.webp) Tambahkan ke adegan... {#add}
Menampilkan penjelajah proyek; saat sebuah proyek dipilih, isinya akan digabungkan ke adegan saat ini.

### ![](/icons/trash.webp) Hapus... {#delete}
Menampilkan penjelajah proyek; proyek yang dipilih akan dihapus dari sistem file.

### ![](/icons/new_file.webp) Baru {#new}
Memulai proyek baru. Jika ada perubahan yang belum disimpan, Anda akan diminta konfirmasi. Konfirmasi ini memungkinkan Anda memilih `Pertahankan` atau `Setel ulang` untuk pengaturan `Latar belakang`, `Lingkungan`, `MatCap` dan `X-Ray`, serta memilih apakah proyek baru memakai `Simpan riwayat`.

### ![](/icons/autosave.webp) Simpan Otomatis... {#auto-save}
Menu untuk mengatur opsi simpan otomatis. Aktifkan `Simpan Otomatis` untuk menyimpan proyek Anda ke file terpisah secara berkala. Lencana pada tombol menunjukkan apakah fitur ini menyala.

Nomad tidak menyimpan di latar belakang karena file 3d bisa cukup besar, sehingga bisa menimbulkan jeda yang terasa saat Anda sedang memahat.

Selain itu, untuk menghindari masalah kehabisan memori, adegan biasanya dikompresi sebelum disimpan.
Proses kompresi/dekompresi ini juga memperlambat penyimpanan.

### Interval penyimpanan {#timer-pop-up}
Berapa menit Nomad menunggu di antara setiap simpan otomatis.

### Tampilkan hitung mundur {#popup-timeout}
Menampilkan hitung mundur sebelum setiap simpan otomatis, agar Anda bisa membatalkannya jika sedang di tengah pekerjaan. Jika dinonaktifkan, Nomad menyimpan begitu Anda berhenti memahat.

### ![](/icons/trash.webp) Buang Simpan Otomatis {#discard-autosave}
Jika ada file simpan otomatis untuk sebuah proyek, file itu akan dimuat secara otomatis sebagai ganti proyek aslinya. Jika Anda tidak membutuhkannya, tombol ini akan menghapus file simpan otomatis tersebut. Memuat file itu kemudian akan memuat simpanan manual terakhir dari proyek.

### ![](/icons/open.webp) Buka simpanan yang usang {#open-outdated-save}
Jika sebuah proyek punya simpan otomatis sekaligus simpan manual, tombol ini membuka yang lebih lama dari keduanya (`Buka auto simpan yang usang` atau `Buka simpan manual yang usang`), beserta tanggalnya. Praktis jika simpanan terbaru bukan yang Anda inginkan.

### ![](/icons/storage.webp) Baru dihapus... {#recently-deleted}
Nomad menyimpan data proyek yang telah keluar dari folder proyek, serta file yang tergantikan oleh impor, selama beberapa hari sebelum menghapusnya secara permanen. File yang gagal diimpor tetap ada sampai Anda menghapusnya. Daftar ini menampilkannya beserta ukuran dan tanggalnya, jadi Anda bisa menghapusnya satu per satu atau dengan `Hapus semua`.

## Impor {#import}

### ![](/icons/add_file.webp) Impor {#import-button}
Untuk mengimpor file 3d yang bukan proyek Nomad.

Saat Anda mengimpor file adegan eksternal ke Nomad, Anda bisa *menambahkannya* atau memulai proyek *baru* dengannya.

Menambahkan file akan menambahkan objek-objeknya ke adegan saat ini.
Memilih `Baru` akan membuat proyek Nomad baru yang berisi objek-objek tersebut.

Jendela impor menampilkan setiap file yang Anda pilih, masing-masing dengan opsi impornya sendiri. Gambar juga bisa diimpor dengan cara ini: pilih untuk setiap gambar apakah akan menjadi `HDRI`, `MatCap`, `Referensi`, `Alpha`, `Tekstur` atau `VDM`.

Nomad bisa mengimpor format berikut:
- Nomad (.nom)
- glTF (.glb, .gltf)
- OBJ (.obj)
- STL (.stl)
- PLY (.ply)
- FBX (.fbx)
- ZBrush (.ztl, .zpr)
- USD (.usd, .usdz, .usda, .usdc), di platform yang mendukungnya

### ![](/icons/cog.webp) Pengaturan {#advanced}
Tombol `Pengaturan...` di sebelah gambar mini proyek menampilkan opsi impor utama. Pengaturan ini tidak disimpan, dan jendela impor menampilkan opsi yang berlaku untuk file yang sedang Anda impor.

### Semua format {#project-gltf-obj-stl-fbx}
#### ![](/icons/nomad.webp) Pertahankan topologi {#keep-topology}
Secara bawaan, Nomad akan mencoba memperbaiki geometri yang bermasalah saat memuat. Mengaktifkan opsi ini mencegah Nomad mengurutkan ulang verteks/face, menggabungkan duplikat, dan menghapus verteks yang tidak terpakai.

::: warning
Dengan `Pertahankan topologi`, operasi seperti Boolean, Gabung, Desimasi atau Manifold mungkin tidak menggabungkan verteks duplikat.
:::

#### ![](/icons/image.webp) Lewati tekstur {#skip-textures}
Tidak memuat tekstur yang tersemat di dalam file, untuk format yang mendukungnya seperti glTF.

### Nomad / glTF {#project-gltf}
#### ![](/icons/sliders.webp) Muat pengaturan UI {#keep-gui-settings}
Saat membuka atau mengimpor file proyek, muat semua pengaturan antarmuka yang tersimpan di dalamnya.

### OBJ {#obj}
#### ![](/icons/group_gray.webp) Pisahkan OBJ berdasarkan grup {#split-obj-by-groups}
Memisahkan grup OBJ menjadi objek-objek terpisah.

#### ![](/icons/vertex.webp) Gabungkan posisi duplikat {#merge-duplicate-positions}
Menggabungkan verteks yang posisinya sama.

#### ![](/icons/uv.webp) Gabungkan duplikat UV {#merge-duplicate-uvs}
Menggabungkan koordinat tekstur yang UV-nya sama.

#### ![](/icons/paint.webp) Ruang Warna {#color-space}
Mengatur cara mode warna dari file dibaca: `Otomatis`, `Linear`, atau `sRGB`. Coba ubah opsi ini jika warnanya tampak tidak benar.

#### ![](/icons/image.webp) Format {#normal-format}
Format normal map pada tekstur: `Otomatis`, `OpenGL (+Y)` atau `DirectX (-Y)`. Coba yang satunya jika detail normal map tampak terbalik.

### PLY / STL {#ply}
#### ![](/icons/paint.webp) Ruang Warna {#color-space-ply}
Mengatur cara mode warna dari file dibaca: `Otomatis`, `Linear`, atau `sRGB`.


### FBX {#fbx}
#### ![](/icons/uv.webp) Gabungkan duplikat UV {#merge-duplicate-uvs-fbx}
Menggabungkan koordinat tekstur yang UV-nya sama.

#### ![](/icons/paint.webp) Ruang Warna {#color-space-fbx}
Mengatur cara mode warna dari file dibaca: `Otomatis`, `Linear`, atau `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-fbx}
Format normal map pada tekstur: `Otomatis`, `OpenGL (+Y)` atau `DirectX (-Y)`.

### USD {#usd}
#### ![](/icons/paint.webp) Ruang Warna {#color-space-usd}
Mengatur cara mode warna dari file dibaca: `Otomatis`, `Linear`, atau `sRGB`.

#### ![](/icons/image.webp) Format {#normal-format-usd}
Format normal map pada tekstur: `Otomatis`, `OpenGL (+Y)` atau `DirectX (-Y)`.



## Ekspor {#export}
Menyimpan ke format geometri 3d yang bisa dipakai di perangkat lunak lain. 

![](/images/file_export.webp)

Setiap format file mendukung fitur yang berbeda, jadi opsi yang tersedia akan berubah sesuai jenis file yang dipilih.

<!-- https://www.tablesgenerator.com/markdown_tables# -->
<!-- http://markdowntable.com/ -->
|                                 | NOM    | GLTF/GLB             | OBJ  | USD | PLY  | STL   | FBX                    |
| :-----------------------------: | :----: | :------------------: | :--: | :--: | :--: | :---: | :--------------------: |
| [Warna verteks](#vertex-colors) | ✅     | ✅                   | ✅   | ✅ | ✅    | ✅    | ✅                     |
| [PBR verteks](#pbr-paint)       | ✅     | Nomad ✅<br>Lainnya ⚠️ | ❌   | ✅ | ✅    | ❌    | ❌                     |
| Quad                            | ✅     | Nomad ✅<br>Lainnya ⚠️ | ✅   | ✅ | ✅    | ❌    | ✅                     |
| [Lapisan](#layers)              | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Objek                           | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Grup Face                       | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Hierarki                        | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Lampu                           | ✅     | ✅                   | ❌   | ✅ | ❌    | ❌    | ✅                     |
| Tekstur                         | ✅     | ✅                   | ✅   | ✅ | ❌    | ❌    | ✅                     |
| Primitif, PascaProses, dll.     | ✅     | Nomad ✅<br>Lainnya ❌ | ❌   | ❌ | ❌    | ❌    | ❌                     |


### ![](/icons/export.webp) Tombol Ekspor {#export-button}
Klik ini untuk mengekspor geometri dengan pengaturan yang dipilih. Tombol ini menampilkan format yang dipilih dan perkiraan ukuran file. Di Android, tombol `Bagikan` di sebelahnya mengirim file langsung ke aplikasi lain.

### Format file {#file-format}
Pilih format ekspor: `NOMAD`, `glTF`, `OBJ`, `FBX`, `PLY`, `STL` atau `USD`. NOMAD adalah format milik Nomad sendiri dan tidak bisa dimuat di perangkat lunak lain, jadi format ini terutama untuk diimpor kembali ke Nomad.

### Termasuk {#allvisibleselected}
Pilih objek mana yang akan diekspor: `Semua`, `Terlihat` atau `Dipilih`. Angka di sebelah setiap opsi menunjukkan berapa banyak objek yang akan diekspor.

### Satu file per objek {#one-file-per-object}
Mengekspor setiap objek ke filenya sendiri. Angkanya menunjukkan berapa banyak file yang akan ditulis.

### Jenis {#type}
Saat ekspor menghasilkan beberapa file (satu file per objek, atau OBJ dengan tekstur), simpan file-file itu dalam `Folder` atau `Zip`. Beberapa aplikasi (Google Drive, One Drive, dll.) tidak mendukung impor folder, jadi Anda bisa memakai Zip sebagai gantinya.

### Sematkan riwayat {#embed-history}
Khusus NOMAD. Menyertakan riwayat urungkan di dalam file, yang akan dipulihkan saat file dibuka di Nomad. Ini menambah ukuran file, dan seluruh adegan harus diekspor sebagai satu file.

### Sematkan aset {#embed-assets}
Khusus NOMAD. Menyertakan matcap, lingkungan, dan font kustom Anda di dalam file. Aset bawaan tidak disematkan.

### Warna verteks {#vertex-colors}
Mengekspor warna verteks jika didukung oleh format file. Sebagian perangkat lunak 3d bisa membacanya, tetapi tidak semua.

Untuk OBJ, Anda bisa memilih:
* `Tidak ada` - Tanpa warna.
* `RGB` - Warna ditambahkan setelah verteks.
* `MRGB (ZBrush)` - Cara alternatif untuk menyandikan warna, yang juga mendukung data masker.

### Ruang Warna {#color-space-export}
Khusus OBJ, dengan warna verteks `RGB`. Menulis warna sebagai `Linear` atau `sRGB`.

### Cat PBR {#pbr-paint}
Mengekspor cat roughness, metalness dan masker. Perangkat lunak lain mungkin mengabaikan data ini.
Warna verteks PBR diekspor sebagai atribut warna verteks sekunder.
Kanal-kanalnya dikemas sebagai berikut:

|           | Kanal    |
| :-------: | :------: |
| Roughness | R        |
| Metalness | G        |
| Masker    | B        |


### Lapisan {#layers}
Lapisan didukung melalui morph target glTF. Ini didukung secara resmi oleh glTF, jadi seharusnya juga bekerja di perangkat lunak lain.
Nomad juga mengekspor warna, roughness dan metalness per lapisan, tetapi data ini akan diabaikan oleh perangkat lunak lain.

### Melukis lapisan {#layer-painting}
Mengekspor cat lapisan, yang biasanya diabaikan oleh perangkat lunak lain.

### Grup Face {#face-group}
Mengekspor grup face; mengekspornya terkadang bisa mengganggu perangkat lunak lain.

### Tulis Objek {#write-objects}
Khusus OBJ. Menjaga objek tetap terpisah. Nonaktifkan untuk mengekspor semuanya sebagai satu objek, misalnya untuk memakai fitur 'Mesh ID / Polygroup' di Substance Painter.

### Normal {#normals}
Mengekspor informasi normal. Perlu diingat bahwa Nomad selalu menghitung normalnya sendiri saat mengimpor format file lain.

### Tangen {#tangents}
Mengekspor informasi tangen, yang dipakai jika model punya normal map. 

### Tekstur {#textures}
Jika tekstur sudah ditambahkan ke material, tekstur itu akan diekspor. Perlu diingat bahwa ini tidak melakukan bake tekstur; itu dilakukan lewat opsi bake di menu Topologi.

### Format {#fbx-format}
Khusus FBX. `Biner` lebih kecil tetapi mungkin tidak bekerja di semua aplikasi, `Ascii` berupa file teks.

### Terkompresi {#compressed}
Khusus FBX. Memperkecil ukuran file, dengan konsekuensi ekspor dan impor yang lebih lambat.

### Prasetel {#usd-preset}
Khusus USD. Pilih aplikasi tujuan ekspor Anda: `OpenUSD`, `Apple`, `Procreate` atau `Zbrush`. Beberapa opsi hanya tersedia untuk prasetel tertentu.

### Instansi {#instance}
Khusus USD. Mengekspor objek instans sebagai instans, alih-alih menduplikasi geometrinya.

### Izinkan skew {#allow-skew}
Khusus USD. Mengizinkan skew pada transformasi matriks. Jika dinonaktifkan, Nomad memecah transformasi yang miring menjadi transformasi skala dan rotasi yang terpisah.

### Pengulang {#repeater}
Khusus USD. Mengekspor salinan yang dibuat oleh pengulang sebagai instans.

### Gabungkan salinan {#join-copies}
Setiap objek beserta salinan pengulangnya menjadi satu objek.

::: tip Tips: Mengimpor roughness dan metalness ke Blender

Blender bisa mengimpor glTF/glb, tetapi tidak otomatis memahami atribut verteks untuk metalness dan roughness. Untuk memakainya, buat node Vertex Color di editor material, lalu atur propertinya ke atribut warna berikutnya (biasanya Col.001). Hubungkan node 'Separate XYZ', kirim X ke roughness, dan Y ke Metallic.

Video ini menunjukkan prosesnya:

![](/videos/blender_pbr.mp4)

::: 

::: tip Tips: Dukungan fitur USD

USD adalah format yang rumit. Spesifikasinya mendukung banyak fitur, tetapi tidak semua perangkat lunak 3d mendukungnya. Misalnya, OSX/iOS tidak mendukung warna verteks. Mode prasetel di pengekspor USD berusaha menebak kompatibilitas terbaik dengan OpenUSD, Apple, Procreate, Zbrush.

::: 

## ![](/icons/screen.webp) Render {#render}

Mengekspor gambar yang menggabungkan semua pengaturan dalam proyek (lampu, material, pascaproses, dll.). 

![](/images/file_render.webp)
### ![](/icons/preview.webp) Pratinjau {#preview}

Tombol `Pratinjau` di sebelah judul menu membuat antarmuka tembus pandang, untuk membantu melihat pembingkaian hasil akhirnya.

### ![](/icons/home.webp) Fokus {#focus}
Membingkai adegan atau seleksi agar pas dengan ukuran render. Ketuk lagi untuk beralih di antara keduanya.

### ![](/icons/map.webp) Peta Tinggi {#heightmap}
Merender adegan sebagai peta ketinggian skala abu-abu dilihat dari kamera, dengan bagian terdekat paling terang. Mengaktifkannya beralih ke ukuran `Persegi` dan membingkai seleksi. Sebuah bilah kecil di viewport memungkinkan Anda mengatur `Fokus` gradiennya.

Saat `Peta Tinggi` aktif, tombol `Simpan sebagai alfa` muncul di sebelah tombol ekspor, untuk menyimpan render sebagai alpha kuas baru alih-alih mengekspor file.

### ![](/icons/opacity.webp) Latar belakang transparan {#transparent-background}
Mengaktifkan kanal alpha untuk render, berguna untuk menggabungkan render dengan gambar lain di program 2d. Perlu diingat bahwa transparansi parsial tidak didukung.

### ![](/icons/sliders.webp) Tampilkan antarmuka {#show-interface}
Menyertakan UI Nomad di dalam render.

### Ukuran akhir {#final-size}
Resolusi yang dipakai untuk render: `Layar`, `720`, `1080`, `4096`, `Persegi` atau `Kustom`.

Saat menu File aktif, garis putus-putus akan digambar di viewport untuk menandai area render jika tidak sama dengan resolusi layar.

### Lebar / Tinggi {#render-ratio}
Dengan `Kustom`, atur lebar dan tinggi gambar. Tombol tautan di antara kedua penggeser menjaga rasionya saat Anda mengubah salah satunya. Dengan `Persegi`, hanya lebarnya yang bisa diatur.

### ![](/icons/export.webp) Ekspor → PNG {#export-png}
Klik tombol ini untuk memulai proses render. Setelah selesai, Anda bisa memilih cara menyimpan atau membagikan gambarnya. Ukuran yang sangat besar akan meminta konfirmasi terlebih dahulu: simpan proyek Anda sebelumnya, untuk berjaga-jaga jika memori perangkat Anda habis.

## ![](/icons/network.webp) Tautan {#link}

Menghubungkan Nomad dengan perangkat atau aplikasi lain, untuk mengirim dan menerima objek, atau menyinkronkan suntingan Anda secara langsung. Satu perangkat menjadi host sesi, perangkat lainnya bergabung.

### Aktifkan GoZ {#enable-goz}
Khusus desktop. Bertukar mesh dengan ZBrush di komputer ini. `Kirim` mengimpornya ke ZBrush, `Ambil` mengimpor dari ZBrush yang sedang berjalan: `Seleksi` mengambil subtool aktif, `Adegan` mengambil semua subtool. Anda juga bisa menekan GoZ di ZBrush kapan saja.

### Mode {#link-mode}
* `Nonaktif` - Tidak ada tautan.
* `Host` - Perangkat ini menjadi host sesi dan menunggu perangkat lain bergabung.
* `Gabung` - Mencari perangkat di sekitar, lalu ketuk nama host untuk bergabung.

Untuk menghubungkan dua Nomad, pilih `Host` di satu perangkat dan `Gabung` di perangkat lainnya. Untuk terhubung dengan Blender, Nomad harus menjadi host: tombol bantuan di sebelah judul `Tautan` menunjukkan cara memasang ekstensi Nomad Blender Link.

### ![](/icons/network.webp) Port jaringan {#network-port}
Port jaringan yang dipakai oleh tautan. Ubah hanya jika aplikasi lain sudah memakainya.

### Kirim / Ambil {#send-get}
Setelah terhubung, `Kirim` `Seleksi` Anda atau seluruh `Adegan` ke perangkat lain, atau `Ambil` dari perangkat tersebut. `Ganti` menghapus adegan saat ini, lalu mengambil adegan dari perangkat lain.

### ![](/icons/link.webp) Sinkronisasi langsung {#live-sync}
Mengalirkan suntingan Anda ke perangkat lain sambil Anda bekerja. `Tampilan kerja` juga menyinkronkan kamera. `Edit adegan` menentukan perangkat mana yang mengirim suntingan: `Otomatis` memberi arah ke aktivitas terbaru. Lalu pilih apa yang disinkronkan: `Objek & geometri`, `Material`, `Lampu`, `Kamera`, dan jika sisi lainnya mendukung, `Shading` dan `PascaProses`.

::: tip
Objek yang sudah ada perlu satu kali `Kirim` atau `Ambil` terlebih dahulu, untuk menautkannya sebelum sinkronisasi langsung bisa memperbaruinya.
:::
