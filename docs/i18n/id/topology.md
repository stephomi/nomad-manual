# ![](/icons/multires.webp) Topologi {#topology}

Menu ini mengontrol topologi objek di Nomad, serta alat untuk membake dan mentransfer detail antar objek, dan antar tekstur.

![](/images/topology_overview.webp)

Nomad berbasis poligon, menggunakan segitiga dan quad untuk menangani geometri.
Dengan topologi, yang dimaksud adalah baik jumlah face maupun cara titik-titik (vertex) saling terhubung.

Penting untuk memantau topologi, terutama jika ingin memahat atau mengecat detail halus.

::: tip Bagaimana memantau topologi?
Anda bisa menampilkan [Wireframe](settings.md#wireframe) atau cukup menonaktifkan [Smooth Shading](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Menu topology di Nomad memiliki beberapa bagian:

| Method                                | Icon                         | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Mengedit beberapa level detail menggunakan subdivision           |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | Menghitung ulang topologi baru dengan kerapatan seragam          |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | Menambah/Menghapus face secara lokal secara real-time saat memahat atau mengecat |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | Decimation, UV, baking, remeshing, reprojection                  |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | Opsi primitive                                                   |


## Statistik poligon {#polygon-stats}

![](/images/topology_stats.webp)

Bagian atas menu topology menampilkan informasi poligon untuk objek terpilih dan seluruh scene. Angka-angka menunjukkan total jumlah vertex, total jumlah segitiga, dan total jumlah quad (poligon 4 sisi).

Mengetuk bagian ini akan menampilkan daftar statistik poligon untuk semua objek poligon di scene.

## ![](/icons/multires.webp) Multiresolusi {#multiresolution}

![](/images/topology_multires_menu.webp)

### Apa itu multiresolusi? {#what-is-multiresolution}
Fitur multiresolution berguna untuk dua skenario utama:
- Algoritma smooth subdivision untuk meningkatkan jumlah poligon objek Anda
- Menangani beberapa level resolusi sehingga Anda bisa bergantian antara edit skala besar dan kecil

![](/videos/multiresolution.mp4)

#### Alur kerja multiresolusi {#multiresolution-workflow}
Satu aspek penting dari multiresolution adalah Anda bisa kembali ke resolusi lebih rendah, melakukan perubahan pada objek lalu kembali ke resolusi tertinggi tanpa kehilangan detail resolusi tinggi. Semua detail resolusi tinggi akan diproyeksikan secara otomatis.

::: warning
Jika Anda menggunakan tool yang mengubah topologi objek, Anda akan kehilangan semua resolusi lain dari objek tersebut!
Anda akan selalu mendapat peringatan jika hal ini akan terjadi, misalnya saat menggunakan:
- [Voxel Remesher](#voxel-remesher)
- [Dynamic Topology](#dynamic-topology)
- [Trim tool](tools.md#trim)
- [Split tool](tools.md#split)
:::


### Slider multiresolusi {#multiresolution-slider}
Slider ini menunjukkan jumlah level subdivision pada objek saat ini. Jika ada 6 bar vertikal, berarti ada 6 level subdivision. Lingkaran menunjukkan level subdivision yang sedang ditampilkan. 

### Balik {#reverse}
Saat berada di level subdivision terendah, tombol reverse akan mencoba membuat level di bawah level saat ini. Perlu dicatat bahwa ini umumnya hanya bisa dilakukan jika objek awalnya dibuat dengan subdivision, misalnya di Nomad atau aplikasi 3D lain yang menggunakan multiresolution subdivision surfaces.

### Subdivisi {#subdivide}
Tombol *Subdivide* akan meningkatkan jumlah poligon sebanyak 4 kali lipat, jadi pastikan untuk memantau polycount karena bisa naik sangat cepat!
Satu aspek penting dari *Subdivision Surface* adalah bahwa ia akan berkumpul menjadi *Smooth Surface*.
Untuk memahami cara kerjanya, Anda bisa mencoba tombol *Subdivide* pada objek dengan hanya beberapa poligon.

Anda bisa menonaktifkan perilaku *Smooth* ini dengan mencentang opsi `Linear subdivision`.

### Hapus level bawah {#delete-lower}
Jika ada subdivision di bawah level yang sedang ditampilkan, hapus level-level tersebut. Jika ini dilakukan tanpa sengaja, Anda bisa membuatnya kembali dengan tombol Reverse.

### Hapus level atas {#delete-higher}
Jika ada subdivision di atas level yang sedang ditampilkan, hapus level-level tersebut.

### Subdivisi linear {#linear-subdivision}
Membagi mesh tanpa menerapkan smoothing.

### Batas tajam {#sharp-border}
Jika objek Anda memiliki facegroup, mengaktifkan opsi ini akan menjaga tepi facegroup tetap tajam. Ini bisa diatur di setiap level subdivision (slider subdivision akan memiliki ikon kecil di atas level untuk menandakan hal ini).

### Pertahankan segitiga {#keep-triangles}
Sebagian besar sistem subdivision surface standar akan mencoba mengonversi semua poligon menjadi quad selama operasi subdivision. Toggle ini akan memaksa subdivision menggunakan segitiga sebagai gantinya.

### Kunci (LV0) {#lock-lv0}

Mencegah level subdivision terendah dimodifikasi. Ini bisa penting jika objek Anda dibuat di aplikasi lain, dan objek dasar harus tetap tidak berubah. Saat opsi ini dinonaktifkan, perubahan besar di level subdivision lebih tinggi akan menggerakkan level 0.

::: tip 

Subdivision akan menghaluskan semua tepi tajam secara default. Untuk menjaga tepi tetap agak tajam, coba gunakan linear subdivision atau Sharp border pada 2 level subdivide pertama, lalu matikan pada level-level yang lebih tinggi. Ini akan menghasilkan mesh subdivide yang semi-tajam.

:::


## ![](/icons/voxel.webp) Voxel Remesher {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Saat menggunakan `Voxel Remesher`, seluruh mesh akan dipaksa memiliki topologi dengan resolusi seragam, artinya semua poligon kurang lebih memiliki ukuran yang sama. Ini sangat berguna ketika Anda tidak ingin memikirkan topologi dan hanya ingin melakukan sculpting bebas.

Alur kerja sculpting yang umum bisa dimulai dengan menggunakan `Voxel Remesher` untuk memblok bentuk kasar dengan resolusi rendah.
Cukup tekan tombol *Remesh* sesekali saat Anda terlalu banyak meregangkan mesh untuk menghindari distorsi berlebihan.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Seperti disebutkan di atas, Nomad adalah perangkat lunak poligonal, tetapi `Voxel Remesher` adalah satu pengecualian di mana pendekatan lain digunakan (sementara) untuk melakukan remeshing.

Satu perbedaan besar adalah bahwa pendekatan voxel tidak menerima self intersection, sehingga hal tersebut akan diselesaikan.
Selain itu, ia tidak mendukung mesh dengan lubang.

Dengan lubang, yang dimaksud bukan `genus hole` (`hole` pada donat), melainkan mesh yang tidak `watertight`/`closed`.
Biasanya, ini berarti sebelum menerapkan remeshing, setiap lubang akan ditutup, mirip dengan [Trim tool](tools.md#trim) atau [fitur Hole filling](scene.md#hole-filling).
:::

### Remesh {#voxel-remesh}
Menjalankan voxel remesh.

### Resolusi {#voxel-resolution}
Ukuran voxel yang digunakan selama perhitungan. Saat mengubah parameter ini pola papan catur akan ditumpangkan pada mesh untuk memberikan pratinjau hasil.

### Bangun multiresolusi {#build-multiresolution}
Membuat level multiresolution yang lebih rendah untuk voxel remesh. Jika Anda menggunakan pola papan catur untuk mengatur resolusi, dan mengatur build multiresolution ke 2, hasil akhir akan memiliki detail yang sesuai dengan slider resolusi, dan jika Anda pergi ke tab multires, levelnya akan di 2, artinya Anda memiliki mesh multires resolusi lebih rendah di level 1 dan level 0. Ini bisa menjadi cara yang baik untuk sekaligus menghasilkan mesh bersih dengan poligon merata, dan memiliki mesh kontrol resolusi rendah.

::: tip Tip: Build multiresolution dan stable smoothing

Opsi ini kadang dapat menyebabkan 'loop' pada geometri yang sulit dihaluskan, menimbulkan bintik-bintik kecil. Jika ini terjadi, aktifkan 'Stable smoothing' di opsi tool smooth. 

:::

### Pertahankan sisi tajam {#keep-sharp-edges}
Mengaktifkan snapping titik-titik baru ke tepi tajam pada mesh asli. Ini bisa menimbulkan distorsi.

## ![](/icons/dynamic.webp) Topologi Dinamis {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Multiresolution dan voxel remeshing adalah metode industri umum untuk mengontrol topologi, tetapi keduanya mengharuskan Anda mengawasi agar poligon tidak terlalu diregangkan atau terlalu dipadatkan. 

Dynamic Topology adalah metode alternatif. Saat Anda memahat, Nomad akan secara adaptif menambah dan menghapus poligon selama sapuan kuas, sehingga mengukir detail kecil akan menambah banyak poligon kecil di area yang Anda butuhkan, dan smoothing di tempat lain akan mengurangi poligon.

Perlu dicatat bahwa dynamic topology akan menggunakan poligon segitiga, bukan quad. Ini bisa terlihat agak berantakan, tetapi hampir lebih baik untuk tidak melihat wireframe, cukup fokus membuat sculpt yang bagus tanpa memikirkan topologi, lalu nanti Anda bisa menggunakan salah satu alat remeshing Nomad lainnya untuk menghasilkan mesh quad yang bersih.

Lihat video di bawah untuk aksinya.

![](/videos/dynamic.mp4)

### Diaktifkan {#enabled}
Mengaktifkan dynamic topology. Ikon DynTopo akan ditempatkan di bawah slider radius dan intensitas kuas untuk memungkinkan Anda mengaktifkan/mematikan Dyntopo per tool.

### Detail {#dyn-detail}
Mengontrol jumlah detail, perilakunya berubah berdasarkan pilihan 'Detail based on...', lihat di bawah.

### Detail berdasarkan... {#detail-based-on}
| Method   | Description                                                     |
| :------: | :-------------------------------------------------------------: |
| Screen   | Tingkat detail akan bergantung pada seberapa besar objek di layar. Slider detail 100% atau lebih tinggi untuk detail halus, menghasilkan segitiga kecil, atau 1% untuk detail rendah, menghasilkan segitiga besar.  |
| Radius   | Radius tool menentukan jumlah detail. Gunakan radius tool kecil untuk detail halus, radius besar untuk detail rendah. Slider detail adalah pengali pada rasio ini.                     |
| Constant | Slider detail menentukan jumlah detail, dan tidak terpengaruh oleh ukuran layar atau ukuran tool.             |

::: tip TIP: Mode Radius

Untuk memahami lebih baik cara kerja mode radius, mulai gerakkan slider detail dengan satu jari, lalu pada saat yang sama ubah radius tool dengan jari lain. Anda akan melihat bagaimana keduanya saling terkait.

:::

### Lebih mengutamakan... {#prefer}
| Method  | Description       |
| :-----: | :---------------: |
| Speed   | Mengutamakan performa |
| Quality | Mengutamakan kualitas |

Saat Anda mengutamakan `Quality`, ada 2 perbedaan utama:
- refinement diterapkan sebelum sculpting, sehingga Anda akan mendapatkan lebih sedikit artefak interpolasi saat mengecat atau memahat detail sangat kecil
- refinement berjalan hingga konvergen ke tingkat detail yang benar, berbeda dengan perilaku inkremental.
 
Dengan demikian, jika Anda memahat detail sangat kecil atau melakukan sapuan cepat, topologi akan selalu diperhalus seperti yang diharapkan


### Gunakan tekanan pada radius {#use-pressure-on-radius}
Hanya relevan jika `Radius` diaktifkan. Saat diaktifkan, tingkat detail akan selalu mencerminkan ukuran kuas, bahkan ketika ukuran kuas dipengaruhi oleh tekanan pensil.

### Gunakan falloff goresan {#use-stroke-falloff}

Juga menyertakan kurva falloff kuas dan alpha dalam perhitungan dyntopo.

### Metode {#method}
Baik Anda menggunakan `Dynamic Topology` pada [Brush](#brush) atau [Secara Global](#global), Anda bisa memilih mode operasinya:

| Method         | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | Dapat menambah dan menghapus face, ini adalah mode yang digunakan di video di atas |
| Subdivision    | Hanya menambah face baru, tidak bisa menghapus face                  |
| Decimation     | Hanya menghapus face, tidak bisa menambah face                       |

### Lindungi area termasker {#protect-masked-area}
Mengaktifkan area yang dimask agar terlindungi dari perubahan topologi.

### Ekstrapolasi vertex {#vertex-extrapolation}


### Detail {#all-detail}
Resolusi yang digunakan untuk operasi remesh. Jika Dyntopo dalam mode 'Constant', nilainya akan sama dengan slider Detail di bagian atas menu ini.

### Remesh {#dyn-remesh}
Menjalankan remesh global menggunakan algoritma dyntopo. Biasanya Anda sebaiknya menggunakan [Voxel Remesher](#voxel-remesher) untuk remeshing penuh.

Namun satu keunggulan dibanding voxel adalah area yang dimask akan terlindungi, sehingga Anda bisa memiliki kontrol lebih baik di mana menempatkan kerapatan lebih banyak atau lebih sedikit.



## ![](/icons/topo_extra.webp) Lainnya {#misc}

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) Menu roda gigi {#gear-menu}
Banyak tool di menu ini memiliki opsi tambahan. Opsi-opsi tersebut dapat diakses melalui ikon gear di sebelah judul bagian.

### Desimasi {#decimation}

![](/images/topology_decimation.webp)

Mengurangi jumlah poligon dengan mencoba mempertahankan sebanyak mungkin detail, menggunakan poligon segitiga.

Fitur ini bisa berguna jika Anda ingin mengekspor untuk pencetakan 3D.
Namun sebaiknya jangan digunakan jika Anda ingin terus memahat di atasnya, karena bisa menghasilkan segitiga yang tidak merata.

Perlu dicatat bahwa area yang dimask tidak akan didecimate.

![](/videos/decimate.mp4)

::: tip

Menggunakan [Quadremesh tool](tools.md#quad-remesher) pada objek high poly bisa memakan waktu lama untuk dihitung, dan memberikan hasil yang sulit dikontrol. Memproses mesh terlebih dahulu dengan [facegroups](tools.md#facegroup-1) dan decimate akan membuat Quadremesh berjalan jauh lebih cepat, dan memungkinkan kontrol topologi yang jauh lebih baik.

* Facegroup mesh untuk mendefinisikan alur quad ideal Anda.
* Facegroup relax untuk mendapatkan tepi facegroup yang halus.
* Decimate. Ini akan memastikan Anda tidak memiliki face tipis atau terdistorsi di tepi facegroup. Di pengaturan decimate pastikan facegroup diaktifkan. Ini akan membuat tepi segitiga mengikuti tepi facegroup Anda dengan tepat.
* Di opsi Quadremesh pastikan relax dinonaktifkan (karena Anda sudah merelaksasi mesh) dan Anda seharusnya mendapatkan hasil yang baik.

:::

#### Desimate {#decimate}
Memulai operasi decimate.

Ikon di sebelah tombol decimate memungkinkan Anda mengaktifkan/mematikan opsi yang memengaruhi decimation. Persentase menunjukkan seberapa kuat opsi tersebut, dan dapat diatur di menu gear lanjutan.

* ![](/icons/palette.webp)  `Preserve Painting` - Menempatkan lebih banyak segitiga di area yang memiliki detail painting.
* ![](/icons/triforce.webp) `Uniform Faces` - Lebih memilih membuat segitiga dengan ukuran seragam.
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - Decimate akan mencoba menjaga tepi dekat geometri terbuka dan lubang tetap tidak berubah.
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - Decimate akan mencoba menjaga tepi facegroup tetap tidak berubah.
* ![](/icons/uv.webp) `Preserve UV Borders` - Decimate akan mencoba menjaga tepi UV tetap tidak berubah.

#### ![](/icons/cog.webp) Menu roda gigi Desimate {#decimate-gear-menu}
Menu gear memiliki opsi lanjutan berikut:
##### Pertahankan pewarnaan {#preserve-painting}
Checkbox akan mengaktifkan/mematikan mode ini, nilainya akan menentukan seberapa akurat detail painting akan dipertahankan. Nilai lebih tinggi akan mempertahankan lebih banyak painting. Atur ke 0 jika Anda tidak peduli dengan painting.


##### Wajah seragam {#uniform-faces}
Checkbox akan mengaktifkan/mematikan mode ini. Nilai lebih tinggi akan menghasilkan segitiga dengan ukuran serupa.

##### Pertahankan batas {#preserve-borders}
Aktifkan untuk mencegah border didecimate. Bobot border dapat dipilih untuk border `Geometry`, `Face Group` atau `UV`.

#### Target segitiga {#target-triangles}
Mengatur target jumlah segitiga. Nilai default adalah 50%, tombol percent/target akan beralih antara persentase atau jumlah poligon target yang pasti.



### UV Unwrap - UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
Menghitung koordinat tekstur (UV) untuk mesh saat ini, umumnya lebih memilih membuat lebih banyak island dengan potongan, untuk meminimalkan distorsi.

Ikon mata kecil di antara judul menu dan menu gear akan mengaktifkan/mematikan pratinjau UV pada objek.

![](/videos/unwrap.mp4)

#### Unwrap {#unwrap}
Menghitung UV untuk objek terpilih, yang akan ditampilkan di latar belakang.

#### Hapus UV {#delete-uvs}
Menghapus UV pada objek.

#### ![](/icons/cog.webp) Menu roda gigi UVAtlas {#uvatlas-gear-menu}
Menu gear memiliki opsi lanjutan berikut:

#### Grup wajah {#atlas-face-group}

Gunakan facegroup untuk mendefinisikan potongan UV.

##### Regangan maks {#max-stretch}
Nilai rendah menghasilkan distorsi lebih sedikit dan lebih banyak island, nilai tinggi menghasilkan distorsi lebih banyak dan lebih sedikit island. 

##### Jarak antar pulau {#island-spacing}
Jumlah jarak antar island. Nilai rendah akan mengurangi ruang terbuang, tetapi berisiko tekstur saling bocor antar island. 

::: warning
Menghitung UV bisa memakan waktu, sebaiknya gunakan mesh dengan kurang dari 100k vertex.
:::

::: tip UVs?
Analogi umum untuk UV adalah membungkus kado; apa cara terbaik memotong kertas kado untuk sepenuhnya menutupi objek, tanpa tumpang tindih? 

UV mirip, tetapi alih-alih memotong kertas, Anda memotong objek. Bayangkan jika model Anda terbuat dari plastik tipis, bagaimana Anda akan memotong model tersebut untuk dibentangkan rata, mengecatnya dalam keadaan rata, lalu merakitnya kembali?

Sekarang bayangkan permukaan model Anda terbuat dari lycra elastis. Anda bisa meregangkan model hingga rata, atau memotongnya, atau kombinasi keduanya. Tetapi jika Anda mengecat pola papan catur pada objek saat diratakan, pola itu akan terdistorsi saat Anda merakitnya kembali. Mana metode yang lebih baik, lebih banyak potongan dengan distorsi lebih sedikit, atau lebih sedikit potongan dengan distorsi lebih banyak?

UV adalah instruksi untuk memberi tahu perangkat lunak 3D bagaimana 'memotong dan meregangkan' objek saat menerapkan tekstur. Tool UV Atlas umumnya menggunakan pendekatan 'lebih banyak potongan, distorsi lebih sedikit'.


:::

::: tip UV di Nomad dan aplikasi lain

Sebagian besar model bertekstur yang Anda temukan online akan diberi tekstur dengan UV. Nomad dapat mengimpor dan menampilkannya melalui panel [material](material#textures).

Saat model dibuat di Nomad, Anda bisa mengecat langsung pada objek tanpa UV. Jika Anda perlu mengekspornya ke aplikasi lain, misalnya [Procreate](https://procreate.art/), Anda bisa 'membake' informasi warna Nomad ke dalam tekstur melalui UV. 

:::

### UV Unwrap - BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

UV BFF lebih mengutamakan pendekatan 'lebih sedikit potongan, distorsi lebih banyak'. 

#### ![](/icons/cog.webp) Menu roda gigi UV BFF {#uv-bff-gear-menu}

#### Grup wajah {#bff-face-group}

Gunakan facegroup untuk mendefinisikan potongan UV.

##### Jumlah kerucut {#cone-count}
Menentukan jumlah proyeksi utama yang digunakan. Nilai lebih rendah akan menghasilkan lebih sedikit island, tetapi distorsi lebih banyak.

##### Patch tanpa jahitan {#seamless-patches}
Mempengaruhi tata letak patch UV, bekerja paling baik dengan facegroup yang dibuat dengan hati-hati.

### Bake -> tekstur {#bake-texture}
![](/images/topology_bake_menu.webp)

Texture baking akan membuat tekstur dengan memproyeksikan objek lain yang terlihat di scene ke dalam UV objek terpilih.

Berikut alur kerja tipikal untuk baking:
- Anda memiliki mesh dengan detail halus dan painting
- Clone mesh tersebut
- Decimate (atur `Preserve painting` ke 0)
- UV unwrap
- Bake!

Secara default Nomad akan mempertimbangkan setiap mesh yang terlihat di scene.
Anda juga bisa menggunakan mode Solo untuk dengan cepat menyembunyikan sebagian besar mesh lain.
Jika tidak ada objek lain yang terlihat, maka seluruh scene akan dipertimbangkan.

Sekarang Anda seharusnya memiliki mesh resolusi rendah yang mempertahankan sebagian besar cat dan detail dari objek sebelumnya.

Setelah operasi, warna vertex akan dipindahkan ke layer baru yang dinonaktifkan, sehingga tidak mengganggu tekstur.

#### Dari dirinya sendiri {#tex-from-itself}
Membake level multiresolution tertinggi ke level terendah pada objek saat ini. Ini mudah diatur, tetapi sering kali Anda memerlukan kontrol lebih, dalam hal ini opsi berikutnya lebih berguna.

#### Dari resolusi tinggi () {#tex-from-high-res}
Membake dari objek lain yang terlihat di scene ke objek terpilih. Angka dalam tanda kurung menunjukkan jumlah objek lain yang terlihat yang akan digunakan sebagai target high-res, dan dibake ke objek low-res saat ini dengan UV. Objek lain tidak perlu memiliki layout atau topologi yang mirip dengan objek yang dibake, memungkinkan alur kerja bake yang fleksibel.

#### Resolusi {#tex-bake-resolution}
Resolusi tekstur hasil bake. Tekstur bake selalu persegi, jadi 1024 akan membuat gambar 1024x1024. 

Tombol di bawah adalah shortcut untuk resolusi yang umum digunakan. Sebagai referensi, 512x512 relatif kecil, misalnya untuk grafis web dan geometri sederhana. 4096x4096 (disingkat 4k) untuk render berkualitas tinggi.

#### ![](/icons/cog.webp) Menu roda gigi Bake {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Menu gear memiliki opsi lanjutan berikut:

##### Normal, Roughness, Metalness, Color, Emissive, Opacity {#tex-normal-roughness-metalness-color-emissive-opacity}
Checkbox ini menentukan properti mana yang akan dibake, masing-masing ke dalam map terpisah. Setelah bake selesai, map ini akan ditambahkan sebagai tekstur ke material objek saat ini.

##### Cadangan {#tex-backup}
Untuk mempratinjau tekstur hasil bake, informasi paint objek harus dinonaktifkan. Opsi ini akan memindahkan informasi paint ke layer baru sebagai cadangan sehingga bisa dengan mudah diaktifkan/nonaktifkan.

#### Radius sangkar {#tex-cage-radius}
Mengatur seberapa jauh dari objek bake sinar dikirim untuk mencari objek target. Secara default jarak ini dijaga tetap rendah untuk menghindari artefak, tetapi bisa ditingkatkan jika objek target jauh dari objek bake.

##### Offset sinar {#tex-ray-offset}
Mengatur dari mana perhitungan bake dimulai pada objek bake. Secara default dimulai 5% dari permukaan, yang menghindari sebagian besar artefak umum. Jika objek target sangat jauh dari objek bake, offset ini mungkin perlu ditingkatkan.


### Proyeksi ulang ke vertex {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Memproyeksikan detail sculpt, painting, layer, tekstur ke nilai vertex.

Ini bisa dianggap sebagai kebalikan dari baking; jika baking mentransfer properti vertex ke tekstur, reproject mentransfer tekstur (dan properti lain)
 kembali ke vertex.

::: tip
Saat menggunakan `Bake to texture` atau `Reproject to vertex`, baik warna vertex maupun tekstur material akan diperhitungkan.
:::

#### Dari dirinya sendiri {#vertex-from-itself}
Mengonversi tekstur dari material menjadi nilai vertex. Tombol ini hanya aktif jika objek memiliki UV, dan tekstur aktif di material.

::: tip TIP: Texture painting
Nomad tidak secara langsung mendukung painting dan pengeditan tekstur, tetapi hasil yang sangat mirip dapat dicapai dengan memproyeksikan tekstur -> nilai vertex, mengecat pada vertex, lalu membake vertex -> tekstur:

1. Siapkan objek low poly dengan UV
1. Muat tekstur ke dalam materialnya
1. Subdivide secukupnya untuk bisa mengecat
1. `Reproject to vertex` dalam mode `From itself`, sekarang tekstur telah dikonversi ke nilai vertex
1. Cat, haluskan, smudge, stamp, lakukan edit apa pun yang Anda perlukan
1. `Bake to texture`, dalam mode `From itself`. Edit tersebut dikonversi kembali menjadi tekstur.
:::

#### Dari resolusi tinggi () {#vertex-from-high-res}
Mengonversi objek apa pun yang terlihat menjadi nilai vertex pada objek terpilih. Angka pada tombol ini menunjukkan jumlah objek yang terlihat.

::: tip
Reproject objek lain dapat digunakan bukan hanya untuk mentransfer informasi warna dari objek lain, tetapi juga untuk memproyeksikan vertex ke objek lain, misalnya perban dapat diproyeksikan ke karakter.
:::

#### ![](/icons/cog.webp) Menu roda gigi Reproject {#vertex-reproject-gear-menu}
Menu gear memiliki opsi lanjutan berikut:

#### Vertex, Roughness, Metalness, Color, Opacity, Opacity->Mask, Mask, Layers, Face Group {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Checkbox ini menentukan properti mana yang akan diproyeksikan ke objek terpilih. 

#### Relaksasi {#vertex-relax}
Mesh terpilih dapat dihaluskan atau direlaksasi tata letaknya sejumlah tertentu agar lebih cocok dengan target reprojection. Smooth lebih baik untuk mesh high poly. Relax lebih baik untuk mesh low poly. Auto akan membiarkan Nomad menentukan metode terbaik.

#### Iterasi {#vertex-iterations}
Berapa kali operasi relax harus diterapkan selama reprojection.

#### Radius sangkar {#vertex-cage-radius}
Mengatur seberapa jauh dari objek terpilih sinar dikirim untuk mencari objek target. Secara default jarak ini dijaga tetap rendah untuk menghindari artefak, tetapi bisa ditingkatkan jika objek target jauh dari objek bake.

#### Bias sinar {#vertex-ray-bias}
Nilai lebih rendah akan lebih mengutamakan proyeksi ke titik terdekat pada permukaan target. Nilai lebih tinggi akan lebih mengutamakan titik perpotongan menggunakan normal permukaan. 

#### Offset sinar {#ray-vertex-offset}
Mengatur dari mana perhitungan bake dimulai pada objek terpilih. Secara default dimulai 5% dari permukaan, yang menghindari artefak tertentu. Jika objek target sangat jauh dari objek bake, offset ini mungkin perlu ditingkatkan.


### Quad Remesh - Instan {#quad-remesh-instant}
![](/images/topology_quadremesh_menu.webp)
Remesh menggunakan [algoritma Instant Meshes oleh Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Algoritma ini akan menganalisis alur mesh dan membuat topologi quad yang bersih.

::: tip
Di iOS dan desktop, tool [Quad remesher](tools#quad-remesher) memberikan hasil yang lebih baik dan kontrol lebih.
:::

#### Remesh {#instant-remesh}
Memulai operasi instant meshes.

#### Target quad {#target-quads}
Jumlah poligon quad yang akan diupayakan dibuat oleh quad remesh.

#### ![](/icons/cog.webp) Menu roda gigi Quad Remesh Instan {#quad-remesh-instant-gear-menu}
Menu gear memiliki opsi lanjutan berikut:

##### Sudut crease {#crease-angle}
Ambang sudut tajam yang akan membantu memandu operasi remesh.

#### Isi lubang maks {#max-fill-hole}
Algoritma kadang dapat menghasilkan lubang yang tidak diinginkan. Jika lubang memiliki jumlah vertex lebih sedikit dari nilai ini, maka lubang akan diisi.

### Lubang {#holes}
![](/images/topology_holes_menu.webp)
Sebagian besar waktu, objek Anda mungkin watertight, artinya mesh 'tertutup'.

Jika objek Anda memiliki lubang, Anda bisa mengisinya. Perlu dicatat bahwa ini hanya berfungsi pada lubang 'naif', sehingga tidak dapat 'mengelas' dua border terpisah.

![](/videos/hole_filling.mp4)

::: tip
Saat Anda menjalankan Voxel remesher, semua lubang akan otomatis ditutup, baik Anda menggunakannya pada 1 atau beberapa mesh.
:::

#### Tutup lubang {#close-holes}
Menjalankan aksi penutupan lubang.

#### ![](/icons/cog.webp) Menu roda gigi Lubang {#holes-gear-menu}
Menu gear memiliki opsi lanjutan berikut:

##### Detail {#fill-detail}
Kerapatan poligon yang digunakan untuk mengisi lubang. Saat menggeser slider ini pola papan catur akan ditampilkan pada model, ini akan memberikan indikasi ukuran segitiga yang digunakan. Checkbox akan menonaktifkan ini, dan hanya menggunakan titik yang ada, yang biasanya akan membuat segitiga panjang dan tipis di atas lubang, yang bisa sulit dipahat.

##### Isi non-manifold {#fill-non-manifold}
Mencoba mengisi lubang non-manifold.

##### Grup wajah {#fill-face-group}

Saat mengisi lubang, apakah setiap lubang mendapatkan facegroup sendiri (Auto), atau semuanya berbagi satu facegroup (Off), atau tidak membuat facegroup (On).

### Paksa manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Mencoba membersihkan edge non-manifold. Ini bisa berguna untuk perangkat lunak eksternal yang tidak mendukung edge dengan lebih dari 2 face yang berbagi.

#### Bersihkan {#clean}
Menjalankan aksi clean.
#### ![](/icons/cog.webp) Menu roda gigi Paksa manifold {#force-manifold-gear-menu}
Menu gear memiliki opsi lanjutan berikut:

#### Hapus wajah kecil {#delete-small-faces}
Ambang yang digunakan untuk menghapus dan menggabungkan poligon kecil.


### Triplanar {#triplanar}
![](/images/topology_triplanar_menu.webp)
Mengonversi mesh menjadi primitive [triplanar](scene.md#triplanar).
Anda kemungkinan akan kehilangan banyak detail dalam proses ini.

#### Paksa kubik {#force-cubic}
Memaksa triplanar menjadi kubus. Jika tidak, triplanar akan menyesuaikan dengan bounding box terdekat di sekitar objek Anda.

#### Konversi {#convert}
Menjalankan aksi triplanar.

#### Resolusi {#triplanar-resolution}
Ukuran voxel yang digunakan dalam operasi triplanar.

## ![](/icons/dot.webp) Primitif {#primitive}
Parameter untuk primitive terpilih. Ini juga tersedia di toolbar viewport primitive.

![](/images/topology_primitive_screenshot.webp)