# ![](/icons/brush.webp) Goresan {#stroke}

---
![](/images/stroke_overview.webp) 

## Ikhtisar {#overview}

Anda bisa mengatur perilaku goresan pada sebagian besar kuas alat.
Pengaturannya mirip dengan yang ada di aplikasi lukis 2d, tetapi beberapa opsi khusus untuk sculpting dan 3d.

Opsi-opsinya terbagi dalam 5 submenu:

| Nama     | Ikon                         | Deskripsi                                                          |
| :------: | :--------------------------: | :----------------------------------------------------------------: |
| Goresan  | ![](/icons/brush.webp)      | Mengatur cara goresan diterapkan pada model                        |
| Alpha    | ![](/icons/alpha.webp)      | Cara tekstur skala abu-abu dipakai sebagai cap kuas                |
| Penurunan | ![](/icons/falloff.webp)   | Mengatur perubahan kekuatan kuas dari tengah ke tepi               |
| Filter   | ![](/icons/filter.webp)     | Cara kuas dipengaruhi oleh geometri model                          |
| Tekanan  | ![](/icons/pressure.webp)   | Mengatur respons tekanan stylus                                    |

::: tip
Tidak semua opsi goresan berlaku untuk semua alat. Opsi goresan yang tidak dipakai oleh alat yang sedang aktif akan dinonaktifkan atau disembunyikan. 
:::


## ![](/icons/brush.webp) Goresan {#stroke-1}

### ![](/icons/radius.webp) Jari-jari {#radius}

![](/images/stroke_radius.webp)

Opsi jari-jari adalah pengaturan global: berlaku untuk semua alat.

#### Ruang {#size}

* `Layar` - jari-jari diatur dalam satuan layar. Jika Anda membuat jari-jari selebar 100 piksel, lebarnya akan tetap 100 piksel, entah Anda memperbesar atau memperkecil tampilan.
* `Dunia (3D)` - jari-jari diatur dalam satuan 3d. Misalnya, jika Anda membuat bola lalu menyamakan jari-jari dengan ukuran bola itu, jari-jari akan tetap seukuran bola saat Anda memperbesar atau memperkecil tampilan.

#### ![](/icons/link.webp) Sinkronkan pintasan {#sync-shortcut}

Jika diaktifkan, pengaturan jari-jari dan siluet tetap disamakan saat Anda beralih ke kuas pintasan (`Haluskan`, `Topeng` atau `Sembunyi`). Dengan begitu, penghalusan atau masker cepat memakai ukuran kuas yang sama dengan alat yang tadi Anda gunakan.

#### ![](/icons/link.webp) Bagikan radius {#share-radius}

Jika diaktifkan, semua alat akan memakai jari-jari yang sama. Secara bawaan, setiap alat punya jari-jarinya sendiri.


### Jenis goresan {#stroke-type}

![](/images/stroke_strokemode.webp)

Goresan bisa bekerja dalam beberapa mode:

### ![](/icons/stroke_dot.webp) Titik {#dot}
Seret seperti goresan cat biasa. 
![](/videos/stroke_dot.mp4) 

### ![](/icons/stroke_roll.webp) Roll alpha {#roll}
Alpha kuas akan diputar mengikuti arah goresan, berguna untuk membuat jahitan kain. 
![](/videos/stroke_roll.mp4) 

### ![](/icons/radius.webp) Kunci + jari-jari {#lock-radius}
Mengecap goresan kuas dengan **_tinggi_** tetap. Seretan Anda mengatur skala dan rotasi.
![](/videos/stroke_lock_radius.mp4) 

### ![](/icons/normal.webp) Kunci + intensitas {#lock-intensity}
Mengecap goresan kuas dengan **_jari-jari_** tetap. Seretan Anda mengatur tinggi dan rotasi.
![](/videos/stroke_lock_intensity.mp4) 

