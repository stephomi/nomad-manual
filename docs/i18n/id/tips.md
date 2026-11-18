# ![](/icons/manual.webp) Tips {#tips}

[[toc]]

## Cara memulai sebuah model {#how-to-start-a-model}

Pemula di dunia sculpting 3d sering bertanya cara terbaik untuk memulai sebuah model. Tidak ada cara terbaik, setiap orang punya preferensi masing-masing. Berikut beberapa pendekatan yang paling umum.

### Memahat di bola, multiresolusi {#sculpt-on-sphere-multires}

Model bawaan saat Nomad dijalankan adalah cara yang paling umum. Gunakan alat pindah, clay, dan crease untuk mendorong dan menarik bola hingga terbentuk, gunakan tingkat subdivisi yang lebih rendah saat Anda ingin membuat perubahan besar dengan cepat, dan tingkat subdivisi yang lebih tinggi untuk mengerjakan detail.

Masalah yang sering muncul adalah Anda kehabisan poligon di tempat yang membutuhkannya, sementara di tempat lain poligonnya terlalu banyak. Misalnya, jika Anda membentuk bola bawaan menjadi seluruh tubuh, kemungkinan detailnya tidak cukup untuk membuat jari-jari tangan, sementara banyak poligon terbuang di bagian belakang kepala. Namun untuk bentuk yang sebagian besar bulat seperti kepala, cara ini tidak masalah.

### Dyntopo {#dyntopo}

Mengaktifkan Dyntopo akan menambah dan mengurangi poligon secara adaptif saat Anda memahat. Poligon-poligon ini berupa segitiga, dan pemula sering tidak menyukai susunannya yang berantakan dibanding tampilan multiresolusi yang rapi. Tapi layak untuk terus dicoba! Jika Anda menyalakan shading halus, mematikan wireframe, dan berhenti mengkhawatirkan susunannya, mode ini bisa terasa sangat mirip tanah liat. Jangan lupa bahwa jika Anda memakai kuas besar atau kuas penghalus, mode ini juga bisa mengurangi poligon, sehingga alatnya selalu terasa cepat dan responsif. Setelah tahap pertama pahatan selesai, Anda bisa mengklonnya, memprosesnya dengan quad remesher untuk mendapatkan susunan yang rapi, lalu memproyeksikan ulang detail aslinya ke tingkat subdivisi yang tinggi.

### Voxel remesh {#voxel-remesh}

Voxel remesh menerapkan topologi yang sebagian besar berbasis quad pada pahatan Anda. Operasi ini cepat pada resolusi rendah, dan bisa dipakai untuk segera mengganti poligon yang meregang atau terlalu padat dengan susunan yang merata. Ini bisa menjadi cara yang bagus untuk memulai seluruh tubuh dari sebuah bola; misalnya Anda mulai dari kepala, tarik keluar leher, voxel remesh. Tarik keluar tubuh, voxel remesh, lengan, voxel remesh, dan seterusnya, sampai bentuk dasarnya jadi.

### Memakai beberapa objek {#use-multiple-objects}

Banyak panduan anatomi menggambarkan tubuh dari bola, silinder, dan kubus sederhana. Anda juga bisa memahat dengan cara ini di Nomad. Keuntungannya, Anda bisa menautkan objek sebagai induk-anak dalam hierarki adegan, jadi misalnya Anda bisa memutar leher dan kepala akan ikut. Kemampuan memakai alat gizmo untuk translasi/rotasi/skala yang presisi juga sangat berguna, dan Anda juga bisa mengatur poros per bentuk agar bergerak persis seperti yang Anda harapkan. Setelah balok-balok dasarnya berada di tempat yang tepat, Anda bisa memilih semuanya lalu melakukan voxel remesh atau boolean untuk menyatukannya menjadi satu permukaan untuk sculpting yang lebih detail.

