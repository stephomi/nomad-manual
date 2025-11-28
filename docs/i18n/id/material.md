# ![](/icons/material.webp) Material {#material}

Menu ini memungkinkan Anda mengubah material objek saat ini, properti render objek/material, dan menetapkan tekstur ke material.

![](/images/material_overview.webp)

Material menentukan bagaimana sebuah objek terlihat, dengan mengontrol bagaimana ia bereaksi terhadap cahaya dan terhadap objek lain. Tampilan sebuah objek dikendalikan oleh properti berikut:

* `Material type`
* `Color`
* `Roughness`
* `Metalness`
* `Opacity`
* `Reflectance`
* `Emissive/unlit`

Kombinasi dari properti ini dapat menghasilkan berbagai macam tampilan, mulai dari fotorealistis, kartun, hingga eksperimental.

Color, roughness, metalness dan opacity dapat dilukis, lihat [Vertex Paint options](painting.md) untuk informasi lebih lanjut.

Material type, reflectance, emssive/unlit adalah properti material yang dijelaskan di bawah.

Tombol copy/paste di bagian atas menu ini memungkinkan Anda menyalin material dari satu objek ke objek lain.

Perhatikan bahwa renderer Nomad adalah renderer realtime; meskipun kuat, ia lebih mengutamakan kecepatan daripada akurasi untuk efek tertentu. 

## Jenis material {#material-types}

![](/images/material_types.webp)

Tipe material Nomad adalah Opaque, Subsurface, Blending, Additive, Refraction, Dithering, Shadow Catcher.

### ![](/icons/material_opaque.webp) Buram {#opaque}
Mode bawaan yang memperlakukan permukaan sebagai material sederhana yang mendukung color, roughness, metalness, opacity yang dapat dilukis.

### ![](/icons/material_subsurface.webp) Subpermukaan {#subsurface}
Mode ini dapat mensimulasikan material yang memungkinkan cahaya mengaburkan dan menyebarkan cahaya secara internal seperti kulit, lilin, giok.

Untuk hasil terbaik, beralihlah ke mode shading PBR dan gunakan setidaknya satu directional atau spot light, idealnya dengan environment yang redup.

`Depth` mengontrol seberapa jauh cahaya menyebar dari bagian depan, ke bawah permukaan, lalu keluar lagi dari permukaan depan. Ini memiliki efek melembutkan bayangan keras, dan mengaburkan detail permukaan.

`Translucency` mengontrol bagaimana cahaya menyebar dari depan ke belakang sebuah bentuk, seperti penyebaran cahaya melalui bagian bawah daun, atau ketika telinga disinari kuat dari belakang. 

### ![](/icons/material_blending.webp) Pencampuran {#blending}

Mirip dengan Opaque, tetapi mendukung slider opacity untuk memungkinkan material bercampur antara padat dan transparan. Ini adalah slider tunggal yang sederhana untuk opacity, dibandingkan opacity yang dapat dilukis yang didukung oleh material opaque. 

::: warning
Mode Blending dapat menyebabkan flickering dan popping pada bentuk yang kompleks atau saling berpotongan.
:::

### ![](/icons/material_additive.webp) Aditif {#additive}
Anda dapat membuat mesh Anda semi-transparan dengan material ini. Mirip dengan material blending, tetapi sementara blending akan bercampur dengan sekelilingnya, additive akan selalu lebih terang daripada objek di belakangnya, cocok untuk efek terang seperti sinar cahaya, api, ledakan.

