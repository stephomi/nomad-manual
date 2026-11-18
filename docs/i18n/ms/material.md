# ![](/icons/material.webp) Bahan {#material}

Menu ini membolehkan anda mengubah bahan objek semasa, sifat pemaparan objek/bahan, dan menetapkan tekstur kepada bahan.

![](/images/material_overview.webp)

Bahan menentukan rupa sesuatu objek, dengan mengawal cara ia bertindak balas terhadap cahaya dan objek lain. Rupa objek dikawal oleh sifat-sifat berikut:

* `Jenis bahan`
* `Warna`
* `Kekasaran`
* `Kemetalan`
* `Kelegapan`
* `Pantulan`
* `Pancaran/tanpa pencahayaan`

Gabungan sifat-sifat ini boleh menghasilkan pelbagai hasil, daripada fotorealistik hingga kartun hingga eksperimental.

Warna, kekasaran, kemetalan dan kelegapan boleh dicat; lihat [pilihan Cat Verteks](painting.md) untuk maklumat lanjut.

Jenis bahan, pantulan dan pancaran/tanpa pencahayaan ialah sifat bahan yang diterangkan di bawah.

Butang `Salin` dan `Tampal` di bahagian atas menu ini membolehkan anda menyalin bahan dari satu objek ke objek lain.

Perhatikan bahawa pemapar Nomad ialah pemapar masa nyata; walaupun berkuasa, ia mengutamakan kelajuan berbanding ketepatan bagi sesetengah kesan. 

## Jenis bahan {#material-types}

![](/images/material_types.webp)

Jenis bahan dalam Nomad ialah Legap, Bawah permukaan, Pencampuran, Penambahan, Pembiasan, Dithering dan Penangkap bayang.

### ![](/icons/material_opaque.webp) Legap {#opaque}
Mod lalai yang menganggap permukaan sebagai bahan ringkas yang menyokong warna, kekasaran, kemetalan dan kelegapan yang dicat. Kelegapan yang dicat, tekstur kelegapan atau saluran alpha tekstur warna masih menjadikan objek lut sinar, menggunakan dithering. Hanya peluncur kelegapan utama yang diabaikan.

### ![](/icons/material_subsurface.webp) Bawah permukaan {#subsurface}
Mod ini boleh menyimulasikan bahan yang membolehkan cahaya kabur dan berselerak di dalamnya, seperti kulit, lilin dan jed.

Ia memerlukan mod shading PBR. Untuk hasil terbaik, gunakan sekurang-kurangnya satu lampu berarah atau lampu sorot, sebaik-baiknya dengan persekitaran yang malap.

Petak warna menetapkan warna cahaya yang berselerak.

`Kedalaman` mengawal sejauh mana cahaya berselerak dari hadapan, ke bawah permukaan, kemudian keluar semula melalui permukaan hadapan. Ini melembutkan bayang yang keras, dan mengaburkan butiran permukaan.

`Tembus cahaya` mengawal cara cahaya berselerak dari hadapan ke belakang sesuatu bentuk, seperti cahaya yang menembusi bahagian bawah daun, atau apabila telinga disinari kuat dari belakang. Anda memerlukan lampu yang menghasilkan bayang untuk melihatnya.

### ![](/icons/material_blending.webp) Pencampuran {#blending}

Serupa dengan Legap, tetapi menyokong peluncur kelegapan untuk membolehkan bahan bercampur antara padu dan lut sinar. Ini ialah peluncur kelegapan tunggal yang ringkas, berbanding kelegapan boleh cat yang disokong oleh bahan legap. 

::: warning
Mod pencampuran boleh menyebabkan kelipan dan objek muncul-hilang pada bentuk yang kompleks atau bersilang.
:::

### ![](/icons/material_additive.webp) Penambahan {#additive}
Anda boleh menjadikan mesh anda separa lut sinar dengan bahan ini. Ia serupa dengan bahan pencampuran, tetapi sementara pencampuran bercampur dengan persekitarannya, penambahan sentiasa lebih terang daripada objek di belakangnya; sesuai untuk kesan terang seperti sinaran cahaya, api dan letupan.