Tips praktis untuk cara kerja ini: mulai dengan bola, ubah skalanya menjadi seperti sosis memanjang, tekan poros, klik 'bawah', lalu tekan poros lagi. Sekarang Anda punya bagian tubuh yang bisa diklon, digeser sepanjang bola pertama, diklon, diputar, diklon, digeser, diklon, dst. untuk menyusun tubuh dengan cepat.

### Tabung {#tubes}

Alat tabung adalah cara yang bagus untuk memulai pahatan. Ekor reptil, lengan, kaki, jari, alis, semuanya bisa dibuat sketsanya dengan cepat memakai alat tabung, lalu mudah disunting setelahnya. Alat ini juga memungkinkan Anda mengubah profil penampangnya, sehingga bentuknya bisa diubah dengan cepat. Anda bisa memvalidasi bentuknya untuk mulai memahatnya, dan melakukan voxel remesh bersama objek lain untuk mendapatkan mesh seluruh tubuh.

### Memakai aplikasi lain {#use-other-apps}

Sebagian orang lebih suka memulai model di aplikasi lain, dan itu juga tidak masalah. Alat seperti Blender atau Valence memungkinkan model dimulai dengan teknik low poly, lalu diimpor ke Nomad untuk dipahat.

### Memakai prasetel bawaan {#use-the-built-in-presets}

Dari menu [File](files.md), klik `Prasetel…` di sebelah kiri bagian proyek. Di sini Anda akan menemukan beberapa prasetel bentuk kepala dan tubuh dari Blender foundation. Pilih yang Anda suka, ketuk lagi, lalu tambahkan ke adegan Anda. 

### Memakai model online {#use-online-models}

Ada banyak model gratis yang tersedia secara online, misalnya polyhaven, sketchfab, turbosquid. Biasanya model-model ini bisa diimpor ke Nomad, lalu dipahat langsung atau dipakai sebagai referensi.

### Tanpa aturan! {#no-rules}

Pada akhirnya, Anda bisa memakai kombinasi apa pun dari teknik-teknik ini, atau tidak sama sekali! Nomad sangat fleksibel dalam hal ini. Pengguna mahir mungkin memulai dengan tabung, lalu dyntopo, lalu menggabungkannya dengan kaki yang diunduh, lalu melakukan quad remesh pada semuanya, lalu multiresolusi untuk detail akhir. Apa pun yang cocok untuk Anda.

## Grup face {#facegroups}

Alat grup face bisa dipakai untuk banyak hal, seperti yang dijelaskan dalam video youtube ini: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Berikut ringkasan tertulis dari fitur-fitur yang dibahas dalam video tersebut.

### Mengapa grup face? {#why-facegroups}

Grup face memungkinkan Anda mengatur dan memilih face ('face' dan 'poligon' dipakai bergantian dalam manual ini). Ini lebih mudah dijelaskan jika dibandingkan dengan alat seleksi dan pengaturan lain di Nomad. Nomad memungkinkan Anda membuat objek, memberinya nama, dan menjadikannya induk-anak, sehingga mudah membuat struktur objek untuk sebuah ruangan yang terdiri dari lantai, dinding, kursi, meja, dan sebagainya.

Untuk karakter, Anda mungkin membuat bentuk dasar awal dengan objek terpisah untuk kepala, lengan, kaki, tetapi begitu semua bagian digabung menjadi satu mesh, struktur ini hilang. Anda bisa mengerjakan bagian-bagian karakter dengan masker, tetapi lama-lama melelahkan jika harus terus mengecat masker untuk tangan, lalu hidung, lalu tangan lagi.

Di sinilah grup face berguna. Grup face memungkinkan Anda menandai face poligon dengan sebuah warna, lalu memilih dan memanipulasi poligon yang berwarna sama. Perlu diingat bahwa warna grup face dan warna verteks adalah dua hal yang berbeda.

Analogi yang paling mendekati adalah mewarnai peta, lalu nantinya bisa memilih negara atau wilayah berdasarkan warnanya.

Untuk kepala karakter, Anda bisa mewarnai zona untuk menandai rongga mata, hidung, bibir, dagu, telinga, lalu dengan mudah memilih zona-zona itu nanti. Untuk sculpting hard surface dan mekanis, grup face berguna untuk menentukan panel dan bagian.

