# ![](/icons/manual.webp) Tips {#tips}

[[toc]]

## Cara memulai model {#how-to-start-a-model}

Pemula dalam pemodelan 3D sculpting sering bertanya cara terbaik untuk memulai sebuah model. Tidak ada cara yang paling benar, setiap orang punya preferensi berbeda. Berikut beberapa pendekatan yang paling umum.

### Memahat pada bola, multires {#sculpt-on-sphere-multires}

Model bawaan ketika Nomad dijalankan adalah cara yang paling umum. Gunakan tool move, clay, crease untuk mendorong dan menarik sphere hingga membentuk bentuk yang diinginkan, gunakan level subdivisi yang lebih rendah ketika ingin membuat perubahan besar dengan cepat, gunakan level subdivisi yang lebih tinggi untuk pekerjaan detail.

Masalah umum adalah Anda sering kehabisan poligon di area yang membutuhkannya, sementara di tempat lain justru terlalu banyak poligon. Misalnya jika Anda mendorong sphere bawaan menjadi satu tubuh penuh, kemungkinan Anda tidak punya cukup detail untuk membuat jari, sementara banyak poligon terbuang di bagian belakang kepala. Namun untuk bentuk yang sebagian besar bulat seperti kepala, hal ini bisa saja cukup.

### Dyntopo {#dyntopo}

Mengaktifkan Dyntopo akan secara adaptif menambah dan menghapus poligon saat Anda melakukan sculpt. Poligon ini akan berupa segitiga, dan pemula sering tidak menyukai tata letak yang berantakan dibandingkan tampilan rapi pada multires. Layak untuk terus dicoba! Jika Anda menyalakan smooth shading, mematikan wireframe dan berhenti mengkhawatirkan tata letak, mode ini bisa memberikan rasa seperti tanah liat. Jangan lupa bahwa jika Anda menggunakan kuas besar, atau kuas smooth, mode ini juga bisa menghapus poligon, sehingga tool selalu terasa cepat dan responsif. Setelah Anda menyelesaikan pass pertama sculpt, Anda bisa mengkloningnya dan menjalankannya melalui quad remesher untuk mendapatkan tata letak yang bagus, lalu memproyeksikan ulang detail asli ke level subdivisi tinggi.

### Voxel remesh {#voxel-remesh}

Voxel remesh akan menerapkan topologi berbasis quad pada sculpt Anda. Operasi ini cepat pada resolusi rendah, dan bisa digunakan untuk dengan cepat mengganti poligon yang tertarik berlebihan atau terlalu padat dengan tata letak yang jaraknya merata. Ini bisa menjadi cara yang bagus untuk memulai tubuh penuh dari sebuah sphere; misalnya Anda mulai dengan kepala, Anda bisa menarik leher, voxel remesh. Tarik badan, voxel remesh, lengan, voxel remesh, dan seterusnya, sampai Anda mendapatkan bentuk dasar.

### Gunakan beberapa objek {#use-multiple-objects}

Banyak panduan anatomi akan merepresentasikan tubuh dari bola, silinder, kubus sederhana. Anda juga bisa melakukan sculpt seperti ini di Nomad. Ini memiliki keuntungan karena memungkinkan Anda untuk melakukan parent objek dalam hierarki scene, sehingga Anda bisa memutar leher dan kepala akan ikut, misalnya. Kemampuan menggunakan tool gizmo untuk translasi/rotasi/skala yang presisi juga sangat berguna, dan Anda juga bisa mengatur pivot per bentuk sehingga mereka bergerak persis seperti yang Anda harapkan. Ketika blok-blok dasar sudah berada di posisi yang tepat, Anda bisa memilih semuanya dan melakukan voxel remesh atau boolean menjadi satu permukaan untuk sculpting yang lebih detail.

Tips praktis untuk cara kerja ini adalah mulai dengan sebuah sphere, skala menjadi bentuk sosis memanjang, tekan pivot, klik 'bottom', tekan pivot lagi. Sekarang Anda punya bagian tubuh yang bisa diklon, digeser sepanjang panjang sphere pertama, diklon, diputar, diklon, digeser, diklon dan seterusnya untuk menyusun tubuh dengan cepat.

