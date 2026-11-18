# ![](/icons/sun.webp) Shading {#shading}

Menu ini mengawal mod shading yang digunakan oleh Nomad, sifat pencahayaan, persekitaran dan matcap, serta kabut.

![](/images/shading_overview.webp)



Anda boleh memilih antara beberapa mod render:

| Mod                         | Maksud                     | Penerangan                                                      |
| :-------------------------: | :------------------------: | :-------------------------------------------------------------: |
| [Cerah (PBR)](#pbr)         | Physically Based Rendering | Lampu, bayang, persekitaran, serta kelogaman/kekasaran yang diwarnakan |
| [MatCap](#matcap)           | Material Capture           | Mod pantas untuk mengukir, menggunakan gpu/cpu lebih sedikit daripada PBR |
| [Tanpa cahaya](#unlit)      | Warna Permukaan            | Warna permukaan sahaja tanpa shading atau pencahayaan           |
| [ID Objek](#object-id)      | ID Objek                   | Warna rawak bagi setiap objek, berguna untuk aplikasi lukisan.  |
| [ID instans](#instance-id)  | ID Instans                 | Warna rawak bagi setiap instans, berguna untuk mengenal pasti mesh yang dikongsi |

Jika anda ingin mengetahui lebih lanjut tentang kelogaman dan kekasaran, lihat bahagian [Cat Verteks](painting.md).

---

![](/images/shading_second.webp)

### ![](/icons/group_gray.webp) Kumpulan muka {#face-group}
Menindih warna kumpulan muka. Kumpulan muka ialah pemilihan poligon berwarna yang boleh dicipta dengan alat [Kumpulan muka](tools#facegroup), dan dibuat secara automatik bagi kebanyakan primitif.

Sesetengah alat akan menapis mengikut kumpulan muka secara automatik apabila kumpulan muka kelihatan.

### ![](/icons/palette.webp) Tunjukkan cat {#show-paint}
Nomad boleh menyimpan warna, kekasaran dan kelogaman dalam verteks ukiran anda. Anda boleh menogol paparan sifat-sifat ini secara global dengan kotak semak ini.

Ambil perhatian bahawa jika anda mempunyai kedua-dua sifat verteks dan tekstur, dan kedua-duanya didayakan, nilainya akan didarabkan bersama.

### ![](/icons/shield.webp) Tunjukkan topeng {#show-mask}
Menogol tindihan topeng skala kelabu bagi [alat topeng](tools#mask). Apabila ini dinyahdayakan, topeng juga dinyahdayakan. Ini berguna untuk membuat perubahan pantas tanpa topeng, kemudian anda boleh mendayakannya semula tanpa kehilangan topeng anda.

### ![](/icons/tool_hide.webp) Gunakan Sembunyi {#use-hide}

Menogol muka yang tersembunyi. Ambil perhatian bahawa ini hanya berfungsi jika anda TIDAK berada dalam alat sembunyi!

### ![](/icons/image.webp) Gunakan tekstur {#use-textures}

Nomad membenarkan tekstur ditetapkan pada objek melalui menu [Bahan](material). Jika tekstur telah ditetapkan, ia boleh ditogol secara global dengan kotak semak ini.

Anda tidak boleh mencipta atau menyunting tekstur di dalam Nomad, tetapi tekstur daripada fail yang diimport boleh digunakan. Tekstur kelegapan berfungsi dalam Cerah, MatCap dan Tanpa cahaya, peta normal dalam Cerah dan MatCap, warna dalam Cerah dan Tanpa cahaya, manakala pancaran, kekasaran dan kelogaman hanya dalam Cerah. Butang ini menjadi kelabu apabila adegan tidak mempunyai tekstur.

### Gambaran keseluruhan PBR dan lampu {#pbr}
Manual ini tidak akan menghuraikan secara mendalam tentang Physically Based Rendering.

Satu perkara penting yang perlu diingat ialah pencahayaan dan bahan dipisahkan sepenuhnya.
Ini bermakna anda boleh mewarnakan warna, kekasaran dan kelogaman objek anda, manakala pencahayaan dikendalikan secara berasingan.
Ini membolehkan anda mewarnakan objek anda dahulu, kemudian melaraskan pencahayaan kemudian, tanpa merosakkan rupa keseluruhan model anda.

Lampu, persekitaran dan kabut hanya tersedia dalam [mod PBR](#pbr).
Atas sebab prestasi, anda dihadkan kepada 4 lampu pada peranti mudah alih dan 6 pada desktop.

::: tip
Anda boleh memuatkan fail glTF yang mengandungi lebih banyak lampu dan Nomad akan mengekalkan kesemuanya.
Walau bagaimanapun, prestasinya mungkin tidak begitu baik.
:::

::: tip
Anda boleh memalsukan banyak lampu dengan menjadikan objek tanpa cahaya/memancar, kemudian mendayakan pencahayaan global dalam menu [Pemprosesan Pasca](postprocess).
:::

### Gambaran keseluruhan jenis lampu {#light-types-overview}

Berikut ialah jenis lampu yang disokong pada masa ini:

| Mod                         | Penerangan                                              | Boleh menghasilkan bayang |
| :-------------------------: | :-----------------------------------------------------: | :--------------: |
| [Bercahaya arah](#directional) | Cahaya matahari yang terletak jauh tidak terhingga   | Ya               |
| [Persekitaran](#env-light)  | Lampu jauh yang dipadankan dengan HDR persekitaran      | Ya               |
| [Spot](#spot)               | Lampu berbentuk kon                                     | Ya               |
| [Titik](#point)             | Titik cahaya ke semua arah                              | Ya               |

#### ![](/icons/sun.webp) Bercahaya arah {#directional}
Lampu ini memancarkan cahaya dari jarak yang jauh tidak terhingga, dengan intensiti yang seragam.
Kedudukan 3dnya dalam adegan tidak penting, hanya orientasinya yang penting.

Anda boleh melekatkan lampu ini pada kamera, supaya pencahayaannya sentiasa konsisten.
Contohnya, anda boleh menggunakannya untuk membuat lampu tepi (rim light, iaitu cahaya kuat yang dipancarkan dari belakang model anda, menghala ke arah kamera) yang sentiasa menerangi bahagian belakang model anda.

#### ![](/icons/panorama.webp) Lampu persekitaran {#env-light}
Menggunakan [HDR persekitaran](#environment) sesuai untuk pencahayaan lembut secara keseluruhan, tetapi jika terdapat cahaya kuat yang tajam dalam HDR itu, bayang yang dihasilkannya akan menjadi sangat lembut, malah selalunya tidak kelihatan langsung. Menggunakan lampu berarah bersama HDR persekitaran boleh membantu, tetapi agak sukar untuk menyelaraskan kedua-duanya.

Lampu ini melakukan kerja itu untuk anda. Lampu akan diputar secara automatik untuk sejajar dengan bahagian paling terang dalam HDR, kemudian anda boleh mengawal intensiti dan sudutnya (kelembutan bayang) secara berasingan.

#### ![](/icons/spotlight.webp) Spot {#spot}
Lampu spot memancarkan cahaya ke satu arah, dihadkan oleh bentuk kon.

#### ![](/icons/light.webp) Titik {#point}
Lampu titik memancarkan cahaya ke semua arah, dan ia juga boleh menghasilkan bayang.

#### Bayang {#shadows}
Setiap lampu boleh menghasilkan bayang, dan anda boleh memilih cara bayang dikira dalam [tetapannya](#light-extra-controls). Jika anda melihat artifak bayang, gelangsar `Toleransi` di sana boleh membantu.

Kualiti bayang bergantung pada saiz objek berbanding keseluruhan adegan.
Jika anda mempunyai objek besar dalam adegan yang tidak perlu menghasilkan bayang (contohnya satah yang besar), pastikan anda menyahdayakan penghasilan bayang dalam [tetapan bahannya](material.md#casts-shadows).

## ![](/icons/sun.webp) Cahaya {#lights}

![](/images/shading_lights.webp)

### ![](/icons/checked.webp) Kotak semak Cahaya {#lights-checkbox}

Menogol semua lampu langsung dalam adegan.



### Tambah lampu {#add-light}

Menambah lampu ke dalam adegan, sehingga 4 lampu pada peranti mudah alih dan 6 pada desktop. Apabila lampu ditambah, senarai lampu dipaparkan bersama butang-butang, dan bar alat lampu ditambah di bahagian atas port pandangan.

![](/images/shading_lights_icons.webp)

* Teks menunjukkan nama lampu dan kecerahannya. Ketik untuk memilih lampu itu.
* Ikon mata menogol keterlihatan.
* Ikon pensel membolehkan anda menamakan semula lampu.
* Ikon tong sampah akan memadam lampu.
* Ikon salin akan menduplikasi lampu.
* Ikon 3 titik akan membuka penyunting lampu penuh. Kebanyakan fungsi ini juga tersedia daripada bar alat yang muncul dalam port pandangan.

Anda juga boleh menyeret lampu dalam senarai untuk menyusunnya semula.

### ![](/icons/spotlight.webp)  Ikon-ikon {#icons}

Menogol paparan ikon lampu dalam port pandangan

### Bar alat lampu {#light-toolbar}
![](/images/shading_lights_toolbar.webp) 

Bar alat ini akan muncul di bahagian atas port pandangan apabila lampu dipilih.

* `Kelihatan` akan menogol keterlihatan lampu.
* Bercahaya arah/Persekitaran/Spot/Titik akan menukar jenis lampu. Ketik untuk bertukar secara berkitar, atau tekan lama untuk melihat menu.
* Intensiti mengawal kekuatan lampu. Nilainya boleh melebihi 1.0 untuk lampu yang sangat kuat, berguna apabila digunakan bersama Pencahayaan Global dalam Pemprosesan Pasca.
* Apabila diklik, petak warna akan membuka pemilih warna. Nomad menawarkan beberapa cara untuk memilih warna. Kawalan Kelvin menawarkan cara semula jadi untuk memilih pencahayaan hangat/sejuk.
* Bayang akan menogol bayang.
* Sudut (_bercahaya arah dan persekitaran_) atau Saiz (_spot dan titik_) menetapkan lebar sesuatu lampu. Lampu yang lebih lebar akan menghasilkan bayang yang lembut, pencahayaan yang lembut, dan sorotan yang lebih lembut pada objek.
* Lampiran (_bercahaya arah sahaja_), Sudut kerucut dan Kelembutan (_spot sahaja_) diterangkan dalam [penyunting lampu](#light-extra-controls) di bawah.
* ... akan membuka `Klona`, `Pusatkan semula` dan `Padam`, bersama tetapan bayang.

### Kawalan tambahan lampu {#light-extra-controls}

![](/images/shading_extra_controls.webp) 

Ikon 3 titik bagi sesuatu lampu dalam senarai membuka penyunting penuhnya. Ambil perhatian bahawa sesetengah pilihan khusus untuk jenis lampu tertentu.

* `Bercahaya arah/Persekitaran/Spot/Titik` membolehkan anda menukar jenis lampu.
* Apabila diklik, `petak warna` akan membuka pemilih warna.
* `Intensiti` mengawal kekuatan lampu.
* `Lampiran` (_bercahaya arah sahaja_) akan menetapkan lampu supaya berinduk pada dunia (`Tetap`), atau berinduk pada kamera (`Kamera`). Contohnya, jika anda menggunakan lampu berarah di belakang watak anda sebagai lampu tepi, apabila lampiran pada kamera dipilih, memutar kamera akan sentiasa mengekalkan lampu di belakang watak.
* `Kelembutan` (_spot sahaja_) mengawal ketajaman tepi kon lampu spot. 0 ialah tepi yang sangat tajam. 1 sangat lembut, dengan kecerunan ke arah tengah kon cahaya. Dalam port pandangan, titik biru kecil pada kon lampu spot boleh digunakan untuk menetapkan kelembutan secara interaktif.
* `Sudut kerucut` (_spot sahaja_) mengawal sudut sebaran lampu spot. Sudut yang kecil ialah alur cahaya yang sangat nipis, manakala 170 ialah sebaran cahaya yang sangat luas. Dalam port pandangan, titik jingga boleh digunakan untuk menetapkan sudut kerucut secara interaktif.
* `Sudut` (_bercahaya arah dan persekitaran sahaja_) ialah saiz ketara lampu; bayangkan ia sebagai sebesar mana matahari kelihatan di langit. Sudut yang lebih besar akan menghasilkan bayang yang lebih lembut dan sorotan yang lebih luas.
* `Saiz` (_spot dan titik sahaja_) ialah lebar lampu. Lampu yang lebih besar menghasilkan bayang yang lebih lembut.
* `Bayang` akan menogol bayang untuk lampu semasa.
* Jenis bayang menentukan cara bayang dikira. `Peta bayang` merender adegan dari kedudukan lampu, jadi ia turut membayangi geometri yang tidak dapat dilihat oleh kamera. `Kawasan skrin` hanya menggunakan apa yang sudah kelihatan pada skrin: ia lebih ringan, tetapi masih dalam percubaan. Secara amnya, peta bayang lebih boleh dipercayai.
* `Toleransi` (_kawasan skrin sahaja_): jika artifak bayang kelihatan (sama ada bayang tidak kelihatan menyentuh permukaan, atau terdapat hingar dan corak dalam bayang), melaraskan toleransi boleh membantu membetulkan masalah tersebut.
* `Kontak` menambah bayang yang lebih tepat pada jarak dekat, di tempat objek bersentuhan. Dengan `Auto`, hanya lampu paling dominan dalam adegan yang mendapat bayang kontak; `Tidak` dan `Ya` memaksanya mati atau hidup untuk lampu ini. Gelangsar `Toleransi`nya berfungsi seperti yang di atas.

Butang `...` pada bar alat port pandangan menyimpan tetapan bayang yang sama, serta:

* `Klona` akan menduplikasi lampu.
* `Pusatkan semula` akan mengalihkan lampu ke hadapan kamera, sambil mengekalkan orientasinya.
* `Padam` akan memadam lampu.


## ![](/icons/panorama.webp) Persekitaran {#environment}

![](/images/shading_environment.webp)

Cahaya di dunia sebenar datang dari semua arah; biru langit, hijau rumput, merah sebuah bangunan, semua cahaya daripada 'persekitaran' ini boleh disimulasikan dengan peta persekitaran.

Gunakan kotak semak di sebelah tajuk untuk menghidupkan atau mematikan pencahayaan persekitaran.

Nomad disertakan dengan beberapa contoh peta persekitaran untuk kawasan dalaman dan luaran, dengan warna dan tahap kecerahan yang berbeza. Cuba peta yang berbeza untuk melihat yang mana paling menonjolkan butiran dalam ukiran anda.

Ketik pada imej untuk melihat peta persekitaran yang tersedia. Daripada dialog itu, pilih `Import...` untuk memuatkan peta anda sendiri. Sebaik-baiknya gunakan imej High Dynamic Range (HDR), dalam format latlong atau equirectangular, sama ada sebagai fail .hdr atau .exr. Pelayar ini juga boleh memuat turun persekitaran terus daripada [Poly Haven](https://polyhaven.com/hdris), yang mempunyai koleksi peta persekitaran percuma yang bagus.

### Dedahan {#env-exposure}
Melaraskan kecerahan peta persekitaran. Selalunya peta boleh menjadi terlalu terang apabila digunakan bersama lampu biasa; menurunkan dedahan boleh membantu mengimbanginya, terutamanya apabila digunakan bersama Pencahayaan Global dalam tetapan [Pemprosesan Pasca](postprocess).

### Putaran {#env-rotation}

Oleh sebab peta persekitaran menangkap cahaya dari semua arah, anda boleh memutarnya supaya pantulan dan pencahayaan keseluruhan sepadan dengan ukiran anda. Anda juga boleh memutar persekitaran dengan menyeret 3 jari secara mendatar pada port pandangan.

### Melekat pada kamera {#env-attached}
Melekatkan persekitaran pada kamera.

Ini akan memaksa pencahayaan sentiasa konsisten, yang boleh berguna semasa mengukir.

### Kaburkan (latar belakang) {#env-background-blur}
Gelangsar ini hanya muncul apabila [latar belakang](background.md) ditetapkan kepada persekitaran. Ia mengaburkan imej persekitaran di belakang model anda, tanpa mengubah pencahayaan.


## ![](/icons/fog.webp) Kabut {#fog}

Kabut menambah kedalaman atmosfera pada adegan anda dan menjadikan alur cahaya kelihatan. Dayakannya dengan kotak semak di sebelah tajuk. Seperti lampu dan persekitaran, ia hanya tersedia dalam mod [Cerah (PBR)](#pbr).

::: tip Alur cahaya yang lebih kuat
Turunkan `Persekitaran` kabut, dan gunakan lampu spot atau titik yang terang. Naikkan `Kepadatan` sehingga kabut kelihatan dengan jelas. Untuk alur cahaya yang kelihatan dalam kabut yang lebih nipis, tetapkan `Arah Serakan` kepada nilai positif yang tinggi dan halakan kamera ke arah lampu.
:::

### Warna {#fog-color}
Warna kabut dan warna cahaya yang diserakkannya.

### Kepadatan {#fog-density}
Seberapa cepat kabut menebal mengikut jarak.

### Kelegapan Maksimum {#fog-opacity}
Mengehadkan sejauh mana kabut boleh menutupi adegan, walaupun pada kepadatan yang tinggi.

### Arah Serakan {#fog-scattering}
Arah kabut menyerakkan cahaya (juga dikenali sebagai anisotropi). Nilai positif mencerahkan kabut apabila anda memandang ke arah lampu, nilai negatif apabila anda memandang ke arah bertentangan, dan sifar menyerakkan cahaya secara sekata ke semua arah.

### ![](/icons/panorama.webp) Persekitaran {#fog-environment}
Sejauh mana [persekitaran](#environment) menerangi kabut. Ia menjadi kelabu apabila persekitaran dimatikan.

### Hingar {#fog-noise}
Mencampurkan hingar ke dalam kabut untuk memecahkannya kepada tompok-tompok, tanpa mengubah kepadatan keseluruhannya. Apabila hingar melebihi 0, gelangsar `Saiz` menetapkan saiz corak.

### Bentuk {#fog-shape}
Di mana kabut memenuhi adegan:

* `Seragam` - memenuhi keseluruhan adegan.
* `Menegak` - mengekalkan kabut di dalam jalur menegak dengan tepi yang lembut. Gelangsar `Bawah` dan `Atas` menetapkan ketinggian tepi bawah dan atasnya, dan butang mata pada setiap satunya menunjukkan jalur itu dalam port pandangan semasa anda melaraskannya.


## ![](/icons/sphere_smooth.webp) MatCap {#matcap}

![](/images/shading_matcap.webp)

Seperti namanya (MATerial CAPture), matcap menguruskan kedua-dua maklumat pencahayaan dan bahan dalam satu imej.
Oleh sebab bahan itu sendiri sudah ada dalam matcap, saluran pewarnaan kekasaran dan kelogaman akan diabaikan.
Warna cat akan didarabkan dengan matcap, bermakna jika anda mempunyai matcap hitam/kelabu, menggunakan cat putih tidak akan menjadikannya lebih terang.

Artis lebih gemar menggunakan mod ini untuk mengukir kerana ia membolehkan mereka memberi tumpuan kepada bentuk dan geometri itu sendiri.

Mengetik pada sfera akan membuka pelayar imej. Anda juga boleh menambah matcap anda sendiri; secara amnya, apa-apa foto, render, malah lukisan sfera yang dipotong rapat menjadi segi empat sama boleh digunakan. Banyak pustaka matcap tersedia dalam talian; salah satu sumber yang berguna ialah [pustaka matcap nidorx](https://github.com/nidorx/matcaps).

### Gunakan MatCap global {#matcap-global}

Biasanya artis menggunakan satu matcap untuk keseluruhan ukiran, tetapi jika togol ini dinyahdayakan, objek yang dipilih boleh mempunyai matcapnya sendiri. Ini boleh digunakan secara artistik untuk mendapatkan hasil yang menarik.

::: tip
Nyahdayakan pilihan ini, dan gunakan imej bebola mata untuk mata watak anda!
:::

### Putaran {#matcap-rotation}
Matcap ialah sejenis peta persekitaran yang khusus, jadi seperti peta persekitaran, ia boleh diputar. Anda juga boleh melakukannya pada bila-bila masa dalam port pandangan dengan menyeret 3 jari ke kiri dan ke kanan.

Butang kunci di sebelah gelangsar mengunci putaran, supaya seretan 3 jari tidak memutar matcap secara tidak sengaja.



## ![](/icons/circle_fill.webp) Tanpa cahaya {#unlit}

Mod ini hanya menunjukkan warna permukaan. Ia berguna untuk memastikan warna permukaan objek anda adalah seperti yang dijangka, tanpa terganggu oleh lampu, bayang, pantulan atau kelutsinaran.

Mod ini juga boleh digunakan untuk render bukan fotorealistik, bagi mendapatkan rupa kartun yang rata.

## ![](/icons/cube.webp) ID Objek {#object-id}

Semua maklumat pencahayaan dan permukaan diabaikan, dan setiap objek diwarnakan dengan warna rata yang unik. Jika ini dirender bersama render PBR, ia boleh digunakan dalam program lukisan untuk memilih mengikut warna, dan seterusnya membolehkan pembetulan warna dibuat pada objek tertentu.

Ambil perhatian bahawa warna-warna ini juga akan muncul dalam [paparan pepohon menu Adegan](scene#tree-view).

### Acak id {#object-random}

Menjana set warna rawak yang baharu.

## ![](/icons/link.webp) ID instans {#instance-id}

Sama seperti ID Objek, tetapi instans akan mempunyai warna yang sama.

### Acak id {#instance-random}

Menjana set warna rawak yang baharu.