Anda dapat mengatur nilai opacity lebih tinggi dari 1, yang berarti objek akan lebih terang.  
Ini bisa berguna jika Anda ingin menggunakan [bloom](postprocess.md#bloom) dan `threshold parameter` untuk hanya membuat objek ini bersinar seperti objek emissive.

Mode ini cenderung memiliki lebih sedikit artefak dibandingkan [Blending](#blending) (order independent transparency).

### ![](/icons/material_refraction.webp) Refraksi {#refraction}
Mode ini dapat digunakan untuk mensimulasikan material kaca. Karena keterbatasan waktu nyata, self-refraction dan refraction berlapis banyak agak terbatas.

Roughness yang dilukis pada model memengaruhi seberapa buram refraksi tersebut.
Secara bawaan, setiap objek yang dibuat di Nomad memiliki roughness sekitar 25%, sehingga refraksi tidak akan sempurna tetapi agak buram.
Anda dapat menggunakan tombol `paint glossy` untuk melukis ulang model Anda dengan roughness dan metalness 0 (warna tidak akan terpengaruh).

Ada 2 roughness berbeda yang berperan, satu mengendalikan seberapa buram pantulan di permukaan, dan yang lain mengendalikan bagian dalam (refraction).  
Namun, karena hanya ada satu channel roughness lukisan di Nomad, roughness interior dan eksterior akan berbagi nilai yang sama.  
Untuk mendapatkan nilai yang berbeda (misalnya permen lollipop dengan permukaan tajam tetapi interior buram) Anda dapat menggunakan slider `Surface glossiness` dan `Interior roughness` untuk menimpa roughness yang dilukis.

![](/videos/refraction.mp4)


### ![](/icons/material_dithering.webp) Dithering {#dithering}
Membuat objek semi-transparan dengan membuang beberapa piksel secara acak.

### ![](/icons/material_shadow_catcher.webp) Penangkap bayangan {#shadow-catcher}

Membuat objek tidak terlihat, dan hanya menerima bayangan. Berguna untuk menggabungkan render Nomad dengan gambar lain. 

::: tip

Informasi lebih lanjut tentang transparency dan blending modes dapat ditemukan di https://support.fab.com/s/article/Transparency-Opacity

:::

## Kontrol {#controls}

![](/images/material_controls.webp)

### Selalu tanpa pencahayaan {#always-unlit}
Jika diaktifkan, objek akan mengabaikan PBR dan Matcap dan hanya menampilkan lukisan warnanya tanpa shading.
Perhatikan bahwa jika Anda menggunakan [Additive](#additive), Anda dapat melukis transparansi secara langsung dengan menggunakan warna hitam.

### Opasitas {#opacity}
Seberapa padat atau buram sebuah objek akan terlihat; 100% padat, 0% transparan. Anda juga dapat melukis opacity untuk kontrol yang lebih halus.

### Reflektansi {#reflectance}
Mengontrol jumlah pantulan yang akan diterima material untuk material non-logam. Sebagian besar waktu nilai bawaan sebaiknya digunakan (yang sesuai dengan 4% cahaya yang dipantulkan pada sudut normal), tetapi dapat dinaikkan untuk meningkatkan pantulan dan highlight pada mata karakter, misalnya.

### Pembalikan culling {#inverse-culling}
Membalik normal permukaan. Biasanya tidak diperlukan, tetapi dapat digunakan jika model tampak terbalik, atau dikombinasikan dengan `Two sided` yang dimatikan, dapat digunakan untuk membuat interior di mana dinding yang paling dekat dengan kamera selalu tersembunyi.

### Penghalusan bayangan {#smooth-shading}
Lihat [global option](settings.md#smooth-shading).  
Nilai `Auto` akan menggunakan global option.

### Dua sisi {#two-sided}
Lihat [global option](settings.md#two-sided).  
Nilai `Auto` akan menggunakan global option.

### Bagian belakang berwarna {#coloured-backface}
Lihat [global option](settings#two-sided).
Nilai `Auto` akan menggunakan global option.

### Menjatuhkan bayangan {#casts-shadows}
Untuk saat ini `Auto` sama dengan `On`.
Objek transparan juga menghasilkan bayangan (dengan pola dithering untuk meniru bayangan blended).  
Pastikan untuk menonaktifkan shadow casting jika Anda memiliki objek besar di scene yang tidak perlu menghasilkan bayangan (misalnya lantai besar).

### Menerima bayangan {#recieve-shadows}
Untuk saat ini `Auto` sama dengan `On`.

### Wireframe {#wireframe}
Lihat [global option](settings.md#wireframe).  
Nilai `Auto` akan menggunakan global option.


## Tekstur {#textures}

![](/images/material_textures.webp)

Jika sebuah objek memiliki UV, maka tekstur dapat diterapkan ke material selain vertex color/roughness/metalness/opacity. Biasanya ini adalah hasil dari texture bake, tetapi gambar yang dibuat di luar Nomad juga dapat digunakan.

Tekstur dapat diterapkan ke

* Color
* Normal
* Roughness
* Metalness
* Opacity
* Emissive

Mengklik sebuah slot tekstur akan menampilkan pemilih. Setelah tekstur ditetapkan ke slot material, mengklik lagi akan menampilkan panel tekstur:

### Opsi panel tekstur {#texture-panel-options}

![](/images/material_texture_panel.webp)

### Buka {#open}
Memilih tekstur lain

### Tidak ada {#none}
Menghapus tekstur

### Opasitas {#texture-opacity}

Jika gambar memiliki alpha channel, ini akan memungkinkan Anda menggunakannya untuk Opacity, atau mengabaikannya.

### ![](/icons/link.webp) Ikon rantai/tautan {#chainlink-icon}

Ikon link di bagian berikut, ketika diaktifkan, berarti opsi apa pun yang digunakan akan dibagikan dengan tekstur lain (color, normal, roughness, metalness, opacity, emissive) yang juga memiliki ikon link mereka diaktifkan. 

Ini memungkinkan Anda memastikan jika Anda memiliki tekstur yang selaras, tekstur tersebut akan tetap selaras bahkan ketika Anda mengubah parameter atau tipe proyeksi.


### Proyeksi {#projection}
![](/images/material_projection.webp)

Mengatur bagaimana tekstur harus diterapkan ke objek.

* `Auto` - Jika objek memiliki uv, UV, jika tidak Triplanar
* `UV` - Menggunakan koordinat uv mesh untuk menerapkan tekstur. Jika mesh dan tekstur berasal dari luar Nomad, atau akan diekspor dari Nomad untuk digunakan di tempat lain, UV adalah opsi yang benar.
* `Triplanar` - Memproyeksikan tekstur sepanjang sumbu X,Y,Z, dan mengaburkan sambungannya. 

### Triplanar {#triplanar}
![](/images/material_triplanar.webp)

Proyeksi Triplanar adalah cara yang kuat namun sederhana untuk menerapkan tekstur ke objek.

Triplanar seperti memiliki 6 proyektor video dengan gambar yang sama, menyinari bagian depan, belakang, kiri, kanan, atas dan bawah objek Anda.

Ini kemudian dapat di-bake ke UV atau vertex color jika diperlukan.


![](/images/material_triplanar_example.webp)

#### Metode {#method}

* `Local` - Proyeksi akan bergerak mengikuti transform objek
* `World` - Proyeksi tetap diam, menggerakkan objek akan menggesernya melalui proyeksi.

#### Kekerasan {#hardness}

Bagaimana proyeksi bercampur. 100% tidak akan melakukan blending, dan tepi proyeksi akan tajam. 0% akan mengaburkan tepi pada sudut yang lebar. Nilai bawaan adalah 90%, cukup pencampuran untuk menyembunyikan tepi, dan membiarkan bagian lain dari proyeksi tetap tajam.

### Seragam {#uniform}

Jika dicentang, hardness yang sama digunakan untuk semua proyeksi. Jika tidak dicentang, kontrol hardness tambahan akan ditampilkan untuk proyeksi X, Y, Z.


### Parameter {#parameter}
![](/images/material_parameter.webp)

#### Penyaringan {#filtering}
Metode filter tekstur yang digunakan, `Auto` adalah bawaan, metodenya adalah `Nearest`, `Linear`, `Mipmap`. Nearest tidak melakukan filtering, sehingga tekstur dapat mendapatkan artefak bergerigi ketika dilihat dari dekat. Linear dan Mipmap melakukan filtering yang lebih baik, sehingga tekstur tampak buram daripada bergerigi dari dekat.

#### Ulangan-X {#tiling-x}
Jika parameter Scale lebih besar dari 1, membuat tekstur lebih kecil daripada UV objek, bagaimana tekstur akan diulang sepanjang sumbu X. `None` berarti tanpa pengulangan. `Repeat` akan membuat salinan tekstur. `Mirror` akan membuat salinan tekstur, dengan setiap salinan kedua dibalik, yang dapat membantu menyembunyikan artefak tiling.

#### Ulangan-Y {#tiling-y}
Sama seperti Tiling-X, tetapi untuk sumbu Y.

### Transformasi {#transform}
![](/images/material_transform.webp)

Transformasi 2D tambahan yang diterapkan ke tekstur dalam ruang UV. Tombol reset mengembalikan ke bawaan, ikon rantai (ketika tekstur selain color dipilih) akan menghubungkan atau memutus transform agar sama dengan tekstur color.

#### Translasi {#translation}
Offset X dan Y dari tekstur

#### Rotasi {#rotation}
Rotasi tekstur

#### Skala {#scale}
Skala tekstur, angka yang lebih besar akan membuat tekstur lebih kecil pada objek, gunakan slider Tiling-X dan Tiling-Y untuk mengontrol apa yang terjadi.

### Skala seragam {#uniform-scale}
Ketika dimatikan Nomad akan menampilkan kontrol terpisah untuk Scale-X dan Scale-Y.