::: tip
Mode `Kunci + jari-jari` dan `Kunci + intensitas` mengabaikan pengaturan [Tekanan](#pressure), karena seretan sudah menentukan ukuran dan kekuatannya.
:::

![](/images/stroke_strokemodemove.webp)

Alat `Pindah` dan `Tarik` punya 3 opsi sendiri:

### ![](/icons/snake.webp) Seret {#drag}

Terus memperbarui apa yang berada di dalam jari-jari kuas selama goresan. Goresan cepat akan meninggalkan permukaan di belakang, sedangkan goresan lambat akan terus menahan materialnya sehingga terbentuk bentuk yang lebih panjang. Ini adalah mode bawaan alat `Tarik`. Bersama `Topologi dinamis`, mode ini bisa dipakai untuk membuat ekstrusi seperti ular. 
![](/videos/stroke_drag.mp4) 


### ![](/icons/grab.webp) Ambil {#grab}
Memilih apa yang berada di dalam jari-jari kuas saat goresan dimulai, lalu mempertahankan pilihan itu. Ini berguna untuk pemindahan yang lebih presisi, karena Anda bisa mengatur jarak pemindahan dengan cermat tanpa tidak sengaja ikut memindahkan lebih banyak dari yang Anda pilih di awal. Ini adalah mode bawaan alat `Pindah`.
![](/videos/stroke_grab.mp4) 


### ![](/icons/radius.webp) Kunci + jari-jari (seret) {#lock-radius-drag}
Jari-jari yang Anda atur diabaikan, dan diatur secara dinamis berdasarkan seberapa jauh goresan diseret dari titik awalnya. Jarak kecil = jari-jari kecil, jarak lebih jauh = jari-jari lebih besar. Gunakan penggeser intensitas untuk mengatur bentuk falloff. Berguna untuk membuat bentuk dasar organik yang kenyal.
![](/videos/stroke_lockradius_drag.mp4) 

Beberapa alat lain menampilkan jenis goresannya sendiri di sini, misalnya `Santai`, `Haluskan` dan `Smudge` untuk alat penghalus, atau bentuk seperti `Tali` dan `Lengkung` untuk alat berbasis seleksi. Semuanya dijelaskan bersama masing-masing [alat](tools.md).


### Sesuaikan intensitas jarak {#adjust-spacing-intensity}
![](/images/stroke_space_smooth.webp)

Goresan dengan jarak kecil (di bawah 50%) bisa menumpuk dengan cepat, sehingga hasilnya lebih kuat dibanding goresan dengan jarak lebih besar. Opsi ini mengimbanginya, sehingga intensitas goresan kurang lebih sama berapa pun jaraknya.

### Jarak antar stroke {#stroke-spacing}
Seberapa jauh jarak antar cap kuas saat Anda menyeret. Nilai di bawah 100% akan saling tumpang tindih sehingga goresan tampak menyambung. Nilai di atas 100% mulai menyisakan celah, berguna untuk memahat detail seperti jahitan atau ritsleting.

### Stabilisator tali malas {#lazy-rope-stabilizer}
Goresan akan tertinggal di belakang posisi penunjuk dengan jarak tertentu. Ini bisa dipakai untuk menggambar garis yang mulus.
![](/videos/stroke_lazy_rope.mp4) 

### Penghalusan stroke {#stroke-smoothing}
Merata-ratakan beberapa posisi penunjuk agar goresan lebih halus.
Dengan nilai tinggi, goresan akan tertinggal di belakang penunjuk, tetapi pada akhirnya akan menyusul.
Ini berguna untuk menggambar garis yang mulus.

### Jari-jari snap {#snap-radius}
Menyambungkan goresan ke goresan sebelumnya jika penunjuk mulai di dekat ujung goresan terakhir. Jari-jari ini menentukan seberapa jauh ujung goresan sebelumnya dicari. Berguna untuk menggambar garis panjang yang menyambung sambil sering berhenti sejenak.

### ![](/icons/trail.webp) Jejak {#trail}

Jika diaktifkan, setiap cap baru juga menerapkan ulang titik-titik terakhir dari goresan di belakangnya. `Jumlah jejak` mengatur berapa banyak titik yang diterapkan ulang, `Intensitas jejak` seberapa kuat titik-titik itu, dan `Radius jejak` seberapa besar pertambahan ukurannya.

Jejak hanya bekerja dengan jenis goresan `Titik`, dan tidak dengan [pengaruh falloff](#influence) `Punggungan`.

### ![](/icons/silhouette.webp) Siluet {#silhouette}
![](/images/stroke_silhouette.webp)
Secara bawaan, goresan hanya memengaruhi permukaan model di dalam jari-jari kuas. Jika siluet diaktifkan, goresan akan diproyeksikan menembus seluruh model. Ini sangat berguna saat membuat bentuk dasar model di tahap awal, atau untuk bentuk yang sisi-sisinya harus tetap tegak lurus.

Arah proyeksinya bisa diatur secara eksplisit:

* `X`, `Y`, `Z` - proyeksi sepanjang sumbu tetap.
* `Tampilan` - proyeksi searah kamera.
* `Saat snap` - proyeksi searah kamera, tetapi hanya selama kamera di-snap ke suatu tampilan. Jika tidak, goresannya tetap goresan biasa.
* `Terdekat` - proyeksi sepanjang sumbu yang paling dekat dengan arah kamera. Ini adalah pilihan bawaan.

![](/videos/stroke_silhouette.mp4) 

### ![](/icons/dice.webp)Acak {#randomize}

![](/images/stroke_randomize.webp)

`Intensitas`, `Offset`, `Rotasi` dan `Skala` goresan masing-masing bisa diacak. Gunakan kotak centang di tiap baris untuk menyalakan atau mematikannya. Ini bisa menghasilkan berbagai efek, misalnya acak dengan alat cat bisa membuat warna berbintik, atau acak dengan alat crease bisa dipakai untuk membuat detail kulit.

`Periode (lebih lambat)` mengatur panjang siklus acaknya: naikkan untuk variasi yang lambat dan bergelombang, turunkan untuk noise yang cepat. Tombol kecil di samping tiap baris mengatur skala periode untuk baris itu saja.

![](/videos/stroke_randomize.mp4) 

### ![](/icons/paint.webp) Acak - HSV {#randomize-hsv}

Untuk alat yang mengecat, `Rona`, `Saturasi` dan `Nilai` warna cat juga bisa diacak, dengan periodenya sendiri. Sangat cocok untuk menambahkan variasi warna halus pada kulit atau batu.

### Offset stroke {#stroke-offset}

Menerapkan offset tetap pada goresan, agar jari Anda tidak menutupinya. Ini berguna di layar kecil. Ini adalah pengaturan global: aktifkan dengan kotak centangnya, dan pengaturan ini berlaku untuk semua alat.

## ![](/icons/alpha.webp) Alpha {#alpha}
![](/images/stroke_alpha.webp) 

`Alpha` adalah tekstur yang memodulasi perilaku kuas Anda.
Ini adalah gambar skala abu-abu: piksel hitam berarti tidak ada deformasi, dan piksel putih berarti deformasi penuh.

Klik gambar alpha untuk menggantinya. Selain alpha bawaan dan alpha yang Anda impor sendiri, daftar alpha juga bisa mengunduh peta displacement dari Poly Haven.

Klik pratinjau material untuk memuat alpha dari prasetel material. Di sini Anda juga bisa menyimpan prasetel material, dan memilih untuk menyertakan teksturnya bersama alat.

::: tip
Tekstur tidak pernah diubah ukurannya, jadi tekstur besar bisa memperlambat kinerja.
:::

### ![](/icons/blend_contrast.webp) Perbaiki alfa {#invert-pixels}
Tombol `Perbaiki...` pada alpha yang diimpor membuka popup untuk mengoreksi gambarnya langsung: nilai tengahnya, membalik piksel (hitam menjadi putih dan putih menjadi hitam), rotasi 90°, serta pembalikan horizontal atau vertikal. File gambarnya ditulis ulang, jadi aplikasi lain juga melihat gambar yang sudah dikoreksi.

::: tip

Alpha bawaan yang disertakan dengan Nomad tidak bisa diperbaiki.

:::

### Proyeksi {#projection}

Cara alpha diproyeksikan ke model:

* `Permukaan` - alpha terletak di permukaan di bawah kuas, mengikuti orientasinya.
* `Layar` - alpha diproyeksikan lurus dari tampilan.
* `Ubin` - alpha diproyeksikan dari tampilan dan tetap di tempatnya saat Anda mengecat di atasnya, seperti stensil, sehingga pola berulang tersambung dengan mulus. Rotasinya terkunci, dan tekanan pena tidak mengubah ukuran polanya.
* `Triplanar` - alpha diproyeksikan sepanjang 3 sumbu. Opsi skala, rotasi dan ubin di bawah digantikan oleh pengaturan tekstur triplanar.

### ![](/icons/diagonal.webp) Skala {#scaling}

Ukuran kuas di Nomad berupa lingkaran dengan jari-jari yang Anda tentukan. Tekstur sering kali berbentuk persegi atau persegi panjang, dan parameter `Skala` memungkinkan Anda menentukan bagaimana tekstur dimuat di dalam lingkaran itu. Untuk tekstur persegi, nilai 0,7 akan pas di dalam lingkaran. Nilai 1 akan memperbesar tekstur sehingga lingkarannya yang berada di dalam tekstur, dan tepi tekstur terpotong.

![](/images/alpha_scaling.webp) 

Mengaktifkan `Skala Y` memungkinkan Anda meregangkan alpha secara vertikal. Penggeser pertama lalu menjadi `Skala X`.

![](/images/alpha_scaling_y.webp) 

`Balik horizontal` mencerminkan alpha dari kiri ke kanan.

### Rotasi {#rotation}

Tekstur alpha akan diputar mengikuti arah goresan. Anda bisa menambahkan offset rotasi, dan jika ikon gembok diaktifkan, tekstur akan tetap terkunci pada rotasi ini relatif terhadap layar.

Tombol pena di sebelahnya memutar alpha saat Anda memutar stylus (barrel roll), dengan goresan `Kunci + jari-jari` dan `Kunci + intensitas` selama rotasinya tidak dikunci. Ini hanya bekerja dengan stylus yang mendukungnya.

### Ubin {#tiling}
![](/images/stroke_tiling.webp) 

Seberapa sering tekstur berulang di dalam profil kuas. Mode `Ubin - X` dan `Ubin - Y` memungkinkan Anda membatasi hanya satu tekstur di dalam goresan (`Tidak ada`), tekstur berulang (`Ulangi`), atau dicerminkan, di mana setiap tekstur kedua dibalik untuk membuat pola atau membantu membuat tekstur tanpa sambungan (`Cermin`). Mode ini tersedia dengan goresan `Roll alpha`, proyeksi `Ubin`, atau `Ubin` di atas 1.

`Pas ketat (gambar non-persegi)` hanya berpengaruh untuk alpha dan tekstur kuas yang tidak persegi. Jika diaktifkan, setiap gambar diulang sendiri-sendiri tanpa jarak. Nonaktifkan agar alpha dan gambar lainnya tetap selaras saat rasio aspeknya berbeda.

![](/videos/alpha_tiling.mp4) 



### Nilai tengah {#mid-value}

Secara bawaan, piksel hitam berarti tidak ada deformasi, dan piksel putih berarti deformasi positif penuh. Jadi misalnya, kuas clay dengan tekstur alpha berupa bebatuan hanya akan menarik permukaan keluar di bagian alpha yang tidak hitam.

Jika Anda ingin kuas mendorong permukaan ke dalam, atau mendorong ke dalam DAN menarik keluar sekaligus, Anda bisa mengubah nilai tengahnya. Jadi jika Anda mengaturnya ke 0,5, abu-abu tengah pada alpha tidak melakukan apa-apa, nilai hitam akan mendorong ke dalam, dan putih akan menarik keluar.

Dua tombol membantu Anda menemukan nilai yang tepat: tombol persegi membaca nilai tengah dari tepi gambar, dan pemilih memungkinkan Anda mengambilnya langsung dari alpha.




## ![](/icons/falloff.webp) Penurunan {#falloff}

![](/images/falloff_menu.webp) 

Ini mirip dengan [Alpha](#alpha), hanya saja intensitasnya dikendalikan oleh satu kurva. Falloff digabungkan dengan alpha, sehingga Anda bisa memakai tekstur untuk detail, dan falloff untuk mengatur pemudaran di tepi serta intensitas di tengah alat.

Saat kurva berada di atas, deformasinya penuh; saat berada di bawah, kuas tidak berpengaruh.

Anda bisa membayangkan kurva ini sebagai penampang ujung kuas. Bagian bawah menampilkan pratinjau seperti apa satu 'cap' kuas di permukaan model, dan jika kuas memiliki tekstur alpha, tekstur itu juga ditampilkan untuk melihat bagaimana falloff dan alpha saling berpadu.

### ![](/icons/fx.webp) Prasetel {#preset}
Dengan `Prasetel...` dipilih, mengklik grafik kurva akan memunculkan menu prasetel. Kurva yang membulat memberi hasil lebih lembut, kurva bersudut memberi hasil lebih tajam. Tombol `Kurang` di bilah alat kiri pada dasarnya membalik falloff, sehingga puncak kurva akan mendorong permukaan ke dalam alih-alih menariknya keluar, atau sebaliknya.

### ![](/icons/curve_catmull.webp) Catmull-Rom {#catmull-rom}
Jika dipilih, Anda bisa menggambar kurva falloff sendiri. Editor kurvanya bekerja sama seperti kurva di bagian lain Nomad:

* Klik pada kurva untuk membuat titik baru
* Seret titik untuk memindahkannya
* Klik pada titik untuk beralih antara tajam dan halus
* Seret titik ke titik tetangganya untuk menghapusnya

### ![](/icons/curve_bspline.webp) B-spline {#b-spline}
Jika dipilih, Anda bisa menggambar kurva falloff sendiri. Editornya bekerja sama seperti Catmull-Rom, tetapi titik-titiknya memengaruhi kurva alih-alih berada tepat di atas kurva, yang bisa membantu membuat bentuk kurva lebih halus.

### ![](/icons/curve_bevel.webp) Bevel {#bevel}
Titik-titiknya dihubungkan dengan garis lurus, dengan sudut membulat yang ukurannya bergantung pada ketajaman tiap titik. Praktis untuk kuas berpuncak datar dengan bevel rapi di tepinya.

Editor kurva punya 3 tombol:

| Item     | Ikon                        | Deskripsi                                    |
| :------: | :-------------------------: | :------------------------------------------: |
| Maksimalkan | ![](/icons/maximize.webp) | Memperbesar editor kurva                   |
| Setel ulang | ![](/icons/reset.webp)  | Mengembalikan kurva ke keadaan bawaan        |
| Simetri  | ![](/icons/symmetric.webp) | Menampilkan kurva sebagai 'ujung kuas' simetris |


### Pengaruh {#influence}

* `Bola` (3d) - Pengaruh dihitung dari jarak verteks ke pusat kuas.
* `Lingkaran` (2d) - Verteks terlebih dahulu diproyeksikan ke bidang area, baru kemudian diukur jaraknya ke pusat kuas. Ini mirip dengan cara alpha diambil sampelnya. 
* `Silinder` - Pengaruh diproyeksikan menembus area sebagai silinder. Ini sama dengan mengaktifkan [Siluet](#silhouette-1) di bawah.
* `Punggungan` - Falloff diukur melintang goresan, sehingga kurvanya menjadi penampang seluruh goresan. Tombol `Sim` lalu mencerminkan profilnya melintang goresan: ubah satu sisi dan sisi lainnya mengikuti. Jika dimatikan, kurva berjalan dari sisi kiri goresan ke sisi kanannya. Tidak tersedia untuk alat berbasis flatten.

### ![](/icons/silhouette.webp) Siluet {#silhouette-1}
Secara bawaan, goresan hanya memengaruhi permukaan model di dalam jari-jari kuas. Jika siluet diaktifkan, goresan akan diproyeksikan menembus seluruh model. Ini sangat berguna saat membuat bentuk dasar model di tahap awal, atau untuk bentuk yang sisi-sisinya harus tetap tegak lurus. Opsi proyeksinya sama dengan [Siluet](#silhouette) di tab Goresan.



## ![](/icons/filter.webp) Filter {#filter}

![](/images/filter_menu.webp) 

### ![](/icons/accumulate.webp) Akumulasi stroke {#accumulate-stroke}
Menghapus batas berapa banyak material yang bisa ditambahkan/dikurangi per goresan. Misalnya, alat `Tanah Liat` mengaktifkan opsi ini, jadi material bisa terus menumpuk, sedangkan alat `Kuas` menonaktifkannya, jadi goresan berhenti menambah material jika Anda terus menggerakkan goresan yang sama di area mesh yang sama. 

### ![](/icons/culling.webp) Hanya verteks menghadap depan {#front-facing-vertex-only}
Opsi ini mengabaikan verteks yang menghadap ke belakang.
Berguna jika Anda ingin mengecat sebagian geometri yang tipis tanpa mengenai sisi baliknya.
Opsi ini juga bekerja untuk sculpting, tetapi mungkin muncul beberapa artefak.

### ![](/icons/eye_open.webp) Hanya vertex terlihat {#visible-vertex-only}
Mengabaikan verteks yang tersembunyi di balik permukaan lain, dilihat dari kamera. Opsi ini muncul untuk goresan bentuk (laso, persegi panjang...) pada alat masker, alat cat, `Grup Face` dan `Sembunyi`.

### ![](/icons/dynamic.webp) Izinkan topologi dinamis {#allow-dynamic-topology}
Opsi ini hanya tersedia jika mesh Anda dalam mode [Topologi dinamis](topology.md#dynamic-topology). Anda bisa menonaktifkan atau mengaktifkan topologi dinamis per alat.

### ![](/icons/connect.webp) Topologi terhubung {#connected-topology}
Hanya memahat verteks yang terhubung dengan permukaan yang Anda sentuh dengan alat. Misalnya, jika dipakai dengan alat `Pindah`, opsi ini memungkinkan Anda memindahkan satu bagian meskipun bagian itu bersinggungan dengan bagian lain.
![](/videos/connected_topology.mp4)

### Lindungi area {#protect-area}
![](/images/filter_protect_area.webp) 

Opsi-opsi ini mencegah alat memengaruhi bagian mesh Anda dalam berbagai kondisi. Masing-masing bisa diatur ke `Otomatis`, `Tidak` atau `Ya`, dan panah kecil menunjukkan nilai yang saat ini dipakai oleh `Otomatis`.

* `Sembunyi` - Jika ada bagian mesh yang disembunyikan dengan alat sembunyi, tentukan apakah bagian itu dilindungi. Pada `Otomatis`, face yang tersembunyi dilindungi, kecuali wireframe-nya terlihat (lihat pengaturan [Kerangka kawat](settings.md#wireframe)).
* `Topeng` - Jika ada bagian mesh yang diberi masker, tentukan apakah bagian itu dilindungi. Pada `Otomatis`, bagian yang bermasker dilindungi selama masker terlihat di menu [Shading](shading).
* `Grup Face` - Tentukan apakah alat hanya bisa dipakai di dalam grup face yang pertama kali disentuh. Pada `Otomatis`, ini mengikuti apakah grup face terlihat di menu [Shading](shading).

Tombol `(All)` menentukan apakah perlindungan ini berlaku global, dipakai bersama oleh semua alat, atau diatur per alat.


### Pengambilan sampel area {#area-sampling}
Beberapa kuas atau opsi goresan memerlukan normal bidang dan posisi bidang pada permukaan agar bisa bekerja.

Anda bisa mengatur cara bidang rata-rata ini dihitung dengan menetapkan area pengambilan sampel sebagai rasio dari jari-jari alat.

Pada 100%, setiap titik di dalam lingkaran seleksi ikut diperhitungkan.

Pada 0%, hanya verteks atau segitiga terdekat yang diperhitungkan. Nilai-nilai ini bisa ditautkan untuk `Radius normal` dan `Radius posisi`, atau dilepas tautannya dan diatur masing-masing.

### Filter Normal Area {#keep-sharp-edges}
Mengecualikan titik yang normalnya terlalu menyimpang dari normal permukaan.

Ini mengubah cara area bidang dihitung (Pengambilan sampel area), jadi paling berguna untuk alat clay atau alat berbasis flatten, atau jika Anda ingin mewarnai permukaan yang sebagian besar datar tanpa warnanya meluber.

Sudut `Min` dan `Maks` mengatur peralihan antara titik yang dikecualikan dan titik yang terpengaruh penuh, seperti yang ditunjukkan oleh cakram berwarna kecil di sebelahnya.

![](/videos/filter_keep_sharp_edges.mp4)

### Filter Normal Falloff {#falloff-normal-filter}
Seperti [Filter Normal Area](#keep-sharp-edges), filter ini mengecualikan titik yang normalnya terlalu menyimpang dari normal permukaan, tetapi bekerja pada falloff kuas, bukan pada perhitungan bidang. Berguna untuk mengecat lipatan atau tonjolan.


### Filter kedalaman {#depth-masking}
![](/images/stroke_depthmask.webp)

Mengecualikan titik yang berada di atas atau di bawah jarak tertentu dari bidang yang dihitung (Pengambilan sampel area).

Ini bisa dipakai untuk mengecat hanya di area yang menonjol, atau hanya di area cekungan.

Grafiknya menggambarkan penampang permukaan; garis horizontal adalah letak permukaan, dan lingkaran menggambarkan jari-jari falloff cat di atas dan di bawah permukaan. `Penggeseran tinggi` adalah persentase di atas atau di bawah permukaan tempat perhitungan penyaringan dimulai. Dengan `Peredupan kedalaman` diaktifkan, `Area atas` dan `Area bawah` memungkinkan Anda mengatur skala falloff di atas dan di bawah titik offset.

#### Contoh: Mengecat di cekungan {#example-paint-in-cavities}
Untuk mengecat hanya area cekungan, atur penggeseran tinggi ke -100%, lalu sesuaikan penggeser area atas agar menjauh dari garis horizontal. Artinya, klik pertama menetapkan kedalaman 'nol', lalu hanya area di bawah kedalaman ini yang akan terpengaruh.

![](/videos/stroke_depth_cavity.mp4)

#### Contoh: Mengecat di tonjolan {#example-paint-on-bumps}
Untuk mengecat hanya di area tinggi, atur penggeseran tinggi ke +90%, sehingga bagian bawah lingkaran sedikit memotong garis horizontal. Saat Anda mengklik puncak zona yang 'tinggi', kedalamannya ditetapkan di situ, sehingga semua yang berada di kedalaman itu, ditambah sedikit di bawahnya, dan semua yang lebih tinggi akan dicat. Cekungan yang dalam akan dilewati.
![](/videos/stroke_depth_bump.mp4)


## ![](/icons/pressure.webp) Tekanan {#pressure}
![](/images/pressure_menu.webp) 

Mengatur bagaimana tekanan stylus/pena memengaruhi kuas.

### Gunakan pengaturan global {#use-global-settings}

Secara bawaan, `Gunakan pengaturan global` diaktifkan, artinya semua kuas memakai nilai tekanan yang sama. Hapus centangnya untuk memberi alat yang sedang aktif pengaturan tekanannya sendiri.

### ![](/icons/radius.webp) Radius {#pressure-radius}

Kurva ini mengatur bagaimana jari-jari kuas dipengaruhi oleh tekanan. Bawaannya adalah hubungan linear, jadi jika stylus Anda responsnya halus, perubahan jari-jarinya juga akan terasa halus. Meski begitu, banyak stylus punya respons yang tidak linear, dan Anda bisa mengimbanginya dengan kurva ini. Misalnya, jika jari-jari terasa tidak mencapai nilai maksimumnya pada tekanan tinggi, gunakan prasetel kurva seperti 'out-pow3', dengan lengkungan yang mengarah ke atas, agar jari-jari membesar lebih awal.

Dialog ini mirip dengan tampilan kurva falloff: Anda bisa memakai prasetel dengan mengetuk jendela kurva, atau menggambar kurva sendiri dengan mode `Catmull-Rom`, `B-spline` dan `Bevel`.

Jika Anda ingin jari-jari tetap, nonaktifkan bagian ini.

### ![](/icons/intensity.webp) Intensitas {#pressure-intensity}

Mirip dengan kurva jari-jari, tetapi untuk mengatur intensitas. Jika Anda ingin intensitas tetap, nonaktifkan bagian ini.

### Batasi tekanan pada 100% {#limit-pressure}

Memastikan tekanan stylus tidak pernah melebihi 100%. Ini adalah pengaturan global.

### Pelunakan tekanan {#pressure-smoothing}

Merata-ratakan data tekanan stylus untuk hasil yang lebih halus.
