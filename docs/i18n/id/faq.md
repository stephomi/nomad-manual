# ![](/icons/faq.webp) FAQ {#faq}

[[toc]]

## Platform {#platform}
### Di mana letak proyek saya di perangkat? {#locate}
Proyek berada di folder `projects` di dalam folder utama Nomad.

Di iOS, Anda bisa mengakses folder Nomad dengan aplikasi Files di iOS.

Di Android, folder Nomad berada di `Android/data/com.stephaneginier.nomad/files/`.  
Di versi Android terbaru (10/11), Anda tidak lagi punya akses ke folder `Android/data`.
Anda bisa mengaksesnya lewat aplikasi terpisah, misalnya [yang ini](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer).
<!-- [this one](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager) -->
<!-- [this one](https://play.google.com/store/apps/details?id=com.mi.android.globalFileexplorer) -->

### Apakah ada cara untuk ikut uji beta? {#beta}
Untuk Windows & MacOS, versi beta mungkin tersedia di [Beranda](https://nomadsculpt.com).
<br>
Untuk iOS ada TestFlight privat, kunjungi [Discord](https://discord.com/invite/8h7BwpRz29) di kanal #beta-ios.
<br>
[Demo Web](https://nomadsculpt.com/demo) biasanya diperbarui dengan fitur-fitur terbaru.

### Kenapa ada uji coba gratis di Android, tapi tidak di iOS? {#android-trial}
Karena perangkat Android lama itu payah (dan beberapa yang baru juga...), dan saya tidak ingin orang membeli aplikasinya lalu disambut layar hitam.
Tapi alasan utamanya adalah saya merasa aplikasi Android berbayar bukanlah hal yang lazim.

### Tablet apa yang terbaik untuk menjalankan Nomad? {#best-tablet}

Singkatnya: iPad.

Jawaban yang sedikit lebih panjang adalah 

> "iPad terbaru yang _sanggup Anda beli_, kecuali Anda benar-benar membenci Apple, dalam hal ini tablet Samsung terbaru yang sanggup Anda beli. Selain itu, uji dulu." 

Orang selalu ingin informasi lebih, jadi berikut ringkasannya.

Nomad berjalan paling baik di iPad yang lebih baru:

* iPad dan iPhone bisa mengakses plugin [Quad Remesher](tools#quad-remesher) dari [Exoside](https://exoside.com/)
* iPad terbaru dengan pencil terbaru mendukung [barrel roll](https://www.youtube.com/watch?v=XcDQazDYpo0), jadi Anda bisa memutar pencil di alat-alat tertentu di Nomad. 
* kinerja chip seri M terbaru sangat cepat. 

iPad terbaru dan termahal yang tersedia akan bisa merender gambar akhir dengan sangat cepat, dan memungkinkan Anda memahat banyak detail.

Namun, penurunan kinerja pada iPad yang lebih murah dan lebih lama tidak separah yang orang kira. iPad apa pun yang mendukung Apple Pencil menjalankan Nomad dengan cukup baik. Misalnya:

* iPad Pro tahun 2023 bisa menangani pahatan 5 juta poligon dengan tetap responsif, dan gambar berkualitas akhir bisa dirender dalam 5 detik.
* iPad Pro tahun 2015 bisa menangani objek 1,2 juta poligon dengan sedikit lag, dan gambar berkualitas akhir bisa dirender dalam 20 detik.

Itu perbedaan kinerja yang besar, tetapi Anda juga harus memperhitungkan harganya:

* iPad Pro 2025 harganya *$2500 USD* baru dengan semua opsi. 
* iPad Pro 2023 saat ini harganya *$400 USD* di eBay.
* iPad Pro 2015 harganya *$250 USD* di eBay.

Apakah tambahan 4 juta poligon dan hemat 15 detik sepadan dengan $2100? Itu terserah Anda.

Model non-Pro bisa lebih murah lagi dan menawarkan beragam pilihan ukuran dan kinerja. iPad Air saat ini mendukung pencil generasi 2 dengan barrel roll, dan jauh lebih murah daripada Pro. Pasar barang bekas dan rekondisi punya lebih banyak pilihan lagi. 

Artinya, berapa pun anggaran Anda, Anda seharusnya bisa menemukan iPad yang cocok. Dan ingat, kebanyakan pahatan tidak sampai jutaan poligon! Jika Anda bisa tetap di bawah 500.000 poligon, iPad lama pun bisa dipakai memahat dengan cepat.

`Bagaimana dengan Android?`

Kinerja grafis Android berada di bawah iPad. Menurut pengembang Nomad, "Samsung Galaxy Tab S9 menjalankan Nomad sepuluh kali lebih lambat daripada iPad Air". Meski begitu, banyak pengguna yang sangat puas dengan tablet Samsung mereka, dan Nomad berjalan dengan baik untuk sebagian besar sculpting. 

Untuk tablet Android lainnya, berhati-hatilah. Kinerja perangkat keras Android bisa sangat bervariasi, jadi sulit memperkirakan bagaimana Nomad akan berjalan.

Silakan uji dulu dengan versi gratis Nomad yang fitur simpannya dinonaktifkan. 

`Bagaimana dengan memori dan penyimpanan?`

Kebanyakan file Nomad berukuran 100mb atau kurang. Artinya, hampir semua tablet yang Anda beli saat ini, iPad maupun Android, akan punya ruang yang lebih dari cukup untuk proyek-proyek Nomad Anda.


### Saya membeli Nomad untuk satu perangkat, apakah bisa saya pakai di perangkat lain? {#multi-devices}
Selama memakai toko aplikasi yang sama dan akun yang sama, bisa.

Misalnya, jika Anda membelinya di App Store iOS, Anda bisa memakainya di perangkat iOS Anda yang lain.

Jika Anda membelinya untuk tablet Android Anda di Google Play, Anda bisa memakainya di perangkat Android Anda yang lain.

Namun, jika Anda membeli Nomad di Android, lalu Anda punya iPad, Anda harus membelinya lagi.

Ini karena Nomad tidak punya server lisensi atau model langganan sendiri. Tidak ada kesepakatan antara Apple/Google/AppGallery untuk berbagi lisensi. 


### Bagaimana cara memulihkan pembelian saya? {#restore}
Google Play dan AppGallery sama-sama menangani sinkronisasi secara otomatis.

- Buka menu Tentang (ikon Nomad di kiri atas), lalu tekan `Pulihkan pembelian`
- Pastikan Anda masuk ke akun yang sama dengan yang Anda pakai untuk membeli Nomad (di Google Play).
- Mulai ulang perangkat
- Terkadang Anda perlu menunggu beberapa jam
- Pastikan aplikasi Google Play sudah versi terbaru
- Instal ulang Nomad (pastikan untuk [mencadangkan file Anda](#locate) jika tidak ingin kehilangan apa pun)
- Anda bisa mencoba membeli lagi untuk melihat apa yang terjadi (catatan: Anda tidak bisa membeli item yang sama dua kali dengan akun yang sama)

:::tip
Anda bisa menghubungi saya di <support@nomadsculpt.com>, tetapi *satu-satunya* hal yang bisa saya lakukan adalah memastikan apakah sebuah email memiliki pembelian yang terkait dengannya.

Perlu diketahui, saya rutin menerima laporan tentang lisensi yang tidak diperbarui dengan benar setelah membeli perangkat baru.
Saya tidak punya kendali apa pun atas pembayaran dan sinkronisasi akun, semuanya ditangani oleh Google/AppGallery!

Pada akhirnya pembelian selalu berhasil dipulihkan, tetapi langkah yang diperlukan untuk mempercepat prosesnya belum jelas.
:::

::: warning
Perangkat Huawei terbaru tidak punya akses ke layanan Google.
Dalam hal ini, Anda perlu membeli aplikasinya lagi di AppGallery (toko aplikasi Huawei).
:::

### Bisakah Anda menerjemahkan atau memperbaiki [bahasa-saya]? {#locale}
Saya bisa menambahkan bahasa lain dengan relatif mudah, tetapi saya mengandalkan terjemahan AI karena jauh lebih mudah dikelola untuk pembaruan rutin.
File terjemahannya bisa ditemukan [di sini](https://github.com/stephomi/nomad-translation).

## Fitur {#features}

### Kenapa gizmo tidak bergerak? {#gizmo-not-moving}
Mungkin Anda mengaktifkan [pin di bilah alat menu kiri](tools#left-menu-toolbar). 

### Bisakah kita membuat animasi di dalam Nomad? {#animate}
Untuk saat ini belum. Fitur linimasa yang bisa menganimasikan lapisan mungkin menarik, tetapi saat ini belum benar-benar direncanakan.  

Saya ingin mendukung rigging/skinning di masa depan, tetapi ini punya beberapa tantangan (terutama interaksinya dengan alat sculpting...) jadi belum ada yang pasti untuk saat ini.


### Bisakah kita melakukan pemodelan low-poly yang sesungguhnya? {#lowpoly}
Untuk saat ini belum.
Ini sebenarnya bukan cakupan Nomad *Sculpt*, tetapi mungkin saya akan menyediakan beberapa alat di masa depan.


### Bisakah kita membuat uv dan tekstur? {#texturing}
Jawaban singkat: Ya. Jawaban panjang: Tidak secara langsung, tetapi ada beberapa cara untuk memadukan alat vertex paint Nomad yang luar biasa dengan uv dan tekstur.

* Nomad memungkinkan Anda mengecat warna, roughness, dan properti material langsung ke verteks pahatan Anda.
* Nomad memungkinkan jumlah verteks yang sangat tinggi, sehingga Anda bisa mengecat tanpa perlu memikirkan uv.
* Nomad bisa memuat tekstur untuk dipakai di kuas, sehingga Anda bisa mengecap dan mengecat dengan tekstur.
* Nomad bisa memuat objek yang sudah memiliki tekstur, untuk keperluan render.
* Nomad bisa melakukan [UV unwrap](topology.md#uv-unwrap-uvatlas) pada objek berpoligon rendah.
* Warna/roughness/metalness bisa ditransfer dari tekstur ke verteks lewat [opsi proyeksi](topology.md#reproject-to-vertex).
* Warna/roughness/metalness/normal bisa di-bake dari verteks ke tekstur lewat [opsi bake](topology.md#bake-texture)
* Bake dan proyeksi bisa dilakukan antara satu objek atau banyak objek, atau antara tingkat subdivisi tertinggi dan terendah dari satu objek, sehingga memungkinkan beragam alur kerja bake dan proyeksi.
* Setelah bake, mengekspor obj juga akan mengekspor teksturnya, yang bisa dibawa ke aplikasi seperti Procreate untuk dicat langsung di teksturnya.

### Bisakah saya merekam video turntable? {#video}
Belum direncanakan untuk saat ini; iOS punya [fitur perekaman video](https://support.apple.com/en-au/guide/ipad/ipaddf78ce08/ipados) yang sangat mudah dipakai.

Di iOS, caranya dengan menggeser ke bawah dari kiri atas, lalu mengetuk tombol rekam. Anda akan mendapat hitung mundur 3 detik; geser menu menjauh untuk menampilkan Nomad, lalu gunakan fitur turntable. Setelah selesai, geser ke bawah lagi dari kanan atas, lalu ketuk tombol rekam lagi. Sunting videonya dari galeri foto untuk membuang rekaman berlebih di awal dan akhir video.

### Bisakah Anda menambahkan [fitur-favorit] sebagai tombol di tingkat atas? {#interface}
Ya, bilah alat bawah sekarang bisa disesuaikan dari menu [Antarmuka](interface.md#shortcuts), dan bilah alat mengambang sekarang bisa dibuat.

### Apa fitur-fitur berikutnya? {#next-features}
Untuk peta jalan jangka menengah/panjang saya punya banyak ide, tetapi belum tahu pasti.  

Perbaikan bug dan peningkatan fitur yang sudah ada akan selalu lebih diprioritaskan daripada menambahkan fitur baru.


### Bisakah kita melakukan rigging di Nomad? {#rigging}
Belum, tetapi sudah direncanakan. Untuk saat ini Anda bisa menautkan bentuk-bentuk sebagai induk-anak dan mengubah titik poros, sehingga bisa membuat pahatan sederhana yang bisa diatur posenya.

### Bisakah kita memakai lebih dari 4 cahaya? {#lights}
Anda bisa memakai hingga 4 cahaya di perangkat seluler, dan hingga 6 di desktop. Ini adalah keterbatasan mesin render real-time di dalam Nomad. Anda bisa menirunya dengan objek emisif dan pencahayaan global di pascaproses, seperti yang ditunjukkan di [tutorial ini](https://www.youtube.com/watch?v=QhrUGH7CuUA)

### Bisakah kita mengimpor alat Zbrush? {#zbrush-import}
Tidak, Zbrush memakai format proprietary. Anda seharusnya bisa mengekstrak peta alpha-nya dan memakainya di Nomad. 

### Kenapa warnanya tidak sesuai dengan yang saya cat? Kenapa saya tidak bisa mendapatkan warna putih di render? {#paint-pbr}
Bayangkan memotret selembar kertas, dibandingkan memotret lampu meja, dibandingkan memotret matahari. Kamera dan layar lama akan membuat semuanya sama-sama 'putih'. Sistem yang lebih modern bisa menunjukkan perbedaan antara putih yang dipantulkan kertas, cahaya yang dipancarkan lampu, dan terangnya matahari yang luar biasa.

Grafis komputer modern mencoba bekerja dengan cara serupa, meniru fisika cahaya dan permukaan. Ini disebut `Physically Based Rendering`, atau PBR, dan renderer PBR Nomad didasarkan pada hal ini. Hasilnya tampak realistis dan seimbang, tetapi warna cat yang cerah sering kali tampak lebih gelap.

Jika Anda ingin render lebih mendekati warna yang dicat, Anda bisa mengatasinya dengan cara yang tidak berbasis fisika maupun yang berbasis fisika:

Non PBR:
* `Gunakan mode 'Tanpa pencahayaan' di menu Shading`. Warna akan ditampilkan persis seperti yang dicat, tetapi Anda juga kehilangan semua shading. Praktis untuk pengecekan cepat, dan untuk hasil yang lebih grafis.
* `Gunakan mode 'MatCap' di menu Shading`. Pilih matcap yang lebih terang, sebagian besar putih, tanpa sentuhan warna.

PBR:
* `Gunakan lingkungan yang netral`. Anda bisa [mengganti lingkungan](shading.md#environment) dengan yang lebih netral. Hindari lingkungan dalam ruangan karena cenderung lebih berwarna. Lebih baik pilih lingkungan luar ruangan di siang hari atau lingkungan studio.
* `Perkuat pencahayaan`. Jika Anda memotret kertas putih di ruangan gelap, Anda cukup menambah cahaya. Pada cahaya lingkungan, naikkan penggeser eksposur sampai warnanya terasa pas bagi Anda, atau tambahkan lebih banyak cahaya individual dengan intensitas lebih tinggi.
* `Perkuat eksposur kamera`. Jika ruangan gelap itu tidak punya cahaya tambahan, Anda bisa membuat kamera membuka rana lebih lama, atau memakai ISO yang lebih sensitif. Di Nomad, Anda bisa mendapatkan hasil serupa dengan pascaproses. Buka PascaProses, aktifkan, turun ke Pemetaan Nada, aktifkan, lalu naikkan penggeser eksposur sampai warnanya terasa pas.
* `Gunakan warna emisif`. Di menu Material, Anda bisa mengaktifkan 'Emisif' di bagian tekstur, yang akan membuat objek tampak seperti sumber cahaya. Jika Anda menyalakan pencahayaan global di pengaturan PascaProses, objek itu akan memancarkan cahaya ke objek lain di adegan. Anda juga bisa mengaktifkan 'Selalu tidak berlampu' untuk material itu, yang akan memberi tampilan serupa tanpa tekstur.

## Crash {#crashes}

### Aplikasi crash saat saya menyimpan atau melakukan remesh pada model! {#crash-remesh}
Memori (RAM) perangkat Anda habis.  
Untuk mengurangi penggunaan memori di adegan Anda, Anda bisa memakai beberapa opsi [Topologi](topology.md) untuk mengurangi jumlah poligon.

::: tip RAM/Penyimpanan
Yang penting adalah jumlah RAM, bukan penyimpanan (yang biasanya jauh lebih besar).
:::


### Aplikasi crash saat saya memuat proyek! {#crash-load}
Jika filenya kecil, Anda bisa mengirimkannya kepada saya dan saya akan memeriksanya (lewat email <support@nomadsculpt.com>).

Jika tidak, kemungkinan besar memori RAM perangkat Anda habis.

- Pastikan Anda menutup semua aplikasi lain yang terbuka di perangkat Anda.
- Mulai proyek baru di Nomad, alih-alih membiarkan sebuah proyek sedang terbuka.
- Jika masih crash, satu-satunya solusi adalah memuat [file proyek Anda](#locate) di perangkat dengan memori lebih besar.

::: tip
Jika perangkat seluler Anda tidak bisa memuat proyeknya, coba [versi desktop](https://nomadsculpt.com). Anda bisa memakainya secara gratis dalam mode Demo untuk mengimpor dan mengekspor proyek, meskipun hanya beberapa alat penyuntingan yang tersedia.

Jika proyek Anda memakai [Lapisan](layers.md), Anda mungkin ingin menggabungkannya untuk mengurangi penggunaan memori.
:::

### Aplikasi crash saat saya menjalankan Nomad! {#crash-start}
Jika crash saat memuat, artinya Nomad kesulitan dengan file tertentu yang ada di folder Nomad.

Sebagian besar kasus terjadi karena proyeknya berat dan sayangnya melebihi batas RAM.

Temukan [folder Nomad](#locate), lalu ganti nama atau pindahkan beberapa file untuk menemukan penyebabnya.

Pertama, coba ganti nama `settings.json`. Dengan begitu, Nomad berhenti memuat proyek terakhir.

Jika tidak berhasil, coba pindahkan beberapa file terbaru keluar dari folder sumber dayanya masing-masing (`projects`, `matcaps`, `environments`, dll.).

Anda juga bisa mengganti nama foldernya sendiri agar Nomad sepenuhnya mengabaikannya.
Jika Anda mengganti nama atau memindahkan semua file di folder Nomad, hasilnya akan sama seperti instalasi bersih.

::: tip
Saat Nomad memuat file ketika dijalankan, Nomad selalu memindahkan file itu ke folder `can_be_deleted/`.
Jika operasinya berhasil, file itu dipindahkan kembali ke folder aslinya.

Jika crash sebelum pemuatan selesai, Nomad akan berhasil dijalankan pada percobaan berikutnya, karena Nomad mengabaikan folder `can_be_deleted/`.

Anda bisa mencoba memuat file ini lagi jika menurut Anda bisa berhasil.
:::