### Membuat dan menyunting grup face {#creating-and-editing-facegroups}

Grup face bisa diterapkan dengan kuas, di mana setiap goresan baru membuat grup face baru, atau kuas bisa memilih grup face di bawah kursor lalu memperluasnya. Grup face juga bisa dibuat dengan bentuk.

* Titik, mode bawaan - satu seretan akan menentukan warna grup face baru dan menerapkannya ke face yang Anda seret. Setiap seretan baru menentukan grup face baru. Satu ketukan akan mengisi penuh grup face baru.
* Titik, mode `Pilih` - saat tombol `Pilih` di bilah alat kiri aktif, Nomad akan memilih grup face di bawah kursor, lalu menerapkannya selama sisa seretan. Ini berguna untuk merapikan grup face tanpa harus memilihnya secara manual.

### Masker {#masking}

Saat alat masker aktif, dan tombol grup face di bilah alatnya aktif, mengetuk sebuah grup face akan memberinya masker.


### Menyembunyikan {#hiding}

Saat alat sembunyi aktif, dan tombol grup face di bilah alatnya aktif, mengetuk sebuah grup face akan menyembunyikannya.

### Mengatur {#organizing}

Seperti disebutkan sebelumnya, grup face bisa dipakai untuk mengatur mesh Anda tanpa harus membuat objek terpisah. Anda mungkin tidak ingin memecah kepala menjadi objek terpisah untuk hidung, dagu, telinga, tetapi sangat berguna jika bagian-bagian itu ditentukan lewat grup face.

### Wilayah UV {#uv-regions}

Alat UV Atlas akan mencoba menentukan seam secara otomatis, tetapi terkadang menaruh seam di tempat yang tidak Anda inginkan. Jika ada grup face pada sebuah objek, dan opsi grup face aktif di opsi UV Atlas, alat ini akan memakai batas grup face sebagai seam UV.

### Quad remesher {#quad-remesher}

Plugin quad remesher biasanya mengalirkan edge dengan rapi di model Anda, tetapi Anda bisa memakai grup face untuk membantu mengarahkannya jika opsi grup face diaktifkan. Ini memudahkan Anda menentukan aliran edge yang rapi di sekitar mata, tonjolan alis, bibir, atau lipatan pipi, misalnya.

### Menyaring dengan alat lain {#filter-with-other-tools}

Banyak alat punya opsi untuk memperhitungkan grup face, baik dari menu utama alatnya, atau lewat menu Goresan -> Filter. Misalnya, alat penghalus dengan kekuatan di atas 100% bisa menghaluskan detail secara agresif di dalam sebuah grup face, tetapi tetap menjaga batas grup face relatif utuh.

### Merelaksasi dan menghaluskan batas grup face {#relax-and-smooth-facegroup-borders}

Opsi `Santai` di alat grup face sangat bagus untuk menghaluskan batas grup face sambil menjaga fitur lain tetap utuh. Ini bisa menjadi cara yang bagus untuk menentukan wilayah batas grup face yang halus sebelum melakukan quad remesh.

## Keterbatasan di tablet/ponsel {#limitations-on-tabletmobile}

Tablet dan ponsel saat ini sangat bertenaga, tetapi punya perbedaan penting dibanding komputer desktop dan laptop:

### Tanpa pendinginan aktif {#no-active-cooling}

Komputer punya kipas dan/atau heatsink besar agar tetap dingin, dan dirancang untuk berjalan pada suhu tinggi. Perangkat keras seluler biasanya dirancang untuk tipis terlebih dahulu, bukan untuk membantu menjaga komponen di dalamnya tetap dingin. Jika Nomad dipaksa ke pengaturan kualitas tertingginya (mode pencahayaan PBR, material yang rumit, banyak objek, banyak opsi pascaproses aktif), perangkat bisa kepanasan dan baterainya bisa cepat habis. 

