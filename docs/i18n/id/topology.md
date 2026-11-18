# ![](/icons/multires.webp) Topologi {#topology}

Menu ini mengatur topologi objek di Nomad, dan juga berisi alat untuk melakukan bake serta memindahkan detail antar objek, dan antar tekstur.

![](/images/topology_overview.webp)

Nomad bekerja dengan poligon: geometri disusun dari segitiga dan kuad.
Yang kami maksud dengan topologi adalah jumlah face, tetapi juga cara titik-titik (verteks) saling terhubung.

Penting untuk selalu memperhatikan topologi, terutama jika Anda ingin memahat atau mewarnai detail halus.

::: tip Bagaimana cara memantau topologi Anda?
Anda bisa menampilkan [Kerangka kawat](settings.md#wireframe) atau cukup menonaktifkan [Shading halus](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Menu topologi Nomad punya beberapa tab, tersusun dalam dua baris:

| Metode                                | Ikon                         | Deskripsi                                                        |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolusi](#multiresolution)     | ![](/icons/multires.webp)   | Mengedit beberapa level detail dengan subdivisi                  |
| [Remesh voxel](#voxel-remesher)       | ![](/icons/voxel.webp)      | Menghitung ulang topologi baru dengan kepadatan yang seragam     |
| [Topologi dinamis](#dynamic-topology) | ![](/icons/dynamic.webp)    | Menambah/menghapus face secara lokal dan real-time saat memahat atau mewarnai |
| [Lainnya](#misc)                      | ![](/icons/topo_extra.webp) | Menutup lubang, memaksa manifold, dan mengonversi ke triplanar   |
| [Primitif](#primitive)                | ![](/icons/dot.webp)        | Opsi primitif                                                    |
| [Desimasi](#decimation)               | ![](/icons/decimate.webp)      | Mengurangi jumlah face sambil mempertahankan bentuk           |
| [Remesh Kuad](#quad-remesh)           | ![](/icons/quad.webp)       | Menyusun ulang objek dengan tata letak kuad yang rapi            |
| [Unwrap UV](#uv-unwrap)               | ![](/icons/uv.webp)         | Membuat UV untuk tekstur                                         |
| [Bake](#bake)                         | ![](/icons/bake.webp)       | Melakukan bake detail dan cat ke tekstur, verteks, atau stempel VDM |


## Statistik poligon {#polygon-stats}

![](/images/topology_stats.webp)

Bagian atas setiap tab menampilkan jumlah poligon untuk objek yang dipilih, dan untuk seluruh adegan jika ada lebih dari satu objek. Kolom-kolomnya adalah jumlah verteks, segitiga, kuad (poligon bersisi 4), dan koordinat UV (0 jika objek tidak punya UV).

Ketuk bagian ini untuk melihat daftar semua objek di adegan beserta jumlah pastinya, termasuk jumlah grup face masing-masing.

## ![](/icons/cog.webp) Menu roda gigi {#gear-menu}
Beberapa bagian, seperti yang ada di tab [Remesh Kuad](#quad-remesh) dan [Bake](#bake), punya opsi tambahan. Buka opsi tersebut dengan ikon roda gigi di samping judul bagian.

## ![](/icons/multires.webp) Multiresolusi {#multiresolution}

![](/images/topology_multires_menu.webp)

### Apa itu multiresolusi? {#what-is-multiresolution}
Fitur multiresolusi berguna untuk dua skenario utama:
- Algoritma subdivisi halus untuk menambah jumlah poligon objek Anda
- Mengelola beberapa level resolusi sehingga Anda bisa berganti antara edit skala kecil dan skala besar

![](/videos/multiresolution.mp4)

#### Alur kerja multiresolusi {#multiresolution-workflow}
Salah satu keunggulan penting multiresolusi adalah Anda bisa kembali ke resolusi yang lebih rendah, mengubah objek, lalu kembali ke resolusi tertinggi tanpa kehilangan detail resolusi tingginya. Semua detail resolusi tinggi akan diproyeksikan secara otomatis.

[Lapisan](layers.md#layers) tersedia di setiap resolusi.

::: warning
Jika Anda menggunakan alat yang mengubah topologi objek, semua resolusi lain dari objek tersebut akan hilang!
Anda seharusnya selalu mendapat peringatan sebelum hal ini terjadi, misalnya saat menggunakan:
- [Remesh voxel](#voxel-remesher)
- [Topologi dinamis](#dynamic-topology)
- [Alat Pangkas](tools.md#trim)
- [Alat Pisah](tools.md#split)
:::


### Penggeser multiresolusi {#multiresolution-slider}
Penggeser ini menunjukkan jumlah level subdivisi pada objek saat ini. Jika ada 6 batang vertikal, berarti ada 6 level subdivisi. Lingkaran menandai level subdivisi yang sedang ditampilkan.

Ikon kecil di atas penggeser menunjukkan opsi mana (`Kunci level 0`, `Linear`, `Batas tajam`, `Pertahankan segitiga`) yang dipakai untuk setiap level.

### Balikkan {#reverse}
Saat berada di level subdivisi terendah, tombol balikkan akan mencoba membuat level di bawah level saat ini. Perlu diingat bahwa ini umumnya hanya berhasil jika objek memang dibuat dengan subdivisi sejak awal, misalnya di Nomad atau di aplikasi 3d lain yang mendukung permukaan subdivisi multiresolusi.

### Subdivisi {#subdivide}
Tombol *Subdivisi* akan melipatgandakan jumlah poligon sebanyak 4 kali, jadi selalu perhatikan jumlah poligonnya karena bisa naik dengan sangat cepat! Nomad akan meminta konfirmasi jika hasilnya akan sangat berat.
Hal penting dari *Permukaan Subdivisi* adalah bentuknya akan mendekati *Permukaan Halus*.
Untuk memahami cara kerjanya, coba tekan tombol *Subdivisi* pada objek yang hanya punya sedikit poligon.

Anda bisa menonaktifkan perilaku *Halus* ini dengan opsi `Linear`.

### Hapus lebih rendah {#delete-lower}
Jika ada level subdivisi di bawah level yang sedang ditampilkan, hapus semuanya. Jika Anda tidak sengaja melakukannya, Anda bisa membuatnya kembali dengan tombol Balikkan.

### Hapus lebih tinggi {#delete-higher}
Jika ada level subdivisi di atas level yang sedang ditampilkan, hapus semuanya.

### ![](/icons/lock.webp) Kunci level 0 {#lock-lv0}
Mempertahankan bentuk level subdivisi terendah saat Anda memahat di level yang lebih tinggi. Cat tetap diteruskan sampai ke level 0. Ini bisa penting jika objek Anda dibuat di aplikasi lain dan objek dasarnya harus tetap tidak berubah.

Opsi ini hanya tersedia sebelum subdivisi pertama. Jika nonaktif, perubahan besar di level subdivisi yang lebih tinggi akan menggeser level 0.

### ![](/icons/linear.webp) Linear {#linear-subdivision}
Membagi mesh tanpa menerapkan penghalusan apa pun.

### ![](/icons/group.webp) Batas tajam {#sharp-border}
Jika objek Anda punya grup face, mengaktifkan opsi ini akan menjaga batas grup face tetap tajam. Opsi ini bisa diatur di setiap level subdivisi (penggeser subdivisi akan menampilkan ikon kecil di atas level tersebut sebagai penanda).

### ![](/icons/triangle.webp) Pertahankan segitiga {#keep-triangles}
Sebagian besar sistem permukaan subdivisi standar akan mencoba mengubah semua poligon menjadi kuad saat subdivisi. Opsi ini memaksa subdivisi untuk tetap memakai segitiga.

::: tip

Secara bawaan, subdivisi akan menghaluskan semua tepi tajam. Agar tepi tetap sedikit tajam, coba gunakan `Linear` atau `Batas tajam` pada 2 level subdivisi pertama, lalu matikan untuk level yang lebih tinggi. Hasilnya adalah mesh tersubdivisi yang semi-tajam.

:::

### Tampilkan level tertinggi {#show-highest-level}
Menampilkan level tertinggi dengan semua detailnya selagi Anda memahat di level yang lebih rendah. Praktis untuk melihat hasil akhir saat Anda membuat perubahan besar.

### Kerangka kawat: Hanya level 0 {#wireframe-level-0-only}
Saat [Kerangka kawat](settings.md#wireframe) aktif, hanya tampilkan kerangka kawat level terendah. Kerangka kawat yang rapat dari level tinggi bisa menutupi bentuk objek.


## ![](/icons/voxel.webp) Remesh voxel {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Saat menggunakan `Remesh voxel`, seluruh mesh dipaksa memiliki topologi dengan resolusi seragam, artinya semua poligon berukuran kurang lebih sama. Ini sangat berguna saat Anda tidak ingin memikirkan topologi dan hanya ingin memahat secara bebas.

Alur kerja memahat yang umum bisa dimulai dengan `Remesh voxel` untuk membuat bentuk kasar (block-out) dengan resolusi rendah.
Cukup tekan tombol *Remesh* sesekali, saat mesh mulai terlalu meregang, untuk menghindari distorsi berlebihan.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Seperti disebutkan di atas, Nomad adalah perangkat lunak berbasis poligon, tetapi `Remesh voxel` adalah satu pengecualian yang (untuk sementara) memakai pendekatan lain untuk melakukan remesh.

Satu perbedaan besarnya, pendekatan voxel tidak menerima perpotongan dengan dirinya sendiri, jadi bagian yang saling tembus akan diselesaikan.
Selain itu, pendekatan ini tidak mendukung mesh yang berlubang.

Yang kami maksud dengan lubang bukan `genus hole` (`lubang` pada donat), melainkan mesh yang tidak `kedap air`/`tertutup`.
Biasanya ini berarti sebelum remesh diterapkan, semua lubang akan diisi, mirip dengan [Alat Pangkas](tools.md#trim) atau [fitur pengisian lubang](#holes). Opsi [Lubang](#voxel-holes) di bawah menentukan caranya.
:::

### ![](/icons/voxel.webp) Remesh {#voxel-remesh}
Menjalankan remesh voxel. Ikon kecil pada tombol mengingatkan Anda opsi mana saja di bawah ini yang sedang aktif.

### Resolusi {#voxel-resolution}
Ukuran voxel yang dipakai dalam perhitungan; nilai lebih tinggi memberi lebih banyak detail. Saat Anda mengubah parameter ini, pola papan catur akan ditampilkan di atas mesh sebagai pratinjau hasilnya.

Pipet mengambil resolusi dari kepadatan mesh di tempat yang Anda ketuk. Tombol kubus di sebelahnya mengubah nilai menjadi `Panjang tepi` dalam satuan dunia: nilai yang sama lalu memberi detail yang sama pada objek apa pun.

### Bangun multiresolusi {#build-multiresolution}
Membuat level multiresolusi yang lebih rendah untuk hasil remesh voxel. Jika Anda memakai pola papan catur untuk menentukan resolusi, lalu mengatur bangun multiresolusi ke 2, hasil akhirnya akan punya detail sesuai penggeser resolusi, dan jika Anda membuka tab multires, mesh akan berada di level 2, artinya Anda punya mesh multires beresolusi lebih rendah di level 1 dan level 0. Ini cara yang bagus untuk mendapatkan mesh yang rapi dengan poligon merata sekaligus mesh kontrol beresolusi rendah.

Opsi ini juga berjalan lebih cepat dan memakai lebih sedikit memori pada resolusi tinggi. Tetapi dengan resolusi rendah dan banyak level, Anda akan kehilangan detail.

::: tip Tips: Bangun multiresolusi dan penghalusan stabil

Opsi ini terkadang bisa menimbulkan 'loop' pada geometri yang sulit dihaluskan, sehingga muncul bintil-bintil kecil. Jika ini terjadi, aktifkan 'Pelembutan stabil' di opsi alat Haluskan.

:::

### Pertebal bagian tipis {#thicken-thin-parts}
Bagian yang lebih tipis dari voxel bisa patah atau hilang saat remesh. Opsi ini mempertebalnya agar tetap ada; nilai lebih tinggi mempertebal lebih banyak. Opsi ini tidak tersedia bersama `Tepi tajam` atau `Batas tajam`.

### Lubang {#voxel-holes}
Cara lubang ditutup sebelum remesh:

* `Isi` - Setiap lubang ditutup sendiri-sendiri, dari tepinya.
* `Bentuk` - Lubang ditutup dengan mengikuti permukaan di sekitarnya, dan bagian terbuka yang saling tumpang tindih digabungkan.

### ![](/icons/angle.webp) Tepi tajam {#keep-sharp-edges}
Menempelkan titik-titik baru ke tepi tajam mesh asli. Ini paling berguna untuk operasi boolean sederhana pada primitif, dan bisa menimbulkan distorsi.

### ![](/icons/group.webp) Batas tajam {#voxel-sharp-border}
Face baru mengikuti batas grup face, dan batas tetap tajam di tempat permukaan membentuk lipatan di sepanjangnya.

### ![](/icons/group_separate.webp) Pisahkan grup {#keep-groups-separate}
Setiap grup face di-remesh sendiri-sendiri: grup tidak pernah bergabung, dan masing-masing tetap menjadi bagian tertutup dalam grupnya sendiri. Multiresolusi tidak dibangun dalam mode ini. Opsi ini tersedia jika objek punya beberapa grup face.

## ![](/icons/dynamic.webp) Topologi dinamis {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Multiresolusi dan remesh voxel adalah metode umum di industri untuk mengontrol topologi, tetapi keduanya mengharuskan Anda berhati-hati agar poligon tidak terlalu meregang atau terlalu berdesakan.

Topologi dinamis adalah metode alternatif. Saat Anda memahat, Nomad akan menambah dan menghapus poligon secara adaptif selama sapuan kuas, sehingga mengukir detail kecil akan menambah banyak poligon kecil di tempat yang Anda butuhkan, dan menghaluskan di tempat lain akan mengurangi poligon.

Perlu diingat bahwa topologi dinamis memakai poligon segitiga, bukan kuad. Hasilnya bisa tampak agak berantakan, tetapi sebaiknya jangan terlalu memperhatikan kerangka kawatnya: fokus saja membuat pahatan yang bagus tanpa memikirkan topologi, lalu nanti Anda bisa memakai salah satu alat remesh Nomad lainnya untuk membuat mesh kuad yang rapi.

Lihat cara kerjanya di video di bawah ini.

![](/videos/dynamic.mp4)

### Diaktifkan {#enabled}
Mengaktifkan topologi dinamis. Ikon DynTopo akan muncul di bawah penggeser radius dan intensitas kuas, sehingga Anda bisa menyalakan atau mematikan DynTopo per alat. Fitur ini bisa cukup berpengaruh pada performa, dan lapisan tetap diperbarui dengan benar.

### Detail {#dyn-detail}
Mengatur jumlah detail; perilakunya bergantung pada pilihan 'Detail berdasarkan...', lihat di bawah. Dalam mode `Layar`, labelnya menunjukkan ukuran segitiga target dalam piksel. Dalam mode `Konstan`, pipet memungkinkan Anda mengambil detail dari kepadatan mesh di tempat yang Anda ketuk.

### Detail berdasarkan... {#detail-based-on}
| Metode   | Deskripsi                                                       |
| :------: | :-------------------------------------------------------------: |
| Layar    | Level detail bergantung pada seberapa besar objek tampil di layar. Penggeser detail di 100% atau lebih untuk detail halus, menghasilkan segitiga kecil, atau 1% untuk detail rendah, menghasilkan segitiga besar.  |
| Radius   | Radius alat menentukan jumlah detail. Gunakan radius alat kecil untuk detail halus, dan radius besar untuk detail rendah. Penggeser detail menjadi pengali untuk rasio ini.                     |
| Konstan  | Penggeser detail menentukan jumlah detail, dan tidak dipengaruhi ukuran layar maupun ukuran alat. Nilainya sama dengan penggeser [Detail](#all-detail) pada `Remesh`.             |

::: tip TIPS: Mode radius

Agar lebih memahami cara kerja mode radius, mulailah menggeser penggeser detail dengan satu jari, lalu pada saat yang sama ubah radius alat dengan jari lain. Anda akan melihat bagaimana keduanya saling terhubung.

:::

### Lebih mengutamakan... {#prefer}
| Metode    | Deskripsi                 |
| :-------: | :-----------------------: |
| Kecepatan | Mengutamakan performa     |
| Kualitas  | Mengutamakan kualitas     |

Jika Anda mengutamakan `Kualitas`, ada 2 perbedaan utama:
- penyempurnaan diterapkan sebelum memahat, sehingga artefak interpolasi berkurang saat mewarnai atau memahat detail yang sangat kecil
- penyempurnaan terus berjalan sampai mencapai level detail yang tepat, bukan bertahap sedikit demi sedikit.
 
Dengan begitu, jika Anda memahat detail yang sangat kecil atau membuat sapuan cepat, topologi akan selalu disempurnakan sesuai harapan.


### ![](/icons/pressure.webp) Gunakan tekanan pada radius {#use-pressure-on-radius}
Hanya relevan jika `Radius` aktif. Jika diaktifkan, level detail akan selalu mengikuti ukuran kuas, bahkan saat ukuran kuas dipengaruhi tekanan pena.

### Gunakan penurunan sapuan {#use-stroke-falloff}

Ikut memperhitungkan kurva falloff dan alpha kuas dalam perhitungan dyntopo.

### Metode {#method}
Memilih cara topologi dinamis mengubah mesh, baik saat Anda memahat maupun saat Anda memakai [Remesh](#dyn-remesh):

| Metode         | Deskripsi                                                             |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisasi   | Bisa menambah dan menghapus face; mode inilah yang dipakai di video di atas |
| Subdivisi      | Hanya menambah face baru, tidak bisa menghapus face                   |
| Desimasi       | Hanya menghapus face, tidak bisa menambah face baru                   |

### ![](/icons/shield.webp) Lindungi area yang dimasker {#protect-masked-area}
Melindungi topologi di area yang di-mask agar tidak berubah.

### ![](/icons/normal.webp) Ekstrapolasi Vertex {#vertex-extrapolation}
Menempatkan titik-titik pada permukaan halus yang mengikuti kelengkungan di sekitarnya, bukan rata di atas face yang sudah ada.

### Detail {#all-detail}
Resolusi yang dipakai untuk operasi remesh. Jika Dyntopo dalam mode 'Konstan', nilainya sama dengan penggeser Detail di bagian atas menu ini. Pipet mengambil detail dari kepadatan mesh di tempat yang Anda ketuk.

### Remesh {#dyn-remesh}
Menjalankan remesh menyeluruh dengan algoritma dyntopo. Biasanya Anda sebaiknya memakai [Remesh voxel](#voxel-remesher) untuk remesh penuh.

Namun, satu keunggulannya dibanding voxel adalah mesh tidak harus tertutup, dan area yang di-mask akan dilindungi, sehingga Anda bisa lebih mengontrol di mana kepadatan ditambah atau dikurangi.



## ![](/icons/topo_extra.webp) Lainnya {#misc}

![](/images/topology_misc_menu.webp)

Tab ini mengumpulkan alat untuk membersihkan atau mengonversi mesh: menutup lubangnya, memaksanya menjadi manifold, atau mengubahnya menjadi triplanar.

### ![](/icons/hole.webp) Lubang {#holes}
![](/images/topology_holes_menu.webp)
Biasanya objek Anda sudah kedap air, artinya mesh-nya 'tertutup'.

Jika objek Anda punya lubang, Anda bisa mengisinya.

![](/videos/hole_filling.mp4)

::: tip
Saat Anda menjalankan remesh voxel, semua lubang otomatis ditutup, baik Anda memakainya pada 1 maupun beberapa mesh.
:::

#### Tutup lubang {#close-holes}
Menjalankan aksi penutupan lubang.

#### Opsi {#holes-gear-menu}
Opsi-opsi ini mengubah cara lubang diisi:

##### Grup Face {#fill-face-group}
Memilih grup face untuk face baru:

* `Campuran` - Lubang yang dikelilingi satu grup face memakai grup itu lagi, lubang yang menyentuh beberapa grup mendapat grup baru.
* `Baru` - Lubang yang diisi mendapat grup face baru.
* `Gunakan ulang` - Setiap lubang memakai grup face yang paling banyak mengelilinginya.

##### Rincian {#fill-detail}
Kepadatan poligon yang dipakai untuk mengisi lubang. Saat Anda menggeser penggeser ini, pola papan catur akan ditampilkan di model sebagai gambaran ukuran segitiga yang akan dipakai. Kotak centang akan menonaktifkannya dan hanya memakai titik-titik yang sudah ada, yang biasanya menghasilkan segitiga panjang dan tipis di atas lubang, yang bisa sulit dipahat.

##### Jembatan {#fill-non-manifold}
Mengisi lubang beserta pulau-pulau di dalamnya sebagai satu permukaan, bukan mengisi setiap tepi sendiri-sendiri. Sudut yang lebih besar bisa menjembatani lubang yang lebih melengkung. Kotak centang menonaktifkannya.

### ![](/icons/cog.webp) Paksa manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Mencoba membersihkan tepi non-manifold. Ini bisa berguna untuk perangkat lunak lain yang tidak mendukung tepi yang dimiliki bersama oleh lebih dari 2 face.

#### Bersihkan {#clean}
Menjalankan aksi pembersihan.

#### Opsi {#force-manifold-gear-menu}
Opsi ini mengubah cara mesh dibersihkan:

##### Hapus face kecil {#delete-small-faces}
Ambang batas untuk menghapus dan menggabungkan poligon kecil. Aktifkan dengan kotak centangnya.


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
![](/images/topology_triplanar_menu.webp)
Mengonversi mesh menjadi primitif [triplanar](scene.md#triplanar).
Kemungkinan besar Anda akan kehilangan banyak detail dalam prosesnya: lapisan, cat, dan multiresolusi juga hilang.

#### Paksa kubik {#force-cubic}
Membuat triplanar berbentuk kubus. Jika tidak, triplanar akan menyesuaikan diri dengan kotak pembatas terdekat di sekitar objek Anda.

#### Konversi {#convert}
Menjalankan aksi triplanar.

#### Resolusi {#triplanar-resolution}
Resolusi grid triplanar; nilai lebih tinggi mempertahankan lebih banyak detail.

## ![](/icons/decimate.webp) Desimasi {#decimation}

![](/images/topology_decimation.webp)

Mengurangi jumlah poligon sambil berusaha mempertahankan detail sebanyak mungkin, dengan poligon segitiga.

Fitur ini bisa berguna jika Anda ingin mengekspor untuk cetak 3d.
Namun sebaiknya jangan dipakai jika Anda masih ingin melanjutkan memahat, karena bisa menghasilkan segitiga yang tidak merata.

Perlu diingat bahwa area yang di-mask tidak akan didesimasi.

![](/videos/decimate.mp4)

::: tip

Memakai [alat Quad Remesher](tools.md#quad-remesher) pada objek high poly bisa memakan waktu lama dan memberi hasil yang sulit dikendalikan. Memproses mesh terlebih dahulu dengan [grup face](tools.md#facegroup) dan desimasi akan membuat Quad Remesher berjalan jauh lebih cepat, dan memberi kontrol yang jauh lebih baik atas topologi.

* Beri grup face pada mesh untuk menentukan alur kuad yang ideal.
* Gunakan relax grup face agar batas grup face menjadi halus.
* Lakukan desimasi. Ini memastikan tidak ada face yang tipis atau terdistorsi di tepi grup face. Di bawah `Pertahankan batas`, pastikan `Grup Face` aktif. Dengan begitu tepi segitiga akan mengikuti tepi grup face Anda dengan tepat.
* Di opsi Quad Remesher, pastikan relax dinonaktifkan (karena Anda sudah melakukan relax pada mesh), dan Anda seharusnya mendapat hasil yang bagus.

:::

### Desimasi {#decimate}
Memulai operasi desimasi.

Ikon di samping tombol desimasi menampilkan opsi-opsi di bawah dan memungkinkan Anda menyalakan atau mematikannya. Persentasenya menunjukkan seberapa kuat opsi tersebut.

* ![](/icons/palette.webp)  `Pelihara lukisan` - Menempatkan lebih banyak segitiga di tempat yang punya detail cat.
* ![](/icons/triforce.webp) `Wajah Seragam` - Mengutamakan segitiga berukuran merata.
* ![](/icons/hole.webp)  `Lubang` - Desimasi akan berusaha menjaga tepi di sekitar geometri terbuka dan lubang tetap tidak berubah.
* ![](/icons/group.webp) `Grup Face` - Desimasi akan berusaha menjaga batas grup face tetap tidak berubah.
* ![](/icons/uv.webp) `UV` - Desimasi akan berusaha menjaga batas UV tetap tidak berubah.

### Targetkan segitiga {#target-triangles}
Menentukan jumlah segitiga target. Nilai bawaannya 50%; tombol persen/target berganti antara persentase atau jumlah poligon target yang pasti.

### Opsi {#decimate-gear-menu}
Setiap opsi punya kotak centang untuk menyalakan atau mematikannya, dan nilai untuk kekuatannya:

#### ![](/icons/palette.webp) Pelihara lukisan {#preserve-painting}
Nilainya menentukan seberapa akurat detail cat dipertahankan. Nilai lebih tinggi mempertahankan lebih banyak cat. Atur ke 0 jika Anda tidak peduli dengan cat.

#### ![](/icons/triforce.webp) Wajah Seragam {#uniform-faces}
Nilai lebih tinggi akan menghasilkan segitiga dengan ukuran yang mirip.

#### Pertahankan batas {#preserve-borders}
Mencegah tepi ikut didesimasi. Bobot tepi bisa diatur untuk tepi `Lubang`, `Grup Face`, atau `UV` (`UV` memerlukan objek yang punya UV).

## ![](/icons/quad.webp) Remesh Kuad {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Menyusun ulang objek dengan tata letak kuad yang rapi. Tab ini punya beberapa remesher, masing-masing dengan tombol `Remesh`, penggeser `Targetkan kuad`, dan menu roda giginya sendiri. Coba semuanya pada objek Anda, hasilnya cukup berbeda satu sama lain!

### Quad Remesher {#quad-remesher}
Remesher yang sama dengan alat [Quad Remesher](tools.md#quad-remesher), dikembangkan oleh [Exoside](https://exoside.com/). Remesher ini hanya tersedia di beberapa platform dan perlu dibeli: sebelum dibeli, tombol `Remesh` menampilkan ikon keranjang.

`Pilih alat` beralih ke alat Quad Remesher, untuk menggambar panduan dan mewarnai kepadatan. Menu roda gigi berisi `Jumlah Kuad Adaptif`, `Ukuran Adaptif` (di 100% ukuran kuad mengikuti kelengkungan, di 0% kuad seragam), `Deteksi Tepi Keras Otomatis`, dan `Proyeksikan Ulang Vertex`.

::: tip
Di platform yang mendukungnya, Quad Remesher umumnya memberi hasil terbaik dan kontrol paling banyak.
:::

### AutoRemesher {#autoremesher}
Remesher kuad alternatif, dengan opsi untuk menyesuaikan ukuran dan bentuk kuad dengan permukaan.

#### ![](/icons/cog.webp) Menu roda gigi AutoRemesher {#autoremesher-gear-menu}
Menu roda gigi berisi opsi lanjutan berikut:

##### Penskalaan tepi {#edge-scaling}
Mengubah skala ukuran kuad; nilai lebih tinggi menghasilkan kuad yang lebih besar.

##### Adaptivitas {#adaptivity}
Menyesuaikan kepadatan kuad dengan kelengkungan. 0 menghasilkan kuad seragam, 1 menghasilkan kuad lebih kecil di area yang melengkung.

##### Anisotropi {#anisotropy}
Meregangkan kuad mengikuti arah permukaan yang paling datar. 0 menghasilkan kuad persegi, 1 menghasilkan kuad memanjang pada bentuk tabung dan punggungan.

##### Tepi tajam {#sharp-edge}
Tepi yang tertekuk lebih dari sudut ini dipertahankan sebagai fitur tajam.

##### Haluskan normal {#smooth-normal}
0 membuat permukaan tetap bersegi selama remesh. Nilai lebih tinggi menghaluskan permukaan dengan memperhitungkan normal verteks.

##### Maksimal isi lubang {#autoremesher-max-fill-hole}
Algoritma ini terkadang bisa menghasilkan lubang yang tidak diinginkan. Jika sebuah lubang punya verteks lebih sedikit dari nilai ini, lubang itu akan diisi.

### Instant Mesh {#quad-remesh-instant}
Remesh dengan [algoritma Instant Meshes karya Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Algoritma ini menganalisis alur mesh dan membuat topologi kuad yang rapi.

#### Remesh {#instant-remesh}
Memulai operasi remesh.

#### Targetkan kuad {#target-quads}
Jumlah poligon kuad yang akan coba dibuat oleh remesher.

#### ![](/icons/cog.webp) Menu roda gigi Instant Mesh {#quad-remesh-instant-gear-menu}
Menu roda gigi berisi opsi lanjutan berikut:

##### Sudut lipatan {#crease-angle}
Ambang batas sudut tajam yang akan membantu memandu operasi remesh. Aktifkan dengan kotak centangnya.

##### Maksimal isi lubang {#max-fill-hole}
Algoritma ini terkadang bisa menghasilkan lubang yang tidak diinginkan. Jika sebuah lubang punya verteks lebih sedikit dari nilai ini, lubang itu akan diisi.

### QuadriFlow {#quadriflow}
Remesh dengan algoritma QuadriFlow, cara lain untuk mendapatkan tata letak kuad yang rapi.

#### ![](/icons/cog.webp) Menu roda gigi QuadriFlow {#quadriflow-gear-menu}
Menu roda gigi berisi opsi lanjutan berikut:

##### Pertahankan batas {#quadriflow-preserve-boundary}
Melindungi tepi lubang.

##### Pertahankan ketajaman {#keep-sharp}
Menyelaraskan kuad dengan tepi tajam permukaan.

##### Aliran biaya minimum {#min-cost-flow}
Memakai solver aliran biaya minimum untuk tata letak kuad. Lebih lambat, tetapi bisa menghasilkan topologi yang lebih teratur.

## ![](/icons/uv.webp) Unwrap UV {#uv-unwrap}
Menghitung koordinat tekstur (UV) untuk objek yang dipilih. Nomad punya dua metode, `UVAtlas` dan `BFF`, masing-masing dengan tombol `Unwrap` sendiri.

![](/videos/unwrap.mp4)

::: tip UV?
Analogi yang umum untuk UV adalah membungkus kado: bagaimana cara terbaik memotong kertas kado agar menutupi seluruh benda tanpa ada yang tumpang tindih?

UV mirip dengan itu, tetapi yang dipotong bukan kertasnya, melainkan objeknya. Bayangkan model Anda terbuat dari plastik tipis: bagaimana Anda akan memotongnya agar bisa dibuka dan dibentangkan rata, mewarnainya dalam keadaan rata itu, lalu merakitnya kembali?

Sekarang bayangkan permukaan model Anda terbuat dari kain lycra yang elastis. Anda bisa meregangkannya sampai rata, memotongnya, atau gabungan keduanya. Tetapi jika Anda menggambar pola papan catur pada objek saat dalam keadaan rata, pola itu akan terdistorsi saat objek dirakit kembali. Mana metode yang lebih baik: lebih banyak potongan dengan distorsi lebih sedikit, atau lebih sedikit potongan dengan distorsi lebih banyak?

UV adalah instruksi yang memberi tahu perangkat lunak 3d cara 'memotong dan meregangkan' objek saat menerapkan tekstur. Alat UV Atlas umumnya memakai pendekatan 'lebih banyak potongan, lebih sedikit distorsi'.


:::

::: tip UV, Nomad, dan aplikasi lain

Sebagian besar model bertekstur yang Anda temukan secara online diberi tekstur lewat UV. Nomad bisa mengimpor dan menampilkannya melalui panel [material](material.md#textures).

Saat membuat model di Nomad, Anda bisa langsung mewarnai objek tanpa UV. Jika Anda perlu mengekspornya ke aplikasi lain, misalnya [Procreate](https://procreate.art/), Anda bisa melakukan 'bake' informasi warna Nomad ke tekstur melalui UV.

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
UVAtlas umumnya lebih memilih membuat lebih banyak pulau dengan potongan, untuk meminimalkan distorsi.

#### Unwrap {#unwrap}
Menghitung UV untuk objek yang dipilih.

#### Opsi {#uvatlas-gear-menu}
Tombol-tombol di samping `Unwrap`:

##### Grup Face {#atlas-face-group}
Saat menampilkan `Ya`, grup face menentukan potongan UV. Pengaturan ini dipakai bersama dengan BFF.

##### Hapus UV {#delete-uvs}
Tombol tempat sampah menghapus UV objek.

##### Periksa {#uv-inspect}
Menampilkan UV objek di latar belakang.

#### Peregangan Maks {#max-stretch}
Nilai rendah menghasilkan distorsi lebih sedikit dan pulau lebih banyak, nilai tinggi menghasilkan distorsi lebih banyak dan pulau lebih sedikit.

#### Jarak Antarpulau {#island-spacing}
Jarak antar pulau. Nilai rendah membuang lebih sedikit ruang, tetapi berisiko membuat tekstur merembes ke pulau di sebelahnya.

::: warning
Menghitung UV bisa memakan waktu; sebaiknya gunakan mesh dengan kurang dari 100k verteks.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

UV BFF lebih memilih pendekatan 'lebih sedikit potongan, lebih banyak distorsi'.

#### Opsi {#uv-bff-gear-menu}
Tombol `Grup Face`, hapus, dan `Periksa` yang sama seperti pada [UVAtlas](#uvatlas-gear-menu) ada di samping `Unwrap`.

##### Grup Face {#bff-face-group}

Memakai grup face untuk menentukan potongan UV.

#### Jumlah kerucut {#cone-count}
Menentukan jumlah proyeksi utama yang dipakai. Nilai lebih rendah menghasilkan pulau lebih sedikit, tetapi distorsi lebih banyak. Nilai lebih tinggi butuh waktu hitung lebih lama.

#### Patch mulus {#seamless-patches}
Memengaruhi tata letak patch UV, dan bisa menimbulkan distorsi yang cukup besar. Paling baik dipakai dengan grup face yang dibuat dengan cermat.

::: warning
BFF bisa membuat UV yang saling tumpang tindih jika mesh punya pegangan (seperti lubang pada donat).
:::

### ![](/icons/preview.webp) Tampilkan UV setelah unwrap {#show-uv-after-unwrap}
Membuka tampilan pemeriksa UV setelah unwrap, sehingga Anda bisa langsung memeriksa hasilnya.

### ![](/icons/bake.webp) Bake: Tekstur → Tekstur {#unwrap-bake-texture}
Hanya tersedia jika material objek punya tekstur. Saat Anda melakukan unwrap lagi, tekstur dipindahkan ke UV yang baru, sehingga tetap pas. Resolusinya `Otomatis` secara bawaan, menyesuaikan tekstur terbesar, atau Anda bisa mengaturnya sendiri.

## ![](/icons/bake.webp) Bake {#bake}
Tab ini memindahkan detail dan cat antar objek, dan antara verteks dan tekstur.

`Dari resolusi tinggi` memakai objek lain sebagai sumber; angka di dalam kurung menunjukkan jumlahnya. Nomad memilihnya dengan cara berikut:

- semua objek yang dipilih dipakai, dan objek pilihan utama menjadi target (sorotan paling terang di menu [Adegan](scene.md))
- jika hanya satu objek yang dipilih, Nomad memakai semua objek yang terlihat
- jika semua objek lain disembunyikan (misalnya dengan Solo), seluruh adegan dipakai

### ![](/icons/bake.webp) Bake → Tekstur {#bake-texture}
![](/images/topology_bake_menu.webp)

Bake tekstur membuat tekstur dengan memproyeksikan objek lain yang terlihat di adegan ke UV objek yang dipilih. Objek tersebut memerlukan UV.

Berikut alur kerja bake yang umum:
- Anda punya mesh dengan detail halus dan cat
- Klon mesh tersebut
- Lakukan desimasi (atur `Pelihara lukisan` ke 0)
- Lakukan unwrap UV
- Lakukan bake!

Sekarang Anda seharusnya punya mesh beresolusi rendah yang mempertahankan sebagian besar cat dan detail dari objek sebelumnya.

Setelah operasi, warna verteks akan dipindahkan ke lapisan baru yang nonaktif, agar tidak mengganggu tekstur.

#### Dari objek ini {#tex-from-itself}
Melakukan bake objek ke UV-nya sendiri: catnya menjadi tekstur, dan jika objek punya level multiresolusi, detail level tertinggi di-bake ke level saat ini (ikon multires lalu muncul di tombol). Cara ini mudah disiapkan, tetapi sering kali Anda butuh kontrol lebih, dan untuk itu opsi berikutnya lebih berguna.

#### Dari resolusi tinggi {#tex-from-high-res}
Melakukan bake dari objek-objek lain ke objek yang dipilih. Angka di dalam kurung menunjukkan jumlah objek lain yang akan dipakai sebagai sumber resolusi tinggi, yang di-bake ke objek resolusi rendah saat ini yang punya UV. Objek-objek lain tidak perlu punya tata letak atau topologi yang mirip dengan objek yang di-bake, sehingga alur kerja bake bisa sangat fleksibel.

#### Resolusi {#tex-bake-resolution}
Resolusi tekstur hasil bake. Tekstur hasil bake selalu persegi, jadi 1024 akan membuat gambar 1024x1024.

Tombol-tombol di bawahnya adalah pintasan untuk resolusi yang sering dipakai. Sebagai acuan, 512x512 tergolong kecil, misalnya untuk grafis web dan geometri sederhana. 4096x4096 (disingkat 4k) untuk render berkualitas tinggi.

#### Warna, Kekasaran, Kemetalan, Normal, Perpindahan, Emisif, Opasitas {#tex-normal-roughness-metalness-color-emissive-opacity}
Tombol-tombol ini menentukan properti mana yang akan di-bake, masing-masing ke map terpisah. Setelah bake selesai, map tersebut akan ditambahkan sebagai tekstur ke material objek saat ini. `Perpindahan` melakukan bake ketinggian detail sebagai displacement map.

#### ![](/icons/cog.webp) Menu roda gigi Bake {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Menu roda gigi berisi opsi lanjutan berikut:

##### Cadangan {#tex-backup}
Untuk melihat pratinjau tekstur hasil bake, informasi cat objek harus dinonaktifkan. `Cadangan (Melukis → Lapisan)` akan memindahkan semua informasi cat ke lapisan baru sebagai cadangan, sehingga mudah diaktifkan/dinonaktifkan.

##### Gunakan multires {#tex-use-multires}
Untuk `Dari objek ini` pada objek yang punya level multiresolusi. Nomad membaca resolusi tinggi melalui level subdivisi alih-alih menembakkan sinar: lebih cepat dan bebas dari kesalahan proyeksi. Matikan untuk melakukan bake dengan opsi-opsi di bawah.

##### Dasar halus {#tex-smooth-base}
Untuk `Perpindahan` pada objek yang punya level multiresolusi. Mengukur displacement dari dasar yang sudah tersubdivisi, bukan dari face datarnya. Biarkan aktif jika displacement map akan dipakai pada mesh tersubdivisi, seperti adaptive subdivision di Blender.

##### Jarak pencarian {#tex-cage-radius}
Jarak maksimum untuk mencari permukaan sumber. Secara bawaan jarak ini dibuat kecil untuk menghindari artefak, tetapi bisa diperbesar jika objek sumber berada jauh dari objek yang di-bake.

##### Proyeksi {#tex-projection}
Cara permukaan sumber dicari:

* `Sinar` - Memproyeksikan mengikuti normal permukaan.
* `Sinar + terdekat` - Memakai sinar normal, lalu memakai permukaan terdekat jika sinar meleset.
* `Terdekat` - Memproyeksikan ke titik terdekat pada permukaan sumber.

##### Offset sinar {#tex-ray-offset}
Mengatur titik awal perhitungan bake pada objek yang di-bake. Offset kecil dari permukaan menghindari sebagian besar artefak yang umum. Jika objek sumber berada sangat jauh dari objek yang di-bake, offset ini mungkin perlu diperbesar. Tidak dipakai oleh `Terdekat`.


### ![](/icons/bake.webp) Proyeksi ulang → Verteks {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Memproyeksikan detail pahatan, cat, lapisan, dan tekstur ke nilai verteks.

Ini bisa dianggap kebalikan dari bake: jika bake memindahkan properti verteks ke tekstur, proyeksi ulang memindahkan tekstur (dan properti lain)
 kembali ke verteks.

::: tip
Saat memakai `Bake → Tekstur` atau `Proyeksi ulang → Verteks`, warna verteks dan tekstur material sama-sama diperhitungkan.
:::

#### Dari objek ini {#vertex-from-itself}
Mengonversi tekstur dari material menjadi nilai verteks. Tombol ini hanya aktif jika objek punya UV, dan tekstur aktif di material.

::: tip TIPS: Mewarnai tekstur
Nomad tidak mendukung pengecatan dan pengeditan tekstur secara langsung, tetapi hasil yang sangat mirip bisa didapat dengan memproyeksikan tekstur -> nilai verteks, mewarnai verteks, lalu melakukan bake verteks -> tekstur:

1. Siapkan objek low poly yang punya UV
1. Muat tekstur ke materialnya
1. Lakukan subdivisi secukupnya agar bisa diwarnai
1. `Proyeksi ulang → Verteks` dalam mode `Dari objek ini`; sekarang tekstur sudah dikonversi menjadi nilai verteks
1. Warnai, haluskan, usapkan, stempel, lakukan edit apa pun yang Anda perlukan
1. `Bake → Tekstur` dalam mode `Dari objek ini`. Hasil edit tersebut dikonversi kembali menjadi tekstur.
:::

#### Dari resolusi tinggi {#vertex-from-high-res}
Mengonversi objek-objek lain menjadi nilai verteks pada objek yang dipilih. Angka pada tombol ini menunjukkan jumlah objek sumber. Ini terutama dimaksudkan untuk dipakai pada mesh beresolusi tinggi juga, biasanya dengan topologi yang rapi.

::: tip
Memproyeksikan ulang objek lain tidak hanya berguna untuk memindahkan informasi warna dari objek lain, tetapi juga untuk memproyeksikan verteks ke objek lain, misalnya perban bisa diproyeksikan ke sebuah karakter.
:::

#### Verteks, Warna, Kekasaran, Kemetalan, Opasitas, Topeng, Lapisan, Grup Face {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Tombol-tombol ini menentukan properti mana yang akan diproyeksikan ke objek yang dipilih. `Lapisan` memindahkan lapisan-lapisan lain ke mesh yang dipilih.

#### ![](/icons/cog.webp) Menu roda gigi Proyeksi ulang {#vertex-reproject-gear-menu}
Menu roda gigi berisi opsi lanjutan berikut:

##### Opasitas → Topeng {#vertex-opacity-to-mask}
Mengubah opasitas sumber menjadi mask pada objek yang dipilih.

##### Iterasi {#vertex-iterations}
Berapa kali operasi relax diterapkan selama proyeksi ulang. Hanya dipakai jika `Verteks` aktif.

##### Santai {#vertex-relax}
Tata letak mesh yang dipilih bisa dihaluskan atau di-relax sampai tingkat tertentu agar lebih pas dengan objek sumber proyeksi ulang. `Halus` lebih cocok untuk mesh high poly, `Santai` lebih cocok untuk mesh low poly. `Otomatis` membiarkan Nomad menentukan metode terbaik.

##### Jarak pencarian {#vertex-cage-radius}
Jarak maksimum untuk mencari permukaan sumber. Secara bawaan jarak ini dibuat kecil untuk menghindari artefak, tetapi bisa diperbesar jika objek sumber berada jauh dari objek yang dipilih.

##### Proyeksi {#vertex-projection}
Cara permukaan sumber dicari:

* `Sinar` - Memproyeksikan mengikuti normal permukaan.
* `Campuran adaptif` - Mencampur sinar normal dan permukaan terdekat sesuai jarak dan `Preferensi sinar`. Jika salah satunya meleset, yang lain dipakai.
* `Terdekat` - Memproyeksikan ke titik terdekat pada permukaan sumber.

##### Preferensi sinar {#vertex-ray-bias}
Hanya untuk `Campuran adaptif`. Nilai lebih tinggi menggeser campuran ke hasil sinar normal, nilai lebih rendah ke titik terdekat.

##### Offset sinar {#ray-vertex-offset}
Mengatur titik awal perhitungan bake pada objek yang dipilih. Offset kecil dari permukaan menghindari beberapa artefak. Jika objek sumber berada sangat jauh dari objek yang di-bake, offset ini mungkin perlu diperbesar. Tidak dipakai oleh `Terdekat`.

### ![](/icons/bake.webp) Bake → VDM {#bake-vdm}
Membuat stempel VDM (vector displacement) dari objek yang dipilih dan menambahkannya ke pustaka VDM. Anda akan diminta memberi nama.

Berikut alur kerja yang umum:
- Tambahkan sebuah bidang, atau pilih `VDM baru` di pemilih VDM untuk menambahkan bidang yang sudah dikonfigurasi (primitif [VDM](scene.md#add-menu))
- Pahat bentuk Anda di atasnya, dengan tepinya tetap datar
- Lakukan bake!

UV bidang tersebut menentukan area persegi yang di-bake, jadi objek memerlukan UV. Pilih ukuran stempel dengan `Resolusi`, dan pilih dengan `Warna`, `Kekasaran`, `Kemetalan`, dan `Opasitas` apa saja yang dibawa stempel selain displacement.

::: tip
Hindari DynTopo pada bidang tersebut, karena akan merusak UV-nya dan stempel yang dihasilkan jadi terdistorsi. Memahat di sebuah lapisan memberi hasil paling akurat, karena bidang datarnya tetap ada di bawahnya. Mewarnai juga memerlukan lapisan; jika tidak, material akan distempel ke seluruh area persegi, bukan hanya di tempat yang Anda warnai.
:::

## ![](/icons/dot.webp) Primitif {#primitive}
Parameter untuk primitif yang dipilih. Sebagian besar juga tersedia dari tombol `…` di toolbar viewport primitif.

![](/images/topology_primitive_screenshot.webp)