Anda boleh menetapkan nilai kelegapan melebihi 1, yang bermakna objek akan menjadi lebih terang.  
Ini berguna jika anda mahu menggunakan [pemekaran](postprocess.md#bloom) dan parameter `Ambang` supaya hanya objek ini bercahaya seperti objek pancaran.

Mod ini cenderung mempunyai kurang artifak berbanding [Pencampuran](#blending) (kelutsinaran bebas susunan).

### ![](/icons/material_refraction.webp) Pembiasan {#refraction}
Mod ini boleh digunakan untuk menyimulasikan bahan kaca. Ia memerlukan mod shading PBR. Disebabkan kekangan masa nyata, pembiasan kendiri dan pembiasan berbilang lapisan agak terhad.

Kekasaran yang dicat pada model mempengaruhi tahap kekaburan pembiasan.
Secara lalai, setiap objek yang dicipta dalam Nomad mempunyai kekasaran sekitar 25%, jadi pembiasan tidak akan sempurna tetapi sedikit kabur.
Anda boleh menggunakan butang `Cat berkilat` untuk mengecat semula model anda dengan kekasaran dan kemetalan 0 (warna tidak akan terjejas).

Terdapat 2 kekasaran berbeza yang terlibat: satu mengawal tahap kekaburan pantulan pada permukaan, dan satu lagi mengawal bahagian dalam (pembiasan).  
Walau bagaimanapun, oleh sebab Nomad hanya mempunyai satu saluran kekasaran cat, kekasaran dalaman dan luaran akan berkongsi nilai yang sama.  
Untuk mendapatkan nilai yang berbeza (contohnya lolipop dengan permukaan tajam tetapi bahagian dalam yang kabur), gunakan peluncur `Permukaan` dan `Dalaman` di bawah `Gantikan kekasaran` untuk menggantikan kekasaran yang dicat.

![](/videos/refraction.mp4)

#### Indeks Pembiasan {#index-of-refraction}
Sejauh mana cahaya membengkok apabila memasuki objek. Nilai yang lebih tinggi membengkokkannya lebih banyak, seperti kanta tebal.

#### Penyerapan {#absorption}
Menyimulasikan cahaya yang diserap semasa ia bergerak melalui isipadu, diwarnakan oleh petak warna, dengan `Faktor` menetapkan kekuatannya. Bahagian yang nipis lebih terang kerana ia membenarkan lebih banyak cahaya melaluinya, manakala kawasan yang tebal lebih gelap. Hanya anggaran ketebalan objek yang digunakan, jadi kesannya sangat bergantung pada bentuk.


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Menjadikan objek separa lut sinar dengan membuang sebahagian piksel secara rawak.

### ![](/icons/material_shadow_catcher.webp) Penangkap bayang {#shadow-catcher}

Menjadikan objek tidak kelihatan, dan hanya menerima bayang daripada lampu. Berguna untuk menggabungkan hasil pemaparan Nomad dengan imej lain, biasanya pada satah. Petak warna menetapkan warna bayang.

Mesti ada lampu yang menghasilkan bayang dalam adegan; jika tidak, penangkap bayang tidak melakukan apa-apa. Butang `Kemetalan → 0%` dan `Kemetalan → 100%` mengecat semula objek: apabila logam sepenuhnya, penangkap bayang juga boleh memantulkan adegan apabila pemprosesan pasca [Pantulan (SSR)](postprocess.md#reflection-ssr) didayakan.

::: tip

Maklumat lanjut tentang kelutsinaran dan mod pencampuran boleh didapati di https://support.fab.com/s/article/Transparency-Opacity

:::

## Kawalan {#controls}

![](/images/material_controls.webp)

### ![](/icons/circle_fill.webp) Sentiasa tanpa pencahayaan {#always-unlit}
Jika didayakan, objek akan mengabaikan PBR dan MatCap dan hanya memaparkan warna catnya tanpa shading.
Perhatikan bahawa jika anda menggunakan [Penambahan](#additive), anda boleh mengecat kelutsinaran terus dengan menggunakan warna hitam.

### Kelegapan {#opacity}
Sejauh mana padu atau legapnya sesuatu objek; 100% ialah padu, 0% ialah lut sinar. Peluncur ini dipaparkan untuk jenis Pencampuran, Penambahan, Dithering dan Penangkap bayang. Anda juga boleh mengecat kelegapan untuk kawalan yang lebih halus.

### Laluan pra-pembiasan {#pre-refract-pass}
Pencampuran dan Penambahan sahaja. Melukis objek lut sinar ini sebelum laluan pembiasan. Berguna apabila objek yang membias berada di hadapan permukaan lut sinar yang lain.

### Pantulan {#reflectance}
Mengawal jumlah pantulan yang diterima oleh bahan bukan logam. Biasanya nilai lalai patut digunakan (yang sepadan dengan piawai 4% cahaya dipantulkan pada sudut normal), tetapi ia boleh dinaikkan untuk menguatkan pantulan dan kilauan pada mata watak, sebagai contoh. Ia memerlukan mod shading PBR.

### ![](/icons/culling.webp) Pengubahan pemotongan {#inverse-culling}
Menyongsangkan normal sesuatu permukaan. Biasanya tidak diperlukan, tetapi boleh digunakan jika model kelihatan terbalik dari dalam ke luar, atau digabungkan dengan `Dua belah` yang dinyahdayakan untuk menghasilkan ruang dalaman di mana dinding yang paling hampir dengan kamera sentiasa tersembunyi.

Pilihan berikut boleh ditetapkan kepada `Auto`, `Tidak` atau `Ya`. Dengan `Auto`, anak panah menunjukkan nilai yang sebenarnya digunakan.

### ![](/icons/sphere_smooth.webp) Shading licin {#smooth-shading}
Lihat [pilihan global](settings.md#smooth-shading).  
Nilai `Auto` akan menggunakan pilihan global.

### ![](/icons/culling.webp) Dua belah {#two-sided}
Muka akan kelihatan dari kedua-dua belah. Lihat [pilihan global](settings.md#two-sided-quick).  
Nilai `Auto` akan menggunakan pilihan global.

### ![](/icons/culling.webp) Warna belakang {#coloured-backface}
Lihat [pilihan global](settings.md#two-sided-quick).
Nilai `Auto` akan menggunakan pilihan global.

### ![](/icons/shadow_cast.webp) Hasilkan bayang {#casts-shadows}
Objek lut sinar juga menghasilkan bayang (dalam corak dithering untuk meniru bayang bercampur).  
Pastikan anda menyahdayakan penghasilan bayang jika anda mempunyai objek besar dalam adegan yang tidak perlu menghasilkan bayang (contohnya lantai yang besar).

### ![](/icons/shadow_receive.webp) Menerima bayang {#recieve-shadows}
Sama ada bayang daripada objek lain dilukis pada objek ini.

### ![](/icons/wireframe.webp) Kerangka dawai {#wireframe}
Lihat [pilihan global](settings.md#wireframe).  
Nilai `Auto` akan menggunakan pilihan global.

### ![](/icons/trash.webp) Tetapkan semula normal {#reset-normals}
Hanya dipaparkan apabila objek yang diimport membawa normalnya sendiri (contohnya dengan `Kekalkan topologi`). Ia membuangnya, supaya shading menggunakan normal yang dikira daripada permukaan.


## Tekstur {#textures}

![](/images/material_textures.webp)

Jika objek mempunyai UV, tekstur boleh digunakan pada bahan sebagai tambahan kepada warna/kekasaran/kemetalan/kelegapan verteks. Biasanya tekstur ini terhasil daripada bake tekstur, tetapi imej yang dicipta di luar Nomad juga boleh digunakan. `UV:✓` atau `UV:✗` di sebelah tajuk memberitahu anda sama ada objek mempunyai UV.

Tekstur boleh digunakan pada

* Warna
* Normal
* Kekasaran
* Kemetalan
* Kelegapan
* Sesaran
* Pancaran

Baris `Penghalangan` juga muncul apabila objek yang diimport mempunyai tekstur oklusi, tetapi Nomad tidak menggunakannya.

Peluncur pada setiap baris menetapkan sejauh mana teksturnya digunakan, daripada tidak langsung hingga sepenuhnya. `Warna` dan `Pancaran` juga mempunyai petak warna yang mewarnai tekstur, dan `Pancaran` menetapkan kekuatan cahayanya.

`Sesaran` menetapkan sejauh mana peta sesaran menolak permukaan. Butang `Gunakan` menggerakkan verteks mengikut sesaran, kemudian membuang peta itu. Hasilnya dimasukkan ke dalam lapisan aktif.

Butang palet di sebelah tajuk membuka pratetap bahan dalam menu [cat](painting.md): ketuk salah satu untuk menyalin teksturnya ke objek. Pada desktop, imej yang diimport disegerakkan dengan fail asalnya apabila anda kembali ke Nomad, dan butang segerak di sebelah tajuk memuatkannya semula.

Mengklik slot tekstur akan memaparkan pemilih. Selepas tekstur ditetapkan kepada slot bahan, mengklik sekali lagi akan memaparkan panel tekstur:

### Pilihan panel tekstur {#texture-panel-options}

![](/images/material_texture_panel.webp)

Panel ini menunjukkan saiz imej dan pratonton tekstur.

### ![](/icons/open.webp) Buka {#open}
Pilih tekstur lain. Pada desktop, `Teroka` menunjukkan fail imej dalam pelayar fail anda.

### ![](/icons/circle_cross.webp) Tiada {#none}
Buang tekstur

### Kelegapan {#texture-opacity}

Tekstur warna sahaja. Jika imej mempunyai saluran alpha, ini membolehkan anda menggunakannya untuk Kelegapan, atau mengabaikannya.

### Format {#normal-format}
Tekstur normal sahaja. Peta normal datang dalam dua jenis, `OpenGL (+Y)` dan `DirectX (-Y)`. Jika butiran kelihatan terbalik, cuba yang satu lagi.

### Ketinggian {#displacement-height}
Tekstur sesaran sahaja.
* `Tempatan` - Ketinggian membesar dan mengecil mengikut skala objek.
* `Dunia` - Ketinggian kekal sama tanpa mengira skala objek.

### Darab {#multiply}
Tekstur kekasaran, kemetalan dan kelegapan sahaja. Mendarabkan nilai tekstur. Apabila nilainya bukan 100%, nilai itu ditunjukkan pada slot tekstur.

### ![](/icons/link.webp) Ikon Rantai/Pautan {#chainlink-icon}

Apabila ikon pautan dalam bahagian berikut didayakan, apa-apa pilihan yang digunakan akan dikongsi dengan tekstur lain (warna, normal, kekasaran, kemetalan, kelegapan, pancaran) yang ikon pautannya juga didayakan. 

Ini memastikan bahawa jika anda mempunyai tekstur yang sejajar, tekstur itu akan kekal sejajar walaupun anda mengubah parameter atau jenis projeksi.


### Projeksi {#projection}
![](/images/material_projection.webp)

Tetapkan cara tekstur digunakan pada objek.

* `Auto` - Jika objek mempunyai UV, gunakan UV; jika tidak, Triplanar
* `UV` - Gunakan koordinat UV mesh untuk menggunakan tekstur. Jika mesh dan tekstur datang dari luar Nomad, atau akan dieksport dari Nomad untuk digunakan di tempat lain, UV ialah pilihan yang betul.
* `Triplanar` - Unjurkan tekstur mengikut paksi X, Y, Z, dan campurkan sambungannya. 

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Unjuran triplanar ialah cara yang berkuasa tetapi ringkas untuk menggunakan tekstur pada objek.

Triplanar umpama mempunyai 6 projektor video yang memancarkan imej yang sama ke bahagian depan, belakang, kiri, kanan, atas dan bawah objek anda.

Hasilnya kemudian boleh di-bake ke dalam UV atau warna verteks jika perlu.


![](/images/material_triplanar_example.webp)

#### Kaedah {#method}

* `Tempatan` - Unjuran akan bergerak bersama transformasi objek
* `Dunia` - Unjuran kekal tetap; menggerakkan objek akan menggelongsorkannya melalui unjuran.

#### Kekerasan {#hardness}

Cara unjuran bercampur. 100% tidak melakukan sebarang pencampuran, dan tepi unjuran akan tajam. 0% akan mencampurkan tepi pada sudut yang luas. Nilai lalai ialah 90%, cukup pencampuran untuk menyembunyikan tepi, sambil membiarkan bahagian lain unjuran kekal tajam.

### Seragam {#uniform}

Apabila ditanda, kekerasan yang sama digunakan untuk semua unjuran. Apabila tidak ditanda, kawalan kekerasan tambahan dipaparkan untuk unjuran X, Y, Z.


### Parameter {#parameter}
![](/images/material_parameter.webp)

#### Penapisan {#filtering}
Kaedah penapisan tekstur yang digunakan. `Auto` ialah nilai lalai; kaedahnya ialah `Terdekat`, `Linear` dan `Mipmap`. Terdekat tidak melakukan sebarang penapisan, jadi tekstur boleh mempunyai artifak bergerigi apabila dilihat dari dekat. Linear dan Mipmap melakukan penapisan yang lebih baik, jadi tekstur kelihatan kabur dan bukannya bergerigi dari dekat.

#### Jubinan - X {#tiling-x}
Jika parameter Skala melebihi 1, menjadikan tekstur lebih kecil daripada UV objek, beginilah cara tekstur dijubinkan di sepanjang paksi X. `Tiada` bermaksud tiada ulangan. `Ulang` akan membuat salinan tekstur. `Pantulan` akan membuat salinan tekstur dengan setiap salinan kedua diterbalikkan, yang boleh membantu menyembunyikan artifak jubinan.

#### Jubinan - Y {#tiling-y}
Sama seperti Jubinan - X, tetapi untuk paksi Y.

### Transformasi {#transform}
![](/images/material_transform.webp)

Transformasi 2d tambahan yang digunakan pada tekstur dalam ruang UV. Butang tetapkan semula mengembalikan nilai lalai; ikon rantai (apabila tekstur selain warna dipilih) akan memautkan atau menyahpautkan transformasi supaya sama dengan tekstur warna.

#### Anjakan {#translation}
Ofset X dan Y tekstur

#### Putaran {#rotation}
Putaran tekstur

#### Skala {#scale}
Skala tekstur; nombor yang lebih besar akan menjadikan tekstur lebih kecil pada objek. Gunakan pilihan Jubinan - X dan Jubinan - Y untuk mengawal apa yang berlaku.

### Skala seragam {#uniform-scale}
Apabila dimatikan, Nomad akan memaparkan kawalan berasingan untuk Skala-X dan Skala-Y.
