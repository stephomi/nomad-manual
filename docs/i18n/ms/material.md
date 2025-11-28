# ![](/icons/material.webp) Bahan {#material}

Menu ini membolehkan anda menukar bahan objek semasa, sifat render objek/bahan, dan menetapkan tekstur pada bahan.

![](/images/material_overview.webp)

Bahan menentukan rupa sesuatu objek, dengan mengawal cara ia bertindak balas terhadap cahaya dan objek lain. Rupa objek dikawal oleh sifat berikut:

* `Jenis bahan`
* `Warna`
* `Kekasaran`
* `Kelogaman`
* `Kelegapan`
* `Pantulan`
* `Emisif/tanpa pencahayaan (unlit)`

Gabungan sifat-sifat ini boleh menghasilkan pelbagai rupa daripada fotorealistik kepada kartun hinggalah eksperimental.

Warna, kekasaran, kelogaman dan kelegapan boleh dilukis, lihat [Pilihan Vertex Paint](painting.md) untuk maklumat lanjut.

Jenis bahan, pantulan, emisif/tanpa pencahayaan ialah sifat bahan yang diterangkan di bawah.

Butang salin/tampal di bahagian atas menu ini membolehkan anda menyalin bahan daripada satu objek ke objek lain.

Perlu diingat bahawa enjin render Nomad adalah enjin render masa nyata; walaupun berkuasa, ia mengutamakan kelajuan berbanding ketepatan untuk kesan tertentu. 

## Jenis bahan {#material-types}

![](/images/material_types.webp)