Pendekatan yang lebih baik adalah memakai mode pencahayaan matcap, dan memakai `Resolusi render` yang lebih rendah (di bagian atas menu PascaProses). Pilihan ini menjaga perangkat tetap dingin dan memungkinkan Anda memahat lebih lama.

### Memori terbatas {#limited-memory}

Nomad bisa mencapai hasil yang setara dengan sebagian besar aplikasi sculpting desktop, tetapi tidak bisa melawan hukum fisika! Sebagian besar komputer desktop punya memori dua kali lipat perangkat seluler, dan workstation yang dibuat untuk animasi 3d sering punya memori 4x atau 8x lipat. Karena itu, ada baiknya Anda tahu berapa banyak poligon yang Anda pakai; lakukan beberapa uji coba di perangkat Anda untuk melihat kapan mulai terasa lambat. Hampir semua perangkat yang bisa menjalankan Nomad bisa menangani 1 juta poligon dengan cukup mudah. iPad Pro M2 bisa menangani 8 juta dengan nyaman, dan orang-orang yang mengujinya di iPad terbaru mencapai jauh di atas itu.

Meski begitu, hanya pahatan yang paling detail yang membutuhkan lebih dari 4 juta poligon; jika Anda membuat objek yang relatif sederhana dan sering melewati 500.000, 1 juta, 4 juta, berarti Anda memakai terlalu banyak poligon! Pastikan `Shading halus` diaktifkan di [Pengaturan](settings.md).

### OS kurang toleran terhadap aplikasi berat {#os-is-less-forgiving-with-intensive-apps}

Apple dan Android mengharapkan aplikasi menyimpan dan memuat file kecil dengan sangat cepat. Mereka juga menganggap aplikasi bisa berpindah tugas dengan sangat cepat. Sekali lagi, Nomad memakai beberapa trik cerdas untuk menjaga ukuran file relatif kecil dan menyimpannya dengan sangat cepat, tetapi jika OS seluler menganggap Nomad terlalu lama, OS akan langsung menghentikannya sebelum tugasnya selesai. Ini alasan lain untuk menjaga ukuran file tetap kecil; bekerja dengan pahatan 37 juta poligon memang mungkin, seperti yang dilaporkan seorang pengguna di discord, tetapi tidak disarankan!

## Bekerja di layar kecil {#working-on-small-screens}

Nomad dirancang untuk tablet, tetapi juga bekerja dengan baik di ponsel. Memahat di layar kecil seperti ponsel bisa dibuat lebih mudah dengan beberapa penyesuaian UI dan alur kerja:

