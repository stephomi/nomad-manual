# ![](/icons/multires.webp) Topologi {#topology}

Menu ini mengawal topologi objek dalam Nomad, dan juga mengandungi alat untuk melakukan bake dan memindahkan perincian antara objek, serta antara tekstur.

![](/images/topology_overview.webp)

Nomad berasaskan poligon: ia menggunakan segi tiga dan kuad untuk mengendalikan geometri.
Topologi merujuk kepada bilangan muka dan juga cara titik (verteks) disambungkan.

Penting untuk sentiasa memantau topologi, terutamanya jika anda mahu mengukir atau mengecat perincian halus.

::: tip Bagaimana untuk memantau topologi anda?
Anda boleh memaparkan [Kerangka dawai](settings.md#wireframe) atau hanya mematikan [Shading licin](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Menu topologi Nomad mempunyai beberapa tab, dalam dua baris:

| Kaedah                                | Ikon                         | Penerangan                                                       |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolusi](#multiresolution)     | ![](/icons/multires.webp)   | Sunting beberapa tahap perincian menggunakan pembahagian          |
| [Remes voxel](#voxel-remesher)        | ![](/icons/voxel.webp)      | Kira semula topologi baharu dengan ketumpatan seragam             |
| [Topologi dinamik](#dynamic-topology) | ![](/icons/dynamic.webp)    | Tambah/buang muka secara setempat dalam masa nyata semasa mengukir atau mengecat |
| [Pelbagai](#misc)                     | ![](/icons/topo_extra.webp) | Tutup lubang, paksa manifold dan tukar kepada triplanar           |
| [Primitif](#primitive)                | ![](/icons/dot.webp)        | Pilihan primitif                                                  |
| [Kurangkan](#decimation)              | ![](/icons/decimate.webp)      | Kurangkan bilangan muka sambil mengekalkan bentuk             |
| [Remesh kuad](#quad-remesh)           | ![](/icons/quad.webp)       | Bina semula objek dengan susun atur kuad yang kemas               |
| [Buka balut UV](#uv-unwrap)           | ![](/icons/uv.webp)         | Cipta UV untuk tekstur                                            |
| [Bake](#bake)                         | ![](/icons/bake.webp)       | Bake perincian dan cat ke tekstur, verteks atau cop VDM           |


## Statistik poligon {#polygon-stats}

![](/images/topology_stats.webp)

Bahagian atas setiap tab menunjukkan bilangan poligon bagi objek yang dipilih, dan bagi keseluruhan adegan apabila ia mempunyai lebih daripada satu objek. Lajur-lajurnya ialah bilangan verteks, segi tiga, kuad (poligon 4 sisi) dan koordinat UV (0 apabila objek tidak mempunyai UV).

Ketuk bahagian ini untuk menyenaraikan setiap objek dalam adegan dengan bilangan tepatnya, termasuk bilangan kumpulan mukanya.

## ![](/icons/cog.webp) Menu gear {#gear-menu}
Sesetengah bahagian, seperti dalam tab [Remesh kuad](#quad-remesh) dan [Bake](#bake), mempunyai pilihan tambahan. Bukanya dengan ikon gear di sebelah tajuk bahagian.

## ![](/icons/multires.webp) Multiresolusi {#multiresolution}

![](/images/topology_multires_menu.webp)

### Apakah multiresolusi? {#what-is-multiresolution}
Ciri multiresolusi berguna untuk dua senario utama:
- Algoritma pembahagian licin untuk menambah bilangan poligon objek anda
- Mengendalikan beberapa tahap resolusi supaya anda boleh bertukar antara suntingan berskala kecil dan besar

![](/videos/multiresolution.mp4)

#### Aliran kerja multiresolusi {#multiresolution-workflow}
Satu aspek penting multiresolusi ialah anda boleh kembali ke resolusi yang lebih rendah, membuat perubahan pada objek anda, dan kemudian kembali ke resolusi tertinggi tanpa kehilangan perincian resolusi tinggi. Semua perincian resolusi tinggi akan diunjurkan secara automatik.

[Lapisan](layers.md#layers) tersedia pada setiap resolusi.

::: warning
Jika anda menggunakan alat yang mengubah topologi objek anda, anda akan kehilangan semua resolusi lain objek tersebut!
Anda sepatutnya sentiasa menerima amaran jika ini akan berlaku, contohnya apabila anda menggunakan:
- [Remes voxel](#voxel-remesher)
- [Topologi dinamik](#dynamic-topology)
- [alat Potong (Trim)](tools.md#trim)
- [alat Pisahkan](tools.md#split)
:::


### Peluncur multiresolusi {#multiresolution-slider}
Peluncur ini menunjukkan bilangan tahap pembahagian dalam objek semasa. Jika terdapat 6 bar menegak, terdapat 6 tahap pembahagian. Bulatan menunjukkan tahap pembahagian yang sedang dipaparkan.

Ikon kecil di atas peluncur menunjukkan pilihan (`Kunci tahap 0`, `Linear`, `Sempadan tajam`, `Simpan segitiga`) yang digunakan bagi setiap tahap.

### Terbalikkan {#reverse}
Apabila berada pada tahap pembahagian terendah, butang terbalikkan akan cuba mencipta tahap di bawah tahap semasa. Perhatikan bahawa ini biasanya hanya boleh berlaku jika objek itu pada asalnya dicipta dengan pembahagian, contohnya dalam Nomad atau dalam aplikasi 3d lain yang menyokong permukaan pembahagian multiresolusi.

### Perbahagikan {#subdivide}
Butang *Perbahagikan* akan menggandakan bilangan poligon sebanyak 4 kali, jadi pastikan anda memantau bilangan poligon kerana ia boleh bertambah dengan sangat cepat! Nomad meminta pengesahan apabila hasilnya akan menjadi sangat berat.
Satu aspek penting *Permukaan Pembahagian* ialah ia akan menumpu kepada *Permukaan Licin*.
Untuk memahami cara ia berfungsi, anda boleh mencuba butang *Perbahagikan* pada objek yang hanya mempunyai beberapa poligon.

Anda boleh mematikan tingkah laku *Licin* ini dengan pilihan `Linear`.

### Padam lebih rendah {#delete-lower}
Jika terdapat pembahagian di bawah tahap yang sedang dipaparkan, padamkannya. Jika anda melakukannya secara tidak sengaja, anda boleh menciptanya semula dengan butang Terbalikkan.

### Padam lebih tinggi {#delete-higher}
Jika terdapat pembahagian di atas tahap yang sedang dipaparkan, padamkannya.

### ![](/icons/lock.webp) Kunci tahap 0 {#lock-lv0}
Kekalkan bentuk tahap pembahagian terendah semasa anda mengukir pada tahap yang lebih tinggi. Pewarnaan masih dibawa turun ke tahap 0. Ini boleh menjadi penting jika objek anda dijana dalam aplikasi lain, dan objek asasnya mesti kekal tidak berubah.

Pilihan ini hanya tersedia sebelum pembahagian pertama. Apabila ia dimatikan, perubahan besar yang dibuat pada tahap pembahagian yang lebih tinggi akan menggerakkan tahap 0.

### ![](/icons/linear.webp) Linear {#linear-subdivision}
Bahagikan mesh tanpa menggunakan sebarang pelicinan.

### ![](/icons/group.webp) Sempadan tajam {#sharp-border}
Jika objek anda mempunyai kumpulan muka, mendayakan pilihan ini akan mengekalkan ketajaman sempadan kumpulan muka. Ini boleh ditetapkan pada setiap tahap pembahagian (peluncur pembahagian akan memaparkan ikon kecil di atas tahap tersebut untuk menunjukkannya).

### ![](/icons/triangle.webp) Simpan segitiga {#keep-triangles}
Kebanyakan sistem permukaan pembahagian standard akan cuba menukar semua poligon kepada kuad semasa operasi pembahagian. Suis ini memaksa pembahagian menggunakan segi tiga sebaliknya.

::: tip

Pembahagian akan melicinkan semua tepi tajam secara lalai. Untuk mengekalkan tepi yang sedikit tajam, cuba gunakan `Linear` atau `Sempadan tajam` pada 2 tahap pembahagian pertama, kemudian matikannya untuk tahap yang lebih tinggi. Ini akan menghasilkan mesh terbahagi yang separa tajam.

:::

### Tunjukkan tahap tertinggi {#show-highest-level}
Paparkan tahap tertinggi dengan semua perinciannya semasa anda mengukir pada tahap yang lebih rendah. Berguna untuk melihat hasil akhir semasa anda membuat perubahan besar.

### Kerangka dawai: Hanya Tahap 0 {#wireframe-level-0-only}
Apabila [Kerangka dawai](settings.md#wireframe) dihidupkan, hanya paparkan kerangka dawai tahap terendah. Kerangka dawai yang padat pada tahap tinggi boleh melindungi bentuk.


## ![](/icons/voxel.webp) Remes voxel {#voxel-remesher}
![](/images/topology_voxel_menu.webp)
Apabila menggunakan `Remes voxel`, topologi keseluruhan mesh akan dipaksa mempunyai resolusi seragam, bermakna semua poligon mempunyai saiz yang lebih kurang sama. Ini sangat berguna apabila anda tidak mahu memikirkan topologi dan hanya mahu mengukir secara bebas.

Aliran kerja mengukir yang biasa boleh bermula dengan menggunakan `Remes voxel` untuk membina bentuk kasar dengan resolusi rendah.
Hanya tekan butang *Remesh* sekali-sekala apabila anda terlalu meregangkan mesh, untuk mengelakkan herotan yang berlebihan.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Seperti yang dinyatakan di atas, Nomad ialah perisian berasaskan poligon, tetapi `Remes voxel` ialah satu pengecualian di mana pendekatan lain digunakan (buat sementara) untuk melakukan remesh.

Satu perbezaan besar ialah pendekatan voxel tidak menerima persilangan diri, jadi persilangan ini akan diselesaikan.
Ia juga tidak menyokong mesh yang mempunyai lubang.

Dengan lubang, kami tidak maksudkan `lubang genus` (`lubang` pada donat), tetapi mesh yang tidak `kedap air`/`tertutup`.
Biasanya, ini bermakna sebelum remesh dilakukan, setiap lubang akan diisi, sama seperti [alat Potong (Trim)](tools.md#trim) atau [ciri pengisian lubang](#holes). Pilihan [Lubang](#voxel-holes) di bawah menentukan caranya.
:::

### ![](/icons/voxel.webp) Remesh {#voxel-remesh}
Laksanakan remesh voxel. Ikon kecil pada butang mengingatkan anda pilihan di bawah yang sedang dihidupkan.

### Resolusi {#voxel-resolution}
Saiz voxel yang digunakan semasa pengiraan; nilai yang lebih tinggi memberikan lebih banyak perincian. Semasa mengubah parameter ini, corak papan dam akan ditindih pada mesh untuk mempratonton hasilnya.

Penitis mengambil resolusi daripada ketumpatan mesh di tempat yang anda ketuk. Butang kiub di sebelahnya menukar nilai kepada `Panjang tepi` dalam unit dunia: nilai yang sama kemudian memberikan perincian yang sama pada mana-mana objek.

### Bina multiresolusi {#build-multiresolution}
Cipta tahap multiresolusi yang lebih rendah untuk remesh voxel. Jika anda menggunakan corak papan dam untuk menetapkan resolusi, dan menetapkan bina multiresolusi kepada 2, hasil akhir akan mempunyai perincian yang sepadan dengan peluncur resolusi, dan jika anda pergi ke tab multires, ia akan berada pada tahap 2, bermakna anda mempunyai mesh multires beresolusi lebih rendah pada tahap 1 dan tahap 0. Ini boleh menjadi cara yang baik untuk menjana mesh yang kemas dengan poligon sekata, sambil mempunyai mesh kawalan beresolusi rendah.

Ia juga lebih pantas dan menggunakan kurang memori pada resolusi tinggi. Tetapi dengan resolusi rendah dan banyak tahap, anda akan kehilangan perincian.

::: tip Petua: Bina multiresolusi dan pelicinan stabil

Pilihan ini kadangkala boleh menyebabkan 'gelung' dalam geometri yang sukar dilicinkan, sehingga menghasilkan bintil-bintil kecil. Jika ini berlaku, dayakan 'Melicinkan stabil' dalam pilihan alat lancar.

:::

### Tebalkan bahagian nipis {#thicken-thin-parts}
Bahagian yang lebih nipis daripada voxel boleh terpecah atau hilang semasa remesh. Pilihan ini menebalkannya supaya ia kekal; nilai yang lebih tinggi menebalkan lebih banyak. Ia tidak tersedia dengan `Tepi tajam` atau `Sempadan tajam`.

### Lubang {#voxel-holes}
Cara lubang ditutup sebelum remesh:

* `Isi` - Setiap lubang ditutup secara berasingan, daripada sempadannya.
* `Bentuk` - Lubang ditutup dengan mengikut permukaan di sekelilingnya, dan kepingan terbuka yang bertindih akan dicantumkan.

### ![](/icons/angle.webp) Tepi tajam {#keep-sharp-edges}
Lekapkan titik baharu pada tepi tajam mesh asal. Ia paling berguna untuk operasi boolean primitif yang ringkas, dan ia boleh menyebabkan herotan.

### ![](/icons/group.webp) Sempadan tajam {#voxel-sharp-border}
Muka baharu mengikut sempadan kumpulan muka, dan sempadan kekal tajam di tempat permukaan berlipat di sepanjangnya.

### ![](/icons/group_separate.webp) Asingkan kumpulan {#keep-groups-separate}
Setiap kumpulan muka di-remesh secara berasingan: kumpulan tidak pernah bercantum, dan setiap satu kekal sebagai kepingan tertutup dalam kumpulannya sendiri. Multiresolusi tidak dibina dalam mod ini. Ia tersedia apabila objek mempunyai beberapa kumpulan muka.

## ![](/icons/dynamic.webp) Topologi dinamik {#dynamic-topology}

![](/images/topology_dyntopo_menu.webp)
Multiresolusi dan remesh voxel ialah kaedah biasa dalam industri untuk mengawal topologi, tetapi kedua-duanya memerlukan anda berhati-hati supaya tidak meregangkan poligon terlalu jauh, atau memampatkan poligon terlalu rapat.

Topologi dinamik ialah kaedah alternatif. Semasa anda mengukir, Nomad akan menambah dan membuang poligon secara adaptif sepanjang sapuan berus, jadi mengukir perincian kecil akan menambah banyak poligon kecil di tempat yang anda perlukan, dan melicinkan di tempat lain akan membuang poligon.

Perhatikan bahawa topologi dinamik menggunakan poligon segi tiga dan bukannya kuad. Ini mungkin kelihatan agak berselerak, tetapi lebih baik tidak melihat kerangka dawai: tumpukan perhatian untuk menghasilkan arca yang cantik tanpa risau tentang topologi, kemudian anda boleh menggunakan salah satu alat remesh Nomad yang lain untuk menjana mesh kuad yang kemas.

Lihat video di bawah untuk melihatnya beraksi.

![](/videos/dynamic.mp4)

### Didayakan {#enabled}
Hidupkan topologi dinamik. Ikon DynTopo akan diletakkan di bawah peluncur jejari dan keamatan berus supaya anda boleh menghidupkan atau mematikan DynTopo bagi setiap alat. Ia boleh memberi kesan ketara pada prestasi, dan lapisan dikemas kini dengan betul.

### Perincian {#dyn-detail}
Kawal jumlah perincian; tingkah lakunya berubah berdasarkan pilihan 'Perincian berdasarkan...', lihat di bawah. Dalam mod `Skrin`, label menunjukkan saiz segi tiga sasaran dalam piksel. Dalam mod `Tetap`, penitis membolehkan anda mengambil perincian daripada ketumpatan mesh di tempat yang anda ketuk.

### Perincian berdasarkan... {#detail-based-on}
| Kaedah   | Penerangan                                                      |
| :------: | :-------------------------------------------------------------: |
| Skrin    | Tahap perincian bergantung pada saiz objek di skrin. Peluncur perincian pada 100% atau lebih untuk perincian halus, menghasilkan segi tiga kecil, atau 1% untuk perincian rendah, menghasilkan segi tiga besar. |
| Jejari   | Jejari alat menentukan jumlah perincian. Gunakan jejari alat yang kecil untuk perincian halus, dan jejari alat yang besar untuk perincian rendah. Peluncur perincian ialah pendarab pada nisbah ini. |
| Tetap    | Peluncur perincian menentukan jumlah perincian, dan tidak dipengaruhi oleh saiz skrin atau saiz alat. Ia nilai yang sama dengan peluncur [Perincian](#all-detail) bagi `Remesh`. |

::: tip PETUA: Mod jejari

Untuk lebih memahami cara mod jejari berfungsi, mula gerakkan peluncur perincian dengan satu jari, kemudian pada masa yang sama ubah jejari alat dengan jari lain. Anda akan melihat bagaimana kedua-duanya berkait.

:::

### Keutamaan... {#prefer}
| Kaedah   | Penerangan        |
| :------: | :---------------: |
| Kelajuan | Utamakan prestasi |
| Kualiti  | Utamakan kualiti  |

Apabila anda mengutamakan `Kualiti`, terdapat 2 perbezaan utama:
- penghalusan dilakukan sebelum mengukir, jadi anda akan mendapat kurang artifak interpolasi semasa mengecat atau mengukir perincian yang sangat kecil
- penghalusan berjalan sehingga ia menumpu kepada tahap perincian yang betul, berbeza dengan tingkah laku berperingkat.

Dengan cara itu, jika anda mengukir perincian yang sangat kecil atau membuat sapuan pantas, topologi akan sentiasa dihaluskan seperti yang dijangka.


### ![](/icons/pressure.webp) Guna tekanan pada jejari {#use-pressure-on-radius}
Hanya relevan jika `Jejari` diaktifkan. Apabila didayakan, tahap perincian akan sentiasa mencerminkan saiz berus, walaupun saiz berus dipengaruhi oleh tekanan pensel.

### Guna jatuhan strok {#use-stroke-falloff}

Turut sertakan lengkung pengurangan berus dan alpha dalam pengiraan DynTopo.

### Kaedah {#method}
Pilih cara topologi dinamik mengubah mesh, sama ada semasa anda mengukir atau apabila anda menggunakan [Remesh](#dyn-remesh):

| Kaedah         | Penerangan                                                            |
| :------------: | :-------------------------------------------------------------------: |
| Penyeragaman   | Ia boleh menambah dan membuang muka; ini mod yang digunakan dalam video di atas |
| Pecahan        | Hanya menambah muka baharu, ia tidak boleh membuang muka              |
| Pengurangan    | Hanya membuang muka, ia tidak boleh menambah muka baharu              |

### ![](/icons/shield.webp) Lindung kawasan yang bertopeng {#protect-masked-area}
Dayakan supaya kawasan bertopeng melindungi topologi daripada diubah.

### ![](/icons/normal.webp) Ekstrapolasi verteks {#vertex-extrapolation}
Letakkan titik pada permukaan licin yang mengikut kelengkungan di sekelilingnya, dan bukannya rata pada muka sedia ada.

### Perincian {#all-detail}
Resolusi yang digunakan untuk operasi remesh. Jika DynTopo dalam mod 'Tetap', ia akan menjadi nilai yang sama dengan peluncur Perincian di bahagian atas menu ini. Penitis mengambil perincian daripada ketumpatan mesh di tempat yang anda ketuk.

### Remesh {#dyn-remesh}
Laksanakan remesh global menggunakan algoritma DynTopo. Biasanya anda sepatutnya menggunakan [Remes voxel](#voxel-remesher) untuk remesh penuh.

Namun, satu kelebihannya berbanding voxel ialah mesh tidak perlu tertutup, dan kawasan bertopeng akan dilindungi, jadi anda mempunyai kawalan yang lebih baik ke atas tempat untuk meletakkan lebih banyak atau kurang ketumpatan.



## ![](/icons/topo_extra.webp) Pelbagai {#misc}

![](/images/topology_misc_menu.webp)

Tab ini mengumpulkan alat untuk membersihkan atau menukar mesh: menutup lubangnya, memaksanya menjadi manifold, atau menukarnya menjadi triplanar.

### ![](/icons/hole.webp) Lubang {#holes}
![](/images/topology_holes_menu.webp)
Kebanyakan masa, objek anda mungkin kedap air, bermakna mesh itu 'tertutup'.

Jika objek anda mempunyai lubang, anda boleh mengisinya.

![](/videos/hole_filling.mp4)

::: tip
Apabila anda menjalankan Remes voxel, semua lubang ditutup secara automatik, sama ada anda menggunakannya pada 1 atau beberapa mesh.
:::

#### Tutup lubang {#close-holes}
Laksanakan tindakan menutup lubang.

#### Pilihan {#holes-gear-menu}
Pilihan ini mengubah cara lubang diisi:

##### Kumpulan muka {#fill-face-group}
Pilih kumpulan muka bagi muka baharu:

* `Campuran` - Lubang yang dikelilingi oleh satu kumpulan muka menggunakan semula kumpulan tersebut, manakala lubang yang menyentuh beberapa kumpulan mendapat kumpulan baharu.
* `Baru` - Lubang yang diisi mendapat kumpulan muka baharu.
* `Guna semula` - Setiap lubang mengambil kumpulan muka yang paling banyak mengelilinginya.

##### Perincian {#fill-detail}
Ketumpatan poligon yang digunakan untuk mengisi lubang. Semasa menyeret peluncur ini, corak papan dam akan dipaparkan pada model untuk memberi gambaran saiz segi tiga yang akan digunakan. Kotak semak akan mematikan ini dan hanya menggunakan titik sedia ada, yang biasanya menghasilkan segi tiga panjang dan nipis di atas lubang, yang boleh menyukarkan pengukiran.

##### Jambatan {#fill-non-manifold}
Isi lubang dan pulau-pulau di dalamnya sebagai satu permukaan, dan bukannya mengisi setiap sempadan secara berasingan. Sudut yang lebih tinggi menjambatani lubang yang lebih melengkung. Kotak semak mematikannya.

### ![](/icons/cog.webp) Paksa manifold {#force-manifold}
![](/images/topology_forcemanifold_menu.webp)
Cuba membersihkan tepi bukan manifold. Ia boleh berguna untuk perisian luaran yang tidak menyokong tepi yang dikongsi oleh lebih daripada 2 muka.

#### Bersihkan {#clean}
Laksanakan tindakan pembersihan.

#### Pilihan {#force-manifold-gear-menu}
Pilihan ini mengubah cara mesh dibersihkan:

##### Padamkan muka kecil {#delete-small-faces}
Ambang yang digunakan untuk membuang dan mencantumkan poligon kecil. Dayakannya dengan kotak semaknya.


### ![](/icons/triplanar.webp) Triplanar {#triplanar}
![](/images/topology_triplanar_menu.webp)
Menukar mesh menjadi primitif [triplanar](scene.md#triplanar).
Anda mungkin akan kehilangan banyak perincian dalam proses ini: lapisan, cat dan multiresolusi juga hilang.

#### Paksa kubik {#force-cubic}
Dayakan supaya triplanar berbentuk kiub. Jika tidak, triplanar akan dimuatkan pada kotak sempadan terdekat di sekeliling objek anda.

#### Tukar {#convert}
Laksanakan tindakan triplanar.

#### Resolusi {#triplanar-resolution}
Resolusi grid triplanar; nilai yang lebih tinggi mengekalkan lebih banyak perincian.

## ![](/icons/decimate.webp) Kurangkan {#decimation}

![](/images/topology_decimation.webp)

Kurangkan bilangan poligon sambil cuba mengekalkan sebanyak mungkin perincian, menggunakan poligon segi tiga.

Ciri ini boleh berguna jika anda mahu mengeksport untuk cetakan 3d.
Namun, anda mungkin tidak patut menggunakannya jika anda mahu terus mengukir pada mesh tersebut, kerana ia boleh menghasilkan segi tiga yang tidak sekata.

Perhatikan bahawa kawasan bertopeng tidak akan dikurangkan.

![](/videos/decimate.mp4)

::: tip

Menggunakan [alat Quad Remesher](tools.md#quad-remesher) pada objek dengan banyak poligon boleh mengambil masa yang lama untuk dikira, dan memberikan hasil yang sukar dikawal. Memproses mesh terlebih dahulu dengan [kumpulan muka](tools.md#facegroup) dan pengurangan akan menjadikan Quad Remesher berjalan jauh lebih pantas, dan memberikan kawalan yang jauh lebih baik ke atas topologi.

* Bahagikan mesh dengan kumpulan muka untuk menentukan aliran kuad yang ideal.
* Santaikan (relax) kumpulan muka untuk mendapatkan sempadan kumpulan muka yang licin.
* Kurangkan. Ini memastikan tiada muka yang nipis atau herot pada tepi kumpulan muka. Di bawah `Kekalkan sempadan`, pastikan `Kumpulan muka` didayakan. Ini akan menjadikan tepi segi tiga mengikut tepi kumpulan muka anda dengan tepat.
* Dalam pilihan Quad Remesher, pastikan relax dimatikan (kerana anda sudah pun menyantaikan mesh) dan anda sepatutnya mendapat hasil yang baik.

:::

### Kurangkan {#decimate}
Mulakan operasi pengurangan.

Ikon di sebelah butang kurangkan menunjukkan pilihan di bawah, dan membolehkan anda menghidupkan atau mematikannya. Peratusan menunjukkan kekuatan pilihan tersebut.

* ![](/icons/palette.webp)  `Kekalkan lukisan` - Letakkan lebih banyak segi tiga di tempat yang mempunyai perincian cat.
* ![](/icons/triforce.webp) `Muka seragam` - Utamakan segi tiga yang bersaiz sekata.
* ![](/icons/hole.webp)  `Lubang` - Pengurangan akan cuba mengekalkan sempadan berhampiran geometri terbuka dan lubang tanpa perubahan.
* ![](/icons/group.webp) `Kumpulan muka` - Pengurangan akan cuba mengekalkan sempadan kumpulan muka tanpa perubahan.
* ![](/icons/uv.webp) `UV` - Pengurangan akan cuba mengekalkan sempadan UV tanpa perubahan.

### Sasaran tiga segi {#target-triangles}
Tetapkan bilangan segi tiga sasaran. Nilai lalai ialah 50%; butang peratus/sasaran bertukar antara peratusan atau bilangan poligon sasaran yang tepat.

### Pilihan {#decimate-gear-menu}
Setiap pilihan mempunyai kotak semak untuk menghidupkan atau mematikannya, dan nilai untuk kekuatannya:

#### ![](/icons/palette.webp) Kekalkan lukisan {#preserve-painting}
Nilai ini menentukan sejauh mana perincian cat dikekalkan dengan tepat. Nilai yang lebih tinggi mengekalkan lebih banyak cat. Tetapkan kepada 0 jika anda tidak kisah tentang cat.

#### ![](/icons/triforce.webp) Muka seragam {#uniform-faces}
Nilai yang lebih tinggi menghasilkan segi tiga dengan saiz yang serupa.

#### Kekalkan sempadan {#preserve-borders}
Halang sempadan daripada dikurangkan. Pemberat sempadan boleh ditetapkan untuk sempadan `Lubang`, `Kumpulan muka` atau `UV` (`UV` memerlukan objek yang mempunyai UV).

## ![](/icons/quad.webp) Remesh kuad {#quad-remesh}
![](/images/topology_quadremesh_menu.webp)
Bina semula objek dengan susun atur kuad yang kemas. Tab ini mempunyai beberapa alat remesh, masing-masing dengan butang `Remesh`, peluncur `Sasaran quad` dan menu gearnya sendiri. Cuba semuanya pada objek anda, hasilnya agak berbeza!

### Quad Remesher {#quad-remesher}
Alat remesh yang sama seperti alat [Quad Remesher](tools.md#quad-remesher), dibangunkan oleh [Exoside](https://exoside.com/). Ia hanya tersedia pada sesetengah platform, dan memerlukan pembelian: sehingga itu, butang `Remesh` memaparkan troli.

`Pilih alat` bertukar kepada alat Quad Remesher, untuk melukis panduan dan mengecat ketumpatan. Menu gear mengandungi `Kiraan Kuad Adaptif`, `Saiz Adaptif` (pada 100% saiz kuad mengikut kelengkungan, pada 0% kuad adalah seragam), `Auto-Kesan Tepi Keras` dan `Reprojek Vertex`.

::: tip
Di tempat ia tersedia, Quad Remesher secara amnya memberikan hasil terbaik dan kawalan paling banyak.
:::

### AutoRemesher {#autoremesher}
Alat remesh kuad alternatif, dengan pilihan untuk menyesuaikan saiz dan bentuk kuad dengan permukaan.

#### ![](/icons/cog.webp) Menu gear AutoRemesher {#autoremesher-gear-menu}
Menu gear mempunyai pilihan lanjutan berikut:

##### Penskalaan tepi {#edge-scaling}
Skalakan saiz kuad; nilai yang lebih tinggi menghasilkan kuad yang lebih besar.

##### Kebolehsuaian {#adaptivity}
Sesuaikan ketumpatan kuad dengan kelengkungan. 0 menghasilkan kuad seragam, 1 menghasilkan kuad yang lebih kecil di kawasan melengkung.

##### Anisotropi {#anisotropy}
Regangkan kuad sepanjang arah permukaan yang paling rata. 0 menghasilkan kuad segi empat sama, 1 menghasilkan kuad memanjang pada tiub dan rabung.

##### Tepi tajam {#sharp-edge}
Tepi yang bengkok lebih daripada sudut ini dikekalkan sebagai ciri tajam.

##### Licinkan normal {#smooth-normal}
0 mengekalkan permukaan bersegi semasa remesh. Nilai yang lebih tinggi melicinkan permukaan dengan mengambil kira normal verteks.

##### Mengisi lubang maksimum {#autoremesher-max-fill-hole}
Algoritma ini kadangkala boleh menghasilkan lubang yang tidak diingini. Jika sesuatu lubang mempunyai verteks yang lebih sedikit daripada nilai ini, ia akan diisi.

### Instant Mesh {#quad-remesh-instant}
Remesh menggunakan [algoritma Instant Meshes oleh Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Ia akan menganalisis aliran mesh dan mencipta topologi kuad yang kemas.

#### Remesh {#instant-remesh}
Mulakan operasi remesh.

#### Sasaran quad {#target-quads}
Bilangan poligon kuad yang akan cuba dicipta oleh alat remesh.

#### ![](/icons/cog.webp) Menu gear Instant Mesh {#quad-remesh-instant-gear-menu}
Menu gear mempunyai pilihan lanjutan berikut:

##### Sudut lipatan {#crease-angle}
Ambang sudut tajam yang akan cuba membantu membimbing operasi remesh. Dayakannya dengan kotak semaknya.

##### Mengisi lubang maksimum {#max-fill-hole}
Algoritma ini kadangkala boleh menghasilkan lubang yang tidak diingini. Jika sesuatu lubang mempunyai verteks yang lebih sedikit daripada nilai ini, ia akan diisi.

### QuadriFlow {#quadriflow}
Remesh menggunakan algoritma QuadriFlow, satu lagi cara untuk mendapatkan susun atur kuad yang kemas.

#### ![](/icons/cog.webp) Menu gear QuadriFlow {#quadriflow-gear-menu}
Menu gear mempunyai pilihan lanjutan berikut:

##### Kekalkan sempadan {#quadriflow-preserve-boundary}
Lindungi sempadan lubang.

##### Kekalkan ketajaman {#keep-sharp}
Jajarkan kuad dengan tepi tajam permukaan.

##### Aliran kos minimum {#min-cost-flow}
Gunakan penyelesai aliran kos minimum untuk susun atur kuad. Lebih perlahan, tetapi boleh menghasilkan topologi yang lebih teratur.

## ![](/icons/uv.webp) Buka balut UV {#uv-unwrap}
Kira koordinat tekstur (UV) bagi objek yang dipilih. Nomad mempunyai dua kaedah, `UVAtlas` dan `BFF`, masing-masing dengan butang `Nyahbalut` sendiri.

![](/videos/unwrap.mp4)

::: tip UV?
Analogi biasa untuk UV ialah membalut hadiah: apakah cara terbaik untuk memotong kertas pembalut supaya ia menutup sesuatu objek sepenuhnya, tanpa bertindih?

UV adalah serupa, tetapi bukannya memotong kertas, anda memotong objek. Bayangkan model anda diperbuat daripada plastik nipis: bagaimana anda akan memotong model anda supaya ia boleh dibuka dan dibaringkan rata, dicat dalam keadaan rata itu, kemudian dicantumkan semula?

Sekarang bayangkan permukaan model anda diperbuat daripada lycra yang boleh diregangkan. Anda boleh meregangkan model sehingga rata, atau memotongnya, atau gabungan kedua-duanya. Tetapi jika anda mengecat corak papan dam pada objek semasa ia diratakan, corak itu akan herot apabila anda mencantumkannya semula. Kaedah mana yang lebih baik, lebih banyak potongan dengan kurang herotan, atau kurang potongan dengan lebih banyak herotan?

UV ialah arahan yang memberitahu perisian 3d cara untuk 'memotong dan meregangkan' objek apabila memasang tekstur. Alat UV Atlas secara amnya menggunakan pendekatan 'lebih banyak potongan, kurang herotan'.


:::

::: tip UV dalam Nomad dan aplikasi lain

Kebanyakan model bertekstur yang anda temui dalam talian menggunakan tekstur dengan UV. Nomad boleh mengimport dan memaparkannya melalui panel [bahan](material.md#textures).

Apabila model dibuat dalam Nomad, anda boleh mengecat terus pada objek tanpa UV. Jika anda perlu mengeksportnya ke aplikasi lain, contohnya [Procreate](https://procreate.art/), anda boleh melakukan 'bake' maklumat warna Nomad ke dalam tekstur melalui UV.

:::

### UVAtlas {#uv-unwrap-uvatlas}

![](/images/topology_uvatlas_menu.webp)
UVAtlas secara amnya lebih suka menghasilkan lebih banyak pulau dengan potongan, untuk meminimumkan herotan.

#### Nyahbalut {#unwrap}
Kira UV bagi objek yang dipilih.

#### Pilihan {#uvatlas-gear-menu}
Butang di sebelah `Nyahbalut`:

##### Kumpulan muka {#atlas-face-group}
Apabila ia menunjukkan `Ya`, kumpulan muka menentukan potongan bagi UV. Tetapan ini dikongsi dengan BFF.

##### Padamkan UVs {#delete-uvs}
Butang tong sampah memadam UV objek.

##### Periksa {#uv-inspect}
Paparkan UV objek di latar belakang.

#### Regangan Maksimum {#max-stretch}
Nilai rendah menghasilkan kurang herotan dan lebih banyak pulau, nilai tinggi menghasilkan lebih banyak herotan dan kurang pulau.

#### Jarak Pulau {#island-spacing}
Jumlah ruang antara pulau. Nilai rendah membazirkan kurang ruang, tetapi berisiko tekstur meresap antara pulau.

::: warning
Pengiraan UV boleh mengambil masa; sebaiknya gunakan mesh dengan kurang daripada 100k verteks.
:::

### BFF {#uv-unwrap-bff}
![](/images/topology_uvbff_menu.webp)

UV BFF mengutamakan pendekatan 'kurang potongan, lebih banyak herotan'.

#### Pilihan {#uv-bff-gear-menu}
Butang `Kumpulan muka`, padam dan `Periksa` yang sama seperti [UVAtlas](#uvatlas-gear-menu) terletak di sebelah `Nyahbalut`.

##### Kumpulan muka {#bff-face-group}

Gunakan kumpulan muka untuk menentukan potongan bagi UV.

#### Kiraan kon {#cone-count}
Tentukan bilangan unjuran utama yang digunakan. Nilai lebih rendah menghasilkan kurang pulau, tetapi lebih banyak herotan. Nilai lebih tinggi mengambil masa lebih lama untuk dikira.

#### Tampalan lancar {#seamless-patches}
Mempengaruhi susun atur tampalan UV; ia boleh menyebabkan herotan yang ketara. Ia paling berkesan dengan kumpulan muka yang dicipta dengan teliti.

::: warning
BFF boleh menghasilkan UV yang bertindih jika mesh mempunyai pemegang (seperti lubang pada donat).
:::

### ![](/icons/preview.webp) Tunjuk UV selepas nyahbalut {#show-uv-after-unwrap}
Buka paparan pemeriksa UV selepas nyahbalut, supaya anda boleh menyemak hasilnya dengan segera.

### ![](/icons/bake.webp) Bake: Tekstur → Tekstur {#unwrap-bake-texture}
Hanya tersedia apabila bahan objek mempunyai tekstur. Apabila anda menyahbalutnya semula, tekstur dipindahkan ke UV baharu, jadi ia masih sepadan. Resolusinya `Auto` secara lalai, sepadan dengan tekstur terbesar, atau anda boleh menetapkannya sendiri.

## ![](/icons/bake.webp) Bake {#bake}
Tab ini memindahkan perincian dan cat antara objek, dan antara verteks dan tekstur.

`Daripada resolusi tinggi` menggunakan objek lain sebagai sumber; nombor dalam kurungan ialah bilangannya. Nomad memilihnya seperti berikut:

- semua objek yang dipilih digunakan, dan objek pilihan utama ialah sasaran (serlahan paling kuat dalam menu [Adegan](scene.md))
- jika hanya satu objek dipilih, Nomad menggunakan semua objek yang kelihatan sebaliknya
- jika setiap objek lain disembunyikan (contohnya dengan Solo), keseluruhan adegan digunakan

### ![](/icons/bake.webp) Bake → Tekstur {#bake-texture}
![](/images/topology_bake_menu.webp)

Bake tekstur akan mencipta tekstur dengan mengunjurkan objek lain yang kelihatan dalam adegan ke dalam UV objek yang dipilih. Objek tersebut memerlukan UV.

Berikut ialah aliran kerja biasa untuk bake:
- Anda mempunyai mesh dengan perincian halus dan cat
- Klonkannya
- Kurangkannya (tetapkan `Kekalkan lukisan` kepada 0)
- Buka balut UV-nya
- Bake!

Kini anda sepatutnya mempunyai mesh beresolusi rendah yang mengekalkan kebanyakan cat dan perincian objek asal anda.

Selepas operasi, warna verteks akan dipindahkan ke lapisan baharu yang dinyahaktifkan, supaya ia tidak mengganggu tekstur.

#### Daripada objek ini {#tex-from-itself}
Bake objek ke atas UV-nya sendiri: catnya menjadi tekstur, dan jika ia mempunyai tahap multiresolusi, perincian tahap tertinggi di-bake ke atas tahap semasa (ikon multires kemudian dipaparkan pada butang). Ini mudah disediakan, tetapi selalunya anda memerlukan lebih banyak kawalan, dan dalam kes itu pilihan seterusnya lebih berguna.

#### Daripada resolusi tinggi {#tex-from-high-res}
Bake daripada objek lain ke objek yang dipilih. Nombor dalam kurungan menunjukkan bilangan objek lain yang akan digunakan sebagai sumber resolusi tinggi, dan di-bake ke dalam objek resolusi rendah semasa yang mempunyai UV. Objek lain tidak perlu mempunyai susun atur atau topologi yang serupa dengan objek yang di-bake, jadi aliran kerja bake boleh menjadi sangat fleksibel.

#### Resolusi {#tex-bake-resolution}
Resolusi tekstur yang di-bake. Tekstur bake sentiasa segi empat sama, jadi 1024 akan menghasilkan imej 1024x1024.

Butang di bawah ialah pintasan untuk resolusi yang kerap digunakan. Sebagai rujukan, 512x512 agak kecil, contohnya untuk grafik web dan geometri ringkas. 4096x4096 (ringkasnya 4k) adalah untuk render berkualiti tinggi.

#### Warna, Kekasaran, Kemetalan, Normal, Sesaran, Pancaran, Kelegapan {#tex-normal-roughness-metalness-color-emissive-opacity}
Butang-butang ini menentukan sifat yang akan di-bake, setiap satu ke dalam peta yang berasingan. Selepas bake selesai, peta ini akan ditambah sebagai tekstur pada bahan objek semasa. `Sesaran` melakukan bake ketinggian perincian sebagai peta sesaran.

#### ![](/icons/cog.webp) Menu gear Bake {#tex-bake-gear-menu}
![](/images/topology_bake_gear_menu.webp)
Menu gear mempunyai pilihan lanjutan berikut:

##### Sandarkan {#tex-backup}
Untuk mempratonton tekstur yang di-bake, maklumat cat objek perlu dinyahaktifkan. `Sandarkan (Pewarnaan → Lapisan)` akan memindahkan sebarang maklumat cat ke lapisan baharu sebagai sandaran supaya ia boleh didayakan/dinyahaktifkan dengan mudah.

##### Gunakan multires {#tex-use-multires}
Untuk `Daripada objek ini` pada objek yang mempunyai tahap multiresolusi. Nomad membaca resolusi tinggi melalui tahap pembahagian dan bukannya memancarkan sinar: ia lebih pantas dan bebas daripada ralat unjuran. Matikannya untuk melakukan bake dengan pilihan di bawah.

##### Asas licin {#tex-smooth-base}
Untuk `Sesaran` pada objek yang mempunyai tahap multiresolusi. Mengukur sesaran daripada asas yang dibahagikan dan bukannya daripada muka ratanya. Biarkan ia hidup apabila peta sesaran akan digunakan pada mesh yang dibahagikan, seperti pembahagian adaptif Blender.

##### Jarak carian {#tex-cage-radius}
Jarak maksimum yang digunakan untuk mencari permukaan sumber. Secara lalai, jarak ini dikekalkan rendah untuk mengelakkan artifak, tetapi boleh ditambah jika objek sasaran jauh dari objek bake.

##### Unjuran {#tex-projection}
Cara permukaan sumber dicari:

* `Sinar` - Unjur sepanjang normal permukaan.
* `Sinar + terdekat` - Gunakan sinar normal, kemudian gunakan permukaan terdekat jika sinar tersasar.
* `Terdekat` - Unjur ke titik terdekat pada permukaan sumber.

##### Ofset sinar {#tex-ray-offset}
Laraskan titik permulaan pengiraan bake pada objek bake. Ofset kecil dari permukaan mengelakkan kebanyakan artifak biasa. Jika objek sasaran sangat jauh dari objek bake, ofset ini mungkin perlu ditambah. Ia tidak digunakan oleh `Terdekat`.


### ![](/icons/bake.webp) Unjur semula → Verteks {#reproject-to-vertex}

![](/images/topology_reproject_menu.webp)

Unjurkan perincian ukiran, cat, lapisan dan tekstur ke dalam nilai verteks.

Ia boleh dianggap sebagai kebalikan bake; jika bake memindahkan sifat verteks ke tekstur, unjur semula memindahkan tekstur (dan sifat lain)
 kembali ke dalam verteks.

::: tip
Apabila menggunakan `Bake → Tekstur` atau `Unjur semula → Verteks`, kedua-dua warna verteks dan tekstur bahan akan diambil kira.
:::

#### Daripada objek ini {#vertex-from-itself}
Tukar tekstur daripada bahan kepada nilai verteks. Butang ini hanya aktif jika objek mempunyai UV, dan tekstur aktif dalam bahan.

::: tip PETUA: Mengecat tekstur
Nomad tidak menyokong pengecatan dan penyuntingan tekstur secara langsung, tetapi hasil yang sangat serupa boleh dicapai dengan mengunjurkan tekstur -> nilai verteks, mengecat pada verteks, kemudian bake verteks -> tekstur:

1. Sediakan objek dengan sedikit poligon yang mempunyai UV
1. Muatkan tekstur ke dalam bahannya
1. Bahagikan ia secukupnya untuk dicat
1. `Unjur semula → Verteks` dalam mod `Daripada objek ini`; kini tekstur telah ditukar kepada nilai verteks
1. Cat, licinkan, smudge, cop, lakukan apa sahaja suntingan yang anda perlukan
1. `Bake → Tekstur`, dalam mod `Daripada objek ini`. Suntingan tersebut ditukar semula menjadi tekstur.
:::

#### Daripada resolusi tinggi {#vertex-from-high-res}
Tukar objek lain kepada nilai verteks pada objek yang dipilih. Nombor pada butang ini menunjukkan bilangan objek sumber. Ini terutamanya bertujuan untuk digunakan pada mesh beresolusi tinggi juga, biasanya dengan topologi yang kemas.

::: tip
Mengunjur semula objek lain bukan sahaja boleh digunakan untuk memindahkan maklumat warna daripada objek lain, tetapi juga untuk mengunjurkan verteks ke atas objek lain, contohnya pembalut boleh diunjurkan ke atas watak.
:::

#### Bucu, Warna, Kekasaran, Kemetalan, Kelegapan, Topeng, Lapisan, Kumpulan muka {#vertex-vertices-roughness-metalness-color-opacity-opacity-mask-mask-layers-face-group}
Butang-butang ini menentukan sifat yang akan diunjurkan ke objek yang dipilih. `Lapisan` memindahkan lapisan lain ke atas mesh yang dipilih.

#### ![](/icons/cog.webp) Menu gear Unjur semula {#vertex-reproject-gear-menu}
Menu gear mempunyai pilihan lanjutan berikut:

##### Kelegapan → Topeng {#vertex-opacity-to-mask}
Tukar kelegapan sumber menjadi topeng pada objek yang dipilih.

##### Ulangan {#vertex-iterations}
Berapa kali operasi santai patut digunakan semasa unjur semula. Hanya digunakan apabila `Bucu` dihidupkan.

##### Santai {#vertex-relax}
Susun atur mesh yang dipilih boleh dilicinkan atau disantaikan pada kadar tertentu supaya lebih sepadan dengan sasaran unjur semula. `Lancar` lebih baik untuk mesh dengan banyak poligon, `Santai` lebih baik untuk mesh dengan sedikit poligon. `Auto` membiarkan Nomad menentukan kaedah terbaik.

##### Jarak carian {#vertex-cage-radius}
Jarak maksimum yang digunakan untuk mencari permukaan sumber. Secara lalai, jarak ini dikekalkan rendah untuk mengelakkan artifak, tetapi boleh ditambah jika objek sasaran jauh dari objek yang dipilih.

##### Unjuran {#vertex-projection}
Cara permukaan sumber dicari:

* `Sinar` - Unjur sepanjang normal permukaan.
* `Campuran penyesuaian` - Campurkan sinar normal dan permukaan terdekat mengikut jarak dan `Keutamaan sinar`. Jika satu tersasar, gunakan yang satu lagi.
* `Terdekat` - Unjur ke titik terdekat pada permukaan sumber.

##### Keutamaan sinar {#vertex-ray-bias}
Hanya untuk `Campuran penyesuaian`. Nilai yang lebih tinggi mencondongkan campuran ke arah hasil sinar normal, nilai yang lebih rendah ke arah titik terdekat.

##### Ofset sinar {#ray-vertex-offset}
Laraskan titik permulaan pengiraan bake pada objek yang dipilih. Ofset kecil dari permukaan mengelakkan artifak tertentu. Jika objek sasaran sangat jauh dari objek bake, ofset ini mungkin perlu ditambah. Ia tidak digunakan oleh `Terdekat`.

### ![](/icons/bake.webp) Bake → VDM {#bake-vdm}
Cipta cop VDM (anjakan vektor) daripada objek yang dipilih dan tambahkannya ke pustaka VDM. Anda akan diminta memberikan nama.

Berikut ialah aliran kerja biasa:
- Tambah satah, atau pilih `VDM baharu` dalam pemilih VDM untuk menambah satah yang sudah dikonfigurasi (primitif [VDM](scene.md#add-menu))
- Ukir bentuk anda padanya, dengan mengekalkan sempadannya rata
- Bake!

UV satah menentukan segi empat sama yang di-bake, jadi objek memerlukan UV. Pilih saiz cop dengan `Resolusi`, dan pilih dengan `Warna`, `Kekasaran`, `Kemetalan` dan `Kelegapan` apa yang dibawa oleh cop selain anjakan.

::: tip
Elakkan DynTopo pada satah, kerana ia merosakkan UV-nya dan cop akan menjadi herot. Mengukir dalam lapisan memberikan hasil yang paling tepat, kerana satah rata masih ada di bawahnya. Mengecat juga memerlukan lapisan; jika tidak, bahan akan dicop pada keseluruhan segi empat sama dan bukan hanya di tempat yang anda cat.
:::

## ![](/icons/dot.webp) Primitif {#primitive}
Parameter bagi primitif yang dipilih. Kebanyakannya juga tersedia daripada butang `…` pada bar alat ruang pandang primitif.

![](/images/topology_primitive_screenshot.webp)
