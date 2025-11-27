# ![](/icons/multires.webp) Topologi 

Menu ini mengawal topologi objek dalam Nomad, serta alat untuk membakar (bake) dan memindahkan butiran antara objek, dan antara tekstur.

![](/images/topology_overview.webp)

Nomad berasaskan poligon, ia menggunakan segi tiga dan segi empat (quad) untuk mengendalikan geometri.
Dengan topologi, kita merujuk kepada kedua-dua bilangan permukaan (faces) dan juga cara titik (vertex) disambungkan.

Adalah penting untuk menjejak topologi, terutamanya jika anda mahu mengukir atau mengecat butiran halus.

::: tip Bagaimana menjejak topologi anda?
Anda boleh memaparkan [Wireframe](settings.md#wireframe) atau hanya nyahaktifkan [Smooth Shading](settings.md#smooth-shading).
:::

![](/images/topology_top.webp)

Menu topologi Nomad mempunyai beberapa bahagian:

| Method                                | Icon                         | Description                                                      |
| :-----------------------------------: | :--------------------------: | :--------------------------------------------------------------: |
| [Multiresolution](#multiresolution)   | ![](/icons/multires.webp)   | Edit beberapa tahap butiran menggunakan subdivision              |
| [Voxel Remesher](#voxel-remesher)     | ![](/icons/voxel.webp)      | Kira semula topologi baharu dengan ketumpatan seragam            |
| [Dynamic Topology](#dynamic-topology) | ![](/icons/dynamic.webp)    | Tambah/Buang permukaan secara setempat dalam masa nyata ketika mengukir atau mengecat |
| [Misc](#misc)                         | ![](/icons/topo_extra.webp) | Decimation, UV, baking, remeshing, reprojection                  |
| [Primitive](#msc)                     | ![](/icons/dot.webp)        | Pilihan primitif                                                 |


## Statistik poligon

![](/images/topology_stats.webp)

Bahagian atas menu topologi memaparkan maklumat poligon untuk objek terpilih dan keseluruhan senario (scene). Nombor menunjukkan jumlah keseluruhan vertex, jumlah keseluruhan segi tiga, dan jumlah keseluruhan quad (poligon 4 sisi).

Mengetik pada bahagian ini akan memaparkan senarai statistik poligon untuk semua objek poligon dalam senario.

## ![](/icons/multires.webp) Multiresolution

![](/images/topology_multires_menu.webp)

### Apa itu multiresolution?
Fungsi multiresolution berguna untuk dua senario utama:
- Algoritma subdivision licin untuk meningkatkan bilangan poligon objek anda
- Mengendalikan beberapa tahap resolusi supaya anda boleh bergilir antara suntingan skala kecil dan besar

![](/videos/multiresolution.mp4)

#### Aliran kerja multiresolution
Satu aspek penting multiresolution ialah anda boleh kembali ke resolusi lebih rendah, membuat perubahan pada objek dan kemudian kembali ke resolusi tertinggi tanpa kehilangan butiran resolusi tinggi. Semua butiran resolusi tinggi akan diproyeksikan secara automatik.

::: warning
Jika anda menggunakan alat yang mengubah topologi objek anda, anda akan kehilangan semua resolusi lain objek anda!
Anda sepatutnya sentiasa mendapat amaran jika ini bakal berlaku, contohnya apabila anda menggunakan:
- [Voxel Remesher](#voxel-remesher)
- [Dynamic Topology](#dynamic-topology)
- [Trim tool](tools.md#trim)
- [Split tool](tools.md#split)
:::


### Peluncur multiresolution
Peluncur ini menunjukkan bilangan tahap subdivision dalam objek semasa. Jika terdapat 6 bar menegak, terdapat 6 tahap subdivision. Bulatan menunjukkan tahap subdivision yang sedang dipaparkan. 

### Reverse
Apabila berada pada tahap subdivision paling rendah, butang reverse akan cuba mencipta satu tahap di bawah tahap semasa. Perlu diingat ini biasanya hanya boleh berlaku jika objek itu dicipta dengan subdivision dari awal, contohnya dalam Nomad atau aplikasi 3D lain yang menyokong permukaan subdivision multiresolution.

### Subdivide
Butang *Subdivide* akan meningkatkan bilangan poligon sebanyak 4 kali ganda, jadi pastikan anda memantau bilangan poligon kerana ia boleh meningkat dengan sangat cepat!
Satu aspek penting *Subdivision Surface* ialah ia akan menumpu kepada *Smooth Surface*.
Untuk memahami cara ia berfungsi, anda boleh cuba butang *Subdivide* pada objek dengan hanya beberapa poligon.

Anda boleh nyahaktifkan kelakuan *Smooth* ini dengan menanda pilihan `Linear subdivision`.

### Delete lower
Jika terdapat subdivision di bawah tahap yang sedang dipaparkan, padamkannya. Jika anda melakukannya secara tidak sengaja, anda boleh menciptanya semula dengan butang Reverse.

### Delete higher
Jika terdapat subdivision di atas tahap yang sedang dipaparkan, padamkannya.

### Linear subdivision
Subdivide mesh tanpa menggunakan pelicinan.

### Sharp border
Jika objek anda mempunyai facegroup, mengaktifkan pilihan ini akan mengekalkan sempadan facegroup tajam. Ini boleh ditetapkan pada setiap tahap subdivision (peluncur subdivision akan mempunyai ikon kecil di atas tahap untuk menunjukkan perkara ini).

### Keep triangles
Kebanyakan sistem subdivision surface piawai akan cuba menukar semua poligon kepada quad semasa operasi subdivision. Togol ini akan memaksa subdivision menggunakan segi tiga sebaliknya.

### Lock (LV0)

Menghalang tahap subdivision paling rendah daripada diubah suai. Ini boleh menjadi penting jika objek anda dijana dalam aplikasi lain, dan objek asas perlu kekal tidak berubah. Apabila pilihan ini dinyahaktifkan, perubahan besar yang dibuat pada tahap subdivision lebih tinggi akan menggerakkan tahap 0.

::: tip 

Subdivision akan melicinkan semua tepi tajam secara lalai. Untuk mengekalkan tepi sedikit tajam, cuba gunakan linear subdivision atau Sharp border pada 2 tahap subdivision pertama, kemudian matikannya untuk tahap lebih tinggi. Ini akan menghasilkan mesh subdivided separa tajam.

:::


## ![](/icons/voxel.webp) Voxel Remesher
![](/images/topology_voxel_menu.webp)
Apabila menggunakan `Voxel Remesher`, keseluruhan mesh akan memaksa topologi mempunyai resolusi seragam, bermakna semua poligon mempunyai saiz lebih kurang sama. Ini sangat berguna apabila anda tidak mahu memikirkan topologi dan hanya mahu mengukir bebas (free-form sculpting).

Aliran kerja mengukir tipikal boleh bermula dengan menggunakan `Voxel Remesher` untuk membentuk kasar (block-out) dengan resolusi rendah.
Hanya tekan butang *Remesh* sekali-sekala apabila anda meregangkan mesh terlalu banyak untuk mengelakkan herotan berlebihan.

![](/videos/voxel_remesher.mp4)


::: tip Voxel?
Seperti dinyatakan di atas, Nomad ialah perisian poligon, tetapi `Voxel Remesher` ialah satu pengecualian di mana pendekatan lain digunakan (sementara) untuk melakukan remeshing.

Satu perbezaan besar ialah pendekatan voxel tidak menerima self intersection, jadi ia akan diselesaikan.
Ia juga tidak menyokong mesh yang mempunyai lubang.

Dengan lubang, kita tidak maksudkan `genus hole` (`hole` pada donut), tetapi sebaliknya mesh yang tidak `watertight`/`closed`.
Kebiasaannya, ini bermakna sebelum menggunakan remeshing, setiap lubang akan diisi, sama seperti [Trim tool](tools.md#trim) atau [Hole filling feature](scene.md#hole-filling).
:::

### Remesh
Laksanakan voxel remesh.

### Resolution
Saiz voxel yang digunakan semasa pengiraan. Semasa menukar parameter ini, corak papan dam (checkerboard) akan ditindih pada mesh untuk memberikan pratonton hasil.

### Build multiresolution
Cipta tahap multiresolution lebih rendah untuk voxel remesh. Jika anda menggunakan corak papan dam untuk menetapkan resolusi, dan tetapkan build multiresolution kepada 2, hasil akhir akan mempunyai butiran yang sepadan dengan peluncur resolusi, dan jika anda pergi ke tab multires, ia akan berada pada tahap 2, bermakna anda mempunyai mesh multires resolusi lebih rendah pada tahap 1 dan tahap 0. Ini boleh menjadi cara yang baik untuk menjana mesh bersih dengan poligon sekata, dan mempunyai mesh kawalan resolusi rendah.

::: tip Tip: Build multiresolution dan stable smoothing

Pilihan ini kadangkala boleh menyebabkan 'gelung' dalam geometri yang sukar untuk dilicinkan, menyebabkan bonjolan kecil. Jika ini berlaku, aktifkan 'Stable smoothing' dalam pilihan alat smooth. 

:::

### Keep sharp edges
Aktifkan snapping titik baharu kepada tepi tajam pada mesh asal. Ia boleh memperkenalkan herotan.

## ![](/icons/dynamic.webp) Dynamic Topology

![](/images/topology_dyntopo_menu.webp)
Multiresolution dan voxel remeshing ialah kaedah industri biasa untuk mengawal topologi, tetapi kedua-duanya memerlukan anda memerhati supaya anda tidak meregangkan poligon terlalu jauh, atau memampatkan poligon terlalu rapat. 

Dynamic Topology ialah kaedah alternatif. Semasa anda mengukir, Nomad akan secara adaptif menambah dan membuang poligon semasa sapuan berus, jadi mengukir butiran kecil akan menambah banyak poligon kecil di tempat yang anda perlukan, dan melicinkan di tempat lain akan membuang poligon.

Perlu diingat bahawa dynamic topology akan menggunakan poligon segi tiga dan bukannya quad. Ini boleh kelihatan agak berselerak, tetapi selalunya lebih baik untuk tidak melihat wireframe, hanya tumpukan pada menghasilkan ukiran yang kelihatan baik tanpa risau tentang topologi, kemudian kemudian anda boleh menggunakan salah satu alat remeshing lain Nomad untuk menjana mesh quad yang bersih.

Lihat video di bawah dalam tindakan.

![](/videos/dynamic.mp4)

### Enabled
Hidupkan dynamic topology. Ikon DynTopo akan diletakkan di bawah peluncur jejari dan intensiti berus untuk membolehkan anda togol Dyntopo bagi setiap alat.

### Detail
Mengawal jumlah butiran, kelakuannya berubah berdasarkan pilihan 'Detail based on...', lihat di bawah.

### Detail based on...
| Method   | Description                                                     |
| :------: | :-------------------------------------------------------------: |
| Screen   | Tahap butiran bergantung pada betapa besar objek di skrin. Peluncur detail ialah 100% atau lebih tinggi untuk butiran halus, menghasilkan segi tiga kecil, atau 1% untuk butiran rendah, menghasilkan segi tiga besar.  |
| Radius   | Jejari alat menentukan jumlah butiran. Gunakan jejari alat kecil untuk butiran halus, jejari alat besar untuk butiran rendah. Peluncur detail ialah pengganda pada nisbah ini.                     |
| Constant | Peluncur detail menentukan jumlah butiran, dan tidak dipengaruhi oleh saiz skrin atau saiz alat.             |

::: tip TIP: Mod Radius

Untuk mendapatkan gambaran lebih baik tentang cara mod radius berfungsi, mula gerakkan peluncur detail dengan satu jari, kemudian pada masa yang sama ubah jejari alat dengan jari lain. Anda akan nampak bagaimana ia berkait.

:::

### Prefer...
| Method  | Description       |
| :-----: | :---------------: |
| Speed   | Utamakan prestasi |
| Quality | Utamakan kualiti  |

Apabila anda mengutamakan `Quality`, 2 perbezaan utama ialah:
- penapisan (refinement) digunakan sebelum mengukir, jadi anda akan mendapat kurang artifak interpolasi apabila mengecat atau mengukir butiran sangat kecil
- penapisan berjalan sehingga ia menumpu kepada tahap butiran yang betul, berbeza dengan kelakuan bertambah (incremental).
 
Dengan cara itu, jika anda mengukir butiran sangat kecil atau membuat sapuan pantas, topologi akan sentiasa ditapis seperti yang dijangka


### Use pressure on radius
Hanya relevan jika `Radius` diaktifkan. Apabila diaktifkan, tahap butiran akan sentiasa mencerminkan saiz berus, walaupun saiz berus dipengaruhi oleh tekanan pensel.

### Use stroke falloff

Juga sertakan lengkung falloff berus dan alpha dalam pengiraan dyntopo.

### Method
Sama ada anda menggunakan `Dynamic Topology` pada [Brush](#brush) atau [Globally](#global), anda boleh memilih mod operasinya:

| Method         | Description                                                           |
| :------------: | :-------------------------------------------------------------------: |
| Uniformisation | Ia boleh menambah dan membuang permukaan, ini ialah mod yang digunakan dalam video di atas |
| Subdivision    | Hanya menambah permukaan baharu, tidak boleh membuang permukaan       |
| Decimation     | Hanya membuang permukaan, tidak boleh menambah permukaan              |

### Protect masked area
Aktifkan kawasan bertopeng (masked) untuk melindungi topologi daripada diubah.

### Vertex extrapolation


### Detail
Resolusi yang digunakan untuk operasi remesh. Jika Dyntopo berada dalam mod 'Constant', ia akan menjadi nilai yang sama seperti peluncur Detail di bahagian atas menu ini.

### Remesh
Laksanakan remesh global menggunakan algoritma dyntopo. Biasanya anda patut menggunakan [Voxel Remesher](#voxel-remesher) untuk remeshing penuh.

Namun satu kelebihan berbanding voxel ialah kawasan bertopeng akan dilindungi, jadi anda boleh mempunyai kawalan lebih baik di mana untuk meletakkan lebih atau kurang ketumpatan.



## ![](/icons/topo_extra.webp) Misc

![](/images/topology_misc_menu.webp)

##### ![](/icons/cog.webp) Menu gear
Banyak alat dalam menu ini mempunyai pilihan tambahan. Ia boleh diakses melalui ikon gear di sebelah tajuk bahagian.

### Decimation

![](/images/topology_decimation.webp)

Kurangkan bilangan poligon dengan cuba mengekalkan sebanyak mungkin butiran, menggunakan poligon segi tiga.

Fungsi ini boleh berguna jika anda mahu mengeksport untuk cetakan 3D.
Walau bagaimanapun anda mungkin tidak patut menggunakannya jika anda mahu terus mengukir padanya, kerana ia boleh menghasilkan segi tiga tidak sekata.

Perlu diingat bahawa kawasan bertopeng tidak akan didecimate.

![](/videos/decimate.mp4)

::: tip

Menggunakan [Quadremesh tool](tools.md#quad-remesher) pada objek poligon tinggi boleh mengambil masa yang lama untuk dikira, dan memberikan hasil yang sukar dikawal. Pra-proses mesh dengan [facegroups](tools.md#facegroup-1) dan decimate akan menjadikan Quadremesh berjalan jauh lebih pantas, dan membenarkan lebih banyak kawalan ke atas topologi.

* Facegroup mesh untuk menentukan aliran quad ideal anda.
* Facegroup relax untuk mendapatkan sempadan facegroup yang licin.
* Decimate. Ini akan memastikan anda tidak mempunyai permukaan nipis atau terherot pada tepi facegroup. Dalam tetapan decimate pastikan facegroup diaktifkan. Ini akan membuat tepi segi tiga mengikut tepi facegroup anda dengan tepat.
* Dalam pilihan Quadremesh pastikan relax dinyahaktifkan (kerana anda sudah melicinkan mesh) dan anda sepatutnya mendapat hasil yang baik.

:::

#### Decimate
Mulakan operasi decimate.

Ikon di sebelah butang decimate membolehkan anda togol pilihan yang mempengaruhi decimation. Peratusan menunjukkan sekuat mana pilihan itu, dan boleh ditetapkan dalam menu gear lanjutan.

* ![](/icons/palette.webp)  `Preserve Painting` - Letakkan lebih banyak segi tiga di tempat terdapat butiran lukisan.
* ![](/icons/triforce.webp) `Uniform Faces` - Lebih suka menghasilkan segi tiga bersaiz sekata.
* ![](/icons/hole.webp)  `Preserve Geometry Borders` - Decimate akan cuba mengekalkan sempadan berhampiran geometri terbuka dan lubang tidak berubah.
* ![](/icons/facegroup.webp) `Preserve Facegroup Borders` - Decimate akan cuba mengekalkan sempadan facegroup tidak berubah.
* ![](/icons/checkerboard.webp) `Preserve UV Borders` - Decimate akan cuba mengekalkan sempadan UV tidak berubah.

#### ![](/icons/cog.webp) Menu gear Decimate
Menu gear mempunyai pilihan lanjutan berikut:
##### Preserve painting
Kotak semak akan menogol mod ini, nilai akan menentukan sejauh mana butiran lukisan akan dipelihara. Nilai lebih tinggi akan memelihara lebih banyak lukisan. Tetapkan kepada 0 jika anda tidak peduli tentang lukisan.


##### Uniform faces
Kotak semak akan menogol mod ini. Nilai lebih tinggi akan menghasilkan segi tiga dengan saiz serupa.

##### Preserve borders
Aktifkan untuk menghalang sempadan daripada didecimate. Berat sempadan boleh dipilih untuk sempadan `Geometry`, `Face Group` atau `UV`.

#### Target triangles
Tetapkan sasaran bilangan segi tiga. Nilai lalai ialah 50%, butang percent/target akan menogol antara peratusan atau kiraan poligon sasaran tepat.



### UV Unwrap - UVAtlas

![](/images/topology_uvatlas_menu.webp)
Kira koordinat tekstur (UV) untuk mesh semasa, secara umum lebih suka menghasilkan lebih banyak pulau (islands) dengan potongan, untuk meminimumkan herotan.

Ikon mata kecil antara tajuk menu dan menu gear akan menogol pratonton UV pada objek.

![](/videos/unwrap.mp4)

#### Unwrap
Kira UV untuk objek terpilih, yang akan dipaparkan di latar belakang.

#### Delete UVs
Padam UV pada objek.

#### ![](/icons/cog.webp) Menu gear UVAtlas
Menu gear mempunyai pilihan lanjutan berikut:

#### Face Group

Gunakan facegroup untuk menentukan potongan bagi UV.

##### Max Stretch
Nilai rendah menghasilkan kurang herotan dan lebih banyak pulau, nilai tinggi menghasilkan lebih banyak herotan dan kurang pulau. 

##### Island spacing
Jumlah jarak (padding) antara pulau. Nilai rendah akan membazirkan kurang ruang, tetapi berisiko tekstur bocor antara pulau. 

::: warning
Mengira UV boleh mengambil masa, adalah terbaik mempunyai mesh dengan kurang daripada 100k vertex.
:::

::: tip UV?
Analogi biasa untuk UV ialah membalut hadiah; apakah cara terbaik untuk memotong kertas pembalut untuk menutup sepenuhnya objek, tanpa pertindihan? 

UV adalah serupa, tetapi bukannya memotong kertas, anda memotong objek. Bayangkan jika model anda diperbuat daripada plastik nipis, bagaimana anda akan memotong model anda untuk membukanya supaya ia rata, mengecatnya dalam keadaan rata, kemudian memasangnya semula?

Sekarang bayangkan permukaan model anda diperbuat daripada lycra yang boleh diregang. Anda boleh meregangkan model supaya rata, atau memotongnya, atau gabungan kedua-duanya. Tetapi jika anda melukis papan dam pada objek ketika diratakan, papan dam itu akan terherot apabila anda memasangnya semula. Mana satu kaedah lebih baik, lebih banyak potongan dengan kurang herotan, atau kurang potongan dengan lebih herotan?

UV ialah arahan untuk memberitahu perisian 3D bagaimana untuk 'memotong dan meregangkan' objek apabila menggunakan tekstur. Alat UV Atlas secara umum menggunakan pendekatan 'lebih banyak potongan, kurang herotan'.


:::

::: tip UV dan Nomad dan aplikasi lain

Kebanyakan model bertekstur yang anda temui dalam talian akan bertekstur dengan UV. Nomad boleh mengimport dan memaparkannya melalui panel [material](material#textures).

Apabila model dibuat dalam Nomad, anda boleh mengecat terus pada objek tanpa UV. Jika anda perlu mengeksportnya ke aplikasi lain, contohnya [Procreate](https://procreate.art/), anda boleh 'bake' maklumat warna Nomad ke dalam tekstur melalui UV. 

:::

### UV Unwrap - BFF
![](/images/topology_uvbff_menu.webp)

UV BFF mengutamakan pendekatan 'kurang potongan, lebih herotan'. 

#### ![](/icons/cog.webp) Menu gear UV BFF

#### Face Group

Gunakan facegroup untuk menentukan potongan bagi UV.

##### Cone count
Tentukan bilangan unjuran utama yang digunakan. Nilai lebih rendah akan menghasilkan kurang pulau, tetapi lebih banyak herotan.

##### Seamless patches
Mempengaruhi susun atur tampalan UV, berfungsi paling baik dengan facegroup yang dibuat dengan teliti.

### Bake -> texture 
![](/images/topology_bake_menu.webp)

Texture baking akan mencipta tekstur dengan memproyeksikan objek lain yang kelihatan dalam senario ke dalam UV objek terpilih.

Berikut ialah aliran kerja tipikal untuk baking:
- Anda mempunyai mesh dengan butiran halus dan lukisan
- Klon ia
- Decimate ia (tetapkan `Preserve painting` kepada 0)
- UV unwrap ia
- Bake!

Secara lalai Nomad akan mengambil kira setiap mesh yang kelihatan dalam senario.
Anda juga boleh menggunakan mod Solo untuk dengan cepat menyembunyikan kebanyakan mesh lain.
Jika tiada objek lain yang kelihatan, maka ia akan mengambil keseluruhan senario sebagai kiraan.

Anda kini sepatutnya mempunyai mesh resolusi rendah yang mengekalkan kebanyakan cat dan butiran objek anda sebelum ini.

Selepas operasi, warna vertex akan dipindahkan ke lapisan baharu yang dinyahaktifkan, supaya ia tidak mengganggu tekstur.

#### From itself
Bake tahap multiresolution tertinggi ke tahap terendah pada objek semasa. Ini mudah disediakan, tetapi selalunya anda memerlukan lebih kawalan, dalam kes itu pilihan seterusnya lebih berguna.

#### From high-res ()
Bake daripada objek lain yang kelihatan dalam senario ke objek terpilih. Nombor dalam kurungan menunjukkan bilangan objek lain yang kelihatan yang akan digunakan sebagai sasaran resolusi tinggi, dan dibake ke dalam objek resolusi rendah semasa dengan UV. Objek lain tidak perlu serupa dari segi susun atur atau topologi dengan objek yang dibake, membenarkan aliran kerja bake yang pelbagai.

#### Resolution
Resolusi tekstur bake. Tekstur bake sentiasa segi empat sama, jadi 1024 akan menghasilkan imej 1024x1024. 

Butang di bawah ialah pintasan untuk resolusi yang biasa digunakan. Sebagai rujukan, 512x512 agak kecil, contohnya untuk grafik web dan geometri ringkas. 4096x4096 (ringkasnya 4k) adalah untuk render berkualiti tinggi.

#### ![](/icons/cog.webp) Menu gear Bake
![](/images/topology_bake_gear_menu.webp)
Menu gear mempunyai pilihan lanjutan berikut:

##### Normal, Roughness, Metalness, Color, Emissive, Opacity
Kotak semak ini akan menentukan sifat mana yang akan dibake, setiap satu ke dalam peta berasingan. Selepas bake selesai, ini akan ditambah sebagai tekstur kepada material objek semasa.

##### Backup
Untuk pratonton tekstur bake, maklumat cat objek perlu dinyahaktifkan. Pilihan ini akan memindahkan sebarang maklumat cat ke lapisan baharu sebagai sandaran supaya ia boleh diaktif/nyahaktif dengan mudah.

#### Cage radius
Laraskan sejauh mana dari objek bake sinar dihantar untuk mencari objek sasaran. Secara lalai jarak ini dikekalkan rendah untuk mengelakkan artifak, tetapi boleh ditingkatkan jika objek sasaran jauh dari objek bake.

##### Ray offset
Laraskan di mana pengiraan bake bermula pada objek bake. Secara lalai ia bermula 5% jauh dari permukaan, yang mengelakkan kebanyakan artifak biasa. Jika objek sasaran sangat jauh dari objek bake, offset ini mungkin perlu ditingkatkan.


### Reproject to vertex

![](/images/topology_reproject_menu.webp)

Projek butiran ukiran, lukisan, lapisan, tekstur ke dalam nilai vertex.

Ia boleh dianggap sebagai songsangan baking; jika baking memindahkan sifat vertex ke tekstur, reproject memindahkan tekstur (dan sifat lain)
 kembali ke vertex.

::: tip
Apabila menggunakan `Bake to texture` atau `Reproject to vertex`, kedua-dua warna vertex dan tekstur material akan diambil kira.
:::

#### From itself
Tukar tekstur daripada material kepada nilai vertex. Butang ini hanya akan aktif jika objek mempunyai UV, dan tekstur aktif dalam material.

::: tip TIP: Texture painting
Nomad tidak secara langsung menyokong pengecatan dan penyuntingan tekstur, tetapi hasil yang sangat serupa boleh dicapai dengan memproyeksikan tekstur -> nilai vertex, mengecat pada vertex, kemudian bake vertex -> tekstur:

1. Sediakan objek poligon rendah dengan UV
1. Muatkan tekstur ke dalam materialnya
1. Subdivide secukupnya untuk boleh mengecat
1. `Reproject to vertex` dalam mod `From itself`, kini tekstur telah ditukar kepada nilai vertex
1. Cat, smooth, smudge, stamp, lakukan apa sahaja suntingan yang anda perlukan
1. `Bake to texture`, dalam mod `From itself`. Suntingan tersebut ditukar kembali ke tekstur.
:::

#### From high-res ()
Tukar sebarang objek yang kelihatan kepada nilai vertex pada objek terpilih. Nombor pada butang ini menunjukkan bilangan objek yang kelihatan.

::: tip
Reproject objek lain boleh digunakan bukan sahaja untuk memindahkan maklumat warna daripada objek lain, tetapi untuk memproyeksikan vertex ke atas objek lain, contohnya balutan (bandages) boleh diproyeksikan ke atas watak.
:::

#### ![](/icons/cog.webp) Menu gear Reproject
Menu gear mempunyai pilihan lanjutan berikut:

#### Vertices, Roughness, Metalness, Color, Opacity, Opacity->Mask, Mask, Layers, Face Group
Kotak semak ini menentukan sifat mana yang akan diproyeksikan ke objek terpilih. 

#### Relax
Mesh terpilih boleh mempunyai susun aturnya dilicinkan atau direlaks tertentu untuk lebih sesuai dengan sasaran reprojection. Smooth lebih baik untuk mesh poligon tinggi. Relax lebih baik untuk mesh poligon rendah. Auto akan membenarkan Nomad menentukan kaedah terbaik.

#### Iterations
Berapa kali operasi relax patut digunakan semasa reprojection.

#### Cage radius
Laraskan sejauh mana dari objek terpilih sinar dihantar untuk mencari objek sasaran. Secara lalai jarak ini dikekalkan rendah untuk mengelakkan artifak, tetapi boleh ditingkatkan jika objek sasaran jauh dari objek bake.

#### Ray bias
Nilai lebih rendah akan mengutamakan projek ke titik terdekat pada permukaan sasaran. Nilai lebih tinggi akan mengutamakan titik persilangan menggunakan normal permukaan. 

#### Ray offset
Laraskan di mana pengiraan bake bermula pada objek terpilih. Secara lalai ia bermula 5% jauh dari permukaan, yang mengelakkan artifak tertentu. Jika objek sasaran sangat jauh dari objek bake, offset ini mungkin perlu ditingkatkan.


### Quad Remesh - Instant
![](/images/topology_quadremesh_menu.webp)
Remesh menggunakan [algoritma Instant Meshes oleh Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung](https://igl.ethz.ch/projects/instant-meshes/). Ia akan menganalisis aliran mesh dan mencipta topologi quad yang bersih.

::: tip
Pada iOS dan desktop, alat [Quad remesher](tools#quad-remesher) memberikan hasil yang lebih baik dan lebih kawalan.
:::

#### Remesh
Mulakan operasi instant meshes.

#### Target quads
Bilangan poligon quad yang akan cuba dicipta oleh quad remesh.

#### ![](/icons/cog.webp) Menu gear Quad Remesh Instant
Menu gear mempunyai pilihan lanjutan berikut:

##### Crease angle
Ambang sudut tajam yang akan cuba membantu membimbing operasi remesh.

#### Max fill hole
Algoritma kadangkala boleh menghasilkan lubang yang tidak diingini. Jika lubang mempunyai bilangan vertex kurang daripada nilai ini, maka ia akan diisi.

### Holes
![](/images/topology_holes_menu.webp)
Kebanyakan masa, objek anda mungkin watertight, bermakna mesh adalah 'tertutup'.

Jika objek anda mempunyai lubang, anda boleh mengisinya. Perlu diingat ia hanya berfungsi pada lubang 'naif', oleh itu ia tidak boleh 'mengimpal' dua sempadan berasingan.

![](/videos/hole_filling.mp4)

::: tip
Apabila anda menjalankan Voxel remesher, semua lubang ditutup secara automatik, sama ada anda menggunakannya pada 1 atau berbilang mesh.
:::

#### Close holes
Laksanakan tindakan menutup lubang.

#### ![](/icons/cog.webp) Menu gear Holes
Menu gear mempunyai pilihan lanjutan berikut:

##### Detail
Ketumpatan poligon yang digunakan untuk mengisi lubang. Semasa menyeret peluncur ini corak papan dam akan ditunjukkan pada model, ini akan memberikan petunjuk saiz segi tiga yang akan digunakan. Kotak semak akan menyahaktifkan ini, dan hanya menggunakan titik sedia ada, yang biasanya akan menghasilkan segi tiga panjang dan nipis di atas lubang, yang boleh sukar untuk diukir.

##### Fill non-manifold
Cuba isi lubang non-manifold.

##### Face Group

Apabila mengisi lubang, patutkah setiap lubang mendapat facegroup sendiri (Auto), atau semuanya berkongsi satu facegroup (Off), atau jangan cipta facegroup (On).

### Force Manifold
![](/images/topology_forcemanifold_menu.webp)
Cuba membersihkan tepi non-manifold. Ia boleh berguna untuk perisian luaran yang tidak menyokong tepi yang mempunyai lebih daripada 2 permukaan bersama.

#### Clean
Laksanakan tindakan clean.
#### ![](/icons/cog.webp) Menu gear Force manifold
Menu gear mempunyai pilihan lanjutan berikut:

#### Delete small faces
Ambang yang digunakan untuk membuang dan menyambung poligon kecil.


### Triplanar
![](/images/topology_triplanar_menu.webp)
Menukar mesh kepada primitif [triplanar](scene.md#triplanar).
Anda mungkin akan kehilangan banyak butiran dalam proses ini.

#### Force cubic
Aktifkan triplanar supaya menjadi kubus. Jika tidak, triplanar akan muat ke kotak pembatas (bounding box) paling hampir di sekeliling objek anda.

#### Convert
Laksanakan tindakan triplanar.

#### Resolution
Saiz voxel yang digunakan dalam operasi triplanar.

## ![](/icons/dot.webp) Primitive
Parameter untuk primitif terpilih. Ini juga tersedia dalam bar alat viewport primitif.

![](/images/topology_primitive_screenshot.webp)