### Tabung {#tubes}

Tool tube adalah cara yang sangat bagus untuk memulai sculpt. Ekor reptil, lengan, kaki, jari, alis, semuanya bisa dengan cepat digambar dengan tool tube, lalu mudah diedit setelahnya. Tool ini juga memungkinkan Anda memodifikasi profil penampang, sehingga perubahan bentuk bisa dilakukan dengan cepat. Anda bisa memvalidasi bentuk untuk mulai melakukan sculpt di atasnya, dan melakukan voxel remesh bersama objek lain untuk mendapatkan mesh tubuh penuh.

### Gunakan aplikasi lain {#use-other-apps}

Sebagian orang lebih suka memulai model di aplikasi lain, itu juga tidak masalah. Tool seperti Blender atau Valence memungkinkan model dimulai dengan teknik low poly, lalu bisa diimpor ke Nomad untuk sculpting.

### Gunakan preset bawaan {#use-the-built-in-presets}

Dari menu project klik `Preset...` di kanan atas. Di sini Anda akan menemukan beberapa preset bentuk kepala dan tubuh dari Blender Foundation. Pilih yang Anda suka, ketuk lagi, tambahkan ke scene Anda. 

### Gunakan model daring {#use-online-models}

Ada banyak model gratis yang tersedia secara online, misalnya polyhaven, sketchfab, turbosquid. Biasanya model-model ini bisa diimpor ke Nomad, dan bisa langsung di-sculpt, atau digunakan sebagai referensi.

### Tanpa aturan! {#no-rules}

Pada akhirnya Anda bisa menggunakan kombinasi teknik-teknik ini, atau tidak sama sekali! Nomad sangat fleksibel dalam hal ini, pengguna mahir mungkin menggunakan tubes untuk memulai, lalu dyntopo, lalu menggabungkannya dengan kaki yang diunduh, lalu melakukan quad remesh pada semuanya, lalu multires untuk detail akhir. Apa pun yang cocok untuk Anda.

## Facegroups {#facegroups}

Tool facegroup bisa digunakan untuk banyak hal, seperti dijelaskan dalam video youtube ini: https://youtu.be/qtjYcxS8f9s?si=HGWTG-NqXGstWehx

Ini adalah ringkasan teks dari fitur-fitur yang dibahas dalam video tersebut.

### Mengapa facegroups? {#why-facegroups}

Facegroups memungkinkan Anda mengatur dan memilih faces ('faces' dan 'polygons' digunakan secara bergantian dalam manual ini). Ini lebih mudah dijelaskan dibandingkan tool seleksi dan organisasi lain di Nomad. Nomad memungkinkan Anda membuat objek, menamainya, melakukan parent, mudah untuk membuat struktur objek untuk mendefinisikan sebuah ruangan yang terdiri dari lantai, dinding, kursi, meja dan seterusnya.

Untuk karakter Anda mungkin melakukan block-out awal menggunakan objek terpisah untuk kepala, lengan, kaki, tetapi setelah Anda menggabungkan semua bagian menjadi satu mesh, struktur ini hilang. Anda bisa mengerjakan sub-bagian karakter dengan mask, tetapi bisa melelahkan jika harus terus-menerus melukis mask untuk tangan, lalu hidung, lalu tangan lagi.

Di sinilah facegroups berguna. Ini memungkinkan Anda memberi tag pada polygon faces dengan sebuah warna, lalu dapat memilih dan memanipulasi poly yang memiliki warna yang sama. Perhatikan bahwa warna facegroup dan warna vertex adalah dua hal yang berbeda.

Analogi terdekat adalah mewarnai peta, lalu kemudian bisa memilih negara atau wilayah berdasarkan warna.

Untuk kepala karakter Anda bisa mewarnai zona untuk menandai rongga mata, hidung, bibir, dagu, telinga, lalu dengan mudah memilih zona tersebut nanti. Untuk sculpting hard surface dan mekanikal, ini bisa berguna untuk mendefinisikan panel dan bagian-bagian.

