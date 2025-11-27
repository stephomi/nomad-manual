# ![](/icons/sun.webp) Peneduhan

Menu ini mengawal mod peneduhan yang digunakan oleh Nomad, sifat pencahayaan, dan sifat cahaya persekitaran/matcap.

![](/images/shading_overview.webp)



Anda boleh memilih antara beberapa mod pemaparan:

| Mod                         | Maksud                    | Penerangan                                                    |
| :-------------------------: | :------------------------: | :-----------------------------------------------------------: |
| [Lit(PBR)](#pbr)            | Pemaparan Berasaskan Fizik | Mewarna dengan metalness/roughness                            |
| [Matcap](#matcap)           | Material Capture           | Digunakan semasa mengukir dengan penggunaan gpu/cpu lebih rendah berbanding PBR |
| [Unlit](#unlit)             | Warna Permukaan            | Hanya warna permukaan tanpa peneduhan atau pencahayaan        |
| [Object Id](#object-id)      | ID Objek                   | Warna rawak bagi setiap objek, berguna untuk aplikasi melukis |
| [Instance Id](#instance-id)  | ID Instans                 | Warna rawak bagi setiap instans, berguna untuk mengenal pasti mesh kongsi |

Jika anda ingin belajar lebih lanjut tentang metalness dan roughness, lihat bahagian [Vertex Paint](painting.md).

---

![](/images/shading_second.webp)

### Face Group
Tindihan warna facegroup. Facegroup ialah pemilihan poligon berwarna yang boleh dicipta dengan alat [Face group](tools#facegroup), dan dihasilkan secara automatik dengan kebanyakan primitif.

Sesetengah alat akan menapis secara automatik mengikut facegroup apabila facegroup kelihatan.

### Show paint
Nomad boleh menyimpan warna, roughness, metalness dalam verteks arca anda. Anda boleh togol paparan sifat ini secara global dengan kotak semak ini.

Perhatikan bahawa jika anda mempunyai kedua-dua sifat verteks dan tekstur, dan kedua-duanya didayakan, nilainya akan didarab antara satu sama lain.

### Show mask
Togol tindihan mask skala kelabu bagi [alat mask](tools#mask). Apabila ini dinyahdayakan, mask juga dinyahdayakan, berguna untuk membuat perubahan pantas tanpa mask, kemudian anda boleh mengaktifkannya semula tanpa kehilangan mask anda.

### Use Hide

Togol muka tersembunyi. Perhatikan ini hanya berfungsi jika anda TIDAK berada dalam alat hide!

### Use textures

Nomad membenarkan tekstur diberikan kepada objek daripada menu [material](material). Jika tekstur diberikan ia boleh ditogol secara global dengan kotak semak ini.







### Gambaran keseluruhan PBR dan lampu
Manual ini tidak akan menyelami butiran tentang Pemaparan Berasaskan Fizik.

Satu perkara penting untuk diingat ialah pencahayaan dan material dipisahkan sepenuhnya.
Ini bermakna anda boleh mewarna warna objek anda, roughness dan metalness sementara pencahayaan dikendalikan secara berasingan.
Ia membolehkan anda mewarna objek anda dan kemudian melaras pencahayaan kemudian, tanpa merosakkan rupa keseluruhan model anda.

Lampu hanya tersedia dengan [mod PBR](#pbr).
Atas sebab prestasi, anda dihadkan kepada hanya 4 lampu.

::: tip
Anda boleh memuatkan fail glTF dengan lebih daripada 4 lampu di dalamnya dan Nomad akan mengekalkan kesemuanya.
Walau bagaimanapun ia mungkin tidak berprestasi dengan baik.
:::

::: tip
Anda boleh memalsukan banyak lampu dengan menjadikan objek unlit/emissive, kemudian aktifkan global illumination dalam menu [post process](postprocess).
:::

### Gambaran keseluruhan jenis lampu

Berikut ialah jenis lampu yang kini disokong:

| Mod                         | Penerangan                                             | Boleh membuang bayang-bayang                             |
| :-------------------------: | :-----------------------------------------------------: | :------------------------------------------------------: |
| [Directional](#directional) | Cahaya matahari yang sangat jauh                       | ya                                                       |
| [Environment](#environment) | Cahaya jauh yang dipadankan dengan persekitaran HDR    | ya                                                       |
| [Spot](#spot)               | Cahaya berbentuk kon                                   | Ya                                                       |
| [Point](#point)             | Titik cahaya omni-arah                                 | Ya, tetapi hanya melalui bayang skrin-ruang yang kurang mantap |

#### Directional
Ia memancarkan cahaya dari jarak yang sangat jauh, dengan keamatan seragam.
Kedudukan 3Dnya dalam adegan tidak penting, hanya orientasinya sahaja.

Anda boleh melampirkan lampu ini pada kamera, dengan itu ia mempunyai pencahayaan yang konsisten.  
Sebagai contoh anda boleh menggunakannya untuk membuat rim light (cahaya kuat yang memancar dari belakang model anda, menghala ke kamera) yang sentiasa menerangi bahagian belakang model anda.

#### Environment light
Menggunakan [environment hdr](#environment) berfungsi dengan baik untuk pencahayaan lembut keseluruhan, tetapi jika terdapat cahaya tajam yang kuat kelihatan dalam HDR, bayang yang dicipta olehnya akan sangat lembut, selalunya tidak kelihatan langsung. Menggunakan lampu directional bersama HDR persekitaran boleh membantu, tetapi boleh menjadi sukar untuk menyelaraskannya.

Lampu ini melakukan kerja itu untuk anda. Lampu akan diputar secara automatik untuk sejajar dengan bahagian paling terang HDR, kemudian anda boleh mengawal keamatan dan sudutnya (kelembutan bayang) secara berasingan. 

#### Spot
Lampu spot memancarkan cahaya dalam satu arah, dihadkan oleh bentuk kon.

#### Point
Lampu point akan memancarkan cahaya ke semua arah.  
Pada masa ini, lampu point tidak menyokong bayang-bayang.

#### Shadows
Pilihan `normal bias` boleh digunakan untuk mengurangkan artifak bayang biasa (acne/peter-panning).

Kualiti bayang-bayang bergantung pada saiz objek relatif kepada keseluruhan adegan.  
Jika anda mempunyai objek besar dalam adegan anda yang tidak perlu membuang bayang (contohnya satah besar), pastikan untuk menyahdayakan bayang dalam [tetapan material](material.md#cast-shadows)nya.

## Lights

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Kotak semak Lights

Togol semua lampu langsung dalam adegan.



### Add light

Tambah lampu ke adegan, maksimum 4. Apabila lampu ditambah, senarai lampu dipaparkan dengan butang, dan bar alat lampu ditambah ke bahagian atas viewport.

![](/images/shading_lights_icons.webp)

* Teks menunjukkan nama lampu dan kecerahan.
* Ikon mata menogol keterlihatan.
* Ikon pensel membolehkan anda menamakan semula lampu.
* Ikon tong sampah akan memadam lampu.
* Ikon salin akan menggandakan lampu. 
* Ikon 3 titik akan memaparkan penyunting lampu penuh. Kebanyakan fungsi ini juga tersedia daripada bar alat yang muncul dalam viewport. 

### ![](/icons/spotlight.webp)  Icons

Togol paparan ikon lampu dalam viewport

### Light toolbar
![](/images/shading_lights_toolbar.webp) 

Bar alat ini akan muncul di bahagian atas viewport apabila lampu dipilih.

* Show akan menogol keterlihatan lampu.
* Directional/Environment/Spot/Point akan menukar jenis lampu. Ketik untuk kitar, atau tekan lama untuk melihat menu.
* Intensity mengawal kekuatan lampu, nilai boleh melebihi 1.0 untuk lampu yang sangat kuat, berguna apabila digunakan dengan Global Illumination dalam Post Process
* Swatch warna apabila diklik akan memaparkan pemilih warna. Nomad menawarkan beberapa cara untuk memilih warna. Kawalan Kelvin menawarkan cara semula jadi untuk memilih pencahayaan panas/sejuk.
* Shadow akan menogol bayang-bayang.
* Size menetapkan lebar lampu. Lampu yang lebih lebar akan membuang bayang lembut, pencahayaan lembut, dan highlight yang lebih lembut pada objek.
* ... akan memaparkan kawalan tambahan.

### Kawalan tambahan lampu

![](/images/shading_extra_controls.webp) 

Perhatikan bahawa sesetengah pilihan khusus untuk jenis lampu tertentu.

* `Clone` akan menggandakan lampu.
* `Recenter` akan mengalihkan lampu kembali ke origin.
* `Delete` akan memadam lampu.
* `Directional/Environment/Spot/Point` membolehkan anda menukar jenis lampu.
* `Colour swatch` apabila diklik akan memaparkan pemilih warna. 
* `Intensity` mengawal kekuatan lampu.
* `Attachment` (_directional sahaja_) akan menetapkan lampu sama ada diparentkan kepada dunia, atau diparentkan kepada kamera. Contohnya jika anda menggunakan lampu directional di belakang watak anda sebagai rim light, apabila attachment sebagai kamera dipilih, memutar kamera akan sentiasa meletakkan lampu di belakang watak.
* `Angle` (_directional dan environment sahaja_) ialah saiz tampak lampu, anggap ia sebagai betapa besarnya matahari kelihatan di langit. Sudut yang lebih besar akan membuang bayang lebih lembut dan highlight lebih lebar.
* `Softness` (_spotlight sahaja_) mengawal ketajaman tepi kon spotlight. 0 ialah tepi yang sangat tajam. 1 sangat lembut, dengan gradien ke pusat kon cahaya. Dalam viewport, titik biru kecil pada kon spotlight boleh digunakan untuk menetapkan softness secara interaktif.
* `Cone angle` (_spotlight sahaja_) mengawal sudut sebaran spotlight. Sudut kecil ialah pancaran cahaya yang sangat nipis, 170 ialah sebaran cahaya yang sangat luas. Dalam viewport, titik oren boleh digunakan untuk menetapkan cone angle secara interaktif.
* `Shadow` akan menogol bayang untuk lampu semasa.
* `Shadow map` dan `screenspace` ialah cara berbeza untuk mengira bayang, secara umum shadow map lebih boleh dipercayai.
* `Contact` melaras cara bayang dikira. Bayang ialah masalah sukar dalam grafik komputer, dan boleh menyebabkan artifak dalam pemaparan. Bayang yang lebih tepat boleh dipilih untuk lampu paling penting dalam adegan, kawalan ini menentukan sama ada lampu paling penting dipilih secara automatik oleh Nomad, atau jika pengguna memilihnya.
* `Tolerance` jika artifak bayang kelihatan (sama ada bayang nampaknya tidak menyentuh permukaan, atau terdapat hingar dan corak dalam bayang), melaras tolerance boleh membantu membetulkan isu tersebut.


## Environment

![](/images/shading_environment.webp)

Cahaya di dunia sebenar datang dari semua arah; biru langit, hijau rumput, merah bangunan, semua cahaya daripada 'persekitaran' ini boleh disimulasikan dengan peta persekitaran. 

Nomad disertakan dengan beberapa contoh peta persekitaran untuk kawasan dalam dan luar bangunan, dengan tona dan tahap kecerahan berbeza. Cuba peta berbeza untuk melihat yang mana menyerlahkan paling banyak perincian pada arca anda.

Ketik pada imej untuk melihat peta persekitaran yang tersedia. Daripada dialog itu pilih 'Import...' untuk memuatkan peta anda sendiri. Adalah terbaik menggunakan imej High Dynamic Range (HDR), dalam format latlong atau equirectangular, sebagai fail .hdr atau .exr. [www.polyhaven.com](https://polyhaven.com/hdris) mempunyai koleksi peta persekitaran percuma yang baik untuk digunakan, secara umum peta hdr 1k ialah saiz dan kualiti yang baik.

### Exposure
Laras kecerahan peta persekitaran. Selalunya peta boleh terlalu terang apabila digunakan dengan lampu biasa, menurunkan exposure boleh membantu mengimbangi, terutamanya apabila digunakan dengan Global Illumination dalam tetapan [Post Process](postprocess).

### Rotation

Oleh kerana peta persekitaran menangkap cahaya dari semua arah, anda boleh memutarnya untuk mendapatkan pantulan dan pencahayaan keseluruhan yang serasi dengan arca anda.

### Attached to camera
Lampirkan persekitaran kepada kamera.

Ia akan memaksa pencahayaan menjadi konsisten, yang boleh berguna semasa mengukir.


## ![](/icons/sphere_smooth.webp) Matcap

![](/images/shading_matcap.webp)

Seperti namanya (MATerial CAPture), matcap mengurus kedua-dua maklumat pencahayaan dan material dalam satu imej.
Memandangkan material itu sendiri sudah hadir dalam matcap, saluran pewarnaan roughness dan metalness akan diabaikan.
Warna pewarnaan akan didarab dengan matcap, bermakna jika anda mempunyai matcap hitam/kelabu, menggunakan cat putih tidak akan menjadikannya lebih cerah.

Artis cenderung menggemari mod ini untuk tujuan mengukir kerana ia membolehkan mereka menumpukan pada bentuk dan geometri itu sendiri.

Mengetik pada sfera akan memaparkan pelayar imej. Anda juga boleh menambah matcap anda sendiri, secara umum sebarang foto, render, malah lukisan sfera yang telah dipotong ketat menjadi segi empat sama boleh digunakan. Banyak pustaka matcap tersedia dalam talian, sumber berguna ialah [pustaka matcap nidorx](https://github.com/nidorx/matcaps).

### Use global Matcap

Biasanya artis akan menggunakan satu matcap untuk keseluruhan arca, tetapi jika togol ini dinyahdayakan, setiap objek boleh mempunyai matcap sendiri. Ini boleh digunakan secara artistik untuk mendapatkan hasil yang menarik.

::: tip
Nyahtogol pilihan ini, dan gunakan imej bola mata untuk mata watak anda!
:::

### Rotation
Matcap ialah bentuk khusus peta persekitaran, jadi seperti peta persekitaran, ia boleh diputar. Anda juga boleh melakukannya pada bila-bila masa dalam viewport dengan menyeret menggunakan 3 jari ke kiri dan kanan.



## ![](/icons/circle_fill.webp) Unlit

Mod ini hanya akan menunjukkan warna permukaan. Ia boleh berguna untuk menyemak warna permukaan objek anda adalah seperti yang anda jangkakan, tanpa diganggu oleh lampu, bayang, pantulan, ketelusan. 

Mod ini juga boleh digunakan untuk render bukan fotorealistik, menghasilkan rupa rata dan kartun.

## ![](/icons/cube.webp) Object ID

Semua maklumat pencahayaan dan permukaan diabaikan, dan setiap objek diwarnakan dengan warna rata yang unik. Jika ini dirender bersama render PBR, ia boleh digunakan dalam program melukis untuk memilih mengikut warna, dan dengan itu dapat melakukan pembetulan warna pada objek tertentu.

Perhatikan bahawa warna ini juga akan muncul dalam [paparan pokok menu Scene](scene#tree-view).

### Randomise id

Jana set warna rawak yang baharu. 

## ![](/icons/link.webp) Instance ID

Sama seperti Object ID, tetapi instans akan mempunyai warna yang sama. 

### Randomise id

Jana set warna rawak yang baharu.