Jenis bahan Nomad ialah Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Legap {#opaque}
Mod lalai yang menganggap permukaan sebagai bahan ringkas yang menyokong warna, kekasaran, kelogaman dan kelegapan yang dilukis.

### ![](/icons/material_subsurface.webp) Bawah permukaan {#subsurface}
Mod ini boleh mensimulasikan bahan yang membenarkan cahaya kabur dan berselerak secara dalaman seperti kulit, lilin, jed.

Untuk hasil terbaik, tukar kepada mod penaungan PBR dan gunakan sekurang-kurangnya satu cahaya berarah atau spot, sebaiknya dengan persekitaran yang malap.

`Depth` mengawal sejauh mana cahaya berselerak dari bahagian hadapan, menembusi ke bawah permukaan, kemudian keluar semula melalui permukaan hadapan. Ini melembutkan bayang-bayang keras dan mengaburkan perincian permukaan.

`Translucency` mengawal bagaimana cahaya berselerak dari bahagian hadapan ke bahagian belakang bentuk, seperti cahaya yang menembusi bahagian bawah daun, atau apabila telinga disinari kuat dari belakang. 

### ![](/icons/material_blending.webp) Pengadunan {#blending}

Serupa dengan Opaque, tetapi menyokong peluncur kelegapan untuk membolehkan bahan bercampur antara pepejal dan lutsinar. Ini ialah peluncur tunggal ringkas untuk kelegapan, berbanding kelegapan boleh lukis yang disokong oleh bahan opaque. 

::: warning
Mod Blending boleh menyebabkan berkelip dan “popping” pada bentuk yang kompleks atau bersilang.
:::

### ![](/icons/material_additive.webp) Aditif {#additive}
Anda boleh menjadikan mesh separa lutsinar dengan bahan ini. Ia serupa dengan bahan blending, tetapi sementara blending akan bercampur dengan persekitarannya, additive akan sentiasa lebih cerah daripada objek di belakangnya, sesuai untuk kesan terang seperti sinar cahaya, api, letupan.

Anda boleh menetapkan nilai kelegapan lebih tinggi daripada 1, yang bermaksud objek akan menjadi lebih cerah.  
Ini berguna jika anda mahu menggunakan [bloom](postprocess.md#bloom) dan `parameter threshold` untuk hanya menjadikan objek ini bersinar seperti objek emisif.

Mod ini cenderung mempunyai artifak yang lebih sedikit berbanding [Blending](#blending) (ketelusan bebas tertib).

### ![](/icons/material_refraction.webp) Pembiasan {#refraction}
Mod ini boleh digunakan untuk mensimulasikan bahan kaca. Disebabkan kekangan masa nyata, pembiasan kendiri dan pembiasan berlapis berbilang adalah agak terhad.

Lukisan kekasaran pada model mempengaruhi sejauh mana kaburnya pembiasan.
Secara lalai, setiap objek yang dicipta dalam Nomad mempunyai kekasaran sekitar 25%, jadi pembiasan tidak akan sempurna tetapi sedikit kabur.
Anda boleh menggunakan butang `paint glossy` untuk melukis semula model anda dengan kekasaran dan kelogaman 0 (warna tidak akan terjejas).

Terdapat 2 kekasaran berbeza yang terlibat, satu memacu sejauh mana kaburnya pantulan pada permukaan, dan satu lagi memacu bahagian dalam (pembiasan).  
Walau bagaimanapun, kerana hanya ada satu saluran kekasaran lukisan dalam Nomad, kekasaran dalaman dan luaran akan berkongsi nilai yang sama.  
Untuk mendapatkan nilai berbeza (contohnya gula-gula lolipop dengan permukaan tajam tetapi bahagian dalam kabur) anda gunakan peluncur `Surface glossiness` dan `Interior roughness` untuk menindih nilai kekasaran yang dilukis.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Menjadikan objek separa lutsinar dengan membuang beberapa piksel secara rawak.

### ![](/icons/material_shadow_catcher.webp) Penangkap bayang {#shadow-catcher}

Menjadikan objek tidak kelihatan, dan hanya menerima bayang-bayang. Berguna untuk menggabungkan render Nomad dengan imej lain. 

::: tip

Maklumat lanjut tentang ketelusan dan mod blending boleh didapati di https://support.fab.com/s/article/Transparency-Opacity

:::

## Kawalan {#controls}

![](/images/material_controls.webp)

### Sentiasa tidak berlampu {#always-unlit}
Jika diaktifkan, objek akan mengabaikan PBR dan Matcap dan hanya memaparkan warna lukisan tanpa penaungan.
Perlu diingat jika anda menggunakan [Additive](#additive), anda boleh melukis ketelusan secara terus dengan menggunakan warna hitam.

### Kelegapan {#opacity}
Seberapa pepejal atau legap sesuatu objek akan kelihatan; 100% ialah pepejal, 0% ialah lutsinar. Anda juga boleh melukis kelegapan untuk kawalan lebih halus.

### Pantulan {#reflectance}
Mengawal jumlah pantulan yang diterima bahan untuk bahan bukan logam. Kebanyakan masa nilai lalai patut digunakan (yang sepadan dengan 4% cahaya dipantulkan pada sudut normal), tetapi boleh dinaikkan untuk menguatkan pantulan dan sorotan pada mata watak, sebagai contoh.

### Pemotongan songsang {#inverse-culling}
Membalikkan normal permukaan. Biasanya tidak diperlukan, tetapi boleh digunakan jika model kelihatan terbalik, atau bersama dengan `Two sided` dimatikan, boleh digunakan untuk membuat bahagian dalam di mana dinding paling hampir dengan kamera sentiasa disembunyikan.

### Lorekan licin {#smooth-shading}
Lihat [pilihan global](settings.md#smooth-shading).  
Nilai `Auto` akan menggunakan pilihan global.

### Dua sisi {#two-sided}
Lihat [pilihan global](settings.md#two-sided).  
Nilai `Auto` akan menggunakan pilihan global.

### Bahagian belakang berwarna {#coloured-backface}
Lihat [pilihan global](settings#two-sided).
Nilai `Auto` akan menggunakan pilihan global.

### Membaling bayang {#casts-shadows}
Buat masa ini `Auto` sama seperti `On`.
Objek lutsinar juga membuang bayang-bayang (dalam corak dithering untuk meniru bayang-bayang blended).  
Pastikan untuk mematikan bayang-bayang jika anda mempunyai objek besar dalam adegan yang tidak perlu membuang bayang-bayang (contohnya lantai besar).

### Menerima bayang {#recieve-shadows}
Buat masa ini `Auto` sama seperti `On`.

### Rangka dawai {#wireframe}
Lihat [pilihan global](settings.md#wireframe).  
Nilai `Auto` akan menggunakan pilihan global.


## Tekstur {#textures}

![](/images/material_textures.webp)

Jika objek mempunyai UV, tekstur boleh digunakan pada bahan sebagai tambahan kepada warna/kekasaran/kelogaman/kelegapan verteks. Biasanya ini ialah hasil daripada “texture bake”, tetapi imej yang dicipta di luar Nomad juga boleh digunakan.

Tekstur boleh digunakan pada

* Warna
* Normal
* Kekasaran
* Kelogaman
* Kelegapan
* Emisif

Mengklik pada slot tekstur akan memaparkan pemilih. Selepas tekstur ditetapkan pada slot bahan, mengklik sekali lagi akan memaparkan panel tekstur:

### Pilihan panel tekstur {#texture-panel-options}

![](/images/material_texture_panel.webp)

### Buka {#open}
Pilih tekstur lain

### Tiada {#none}
Buang tekstur

### Kelegapan {#texture-opacity}

Jika imej mempunyai saluran alfa, ini membolehkan anda menggunakannya untuk Kelegapan, atau mengabaikannya.

### ![](/icons/link.webp) Ikon rantai/pautan {#chainlink-icon}

Ikon pautan dalam bahagian berikut, apabila diaktifkan, bermaksud apa sahaja pilihan yang digunakan akan dikongsi dengan tekstur lain (warna, normal, kekasaran, kelogaman, kelegapan, emisif) yang juga mempunyai ikon pautan diaktifkan. 

Ini membolehkan anda memastikan jika anda mempunyai tekstur yang sejajar, ia akan kekal sejajar walaupun anda mengubah parameter atau jenis unjuran.


### Unjuran {#projection}
![](/images/material_projection.webp)

Tetapkan bagaimana tekstur harus digunakan pada objek.

* `Auto` - Jika objek mempunyai uv, UV, jika tidak Triplanar
* `UV` - Gunakan koordinat uv mesh untuk menggunakan tekstur. Jika mesh dan tekstur datang dari luar Nomad, atau akan dieksport dari Nomad untuk digunakan di tempat lain, UV ialah pilihan yang betul.
* `Triplanar` - Unjurkan tekstur sepanjang paksi X,Y,Z, dan gabungkan sambungan.

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Unjuran triplanar ialah cara yang berkuasa tetapi ringkas untuk menggunakan tekstur pada objek.

Triplanar adalah seperti mempunyai 6 projektor video dengan imej yang sama, memancar ke hadapan, belakang, kiri, kanan, atas dan bawah objek anda.

Ini kemudian boleh dibakar ke dalam UV atau warna verteks jika perlu.


![](/images/material_triplanar_example.webp)

#### Kaedah {#method}

* `Local` - Unjuran akan bergerak bersama transform objek
* `World` - Unjuran kekal tetap, menggerakkan objek akan meluncurkannya melalui unjuran.

#### Kekerasan {#hardness}

Bagaimana unjuran bercampur. 100% tidak akan melakukan sebarang pengadunan, dan tepi unjuran akan tajam. 0% akan mengadun tepi dalam sudut yang luas. Lalai ialah 90%, cukup pengadunan untuk menyembunyikan tepi, dan membiarkan selebih unjuran kekal tajam.

### Seragam {#uniform}

Apabila ditanda, kekerasan yang sama digunakan untuk semua unjuran. Apabila dinyah tanda, kawalan kekerasan tambahan didedahkan untuk unjuran X, Y, Z.


### Parameter {#parameter}
![](/images/material_parameter.webp)

#### Penapisan {#filtering}
Kaedah penapisan tekstur untuk digunakan, `Auto` ialah lalai, kaedah ialah `Nearest`, `Linear`, `Mipmap`. Nearest tidak melakukan penapisan, jadi tekstur boleh mendapat artifak bergerigi apabila dilihat dari dekat. Linear dan Mipmap melakukan penapisan yang lebih baik, jadi tekstur kelihatan kabur dan bukannya bergerigi apabila dekat.

#### Ulangan-X {#tiling-x}
Jika parameter Scale lebih besar daripada 1, menjadikan tekstur lebih kecil daripada UV objek, bagaimana tekstur akan diulang sepanjang paksi X. `None` bermaksud tiada ulangan. `Repeat` akan membuat salinan tekstur. `Mirror` akan membuat salinan tekstur, dengan setiap salinan kedua diterbalikkan, yang boleh membantu menyembunyikan artifak pengulangan.

#### Ulangan-Y {#tiling-y}
Sama seperti Tiling-X, tetapi untuk paksi Y.

### Transformasi {#transform}
![](/images/material_transform.webp)

Transformasi 2D tambahan digunakan pada tekstur dalam ruang UV. Butang reset menetapkan semula kepada lalai, ikon rantai (apabila tekstur selain warna dipilih) akan memaut atau menyahpaut transform supaya sama seperti tekstur warna.

#### Terjemahan {#translation}
Ofset X dan Y tekstur

#### Putaran {#rotation}
Putaran tekstur

#### Skala {#scale}
Skala tekstur, nombor lebih besar akan menjadikan tekstur lebih kecil pada objek, gunakan peluncur Tiling-X dan Tiling-Y untuk mengawal apa yang berlaku.

### Skala seragam {#uniform-scale}
Apabila dimatikan Nomad akan memaparkan kawalan berasingan untuk Scale-X dan Scale-Y.