### Membuat dan mengedit facegroups {#creating-and-editing-facegroups}

Facegroups bisa diterapkan dengan kuas, di mana setiap sapuan baru membuat facegroup baru, atau bisa memilih facegroup di bawah kursor dan memperluasnya. Facegroups juga bisa dibuat menggunakan bentuk-bentuk.

* Dot, auto-pick aktif - satu drag akan mendefinisikan warna facegroup baru dan menerapkannya ke faces yang Anda lewati. Setiap drag baru akan mendefinisikan facegroup baru. Satu tap akan melakukan flood fill facegroup baru.
* Dot, auto-pick nonaktif - ketika tombol auto-pick berada dalam mode 'sub', Nomad akan memilih facegroup di bawah kursor, dan menerapkannya selama sisa drag. Ini berguna untuk menyempurnakan facegroups tanpa harus memilihnya secara manual.

### Masking {#masking}

Ketika tool mask aktif, dan tombol facegroup aktif di toolbar-nya, mengetuk sebuah facegroup akan mem-mask-nya.


### Menyembunyikan {#hiding}

Ketika tool hide aktif, dan tombol facegroup aktif di toolbar-nya, mengetuk sebuah facegroup akan menyembunyikannya.

### Mengorganisir {#organizing}

Seperti disebutkan sebelumnya facegroups bisa digunakan untuk mengorganisasi mesh Anda tanpa mengharuskan Anda membuat objek terpisah. Anda mungkin tidak ingin membagi kepala menjadi objek terpisah untuk hidung, dagu, telinga, tetapi sangat berguna jika bagian-bagian tersebut didefinisikan melalui facegroups.

### Wilayah UV {#uv-regions}

Tool UV Atlas akan mencoba mendefinisikan seams secara otomatis, tetapi terkadang menempatkan seams di tempat yang tidak Anda inginkan. Jika facegroups ada pada sebuah objek, dan opsi facegroup aktif di opsi UV Atlas, maka ia akan menggunakan batas facegroup sebagai UV seams sebagai gantinya.

### Quad remesher {#quad-remesher}

Plugin quad remesher biasanya akan mengalirkan edges dengan baik pada model Anda, tetapi Anda bisa menggunakan facegroups untuk membantu mengarahkannya ketika opsi facegroup diaktifkan. Ini bisa memudahkan untuk mendefinisikan alur edge yang bersih di sekitar mata, tulang alis, bibir, lipatan pipi misalnya.

### Filter dengan alat lain {#filter-with-other-tools}

Banyak tool memiliki opsi untuk menyadari facegroup, baik dari menu tool utama, atau melalui menu stroke -> filtering. Misalnya tool smooth pada kekuatan di atas 100% bisa secara agresif menghaluskan detail di dalam sebuah facegroup, tetapi menjaga batas facegroup relatif utuh.

### Merilekskan dan menghaluskan batas facegroup {#relax-and-smooth-facegroup-borders}

Opsi relax di dalam tool facegroup sangat baik dalam menghaluskan batas facegroup sambil menjaga fitur lain tetap utuh. Ini bisa menjadi cara yang bagus untuk mendefinisikan wilayah batas facegroup yang halus sebelum melakukan quad remeshing.

## Keterbatasan pada tablet/mobile {#limitations-on-tabletmobile}

Tablet dan ponsel saat ini sangat bertenaga, tetapi memiliki perbedaan penting dibanding komputer desktop dan laptop:

### Tanpa pendinginan aktif {#no-active-cooling}

Komputer memiliki kipas dan/atau heatsink besar untuk menjaga tetap dingin, dan dirancang untuk berjalan pada suhu tinggi. Perangkat mobile biasanya dirancang untuk setipis mungkin terlebih dahulu, bukan untuk membantu menjaga bagian dalam tetap dingin. Jika Nomad dipaksa ke pengaturan kualitas tertinggi (mode pencahayaan PBR, material kompleks, banyak objek, banyak opsi post processing diaktifkan), ini bisa membuat perangkat terlalu panas dan menguras baterai dengan sangat cepat. 

