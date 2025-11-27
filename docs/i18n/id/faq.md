# ![](/icons/faq.webp) FAQ

[[toc]]

## Platform 
### Di mana proyek saya berada di perangkat?
Proyek berada di folder `projects` di dalam folder utama Nomad.

Di iOS, Anda dapat mengakses folder Nomad dengan aplikasi Files iOS.

Di Android, folder Nomad berada di `Android/data/com.stephaneginier.nomad/files/`.  
Pada Android versi terbaru (10/11), Anda tidak lagi memiliki akses ke folder `Android/data`.
Anda dapat mengaksesnya melalui aplikasi terpisah, misalnya [yang ini](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Apakah ada cara untuk ikut beta test?
Untuk Windows & MacOS, versi beta mungkin tersedia di [Homepage](https://nomadsculpt.com).
<br>
Untuk iOS ada TestFlight privat, kunjungi [Discord](https://discord.com/invite/8h7BwpRz29) di kanal #beta-ios.
<br>
[Web Demo](https://nomadsculpt.com/demo) biasanya diperbarui dengan fitur-fitur terbaru.

### Kenapa ada uji coba gratis di Android? Tapi tidak di iOS?
Karena perangkat Android lama jelek (dan beberapa yang baru juga...), dan saya tidak ingin orang membeli aplikasi lalu disambut dengan layar hitam.
Tapi alasan utamanya adalah saya merasa aplikasi berbayar di Android bukanlah hal yang umum.

### Tablet apa yang paling baik untuk menjalankan Nomad?

Singkatnya: iPad.

Jawaban yang sedikit lebih panjang adalah 

> "iPad terbaru _yang bisa Anda beli_, kecuali Anda benar-benar benci Apple, dalam hal ini tablet Samsung terbaru yang bisa Anda beli. Selain itu, tes dulu." 

Orang selalu ingin lebih banyak informasi, jadi berikut ringkasannya.

Nomad berjalan paling baik di iPad yang lebih baru:

* iPad dan iPhone dapat mengakses plugin [Quad Remesher](tools#quad-remesher) dari [Exoside](https://exoside.com/)
* iPad terbaru dengan pencil terbaru mendukung [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), Anda bisa memutar pencil pada alat tertentu di Nomad. 
* performa chip seri M terbaru sangat cepat. 

iPad terbaru dan termahal yang tersedia akan dapat merender gambar final dengan sangat cepat, dan memungkinkan Anda memahat dengan banyak detail.

Namun, penurunan performa pada iPad yang lebih murah dan lebih tua tidak separah yang orang kira. iPad apa pun yang mendukung Apple Pencil menjalankan Nomad dengan cukup baik. Misalnya:

* iPad Pro tahun 2023 dapat menangani sculpt 5 juta poly dan tetap responsif, gambar kualitas final dapat dirender dalam 5 detik.
* iPad Pro tahun 2015 dapat menangani objek 1,2 juta poly dengan sedikit lag, gambar kualitas final dapat dirender dalam 20 detik.

Itu perbedaan performa yang besar, tetapi Anda juga harus mempertimbangkan harganya:

* iPad Pro 2025 *$2500 USD* baru dengan semua opsi. 
* iPad Pro 2023 saat ini seharga *$400 USD* di eBay.
* iPad Pro 2015 seharga *$250 USD* di eBay.

Apakah tambahan 4 juta poly dan penghematan 15 detik sebanding dengan $2100? Itu terserah Anda.

Model non Pro bisa lebih murah lagi dan memberi berbagai pilihan ukuran dan performa. iPad Air saat ini mendukung pencil gen 2 dengan barrel roll, dan jauh lebih murah daripada Pro. Pasar second dan refurbished punya lebih banyak pilihan lagi. 

Ini berarti berapa pun anggaran Anda, Anda seharusnya bisa menemukan iPad yang cocok. Dan ingat bahwa sebagian besar sculpt bukan jutaan poly! Jika Anda bisa tetap di bawah 500.000 poly, bahkan iPad lama pun akan memungkinkan Anda memahat dengan cepat.

`Bagaimana dengan Android?`

Performa grafis Android berada di bawah iPad. Menurut pengembang Nomad, "Samsung Galaxy Tab S9 akan menjalankan Nomad satu ordo magnitudo lebih lambat daripada iPad Air". Meski begitu banyak pengguna sangat puas dengan tablet Samsung mereka, Nomad berjalan baik untuk sebagian besar pemahatan. 

Untuk tablet Android lainnya, berhati-hatilah. Performa hardware Android bisa sangat bervariasi, tidak mudah memprediksi bagaimana Nomad akan berjalan.

Silakan gunakan versi gratis Nomad yang tidak bisa menyimpan untuk menguji terlebih dahulu. 

`Bagaimana dengan memori dan penyimpanan?`

Sebagian besar file Nomad cenderung berukuran 100mb atau kurang. Ini berarti hampir semua tablet yang Anda beli saat ini, iPad atau Android, akan memiliki banyak ruang untuk proyek Nomad Anda.


### Saya membeli Nomad untuk satu perangkat, bisakah saya menggunakannya di perangkat lain?
Selama menggunakan toko aplikasi dan akun yang sama, bisa.

Misalnya jika Anda membelinya di App Store iOS, Anda dapat menggunakannya di perangkat iOS lain Anda.

Jika Anda membelinya untuk tablet Android di Google Play, Anda dapat menggunakannya di perangkat Android lain Anda.

Namun jika Anda membeli Nomad di Android, lalu Anda membeli iPad, Anda harus membelinya lagi.

Ini karena Nomad tidak memiliki server lisensi sendiri atau model langganan. Tidak ada perjanjian antara Apple/Google/AppGallery untuk menangani berbagi lisensi. 


### Bagaimana cara memulihkan pembelian saya?
Google Play dan AppGallery menangani sinkronisasi secara otomatis.

- Masuk ke menu About (ikon nomad kiri atas), lalu tekan `restore purchase`
- Pastikan Anda masuk dengan akun yang sama yang digunakan untuk membeli Nomad (di Google Play).
- Reboot perangkat
- Terkadang Anda perlu menunggu beberapa jam
- Pastikan aplikasi Google Play sudah versi terbaru
- Instal ulang Nomad (pastikan untuk [mencadangkan file Anda](#where-are-my-projects-located-on-my-device) jika Anda tidak ingin kehilangan apa pun)
- Anda bisa mencoba membeli lagi untuk melihat apa yang terjadi (catatan: Anda tidak bisa membeli item yang sama dua kali di akun yang sama)

:::tip
Anda dapat menghubungi saya di <support@nomadsculpt.com> tetapi *satu-satunya* hal yang bisa saya lakukan adalah mengonfirmasi apakah sebuah email memiliki pembelian yang terkait dengannya.

Perlu dicatat bahwa saya secara teratur menerima laporan tentang lisensi yang tidak diperbarui dengan benar setelah mendapatkan perangkat baru.
Saya tidak punya kendali atas pembayaran dan sinkronisasi akun, semuanya ditangani oleh Google/AppGallery!

Akhirnya pembelian selalu bisa dipulihkan, tetapi langkah-langkah yang diperlukan untuk mempercepat prosesnya tidak jelas.
:::

::: warning
Perangkat Huawei terbaru tidak memiliki akses ke layanan Google.
Dalam kasus itu Anda perlu membeli aplikasinya lagi di AppGallery (toko aplikasi Huawei).
:::

### Bisakah Anda menerjemahkan atau memperbaiki [bahasa-saya]?
Saya relatif mudah menambahkan bahasa lain, tetapi saya mengandalkan terjemahan AI karena jauh lebih mudah ditangani untuk pembaruan rutin.
File terjemahan dapat ditemukan [di sini](https://github.com/stephomi/nomad-translation).

## Fitur

### Kenapa gizmo tidak bergerak?
Anda mungkin mengaktifkan [pin di toolbar menu kiri](tools#left-menu-toolbar). 

### Bisakah kita menganimasikan di dalam Nomad?
Belum untuk sekarang. Fitur timeline yang bisa menganimasikan layer mungkin menarik, tetapi belum benar-benar direncanakan saat ini.  

Saya ingin mendukung rigging/skinning di masa depan, tetapi ini menimbulkan beberapa tantangan (terutama interaksi dengan alat sculpting...) jadi belum ada kepastian untuk sekarang.


### Bisakah kita melakukan pemodelan low-poly yang benar?
Belum untuk sekarang.
Ini bukan benar-benar cakupan Nomad *Sculpt*, tetapi mungkin saya akan menyediakan beberapa alat di masa depan.


### Bisakah kita melakukan uv dan texturing?
Jawaban singkat: Ya. Jawaban panjang: Tidak secara langsung, tetapi ada beberapa cara untuk menggabungkan alat vertex paint Nomad yang sangat baik dengan uv dan tekstur.

* Nomad memungkinkan Anda mengecat warna, roughness, properti material langsung ke vertex sculpt Anda.
* Nomad memungkinkan jumlah vertex yang sangat tinggi sehingga Anda dapat mengecat tanpa memikirkan uv.
* Nomad dapat memuat tekstur untuk digunakan di kuas, memungkinkan stamping dan pengecatan dengan tekstur.
* Nomad dapat memuat objek yang sudah memiliki tekstur yang ditetapkan, untuk keperluan rendering.
* Nomad dapat melakukan [UV unwrap](topology.md#uv-unwrap) pada objek low poly.
* Warna/roughness/metalness dapat ditransfer dari tekstur ke vertex melalui [opsi project](topology.md#reproject-to-vertex).
* Warna/roughness/metalness/normal dapat dibake dari vertex ke tekstur melalui [opsi baking](topology.md#bake-to-texture)
* Baking dan projecting dapat ditangani antara objek tunggal atau banyak objek, atau antara level subdivisi tertinggi dan terendah dari satu objek, memungkinkan berbagai workflow bake dan project.
* Setelah baking, mengekspor obj juga akan mengekspor tekstur, yang dapat dibawa ke aplikasi seperti Procreate untuk mengecat langsung pada tekstur.

### Bisakah saya merekam video turntable?
Belum direncanakan untuk sekarang, iOS memiliki [fitur perekaman video](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) yang sangat mudah digunakan.

Di iOS, ini dilakukan dengan menggeser ke bawah dari kiri atas, dan mengetuk tombol rekam. Akan ada hitung mundur 3 detik, geser menu untuk menampilkan Nomad, dan gunakan fitur turntable. Setelah selesai, geser lagi dari kanan atas, dan ketuk tombol rekam lagi. Edit video dari photo library untuk menghapus bagian berlebih di awal dan akhir video.

### Bisakah Anda menambahkan [fitur-favorit-saya] sebagai tombol level atas?
Bisa, toolbar bawah sekarang dapat dikustomisasi dari menu [interface](interface.md), dan toolbar mengambang sekarang dapat dibuat.

### Fitur apa berikutnya?
Untuk roadmap jangka menengah/panjang saya punya banyak ide tetapi belum tahu pasti.  

Perbaikan bug dan peningkatan fitur yang ada akan selalu memiliki prioritas lebih tinggi daripada menambah fitur baru.


### Bisakah kita rig di Nomad?
Tidak, tetapi ini direncanakan. Untuk sekarang Anda bisa mem-parent bentuk satu sama lain dan mengubah titik pivot, memungkinkan sculpt sederhana yang bisa diposisikan.

### Bisakah kita menggunakan lebih dari 4 lampu?
Tidak, ini adalah batasan dari mesin render realtime di dalam Nomad. Ini bisa diakali dengan menggunakan objek emissive dan global illumination di post process, seperti yang ditunjukkan di [tutorial ini](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Bisakah kita mengimpor Zbrush tools?
Tidak, Zbrush menggunakan format proprietari. Anda seharusnya bisa mengekstrak alpha map dan menggunakannya di Nomad. 

### Kenapa warna tidak cocok dengan yang saya cat? Kenapa saya tidak bisa mendapatkan warna putih di render?
Bayangkan memotret selembar kertas, vs foto lampu meja, vs foto matahari. Kamera dan layar lama hanya akan membuat semuanya ‘putih’. Sistem yang lebih modern dapat menunjukkan perbedaan antara putih pantulan kertas vs cahaya yang dipancarkan lampu, vs super terang matahari.

Grafis komputer modern mencoba bekerja dengan cara yang mirip, meniru fisika cahaya dan permukaan. Ini disebut `Physically Based Rendering`, atau PBR, dan renderer PBR Nomad didasarkan pada ini. Ini terlihat realistis dan seimbang, tetapi sering kali warna yang dicat terang akan tampak lebih gelap.

Jika Anda perlu agar render lebih mendekati warna yang dicat, Anda bisa memperbaikinya dengan cara non-physically based dan physically based:

Non PBR:
* `Gunakan mode 'Unlit' di menu lighting`. Warna akan ditampilkan persis seperti yang dicat, tetapi Anda juga kehilangan semua shading. Berguna untuk pengecekan cepat, dan output yang lebih grafis.
* `Gunakan mode 'Matcap' di menu lighting`. Pilih matcap yang lebih terang yang sebagian besar putih, tanpa tint warna.

PBR:
* `Gunakan environment netral`. Anda bisa [mengganti environment](shading.md#environment) ke yang lebih netral. Hindari environment indoor karena cenderung lebih berwarna. Lebih pilih environment luar ruangan siang hari atau studio.
* `Tingkatkan pencahayaan`. Jika Anda memotret kertas putih di ruangan gelap, Anda cukup menambah cahaya. Pada environment light, naikkan slider exposure sampai warna mulai terasa pas bagi Anda, atau tambahkan lebih banyak lampu individual dengan intensitas lebih tinggi.
* `Tingkatkan exposure kamera`. Jika ruangan gelap tidak punya lampu tambahan, Anda bisa membuat kamera menahan shutter lebih lama, atau menggunakan ISO yang lebih sensitif. Di Nomad Anda bisa mencapai hasil serupa dengan post processing. Masuk ke post process, aktifkan, turun ke tone mapping, aktifkan, dan naikkan slider exposure sampai warna terasa pas.
* `Gunakan emissive color`. Di menu material, Anda bisa mengaktifkan 'emissive' di bawah textures, yang akan membuat objek tampak seperti sumber cahaya. Jika Anda menyalakan global illumination di pengaturan post process, ini akan memancarkan cahaya ke objek lain di scene. Anda juga bisa mengaktifkan 'unlit' untuk material tersebut, yang akan menghasilkan tampilan serupa tanpa tekstur.

## Crash

### Aplikasi crash saat saya menyimpan atau remesh model!
Perangkat Anda kehabisan memori (RAM).  
Untuk mengurangi penggunaan memori di scene Anda, Anda bisa menggunakan beberapa opsi [Topology](topology.md) untuk mengurangi jumlah poligon.

::: tip RAM/Penyimpanan
Yang penting adalah jumlah RAM, bukan penyimpanan (yang biasanya jauh lebih besar).
:::


### Aplikasi crash saat saya memuat proyek!
Jika filenya kecil, Anda bisa mengirimkannya ke saya dan saya akan melihatnya (via email <support@nomadsculpt.com>).

Jika tidak, perangkat mungkin kehabisan memori RAM.

- Pastikan Anda menutup aplikasi lain yang terbuka di perangkat Anda.
- Mulai proyek baru di Nomad alih-alih memiliki proyek yang sedang terbuka.
- Jika masih crash, satu-satunya solusi adalah memuat [file proyek Anda](#where-are-my-projects-located-on-my-device) di perangkat dengan memori lebih besar.

::: tip
Di browser desktop, Anda bisa mencoba memuat file Anda [di url ini](https://nomadsculpt.com/demo_save/) lalu mengekspornya kembali setelah menyederhanakan scene Anda.

Beberapa browser membatasi jumlah RAM yang bisa digunakan satu tab, jadi mungkin teknik ini tidak akan berhasil.

Jika proyek Anda menggunakan [Layers](layers.md), Anda mungkin ingin men-squash-nya untuk mengurangi penggunaan memori.
:::

<!-- ::: tip
Additionally, for legacy glb.lz4 file format, you can try the following:

1. If your project is using [Layers](layers.md), enable the `Merge layers` option before loading the project.
The option can be found in the `Files -> Settings` sub menu.
Layers can take a lot of memory, merging them at loading can help reduce the memory peak usage.

2. Decompress your [project](#where-are-my-projects-located-on-my-device) (`.glb.lz4` to `.glb`).
On windows, you need to download [LZ4](https://github.com/lz4/lz4/releases).
On MacOS, you can use the command line.
With homebrew, simply do `brew install lz4` and then `lz4 myproject.glb.lz4`.

3. Try to load the `.glb` file directly into Nomad again.

4. If it still crashes at loading, you can open the file on any 3d desktop software that supports `glTF`.
::: -->

### Aplikasi crash saat saya memulai Nomad!
Jika crash saat loading, berarti Nomad bermasalah dengan file tertentu yang ada di folder Nomad.

Sebagian besar waktu, ini terjadi karena proyeknya berat dan sayangnya akan melebihi batas RAM.

Temukan [folder Nomad](#where-are-my-projects-located-on-my-device), lalu ganti nama atau pindahkan beberapa file untuk menemukan penyebabnya.

Pertama, coba ganti nama `settings.json`. Dengan begitu Nomad akan berhenti memuat proyek terakhir.

Jika tidak berhasil, coba pindahkan beberapa file terbaru ke luar folder resource masing-masing (`projects`, `matcaps`, `environments`, dll).

Anda juga bisa mengganti nama folder itu sendiri sehingga Nomad benar-benar mengabaikannya.
Jika Anda mengganti nama atau memindahkan semua file di folder Nomad, ini akan memberikan hasil yang sama seperti instalasi bersih.

::: tip
Saat Nomad memuat file saat startup, ia selalu memindahkan file ke folder `can_be_deleted/`.
Jika operasi berhasil, maka file dipindahkan kembali ke folder aslinya.

Jika crash sebelum loading selesai, maka Nomad akan berjalan dengan sukses pada start berikutnya, karena mengabaikan folder `can_be_deleted/`.

Anda bisa mencoba memuat file ini lagi jika Anda pikir bisa berhasil.
:::