* Ketukan 4 jari akan menyembunyikan atau menampilkan seluruh UI, memberi Anda lebih banyak ruang untuk memahat.
* Seretan 3 jari ke atas dan ke bawah akan mengubah jari-jari kuas
* Skala UI bisa diperkecil agar muat lebih banyak tombol jika penglihatan Anda bagus, atau diperbesar jika penglihatan Anda kurang baik!
* Menu yang lebih lebar terkadang bisa menghalangi pahatan; Anda bisa membuatnya transparan dan tidak buram agar pahatan di bawah menu tetap terlihat.
* Jika memahat dengan jari, gunakan opsi [`Offset stroke`](stroke.md#stroke-offset) untuk menggeser pusat kuas sedikit menjauh dari jari Anda.
* Opsi-opsi ini dan banyak lagi bisa ditemukan di [menu Antarmuka](./interface.md). 


## Deformer inflate atau peak {#inflate-or-peak-deformer}

Banyak aplikasi 3d punya deformer inflate, yang mendorong semua verteks sepanjang normalnya sejauh jumlah yang bisa diatur. Meskipun Nomad saat ini belum punya deformer, perilaku ini bisa ditiru dengan kuas kembung:

* Pilih kuas kembung
* Dari [menu Goresan](./stroke.md#stroke), ubah metode goresan ke `Kunci + jari-jari`
* Buat jari-jari kuas lebih besar dari pahatan Anda, dan mundurkan kamera dari pahatan jika perlu.
* Klik lalu seret sebuah goresan di permukaan objek Anda; jika jari-jarinya lebih besar dari objek, seluruh bentuk akan menggembung secara merata sejauh jumlah yang tetap.
* Sesuaikan intensitas kuas untuk mengatur seberapa besar penggembungannya
* Gunakan masker jika perlu, untuk melindungi atau mengurangi efek kembung di area tertentu.

## Menghilangkan benjolan atau 'jerawat' dari operasi voxel remesh {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Voxel remesh sangat bagus untuk membuat poligon yang merata, tetapi terkadang menghasilkan topologi yang menimbulkan benjolan atau jerawat kecil saat dihaluskan. Contohnya:

* Gunakan kuas crease pada bola bawaan dan buat pusaran
* Lakukan voxel remesh dengan `Bangun multiresolusi` di 3
* Haluskan dengan intensitas tinggi
* artefak muncul (lebih mudah terlihat dengan material matcap yang kontrasnya tinggi):

![](/videos/tip_pimples_before.mp4)

Untuk memperbaikinya lewat sculpting, coba opsi `Pelembutan stabil` di pengaturan penghalus. Opsi ini bisa menangani susunan topologi voxel remesh yang tidak merata, dan memberi hasil yang bersih.

![](/videos/tip_pimples_stable_smooth.mp4)

Untuk memperbaiki topologinya sendiri, gunakan primitif baru, alat quad remesh, atau aplikasi pemodelan 3d eksternal, lalu proyeksikan detail dari mesh asli ke mesh baru lewat `Topologi -> Bake -> Proyeksi ulang → Verteks`. 

![](/videos/tip_pimples_reproject.mp4)

## Pencahayaan siang hari {#daylight-lighting}

Render PBR bawaan, sesuai namanya, berbasis fisika, dan seperti foto digital yang belum diolah, hasilnya bisa tampak sedikit pucat dan datar. Cahaya dan pascaproses Nomad bisa dipakai untuk membuat render tampak lebih hidup.

Berikut render bawaan, mari kita lihat apakah bisa dibuat lebih bagus:
![](/images/tips_lighting_default.webp)

Mengaktifkan pascaproses dan tonemapping bisa menambah kecerahan dan kontras:

![](/images/tips_lighting_tonemap.webp)

Untuk cahayanya, cahaya lingkungan bawaan sudah bagus untuk memahat, tetapi bisa ditingkatkan untuk render akhir. Salah satu cara memikirkannya adalah memisahkan cahaya langsung (misalnya matahari) dari cahaya lingkungan (misalnya cahaya dari birunya langit, atau dari tanah). Dengan mengurangi cahaya lingkungan dan memutarnya, hasilnya mulai menyerupai pencahayaan subjek yang berada di area teduh:

![](/images/tips_lighting_env.webp)

Cahaya langsung bisa ditambahkan, dan intensitasnya dinaikkan untuk meniru sinar matahari yang terik. Menyeimbangkannya dengan cahaya lingkungan akan memberi hasil yang enak dilihat:

![](/images/tips_lighting_sunlight.webp)

Karakter bisa terlihat lebih bagus jika materialnya diganti menjadi subsurface, dan lampu sorot ditempatkan di belakang karakter mengarah ke telinga agar telinganya tampak bercahaya:

![](/images/tips_lighting_sss.webp)

Lalu bereksperimenlah dengan pengaturan pascaproses lainnya! Global Illumination dan Ambient Occlusion membantu menghasilkan pencahayaan yang lebih realistis. Curvature dan Sharpen bisa membantu menonjolkan lebih banyak detail pada pahatan. Chromatic Aberration, Depth of Field, Grain, Bloom, dan Vignette membantu meniru efek kamera. Perlu diingat, setiap kali fitur diaktifkan, pencahayaan dan nilai pascaproses lainnya perlu disesuaikan untuk mengimbanginya.

Berikut render dengan serangkaian penyesuaian pascaproses lengkap:
![](/images/tips_lighting_final.webp)