Pendekatan yang lebih baik adalah menggunakan mode pencahayaan matcap, dan menggunakan render multiplier yang lebih rendah (di bagian atas menu post process). Pilihan-pilihan ini akan menjaga perangkat tetap dingin dan memungkinkan Anda melakukan sculpt lebih lama.

### Memori terbatas {#limited-memory}

Nomad bisa mencapai hasil setara dengan sebagian besar aplikasi sculpting desktop, tetapi tidak bisa melanggar hukum fisika! Kebanyakan komputer desktop memiliki dua kali memori perangkat mobile, workstation yang dibuat untuk animasi 3D sering memiliki 4x atau 8x memori. Karena itu, sebaiknya Anda menyadari berapa banyak poligon yang digunakan, lakukan beberapa tes pada perangkat Anda untuk melihat kapan mulai terasa lag. Hampir semua perangkat yang bisa menjalankan Nomad dapat menangani 1 juta poligon dengan cukup mudah. Ipad Pro M2 bisa menangani 8 juta dengan nyaman, orang-orang telah menguji pada Ipad terbaru jauh di atas itu.

Meski begitu, hanya sculpt yang sangat detail yang membutuhkan lebih dari 4 juta poly; jika Anda membuat objek yang relatif sederhana dan sering mendapati diri Anda melampaui 500.000, 1 juta, 4 juta, berarti Anda menggunakan terlalu banyak poligon! Pastikan mode smooth shaded diaktifkan di opsi.

### OS kurang toleran terhadap aplikasi intensif {#os-is-less-forgiving-with-intensive-apps}

Apple dan Android mengharapkan aplikasi akan menyimpan dan memuat file kecil dengan sangat cepat. Mereka juga mengasumsikan aplikasi bisa berpindah tugas dengan sangat cepat. Sekali lagi Nomad melakukan beberapa trik cerdas untuk menjaga ukuran file relatif kecil dan menyimpannya dengan sangat cepat, tetapi jika OS mobile memutuskan Nomad memakan waktu terlalu lama, ia akan langsung mematikannya sebelum menyelesaikan tugas. Ini alasan lain untuk menjaga file tetap kecil; memungkinkan untuk bekerja dengan sculpt 37 juta poly seperti yang dilaporkan salah satu pengguna di discord, tetapi tidak direkomendasikan!

## Bekerja pada layar kecil {#working-on-small-screens}

Nomad dirancang untuk bekerja pada tablet, tetapi juga bekerja dengan baik di ponsel. Sculpting pada layar kecil seperti ponsel bisa dibuat lebih mudah dengan beberapa penyesuaian UI dan alur kerja:

* Tap 4 jari akan mengaktifkan/nonaktifkan seluruh UI, memberi Anda lebih banyak ruang untuk sculpt.
* Drag 3 jari ke atas dan ke bawah akan mengubah radius kuas
* Skala UI bisa dibuat lebih kecil untuk memuat lebih banyak tombol jika penglihatan Anda baik, atau lebih besar jika penglihatan Anda kurang baik!
* Menu yang lebih lebar terkadang menghalangi sculpt, Anda bisa membuatnya transparan dan tanpa blur agar bisa melihat sculpt di bawah menu.
* Jika melakukan sculpt dengan jari, gunakan opsi offset untuk memindahkan pusat kuas sedikit menjauh dari jari Anda.
* Opsi-opsi ini dan banyak lagi bisa ditemukan di [Interface menu](./interface.md). 


## Deformer inflate atau peak {#inflate-or-peak-deformer}

Banyak aplikasi 3D memiliki inflate deformer, yang akan mendorong semua vertex sepanjang normal-nya dengan jumlah yang bisa diatur. Meskipun Nomad saat ini belum memiliki deformers, perilaku ini bisa ditiru dengan kuas inflate:

* Pilih kuas inflate
* Dari [Stroke menu](./stroke.md#stroke) ubah metode stroke menjadi `Lock + Radius'
* Buat radius kuas lebih besar dari sculpt Anda, zoom kamera menjauh dari sculpt jika perlu.
* Klik lalu drag sebuah stroke di permukaan objek Anda; ketika radius lebih besar dari objek, seluruh bentuk akan mengembang secara merata dengan jumlah tetap.
* Sesuaikan intensitas kuas untuk mengontrol jumlah pengembangan
* Gunakan masking jika perlu untuk melindungi atau mengurangi efek inflate di area tertentu.

## Menghilangkan tonjolan atau 'jerawat' dari operasi voxel remesh {#remove-lumps-or-pimples-from-a-voxel-remesh-operation}

Voxel remesh sangat bagus untuk membuat poligon yang jaraknya merata, tetapi terkadang menciptakan topologi yang akan menyebabkan benjolan kecil atau jerawat ketika dihaluskan. Misalnya:

* Gunakan kuas crease pada sphere bawaan dan buat pusaran
* Voxel remesh dengan 'build multiresolution at 3'
* Smooth dengan intensitas tinggi
* artefak muncul (lebih mudah dilihat dengan material matcap kontras tinggi):

![](/videos/tip_pimples_before.mp4)

Untuk memperbaiki lewat sculpting, coba opsi `Stable smoothing` di pengaturan smooth. Ini bisa menangani tata letak topologi yang tidak rata dari voxel remesh, dan menghasilkan hasil yang bersih.

![](/videos/tip_pimples_stable_smooth.mp4)

Untuk memperbaiki topologi itu sendiri, gunakan primitive baru, atau tool quad remesh, atau pemodel 3D eksternal, dan proyeksikan detail dari mesh asli ke mesh baru melalui `Topology -> Misc -> Reproject`. 

![](/videos/tip_pimples_reproject.mp4)

## Pencahayaan siang hari {#daylight-lighting}

Render PBR bawaan, seperti namanya, berbasis fisika, yang seperti foto digital mentah bisa terlihat agak pudar dan datar. Lampu dan post processing Nomad bisa digunakan untuk membuat render terlihat lebih hidup.

Berikut render bawaan, mari kita lihat apakah bisa dibuat lebih baik:
![](/images/tips_lighting_default.webp)

Mengaktifkan post processing dan tonemapping bisa menambah kecerahan dan kontras:

![](/images/tips_lighting_tonemap.webp)

Untuk fokus pada lampu, environment light bawaan bagus untuk sculpting, tetapi bisa ditingkatkan untuk render akhir. Salah satu cara memikirkannya adalah memisahkan direct light (misalnya matahari) vs environment light (misalnya cahaya dari birunya langit, tanah). Dengan mengurangi environment light dan memutarnya, ini mulai menangkap seperti apa pencahayaan jika subjek berada di area teduh:

![](/images/tips_lighting_env.webp)

Sebuah direct light bisa ditambahkan, dan intensitasnya ditingkatkan untuk mensimulasikan sinar matahari yang keras. Menyeimbangkan ini dengan environment light akan menghasilkan hasil yang menyenangkan:

![](/images/tips_lighting_sunlight.webp)

Karakter bisa mendapatkan manfaat dari penggantian material menjadi subsurface, dan menempatkan spotlight di belakang karakter mengarah ke telinga untuk membuatnya berpendar:

![](/images/tips_lighting_sss.webp)

Lalu bereksperimenlah dengan sisa pengaturan post process! Global Illumination dan Ambient Occlusion membantu pencahayaan yang lebih realistis. Curvature dan Sharpen bisa membantu menonjolkan lebih banyak detail sculpt. Chromatic Aberration, Depth of Field, Grain, Bloom, Vignette membantu mensimulasikan efek kamera. Perhatikan bahwa ketika fitur diaktifkan, pencahayaan dan nilai post processing lain perlu disesuaikan untuk mengompensasi.

Berikut render dengan serangkaian penuh penyesuaian post processing:
![](/images/tips_lighting_final.webp)